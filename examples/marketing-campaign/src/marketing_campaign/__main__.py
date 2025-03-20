from agntcy_acp.models import AgentRef, AgentMetadata

from app import graph
import state
from marketing_campaign.state import MailComposerState
from state import OverallState, ConfigModel
from dotenv import load_dotenv, find_dotenv
import mailcomposer



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
                "config": state.ConfigModel(
                    recipient_email_address="Alessandro Duminuco <aduminuc@cisco.com>",
                    sender_email_address="casey.agntcy.demo@gmail.com",
                    target_audience="academic"
                ).model_dump(),
            }
        })


        # TODO : FIX this!
        mcstate = output.get("mailcomposer_state", None)
        sgstate = output.get("sendgrid_state", None)
        output["mailcomposer_state"] = None
        output["sendgrid_state"] = None
        outputState = OverallState.model_validate(output)
        outputState.mailcomposer_state = mcstate
        outputState.sendgrid_state = sgstate
        if len(outputState.operation_logs) > 0:
            print(outputState.operation_logs)
            break
        else:
            print(outputState.messages[-1].content)
        inputState = outputState



main()
