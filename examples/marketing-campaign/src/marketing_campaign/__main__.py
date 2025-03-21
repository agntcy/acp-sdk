from marketing_campaign.app import graph
from marketing_campaign.state import OverallState, ConfigModel
from marketing_campaign import mailcomposer
from marketing_campaign.email_reviewer import TargetAudience


def main():
    print("What marketing campaign do you want to create?")
    inputState = OverallState(
        messages=[],
        operation_logs=[],
        has_composer_completed=False
    )
    while True:
        usermsg = input("YOU [Type OK when you are happy with the email proposed] >>> ")
        inputState.messages.append(mailcomposer.Message(content=usermsg, type=mailcomposer.Type.human))
        output = graph.invoke(inputState, {
            "configurable": {
                "thread_id": "foo",
                "config": ConfigModel(
                    recipient_email_address="Giovanni Conte <giconte@cisco.com>",
                    sender_email_address="casey.agntcy.demo@gmail.com",
                    target_audience=TargetAudience.academic
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
