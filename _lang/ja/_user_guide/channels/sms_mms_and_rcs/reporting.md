---
nav_title: "レポート"
article_title: "レポート"
page_order: 21
description: "このリファレンス記事では、Brazeで使用されるSMS、MMS、RCSの指標と、SMS、MMS、RCSのキャンペーンでそれらを確認する方法について説明します。"
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

> このリファレンス記事では、Brazeで使用されるSMS、MMS、RCSの指標と、SMS、MMS、RCSのキャンペーンでそれらを確認する方法について説明します。

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

{% alert note %}
*合計クリック数*などのダッシュボードのクリック指標には、ボットアクティビティの疑いがあるものは含まれませんが、Currentsはデータウェアハウスでの照合のために、`is_suspected_bot_click`および`suspected_bot_click_reason`を含むすべてのクリックイベントをエクスポートします。影響を受けるダッシュボード指標、セグメンテーション、オーケストレーションについては、[SMS/RCSリンクのボットクリックフィルタリング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering)を参照してください。
{% endalert %}

## SMSのオプトインとオプトアウトのトラッキング {#track-sms-opt-ins-and-opt-outs}

以下の方法でSMSのオプトインとオプトアウトをトラッキングできます。

| 方法 | 説明 |
|--------|-------------|
| セグメンター | セグメンターは、特定の[購読グループ]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group)内のユーザー数を表示します。電話番号による重複排除は行われません。複数のユーザーが同じ電話番号を共有している場合、各インスタンスが個別にカウントされます。 |
| 購読グループの時系列 | メールと電話番号の購読に関する日次スナップショットを提供します。時系列では、購読、購読解除、再購読がカウントされます。たとえば、ユーザーが購読し、購読解除し、再度購読した場合、1人の購読ユーザーとしてカウントされます。 |
| Currents | Currentsを使用して[購読およびエンゲージメントイベント]({{site.baseurl}}/message_events_glossary)をエクスポートし、独自のレポートに活用できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSのオプトインとオプトアウトのトラッキング" }

{% alert note %}
**SMS/MMS/RCSパフォーマンス**パネルの_オプトイン_および_オプトアウト_の統計は、受信キーワードを通じてオプトインまたはオプトアウトしたユーザーを反映しています（たとえば、オプトインの場合は「START」、オプトアウトの場合は「STOP」とテキストを送信します）。これらの数値は通常、セグメンターに表示される数値よりも低くなります。これは、SMSに購読しているユーザーの総数ではなく、これらのキーワードがテキスト送信された回数をカウントしているためです。
{% endalert %}

### SMSキャンペーンのオプトアウトのトラッキング {#track-sms-campaign-opt-outs}

キャンペーンレベルでのSMSオプトアウトは、購読グループの状態変更テーブルではなく、受信テーブルを使用してトラッキングします。たとえば、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)またはデータウェアハウスで、`USERS_MESSAGES_SMS_INBOUNDRECEIVE`または[`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED)テーブルを参照するクエリを実行できます。

このクエリの例では`USERS_MESSAGES_SMS_INBOUNDRECEIVE`テーブルを参照しています。

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

このクエリは、指定されたワークスペースと購読グループのSMS通信からオプトアウトしたユーザーを返します。キャンペーンまたはキャンバスに関連付けられているユーザーのみにフィルタリングされます。

### オプトアウトのタイミング {#opt-out-timing}

Currentsまたはデータウェアハウスにおけるキーワードおよび受信メッセージイベント（[`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)のタイムスタンプや購読グループの状態変更イベントなど）は、Brazeがオプトアウトを記録した時刻の正式なソースです。

{% alert note %}
イベントのタイムスタンプは、Brazeが受信メッセージを受信または処理した時刻を反映しており、ユーザーがSMSを送信した時刻やキャリアまたはSMSプロバイダーが受信した時刻とは必ずしも一致しません。分析でオプトアウトをBrazeが受信オプトアウトパスを処理した時点として扱う場合、これらのタイムスタンプはその定義と一致します。
{% endalert %}

ユーザープロファイルには現在の購読状態が表示されますが、オプトアウトの処理時に[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)などを設定しない限り、単一の「SMS購読解除日時」フィールドは表示されない場合があります。

## SMS送信結果に適用される料金 {#charges-applied-to-sms-sending-outcomes}

この表はBrazeの課金を反映しており、プロバイダーの課金ではありません。Brazeから課金されない結果でも、プロバイダーから課金される場合があります。

| 結果 | 定義 | Brazeの課金 |
|--------|------------|--------|
| 送信済み | キャンペーンまたはキャンバスステップが起動またはトリガーされ、SMSペイロードがSMSプロバイダーに送信されました。 | 課金なし |
| 配信失敗 | SMSペイロードをSMSプロバイダーに送信できませんでした。これは、キューのオーバーフロー、アカウントの一時停止、またはメディアエラー（MMSの場合）が原因で発生する可能性があります。 | 課金なし |
| 配信済み | SMSプロバイダーが上流キャリアから（利用可能な場合は送信先デバイスからも）メッセージ配信の確認を受け取りました。 | 課金あり |
| 拒否 | SMSプロバイダーがメッセージが配信されなかったことを示す拒否レシートを受け取りました。これは、キャリアのコンテンツフィルタリングや送信先デバイスの利用可否など、さまざまな理由で発生する可能性があります。 | 課金あり |
| **Sends to Carrier** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 新しいダッシュボードでは非推奨です。一部のダッシュボードでは、この指標が**Sent to Carrier**と表示される場合があります。 | 個々のメッセージ送信結果に基づいて課金される場合があります |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS送信結果に適用される料金" }

{% alert note %}
**Sends to Carrier**は新しいダッシュボードでは非推奨です。現在のレポートには**Sent**、**Confirmed Delivery**、**Delivery Failed**、**Rejections**を使用してください。定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/analytics/metrics_glossary)を参照してください。
{% endalert %}

## RCSとSMSフォールバックのレポート {#rcs-and-sms-fallback-reporting}

RCS SMSフォールバックイベントの動作（`IS_SMS_FALLBACK=TRUE`を含む）については、[SMSフォールバックがイベントとセグメンテーションでどのように機能するか]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup#how-sms-fallback-works-with-events-and-segmentation)を参照してください。

{% alert note %}
ダッシュボードのキャンペーン分析とSnowflakeエクスポートでは、タイミングや集計がわずかに異なる場合があります。データウェアハウスでの照合を行う際に、指標がダッシュボードと正確に一致しない場合は、SnowflakeまたはCurrentsイベントストリームをより詳細なソースとして扱ってください。
{% endalert %}

## *拒否*をSnowflakeまたはCurrentsと照合する {#reconcile-rejections-with-snowflake-or-currents}

ダッシュボードの*拒否*指標は、ワークスペース全体の集計カウントです。行レベルのエクスポートではないため、各拒否をSnowflakeの単一の行や、Currentsの単一の`users.messages.sms.Rejection`イベントに常に一致させることはできません。たとえば、Brazeがデータウェアハウスエクスポート用の拒否処理を完了する前にユーザープロファイルが削除された場合、その拒否は`USERS_MESSAGES_SMS_REJECTION_SHARED`テーブルやCurrentsのペイロードには表示されませんが、SMSの集計レポートには結果が反映される場合があります。詳しくは、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles)およびCurrentsイベント用語集の[SMS拒否イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events)を参照してください。