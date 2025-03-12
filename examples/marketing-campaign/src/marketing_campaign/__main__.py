from agntcy_iomapper.langgraph import LangGraphIOMapperConfig
from langchain_core.messages import HumanMessage

from maa import graph
from src.marketing_campaign.sdk import ACPState
from state import InputState, OutputState, OverallState
from langchain_openai.chat_models.azure import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv



def get_azure():
    return AzureChatOpenAI(
        model="gpt-4o-mini",
        api_version="2024-07-01-preview",
        seed=42,
        temperature=0,
    )

def main():
    load_dotenv(dotenv_path=find_dotenv(usecwd=True))

    print("What marketing campaign do you want to create?")
    inputState = OverallState(messages=[])
    while True:
        usermsg = input()
        inputState.messages.append(HumanMessage(usermsg))
        output = graph.invoke(inputState, {"configurable": {"thread_id": "foo", "llm": get_azure()}})
        outputState = OverallState.model_validate(output)
        if len(outputState.operation_logs)>0:
            print(outputState.operation_logs)
            break
        else: print(outputState.messages[-1].content)
        inputState = outputState



main()