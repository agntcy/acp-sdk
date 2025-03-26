# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from agntcy_acp import AsyncACPClient, ApiClientConfiguration, AsyncApiClient
from agntcy_acp.models import RunSearchRequest, RunCreateStateless

async def test_acp_client_stateless_runs_api(mock_async_api_client, default_api_key, default_agent_id):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})

    async with AsyncApiClient(config) as api_client:
        client = AsyncACPClient(api_client)

        response = await client.create_stateless_run(run_create_stateless=RunCreateStateless(agent_id=default_agent_id))
        assert response is not None
        run_id = response.run_id

        response = await client.get_stateless_run(run_id)
        assert response is not None

        response = await client.wait_for_stateless_run_output(run_id)
        assert response is not None

        response = await client.stream_stateless_run_output(run_id)
        assert response is not None

        response = await client.resume_stateless_run(run_id, {})
        assert response is not None

        response = await client.search_stateless_runs(RunSearchRequest(agent_id=default_agent_id))
        assert response is not None

        response = await client.delete_stateless_run(run_id)
        assert response is not None
