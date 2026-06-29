---
nav_title: セグメントと Currents
article_title: セグメントと Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "このリファレンス記事では、Braze Currentsとセグメントの連携について概説します。セグメントは、マーケティングスタック内のソース間で情報を収集しルーティングする顧客データプラットフォームです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# セグメントと Currents {#segment-for-currents}

> [セグメント](https://segment.com) は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。このリファレンス記事では、Braze Currentsとセグメントの接続について概要を説明し、適切な実装と使用のための要件とプロセスを紹介します。

Brazeとセグメントの統合により、Braze Currentsを利用してBrazeイベントをセグメントにエクスポートし、コンバージョン、リテンション、製品使用率に関するより詳細な分析を行うことができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメントアカウント | このパートナーシップを活用するには、[セグメントアカウント](https://app.segment.com/login)が必要です。 |
| Brazeの送信先 | セグメントの統合で、すでに[Brazeを送信先として設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)しておく必要があります。<br><br>これには、[接続設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)で正しいBrazeデータセンターとREST APIキーを提供することも含まれます。 |
| Currents | セグメントにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1:セグメントライトキーの取得 {#step-1-obtain-segment-write-key}

セグメントダッシュボードで、セグメントソースを選択します。次に、**Settings > API keys** に移動します。ここで **セグメント Write Key** を確認します。

{% alert warning %}
セグメント Write Keyを最新の状態に保つことが重要です。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。これが**5日間**以上続くと、コネクターのイベントはドロップされ、データは永久に失われます。
{% endalert %}

### ステップ2:新しいCurrentsコネクターを作成する {#step-2-create-a-new-currents-connector}

1. Brazeで、**Partner Integrations** > **Data Export** に移動します。
2. **+ Create New Current** > **セグメント Data Export** をクリックします。
3. 次に、統合名、連絡先メール、セグメント Write Key、およびセグメントリージョンを指定します。

![Brazeのセグメント Currentsページ。統合名、連絡先メール、セグメントリージョン、APIキーのフィールドがあります。]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### ステップ3:メッセージエンゲージメントイベントをエクスポートする {#step-3-export-message-engagement-events}

次に、エクスポートするメッセージエンゲージメントイベントを選択します。以下のエクスポートイベントおよびプロパティテーブルを参照してください。セグメントに送信されるすべてのイベントには、ユーザーの`external_user_id`が`userId`として、ユーザーの`braze_id`が`anonymousId`として含まれます。

Brazeは、**Include events from anonymous users** にチェックが入っている場合にのみ、`external_user_id`を持たないユーザーのイベントデータを送信する点にご注意ください。

{% multi_lang_include alerts/early_access_beta_alert.md feature='Anonymous user export' %}

![Brazeのセグメント Currentsページで利用可能なすべてのメッセージエンゲージメントイベントのリスト。]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

最後に **Launch Current** を選択します。

{% multi_lang_include alerts/warning_alerts.md alert='セグメント Currents multiple connectors' %}

詳細については、セグメントの[ドキュメント](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/)を参照してください。

## Currentsの更新 {#updating-your-current}

{% multi_lang_include currents/updating_currents.md %}

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeは以下のイベントをセグメントにエクスポートできます。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

各イベントのペイロード構造については、[メッセージエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)および[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)の **セグメント** タブを選択してください。