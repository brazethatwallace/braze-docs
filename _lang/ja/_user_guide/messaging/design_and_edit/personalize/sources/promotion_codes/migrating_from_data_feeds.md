---
nav_title: データフィードからの移行
article_title: データフィードからプロモーションコードへの移行
page_order: 10
description: "この参照記事では、データフィードからプロモーションコードへの移行に関するガイダンスを提供します。"
---

# データフィードからプロモーションコードへの移行 {#migrate-from-data-feeds-to-promotion-codes}

> このページでは、データフィードからプロモーションコードへの移行手順を説明します。これは簡単なプロセスで、データフィードの情報を使用してプロモーションコードリストを手動で作成し、メッセージの参照を適宜更新します。

{% alert note %}
データフィードは廃止予定です。Brazeでは、データフィードを使用している顧客はプロモーションコードリストに移行することを推奨しています。
{% endalert %}

## 機能と特徴 {#features-and-functionality}

プロモーションコードリストとデータフィードにはいくつかの違いがあります。

| 機能          | プロモーションコード | データフィード   |
|------------------|-----------------|--------------|
| 説明     | あり             | なし           |
| 有効期限 | あり             | なし           |
| 作成方法  | CSVのアップロード | テキストの貼り付け |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Features and functionality" }

## 移行方法 {#how-to-migrate}

データフィードをプロモーションコードリストに置き換えるには、以下の手順を実行します。

1. **Data Settings**に移動し、**Create Promotion Code List**を選択します。
2. [プロモーションコードリストを設定します]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/)。
3. 以前データフィードを参照していたメッセージに移動し、プロモーションコードリストを使用するように更新します。