# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import click

from acp_sdk.manifest.validator import validate_manifest_file
from acp_sdk.manifest import generator
import yaml


@click.group()
def cli():
    pass


@cli.command()
@click.argument("manifest_path", required=True)
def validate_manifest(manifest_path):
    """
    Validate the manifest provided against the ACP specification
    """
    manifest = validate_manifest_file(manifest_path)
    if manifest: print("Manifest is valid")


@cli.command()
@click.argument("manifest_path", required=True)
@click.option("--output", type=str, required=False, help="OpenAPI output file")
def generate_agent_oapi(manifest_path, output):
    """
    Generate OpenAPI spec for an agent based its manifest
    """
    manifest = validate_manifest_file(manifest_path)
    oas = generator.generate_agent_oapi(manifest)
    if output:
        with open(output, 'w') as file:
            yaml.dump(oas, file, default_flow_style=False)
    else:
        print(yaml.dump(oas, default_flow_style=False))


@cli.command()
@click.argument("manifest_path", required=True)
@click.option("--output-dir", type=str, required=True,
              help="Pydantic models for specific agent based on provided manifest")
def generate_agent_models(manifest_path, output_dir):
    """
    Generate pydantic models for an agent based on its manifest
    """
    manifest = validate_manifest_file(manifest_path)
    generator.generate_agent_models(manifest, output_dir)


@cli.command()
@click.argument("manifest_path", required=True)
@click.option("--output-dir", type=str, required=True,
              help="Pydantic client for specific agent based on provided manifest")
def generate_agent_client(manifest_path, output_dir):
    """
    Generate python client to interact through ACP with an agent based on its manifest
    """
    manifest = validate_manifest_file(manifest_path)
    generator.generate_agent_client(manifest, output_dir)


if __name__ == "__main__":
    cli()
