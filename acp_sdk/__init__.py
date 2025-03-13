# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
from typing import Literal

type ACPSpecVersion = Literal["0.1"]
CurrentACPSpecVersion = Literal["0.1"]

from .acp_v0.sync_client.api import AgentsApi, RunsApi, ThreadsApi
from .acp_v0.sync_client import ApiClient
from .acp_v0.async_client.api import AgentsApi as AsyncAgentsApi
from .acp_v0.async_client.api import RunsApi as AsyncRunsApi
from .acp_v0.async_client.api import ThreadsApi as AsyncThreadsApi
from .acp_v0.async_client import ApiClient as AsyncApiClient
from .acp_v0 import ApiResponse, Configuration
from .acp_v0.spec_version import ACP_VERSION, ACP_MAJOR_VERSION, ACP_MINOR_VERSION

class ACPClient(AgentsApi, RunsApi, ThreadsApi):
    def __init__(self, api_client: ApiClient | None = None):
        super().__init__(api_client)

class AsyncACPClient(AsyncAgentsApi, AsyncRunsApi, AsyncThreadsApi):
    def __init__(self, api_client: AsyncApiClient | None = None):
        super().__init__(api_client)
