import json
from swagger_client import DataSourcesApi, ApiClient
from swagger_client.rest import ApiException


def data_source_parse(subparsers):
    data_source_parser = subparsers.add_parser('data_source',
                                               help='Create and manage data sources the API.',
                                               usage='dsfcli [options] data_source <command> [options]')
    data_source_subparsers = data_source_parser.add_subparsers(description='valid subcommands',
                                                               help='additional help')

    data_source_create_parser = data_source_subparsers.add_parser('create', help='Create a new data source.',
                                                                  usage='dsfcli [options] data_source create data_source_id')
    data_source_create_parser.add_argument('json', help='The JSON object to POST.')
    data_source_create_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    data_source_create_parser.set_defaults(func=create)

    data_source_read_parser = data_source_subparsers.add_parser('read', help='Retrieve data source details by id.',
                                                               usage='dsfcli [options] data_source read data_source_id')
    data_source_read_parser.add_argument('--id', help='The data_source ID.')
    data_source_read_parser.set_defaults(func=read)

    data_source_update_parser = data_source_subparsers.add_parser('update', help='Update an existing data source by id.',
                                                                  usage='dsfcli [options] data_source update data_source_id')
    data_source_update_parser.add_argument('id', help='The data_source ID.')
    data_source_update_parser.add_argument('json', help='The JSON object to PUT.')
    data_source_update_parser.add_argument('--sync_type', default='', help='Determines whether to sync this operation with the gateways. '
                                                                           '\"Blocking\" here means the request will wait for the sync operation'
                                                                           ' to complete before getting a response from the server. '
                                                                           '(optional) (default to SYNC_GW_BLOCKING)')
    data_source_update_parser.set_defaults(func=update)

    data_source_delete_parser = data_source_subparsers.add_parser('delete', help='Delete data source by id.',
                                                                  usage='dsfcli [options] data_source delete data_source_id')
    data_source_delete_parser.add_argument('id', help='The data_source ID.')
    data_source_delete_parser.set_defaults(func=delete)


def create(args, configuration):
    param = vars(args)
    ds_instance = DataSourcesApi(ApiClient(configuration))
    try:
        return ds_instance.create_asset3(json.loads(param["json"]), async_req=param["sync_type"])
    except ApiException as e:
        return e


def read(args, configuration):
    param = vars(args)
    ds_instance = DataSourcesApi(ApiClient(configuration))
    try:
        if param["id"]:
            return ds_instance.get_asset3(param["id"])
        else:
            return ds_instance.get_assets3()
    except ApiException as e:
        return e


def update(args, configuration):
    param = vars(args)
    ds_instance = DataSourcesApi(ApiClient(configuration))
    try:
        return ds_instance.update_asset_full3(json.loads(param["json"]), param["id"], async_req=param["sync_type"])
    except ApiException as e:
        return e


def delete(args, configuration):
    param = vars(args)
    ds_instance = DataSourcesApi(ApiClient(configuration))
    try:
        if param["id"]:
            return ds_instance.delete_asset3(param["id"])
    except ApiException as e:
        return e
