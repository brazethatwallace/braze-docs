{% alert important %}
Braze는 사용자 접근 권한을 보다 유연하게 관리할 수 있는 [세분화된 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) 기능을 도입하고 있습니다. 마이그레이션 프로세스에 대해 알아보려면 [세분화된 권한으로 마이그레이션하기]({{site.baseurl}}/granular_permissions_migration)를 참조하고, [세분화된 SCIM API]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api/) 탭에서 세분화된 SCIM API 오브젝트 및 부록을 확인하세요.
{% endalert %}

## 권한 오브젝트 {#permissions-object}

권한 오브젝트는 SCIM ID 권한을 통해 사용자 리소스와 인터페이스할 때 일부 요청 및 응답에서 발견되는 필드입니다.

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

유효한 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다.

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `companyPermissions` | 선택 사항 | 배열 | [회사 권한 문자열]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company) 테이블의 회사 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 해당 권한을 가지고 있음을 나타냅니다. |
| `roles` | 선택 사항 | 배열 | [역할 오브젝트]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object)의 배열입니다. |
| `appGroup` | 필수 | 배열 | [워크스페이스 권한 오브젝트]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### 워크스페이스 권한 오브젝트 {#workspace-permission-object}

유효한 앱 그룹 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다.

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupName` | 선택 사항 | 문자열 | 워크스페이스의 이름입니다. 이 오브젝트에 포함된 권한이 적용될 워크스페이스를 지정하는 데 사용됩니다. |
| `appGroupId` | `appGroupName`이 없으면 필수 | 문자열 | 워크스페이스의 ID로, 워크스페이스를 지정하는 대체 방법으로 사용됩니다. |
| `appGroupPermissionSets` | 선택 사항 | 배열 | 단일 [워크스페이스 권한 세트 오브젝트]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object)가 포함된 배열입니다. |
| `appGroupPermissions` | 필수 | 배열 | [워크스페이스 권한 문자열]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings) 테이블의 워크스페이스 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 워크스페이스에 대한 해당 권한을 가지고 있음을 나타냅니다. |
| `team` | 선택 사항 | 배열 | [Teams 권한 오브젝트]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object)의 배열입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object #workspace-permission-object" }

### 워크스페이스 권한 세트 오브젝트 {#workspace-permissions-set-object}

유효한 워크스페이스 권한 세트 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다.

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | 선택 사항 | 문자열 | 이 워크스페이스에 대해 사용자에게 할당되는 워크스페이스 권한 세트의 이름입니다. |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`이 없으면 필수 | 문자열 | 워크스페이스의 ID로, 이 워크스페이스에 대해 사용자에게 할당된 워크스페이스 권한 세트를 지정하는 대체 방법으로 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object #workspace-permissions-set-object" }

### Teams 권한 오브젝트 {#team-permissions-object}

유효한 Teams 권한 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다.

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `teamName` | 선택 사항 | 문자열 | 팀의 이름으로, 이 오브젝트 내의 권한이 어떤 팀에 적용되는지 지정하는 데 사용할 수 있습니다. |
| `teamId` | `teamName`이 없으면 필수 | 문자열 | 팀의 ID로, 팀을 지정하는 대체 방법으로 사용됩니다. |
| `teamPermissions` | 필수 | 배열 | [Teams 권한 문자열]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team) 테이블의 팀 수준 권한 문자열 배열로, 문자열이 존재하면 사용자가 지정된 팀에 대한 해당 권한을 가지고 있음을 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## 역할 오브젝트 {#role-object}

유효한 역할 오브젝트는 다음 키-값 페어를 가진 JSON 오브젝트입니다.

| 키 | 필수 | 데이터 유형 | 설명 |
| --- | --- | --- | --- |
| `roleName` | 선택 사항 | 문자열 | 사용자에게 할당되는 역할의 이름입니다. |
| `roleId` | `roleName`이 없으면 필수 | 문자열 | 역할의 ID로, 역할을 지정하는 대체 방법으로 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## 부록 {#appendix}

### 회사 권한 문자열 {#company}

| UI에 표시되는 이름 | SCIM API 문자열 |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings #company" }

### 워크스페이스 권한 문자열 {#workspace-strings}

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace permission strings #workspace-strings" }

### Teams 권한 문자열 {#team}

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings #team" }

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