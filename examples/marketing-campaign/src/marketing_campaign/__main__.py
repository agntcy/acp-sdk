from agntcy_iomapper.langgraph import LangGraphIOMapperConfig

from maa import graph
from src.marketing_campaign.sdk import ACPState
from state import InputState, OutputState, State
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

    maa_input = State(description="Advertise a new pair of shoes")
    output:OutputState = graph.invoke(maa_input, {"configurable": {"thread_id": "foo", "llm": get_azure()}})

    print(output)



main()