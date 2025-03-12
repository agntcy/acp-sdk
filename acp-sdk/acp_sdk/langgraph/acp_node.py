from pydantic import BaseModel

from typing import Any, Dict
from typing_extensions import TypedDict
from langchain_core.runnables import RunnableConfig
from langgraph.utils.runnable import RunnableCallable
from acp_sdk import ACPClient, ApiClient, AsyncACPClient, AsyncApiClient, Configuration
from acp_sdk.models import RunCreate, Run, RunResult

INPUT_KEY = "input"
OUTPUT_KEY = "output"

class BaseModelACPState(BaseModel):
    """
    Class that holds the state section for all the ACP nodes in a langgraph graph.
    This must be included in the overall graph state when that is defined as a BaseModel.
    """
    acp__: Dict[str, Any] = {}

class TypedDictAcpState(TypedDict):
    """
    Class that holds the state section for all the ACP nodes in a langgraph graph.
    This must be included in the overall graph state when that is defined as a TypedDict.
    """
    acp__: Dict[str, Any] = {}

def _extract_acp_state(state, default={})-> Dict[str, Any]:
    """
    internal helper to extract the acp section of the state from the overall state

    :param state: overall langgraph state
    :param default: default value to return in case the state cannot be extracted
    :return: the ACP sub-state extracted from the overall state.
    """
    acp_key = list(BaseModelACPState.model_fields.keys())[0]
    return state.get(acp_key, default) if isinstance(state, dict) else getattr(state, acp_key, default)

class ACPNode():

    def __init__(self, name:str, inputModel, outputModel, clientConfig:Configuration, agentConfig):
        """
        Instantiate a Langgraph node encapsulating a remote ACP agent
        :param name: Name of the node in the langgraph graph. It is also used as a key in the state to hold agent input and output
        :param inputModel: Schema of the agent input model
        :param outputModel: Schema of the agent output model
        """
        self.name = name
        self.inputModel = inputModel
        self.outputModel = outputModel
        self.clientConfig = clientConfig
        self.agentConfig = agentConfig

    def __extract_input(self, state: Any):
        acp_state = _extract_acp_state(state)
        acp_input = acp_state.get(self.name, {}).get(INPUT_KEY, None)

        if acp_input is None:
            raise Exception(f"ERROR in ACP Node {self.name}. Unable to extract input from state {state}")

        return acp_state, acp_input

    def __set_output(self, acp_state: Any, output: Any):
        acp_state[self.name][OUTPUT_KEY] = output


    def invoke(self, state: Any, config: RunnableConfig)->Any:
        acp_state, acp_input = self.__extract_input(state)

        api_client = ApiClient(configuration=self.clientConfig)
        acp_client = ACPClient(api_client=api_client)

        # TODO: Merge config with runnable config

        run_create = RunCreate(
            agent_id="pippo",
            input=acp_input.model_dump(),
            config=self.agentConfig
        )
        run: Run = acp_client.create_run(run_create)

        # Block and wait
        run_output = acp_client.get_run_output(run_id=run.run_id, block_timeout=120)
        if isinstance(run_output.actual_instance, RunResult):
            run_result:RunResult = run_output.actual_instance
            self.__set_output(acp_state, self.outputModel.model_validate(run_result.result))
        else:
            pass
            # TODO: handle other cases

        return state

    async def ainvoke(self, state: Any, config: RunnableConfig)->Any:
        acp_state, acp_input = self.__extract_input(state)

        api_client = AsyncApiClient(configuration=self.clientConfig)
        acp_client = AsyncACPClient(api_client=api_client)

        # TODO: Merge config with runnable config
        run: Run = acp_client.create_run(RunCreate(input=acp_input, config=self.agentConfig))

        # Block and wait
        output = acp_client.get_run_output(run_id=run.run_id, block_timeout=120)

        self.__set_output(acp_state, output)
        return state

    def as_runnable(self)->RunnableCallable:
        return RunnableCallable(self.invoke, self.ainvoke)

