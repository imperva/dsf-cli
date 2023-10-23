import json
from swagger_client import LogAggregatorsApi, ApiClient
from swagger_client.rest import ApiException


def log_aggregator_parse(subparsers):
    log_aggregator_parser = subparsers.add_parser('log_aggregator',
                                               help='Create and manage log aggregators for your account using the API.',
                                               usage='dsfcli [options] log_aggregator <command> [options]')
    log_aggregator_subparsers = log_aggregator_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    log_aggregator_create_parser = log_aggregator_subparsers.add_parser('create', help='Create a new log aggregator.',
                                                                  usage='dsfcli [options] log_aggregator create "<asset_id>"')
    log_aggregator_create_parser.add_argument('json', help='The JSON object to POST.')
    log_aggregator_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    log_aggregator_create_parser.set_defaults(func=create)

    log_aggregator_read_parser = log_aggregator_subparsers.add_parser('read', help='Retrieve log aggregator details by id.',
                                                               usage='dsfcli [options] log_aggregator read "<asset_id>"')
    log_aggregator_read_parser.add_argument('--id', help='The log_aggregator ID.')
    log_aggregator_read_parser.set_defaults(func=read)

    log_aggregator_update_parser = log_aggregator_subparsers.add_parser('update', help='Update an existing log aggregator by id.',
                                                                  usage='dsfcli [options] log_aggregator update "<asset_id>"')
    log_aggregator_update_parser.add_argument('id', help='The log_aggregator ID.')
    log_aggregator_update_parser.add_argument('json', help='The JSON object to PUT.')
    log_aggregator_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    log_aggregator_update_parser.set_defaults(func=update)

    log_aggregator_delete_parser = log_aggregator_subparsers.add_parser('delete', help='Delete log aggregator by id.',
                                                                  usage='dsfcli [options] log_aggregator delete "<asset_id>"')
    log_aggregator_delete_parser.add_argument('id', help='The log_aggregator ID.')
    log_aggregator_delete_parser.set_defaults(func=delete)


def create(args, configuration):
    param = vars(args)
    la_instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return la_instance.create_asset2(json.loads(param["json"]), async_req=param["sync_type"])
    except ApiException as e:
        return e


def read(args, configuration):
    param = vars(args)
    la_instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return la_instance.get_asset2(param["id"])
        else:
            return la_instance.get_assets2()
    except ApiException as e:
        return e


def update(args, configuration):
    param = vars(args)
    la_instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        return la_instance.update_asset_full2(json.loads(param["json"]), param["id"], async_req=param["sync_type"])
    except ApiException as e:
        return e


def delete(args, configuration):
    param = vars(args)
    la_instance = LogAggregatorsApi(ApiClient(configuration))
    try:
        if param["id"]:
            return la_instance.delete_asset2(param["id"])
    except ApiException as e:
        return e
