# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import click

from acp_sdk.descriptor.validator import validate_agent_descriptor_file
from acp_sdk.descriptor import generator
import yaml


@click.group()
def cli():
    pass


@cli.command()
@click.argument("agent_descriptor_path", required=True)
def validate_acp_descriptor(agent_descriptor_path):
    """
    Validate the Agent Descriptor provided against the ACP specification
    """
    descriptor = validate_agent_descriptor_file(agent_descriptor_path)
    if descriptor: print("Agent ACP Descriptor is valid")


@cli.command()
@click.argument("agent_descriptor_path", required=True)
@click.option("--output", type=str, required=False, help="OpenAPI output file")
def generate_agent_oapi(agent_descriptor_path, output):
    """
    Generate OpenAPI spec for an agent based on its ACP descriptor
    """
    descriptor = validate_agent_descriptor_file(agent_descriptor_path)
    oas = generator.generate_agent_oapi(descriptor)
    if output:
        with open(output, 'w') as file:
            yaml.dump(oas, file, default_flow_style=False)
    else:
        print(yaml.dump(oas, default_flow_style=False))


@cli.command()
@click.argument("agent_descriptor_path", required=True)
@click.option("--output-dir", type=str, required=True,
              help="Pydantic models for specific agent based on provided agent descriptor")
@click.option("--model-file-name", type=str, required=False, default="models.py", help="Filename containing the pydantic model of the agent schemas")
def generate_agent_models(agent_descriptor_path, output_dir, model_file_name):
    """
    Generate pydantic models for an agent based on its ACP descriptor
    """
    descriptor = validate_agent_descriptor_file(agent_descriptor_path)
    generator.generate_agent_models(descriptor, output_dir, model_file_name)


@cli.command()
@click.argument("agent_descriptor_path", required=True)
@click.option("--output-dir", type=str, required=True,
              help="Pydantic client for specific agent based on provided agent descriptor")
def generate_agent_client(agent_descriptor_path, output_dir):
    """
    Generate python client to interact through ACP with an agent based on its ACP descriptor
    """
    descriptor = validate_agent_descriptor_file(agent_descriptor_path)
    generator.generate_agent_client(descriptor, output_dir)


if __name__ == "__main__":
    cli()
