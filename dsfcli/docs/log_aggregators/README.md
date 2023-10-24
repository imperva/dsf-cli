## DSF-CLI - Log Aggregators:
[Click here](https://github.com/imperva/dsf-cli/tree/main/dsfcli/docs/log_aggregators/examples) for example payloads for optional and required fields for all log aggregator types.

### Usage:
`dsfcli log_aggregator -h`

### List all log_aggregators:
`dsfcli log_aggregator read`

### Retrieve a specific log_aggregator by id:
`dsfcli log_aggregator read "<asset_id>"`<br /><br />
`dsfcli log_aggregator read "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2"`

### Create a log_aggregator from input string:
`dsfcli log_aggregator create '<json-object>'`<br /><br />
`dsfcli log_aggregator create '{"data": {"assetData": {"asset_display_name": "some-log-group-asset","arn": "arn:aws:logs:us-east-1:1234567890:log-group:/aws/rds/instance/my-database/audit:*","admin_email": "test@imperva.com","parent_asset_id": "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2","connections": [{"reason": "default","connectionData": {"auth_mechanism": "default","region": "us-east-1"}}]},"serverType": "AWS LOG GROUP","parentAssetId": "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2","gatewayId": "60343559-211f-4d8a-9477-8042720bae58"}}'`

### Create a log_aggregator from local file:
`dsfcli log_aggregator create '<json-object>'`<br /><br />
`dsfcli log_aggregator create "$(cat < log_aggregator_AWS.json)"`

### Update a data_source from input string by id:
`dsfcli log_aggregator update "<asset_id>" '<json-object>'`<br /><br />
`dsfcli log_aggregator update "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2" '{"data": {"assetData": {"asset_display_name": "some-log-group-asset","arn": "arn:aws:logs:us-east-1:1234567890:log-group:/aws/rds/instance/my-database/audit:*","admin_email": "test@imperva.com","parent_asset_id": "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2","connections": [{"reason": "default","connectionData": {"auth_mechanism": "default","region": "us-east-1"}}]},"serverType": "AWS LOG GROUP","parentAssetId": "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2","gatewayId": "60343559-211f-4d8a-9477-8042720bae58"}}'`

### Update a log_aggregator from local file by id:
`dsfcli log_aggregator update "<asset_id>" '<json-object>'`<br /><br />
`dsfcli log_aggregator update "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2" "$(cat < log_aggregator_AWS.json)" "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2"`

### Delete a log_aggregator by id:
`dsfcli log_aggregator delete "<asset_id>"`<br /><br />
`dsfcli log_aggregator delete "arn:aws:iam::658749227924:role/some-role-for-sonar-gateway2"`

#### Config Options ####

`data.admin_email` [string] - _(required)_ The email address to notify about this asset Default Value: null

`data.arn` [string] - _(required)_ Amazon Resource Name - format is arn:partition:service:region:account-id and used as the asset_id Default Value: ""

`data.asset_display_name` [string] - _(required)_ User-friendly name of the asset, defined by user. Default Value: ""

`data.asset_id` [string] - _(required)_  Default Value: null

`data.asset_source` [string] - _(optional)_ The source platform/vendor/system of the asset data. Usually the service responsible for creating that asset document Default Value: ""

`data.audit_data_type` [string] - _(optional)_  Default Value: null

`data.audit_info` [map] - _(optional)_ Normally auto-populated when enabling the audit policy, it is a sub-document in JSON format containing configuration information for audit management. See documentation for values that can be added manually depending on asset type. Editing this value does NOT enable the audit policy. Default Value: null

`data.audit_pull_enabled` [bool] - _(optional)_ If true, sonargateway will collect the audit logs for this system if it can. Default Value: null

`data.audit_type` [options] - _(optional)_ Used to indicate what mechanism should be used to fetch logs on systems supporting multiple ways to get logs, see asset specific documentation for details Default Value: null Possible Values: LOG_GROUP`, `CLOUDWATCH

`data.aws_proxy_config` [map] - _(optional)_ AWS specific proxy configuration Default Value: null

`data.ca_certs_path` [string] - _(optional)_ Certificate authority certificates path; what location should the sysetm look for certificate information from. Equivalent to --capath in a curl call Default Value: null

`data.ca_file` [string] - _(optional)_ Path to a certificate authority file to use with the call. Equivalent to --cacert in a curl call Default Value: null

`data.consumer_group` [string] - _(optional)_ The Consumer Group the EventHub Consumer Client will use to fetch events. Defaults to '$Default' Default Value: null

`data.consumer_group_workers` [string] - _(optional)_ Only applies if pull_type is consumer_group. The number of consumers that will be part of the consumer group. For best performance this should match the number of shards in your logstore. Default Value: 2

`data.content_type` [string] - _(optional)_ Content type should be set to the desired <'parent' asset 'Server Type'>, which is the one that uses this asset as a destination for logs. NOTE: The content_type field will take precedence on the lookup for parent_asset_id field when checking which server is sending logs to this asset. Default Value: null

`data.credentials_endpoint` [string] - _(optional)_ A specific sts endpoint to use Default Value: null

`data.criticality` [options] - _(optional)_ The asset's importance to the business. These values are measured on a scale from "Most critical" (1) to "Least critical" (4). Allowed values: 1, 2, 3, 4 Default Value: null

`data.database_name` [string] - _(optional)_ Specifies the name of the database (or default DB) to connect to. Default Value: null

`data.db_engine` [string] - _(optional)_ Specifies the version of the engine being used by the database (e.g. oracle-ee, oracle-se, oracle-se1, oracle-se2) Default Value: null

`data.enable_audit_management` [bool] - _(optional)_ If true, Sonar is responsible for setting and updating the policies Default Value: null

`data.enable_audit_monitoring` [bool] - _(optional)_ If true, Sonar sends emails/alerts when the audit policies change. Default Value: null

`data.endpoint` [string] - _(required)_ Logstore's endpoint Default Value: null

`data.entitlement_enabled` [bool] - _(optional)_ If true, Entitlement Management system is enabled. Default Value: null

`data.gateway_id` [string] - _(required)_  Default Value: null

`data.gateway_service` [string] - _(optional)_ The name of the gateway pull service (if any) used to retrieve logs for this source. Usually set by the connect gateway playbook. Default Value: null

`data.jsonar_uid` [string] - _(optional)_ Unique identifier (UID) attached to the Sonar machine controlling the asset Default Value: null

`data.location` [string] - _(optional)_ Current human-readable description of the physical location of the asset, or region. Default Value: null

`data.logs_destination_asset_id` [string] - _(optional)_ The asset name of the log aggregator that stores this asset's logs. Default Value: null

`data.logstore` [string] - _(required)_ Unit that is used to collect, store and query logs Default Value: null

`data.managed_by` [string] - _(optional)_ Email of the person who maintains the asset; can be different from the owner specified in the owned_by field. Defaults to admin_email. Default Value: null

`data.max_concurrent_conn` [string] - _(optional)_ Maximum number of concurrent connections that sensitive data management should use at once. Default Value: null

`data.owned_by` [string] - _(optional)_ Email of Owner / person responsible for the asset; can be different from the person in the managed_by field. Defaults to admin_email. Default Value: null

`data.parent_asset_id` [string] - _(optional)_ The name of an asset that this asset is part of (/related to). E.g. an AWS resource will generally have an AWS account asset as its parent. Also used to connect some log aggregating asset with the sources of their logs. E.g. An AWS LOG GROUP asset can have an AWS RDS as its parent, indicating that that is the log group for that RDS. Default Value: null

`data.project` [string] - _(required)_ Project separates different resources of multiple users and control access to specific resources Default Value: null

`data.provider` [string] - _(optional)_ The type of AWS RDS instance that the S3 asset is receiving audit logs from Default Value: "aws-rds-mssql"

`data.proxy` [string] - _(optional)_  Default Value: null

`data.pubsub_subscription` [string] - _(required)_  Default Value: null

`data.pull_type` [string] - _(optional)_ The method used to pull data from the logstore. Default Value: "log_client" Possible Values: log_client`, `consumer_group

`data.region` [string] - _(optional)_ For cloud systems with regions, the default region or region used with this asset Default Value: null

`data.sdm_enabled` [bool] - _(optional)_ Sensitive data management (SDM) is enabled if this parameter is set to True. Default Value: null

`data.server_host_name` [string] - _(required)_ Bucket name Default Value: null

`data.server_port` [string] - _(required)_ Port used by the source server Default Value: null

`data.service_endpoint` [string] - _(optional)_ Specify a particular endpoint for a given service Default Value: null

`data.ssl` [bool] - _(optional)_  Default Value: null

`data.used_for` [options] - _(optional)_ Designates how this asset is used / the environment that the asset is supporting. Default Value: null Possible Values: Production`, `Test`, `Development`, `Demonstration`, `QA`, `Staging`, `Training`, `Disaster Recovery

`data.version` [string] - _(optional)_ Denotes the version of the asset Default Value: null

`data.connections[].connectionData.amazon_secret` [map] - _(optional)_ Configuration to integrate with AWS Secrets Manager Default Value: null

`data.connections[].connectionData.cache_file` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.db_role` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.external` [bool] - _(optional)_  Default Value: null

`data.connections[].connectionData.extra_kinit_parameters` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.hashicorp_secret` [map] - _(optional)_ Configuration to integrate with HashiCorp Vault Default Value: null

`data.connections[].connectionData.kerberos_kdc` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_service_kdc` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_service_realm` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_spn` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.key_file` [string] - _(required)_ Location on disk on the key to be used to authenticate Default Value: null

`data.connections[].connectionData.keytab_file` [string] - _(optional)_ Specify a non-default keytab location Default Value: null

`data.connections[].connectionData.kinit_program_path` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.passphrase` [string] - _(optional)_ The passphrase for the SSH client Default Value: null

`data.connections[].connectionData.password` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.principal` [string] - _(optional)_ The principal used to authenticate Default Value: null

`data.connections[].connectionData.region` [string] - _(required)_ AWS region Default Value: ""

`data.connections[].connectionData.secret_key` [string] - _(optional)_ The secret key for the SSH client Default Value: null

`data.connections[].connectionData.ssl` [bool] - _(optional)_ If true, use SSL when connecting Default Value: null

`data.connections[].connectionData.ssl_server_cert` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.use_keytab` [bool] - _(optional)_ If true, authenticate using a key tab Default Value: null

`data.connections[].connectionData.username` [string] - _(optional)_  Default Value: null



