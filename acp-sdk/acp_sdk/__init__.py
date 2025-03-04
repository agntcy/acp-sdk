# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
from typing import Literal

type ACPSpecVersion = Literal["0.1"]
CurrentACPSpecVersion = Literal["0.1"]

from .v0_1.acp_client.api import AgentsApi, RunsApi, ThreadsApi
from .v0_1.acp_client.api_client import *
from .v0_1.acp_client.api_response import *

class ACPClient(AgentsApi, RunsApi, ThreadsApi):
    def __init__(self, api_client=None):
        super().__init__(api_client)