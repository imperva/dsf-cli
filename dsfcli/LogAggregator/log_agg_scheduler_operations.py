from swagger_client import LogAggregatorsApi, ApiClient
from swagger_client.rest import ApiException


def sync_asset_operation(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return instance.sync_asset_operation2(id=param["id"])
    except ApiException as e:
        return e


def test_connection_operation(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return instance.test_connection_operation2(id=param["id"], purpose=param["purpose"])
    except ApiException as e:
        return e


def enable_audit_collection_operation(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return instance.enable_audit_collection_operation(id=param["id"])
    except ApiException as e:
        return e


def disable_audit_collection_operation(args, configuration):
    param = vars(args)
    instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return instance.disable_audit_collection_operation(id=param["id"])
    except ApiException as e:
        return e