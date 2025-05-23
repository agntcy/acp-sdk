# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import json
from os import getenv
from pathlib import Path
from typing import Dict, List, Optional, Union
from pydantic import BaseModel
import yaml

from .acp_v0.configuration import Configuration
from .acp_v0.async_client.api import AgentsApi as AsyncAgentsApi
from .acp_v0.async_client.api import StatelessRunsApi as AsyncStatelessRunsApi
from .acp_v0.async_client.api import ThreadRunsApi as AsyncThreadRunsApi
from .acp_v0.async_client.api import ThreadsApi as AsyncThreadsApi
from .acp_v0.async_client.api_client import ApiClient as AsyncApiClient
from .acp_v0.configuration import ServerVariablesT
from .acp_v0.sync_client.api import (
    AgentsApi,
    StatelessRunsApi,
    ThreadRunsApi,
    ThreadsApi,
)
from .acp_v0.sync_client.api_client import ApiClient
from .agws_v0.models import AgentACPSpec, AgentManifest

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader


__ENV_VAR_SPECIAL_CHAR_TABLE = str.maketrans("-.", "__")


def _get_envvar_param(prefix: str, varname: str) -> Optional[str]:
    env_varname = prefix + varname.upper()
    return getenv(env_varname.translate(__ENV_VAR_SPECIAL_CHAR_TABLE), None)


class ApiClientConfiguration(Configuration,BaseModel):
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
    :param timeout: Int, float for total timeout number of seconds or tuple of
      both for (connect, read) timeouts.
    :param ca_cert_data: verify the peer using concatenated CA certificate data
      in PEM (str) or DER (bytes) format.
    :param debug: Debug switch.

    """

    def __init__(
        self,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        timeout: Optional[Union[List[Union[int,float]],int,float]] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ):
        super().__init__(
            host,
            api_key,
            api_key_prefix,
            username,
            password,
            access_token,
            None,
            server_variables,
            None,
            server_operation_variables,
            True,
            ssl_ca_cert,
            retries,
            timeout,
            ca_cert_data,
            debug=debug,
        )

    @classmethod
    def fromEnvPrefix(
        cls,
        env_var_prefix: str,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        timeout: Optional[Union[List[Union[int,float]],int,float]] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> "ApiClientConfiguration":
        """Construct a configuration object using environment variables as
        default source of parameter values. For example, with env_var_prefix="MY\\_",
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
        if timeout is None:
            str_value = _get_envvar_param(prefix, "timeout")
            if str_value is not None:
                timeout = json.loads(str_value)
        if ca_cert_data is None:
            str_value = _get_envvar_param(prefix, "ca_cert_data")
            if str_value is not None:
                ca_cert_data = str_value
        if debug is None:
            str_value = _get_envvar_param(prefix, "debug")
            if str_value is not None:
                debug = str_value.lower() == "true"

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
            timeout,
            ca_cert_data,
            debug=debug,
        )


class ACPClient(AgentsApi, StatelessRunsApi, ThreadsApi, ThreadRunsApi):
    """Client for ACP API."""

    def __init__(
        self,
        api_client: Optional[ApiClient] = None,
        configuration: Optional[ApiClientConfiguration] = None,
        manifest: Optional[Union[str, Path, AgentManifest, AgentACPSpec]] = None,
        stream_chunk_size: int = 4096,
    ):
        if api_client is None and configuration is not None:
            api_client = ApiClient(configuration)
        super().__init__(api_client)
        self.__workflow_server_update_api_client()
        self.stream_chunk_size = stream_chunk_size

        if isinstance(manifest, AgentManifest):
            self.agent_acp_spec = manifest.specs
        elif isinstance(manifest, AgentACPSpec):
            self.agent_acp_spec = manifest
        elif manifest is not None:
            with open(manifest, "r") as mfh:
                manifest_data = yaml.load(mfh, Loader=SafeLoader)
                self.agent_acp_spec = AgentManifest.model_validate(manifest_data).specs
        else:
            self.agent_acp_spec = None

    def __workflow_server_update_api_client(self):
        if self.api_client.configuration.api_key is not None:
            # Check for 'x-api-key' config and move to header.
            try:
                self.api_client.default_headers["x-api-key"] = (
                    self.api_client.configuration.api_key["x-api-key"]
                )
            except KeyError:
                pass  # ignore

    # Convenience functions to use this client as an sync context manager.
    def __enter__(self):
        self.api_client.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.api_client.__exit__(exc_type, exc_value, traceback)

    # Convenience functions to generate from config.
    @classmethod
    def fromEnvPrefix(
        cls,
        env_var_prefix: str,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        timeout: Optional[Union[List[Union[int,float]],int,float]] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> "ACPClient":
        """Construct an ACPClient object using environment variables as
        default source of the API client configuration values. For example,
        with env_var_prefix="MY\\_", the default host parameter value would be
        looked up in the "MY_HOST" environment variable if not provided.

        :param env_var_prefix: String used as prefix for environment variable
          names.

        :return: ACP client object
        :rtype: ACPClient
        """
        client_config = ApiClientConfiguration.fromEnvPrefix(
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
            timeout,
            ca_cert_data,
            debug=debug,
        )
        return ACPClient(api_client=ApiClient(client_config))

    @classmethod
    def fromConfiguration(
        cls,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        timeout: Optional[Union[List[Union[int,float]],int,float]] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> "ACPClient":
        """Construct an ACPClient object using configuration values. For example,
        with env_var_prefix="MY\\_", the default host parameter value would be
        looked up in the "MY_HOST" environment variable if not provided.

        :param env_var_prefix: String used as prefix for environment variable
          names.

        :return: ACP client object
        :rtype: ACPClient
        """
        client_config = ApiClientConfiguration(
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
            timeout,
            ca_cert_data,
            debug=debug,
        )
        return ACPClient(api_client=ApiClient(client_config))


class AsyncACPClient(
    AsyncAgentsApi, AsyncStatelessRunsApi, AsyncThreadsApi, AsyncThreadRunsApi
):
    """Async client for ACP API."""

    def __init__(
        self,
        api_client: Optional[AsyncApiClient] = None,
        configuration: Optional[ApiClientConfiguration] = None,
        manifest: Optional[Union[str, Path, AgentManifest, AgentACPSpec]] = None,
        stream_chunk_size: int = 4096,
    ):
        if api_client is None and configuration is not None:
            api_client = AsyncApiClient(configuration)
        super().__init__(api_client)
        self.__workflow_server_update_api_client()
        self.stream_chunk_size = stream_chunk_size
        self.manifest = manifest
        self.agent_acp_spec = None

    def __workflow_server_update_api_client(self):
        if self.api_client.configuration.api_key is not None:
            # Check for 'x-api-key' config and move to header.
            try:
                self.api_client.default_headers["x-api-key"] = (
                    self.api_client.configuration.api_key["x-api-key"]
                )
            except KeyError:
                pass  # ignore

    async def _get_agent_acp_spec(self) -> Optional[AgentACPSpec]:
        if self.agent_acp_spec is not None:
            return self.agent_acp_spec
        elif self.manifest is None:
            return None
        elif isinstance(self.manifest, AgentManifest):
            self.agent_acp_spec = self.manifest.specs
        elif isinstance(self.manifest, AgentACPSpec):
            self.agent_acp_spec = self.manifest
        else:
            import aiofiles

            async with aiofiles.open(self.manifest, "r") as mfh:
                raw_data = await mfh.read()
                manifest_data = yaml.load(raw_data, Loader=SafeLoader)
                self.agent_acp_spec = AgentManifest.model_validate(manifest_data).specs
            return self.agent_acp_spec

    # Convenience functions to use this client as an async context manager.
    async def __aenter__(self):
        await self.api_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.api_client.__aexit__(exc_type, exc_value, traceback)

    # Convenience functions to generate from config.
    @classmethod
    def fromEnvPrefix(
        cls,
        env_var_prefix: str,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        timeout: Optional[Union[List[Union[int,float]],int,float]] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> "AsyncACPClient":
        """Construct an AsyncACPClient object using environment variables as
        default source of the API client configuration values. For example,
        with env_var_prefix="MY\\_", the default host parameter value would be
        looked up in the "MY_HOST" environment variable if not provided.

        :param env_var_prefix: String used as prefix for environment variable
          names.

        :return: Async ACP client object
        :rtype: AsyncACPClient
        """
        client_config = ApiClientConfiguration.fromEnvPrefix(
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
            timeout,
            ca_cert_data,
            debug=debug,
        )
        return AsyncACPClient(api_client=AsyncApiClient(client_config))

    @classmethod
    def fromConfiguration(
        cls,
        host: Optional[str] = None,
        api_key: Optional[Dict[str, str]] = None,
        api_key_prefix: Optional[Dict[str, str]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_token: Optional[str] = None,
        server_variables: Optional[ServerVariablesT] = None,
        server_operation_variables: Optional[Dict[int, ServerVariablesT]] = None,
        ssl_ca_cert: Optional[str] = None,
        retries: Optional[int] = None,
        timeout: Optional[Union[List[Union[int,float]],int,float]] = None,
        ca_cert_data: Optional[Union[str, bytes]] = None,
        *,
        debug: Optional[bool] = None,
    ) -> "AsyncACPClient":
        """Construct an AsyncACPClient object using configuration values. For example,
        with env_var_prefix="MY\\_", the default host parameter value would be
        looked up in the "MY_HOST" environment variable if not provided.

        :param env_var_prefix: String used as prefix for environment variable
          names.

        :return: Async ACP client object
        :rtype: AsyncACPClient
        """
        client_config = ApiClientConfiguration(
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
            timeout,
            ca_cert_data,
            debug=debug,
        )
        return AsyncACPClient(api_client=AsyncApiClient(client_config))
