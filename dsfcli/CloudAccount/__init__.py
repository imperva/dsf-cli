import json
from swagger_client import CloudAccountsApi, ApiClient
from swagger_client.rest import ApiException


def cloud_account_parse(subparsers):
    cloud_account_parser = subparsers.add_parser('cloud_account',
                                               help='Create and manage cloud accounts using the API.',
                                               usage='dsfcli [options] cloud_account <command> [options]')
    cloud_account_subparsers = cloud_account_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    cloud_account_create_parser = cloud_account_subparsers.add_parser('create', help='Create a new cloud account.',
                                                                  usage='dsfcli [options] cloud_account create "<asset_id>"')
    cloud_account_create_parser.add_argument('json', help='The JSON object to POST.')
    cloud_account_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    cloud_account_create_parser.set_defaults(func=create)

    cloud_account_read_parser = cloud_account_subparsers.add_parser('read', help='Retrieve cloud account details by id.',
                                                               usage='dsfcli [options] cloud_account read "<asset_id>"')
    cloud_account_read_parser.add_argument('--id', help='The cloud_account ID.')
    cloud_account_read_parser.set_defaults(func=read)

    cloud_account_update_parser = cloud_account_subparsers.add_parser('update', help='Update an existing cloud account by id.',
                                                                  usage='dsfcli [options] cloud_account update "<asset_id>"')
    cloud_account_update_parser.add_argument('id', help='The cloud_account ID.')
    cloud_account_update_parser.add_argument('json', help='The JSON object to PUT.')
    cloud_account_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    cloud_account_update_parser.set_defaults(func=update)

    cloud_account_delete_parser = cloud_account_subparsers.add_parser('delete', help='Delete cloud account by id.',
                                                                  usage='dsfcli [options] cloud_account delete "<asset_id>"')
    cloud_account_delete_parser.add_argument('id', help='The cloud_account ID.')
    cloud_account_delete_parser.set_defaults(func=delete)


def create(args, configuration):
    param = vars(args)
    ca_instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return ca_instance.create_asset4(json.loads(param["json"]), async_req=param["sync_type"])
    except ApiException as e:
        return e


def read(args, configuration):
    param = vars(args)
    ca_instance = CloudAccountsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return ca_instance.get_asset4(param["id"])
        else:
            return ca_instance.get_assets4()
    except ApiException as e:
        return e


def update(args, configuration):
    param = vars(args)
    ca_instance = CloudAccountsApi(ApiClient(configuration))
    try:
        return ca_instance.update_asset_full4(json.loads(param["json"]), param["id"], async_req=param["sync_type"])
    except ApiException as e:
        return e


def delete(args, configuration):
    param = vars(args)
    ca_instance = CloudAccountsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return ca_instance.delete_asset4(param["id"])
    except ApiException as e:
        return e
