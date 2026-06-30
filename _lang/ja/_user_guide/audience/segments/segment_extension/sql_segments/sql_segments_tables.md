---
nav_title: "SQLテーブルリファレンス"
article_title: "SQLテーブルリファレンス"
page_order: 3
page_type: reference
toc_headers: h2
description: "このページは、クエリビルダー、SQLセグメントエクステンション、Snowflakeデータ共有で使用されるSnowflake SQLテーブルとカラムのリファレンスです。"
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQLテーブルリファレンス {#sql-table-reference}

このページは、以下のBrazeツールで利用可能なSnowflake SQLテーブルとカラムのリファレンスです。

- [クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Snowflakeデータ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

ほとんどのテーブルは3つのツールすべてで利用できます。**Snowflakeデータ共有のみ**と記載されたテーブルはSnowflakeデータ共有専用であり、クエリビルダーやSQLセグメントエクステンションではアクセスできません。

{% alert tip %}
これらのSQLテーブルは、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)に記載されているイベントに対応しています。たとえば、SQLテーブル`USERS_MESSAGES_EMAIL_SEND_SHARED`はCurrentsイベント`users.messages.email.Send`に対応しています。JSONイベントスキーマやパートナー固有のフォーマット（Amplitude、Mixpanel、Segment）が必要な場合は、Currents用語集を参照してください。
{% endalert %}

## 目次 {#table-of-contents}

テーブル | 説明
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | エージェントコンソールのエージェントが実行されたとき（**Snowflake データ共有のみ**）
[AGENTCONSOLE_RAWLLMREQUEST_SHARED](#AGENTCONSOLE_RAWLLMREQUEST_SHARED) | 各 LLM コールからの生情報（**Snowflake データ共有のみ**）
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | ツールが実行されたとき（**Snowflake データ共有のみ**）
[USER_CUSTOM_ATTRIBUTES_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED) | ユーザーごとのカスタムプロファイル属性の定期スナップショット
[USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED) | 有効日範囲付きのデフォルトプロファイル属性の履歴
[USER_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED) | ユーザーごとのデフォルトプロファイル属性の定期スナップショット
[USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED) | ユーザーごとのほぼリアルタイムのデフォルトプロファイル属性
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | 削除されていないカタログアイテム
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | Campaignが変更されたとき（**Snowflake データ共有のみ**）
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Canvasが変更されたとき（**Snowflake データ共有のみ**）
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | グローバルコントロールグループが変更されたとき
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | ユーザーがカスタムイベントを実行したとき
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | ユーザーがアプリをインストールし、パートナーにアトリビューションされたとき
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | ユーザーがロケーションを記録したとき
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | ユーザーが購入を行ったとき
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | ユーザーがアプリをアンインストールしたとき
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | ユーザーがアプリをアップグレードしたとき
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | ユーザーが初回セッションを行ったとき
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | ユーザーがNews Feedを閲覧したとき
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | ユーザーがアプリでセッションを終了したとき
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | ユーザーがアプリでセッションを開始したとき
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | ユーザーがジオフェンスエリアをトリガーしたとき（例: ジオフェンスへの入場または退出）。このイベントは他のイベントとバッチ処理され、標準イベントエンドポイントを通じて受信されるため、リアルタイムで表示されない場合があります。<br><br>このテーブルにジオフェンスアクティビティを記録するには、各ジオフェンスの詳細設定で **Enable Analytics for Enter** と **Enable Analytics for Exit** を選択してください。詳細は[ジオフェンスを手動で作成する]({{site.baseurl}}/user_guide/audience/locations_and_geofences/creating_geofences#manually-create-geofences)のステップ 3 を参照してください。
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | ユーザーがジオフェンスエリアをトリガーしたとき（例: ジオフェンスへの入場または退出）。このイベントは専用のジオフェンスエンドポイントを通じて受信されるため、ユーザーのデバイスがジオフェンスのトリガーを検出するとリアルタイムで受信されます。<br><br>また、ジオフェンスエンドポイントのレート制限により、一部のジオフェンスイベントが RecordEvent として反映されない場合があります。ただし、すべてのジオフェンスイベントは DataEvent で表現されます（バッチ処理による遅延が発生する可能性があります）。
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Live Activity の push-to-start トークンが変更されたとき
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Live Activity の更新トークンが変更されたとき
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | プッシュ通知トークンの状態が変更されたとき
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | ユーザーがメールなどのチャネルでグローバルに購読または購読解除されたとき
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | ユーザーがサブスクリプショングループに購読または購読解除されたとき
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | ユーザーがCampaignでコンバージョンしたとき
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | ユーザーがCampaignのコントロールグループに登録されたとき
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | ユーザーがCampaignでフリークエンシーキャップに達したとき
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | ユーザーが1次コンバージョン期間内に収益を生成したとき
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | ユーザーがキャンバスステップに進んだとき
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | ユーザーがCanvasのコンバージョンイベントでコンバージョンしたとき
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | ユーザーがCanvasに入ったとき
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | ユーザーがオーディエンス退出条件に一致してCanvasを退出したとき
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | ユーザーが例外イベントを実行してCanvasを退出したとき
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | ユーザーがCanvasの実験ステップでコンバージョンしたとき
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | ユーザーが実験ステップのパスに入ったとき
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | ユーザーがキャンバスステップでフリークエンシーキャップに達したとき
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | ユーザーが1次コンバージョンイベント期間内に収益を生成したとき
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | 元々スケジュールされたバナーメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | ユーザーがバナーをクリックしたとき
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | ユーザーがバナーを閲覧したとき
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 元々スケジュールされたコンテンツカードメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | ユーザーがコンテンツカードをクリックしたとき
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | ユーザーがコンテンツカードを閉じたとき
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | ユーザーがコンテンツカードを閲覧したとき
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | ユーザーにコンテンツカードを送信したとき
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 元々スケジュールされたメールメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | メールサービスプロバイダーがハードバウンスを返したとき。ハードバウンスは永続的な配信失敗を示します。
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | ユーザーがメール内のリンクをクリックしたとき
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | メールが遅延されたとき
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | メールが配信されたとき
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | メールがスパムとしてマークされたとき
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | ユーザーがメールを開封したとき
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | ユーザーにメールを送信したとき
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | メールがソフトバウンスしたとき
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | ユーザーがメールの配信停止を行ったとき
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | メールメッセージが優先度低下またはフリークエンシーキャップ後にリトライされたとき（**Snowflake データ共有のみ**）
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | ユーザーがフィーチャーフラグを閲覧したとき
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 元々スケジュールされたアプリ内メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | ユーザーがアプリ内メッセージをクリックしたとき
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | ユーザーがアプリ内メッセージを閲覧したとき
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | スケジュールされた LINE メッセージが LINE への送信前に配信できなかったとき
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | ユーザーが LINE メッセージ内のリンクをクリックしたとき
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | ユーザーから LINE メッセージを受信したとき
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | LINE メッセージが LINE に送信されたとき
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | LINE メッセージが優先度低下またはフリークエンシーキャップ後にリトライされたとき（**Snowflake データ共有のみ**）
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Live Activity にアウトカムイベントが発生したとき
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Live Activity メッセージが送信されたとき
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 元々スケジュールされたNews Feedカードメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | ユーザーがNews Feedカードをクリックしたとき
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | ユーザーがNews Feedカードを閲覧したとき
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 元々スケジュールされたプッシュ通知メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | プッシュ通知がバウンスしたとき
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | ユーザーが通知を受信した後、通知をクリックせずにアプリを開いたとき
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | アプリが開いている状態でユーザーがプッシュ通知を受信したとき。<br><br>このイベントは [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) ではサポートされておらず、[Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) では非推奨です。
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | ユーザーがプッシュ通知を開くか、プッシュ通知ボタン（アプリを開かない CLOSE ボタンを含む）をクリックしたとき。<br><br>プッシュボタンアクションには複数の結果があります。No、Decline、Cancel アクションは「クリック」であり、Accept アクションは「開封」です。両方ともこのテーブルに表示されますが、**BUTTON_ACTION_TYPE** 列で区別できます。例えば、`BUTTON_ACTION_TYPE` が No、Decline、Cancel ではないものでグループ化するクエリを使用できます。
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | ユーザーにプッシュ通知を送信したとき
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Braze 内で検出されたエラーにより RCS 送信が中断され、メッセージがドロップされたとき
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | エンドユーザーが RCS メッセージの UI 要素をタップまたはクリックして操作したとき
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | RCS メッセージがエンドユーザーのモバイルデバイスに正常に配信されたとき
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Braze がエンドユーザーからの RCS メッセージを受信したとき
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | エンドユーザーがデバイスで RCS メッセージを開いたとき
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | キャリアの介入により RCS メッセージの配信に失敗したとき
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | RCS メッセージが Braze のシステムからラストマイル配信パートナーに送信されたとき
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 元々スケジュールされた SMS メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | SMS メッセージがキャリアに送信されたとき
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMS メッセージが配信されたとき
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Braze が SMS メッセージを SMS サービスプロバイダーに配信できなかったとき
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | ユーザーから SMS メッセージを受信したとき
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | SMS メッセージがユーザーに配信されなかったとき
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMS メッセージが送信されたとき
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | ユーザーが SMS メッセージに含まれる Braze 短縮 URL をクリックしたとき
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | SMS メッセージが優先度低下またはフリークエンシーキャップ後にリトライされたとき（**Snowflake データ共有のみ**）
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 元々スケジュールされた Webhook メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Webhook メッセージが配信されたが、エンドポイントからエラーレスポンスが返されたとき
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | ユーザーに対して Webhook を送信したとき
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Webhook メッセージが優先度低下またはフリークエンシーキャップ後にリトライされたとき（**Snowflake データ共有のみ**）
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 元々スケジュールされた WhatsApp メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | ユーザーが WhatsApp メッセージ内のリンクまたはボタンをクリックしたとき
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | WhatsApp メッセージが配信されたとき
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsApp メッセージがユーザーに配信されなかったとき
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | ユーザーから WhatsApp メッセージを受信したとき
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | ユーザーが WhatsApp メッセージを開いたとき
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | ユーザーに対して WhatsApp メッセージを送信したとき
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | WhatsApp メッセージが優先度低下またはフリークエンシーキャップ後にリトライされたとき（**Snowflake データ共有のみ**）
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | ユーザーのランダムバケット番号が変更されたとき
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 顧客のリクエストによりユーザーが削除されたとき
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | ユーザーが別のユーザーのプロファイルとマージされ、元のプロファイルが孤立したとき
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | アプリスナップショット（**Snowflake データ共有のみ**）
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | Campaignメッセージバリエーションスナップショット（**Snowflake データ共有のみ**）
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | キャンバスフローステップスナップショット（**Snowflake データ共有のみ**）
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | キャンバスステップスナップショット（**Snowflake データ共有のみ**）
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Canvasバリエーションスナップショット（**Snowflake データ共有のみ**）
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | 実験ステップスナップショット（**Snowflake データ共有のみ**）


## エージェントコンソール {#agent-console}

{% alert note %}
エージェントコンソールテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`invocation_id` | `string` | このメッセージのグローバル一意 ID
`request_id` | `string` | この LLM リクエスト全体と完全な実行の一意 ID
`duration` | `int` | セッションの持続時間（秒）
`prompt_tokens` | `int` | このリクエストで使用されたプロンプトトークン数
`completion_tokens` | `int` | このリクエストで使用された補完トークン数
`total_tokens` | `int` | このリクエストで使用された合計トークン数
`cache_tokens` | `int` | このリクエストで使用されたキャッシュトークン数
`reasoning_tokens` | `int` | このリクエストで使用された推論トークン数
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`agent_id` | `string` | CustomerDefinedAgent の BSON ID
`agent_name` | `string` | CustomerDefinedAgent の名前
`model_provider` | `string` | LLM モデルプロバイダーの名前
`model_name` | `string` | このリクエストで使用された LLM モデルの名前
`provider_request_id` | `string` | API コールに対してモデルプロバイダーから付与されたリクエスト ID
`cache_hit` | `boolean` | このリクエストがキャッシュにヒットしてレスポンスを返したかどうか
`llm_owned_by_customer` | `boolean` | true の場合、顧客の API キーが使用されました。false の場合、Braze のキーが使用されました
`is_error` | `boolean` | このリクエストがエラーになったかどうか
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するCanvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するCanvasバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの external ID
`input` | `null,`&nbsp;`string` | [PII] LLM への入力
`output` | `null,`&nbsp;`string` | [PII] LLM からのレスポンス
`invocation_source` | `null,`&nbsp;`string` | LLM リクエストを呼び出した Ruby オブジェクト
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLEAGENTEXECUTEDSHARED #AGENTCONSOLEAGENTEXECUTEDSHARED" }

### AGENTCONSOLE_RAWLLMREQUEST_SHARED {#AGENTCONSOLE_RAWLLMREQUEST_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`invocation_id` | `string` | このメッセージのグローバル一意 ID
`request_id` | `string` | この LLM リクエスト全体と完全な実行の一意 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このイベントが属するアプリグループの BSON ID
`agent_id` | `string` | CustomerDefinedAgent の BSON ID
`agent_name` | `string` | CustomerDefinedAgent の名前
`model_provider` | `string` | LLM モデルプロバイダーの名前
`model_name` | `string` | このリクエストで使用された LLM モデルの名前
`duration` | `int`,&nbsp;`null` | セッションの持続時間（秒）
`request` | `string` | [PII] リクエストで使用されたプロンプト
`http_status_code` | `int`,&nbsp;`null` | レスポンスの HTTP ステータスコード
`response_body` | `string`,&nbsp;`null` | [PII] LLM からのレスポンス
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLERAWLLMREQUESTSHARED #AGENTCONSOLERAWLLMREQUESTSHARED" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`tool_call_id` | `string` | このツールコールのグローバル一意 ID
`duration` | `int` | セッションの持続時間（秒）
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`agent_id` | `string` | CustomerDefinedAgent の BSON ID
`agent_name` | `string` | CustomerDefinedAgent の名前
`is_error` | `boolean` | このリクエストがエラーになったかどうか
`tool_name` | `string` | ツールの名前
`tool_arguments` | `null,`&nbsp;`string` | [PII] ツール引数の JSON
`invocation_source` | `null,`&nbsp;`string` | LLM リクエストを呼び出した Ruby オブジェクト
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLETOOLINVOCATIONSHARED #AGENTCONSOLETOOLINVOCATIONSHARED" }

## ユーザープロファイル属性ビュー {#user-profile-attribute-views}

### USER_CUSTOM_ATTRIBUTES_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_id` | `string` | ワークスペースの BSON ID
`app_id` | `string` | アプリの BSON ID
`user_id` | `string` | [PII] Braze ユーザー ID
`time` | `int` | プロファイル更新の UNIX タイムスタンプ（秒）（バックフィルされた行の場合はバックフィルの時刻）
`time_ms` | `int` | プロファイル更新の UNIX タイムスタンプ（ミリ秒）（バックフィルされた行の場合はバックフィルの時刻）
`update_source` | `string` | プロファイル更新のソース
`sf_updated_at` | `timestamp` | この行が Snowflake で更新された日時
`custom_attributes` | `variant` | [PII] JSON オブジェクトとしてのカスタム属性
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED #USERCUSTOMATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_id` | `string` | ワークスペースの BSON ID
`app_id` | `string` | アプリの BSON ID
`user_id` | `string` | [PII] Braze ユーザー ID
`time` | `int` | プロファイル更新の UNIX タイムスタンプ（秒）（バックフィルされた行の場合はバックフィルの時刻）
`time_ms` | `int` | プロファイル更新の UNIX タイムスタンプ（ミリ秒）（バックフィルされた行の場合はバックフィルの時刻）
`update_source` | `string` | プロファイル更新のソース
`sf_updated_at` | `timestamp` | この行が Snowflake で更新された日時
`external_user_id` | `string` | [PII] ユーザーの external ID
`first_name` | `string` | [PII] 名
`last_name` | `string` | [PII] 姓
`email_address` | `string` | [PII] メールアドレス
`gender` | `string` | [PII] 性別
`phone_number` | `string` | [PII] 電話番号
`dob` | `string` | [PII] 生年月日
`TIME_ZONE` | `string` | [PII] タイムゾーン
`home_city` | `string` | [PII] 居住都市
`country` | `string` | [PII] 国
`language` | `string` | [PII] 言語
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED #USERDEFAULTATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_id` | `string` | ワークスペースの BSON ID
`user_id` | `string` | [PII] Braze ユーザー ID
`app_id` | `string` | アプリの BSON ID
`time` | `int` | プロファイル更新の UNIX タイムスタンプ（秒）（バックフィルされた行の場合はバックフィルの時刻）
`time_ms` | `int` | プロファイル更新の UNIX タイムスタンプ（ミリ秒）（バックフィルされた行の場合はバックフィルの時刻）
`update_source` | `string` | プロファイル更新のソース
`sf_updated_at` | `timestamp` | この行が Snowflake で更新された日時
`external_user_id` | `string` | [PII] ユーザーの external ID
`first_name` | `string` | [PII] 名
`last_name` | `string` | [PII] 姓
`email_address` | `string` | [PII] メールアドレス
`gender` | `string` | [PII] 性別
`phone_number` | `string` | [PII] 電話番号
`dob` | `string` | [PII] 生年月日
`TIME_ZONE` | `string` | [PII] タイムゾーン
`home_city` | `string` | [PII] 居住都市
`country` | `string` | [PII] 国
`language` | `string` | [PII] 言語
`eff_dt` | `timestamp` | この属性状態が有効だった期間の開始日時
`end_dt` | `timestamp` | その期間の終了日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED #USERDEFAULTATTRIBUTESHISTORYVIEWSHARED" }

### USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_id` | `string` | ワークスペースの BSON ID
`app_id` | `string` | アプリの BSON ID
`user_id` | `string` | [PII] Braze ユーザー ID
`time` | `int` | プロファイル更新の UNIX タイムスタンプ（秒）（バックフィルされた行の場合はバックフィルの時刻）
`time_ms` | `int` | プロファイル更新の UNIX タイムスタンプ（ミリ秒）（バックフィルされた行の場合はバックフィルの時刻）
`update_source` | `string` | プロファイル更新のソース
`sf_updated_at` | `timestamp` | この行が Snowflake で更新された日時
`external_user_id` | `string` | [PII] ユーザーの external ID
`first_name` | `string` | [PII] 名
`last_name` | `string` | [PII] 姓
`email_address` | `string` | [PII] メールアドレス
`gender` | `string` | [PII] 性別
`phone_number` | `string` | [PII] 電話番号
`dob` | `string` | [PII] 生年月日
`home_city` | `string` | [PII] 居住都市
`country` | `string` | [PII] 国
`language` | `string` | [PII] 言語
`TIME_ZONE` | `string` | [PII] タイムゾーン
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED #USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

## カタログ {#catalogs}

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`catalog_id` | `string` | カタログの BSON ID
`item_id` | `string` | カタログアイテムの BSON ID
`app_group_id` | `null,`&nbsp;`string` | アプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | アプリグループの API ID
`field_name` | `null,`&nbsp;`string` | フィールドの名前
`field_value` | `null,`&nbsp;`string` | フィールドの値
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CATALOGSITEMSSHARED #CATALOGSITEMSSHARED" }

## 変更ログ {#changelogs}

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`random_bucket_number` | `null, int` | 新しいランダムバケット番号
`global_control_group` | `null, boolean` | この変更により、バケット番号がグローバルコントロールグループに含まれるようになったかどうか
`previous_global_control_group` | `null, boolean` | この変更前にバケット番号がグローバルコントロールグループに含まれていたが、現在は含まれていないかどうか
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSGLOBALCONTROLGROUPSHARED #CHANGELOGSGLOBALCONTROLGROUPSHARED" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% alert note %}
このテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | Campaignの API ID
`name` | `null,`&nbsp;`string` | Campaignの名前
`conversion_behaviors` | `null,`&nbsp;`string` | Campaignのコンバージョン動作
`actions` | `null,`&nbsp;`string` | Campaignのアクション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCAMPAIGNSHARED #CHANGELOGSCAMPAIGNSHARED" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% alert note %}
このテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | Canvasの API ID
`name` | `null,`&nbsp;`string` | Canvasの名前
`conversion_behaviors` | `null,`&nbsp;`string` | Canvasのコンバージョン動作
`variations` | `null,`&nbsp;`string` | Canvasのバリエーション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCANVASSHARED #CHANGELOGSCANVASSHARED" }

## 動作 {#behaviors}

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`name` | `string` | カスタムイベントの名前
`properties` | `string` | JSON エンコードされた文字列として保存されたイベントのカスタムプロパティ
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSCUSTOMEVENTSHARED #USERSBEHAVIORSCUSTOMEVENTSHARED" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | インストールしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | ユーザーがインストールした Unix タイムスタンプ
`source` | `string` | アトリビューションのソース
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSINSTALLATTRIBUTIONSHARED #USERSBEHAVIORSINSTALLATTRIBUTIONSHARED" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | ロケーションを記録したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このロケーションが記録されたアプリの API ID
`time` | `int` | ロケーションが記録された Unix タイムスタンプ
`latitude` | `float` | [PII] 記録されたロケーションの緯度
`longitude` | `float` | [PII] 記録されたロケーションの経度
`altitude` | `null, float` | [PII] 記録されたロケーションの高度
`ll_accuracy` | `null, float` | 記録されたロケーションの緯度・経度の精度
`alt_accuracy` | `null, float` | 記録されたロケーションの高度の精度
`device_id` | `null,`&nbsp;`string` | ロケーションが記録されたデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | ロケーション記録時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLOCATIONSHARED #USERSBEHAVIORSLOCATIONSHARED" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 購入を行ったユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | 購入が発生したアプリの API ID
`time` | `int` | ユーザーが購入を行った Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | 購入が発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | 購入時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`product_id` | `string` | 購入された製品の ID
`price` | `float` | 購入の価格
`currency` | `string` | 購入の通貨
`properties` | `string` | JSON エンコードされた文字列として保存された購入のカスタムプロパティ
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPURCHASESHARED #USERSBEHAVIORSPURCHASESHARED" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アンインストールしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | アンインストールされたアプリの API ID
`time` | `int` | ユーザーがアンインストールした Unix タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUNINSTALLSHARED #USERSBEHAVIORSUNINSTALLSHARED" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アプリをアップグレードしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | ユーザーがアップグレードしたアプリの API ID
`time` | `int` | ユーザーがアプリをアップグレードした Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | ユーザーがアプリをアップグレードしたデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | 使用中の Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`old_app_version` | `null,`&nbsp;`string` | アプリの旧バージョン
`new_app_version` | `null,`&nbsp;`string` | アプリの新バージョン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUPGRADEDAPPSHARED #USERSBEHAVIORSUPGRADEDAPPSHARED" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`time` | `int` | セッションが開始された Unix タイムスタンプ
`session_id` | `string` | セッションの UUID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPFIRSTSESSIONSHARED #USERSBEHAVIORSAPPFIRSTSESSIONSHARED" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED #USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`time` | `int` | セッションが終了した Unix タイムスタンプ
`duration` | `null, float` | セッションの長さ（秒単位）
`session_id` | `string` | セッションの UUID
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONENDSHARED #USERSBEHAVIORSAPPSESSIONENDSHARED" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | セッションが開始された Unix タイムスタンプ
`session_id` | `string` | セッションの UUID
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONSTARTSHARED #USERSBEHAVIORSAPPSESSIONSTARTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類（例: 'enter' または 'exit'）
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCEDATAEVENTSHARED #USERSBEHAVIORSGEOFENCEDATAEVENTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類（例: 'enter' または 'exit'）
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCERECORDEVENTSHARED #USERSBEHAVIORSGEOFENCERECORDEVENTSHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`activity_attributes_type` | `null,`&nbsp;`string` | ライブアクティビティの属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | ライブアクティビティの push-to-start トークン
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APNS ゲートウェイ。iOS プッシュトークンにのみ適用され、1 は開発用、2 は本番用です
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`activity_id` | `null,`&nbsp;`string` | ライブアクティビティの識別子
`update_token` | `null,`&nbsp;`string` | ライブアクティビティの更新トークン
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APNS ゲートウェイ。iOS プッシュトークンにのみ適用され、1 は開発用、2 は本番用です
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`time_ms` | `int` | イベントが発生した時刻（ミリ秒単位）
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`push_token` | `null,`&nbsp;`string` | イベントのプッシュトークン
`push_token_created_at` | `null, int` | プッシュトークンが作成された UNIX タイムスタンプ
`push_token_updated_at` | `null, int` | プッシュトークンが最後に更新された UNIX タイムスタンプ
`push_token_foreground_push_disabled` | `null, boolean` | プッシュトークンのフォアグラウンドプッシュ無効フラグ
`push_token_device_id` | `null,`&nbsp;`string` | プッシュトークンのデバイス ID
`push_token_provisionally_opted_in` | `null, boolean` | プッシュトークンの仮オプトインフラグ
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APNS ゲートウェイ。iOS プッシュトークンにのみ適用され、1 は開発用、2 は本番用です
`web_push_token_public_key` | `null,`&nbsp;`string` | プッシュトークンの公開キー。Web プッシュトークンにのみ適用されます
`web_push_token_user_auth` | `null,`&nbsp;`string` | プッシュトークンのユーザー認証。Web プッシュトークンにのみ適用されます
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | プッシュトークンの VAPID 公開キー。Web プッシュトークンにのみ適用されます
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED #USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`state_change_source` | `null,`&nbsp;`string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`subscription_status` | `string` | サブスクリプションステータス: 'Subscribed'、'Unsubscribed'、または 'Opted In'
`channel` | `null,`&nbsp;`string` | メールなどのグローバルサブスクリプション状態のチャネル
`time` | `int` | サブスクリプション状態が変更された Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | イベントが属するアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するCanvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するCanvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するCanvasバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`send_id` | `null,`&nbsp;`string` | このサブスクリプション状態変更アクションの発生元であるメッセージ送信 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] イベント対象チャネルにおけるユーザーの識別子
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`phone_number` | `null,`&nbsp;`string` | [PII] e164 形式のユーザーの電話番号
`app_api_id` | `null,`&nbsp;`string` | イベントが属するアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するCanvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するCanvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するCanvasバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`channel` | `null,`&nbsp;`string` | チャネル: サブスクリプショングループのチャネルタイプに応じて 'email' または 'sms'
`subscription_status` | `string` | サブスクリプションステータス: 'Subscribed'、'Unsubscribed'、または 'Opted In'
`time` | `int` | サブスクリプション状態が変更された Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`send_id` | `null,`&nbsp;`string` | このサブスクリプション状態変更アクションの発生元であるメッセージ送信 ID
`state_change_source` | `null,`&nbsp;`string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] イベント対象チャネルにおけるユーザーの識別子
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED" }

## Campaigns

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するCampaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`conversion_behavior_index` | `null, int` | コンバージョン動作のインデックス
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSCONVERSIONSHARED #USERSCAMPAIGNSCONVERSIONSHARED" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するCampaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSENROLLINCONTROLSHARED #USERSCAMPAIGNSENROLLINCONTROLSHARED" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するCampaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`channel` | `null,`&nbsp;`string` | このイベントが属するチャネル
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSFREQUENCYCAPSHARED #USERSCAMPAIGNSFREQUENCYCAPSHARED" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するCampaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するCampaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`revenue` | `long` | 生成された USD 収益額（セント単位）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSREVENUESHARED #USERSCAMPAIGNSREVENUESHARED" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID        |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `progression_type`                     | `string`,&nbsp;`null`    | ステップ進行イベントのタイプ |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Canvasの最初のステップへのエントリーかどうか        |
| `exit_reason`                          | `string`,&nbsp;`null`    | 離脱の場合、ユーザーがそのステップ中にCanvasを離脱した理由                  |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Canvas内のこのユーザーインスタンスの一意な識別子  |
| `next_step_id`                         | `string`,&nbsp;`null`    | Canvas内の次のステップの BSON ID |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | Canvas内の次のステップの API ID |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASSTEPPROGRESSIONSHARED #USERSCANVASSTEPPROGRESSIONSHARED" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| フィールド                                  | タイプ                     | 説明                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `app_api_id`                           | `string`,&nbsp;`null`    | このイベントが発生したアプリの API ID                                                                  |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                                                                      |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID                                                  |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | ユーザーが実行したコンバージョンイベントのタイプ。「0」は1次コンバージョン、「1」は2次コンバージョンを表します |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                                                                        |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                                                                       |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                                                            |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                                                                      |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCONVERSIONSHARED #USERSCANVASCONVERSIONSHARED" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `device_id`               | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [非推奨] このイベントが属するキャンバスステップの API ID         |
| `gender`                  | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                             |
| `country`                 | `string`,&nbsp;`null`    | [PII] ユーザーの国                                            |
| `timezone`                | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                 |
| `language`                | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                           |
| `in_control_group`        | `boolean`,&nbsp;`null`   | ユーザーがコントロールグループに登録されたかどうか                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASENTRYSHARED #USERSCANVASENTRYSHARED" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED #USERSCANVASEXITMATCHEDAUDIENCESHARED" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITPERFORMEDEVENTSHARED #USERSCANVASEXITPERFORMEDEVENTSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| フィールド                       | タイプ                     | 説明                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                                                               |
| `user_id`                   | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                                                                   |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                                                              |
| `app_group_id`              | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                                                                   |
| `time`                      | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | このイベントが発生したアプリの API ID                                                                  |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID                                                     |
| `canvas_api_id`             | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                                                            |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                                                                 |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | このイベントが属する実験ステップの API ID                                                             |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | ユーザーが実行したコンバージョンイベントのタイプ。「0」は1次コンバージョン、「1」は2次コンバージョンを表します |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                                                   |
| `experiment_split_api_id` | `string`,&nbsp;`null` | ユーザーが登録された実験スプリットの API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED #USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| フィールド                     | タイプ                     | 説明                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                    |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | このイベントが属する実験ステップの API ID                  |
| `in_control_group`        | `boolean`,&nbsp;`null`   | ユーザーがコントロールグループに登録されたかどうか                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

| `experiment_split_api_id` | `string`,&nbsp;`null` | ユーザーが登録された実験スプリットの API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED #USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                    |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID       |
| `channel`                              | `string`,&nbsp;`null`    | このイベントが属するメッセージングチャネル（メール、プッシュなど）          |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASFREQUENCYCAPSHARED #USERSCANVASFREQUENCYCAPSHARED" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| フィールド                                  | タイプ                     | 説明                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                    |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスの ID |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                         |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze 内部使用のみ) このイベントが属するCanvasの ID          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するCanvasの API ID                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するCanvasバリエーションの API ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップの API ID                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID       |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                            |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                           |
| `revenue`                              | `int`,&nbsp;`null`       | 生成された収益額（USD、セント単位で表示）               |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                        |
| `app_api_id` | `string`,&nbsp;`null` | このイベントが発生したアプリの API ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASREVENUESHARED #USERSCANVASREVENUESHARED" }

## メッセージ {#messages}


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー - user_agent から抽出 - 開封が発生したブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナー配置 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERABORTSHARED #USERSMESSAGESBANNERABORTSHARED" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー - user_agent から抽出 - 開封が発生したブラウザー
`button_id` | `null,`&nbsp;`string` | クリックされたボタンの ID（このクリックがボタンのクリックを表す場合）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナー配置 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERCLICKSHARED #USERSMESSAGESBANNERCLICKSHARED" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー - user_agent から抽出 - 開封が発生したブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナー配置 ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERIMPRESSIONSHARED #USERSMESSAGESBANNERIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDABORTSHARED #USERSMESSAGESCONTENTCARDABORTSHARED" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを生成したカードの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDCLICKSHARED #USERSMESSAGESCONTENTCARDCLICKSHARED" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを生成したカードの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDDISMISSSHARED #USERSMESSAGESCONTENTCARDDISMISSSHARED" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`content_card_id` | `string` | このイベントを生成したカードの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDIMPRESSIONSHARED #USERSMESSAGESCONTENTCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`content_card_id` | `string` | このイベントを生成したカードの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDSENDSHARED #USERSMESSAGESCONTENTCARDSENDSHARED" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILABORTSHARED #USERSMESSAGESEMAILABORTSHARED" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`bounce_reason` | `null,`&nbsp;`string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザーフレンドリーなメッセージ
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_drop` | `null, boolean` | このイベントがドロップイベントとしてカウントされるかどうかを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILBOUNCESHARED #USERSMESSAGESEMAILBOUNCESHARED" }

{% alert note %}
1回のハードバウンスに対して、同じユーザーの複数の行が表示される場合があります。これは、イベントが非同期に処理された場合や、関連する送信の `dispatch_id` 値が異なる場合に発生することがあります。重複排除やエクスポートの分析を行う際は、`dispatch_id`、`time`、`id` を組み合わせて検討してください。
{% endalert %}

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`user_agent` | `null,`&nbsp;`string` | クリックが発生したユーザーエージェント
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`link_id` | `null,`&nbsp;`string` | Braze が作成した、クリックされたリンクの一意の ID
`link_alias` | `null,`&nbsp;`string` | このリンク ID に関連付けられたエイリアス
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_amp` | `null, boolean` | これが AMP イベントであるかどうかを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`suspected_bot_click_reason` | `null, object` | このイベントがボットとして分類された理由
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILCLICKSHARED #USERSMESSAGESEMAILCLICKSHARED" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`recipient_domain` | `null,`&nbsp;`string` | 受信者のメールドメイン
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（Sparkpost、Sendgrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`deferral_reason` | `null,`&nbsp;`string` | [PII] この遅延イベントで受信した SMTP 理由コードとユーザーフレンドリーなメッセージ
`attempt_count` | `null, int` | メッセージの送信試行回数
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDEFERRALSHARED #USERSMESSAGESEMAILDEFERRALSHARED" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDELIVERYSHARED #USERSMESSAGESEMAILDELIVERYSHARED" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,`&nbsp;`string` | スパム報告が発生したユーザーエージェント
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILMARKASSPAMSHARED #USERSMESSAGESEMAILMARKASSPAMSHARED" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,`&nbsp;`string` | 開封が発生したユーザーエージェント
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`machine_open` | `null,`&nbsp;`string` | ユーザーの操作なしに開封イベントがトリガーされた場合（例: メールプライバシー保護が有効な Apple デバイスなど）に 'true' が設定されます。値はより詳細な情報を提供するために変更される場合があります。
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_amp` | `null, boolean` | これが AMP イベントであるかどうかを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILOPENSHARED #USERSMESSAGESEMAILOPENSHARED" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSENDSHARED #USERSMESSAGESEMAILSENDSHARED" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`bounce_reason` | `null,`&nbsp;`string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザーフレンドリーなメッセージ
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSOFTBOUNCESHARED #USERSMESSAGESEMAILSOFTBOUNCESHARED" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILUNSUBSCRIBESHARED #USERSMESSAGESEMAILUNSUBSCRIBESHARED" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライウィンドウ内で後から再試行された場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILRETRYSHARED #USERSMESSAGESEMAILRETRYSHARED" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`feature_flag_id_name` | `null,`&nbsp;`string` | フィーチャーフラグのロールアウト識別子
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー - user_agent から抽出 - 開封が発生したブラウザー
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED #USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEABORTSHARED #USERSMESSAGESINAPPMESSAGEABORTSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`button_id` | `null,`&nbsp;`string` | クリックされたボタンの ID（このクリックがボタンのクリックを表す場合）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGECLICKSHARED #USERSMESSAGESINAPPMESSAGECLICKSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`locale_key` | `null,`&nbsp;`string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例: 'en-us'）（デフォルトの場合は null）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED #USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEABORTSHARED #USERSMESSAGESLINEABORTSHARED" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`short_url` | `null,`&nbsp;`string` | クリックされた短縮 URL
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`user_agent` | `null,`&nbsp;`string` | スパム報告が発生したユーザーエージェント
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINECLICKSHARED #USERSMESSAGESLINECLICKSHARED" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`media_id` | `null,`&nbsp;`string` | LINE から受信メディアを取得するために使用できる LINE 生成 ID
`message_body` | `null,`&nbsp;`string` | ユーザーからの入力応答
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEINBOUNDRECEIVESHARED #USERSMESSAGESLINEINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINESENDSHARED #USERSMESSAGESLINESENDSHARED" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライウィンドウ内で後から再試行された場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル ID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先の LINE チャネル名
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元のユーザーの LINE ID
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの API ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINERETRYSHARED #USERSMESSAGESLINERETRYSHARED" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`activity_id` | `null,`&nbsp;`string` | ライブアクティビティの識別子
`activity_attributes_type` | `null,`&nbsp;`string` | ライブアクティビティの属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | ライブアクティビティの push to start トークン
`update_token` | `null,`&nbsp;`string` | ライブアクティビティの更新トークン
`live_activity_event_type` | `null,`&nbsp;`string` | ライブアクティビティのイベントタイプ。['start', 'update', 'end'] のいずれか
`live_activity_event_outcome` | `null,`&nbsp;`string` | ライブアクティビティイベントの結果
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYOUTCOMESHARED #USERSMESSAGESLIVEACTIVITYOUTCOMESHARED" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`activity_id` | `null,`&nbsp;`string` | ライブアクティビティの識別子
`activity_attributes_type` | `null,`&nbsp;`string` | ライブアクティビティの属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | ライブアクティビティの push to start トークン
`update_token` | `null,`&nbsp;`string` | ライブアクティビティの更新トークン
`live_activity_event_type` | `null,`&nbsp;`string` | ライブアクティビティのイベントタイプ。['start', 'update', 'end'] のいずれか
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYSENDSHARED #USERSMESSAGESLIVEACTIVITYSENDSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー - user_agent から抽出 - 開封が発生したブラウザー
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDABORTSHARED #USERSMESSAGESNEWSFEEDCARDABORTSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー - user_agent から抽出 - 開封が発生したブラウザー
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDCLICKSHARED #USERSMESSAGESNEWSFEEDCARDCLICKSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`card_api_id` | `null,`&nbsp;`string` | カードの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー - user_agent から抽出 - 開封が発生したブラウザー
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED #USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | 配信を試みた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONABORTSHARED #USERSMESSAGESPUSHNOTIFICATIONABORTSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`push_token` | `null,`&nbsp;`string` | バウンスしたプッシュトークン
`device_id` | `null,`&nbsp;`string` | 配信を試みてバウンスした `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED #USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
このイベントは [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) ではサポートされておらず、[Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) では非推奨です。
{% endalert %}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED #USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`button_string` | `null,`&nbsp;`string` | クリックされたプッシュ通知ボタンの識別子（button_string）。ボタンクリックでない場合は null
`button_action_type` | `null,`&nbsp;`string` | プッシュ通知ボタンのアクションタイプ。[URI, DEEP_LINK, NONE, CLOSE] のいずれか。ボタンクリックでない場合は null
`slide_id` | `null,`&nbsp;`string` | ユーザーがクリックしたプッシュカルーセルスライドのスライド識別子
`slide_action_type` | `null,`&nbsp;`string` | プッシュカルーセルスライドのアクションタイプ
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`push_token` | `null,`&nbsp;`string` | 配信を試みたプッシュトークン
`device_id` | `null,`&nbsp;`string` | 配信を試みた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`is_sampled` | `null,`&nbsp;`string` | プッシュ送信がサンプリングされ、配信イベントが期待されたかどうかを示します
`locale_key` | `null,`&nbsp;`string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例: 'en-us'）（デフォルトの場合は null）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONSENDSHARED #USERSMESSAGESPUSHNOTIFICATIONSENDSHARED" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大128文字）
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSABORTSHARED #USERSMESSAGESRCSABORTSHARED" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`short_url` | `null,`&nbsp;`string` | クリックされた短縮 URL
`suspected_bot_click_reason` | `null,`&nbsp;`string` | このイベントがボットとして分類された理由
`user_agent` | `null,`&nbsp;`string` | スパム報告が発生したユーザーエージェント
`user_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信したユーザーの電話番号
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`interaction_type` | `null,`&nbsp;`string` | クリックを生成したインタラクションのタイプ。文字列値の例: Text URL、Reply、OpenURL
`element_label` | `null,`&nbsp;`string` | クリックされた要素に関するオプションの詳細（候補返信やボタンのテキストなど）
`element_type` | `null,`&nbsp;`string` | 候補とボタンに共通する interaction_type が候補から来たのかボタンから来たのかを指定します。例: Suggestion、Button
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSCLICKSHARED #USERSMESSAGESRCSCLICKSHARED" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例: +14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSDELIVERYSHARED #USERSMESSAGESRCSDELIVERYSHARED" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`action` | `null,`&nbsp;`string` | このメッセージに対して実行されたアクション（例: Subscribed、Unsubscribed、または None）
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`media_urls` | `null,`&nbsp;`string` | ユーザーからのメディア URL
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`user_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信したユーザーの電話番号
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`message_body` | `null,`&nbsp;`string` | ユーザーからの入力応答
`to_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信先の受信 RCS 送信者
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSINBOUNDRECEIVESHARED #USERSMESSAGESRCSINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例: +14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREADSHARED #USERSMESSAGESRCSREADSHARED" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`error` | `null,`&nbsp;`string` | エラー名
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`provider_error_code` | `null,`&nbsp;`string` | プロバイダーからのエラーコード
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例: +14155552671）
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREJECTIONSHARED #USERSMESSAGESRCSREJECTIONSHARED" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`category` | `null,`&nbsp;`string` | キーワードカテゴリ名。自動返信メッセージの場合のみ設定されます: 'opt-in'、'opt-out'、'help'、またはカスタム値
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`message_extras` | `null,`&nbsp;`string` | Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | サブスクリプショングループの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164 形式、例: +14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSSENDSHARED #USERSMESSAGESRCSSENDSHARED" }

## SMS メッセージイベントと削除されたユーザープロファイル {#sms-message-events-and-deleted-user-profiles}

{% alert note %}
`USERS_MESSAGES_SMS_*` 共有テーブル（[`USERS_MESSAGES_SMS_REJECTION_SHARED`](#USERS_MESSAGES_SMS_REJECTION_SHARED)、[`USERS_MESSAGES_SMS_DELIVERY_SHARED`](#USERS_MESSAGES_SMS_DELIVERY_SHARED)、[`USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED`](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) を含む）について、Braze はイベントが Snowflake データ共有および Currents 向けに処理される時点でワークスペースに Braze ユーザープロファイルがまだ存在する場合にのみ行を書き込みます。処理が完了する前にそのユーザーが削除された場合、ダッシュボードの SMS ワークスペース指標が Braze のレポートパスからの集計カウントを引き続き反映していても、そのイベントは Snowflake や Currents エクスポートには表示されません。対応する Currents の動作については、同じ用語集の [SMS Rejection イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) および関連する SMS イベントタイプを参照してください。
{% endalert %}

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大 2,000 文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSABORTSHARED #USERSMESSAGESSMSABORTSHARED" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSCARRIERSENDSHARED #USERSMESSAGESSMSCARRIERSENDSHARED" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYSHARED #USERSMESSAGESSMSDELIVERYSHARED" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`error` | `null,`&nbsp;`string` | エラー名
`provider_error_code` | `null,`&nbsp;`string` | SMS サービスプロバイダーからのエラーコード
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYFAILURESHARED #USERSMESSAGESSMSDELIVERYFAILURESHARED" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,`&nbsp;`string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | 受信電話番号に関連付けられたワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`user_phone_number` | `string` | [PII] メッセージの受信元であるユーザーの電話番号
`subscription_group_id` | `null,`&nbsp;`string` | この SMS メッセージの対象となるサブスクリプショングループの ID
`subscription_group_api_id` | `null,`&nbsp;`string` | この SMS メッセージの対象となるサブスクリプショングループの API ID
`inbound_phone_number` | `string` | メッセージの送信先である受信番号
`action` | `string` | このメッセージに対して実行されたアクション。例: `Subscribed`、`Unsubscribed`、`None`
`message_body` | `string` | ユーザーからの応答
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディア URL
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップメッセージバリエーションの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSINBOUNDRECEIVESHARED #USERSMESSAGESSMSINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`error` | `null,`&nbsp;`string` | エラー名
`provider_error_code` | `null,`&nbsp;`string` | SMS サービスプロバイダーからのエラーコード
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントとリンク/ペアになっています
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSREJECTIONSHARED #USERSMESSAGESSMSREJECTIONSHARED" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループの外部 ID
`category` | `null,`&nbsp;`string` | キーワードカテゴリ名。自動応答メッセージの場合のみ設定されます: 'Opt-in'、'Opt-out'、'Help'、またはカスタム値
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSENDSHARED #USERSMESSAGESSMSSENDSHARED" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `null,`&nbsp;`string` | short_url の対象ユーザーの Braze ID。short_url がユーザークリックトラッキングを使用していない場合は null
`external_user_id` | `null,`&nbsp;`string` | [PII] short_url の対象ユーザーの外部 ID（存在する場合）。short_url がユーザークリックトラッキングを使用していない場合は null
`app_group_api_id` | `null,`&nbsp;`string` | short_url の生成に使用されたワークスペースの API ID
`time` | `int` | short_url がクリックされた Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`campaign_id` | `null,`&nbsp;`string` | short_url が生成された Campaignの Braze ID。Campaign からでない場合は null
`campaign_api_id` | `null,`&nbsp;`string` | short_url が生成された Campaignの API ID。Campaign からでない場合は null
`message_variation_api_id` | `null,`&nbsp;`string` | short_url が生成されたメッセージバリエーションの API ID。Campaign からでない場合は null
`canvas_id` | `null,`&nbsp;`string` | short_url が生成された Canvasの Braze ID。Canvas からでない場合は null
`canvas_api_id` | `null,`&nbsp;`string` | short_url が生成された Canvasの API ID。Canvas からでない場合は null
`canvas_variation_api_id` | `null,`&nbsp;`string` | short_url が生成された Canvas バリエーションの API ID。Canvas からでない場合は null
`canvas_step_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスステップの API ID。Canvas からでない場合は null
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスステップメッセージバリエーションの API ID。Canvas からでない場合は null
`url` | `string` | short_url によってリダイレクトされるメッセージ内の元の URL
`short_url` | `string` | クリックされた短縮 URL
`user_agent` | `null,`&nbsp;`string` | short_url をリクエストしたユーザーエージェント
`user_phone_number` | `string` | [PII] ユーザーの電話番号
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`suspected_bot_click_reason` | `null, object` | このイベントがボットとして分類された理由
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSHORTLINKCLICKSHARED #USERSMESSAGESSMSSHORTLINKCLICKSHARED" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライウィンドウ内で後からリトライされた場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループ API ID
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSRETRYSHARED #USERSMESSAGESSMSRETRYSHARED" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大 2,000 文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKABORTSHARED #USERSMESSAGESWEBHOOKABORTSHARED" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`http_status_code` | `null, int` | レスポンスの HTTP ステータスコード
`endpoint_url` | `null,`&nbsp;`string` | リクエスト先のエンドポイント URL
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`content_length` | `null, int` | レスポンスのコンテンツ長
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`host` | `null,`&nbsp;`string` | リクエストのホスト
`id` | `string` | このイベントのグローバルな一意の ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`raw_response` | `null,`&nbsp;`string` | エンドポイントからの切り詰められた生レスポンス
`retry_count` | `null, int` | 試行されたリトライ回数
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`url_path` | `null,`&nbsp;`string` | リクエスト先 URL のパス
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`webhook_duration` | `null, int` | このリクエストの合計所要時間（ミリ秒）
`webhook_failure_source` | `null,`&nbsp;`string` | エラーが Braze によって生成されたか、エンドポイント自体によって生成されたかを示します。source フィールドの値は External Endpoint、Treat no status code to host unreachable のいずれかです
`is_terminal` | `null, boolean` | このイベントが送信における最終試行であったかどうか
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKFAILURESHARED #USERSMESSAGESWEBHOOKFAILURESHARED" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_name` | `null,`&nbsp;`string` | Campaignの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`canvas_name` | `null,`&nbsp;`string` | Canvasの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信した Canvas バリエーションの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKSENDSHARED #USERSMESSAGESWEBHOOKSENDSHARED" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライウィンドウ内で後からリトライされた場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKRETRYSHARED #USERSMESSAGESWEBHOOKRETRYSHARED" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大 2,000 文字）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPABORTSHARED #USERSMESSAGESWHATSAPPABORTSHARED" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`short_url` | `null,`&nbsp;`string` | クリックされた短縮 URL
`user_agent` | `null,`&nbsp;`string` | スパムレポートが発生したユーザーエージェント
`user_phone_number` | `null,`&nbsp;`string` | [PII] メッセージの受信元であるユーザーの電話番号
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPCLICKSHARED #USERSMESSAGESWHATSAPPCLICKSHARED" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | Meta がこのメッセージに対して生成した一意の ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPDELIVERYSHARED #USERSMESSAGESWHATSAPPDELIVERYSHARED" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`provider_error_code` | `null,`&nbsp;`string` | WhatsApp からのエラーコード
`provider_error_title` | `null, `&nbsp;`string` | WhatsApp からのエラータイトル
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`message_id` | `null,`&nbsp;`string` | Meta がこのメッセージに対して生成した一意の ID
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPFAILURESHARED #USERSMESSAGESWHATSAPPFAILURESHARED" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`user_phone_number` | `string` | [PII] メッセージの受信元であるユーザーの電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`inbound_phone_number` | `string` | メッセージの送信先である受信番号
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`message_body` | `string` | ユーザーからの応答
`quick_reply_text` | `string` | ユーザーが押したボタンのテキスト
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディア URL
`action` | `string` | このメッセージに対して実行されたアクション。例: `Subscribed`、`Unsubscribed`、`None`
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`catalog_id` | `null,`&nbsp;`string` | 受信メッセージで製品が参照されている場合の製品のカタログ ID。それ以外の場合は空
`product_id` | `null,`&nbsp;`string` | 購入された製品の ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
`flow_response_json` | `null,`&nbsp;`string` | [PII] ユーザーが応答したフォームの値。ユーザーが WhatsApp フローに応答している場合に存在します。
`message_id` | `null,`&nbsp;`string` | Meta がこのメッセージに対して生成した一意の ID
`in_reply_to` | `null,`&nbsp;`string` | このメッセージが返信したメッセージの message_id
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED #USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | Meta がこのメッセージに対して生成した一意の ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPREADSHARED #USERSMESSAGESWHATSAPPREADSHARED" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string`	| [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づく `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | サブスクリプショングループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | Meta がこのメッセージに対して生成した一意の ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPSENDSHARED #USERSMESSAGESWHATSAPPSENDSHARED" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% alert note %}
このテーブルは Snowflake データ共有でのみ利用可能です。
{% endalert %}

このイベントは、メッセージの優先度が下げられたりフリークエンシーキャップが適用されたりして、設定されたリトライウィンドウ内で後からリトライされた場合に発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] e.164 形式でメッセージを受信するユーザーの電話番号
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`subscription_group_api_id` | `null,`&nbsp;`string` | サブスクリプショングループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属する Campaignの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvasの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属する Canvas バリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を記述するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPRETRYSHARED #USERSMESSAGESWHATSAPPRETRYSHARED" }

## ユーザー {#users}

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| フィールド                  | タイプ                   | 説明                                               |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                |
| `app_group_id`              | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの Braze ID      |
| `app_group_api_id`          | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの API ID        |
| `user_id`                   | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID          |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                       |
| `time`                      | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ             |
| `random_bucket_number`      | `int`,&nbsp;`null`       | ユーザーに割り当てられた現在のランダムバケット番号 |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | ユーザーに割り当てられた以前のランダムバケット番号 |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSRANDOMBUCKETNUMBERUPDATESHARED #USERSRANDOMBUCKETNUMBERUPDATESHARED" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| フィールド         | タイプ                   | 説明                                                          |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                            |
| `user_id`          | `string`,&nbsp;`null`    | 削除されたユーザーの Braze ID                                  |
| `app_group_id`     | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの Braze ID                  |
| `app_group_api_id` | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの API ID                    |
| `time`             | `int`,&nbsp;`null`       | ユーザー削除リクエストが処理された Unix タイムスタンプ         |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERDELETEREQUESTSHARED #USERSUSERDELETEREQUESTSHARED" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| フィールド         | タイプ                   | 説明                                                                          |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                            |
| `user_id`          | `string`,&nbsp;`null`    | 孤立したユーザーの Braze ID                                                    |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] ユーザーの external ID                                                  |
| `device_id`        | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づくデバイスの ID                        |
| `app_group_id`     | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの Braze ID                                  |
| `app_group_api_id` | `string`,&nbsp;`null`    | このユーザーが属するワークスペースの API ID                                    |
| `app_api_id`       | `string`,&nbsp;`null`    | 孤立したユーザーが属していたアプリの API ID                                    |
| `time`             | `int`,&nbsp;`null`       | ユーザーが孤立した Unix タイムスタンプ                                         |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | 孤立したユーザーのプロファイルとマージされたユーザーの Braze ID                 |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERORPHANSHARED #USERSUSERORPHANSHARED" }

## スナップショット {#snapshots}

{% alert note %}
スナップショットテーブルは Snowflake データ共有でのみ利用できます。
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意な ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | アプリの API ID
`name` | `null,`&nbsp;`string` | アプリの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSAPPSHARED #SNAPSHOTSAPPSHARED" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意な ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | Campaignメッセージバリエーションの API ID
`name` | `null,`&nbsp;`string` | Campaignメッセージバリエーションの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED #SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意な ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`type` | `null,`&nbsp;`string` | キャンバスフローステップのタイプ
`api_step_id` | `string` | キャンバスステップの API ID
`experiment_splits` | `null,`&nbsp;`string` | ステップの実験分割
`conversion_behaviors` | `null,`&nbsp;`string` | ステップのコンバージョン動作
`name` | `null,`&nbsp;`string` | キャンバスフローステップの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASFLOWSTEPSHARED #SNAPSHOTSCANVASFLOWSTEPSHARED" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意な ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | キャンバスステップの API ID
`name` | `null,`&nbsp;`string` | キャンバスステップの名前
`actions` | `null,`&nbsp;`string` | キャンバスステップのアクション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASSTEPSHARED #SNAPSHOTSCANVASSTEPSHARED" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意な ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`api_id` | `string` | キャンバスバリエーションの API ID
`name` | `null,`&nbsp;`string` | キャンバスバリエーションの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASVARIATIONSHARED #SNAPSHOTSCANVASVARIATIONSHARED" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意な ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループの BSON ID
`type` | `null,`&nbsp;`string` | 実験ステップのタイプ
`api_step_id` | `string` | 実験ステップの API ID
`experiment_splits` | `null,`&nbsp;`string` | ステップの実験分割
`conversion_behaviors` | `null,`&nbsp;`string` | ステップのコンバージョン動作
`name` | `null,`&nbsp;`string` | 実験ステップの名前
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSEXPERIMENTSTEPSHARED #SNAPSHOTSEXPERIMENTSTEPSHARED" }

## 中止タイプ {#abort-types}

{% include currents/abort_types_reference.md combined_content_rendering=true %}