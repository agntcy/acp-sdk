# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from typing import Any, Optional

import requests
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field

from agntcy_acp.langgraph import acp_node


class APIBridgeInput(BaseModel):
    query: str = Field(
        ..., description="Query for the API bridge agent in natural language"
    )


class APIBridgeOutput(BaseModel):
    result: str = Field(..., description="API response from API bridge agent")


class APIBridgeAgentNode(acp_node.ACPNode):
    """
    An ACP node that enables using remotely the API bridge agent in a LangGraph
    multi agent software
    """

    def __init__(
        self,
        name: str,
        hostname: str,
        service_name: str,
        input_path: str,
        output_path: str,
        service_api_key: str,
        input_type: Any = APIBridgeInput,
        output_type: Any = APIBridgeOutput,
        apikey: Optional[str] = None,
    ):
        self.__name__ = name
        self.hostname = hostname
        self.apikey = apikey
        self.service_name = service_name
        # API Bridge agent requires the endpoint to end with '/'
        if not self.service_name.endswith("/"):
            self.service_name += "/"
        self.inputType = input_type
        self.outputType = output_type
        self.inputPath = input_path
        self.outputPath = output_path
        self.service_api_key = service_api_key

    def invoke(self, state: Any, config: RunnableConfig) -> Any:
        api_bridge_input = self._extract_input(state)

        # TODO: Merge config with runnable config
        headers = {
            "Authorization": f"Bearer {self.service_api_key}",
            "Content-Type": "application/nlq",
        }
        r = requests.post(
            f"{self.hostname}/{self.service_name}",
            headers=headers,
            data=api_bridge_input["query"],
        )
        r.raise_for_status()
        response = r.text
        if not response:
            response = f"Operation performed: {r.url} Result{r.status_code}"
        output = APIBridgeOutput(result=response)
        self._set_output(state, self.outputType.model_validate(output.model_dump()))

        return state

    async def ainvoke(self, state: Any, config: RunnableConfig) -> Any:
        # TODO: Add proper support for ainvoke.
        self.invoke(state, config)

        return state
