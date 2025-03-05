# generated by datamodel-codegen:
#   filename:  openapi.yaml

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, conint
from typing_extensions import Literal


class AgentRef(BaseModel):
    name: str = Field(
        ...,
        description='Name of the agent that identifies the agent in its record',
        title='Name',
    )
    version: str = Field(
        ...,
        description='Version of the agent in its record. Should be formatted according to semantic versioning (https://semver.org)',
        title='Version',
    )
    url: Optional[AnyUrl] = Field(
        None,
        description='URL of the record. Can be a network location or a file.',
        title='Agent Record URL',
    )


class Streaming(BaseModel):
    result: Optional[bool] = Field(
        None,
        description='This is `true` if the agent supports result streaming. If `false` or missing, result streaming is not supported. Result streaming consists of a stream of objects of type `RunResult`, where each one sent over the stream fully replace the previous one.',
        title='Result Streaming',
    )
    custom: Optional[bool] = Field(
        None,
        description='This is `true` if the agent supports custom objects streaming. If `false` or missing, custom streaming is not supported. Custom Objects streaming consists of a stream of object whose schema is specified by the agent ACP descriptor under `specs.custom_streaming_update`.',
        title='Custom Objects Streaming',
    )


class Capabilities(BaseModel):
    threads: Optional[bool] = Field(
        False,
        description='This is `true` if the agent supports run threads. If this is `false`, then the threads tagged with `Threads` are not available. If missing, it means `false`',
        title='Thread Support',
    )
    interrupts: Optional[bool] = Field(
        False,
        description='This is `true` if the agent runs can interrupt to request additional input and can be subsequently resumed. If missing, it means `false`',
        title='Interrupt Support',
    )
    callbacks: Optional[bool] = Field(
        False,
        description='This is `true` if the agent supports a webhook to report run results. If this is `false`, providing a `webhook` at run creation has no effect. If missing, it means `false`',
        title='Callback Support',
    )
    streaming: Optional[Streaming] = Field(
        None,
        description='Supported streaming modes. If missing, streaming is not supported.  If no mode is supported attempts to stream output will result in an error.',
        title='Streaming Modes',
    )


class Interrupt(BaseModel):
    interrupt_type: str = Field(
        ...,
        description='Name of this interrupt type. Needs to be unique in the list of interrupts.',
        title='Interrupt Type Name',
    )
    interrupt_payload: Dict[str, Any] = Field(
        ...,
        description='This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object',
        examples=[
            {
                'type': 'object',
                'required': ['name'],
                'properties': None,
                'name': {'type': 'string'},
                'address': {'type': 'string'},
                'age': {'type': 'integer', 'format': 'int32', 'minimum': 0},
            }
        ],
    )
    resume_payload: Dict[str, Any] = Field(
        ...,
        description='This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object',
        examples=[
            {
                'type': 'object',
                'required': ['name'],
                'properties': None,
                'name': {'type': 'string'},
                'address': {'type': 'string'},
                'age': {'type': 'integer', 'format': 'int32', 'minimum': 0},
            }
        ],
    )


class Specs(BaseModel):
    capabilities: Capabilities = Field(
        ...,
        description='Declares what invocation features this agent is capable of.',
        title='Agent Capabilities',
    )
    input: Dict[str, Any] = Field(
        ...,
        description='This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object',
        examples=[
            {
                'type': 'object',
                'required': ['name'],
                'properties': {
                    'name': {'type': 'string'},
                    'address': {'type': 'string'},
                    'age': {'type': 'integer', 'format': 'int32', 'minimum': 0},
                },
            }
        ],
    )
    output: Dict[str, Any] = Field(
        ...,
        description='This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object',
        examples=[
            {
                'type': 'object',
                'required': ['name'],
                'properties': None,
                'name': {'type': 'string'},
                'address': {'type': 'string'},
                'age': {'type': 'integer', 'format': 'int32', 'minimum': 0},
            }
        ],
    )
    custom_streaming_update: Optional[Dict[str, Any]] = Field(
        None,
        description='This describes the format of an Update in the streaming.  Must be specified if `streaming.custom` capability is true and cannot be specified otherwise. Format follows: https://spec.openapis.org/oas/v3.1.1.html#schema-object',
        examples=[
            {
                'type': 'object',
                'required': ['name'],
                'properties': None,
                'name': {'type': 'string'},
                'address': {'type': 'string'},
                'age': {'type': 'integer', 'format': 'int32', 'minimum': 0},
            }
        ],
    )
    thread_state: Optional[Dict[str, Any]] = Field(
        None,
        description='This describes the format of ThreadState.  Cannot be specified if `threads` capability is false. If not specified, when `threads` capability is true, then the API to retrieve ThreadState from a Thread or a Run is not available. This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object',
        examples=[
            {
                'type': 'object',
                'required': ['name'],
                'properties': None,
                'name': {'type': 'string'},
                'address': {'type': 'string'},
                'age': {'type': 'integer', 'format': 'int32', 'minimum': 0},
            }
        ],
    )
    config: Dict[str, Any] = Field(
        ...,
        description='This object contains an instance of an OpenAPI schema object, formatted as per the OpenAPI specs: https://spec.openapis.org/oas/v3.1.1.html#schema-object',
        examples=[
            {
                'type': 'object',
                'required': ['name'],
                'properties': None,
                'name': {'type': 'string'},
                'address': {'type': 'string'},
                'age': {'type': 'integer', 'format': 'int32', 'minimum': 0},
            }
        ],
    )
    interrupts: Optional[List[Interrupt]] = Field(
        None,
        description='List of possible interrupts that can be provided by the agent. If `interrupts` capability is true, this needs to have at least one item.',
    )


class AgentSearchRequest(BaseModel):
    name: Optional[str] = Field(
        None, description='Match all agents with the name specified.', title='Name'
    )
    version: Optional[str] = Field(
        None,
        description='Match all agents with the version specified. Formatted according to semantic versioning (https://semver.org)',
        title='Version',
    )
    limit: Optional[conint(ge=1, le=1000)] = Field(
        10, description='Maximum number to return.', title='Limit'
    )
    offset: Optional[conint(ge=0)] = Field(
        0, description='Offset to start from.', title='Offset'
    )


class ErrorResponse(RootModel[str]):
    root: str = Field(
        ..., description='Error message returned from the server', title='ErrorResponse'
    )


class StreamingMode(Enum):
    result = 'result'
    custom = 'custom'


class RunStatus(Enum):
    pending = 'pending'
    error = 'error'
    success = 'success'
    timeout = 'timeout'
    interrupted = 'interrupted'


class RunSearchRequest(BaseModel):
    agent_id: Optional[UUID] = Field(
        None,
        description='Matches all the Runs associated with the specified Agent ID.',
        title='Agent Id',
    )
    status: Optional[RunStatus] = Field(
        None,
        description="Matches all the Runs associated with the specified status. One of 'pending', 'error', 'success', 'timeout', 'interrupted'.",
        title='Status',
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description='Matches all threads for which metadata has  keys and values equal to those specified in this object.',
        title='Metadata Filter',
    )
    limit: Optional[conint(ge=1, le=1000)] = Field(
        10, description='Maximum number to return.', title='Limit'
    )
    offset: Optional[conint(ge=0)] = Field(
        0, description='Offset to start from.', title='Offset'
    )


class Type(Enum):
    result = 'result'


class Event(Enum):
    agent_event = 'agent_event'


class Type1(Enum):
    custom = 'custom'


class Type2(Enum):
    error = 'error'


class RunError(BaseModel):
    type: Literal['error'] = Field(..., title='Output Type')
    run_id: UUID = Field(..., description='The ID of the run.', title='Run Id')
    errcode: int = Field(..., description='code of the error', title='Error Code')
    description: str = Field(
        ..., description='description of the error', title='Error Description'
    )


class Type3(Enum):
    interrupt = 'interrupt'


class InputSchema(BaseModel):
    pass


class OutputSchema(BaseModel):
    pass


class ConfigSchema(BaseModel):
    pass


class ThreadStateSchema(BaseModel):
    pass


class StreamUpdateSchema(BaseModel):
    pass


class InterruptPayloadSchema(BaseModel):
    pass


class ResumePayloadSchema(BaseModel):
    pass


class ThreadCreate(BaseModel):
    agent_id: str = Field(
        ...,
        description='Identifier of the agent this thread is executed on',
        title='Agent ID',
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None, description='Free form metadata for this thread', title='Metadata'
    )


class ThreadSearchRequest(BaseModel):
    agent_id: Optional[UUID] = Field(
        None,
        description='Matches all threads associated with the specified agent ID.',
        title='Agent Id',
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description='Matches all threads for which metadata has  keys and values equal to those specified in this object.',
        title='Metadata Filter',
    )
    limit: Optional[conint(ge=1, le=1000)] = Field(
        10, description='Maximum number to return.', title='Limit'
    )
    offset: Optional[conint(ge=0)] = Field(
        0, description='Offset to start from.', title='Offset'
    )


class Thread(BaseModel):
    thread_id: str = Field(
        ..., description='unique identifier of a thread', title='Thread ID'
    )
    agent_id: str = Field(
        ...,
        description='Identifier of the agent this thread is executed on',
        title='Agent ID',
    )
    metadata: Optional[Dict[str, Any]] = Field(
        None, description='Free form metadata for this thread', title='Metadata'
    )


class AgentMetadata(BaseModel):
    ref: AgentRef
    description: str = Field(
        ...,
        description='Description of this agent, which should include what the intended use is, what tasks it accomplishes and how uses input and configs to produce the output and any other side effect',
        title='Description',
    )


class AgentACPDescriptor(BaseModel):
    metadata: AgentMetadata
    specs: Specs = Field(
        ...,
        description='Specification of agent capabilities, config, input, output, and interrupts',
        title='Agent ACP Specs',
    )


class RunCreate(BaseModel):
    agent_id: UUID = Field(..., description='The ID of the agent.', title='Agent Id')
    thread_id: Optional[UUID] = Field(
        None,
        description='Optional Thread ID wher the Run belongs to. This can be used only for agents supporting Threads.',
        title='Agent ID',
    )
    input: Optional[InputSchema] = None
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        description='Metadata to assign to the run. Optional free format metadata to attach to the run.',
        title='Metadata',
    )
    config: Optional[ConfigSchema] = None
    webhook: Optional[AnyUrl] = Field(
        None,
        description='Webhook to call upon change of run status. This is a url that accepts a POST containing the `Run` object as body. See Callbacks definition.',
        title='Status change webhook',
    )
    streaming: Optional[StreamingMode] = Field(
        None,
        description='If populated, indicates that the client requests to stream results with the specified streaming mode. The requested streaming mode must be one of the one supported by the agent as declared in agent ACP descriptor  under `specs.capabilities`',
        title='Streaming Mode',
    )


class Run(BaseModel):
    creation: RunCreate
    run_id: UUID = Field(..., description='The ID of the run.', title='Run Id')
    agent_id: UUID = Field(
        ..., description='The agent that was used for this run.', title='Agent Id'
    )
    thread_id: Optional[UUID] = Field(
        None,
        description='Optional Thread ID wher the Run belongs to. This is populated only for runs on agents agents supporting Threads.',
        title='Agent ID',
    )
    created_at: AwareDatetime = Field(
        ..., description='The time the run was created.', title='Created At'
    )
    updated_at: AwareDatetime = Field(
        ..., description='The last time the run was updated.', title='Updated At'
    )
    status: RunStatus = Field(
        ...,
        description="The status of the run. One of 'pending', 'error', 'success', 'timeout', 'interrupted'.",
        title='Status',
    )


class RunResult(BaseModel):
    type: Literal['result'] = Field(..., title='Output Type')
    run_id: UUID = Field(..., description='The ID of the run.', title='Run Id')
    status: RunStatus = Field(
        ...,
        description='Status of the Run when this result was generated. This is particurarly useful when this data structure is used for streaming results. As the server can indicate an interrupt or an error condition while streaming the result.',
        title='Run Status',
    )
    result: OutputSchema


class CustomRunResultUpdate(BaseModel):
    type: Literal['custom'] = Field(..., title='Output Type')
    run_id: UUID = Field(..., description='The ID of the run.', title='Run Id')
    status: RunStatus = Field(
        ...,
        description='Status of the Run when this result was generated',
        title='Run Status',
    )
    update: StreamUpdateSchema


class RunInterrupt(BaseModel):
    type: Literal['interrupt'] = Field(..., title='Output Type')
    interrupt: InterruptPayloadSchema


class Agent(BaseModel):
    agent_id: UUID = Field(
        ...,
        description='Unique identifier of the agent in this server.',
        title='Agent Id',
    )
    metadata: AgentMetadata


class RunOutput(RootModel[Union[RunResult, RunInterrupt, RunError]]):
    root: Union[RunResult, RunInterrupt, RunError] = Field(
        ...,
        description='Output of a Run. Can be the final result or an interrupt.',
        discriminator='type',
        title='Run Output',
    )


class RunOutputStream(BaseModel):
    id: str = Field(..., description='Unique identifier of the event', title='Event ID')
    event: Event = Field(
        ...,
        description='Event type. This is the constant string `agent_event` to be compatible with SSE spec. The actual type differentiation is done in the event itself.',
    )
    data: Union[RunResult, CustomRunResultUpdate] = Field(
        ...,
        description='A serialized JSON data structure carried in the SSE event data field. The event can carry either a full `RunResult`, if streaming mode is `result` or an custom update if streaming mode is `custom`',
        discriminator='type',
        title='Stream Event Payload',
    )
