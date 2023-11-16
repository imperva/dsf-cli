import json
from swagger_client import DataSourcesApi, ApiClient
from swagger_client.rest import ApiException


def create(args, configuration):
    param = vars(args)
    instance = DataSourcesApi(ApiClient(configuration))
    try:
        return instance.create_asset3(json.loads(param["json"]), async_req=param["sync_type"])
    except ApiException as e:
        return e


def read(args, configuration):
    param = vars(args)
    instance = DataSourcesApi(ApiClient(configuration))
    try:
        if param["id"]:
            return instance.get_asset3(param["id"])
        else:
            return instance.get_assets3()
    except ApiException as e:
        return e


def update(args, configuration):
    param = vars(args)
    instance = DataSourcesApi(ApiClient(configuration))
    try:
        return instance.update_asset_full3(json.loads(param["json"]), param["id"], async_req=param["sync_type"])
    except ApiException as e:
        return e


def delete(args, configuration):
    param = vars(args)
    instance = DataSourcesApi(ApiClient(configuration))
    try:
        if param["id"]:
            return instance.delete_asset3(param["id"])
    except ApiException as e:
        return e