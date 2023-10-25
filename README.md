# Data Security Fabric (DSF) Hub CLI

The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to manage DSF configurations and processes via the [DSF Open API](https://docs.imperva.com/bundle/v4.13-sonar-user-guide/page/84552.htm) easily integrating into configurations management, orchestration or automation frameworks to support the DevOps model.

## Installation
    pip3 install dsf-cli

## Authentication - Setting up the required environment variables:
Set [environment variables](https://en.wikipedia.org/wiki/Environment_variable) to configure a token for authentication, and the specific hub endpoint, example:  

	export IMPV_DSF_HOST="https://1.2.3.4:8443"  
    export IMPV_DSF_TOKEN="abcde-1234-efghi-6789-12345abcde"  
	export IMPV_DSF_DEBUG=True (Optional to see cli debug logs in terminal output)  

[CLICK HERE](https://docs.imperva.com/bundle/v4.13-sonar-user-guide/page/84555.htm) to see how create a token to authenticate.

## Running the CLI
	dsf -h
	dsf data_source -h
	dsf data_source read

## Check out run locally not as pip package
	git clone git@github.com:imperva/dsf-cli.git
	cd dsf-cli
	python3 -m dsfcli -h

This CLI is a Python 3 application and has been tested with Python 3.6 -> 3.8
## Requirements:
    python 3.6 or higher

## Confirm your version of python if installed:
    Open a terminal
    Enter: python -V or python3 -V

## Usage:
    usage: dsf <resource> <command> [options]

    CLI for data_source, account and security CRUD on DSF via API.

    positional arguments:
      {data_source,secret_manager,cloud_account,log_aggregator,general_assets}
		data_source         Create and manage data sources the API.
		secret_manager      Create and manage secret managers using the API.
		cloud_account       Create and manage cloud accounts using the API.
		log_aggregator      Create and manage log aggregators for your account using the API.
		general_assets      Create and manage general assets using the API.
		gateway				Read list of all gateways using the API.

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit

## Installing the correct version for environment:
https://www.python.org/downloads/

Examples by resource type:
1. [Cloud Accounts](https://github.com/imperva/dsf-cli/blob/main/dsfcli/CloudAccount/)
1. [Data Sources](https://github.com/imperva/dsf-cli/blob/main/dsfcli/DataSources/)
1. [Gateways](https://github.com/imperva/dsf-cli/blob/main/dsfcli/Gateways/)
1. [Log Aggregators](https://github.com/imperva/dsf-cli/blob/main/dsfcli/LogAggregator/)
1. [Secret Managers](https://github.com/imperva/dsf-cli/blob/main/dsfcli/SecretManager/)