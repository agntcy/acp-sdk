# Generated from ACP Descriptor org.agntcy.mailcomposer using datamodel_code_generator.

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Literal


class AIMessage(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    content: Union[str, List[Union[str, Dict[str, Any]]]] = Field(..., title='Content')
    additional_kwargs: Optional[Dict[str, Any]] = Field(None, title='Additional Kwargs')
    response_metadata: Optional[Dict[str, Any]] = Field(None, title='Response Metadata')
    type: Literal['ai'] = Field('ai', title='Type')
    name: Optional[str] = Field(None, title='Name')
    id: Optional[str] = Field(None, title='Id')
    example: Optional[bool] = Field(False, title='Example')
    tool_calls: Optional[List[ToolCall]] = Field([], title='Tool Calls')
    invalid_tool_calls: Optional[List[InvalidToolCall]] = Field(
        [], title='Invalid Tool Calls'
    )
    usage_metadata: Optional[UsageMetadata] = None


class ConfigSchema(BaseModel):
    messages: Optional[List[Union[AIMessage, HumanMessage]]] = Field(
        None, title='Messages'
    )
    is_completed: Optional[bool] = Field(None, title='Is Completed')
    final_email: str = Field(..., title='Final Email')


class HumanMessage(BaseModel):
    model_config = ConfigDict(
        extra='allow',
    )
    content: Union[str, List[Union[str, Dict[str, Any]]]] = Field(..., title='Content')
    additional_kwargs: Optional[Dict[str, Any]] = Field(None, title='Additional Kwargs')
    response_metadata: Optional[Dict[str, Any]] = Field(None, title='Response Metadata')
    type: Literal['human'] = Field('human', title='Type')
    name: Optional[str] = Field(None, title='Name')
    id: Optional[str] = Field(None, title='Id')
    example: Optional[bool] = Field(False, title='Example')


class InputSchema(BaseModel):
    messages: Optional[List[Union[AIMessage, HumanMessage]]] = Field(
        None, title='Messages'
    )
    is_completed: Optional[bool] = Field(None, title='Is Completed')


class InputTokenDetails(BaseModel):
    audio: Optional[int] = Field(None, title='Audio')
    cache_creation: Optional[int] = Field(None, title='Cache Creation')
    cache_read: Optional[int] = Field(None, title='Cache Read')


class InvalidToolCall(BaseModel):
    name: Optional[str] = Field(..., title='Name')
    args: Optional[str] = Field(..., title='Args')
    id: Optional[str] = Field(..., title='Id')
    error: Optional[str] = Field(..., title='Error')
    type: Literal['invalid_tool_call'] = Field('invalid_tool_call', title='Type')


class OutputSchema(BaseModel):
    messages: Optional[List[Union[AIMessage, HumanMessage]]] = Field(
        None, title='Messages'
    )
    is_completed: Optional[bool] = Field(None, title='Is Completed')
    final_email: str = Field(..., title='Final Email')


class OutputTokenDetails(BaseModel):
    audio: Optional[int] = Field(None, title='Audio')
    reasoning: Optional[int] = Field(None, title='Reasoning')


class ToolCall(BaseModel):
    name: str = Field(..., title='Name')
    args: Dict[str, Any] = Field(..., title='Args')
    id: Optional[str] = Field(..., title='Id')
    type: Literal['tool_call'] = Field('tool_call', title='Type')


class UsageMetadata(BaseModel):
    input_tokens: int = Field(..., title='Input Tokens')
    output_tokens: int = Field(..., title='Output Tokens')
    total_tokens: int = Field(..., title='Total Tokens')
    input_token_details: Optional[InputTokenDetails] = None
    output_token_details: Optional[OutputTokenDetails] = None
