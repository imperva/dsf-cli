# swagger_client.SecretManagersApi

All URIs are relative to */dsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](SecretManagersApi.md#create_asset) | **POST** /api/v2/secret-managers | Create a new secret manager
[**delete_asset**](SecretManagersApi.md#delete_asset) | **DELETE** /api/v2/secret-managers/{id} | Delete a secret manager
[**get_asset**](SecretManagersApi.md#get_asset) | **GET** /api/v2/secret-managers/{id} | Get a secret manager
[**get_assets**](SecretManagersApi.md#get_assets) | **GET** /api/v2/secret-managers | Get all secret managers
[**sync_asset_operation**](SecretManagersApi.md#sync_asset_operation) | **POST** /api/v2/secret-managers/{id}/operations/sync-with-gateway | Sync a secret manager asset between the DSF Hub and the Gateways
[**test_connection_operation**](SecretManagersApi.md#test_connection_operation) | **POST** /api/v2/secret-managers/{id}/operations/test-connection | Test secret manager connection
[**update_asset_full**](SecretManagersApi.md#update_asset_full) | **PUT** /api/v2/secret-managers/{id} | Update a secret manager with full update semantics
[**update_asset_partial**](SecretManagersApi.md#update_asset_partial) | **POST** /api/v2/secret-managers/{id} | Update a secret manager with partial update semantics

# **create_asset**
> create_asset(body, sync_type=sync_type)

Create a new secret manager

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Create a new secret manager
    api_instance.create_asset(body, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling SecretManagersApi->create_asset: %s\n" % e)
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

# **delete_asset**
> delete_asset(id)

Delete a secret manager

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a secret manager
    api_instance.delete_asset(id)
except ApiException as e:
    print("Exception when calling SecretManagersApi->delete_asset: %s\n" % e)
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

# **get_asset**
> get_asset(id)

Get a secret manager

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a secret manager
    api_instance.get_asset(id)
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_asset: %s\n" % e)
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

# **get_assets**
> get_assets()

Get all secret managers

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))

try:
    # Get all secret managers
    api_instance.get_assets()
except ApiException as e:
    print("Exception when calling SecretManagersApi->get_assets: %s\n" % e)
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

# **sync_asset_operation**
> sync_asset_operation(id)

Sync a secret manager asset between the DSF Hub and the Gateways

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Sync a secret manager asset between the DSF Hub and the Gateways
    api_instance.sync_asset_operation(id)
except ApiException as e:
    print("Exception when calling SecretManagersApi->sync_asset_operation: %s\n" % e)
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

# **test_connection_operation**
> test_connection_operation(id, purpose)

Test secret manager connection

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
purpose = 'purpose_example' # str | 

try:
    # Test secret manager connection
    api_instance.test_connection_operation(id, purpose)
except ApiException as e:
    print("Exception when calling SecretManagersApi->test_connection_operation: %s\n" % e)
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

# **update_asset_full**
> update_asset_full(body, id, sync_type=sync_type)

Update a secret manager with full update semantics

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a secret manager with full update semantics
    api_instance.update_asset_full(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling SecretManagersApi->update_asset_full: %s\n" % e)
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

# **update_asset_partial**
> update_asset_partial(body, id, sync_type=sync_type)

Update a secret manager with partial update semantics

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
api_instance = swagger_client.SecretManagersApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a secret manager with partial update semantics
    api_instance.update_asset_partial(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling SecretManagersApi->update_asset_partial: %s\n" % e)
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

