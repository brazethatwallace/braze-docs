---
nav_title: "SQL テーブルリファレンス"
article_title: "SQL テーブルリファレンス"
page_order: 3
page_type: reference
toc_headers: h2
description: "このページは、クエリビルダー、SQL セグメントエクステンション、Snowflake データ共有で使用される Snowflake SQL テーブルとカラムのリファレンスです。"
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL テーブルリファレンス {#sql-table-reference}

このページは、以下の Braze ツールで利用可能な Snowflake SQL テーブルとカラムのリファレンスです。

- [クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [SQL セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Snowflake データ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

ほとんどのテーブルは3つのツールすべてで利用可能です。**Snowflake データ共有のみ**と記載されたテーブルは Snowflake データ共有専用であり、クエリビルダーや SQL セグメントエクステンションではアクセスできません。

{% alert tip %}
これらの SQL テーブルは、[Currents イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)に記載されているイベントに対応しています。たとえば、SQL テーブル `USERS_MESSAGES_EMAIL_SEND_SHARED` は Currents イベント `users.messages.email.Send` に対応しています。JSON イベントスキーマやパートナー固有のフォーマット（Amplitude、Mixpanel、セグメント）が必要な場合は、Currents 用語集を参照してください。
{% endalert %}

## 目次 {#table-of-contents}

テーブル | 説明
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | エージェントコンソールのエージェントが実行されたとき（**Snowflake Data Sharing のみ**）
[AGENTCONSOLE_RAWLLMREQUEST_SHARED](#AGENTCONSOLE_RAWLLMREQUEST_SHARED) | 各 LLM 呼び出しの生情報（**Snowflake Data Sharing のみ**）
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | ツールが実行されたとき（**Snowflake Data Sharing のみ**）
[USER_CUSTOM_ATTRIBUTES_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED) | ユーザーごとのカスタムプロファイル属性の定期スナップショット
[USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED) | 有効日付範囲付きのデフォルトプロファイル属性の履歴
[USER_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED) | ユーザーごとのデフォルトプロファイル属性の定期スナップショット
[USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED) | ユーザーごとのほぼリアルタイムのデフォルトプロファイル属性
[USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED) | 有効日付範囲付きのカスタムプロファイル属性の履歴（**Snowflake Data Sharing のみ**）
[USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED](#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED) | ユーザーごとのほぼリアルタイムのカスタムプロファイル属性（**Snowflake Data Sharing のみ**）
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | 削除されていないカタログアイテム
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | キャンペーンが変更されたとき（**Snowflake Data Sharing のみ**）
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | キャンバスが変更されたとき（**Snowflake Data Sharing のみ**）
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | グローバルコントロールグループが変更されたとき
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | ユーザーがカスタムイベントを実行したとき
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | ユーザーがアプリをインストールし、パートナーにアトリビューションされたとき
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | ユーザーが位置情報を記録したとき
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | ユーザーが購入を行ったとき
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | ユーザーがアプリをアンインストールしたとき
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | ユーザーがアプリをアップグレードしたとき
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | ユーザーが初めてのセッションを行ったとき
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | ユーザーが News Feed を閲覧したとき
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | ユーザーがアプリでセッションを終了したとき
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | ユーザーがアプリでセッションを開始したとき
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | ユーザーがジオフェンスエリアをトリガーしたとき。たとえばジオフェンスに入場または退場した場合です。このイベントは他のイベントとバッチ処理され、標準イベントエンドポイント経由で受信されるため、リアルタイムに表示されない場合があります。<br><br>このテーブルにジオフェンスアクティビティを記録するには、各ジオフェンスの詳細設定で **Enable Analytics for Enter** と **Enable Analytics for Exit** を選択してください。詳細は [ジオフェンスの手動作成]({{site.baseurl}}/user_guide/audience/locations_and_geofences/creating_geofences#manually-create-geofences)のステップ 3 を参照してください。
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | ユーザーがジオフェンスエリアをトリガーしたとき（たとえばジオフェンスに入場または退場した場合）。このイベントは専用のジオフェンスエンドポイント経由で受信されるため、ユーザーのデバイスがジオフェンスのトリガーを検出するとリアルタイムで受信されます。<br><br>また、ジオフェンスエンドポイントのレート制限により、一部のジオフェンスイベントが RecordEvent として反映されない場合があります。ただし、すべてのジオフェンスイベントは DataEvent として表現されます（バッチ処理による遅延が発生する場合があります）。
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | ライブアクティビティの push-to-start トークンが変更されたとき
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | ライブアクティビティの更新トークンが変更されたとき
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | プッシュ通知のトークン状態が変更されたとき
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | ユーザーがメールなどのチャネルに対してグローバルに購読または購読解除されたとき
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | ユーザーが購読グループに購読または購読解除されたとき
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | ユーザーがキャンペーンでコンバージョンしたとき
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | ユーザーがキャンペーンのコントロールグループに登録されたとき
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | ユーザーがキャンペーンのフリークエンシーキャップに達したとき
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | ユーザーが1次コンバージョン期間内に収益を生成したとき
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | ユーザーがキャンバスステップに進んだとき
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | ユーザーがキャンバスのコンバージョンイベントでコンバージョンしたとき
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | ユーザーがキャンバスにエントリしたとき
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | ユーザーがオーディエンス離脱条件に一致してキャンバスを離脱したとき
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | ユーザーが例外イベントを実行してキャンバスを離脱したとき
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | ユーザーがキャンバスの実験ステップでコンバージョンしたとき
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | ユーザーが実験ステップのパスにエントリしたとき
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | ユーザーがキャンバスステップのフリークエンシーキャップに達したとき
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | ユーザーが1次コンバージョンイベント期間内に収益を生成したとき
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | 元々スケジュールされたバナーメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | ユーザーがバナーをクリックしたとき
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | ユーザーがバナーを閲覧したとき
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | 元々スケジュールされた Content Cards メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | ユーザーが Content Cardsをクリックしたとき
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | ユーザーが Content Cardsを閉じたとき
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | ユーザーが Content Cardsを閲覧したとき
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | ユーザーに Content Cardsを送信したとき
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | 元々スケジュールされたメールメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | メールサービスプロバイダー (ESP) がハードバウンスを返したとき。ハードバウンスは恒久的な配信失敗を示します。
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | ユーザーがメール内のリンクをクリックしたとき
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | メールが延期されたとき
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | メールが配信されたとき
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | メールがスパムとしてマークされたとき
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | ユーザーがメールを開封したとき
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | ユーザーにメールを送信したとき
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | メールがソフトバウンスしたとき
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | ユーザーがメールを購読解除したとき
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | 優先度が下げられた、またはフリークエンシーキャップに達した後にメールメッセージが再試行されたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | ユーザーがフィーチャーフラグを閲覧したとき
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | 元々スケジュールされたアプリ内メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | ユーザーがアプリ内メッセージをクリックしたとき
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | ユーザーがアプリ内メッセージを閲覧したとき
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | LINE への送信前に、スケジュールされた LINE メッセージが配信できなかったとき
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | ユーザーが LINE メッセージ内のリンクをクリックしたとき
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | ユーザーから LINE メッセージを受信したとき
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | LINE メッセージが LINE に送信されたとき
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | 優先度が下げられた、またはフリークエンシーキャップに達した後に LINE メッセージが再試行されたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | ライブアクティビティでアウトカムイベントが発生したとき
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | ライブアクティビティメッセージが送信されたとき
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | 元々スケジュールされた News Feed カードメッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | ユーザーが News Feed カードをクリックしたとき
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | ユーザーが News Feed カードを閲覧したとき
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | 元々スケジュールされたプッシュ通知メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | プッシュ通知がバウンスしたとき
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | ユーザーが通知を受信した後、通知をクリックせずにアプリを開いたとき
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | アプリが開いている状態でユーザーがプッシュ通知を受信したとき。<br><br>このイベントは [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) ではサポートされておらず、[Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) では非推奨です。
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | ユーザーがプッシュ通知を開いた、またはプッシュ通知ボタン（アプリを開かない「閉じる」ボタンを含む）をクリックしたとき。<br><br>プッシュボタンアクションには複数の結果があります。No、Decline、Cancel のアクションは「クリック」であり、Accept のアクションは「開封」です。どちらもこのテーブルに記録されますが、**BUTTON_ACTION_TYPE** 列で区別できます。たとえば、`BUTTON_ACTION_TYPE` が No、Decline、Cancel ではないものでグループ化するクエリを使用できます。
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | ユーザーにプッシュ通知を送信したとき
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Braze 内で検出されたエラーにより RCS 送信が中断され、メッセージが破棄されたとき
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | エンドユーザーが RCS メッセージの UI 要素をタップまたはクリックして操作したとき
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | RCS メッセージがエンドユーザーのモバイルデバイスに正常に配信されたとき
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Braze がエンドユーザーからの RCS メッセージを受信したとき
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | エンドユーザーがデバイスで RCS メッセージを開いたとき
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | キャリアの介入により RCS メッセージの配信に失敗したとき
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | RCS メッセージが Braze のシステムからラストマイル配信パートナーに送信されたとき
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | 元々スケジュールされた SMS メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | SMS メッセージがキャリアに送信されたとき
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | SMS メッセージが配信されたとき
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Braze が SMS サービスプロバイダーへの SMS メッセージの配信に失敗したとき
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | ユーザーから SMS メッセージを受信したとき
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | SMS メッセージがユーザーに配信されなかったとき
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | SMS メッセージが送信されたとき
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | ユーザーが SMS メッセージに含まれる Braze 短縮 URL をクリックしたとき
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | 優先度が下げられた、またはフリークエンシーキャップに達した後に SMS メッセージが再試行されたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | 元々スケジュールされた Webhook メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Webhook メッセージが配信されたが、エンドポイントからエラーレスポンスで失敗したとき
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | ユーザーに対して Webhook を送信したとき
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | 優先度が下げられた、またはフリークエンシーキャップに達した後に Webhook メッセージが再試行されたとき（**Snowflake Data Sharing のみ**）
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | 元々スケジュールされた WhatsApp メッセージが何らかの理由で中止されたとき
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | ユーザーが WhatsApp メッセージ内のリンクまたはボタンをクリックしたとき
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | WhatsApp メッセージが配信されたとき
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | WhatsApp メッセージがユーザーに配信されなかったとき
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | ユーザーから WhatsApp メッセージを受信したとき
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | ユーザーが WhatsApp メッセージを開封したとき
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | ユーザーに対して WhatsApp メッセージを送信したとき
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | 優先度が下げられた、またはフリークエンシーキャップに達した後に WhatsApp メッセージが再試行されたとき（**Snowflake Data Sharing のみ**）
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | ユーザーのランダムバケット番号が変更されたとき
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | 顧客のリクエストによりユーザーが削除されたとき
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | ユーザーが別のユーザーのプロファイルにマージされ、元のプロファイルが孤立したとき
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | アプリスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | キャンペーンメッセージバリアントのスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | キャンバスフローステップのスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | キャンバスステップのスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | キャンバスバリアントのスナップショット（**Snowflake Data Sharing のみ**）
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | 実験ステップのスナップショット（**Snowflake Data Sharing のみ**）

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
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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

### USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

使用方法のガイダンスとクエリの例については、[Snowflake ユーザー属性]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#historical-change-logs)を参照してください。

### USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED {#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

使用方法のガイダンスとクエリの例については、[Snowflake ユーザー属性]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#real-time-user-profile-views)を参照してください。

## カタログ {#catalogs}

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

フィールド | タイプ | 説明
------|------|------------
`catalog_id` | `string` | カタログのBSON ID
`item_id` | `string` | カタログアイテムのBSON ID
`app_group_id` | `null,`&nbsp;`string` | アプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | アプリグループのAPI ID
`field_name` | `null,`&nbsp;`string` | フィールドの名前
`field_value` | `null,`&nbsp;`string` | フィールドの値
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CATALOGSITEMSSHARED #CATALOGSITEMSSHARED" }

## 変更ログ {#changelogs}

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`random_bucket_number` | `null, int` | 新しいランダムバケット番号
`global_control_group` | `null, boolean` | この変更により、バケット番号がグローバルコントロールグループに含まれます
`previous_global_control_group` | `null, boolean` | この変更前はバケット番号がグローバルコントロールグループに含まれていましたが、現在は含まれていません
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSGLOBALCONTROLGROUPSHARED #CHANGELOGSGLOBALCONTROLGROUPSHARED" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループのBSON ID
`api_id` | `string` | キャンペーンのAPI ID
`name` | `null,`&nbsp;`string` | キャンペーンの名前
`conversion_behaviors` | `null,`&nbsp;`string` | キャンペーンのコンバージョン行動
`actions` | `null,`&nbsp;`string` | キャンペーンのアクション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCAMPAIGNSHARED #CHANGELOGSCAMPAIGNSHARED" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバル一意ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `string` | このユーザーが属するアプリグループのBSON ID
`api_id` | `string` | キャンバスのAPI ID
`name` | `null,`&nbsp;`string` | キャンバスの名前
`conversion_behaviors` | `null,`&nbsp;`string` | キャンバスのコンバージョン行動
`variations` | `null,`&nbsp;`string` | キャンバスのバリエーション
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCANVASSHARED #CHANGELOGSCANVASSHARED" }

## ビヘイビア {#behaviors}

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`name` | `string` | カスタムイベントの名前
`properties` | `string` | JSON エンコードされた文字列として保存されたイベントのカスタムプロパティ
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSCUSTOMEVENTSHARED #USERSBEHAVIORSCUSTOMEVENTSHARED" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | インストールを行ったユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合にこのユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | ユーザーがインストールした Unix タイムスタンプ
`source` | `string` | アトリビューションのソース
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSINSTALLATTRIBUTIONSHARED #USERSBEHAVIORSINSTALLATTRIBUTIONSHARED" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 位置情報を記録したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | この位置情報が記録されたアプリの API ID
`time` | `int` | 位置情報が記録された Unix タイムスタンプ
`latitude` | `float` | [PII] 記録された位置の緯度
`longitude` | `float` | [PII] 記録された位置の経度
`altitude` | `null, float` | [PII] 記録された位置の高度
`ll_accuracy` | `null, float` | 記録された位置の緯度・経度の精度
`alt_accuracy` | `null, float` | 記録された位置の高度の精度
`device_id` | `null,`&nbsp;`string` | 位置情報が記録されたデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | 位置情報の記録時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLOCATIONSHARED #USERSBEHAVIORSLOCATIONSHARED" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 購入を行ったユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | 購入が発生したアプリの API ID
`time` | `int` | ユーザーが購入した Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | 購入が発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | 購入時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`product_id` | `string` | 購入された商品の ID
`price` | `float` | 購入の価格
`currency` | `string` | 購入の通貨
`properties` | `string` | JSON エンコードされた文字列として保存された購入のカスタムプロパティ
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または `roku_ad_id` のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPURCHASESHARED #USERSBEHAVIORSPURCHASESHARED" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アンインストールしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合にこのユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | アンインストールされたアプリの API ID
`time` | `int` | ユーザーがアンインストールした Unix タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUNINSTALLSHARED #USERSBEHAVIORSUNINSTALLSHARED" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | アプリをアップグレードしたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | ユーザーがアップグレードしたアプリの API ID
`time` | `int` | ユーザーがアプリをアップグレードした Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | ユーザーがアプリをアップグレードしたデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | 使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`old_app_version` | `null,`&nbsp;`string` | アプリの旧バージョン
`new_app_version` | `null,`&nbsp;`string` | アプリの新バージョン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUPGRADEDAPPSHARED #USERSBEHAVIORSUPGRADEDAPPSHARED" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
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
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPFIRSTSESSIONSHARED #USERSBEHAVIORSAPPFIRSTSESSIONSHARED" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED #USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`time` | `int` | セッションが終了した Unix タイムスタンプ
`duration` | `null, float` | セッションの継続時間（秒）
`session_id` | `string` | セッションの UUID
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONENDSHARED #USERSBEHAVIORSAPPSESSIONENDSHARED" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このアクションを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_api_id` | `null,`&nbsp;`string` | このセッションが発生したアプリの API ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | セッションが開始された Unix タイムスタンプ
`session_id` | `string` | セッションの UUID
`device_id` | `null,`&nbsp;`string` | セッションが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | セッション中に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONSTARTSHARED #USERSBEHAVIORSAPPSESSIONSTARTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類（例: 'enter' または 'exit'）
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCEDATAEVENTSHARED #USERSBEHAVIORSGEOFENCEDATAEVENTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | イベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | このアクションが発生したアプリの API ID
`time` | `int` | ユーザーがイベントを実行した Unix タイムスタンプ
`device_id` | `null,`&nbsp;`string` | カスタムイベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`event_type` | `string` | トリガーされたジオフェンスイベントの種類（例: 'enter' または 'exit'）
`location_set_id` | `string` | トリガーされたジオフェンスのロケーションセットの ID
`geofence_id` | `string` | トリガーされたジオフェンスの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCERECORDEVENTSHARED #USERSBEHAVIORSGEOFENCERECORDEVENTSHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`activity_attributes_type` | `null,`&nbsp;`string` | ライブアクティビティの属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | ライブアクティビティの Push to Start トークン
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APNS ゲートウェイ。iOS プッシュトークンにのみ適用されます。1 は開発用、2 は本番用です
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`activity_id` | `null,`&nbsp;`string` | ライブアクティビティの識別子
`update_token` | `null,`&nbsp;`string` | ライブアクティビティの更新トークン
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APNS ゲートウェイ。iOS プッシュトークンにのみ適用されます。1 は開発用、2 は本番用です
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`time_ms` | `int` | イベントが発生した時刻（ミリ秒）
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`push_token` | `null,`&nbsp;`string` | イベントのプッシュトークン
`push_token_created_at` | `null, int` | プッシュトークンが作成された UNIX タイムスタンプ
`push_token_updated_at` | `null, int` | プッシュトークンが最後に更新された UNIX タイムスタンプ
`push_token_foreground_push_disabled` | `null, boolean` | プッシュトークンのフォアグラウンドプッシュ無効化フラグ
`push_token_device_id` | `null,`&nbsp;`string` | プッシュトークンのデバイス ID
`push_token_provisionally_opted_in` | `null, boolean` | プッシュトークンの仮オプトインフラグ
`ios_push_token_apns_gateway` | `null, int` | プッシュトークンの APNS ゲートウェイ。iOS プッシュトークンにのみ適用されます。1 は開発用、2 は本番用です
`web_push_token_public_key` | `null,`&nbsp;`string` | プッシュトークンの公開キー。Web プッシュトークンにのみ適用されます
`web_push_token_user_auth` | `null,`&nbsp;`string` | プッシュトークンのユーザー認証。Web プッシュトークンにのみ適用されます
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | プッシュトークンの VAPID 公開キー。Web プッシュトークンにのみ適用されます
`push_token_state_change_type` | `null,`&nbsp;`string` | プッシュトークンの状態変更タイプの説明
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの API ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED #USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`state_change_source` | `null,`&nbsp;`string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`subscription_status` | `string` | 購読ステータス: 'Subscribed'、'Unsubscribed'、または 'Opted In'
`channel` | `null,`&nbsp;`string` | メールなど、グローバル購読状態のチャネル
`time` | `int` | 購読状態が変更された Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`app_api_id` | `null,`&nbsp;`string` | イベントが属するアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`send_id` | `null,`&nbsp;`string` | この購読状態変更アクションの発生元であるメッセージ送信 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] イベント対象チャネルにおけるユーザーの識別子
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | 影響を受けたユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合にこのユーザーに紐づく `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`phone_number` | `null,`&nbsp;`string` | [PII] e164 形式のユーザーの電話番号
`app_api_id` | `null,`&nbsp;`string` | イベントが属するアプリの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`subscription_group_api_id` | `string` | 購読グループ API ID
`channel` | `null,`&nbsp;`string` | チャネル: 購読グループのチャネルタイプに応じて 'email' または 'sms'
`subscription_status` | `string` | 購読ステータス: 'Subscribed'、'Unsubscribed'、または 'Opted In'
`time` | `int` | 購読状態が変更された Unix タイムスタンプ
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`send_id` | `null,`&nbsp;`string` | この購読状態変更アクションの発生元であるメッセージ送信 ID
`state_change_source` | `null,`&nbsp;`string` | 状態変更のソース（REST、SDK、ダッシュボードなど）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`channel_identifier` | `null,`&nbsp;`string` | [PII] イベント対象チャネルにおけるユーザーの識別子
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED" }

## キャンペーン {#campaigns}

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられる `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの Braze 内部使用 ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`conversion_behavior_index` | `null, int` | コンバージョン行動のインデックス
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe により取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSCONVERSIONSHARED #USERSCAMPAIGNSCONVERSIONSHARED" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられる `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの Braze 内部使用 ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe により取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSENROLLINCONTROLSHARED #USERSCAMPAIGNSENROLLINCONTROLSHARED" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられる `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの Braze 内部使用 ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`channel` | `null,`&nbsp;`string` | このイベントが属するチャネル
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe により取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSFREQUENCYCAPSHARED #USERSCAMPAIGNSFREQUENCYCAPSHARED" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられる `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `string` | このイベントが属するキャンペーンの Braze 内部使用 ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`revenue` | `long` | 生成された USD 収益の金額（セント単位）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe により取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSREVENUESHARED #USERSCAMPAIGNSREVENUESHARED" }

## キャンバス {#canvas}

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| フィールド                             | タイプ                   | 説明                                                                                                            |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                                                              |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                                                                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                                                                     |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスのID                                                    |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                                                                  |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのAPI ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                                                            |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID                                                          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                                                                          |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                                                                  |
| `progression_type`                     | `string`,&nbsp;`null`    | ステップ進行イベントのタイプ                                                                                    |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | キャンバスの最初のステップへのエントリかどうか                                                                  |
| `exit_reason`                          | `string`,&nbsp;`null`    | 離脱の場合、ユーザーがそのステップでキャンバスを離脱した理由                                                    |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | キャンバス内のユーザーのこのインスタンスの一意の識別子                                                          |
| `next_step_id`                         | `string`,&nbsp;`null`    | キャンバスの次のステップのBSON ID                                                                               |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | キャンバスの次のステップのAPI ID                                                                                |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                                                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASSTEPPROGRESSIONSHARED #USERSCANVASSTEPPROGRESSIONSHARED" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| フィールド                             | タイプ                   | 説明                                                                                                            |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                                                              |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                                                                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                                                                     |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスのID                                                    |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                                                                  |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのAPI ID                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                                                            |
| `app_api_id`                           | `string`,&nbsp;`null`    | このイベントが発生したアプリのAPI ID                                                                            |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID                                                          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                                                                          |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                                                                  |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID                                        |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | ユーザーが実行したコンバージョンイベントのタイプ。「0」は1次コンバージョン、「1」は2次コンバージョンです         |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                                                                            |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                                                                              |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                                                                          |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                                                                            |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                                                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCONVERSIONSHARED #USERSCANVASCONVERSIONSHARED" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| フィールド                | タイプ                   | 説明                                                                 |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                   |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                             |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                          |
| `device_id`               | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスのID         |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                       |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                 |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID               |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                               |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [非推奨] このイベントが属するキャンバスステップのAPI ID              |
| `gender`                  | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                                 |
| `country`                 | `string`,&nbsp;`null`    | [PII] ユーザーの国                                                   |
| `timezone`                | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                               |
| `language`                | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                                 |
| `in_control_group`        | `boolean`,&nbsp;`null`   | ユーザーがコントロールグループに登録されたかどうか                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASENTRYSHARED #USERSCANVASENTRYSHARED" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| フィールド                | タイプ                   | 説明                                                                 |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                   |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                             |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                          |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                       |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                 |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID               |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                               |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                       |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED #USERSCANVASEXITMATCHEDAUDIENCESHARED" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| フィールド                | タイプ                   | 説明                                                                 |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                   |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                             |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                          |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                       |
| `app_group_api_id`        | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                 |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID               |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                               |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                       |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITPERFORMEDEVENTSHARED #USERSCANVASEXITPERFORMEDEVENTSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| フィールド                  | タイプ                   | 説明                                                                                                            |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                                                              |
| `user_id`                   | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                                                                        |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                                                                     |
| `app_group_id`              | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                                                                  |
| `time`                      | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                                                            |
| `app_api_id`                | `string`,&nbsp;`null`    | このイベントが発生したアプリのAPI ID                                                                            |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID                                                          |
| `canvas_api_id`             | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                                                                          |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                                                            |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                                                                  |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | このイベントが属する実験ステップのAPI ID                                                                        |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | ユーザーが実行したコンバージョンイベントのタイプ。「0」は1次コンバージョン、「1」は2次コンバージョンです         |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                                                                    |
| `experiment_split_api_id` | `string`,&nbsp;`null` | ユーザーが登録された実験スプリットのAPI ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED #USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| フィールド                | タイプ                   | 説明                                                                 |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                   |
| `user_id`                 | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                             |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                          |
| `app_group_id`            | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                       |
| `time`                    | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                 |
| `canvas_id`               | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID               |
| `canvas_api_id`           | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                               |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                       |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | このイベントが属する実験ステップのAPI ID                             |
| `in_control_group`        | `boolean`,&nbsp;`null`   | ユーザーがコントロールグループに登録されたかどうか                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

| `experiment_split_api_id` | `string`,&nbsp;`null` | ユーザーが登録された実験スプリットのAPI ID |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED #USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| フィールド                             | タイプ                   | 説明                                                                 |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                   |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                             |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                          |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスのID         |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                       |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                 |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID               |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                               |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                       |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID |
| `channel`                              | `string`,&nbsp;`null`    | このイベントが属するメッセージングチャネル（メール、プッシュなど）   |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                                 |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                                   |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                               |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                                 |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASFREQUENCYCAPSHARED #USERSCANVASFREQUENCYCAPSHARED" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| フィールド                             | タイプ                   | 説明                                                                 |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | このイベントのグローバルな一意のID                                   |
| `user_id`                              | `string`,&nbsp;`null`    | このイベントを実行したユーザーのBraze ID                             |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] ユーザーのexternal ID                                          |
| `device_id`                            | `string`,&nbsp;`null`    | ユーザーが匿名の場合、このユーザーに紐づけられたデバイスのID         |
| `app_group_id`                         | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのBraze ID                       |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースのAPI ID                         |
| `time`                                 | `int`,&nbsp;`null`       | イベントが発生したUnixタイムスタンプ                                 |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Braze内部使用のみ) このイベントが属するキャンバスのID               |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | このイベントが属するキャンバスのAPI ID                               |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | このイベントが属するキャンバスバリエーションのAPI ID                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | このイベントが属するキャンバスステップのAPI ID                       |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID |
| `gender`                               | `string`,&nbsp;`null`    | [PII] ユーザーの性別                                                 |
| `country`                              | `string`,&nbsp;`null`    | [PII] ユーザーの国                                                   |
| `timezone`                             | `string`,&nbsp;`null`    | ユーザーのタイムゾーン                                               |
| `language`                             | `string`,&nbsp;`null`    | [PII] ユーザーの言語                                                 |
| `revenue`                              | `int`,&nbsp;`null`       | 生成された収益額（USD、セント単位で表示）                            |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時                         |
| `app_api_id` | `string`,&nbsp;`null` | このイベントが発生したアプリのAPI ID |
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
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
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナープレースメント ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
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
`button_id` | `null,`&nbsp;`string` | クリックされたボタンの ID（このクリックがボタンのクリックである場合）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id'] のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナープレースメント ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
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
`banner_placement_id` | `null,`&nbsp;`string` | 顧客が指定したバナープレースメント ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERIMPRESSIONSHARED #USERSMESSAGESBANNERIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を記述するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDIMPRESSIONSHARED #USERSMESSAGESCONTENTCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`content_card_id` | `string` | このイベントを生成したカードの ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDSENDSHARED #USERSMESSAGESCONTENTCARDSENDSHARED" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILABORTSHARED #USERSMESSAGESEMAILABORTSHARED" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`bounce_reason` | `null,`&nbsp;`string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザー向けメッセージ
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_drop` | `null, boolean` | このイベントがドロップイベントとしてカウントされるかどうかを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILBOUNCESHARED #USERSMESSAGESEMAILBOUNCESHARED" }

{% alert note %}
1回のハードバウンスに対して、同じユーザーに複数の行が表示される場合があります。これは、イベントが非同期に処理された場合や、関連する送信の `dispatch_id` 値が異なる場合に発生する可能性があります。重複を排除したりエクスポートを分析したりする際は、`dispatch_id`、`time`、および `id` を合わせて確認してください。
{% endalert %}

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`deferral_reason` | `null,`&nbsp;`string` | [PII] この保留イベントで受信した SMTP 理由コードとユーザー向けメッセージ
`attempt_count` | `null, int` | メッセージ送信の試行回数
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDEFERRALSHARED #USERSMESSAGESEMAILDEFERRALSHARED" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDELIVERYSHARED #USERSMESSAGESEMAILDELIVERYSHARED" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILMARKASSPAMSHARED #USERSMESSAGESEMAILMARKASSPAMSHARED" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`user_agent` | `null,`&nbsp;`string` | 開封が発生したユーザーエージェント
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`machine_open` | `null,`&nbsp;`string` | ユーザーの操作なしに開封イベントがトリガーされた場合（たとえば、メールプライバシー保護が有効な Apple デバイスによる場合）に 'true' が設定されます。より詳細な情報を提供するために、この値は今後変更される可能性があります。
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`is_amp` | `null, boolean` | これが AMP イベントであるかどうかを示します
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILOPENSHARED #USERSMESSAGESEMAILOPENSHARED" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSENDSHARED #USERSMESSAGESEMAILSENDSHARED" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`sending_ip` | `null,`&nbsp;`string` | メール送信に使用された IP アドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`bounce_reason` | `null,`&nbsp;`string` | [PII] このバウンスイベントで受信した SMTP 理由コードとユーザー向けメッセージ
`esp` | `null,`&nbsp;`string` | イベントに関連する ESP（SparkPost、SendGrid、または Amazon SES）
`from_domain` | `null,`&nbsp;`string` | メールの送信ドメイン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSOFTBOUNCESHARED #USERSMESSAGESEMAILSOFTBOUNCESHARED" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

このテーブルには、受信者側からのメッセージレベルのメール購読解除が記録されます。これには、購読解除リンクのクリック、メールクライアントのワンクリック List-Unsubscribe、ユーザー設定センターの送信、および ESP から報告された購読解除が含まれます。REST APIを通じて行われた購読解除は含まれません。それらの操作では、代わりに [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) または [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) イベントが送出されます。

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用された IP プール
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILUNSUBSCRIBESHARED #USERSMESSAGESEMAILUNSUBSCRIBESHARED" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

このイベントは、メッセージの優先度が下げられた場合やフリークエンシーキャップが適用された場合に発生し、設定されたリトライウィンドウ内で後ほど再試行されます。

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | [PII] このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`retry_type` | `null,`&nbsp;`string` | リトライの種類
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を説明するログメッセージ
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのBSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`email_address` | `null,`&nbsp;`string` | [PII] ユーザーのメールアドレス
`ip_pool` | `null,`&nbsp;`string` | メール送信に使用されたIPプール
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILRETRYSHARED #USERSMESSAGESEMAILRETRYSHARED" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのBSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのBSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`feature_flag_id_name` | `null,`&nbsp;`string` | フィーチャーフラグのロールアウト識別子
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー — user_agentから抽出 — 開封が発生したブラウザー
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED #USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,`&nbsp;`string` | カードのAPI ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または`roku_ad_id`のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`abort_type` | `null,`&nbsp;`string` | 中止の種類。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEABORTSHARED #USERSMESSAGESINAPPMESSAGEABORTSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,`&nbsp;`string` | カードのAPI ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`button_id` | `null,`&nbsp;`string` | このクリックがボタンのクリックである場合の、クリックされたボタンのID
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または`roku_ad_id`のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGECLICKSHARED #USERSMESSAGESINAPPMESSAGECLICKSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,`&nbsp;`string` | カードのAPI ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`version` | `string` | アプリ内メッセージのバージョン（レガシーまたはトリガー）
`ad_id` | `null,`&nbsp;`string` | [PII] 広告識別子
`ad_id_type` | `null,`&nbsp;`string` | `ios_idfa`、`google_ad_id`、`windows_ad_id`、または`roku_ad_id`のいずれか
`ad_tracking_enabled` | `null, boolean` | デバイスで広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquidレンダリング時にタグ付けされたキーと値のペアのJSON文字列
`locale_key` | `null,`&nbsp;`string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例: 'en-us'）（デフォルトの場合はnull）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED #USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

フィールド | 型 | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`id` | `string` | このイベントのグローバルに一意なID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大128文字）
`abort_type` | `null,`&nbsp;`string` | 中止の種類。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネルID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネル名
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元となるユーザーのLine ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | 購読グループAPI ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`campaign_name` | `null,`&nbsp;`string` | キャンペーン名
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップ名
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEABORTSHARED #USERSMESSAGESLINEABORTSHARED" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

フィールド | 型 | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`id` | `string` | このイベントのグローバルに一意なID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元となるユーザーのLine ID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネルID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネル名
`subscription_group_api_id` | `string` | 購読グループAPI ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーン名
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップ名
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`is_suspected_bot_click` | `null, boolean` | このイベントがボットイベントとして処理されたかどうか
`short_url` | `null,`&nbsp;`string` | クリックされた短縮URL
`url` | `null,`&nbsp;`string` | ユーザーがクリックしたURL
`user_agent` | `null,`&nbsp;`string` | スパムレポートが発生したユーザーエージェント
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINECLICKSHARED #USERSMESSAGESLINECLICKSHARED" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

フィールド | 型 | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`id` | `string` | このイベントのグローバルに一意なID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーン名
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップ名
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネルID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネル名
`media_id` | `null,`&nbsp;`string` | LINEから受信メディアを取得するために使用できるLINE生成ID
`message_body` | `null,`&nbsp;`string` | ユーザーからの入力応答
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元となるユーザーのLine ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | 購読グループAPI ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEINBOUNDRECEIVESHARED #USERSMESSAGESLINEINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

フィールド | 型 | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`id` | `string` | このイベントのグローバルに一意なID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーン名
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップ名
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネルID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネル名
`message_extras` | `null,`&nbsp;`string` | [PII] Liquidレンダリング時にタグ付けされたキーと値のペアのJSON文字列
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元となるユーザーのLine ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`subscription_group_api_id` | `string` | 購読グループAPI ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINESENDSHARED #USERSMESSAGESLINESENDSHARED" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

このイベントは、メッセージの優先度が下げられた場合やフリークエンシーキャップが適用された場合に発生し、設定されたリトライウィンドウ内で後ほど再試行されます。

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | [PII] このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`retry_type` | `null,`&nbsp;`string` | リトライの種類
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を説明するログメッセージ
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのBSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`line_channel_id` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネルID
`line_channel_name` | `null,`&nbsp;`string` | メッセージの送受信先のLINEチャネル名
`native_line_id` | `null,`&nbsp;`string` | [PII] メッセージの送受信元となるユーザーのLine ID
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループAPI ID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINERETRYSHARED #USERSMESSAGESLINERETRYSHARED" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`activity_id` | `null,`&nbsp;`string` | ライブアクティビティ識別子
`activity_attributes_type` | `null,`&nbsp;`string` | ライブアクティビティの属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | ライブアクティビティのpush to startトークン
`update_token` | `null,`&nbsp;`string` | ライブアクティビティの更新トークン
`live_activity_event_type` | `null,`&nbsp;`string` | ライブアクティビティのイベントタイプ。['start', 'update', 'end']のいずれか
`live_activity_event_outcome` | `null,`&nbsp;`string` | ライブアクティビティイベントの結果
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYOUTCOMESHARED #USERSMESSAGESLIVEACTIVITYOUTCOMESHARED" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`activity_id` | `null,`&nbsp;`string` | ライブアクティビティ識別子
`activity_attributes_type` | `null,`&nbsp;`string` | ライブアクティビティの属性タイプ
`push_to_start_token` | `null,`&nbsp;`string` | ライブアクティビティのpush to startトークン
`update_token` | `null,`&nbsp;`string` | ライブアクティビティの更新トークン
`live_activity_event_type` | `null,`&nbsp;`string` | ライブアクティビティのイベントタイプ。['start', 'update', 'end']のいずれか
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYSENDSHARED #USERSMESSAGESLIVEACTIVITYSENDSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,`&nbsp;`string` | カードのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー — user_agentから抽出 — 開封が発生したブラウザー
`abort_type` | `null,`&nbsp;`string` | 中止の種類。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大128文字）
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDABORTSHARED #USERSMESSAGESNEWSFEEDCARDABORTSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,`&nbsp;`string` | カードのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー — user_agentから抽出 — 開封が発生したブラウザー
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDCLICKSHARED #USERSMESSAGESNEWSFEEDCARDCLICKSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`card_api_id` | `null,`&nbsp;`string` | カードのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー — user_agentから抽出 — 開封が発生したブラウザー
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED #USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザーID
`device_id` | `null,`&nbsp;`string` | 配信を試みた`device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `string` | デバイスのプラットフォーム
`abort_type` | `null,`&nbsp;`string` | 中止の種類。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大2,000文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONABORTSHARED #USERSMESSAGESPUSHNOTIFICATIONABORTSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザーID
`push_token` | `null,`&nbsp;`string` | バウンスしたプッシュトークン
`device_id` | `null,`&nbsp;`string` | バウンスした配信試行先の`device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`ad_id` | `null,`&nbsp;`string` | [PII] 配信試行先デバイスの広告ID
`ad_id_type` | `null,`&nbsp;`string` | 広告IDの種類
`ad_tracking_enabled` | `null, boolean` | 広告トラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED #USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

フィールド | 型 | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意なID
`user_id` | `string` | このイベントを実行したユーザーのBraze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザーID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`app_api_id` | `null,`&nbsp;`string` | このイベントが発生したアプリのAPI ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`sdk_version` | `null,`&nbsp;`string` | イベント発生時に使用されていたBraze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスのキャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザー
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループのBSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeに取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
このイベントは[Swift SDK](https://github.com/braze-inc/braze-swift-sdk)ではサポートされておらず、[Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk)では非推奨になっています。
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザ
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`sdk_version` | `null,`&nbsp;`string` | イベント時に使用されていた Braze SDKのバージョン
`platform` | `null,`&nbsp;`string` | デバイスのプラットフォーム
`os_version` | `null,`&nbsp;`string` | デバイスのオペレーティングシステムのバージョン
`device_model` | `null,`&nbsp;`string` | デバイスのモデル
`resolution` | `null,`&nbsp;`string` | デバイスの解像度
`carrier` | `null,`&nbsp;`string` | デバイスの通信キャリア
`browser` | `null,`&nbsp;`string` | デバイスのブラウザ
`button_string` | `null,`&nbsp;`string` | クリックされたプッシュ通知ボタンの識別子 (button_string)。ボタンのクリックによるものでない場合は null
`button_action_type` | `null,`&nbsp;`string` | プッシュ通知ボタンのアクションタイプ。[URI, DEEP_LINK, NONE, CLOSE] のいずれか。ボタンのクリックによるものでない場合は null
`slide_id` | `null,`&nbsp;`string` | ユーザーがクリックしたプッシュカルーセルスライドのスライド識別子
`slide_action_type` | `null,`&nbsp;`string` | プッシュカルーセルスライドのアクションタイプ
`ad_id` | `null,`&nbsp;`string` | [PII] 配信を試みたデバイスの広告 ID
`ad_id_type` | `null,`&nbsp;`string` | 広告 ID のタイプ
`ad_tracking_enabled` | `null, boolean` | 広告のトラッキングが有効かどうか
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング時にタグ付けされたキーと値のペアの JSON 文字列
`is_sampled` | `null,`&nbsp;`string` | プッシュ送信がサンプリングされ、配信イベントが期待されていたかどうかを示します
`locale_key` | `null,`&nbsp;`string` | [PII] このメッセージの作成に使用された翻訳に対応するキー（例: 'en-us'）。デフォルトの場合は null です。
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONSENDSHARED #USERSMESSAGESPUSHNOTIFICATIONSENDSHARED" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大128文字）
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスバリエーションの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`subscription_group_api_id` | `string` | 購読グループの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSABORTSHARED #USERSMESSAGESRCSABORTSHARED" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
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
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`interaction_type` | `null,`&nbsp;`string` | クリックを発生させたインタラクションのタイプ。文字列値の例: Text URL、Reply、OpenURL
`element_label` | `null,`&nbsp;`string` | クリックされた要素に関するオプションの詳細（候補の返信やボタンのテキストなど）
`element_type` | `null,`&nbsp;`string` | 候補とボタンに共通する interaction_type が候補由来かボタン由来かを指定します。例: Suggestion、Button
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`url` | `null,`&nbsp;`string` | ユーザーがクリックした URL
`subscription_group_api_id` | `string` | 購読グループの API ID
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスバリエーションの名前
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSCLICKSHARED #USERSMESSAGESRCSCLICKSHARED" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスバリエーションの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | 購読グループの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164形式。例: +14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSDELIVERYSHARED #USERSMESSAGESRCSDELIVERYSHARED" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`action` | `null,`&nbsp;`string` | このメッセージに対して実行されたアクション（例: Subscribed、Unsubscribed、None）
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`media_urls` | `null,`&nbsp;`string` | ユーザーからのメディア URL
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`user_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信したユーザーの電話番号
`subscription_group_api_id` | `string` | 購読グループの API ID
`message_body` | `null,`&nbsp;`string` | ユーザーからの入力されたレスポンス
`to_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信先である受信 RCS 送信者
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSINBOUNDRECEIVESHARED #USERSMESSAGESRCSINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスバリエーションの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164形式。例: +14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREADSHARED #USERSMESSAGESRCSREADSHARED" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスバリエーションの名前
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`error` | `null,`&nbsp;`string` | エラー名
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`is_sms_fallback` | `null, boolean` | この拒否された RCS メッセージに対して SMS フォールバックが試行されたかどうかを示します。SMS 配信イベントにリンク/ペアリングされています
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`provider_error_code` | `null,`&nbsp;`string` | プロバイダーからのエラーコード
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | 購読グループの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164形式。例: +14155552671）
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREJECTIONSHARED #USERSMESSAGESRCSREJECTIONSHARED" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

フィールド | タイプ | 説明
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
`canvas_step_name` | `null,`&nbsp;`string` | キャンバスステップの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスバリエーションの名前
`category` | `null,`&nbsp;`string` | キーワードカテゴリ名。自動返信メッセージの場合にのみ設定されます: 'opt-in'、'opt-out'、'help'、またはカスタム値
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスの ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`from_rcs_sender` | `null,`&nbsp;`string` | メッセージの送信に使用された RCS 送信者 ID またはエージェント名
`message_extras` | `null,`&nbsp;`string` | Liquid レンダリング時にタグ付けされたキーと値のペアの JSON 文字列
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`subscription_group_api_id` | `string` | 購読グループの API ID
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーの電話番号（e.164形式。例: +14155552671）
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取り込まれた日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSSENDSHARED #USERSMESSAGESRCSSENDSHARED" }

## SMS メッセージイベントと削除されたユーザープロファイル {#sms-message-events-and-deleted-user-profiles}

{% alert note %}
`USERS_MESSAGES_SMS_*` 共有テーブル（[`USERS_MESSAGES_SMS_REJECTION_SHARED`](#USERS_MESSAGES_SMS_REJECTION_SHARED)、[`USERS_MESSAGES_SMS_DELIVERY_SHARED`](#USERS_MESSAGES_SMS_DELIVERY_SHARED)、[`USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED`](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) を含む）について、Brazeはイベントが Snowflake データ共有および Currents 向けに処理される時点でワークスペースにBrazeユーザープロファイルがまだ存在している場合にのみ行を書き込みます。処理完了前にそのユーザーが削除された場合、ダッシュボードの SMS ワークスペースメトリクスが Braze のレポートパスからの集計カウントを反映していても、そのイベントは Snowflake や Currents エクスポートに表示されません。対応する Currents の動作については、同じ用語集にある [SMS 拒否イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) および関連する SMS イベントタイプを参照してください。
{% endalert %}

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループの外部 ID
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大 2,000 文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSABORTSHARED #USERSMESSAGESSMSABORTSHARED" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSCARRIERSENDSHARED #USERSMESSAGESSMSCARRIERSENDSHARED" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループの外部 ID
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
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループの外部 ID
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
`subscription_group_id` | `null,`&nbsp;`string` | この SMS メッセージの対象となる購読グループの ID
`subscription_group_api_id` | `null,`&nbsp;`string` | この SMS メッセージの対象となる購読グループの API ID
`inbound_phone_number` | `string` | メッセージの送信先である受信番号
`action` | `string` | このメッセージに応じて実行されたアクション。例: `Subscribed`、`Unsubscribed`、`None`。
`message_body` | `string` | ユーザーからの応答
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディア URL
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`from_phone_number` | `null,`&nbsp;`string` | SMS メッセージの送信元電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループの外部 ID
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
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループの外部 ID
`category` | `null,`&nbsp;`string` | キーワードカテゴリ名。自動返信メッセージの場合のみ設定されます: 'Opt-in'、'Opt-out'、'Help'、またはカスタム値
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
`campaign_id` | `null,`&nbsp;`string` | short_url が生成されたキャンペーンの Braze ID。キャンペーンからでない場合は null
`campaign_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンペーンの API ID。キャンペーンからでない場合は null
`message_variation_api_id` | `null,`&nbsp;`string` | short_url が生成されたメッセージバリエーションの API ID。キャンペーンからでない場合は null
`canvas_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスの Braze ID。キャンバスからでない場合は null
`canvas_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスの API ID。キャンバスからでない場合は null
`canvas_variation_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスバリエーションの API ID。キャンバスからでない場合は null
`canvas_step_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスステップの API ID。キャンバスからでない場合は null
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | short_url が生成されたキャンバスステップメッセージバリエーションの API ID。キャンバスからでない場合は null
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

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

このイベントは、メッセージの優先度が下げられた場合やフリークエンシーキャップが適用された場合に、設定されたリトライウィンドウ内で後からリトライされたときに発生します。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`user_id` | `string` | [PII] このイベントを実行したユーザーの Braze ユーザー ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループ API ID
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を説明するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSRETRYSHARED #USERSMESSAGESSMSRETRYSHARED" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大 2,000 文字）
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKABORTSHARED #USERSMESSAGESWEBHOOKABORTSHARED" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`http_status_code` | `null, int` | レスポンスの HTTP ステータスコード
`endpoint_url` | `null,`&nbsp;`string` | リクエストされているエンドポイント URL
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの API ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するアプリグループの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`content_length` | `null, int` | レスポンスのコンテンツ長
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部 ID
`host` | `null,`&nbsp;`string` | リクエストのホスト
`id` | `string` | このイベントのグローバルな一意の ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`raw_response` | `null,`&nbsp;`string` | エンドポイントからの切り詰められた生レスポンス
`retry_count` | `null, int` | 試行されたリトライの回数
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`time` | `int` | イベントが発生した UNIX タイムスタンプ
`url_path` | `null,`&nbsp;`string` | リクエストされている URL のパス
`user_id` | `string` | このイベントを実行したユーザーの Braze ユーザー ID
`webhook_duration` | `null, int` | このリクエストの合計所要時間（ミリ秒）
`webhook_failure_source` | `null,`&nbsp;`string` | エラーが Braze によって生成されたのか、エンドポイント自体によって生成されたのかを示します。source フィールドの値は External Endpoint、Treat no status code to host unreachable のいずれかです
`is_terminal` | `null, boolean` | このイベントが送信における最終試行であったかどうか
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKFAILURESHARED #USERSMESSAGESWEBHOOKFAILURESHARED" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`campaign_name` | `null,`&nbsp;`string` | キャンペーンの名前
`message_variation_name` | `null,`&nbsp;`string` | メッセージバリエーションの名前
`canvas_name` | `null,`&nbsp;`string` | キャンバスの名前
`canvas_variation_name` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスバリエーションの名前
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

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

このイベントは、メッセージの優先度が下げられた場合やフリークエンシーキャップが適用された場合に、設定されたリトライウィンドウ内で後からリトライされたときに発生します。

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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`gender` | `null,`&nbsp;`string` | [PII] ユーザーの性別
`country` | `null,`&nbsp;`string` | [PII] ユーザーの国
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`language` | `null,`&nbsp;`string` | [PII] ユーザーの言語
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を説明するログメッセージ
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
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | 購読グループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`abort_type` | `null,`&nbsp;`string` | 中止のタイプ。値の一覧については、[中止タイプ](#abort-types)を参照してください。
`abort_log` | `null,`&nbsp;`string` | [PII] 中止の詳細を説明するログメッセージ（最大 2,000 文字）
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
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの BSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの BSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
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
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | 購読グループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | このメッセージに対して Meta が生成した一意の ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPDELIVERYSHARED #USERSMESSAGESWHATSAPPDELIVERYSHARED" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | 購読グループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`provider_error_code` | `null,`&nbsp;`string` | WhatsApp からのエラーコード
`provider_error_title` | `null, `&nbsp;`string` | WhatsApp からのエラータイトル
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`message_id` | `null,`&nbsp;`string` | このメッセージに対して Meta が生成した一意の ID
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
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | 購読グループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`message_body` | `string` | ユーザーからの応答
`quick_reply_text` | `string` | ユーザーが押したボタンのテキスト
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | ユーザーからのメディア URL
`action` | `string` | このメッセージに応じて実行されたアクション。例: `Subscribed`、`Unsubscribed`、`None`。
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`catalog_id` | `null,`&nbsp;`string` | 受信メッセージで商品が参照されている場合の商品のカタログ ID。それ以外の場合は空です。
`product_id` | `null,`&nbsp;`string` | 購入された商品の ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
`flow_response_json` | `null,`&nbsp;`string` | [PII] ユーザーが応答したフォームの値。ユーザーが WhatsApp フローに応答している場合に存在します。
`message_id` | `null,`&nbsp;`string` | このメッセージに対して Meta が生成した一意の ID
`in_reply_to` | `null,`&nbsp;`string` | このメッセージが返信しているメッセージの message_id
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED #USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルな一意の ID
`time` | `int` | イベントが発生した Unix タイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] 受信者の電話番号
`user_id` | `string` | このイベントを実行したユーザーの Braze ID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ユーザー ID
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | 購読グループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | このメッセージに対して Meta が生成した一意の ID
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
`device_id` | `null,`&nbsp;`string` | ユーザーが匿名の場合、このユーザーに紐づけられた `device_id`
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`from_phone_number` | `null,`&nbsp;`string` | WhatsApp メッセージの送信元電話番号
`app_group_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが属するワークスペースの API ID
`subscription_group_api_id` | `string` | 購読グループ API ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの内部使用 Braze ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンの API ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリエーションの API ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの内部使用 Braze ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスの API ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションの API ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップの API ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションの API ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチの ID
`message_extras` | `null,`&nbsp;`string` | [PII] Liquid レンダリング中にタグ付けされたキーと値のペアの JSON 文字列
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントが Snowpipe に取得された日時
`send_id` | `null,`&nbsp;`string` | このメッセージが属するメッセージ送信 ID
`flow_id` | `null,`&nbsp;`string` | WhatsApp Manager 内のフローの一意の ID。ユーザーが WhatsApp フローに応答している場合に存在します。
`template_name` | `null,`&nbsp;`string` | [PII] WhatsApp Manager 内のテンプレートの名前。テンプレートメッセージを送信する場合に存在します
`message_id` | `null,`&nbsp;`string` | このメッセージに対して Meta が生成した一意の ID
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPSENDSHARED #USERSMESSAGESWHATSAPPSENDSHARED" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

このイベントは、メッセージの優先度が下げられたり、フリークエンシーキャップが適用されたりした場合に発生し、設定されたリトライウィンドウ内で後から再試行されます。

フィールド | タイプ | 説明
------|------|------------
`id` | `string` | このイベントのグローバルに一意のID
`user_id` | `string` | [PII] このイベントを実行したユーザーのBrazeユーザーID
`external_user_id` | `null,`&nbsp;`string` | [PII] ユーザーの外部ID
`app_group_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループのBSON ID
`app_group_api_id` | `null,`&nbsp;`string` | このユーザーが所属するアプリグループのAPI ID
`time` | `int` | イベントが発生したUNIXタイムスタンプ
`to_phone_number` | `null,`&nbsp;`string` | [PII] メッセージを受信するユーザーのe.164形式の電話番号
`device_id` | `null,`&nbsp;`string` | イベントが発生したデバイスのID
`timezone` | `null,`&nbsp;`string` | ユーザーのタイムゾーン
`subscription_group_api_id` | `null,`&nbsp;`string` | 購読グループのAPI ID
`campaign_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのBSON ID
`campaign_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンペーンのAPI ID
`message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したメッセージバリアントのAPI ID
`canvas_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのBSON ID
`canvas_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスのAPI ID
`canvas_variation_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスバリエーションのAPI ID
`canvas_step_api_id` | `null,`&nbsp;`string` | このイベントが属するキャンバスステップのAPI ID
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | このユーザーが受信したキャンバスステップメッセージバリエーションのAPI ID
`dispatch_id` | `null,`&nbsp;`string` | このメッセージが属するディスパッチのID
`retry_type` | `null,`&nbsp;`string` | リトライのタイプ
`retry_log` | `null,`&nbsp;`string` | リトライの詳細を説明するログメッセージ
`sf_created_at` | `timestamp`,&nbsp;`null` | このイベントがSnowpipeによって取得された日時
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPRETRYSHARED #USERSMESSAGESWHATSAPPRETRYSHARED" }

## ユーザー {#users}

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| フィールド                    | タイプ                    | 説明                                                |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                  |
| `app_group_id`              | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID      |
| `app_group_api_id`          | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID       |
| `user_id`                   | `string`,&nbsp;`null`    | このイベントを実行したユーザーの Braze ID            |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] ユーザーの外部ユーザー ID                     |
| `time`                      | `int`,&nbsp;`null`       | イベントが発生した Unix タイムスタンプ               |
| `random_bucket_number`      | `int`,&nbsp;`null`       | ユーザーに割り当てられた現在のランダムバケット番号   |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | ユーザーに割り当てられた以前のランダムバケット番号   |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSRANDOMBUCKETNUMBERUPDATESHARED #USERSRANDOMBUCKETNUMBERUPDATESHARED" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| フィールド           | タイプ                    | 説明                                                          |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                             |
| `user_id`          | `string`,&nbsp;`null`    | 削除されたユーザーの Braze ID                                   |
| `app_group_id`     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                  |
| `time`             | `int`,&nbsp;`null`       | ユーザー削除リクエストが処理された Unix タイムスタンプ          |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERDELETEREQUESTSHARED #USERSUSERDELETEREQUESTSHARED" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| フィールド           | タイプ                    | 説明                                                                            |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | このイベントのグローバルに一意な ID                                              |
| `user_id`          | `string`,&nbsp;`null`    | 孤立したユーザーの Braze ID                                                      |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] ユーザーの外部ユーザー ID                                                 |
| `device_id`        | `string`,&nbsp;`null`    | このユーザーに紐付けられたデバイスの ID（匿名ユーザーの場合）                    |
| `app_group_id`     | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの Braze ID                                  |
| `app_group_api_id` | `string`,&nbsp;`null`    | このユーザーが所属するワークスペースの API ID                                   |
| `app_api_id`       | `string`,&nbsp;`null`    | 孤立したユーザーが所属していたアプリの API ID                                    |
| `time`             | `int`,&nbsp;`null`       | ユーザーが孤立した Unix タイムスタンプ                                           |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | 孤立したユーザーのプロファイルとマージされたユーザーの Braze ID                   |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | このイベントが Snowpipe によって取得された日時                                   |
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
`api_id` | `string` | キャンペーンメッセージバリエーションの API ID
`name` | `null,`&nbsp;`string` | キャンペーンメッセージバリエーションの名前
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