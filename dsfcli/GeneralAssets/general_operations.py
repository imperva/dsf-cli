import json
from swagger_client import GeneralAssetsApi, ApiClient
from swagger_client.rest import ApiException


def sync_asset_operation(args, configuration):
    param = vars(args)
    instance = GeneralAssetsApi(ApiClient(configuration))
    try:
        return instance.sync_asset_operation1(id=param["id"])
    except ApiException as e:
        return e


def test_connection_operation(args, configuration):
    param = vars(args)
    instance = GeneralAssetsApi(ApiClient(configuration))
    try:
        return instance.test_connection_operation1(id=param["id"], purpose=param["purpose"])
    except ApiException as e:
        return e