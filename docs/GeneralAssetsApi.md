# swagger_client.GeneralAssetsApi

All URIs are relative to */dsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset1**](GeneralAssetsApi.md#create_asset1) | **POST** /api/v2/others | Create a new general asset
[**delete_asset1**](GeneralAssetsApi.md#delete_asset1) | **DELETE** /api/v2/others/{id} | Delete a general asset
[**get_asset1**](GeneralAssetsApi.md#get_asset1) | **GET** /api/v2/others/{id} | Get a general asset
[**get_assets1**](GeneralAssetsApi.md#get_assets1) | **GET** /api/v2/others | Get all general assets
[**sync_asset_operation1**](GeneralAssetsApi.md#sync_asset_operation1) | **POST** /api/v2/others/{id}/operations/sync-with-gateway | Sync a general asset between the DSF Hub and the Gateways
[**test_connection_operation1**](GeneralAssetsApi.md#test_connection_operation1) | **POST** /api/v2/others/{id}/operations/test-connection | Test general asset connection
[**update_asset_full1**](GeneralAssetsApi.md#update_asset_full1) | **PUT** /api/v2/others/{id} | Update a general asset with full update semantics
[**update_asset_partial1**](GeneralAssetsApi.md#update_asset_partial1) | **POST** /api/v2/others/{id} | Update a general asset with partial update semantics

# **create_asset1**
> create_asset1(body, sync_type=sync_type)

Create a new general asset

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Create a new general asset
    api_instance.create_asset1(body, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->create_asset1: %s\n" % e)
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

# **delete_asset1**
> delete_asset1(id)

Delete a general asset

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a general asset
    api_instance.delete_asset1(id)
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->delete_asset1: %s\n" % e)
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

# **get_asset1**
> get_asset1(id)

Get a general asset

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a general asset
    api_instance.get_asset1(id)
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->get_asset1: %s\n" % e)
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

# **get_assets1**
> get_assets1()

Get all general assets

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))

try:
    # Get all general assets
    api_instance.get_assets1()
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->get_assets1: %s\n" % e)
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

# **sync_asset_operation1**
> sync_asset_operation1(id)

Sync a general asset between the DSF Hub and the Gateways

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Sync a general asset between the DSF Hub and the Gateways
    api_instance.sync_asset_operation1(id)
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->sync_asset_operation1: %s\n" % e)
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

# **test_connection_operation1**
> test_connection_operation1(id, purpose)

Test general asset connection

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
purpose = 'purpose_example' # str | 

try:
    # Test general asset connection
    api_instance.test_connection_operation1(id, purpose)
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->test_connection_operation1: %s\n" % e)
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

# **update_asset_full1**
> update_asset_full1(body, id, sync_type=sync_type)

Update a general asset with full update semantics

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a general asset with full update semantics
    api_instance.update_asset_full1(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->update_asset_full1: %s\n" % e)
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

# **update_asset_partial1**
> update_asset_partial1(body, id, sync_type=sync_type)

Update a general asset with partial update semantics

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
api_instance = swagger_client.GeneralAssetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a general asset with partial update semantics
    api_instance.update_asset_partial1(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling GeneralAssetsApi->update_asset_partial1: %s\n" % e)
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

