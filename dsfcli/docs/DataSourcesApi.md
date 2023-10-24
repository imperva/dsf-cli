# swagger_client.DataSourcesApi

All URIs are relative to */dsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset3**](DataSourcesApi.md#create_asset3) | **POST** /api/v2/data-sources | Create a new data source
[**delete_asset3**](DataSourcesApi.md#delete_asset3) | **DELETE** /api/v2/data-sources/{id} | Delete a data source
[**disable_audit_collection_operation1**](DataSourcesApi.md#disable_audit_collection_operation1) | **POST** /api/v2/data-sources/{id}/operations/disable-audit-collection | Disable data source audit collection
[**enable_audit_collection_operation1**](DataSourcesApi.md#enable_audit_collection_operation1) | **POST** /api/v2/data-sources/{id}/operations/enable-audit-collection | Enable data source audit collection
[**get_asset3**](DataSourcesApi.md#get_asset3) | **GET** /api/v2/data-sources/{id} | Get a data source
[**get_assets3**](DataSourcesApi.md#get_assets3) | **GET** /api/v2/data-sources | Get all data sources
[**sync_asset_operation3**](DataSourcesApi.md#sync_asset_operation3) | **POST** /api/v2/data-sources/{id}/operations/sync-with-gateway | Sync a data source between the DSF Hub and the Gateways
[**test_connection_operation3**](DataSourcesApi.md#test_connection_operation3) | **POST** /api/v2/data-sources/{id}/operations/test-connection | Test data source connection
[**update_asset_full3**](DataSourcesApi.md#update_asset_full3) | **PUT** /api/v2/data-sources/{id} | Update a data source with full update semantics
[**update_asset_partial3**](DataSourcesApi.md#update_asset_partial3) | **POST** /api/v2/data-sources/{id} | Update a data source with partial update semantics

# **create_asset3**
> create_asset3(body, sync_type=sync_type)

Create a new data source

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Create a new data source
    api_instance.create_asset3(body, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling DataSourcesApi->create_asset3: %s\n" % e)
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

# **delete_asset3**
> delete_asset3(id)

Delete a data source

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a data source
    api_instance.delete_asset3(id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->delete_asset3: %s\n" % e)
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

# **disable_audit_collection_operation1**
> disable_audit_collection_operation1(id)

Disable data source audit collection

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Disable data source audit collection
    api_instance.disable_audit_collection_operation1(id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->disable_audit_collection_operation1: %s\n" % e)
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

# **enable_audit_collection_operation1**
> enable_audit_collection_operation1(id)

Enable data source audit collection

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Enable data source audit collection
    api_instance.enable_audit_collection_operation1(id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->enable_audit_collection_operation1: %s\n" % e)
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

# **get_asset3**
> get_asset3(id)

Get a data source

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a data source
    api_instance.get_asset3(id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_asset3: %s\n" % e)
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

# **get_assets3**
> get_assets3()

Get all data sources

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))

try:
    # Get all data sources
    api_instance.get_assets3()
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_assets3: %s\n" % e)
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

# **sync_asset_operation3**
> sync_asset_operation3(id)

Sync a data source between the DSF Hub and the Gateways

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Sync a data source between the DSF Hub and the Gateways
    api_instance.sync_asset_operation3(id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->sync_asset_operation3: %s\n" % e)
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

# **test_connection_operation3**
> test_connection_operation3(id, purpose)

Test data source connection

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
purpose = 'purpose_example' # str | 

try:
    # Test data source connection
    api_instance.test_connection_operation3(id, purpose)
except ApiException as e:
    print("Exception when calling DataSourcesApi->test_connection_operation3: %s\n" % e)
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

# **update_asset_full3**
> update_asset_full3(body, id, sync_type=sync_type)

Update a data source with full update semantics

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a data source with full update semantics
    api_instance.update_asset_full3(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling DataSourcesApi->update_asset_full3: %s\n" % e)
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

# **update_asset_partial3**
> update_asset_partial3(body, id, sync_type=sync_type)

Update a data source with partial update semantics

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
api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
body = swagger_client.APIDataAssetDto() # APIDataAssetDto | Details
id = 'id_example' # str | 
sync_type = 'SYNC_GW_BLOCKING' # str | Determines whether to sync this operation with the gateways. \"Blocking\" here means the request will wait for the sync operation to complete before getting a response from the server. (optional) (default to SYNC_GW_BLOCKING)

try:
    # Update a data source with partial update semantics
    api_instance.update_asset_partial3(body, id, sync_type=sync_type)
except ApiException as e:
    print("Exception when calling DataSourcesApi->update_asset_partial3: %s\n" % e)
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

