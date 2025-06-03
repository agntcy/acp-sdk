# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import json
import os
import tempfile
from pathlib import Path
from typing import Optional, Union

import datamodel_code_generator
import yaml
from openapi_spec_validator import validate
from openapi_spec_validator.readers import read_from_filename

from ..agws_v0 import OASF_EXTENSION_NAME_MANIFEST, AgentManifest
from ..exceptions import ACPDescriptorValidationException
from ..models import (
    AgentACPDescriptor,
    AgentACPSpec,
    StreamingMode,
)


def _convert_descriptor_schema(schema_name, schema):
    return json.loads(
        json.dumps(schema).replace(
            "#/$defs/", f"#/components/schemas/{schema_name}/$defs/"
        )
    )


def _gen_oas_thread_runs(descriptor: AgentACPSpec, spec_dict):
    # Manipulate the spec according to the thread capability flag in the descriptor

    if descriptor.capabilities.threads:
        if descriptor.thread_state:
            spec_dict["components"]["schemas"]["ThreadStateSchema"] = (
                _convert_descriptor_schema("ThreadStateSchema", descriptor.thread_state)
            )
        # else:
        #    # No thread schema defined, hence no support to retrieve thread state
        #    del spec_dict['paths']['/threads/{thread_id}/state']
    else:
        # Threads are not enabled
        if descriptor.thread_state:
            raise ACPDescriptorValidationException(
                "Cannot define `thread_state` if `capabilities.threads` is `false`"
            )
        else:
            # Remove all threads paths
            spec_dict["tags"] = [
                tag for tag in spec_dict["tags"] if tag["name"] != "Threads"
            ]
            spec_dict["paths"] = {
                k: v
                for k, v in spec_dict["paths"].items()
                if not k.startswith("/threads")
            }


def _gen_oas_interrupts(descriptor: AgentACPSpec, spec_dict):
    # Manipulate the spec according to the interrupts capability flag in the descriptor

    if descriptor.capabilities.interrupts:
        if not descriptor.interrupts or len(descriptor.interrupts) == 0:
            raise ACPDescriptorValidationException(
                "Missing interrupt definitions with `spec.capabilities.interrupts=true`"
            )

        # Add the interrupt payload and resume payload types for the schemas declared in the descriptor
        interrupt_payload_schema = spec_dict["components"]["schemas"][
            "InterruptPayloadSchema"
        ] = {
            "oneOf": [],
        }
        resume_payload_schema = spec_dict["components"]["schemas"][
            "ResumePayloadSchema"
        ] = {
            "oneOf": [],
        }
        for interrupt in descriptor.interrupts:
            interrupt_payload_schema_name = (
                f"{interrupt.interrupt_type}InterruptPayload"
            )
            interrupt_payload_schema["oneOf"].append(
                {
                    "type": "object",
                    "properties": {
                        interrupt.interrupt_type: {
                            "$ref": f"#/components/schemas/{interrupt_payload_schema_name}",
                        },
                    },
                    "additionalProperties": False,
                    "required": [interrupt.interrupt_type],
                }
            )
            spec_dict["components"]["schemas"][interrupt_payload_schema_name] = (
                _convert_descriptor_schema(
                    interrupt_payload_schema_name, interrupt.interrupt_payload
                )
            )

            resume_payload_schema_name = f"{interrupt.interrupt_type}ResumePayload"
            resume_payload_schema["oneOf"].append(
                {
                    "type": "object",
                    "properties": {
                        interrupt.interrupt_type: {
                            "$ref": f"#/components/schemas/{resume_payload_schema_name}",
                        },
                    },
                    "additionalProperties": False,
                    "required": [interrupt.interrupt_type],
                }
            )
            spec_dict["components"]["schemas"][resume_payload_schema_name] = (
                _convert_descriptor_schema(
                    resume_payload_schema_name, interrupt.resume_payload
                )
            )
    else:
        # Interrupts are not supported

        if descriptor.interrupts and len(descriptor.interrupts) > 0:
            raise ACPDescriptorValidationException(
                "Interrupts defined with `spec.capabilities.interrupts=false`"
            )

        # Remove interrupt support from API
        del spec_dict["paths"]["/runs/{run_id}"]["post"]
        interrupt_ref = spec_dict["components"]["schemas"]["RunOutput"][
            "discriminator"
        ]["mapping"]["interrupt"]
        del spec_dict["components"]["schemas"]["RunOutput"]["discriminator"]["mapping"][
            "interrupt"
        ]
        spec_dict["components"]["schemas"]["RunOutput"]["oneOf"] = [
            e
            for e in spec_dict["components"]["schemas"]["RunOutput"]["oneOf"]
            if e["$ref"] != interrupt_ref
        ]


def _gen_oas_streaming(descriptor: AgentACPSpec, spec_dict):
    # Manipulate the spec according to the streaming capability flag in the descriptor
    streaming_modes = []
    if descriptor.capabilities.streaming:
        if descriptor.capabilities.streaming.custom:
            streaming_modes.append(StreamingMode.CUSTOM)
        if descriptor.capabilities.streaming.values:
            streaming_modes.append(StreamingMode.VALUES)

    # Perform the checks for custom_streaming_update
    if (
        StreamingMode.CUSTOM not in streaming_modes
        and descriptor.custom_streaming_update
    ):
        raise ACPDescriptorValidationException(
            "custom_streaming_update defined with `spec.capabilities.streaming.custom=false`"
        )

    if (
        StreamingMode.CUSTOM in streaming_modes
        and not descriptor.custom_streaming_update
    ):
        raise ACPDescriptorValidationException(
            "Missing custom_streaming_update definitions with `spec.capabilities.streaming.custom=true`"
        )

    if len(streaming_modes) == 0:
        # No streaming is supported. Removing streaming method.
        del spec_dict["paths"]["/runs/{run_id}/stream"]
        # Removing streaming option from RunCreate
        del spec_dict["components"]["schemas"]["RunCreate"]["properties"]["stream_mode"]
        return

    if len(streaming_modes) == 2:
        # Nothing to do
        return

    # If we reach this point only 1 streaming mode is supported, hence we need to restrict the APIs only to accept it and not the other.
    assert len(streaming_modes) == 1

    supported_mode = streaming_modes[0].value
    spec_dict["components"]["schemas"]["StreamingMode"]["enum"] = [supported_mode]
    spec_dict["components"]["schemas"]["RunOutputStream"]["properties"]["data"][
        "$ref"
    ] = spec_dict["components"]["schemas"]["RunOutputStream"]["properties"]["data"][
        "discriminator"
    ]["mapping"][supported_mode]
    del spec_dict["components"]["schemas"]["RunOutputStream"]["properties"]["data"][
        "oneOf"
    ]
    del spec_dict["components"]["schemas"]["RunOutputStream"]["properties"]["data"][
        "discriminator"
    ]


def _gen_oas_callback(descriptor: AgentACPSpec, spec_dict):
    # Manipulate the spec according to the callback capability flag in the descriptor
    if not descriptor.capabilities.callbacks:
        # No streaming is supported. Removing callback option from RunCreate
        del spec_dict["components"]["schemas"]["RunCreate"]["properties"]["webhook"]


def generate_agent_oapi_for_schemas(specs: AgentACPSpec):
    spec_dict = {
        "openapi": "3.1.0",
        "info": {"title": "Agent Schemas", "version": "0.1.0"},
        "components": {"schemas": {}},
    }

    spec_dict["components"]["schemas"]["InputSchema"] = _convert_descriptor_schema(
        "InputSchema", specs.input
    )
    spec_dict["components"]["schemas"]["OutputSchema"] = _convert_descriptor_schema(
        "OutputSchema", specs.output
    )
    spec_dict["components"]["schemas"]["ConfigSchema"] = _convert_descriptor_schema(
        "ConfigSchema", specs.config
    )

    validate(spec_dict)
    return spec_dict


def generate_agent_oapi(
    descriptor: Union[AgentACPDescriptor, AgentManifest],
    spec_path: Optional[str] = None,
):
    if spec_path is None:
        spec_path = os.getenv("ACP_SPEC_PATH", "acp-spec/openapi.json")
    spec_dict, _ = read_from_filename(spec_path)
    # If no exception is raised by validate(), the spec is valid.
    validate(spec_dict)

    agent_spec = None
    if isinstance(descriptor, AgentACPDescriptor):
        agent_spec = descriptor.specs
        agent_name = descriptor.metadata.ref.name
    elif isinstance(descriptor, AgentManifest):
        for ext in descriptor.extensions:
            if ext.name == OASF_EXTENSION_NAME_MANIFEST:
                agent_spec = ext.data.acp
                agent_name = descriptor.name
    else:
        raise ValueError("unknown object type for descriptor")

    spec_dict["info"]["title"] = f"ACP Spec for {agent_name}"

    spec_dict["components"]["schemas"]["InputSchema"] = _convert_descriptor_schema(
        "InputSchema", agent_spec.input
    )
    spec_dict["components"]["schemas"]["OutputSchema"] = _convert_descriptor_schema(
        "OutputSchema", agent_spec.output
    )
    spec_dict["components"]["schemas"]["ConfigSchema"] = _convert_descriptor_schema(
        "ConfigSchema", agent_spec.config
    )

    _gen_oas_thread_runs(agent_spec, spec_dict)
    _gen_oas_interrupts(agent_spec, spec_dict)
    _gen_oas_streaming(agent_spec, spec_dict)
    _gen_oas_callback(agent_spec, spec_dict)

    validate(spec_dict)
    return spec_dict


def generate_agent_models(
    descriptor: Union[AgentACPDescriptor, AgentManifest],
    path: str,
    model_file_name: str = "models.py",
):
    agent_spec = None
    if isinstance(descriptor, AgentACPDescriptor):
        agent_spec = generate_agent_oapi_for_schemas(descriptor.specs)
        agent_name = descriptor.metadata.ref.name
    elif isinstance(descriptor, AgentManifest):
        for ext in descriptor.extensions:
            if ext.name == OASF_EXTENSION_NAME_MANIFEST:
                agent_spec = generate_agent_oapi_for_schemas(ext.data.acp)
                agent_name = descriptor.name
    else:
        raise ValueError("unknown object type for descriptor")

    if agent_spec is None:
        raise ValueError("cannot find ACP descriptor")

    agent_sdk_path = path  # os.path.join(path, f'{descriptor.metadata.ref.name}')
    agent_models_dir = agent_sdk_path
    tmp_dir = tempfile.TemporaryDirectory()
    specpath = os.path.join(tmp_dir.name, "openapi.yaml")
    modelspath = os.path.join(agent_models_dir, model_file_name)

    os.makedirs(agent_models_dir, exist_ok=True)

    with open(specpath, "w") as file:
        yaml.dump(agent_spec, file, default_flow_style=False)

    datamodel_code_generator.generate(
        json.dumps(agent_spec),
        input_filename=specpath,
        input_file_type=datamodel_code_generator.InputFileType.OpenAPI,
        output_model_type=datamodel_code_generator.DataModelType.PydanticV2BaseModel,
        output=Path(modelspath),
        disable_timestamp=True,
        custom_file_header=f"# Generated from ACP Descriptor {agent_name} using datamodel_code_generator.",
        keep_model_order=True,
        use_double_quotes=True,  # match ruff formatting
    )
