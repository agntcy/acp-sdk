# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import logging
from collections.abc import MutableMapping
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel
from langchain_core.runnables import RunnableConfig
from langgraph.types import (
    interrupt,
)
from langgraph.utils.runnable import RunnableCallable
from pydantic import BaseModel

from agntcy_acp import (
    ACPClient,
    ApiClientConfiguration,
    AsyncACPClient,
)
from agntcy_acp.exceptions import ACPRunException
from agntcy_acp.models import (
    Config,
    RunCreateStateful,
    RunCreateStateless,
    RunError,
    RunInterrupt,
    RunOutput,
    RunResult,
    RunWaitResponseStateless,
)

logger = logging.getLogger(__name__)


def _extract_element(container: Any, path: str) -> Any:
    element = container
    for path_el in path.split("."):
        element = (
            element.get(path_el)
            if isinstance(element, MutableMapping)
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
        client_config: ApiClientConfiguration,
        input_path: str,
        input_type,
        output_path: str,
        output_type,
        config_path: Optional[str] = None,
        config_type=None,
        auth_header: Optional[Dict] = None,
        use_threads: bool = False,
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
        self.previous_thread_run = {}

    def get_name(self):
        return self.__name__

    def _extract_input(self, state: Any) -> Any:
        if not state:
            return state

        try:
            if self.inputPath:
                state = _extract_element(state, self.inputPath)
        except Exception as e:
            raise Exception(
                f"ERROR in ACP Node {self.get_name()}. Unable to extract input: {e}"
            )

        if isinstance(state, BaseModel):
            return state.model_dump()
        elif isinstance(state, MutableMapping):
            return state
        else:
            return {}

    def _extract_config(self, config: Any) -> Any:
        if not config:
            return config

        try:
            if not self.configPath:
                config = {}
            else:
                if "configurable" not in config:
                    logger.error(
                        f'ACP Node {self.get_name()}. Unable to extract config: missing key "configurable" in RunnableConfig'
                    )
                    return None

                config = _extract_element(config["configurable"], self.configPath)
        except Exception as e:
            logger.info(f"ACP Node {self.get_name()}. Unable to extract config: {e}")
            return None

        if self.configType is not None:
            # Set defaults, etc.
            agent_config = self.configType.model_validate(config)
        else:
            agent_config = config

        if isinstance(agent_config, BaseModel):
            return agent_config.model_dump()
        elif isinstance(agent_config, MutableMapping):
            return agent_config
        else:
            return {}

    def _set_output(self, state: Any, output: Optional[Dict[str, Any]]):
        output_parent = state
        output_state = self.outputType.model_validate(output)

        for el in self.outputPath.split(".")[:-1]:
            if isinstance(output_parent, MutableMapping):
                output_parent = output_parent[el]
            elif hasattr(output_parent, el):
                output_parent = getattr(output_parent, el)
            else:
                raise ValueError("object missing attribute: {el}")

        el = self.outputPath.split(".")[-1]
        if isinstance(output_parent, MutableMapping):
            output_parent[el] = output_state
        elif hasattr(output_parent, el):
            setattr(output_parent, el, output_state)
        else:
            raise ValueError("object missing attribute: {el}")
    
    def _handle_run_output(self, state: Any, run_output: RunOutput):
        if isinstance(run_output.actual_instance, RunResult):
            run_result: RunResult = run_output.actual_instance
            self._set_output(state, run_result.values)
        elif isinstance(run_output.actual_instance, RunError):
            run_error: RunError = run_output.actual_instance
            raise ACPRunException(f"Run Failed: {run_error}")
        elif isinstance(run_output.actual_instance, RunInterrupt):
            # This case is handled in the invokes
            pass

        else:
            raise ACPRunException(
                f"ACP Server returned a unsupporteed response: {run_output}"
            )

        return state

    def _get_thread_id(self, config: RunnableConfig) -> Optional[str]:
        configurable = config.get("configurable", {})
        thread_id = configurable.get("thread_id", None)
        return thread_id

    def _handle_interrupt(
        self,
        config: RunnableConfig,
        run_output: RunWaitResponseStateless,
        thread_id: Optional[str],
    ):
        if thread_id is None:
            raise ValueError("Thread_id is required for a interrupted run")

        first_key = next(iter(run_output.output.actual_instance.interrupt))

        value = run_output.output.actual_instance.interrupt[first_key]

        previous_thread_run = self.previous_thread_run.get(thread_id, None)

        if previous_thread_run is None:
            self.previous_thread_run[thread_id] = run_output

        interrupt_result = interrupt(value)
        del self.previous_thread_run[thread_id]

        return interrupt_result

    def invoke(
        self,
        state: dict[str, Any] | Any,
        config: Optional[RunnableConfig] = None,
        **kwargs: Any,
    ) -> Any:
        with ACPClient(configuration=self.clientConfig) as acp_client:
            thread_id = self._get_thread_id(config)
            run_output = None
            if thread_id is not None:
                if thread_id in self.previous_thread_run:
                    run_output = self.previous_thread_run.get(thread_id, None)
                else:
                    run_create = RunCreateStateful(
                        agent_id=self.agent_id,
                        input=self._extract_input(state),
                        config=Config(configurable=self._extract_config(config)),
                    )
                    run_output = acp_client.create_and_wait_for_thread_run_output(thread_id, run_create)
            else:
                run_create = RunCreateStateless(
                    agent_id=self.agent_id,
                    input=self._extract_input(state),
                    config=Config(configurable=self._extract_config(config)),
                )
                run_output = acp_client.create_and_wait_for_stateless_run_output(
                    run_create
                )

            while isinstance(run_output.output.actual_instance, RunInterrupt):
                interrupt_result = self._handle_interrupt(
                    config=config, run_output=run_output, thread_id=thread_id
                )
                resume_run = acp_client.resume_stateless_run(
                    run_id=run_output.run.run_id, body=interrupt_result
                )
                run_output = acp_client.wait_for_stateless_run_output(
                    run_id=resume_run.run_id
                )

        # output is the same between stateful and stateless
        self._handle_run_output(state, run_output.output)
        return state

    async def ainvoke(
        self,
        state: dict[str, Any] | Any,
        config: Optional[RunnableConfig] = None,
        **kwargs: Any,
    ) -> Any:
        async with AsyncACPClient(configuration=self.clientConfig) as acp_client:
            thread_id = self._get_thread_id(config)
            run_output = None

            if thread_id is not None:
                if thread_id in self.previous_thread_run:
                    run_output = self.previous_thread_run.get(thread_id, None)
                else:
                    run_create = RunCreateStateful(
                        agent_id=self.agent_id,
                        input=self._extract_input(state),
                        config=Config(configurable=self._extract_config(config)),
                    )
                    run_output = await acp_client.create_and_wait_for_thread_run_output(thread_id, run_create)
            else:
                run_create = RunCreateStateless(
                    agent_id=self.agent_id,
                    input=self._extract_input(state),
                    config=Config(configurable=self._extract_config(config)),
                )
                run_output = await acp_client.create_and_wait_for_stateless_run_output(
                    run_create
                )

            while isinstance(run_output.output.actual_instance, RunInterrupt):
                interrupt_result = self._handle_interrupt(
                    config=config, run_output=run_output, thread_id=thread_id
                )

                resume_run = await acp_client.resume_stateless_run(
                    run_id=run_output.run.run_id, body=interrupt_result
                )
                run_output = await acp_client.wait_for_stateless_run_output(
                    run_id=resume_run.run_id
                )
        state = self._handle_run_output(state, run_output.output)

    def __call__(self, state, config):
        return RunnableCallable(self.invoke, self.ainvoke)
