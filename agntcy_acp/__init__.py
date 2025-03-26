# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import json
from os import getenv
from typing import Optional, Any, Dict, Union

from .acp_v0.sync_client.api_client import ApiClient
from .acp_v0.sync_client.api import AgentsApi, ThreadsApi, StatelessRunsApi, ThreadRunsApi
from .acp_v0.async_client.api import AgentsApi as AsyncAgentsApi
from .acp_v0.async_client.api import StatelessRunsApi as AsyncStatelessRunsApi
from .acp_v0.async_client.api import ThreadsApi as AsyncThreadsApi
from .acp_v0.async_client.api import ThreadRunsApi as AsyncThreadRunsApi
from .acp_v0.async_client.api_client import ApiClient as AsyncApiClient
from .acp_v0 import ApiResponse
from .acp_v0 import Configuration
from .acp_v0.configuration import ServerVariablesT
from .acp_v0.spec_version import VERSION as ACP_VERSION
from .acp_v0.spec_version import MAJOR_VERSION as ACP_MAJOR_VERSION
from .acp_v0.spec_version import MINOR_VERSION as ACP_MINOR_VERSION
from .agws_v0.spec_version import VERSION as AGWS_VERSION
from .agws_v0.spec_version import MAJOR_VERSION as AGWS_MAJOR_VERSION
from .agws_v0.spec_version import MINOR_VERSION as AGWS_MINOR_VERSION
from .exceptions import ACPDescriptorValidationException, ACPRunException
from agntcy_acp.acp_v0.exceptions import (
    OpenApiException, 
    ApiTypeError,
    ApiValueError,
    ApiKeyError,
    ApiAttributeError,
    ApiException,
    BadRequestException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
    ServiceException,
    ConflictException,
    UnprocessableEntityException,
)

class ACPClient(AgentsApi, StatelessRunsApi, ThreadsApi, ThreadRunsApi):
    """Client for ACP API.
    """
    def __init__(self, api_client: Optional[ApiClient] = None):
        super().__init__(api_client)
        self.__workflow_server_update_api_client()

    def __workflow_server_update_api_client(self):
        if self.api_client.configuration.api_key is not None:
            # Check for 'x-api-key' config and move to header.
            try:
                self.api_client.default_headers['x-api-key'] = self.api_client.configuration.api_key['x-api-key']
            except KeyError:
                pass # ignore

class AsyncACPClient(AsyncAgentsApi, AsyncStatelessRunsApi, AsyncThreadsApi, AsyncThreadRunsApi):
    """Async client for ACP API.
    """
    def __init__(self, api_client: Optional[AsyncApiClient] = None):
        super().__init__(api_client)
        self.__workflow_server_update_api_client()
    
    def __workflow_server_update_api_client(self):
        if self.api_client.configuration.api_key is not None:
            # Check for 'x-api-key' config and move to header.
            try:
                self.api_client.default_headers['x-api-key'] = self.api_client.configuration.api_key['x-api-key']
            except KeyError:
                pass # ignore

__ENV_VAR_SPECIAL_CHAR_TABLE = str.maketrans("-.", "__")

def _get_envvar_param(prefix: str, varname: str) -> Optional[str]:
    env_varname = prefix + varname.upper()
    return getenv(env_varname.translate(__ENV_VAR_SPECIAL_CHAR_TABLE), None)

class ApiClientConfiguration(Configuration):
    """This class contains various settings of the API client.

    :param host: Base url.
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer).
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication.
    :param password: Password for HTTP basic authentication.
    :param access_token: Access token.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum
      values before.
    :param ssl_ca_cert: str - the path to a file of concatenated CA certificates
      in PEM format.
    :param retries: Number of retries for API requests.
    :param ca_cert_data: verify the peer using concatenated CA certificate data
      in PEM (str) or DER (bytes) format.
    :param debug: Debug switch.

    """
    def __init__(
        self, 
        host: Optional[str]=None,
        api_key: Optional[Dict[str, str]]=None,
        api_key_prefix: Optional[Dict[str, str]]=None,
        username: Optional[str]=None,
        password: Optional[str]=None,
        access_token: Optional[str]=None,
        server_variables: Optional[ServerVariablesT]=None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]]=None,
        ssl_ca_cert: Optional[str]=None,
        retries: Optional[int] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ):
        super().__init__(host, api_key, api_key_prefix, username, password, 
                         access_token, None, server_variables, 
                         None, server_operation_variables, 
                         True, ssl_ca_cert, retries, 
                         ca_cert_data, debug=debug)
    
    @classmethod
    def fromEnvPrefix(
        cls,
        env_var_prefix: str,
        host: Optional[str]=None,
        api_key: Optional[Dict[str, str]]=None,
        api_key_prefix: Optional[Dict[str, str]]=None,
        username: Optional[str]=None,
        password: Optional[str]=None,
        access_token: Optional[str]=None,
        server_variables: Optional[ServerVariablesT]=None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]]=None,
        ssl_ca_cert: Optional[str]=None,
        retries: Optional[int] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> "ApiClientConfiguration":
        """Construct a configuration object using environment variables as
        default source of parameter values. For example, with env_var_prefix="MY_", 
        the default host parameter value would be looked up in the "MY_HOST" 
        environment variable if not provided.

        :param env_var_prefix: String used as prefix for environment variable 
        names.

        :return: Configuration object
        :rtype: ApiClientConfiguration
        """
        prefix = env_var_prefix.upper()

        if host is None:
            host = _get_envvar_param(prefix, "host")
            # Workflow server uses "endpoint"
            if host is None:
                host = _get_envvar_param(prefix, "endpoint")
        if api_key is None:
            str_value = _get_envvar_param(prefix, "api_key")
            if str_value is not None:
                api_key = json.loads(str_value)
        if api_key_prefix is None:
            str_value = _get_envvar_param(prefix, "api_key_prefix")
            if str_value is not None:
                api_key_prefix = json.loads(str_value)
        if username is None:
            username = _get_envvar_param(prefix, "username")
        if password is None:
            password = _get_envvar_param(prefix, "password")
        if access_token is None:
            access_token = _get_envvar_param(prefix, "access_token")
        if server_variables is None:
            str_value = _get_envvar_param(prefix, "server_variables")
            if str_value is not None:
                server_variables = json.loads(str_value)
        if server_operation_variables is None:
            str_value = _get_envvar_param(prefix, "server_operation_variables")
            if str_value is not None:
                server_operation_variables = json.loads(str_value)
        if ssl_ca_cert is None:
            ssl_ca_cert = _get_envvar_param(prefix, "ssl_ca_cert")
        if retries is None:
            str_value = _get_envvar_param(prefix, "retries")
            if str_value is not None:
                retries = int(str_value)
        if ca_cert_data is None:
            str_value = _get_envvar_param(prefix, "ca_cert_data")
            if str_value is not None:
                ca_cert_data = str_value
        if debug is None:
            str_value = _get_envvar_param(prefix, "debug")
            if str_value is not None:
                debug = str_value.lower() == 'true'

        return ApiClientConfiguration(
            host,
            api_key, 
            api_key_prefix,
            username,
            password,
            access_token,
            server_variables, 
            server_operation_variables, 
            ssl_ca_cert,
            retries, 
            ca_cert_data,
            debug=debug,
        )

__all__ = [
    "ACPClient",
    "AsyncACPClient",
    "ApiClientConfiguration",
    "ApiResponse",
    "ACPDescriptorValidationException",
    "ACPRunException",
    "OpenApiException", 
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "BadRequestException",
    "NotFoundException",
    "UnauthorizedException",
    "ForbiddenException",
    "ServiceException",
    "ConflictException",
    "UnprocessableEntityException",
    "ACP_VERSION",
    "ACP_MAJOR_VERSION",
    "ACP_MINOR_VERSION",
    "AGWS_VERSION",
    "AGWS_MINOR_VERSION",
    "AGWS_MAJOR_VERSION",
]
