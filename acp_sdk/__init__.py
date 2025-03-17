# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
from .acp_v0.sync_client.api import AgentsApi, RunsApi, ThreadsApi
from .acp_v0.sync_client import ApiClient
from .acp_v0.async_client.api import AgentsApi as AsyncAgentsApi
from .acp_v0.async_client.api import RunsApi as AsyncRunsApi
from .acp_v0.async_client.api import ThreadsApi as AsyncThreadsApi
from .acp_v0.async_client import ApiClient as AsyncApiClient
from .acp_v0 import ApiResponse
from .acp_v0 import Configuration
from .acp_v0.spec_version import ACP_VERSION, ACP_MAJOR_VERSION, ACP_MINOR_VERSION

class ACPClient(AgentsApi, RunsApi, ThreadsApi):
    def __init__(self, api_client: ApiClient | None = None):
        super().__init__(api_client)

class AsyncACPClient(AsyncAgentsApi, AsyncRunsApi, AsyncThreadsApi):
    def __init__(self, api_client: AsyncApiClient | None = None):
        super().__init__(api_client)

class ApiClientConfiguration(Configuration):
    def __init__(
        self, 
        host = None, 
        api_key = None, 
        api_key_prefix = None, 
        username = None, 
        password = None, 
        access_token = None, 
        server_index = None, 
        server_variables = None, 
        server_operation_index = None, 
        server_operation_variables = None, 
        ignore_operation_servers = False, 
        ssl_ca_cert = None, 
        retries = None, 
        ca_cert_data = None, 
        *, 
        debug = None,
    ):
        super().__init__(host, api_key, api_key_prefix, username, password, 
                         access_token, server_index, server_variables, 
                         server_operation_index, server_operation_variables, 
                         ignore_operation_servers, ssl_ca_cert, retries, 
                         ca_cert_data, debug=debug)

__all__ = [
    "ACPClient",
    "AsyncACPClient",
    "ApiClientConfiguration",
    "ApiResponse",
    "ACP_VERSION",
    "ACP_MAJOR_VERSION",
    "ACP_MINOR_VERSION",
]
