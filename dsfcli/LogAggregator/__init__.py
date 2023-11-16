from .log_agg_crud import create, read, update, delete
from .log_agg_scheduler_operations import enable_audit_collection_operation, disable_audit_collection_operation, \
    test_connection_operation, sync_asset_operation


def log_aggregator_parse(subparsers):
    log_aggregator_parser = subparsers.add_parser('log_aggregator',
                                               help='Create and manage log aggregators for your account using the API.',
                                               usage='dsf [options] log_aggregator <command> [options]')
    log_aggregator_subparsers = log_aggregator_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    log_aggregator_create_parser = log_aggregator_subparsers.add_parser('create', help='Create a new log aggregator.',
                                                                  usage=get_help("dsf log_aggregator create"))
    log_aggregator_create_parser.add_argument('json', help='The JSON object to POST.')
    log_aggregator_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    log_aggregator_create_parser.set_defaults(func=create)

    log_aggregator_read_parser = log_aggregator_subparsers.add_parser('read', help='Retrieve log aggregator details by id.',
                                                               usage=get_help("dsf log_aggregator read"))
    log_aggregator_read_parser.add_argument('--id', help='The log_aggregator ID.')
    log_aggregator_read_parser.set_defaults(func=read)

    log_aggregator_update_parser = log_aggregator_subparsers.add_parser('update', help='Update an existing log aggregator by id.',
                                                                  usage=get_help("dsf log_aggregator update"))
    log_aggregator_update_parser.add_argument('id', help='The log_aggregator ID.')
    log_aggregator_update_parser.add_argument('json', help='The JSON object to PUT.')
    log_aggregator_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    log_aggregator_update_parser.set_defaults(func=update)

    log_aggregator_delete_parser = log_aggregator_subparsers.add_parser('delete', help='Delete log aggregator by id.',
                                                                  usage=get_help("dsf log_aggregator delete"))
    log_aggregator_delete_parser.add_argument('id', help='The log_aggregator ID.')
    log_aggregator_delete_parser.set_defaults(func=delete)

    sync_asset_operation_parser = log_aggregator_subparsers.add_parser('sync', help='Sync a log aggregator between the DSF Hub and the Gateways.',
                                                               usage=get_help("dsf log_aggregator sync"))
    sync_asset_operation_parser.add_argument('id', help='The log_aggregator ID.')
    sync_asset_operation_parser.set_defaults(func=sync_asset_operation)

    test_connection_operation_parser = log_aggregator_subparsers.add_parser('test', help='Test log aggregator connection.',
                                                               usage=get_help("dsf log_aggregator test"))
    test_connection_operation_parser.add_argument('purpose', help='The purpose for the test.')
    test_connection_operation_parser.add_argument('id', help='The log_aggregator ID.')
    test_connection_operation_parser.set_defaults(func=test_connection_operation)

    sync_asset_operation_parser = log_aggregator_subparsers.add_parser('enable_audit', help='Enable log aggregator audit collection.',
                                                               usage=get_help("dsf log_aggregator enable_audit"))
    sync_asset_operation_parser.add_argument('id', help='The log_aggregator ID.')
    sync_asset_operation_parser.set_defaults(func=enable_audit_collection_operation)

    sync_asset_operation_parser = log_aggregator_subparsers.add_parser('disable_audit', help='Disable log aggregator audit collection.',
                                                               usage=get_help("dsf log_aggregator disable_audit"))
    sync_asset_operation_parser.add_argument('id', help='The log_aggregator ID.')
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