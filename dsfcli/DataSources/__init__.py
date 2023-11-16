from .data_source_crud import create, read, update, delete
from .data_source_scheduler_operations import test_connection_operation, sync_asset_operation, \
    disable_audit_collection_operation, enable_audit_collection_operation


def data_source_parse(subparsers):
    data_source_parser = subparsers.add_parser('data_source',
                                               help='Create and manage data sources the API.',
                                               usage='dsf [options] data_source <command> [options]')
    data_source_subparsers = data_source_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    data_source_create_parser = data_source_subparsers.add_parser('create', help='Create a new data source.',
                                                                  usage=get_help("dsf data_source create"))
    data_source_create_parser.add_argument('json', help='The JSON object to POST.')
    data_source_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    data_source_create_parser.set_defaults(func=create)

    data_source_read_parser = data_source_subparsers.add_parser('read', help='Retrieve data source details by id.',
                                                               usage=get_help("dsf data_source read"))
    data_source_read_parser.add_argument('--id', help='The data_source ID.')
    data_source_read_parser.set_defaults(func=read)

    data_source_update_parser = data_source_subparsers.add_parser('update', help='Update an existing data source by id.',
                                                                  usage=get_help("dsf data_source update"))
    data_source_update_parser.add_argument('id', help='The data_source ID.')
    data_source_update_parser.add_argument('json', help='The JSON object to PUT.')
    data_source_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    data_source_update_parser.set_defaults(func=update)

    data_source_delete_parser = data_source_subparsers.add_parser('delete', help='Delete data source by id.',
                                                                  usage=get_help("dsf data_source delete"))
    data_source_delete_parser.add_argument('id', help='The data_source ID.')
    data_source_delete_parser.set_defaults(func=delete)

    sync_asset_operation_parser = data_source_subparsers.add_parser('sync', help='Sync a data source between the DSF Hub and the Gateways.',
                                                               usage=get_help("dsf data_source sync"))
    sync_asset_operation_parser.add_argument('id', help='The data_source ID.')
    sync_asset_operation_parser.set_defaults(func=sync_asset_operation)

    test_connection_operation_parser = data_source_subparsers.add_parser('test', help='Test data source connection.',
                                                               usage=get_help("dsf data_source test"))
    test_connection_operation_parser.add_argument('purpose', help='The purpose for the test.')
    test_connection_operation_parser.add_argument('id', help='The data_source ID.')
    test_connection_operation_parser.set_defaults(func=test_connection_operation)

    sync_asset_operation_parser = data_source_subparsers.add_parser('enable_audit', help='Enable data source audit collection.',
                                                               usage=get_help("dsf data_source enable_audit"))
    sync_asset_operation_parser.add_argument('id', help='The data_source ID.')
    sync_asset_operation_parser.set_defaults(func=enable_audit_collection_operation)

    sync_asset_operation_parser = data_source_subparsers.add_parser('disable_audit', help='Disable data source audit collection.',
                                                               usage=get_help("dsf data_source disable_audit"))
    sync_asset_operation_parser.add_argument('id', help='The data_source ID.')
    sync_asset_operation_parser.set_defaults(func=disable_audit_collection_operation)


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