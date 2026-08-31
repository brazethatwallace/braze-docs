---
nav_title: "SCIM API 오브젝트 및 부록"
article_title: "SCIM API 오브젝트 및 부록"
page_type: reference
description: "이 문서에서는 다양한 SCIM API 오브젝트와 부록에 대해 설명합니다."
alias: /scim_api_appendix/
---

# SCIM API 오브젝트 및 부록 {#scim-api-objects-and-appendix}

> 이 문서에서는 다양한 SCIM API 오브젝트와 부록에 대해 설명합니다.

{% sdktabs %}
{% sdktab Granular SCIM API %}

## 세분화된 권한 마이그레이션 {#granular-permissions-migration}

기존 SCIM 통합 및 [레거시 SCIM API 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api)는 세분화된 권한 마이그레이션 이후에도 계속 작동하지만, Braze는 2026년 12월에 레거시 SCIM API 값의 수락을 중단할 예정입니다.

즉각적인 조치를 취할 필요는 없습니다. 그러나 세분화된 권한으로 이동하는 권한에 대해 통합을 검토하세요. 예를 들어, 현재 API에서 `basic_access`를 전송하고 있다면, 세분화된 권한으로 마이그레이션한 후 특정 권한을 포함하도록 통합을 업데이트하세요(예: `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). Braze는 기존 통합이 중단되지 않도록 세분화된 권한 마이그레이션 이후에도 `basic_access`와 같은 레거시 문자열을 계속 수락합니다.

## 권한 오브젝트 {#permissions-object}

권한 오브젝트는 SCIM ID 권한을 통해 사용자 리소스와 인터페이스할 때 일부 요청 및 응답에서 사용되는 필드입니다.

{% alert note %}
앱 그룹은 Braze에서 워크스페이스로 이름이 변경되었지만, 이 페이지의 키는 여전히 이전 용어를 참조합니다(예: `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

유효한 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `companyPermissions` | 선택 사항 | 배열 | [회사 수준 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company)의 배열로, 문자열이 존재하면 사용자가 해당 권한을 가지고 있음을 나타냅니다. |
| `roles` | 선택 사항 | 배열 | [역할 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object)의 배열입니다. |
| `appGroup` | 필수 | 배열 | [워크스페이스 권한 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### 워크스페이스 권한 오브젝트 {#workspace-permissions-object}

유효한 워크스페이스 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupName` | 선택 사항 | 문자열 | 워크스페이스의 이름입니다. 이 오브젝트에 포함된 권한이 어떤 워크스페이스에 대한 것인지 지정하는 데 사용됩니다. |
| `appGroupId` | `appGroupName`이 없는 경우 필수 | 문자열 | 워크스페이스를 지정하는 대체 방법으로 사용되는 워크스페이스 ID입니다. |
| `appGroupPermissionSets` | 선택 사항 | 배열 | 단일 [워크스페이스 권한 세트 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object)를 포함하는 배열입니다. |
| `appGroupPermissions` | 필수 | 배열 | [워크스페이스 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings) 테이블의 워크스페이스 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 워크스페이스에 대해 해당 권한을 가지고 있음을 나타냅니다. |
| `team` | 선택 사항 | 배열 | [팀 권한 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object" }

### 워크스페이스 권한 세트 오브젝트 {#workspace-permissions-set-object}

유효한 워크스페이스 권한 세트 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | 선택 사항 | 문자열 | 이 워크스페이스에 대해 사용자에게 할당되는 워크스페이스 권한 세트의 이름입니다. |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`이 없는 경우 필수 | 문자열 | 이 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트를 지정하는 대체 방법으로 사용되는 워크스페이스 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object" }

### 팀 권한 오브젝트 {#team-permissions-object}

유효한 팀 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `teamName` | 선택 사항 | 문자열 | 팀의 이름으로, 이 오브젝트 내의 권한이 어떤 팀에 대한 것인지 지정하는 데 사용할 수 있습니다. |
| `teamId` | `teamName`이 없는 경우 필수 | 문자열 | 팀을 지정하는 대체 방법으로 사용되는 팀 ID입니다. |
| `teamPermissions` | 필수 | 배열 | [팀 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team) 테이블의 팀 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 팀에 대해 해당 권한을 가지고 있음을 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## 역할 오브젝트 {#role-object}

유효한 역할 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `roleName` | 선택 사항 | 문자열 | 사용자에게 할당되는 역할의 이름입니다. |
| `roleId` | `roleName`이 없는 경우 필수 | 문자열 | 역할을 지정하는 대체 방법으로 사용되는 역할 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## 부록 {#appendix}

### 회사 권한 문자열 {#company}

| UI에 표시되는 이름 | SCIM API 문자열 |
| --- | --- |
| Administrator | `admin` |
| Manage Company Settings | `manage_company_settings` |
| Create and delete workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings" }

### 워크스페이스 권한 문자열 {#workspace-strings}

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| View Campaigns | `view_campaigns` |
| Edit Campaigns | `edit_campaigns` |
| Archive Campaigns | `archive_campaigns` |
| View Canvases | `view_canvases` |
| Edit Canvases | `edit_canvases` |
| Archive Canvases | `archive_canvases` |
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
| View Segments | `view_segments` |
| Edit Segments | `edit_segments` |
| Archive Segments | `archive_segments` |
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
| Launch Campaigns | `launch_campaigns` |
| Launch Canvases | `launch_canvases` |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace permission strings" }

### 팀 권한 문자열 {#team}

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| View Campaigns | `view_campaigns` |
| Edit Campaigns | `edit_campaigns` |
| Archive Campaigns | `archive_campaigns` |
| View Canvases | `view_canvases` |
| Edit Canvases | `edit_canvases` |
| Archive Canvases | `archive_canvases` |
| View Frequency Capping Rules | `view_frequency_caps` |
| Edit Frequency Capping Rules | `edit_frequency_caps` |
| View Message Prioritization | `view_message_prioritization` |
| Edit Message Prioritization | `edit_message_prioritization` |
| View Content Blocks | `view_content_blocks` |
| View Feature Flags | `view_feature_flags` |
| Edit Feature Flags | `edit_feature_flags` |
| Archive Feature Flags | `archive_feature_flags` |
| View Segments | `view_segments` |
| Edit Segments | `edit_segments` |
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
| Launch Campaigns | `launch_campaigns` |
| Launch Canvases | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings" }

### 부서 문자열 {#department-strings}

| UI에 표시되는 이름 | SCIM API 문자열 |
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
Braze는 이제 사용자 액세스를 보다 유연하게 관리할 수 있는 [세분화된 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions)을 제공합니다. 자세한 내용은 [세분화된 권한으로 마이그레이션]({{site.baseurl}}/granular_permissions_migration) 및 [Granular SCIM API]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api/) 탭을 참조하여 세분화된 SCIM API 오브젝트와 부록을 확인하세요. Braze는 2026년 12월에 레거시 SCIM API 값 수락을 중단합니다.
{% endalert %}

## 권한 오브젝트

권한 오브젝트는 SCIM ID 권한을 통해 사용자 리소스와 인터페이스할 때 일부 요청 및 응답에서 사용되는 필드입니다.

{% alert note %}
앱 그룹은 Braze에서 워크스페이스로 이름이 변경되었지만, 이 페이지의 키는 여전히 이전 용어를 참조합니다(예: `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

유효한 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `companyPermissions` | 선택 사항 | 배열 | [회사 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company) 테이블의 회사 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 해당 권한을 가지고 있음을 나타냅니다. |
| `roles` | 선택 사항 | 배열 | [역할 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object)의 배열입니다. |
| `appGroup` | 필수 | 배열 | [워크스페이스 권한 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permission-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### 워크스페이스 권한 오브젝트 {#workspace-permission-object}

유효한 워크스페이스 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupName` | 선택 사항 | 문자열 | 워크스페이스의 이름입니다. 이 오브젝트에 포함된 권한이 어떤 워크스페이스에 대한 것인지 지정하는 데 사용됩니다. |
| `appGroupId` | `appGroupName`이 없는 경우 필수 | 문자열 | 워크스페이스를 지정하는 대체 방법으로 사용되는 워크스페이스 ID입니다. |
| `appGroupPermissionSets` | 선택 사항 | 배열 | 단일 [워크스페이스 권한 세트 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object)를 포함하는 배열입니다. |
| `appGroupPermissions` | 필수 | 배열 | [워크스페이스 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings) 테이블의 워크스페이스 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 워크스페이스에 대해 해당 권한을 가지고 있음을 나타냅니다. |
| `team` | 선택 사항 | 배열 | [팀 권한 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object" }

### 워크스페이스 권한 세트 오브젝트

유효한 워크스페이스 권한 세트 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | 선택 사항 | 문자열 | 이 워크스페이스에 대해 사용자에게 할당되는 워크스페이스 권한 세트의 이름입니다. |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`이 없는 경우 필수 | 문자열 | 이 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트를 지정하는 대체 방법으로 사용되는 워크스페이스 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object" }

### 팀 권한 오브젝트

유효한 팀 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `teamName` | 선택 사항 | 문자열 | 팀의 이름으로, 이 오브젝트 내의 권한이 어떤 팀에 대한 것인지 지정하는 데 사용할 수 있습니다. |
| `teamId` | `teamName`이 없는 경우 필수 | 문자열 | 팀을 지정하는 대체 방법으로 사용되는 팀 ID입니다. |
| `teamPermissions` | 필수 | 배열 | [팀 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team) 테이블의 팀 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 팀에 대해 해당 권한을 가지고 있음을 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## 역할 오브젝트

유효한 역할 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `roleName` | 선택 사항 | 문자열 | 사용자에게 할당되는 역할의 이름입니다. |
| `roleId` | `roleName`이 없는 경우 필수 | 문자열 | 역할을 지정하는 대체 방법으로 사용되는 역할 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## 부록

### 회사 권한 문자열

| UI에 표시되는 이름 | SCIM API 문자열 |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings" }

### 워크스페이스 권한 문자열

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace permission strings" }

### 팀 권한 문자열

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profile | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings" }

### 부서 문자열 {#department-strings}

| UI에 표시되는 이름 | SCIM API 문자열 |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="부서 문자열" }
{% endsdktab %}
{% sdktab Legacy SCIM API %}


{% alert important %}
Braze는 이제 사용자 액세스를 보다 유연하게 관리할 수 있는 [세분화된 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions)을 제공합니다. 자세한 내용은 [세분화된 권한으로 마이그레이션]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) 및 [Granular SCIM API]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=granular%20scim%20api/) 탭을 참조하여 세분화된 SCIM API 오브젝트와 부록을 확인하세요. Braze는 2026년 12월에 레거시 SCIM API 값의 수락을 중단할 예정입니다.
{% endalert %}

## 권한 오브젝트

권한 오브젝트는 SCIM ID 권한을 통해 사용자 리소스와 인터페이스할 때 일부 요청 및 응답에서 사용되는 필드입니다.

{% alert note %}
앱 그룹은 Braze에서 워크스페이스로 이름이 변경되었지만, 이 페이지의 키는 여전히 이전 용어를 참조합니다(예: `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

유효한 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `companyPermissions` | 선택 사항 | 배열 | [회사 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company) 테이블의 회사 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 해당 권한을 가지고 있음을 나타냅니다. |
| `roles` | 선택 사항 | 배열 | [역할 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object)의 배열입니다. |
| `appGroup` | 필수 | 배열 | [워크스페이스 권한 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permission-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="권한 오브젝트" }

### 워크스페이스 권한 오브젝트 {#workspace-permission-object}

유효한 워크스페이스 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupName` | 선택 사항 | 문자열 | 워크스페이스의 이름입니다. 이 오브젝트에 포함된 권한이 어떤 워크스페이스에 대한 것인지 지정하는 데 사용됩니다. |
| `appGroupId` | `appGroupName`이 없는 경우 필수 | 문자열 | 워크스페이스를 지정하는 대체 방법으로 사용되는 워크스페이스 ID입니다. |
| `appGroupPermissionSets` | 선택 사항 | 배열 | 단일 [워크스페이스 권한 세트 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object)를 포함하는 배열입니다. |
| `appGroupPermissions` | 필수 | 배열 | [워크스페이스 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings) 테이블의 워크스페이스 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 워크스페이스에 대해 해당 권한을 가지고 있음을 나타냅니다. |
| `team` | 선택 사항 | 배열 | [팀 권한 오브젝트]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="워크스페이스 권한 오브젝트 #workspace-permission-object" }

### 워크스페이스 권한 세트 오브젝트

유효한 워크스페이스 권한 세트 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | 선택 사항 | 문자열 | 이 워크스페이스에 대해 사용자에게 할당되는 워크스페이스 권한 세트의 이름입니다. |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`이 없는 경우 필수 | 문자열 | 이 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트를 지정하는 대체 방법으로 사용되는 워크스페이스 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="워크스페이스 권한 세트 오브젝트 #workspace-permissions-set-object" }

### 팀 권한 오브젝트

유효한 팀 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `teamName` | 선택 사항 | 문자열 | 팀의 이름으로, 이 오브젝트 내의 권한이 어떤 팀에 대한 것인지 지정하는 데 사용할 수 있습니다. |
| `teamId` | `teamName`이 없는 경우 필수 | 문자열 | 팀을 지정하는 대체 방법으로 사용되는 팀 ID입니다. |
| `teamPermissions` | 필수 | 배열 | [팀 권한 문자열]({{site.baseurl}}/api/objects_filters/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team) 테이블의 팀 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 팀에 대해 해당 권한을 가지고 있음을 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="팀 권한 오브젝트" }

## 역할 오브젝트

유효한 역할 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다:

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `roleName` | 선택 사항 | 문자열 | 사용자에게 할당되는 역할의 이름입니다. |
| `roleId` | `roleName`이 없는 경우 필수 | 문자열 | 역할을 지정하는 대체 방법으로 사용되는 역할 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="역할 오브젝트" }

## 부록

### 회사 권한 문자열

| UI에 표시되는 이름 | SCIM API 문자열 |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="회사 권한 문자열 #company" }

### 워크스페이스 권한 문자열

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="워크스페이스 권한 문자열 #workspace-strings" }

### 팀 권한 문자열

| 권한 이름 | SCIM API 문자열 |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profile | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="팀 권한 문자열 #team" }

### 부서 문자열

| UI에 표시되는 이름 | SCIM API 문자열 |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="부서 문자열" }
{% endsdktab %}
{% endsdktabs %}