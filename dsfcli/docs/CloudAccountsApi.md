# swagger_client.CloudAccountsApi

All URIs are relative to */dsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset4**](CloudAccountsApi.md#create_asset4) | **POST** /api/v2/cloud-accounts | Create a new cloud account
[**create_scheduled_discovery**](CloudAccountsApi.md#create_scheduled_discovery) | **POST** /api/v2/cloud-accounts/{id}/scheduled-discovery | Create scheduled discovery
[**delete_asset4**](CloudAccountsApi.md#delete_asset4) | **DELETE** /api/v2/cloud-accounts/{id} | Delete a cloud account
[**get_asset4**](CloudAccountsApi.md#get_asset4) | **GET** /api/v2/cloud-accounts/{id} | Get a cloud account
[**get_assets4**](CloudAccountsApi.md#get_assets4) | **GET** /api/v2/cloud-accounts | Get all cloud accounts
[**get_scheduled_discovery**](CloudAccountsApi.md#get_scheduled_discovery) | **GET** /api/v2/cloud-accounts/{id}/scheduled-discovery | Get scheduled discovery
[**sync_asset_operation4**](CloudAccountsApi.md#sync_asset_operation4) | **POST** /api/v2/cloud-accounts/{id}/operations/sync-with-gateway | Sync a cloud account between the DSF Hub and the Gateways
[**test_connection_operation4**](CloudAccountsApi.md#test_connection_operation4) | **POST** /api/v2/cloud-accounts/{id}/operations/test-connection | Test cloud account connection
[**trigger_discovery_operation**](CloudAccountsApi.md#trigger_discovery_operation) | **POST** /api/v2/cloud-accounts/{id}/operations/trigger-discovery | Trigger discovery operation
[**update_asset_full4**](CloudAccountsApi.md#update_asset_full4) | **PUT** /api/v2/cloud-accounts/{id} | Update a cloud account with full update semantics
[**update_asset_partial4**](CloudAccountsApi.md#update_asset_partial4) | **POST** /api/v2/cloud-accounts/{id} | Update a cloud account with partial update semantics
[**update_scheduled_discovery**](CloudAccountsApi.md#update_scheduled_discovery) | **PUT** /api/v2/cloud-accounts/{id}/scheduled-discovery | Update scheduled discovery

# **create_asset4**
> create_asset4(body, sync_type=sync_type)

Create a new cloud account

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Create a new cloud account
    api_instance.create_asset4(body, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->create_asset4: %s\n" % e)
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

# **create_scheduled_discovery**
> create_scheduled_discovery(body, id)

Create scheduled discovery

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataScheduleItemDto() # APIDataScheduleItemDto | Details of the item to be created
id = 'id_example' # str | 

try:
    # Create scheduled discovery
    api_instance.create_scheduled_discovery(body, id)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->create_scheduled_discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIDataScheduleItemDto**](APIDataScheduleItemDto.md)| Details of the item to be created | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset4**
> delete_asset4(id)

Delete a cloud account

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a cloud account
    api_instance.delete_asset4(id)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->delete_asset4: %s\n" % e)
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

# **get_asset4**
> get_asset4(id)

Get a cloud account

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a cloud account
    api_instance.get_asset4(id)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->get_asset4: %s\n" % e)
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

# **get_assets4**
> get_assets4()

Get all cloud accounts

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))

try:
    # Get all cloud accounts
    api_instance.get_assets4()
except ApiException as e:
    print("Exception when calling CloudAccountsApi->get_assets4: %s\n" % e)
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

# **get_scheduled_discovery**
> get_scheduled_discovery(id)

Get scheduled discovery

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get scheduled discovery
    api_instance.get_scheduled_discovery(id)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->get_scheduled_discovery: %s\n" % e)
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

# **sync_asset_operation4**
> sync_asset_operation4(id)

Sync a cloud account between the DSF Hub and the Gateways

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Sync a cloud account between the DSF Hub and the Gateways
    api_instance.sync_asset_operation4(id)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->sync_asset_operation4: %s\n" % e)
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

# **test_connection_operation4**
> test_connection_operation4(id, purpose)

Test cloud account connection

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
purpose = 'purpose_example' # str | 

try:
    # Test cloud account connection
    api_instance.test_connection_operation4(id, purpose)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->test_connection_operation4: %s\n" % e)
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

# **trigger_discovery_operation**
> trigger_discovery_operation(body, id)

Trigger discovery operation

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataDiscoveryRequestDto() # APIDataDiscoveryRequestDto | 
id = 'id_example' # str | 

try:
    # Trigger discovery operation
    api_instance.trigger_discovery_operation(body, id)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->trigger_discovery_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIDataDiscoveryRequestDto**](APIDataDiscoveryRequestDto.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_full4**
> update_asset_full4(body, id, sync_type=sync_type)

Update a cloud account with full update semantics

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a cloud account with full update semantics
    api_instance.update_asset_full4(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->update_asset_full4: %s\n" % e)
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

# **update_asset_partial4**
> update_asset_partial4(body, id, sync_type=sync_type)

Update a cloud account with partial update semantics

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a cloud account with partial update semantics
    api_instance.update_asset_partial4(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->update_asset_partial4: %s\n" % e)
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

# **update_scheduled_discovery**
> update_scheduled_discovery(body, id)

Update scheduled discovery

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
api_instance = swagger_client.CloudAccountsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataScheduleItemDto() # APIDataScheduleItemDto | Details of the item to be updated
id = 'id_example' # str | 

try:
    # Update scheduled discovery
    api_instance.update_scheduled_discovery(body, id)
except ApiException as e:
    print("Exception when calling CloudAccountsApi->update_scheduled_discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**APIDataScheduleItemDto**](APIDataScheduleItemDto.md)| Details of the item to be updated | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

