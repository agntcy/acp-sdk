# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
from typing import Literal

type ACPSpecVersion = Literal["0.1"]
CurrentACPSpecVersion = Literal["0.1"]

from .v0 import AgentsApi, RunsApi, ThreadsApi, AsyncAgentsApi, AsyncRunsApi, AsyncThreadsApi, ApiResponse, Configuration, ApiClient, AsyncApiClient

class ACPClient(AgentsApi, RunsApi, ThreadsApi):
    def __init__(self, api_client: ApiClient | None = None):
        super().__init__(api_client)

class AsyncACPClient(AsyncAgentsApi, AsyncRunsApi, AsyncThreadsApi):
    def __init__(self, api_client: AsyncApiClient | None = None):
        super().__init__(api_client)