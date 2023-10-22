## DSF-CLI - Cloud Accounts:
Example payloads for cloud accounts

### Usage:
`dsfcli cloud_accounts -h`

### List all cloud_accounts:
`dsfcli cloud_accounts read`

### Retrieve a specific cloud_accounts by id:
`dsfcli cloud_accounts read --id="arn:aws:rds:us-east-2:1234567890:db:your-db-name-here"`

### Create a cloud_account from input string:
`dsfcli cloud_accounts create --json=''`

### Create a cloud_account from local file:
`dsfcli cloud_accounts create --json="$(cat < cloud_account_AWS.json)"`

### Update a data_source from input string by id:
`dsfcli cloud_accounts update --json='{"data": {"assetData": {"asset_display_name": "your-aws-ec2-iam-role-cloud-asset","arn": "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway","asset_id": "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway","admin_email": "test@imperva.com","connections": [{"reason": "default","connectionData": {"auth_mechanism": "default","region": "us-east-1",}}]},"serverType": "AWS","gatewayId": "12345-abcde-12345-abcde-12345"}}' --id="arn:aws:iam::658749227924:role/some-role-for-sonar-gateway"`

### Update a cloud_account from local file by id:
`dsfcli cloud_account update --json="$(cat < cloud_account_AWS.json)" --id="arn:aws:iam::658749227924:role/some-role-for-sonar-gateway"`

### Delete a cloud_account by id:
`dsfcli cloud_account delete --id="arn:aws:iam::658749227924:role/some-role-for-sonar-gateway"`


#### Config Options ####

`data.admin_email` [string] - _(required)_ The email address to notify about this asset Default Value: null

`data.arn` [string] - _(required)_ Amazon Resource Name - format is arn:partition:service:region:account-id and used as the asset_id Default Value: ""

`data.asset_display_name` [string] - _(required)_ User-friendly name of the asset, defined by user. Default Value: ""

`data.asset_id` [string] - _(required)_  Default Value: null

`data.asset_source` [string] - _(optional)_ The source platform/vendor/system of the asset data. Usually the service responsible for creating that asset document Default Value: ""

`data.available_regions` [string] - _(optional)_ A list of regions to use in discovery actions that iterate through region Default Value: null

`data.aws_proxy_config` [map] - _(optional)_ AWS specific proxy configuration Default Value: null

`data.credentials_endpoint` [string] - _(optional)_ A specific sts endpoint to use Default Value: null

`data.criticality` [options] - _(optional)_ The asset's importance to the business. These values are measured on a scale from "Most critical" (1) to "Least critical" (4). Allowed values: 1, 2, 3, 4 Default Value: null

`data.gateway_id` [string] - _(required)_  Default Value: null

`data.jsonar_uid` [string] - _(optional)_ Unique identifier (UID) attached to the Sonar machine controlling the asset Default Value: null

`data.location` [string] - _(optional)_ Current human-readable description of the physical location of the asset, or region. Default Value: null

`data.managed_by` [string] - _(optional)_ Email of the person who maintains the asset; can be different from the owner specified in the owned_by field. Defaults to admin_email. Default Value: null

`data.owned_by` [string] - _(optional)_ Email of Owner / person responsible for the asset; can be different from the person in the managed_by field. Defaults to admin_email. Default Value: null

`data.proxy` [string] - _(optional)_ Proxy to use for AWS calls if aws_proxy_config is populated the proxy field will get populated from the http value there Default Value: null

`data.region` [string] - _(optional)_ For cloud systems with regions, the default region or region used with this asset Default Value: null

`data.server_host_name` [string] - _(required)_ Hostname (or IP if name is unknown) Default Value: null

`data.server_port` [string] - _(optional)_  Default Value: "443"

`data.service_endpoints` [map] - _(optional)_ Specify particular endpoints for a given service in the form of <service name>: "endpoint" Default Value: null

`data.used_for` [options] - _(optional)_ Designates how this asset is used / the environment that the asset is supporting. Default Value: null Possible Values: Production`, `Test`, `Development`, `Demonstration`, `QA`, `Staging`, `Training`, `Disaster Recovery

`data.version` [string] - _(optional)_ Denotes the version of the asset Default Value: null

`data.connections[].connectionData.access_id` [string] - _(required)_ The Access key ID of AWS secret access key used to authenticate Default Value: null

`data.connections[].connectionData.amazon_secret` [map] - _(optional)_ Configuration to integrate with AWS Secrets Manager Default Value: null

`data.connections[].connectionData.ca_certs_path` [string] - _(optional)_ Certificate authority certificates path; what location should the sysetm look for certificate information from. Equivalent to --capath in a curl call Default Value: null

`data.connections[].connectionData.client_secret` [string] - _(required)_ This a string containing a secret used by the application to prove its identity when requesting a token. You can get a secret by going to Azure Active Directory -> App Registrations -> Owned Applications, selecting the desired application and then going to Certificates & secrets -> Client secrets -> + New client secret Default Value: null

`data.connections[].connectionData.credential_fields` [map] - _(optional)_ Document containing values to build a profile from. Filling this will create a profile using the given profile name Default Value: null

`data.connections[].connectionData.external_id` [string] - _(optional)_ External ID to use when assuming a role Default Value: null

`data.connections[].connectionData.hashicorp_secret` [map] - _(optional)_ Configuration to integrate with HashiCorp Vault Default Value: null

`data.connections[].connectionData.key_file` [string] - _(required)_ Location on disk on the key to be used to authenticate Default Value: null

`data.connections[].connectionData.region` [string] - _(required)_ Default AWS region for this asset Default Value: null

`data.connections[].connectionData.role_name` [string] - _(optional)_ What role is used to get credentials from. Default Value: ""

`data.connections[].connectionData.secret_key` [string] - _(required)_ The Secret access key used to authenticate Default Value: null

`data.connections[].connectionData.ssl` [bool] - _(optional)_ If true, use SSL when connecting Default Value: null

`data.connections[].connectionData.username` [string] - _(required)_ The name of a profile in /imperva/local/credentials/.aws/credentials to use for authenticating Default Value: null



