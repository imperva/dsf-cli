import json
from swagger_client import SecretManagersApi, ApiClient
from swagger_client.rest import ApiException


def sync_asset_operation(args, configuration):
    param = vars(args)
    instance = SecretManagersApi(ApiClient(configuration))
    try:
        return instance.sync_asset_operation(id=param["id"])
    except ApiException as e:
        return e


def test_connection_operation(args, configuration):
    param = vars(args)
    instance = SecretManagersApi(ApiClient(configuration))
    try:
        return instance.test_connection_operation(id=param["id"], purpose=param["purpose"])
    except ApiException as e:
        return e