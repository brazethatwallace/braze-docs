---
nav_title: ThoughtSpot
article_title: ThoughtSpot
description: "このリファレンス記事では、BrazeとThoughtSpotのパートナーシップについて説明します。ThoughtSpotは次世代の分析プラットフォームであり、ユーザーがBrazeのインタラクションデータ全体を無制限に検索し、実用的なインサイトを見つけることができます。"
alias: /partners/thoughtspot/
page_type: partner
search_tag: Partner

---

# ThoughtSpot

> [ThoughtSpot](https://www.thoughtspot.com/)は最新の分析クラウドであり、最新のデータスタックにライブ分析を提供する次世代分析プラットフォームです。同僚、パートナー、顧客がデータを実用的なインサイトに変える力を提供します。

BrazeとThoughtSpotの統合は、ThoughtSpot TMLブロックを活用し、会社ユーザーがワークシートやモデルの構築済みテンプレートを使ってユーザー行動分析を加速できるようにします。この統合により、ユーザーはBrazeのインタラクションデータを無制限に検索し、実用的なインサイトを見つけることができます。

## 前提条件 {#prerequisites}

BrazeでThoughtSpotの使用を開始するには、ThoughtSpotがデータに対してライブクエリを実行できるようにするために、そのデータをクラウドデータウェアハウスに送信する必要があります。

| 要件 | 説明 |
| ----------- | ----------- |
| ThoughtSpotアカウント | このパートナーシップを利用するにはThoughtSpotアカウントが必要です。 |
| クラウドデータウェアハウス | Brazeのデータは、Braze Currentsを使用してクラウドデータウェアハウスに保存されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## TMLブロック {#tml-blocks}

会社ユーザーは、すべてのデジタルインタラクションデータに簡単にアクセスし、検索することができます。当社のテンプレートにより、ユーザーはあらかじめ組み込まれたビジュアライゼーションやワークシートを使って、分析を素早くセットアップすることができます。検索、ドリルダウン、spotIQを使ってWebサイトの獲得とユーザー行動を分析できます。

## 統合 {#integration}

### ステップ 1: ThoughtSpotに接続する {#step-1-connect-thoughtspot}

ThoughtSpotインスタンスにログインし、Braze Currentsを使ってBrazeから取り込んだ各テーブルへのEmbrace接続を作成します。

#### ステップ 2: TMLをインポートする {#step-2-import-tml}

ThoughtSpotでワークシートとライブボードのzipファイルをインポートし、エラーなくインポートされたことを確認します。

インポートしたら、ライブボードの検索とカスタマイズを始めることができます。