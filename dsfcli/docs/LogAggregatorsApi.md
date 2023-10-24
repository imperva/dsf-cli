# swagger_client.LogAggregatorsApi

All URIs are relative to */dsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset2**](LogAggregatorsApi.md#create_asset2) | **POST** /api/v2/log-aggregators | Create a new log aggregator
[**delete_asset2**](LogAggregatorsApi.md#delete_asset2) | **DELETE** /api/v2/log-aggregators/{id} | Delete a log aggregator
[**disable_audit_collection_operation**](LogAggregatorsApi.md#disable_audit_collection_operation) | **POST** /api/v2/log-aggregators/{id}/operations/disable-audit-collection | Disable log aggregator audit collection
[**enable_audit_collection_operation**](LogAggregatorsApi.md#enable_audit_collection_operation) | **POST** /api/v2/log-aggregators/{id}/operations/enable-audit-collection | Enable log aggregator audit collection
[**get_asset2**](LogAggregatorsApi.md#get_asset2) | **GET** /api/v2/log-aggregators/{id} | Get a log aggregator
[**get_assets2**](LogAggregatorsApi.md#get_assets2) | **GET** /api/v2/log-aggregators | Get all log aggregators
[**sync_asset_operation2**](LogAggregatorsApi.md#sync_asset_operation2) | **POST** /api/v2/log-aggregators/{id}/operations/sync-with-gateway | Sync a log aggregator between the DSF Hub and the Gateways
[**test_connection_operation2**](LogAggregatorsApi.md#test_connection_operation2) | **POST** /api/v2/log-aggregators/{id}/operations/test-connection | Test log aggregator connection
[**update_asset_full2**](LogAggregatorsApi.md#update_asset_full2) | **PUT** /api/v2/log-aggregators/{id} | Update a log aggregator with full update semantics
[**update_asset_partial2**](LogAggregatorsApi.md#update_asset_partial2) | **POST** /api/v2/log-aggregators/{id} | Update a log aggregator with partial update semantics

# **create_asset2**
> create_asset2(body, sync_type=sync_type)

Create a new log aggregator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Create a new log aggregator
    api_instance.create_asset2(body, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->create_asset2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIDataAssetDto**](APIDataAssetDto.md)| Details | 
 **sync_type** | **str**| Determines whether to sync this operation with the gateways. \&quot;Blocking\&quot; here means the request will wait for the sync operation to complete before getting a response from the server. | [optional] [default to SYNC_GW_BLOCKING]

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset2**
> delete_asset2(id)

Delete a log aggregator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a log aggregator
    api_instance.delete_asset2(id)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->delete_asset2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_audit_collection_operation**
> disable_audit_collection_operation(id)

Disable log aggregator audit collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Disable log aggregator audit collection
    api_instance.disable_audit_collection_operation(id)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->disable_audit_collection_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_audit_collection_operation**
> enable_audit_collection_operation(id)

Enable log aggregator audit collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Enable log aggregator audit collection
    api_instance.enable_audit_collection_operation(id)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->enable_audit_collection_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset2**
> get_asset2(id)

Get a log aggregator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a log aggregator
    api_instance.get_asset2(id)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->get_asset2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets2**
> get_assets2()

Get all log aggregators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))

try:
    # Get all log aggregators
    api_instance.get_assets2()
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->get_assets2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_asset_operation2**
> sync_asset_operation2(id)

Sync a log aggregator between the DSF Hub and the Gateways

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Sync a log aggregator between the DSF Hub and the Gateways
    api_instance.sync_asset_operation2(id)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->sync_asset_operation2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection_operation2**
> test_connection_operation2(id, purpose)

Test log aggregator connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
purpose = 'purpose_example' # str | 

try:
    # Test log aggregator connection
    api_instance.test_connection_operation2(id, purpose)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->test_connection_operation2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **purpose** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_full2**
> update_asset_full2(body, id, sync_type=sync_type)

Update a log aggregator with full update semantics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a log aggregator with full update semantics
    api_instance.update_asset_full2(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->update_asset_full2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIDataAssetDto**](APIDataAssetDto.md)| Details | 
 **id** | **str**|  | 
 **sync_type** | **str**| Determines whether to sync this operation with the gateways. \&quot;Blocking\&quot; here means the request will wait for the sync operation to complete before getting a response from the server. | [optional] [default to SYNC_GW_BLOCKING]

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_partial2**
> update_asset_partial2(body, id, sync_type=sync_type)

Update a log aggregator with partial update semantics

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: auth_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.LogAggregatorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a log aggregator with partial update semantics
    api_instance.update_asset_partial2(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling LogAggregatorsApi->update_asset_partial2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIDataAssetDto**](APIDataAssetDto.md)| Details | 
 **id** | **str**|  | 
 **sync_type** | **str**| Determines whether to sync this operation with the gateways. \&quot;Blocking\&quot; here means the request will wait for the sync operation to complete before getting a response from the server. | [optional] [default to SYNC_GW_BLOCKING]

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

