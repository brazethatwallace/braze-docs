---
nav_title: "APIの概要"
article_title: "APIの概要"
page_order: 2.1
description: "このリファレンス記事では、REST APIとは何か、用語、APIキーの概要など、APIの基本について説明します。"
page_type: reference
alias: /api/api_key/
---

# APIの概要 {#api-overview}

> このリファレンス記事では、一般的な用語、REST APIキーや権限の概要、それらを安全に保つ方法など、APIの基本について説明します。

## Braze REST APIコレクション {#braze-rest-api-collection}

| コレクション                                                                 | 目的                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [カタログ]({{site.baseurl}}/api/endpoints/catalogs)                       | Brazeキャンペーンで参照するカタログやカタログアイテムを作成・管理します。    |
| [Cloud Data Ingestion]({{site.baseurl}}/api/endpoints/cdi)                | データウェアハウスの統合と同期を管理します。                                    |
| [メールリストとアドレス]({{site.baseurl}}/api/endpoints/email)         | Brazeとメールシステム間の双方向同期を設定・管理します。           |
| [エクスポート]({{site.baseurl}}/api/endpoints/export)                           | キャンペーン、キャンバス、KPIsなどのさまざまな詳細にアクセスしてエクスポートします。        |
| [メディアライブラリ]({{site.baseurl}}/api/endpoints/media_library)             | Braze内のアセットを管理します。                                                           |
| [メッセージ]({{site.baseurl}}/api/endpoints/messaging)                      | キャンペーンやキャンバスのスケジュール設定、送信、管理を行います。                               |
| [ユーザー設定センター]({{site.baseurl}}/api/endpoints/preference_center)     | ユーザー設定センターを構築し、そのスタイルを更新します。                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim)                               | クラウドベースのアプリケーションやサービスでユーザーIDを管理します。                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms)                                 | 購読グループ内のユーザーの電話番号を管理します。                         |
| [購読グループ]({{site.baseurl}}/api/endpoints/subscription_groups) | Brazeダッシュボードに保存されているSMSおよびメール購読グループの一覧表示と更新を行います。 |
| [テンプレート]({{site.baseurl}}/api/endpoints/templates)                     | メールメッセージングおよびContent Blocksのテンプレートを作成・更新します。                   |
| [ユーザーデータ]({{site.baseurl}}/api/endpoints/user_data)                     | ユーザーの識別、トラッキング、管理を行います。                                               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze REST APIコレクション" }

## API の定義 {#api-definitions}

以下は、Braze REST API ドキュメントで使用される用語の概要です。

### エンドポイント {#endpoints}

Braze は、ダッシュボードと REST エンドポイント用に複数の異なるインスタンスを管理しています。アカウントがプロビジョニングされると、以下の URL のいずれかにログインします。プロビジョニングされたインスタンスに基づいて、正しい REST エンドポイントを使用してください。不明な場合は、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開くか、以下の表を使用して、使用しているダッシュボードの URL を正しい REST エンドポイントと照合してください。

Braze で REST エンドポイントを確認するには:

1. Braze にログインし、**設定** > **API と識別子** > **API キー**に移動します。
2. 既存の API キーを選択するか、**API キーを作成**を選択して新しいキーを作成します。
3. このタブに表示される REST エンドポイントをコピーし、API リクエストに使用します。

{% alert important %}
API コールにエンドポイントを使用する場合は、REST エンドポイントを使用してください。

SDK 統合には、REST エンドポイントではなく[SDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)を使用してください。
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

### API の制限 {#api-limits}

ほとんどの API について、Braze では1時間あたり250,000リクエストのデフォルトレート制限が設定されています。ただし、特定のリクエストタイプには、顧客ベース全体の大量データをより適切に処理するために独自のレート制限が適用されます。詳細については、[API レート制限]({{site.baseurl}}/api/api_limits)を参照してください。

### ユーザー ID {#user-ids}

- **external ID**: `external_id`は、データを送信する対象のユーザーを一意に識別するものです。この識別子は、同一ユーザーに対して複数のプロファイルが作成されることを防ぐため、Braze SDKで設定したものと同じである必要があります。
- **Braze ユーザー ID**: `braze_id`は、Braze が設定する一意のユーザー識別子です。この識別子を使用して、external_id に加えて REST API 経由でユーザーを削除できます。

詳細については、プラットフォームに応じて以下の記事を参照してください: [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift)、[Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android)、[Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)。

## REST APIキーについて {#about-rest-api-keys}

REST API (REST Application Programming Interface) キーは、APIに渡してAPI呼び出しを認証し、呼び出し元のアプリケーションやユーザーを識別するための一意のコードです。APIへのアクセスは、会社のREST APIエンドポイントへのHTTPS Webリクエストを使用して行います。REST APIキーはアプリ識別子キーと連携して、データのトラッキング、アクセス、送信、エクスポート、分析を行い、すべてがスムーズに動作していることを確認します。

ワークスペースとAPIキーはBrazeにおいて密接に連動しています。ワークスペースは、同じアプリケーションの複数プラットフォームにわたるバージョンを管理するように設計されています。多くのお客様は、同じプラットフォーム上の無料版とプレミアム版のアプリケーションを格納するためにもワークスペースを使用しています。お気づきかもしれませんが、これらのワークスペースもREST APIを利用しており、独自のREST APIキーを持っています。これらのキーは、API上の特定のエンドポイントへのアクセスを含むように個別にスコープを設定できます。APIへの各呼び出しには、対象のエンドポイントへのアクセス権を持つキーを含める必要があります。

REST APIキーとワークスペースAPIキーの両方を`api_key`と呼びます。`api_key`は各リクエストにリクエストヘッダーとして含まれ、REST APIの使用を許可する認証キーとして機能します。これらのREST APIは、ユーザーのトラッキング、メッセージの送信、ユーザーデータのエクスポートなどに使用されます。新しいREST APIキーを作成する際には、特定のエンドポイントへのアクセス権を付与する必要があります。APIキーに特定の権限を割り当てることで、そのAPIキーが認証できる呼び出しを正確に制限できます。

![APIキータブのREST APIキーパネル。]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
REST APIキーに加えて、APIからアプリ、テンプレート、キャンバス、キャンペーン、Content Cards、セグメントなどの特定の要素を参照するために使用できる識別子キーと呼ばれるタイプのキーも存在します。詳細については、[API識別子タイプ]({{site.baseurl}}/api/identifier_types)を参照してください。
{% endalert %}

### REST APIキーの作成 {#creating-rest-api-keys}

新しいREST APIキーを作成するには:

1. **設定** > **APIと識別子**に移動します。
2. **APIキーを作成**を選択します。
3. 一目で識別できるように新しいキーに名前を付けます。
4. 新しいキーの[許可リストに登録するIPアドレス](#api-ip-allowlisting)とサブネットを指定します。
5. 新しいキーに関連付ける[権限](#rest-api-key-permissions)を選択します。

{% alert important %}
新しいAPIキーを作成した後は、権限のスコープや許可リストに登録されたIPを編集できないことにご注意ください。この制限はセキュリティ上の理由から設けられています。キーのスコープを変更する必要がある場合は、更新された権限で新しいキーを作成し、古いキーの代わりにそのキーを実装してください。実装が完了したら、古いキーを削除できます。
{% endalert %}

### REST APIキーの権限 {#rest-api-key-permissions}

APIキーの権限は、ユーザーまたはグループに割り当てて、特定のAPI呼び出しへのアクセスを制限できる権限です。APIキーの権限一覧を表示するには、**設定** > **APIと識別子**に移動し、APIキーを選択します。

{% tabs %}
{% tab ユーザーデータ %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | ユーザー属性、カスタムイベント、購入を記録します。 |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | 任意のユーザーを削除します。 |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias) | 既存ユーザーの新しいエイリアスを作成します。 |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) | エイリアスのみのユーザーをexternal IDで識別します。 |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | ユーザーIDでユーザープロファイル情報を照会します。 |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | セグメントでユーザープロファイル情報を照会します。 |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | 2人の既存ユーザーを統合します。 |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | 既存ユーザーのexternal IDを変更します。 |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | 既存ユーザーのexternal IDを削除します。 |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update) | 既存ユーザーのエイリアスを更新します。 |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) | グローバルコントロールグループのユーザープロファイル情報を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

 {% endtab %}
 {% tab メール %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses) | 購読解除したメールアドレスを照会します。 |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) | メールアドレスのステータスを変更します。 |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces) | ハードバウンスしたメールアドレスを照会します。 |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces) | ハードバウンスリストからメールアドレスを削除します。 |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) | スパムリストからメールアドレスを削除します。 |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist) | メールアドレスをブロックリストに登録します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab メッセージ %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | 特定のユーザーに即時メッセージを送信します。 |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) | 特定の時間にメッセージを送信するようスケジュールします。 |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages) | スケジュールされたメッセージを更新します。 |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages) | スケジュールされたメッセージを削除します。 |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | スケジュールされたすべてのブロードキャストメッセージを照会します。 |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) | iOS Live Activityを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab キャンペーン %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) | 既存のキャンペーンの送信をトリガーします。 |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) | APIトリガー配信でキャンペーンの送信をスケジュールします。 |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns) | APIトリガー配信でスケジュールされたキャンペーンを更新します。 |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages) | APIトリガー配信でスケジュールされたキャンペーンを削除します。 |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | キャンペーンの一覧を照会します。 |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 期間を指定してキャンペーンの分析データを照会します。 |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | 特定のキャンペーンの詳細を照会します。 |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | 期間を指定してメッセージ送信の分析データを照会します。 |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | メッセージ一括送信のトラッキング用送信IDを作成します。 |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | キャンペーン内の特定のメッセージバリエーションのURL詳細を照会します。 |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) | トランザクショナルメッセージングエンドポイントを使用してトランザクショナルメッセージを送信する機能を提供します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab キャンバス %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) | 既存のキャンバスの送信をトリガーします。 |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | APIトリガー配信でキャンバスの送信をスケジュールします。 |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases) | APIトリガー配信でスケジュールされたキャンバスを更新します。 |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases) | APIトリガー配信でスケジュールされたキャンバスを削除します。 |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | キャンバスの一覧を照会します。 |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | 期間を指定してキャンバスの分析データを照会します。 |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | 特定のキャンバスの詳細を照会します。 |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | 期間を指定してキャンバスの分析データのロールアップを照会します。 |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias) | キャンバスステップ内の特定のメッセージバリエーションのURL詳細を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab セグメント %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | セグメントの一覧を照会します。 |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | 期間を指定してセグメントの分析データを照会します。 |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | 特定のセグメントの詳細を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab 購入 %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | アプリ内で購入された商品の一覧を照会します。 |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | 期間を指定してアプリ内の1日あたりの総消費金額を照会します。 |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | 期間を指定してアプリ内の1日あたりの合計購入回数を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab イベント %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | カスタムイベントの一覧を照会します。 |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | 期間を指定してカスタムイベントの発生回数を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab セッション %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | 期間を指定して1日あたりのセッション数を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab KPIs %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | 期間を指定して1日あたりのユニークアクティブユーザー数を照会します。 |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | 期間を指定して30日間のローリングウィンドウにおける合計ユニークアクティブユーザー数を照会します。 |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | 期間を指定して1日あたりの新規ユーザー数を照会します。 |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | 期間を指定して1日あたりのアプリアンインストール数を照会します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab テンプレート %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | ダッシュボードで新しいメールテンプレートを作成します。 |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | 特定のテンプレートの情報を照会します。 |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | メールテンプレートの一覧を照会します。 |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | ダッシュボードに保存されたメールテンプレートを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab SSO %}

| 権限 | 説明 |
| --- | --- |
| `sso.saml.login` | IDプロバイダー起点のログインを設定します。詳細については、[サービスプロバイダー (SP) 起点のログイン]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab Content Blocks %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | 特定のテンプレートの情報を照会します。 |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Content Blocksの一覧を照会します。 |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | ダッシュボードで新しいContent Blockを作成します。 |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | ダッシュボード上の既存のContent Blockを更新します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab ユーザー設定センター %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | ユーザー設定センターを取得します。 |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | ユーザー設定センターの一覧を取得します。 |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | ユーザー設定センターを作成または更新します。 |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | ユーザーのユーザー設定センターリンクを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab 購読 %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | 購読グループのステータスを設定します。 |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | 購読グループのステータスを取得します。 |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | 特定のユーザーが明示的に購読および購読解除している購読グループのステータスを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab SMS %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers) | 無効な電話番号を照会します。 |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) | ユーザーから無効な電話番号フラグを削除します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab カタログ %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | 既存のカタログに複数のアイテムを追加します。 |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | 既存のカタログ内の複数のアイテムを更新します。 |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | 既存のカタログから複数のアイテムを削除します。 |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | 既存のカタログから単一のアイテムを取得します。 |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | 既存のカタログ内の単一のアイテムを更新します。 |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | 既存のカタログに単一のアイテムを作成します。 |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item) | 既存のカタログから単一のアイテムを削除します。 |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | 既存のカタログの単一のアイテムを置き換えます。 |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | カタログを作成します。 |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | カタログの一覧を取得します。 |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | カタログを削除します。 |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | 既存のカタログからアイテムのプレビューを取得します。 |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | 既存のカタログ内のアイテムを置き換えます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% tab SDK認証 %}

| 権限 | エンドポイント | 説明 |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | アプリの新しいSDK認証キーを作成します。 |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key) | SDK認証キーをアプリのプライマリキーとしてマークします。 |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | アプリのSDK認証キーを削除します。 |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | アプリのすべてのSDK認証キーを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーの権限" }

{% endtab %}
{% endtabs %}

### REST APIキーの管理 {#managing-rest-api-keys}

既存のREST APIキーの詳細を表示したり削除したりするには、**設定** > **APIと識別子** > **APIキー**タブに移動します。REST APIキーは作成後に編集できないことにご注意ください。

**APIキー**タブには、各キーについて以下の情報が表示されます。

| フィールド | 説明 |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| APIキー名 | 作成時にキーに付けた名前です。 |
| 識別子 | APIキーです。 |
| 作成者 | キーを作成したユーザーのメールアドレスです。2023年6月以前に作成されたキーの場合、このフィールドには「N/A」と表示されます。 |
| 作成日 | このキーが作成された日付です。 |
| 最終使用日 | このキーが最後に使用された日付です。一度も使用されていないキーの場合、このフィールドには「N/A」と表示されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="REST APIキーの管理" }

APIキーの詳細を表示するには、キーにカーソルを合わせて<i class="fa-solid fa-eye" alt="表示"></i> **表示**を選択します。ここには、このキーが持つすべての権限、ホワイトリストに登録されたIP（ある場合）、およびこのキーがBraze IPホワイトリストにオプトインしているかどうかが含まれます。

![BrazeダッシュボードのAPIキー権限一覧。]({% image_buster /assets/img_archive/view-api-key.png %})

[ユーザーを削除]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)しても、Brazeはそのユーザーが作成した関連APIキーを削除しないことにご注意ください。キーを削除するには、キーにカーソルを合わせて<i class="fa-solid fa-trash-can" alt="削除"></i> **削除**を選択します。

![ゴミ箱アイコンがハイライトされた「Last Seen」という名前のAPIキー。「削除」と表示されています。]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### REST APIキーのセキュリティ {#rest-api-key-security}

APIキーはAPI呼び出しの認証に使用されます。新しいREST APIキーを作成する際には、特定のエンドポイントへのアクセス権を付与する必要があります。APIキーに特定の権限を割り当てることで、そのAPIキーが認証できる呼び出しを正確に制限できます。

REST APIキーは潜在的に機密性の高いREST APIエンドポイントへのアクセスを許可するため、これらのキーを安全に保管し、信頼できるパートナーとのみ共有してください。公開してはなりません。例えば、このキーを使用してWebサイトからAJAX呼び出しを行ったり、その他の公開的な方法で公開したりしないでください。

良いセキュリティプラクティスは、ユーザーに業務遂行に必要な最小限のアクセス権のみを割り当てることです。この原則は、各キーに権限を割り当てることでAPIキーにも適用できます。これらの権限により、アカウントのさまざまな領域に対するセキュリティと制御が向上します。

{% alert warning %}
REST APIキーは潜在的に機密性の高いREST APIエンドポイントへのアクセスを許可するため、安全に保管し使用してください。例えば、このキーを使用してWebサイトからAJAX呼び出しを行ったり、その他の公開的な方法で公開したりしないでください。
{% endalert %}

誤ってキーを公開してしまった場合は、開発者コンソールから削除できます。このプロセスについてサポートが必要な場合は、[サポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を開いてください。

### REST APIキーとSDK APIキーのセキュリティ {#security-of-rest-api-keys-and-sdk-api-keys}

REST APIキーとSDK APIキーにはそれぞれ異なるセキュリティプロファイルがあります。

| | REST APIキー | SDK APIキー |
|---|---|---|
| 用途 | REST APIのサーバーサイド認証（メッセージ送信、データエクスポート、ユーザー管理） | Braze SDKのクライアントサイド識別（データ取り込み、アプリ内メッセージ、Content Cards） |
| 可視性 | **非公開にする必要があります**。クライアントサイドのコード、公開リポジトリ、またはユーザーアプリケーションに公開しないでください。 | 公開されることを前提に設計されています。Google AnalyticsのトラッキングIDと同様に、アプリバイナリにバンドルされたり、WebブラウザのJavaScriptで確認可能です。 |
| 公開された場合の対処 | 直ちにキーを無効化し、**設定** > **APIと識別子** > **APIキー**で代替キーを作成してください。公開されたREST APIキーはメッセージの送信、ユーザーデータのエクスポート、アカウント設定の変更に使用される可能性があります。 | 対応は不要です。SDK APIキーはデータの取り込みとクライアントサイドのメッセージング（アプリ内メッセージやContent Cardsなど）の取得のみが可能です。ユーザーデータのエクスポート、代理でのメッセージ送信、キャンペーンの変更はできません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="REST APIキーとSDK APIキーのセキュリティ" }

### API IP許可リスト {#api-ip-allowlisting}

セキュリティを強化するために、特定のREST APIキーに対してREST APIリクエストの送信を許可するIPアドレスとサブネットのリストを指定できます。これは許可リスト（ホワイトリスト）と呼ばれます。特定のIPアドレスまたはサブネットを許可するには、新しいREST APIキーの作成時に**ホワイトリストIP**セクションに追加します。

![APIキー作成時にIPを許可リストに登録するオプション。]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

何も指定しない場合、任意のIPアドレスからリクエストを送信できます。

{% alert tip %}
Braze間のwebhookを作成し許可リストを使用している場合は、[ホワイトリストに登録するIP]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)のリストを参照してください。
{% endalert %}

## API認証とセキュリティ {#api-authentication-and-security}

### Bearerトークン認証 {#bearer-token-authentication}

Brazeは、`Authorization`リクエストヘッダーにBearerトークンとして渡されたREST APIキーを使用してREST APIリクエストを認証します。リクエストを送信する際は、以下の形式でAPIキーを含めてください。

```bash
Authorization: Bearer YOUR_REST_API_KEY
```

各リクエストに対して、Brazeは以下のサーバー側の検証チェックを実行します。

1. **トークンの有効性：** REST APIキーがBrazeに存在し、アクティブであること（たとえば、取り消されたり無効化されていないこと）を確認します。
2. **トークンの認可：** APIキーがリクエストされたエンドポイントに必要な権限を持っていることを確認します。

認証に失敗した場合、APIはHTTPステータスコードを含むエラーレスポンスを返します。たとえば、`401 Unauthorized`は無効なキーまたはキーの欠落を示し、`403 Forbidden`はキーがリクエストされたエンドポイントに対する権限を持っていないことを示します。詳しくは[APIエラー]({{site.baseurl}}/api/errors)を参照してください。

### リクエストヘッダーの大文字小文字 {#header-casing}

HTTPヘッダー名は大文字小文字を区別しないため、`Authorization`と`authorization`は同等です。`Content-Type`などの他の標準リクエストヘッダーにも同じことが当てはまります。お使いのHTTPクライアントが生成する任意の大文字小文字で送信してください。

Brazeは`Bearer`スキームの任意の大文字小文字（`Bearer`、`bearer`、`BEARER`）も受け付けます。REST APIキー自体は、発行されたとおりに正確に送信してください。

### ネットワークレベルのセキュリティ {#network-level-security}

BrazeへのREST APIリクエストは、リクエストパス全体にわたってTransport Layer Security（TLS）暗号化によって保護されます。以下の表は、サーバーからBrazeへのAPIリクエストのネットワークフローを示しています。

| ステップ | コンポーネント | 説明 |
| --- | --- | --- |
| 1 | お客様のサーバー | TLS暗号化を使用してHTTPSリクエストを開始します。 |
| 2 | Cloudflare | クライアントのTLS接続を終端し、ネットワークレベルの保護を適用します。 |
| 3 | Network Load Balancer（NLB） | アプリケーションインフラにパケットを転送します。NLBはレイヤー4で動作するため、レイヤー7のプロキシは行われません。パケットはHTTPレベルの検査や変更なしに転送されます。 |
| 4 | NGINXイングレス | 内部TLS接続を終端し、リクエストをルーティングします。 |
| 5 | Unicorn（アプリケーションサーバー） | 認証済みのリクエストを処理します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ネットワークレベルのセキュリティ" }

TLS暗号化はチェーン内のすべてのリンクをカバーします。お客様のサーバーはTLSを介してCloudflareに接続し、CloudflareはNLBを経由してNGINXイングレスへの別のTLS接続を確立するため、APIキーとリクエストデータは転送中も暗号化された状態を維持します。

## その他のリソース {#additional-resources}

### Ruby クライアントライブラリ {#ruby-client-library}

Ruby を使用して Braze を実装している場合、[Ruby クライアントライブラリ](https://github.com/braze-inc/braze-api-client-ruby)を使用してデータインポート時間を短縮できます。クライアントライブラリとは、特定のプログラミング言語（この場合は Ruby）に固有のコードの集まりであり、APIの使用を容易にするものです。

Ruby クライアントライブラリは[ユーザーエンドポイント]({{site.baseurl}}/api/endpoints/user_data)をサポートしています。

{% alert important %}
このクライアントライブラリはベータ版です。このライブラリの改善にご協力いただける場合は、[smb-product@braze.com](mailto:smb-product@braze.com) までフィードバックをお送りください。
{% endalert %}