# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
from typing import Literal

type ACPSpecVersion = Literal["0.1"]
CurrentACPSpecVersion = Literal["0.1"]

from .v0.acp_client.api import AgentsApi, RunsApi, ThreadsApi
from .v0.acp_client import ApiClient
from .v0.acp_async_client.api import AgentsApi as AsyncAgentsApi
from .v0.acp_async_client.api import RunsApi as AsyncRunsApi
from .v0.acp_async_client.api import ThreadsApi as AsyncThreadsApi
from .v0.acp_async_client import ApiClient as AsyncApiClient
from .v0 import ApiResponse, Configuration
from .v0.spec_version import ACP_VERSION, ACP_MAJOR_VERSION, ACP_MINOR_VERSION

class ACPClient(AgentsApi, RunsApi, ThreadsApi):
    def __init__(self, api_client: ApiClient | None = None):
        super().__init__(api_client)

class AsyncACPClient(AsyncAgentsApi, AsyncRunsApi, AsyncThreadsApi):
    def __init__(self, api_client: AsyncApiClient | None = None):
        super().__init__(api_client)
