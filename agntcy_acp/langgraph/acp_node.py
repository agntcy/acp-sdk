# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import logging
from typing import Any

from langchain_core.runnables import RunnableConfig
from langgraph.utils.runnable import RunnableCallable

from agntcy_acp import (
    ACPClient,
    ApiClient,
    AsyncACPClient,
    AsyncApiClient,
    Configuration,
)
from agntcy_acp.exceptions import ACPRunException
from agntcy_acp.models import Run, RunCreate, RunError, RunOutput, RunResult

logger = logging.getLogger(__name__)


def _extract_element(container: Any, path: str):
    element = container
    for path_el in path.split("."):
        element = (
            element.get(path_el)
            if isinstance(element, dict)
            else getattr(element, path_el)
        )

    if element is None:
        raise Exception(f"Unable to extract {path} from state {container}")

    return element


class ACPNode:
    """This class represents a Langgraph Node that holds a remote connection to an ACP Agent
    It can be instantiated and added to any langgraph graph.

    my_node = ACPNode(...)
    sg = StateGraph(GraphState)
    sg.add_node(my_node)
    """

    def __init__(
        self,
        name: str,
        agent_id: str,
        client_config: Configuration,
        input_path: str,
        input_type,
        output_path: str,
        output_type,
        config_path: str = None,
        config_type=None,
        auth_header: dict = None,
    ):
        """Instantiate a Langgraph node encapsulating a remote ACP agent

        :param name: Name of the langgraph node
        :param agent_id: Agent ID in the remote server
        :param client_config: Configuration of the ACP Client
        :param input_path: Dot-separated path of the ACP Agent input in the graph overall state
        :param input_type: Pydantic class defining the schema of the ACP Agent input
        :param output_path: Dot-separated path of the ACP Agent output in the graph overall state
        :param output_type: Pydantic class defining the schema of the ACP Agent output
        :param config_path: Dot-separated path of the ACP Agent config in the graph configurable
        :param config_type: Pydantic class defining the schema of the ACP Agent config
        :param auth_header: A dictionary containing auth details necessary to communicate with the node
        """

        self.__name__ = name
        self.agent_id = agent_id
        self.clientConfig = client_config
        self.inputPath = input_path
        self.inputType = input_type
        self.outputPath = output_path
        self.outputType = output_type
        self.configPath = config_path
        self.configType = config_type
        self.auth_header = auth_header

    def get_name(self):
        return self.__name__

    def _extract_input(self, state: Any):
        try:
            return _extract_element(state, self.inputPath)
        except Exception as e:
            raise Exception(
                f"ERROR in ACP Node {self.get_name()}. Unable to extract input: {e}"
            )

    def _extract_config(self, config: Any):
        try:
            config = _extract_element(config["configurable"], self.configPath)
        except Exception as e:
            logger.info(f"ACP Node {self.get_name()}. Unable to extract config: {e}")
            return None

        return self.configType.model_validate(config)

    def _set_output(self, state: Any, output: Any):
        output_parent = state
        for el in self.outputPath.split(".")[:-1]:
            output_parent = getattr(output_parent, el)
        setattr(
            output_parent,
            self.outputPath.split(".")[-1],
            self.outputType.model_validate(output),
        )

    def _prepare_run_create(self, state: Any, config: RunnableConfig):
        agent_input = self._extract_input(state)
        agent_config = self._extract_config(config)

        run_create = RunCreate(
            agent_id=self.agent_id,
            input=agent_input.model_dump(),
            config=agent_config.model_dump() if agent_config else {},
        )

        return run_create

    def _handle_run_output(self, state: Any, run_output: RunOutput):
        if isinstance(run_output.actual_instance, RunResult):
            run_result: RunResult = run_output.actual_instance
            self._set_output(state, run_result.result)
        elif isinstance(run_output.actual_instance, RunError):
            run_error: RunError = run_output.actual_instance
            raise ACPRunException(f"Run Failed: {run_error}")
        else:
            raise ACPRunException(
                f"ACP Server returned a unsupporteed response: {run_output}"
            )

        return state

    def invoke(self, state: Any, config: RunnableConfig) -> Any:

        run_create = self._prepare_run_create(state, config)

        api_client = (
            ApiClient(
                configuration=self.clientConfig,
                header_name=self.auth_header["name"],
                header_value=self.auth_header["value"],
            ),
        )
        acp_client = ACPClient(api_client=api_client)
        run: Run = acp_client.create_run(run_create)
        run_output = acp_client.get_run_output(run_id=run.run_id, block_timeout=120)

        return self._handle_run_output(state, run_output)

    async def ainvoke(self, state: Any, config: RunnableConfig) -> Any:
        run_create = self._prepare_run_create(state, config)
        api_client = AsyncApiClient(
            configuration=self.clientConfig,
            header_name=self.auth_header["name"],
            header_value=self.auth_header["value"],
        )
        acp_client = AsyncACPClient(api_client=api_client)

        run: Run = await acp_client.create_run(run_create)
        run_output = await acp_client.get_run_output(
            run_id=run.run_id, block_timeout=120
        )

        return self._handle_run_output(state, run_output)

    def __call__(self, state, config):
        return RunnableCallable(self.invoke, self.ainvoke)
