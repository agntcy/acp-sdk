# acp_client_v0_1.ThreadsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_thread**](ThreadsApi.md#create_thread) | **POST** /threads | Create an empty Thread
[**delete_thread**](ThreadsApi.md#delete_thread) | **DELETE** /threads/{thread_id} | Delete a thread. If the thread contains any pending run, deletion fails.
[**get_run_threadstate**](ThreadsApi.md#get_run_threadstate) | **GET** /runs/{run_id}/threadstate | Retrieve the thread state at the end of the run
[**get_thread**](ThreadsApi.md#get_thread) | **GET** /threads/{thread_id} | Get a previously created Thread
[**get_thread_history**](ThreadsApi.md#get_thread_history) | **GET** /threads/{thread_id}/history | Retrieve the list of runs and associated state at the end of each run.
[**get_thread_state**](ThreadsApi.md#get_thread_state) | **GET** /threads/{thread_id}/state | Retrieve the current state associated with the thread
[**search_threads**](ThreadsApi.md#search_threads) | **POST** /threads/search | Search Threads


# **create_thread**
> Thread create_thread(thread_create)

Create an empty Thread

Create an empty thread. This is useful to associate metadata to a thread.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.thread import Thread
from acp_client_v0_1.models.thread_create import ThreadCreate
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
    api_instance = acp_client_v0_1.ThreadsApi(api_client)
    thread_create = acp_client_v0_1.ThreadCreate() # ThreadCreate | 

    try:
        # Create an empty Thread
        api_response = api_instance.create_thread(thread_create)
        print("The response of ThreadsApi->create_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->create_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_create** | [**ThreadCreate**](ThreadCreate.md)|  | 

### Return type

[**Thread**](Thread.md)

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

# **delete_thread**
> Thread delete_thread(thread_id)

Delete a thread. If the thread contains any pending run, deletion fails.

Delete a thread.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.thread import Thread
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
    api_instance = acp_client_v0_1.ThreadsApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of the thread.

    try:
        # Delete a thread. If the thread contains any pending run, deletion fails.
        api_response = api_instance.delete_thread(thread_id)
        print("The response of ThreadsApi->delete_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->delete_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of the thread. | 

### Return type

[**Thread**](Thread.md)

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

# **get_run_threadstate**
> object get_run_threadstate(run_id)

Retrieve the thread state at the end of the run

This call can be used only for agents that support thread, i.e. for Runs that specify a thread ID. It can be called only on runs that are in `success` status. It returns the thread state at the end of the Run. Can be used to reconstruct the evolution of the thread state in its history.

### Example


```python
import acp_client_v0_1
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
    api_instance = acp_client_v0_1.ThreadsApi(api_client)
    run_id = 'run_id_example' # str | The ID of the run.

    try:
        # Retrieve the thread state at the end of the run
        api_response = api_instance.get_run_threadstate(run_id)
        print("The response of ThreadsApi->get_run_threadstate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->get_run_threadstate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The ID of the run. | 

### Return type

**object**

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

# **get_thread**
> Thread get_thread(thread_id)

Get a previously created Thread

Get a thread from its ID. 

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.thread import Thread
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
    api_instance = acp_client_v0_1.ThreadsApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of the thread.

    try:
        # Get a previously created Thread
        api_response = api_instance.get_thread(thread_id)
        print("The response of ThreadsApi->get_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->get_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of the thread. | 

### Return type

[**Thread**](Thread.md)

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

# **get_thread_history**
> List[Run] get_thread_history(thread_id)

Retrieve the list of runs and associated state at the end of each run.

Retrieve ordered list of runs for this thread in chronological order.

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
    api_instance = acp_client_v0_1.ThreadsApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of the thread.

    try:
        # Retrieve the list of runs and associated state at the end of each run.
        api_response = api_instance.get_thread_history(thread_id)
        print("The response of ThreadsApi->get_thread_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->get_thread_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of the thread. | 

### Return type

[**List[Run]**](Run.md)

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

# **get_thread_state**
> object get_thread_state(thread_id)

Retrieve the current state associated with the thread

Retrieve the the current state associated with the thread

### Example


```python
import acp_client_v0_1
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
    api_instance = acp_client_v0_1.ThreadsApi(api_client)
    thread_id = 'thread_id_example' # str | The ID of the thread.

    try:
        # Retrieve the current state associated with the thread
        api_response = api_instance.get_thread_state(thread_id)
        print("The response of ThreadsApi->get_thread_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->get_thread_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of the thread. | 

### Return type

**object**

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

# **search_threads**
> List[Thread] search_threads(thread_search_request)

Search Threads

Search for threads.

This endpoint also functions as the endpoint to list all threads.

### Example


```python
import acp_client_v0_1
from acp_client_v0_1.models.thread import Thread
from acp_client_v0_1.models.thread_search_request import ThreadSearchRequest
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
    api_instance = acp_client_v0_1.ThreadsApi(api_client)
    thread_search_request = acp_client_v0_1.ThreadSearchRequest() # ThreadSearchRequest | 

    try:
        # Search Threads
        api_response = api_instance.search_threads(thread_search_request)
        print("The response of ThreadsApi->search_threads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreadsApi->search_threads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_search_request** | [**ThreadSearchRequest**](ThreadSearchRequest.md)|  | 

### Return type

[**List[Thread]**](Thread.md)

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

