# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import asyncio
import json
import logging
import os
import sys
from typing import Any, Dict, List

import click
import yaml
from agntcy_acp import (
    ACPClient,
    ApiClientConfiguration,
    AsyncACPClient,
)
from dotenv import find_dotenv, load_dotenv
from jinja2.sandbox import SandboxedEnvironment

from .client import async_process_operation, process_operation
from .types import TestFile, TestOperation

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

load_dotenv(dotenv_path=find_dotenv(usecwd=True))
logger = logging.getLogger(__name__)


async def arun_test(
    jinja_env: SandboxedEnvironment,
    render_env: Dict[str, Any],
    config: ApiClientConfiguration,
    operations: List[TestOperation],
) -> List[int]:
    render_env["results"] = []
    fails = []
    async with AsyncACPClient(configuration=config) as acp_client:
        for op_idx, op in enumerate(operations):
            # Substitute results in templates to allow forwarding run_id, etc.
            op_json = op.model_dump_json(exclude_defaults=True)
            new_op_json = jinja_env.from_string(op_json).render(render_env)
            op = TestOperation.model_validate_json(new_op_json)

            async for success, result in async_process_operation(
                acp_client, op, op_idx
            ):
                if not success:
                    fails.append(op_idx)
                render_env["results"].append(result)
    return fails


def run_test(
    jinja_env: SandboxedEnvironment,
    render_env: Dict[str, Any],
    config: ApiClientConfiguration,
    operations: List[TestOperation],
) -> List[int]:
    render_env["results"] = []
    fails = []
    with ACPClient(configuration=config) as acp_client:
        for op_idx, op in enumerate(operations):
            # Substitute results in templates to allow forwarding run_id, etc.
            op_json = op.model_dump_json(exclude_defaults=True)
            new_op_json = jinja_env.from_string(op_json).render(render_env)
            op = TestOperation.model_validate_json(new_op_json)

            for success, result in process_operation(acp_client, op, op_idx):
                if not success:
                    fails.append(op_idx)
                render_env["results"].append(result)
    return fails


@click.command(short_help="Execute API client test descriptor file.")
@click.option(
    "--async/--no-async",
    "is_async",
    default=False,
    help="Use the async API client.",
)
@click.option(
    "--env",
    multiple=True,
    help='Override environment variable with format: "name=value" Can be specified multiple times.',
)
@click.option(
    "--log-level",
    type=click.Choice(
        ["critical", "error", "warning", "info", "debug"], case_sensitive=False
    ),
    default="info",
    help="Set logging level.",
)
@click.argument(
    "filename",
    type=click.Path(exists=True),
    metavar="TEST_INPUT_FILENAME",
)
def execute_test_file(
    filename: click.Path, is_async: bool, log_level: str, env: List[str]
):
    """ """
    logging.basicConfig(level=log_level.upper())
    logging.getLogger("urllib3").setLevel(log_level.upper())
    logging.getLogger("aiohttp").setLevel(log_level.upper())

    # CLI overrides environment after loading dotenv
    for env_string in env:
        parsed = env_string.split("=")
        if len(parsed) != 2:
            raise ValueError(f"Error parsing environment string: {env_string}")
        os.environ[parsed[0]] = parsed[1]

    # Read test config
    if filename == "-":
        file_data = sys.stdin.read()
    else:
        with open(str(filename), "r") as fh:
            file_data = fh.read()

    # Substitute templates
    jinja_env = SandboxedEnvironment(
        loader=None,
        enable_async=False,
        autoescape=False,
    )
    # TODO: should we filter the env by the env_prefix if provided?
    render_env = {"env": os.environ}

    # Load YAML
    yaml_data = yaml.load(file_data, Loader=SafeLoader)
    tests = TestFile.model_validate(yaml_data)

    config_args = tests.metadata.client_config.model_dump(exclude_none=True)
    if tests.metadata.env_prefix is not None:
        config = ApiClientConfiguration.fromEnvPrefix(
            tests.metadata.env_prefix, **config_args
        )
    else:
        config = ApiClientConfiguration(**config_args)

    if is_async:
        fails = asyncio.run(arun_test(jinja_env, render_env, config, tests.operations))
    else:
        fails = run_test(jinja_env, render_env, config, tests.operations)

    num_successes = len(tests.operations) - len(fails)
    print(
        f"Finished: Successes: {num_successes}, Failures: {json.dumps(fails) if len(fails) > 0 else 0}"
    )
    sys.exit(0 if len(fails) == 0 else 1)
