---
nav_title: Segmentと Currents
article_title: Segmentと Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "このリファレンス記事では、Braze Currentsと Segmentの連携について概説します。Segmentは、マーケティングスタック内のソース間で情報を収集しルーティングする顧客データプラットフォームです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Segmentと Currents {#segment-for-currents}

> [Segment](https://segment.com) は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。このリファレンス記事では、Braze Currentsと Segmentの接続について概要を説明し、適切な実装と使用のための要件とプロセスを紹介します。

Braze と Segmentの統合により、Braze Currentsを利用して Brazeイベントを Segment にエクスポートし、コンバージョン、リテンション、製品使用率に関するより詳細な分析を行うことができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Segment アカウント | このパートナーシップを活用するには、[Segment アカウント](https://app.segment.com/login)が必要です。 |
| Braze の送信先 | Segmentの統合で、すでに [Braze を送信先として設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)しておく必要があります。<br><br>これには、[接続設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)で正しい Braze データセンターと REST APIキーを提供することも含まれます。 |
| Currents | Segment にデータをエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

### ステップ1:Segment ライトキーの取得 {#step-1-obtain-segment-write-key}

Segment ダッシュボードで、Segment ソースを選択します。次に、**Settings > API keys** に移動します。ここで **Segment Write Key** を確認します。

{% alert warning %}
Segment Write Key を最新の状態に保つことが重要です。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。これが **5日間** 以上続くと、コネクターのイベントはドロップされ、データは永久に失われます。
{% endalert %}

### ステップ2:新しい Currents コネクターを作成する {#step-2-create-a-new-currents-connector}

1. Braze で、**Partner Integrations** > **Data Export** に移動します。
2. **+ Create New Current** > **Segment Data Export** をクリックします。
3. 次に、統合名、連絡先メール、Segment Write Key、および Segment リージョンを指定します。

![Braze の Segment Currents ページ。統合名、連絡先メール、Segment リージョン、APIキーのフィールドがあります。]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### ステップ3:メッセージエンゲージメントイベントをエクスポートする {#step-3-export-message-engagement-events}

次に、エクスポートするメッセージエンゲージメントイベントを選択します。以下のエクスポートイベントおよびプロパティテーブルを参照してください。Segment に送信されるすべてのイベントには、ユーザーの `external_user_id` が `userId` として、ユーザーの `braze_id` が `anonymousId` として含まれます。

Braze は、**Include events from anonymous users** にチェックが入っている場合にのみ、`external_user_id` を持たないユーザーのイベントデータを送信する点にご注意ください。

{% multi_lang_include early_access_beta_alert.md feature='Anonymous user export' %}

![Braze の Segment Currents ページで利用可能なすべてのメッセージエンゲージメントイベントのリスト。]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

最後に **Launch Current** を選択します。

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

詳細については、Segmentの[ドキュメント](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/)を参照してください。

## Currentsの更新 {#updating-your-current}

{% multi_lang_include updating_currents.md %}

## サポートされている Currents イベント {#supported-currents-events}

Braze は、Currentsの[ユーザー動作]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)イベント用語集にリストされている以下のデータを Segment にエクスポートできます。

### 動作 {#behaviors}
- アンインストール: `users.behaviors.Uninstall`
- サブスクリプション（グローバル状態の変更）: `users.behaviors.subscription.GlobalStateChange`
- サブスクリプショングループ（状態の変更）: `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- 中止: `users_campaigns_abort`
- コンバージョン: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`

### Canvas
- 中止: `users_canvas_abort`
- コンバージョン: `users.canvas.Conversion`
- エントリ: `users.canvas.Entry`
- 離脱（オーディエンス照合、実行済みイベント）
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- 実験ステップ（コンバージョン、分割エントリ）
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### メッセージ {#messages}
- コンテンツカード（中止、クリック、却下、インプレッション、送信）
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- メール（中止、バウンス、クリック、配信、スパムとしてマーク、開封、送信、ソフトバウンス、配信停止）
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- アプリ内メッセージ（中止、クリック、インプレッション）
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- プッシュ通知（中止、バウンス、iOSforeground、開封、送信）
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS（中止、キャリア送信、配信、配信失敗、受信、拒否、送信、ショートリンククリック）
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook（中止、送信）
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp（中止、配信、失敗、受信、既読、送信）
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`