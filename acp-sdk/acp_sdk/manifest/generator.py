# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import os

from acp_sdk.models.models import AgentManifest
import yaml
from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename
import datamodel_code_generator
import copy
import json
from pathlib import Path
import subprocess
import shutil
from .exceptions import ManifestValidationException

ACP_SPEC_PATH = os.path.join(os.path.dirname(__file__), "../acp-spec/openapi.yaml")
CLIENT_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "../scripts/create_acp_client.sh")


def _gen_oas_thread_runs(manifest: AgentManifest, spec_dict):
    # Manipulate the spec according to the thread capability flag in the manifest

    if manifest.specs.capabilities.threads:
        if manifest.specs.thread_state:
            spec_dict['components']['schemas']["ThreadStateSchema"] = manifest.specs.thread_state
        else:
            # No thread schema defined, hence no support to retrieve thread state
            del spec_dict['paths']['/threads/{thread_id}/state']
            del spec_dict['paths']['/runs/{run_id}/threadstate']
    else:
        # Threads are not enabled
        if manifest.specs.thread_state:
            raise ManifestValidationException(
                "Cannot define `specs.thread_state` if `specs.capabilities.threads` is `false`")
        else:
            # Remove all threads paths
            spec_dict['tags'] = [tag for tag in spec_dict['tags'] if tag['name'] != 'Threads']
            del spec_dict['paths']['/threads']
            del spec_dict['paths']['/threads/search']
            del spec_dict['paths']['/threads/{thread_id}']
            del spec_dict['paths']['/threads/{thread_id}/history']
            del spec_dict['paths']['/threads/{thread_id}/state']
            del spec_dict['paths']['/runs/{run_id}/threadstate']


def _gen_oas_interrupts(manifest: AgentManifest, spec_dict):
    # Manipulate the spec according to the interrupts capability flag in the manifest

    if manifest.specs.capabilities.interrupts:
        if not manifest.specs.interrupts or len(manifest.specs.interrupts) == 0:
            raise ManifestValidationException("Missing interrupt definitions with `spec.capabilities.interrupts=true`")

        # Add the interrupt payload and resume payload types for the schemas declared in the manifest
        spec_dict['components']['schemas']['InterruptPayloadSchema'] = {
            'oneOf': [],
            'discriminator': {
                'propertyName': 'interrupt_type',
                'mapping': {}
            }
        }
        spec_dict['components']['schemas']['ResumePayloadSchema'] = {
            'oneOf': [],
            'discriminator': {
                'propertyName': 'interrupt_type',
                'mapping': {}
            }
        }
        for interrupt in manifest.specs.interrupts:
            assert interrupt.interrupt_payload['type'] == 'object'

            interrupt_payload_schema_name = f"{interrupt.interrupt_type}InterruptPayload"
            interrupt.interrupt_payload['properties']['interrupt_type'] = {
                'title': 'Interrupt Type',
                'type': 'string',
                'enum': [interrupt.interrupt_type],
                'description': 'interrupt type which this payload is for'
            }
            spec_dict['components']['schemas']['InterruptPayloadSchema']['oneOf'].append(
                {'$ref': f'#/components/schemas/{interrupt_payload_schema_name}'}
            )
            spec_dict['components']['schemas']['InterruptPayloadSchema']['discriminator']['mapping'][
                interrupt.interrupt_type] = f'#/components/schemas/{interrupt_payload_schema_name}'
            spec_dict['components']['schemas'][interrupt_payload_schema_name] = copy.deepcopy(
                interrupt.interrupt_payload)

            resume_payload_schema_name = f"{interrupt.interrupt_type}ResumePayload"
            interrupt.resume_payload['properties']['interrupt_type'] = interrupt.interrupt_payload['properties'][
                'interrupt_type']

            spec_dict['components']['schemas']['ResumePayloadSchema']['oneOf'].append(
                {'$ref': f'#/components/schemas/{resume_payload_schema_name}'}
            )
            spec_dict['components']['schemas']['ResumePayloadSchema']['discriminator']['mapping'][
                interrupt.interrupt_type] = f'#/components/schemas/{resume_payload_schema_name}'
            spec_dict['components']['schemas'][resume_payload_schema_name] = copy.deepcopy(interrupt.resume_payload)

    else:
        # Interrupts are not supported 

        if manifest.specs.interrupts and len(manifest.specs.interrupts) > 0:
            raise ManifestValidationException("Interrupts defined with `spec.capabilities.interrupts=false`")

        # Remove interrupt support from API
        del spec_dict['paths']['/runs/{run_id}']['post']
        interrupt_ref = spec_dict['components']['schemas']['RunOutput']['discriminator']['mapping']['interrupt']
        del spec_dict['components']['schemas']['RunOutput']['discriminator']['mapping']['interrupt']
        spec_dict['components']['schemas']['RunOutput']['oneOf'] = [e for e in
                                                                    spec_dict['components']['schemas']['RunOutput'][
                                                                        'oneOf'] if e['$ref'] != interrupt_ref]


def _gen_oas_streaming(manifest: AgentManifest, spec_dict):
    # Manipulate the spec according to the streaming capability flag in the manifest

    if (
            not manifest.specs.capabilities.streaming or not manifest.specs.capabilities.streaming.custom) and manifest.specs.custom_streaming_update:
        raise ManifestValidationException(
            "custom_streaming_update defined with `spec.capabilities.streaming.custom=false`")

    if not manifest.specs.capabilities.streaming or (
            not manifest.specs.capabilities.streaming.custom and not manifest.specs.capabilities.streaming.custom):
        # No streaming is supported. Removing streaming method.
        del spec_dict['paths']['/runs/{run_id}/stream']
        # Removing streaming option from RunCreate
        del spec_dict['components']['schemas']['RunCreate']['properties']['streaming']
    else:
        # Restricting streaming modes to those supported in RunCreate
        streaming_modes = []

        if manifest.specs.capabilities.streaming.custom and not manifest.specs.capabilities.streaming.values:
            spec_dict['components']['schemas']['RunCreate']['properties']['streaming']['enum'] = ['custom']
            spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['$ref'] = \
            spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['discriminator']['mapping'][
                'custom']
            del spec_dict['components']['schemas']['RunOutputStream']['properties']['oneOf']
            del spec_dict['components']['schemas']['RunOutputStream']['properties']['mapping']

        if not manifest.specs.capabilities.streaming.custom and manifest.specs.capabilities.streaming.values:
            spec_dict['components']['schemas']['RunCreate']['properties']['streaming']['enum'] = ['values']
            spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['$ref'] = \
            spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['discriminator']['mapping'][
                'result']
            del spec_dict['components']['schemas']['RunOutputStream']['properties']['oneOf']
            del spec_dict['components']['schemas']['RunOutputStream']['properties']['mapping']

        if manifest.specs.capabilities.streaming.custom:
            if manifest.specs.custom_streaming_update:
                spec_dict['components']['schemas']["StreamUpdateSchema"] = manifest.specs.custom_streaming_update
            else:
                raise ManifestValidationException(
                    "Missing custom_streaming_update definitions with `spec.capabilities.streaming.custom=true`")


def _gen_oas_callback(manifest: AgentManifest, spec_dict):
    # Manipulate the spec according to the callback capability flag in the manifest
    if not manifest.specs.capabilities.callbacks:
        # No streaming is supported. Removing callback option from RunCreate
        del spec_dict['components']['schemas']['RunCreate']['properties']['webhook']


def generate_agent_oapi(manifest: AgentManifest):
    spec_dict, base_uri = read_from_filename(ACP_SPEC_PATH)

    # If no exception is raised by validate(), the spec is valid.
    validate(spec_dict)

    spec_dict['info']['title'] = f"ACP Spec for {manifest.metadata.ref.name}:{manifest.metadata.ref.version}"

    spec_dict['components']['schemas']["InputSchema"] = manifest.specs.input
    spec_dict['components']['schemas']["OutputSchema"] = manifest.specs.output
    spec_dict['components']['schemas']["ConfigSchema"] = manifest.specs.config

    _gen_oas_thread_runs(manifest, spec_dict)
    _gen_oas_interrupts(manifest, spec_dict)
    _gen_oas_streaming(manifest, spec_dict)
    _gen_oas_callback(manifest, spec_dict)

    validate(spec_dict)
    return spec_dict


def generate_agent_models(manifest: AgentManifest, path: str):
    agent_spec = generate_agent_oapi(manifest)
    agent_sdk_path = os.path.join(path, f'{manifest.metadata.ref.name}')
    agent_models_dir = os.path.join(agent_sdk_path, 'models')
    specpath = os.path.join(agent_sdk_path, f'openapi.yaml')
    modelspath = os.path.join(agent_models_dir, f'models.py')

    os.makedirs(agent_models_dir, exist_ok=True)

    with open(specpath, 'w') as file:
        yaml.dump(agent_spec, file, default_flow_style=False)

    datamodel_code_generator.generate(
        json.dumps(agent_spec),
        input_filename=specpath,
        input_file_type=datamodel_code_generator.InputFileType.OpenAPI,
        output_model_type=datamodel_code_generator.DataModelType.PydanticV2BaseModel,
        output=Path(modelspath)
    )


def generate_agent_client(manifest: AgentManifest, path: str):
    agent_spec = generate_agent_oapi(manifest)
    agent_sdk_path = os.path.join(path, f'{manifest.metadata.ref.name}')
    os.makedirs(agent_sdk_path, exist_ok=True)
    specpath = os.path.join(agent_sdk_path, f'openapi.yaml')

    with open(specpath, 'w') as file:
        yaml.dump(agent_spec, file, default_flow_style=False)

    shutil.copy(CLIENT_SCRIPT_PATH, agent_sdk_path)
    subprocess.run(
        [
            "/bin/bash",
            "create_acp_client.sh",
        ],
        cwd=agent_sdk_path
    )
