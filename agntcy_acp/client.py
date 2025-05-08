# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import json
from pydantic import BaseModel
from typing import Optional, Any, Dict, Union, Callable
from os import getenv
from pathlib import Path
import yaml

from .acp_v0 import Configuration
from .acp_v0.configuration import ServerVariablesT
from .acp_v0.sync_client.api_client import ApiClient
from .acp_v0.sync_client.api import AgentsApi, ThreadsApi, StatelessRunsApi, ThreadRunsApi
from .acp_v0.async_client.api import ThreadsApi as AsyncThreadsApi
from .acp_v0.async_client.api import ThreadRunsApi as AsyncThreadRunsApi
from .acp_v0.async_client.api_client import ApiClient as AsyncApiClient
from .agws_v0.models import AgentManifest, AgentACPSpec
from .acp_v0.async_client.api import AgentsApi as AsyncAgentsApi
from .acp_v0.async_client.api import StatelessRunsApi as AsyncStatelessRunsApi

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

# Import authorization components if available
try:
    from .auth import AuthorizationMiddleware, PermissionDeniedError
except ImportError:
    # Create stub classes if auth module is not available
    class AuthorizationMiddleware:
        def __init__(self, *args, **kwargs):
            pass
        def authorize(self, *args, **kwargs):
            pass
    class PermissionDeniedError(Exception):
        pass

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


class ACPClient(AgentsApi, StatelessRunsApi, ThreadsApi, ThreadRunsApi):
    """Client for ACP API.
    """
    def __init__(
            self,
            api_client: Optional[ApiClient] = None,
            configuration: Optional[ApiClientConfiguration] = None,
            manifest: Optional[Union[str,Path,AgentManifest,AgentACPSpec]] = None,
            stream_chunk_size: int = 4096,
            auth_middleware: Optional[AuthorizationMiddleware] = None,
            user_id_header: str = "X-User-ID"
        ):
        if api_client is None and configuration is not None:
            api_client = ApiClient(configuration)
        super().__init__(api_client)
        self.__workflow_server_update_api_client()
        self.stream_chunk_size = stream_chunk_size
        self.auth_middleware = auth_middleware
        self.user_id_header = user_id_header
        
        if isinstance(manifest, AgentManifest):
            self.agent_acp_spec = manifest.specs
        elif isinstance(manifest, AgentACPSpec):
            self.agent_acp_spec = manifest
        elif manifest is not None:
            with open(manifest, 'r') as mfh:
                manifest_data = yaml.load(mfh, Loader=SafeLoader)
                self.agent_acp_spec = AgentManifest.model_validate(manifest_data).specs
        else:
            self.agent_acp_spec = None

    def __workflow_server_update_api_client(self):
        if self.api_client.configuration.api_key is not None:
            # Check for 'x-api-key' config and move to header.
            try:
                self.api_client.default_headers['x-api-key'] = self.api_client.configuration.api_key['x-api-key']
            except KeyError:
                pass # ignore

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
    ) -> "ACPClient":
        """Construct an ACPClient object using environment variables as
        default source of the API client configuration values. For example, 
        with env_var_prefix="MY_", the default host parameter value would be 
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
            ca_cert_data,
            debug=debug,
        )
        return ACPClient(api_client=ApiClient(client_config))

    @classmethod
    def fromConfiguration(
        cls,
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
    ) -> "ACPClient":
        """Construct an ACPClient object using configuration values. For example, 
        with env_var_prefix="MY_", the default host parameter value would be 
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
            ca_cert_data,
            debug=debug,
        )
        return ACPClient(api_client=ApiClient(client_config))

    def set_auth_middleware(self, middleware: AuthorizationMiddleware) -> None:
        """Set the authorization middleware for permission checking.
        
        Args:
            middleware: The authorization middleware to use
        """
        self.auth_middleware = middleware
    
    def set_user_id(self, user_id: str) -> None:
        """Set the user ID for all subsequent requests.
        
        Args:
            user_id: The user ID to use for authorization
        """
        if not self.api_client.default_headers:
            self.api_client.default_headers = {}
        self.api_client.default_headers[self.user_id_header] = user_id
    
    def get_user_id(self) -> Optional[str]:
        """Get the current user ID from headers.
        
        Returns:
            The current user ID or None if not set
        """
        if not self.api_client.default_headers:
            return None
        return self.api_client.default_headers.get(self.user_id_header)
    
    def _authorize(self, agent_id: str, action: str, resource_id: Optional[str] = None, 
                  metadata: Optional[Dict[str, Any]] = None) -> None:
        """Check authorization for an action.
        
        Args:
            agent_id: The ID of the agent being accessed
            action: The action being performed
            resource_id: Optional ID of the specific resource
            metadata: Additional context for authorization
            
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if not self.auth_middleware:
            return
        
        user_id = self.get_user_id()
        if not user_id:
            raise ValueError("User ID not set. Call set_user_id() before making requests.")
        
        self.auth_middleware.authorize(
            user_id=user_id,
            agent_id=agent_id,
            action=action,
            resource_id=resource_id,
            metadata=metadata
        )
    
    # Override API methods to add authorization
    
    def create_stateless_run(self, **kwargs):
        """Create a stateless agent run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        agent_id = kwargs.get("agent_id")
        if agent_id and self.auth_middleware:
            self._authorize(agent_id=agent_id, action="create_stateless_run")
        return super().create_stateless_run(**kwargs)
    
    def get_stateless_run(self, run_id, **kwargs):
        """Get a stateless run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            # We don't know the agent_id here, so use the run_id as resource
            self._authorize(agent_id="*", action="get_stateless_run", resource_id=run_id)
        return super().get_stateless_run(run_id, **kwargs)
    
    def create_thread(self, **kwargs):
        """Create a thread with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            self._authorize(agent_id="*", action="create_thread")
        return super().create_thread(**kwargs)
    
    def get_thread(self, thread_id, **kwargs):
        """Get a thread with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            self._authorize(agent_id="*", action="get_thread", resource_id=thread_id)
        return super().get_thread(thread_id, **kwargs)
    
    def create_thread_run(self, thread_id, **kwargs):
        """Create a thread run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        agent_id = kwargs.get("agent_id")
        if self.auth_middleware:
            self._authorize(
                agent_id=agent_id or "*", 
                action="create_thread_run", 
                resource_id=thread_id
            )
        return super().create_thread_run(thread_id, **kwargs)
    
    def get_thread_run(self, thread_id, run_id, **kwargs):
        """Get a thread run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            self._authorize(
                agent_id="*", 
                action="get_thread_run", 
                resource_id=f"{thread_id}/{run_id}"
            )
        return super().get_thread_run(thread_id, run_id, **kwargs)


class AsyncACPClient(AsyncAgentsApi, AsyncStatelessRunsApi, AsyncThreadsApi, AsyncThreadRunsApi):
    """Async client for ACP API.
    """
    def __init__(
            self,
            api_client: Optional[AsyncApiClient] = None,
            configuration: Optional[ApiClientConfiguration] = None,
            manifest: Optional[Union[str,Path,AgentManifest,AgentACPSpec]] = None,
            stream_chunk_size: int = 4096,
            auth_middleware: Optional[AuthorizationMiddleware] = None,
            user_id_header: str = "X-User-ID"
        ):
        if api_client is None and configuration is not None:
            api_client = AsyncApiClient(configuration)
        super().__init__(api_client)
        self.__workflow_server_update_api_client()
        self.stream_chunk_size = stream_chunk_size
        self.manifest = manifest
        self.agent_acp_spec = None
        self.auth_middleware = auth_middleware
        self.user_id_header = user_id_header
    
    def __workflow_server_update_api_client(self):
        if self.api_client.configuration.api_key is not None:
            # Check for 'x-api-key' config and move to header.
            try:
                self.api_client.default_headers['x-api-key'] = self.api_client.configuration.api_key['x-api-key']
            except KeyError:
                pass # ignore

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
            async with aiofiles.open(self.manifest, 'r') as mfh:
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
    ) -> "AsyncACPClient":
        """Construct an AsyncACPClient object using environment variables as
        default source of the API client configuration values. For example, 
        with env_var_prefix="MY_", the default host parameter value would be 
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
            ca_cert_data,
            debug=debug,
        )
        return AsyncACPClient(api_client=AsyncApiClient(client_config))

    @classmethod
    def fromConfiguration(
        cls,
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
    ) -> "AsyncACPClient":
        """Construct an AsyncACPClient object using configuration values. For example, 
        with env_var_prefix="MY_", the default host parameter value would be 
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
            ca_cert_data,
            debug=debug,
        )
        return AsyncACPClient(api_client=AsyncApiClient(client_config))

    def set_auth_middleware(self, middleware: AuthorizationMiddleware) -> None:
        """Set the authorization middleware for permission checking.
        
        Args:
            middleware: The authorization middleware to use
        """
        self.auth_middleware = middleware
    
    def set_user_id(self, user_id: str) -> None:
        """Set the user ID for all subsequent requests.
        
        Args:
            user_id: The user ID to use for authorization
        """
        if not self.api_client.default_headers:
            self.api_client.default_headers = {}
        self.api_client.default_headers[self.user_id_header] = user_id
    
    def get_user_id(self) -> Optional[str]:
        """Get the current user ID from headers.
        
        Returns:
            The current user ID or None if not set
        """
        if not self.api_client.default_headers:
            return None
        return self.api_client.default_headers.get(self.user_id_header)
    
    async def _authorize(self, agent_id: str, action: str, resource_id: Optional[str] = None, 
                  metadata: Optional[Dict[str, Any]] = None) -> None:
        """Check authorization for an action.
        
        Args:
            agent_id: The ID of the agent being accessed
            action: The action being performed
            resource_id: Optional ID of the specific resource
            metadata: Additional context for authorization
            
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if not self.auth_middleware:
            return
        
        user_id = self.get_user_id()
        if not user_id:
            raise ValueError("User ID not set. Call set_user_id() before making requests.")
        
        self.auth_middleware.authorize(
            user_id=user_id,
            agent_id=agent_id,
            action=action,
            resource_id=resource_id,
            metadata=metadata
        )
    
    # Override API methods to add authorization
    
    async def create_stateless_run(self, **kwargs):
        """Create a stateless agent run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        agent_id = kwargs.get("agent_id")
        if agent_id and self.auth_middleware:
            await self._authorize(agent_id=agent_id, action="create_stateless_run")
        return await super().create_stateless_run(**kwargs)
    
    async def get_stateless_run(self, run_id, **kwargs):
        """Get a stateless run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            # We don't know the agent_id here, so use the run_id as resource
            await self._authorize(agent_id="*", action="get_stateless_run", resource_id=run_id)
        return await super().get_stateless_run(run_id, **kwargs)
    
    async def create_thread(self, **kwargs):
        """Create a thread with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            await self._authorize(agent_id="*", action="create_thread")
        return await super().create_thread(**kwargs)
    
    async def get_thread(self, thread_id, **kwargs):
        """Get a thread with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            await self._authorize(agent_id="*", action="get_thread", resource_id=thread_id)
        return await super().get_thread(thread_id, **kwargs)
    
    async def create_thread_run(self, thread_id, **kwargs):
        """Create a thread run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        agent_id = kwargs.get("agent_id")
        if self.auth_middleware:
            await self._authorize(
                agent_id=agent_id or "*", 
                action="create_thread_run", 
                resource_id=thread_id
            )
        return await super().create_thread_run(thread_id, **kwargs)
    
    async def get_thread_run(self, thread_id, run_id, **kwargs):
        """Get a thread run with authorization.
        
        Raises:
            PermissionDeniedError: If the user does not have permission
        """
        if self.auth_middleware:
            await self._authorize(
                agent_id="*", 
                action="get_thread_run", 
                resource_id=f"{thread_id}/{run_id}"
            )
        return await super().get_thread_run(thread_id, run_id, **kwargs)
