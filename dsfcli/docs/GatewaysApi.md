# swagger_client.GatewaysApi

All URIs are relative to */dsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gateways**](GatewaysApi.md#get_gateways) | **GET** /api/v2/gateways | Get all gateways

# **get_gateways**
> get_gateways()

Get all gateways

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
api_instance = swagger_client.GatewaysApi(swagger_client.ApiClient(configuration))

try:
    # Get all gateways
    api_instance.get_gateways()
except ApiException as e:
    print("Exception when calling GatewaysApi->get_gateways: %s\n" % e)
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

