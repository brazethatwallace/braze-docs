---
nav_title: Heap コホートインポート
article_title: Heap コホートインポート
description: "このリファレンス記事では、BrazeとHeapの統合について詳しく説明します。Heapはデジタルインサイトプラットフォームであり、HeapデータをBrazeにインポートしたり、ユーザーコホートを作成したり、BrazeデータをHeapにエクスポートしてセグメントを作成したりできます。"
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Heap コホートインポート {#heap-cohort-import}

> [Heap](https://heap.io/) はデジタルインサイトプラットフォームであり、デジタルエクスペリエンスにおいてビジネスに最も大きく影響する機会に集中して取り組むことができるようにし、フリクションを解消し、顧客を楽しませ、収益創出を加速させます。

BrazeとHeapの統合により、[HeapデータをBrazeにインポート](#data-import-integration)し、ユーザーコホートを作成し、[BrazeデータをHeapにエクスポート]({{site.baseurl}}/partners/data_and_analytics/analytics/heap)してセグメントを作成することができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Heapアカウント | このパートナーシップを利用するには、[Heap](https://heap.io/about) アカウントが必要です。 |
| Brazeデータインポートキー | これは、Brazeダッシュボードの**パートナー連携** > **テクノロジーパートナー**から**Heap**を選択することで取得できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
| Braze Currents | BrazeからHeapにデータをエクスポートするには、アカウントで[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)を有効にする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}
- ファネルを放棄したユーザーを再エンゲージする：ユーザーが購入または購読のファネルを放棄したときに、再エンゲージメントメッセージングをトリガーします。
- トライアル体験をパーソナライズする：トライアル体験におけるフリクションポイントを特定し、適切なタイミングでリマインダーを送信してトライアル中のユーザーを再エンゲージし、価値を見出す手助けをします。
- アナウンスやオファーへのエンゲージメントを高める：プロモーション、更新、新しいサービスのアナウンスを関連性のあるオーディエンスにターゲティングします。

## データインポート統合 {#data-import-integration}

HeapとBrazeの統合を使用して、Heapで定義されたコホートをBrazeに自動的に同期します。

### ステップ1：Brazeデータインポートキーを取得する {#step-1-get-the-braze-data-import-key}

Brazeで**パートナー連携** > **テクノロジーパートナー**に移動し、**Heap**を選択します。

このページでは、データインポートキーとRESTエンドポイントを確認できます。これらの両方の値をメモして、Heapアカウントマネージャーに提供し、統合の設定を完了してください。

![BrazeのHeapテクノロジーパートナーページ。データインポートキーとエンドポイントが表示されています。]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### ステップ2：Brazeでインポートされたユーザーをセグメント化する {#step-2-segment-imported-users-in-braze}

Brazeで**セグメント**に移動し、Heapコホートセグメントに名前を付け、フィルターとして**Heap Cohorts**を選択します。ここから、含めたいHeapコホートを選択できます。Heapコホートセグメントを作成したら、キャンペーンまたはキャンバスを作成するときにオーディエンスフィルターとして選択できます。

![Brazeのセグメントビルダーで、ユーザー属性フィルター「Heap cohort」が「次を含む」と「Heap Test Cohort」に設定されている。]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### この統合を使う {#using-this-integration}

Heapセグメントを使用するには、Brazeキャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてそのセグメントを選択します。

![Brazeキャンペーンビルダーのターゲティングステップで、「セグメントを基準にユーザーをターゲットに設定」フィルターが「Heap cohort」に設定されている。]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

## 統合の詳細 {#integration-details}

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクターのペイロード構造と同じです。これは、[カスタムHTTPコネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。

## ユーザーマッチング {#user-matching}

識別されたユーザーは、`external_id`または`alias`のどちらかによって照合できます。匿名ユーザーは、`device_id`によって照合できます。元々匿名ユーザーとして作成された識別済みユーザーは、`device_id`では識別できず、`external_id`または`alias`で識別する必要があります。