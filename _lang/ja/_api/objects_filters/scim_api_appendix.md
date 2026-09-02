---
nav_title: "SCIM APIオブジェクトと付録"
article_title: "SCIM APIオブジェクトと付録"
page_type: reference
description: "この記事では、さまざまなSCIM APIオブジェクトと付録について説明します。"
alias: /scim_api_appendix/
---

# SCIM APIオブジェクトと付録 {#scim-api-objects-and-appendix}

> この記事では、さまざまなSCIM APIオブジェクトと付録について説明します。

{% sdktabs %}
{% sdktab Granular SCIM API %}

## きめ細かな権限の移行 {#granular-permissions-migration}

既存のSCIM統合および[レガシーSCIM APIオブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api)は、きめ細かな権限の移行後も引き続き動作しますが、Brazeは2026年12月にレガシーSCIM API値の受け入れを停止します。

すぐに対応する必要はありません。ただし、きめ細かな権限に移行する権限について統合を確認してください。たとえば、現在APIで `basic_access` を送信している場合は、きめ細かな権限への移行後に特定の権限を含めるよう統合を更新してください（例: `"appGroupPermissions":["view_campaigns","edit_campaigns"]`）。Brazeは、既存の統合が壊れないよう、きめ細かな権限の移行後も `basic_access` などのレガシー文字列を引き続き受け入れます。

## 権限オブジェクト {#permissions-object}

権限オブジェクトは、SCIM ID権限を通じてユーザーリソースとやり取りする際の一部のリクエストおよびレスポンスに含まれるフィールドです。

{% alert note %}
アプリグループはBrazeでワークスペースに名称変更されましたが、このページのキーは引き続き旧用語を参照しています（例: `appGroup`、`appGroupName`）。
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

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `companyPermissions` | 任意 | 配列 | [会社レベルの権限文字列]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company)の配列。文字列が存在する場合、ユーザーが対応する権限を持つことを意味します。 |
| `roles` | 任意 | 配列 | [ロールオブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object)の配列。 |
| `appGroup` | 必須 | 配列 | [ワークスペース権限オブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### ワークスペース権限オブジェクト {#workspace-permissions-object}

有効なワークスペース権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `appGroupName` | 任意 | 文字列 | ワークスペースの名前。このオブジェクトに含まれる権限がどのワークスペースに対するものかを指定するために使用されます。 |
| `appGroupId` | `appGroupName`がない場合は必須 | 文字列 | ワークスペースのID。ワークスペースを指定する代替手段として使用されます。 |
| `appGroupPermissionSets` | 任意 | 配列 | 単一の[ワークスペース権限セットオブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object)を含む配列。 |
| `appGroupPermissions` | 必須 | 配列 | [ワークスペース権限文字列]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings)テーブルのワークスペースレベルの権限文字列の配列。文字列が存在する場合、ユーザーが指定されたワークスペースに対して対応する権限を持つことを意味します。 |
| `team` | 任意 | 配列 | [チーム権限オブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object" }

### ワークスペース権限セットオブジェクト {#workspace-permissions-set-object}

有効なワークスペース権限セットオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | 任意 | 文字列 | このワークスペースに対してユーザーに割り当てられるワークスペース権限セットの名前。 |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`がない場合は必須 | 文字列 | ワークスペースのID。このワークスペースに対してユーザーに割り当てられるワークスペース権限セットを指定する代替手段として使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object #workspace-permissions-set-object" }

### チーム権限オブジェクト {#team-permissions-object}

有効なチーム権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `teamName` | 任意 | 文字列 | チームの名前。このオブジェクト内の権限がどのチームに対するものかを指定するために使用できます。 |
| `teamId` | `teamName`がない場合は必須 | 文字列 | チームのID。チームを指定する代替手段として使用されます。 |
| `teamPermissions` | 必須 | 配列 | [チーム権限文字列]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team)テーブルのチームレベルの権限文字列の配列。文字列が存在する場合、ユーザーが指定されたチームに対して対応する権限を持つことを意味します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## ロールオブジェクト {#role-object}

有効なロールオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `roleName` | 任意 | 文字列 | ユーザーに割り当てられるロールの名前。 |
| `roleId` | `roleName`がない場合は必須 | 文字列 | ロールのID。ロールを指定する代替手段として使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## 付録 {#appendix}

### 会社権限文字列 {#company}

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
| Edit キャンペーン | `edit_campaigns` |
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
| Launch キャンペーン | `launch_campaigns` |
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
| Edit キャンペーン | `edit_campaigns` |
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
| Launch キャンペーン | `launch_campaigns` |
| Launch キャンバス | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings #team" }

### 部門文字列 {#department-strings}

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
{% endsdktab %}
{% sdktab Legacy SCIM API %}


{% alert important %}
Brazeでは、ユーザーアクセスをより柔軟に管理できる[きめ細かな権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions)が提供されるようになりました。詳細については、[きめ細かな権限への移行]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)および[Granular SCIM API]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api/)タブを参照して、きめ細かなSCIM APIオブジェクトと付録をご確認ください。Brazeは2026年12月にレガシーSCIM API値の受け入れを停止します。
{% endalert %}

## 権限オブジェクト

権限オブジェクトは、SCIM ID権限を通じてユーザーリソースとやり取りする際の一部のリクエストおよびレスポンスに含まれるフィールドです。

{% alert note %}
アプリグループはBrazeでワークスペースに名称変更されましたが、このページのキーは引き続き旧用語を参照しています（例: `appGroup`、`appGroupName`）。
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

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `companyPermissions` | 任意 | 配列 | [会社権限文字列]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company)テーブルの会社レベルの権限文字列の配列。文字列が存在する場合、ユーザーが対応する権限を持つことを意味します。 |
| `roles` | 任意 | 配列 | [ロールオブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object)の配列。 |
| `appGroup` | 必須 | 配列 | [ワークスペース権限オブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permission-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### ワークスペース権限オブジェクト {#workspace-permission-object}

有効なワークスペース権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `appGroupName` | 任意 | 文字列 | ワークスペースの名前。このオブジェクトに含まれる権限がどのワークスペースに対するものかを指定するために使用されます。 |
| `appGroupId` | `appGroupName`がない場合は必須 | 文字列 | ワークスペースのID。ワークスペースを指定する代替手段として使用されます。 |
| `appGroupPermissionSets` | 任意 | 配列 | 単一の[ワークスペース権限セットオブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object)を含む配列。 |
| `appGroupPermissions` | 必須 | 配列 | [ワークスペース権限文字列]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings)テーブルのワークスペースレベルの権限文字列の配列。文字列が存在する場合、ユーザーが指定されたワークスペースに対して対応する権限を持つことを意味します。 |
| `team` | 任意 | 配列 | [チーム権限オブジェクト]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object #workspace-permission-object" }

### ワークスペース権限セットオブジェクト

有効なワークスペース権限セットオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | 任意 | 文字列 | このワークスペースに対してユーザーに割り当てられるワークスペース権限セットの名前。 |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`がない場合は必須 | 文字列 | ワークスペースのID。このワークスペースに対してユーザーに割り当てられるワークスペース権限セットを指定する代替手段として使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object #workspace-permissions-set-object" }

### チーム権限オブジェクト

有効なチーム権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `teamName` | 任意 | 文字列 | チームの名前。このオブジェクト内の権限がどのチームに対するものかを指定するために使用できます。 |
| `teamId` | `teamName`がない場合は必須 | 文字列 | チームのID。チームを指定する代替手段として使用されます。 |
| `teamPermissions` | 必須 | 配列 | [チーム権限文字列]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team)テーブルのチームレベルの権限文字列の配列。文字列が存在する場合、ユーザーが指定されたチームに対して対応する権限を持つことを意味します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## ロールオブジェクト

有効なロールオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データ型 | 説明 |
| --- | --- | --- | --- |
| `roleName` | 任意 | 文字列 | ユーザーに割り当てられるロールの名前。 |
| `roleId` | `roleName`がない場合は必須 | 文字列 | ロールのID。ロールを指定する代替手段として使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## 付録

### 会社権限文字列

| UIでの表示 | SCIM API文字列 |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings #company" }

### ワークスペース権限文字列

| 権限名 | SCIM API文字列 |
| --- | --- |
| Admin | `admin` |
| Access キャンペーン, キャンバス, Cards, セグメント, Media Library | `basic_access` |
| Approve and Deny キャンバス | `approve_deny_campaigns` |
| Send キャンペーン, キャンバス | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit セグメント | `edit_segments` |
| Export User Data | `export_user_data` |
| View PII | `view_pii` |
| View User Profiles PII Compliant | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
| View Usage Data | `view_usage_data` |
| Import and Update User Data | `import_update_user_data` |
| View Billing Details | `view_billing_details` |
| Access Dev Console | `dev_console` |
| Launch Content Blocks | `launch_content_blocks` |
| Manage External Integrations | `manage_external_integrations` |
| Manage Apps | `manage_apps` |
| Manage Teams | `manage_teams` |
| Manage Events, Attributes, Purchases | `manage_events_attributes_purchases` |
| Manage Tags | `manage_tags` |
| Manage Email Settings | `manage_email_settings` |
| Manage Subscription Groups | `manage_subscription_groups` |
| Manage Approval Settings | `manage_approval_settings` |
| Manage Catalogs Dashboard Permission | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace permission strings #workspace-strings" }

### チーム権限文字列

| 権限名 | SCIM API文字列 |
| --- | --- |
| Admin | `admin` |
| Access キャンペーン, キャンバス, Cards, セグメント, Media Library | `basic_access` |
| Approve and Deny キャンバス | `approve_deny_campaigns` |
| Send キャンペーン, キャンバス | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit セグメント | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profile | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings #team" }

### 部門文字列

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
{% endsdktab %}
{% endsdktabs %}