# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from typing import Any, Dict, List, Literal, Optional

from agntcy_acp import ApiClientConfiguration
from pydantic import BaseModel

# awk '/operationId/ {print($2);}' acp-spec/openapi.json
OperationId = Literal[
    "search_agents",
    "get_agent_by_id",
    "get_acp_descriptor_by_id",
    "create_thread",
    "search_threads",
    "get_thread_history",
    "copy_thread",
    "get_thread",
    "delete_thread",
    "patch_thread",
    "list_thread_runs",
    "create_thread_run",
    "create_and_stream_thread_run_output",
    "create_and_wait_for_thread_run_output",
    "wait_for_thread_run_output",
    "get_thread_run",
    "resume_thread_run",
    "delete_thread_run",
    "stream_thread_run_output",
    "cancel_thread_run",
    "create_stateless_run",
    "search_stateless_runs",
    "create_and_stream_stateless_run_output",
    "create_and_wait_for_stateless_run_output",
    "wait_for_stateless_run_output",
    "get_stateless_run",
    "resume_stateless_run",
    "delete_stateless_run",
    "stream_stateless_run_output",
    "cancel_stateless_run",
]


class TestInvocation(BaseModel):
    type: str
    arguments: Optional[Dict[str, Any]] = None
    value: Optional[str] = None


class TestMetadata(BaseModel):
    client_config: ApiClientConfiguration
    env_prefix: Optional[str] = None


class TestOperation(BaseModel):
    operation_id: OperationId
    test_input: Optional[Dict[str, TestInvocation]] = None
    output_at_least: Any = None
    output_exact: Any = None


class TestFile(BaseModel):
    metadata: TestMetadata
    operations: List[TestOperation]
