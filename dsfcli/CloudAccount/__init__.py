from .cloud_crud import create, read, update, delete
from .cloud_scheduler_operations import create_scheduled_discovery, read_scheduled_discovery, update_scheduled_discovery, \
    trigger_discovery_operation, sync_asset_operation, test_connection_operation


def cloud_account_parse(subparsers):
    cloud_account_parser = subparsers.add_parser('cloud_account',
                                               help='Create and manage cloud accounts using the API.',
                                               usage='dsf [options] cloud_account <command> [options]')
    cloud_account_subparsers = cloud_account_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    cloud_account_create_parser = cloud_account_subparsers.add_parser('create', help='Create a new cloud account.',
                                                                  usage=get_help("dsf cloud_account create"))
    cloud_account_create_parser.add_argument('json', help='The JSON object to POST.')
    cloud_account_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    cloud_account_create_parser.set_defaults(func=create)

    cloud_account_read_parser = cloud_account_subparsers.add_parser('read', help='Retrieve cloud account details by id.',
                                                               usage=get_help("dsf cloud_account read"))
    cloud_account_read_parser.add_argument('--id', help='The cloud_account ID.')
    cloud_account_read_parser.set_defaults(func=read)

    cloud_account_update_parser = cloud_account_subparsers.add_parser('update', help='Update an existing cloud account by id.',
                                                                  usage=get_help("dsf cloud_account update"))
    cloud_account_update_parser.add_argument('id', help='The cloud_account ID.')
    cloud_account_update_parser.add_argument('json', help='The JSON object to PUT.')
    cloud_account_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    cloud_account_update_parser.set_defaults(func=update)

    cloud_account_delete_parser = cloud_account_subparsers.add_parser('delete', help='Delete cloud account by id.',
                                                                  usage=get_help("dsf cloud_account delete"))
    cloud_account_delete_parser.add_argument('id', help='The cloud_account ID.')
    cloud_account_delete_parser.set_defaults(func=delete)

    create_scheduled_discovery_parser = cloud_account_subparsers.add_parser('csd', help='Create scheduled discovery.',
                                                                  usage=get_help("dsf cloud_account csd"))
    create_scheduled_discovery_parser.add_argument('json', help='The JSON object to POST.')
    create_scheduled_discovery_parser.add_argument('id', default='', help='Asset ID')
    create_scheduled_discovery_parser.set_defaults(func=create_scheduled_discovery)

    read_scheduled_discovery_parser = cloud_account_subparsers.add_parser('rsd', help='Get scheduled discovery.',
                                                               usage=get_help("dsf cloud_account rsd"))
    read_scheduled_discovery_parser.add_argument('id', help='The cloud_account ID.')
    read_scheduled_discovery_parser.set_defaults(func=read_scheduled_discovery)

    update_scheduled_discovery_parser = cloud_account_subparsers.add_parser('usd', help='Get scheduled discovery.',
                                                               usage=get_help("dsf cloud_account usd"))
    update_scheduled_discovery_parser.add_argument('json', help='The JSON object to POST.')
    update_scheduled_discovery_parser.add_argument('id', help='The cloud_account ID.')
    update_scheduled_discovery_parser.set_defaults(func=update_scheduled_discovery)

    trigger_discovery_operation_parser = cloud_account_subparsers.add_parser('trigger', help='Trigger discovery operation.',
                                                               usage=get_help("dsf cloud_account trigger"))
    trigger_discovery_operation_parser.add_argument('json', help='The JSON object to POST.')
    trigger_discovery_operation_parser.add_argument('id', help='The cloud_account ID.')
    trigger_discovery_operation_parser.set_defaults(func=trigger_discovery_operation)

    sync_asset_operation_parser = cloud_account_subparsers.add_parser('sync', help='Sync a cloud account between the DSF Hub and the Gateways.',
                                                               usage=get_help("dsf cloud_account sync"))
    sync_asset_operation_parser.add_argument('id', help='The cloud_account ID.')
    sync_asset_operation_parser.set_defaults(func=sync_asset_operation)

    test_connection_operation_parser = cloud_account_subparsers.add_parser('test', help='Test cloud account connection.',
                                                               usage=get_help("dsf cloud_account test"))
    test_connection_operation_parser.add_argument('purpose', help='The purpose for the test.')
    test_connection_operation_parser.add_argument('id', help='The cloud_account ID.')
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
