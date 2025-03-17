# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
from os import getenv
from typing import Optional, Any

from .acp_v0.sync_client import ApiClient, AgentsApi, RunsApi, ThreadsApi
from .acp_v0.async_client import AgentsApi as AsyncAgentsApi
from .acp_v0.async_client import RunsApi as AsyncRunsApi
from .acp_v0.async_client import ThreadsApi as AsyncThreadsApi
from .acp_v0.async_client import ApiClient as AsyncApiClient
from .acp_v0 import ApiResponse
from .acp_v0 import Configuration
from .acp_v0.spec_version import VERSION as ACP_VERSION
from .acp_v0.spec_version import MAJOR_VERSION as ACP_MAJOR_VERSION
from .acp_v0.spec_version import MINOR_VERSION as ACP_MINOR_VERSION
from .agws_v0.spec_version import VERSION as AGWS_VERSION
from .agws_v0.spec_version import MAJOR_VERSION as AGWS_MAJOR_VERSION
from .agws_v0.spec_version import MINOR_VERSION as AGWS_MINOR_VERSION

class ACPClient(AgentsApi, RunsApi, ThreadsApi):
    def __init__(self, api_client: ApiClient | None = None):
        super().__init__(api_client)

class AsyncACPClient(AsyncAgentsApi, AsyncRunsApi, AsyncThreadsApi):
    def __init__(self, api_client: AsyncApiClient | None = None):
        super().__init__(api_client)

__ENV_VAR_SPECIAL_CHAR_TABLE = str.maketrans("-.", "__")

def _get_envvar_param(prefix: str, varname: str, cur_value: Any) -> Optional[str]:
    if cur_value is not None:
        return cur_value
    else:
        env_varname = prefix + varname.upper()
        return getenv(env_varname.translate(__ENV_VAR_SPECIAL_CHAR_TABLE), None)

class ApiClientConfiguration(Configuration):
    def __init__(
        self, 
        host = None, 
        api_key = None, 
        api_key_prefix = None, 
        username = None, 
        password = None, 
        access_token = None, 
        server_variables = None, 
        server_operation_variables = None, 
        ssl_ca_cert = None, 
        retries = None, 
        ca_cert_data = None, 
        *, 
        debug = None,
    ):
        super().__init__(host, api_key, api_key_prefix, username, password, 
                         access_token, None, server_variables, 
                         None, server_operation_variables, 
                         True, ssl_ca_cert, retries, 
                         ca_cert_data, debug=debug)
    
    @classmethod
    def fromEnv(
        cls,
        env_var_prefix,
        host = None, 
        api_key = None, 
        api_key_prefix = None, 
        username = None, 
        password = None, 
        access_token = None, 
        server_variables = None, 
        server_operation_variables = None, 
        ssl_ca_cert = None, 
        retries = None, 
        ca_cert_data = None, 
        *, 
        debug = None,
    ) -> "ApiClientConfiguration":
        prefix = env_var_prefix.upper()
        return ApiClientConfiguration(
            _get_envvar_param(prefix, "host", host),
            _get_envvar_param(prefix, "api_key", api_key), 
            _get_envvar_param(prefix, "api_key_prefix", api_key_prefix),
            _get_envvar_param(prefix, "username", username),
            _get_envvar_param(prefix, "password", password),
            _get_envvar_param(prefix, "access_token", access_token),
            _get_envvar_param(prefix, "server_variables", server_variables), 
            _get_envvar_param(prefix, "server_operation_variables", server_operation_variables), 
            _get_envvar_param(prefix, "ssl_ca_cert", ssl_ca_cert),
            _get_envvar_param(prefix, "retries", retries), 
            _get_envvar_param(prefix, "ca_cert_data", ca_cert_data),
            debug=_get_envvar_param(prefix, "debug", debug),
        )

__all__ = [
    "ACPClient",
    "AsyncACPClient",
    "ApiClientConfiguration",
    "ApiResponse",
    "ACP_VERSION",
    "ACP_MAJOR_VERSION",
    "ACP_MINOR_VERSION",
    "AGWS_VERSION",
    "AGWS_MINOR_VERSION",
    "AGWS_MAJOR_VERSION",
]
