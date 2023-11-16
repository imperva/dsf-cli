from .general_crud import create, read, update, delete
from .general_operations import test_connection_operation, sync_asset_operation


def general_assets_parse(subparsers):
    general_assets_parser = subparsers.add_parser('general_asset',
                                               help='Create and manage general assets using the API.',
                                               usage='dsf [options] general_asset <command> [options]')
    general_assets_subparsers = general_assets_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    general_assets_create_parser = general_assets_subparsers.add_parser('create', help='Create a new general assets.',
                                                                  usage=get_help("dsf general_asset create"))
    general_assets_create_parser.add_argument('json', help='The JSON object to POST.')
    general_assets_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    general_assets_create_parser.set_defaults(func=create)

    general_assets_read_parser = general_assets_subparsers.add_parser('read', help='Retrieve general asset details by id.',
                                                               usage=get_help("dsf general_asset read"))
    general_assets_read_parser.add_argument('--id', help='The general_assets ID.')
    general_assets_read_parser.set_defaults(func=read)

    general_assets_update_parser = general_assets_subparsers.add_parser('update', help='Update an existing general assets by id.',
                                                                  usage=get_help("dsf general_asset update"))
    general_assets_update_parser.add_argument('id', help='The general_assets ID.')
    general_assets_update_parser.add_argument('json', help='The JSON object to PUT.')
    general_assets_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    general_assets_update_parser.set_defaults(func=update)

    general_assets_delete_parser = general_assets_subparsers.add_parser('delete', help='Delete general assets by id.',
                                                                  usage=get_help("dsf general_asset delete"))
    general_assets_delete_parser.add_argument('id', help='The general_assets ID.')
    general_assets_delete_parser.set_defaults(func=delete)

    sync_asset_operation_parser = general_assets_subparsers.add_parser('sync', help='Sync a general asset between the DSF Hub and the Gateways.',
                                                               usage=get_help("dsf general_asset sync"))
    sync_asset_operation_parser.add_argument('id', help='The general_assets ID.')
    sync_asset_operation_parser.set_defaults(func=sync_asset_operation)

    test_connection_operation_parser = general_assets_subparsers.add_parser('test', help='Test general asset connection.',
                                                               usage=get_help("dsf general_asset test"))
    test_connection_operation_parser.add_argument('purpose', help='The purpose for the test.')
    test_connection_operation_parser.add_argument('id', help='The general_assets ID.')
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