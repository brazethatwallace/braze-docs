---
nav_title: 用語集
article_title: 用語集のレイアウト
page_order: 0
noindex: true
---

# レイアウト例：用語集 {#example-layout-glossary}

> 用語集のレイアウトはYAMLで記述します。いくつかのコンポーネントとパラメーターが必要です。用語集レイアウトは、辞書や特定のカテゴリーのコンテンツなど、ローカライズされた検索可能なコンテンツに適しています。

## 必要なコンポーネント {#required-components}

1. YAMLの開始表記と終了表記。つまり、コンテンツの前に`---`、後に`---`を記述します。
2. 特定のパラメーターの内容を引用符で囲みます。（ヘッダーパラメーター、テキストパラメーター、ハイフンやその他の特殊文字を含むコンテンツ）
3. 用語集タグの表記（これらはフィルタータグです）

## 必須パラメーター {#required-parameters}

| パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
| `page_order` | 数値 | セクション内でページを順番に並べます。この順序は左側のナビゲーションに反映されます。 |
| `nav-title` | 英数字 | 左側のナビゲーションに表示されるタイトルです。 |
| `layout` | 英数字 - スペースなし | ドキュメントの[レイアウトセクション](https://github.com/Appboy/braze-docs/tree/develop/_layouts)からレイアウトを選択します。 |
| `glossary_top_header` | 英数字 | 二重引用符が必要です。タイトルはページ上部に表示されます。 |
| `glossary_top_text` | 文字列、英数字 | 用語集ページについて説明します。これは検索バーとフィルター（選択した場合）の上に表示されます。基本的にHTMLで記述するため、```<br>```を使用して改行を作成できます。 |
| `glossary_tag_name` | 単一単語、英数字 | フィルターに名前を付けます。これらは検索バーの下のチェックボックスや、下のデータに表示されます。 |
| `glossary_filter_text` | 文字列、英数字 | フィルターについて説明します。通常、操作の指示に使用します。 |
| `glossary_tags` | YAMLとコンテンツの追加 | 以下の形式で記述します: <br> glossary_tags: <br>  - name: Content Cards <br>  - name: Email |
| `glossaries` | YAMLとコンテンツの追加 | 以下の[用語集パラメーター](#glossaries-parameters)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Required Parameters" }

### 用語集パラメーター {#glossaries-parameters}

| パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
| `name` | 英数字 | 用語集の項目に名前を付けます。 |
| `description` | 文字列、英数字 | 用語集の項目を説明します。 |
| `calculation` | 文字列 | （オプション）用語集の項目がどのように計算されるかを記述します（通常、データや指標を説明するときに使用します）。 |
| `tags` | 英数字 | `glossary_tags`の下に`name`として記載されているものと一致する必要があります。該当するものをすべて記載してください。`All`と記述すると、すべてのフィルターにその項目が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Glossaries Parameters" }

## 例 {#example}

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
