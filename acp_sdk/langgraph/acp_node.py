from pydantic import BaseModel, Field

from typing import Any
from langchain_core.runnables import RunnableConfig
from langgraph.utils.runnable import RunnableCallable
from acp_sdk import ACPClient, ApiClient, AsyncACPClient, AsyncApiClient, Configuration
from acp_sdk.models import RunCreate, Run, RunResult


class ACPNode():

    def __init__(self, name: str, inputPath: str, inputType, outputPath: str, outputType, clientConfig: Configuration,
                 agentConfig):
        """
        Instantiate a Langgraph node encapsulating a remote ACP agent
        :param name: Name of the node in the langgraph graph. It is also used as a key in the state to hold agent input and output
        :param inputModel: Schema of the agent input model
        :param outputModel: Schema of the agent output model
        """
        self.__name__ = name
        self.inputPath = inputPath
        self.inputType = inputType
        self.outputType = outputType
        self.outputPath = outputPath
        self.clientConfig = clientConfig
        self.agentConfig = agentConfig

    def get_name(self):
        return self.__name__

    def _extract_input(self, state: Any):
        acp_input = state
        for el in self.inputPath.split("."):
            acp_input = getattr(acp_input, el)
        # acp_input = acp_state.get(self.name, {}).get(INPUT_KEY, None)

        if acp_input is None:
            raise Exception(f"ERROR in ACP Node {self.name}. Unable to extract input from state {state}")

        return acp_input

    def _set_output(self, state: Any, output: Any):
        outputParent = state
        for el in self.outputPath.split(".")[:-1]:
            outputParent = getattr(outputParent, el)
        setattr(outputParent, self.outputPath.split(".")[-1], self.outputType.model_validate(output))

    def invoke(self, state: Any, config: RunnableConfig) -> Any:
        acp_input = self._extract_input(state)

        api_client = ApiClient(configuration=self.clientConfig)
        acp_client = ACPClient(api_client=api_client)

        # TODO: Merge config with runnable config

        run_create = RunCreate(
            agent_id="pippo",
            input=acp_input.model_dump(),
            config=self.agentConfig.model_dump()
        )
        run: Run = acp_client.create_run(run_create)

        # Block and wait
        run_output = acp_client.get_run_output(run_id=run.run_id, block_timeout=120)
        if isinstance(run_output.actual_instance, RunResult):
            run_result: RunResult = run_output.actual_instance
            self._set_output(state, run_result.result)
        else:
            pass
            # TODO: handle other cases

        return state

    async def ainvoke(self, state: Any, config: RunnableConfig) -> Any:
        acp_state, acp_input = self._extract_input(state)

        api_client = AsyncApiClient(configuration=self.clientConfig)
        acp_client = AsyncACPClient(api_client=api_client)

        # TODO: Merge config with runnable config
        run: Run = acp_client.create_run(RunCreate(input=acp_input, config=self.agentConfig))

        # Block and wait
        output = acp_client.get_run_output(run_id=run.run_id, block_timeout=120)

        self._set_output(acp_state, output)
        return state

    def __call__(self, state, config):
        return RunnableCallable(self.invoke, self.ainvoke)

