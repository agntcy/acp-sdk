# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import os
import asyncio
from marketing_campaign.app import graph
from marketing_campaign.state import OverallState, ConfigModel
from marketing_campaign import mailcomposer
from marketing_campaign.email_reviewer import TargetAudience
from agntcy_acp import AsyncACPClient, AsyncApiClient, ApiClientConfiguration
from agntcy_acp.models import (
    RunCreateStateless,
    RunResult,
    RunOutput,
    RunError,
    RunInterrupt,
    Config,
)


async def main():
    print("What marketing campaign do you want to create?")
    inputState = OverallState(
        messages=[],
        operation_logs=[],
        has_composer_completed=False
    )

    marketing_campaign_id = os.environ.get("MARKETING_CAMPAIGN_ID", "")
    client_config = ApiClientConfiguration.fromEnvPrefix("MARKETING_CAMPAIGN_")

    api_client = AsyncApiClient(configuration=client_config)
    acp_client = AsyncACPClient(api_client=api_client)

    while True:
        usermsg = input("YOU [Type OK when you are happy with the email proposed] >>> ")
        inputState.messages.append(mailcomposer.Message(content=usermsg, type=mailcomposer.Type.human))
        run_create = RunCreateStateless(
            agent_id=marketing_campaign_id,
            input=inputState.model_dump(),
            config=Config(configurable=ConfigModel(
                recipient_email_address=os.environ["RECIPIENT_EMAIL_ADDRESS"],
                sender_email_address=os.environ["SENDER_EMAIL_ADDRESS"],
                target_audience=TargetAudience.academic
            ).model_dump())
        )
        run_output = await acp_client.create_and_wait_for_stateless_run_output(run_create)
        if isinstance(run_output.actual_instance, RunResult):
            run_result: RunResult = run_output.actual_instance
        elif isinstance(run_output.actual_instance, RunError):
            run_error: RunError = run_output.actual_instance
            raise Exception(f"Run Failed: {run_error}")
        else:
            raise Exception(f"ACP Server returned a unsupported response: {run_output}")

        outputState = OverallState.model_validate(run_result.values)
        if len(outputState.operation_logs) > 0:
            print(outputState.operation_logs)
            break
        else:
            print(outputState.messages[-1].content)
        inputState = outputState


if __name__ == "__main__":
    asyncio.run(main())
