from app import graph
import state
from state import OverallState
from langchain_openai.chat_models.azure import AzureChatOpenAI
import mailcomposer


def get_azure():
    return AzureChatOpenAI(
        model="gpt-4o-mini",
        api_version="2024-07-01-preview",
        seed=42,
        temperature=0,
    )


def main():
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
                    sender_email_address="casey.agntcy.demo@gmail.com",
                    target_audience="business"
                ).model_dump(),
            }
        })
        outputState = OverallState.model_validate(output)
        if len(outputState.operation_logs) > 0:
            print(outputState.operation_logs)
            break
        else:
            print(outputState.messages[-1].content)
        inputState = outputState


main()
