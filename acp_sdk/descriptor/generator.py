# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
import os
import tempfile

from acp_sdk.models import AgentACPDescriptor, StreamingMode, AgentMetadata, AgentACPSpec, AgentCapabilities
import yaml
from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename
import datamodel_code_generator
import json
from pathlib import Path
import subprocess
import shutil
from acp_sdk.exceptions import ACPDescriptorValidationException

ACP_SPEC_PATH = os.getenv("ACP_SPEC_PATH", "acp-spec/openapi.yaml")
CLIENT_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "scripts/create_acp_client.sh")

def _convert_descriptor_schema(schema_name, schema):
    return json.loads(
        json.dumps(schema).replace("#/$defs/", f"#/components/schemas/{schema_name}/$defs/"))


def _gen_oas_thread_runs(descriptor: AgentACPDescriptor, spec_dict):
    # Manipulate the spec according to the thread capability flag in the descriptor

    if descriptor.specs.capabilities.threads:
        if descriptor.specs.thread_state:
            spec_dict['components']['schemas']["ThreadStateSchema"] = _convert_descriptor_schema("ThreadStateSchema", descriptor.specs.thread_state)
        else:
            # No thread schema defined, hence no support to retrieve thread state
            del spec_dict['paths']['/threads/{thread_id}/state']
            del spec_dict['paths']['/runs/{run_id}/threadstate']
    else:
        # Threads are not enabled
        if descriptor.specs.thread_state:
            raise ACPDescriptorValidationException(
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


def _gen_oas_interrupts(descriptor: AgentACPDescriptor, spec_dict):
    # Manipulate the spec according to the interrupts capability flag in the descriptor

    if descriptor.specs.capabilities.interrupts:
        if not descriptor.specs.interrupts or len(descriptor.specs.interrupts) == 0:
            raise ACPDescriptorValidationException("Missing interrupt definitions with `spec.capabilities.interrupts=true`")

        # Add the interrupt payload and resume payload types for the schemas declared in the descriptor
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
        for interrupt in descriptor.specs.interrupts:
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
            spec_dict['components']['schemas'][interrupt_payload_schema_name] = _convert_descriptor_schema(interrupt_payload_schema_name, interrupt.interrupt_payload)

            resume_payload_schema_name = f"{interrupt.interrupt_type}ResumePayload"
            interrupt.resume_payload['properties']['interrupt_type'] = interrupt.interrupt_payload['properties'][
                'interrupt_type']

            spec_dict['components']['schemas']['ResumePayloadSchema']['oneOf'].append(
                {'$ref': f'#/components/schemas/{resume_payload_schema_name}'}
            )
            spec_dict['components']['schemas']['ResumePayloadSchema']['discriminator']['mapping'][
                interrupt.interrupt_type] = f'#/components/schemas/{resume_payload_schema_name}'
            spec_dict['components']['schemas'][resume_payload_schema_name] = _convert_descriptor_schema(resume_payload_schema_name, interrupt.resume_payload)
    else:
        # Interrupts are not supported 

        if descriptor.specs.interrupts and len(descriptor.specs.interrupts) > 0:
            raise ACPDescriptorValidationException("Interrupts defined with `spec.capabilities.interrupts=false`")

        # Remove interrupt support from API
        del spec_dict['paths']['/runs/{run_id}']['post']
        interrupt_ref = spec_dict['components']['schemas']['RunOutput']['discriminator']['mapping']['interrupt']
        del spec_dict['components']['schemas']['RunOutput']['discriminator']['mapping']['interrupt']
        spec_dict['components']['schemas']['RunOutput']['oneOf'] = [e for e in
                                                                    spec_dict['components']['schemas']['RunOutput'][
                                                                        'oneOf'] if e['$ref'] != interrupt_ref]


def _gen_oas_streaming(descriptor: AgentACPDescriptor, spec_dict):
    # Manipulate the spec according to the streaming capability flag in the descriptor
    streaming_modes = []
    if descriptor.specs.capabilities.streaming:
        if descriptor.specs.capabilities.streaming.custom: streaming_modes.append(StreamingMode.CUSTOM)
        if descriptor.specs.capabilities.streaming.result: streaming_modes.append(StreamingMode.RESULT)

    # Perform the checks for custom_streaming_update
    if StreamingMode.CUSTOM not in streaming_modes and descriptor.specs.custom_streaming_update:
        raise ACPDescriptorValidationException(
            "custom_streaming_update defined with `spec.capabilities.streaming.custom=false`")

    if StreamingMode.CUSTOM in streaming_modes and not descriptor.specs.custom_streaming_update:
        raise ACPDescriptorValidationException(
            "Missing custom_streaming_update definitions with `spec.capabilities.streaming.custom=true`")

    if len(streaming_modes) == 0:
        # No streaming is supported. Removing streaming method.
        del spec_dict['paths']['/runs/{run_id}/stream']
        # Removing streaming option from RunCreate
        del spec_dict['components']['schemas']['RunCreate']['properties']['streaming']
        return

    if len(streaming_modes) == 2:
        # Nothing to do
        return

    # If we reach this point only 1 streaming mode is supported, hence we need to restrict the APIs only to accept it and not the other.
    assert (len(streaming_modes) == 1)

    supported_mode = streaming_modes[0].value
    spec_dict['components']['schemas']['StreamingMode']['enum'] = [supported_mode]
    spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['$ref'] = \
    spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['discriminator']['mapping'][
        supported_mode]
    del spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['oneOf']
    del spec_dict['components']['schemas']['RunOutputStream']['properties']['data']['discriminator']['mapping']


def _gen_oas_callback(descriptor: AgentACPDescriptor, spec_dict):
    # Manipulate the spec according to the callback capability flag in the descriptor
    if not descriptor.specs.capabilities.callbacks:
        # No streaming is supported. Removing callback option from RunCreate
        del spec_dict['components']['schemas']['RunCreate']['properties']['webhook']

def generate_agent_oapi_for_schemas(descriptor: AgentACPDescriptor):
    spec_dict = {
        "openapi": "3.1.0",
        "info": {
            "title": "Agent Schemas",
            "version": "0.1.0"
        },
        "components": {
            "schemas": {}
        }
    }

    spec_dict['components']['schemas']["InputSchema"] = _convert_descriptor_schema("InputSchema", descriptor.specs.input)
    spec_dict['components']['schemas']["OutputSchema"] = _convert_descriptor_schema("OutputSchema", descriptor.specs.output)
    spec_dict['components']['schemas']["ConfigSchema"] = _convert_descriptor_schema("ConfigSchema", descriptor.specs.config)
    validate(spec_dict)
    return spec_dict


def generate_agent_oapi(descriptor: AgentACPDescriptor):
    spec_dict, base_uri = read_from_filename(ACP_SPEC_PATH)

    # If no exception is raised by validate(), the spec is valid.
    validate(spec_dict)

    spec_dict['info']['title'] = f"ACP Spec for {descriptor.metadata.ref.name}:{descriptor.metadata.ref.version}"

    spec_dict['components']['schemas']["InputSchema"] = _convert_descriptor_schema("InputSchema", descriptor.specs.input)
    spec_dict['components']['schemas']["OutputSchema"] = _convert_descriptor_schema("OutputSchema", descriptor.specs.output)
    spec_dict['components']['schemas']["ConfigSchema"] = _convert_descriptor_schema("ConfigSchema", descriptor.specs.config)

    _gen_oas_thread_runs(descriptor, spec_dict)
    _gen_oas_interrupts(descriptor, spec_dict)
    _gen_oas_streaming(descriptor, spec_dict)
    _gen_oas_callback(descriptor, spec_dict)

    validate(spec_dict)
    return spec_dict


def generate_agent_models(descriptor: AgentACPDescriptor, path: str, model_file_name:str = "models.py"):
    agent_spec = generate_agent_oapi_for_schemas(descriptor)
    agent_sdk_path = path # os.path.join(path, f'{descriptor.metadata.ref.name}')
    agent_models_dir = agent_sdk_path
    tmp_dir = tempfile.TemporaryDirectory()
    specpath = os.path.join(tmp_dir.name, f'openapi.yaml')
    modelspath = os.path.join(agent_models_dir, model_file_name)

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

def generate_agent_descriptor(metadata:AgentMetadata, inputModel, outputModel, configModel, path):
    input_oapi = inputModel.model_json_schema()
    output_oapi= outputModel.model_json_schema()
    config_oapi = configModel.model_json_schema()
    descriptor = AgentACPDescriptor(
        metadata=metadata,
        specs=AgentACPSpec(
            input=input_oapi,
            output=output_oapi,
            config=config_oapi,
            capabilities=AgentCapabilities()
        )

    )
    with open(path, "w") as f:
        f.write(descriptor.model_dump_json())





def generate_agent_client(descriptor: AgentACPDescriptor, path: str):
    agent_spec = generate_agent_oapi(descriptor)
    agent_sdk_path = os.path.join(path, f'{descriptor.metadata.ref.name}')
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
