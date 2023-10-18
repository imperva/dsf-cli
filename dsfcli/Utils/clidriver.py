import os
import argparse
import json
from ..DataSources import data_source_parse
from ..SecretManager import secret_manager_parse
from ..CloudAccount import cloud_account_parse
from ..LogAggregator import log_aggregator_parse
from ..GeneralAssets import general_assets_parse
import dsfcli
from swagger_client import Configuration
from swagger_client.rest import ApiException
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DSF_HOST = os.getenv("IMPV_DSF_HOST")
DSF_TOKEN = os.getenv("IMPV_DSF_TOKEN")
DSF_DEBUG = bool(os.getenv("IMPV_DSF_DEBUG", False))

configuration = Configuration()
configuration.verify_ssl = False
configuration.api_key["Authorization"] = "Bearer {}".format(DSF_TOKEN)
configuration.host = DSF_HOST
configuration.debug = DSF_DEBUG

parser = argparse.ArgumentParser(prog='dsfcli',
                                 usage='%(prog)s <resource> <command> [options]',
                                 description="CLI for gateway, asset CRUD on DSF via API.")
parser.add_argument('--version', action='version', version=dsfcli.__version__)
subparsers = parser.add_subparsers()

data_source_parser = data_source_parse(subparsers)
secret_manager_parser = secret_manager_parse(subparsers)
cloud_account_parser = cloud_account_parse(subparsers)
log_aggregator_parser = log_aggregator_parse(subparsers)
general_assets_parser = general_assets_parse(subparsers)


def main(args=None):
    args = parser.parse_args(args=args)
    response = args.func(args, configuration)

    if type(response) == ApiException:
        print("Status code: {}".format(response.status))
        print(response)
    else:
        print(json.dumps(response, sort_keys=True, indent=4))





    # gw_instance = swagger_client.GatewaysApi(swagger_client.ApiClient(configuration))
    # print(json.dumps(gw_instance.get_gateways(), indent=4))
    #
    # new_ds = {
    #     "data": {
    #         "assetData": {
    #             "asset_display_name": "arn:aws:rds:us-east-2:658749227924:db:impv-isbt-db",
    #             "arn": "arn:aws:rds:us-east-2:658749227924:db:impv-isbt-db",
    #             "Server Host Name": "impv-isbt-db.cswkrvdhm46x.us-east-2.rds.amazonaws.com",
    #             "admin_email": "ba@imperva.com",
    #             "connections": []
    #         },
    #         "serverType": "AWS RDS MYSQL",
    #         "gatewayId": "e33bfbe4-a93a-c4e5-8e9c-6e5558c2e2cd"
    #     }
    # }
    # api_instance = swagger_client.DataSourcesApi(swagger_client.ApiClient(configuration))
    # body = swagger_client.APIDataAssetDto()
    # print(json.dumps(api_instance.create_asset3(new_ds), indent=4))
    #
    #





