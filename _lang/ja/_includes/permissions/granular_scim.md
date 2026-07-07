## 細粒度権限の移行 {#granular-permissions-migration}

既存のSCIM統合と[レガシーSCIM APIオブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api)は、4月下旬の細粒度権限移行後も引き続き動作します。

すぐに何かアクションを起こす必要はありません。ただし、細粒度化される権限について統合設定を確認することをお勧めします。例えば、現在APIで `basic_access` を送信している場合、細粒度化後に統合を更新し、特定の権限（例：`"appGroupPermissions":["view_campaigns","edit_campaigns"]`）を含めることをお勧めします。Brazeは、既存の統合が壊れないように、細粒度権限移行後もレガシー文字列（`basic_access` など）を引き続き受け付けます。

## 権限オブジェクト {#permissions-object}

権限オブジェクトは、SCIM ID権限を通じてユーザーリソースとやり取りする際に、一部のリクエストやレスポンスに含まれるフィールドです。

{% alert note %}
Brazeではアプリグループはワークスペースに改名されましたが、このページのキーはまだ古い用語を参照しています（例：`appGroup`、`appGroupName`）。
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

有効な権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `companyPermissions` | オプション | 配列 | [会社レベルの権限文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company)の配列です。文字列が存在する場合、ユーザーが対応する権限を持っていることを示します。 |
| `roles` | オプション | 配列 | [ロールオブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object)の配列です。 |
| `appGroup` | 必須 | 配列 | [ワークスペース権限オブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object)の配列です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### ワークスペース権限オブジェクト {#workspace-permissions-object}

有効なアプリグループ権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupName` | オプション | 文字列 | ワークスペースの名前です。このオブジェクトに含まれる権限がどのワークスペースに対するものかを指定するために使用されます。 |
| `appGroupId` | `appGroupName` がない場合は必須 | 文字列 | ワークスペースのIDです。ワークスペースを指定する代替方法として機能します。 |
| `appGroupPermissionSets` | オプション | 配列 | 単一の[ワークスペース権限セットオブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object)を持つ配列です。 |
| `appGroupPermissions` | 必須 | 配列 | [ワークスペース権限文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings)テーブルに基づくワークスペースレベルの権限文字列の配列です。文字列が存在する場合、指定されたワークスペースに対してユーザーが対応する権限を持っていることを示します。 |
| `team` | オプション | 配列 | [チーム権限オブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object)の配列です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object" }

### ワークスペース権限セットオブジェクト {#workspace-permissions-set-object}

有効なワークスペース権限セットオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | オプション | 文字列 | このワークスペースでユーザーに割り当てられるワークスペース権限セットの名前です。 |
| `appGroupPermissionSetID` | `appGroupPermissionSetName` がない場合は必須 | 文字列 | ワークスペースのIDです。このワークスペースでユーザーに割り当てられるワークスペース権限セットを指定する代替方法として機能します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object #workspace-permissions-set-object" }

### チーム権限オブジェクト {#team-permissions-object}

有効なチーム権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `teamName` | オプション | 文字列 | チームの名前です。このオブジェクト内の権限がどのチームに対するものかを指定するために使用できます。 |
| `teamId` | `teamName` がない場合は必須 | 文字列 | チームのIDです。チームを指定する代替方法として機能します。 |
| `teamPermissions` | 必須 | 配列 | [チーム権限文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team)テーブルに基づくチームレベルの権限文字列の配列です。文字列が存在する場合、指定されたチームに対してユーザーが対応する権限を持っていることを示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## ロールオブジェクト {#role-object}

有効なロールオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `roleName` | オプション | 文字列 | ユーザーに割り当てられるロールの名前です。 |
| `roleId` | `roleName` がない場合は必須 | 文字列 | ロールのIDです。ロールを指定する代替方法として機能します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## 付録 {#appendix}

### 会社の権限文字列 {#company}

| UIでの表示 | SCIM API文字列 |
| --- | --- |
| Administrator | `admin` |
| Manage Company Settings | `manage_company_settings` |
| Create and delete workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings #company" }

### ワークスペース権限文字列 {#workspace-strings}

| 権限名 | SCIM API文字列 |
| --- | --- |
| View キャンペーン | `view_campaigns` |
| キャンペーンを編集 | `edit_campaigns` |
| Archive キャンペーン | `archive_campaigns` |
| View キャンバス | `view_canvases` |
| Edit キャンバス | `edit_canvases` |
| Archive キャンバス | `archive_canvases` |
| View Frequency Capping Rules | `view_frequency_caps` |
| Edit Frequency Capping Rules | `edit_frequency_caps` |
| View Message Prioritization | `view_message_prioritization` |
| Edit Message Prioritization | `edit_message_prioritization` |
| View Content Blocks | `view_content_blocks` |
| Edit Content Blocks | `edit_content_blocks` |
| Archive Content Blocks | `archive_content_blocks` |
| View Feature Flags | `view_feature_flags` |
| Edit Feature Flags | `edit_feature_flags` |
| Archive Feature Flags | `archive_feature_flags` |
| View セグメント | `view_segments` |
| Edit セグメント | `edit_segments` |
| Archive セグメント | `archive_segments` |
| View Global Control Group | `view_global_control_group` |
| Edit Global Control Group | `edit_global_control_group` |
| View IAM Templates | `view_iam_templates` |
| Edit IAM Templates | `edit_iam_templates` |
| Archive IAM Templates | `archive_iam_templates` |
| View Email Templates | `view_email_templates` |
| Edit Email Templates | `edit_email_templates` |
| Archive Email Templates | `archive_email_templates` |
| View Webhook Templates | `view_webhook_templates` |
| Edit Webhook Templates | `edit_webhook_templates` |
| Archive Webhook Templates | `archive_webhook_templates` |
| View Email Link Templates | `view_link_templates` |
| Edit Email Link Templates | `edit_link_templates` |
| View Media Library Assets | `view_media_library_assets` |
| View Locations | `view_locations` |
| Edit Locations | `edit_locations` |
| Archive Locations | `archive_locations` |
| View Promotion Codes | `view_promotion_codes` |
| Edit Promotion Codes | `edit_promotion_codes` |
| Export Promotion Codes | `export_promotion_codes` |
| View Preference Centers | `view_preference_centers` |
| Edit Preference Centers | `edit_preference_centers` |
| Edit Reports | `edit_reports` |
| View Placements | `view_placements` |
| Edit Placements | `edit_placements` |
| Archive Placements | `archive_placements` |
| View Banner Templates | `view_banner_templates` |
| View Multi Language Settings | `view_multi_language_settings` |
| Use BrazeAI Operator<sup>TM</sup> | `use_operator` |
| View Decisioning Studio Agents | `view_decisioning_studio_agents` |
| View Decisioning Studio Audience | `view_decisioning_studio_audience` |
| View Decisioning Studio Conversion Event | `view_decisioning_studio_conversion_event` |
| View Decisioning Studio Guardrails | `view_decisioning_studio_guardrails` |
| キャンペーンを起動 | `launch_campaigns` |
| Launch キャンバス | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
| Edit Media Library Assets | `edit_media_library_assets` |
| Delete Media Library Assets | `delete_media_library_assets` |
| View Import Users | `view_import_users` |
| Import Users | `import_users` |
| Edit User Data | `edit_user_data` |
| View User Merge Records | `view_user_merge_records` |
| Merge Duplicate Users | `merge_duplicate_users` |
| View API Keys | `view_api_keys` |
| Edit API Keys | `edit_api_keys` |
| View Internal Groups | `view_internal_user_groups` |
| Edit Internal Groups | `edit_internal_user_groups` |
| Delete Internal Groups | `delete_internal_user_groups` |
| View Message Activity Log | `view_message_activity_log` |
| View Event User Log | `view_event_user_log` |
| View API Identifiers | `view_api_identifiers` |
| View API Usage Dashboard | `view_api_usage_dashboard` |
| View API Limits | `view_api_limits` |
| View API Usage Alerts | `view_api_usage_alerts` |
| Edit API Usage Alerts | `edit_api_usage_alerts` |
| View SDK Debugger | `view_sdk_debugger` |
| Edit SDK Debugger | `edit_sdk_debugger` |
| Launch Content Blocks | `launch_content_blocks` |
| Edit Cloud Data Ingestion | `edit_cloud_data_ingestion` |
| View App Settings | `view_app_settings` |
| Edit App Settings | `edit_app_settings` |
| View Push Settings | `view_push_settings` |
| Edit Push Settings | `edit_push_settings` |
| View Teams | `view_teams` |
| Edit Teams | `edit_teams` |
| Archive Teams | `archive_teams` |
| View Custom Attributes | `view_custom_attributes` |
| Edit Custom Attributes | `edit_custom_attributes` |
| Blocklist Custom Attributes | `blocklist_custom_attributes` |
| Delete Custom Attributes | `delete_custom_attributes` |
| Export Custom Attributes | `export_custom_attributes` |
| View Custom Events | `view_custom_events` |
| Edit Custom Events | `edit_custom_events` |
| Blocklist Custom Events | `blocklist_custom_events` |
| Delete Custom Events | `delete_custom_events` |
| Export Custom Events | `export_custom_events` |
| Edit Custom Event Property Segmentation | `edit_custom_event_property_segmentation` |
| View Products | `view_products` |
| Edit Products | `edit_products` |
| Blocklist Products | `blocklist_products` |
| Edit Purchase Property Segmentation | `edit_purchase_property_segmentation` |
| View Tags | `view_tags` |
| Edit Tags | `edit_tags` |
| Delete Tags | `delete_tags` |
| View Email Settings | `view_email_settings` |
| Edit Email Settings | `edit_email_settings` |
| View Catalogs | `view_catalogs` |
| Edit Catalogs | `edit_catalogs` |
| Export Catalogs | `export_catalogs` |
| Delete Catalogs | `delete_catalogs` |
| View Whatsapp Settings | `view_whatsapp_settings` |
| Edit Technology Partners | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace permission strings #workspace-strings" }

### チーム権限文字列 {#team}

| 権限名 | SCIM API文字列 |
| --- | --- |
| View キャンペーン | `view_campaigns` |
| キャンペーンを編集 | `edit_campaigns` |
| Archive キャンペーン | `archive_campaigns` |
| View キャンバス | `view_canvases` |
| Edit キャンバス | `edit_canvases` |
| Archive キャンバス | `archive_canvases` |
| View Frequency Capping Rules | `view_frequency_caps` |
| Edit Frequency Capping Rules | `edit_frequency_caps` |
| View Message Prioritization | `view_message_prioritization` |
| Edit Message Prioritization | `edit_message_prioritization` |
| View Content Blocks | `view_content_blocks` |
| View Feature Flags | `view_feature_flags` |
| Edit Feature Flags | `edit_feature_flags` |
| Archive Feature Flags | `archive_feature_flags` |
| View セグメント | `view_segments` |
| Edit セグメント | `edit_segments` |
| Edit Global Control Group | `edit_global_control_group` |
| View IAM Templates | `view_iam_templates` |
| Edit IAM Templates | `edit_iam_templates` |
| Archive IAM Templates | `archive_iam_templates` |
| View Email Templates | `view_email_templates` |
| Edit Email Templates | `edit_email_templates` |
| Archive Email Templates | `archive_email_templates` |
| View Webhook Templates | `view_webhook_templates` |
| Edit Webhook Templates | `edit_webhook_templates` |
| Archive Webhook Templates | `archive_webhook_templates` |
| View Email Link Templates | `view_link_templates` |
| Edit Email Link Templates | `edit_link_templates` |
| View Media Library Assets | `view_media_library_assets` |
| View Locations | `view_locations` |
| Edit Locations | `edit_locations` |
| Archive Locations | `archive_locations` |
| View Promotion Codes | `view_promotion_codes` |
| Edit Promotion Codes | `edit_promotion_codes` |
| Export Promotion Codes | `export_promotion_codes` |
| View Preference Centers | `view_preference_centers` |
| Edit Preference Centers | `edit_preference_centers` |
| View Reports | `view_reports` |
| Create Reports | `create_reports` |
| Edit Reports | `edit_reports` |
| View Banner Templates | `view_banner_templates` |
| View Multi Language Settings | `view_multi_language_settings` |
| Use BrazeAI Operator<sup>TM</sup> | `use_operator` |
| View Decisioning Studio Agents | `view_decisioning_studio_agents` |
| キャンペーンを起動 | `launch_campaigns` |
| Launch キャンバス | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings #team" }

### 部門の文字列 {#department-strings}

| UIでの表示 | SCIM API文字列 |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Department strings" }