---
nav_title: Tealium for Currents
article_title: Tealium for Currents
page_order: 3
alias: /partners/tealium_for_currents/
description: "この参考記事では、Braze Currentsと、マーケティングスタックのソース間で情報を収集しルーティングする顧客データプラットフォームであるTealiumとのパートナーシップについて概説します。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Tealium for Currents

> [Tealium](https://www.tealium.com) は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまな場所に情報をルーティングする顧客データプラットフォームです。

BrazeとTealiumの統合により、2つのシステム間の情報の流れをシームレスにコントロールできます。Currentsを使用すると、データをTealiumに接続し、グローススタック全体で活用可能なデータにすることもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Tealium EventStream または Tealium AudienceStream | このパートナーシップを活用するには、[Tealiumアカウント](https://my.tealiumiq.com/)が必要です。 |
| Currents | Tealiumにデータをエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
| Tealium URL | Tealiumのダッシュボードに移動し、取り込みURLをコピーすることで取得できます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1: Tealium内にBraze用のデータソースを作成する {#step-1-create-a-data-source-for-braze-within-tealium}

データソースを作成する手順は、[Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/) サイトにあります。完了すると、TealiumからデータソースURLが提供されます。このURLをコピーして、次のステップで使用します。

### ステップ 2: Currentを作成する {#step-2-create-current}

Brazeで、**Currents** > **+ Create Current** > **Tealium Export** に移動します。統合名、連絡先メール、およびTealium URLを指定します。

次に、利用可能なイベントのリストから追跡するイベントを選択します。デフォルトでは、Tealiumに送信されるすべてのイベントにはユーザーの `external_user_id` が含まれます。ただし、**Include events from anonymous users** チェックボックスを選択すると、`external_user_id` を持たないイベントもTealiumに送信できます。

統合を設定した後、**Launch Current** を選択します。

{% alert important %}
Tealium URLを最新の状態に保つことが重要です。コネクタのURLが正しくない場合、Brazeはイベントを送信できません。これが**5日間**以上続く場合、コネクタのイベントはドロップされ、データは永続的に失われます。
{% endalert %}

## 統合の詳細 {#integration-details}

Brazeでは、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)にリストされているすべてのデータ（[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)イベントおよび[顧客行動]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)イベントのすべてのプロパティを含む）をTealiumにエクスポートできます。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクタのペイロード構造と同じです。これは、[カスタムHTTPコネクタのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。