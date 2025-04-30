Module agntcy_acp
=================

Sub-modules
-----------
* agntcy_acp.acp_v0
* agntcy_acp.agws_v0
* agntcy_acp.exceptions
* agntcy_acp.langgraph
* agntcy_acp.manifest
* agntcy_acp.models

Classes
-------

`ACPClient(api_client: agntcy_acp.acp_v0.sync_client.api_client.ApiClient | None = None)`
:   Client for ACP API.

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.sync_client.api.agents_api.AgentsApi
    * agntcy_acp.acp_v0.sync_client.api.stateless_runs_api.StatelessRunsApi
    * agntcy_acp.acp_v0.sync_client.api.threads_api.ThreadsApi
    * agntcy_acp.acp_v0.sync_client.api.thread_runs_api.ThreadRunsApi

    ### Methods

    `cancel_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> None`
    :   Cancel Stateless Run
        
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Cancel Stateless Run
        
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> urllib3.response.HTTPResponse`
    :   Cancel Stateless Run
        
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> None`
    :   Cancel Run
        
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Cancel Run
        
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> urllib3.response.HTTPResponse`
    :   Cancel Run
        
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `copy_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Copy Thread
        
        Create a new thread with a copy of the state and checkpoints from an existing thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `copy_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Copy Thread
        
        Create a new thread with a copy of the state and checkpoints from an existing thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `copy_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> urllib3.response.HTTPResponse`
    :   Copy Thread
        
        Create a new thread with a copy of the state and checkpoints from an existing thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_stateless_run_output(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Create a stateless run and stream its output
        
        Create a stateless run and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_stateless_run_output_with_http_info(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Create a stateless run and stream its output
        
        Create a stateless run and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_stateless_run_output_without_preload_content(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> urllib3.response.HTTPResponse`
    :   Create a stateless run and stream its output
        
        Create a stateless run and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Create a run on a thread and stream its output
        
        Create a run on a thread and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Create a run on a thread and stream its output
        
        Create a run on a thread and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> urllib3.response.HTTPResponse`
    :   Create a run on a thread and stream its output
        
        Create a run on a thread and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_stateless_run_output(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateless.RunWaitResponseStateless`
    :   Create a stateless run and wait for its output
        
        Create a stateless run and wait for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_stateless_run_output_with_http_info(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateless]`
    :   Create a stateless run and wait for its output
        
        Create a stateless run and wait for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_stateless_run_output_without_preload_content(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> urllib3.response.HTTPResponse`
    :   Create a stateless run and wait for its output
        
        Create a stateless run and wait for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateful.RunWaitResponseStateful`
    :   Create a run on a thread and block waiting for the result of the run
        
        Create a run on a thread and block waiting for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateful]`
    :   Create a run on a thread and block waiting for the result of the run
        
        Create a run on a thread and block waiting for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> urllib3.response.HTTPResponse`
    :   Create a run on a thread and block waiting for the result of the run
        
        Create a run on a thread and block waiting for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_stateless_run(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.models.run_stateless.RunStateless`
    :   Create a Background stateless Run
        
        Create a stateless run, return the run ID immediately. Don't wait for the final run output.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_stateless_run_with_http_info(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]`
    :   Create a Background stateless Run
        
        Create a stateless run, return the run ID immediately. Don't wait for the final run output.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_stateless_run_without_preload_content(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> urllib3.response.HTTPResponse`
    :   Create a Background stateless Run
        
        Create a stateless run, return the run ID immediately. Don't wait for the final run output.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread(self, thread_create: agntcy_acp.acp_v0.models.thread_create.ThreadCreate) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Create an empty Thread
        
        Create a new thread. 
        
        :param thread_create: (required)
        :type thread_create: ThreadCreate
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.models.run_stateful.RunStateful`
    :   Create a Background Run on a thread
        
        Create a run on a thread, return the run ID immediately. Don't wait for the final run output.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]`
    :   Create a Background Run on a thread
        
        Create a run on a thread, return the run ID immediately. Don't wait for the final run output.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> urllib3.response.HTTPResponse`
    :   Create a Background Run on a thread
        
        Create a run on a thread, return the run ID immediately. Don't wait for the final run output.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_with_http_info(self, thread_create: agntcy_acp.acp_v0.models.thread_create.ThreadCreate) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Create an empty Thread
        
        Create a new thread. 
        
        :param thread_create: (required)
        :type thread_create: ThreadCreate
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_without_preload_content(self, thread_create: agntcy_acp.acp_v0.models.thread_create.ThreadCreate) ‑> urllib3.response.HTTPResponse`
    :   Create an empty Thread
        
        Create a new thread. 
        
        :param thread_create: (required)
        :type thread_create: ThreadCreate
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> None`
    :   Delete Stateless Run
        
        Delete a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Delete Stateless Run
        
        Delete a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Delete Stateless Run
        
        Delete a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> None`
    :   Delete a thread. If the thread contains any pending run, deletion fails.
        
        Delete a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> None`
    :   Delete Run
        
        Delete a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Delete Run
        
        Delete a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Delete Run
        
        Delete a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Delete a thread. If the thread contains any pending run, deletion fails.
        
        Delete a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> urllib3.response.HTTPResponse`
    :   Delete a thread. If the thread contains any pending run, deletion fails.
        
        Delete a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_acp_descriptor_by_id(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.models.agent_acp_descriptor.AgentACPDescriptor`
    :   Get Agent ACP Descriptor from its id
        
        Get agent ACP descriptor by agent ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_acp_descriptor_by_id_with_http_info(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[AgentACPDescriptor]`
    :   Get Agent ACP Descriptor from its id
        
        Get agent ACP descriptor by agent ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_acp_descriptor_by_id_without_preload_content(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> urllib3.response.HTTPResponse`
    :   Get Agent ACP Descriptor from its id
        
        Get agent ACP descriptor by agent ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_agent_by_id(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.models.agent.Agent`
    :   Get Agent
        
        Get an agent by ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_agent_by_id_with_http_info(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Agent]`
    :   Get Agent
        
        Get an agent by ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_agent_by_id_without_preload_content(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> urllib3.response.HTTPResponse`
    :   Get Agent
        
        Get an agent by ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_stateless.RunStateless`
    :   Get Run
        
        Get a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]`
    :   Get Run
        
        Get a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Get Run
        
        Get a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Get Thread
        
        Get a thread from its ID. 
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_history(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, before: Annotated[str, Strict(strict=True)] | None = None) ‑> List[agntcy_acp.acp_v0.models.thread_state.ThreadState]`
    :   Get Thread History
        
        Get all past states for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param before:
        :type before: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_history_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, before: Annotated[str, Strict(strict=True)] | None = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[ThreadState]]`
    :   Get Thread History
        
        Get all past states for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param before:
        :type before: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_history_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, before: Annotated[str, Strict(strict=True)] | None = None) ‑> urllib3.response.HTTPResponse`
    :   Get Thread History
        
        Get all past states for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param before:
        :type before: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_stateful.RunStateful`
    :   Get Run
        
        Get a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]`
    :   Get Run
        
        Get a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Get Run
        
        Get a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Get Thread
        
        Get a thread from its ID. 
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> urllib3.response.HTTPResponse`
    :   Get Thread
        
        Get a thread from its ID. 
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `list_thread_runs(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, offset: Annotated[int, Strict(strict=True)] | None = None) ‑> List[agntcy_acp.acp_v0.models.run_stateful.RunStateful]`
    :   List Runs for a thread
        
        List runs for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `list_thread_runs_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, offset: Annotated[int, Strict(strict=True)] | None = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateful]]`
    :   List Runs for a thread
        
        List runs for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `list_thread_runs_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, offset: Annotated[int, Strict(strict=True)] | None = None) ‑> urllib3.response.HTTPResponse`
    :   List Runs for a thread
        
        List runs for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `patch_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], thread_patch: agntcy_acp.acp_v0.models.thread_patch.ThreadPatch) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Patch Thread
        
        Update a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param thread_patch: (required)
        :type thread_patch: ThreadPatch
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `patch_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], thread_patch: agntcy_acp.acp_v0.models.thread_patch.ThreadPatch) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Patch Thread
        
        Update a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param thread_patch: (required)
        :type thread_patch: ThreadPatch
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `patch_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], thread_patch: agntcy_acp.acp_v0.models.thread_patch.ThreadPatch) ‑> urllib3.response.HTTPResponse`
    :   Patch Thread
        
        Update a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param thread_patch: (required)
        :type thread_patch: ThreadPatch
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.models.run_stateless.RunStateless`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> urllib3.response.HTTPResponse`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.models.run_stateful.RunStateful`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> urllib3.response.HTTPResponse`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_agents(self, agent_search_request: agntcy_acp.acp_v0.models.agent_search_request.AgentSearchRequest) ‑> List[agntcy_acp.acp_v0.models.agent.Agent]`
    :   Search Agents
        
        Returns a list of agents matching the criteria provided in the request.  This endpoint also functions as the endpoint to list all agents.
        
        :param agent_search_request: (required)
        :type agent_search_request: AgentSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_agents_with_http_info(self, agent_search_request: agntcy_acp.acp_v0.models.agent_search_request.AgentSearchRequest) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[Agent]]`
    :   Search Agents
        
        Returns a list of agents matching the criteria provided in the request.  This endpoint also functions as the endpoint to list all agents.
        
        :param agent_search_request: (required)
        :type agent_search_request: AgentSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_agents_without_preload_content(self, agent_search_request: agntcy_acp.acp_v0.models.agent_search_request.AgentSearchRequest) ‑> urllib3.response.HTTPResponse`
    :   Search Agents
        
        Returns a list of agents matching the criteria provided in the request.  This endpoint also functions as the endpoint to list all agents.
        
        :param agent_search_request: (required)
        :type agent_search_request: AgentSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_stateless_runs(self, run_search_request: agntcy_acp.acp_v0.models.run_search_request.RunSearchRequest) ‑> List[agntcy_acp.acp_v0.models.run_stateless.RunStateless]`
    :   Search Stateless Runs
        
        Search for stateless run.  This endpoint also functions as the endpoint to list all stateless Runs.
        
        :param run_search_request: (required)
        :type run_search_request: RunSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_stateless_runs_with_http_info(self, run_search_request: agntcy_acp.acp_v0.models.run_search_request.RunSearchRequest) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateless]]`
    :   Search Stateless Runs
        
        Search for stateless run.  This endpoint also functions as the endpoint to list all stateless Runs.
        
        :param run_search_request: (required)
        :type run_search_request: RunSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_stateless_runs_without_preload_content(self, run_search_request: agntcy_acp.acp_v0.models.run_search_request.RunSearchRequest) ‑> urllib3.response.HTTPResponse`
    :   Search Stateless Runs
        
        Search for stateless run.  This endpoint also functions as the endpoint to list all stateless Runs.
        
        :param run_search_request: (required)
        :type run_search_request: RunSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_threads(self, thread_search_request: agntcy_acp.acp_v0.models.thread_search_request.ThreadSearchRequest) ‑> List[agntcy_acp.acp_v0.models.thread.Thread]`
    :   Search Threads
        
        Search for threads.  This endpoint also functions as the endpoint to list all threads.
        
        :param thread_search_request: (required)
        :type thread_search_request: ThreadSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_threads_with_http_info(self, thread_search_request: agntcy_acp.acp_v0.models.thread_search_request.ThreadSearchRequest) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[Thread]]`
    :   Search Threads
        
        Search for threads.  This endpoint also functions as the endpoint to list all threads.
        
        :param thread_search_request: (required)
        :type thread_search_request: ThreadSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_threads_without_preload_content(self, thread_search_request: agntcy_acp.acp_v0.models.thread_search_request.ThreadSearchRequest) ‑> urllib3.response.HTTPResponse`
    :   Search Threads
        
        Search for threads.  This endpoint also functions as the endpoint to list all threads.
        
        :param thread_search_request: (required)
        :type thread_search_request: ThreadSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_stateless_run_output(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Stream output from Stateless Run
        
        Join the output stream of an existing run. This endpoint streams output in real-time from a run. Only output produced after this endpoint is called will be streamed.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_stateless_run_output_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Stream output from Stateless Run
        
        Join the output stream of an existing run. This endpoint streams output in real-time from a run. Only output produced after this endpoint is called will be streamed.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_stateless_run_output_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Stream output from Stateless Run
        
        Join the output stream of an existing run. This endpoint streams output in real-time from a run. Only output produced after this endpoint is called will be streamed.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Stream output from Run
        
        Join the output stream of an existing run. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Stream output from Run
        
        Join the output stream of an existing run. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Stream output from Run
        
        Join the output stream of an existing run. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_stateless_run_output(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateless.RunWaitResponseStateless`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. The output can be:   * an interrupt, this happens when the agent run status is `interrupted`   * the final result of the run, this happens when the agent run status is `success`   * an error, this happens when the agent run status is `error` or `timeout`   This call blocks until the output is available.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_stateless_run_output_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateless]`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. The output can be:   * an interrupt, this happens when the agent run status is `interrupted`   * the final result of the run, this happens when the agent run status is `success`   * an error, this happens when the agent run status is `error` or `timeout`   This call blocks until the output is available.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_stateless_run_output_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. The output can be:   * an interrupt, this happens when the agent run status is `interrupted`   * the final result of the run, this happens when the agent run status is `success`   * an error, this happens when the agent run status is `error` or `timeout`   This call blocks until the output is available.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateful.RunWaitResponseStateful`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateful]`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> urllib3.response.HTTPResponse`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

`ACPDescriptorValidationException(*args, **kwargs)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

`ACPRunException(*args, **kwargs)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

`ApiAttributeError(msg, path_to_item=None)`
:   The base exception class for all OpenAPIExceptions
    
    Raised when an attribute reference or assignment fails.
    
    Args:
        msg (str): the exception message
    
    Keyword Args:
        path_to_item (None/list) the path to the exception in the
            received_data dict

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.AttributeError
    * builtins.Exception
    * builtins.BaseException

`ApiClientConfiguration(host: str | None = None, api_key: Dict[str, str] | None = None, api_key_prefix: Dict[str, str] | None = None, username: str | None = None, password: str | None = None, access_token: str | None = None, server_variables: Dict[str, str] | None = None, server_operation_variables: Dict[int, Dict[str, str]] | None = None, ssl_ca_cert: str | None = None, retries: int | None = None, ca_cert_data: str | bytes | None = None, *, debug: bool | None = None)`
:   This class contains various settings of the API client.
    
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
    
    Constructor

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.configuration.Configuration
    * pydantic.main.BaseModel

    ### Class variables

    `model_config`
    :   The type of the None singleton.

    ### Static methods

    `fromEnvPrefix(env_var_prefix: str, host: str | None = None, api_key: Dict[str, str] | None = None, api_key_prefix: Dict[str, str] | None = None, username: str | None = None, password: str | None = None, access_token: str | None = None, server_variables: Dict[str, str] | None = None, server_operation_variables: Dict[int, Dict[str, str]] | None = None, ssl_ca_cert: str | None = None, retries: int | None = None, ca_cert_data: str | bytes | None = None, *, debug: bool | None = None) ‑> agntcy_acp.ApiClientConfiguration`
    :   Construct a configuration object using environment variables as
        default source of parameter values. For example, with env_var_prefix="MY_", 
        the default host parameter value would be looked up in the "MY_HOST" 
        environment variable if not provided.
        
        :param env_var_prefix: String used as prefix for environment variable 
          names.
        
        :return: Configuration object
        :rtype: ApiClientConfiguration

    `get_default() ‑> Self`
    :   Return the default configuration.
        
        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration.
        
        :return: The configuration object.

    `get_default_copy() ‑> Self`
    :   Deprecated. Please use `get_default` instead.
        
        Deprecated. Please use `get_default` instead.
        
        :return: The configuration object.

    `set_default(default: Self | None) ‑> None`
    :   Set default instance of configuration.
        
        It stores default configuration, which can be
        returned by get_default_copy method.
        
        :param default: object of Configuration

    ### Instance variables

    `access_token`
    :   Access token

    `assert_hostname`
    :   Set this to True/False to enable/disable SSL hostname verification.

    `ca_cert_data`
    :   Set this to verify the peer using PEM (str) or DER (bytes)
        certificate data.

    `cert_file`
    :   client certificate file

    `connection_pool_maxsize`
    :   urllib3 connection pool's maximum number of connections saved
        per pool. urllib3 uses 1 connection as default value, but this is
        not the best value when you are making a lot of possibly parallel
        requests to the same host, which is often the case here.
        cpu_count * 5 is used as default value to increase performance.

    `date_format`
    :   date format

    `datetime_format`
    :   datetime format

    `debug: bool`
    :   Debug status
        
        :param value: The debug status, True or False.
        :type: bool

    `host: str`
    :   Return generated host.

    `ignore_operation_servers`
    :   Ignore operation servers

    `key_file`
    :   client key file

    `logger`
    :   Logging Settings

    `logger_file: str | None`
    :   Debug file location

    `logger_file_handler`
    :   Log file handler

    `logger_format: str`
    :   Log format

    `logger_stream_handler`
    :   Log stream handler

    `password`
    :   Password for HTTP basic authentication

    `proxy`
    :   Proxy URL

    `proxy_headers`
    :   Proxy headers

    `refresh_api_key_hook`
    :   function hook to refresh API key if expired

    `retries`
    :   Adding retries to override urllib3 default value 3

    `safe_chars_for_path_param`
    :   Safe chars for path_param

    `server_operation_index`
    :   Default server index

    `server_operation_variables`
    :   Default server variables

    `socket_options`
    :   Options to pass down to the underlying urllib3 socket

    `ssl_ca_cert`
    :   Set this to customize the certificate file to verify the peer.

    `temp_folder_path`
    :   Temp file folder for downloading files

    `tls_server_name`
    :   SSL/TLS Server Name Indication (SNI)
        Set this to the SNI value expected by the server.

    `username`
    :   Username for HTTP basic authentication

    `verify_ssl`
    :   SSL/TLS verification
        Set this to false to skip verifying SSL certificate when calling API
        from https server.

    ### Methods

    `auth_settings(self) ‑> agntcy_acp.acp_v0.configuration.AuthSettings`
    :   Gets Auth Settings dict for api client.
        
        :return: The Auth Settings information dict.

    `get_api_key_with_prefix(self, identifier: str, alias: str | None = None) ‑> str | None`
    :   Gets API key (with prefix if set).
        
        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.

    `get_basic_auth_token(self) ‑> str | None`
    :   Gets HTTP basic authentication header (string).
        
        :return: The token for basic HTTP authentication.

    `get_host_from_settings(self, index: int | None, variables: Dict[str, str] | None = None, servers: List[agntcy_acp.acp_v0.configuration.HostSetting] | None = None) ‑> str`
    :   Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings

    `get_host_settings(self) ‑> List[agntcy_acp.acp_v0.configuration.HostSetting]`
    :   Gets an array of host settings
        
        :return: An array of host settings

    `to_debug_report(self) ‑> str`
    :   Gets the essential information for debugging.
        
        :return: The report for debugging.

`ApiException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   The base exception class for all OpenAPIExceptions

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException

    ### Descendants

    * agntcy_acp.acp_v0.exceptions.BadRequestException
    * agntcy_acp.acp_v0.exceptions.ConflictException
    * agntcy_acp.acp_v0.exceptions.ForbiddenException
    * agntcy_acp.acp_v0.exceptions.NotFoundException
    * agntcy_acp.acp_v0.exceptions.ServiceException
    * agntcy_acp.acp_v0.exceptions.UnauthorizedException
    * agntcy_acp.acp_v0.exceptions.UnprocessableEntityException

    ### Static methods

    `from_response(*, http_resp, body: str | None, data: Any | None) ‑> Self`
    :

`ApiKeyError(msg, path_to_item=None)`
:   The base exception class for all OpenAPIExceptions
    
    Args:
        msg (str): the exception message
    
    Keyword Args:
        path_to_item (None/list) the path to the exception in the
            received_data dict

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.KeyError
    * builtins.LookupError
    * builtins.Exception
    * builtins.BaseException

`ApiResponse(**data: Any)`
:   API response object
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
    validated to form a valid model.
    
    `self` is explicitly positional-only to allow `self` as a field name.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * typing.Generic

    ### Descendants

    * agntcy_acp.acp_v0.api_response.ApiResponse[AgentACPDescriptor]
    * agntcy_acp.acp_v0.api_response.ApiResponse[Agent]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[Agent]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateful]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateless]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[ThreadState]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[List[Thread]]
    * agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateful]
    * agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateless]
    * agntcy_acp.acp_v0.api_response.ApiResponse[Thread]

    ### Class variables

    `data: ~T`
    :   The type of the None singleton.

    `headers: Mapping[str, str] | None`
    :   The type of the None singleton.

    `model_config`
    :   The type of the None singleton.

    `raw_data: bytes`
    :   The type of the None singleton.

    `status_code: int`
    :   The type of the None singleton.

`ApiTypeError(msg, path_to_item=None, valid_classes=None, key_type=None)`
:   The base exception class for all OpenAPIExceptions
    
    Raises an exception for TypeErrors
    
    Args:
        msg (str): the exception message
    
    Keyword Args:
        path_to_item (list): a list of keys an indices to get to the
                             current_item
                             None if unset
        valid_classes (tuple): the primitive classes that current item
                               should be an instance of
                               None if unset
        key_type (bool): False if our value is a value in a dict
                         True if it is a key in a dict
                         False if our item is an item in a list
                         None if unset

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.TypeError
    * builtins.Exception
    * builtins.BaseException

`ApiValueError(msg, path_to_item=None)`
:   The base exception class for all OpenAPIExceptions
    
    Args:
        msg (str): the exception message
    
    Keyword Args:
        path_to_item (list) the path to the exception in the
            received_data dict. None if unset

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.ValueError
    * builtins.Exception
    * builtins.BaseException

`AsyncACPClient(api_client: agntcy_acp.acp_v0.async_client.api_client.ApiClient | None = None)`
:   Async client for ACP API.

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.async_client.api.agents_api.AgentsApi
    * agntcy_acp.acp_v0.async_client.api.stateless_runs_api.StatelessRunsApi
    * agntcy_acp.acp_v0.async_client.api.threads_api.ThreadsApi
    * agntcy_acp.acp_v0.async_client.api.thread_runs_api.ThreadRunsApi

    ### Methods

    `cancel_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> None`
    :   Cancel Stateless Run
        
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Cancel Stateless Run
        
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Cancel Stateless Run
        
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> None`
    :   Cancel Run
        
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Cancel Run
        
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `cancel_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], wait: Annotated[bool, Strict(strict=True)] | None = None, action: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.')] = None) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Cancel Run
        
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param wait:
        :type wait: bool
        :param action: Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.
        :type action: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `copy_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Copy Thread
        
        Create a new thread with a copy of the state and checkpoints from an existing thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `copy_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Copy Thread
        
        Create a new thread with a copy of the state and checkpoints from an existing thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `copy_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Copy Thread
        
        Create a new thread with a copy of the state and checkpoints from an existing thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_stateless_run_output(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Create a stateless run and stream its output
        
        Create a stateless run and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_stateless_run_output_with_http_info(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Create a stateless run and stream its output
        
        Create a stateless run and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_stateless_run_output_without_preload_content(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Create a stateless run and stream its output
        
        Create a stateless run and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Create a run on a thread and stream its output
        
        Create a run on a thread and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Create a run on a thread and stream its output
        
        Create a run on a thread and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_stream_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Create a run on a thread and stream its output
        
        Create a run on a thread and join its output stream. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_stateless_run_output(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateless.RunWaitResponseStateless`
    :   Create a stateless run and wait for its output
        
        Create a stateless run and wait for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_stateless_run_output_with_http_info(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateless]`
    :   Create a stateless run and wait for its output
        
        Create a stateless run and wait for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_stateless_run_output_without_preload_content(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Create a stateless run and wait for its output
        
        Create a stateless run and wait for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateful.RunWaitResponseStateful`
    :   Create a run on a thread and block waiting for the result of the run
        
        Create a run on a thread and block waiting for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateful]`
    :   Create a run on a thread and block waiting for the result of the run
        
        Create a run on a thread and block waiting for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_and_wait_for_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Create a run on a thread and block waiting for the result of the run
        
        Create a run on a thread and block waiting for its output. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_stateless_run(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.models.run_stateless.RunStateless`
    :   Create a Background stateless Run
        
        Create a stateless run, return the run ID immediately. Don't wait for the final run output.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_stateless_run_with_http_info(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]`
    :   Create a Background stateless Run
        
        Create a stateless run, return the run ID immediately. Don't wait for the final run output.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_stateless_run_without_preload_content(self, run_create_stateless: agntcy_acp.acp_v0.models.run_create_stateless.RunCreateStateless) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Create a Background stateless Run
        
        Create a stateless run, return the run ID immediately. Don't wait for the final run output.
        
        :param run_create_stateless: (required)
        :type run_create_stateless: RunCreateStateless
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread(self, thread_create: agntcy_acp.acp_v0.models.thread_create.ThreadCreate) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Create an empty Thread
        
        Create a new thread. 
        
        :param thread_create: (required)
        :type thread_create: ThreadCreate
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.models.run_stateful.RunStateful`
    :   Create a Background Run on a thread
        
        Create a run on a thread, return the run ID immediately. Don't wait for the final run output.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]`
    :   Create a Background Run on a thread
        
        Create a run on a thread, return the run ID immediately. Don't wait for the final run output.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_create_stateful: agntcy_acp.acp_v0.models.run_create_stateful.RunCreateStateful) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Create a Background Run on a thread
        
        Create a run on a thread, return the run ID immediately. Don't wait for the final run output.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_create_stateful: (required)
        :type run_create_stateful: RunCreateStateful
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_with_http_info(self, thread_create: agntcy_acp.acp_v0.models.thread_create.ThreadCreate) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Create an empty Thread
        
        Create a new thread. 
        
        :param thread_create: (required)
        :type thread_create: ThreadCreate
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `create_thread_without_preload_content(self, thread_create: agntcy_acp.acp_v0.models.thread_create.ThreadCreate) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Create an empty Thread
        
        Create a new thread. 
        
        :param thread_create: (required)
        :type thread_create: ThreadCreate
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> None`
    :   Delete Stateless Run
        
        Delete a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Delete Stateless Run
        
        Delete a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Delete Stateless Run
        
        Delete a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> None`
    :   Delete a thread. If the thread contains any pending run, deletion fails.
        
        Delete a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> None`
    :   Delete Run
        
        Delete a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Delete Run
        
        Delete a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Delete Run
        
        Delete a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[NoneType]`
    :   Delete a thread. If the thread contains any pending run, deletion fails.
        
        Delete a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `delete_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Delete a thread. If the thread contains any pending run, deletion fails.
        
        Delete a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_acp_descriptor_by_id(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.models.agent_acp_descriptor.AgentACPDescriptor`
    :   Get Agent ACP Descriptor from its id
        
        Get agent ACP descriptor by agent ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_acp_descriptor_by_id_with_http_info(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[AgentACPDescriptor]`
    :   Get Agent ACP Descriptor from its id
        
        Get agent ACP descriptor by agent ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_acp_descriptor_by_id_without_preload_content(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Get Agent ACP Descriptor from its id
        
        Get agent ACP descriptor by agent ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_agent_by_id(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.models.agent.Agent`
    :   Get Agent
        
        Get an agent by ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_agent_by_id_with_http_info(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Agent]`
    :   Get Agent
        
        Get an agent by ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_agent_by_id_without_preload_content(self, agent_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the agent.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Get Agent
        
        Get an agent by ID.
        
        :param agent_id: The ID of the agent. (required)
        :type agent_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_stateless.RunStateless`
    :   Get Run
        
        Get a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]`
    :   Get Run
        
        Get a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Get Run
        
        Get a stateless run by ID.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Get Thread
        
        Get a thread from its ID. 
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_history(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, before: Annotated[str, Strict(strict=True)] | None = None) ‑> List[agntcy_acp.acp_v0.models.thread_state.ThreadState]`
    :   Get Thread History
        
        Get all past states for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param before:
        :type before: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_history_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, before: Annotated[str, Strict(strict=True)] | None = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[ThreadState]]`
    :   Get Thread History
        
        Get all past states for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param before:
        :type before: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_history_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, before: Annotated[str, Strict(strict=True)] | None = None) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Get Thread History
        
        Get all past states for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param before:
        :type before: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_stateful.RunStateful`
    :   Get Run
        
        Get a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]`
    :   Get Run
        
        Get a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Get Run
        
        Get a run by ID.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Get Thread
        
        Get a thread from its ID. 
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `get_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Get Thread
        
        Get a thread from its ID. 
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `list_thread_runs(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, offset: Annotated[int, Strict(strict=True)] | None = None) ‑> List[agntcy_acp.acp_v0.models.run_stateful.RunStateful]`
    :   List Runs for a thread
        
        List runs for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `list_thread_runs_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, offset: Annotated[int, Strict(strict=True)] | None = None) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateful]]`
    :   List Runs for a thread
        
        List runs for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `list_thread_runs_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], limit: Annotated[int, Strict(strict=True)] | None = None, offset: Annotated[int, Strict(strict=True)] | None = None) ‑> aiohttp.client_reqrep.ClientResponse`
    :   List Runs for a thread
        
        List runs for a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param limit:
        :type limit: int
        :param offset:
        :type offset: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `patch_thread(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], thread_patch: agntcy_acp.acp_v0.models.thread_patch.ThreadPatch) ‑> agntcy_acp.acp_v0.models.thread.Thread`
    :   Patch Thread
        
        Update a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param thread_patch: (required)
        :type thread_patch: ThreadPatch
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `patch_thread_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], thread_patch: agntcy_acp.acp_v0.models.thread_patch.ThreadPatch) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[Thread]`
    :   Patch Thread
        
        Update a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param thread_patch: (required)
        :type thread_patch: ThreadPatch
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `patch_thread_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], thread_patch: agntcy_acp.acp_v0.models.thread_patch.ThreadPatch) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Patch Thread
        
        Update a thread.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param thread_patch: (required)
        :type thread_patch: ThreadPatch
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_stateless_run(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.models.run_stateless.RunStateless`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_stateless_run_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateless]`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_stateless_run_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_thread_run(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.models.run_stateful.RunStateful`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_thread_run_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunStateful]`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `resume_thread_run_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')], body: Dict[str, Any]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Resume an interrupted Run
        
        Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param body: (required)
        :type body: object
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_agents(self, agent_search_request: agntcy_acp.acp_v0.models.agent_search_request.AgentSearchRequest) ‑> List[agntcy_acp.acp_v0.models.agent.Agent]`
    :   Search Agents
        
        Returns a list of agents matching the criteria provided in the request.  This endpoint also functions as the endpoint to list all agents.
        
        :param agent_search_request: (required)
        :type agent_search_request: AgentSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_agents_with_http_info(self, agent_search_request: agntcy_acp.acp_v0.models.agent_search_request.AgentSearchRequest) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[Agent]]`
    :   Search Agents
        
        Returns a list of agents matching the criteria provided in the request.  This endpoint also functions as the endpoint to list all agents.
        
        :param agent_search_request: (required)
        :type agent_search_request: AgentSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_agents_without_preload_content(self, agent_search_request: agntcy_acp.acp_v0.models.agent_search_request.AgentSearchRequest) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Search Agents
        
        Returns a list of agents matching the criteria provided in the request.  This endpoint also functions as the endpoint to list all agents.
        
        :param agent_search_request: (required)
        :type agent_search_request: AgentSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_stateless_runs(self, run_search_request: agntcy_acp.acp_v0.models.run_search_request.RunSearchRequest) ‑> List[agntcy_acp.acp_v0.models.run_stateless.RunStateless]`
    :   Search Stateless Runs
        
        Search for stateless run.  This endpoint also functions as the endpoint to list all stateless Runs.
        
        :param run_search_request: (required)
        :type run_search_request: RunSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_stateless_runs_with_http_info(self, run_search_request: agntcy_acp.acp_v0.models.run_search_request.RunSearchRequest) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[RunStateless]]`
    :   Search Stateless Runs
        
        Search for stateless run.  This endpoint also functions as the endpoint to list all stateless Runs.
        
        :param run_search_request: (required)
        :type run_search_request: RunSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_stateless_runs_without_preload_content(self, run_search_request: agntcy_acp.acp_v0.models.run_search_request.RunSearchRequest) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Search Stateless Runs
        
        Search for stateless run.  This endpoint also functions as the endpoint to list all stateless Runs.
        
        :param run_search_request: (required)
        :type run_search_request: RunSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_threads(self, thread_search_request: agntcy_acp.acp_v0.models.thread_search_request.ThreadSearchRequest) ‑> List[agntcy_acp.acp_v0.models.thread.Thread]`
    :   Search Threads
        
        Search for threads.  This endpoint also functions as the endpoint to list all threads.
        
        :param thread_search_request: (required)
        :type thread_search_request: ThreadSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_threads_with_http_info(self, thread_search_request: agntcy_acp.acp_v0.models.thread_search_request.ThreadSearchRequest) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[List[Thread]]`
    :   Search Threads
        
        Search for threads.  This endpoint also functions as the endpoint to list all threads.
        
        :param thread_search_request: (required)
        :type thread_search_request: ThreadSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `search_threads_without_preload_content(self, thread_search_request: agntcy_acp.acp_v0.models.thread_search_request.ThreadSearchRequest) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Search Threads
        
        Search for threads.  This endpoint also functions as the endpoint to list all threads.
        
        :param thread_search_request: (required)
        :type thread_search_request: ThreadSearchRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_stateless_run_output(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Stream output from Stateless Run
        
        Join the output stream of an existing run. This endpoint streams output in real-time from a run. Only output produced after this endpoint is called will be streamed.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_stateless_run_output_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Stream output from Stateless Run
        
        Join the output stream of an existing run. This endpoint streams output in real-time from a run. Only output produced after this endpoint is called will be streamed.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_stateless_run_output_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Stream output from Stateless Run
        
        Join the output stream of an existing run. This endpoint streams output in real-time from a run. Only output produced after this endpoint is called will be streamed.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_output_stream.RunOutputStream`
    :   Stream output from Run
        
        Join the output stream of an existing run. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunOutputStream]`
    :   Stream output from Run
        
        Join the output stream of an existing run. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `stream_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Stream output from Run
        
        Join the output stream of an existing run. See 'GET /runs/{run_id}/stream' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_stateless_run_output(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateless.RunWaitResponseStateless`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. The output can be:   * an interrupt, this happens when the agent run status is `interrupted`   * the final result of the run, this happens when the agent run status is `success`   * an error, this happens when the agent run status is `error` or `timeout`   This call blocks until the output is available.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_stateless_run_output_with_http_info(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateless]`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. The output can be:   * an interrupt, this happens when the agent run status is `interrupted`   * the final result of the run, this happens when the agent run status is `success`   * an error, this happens when the agent run status is `error` or `timeout`   This call blocks until the output is available.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_stateless_run_output_without_preload_content(self, run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. The output can be:   * an interrupt, this happens when the agent run status is `interrupted`   * the final result of the run, this happens when the agent run status is `success`   * an error, this happens when the agent run status is `error` or `timeout`   This call blocks until the output is available.
        
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_thread_run_output(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.models.run_wait_response_stateful.RunWaitResponseStateful`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_thread_run_output_with_http_info(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> agntcy_acp.acp_v0.api_response.ApiResponse[RunWaitResponseStateful]`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

    `wait_for_thread_run_output_without_preload_content(self, thread_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the thread.')], run_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='The ID of the run.')]) ‑> aiohttp.client_reqrep.ClientResponse`
    :   Blocks waiting for the result of the run.
        
        Blocks waiting for the result of the run. See 'GET /runs/{run_id}/wait' for details on the return values.
        
        :param thread_id: The ID of the thread. (required)
        :type thread_id: str
        :param run_id: The ID of the run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.

`BadRequestException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   The base exception class for all OpenAPIExceptions

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException

`ConflictException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   Exception for HTTP 409 Conflict.

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException

`ForbiddenException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   The base exception class for all OpenAPIExceptions

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException

`NotFoundException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   The base exception class for all OpenAPIExceptions

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException

`OpenApiException(*args, **kwargs)`
:   The base exception class for all OpenAPIExceptions

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

    ### Descendants

    * agntcy_acp.acp_v0.exceptions.ApiAttributeError
    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.ApiKeyError
    * agntcy_acp.acp_v0.exceptions.ApiTypeError
    * agntcy_acp.acp_v0.exceptions.ApiValueError

`ServiceException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   The base exception class for all OpenAPIExceptions

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException

`UnauthorizedException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   The base exception class for all OpenAPIExceptions

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException

`UnprocessableEntityException(status=None, reason=None, http_resp=None, *, body: str | None = None, data: Any | None = None)`
:   Exception for HTTP 422 Unprocessable Entity.

    ### Ancestors (in MRO)

    * agntcy_acp.acp_v0.exceptions.ApiException
    * agntcy_acp.acp_v0.exceptions.OpenApiException
    * builtins.Exception
    * builtins.BaseException