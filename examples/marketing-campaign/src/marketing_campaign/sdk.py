from agntcy_iomapper.base import ArgumentsDescription
from pydantic import BaseModel, Field

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from typing_extensions import TypedDict, Union
from typing import Any, Dict
from pydantic import create_model
from agntcy_iomapper.langgraph import create_langraph_iomapper, LangGraphIOMapperConfig, LangGraphIOMapperInput, LangGraphIOMapperOutput
import mailcomposer

class IOMapperIntenalState(TypedDict):
    input: LangGraphIOMapperInput
    output: LangGraphIOMapperOutput

class ACPState(BaseModel):
    acp: Dict[str, Any] = {}


def extract_acp_state(state, default={}):
    """

    :param state:
    :param default:
    :return:
    """
    acp_key = list(ACPState.model_fields.keys())[0]
    return state.get(acp_key, default) if isinstance(state, dict) else getattr(state, acp_key, default)

class ACPNode():
    def __init__(self, name: str, inputModel: BaseModel, outputModel: BaseModel, nodeState=None, statekey: str = None,
                 client=None):
        self.client = client
        self.name = name
        self.nodeState = nodeState
        self.inputModel = inputModel
        self.outputModel = outputModel
        self.statekey = statekey
        if not statekey: self.statekey = f"{self.name}_statekey"

    def __call__(self, graph_state: Any) -> Any:
        acpstate = extract_acp_state(graph_state, {})
        inputdata = acpstate.get(self.statekey, {}).get("input", {})

        if inputdata == {}:
            raise Exception(f"Unable to extract input for node {self.name} from state {graph_state}")

        if self.client:
            pass
        else:
            acpstate[self.statekey]["output"] = mailcomposer.Output(
                final_email=inputdata.messages[-1].content
            )
        return graph_state

def _extractField(state, path):
    field_instances=[]
    cmodel = type(state)
    field_instance = state
    for e in path.split('/'):
        f = cmodel.__fields__.get(e, None)
        cmodel = f.annotation
        if field_instance is not None:
            field_instance = getattr(field_instance, e)
        field_instances.append(field_instance)
    return e, f, field_instances

class ACPIOMapper():
    def __init__(self, name: str, config: LangGraphIOMapperConfig, inputs:[str], outputs:[str]):
        self.inputs = inputs
        self.outputs= outputs
        self.name = name
        self.name = name
        # todo: message template

        self.iomapper = create_langraph_iomapper(config)

    def __call__(self, graph_state: Any)->Any:
        inputfields = [_extractField(graph_state, input) for input in self.inputs]
        outputfields = [_extractField(graph_state, output) for output in self.outputs]

        inputState = create_model(
            f"{self.name}_iomapper_model_input",
            __base__=BaseModel,
            **{
                f[0]: (f[1].annotation, f[1]) for f in inputfields
            }
        )
        outputState = create_model(
            f"{self.name}_iomapper_model_output",
            __base__=BaseModel,
            **{
                f[0]: (f[1].annotation, f[1]) for f in outputfields
            }
        )

        self.statemodel = create_model(
            f"{self.name}_iomapper_model",
            __base__=BaseModel,
            input=(inputState, None),
            output=(outputState, None)
        )
        iomapperInput = LangGraphIOMapperInput(
            input=ArgumentsDescription(json_schema=inputState.model_json_schema()),
            output=ArgumentsDescription(json_schema=outputState.model_json_schema()),
            data=inputState.model_construct(None,
                                             **{
                                                f[0]: f[2][-1] for f in inputfields
                                             })
        )

        s = self.iomapper.invoke({"input": iomapperInput})
        s['output'].data['input']['messages'][0]['type']='human'
        for f in outputfields:
           out_instance = f[1].annotation.model_validate(s['output'].data['input'])
           setattr(f[2][-2], f[0], out_instance)

        j = graph_state.model_dump_json()
        print(j)

        t = type(graph_state)(
            operation_logs=graph_state.operation_logs,
            description=graph_state.description,
            mc_statekey=type(graph_state.mc_statekey)(
                input=mailcomposer.Input(messages=[HumanMessage(graph_state.description)], is_completed=True),
                output=mailcomposer.Output(final_email="test")
            )
        )
        jj = t.model_dump_json()
        print(jj)
        gg = graph_state.model_validate_json(jj)
        g = graph_state.model_validate_json(j)
        return g

class ACPContext():

    def __init__(self):
        self.nodes = {}

    def create_acp_node(self, name: str, inputModel: Any, outputModel: Any, statekey: str = None):
        nodeState = create_model(
            f"{name}_state_model",
            __base__=BaseModel,
            input=(inputModel, None),
            output=(outputModel, None),
        )
        # Instantiate ACP client
        self.nodes[name] = ACPNode(name=name, nodeState=nodeState, inputModel=inputModel, outputModel=outputModel, statekey=statekey)
        return self.nodes[name]


    def build_lg_state(self, statemodel):
        self.updated_state_model = create_model(
            f"{statemodel.__name__}_acp",
            __base__=statemodel,
            **{
                n.statekey: (n.nodeState, n.nodeState()) for n in self.nodes.values()
            }
        )
        return self.updated_state_model

