import json
from swagger_client import SecretManagersApi, ApiClient
from swagger_client.rest import ApiException


def secret_manager_parse(subparsers):
    secret_manager_parser = subparsers.add_parser('secret_manager',
                                               help='Create and manage secret managers using the API.',
                                               usage='dsfcli [options] secret_manager <command> [options]')
    secret_manager_subparsers = secret_manager_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    secret_manager_create_parser = secret_manager_subparsers.add_parser('create', help='Create a new secret manager.',
                                                                  usage='dsfcli [options] secret_manager create secret_manager_id')
    secret_manager_create_parser.add_argument('json', help='The JSON object to POST.')
    secret_manager_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    secret_manager_create_parser.set_defaults(func=create)

    secret_manager_read_parser = secret_manager_subparsers.add_parser('read', help='Retrieve secret manager details by id.',
                                                               usage='dsfcli [options] secret_manager read secret_manager_id')
    secret_manager_read_parser.add_argument('--id', help='The secret_manager ID.')
    secret_manager_read_parser.set_defaults(func=read)

    secret_manager_update_parser = secret_manager_subparsers.add_parser('update', help='Update an existing secret manager by id.',
                                                                  usage='dsfcli [options] secret_manager update secret_manager_id')
    secret_manager_update_parser.add_argument('id', help='The secret_manager ID.')
    secret_manager_update_parser.add_argument('json', help='The JSON object to PUT.')
    secret_manager_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    secret_manager_update_parser.set_defaults(func=update)

    secret_manager_delete_parser = secret_manager_subparsers.add_parser('delete', help='Delete secret manager by id..',
                                                                  usage='dsfcli [options] secret_manager delete secret_manager_id')
    secret_manager_delete_parser.add_argument('id', help='The secret_manager ID.')
    secret_manager_delete_parser.set_defaults(func=delete)


def create(args, configuration):
    param = vars(args)
    sm_instance = SecretManagersApi(ApiClient(configuration))
    try:
        return sm_instance.create_asset(json.loads(param["json"]), async_req=param["sync_type"])
    except ApiException as e:
        return e


def read(args, configuration):
    param = vars(args)
    sm_instance = SecretManagersApi(ApiClient(configuration))
    try:
        if param["id"]:
            return sm_instance.get_asset(param["id"])
        else:
            return sm_instance.get_assets()
    except ApiException as e:
        return e


def update(args, configuration):
    param = vars(args)
    sm_instance = SecretManagersApi(ApiClient(configuration))
    try:
        return sm_instance.update_asset_full(json.loads(param["json"]), param["id"], async_req=param["sync_type"])
    except ApiException as e:
        return e


def delete(args, configuration):
    param = vars(args)
    sm_instance = SecretManagersApi(ApiClient(configuration))
    try:
        if param["id"]:
            return sm_instance.delete_asset(param["id"])
    except ApiException as e:
        return e
