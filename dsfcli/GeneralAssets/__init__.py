import json
from swagger_client import GeneralAssetsApi, ApiClient, Configuration
from swagger_client.rest import ApiException


def general_assets_parse(subparsers):
    general_assets_parser = subparsers.add_parser('general_assets',
                                               help='Manage secrets for your account using the API.',
                                               usage='dsfcli [options] general_assets <command> [options]')
    general_assets_subparsers = general_assets_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    general_assets_create_parser = general_assets_subparsers.add_parser('create', help='Create a new data source.',
                                                                  usage='dsfcli [options] general_assets get general_assets_id')
    general_assets_create_parser.add_argument('json', help='The JSON object to POST.')
    general_assets_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    general_assets_create_parser.set_defaults(func=create)

    general_assets_read_parser = general_assets_subparsers.add_parser('read', help='Retrieve data source details',
                                                               usage='dsfcli [options] general_assets get general_assets_id')
    general_assets_read_parser.add_argument('--id', help='The general_assets ID.')
    general_assets_read_parser.set_defaults(func=read)

    general_assets_update_parser = general_assets_subparsers.add_parser('update', help='Update an existing data source.',
                                                                  usage='dsfcli [options] general_assets get general_assets_id')
    general_assets_update_parser.add_argument('id', help='The general_assets ID.')
    general_assets_update_parser.add_argument('json', help='The JSON object to PUT.')
    general_assets_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    general_assets_update_parser.set_defaults(func=update)

    general_assets_delete_parser = general_assets_subparsers.add_parser('delete', help='Delete data source.',
                                                                  usage='dsfcli [options] general_assets delete general_assets_id')
    general_assets_delete_parser.add_argument('id', help='The general_assets ID.')
    general_assets_delete_parser.set_defaults(func=delete)


def create(args, configuration):
    param = vars(args)
    ga_instance = GeneralAssetsApi(ApiClient(configuration))
    try:
        return ga_instance.create_asset1(json.loads(param["json"]), async_req=param["sync_type"])
    except ApiException as e:
        return e


def read(args, configuration):
    param = vars(args)
    ga_instance = GeneralAssetsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return ga_instance.get_asset1(param["id"])
        else:
            return ga_instance.get_assets1()
    except ApiException as e:
        return e


def update(args, configuration):
    param = vars(args)
    ga_instance = GeneralAssetsApi(ApiClient(configuration))
    try:
        return ga_instance.update_asset_full1(json.loads(param["json"]), param["id"], async_req=param["sync_type"])
    except ApiException as e:
        return e


def delete(args, configuration):
    param = vars(args)
    ga_instance = GeneralAssetsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return ga_instance.delete_asset1(param["id"])
    except ApiException as e:
        return e
