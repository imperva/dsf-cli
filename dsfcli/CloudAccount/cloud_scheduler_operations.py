import json
from swagger_client import CloudAccountsApi, ApiClient
from swagger_client.rest import ApiException


def create_scheduled_discovery(args, configuration):
    param = vars(args)
    instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return instance.create_scheduled_discovery(json.loads(param["json"]), id=param["id"])
    except ApiException as e:
        return e


def read_scheduled_discovery(args, configuration):
    param = vars(args)
    instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return instance.get_scheduled_discovery(id=param["id"])
    except ApiException as e:
        return e


def update_scheduled_discovery(args, configuration):
    param = vars(args)
    instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return instance.update_scheduled_discovery(json.loads(param["json"]), id=param["id"])
    except ApiException as e:
        return e


def trigger_discovery_operation(args, configuration):
    param = vars(args)
    instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return instance.trigger_discovery_operation(json.loads(param["json"]), id=param["id"])
    except ApiException as e:
        return e


def sync_asset_operation(args, configuration):
    param = vars(args)
    instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return instance.sync_asset_operation4(id=param["id"])
    except ApiException as e:
        return e


def test_connection_operation(args, configuration):
    param = vars(args)
    instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return instance.test_connection_operation4(id=param["id"], purpose=param["purpose"])
    except ApiException as e:
        return e

