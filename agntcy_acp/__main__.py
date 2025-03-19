# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import click

from agntcy_acp.manifest.validator import  validate_agent_manifest_file, validate_agent_descriptor_file
from agntcy_acp.manifest import generator
import yaml


@click.group()
def cli():
    pass


@cli.command(short_help="Validate agent ACP descriptor")
@click.argument("agent_descriptor_path", required=True)
def validate_acp_descriptor(agent_descriptor_path):
    """
    Validate the Agent Descriptor contained in the file AGENT_DESCRIPTOR_PATH against the ACP specification
    """
    descriptor = validate_agent_descriptor_file(agent_descriptor_path)
    if descriptor: print("Agent ACP Descriptor is valid")


@cli.command(short_help="Validate agent manifest")
@click.argument("agent_manifest_path", required=True)
def validate_acp_manifest(agent_manifest_path):
    """
    Validate the Agent Manifest contained in the file AGENT_MANIFEST_PATH against the Manifest specification
    """
    manifest = validate_agent_manifest_file(agent_manifest_path)
    if manifest: print("Agent Manifest is valid")


@cli.command(short_help="Generate pydantic models from agent manifest or descriptor.")
@click.argument("agent_descriptor_path", required=True)
@click.option("--output-dir", type=str, required=True,
              help="Pydantic models for specific agent based on provided agent descriptor or agent manifest")
@click.option("--model-file-name", type=str, required=False, default="models.py",
              help="Filename containing the pydantic model of the agent schemas")
def generate_agent_models(agent_descriptor_path, output_dir, model_file_name):
    """
    Generate pydantic models from agent manifest or descriptor.
    """
    descriptor = validate_agent_descriptor_file(agent_descriptor_path, raise_exception=True)
    generator.generate_agent_models(descriptor, output_dir, model_file_name)

@cli.command(short_help="Generate OpenAPI Spec from agent manifest or descriptor")
@click.argument("agent_descriptor_path", required=True)
@click.option("--output", type=str, required=False, help="OpenAPI output file")
def generate_agent_oapi(agent_descriptor_path, output):
    """
    Generate OpenAPI Spec from agent manifest or descriptor
    """
    descriptor = validate_agent_descriptor_file(agent_descriptor_path)
    oas = generator.generate_agent_oapi(descriptor)
    if output:
        with open(output, 'w') as file:
            yaml.dump(oas, file, default_flow_style=False)
    else:
        print(yaml.dump(oas, default_flow_style=False))


if __name__ == "__main__":
    cli()
