---
nav_title: Hightouch
article_title: Hightouch
description: "このリファレンス記事では、BrazeとHightouchのパートナーシップについて説明します。Hightouchは、ウェアハウスの顧客データをビジネスツールに同期するプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) は最新のデータ統合プラットフォームであり、ITチームやエンジニアリングチームの支援を必要とせずに、ウェアハウスやデータレイクからお客様が選択したアプリに、顧客データ、製品データ、または独自のデータを同期できます。

BrazeとHightouchの統合により、データウェアハウスの最新の顧客データを使用して、Brazeでより優れたキャンペーンを作成できます。顧客データをBrazeに自動的に同期させることで、データの整合性を心配する必要がなくなり、世界レベルのカスタマーエクスペリエンスの構築に集中して取り組むことができます。

この統合により、[ユーザーコホートをBrazeにインポート]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/)し、ウェアハウスにしか存在しないデータに基づいてターゲットを絞ったキャンペーンを送信することもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Hightouchアカウント | このパートナーシップを活用するには、Hightouchアカウントが必要です。
| Braze REST APIキー | `users.track` および `users.export.ids` の権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)に応じて異なります。<br><br>Hightouchには、Brazeインスタンスが配置されているクラスターの名前が必要です。例えば、Brazeのエンドポイントが `https://rest.iad-01.braze.com` の場合、必要なのは `iad-01` だけです。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

* ユーザーとアカウントに関するデータをBrazeに同期し、高度にパーソナライズされたキャンペーンを構築します。
* Brazeのセグメントをウェアハウスからの最新データで自動的に更新します。
* 他の顧客タッチポイントからのデータをBrazeに取り込むことで、より良い体験を提供します。
* ユーザーのコホートをBrazeにインポートし、ターゲットを絞ったキャンペーンやキャンバスを送信できます。

## 統合 {#integration}

### ステップ1:Hightouch Braze送信先を作成する {#step-1-create-your-hightouch-braze-destination}

1. Hightouchプラットフォームの**Destinations**セクションで**Add destination**をクリックします。
2. 利用可能な送信先のリストから**Braze**を選択します。
3. Braze RESTエンドポイント（「https://rest.」を除く）とBraze REST APIキーを指定します。<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### ステップ2:オブジェクトとイベントの同期 {#step-2-object-and-event-syncing}

Hightouchでは、ユーザーオブジェクトとイベントの両方への同期がサポートされています。

| 送信先 | 説明 | サポートされているモード |
|---|---|---|
| オブジェクト | 送信先のユーザーや組織などのオブジェクトにレコードを同期します。| アップサートまたはアップデート |
| イベント | レコードをイベントとして送信先に同期します。これは多くの場合、トラックコールの形式です。 | イベントまたは購入の追跡 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Object and event syncing" }

{% alert note %}
同期がデータポイントの記録方法にどのように影響するかについては、[Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption)を参照してください。
{% endalert %}

#### Brazeオブジェクトを同期する {#syncing-braze-objects}

Hightouchオブジェクト（ユーザーフィールド）を同等のBrazeデフォルトまたはカスタムフィールドに同期できます。2つのプラットフォーム間でデータを統合するためにレコードマッチングを実行することもできます。

#### Brazeイベントを同期する {#syncing-braze-events}

Hightouchでは、イベントデータと購入データを追跡し、これらのデータをBrazeに同期できます。Hightouchでは、トラッキングデータの設定や存在しないユーザー動作の定義など、同期動作に影響を与えるいくつかのオプションを設定できます。

{% alert important %}
オブジェクトとイベントの同期に関する詳細な手順については、[Hightouchのドキュメント](https://hightouch.io/docs/destinations/braze/)を参照してください。
{% endalert %}



## 統合デモ {#integration-demo}

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" title="Hightouch integration demo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>