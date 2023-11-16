import json
from swagger_client import LogAggregatorsApi, ApiClient
from swagger_client.rest import ApiException


def create(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return instance.create_asset2(json.loads(param["json"]), async_req=param["sync_type"])
    except ApiException as e:
        return e


def read(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return instance.get_asset2(param["id"])
        else:
            return instance.get_assets2()
    except ApiException as e:
        return e


def update(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return instance.update_asset_full2(json.loads(param["json"]), param["id"], async_req=param["sync_type"])
    except ApiException as e:
        return e


def delete(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return instance.delete_asset2(param["id"])
    except ApiException as e:
        return e