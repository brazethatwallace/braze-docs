---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "BrazeとAlpacoの統合により、ブランドに準拠したLiquid互換のメールテンプレートとコンテンツブロックをBrazeにエクスポートし、メールやアプリ内メッセージで使用できるようになります。"
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/)は、Braze用の再利用可能でブランドセーフなコンテンツを構築するためのドラッグアンドドロップエディターを提供するオンラインクリエイティブ管理ツールです。AlpacoとBrazeの統合により、Content Blocks、メールテンプレート、およびアプリ内メッセージテンプレートをエクスポートできます。

_この統合はAlpacoによって管理されています。_

{% alert note %}
Alpacoは[完全なLiquid](https://shopify.github.io/liquid/)変数をサポートしており、Brazeの設定で使用されるすべてのLiquid変数も完全にサポートしています。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ------------| ----------- |
| Alpacoアカウント | このパートナーシップを活用するには、Alpacoアカウントが必要です。 |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| クラスターインスタンス | Brazeの[クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、BrazeダッシュボードとRESTエンドポイントに対応しています。<br><br> たとえば、ダッシュボードのURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

- 完全にデザインされた**メールテンプレート**をエクスポートして、Brazeのキャンペーンやトランザクションメッセージングで使用します。
- 複数のチャネルで再利用可能な**モジュラーコンテンツブロック**（ヘッダー、フッター、プロモーションなど）を作成・管理します。
- メールと同じクリエイティブな柔軟性で魅力的な**アプリ内メッセージ**をデザインし、チャネル間で一貫性のあるオンブランド体験を簡単に提供できるようにします。
- `{{first_name}}`や`{{custom_attribute}}`などのBraze対応Liquidタグを含めることで、**パーソナライゼーション**を実現します。
- Alpacoでクリエイティブデザインを一元管理し、1回のエクスポートでBrazeに更新をプッシュすることで、**ブランドの一貫性**を維持します。

## 統合 {#integration}

Braze REST APIキーとクラスターインスタンスをAlpacoカスタマーサクセスチームに提供してください。チームが初期統合のセットアップを行います。

{% alert note %}
これは1回限りのセットアップであり、今後のエクスポートではこのAPIキーが自動的に使用されます。
{% endalert %}

## AlpacoメッセージをBrazeにエクスポートする {#exporting-alpaco-messages-to-braze}

### ステップ 1:Alpacoでテンプレートを作成する {#step-1-create-a-template-in-alpaco}

Alpacoで、ブランドアイデンティティを表現するテンプレートを作成します。準備ができたら、**Save**を選択します。

![Alpacoのテンプレート作成画面]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### ステップ 2:テンプレートを使用してメッセージを作成する {#step-2-draft-a-message-using-the-template}

次に、Alpacoロビーに移動し、テンプレートを使用してメール、アプリ内メッセージ、またはコンテンツブロックを作成します。エクスポート前にメッセージを確認するには、**Review**を選択します。

![Alpacoのメール作成画面]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### ステップ 3:メッセージをBrazeにエクスポートする {#step-3-export-your-message-to-braze}

**Export**を選択し、Braze統合を選択して、メールテンプレートまたはコンテンツブロックのどちらをエクスポートするかを指定します。

エクスポート後に変更を加えた場合は、Alpacoからコンテンツを再エクスポートしてBrazeで更新できます。

![Alpacoのメールエクスポート画面]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## BrazeでAlpacoテンプレートとブロックを使用する {#using-alpaco-templates-and-blocks-in-braze}

エクスポートするコンテンツのタイプに応じて、テンプレートは次のいずれかのセクションに表示されます。

- **テンプレートとメディア > メールテンプレート**
- **テンプレートとメディア > Content Blocks**

Alpacoテンプレートは、ブランドの一貫性を一元的に管理したい組織に最適です。また、簡単な分類とコンテンツ管理のために、Brazeの組み込みタグもサポートしています。