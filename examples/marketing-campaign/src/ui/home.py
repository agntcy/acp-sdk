import asyncio
import json
import os
import re
import subprocess
import sys
import time
from urllib.parse import urlparse

import gradio as gr
from marketing_campaign import mailcomposer
from marketing_campaign.email_reviewer import TargetAudience
from marketing_campaign.state import ConfigModel, OverallState

from agntcy_acp import ApiClientConfiguration, AsyncACPClient
from agntcy_acp.acp_v0.async_client.api_client import ApiClient as AsyncApiClient
from agntcy_acp.models import (
    Config,
    RunCreateStateless,
    RunError,
    RunResult,
)

overall_state = OverallState(
    messages=[], operation_logs=[], has_composer_completed=False
)
client_config = None

os.environ["RECIPIENT_EMAIL_ADDRESS"] = ""
os.environ["SENDER_EMAIL_ADDRESS"] = ""
PATH_TO_WFSM = "/Users/reginaldocosta/workspace/workflow-srv-mgr/wfsm"
PATH_TO_WFS = "/Users/reginaldocosta/workspace/workflow-srv"


def run_make_commands(path, command):
    """Runs make commands for each project and updates PATH, showing logs."""
    try:
        # Change the directory to the project path
        os.chdir(path)

        if command == "export_path":
            os.environ["PATH"] += os.pathsep + path + "/build"
        else:

            # Execute the make command and capture the output

            process = subprocess.Popen(
                command.split(),
                stdout=subprocess.PIPE,
                stderr=sys.stderr,
                text=True,  # Important for string output
                bufsize=1,  # line buffered
            )

            # stdout, stderr = process.communicate()
            r = 0
            while process.poll() is None:
                line = process.stdout.readline()
                if line:
                    sys.stdout.write(line)
                    sys.stdout.flush()

                time.sleep(0.1)

                match = re.search(
                    r"Agent ID:\s*([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})",
                    line,
                )

                if match:
                    agent_id = match.group(1).lstrip().strip()
                    os.environ["MARKETING_CAMPAIGN_ID"] = str(agent_id)

                #
                match_2 = re.search(
                    r"API Key:\s*([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})",
                    line,
                )

                if match_2:
                    api_key = match_2.group(1).lstrip().strip()
                    api_key = str(api_key)
                    os.environ["MARKETING_CAMPAIGN_API_KEY"] = json.dumps(
                        {"x-api-key": api_key}
                    )
                url_pattern = r"listening for ACP request on: (https?://[^\s\x1b]+)"

                acp_url_match = re.search(url_pattern, line)
                if acp_url_match:
                    acp_url = acp_url_match.group(1)
                    the_url = acp_url.strip()

                    parsed_url = urlparse(the_url)
                    if parsed_url.scheme and parsed_url.netloc:

                        os.environ["MARKETING_CAMPAIGN_HOST"] = str(the_url)
                    else:
                        print("invalid url")
                    print(
                        "Environment variable MARKETING_CAMPAIGN_HOST is set to:",
                        os.environ["MARKETING_CAMPAIGN_HOST"],
                    )

                start_campaign = re.search(r"Uvicorn running on", line)
                if start_campaign:
                    r += 1
                    if r == 3:
                        sys.stdout.write("Done")
                        sys.stdout.flush()
                        return True

        logs = "/n done"
        result_message = (
            "Make command executed successfully and executable moved to path."
        )
        return result_message, logs
    except subprocess.CalledProcessError as e:
        error_logs = f"An error occurred: {e}\n{e.stderr}"
        return error_logs, error_logs


def generate_config_interface(
    components_paths,
):
    """Creates the configuration interface."""

    for i, path in enumerate(components_paths):
        curr_commands = path["commands"]

        for command in curr_commands:
            run_make_commands(path["path"], command)


async def chat_with_bot(api_client, message, history):
    marketing_campaign_id = os.environ.get("MARKETING_CAMPAIGN_ID", "")

    global overall_state
    overall_state.messages.append(
        mailcomposer.Message(content=message, type=mailcomposer.Type.human)
    )

    run_create = RunCreateStateless(
        agent_id=marketing_campaign_id,
        input=overall_state.model_dump(),
        config=Config(
            configurable=ConfigModel(
                recipient_email_address=os.environ["RECIPIENT_EMAIL_ADDRESS"],
                sender_email_address=os.environ["SENDER_EMAIL_ADDRESS"],
                target_audience=TargetAudience.academic,
            ).model_dump()
        ),
    )

    # async with AsyncApiClient(configuration=client_config) as api_client:
    acp_client = AsyncACPClient(api_client=api_client)
    run_output = None

    run_output = await acp_client.create_and_wait_for_stateless_run_output(run_create)

    if run_output.output is None:
        raise Exception("Run output is None")
    actual_output = run_output.output.actual_instance

    if isinstance(actual_output, RunResult):
        run_result: RunResult = actual_output

    elif isinstance(actual_output, RunError):
        run_error: RunError = actual_output
        raise Exception(f"Run Failed: {run_error}")

    else:
        raise Exception(f"ACP Server returned a unsupported response: {run_output}")

    runState = run_result.values  # type: ignore
    outputState = OverallState.model_validate(runState)

    if len(outputState.operation_logs) > 0:
        print(outputState.operation_logs)
    else:
        print(outputState.messages[-1].content)
        history.append({"content": outputState.messages[-1].content, "role": "system"})

    overall_state = outputState


async def gradio_ui():
    path = os.path.abspath(os.getcwd())

    ioa_components_paths = [
        {
            "path": PATH_TO_WFSM,
            "name": "Worflow Server Manager",
            "commands": ["make build", "cd build && chmod +x wfsm", "export_path"],
        },
        {
            "name": "Workflow Server",
            "path": PATH_TO_WFS,
            "commands": [
                "git submodule update --init --recursive",
                "make docker-build-dev",
            ],
        },
        {
            "name": None,
            "path": path,
            "commands": [
                "wfsm deploy -m ./deploy/marketing-campaign.json -e ./deploy/marketing_campaign_example.yaml -b workflowserver:latest"
            ],
        },
    ]

    generate_config_interface(ioa_components_paths)

    # with gr.Blocks() as acp_demo:
    #     with gr.Sidebar(open=True, width=450, position="right"):
    client_config = ApiClientConfiguration.fromEnvPrefix("MARKETING_CAMPAIGN_")
    api_client = AsyncApiClient(configuration=client_config)

    global overall_state

    async with api_client:

        async def response(message, chat_history):
            chat_history.append({"role": "user", "content": message})
            await chat_with_bot(api_client, message=message, history=chat_history)
            yield chat_history

        demo = gr.ChatInterface(response, title="LangGraph Chat", type="messages")

        demo.launch(server_port=7861)


if __name__ == "__main__":
    asyncio.run(gradio_ui())
