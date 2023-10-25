import json
from swagger_client import GatewaysApi, ApiClient
from swagger_client.rest import ApiException


def gateway_parse(subparsers):
    gateway_parse = subparsers.add_parser('gateway',
                                               help='Get all gateways from DSF Hub.',
                                               usage='dsf gateway read')
    gateway_subparse = gateway_parse.add_subparsers(description='valid subcommands',
                                                               help='additional help')
    gateway_read_parser = gateway_subparse.add_parser('read', help='Get all gateways from DSF Hub.',
                                                               usage="Get all gateways from DSF Hub.")
    gateway_read_parser.set_defaults(func=read)


def read(args, configuration):
    gw_instance = GatewaysApi(ApiClient(configuration))
    try:
        return gw_instance.get_gateways()
    except ApiException as e:
        return e