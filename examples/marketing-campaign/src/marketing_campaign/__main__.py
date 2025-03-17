from codecs import namereplace_errors

from acp_sdk.acp_v0.models.agent_ref import AgentRef
from acp_sdk.acp_v0.models.agent_metadata import AgentMetadata

from app import graph
import state
from state import InputState, OutputState, OverallState, ConfigModel
from langchain_openai.chat_models.azure import AzureChatOpenAI
from dotenv import load_dotenv, find_dotenv
from acp_sdk.descriptor import generator
import mailcomposer




def get_azure():
    return AzureChatOpenAI(
        model="gpt-4o-mini",
        api_version="2024-07-01-preview",
        seed=42,
        temperature=0,
    )


def main():
    load_dotenv(dotenv_path=find_dotenv(usecwd=True))
    agent_metadata = AgentMetadata(
    ref=AgentRef(name="org.agntcy.marketing-campaign", version="0.0.1"),
    description="Offer a chat interface to compose an email for a marketing campaign. Final output is the email that could be used for the campaign")
    generator.generate_agent_descriptor(agent_metadata, InputState, OutputState, ConfigModel, "___test.json")


    #agent_metadata = AgentMetadata(
    #ref=AgentRef(name="org.agntcy.apibridge.sendgrid", version="0.0.1"),
    #description="Offer a natural language interface based on api bridge agent to send emails through sendgrid")
    #generator.generate_agent_descriptor(agent_metadata, state.SendGridInput, state.SendGridOutput, ConfigModel, "sendgrid.json")

    print("What marketing campaign do you want to create?")
    inputState = OverallState(
        messages=[],
        operation_logs=[],
        has_composer_completed=False,
        recipient_email_address="",
        sender_email_address=""
    )
    while True:
        usermsg = input()
        inputState.messages.append(mailcomposer.Message(content=usermsg, type=mailcomposer.Type.human))
        output = graph.invoke(inputState, {
            "configurable": {
                    "thread_id": "foo",
                    "llm": get_azure(),
                    "config": state.ConfigModel(
                        recipient_email_address="Alessandro Duminuco <aduminuc@cisco.com>",
                        sender_email_address="casey.agntcy.demo@gmail.com"
                    ).model_dump(),
            }
        })
        outputState = OverallState.model_validate(output)
        if len(outputState.operation_logs)>0:
            print(outputState.operation_logs)
            break
        else: print(outputState.messages[-1].content)
        inputState = outputState



main()