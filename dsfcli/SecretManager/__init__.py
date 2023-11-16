from .secret_manager_crud import create, read, update, delete
from .secret_manager_operations import test_connection_operation, sync_asset_operation


def secret_manager_parse(subparsers):
    secret_manager_parser = subparsers.add_parser('secret_manager',
                                               help='Create and manage secret managers using the API.',
                                               usage='dsf [options] secret_manager <command> [options]')
    secret_manager_subparsers = secret_manager_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    secret_manager_create_parser = secret_manager_subparsers.add_parser('create', help='Create a new secret manager.',
                                                                  usage=get_help("dsf secret_manager create"))
    secret_manager_create_parser.add_argument('json', help='The JSON object to POST.')
    secret_manager_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    secret_manager_create_parser.set_defaults(func=create)

    secret_manager_read_parser = secret_manager_subparsers.add_parser('read', help='Retrieve secret manager details by id.',
                                                               usage=get_help("dsf secret_manager read"))
    secret_manager_read_parser.add_argument('--id', help='The secret_manager ID.')
    secret_manager_read_parser.set_defaults(func=read)

    secret_manager_update_parser = secret_manager_subparsers.add_parser('update', help='Update an existing secret manager by id.',
                                                                  usage=get_help("dsf secret_manager update"))
    secret_manager_update_parser.add_argument('id', help='The secret_manager ID.')
    secret_manager_update_parser.add_argument('json', help='The JSON object to PUT.')
    secret_manager_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    secret_manager_update_parser.set_defaults(func=update)

    secret_manager_delete_parser = secret_manager_subparsers.add_parser('delete', help='Delete secret manager by id..',
                                                                  usage=get_help("dsf secret_manager delete"))
    secret_manager_delete_parser.add_argument('id', help='The secret_manager ID.')
    secret_manager_delete_parser.set_defaults(func=delete)

    sync_asset_operation_parser = secret_manager_subparsers.add_parser('sync', help='Sync a general asset between the DSF Hub and the Gateways.',
                                                               usage=get_help("dsf secret_manager sync"))
    sync_asset_operation_parser.add_argument('id', help='The secret_manager ID.')
    sync_asset_operation_parser.set_defaults(func=sync_asset_operation)

    test_connection_operation_parser = secret_manager_subparsers.add_parser('test', help='Test general asset connection.',
                                                               usage=get_help("dsf secret_manager test"))
    test_connection_operation_parser.add_argument('purpose', help='The purpose for the test.')
    test_connection_operation_parser.add_argument('id', help='The secret_manager ID.')
    test_connection_operation_parser.set_defaults(func=test_connection_operation)


def get_help(match):
    import os
    pwd = os.path.dirname(__file__)
    doc = "README.md"
    abs_path = os.path.join(pwd, doc)
    new_line = "\nEXAMPLES:\n"
    lines = open(abs_path, "r").readlines()
    for line in lines:
        if f"{match}" in line:
            clean_line = line.replace("<br /><br />", "")
            new_line += f"{clean_line}\n"
    return new_line