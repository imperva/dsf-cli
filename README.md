# Data Security Fabric (DSF) Hub - Command Line Interface (CLI)

The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to manage DSF configurations and processes via the [DSF Open API](https://docs.imperva.com/bundle/v4.13-sonar-user-guide/page/84552.htm) easily integrating into configurations management, orchestration or automation frameworks to support the DevOps model.

## Installation
    pip3 install dsf-cli

## Check out run locally not as pip package
	git clone git@github.com:imperva/dsf-cli.git
	cd dsf-cli
	python3 -m dsfcli -h

## Running the CLI

This CLI is a Python 3 application and has been tested with Python 3.6 -> 3.8
## Requirements:
    python 3.6 or higher

## Confirm your version of python if installed:
    Open a terminal
    Enter: python -V or python3 -V

## Setting up the required environment variables:
    Set [environment variables](https://en.wikipedia.org/wiki/Environment_variable) to configure a token for authentication, and the specific hub endpoint:
    IMPV_DSF_TOKEN (required, example: https://1.2.3.4:8443)
    IMPV_DSF_HOST (required, [click here](https://docs.imperva.com/bundle/v4.13-sonar-user-guide/page/84555.htm) to see how create a token, example: abcde-1234-efghi-6789-12345abcde)
	IMPV_DSF_DEBUG (optional to see cli debug logs in terminal output)

## Usage:
    usage: dsfcli <resource> <command> [options]

    CLI for data_source, account and security CRUD on DSF via API.

    positional arguments:
      {data_source,secret_manager,cloud_account,log_aggregator,general_assets}
		data_source         Create and manage data sources the API.
		secret_manager      Create and manage secret managers using the API.
		cloud_account       Create and manage cloud accounts using the API.
		log_aggregator      Create and manage log aggregators for your account using the API.
		general_assets      Create and manage general assets using the API.

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit

## Installing the correct version for environment:
https://www.python.org/downloads/

Examples by resource type:
1. [Cloud Accounts](https://github.com/imperva/dsf-cli/tree/main/docs/cloud_accounts)
1. [Data Sources](https://github.com/imperva/data_sources)
1. [Log Aggregators](https://github.com/imperva/log_aggregators)
1. [Secret Managers](https://github.com/imperva/secret_managers)