---
nav_title: Blings
article_title: Blings
description: "このリファレンス記事では、BrazeとBlingsの連携について説明します。"
alias: /partners/blings/
page_type: partner
search_tag: Partner
---

# Blings

> [Blings](https://www.blings.io/) は、リアルタイムでインタラクティブなデータドリブン型の動画体験を、チャネルを横断して大規模に配信できる次世代パーソナライズド動画プラットフォームです。

_この連携はBlingsによって管理されています。_

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|-----------------|-----------------------------------------------------------------------------|
| Blingsアカウント | このパートナーシップを利用するには、Blingsアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ 1: BlingsのHTMLスニペットを取得する {#step-1-obtain-your-blings-html-snippet}

{% tabs %}
{% tab Blings business and free plans %}

#### Blingsビジネスプランおよびフリープラン {#blings-business-and-free-plans}

BlingsアプリでHTMLスニペットを直接見つけてコピーします。

1. 選択したMP5プロジェクトの**接続**タブに移動します。
2. Blingsの**接続**ページで、対応する変数にBraze Liquidタグを追加します。タグによってHTMLスニペット内の値がダイナミックに入力されます。

![BlingsのHTMLスニペット。]({% image_buster /assets/img/blings/blings_connect_audience.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Blings Enterprise plan %}

#### Blingsエンタープライズプラン {#blings-enterprise-plan}

Blingsの担当者にHTMLスニペットをリクエストしてください。

{% endtab %}
{% endtabs %}

### ステップ 2: Brazeでキャンペーンを作成する {#step-2-create-a-braze-campaign}

Brazeで新しいメールまたはアプリ内メッセージのキャンペーンを作成し、BlingsのHTMLスニペットを挿入します。エディター内プレビューを使用して、パーソナライズされたフィールドとCreative Suiteのダイナミックなコンテンツが期待どおりに表示されることを確認します。

### ステップ 3: テストして起動する {#step-3-test-and-launch}

Brazeでキャンペーンをプレビューし、パーソナライズされたフィールドが正しく入力されていることを確認します。その後、MP5 キャンペーンを大規模に展開します。

![Braze Blingsプレビュー。]({% image_buster /assets/img/blings/blings_braze_preview.png %}){: style="max-width:70%;"}

## サポートを受ける {#getting-support}

ご質問やスニペットのリクエストについては、[support@blings.io](mailto:support@blings.io) でBlingsにお問い合わせいただくか、[Blingsヘルプセンター](https://blings.gitbook.io/blings-knowledge-base/documentation)を参照してください。