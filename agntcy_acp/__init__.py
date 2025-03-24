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

__ENV_VAR_SPECIAL_CHAR_TABLE = str.maketrans("-.", "__")

def _get_envvar_param(prefix: str, varname: str, cur_value: Any) -> Optional[str]:
    if cur_value is not None:
        return cur_value
    else:
        env_varname = prefix + varname.upper()
        return getenv(env_varname.translate(__ENV_VAR_SPECIAL_CHAR_TABLE), None)

class ApiClientConfiguration(Configuration):
    """ This class represents general configurable parameters for an ACP client.
    """

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
        """
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
        """
        super().__init__(host, api_key, api_key_prefix, username, password, 
                         access_token, None, server_variables, 
                         None, server_operation_variables, 
                         True, ssl_ca_cert, retries, 
                         ca_cert_data, debug=debug)
    
    @classmethod
    def fromEnvPrefix(
        cls,
        env_var_prefix: str,
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
        """
        Generate a ApiClientConfiguration using environment variables for values if
        they are not supplied to the function as an argument. Environment variables
        are searched for each parameter by prefixing the "env_var_prefix" value to the
        parameter name to generate the relevant environment variable name.

        :param env_var_prefix: Environment variable prefix for generating environment
        variable from parameters. For example, with env_var_prefix="MY_", the method
        will look for "host" parameter in the "MY_HOST" environment variable if it is
        not provided as an argument to the function.
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

        :return: The configuration object.
        """
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

class ACPClient(AgentsApi, RunsApi, ThreadsApi):
    """ This class sync methods for the different endpoints of the Agent Connect
    Protocol API.
    """
    def __init__(self, api_client: ApiClient | None = None):
        super().__init__(api_client)
    
    @classmethod
    def fromConfiguration(
        cls,
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
    ) -> "ACPClient":
        """
        Generate a :class:`ACPClient` from configuration.

        :param env_var_prefix: Environment variable prefix for generating environment
        variable from parameters. For example, with env_var_prefix="MY_", the method
        will look for "host" parameter in the "MY_HOST" environment variable if it is
        not provided as an argument to the function.
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

        :return: The :class:`ACPClient` object.
        """
        config = ApiClientConfiguration(
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
            debug = debug,
        )
        return ACPClient(ApiClient(config))
    
    @classmethod
    def fromEnvPrefix(
        cls,
        env_var_prefix: str,
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
    ) -> "ACPClient":
        """
        Generate a :class:`ACPClient` using environment variables for values if
        they are not supplied to the function as an argument. Environment variables
        are searched for each parameter by prefixing the "env_var_prefix" value to the
        parameter name to generate the relevant environment variable name.

        :param env_var_prefix: Environment variable prefix for generating environment
        variable from parameters. For example, with env_var_prefix="MY_", the method
        will look for "host" parameter in the "MY_HOST" environment variable if it is
        not provided as an argument to the function.
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

        :return: The :class:`ACPClient` object.
        """
        config = ApiClientConfiguration.fromEnvPrefix(
            env_var_prefix,
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
            debug = debug,
        )
        return ACPClient(ApiClient(config))

class AsyncACPClient(AsyncAgentsApi, AsyncRunsApi, AsyncThreadsApi):
    """ This class async methods for the different endpoints of the Agent Connect
    Protocol API.
    """
    def __init__(self, api_client: AsyncApiClient | None = None):
        super().__init__(api_client)

    @classmethod
    def fromConfiguration(
        cls,
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
    ) -> "AsyncACPClient":
        """
        Generate a :class:`AsyncACPClient` from configuration.

        :param env_var_prefix: Environment variable prefix for generating environment
        variable from parameters. For example, with env_var_prefix="MY_", the method
        will look for "host" parameter in the "MY_HOST" environment variable if it is
        not provided as an argument to the function.
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

        :return: The :class:`AsyncACPClient` object.
        """
        config = ApiClientConfiguration(
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
            debug = debug,
        )
        return AsyncACPClient(AsyncApiClient(config))
    
    @classmethod
    def fromEnvPrefix(
        cls,
        env_var_prefix: str,
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
    ) -> "AsyncACPClient":
        """
        Generate a :class:`AsyncACPClient` using environment variables for values if
        they are not supplied to the function as an argument. Environment variables
        are searched for each parameter by prefixing the "env_var_prefix" value to the
        parameter name to generate the relevant environment variable name.

        :param env_var_prefix: Environment variable prefix for generating environment
        variable from parameters. For example, with env_var_prefix="MY_", the method
        will look for "host" parameter in the "MY_HOST" environment variable if it is
        not provided as an argument to the function.
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

        :return: The :class:`AsyncACPClient` object.
        """
        config = ApiClientConfiguration.fromEnvPrefix(
            env_var_prefix,
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
            debug = debug,
        )
        return AsyncACPClient(AsyncApiClient(config))

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
