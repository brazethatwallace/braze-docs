---
nav_title: MetaRouter
article_title: MetaRouter
description: "MetaRouterを使用して、Brazeでの顧客データ管理を強化します。この高パフォーマンスなサーバーサイドタグ管理ソリューションは、MetaRouterがホストするプライベートクラウドでもお客様のインフラでも、シームレスなデプロイオプションによって最大限のコンプライアンスと制御を提供します。"
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) は、強力なサーバーサイドタグ管理プラットフォームとしてシームレスに統合することで、Brazeエクスペリエンスを向上させます。これにより、最大30%強化される信頼性の高い完全なファーストパーティデータ収集から、パーソナライズされたジャーニーのためのリアルタイムイベントストリームアクティベーションまで、Braze内で完全な顧客データジャーニーをオーケストレーションできます。さらにMetaRouterは、Brazeタグやその他のサードパーティタグの必要性を排除することで実装を効率化し、Brazeに流入するデータをパラメーター単位できめ細かく制御できるようにします。

_この統合はMetarouterによって管理されています。_

## サポートされている機能 {#supported-features}

- リトライを組み込むことができます。
- リクエストはバッチ処理されます。
- レート制限の問題はリトライで処理されます。
- external IDとPIIがサポートされています。MetaRouterは匿名IDと、クライアントが必要とするPII（メール、電話番号、名前）を渡します。
- Brazeの購入データやカスタムイベントデータを送信できます。
  - イベントプロパティがサポートされています。
  - ネストされたイベントプロパティはサポートされていません。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| MetaRouterアカウント | [MetaRouter Enterpriseアカウント](https://enterprise.metarouter.io/)。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。作成するには、**設定** > **API キー** に移動します。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MetaRouterのセットアップ {#setting-up-metarouter}

Brazeとの統合用にMetaRouterをセットアップするには、以下の手順に従います。

1. MetaRouterにアクセスし、新しいクラスターを作成します。
2. トラッキングしたいイベントを選択します。
3. MetaRouter SDKをインストールし、Webサイトにイベントを統合します。
4. クラスターをWebサイトのUIに接続します。
5. 新しいパイプラインを作成します。
6. WebサイトがMetaRouterにイベントを送信していることを確認します。

## Brazeの統合 {#integrating-braze}

### ステップ1:Braze統合を追加する {#step-1-add-the-braze-integration}

Enterprise MetaRouterで、**Integrations** > **New Integration** > **Braze** を選択し、統合に名前を付けます。次に、インスタンスURLとAPIキーを入力し、**Apply Changes** を選択します。

![MetaRouterでBrazeを統合として追加する画面。]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### ステップ2:イベントマッピングを追加する {#step-2-add-event-mapping}

各IDアウトプットにイベントマッピングを追加し、Brazeに送信したいイベントを設定します。完了したら、**Save as New Revision** を選択します。

![各IDアウトプットにイベントマッピングを追加する画面。]({% image_buster /assets/img/metarouter/img2.png %})