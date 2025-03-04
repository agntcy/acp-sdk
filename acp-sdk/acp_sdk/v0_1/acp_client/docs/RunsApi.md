# acp_client_v0_1.RunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_run**](RunsApi.md#create_run) | **POST** /runs | Create Background Run
[**delete_run**](RunsApi.md#delete_run) | **DELETE** /runs/{run_id} | Delete a run. If running, cancel and then delete.
[**get_run**](RunsApi.md#get_run) | **GET** /runs/{run_id} | Get a previously created Run
[**get_run_output**](RunsApi.md#get_run_output) | **GET** /runs/{run_id}/output | Retrieve last output of a run if available
[**get_run_stream**](RunsApi.md#get_run_stream) | **GET** /runs/{run_id}/stream | Stream the run output
[**resume_run**](RunsApi.md#resume_run) | **POST** /runs/{run_id} | Resume an interrupted Run
[**search_runs**](RunsApi.md#search_runs) | **POST** /runs/search | Search Runs


# **create_run**
> Run create_run(run_create)

Create Background Run

Create a run, return the run descriptor immediately. Don't wait for the final run output.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.run import Run
from acp_client_v0_1.models.run_create import RunCreate
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.RunsApi(api_client)
    run_create = acp_client_v0_1.RunCreate() # RunCreate | 

    try:
        # Create Background Run
        api_response = api_instance.create_run(run_create)
        print("The response of RunsApi->create_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->create_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_create** | [**RunCreate**](RunCreate.md)|  | 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run**
> Run delete_run(run_id)

Delete a run. If running, cancel and then delete.

Cancel a run.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.run import Run
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.RunsApi(api_client)
    run_id = 'run_id_example' # str | The ID of the agent.

    try:
        # Delete a run. If running, cancel and then delete.
        api_response = api_instance.delete_run(run_id)
        print("The response of RunsApi->delete_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->delete_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The ID of the agent. | 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run**
> Run get_run(run_id)

Get a previously created Run

Get a run from its ID. Don't wait for the final run output.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.run import Run
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.RunsApi(api_client)
    run_id = 'run_id_example' # str | The ID of the agent.

    try:
        # Get a previously created Run
        api_response = api_instance.get_run(run_id)
        print("The response of RunsApi->get_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->get_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The ID of the agent. | 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_output**
> RunOutput get_run_output(run_id, block_timeout=block_timeout)

Retrieve last output of a run if available

Retrieve the last output of the run.  The output can be:
  * an interrupt, this happens when the agent run status is `interrupted`
  * the final result of the run, this happens when the agent run status is `success`
  * an error, this happens when the agent run status is `error` or `timeout`


If the block timeout is provided and the current run status is `pending`, this call blocks until the state changes or the timeout expires. 
If no timeout is provided or the timeout has expired and  run status is `pending`, this call returns `204` with no content.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.run_output import RunOutput
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.RunsApi(api_client)
    run_id = 'run_id_example' # str | The ID of the run.
    block_timeout = 56 # int |  (optional)

    try:
        # Retrieve last output of a run if available
        api_response = api_instance.get_run_output(run_id, block_timeout=block_timeout)
        print("The response of RunsApi->get_run_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->get_run_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The ID of the run. | 
 **block_timeout** | **int**|  | [optional] 

### Return type

[**RunOutput**](RunOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Output Available |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_stream**
> RunOutputStream get_run_stream(run_id)

Stream the run output

Send a stream of events using Server-sent events (SEE). See <https://html.spec.whatwg.org/multipage/server-sent-events.html> for details.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.run_output_stream import RunOutputStream
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.RunsApi(api_client)
    run_id = 'run_id_example' # str | The ID of the run.

    try:
        # Stream the run output
        api_response = api_instance.get_run_stream(run_id)
        print("The response of RunsApi->get_run_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->get_run_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The ID of the run. | 

### Return type

[**RunOutputStream**](RunOutputStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of agent results either as &#x60;RunResult&#x60; objects or custom objects, according to the specific streaming mode requested. Note that the stream of events is carried using the format specified in SSE spec &#x60;text/event-stream&#x60; |  -  |
**204** | No Output Available |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_run**
> Run resume_run(run_id, body)

Resume an interrupted Run

Provide the needed input to a run to resume its execution. Can only be called for runs that are in the interrupted state Schema of the provided input must match with the schema specified in the agent specs under interrupts for the interrupt type the agent generated for this specific interruption.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.run import Run
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.RunsApi(api_client)
    run_id = 'run_id_example' # str | The ID of the agent.
    body = None # object | 

    try:
        # Resume an interrupted Run
        api_response = api_instance.resume_run(run_id, body)
        print("The response of RunsApi->resume_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->resume_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The ID of the agent. | 
 **body** | **object**|  | 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_runs**
> List[Run] search_runs(run_search_request)

Search Runs

Search for runs.

This endpoint also functions as the endpoint to list all runs.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.run import Run
from acp_client_v0_1.models.run_search_request import RunSearchRequest
from acp_client_v0_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = acp_client_v0_1.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with acp_client_v0_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acp_client_v0_1.RunsApi(api_client)
    run_search_request = acp_client_v0_1.RunSearchRequest() # RunSearchRequest | 

    try:
        # Search Runs
        api_response = api_instance.search_runs(run_search_request)
        print("The response of RunsApi->search_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->search_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_search_request** | [**RunSearchRequest**](RunSearchRequest.md)|  | 

### Return type

[**List[Run]**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

