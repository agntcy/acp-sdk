import os

from acp_sdk.langgraph.api_bridge import APIBridgeAgentNode
from acp_sdk.langgraph.io_mapper import add_io_mapped_edge, add_io_mapped_conditional_edge
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
import mailcomposer
import email_reviewer
import state
from acp_sdk.langgraph.acp_node import ACPNode
from acp_sdk.acp_v0.configuration import Configuration
from langchain_core.runnables.graph import MermaidDrawMethod
from langchain_core.runnables import RunnableConfig
import sendgrid


def process_inputs(state: state.OverallState, config: RunnableConfig) -> state.OverallState:
    user_message = state.messages[-1].content
    configurable = config.get('configurable', {})
    state.recipient_email_address = configurable.get('config', {}).get('recipient_email_address', '')
    state.sender_email_address = config.get('configurable', {}).get('config', {}).get('sender_email_address', '')
    state.target_audience = config.get('configurable', {}).get('config', {}).get('target_audience', '')
    if user_message.upper() == "OK":
        state.has_composer_completed = True
    else:
        state.has_composer_completed = False

    return state


def check_final_email(state: state.OverallState):
    return "done" if (state.mailcomposer_state
                      and state.mailcomposer_state.output
                      and state.mailcomposer_state.output.final_email
                      ) else "user"

def check_email_review(state: state.OverallState) -> str:
    return "done" if (state.email_reviewer_state
        and state.email_reviewer_state.output
        and state.email_reviewer_state.output.correct
        ) else "user"

def build_graph() -> CompiledStateGraph:
    # Fill in client configuration for the remote agent
    mailcomposer_host = os.environ.get("MAILCOMPOSER_HOST")
    mailcomposer_api_key = os.environ.get("MAILCOMPOSER_API_KEY", None)
    mailcomposer_agent_id = os.environ.get("MAILCOMPOSER_AGENT_ID", "")
    email_reviewer_host = os.environ.get("EMAIL_REVIEWER_HOST")
    email_reviewer_api_key = os.environ.get("EMAIL_REVIEWER_API_KEY", None)
    email_reviewer_agent_id = os.environ.get("EMAIL_REVIEWER_AGENT_ID", "")

    mailcomposer_client_config = Configuration(
        api_key={"apiKey": mailcomposer_api_key} if mailcomposer_api_key else None,
        host=mailcomposer_host
    )

    acp_mailcomposer = ACPNode(
        name="mailcomposer",
        agent_id=mailcomposer_agent_id,
        client_config=mailcomposer_client_config,
        input_path="mailcomposer_state.input",
        input_type=mailcomposer.InputSchema,
        output_path="mailcomposer_state.output",
        output_type=mailcomposer.OutputSchema
    )

    email_reviewer_config = Configuration(
        api_key={"apiKey": email_reviewer_api_key} if email_reviewer_api_key else None,
        host=email_reviewer_host
    )

    acp_email_reviewer = ACPNode(
        name="email_reviewer",
        agent_id=email_reviewer_agent_id,
        client_config=email_reviewer_config,
        input_path="email_reviewer_state.input",
        input_type=email_reviewer.InputSchema,
        output_path="email_reviewer_state.output",
        output_type=email_reviewer.OutputSchema
    )

    sendgrid_api_key = os.environ.get("SENDGRID_API_KEY")
    if sendgrid_api_key is None:
        raise ValueError("SENDGRID_API_KEY environment variable is not set")

    send_email = APIBridgeAgentNode(
        name="sendgrid",
        input_path="sendgrid_state.input",
        input_type=sendgrid.InputSchema,
        output_path="sendgrid_state.output",
        output_type=sendgrid.OutputSchema,
        service_api_key=sendgrid_api_key,
        hostname="http://localhost:8080",
        service_name="sendgrid/v3/mail/send"
    )

    sg = StateGraph(state.OverallState)

    sg.add_node("process_inputs", process_inputs)
    sg.add_node(acp_mailcomposer)
    sg.add_node(acp_email_reviewer)
    sg.add_node(send_email)

    sg.add_edge(START, "process_inputs")

    add_io_mapped_edge(
        sg,
        start="process_inputs",
        end=acp_mailcomposer,
        iomapper_config={
            "input_fields": ["messages", "has_composer_completed"]
        }
    )

    add_io_mapped_conditional_edge(
        sg,
        start=acp_mailcomposer,
        path=check_final_email,
        iomapper_config_map={
            "done": {
                "end": acp_email_reviewer,
                "metadata": {
                    "input_fields": ["mailcomposer_state.output.final_email", "target_audience"]
                }
            },
            "user": {
                "end": END,
                "metadata": {
                    "output_fields": ["messages", "operation_logs"],
                }
            }
        }
    )

    add_io_mapped_conditional_edge(
        sg,
        start=acp_email_reviewer,
        path=check_email_review,
        iomapper_config_map={
            "done": {
                "end": send_email,
                "metadata": {
                    "input_fields": ["sender_email_address", "recipient_email_address",
                                     "email_reviewer_state.output.email"]                }
            },
            "user": {
                "end": END,
                "metadata": {
                    "output_fields": ["messages", "operation_logs"],
                }
            }
        }
    )

    # Add edge between send_email and END with an io_mapper between them
    add_io_mapped_edge(
        sg,
        start=send_email,
        end=END,
        iomapper_config={
            "output_fields": ["operation_logs"],
        })

    g = sg.compile()
    g.name = "Marketing Campaign Manager"
    # print(g.get_graph().draw_mermaid())
    with open("___graph.png", "wb") as f:
        f.write(g.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API,
        ))
    return g


graph = build_graph()
