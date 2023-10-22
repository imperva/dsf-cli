## DSF-CLI - Data Sources:
Example payloads for data sources

### Usage:
`dsfcli data_sources -h`

### List all data_sources:
`dsfcli data_source read`

### Retrieve a specific data_source by id:
`dsfcli data_source read --id="arn:aws:rds:us-east-2:123456789:db:your-host-here"`

### Create a data_source from input string:
`dsfcli data_source create --json='{"data": {"assetData": {"asset_display_name": "arn:aws:rds:us-east-2:123456789:db:your-host-here","arn": "arn:aws:rds:us-east-2:123456789:db:your-host-here","Server Host Name": "your-db.endpoint.us-east-2.rds.amazonaws.com","admin_email": "test@imperva.com","connections": []},"serverType": "AWS RDS MYSQL","gatewayId": "12345-abcde-12345-abcde"}}'`

### Create a data_source from local file:
`dsfcli data_source create --json="$(cat < data_source_AWS_RDS_MYSQL.json)"`

### Update a data_source from input string by id:
`dsfcli data_source update --json='{"data": {"assetData": {"asset_display_name": "arn:aws:rds:us-east-2:123456789:db:your-host-here","arn": "arn:aws:rds:us-east-2:123456789:db:your-host-here","Server Host Name": "your-db.endpoint.us-east-2.rds.amazonaws.com","admin_email": "test@imperva.com","connections": []},"serverType": "AWS RDS MYSQL","gatewayId": "12345-abcde-12345-abcde"}}' --id="arn:aws:rds:us-east-2:123456789:db:your-host-here"`

### Update a data_source from local file by id:
`dsfcli data_source update --json="$(cat < data_source_AWS_RDS_MYSQL.json)" --id="arn:aws:rds:us-east-2:123456789:db:your-host-here"`

### Delete a data_source by id:
`dsfcli data_source delete --id="arn:aws:rds:us-east-2:123456789:db:your-host-here"`

#### Config Options ####

`data.admin_email` [string] - _(required)_ The email address to notify about this asset Default Value: null

`data.arn` [string] - _(required)_ Amazon Resource Name - format is arn:partition:service:region:account-id:resource-type:resource-id and used as the asset_id Default Value: ""

`data.asset_display_name` [string] - _(required)_ User-friendly name of the asset, defined by user. Default Value: ""

`data.asset_id` [string] - _(required)_  Default Value: null

`data.asset_source` [string] - _(optional)_ The source platform/vendor/system of the asset data. Usually the service responsible for creating that asset document Default Value: ""

`data.audit_info` [map] - _(optional)_ Normally auto-populated when enabling the audit policy, it is a sub-document in JSON format containing configuration information for audit management. See documentation for values that can be added manually depending on asset type. Editing this value does NOT enable the audit policy. Default Value: null

`data.audit_pull_enabled` [bool] - _(optional)_ If true, sonargateway will collect the audit logs for this system if it can. Default Value: null

`data.audit_type` [options] - _(optional)_ Used to indicate what mechanism should be used to fetch logs on systems supporting multiple ways to get logs, see asset specific documentation for details Default Value: null Possible Values: COSMOS_TABLE

`data.availability_zones` [string] - _(optional)_  Default Value: null

`data.available_regions` [string] - _(optional)_ A list of regions to use in discovery actions that iterate through region Default Value: null

`data.aws_proxy_config` [map] - _(optional)_ AWS specific proxy configuration Default Value: null

`data.ca_certs_path` [string] - _(optional)_ Certificate authority certificates path; what location should the sysetm look for certificate information from. Equivalent to --capath in a curl call Default Value: null

`data.ca_file` [string] - _(optional)_ Path to a certificate authority file to use with the call. Equivalent to --cacert in a curl call Default Value: null

`data.cluster_engine` [string] - _(optional)_  Default Value: null

`data.cluster_id` [string] - _(optional)_  Default Value: null

`data.cluster_member_id` [string] - _(optional)_  Default Value: null

`data.cluster_name` [string] - _(optional)_  Default Value: null

`data.content_type` [string] - _(optional)_ Content type should be set to the desired <'parent' asset 'Server Type'>, which is the one that uses this asset as a destination for logs. NOTE: The content_type field will take precedence on the lookup for parent_asset_id field when checking which server is sending logs to this asset. Default Value: null

`data.credentials_endpoint` [string] - _(optional)_ A specific sts endpoint to use Default Value: null

`data.criticality` [options] - _(optional)_ The asset's importance to the business. These values are measured on a scale from "Most critical" (1) to "Least critical" (4). Allowed values: 1, 2, 3, 4 Default Value: null

`data.database_name` [string] - _(optional)_ Specifies the name of the database (or default DB) to connect to. Default Value: null

`data.db_engine` [string] - _(optional)_ Specifies the version of the engine being used by the database (e.g. oracle-ee, oracle-se, oracle-se1, oracle-se2) Default Value: null

`data.db_instances_display_name` [string] - _(optional)_  Default Value: null

`data.duration_threshold` [string] - _(optional)_  Default Value: null

`data.enable_audit_management` [bool] - _(optional)_ If true, Sonar is responsible for setting and updating the policies Default Value: null

`data.enable_audit_monitoring` [bool] - _(optional)_ If true, Sonar sends emails/alerts when the audit policies change. Default Value: null

`data.enabled_logs_exports` [string] - _(optional)_  Default Value: null

`data.entitlement_enabled` [bool] - _(optional)_ If true, Entitlement Management system is enabled. Default Value: null

`data.gateway_id` [string] - _(required)_  Default Value: null

`data.gateway_service` [string] - _(optional)_ The name of the gateway pull service (if any) used to retrieve logs for this source. Usually set by the connect gateway playbook. Default Value: null

`data.host_timezone_offset` [string] - _(optional)_ The offset value string is in the format "-/+hh:mm" Default Value: null

`data.ignore_latest_of` [string] - _(optional)_ A regex defining a group. From all the files with the same group, the latest one will be ignored, so that it isn't archived until server is done writing Default Value: null

`data.is_cluster` [bool] - _(optional)_  Default Value: null

`data.is_multi_zones` [bool] - _(optional)_  Default Value: null

`data.jsonar_uid` [string] - _(optional)_ Unique identifier (UID) attached to the Sonar machine controlling the asset Default Value: null

`data.location` [string] - _(optional)_ Current human-readable description of the physical location of the asset, or region. Default Value: null

`data.log_bucket_id` [string] - _(optional)_ Asset ID of the S3 bucket which stores the logs for this server Default Value: null

`data.logs_destination_asset_id` [string] - _(optional)_ The asset name of the log aggregator that stores this asset's logs. Default Value: null

`data.managed_by` [string] - _(optional)_ Email of the person who maintains the asset; can be different from the owner specified in the owned_by field. Defaults to admin_email. Default Value: null

`data.max_concurrent_conn` [string] - _(optional)_ Maximum number of concurrent connections that sensitive data management should use at once. Default Value: null

`data.owned_by` [string] - _(optional)_ Email of Owner / person responsible for the asset; can be different from the person in the managed_by field. Defaults to admin_email. Default Value: null

`data.parent_asset_id` [string] - _(optional)_ The name of an asset that this asset is part of (/related to). E.g. an AWS resource will generally have an AWS account asset as its parent. Also used to connect some log aggregating asset with the sources of their logs. E.g. An AWS LOG GROUP asset can have an AWS RDS as its parent, indicating that that is the log group for that RDS. Default Value: null

`data.provider` [string] - _(optional)_ The type of AWS RDS instance that the S3 asset is receiving audit logs from Default Value: "aws-rds-mssql"

`data.provider_url` [string] - _(optional)_  Default Value: null

`data.proxy` [string] - _(optional)_ Proxy to use for AWS calls if aws_proxy_config is populated the proxy field will get populated from the http value there Default Value: null

`data.pubsub_subscription` [string] - _(optional)_  Default Value: null

`data.region` [string] - _(optional)_ For cloud systems with regions, the default region or region used with this asset Default Value: null

`data.sdm_enabled` [bool] - _(optional)_ Sensitive data management (SDM) is enabled if this parameter is set to True. Default Value: null

`data.searches` [string] - _(optional)_  Default Value: null

`data.server_host_name` [string] - _(required)_ Hostname (or IP if name is unknown) Default Value: null

`data.server_port` [string] - _(required)_ Port used by the source server Default Value: null

`data.service_endpoint` [string] - _(optional)_ Specify a particular endpoint for a given service Default Value: null

`data.service_endpoints` [map] - _(optional)_ Specify particular endpoints for a given service in the form of <service name>: "endpoint" Default Value: null

`data.service_name` [string] - _(optional)_  Default Value: "MSSQLSERVER"

`data.ssl` [bool] - _(optional)_  Default Value: null

`data.used_for` [options] - _(optional)_ Designates how this asset is used / the environment that the asset is supporting. Default Value: null Possible Values: Production`, `Test`, `Development`, `Demonstration`, `QA`, `Staging`, `Training`, `Disaster Recovery

`data.version` [string] - _(optional)_ Denotes the version of the asset Default Value: null

`data.virtual_hostname` [string] - _(optional)_  Default Value: null

`data.virtual_ip` [string] - _(optional)_  Default Value: null

`data.xel_directory` [string] - _(optional)_ Absolute path of the XEL files location Default Value: null

`data.connections[].connectionData.access_id` [string] - _(required)_ The Account Name/Access ID to use when authenticating to Snowflake Default Value: null

`data.connections[].connectionData.account_name` [string] - _(required)_ The cloudant account name required when connecting a resource with IAM role Default Value: null

`data.connections[].connectionData.amazon_secret` [map] - _(optional)_ Configuration to integrate with AWS Secrets Manager Default Value: null

`data.connections[].connectionData.api_key` [string] - _(required)_ IAM authentication API key Default Value: null

`data.connections[].connectionData.autocommit` [bool] - _(optional)_ If true, Commit automatically don't wait for transaction to be explicitly committed Default Value: null

`data.connections[].connectionData.aws_connection_id` [string] - _(required)_ The parent AWS connection document_id Default Value: null

`data.connections[].connectionData.bucket` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.ca_certs_path` [string] - _(optional)_ Certificate authority certificates path; what location should the sysetm look for certificate information from. Equivalent to --capath in a curl call Default Value: null

`data.connections[].connectionData.ca_file` [string] - _(optional)_ Use the specified certificate file to verify the peer. The file may contain multiple CA certificates. Default Value: null

`data.connections[].connectionData.cache_file` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.cert_file` [string] - _(optional)_ Use the specified client certificate file when getting a file with HTTPS, FTPS or another SSL-based protocol. Default Value: null

`data.connections[].connectionData.client_id` [string] - _(required)_ Azure client application ID Default Value: null

`data.connections[].connectionData.client_secret` [string] - _(required)_ Azure application client secret Default Value: null

`data.connections[].connectionData.cluster_id` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.cluster_member_id` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.cluster_name` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.content_type` [string] - _(optional)_ Content-Type to append to the HTTP headers in the curl call Default Value: null

`data.connections[].connectionData.credential_fields` [map] - _(optional)_ Document containing values to build a profile from. Filling this will create a profile using the given profile name Default Value: null

`data.connections[].connectionData.crn` [string] - _(required)_ The CRN unique identifier of the resource Default Value: null

`data.connections[].connectionData.database_name` [string] - _(required)_ Specifies the name of the database (or default DB) to connect to. Default Value: null

`data.connections[].connectionData.db_role` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.dn` [string] - _(optional)_ The distinguished name of a particular PKI certificate Default Value: null

`data.connections[].connectionData.dns_srv` [bool] - _(optional)_  Default Value: null

`data.connections[].connectionData.driver` [string] - _(optional)_ A path to a non-default driver location. If populated this driver will be used rather than the default Default Value: null

`data.connections[].connectionData.dsn` [string] - _(required)_ Data Source Name Default Value: null

`data.connections[].connectionData.external` [bool] - _(optional)_  Default Value: null

`data.connections[].connectionData.external_id` [string] - _(optional)_ External ID to use when assuming a role Default Value: null

`data.connections[].connectionData.extra_kinit_parameters` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.hashicorp_secret` [map] - _(optional)_ Configuration to integrate with HashiCorp Vault Default Value: null

`data.connections[].connectionData.hive_server_type` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.host_name_mismatch` [bool] - _(optional)_  Default Value: null

`data.connections[].connectionData.hosts` [string] - _(optional)_ Required for quering the logdna url. cloudantnosqldb in the case of a cloudant DB Default Value: "cloudantnosqldb"

`data.connections[].connectionData.httppath` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.is_cluster` [bool] - _(optional)_  Default Value: null

`data.connections[].connectionData.jdbc_ssl_trust_server_certificate` [bool] - _(optional)_  Default Value: false

`data.connections[].connectionData.jdbc_ssl_trust_store_location` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.jdbc_ssl_trust_store_password` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_host_fqdn` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_kdc` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_retry_count` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_service_kdc` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_service_realm` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.kerberos_spn` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.key_file` [string] - _(optional)_ Private key file name. Allows you to provide your private key in this separate file. Default Value: null

`data.connections[].connectionData.keytab_file` [string] - _(optional)_ Specify a non-default keytab location Default Value: null

`data.connections[].connectionData.kinit_program_path` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.net_service_name` [string] - _(optional)_ Alias in tnsnames.ora replaces hostname, service name, and port in connection string Default Value: null

`data.connections[].connectionData.oauth_parameters` [map] - _(required)_ Additional parameters to pass when requesting a token Default Value: null

`data.connections[].connectionData.odbc_connection_string` [string] - _(optional)_ Additional ODBC connection string parameters. This string will get added to the connection string Default Value: null

`data.connections[].connectionData.passphrase` [string] - _(optional)_ Passphrase for the private key. Default Value: null

`data.connections[].connectionData.password` [string] - _(required)_ The password of the user being used to authenticate Default Value: null

`data.connections[].connectionData.principal` [string] - _(optional)_ The principal used to authenticate Default Value: null

`data.connections[].connectionData.proxy_auto_detect` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.proxy_password` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.proxy_port` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.proxy_server` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.proxy_ssl_type` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.region` [string] - _(required)_ The cloud geography/region/zone/data center that the resource resides Default Value: null

`data.connections[].connectionData.replica_set` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.resource_id` [string] - _(required)_ Azure resource application ID Default Value: null

`data.connections[].connectionData.schema` [string] - _(optional)_ Schema name. A schema is a logical grouping of database objects Default Value: null

`data.connections[].connectionData.secret_key` [string] - _(required)_  Default Value: null

`data.connections[].connectionData.self_signed` [bool] - _(optional)_ Accept self-signed certificates Default Value: null

`data.connections[].connectionData.self_signed_cert` [bool] - _(optional)_  Default Value: null

`data.connections[].connectionData.server_port` [string] - _(required)_  Default Value: null

`data.connections[].connectionData.service_key` [string] - _(required)_ The service key required in the logdna url query to connect to logdna and pull the logs Default Value: null

`data.connections[].connectionData.snowflake_role` [string] - _(required)_ Role with which to log into Snowflake Default Value: null

`data.connections[].connectionData.ssl` [bool] - _(optional)_ If true, use SSL when connecting Default Value: null

`data.connections[].connectionData.ssl_server_cert` [string] - _(optional)_ Path to server certificate to use during authentication Default Value: null

`data.connections[].connectionData.tenant_id` [string] - _(required)_ Azure tenant ID Default Value: null

`data.connections[].connectionData.thrift_transport` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.tmp_user` [bool] - _(optional)_ If true create a temporary user Default Value: false

`data.connections[].connectionData.token` [string] - _(required)_ Saved token to use to authenticate Default Value: null

`data.connections[].connectionData.token_endpoint` [string] - _(required)_ URL of endpoint to query when requesting a token Default Value: null

`data.connections[].connectionData.transportmode` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.use_keytab` [bool] - _(optional)_ If true, authenticate using a key tab Default Value: null

`data.connections[].connectionData.username` [string] - _(required)_ The user to use when connecting Default Value: null

`data.connections[].connectionData.virtual_hostname` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.virtual_ip` [string] - _(optional)_  Default Value: null

`data.connections[].connectionData.wallet_dir` [string] - _(required)_ Path to the Oracle wallet directory Default Value: null

`data.connections[].connectionData.warehouse` [string] - _(optional)_ The name of the warehouse to connect to Default Value: null
