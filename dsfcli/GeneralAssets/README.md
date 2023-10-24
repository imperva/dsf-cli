# DSF-CLI - Data Sources:

## Usage:
`dsfcli general_asset -h`

## List all general_asset:
`dsfcli general_asset read`

## Retrieve a specific general_asset by id:
`dsfcli general_asset read "<asset_id>"`<br /><br />
`dsfcli general_asset read "arn:aws:rds:us-east-2:1234567890:db:your-db-name-here"`

## Create a general_asset from input string:
`dsfcli general_asset create '<json-object>'`<br /><br />
`python3 -m dsfcli general_asset create '{"data": {"assetData": {"asset_display_name": "arn:aws:rds:us-east-2:123456789:db:your-host-here","arn": "arn:aws:rds:us-east-2:123456789:db:your-host-here","Server Host Name": "your-db.endpoint.us-east-2.rds.amazonaws.com","admin_email": "test@imperva.com","connections": []},"serverType": "AWS RDS MYSQL","gatewayId": "12345-abcde-12345-abcde"}}'`

## Create a general_asset from local file:
`dsfcli general_asset create "<asset_id>" '<json-object>'`<br /><br />
`python3 -m dsfcli general_asset create "$(cat < examples/general_asset_AWS_RDS_MYSQL.json)"`

## Update a general_asset from input string by id:
`dsfcli general_asset update "<asset_id>" '<json-object>'`<br /><br />
`python3 -m dsfcli general_asset update "arn:aws:rds:us-east-2:123456789:db:your-host-here" '{"data": {"assetData": {"asset_display_name": "arn:aws:rds:us-east-2:123456789:db:your-host-here","arn": "arn:aws:rds:us-east-2:123456789:db:your-host-here","Server Host Name": "your-db.endpoint.us-east-2.rds.amazonaws.com","admin_email": "test@imperva.com","connections": []},"serverType": "AWS RDS MYSQL","gatewayId": "12345-abcde-12345-abcde"}}'`

## Update a general_asset from local file by id:
`dsfcli general_asset update "<asset_id>" '<json-object>'`<br /><br />
`python3 -m dsfcli general_asset update "$(cat < examples/general_asset_AWS_RDS_MYSQL.json)" "arn:aws:rds:us-east-2:123456789:db:your-host-here"`

## Delete a general_asset by id:
`dsfcli general_asset delete "<asset_id>" '<json-object>'`<br /><br />
`python3 -m dsfcli general_asset delete "arn:aws:rds:us-east-2:123456789:db:your-host-here"`
