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
| 管理者 | `admin` |
| 会社の設定を管理 | `manage_company_settings` |
| ワークスペースの作成と削除 | `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Company permission strings #company" }

### ワークスペース権限文字列 {#workspace-strings}

| 権限名 | SCIM API文字列 |
| --- | --- |
| キャンペーンを表示 | `view_campaigns` |
| キャンペーンを編集 | `edit_campaigns` |
| キャンペーンをアーカイブ | `archive_campaigns` |
| キャンバスを表示 | `view_canvases` |
| キャンバスを編集 | `edit_canvases` |
| キャンバスをアーカイブ | `archive_canvases` |
| フリークエンシーキャップルールを表示 | `view_frequency_caps` |
| フリークエンシーキャップルールを編集 | `edit_frequency_caps` |
| メッセージの優先順位付けを表示 | `view_message_prioritization` |
| メッセージの優先順位付けを編集 | `edit_message_prioritization` |
| Content Blocksを表示 | `view_content_blocks` |
| Content Blocksを編集 | `edit_content_blocks` |
| Content Blocksをアーカイブ | `archive_content_blocks` |
| フィーチャーフラグを表示 | `view_feature_flags` |
| フィーチャーフラグを編集 | `edit_feature_flags` |
| フィーチャーフラグをアーカイブ | `archive_feature_flags` |
| セグメントを表示 | `view_segments` |
| セグメントを編集 | `edit_segments` |
| セグメントをアーカイブ | `archive_segments` |
| グローバルコントロールグループを表示 | `view_global_control_group` |
| グローバルコントロールグループを編集 | `edit_global_control_group` |
| IAMテンプレートを表示 | `view_iam_templates` |
| IAMテンプレートを編集 | `edit_iam_templates` |
| IAMテンプレートをアーカイブ | `archive_iam_templates` |
| メールテンプレートを表示 | `view_email_templates` |
| メールテンプレートを編集 | `edit_email_templates` |
| メールテンプレートをアーカイブ | `archive_email_templates` |
| Webhookテンプレートを表示 | `view_webhook_templates` |
| Webhookテンプレートを編集 | `edit_webhook_templates` |
| Webhookテンプレートをアーカイブ | `archive_webhook_templates` |
| メールリンクテンプレートを表示 | `view_link_templates` |
| メールリンクテンプレートを編集 | `edit_link_templates` |
| メディアライブラリアセットを表示 | `view_media_library_assets` |
| ロケーションを表示 | `view_locations` |
| ロケーションを編集 | `edit_locations` |
| ロケーションをアーカイブ | `archive_locations` |
| プロモーションコードを表示 | `view_promotion_codes` |
| プロモーションコードを編集 | `edit_promotion_codes` |
| プロモーションコードをエクスポート | `export_promotion_codes` |
| ユーザー設定センターを表示 | `view_preference_centers` |
| ユーザー設定センターを編集 | `edit_preference_centers` |
| レポートを編集 | `edit_reports` |
| プレースメントを表示 | `view_placements` |
| プレースメントを編集 | `edit_placements` |
| プレースメントをアーカイブ | `archive_placements` |
| バナーテンプレートを表示 | `view_banner_templates` |
| 多言語設定を表示 | `view_multi_language_settings` |
| BrazeAI Operator<sup>TM</sup>を使用 | `use_operator` |
| Decisioning Studioエージェントを表示 | `view_decisioning_studio_agents` |
| Decisioning Studioオーディエンスを表示 | `view_decisioning_studio_audience` |
| Decisioning Studioコンバージョンイベントを表示 | `view_decisioning_studio_conversion_event` |
| Decisioning Studioガードレールを表示 | `view_decisioning_studio_guardrails` |
| キャンペーンを起動 | `launch_campaigns` |
| キャンバスを起動 | `launch_canvases` |
| ダッシュボードユーザーを編集 | `edit_dashboard_users` |
| メディアライブラリアセットを編集 | `edit_media_library_assets` |
| メディアライブラリアセットを削除 | `delete_media_library_assets` |
| ユーザーインポートを表示 | `view_import_users` |
| ユーザーをインポート | `import_users` |
| ユーザーデータを編集 | `edit_user_data` |
| ユーザーマージ記録を表示 | `view_user_merge_records` |
| 重複ユーザーをマージ | `merge_duplicate_users` |
| APIキーを表示 | `view_api_keys` |
| APIキーを編集 | `edit_api_keys` |
| 内部グループを表示 | `view_internal_user_groups` |
| 内部グループを編集 | `edit_internal_user_groups` |
| 内部グループを削除 | `delete_internal_user_groups` |
| メッセージアクティビティログを表示 | `view_message_activity_log` |
| イベントユーザーログを表示 | `view_event_user_log` |
| API識別子を表示 | `view_api_identifiers` |
| API使用状況ダッシュボードを表示 | `view_api_usage_dashboard` |
| API制限を表示 | `view_api_limits` |
| API使用アラートを表示 | `view_api_usage_alerts` |
| API使用アラートを編集 | `edit_api_usage_alerts` |
| SDKデバッガーを表示 | `view_sdk_debugger` |
| SDKデバッガーを編集 | `edit_sdk_debugger` |
| Content Blocksを起動 | `launch_content_blocks` |
| クラウドデータ取り込みを編集 | `edit_cloud_data_ingestion` |
| アプリ設定を表示 | `view_app_settings` |
| アプリ設定を編集 | `edit_app_settings` |
| プッシュ設定を表示 | `view_push_settings` |
| プッシュ設定を編集 | `edit_push_settings` |
| チームを表示 | `view_teams` |
| チームを編集 | `edit_teams` |
| チームをアーカイブ | `archive_teams` |
| カスタム属性を表示 | `view_custom_attributes` |
| カスタム属性を編集 | `edit_custom_attributes` |
| カスタム属性をブロックリストに追加 | `blocklist_custom_attributes` |
| カスタム属性を削除 | `delete_custom_attributes` |
| カスタム属性をエクスポート | `export_custom_attributes` |
| カスタムイベントを表示 | `view_custom_events` |
| カスタムイベントを編集 | `edit_custom_events` |
| カスタムイベントをブロックリストに追加 | `blocklist_custom_events` |
| カスタムイベントを削除 | `delete_custom_events` |
| カスタムイベントをエクスポート | `export_custom_events` |
| カスタムイベントプロパティのセグメンテーションを編集 | `edit_custom_event_property_segmentation` |
| 製品を表示 | `view_products` |
| 製品を編集 | `edit_products` |
| 製品をブロックリストに追加 | `blocklist_products` |
| 購入プロパティのセグメンテーションを編集 | `edit_purchase_property_segmentation` |
| タグを表示 | `view_tags` |
| タグを編集 | `edit_tags` |
| タグを削除 | `delete_tags` |
| メール設定を表示 | `view_email_settings` |
| メール設定を編集 | `edit_email_settings` |
| カタログを表示 | `view_catalogs` |
| カタログを編集 | `edit_catalogs` |
| カタログをエクスポート | `export_catalogs` |
| カタログを削除 | `delete_catalogs` |
| WhatsApp設定を表示 | `view_whatsapp_settings` |
| テクノロジーパートナーを編集 | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace permission strings #workspace-strings" }

### チーム権限文字列 {#team}

| 権限名 | SCIM API文字列 |
| --- | --- |
| キャンペーンを表示 | `view_campaigns` |
| キャンペーンを編集 | `edit_campaigns` |
| キャンペーンをアーカイブ | `archive_campaigns` |
| キャンバスを表示 | `view_canvases` |
| キャンバスを編集 | `edit_canvases` |
| キャンバスをアーカイブ | `archive_canvases` |
| フリークエンシーキャップルールを表示 | `view_frequency_caps` |
| フリークエンシーキャップルールを編集 | `edit_frequency_caps` |
| メッセージの優先順位付けを表示 | `view_message_prioritization` |
| メッセージの優先順位付けを編集 | `edit_message_prioritization` |
| Content Blocksを表示 | `view_content_blocks` |
| フィーチャーフラグを表示 | `view_feature_flags` |
| フィーチャーフラグを編集 | `edit_feature_flags` |
| フィーチャーフラグをアーカイブ | `archive_feature_flags` |
| セグメントを表示 | `view_segments` |
| セグメントを編集 | `edit_segments` |
| グローバルコントロールグループを編集 | `edit_global_control_group` |
| IAMテンプレートを表示 | `view_iam_templates` |
| IAMテンプレートを編集 | `edit_iam_templates` |
| IAMテンプレートをアーカイブ | `archive_iam_templates` |
| メールテンプレートを表示 | `view_email_templates` |
| メールテンプレートを編集 | `edit_email_templates` |
| メールテンプレートをアーカイブ | `archive_email_templates` |
| Webhookテンプレートを表示 | `view_webhook_templates` |
| Webhookテンプレートを編集 | `edit_webhook_templates` |
| Webhookテンプレートをアーカイブ | `archive_webhook_templates` |
| メールリンクテンプレートを表示 | `view_link_templates` |
| メールリンクテンプレートを編集 | `edit_link_templates` |
| メディアライブラリアセットを表示 | `view_media_library_assets` |
| ロケーションを表示 | `view_locations` |
| ロケーションを編集 | `edit_locations` |
| ロケーションをアーカイブ | `archive_locations` |
| プロモーションコードを表示 | `view_promotion_codes` |
| プロモーションコードを編集 | `edit_promotion_codes` |
| プロモーションコードをエクスポート | `export_promotion_codes` |
| ユーザー設定センターを表示 | `view_preference_centers` |
| ユーザー設定センターを編集 | `edit_preference_centers` |
| レポートを表示 | `view_reports` |
| レポートを作成 | `create_reports` |
| レポートを編集 | `edit_reports` |
| バナーテンプレートを表示 | `view_banner_templates` |
| 多言語設定を表示 | `view_multi_language_settings` |
| BrazeAI Operator<sup>TM</sup>を使用 | `use_operator` |
| Decisioning Studioエージェントを表示 | `view_decisioning_studio_agents` |
| キャンペーンを起動 | `launch_campaigns` |
| キャンバスを起動 | `launch_canvases` |
| ダッシュボードユーザーを編集 | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Team permission strings #team" }

### 部門の文字列 {#department-strings}

| UIでの表示 | SCIM API文字列 |
| --- | --- |
| 代理店 / サードパーティ | `agency` |
| BI / 分析 | `bi` |
| 経営幹部 | `c_suite` |
| エンジニアリング | `engineering` |
| ファイナンス | `finance` |
| マーケティング / 編集 | `marketing` |
| 製品管理 | `pm` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Department strings" }