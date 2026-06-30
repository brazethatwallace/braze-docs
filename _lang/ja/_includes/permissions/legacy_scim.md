{% alert important %}
Brazeは、ユーザーアクセスをより柔軟に管理する手段として、[きめ細かい権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions)を導入しています。移行プロセスについては[きめ細かい権限への移行]({{site.baseurl}}/granular_permissions_migration)を参照してください。また、きめ細かいSCIM APIオブジェクトと付録については[きめ細かいSCIM API]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api/)タブを参照してください。
{% endalert %}

## 権限オブジェクト {#permissions-object}

権限オブジェクトは、SCIM IDの権限を通じてユーザーリソースとやり取りする際に、一部のリクエストとレスポンスに含まれるフィールドです。

{% alert note %}
Brazeではアプリグループはワークスペースに改名されましたが、このページのキーはまだ古い用語を参照しています（例: `appGroup`、`appGroupName`）。
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
| `companyPermissions` | オプション | 配列 | [会社権限文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_company)テーブルからの会社レベルの権限文字列の配列。文字列が存在する場合、そのユーザーが対応する権限を持っていることを示します。 |
| `roles` | オプション | 配列 | [ロールオブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_role-object)の配列。 |
| `appGroup` | 必須 | 配列 | [ワークスペース権限オブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Permissions object" }

### ワークスペース権限オブジェクト {#workspace-permission-object}

有効なアプリグループ権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupName` | オプション | 文字列 | ワークスペースの名前。このオブジェクトに含まれる権限がどのワークスペースに対するものかを指定するために使用します。 |
| `appGroupId` | `appGroupName`がない場合は必須 | 文字列 | ワークスペースのID。ワークスペースを指定する代替方法として機能します。 |
| `appGroupPermissionSets` | オプション | 配列 | 単一の[ワークスペース権限セットオブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-permissions-set-object)を持つ配列。 |
| `appGroupPermissions` | 必須 | 配列 | [ワークスペース権限文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_workspace-strings)テーブルからのワークスペースレベルの権限文字列の配列。文字列が存在する場合、そのユーザーが指定されたワークスペースに対する対応する権限を持っていることを示します。 |
| `team` | オプション | 配列 | [チーム権限オブジェクト]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team-permissions-object)の配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions object #workspace-permission-object" }

### ワークスペース権限セットオブジェクト {#workspace-permissions-set-object}

有効なワークスペース権限セットオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | オプション | 文字列 | このワークスペースでユーザーに割り当てられるワークスペース権限セットの名前。 |
| `appGroupPermissionSetID` | `appGroupPermissionSetName`がない場合は必須 | 文字列 | ワークスペースのID。このワークスペースでユーザーに割り当てられたワークスペース権限セットを指定する代替方法として機能します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Workspace permissions set object #workspace-permissions-set-object" }

### チーム権限オブジェクト {#team-permissions-object}

有効なチーム権限オブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `teamName` | オプション | 文字列 | チームの名前。このオブジェクト内の権限がどのチームに対するものかを指定するために使用できます。 |
| `teamId` | `teamName`がない場合は必須 | 文字列 | チームのID。チームを指定する代替方法として機能します。 |
| `teamPermissions` | 必須 | 配列 | [チーム権限文字列]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api#legacyscimapi_team)テーブルからのチームレベルの権限文字列の配列。文字列が存在する場合、そのユーザーが指定されたチームに対する対応する権限を持っていることを示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Team permissions object" }

## ロールオブジェクト {#role-object}

有効なロールオブジェクトは、以下のキーと値のペアを持つJSONオブジェクトです。

| キー | 必須 | データタイプ | 説明 |
| --- | --- | --- | --- |
| `roleName` | オプション | 文字列 | ユーザーに割り当てられるロールの名前。 |
| `roleId` | `roleName`がない場合は必須 | 文字列 | ロールのID。ロールを指定する代替方法として機能します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Role object" }

## 付録 {#appendix}

### 会社権限文字列 {#company}

| UIでの表示 | SCIM API文字列 |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings #company" }

### ワークスペース権限文字列 {#workspace-strings}

| 権限名 | SCIM API文字列 |
| --- | --- |
| Admin | `admin` |
| Access キャンペーン, キャンバス, Cards, セグメント, Media Library | `basic_access` |
| Approve and Deny キャンバス | `approve_deny_campaigns` |
| キャンペーン、キャンバスを送信 | `send_campaigns_canvases` |
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

### チーム権限文字列 {#team}

| 権限名 | SCIM API文字列 |
| --- | --- |
| Admin | `admin` |
| Access キャンペーン, キャンバス, Cards, セグメント, Media Library | `basic_access` |
| Approve and Deny キャンバス | `approve_deny_campaigns` |
| キャンペーン、キャンバスを送信 | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit セグメント | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profile | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
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