# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from agntcy_acp import ACPClient, ApiClientConfiguration, ApiClient
from agntcy_acp.models import RunSearchRequest, RunCreateStateless

def test_acp_client_stateless_runs_api(mock_sync_api_client, default_api_key, default_agent_id):
    config = ApiClientConfiguration(retries=2, api_key={"x-api-key": default_api_key})

    with ApiClient(config) as api_client:
        client = ACPClient(api_client)

        response = client.create_stateless_run(run_create_stateless=RunCreateStateless(agent_id=default_agent_id))
        assert response is not None
        run_id = response.run_id

        response = client.get_stateless_run(run_id)
        assert response is not None

        response = client.wait_for_stateless_run_output(run_id)
        assert response is not None

        response = client.stream_stateless_run_output(run_id)
        assert response is not None

        response = client.resume_stateless_run(run_id, {})
        assert response is not None

        response = client.search_stateless_runs(RunSearchRequest(agent_id=default_agent_id))
        assert response is not None

        response = client.delete_stateless_run(run_id)
        assert response is not None
