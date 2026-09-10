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

## SMSのオプトインとオプトアウトをトラッキングする {#track-sms-opt-ins-and-opt-outs}

SMSのオプトインとオプトアウトは、以下の方法でトラッキングできます。

| 方法 | 説明 |
|--------|-------------|
| セグメンター | セグメンターは、特定の[購読グループ]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group)に含まれるユーザー数を表示します。電話番号による重複排除は行われません。複数のユーザーが同じ電話番号を共有している場合、各インスタンスが個別にカウントされます。 |
| 購読グループの時系列 | メールと電話番号の購読に関する日次スナップショットを提供します。時系列では、購読、購読解除、再購読がカウントされます。たとえば、あるユーザーが購読し、購読解除し、再度購読した場合、そのユーザーは購読済みユーザー1人としてカウントされます。 |
| Currents | Currentsを使用して、[購読およびエンゲージメントイベント]({{site.baseurl}}/message_events_glossary)を独自のレポート用にエクスポートできます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSのオプトインとオプトアウトのトラッキング" }

{% alert note %}
**SMS/MMS/RCSパフォーマンス**パネルの_オプトイン_および_オプトアウト_の統計は、受信キーワードを通じてオプトインまたはオプトアウトしたユーザーを反映しています（たとえば、オプトインの場合は「START」、オプトアウトの場合は「STOP」をテキスト送信）。これらの数値は通常、セグメンターに表示される数値よりも低くなります。これは、SMSに購読しているユーザーの合計数ではなく、これらのキーワードがテキスト送信された回数をカウントしているためです。
{% endalert %}

### SMSキャンペーンのオプトアウトをトラッキングする {#track-sms-campaign-opt-outs}

SMSのオプトアウトをキャンペーンレベルでトラッキングするには、購読グループのステート変更テーブルではなく、受信メッセージテーブルを使用します。たとえば、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)またはデータウェアハウスで、`USERS_MESSAGES_SMS_INBOUNDRECEIVE`テーブルまたは[`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED)テーブルを参照するクエリを実行できます。

以下のクエリ例では、`USERS_MESSAGES_SMS_INBOUNDRECEIVE`テーブルを参照しています。

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

このクエリは、指定されたワークスペースと購読グループのSMS通信からオプトアウトし、キャンペーンまたはキャンバスに関連付けられているユーザーを返します。

### オプトアウトのタイミング {#opt-out-timing}

Currentsまたはデータウェアハウスのキーワードおよび受信メッセージイベント（[`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events)のタイムスタンプや購読グループのステート変更イベントなど）は、Brazeがオプトアウトを記録した時点に関する信頼性の高いソースです。

{% alert note %}
イベントのタイムスタンプは、Brazeが受信メッセージを受信または処理した時点を反映しており、ユーザーがSMSを送信した時点やキャリアまたはSMSプロバイダーが受信した時点とは限りません。オプトアウトをBrazeが受信オプトアウトパスを処理した時点として分析に使用する場合、これらのタイムスタンプはその定義に一致します。
{% endalert %}

ユーザープロファイルには現在の購読ステートが表示されますが、オプトアウトの処理時に[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)などを設定しない限り、「SMS購読解除日時」のような単一のフィールドは表示されない場合があります。

## SMS送信結果に適用される料金 {#charges-applied-to-sms-sending-outcomes}

この表はBrazeの課金を反映しており、プロバイダーの課金ではありません。Brazeが課金しない結果であっても、プロバイダーが課金する場合があります。

| 結果 | 定義 | Brazeによる課金 |
|--------|------------|--------|
| 送信済み | キャンペーンまたはキャンバスステップが起動またはトリガーされ、SMSペイロードがSMSプロバイダーに送信されました。 | 課金なし |
| 配信失敗 | SMSペイロードをSMSプロバイダーに送信できませんでした。キューのオーバーフロー、アカウントの停止、メディアエラー（MMSの場合）などが原因で発生することがあります。 | 課金なし |
| 配信済み | SMSプロバイダーが上流キャリアから（利用可能な場合は宛先デバイスからも）メッセージ配信の確認を受信しました。 | 課金あり |
| 拒否 | SMSプロバイダーがメッセージが配信されなかったことを示す拒否レシートを受信しました。キャリアのコンテンツフィルタリングや宛先デバイスの利用可否など、さまざまな理由で発生する可能性があります。 | 課金あり |
| **Sends to Carrier** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 新しいダッシュボードでは非推奨です。一部のダッシュボードでは、この指標が**Sent to Carrier**と表示される場合があります。 | 個々のメッセージ送信結果に基づいて課金される場合があります |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS送信結果に適用される料金" }

{% alert note %}
**Sends to Carrier**は新しいダッシュボードでは非推奨です。現在のレポートには**Sent**、**Confirmed Delivery**、**Delivery Failed**、**Rejections**を使用してください。定義については、[レポート指標用語集]({{site.baseurl}}/user_guide/analytics/metrics_glossary)を参照してください。
{% endalert %}

## RCSカードメッセージのレポート {#rcs-card-message-reporting}

RCSカードメッセージの場合、キャンペーンおよびキャンバスの分析における*合計クリック数*には、カードボタンのタップ（**メッセージ返信**や**URLを開く**など）およびサジェスションのインタラクションが含まれます。ユーザーが同じコントロールを複数回タップした場合、この指標は複数回カウントされることがあります。

カードボタンおよびサジェスションのクリックは、[リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)や短縮URLの高度なトラッキング設定では追跡されません。短縮SMSリンクを参照する[ユーザーリターゲティング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links)フィルターは、カードボタンのインタラクションには適用されません。

ユーザーレベルのインタラクションデータについては、Currentsを通じて[RCSクリックイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#rcs-click-events)（`users.messages.rcs.Click`）をエクスポートしてください。これらのイベントには、ボタンタップとサジェスションを区別するための`interaction_type`や`element_type`などのフィールドが含まれています。

## RCSとSMSフォールバックのレポート {#rcs-and-sms-fallback-reporting}

RCS SMSフォールバックイベントの動作（`IS_SMS_FALLBACK=TRUE`を含む）については、[SMSフォールバックがイベントとセグメンテーションでどのように機能するか]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup#how-sms-fallback-works-with-events-and-segmentation)を参照してください。

{% alert note %}
ダッシュボードのキャンペーン分析とSnowflakeエクスポートでは、タイミングや集計方法がわずかに異なる場合があります。データウェアハウスでの照合を行う際、指標がダッシュボードと正確に一致しない場合は、SnowflakeまたはCurrentsイベントストリームをより詳細なソースとして扱ってください。
{% endalert %}

## *拒否*をSnowflakeまたはCurrentsと照合する {#reconcile-rejections-with-snowflake-or-currents}

ダッシュボードの*拒否*指標は、ワークスペース全体の集計カウントです。行レベルのエクスポートではないため、各拒否をSnowflakeの1行やCurrentsの1つの`users.messages.sms.Rejection`イベントに常に一致させることはできません。たとえば、Brazeがデータウェアハウスエクスポート用の拒否処理を完了する前にユーザープロファイルが削除された場合、その拒否は`USERS_MESSAGES_SMS_REJECTION_SHARED`テーブルやCurrentsのペイロードに表示されませんが、集計SMSレポートには結果が反映されることがあります。詳しくは、[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles)およびCurrentsイベント用語集の[SMS拒否イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events)を参照してください。