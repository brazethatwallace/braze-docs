---
nav_title: "レポート"
article_title: "レポート"
page_order: 21
description: "このリファレンス記事では、Brazeで使用されるSMS、MMS、RCSの指標と、SMS、MMS、RCSのCampaignsでそれらを確認する方法について説明します。"
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS

---

# SMS、MMS、RCSのレポート {#reporting-for-sms-mms-and-rcs}

> このリファレンス記事では、Brazeで使用されるSMS、MMS、RCSの指標と、SMS、MMS、RCSのCampaignsでそれらを確認する方法について説明します。

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

## SMSのオプトインとオプトアウトを追跡する {#track-sms-opt-ins-and-opt-outs}

SMSのオプトインとオプトアウトは、以下の方法で追跡できます。

| 方法 | 説明 |
|--------|-------------|
| セグメンター | セグメンターは、特定の[サブスクリプショングループ]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group)のユーザー数を表示します。電話番号による重複排除は行われません。複数のユーザーが同じ電話番号を共有している場合、各インスタンスが個別にカウントされます。 |
| サブスクリプショングループの時系列 | メールと電話番号のサブスクリプションの日次スナップショットを提供します。時系列では、サブスクリプション、配信停止、再サブスクリプションがカウントされます。たとえば、あるユーザーがサブスクリプション登録し、配信停止し、再度サブスクリプション登録した場合、そのユーザーは1人の購読中ユーザーとしてカウントされます。 |
| Currents | Currentsを使用して、独自のレポート用に[サブスクリプションおよびエンゲージメントイベント]({{site.baseurl}}/message_events_glossary)をエクスポートします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSのオプトインとオプトアウトを追跡する" }

{% alert note %}
**SMS/MMS/RCSパフォーマンス**パネルの_オプトイン_と_オプトアウト_の統計は、受信キーワードによるオプトインまたはオプトアウト（たとえば、オプトインの場合は「START」、オプトアウトの場合は「STOP」とテキスト送信）を反映しています。これらの数値は通常、セグメンターに表示される数値よりも低くなります。これは、SMSに購読しているユーザーの合計数ではなく、これらのキーワードがテキスト送信された回数をカウントしているためです。
{% endalert %}

### SMSキャンペーンのオプトアウトを追跡する {#track-sms-campaign-opt-outs}

キャンペーンレベルでのSMSオプトアウトを追跡するには、サブスクリプショングループの状態変更テーブルではなく、受信テーブルを使用します。たとえば、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/query_builder)やデータウェアハウスで、`USERS_MESSAGES_SMS_INBOUNDRECEIVE` または [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) テーブルを参照するクエリを実行できます。

以下のクエリ例は `USERS_MESSAGES_SMS_INBOUNDRECEIVE` テーブルを参照しています。

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

これにより、指定されたワークスペースとサブスクリプショングループのSMS通信をオプトアウトしたユーザーが返されます。CampaignsまたはCanvasesに関連付けられたユーザーにフィルタリングされています。

### オプトアウトのタイミング {#opt-out-timing}

Currentsまたはデータウェアハウスにおけるキーワードおよび受信メッセージイベント（[`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)のタイムスタンプやサブスクリプショングループの状態変更イベントなど）は、Brazeがオプトアウトを記録した時刻の正式なソースです。

{% alert note %}
イベントのタイムスタンプは、Brazeが受信メッセージを受信または処理した時刻を反映しており、ユーザーがSMSを送信した時刻や、キャリアまたはSMSプロバイダーがそれを受信した時刻とは必ずしも一致しません。分析でオプトアウトをBrazeが受信オプトアウトパスを処理した時点として扱う場合、これらのタイムスタンプはその定義に一致します。
{% endalert %}

ユーザープロファイルには現在のサブスクリプション状態が表示されますが、オプトアウトの処理時に[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes)などを設定しない限り、単一の「SMS配信停止日時」フィールドは表示されない場合があります。

## SMS送信結果に適用される料金 {#charges-applied-to-sms-sending-outcomes}

このテーブルはBrazeの課金を反映しており、プロバイダーの課金ではありません。Brazeが課金しない結果でも、プロバイダーによって課金される場合があります。

| 結果 | 定義 | Brazeによる課金 |
|--------|------------|--------|
| 送信済み | CampaignまたはCanvasステップが起動またはトリガーされ、SMSペイロードがSMSプロバイダーに送信されました。 | 課金なし |
| 配信失敗 | SMSペイロードをSMSプロバイダーに送信できませんでした。これは、キューのオーバーフロー、アカウントの停止、またはメディアエラー（MMSの場合）が原因で発生する可能性があります。 | 課金なし |
| 配信済み | SMSプロバイダーが上流キャリアから（利用可能な場合は送信先デバイスからも）メッセージ配信の確認を受信しました。 | 課金あり |
| 拒否 | SMSプロバイダーが、メッセージが配信されなかったことを示す拒否レシートを受信しました。これは、キャリアのコンテンツフィルタリングや送信先デバイスの利用可否など、いくつかの理由で発生する可能性があります。 | 課金あり |
| キャリアに送信済み | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} | 個々のメッセージ送信結果に基づいて課金される場合があります |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS送信結果に適用される料金" }

## *拒否*をSnowflakeまたはCurrentsと照合する {#reconcile-rejections-with-snowflake-or-currents}

ダッシュボードの*拒否*指標は、ワークスペース全体の集計カウントです。行レベルのエクスポートではないため、各拒否をSnowflakeの単一の行や、Currentsの単一の `users.messages.sms.Rejection` イベントと常に一致させることはできません。たとえば、Brazeがデータウェアハウスエクスポート用の拒否処理を完了する前にユーザープロファイルが削除された場合、その拒否は `USERS_MESSAGES_SMS_REJECTION_SHARED` テーブルやCurrentsペイロードには表示されませんが、集計SMSレポートには結果が反映される場合があります。詳しくは、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles)およびCurrentsイベント用語集の[SMS拒否イベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#sms-rejection-events)を参照してください。