# DSF-CLI - Data Sources:

## Usage:
	dsfcli data_sources -h

## List all data_sources:
	dsfcli data_source read
## Retrieve a specific data_source by id:
	dsfcli data_source read --id="arn:aws:rds:us-east-2:1234567890:db:your-db-name-here"

## Create a data_source from input string:
	python3 -m dsfcli data_source create '{"data": {"assetData": {"asset_display_name": "arn:aws:rds:us-east-2:123456789:db:your-host-here","arn": "arn:aws:rds:us-east-2:123456789:db:your-host-here","Server Host Name": "your-db.endpoint.us-east-2.rds.amazonaws.com","admin_email": "test@imperva.com","connections": []},"serverType": "AWS RDS MYSQL","gatewayId": "12345-abcde-12345-abcde"}}'

## Create a data_source from local file:
    python3 -m dsfcli data_source create --json="$(cat < examples/data_source_AWS_RDS_MYSQL.json)"

## Update a data_source from input string by id:
    python3 -m dsfcli data_source update --json='{"data": {"assetData": {"asset_display_name": "arn:aws:rds:us-east-2:123456789:db:your-host-here","arn": "arn:aws:rds:us-east-2:123456789:db:your-host-here","Server Host Name": "your-db.endpoint.us-east-2.rds.amazonaws.com","admin_email": "test@imperva.com","connections": []},"serverType": "AWS RDS MYSQL","gatewayId": "12345-abcde-12345-abcde"}}' --id="arn:aws:rds:us-east-2:123456789:db:your-host-here"

## Update a data_source from local file by id:
    python3 -m dsfcli data_source update --json="$(cat < examples/data_source_AWS_RDS_MYSQL.json)" --id="arn:aws:rds:us-east-2:123456789:db:your-host-here"

## Delete a data_source by id:
    python3 -m dsfcli data_source delete --id="arn:aws:rds:us-east-2:123456789:db:your-host-here"
