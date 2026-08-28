---
nav_title: データ変換
hidden: true
---

# Braze データ変換 {#braze-data-transformation}

> Braze [データ変換]({{site.baseurl}}/data_transformation)は、パートナープラットフォームからWebhookを取り込み、そのWebhookのペイロードをBrazeユーザープロファイル上の属性、イベント、購入などの目的のユーザーデータに変換するためのマッピングを定義できます。

## データ変換ベースの連携の概要 {#what-a-data-transformation-based-integration-would-look-like}

データ変換機能に基づくパートナー連携は、公開ドキュメントを通じて顧客と共有される変換コードテンプレートとなります。

共通の顧客にとっては、次のようなフローになります。

1. 貴社のプラットフォームにログインし、Webhookを設定します。
2. Brazeチームと連携してBrazeデータ変換へのアクセスを取得し、Brazeダッシュボード内で新しい変換を作成します。
3. 変換によって生成されたURLをコピーします。
4. Brazeに戻り、コピーした変換URLにテストWebhookを送信します。
5. Brazeで変換コードテンプレートをコピーして貼り付けます。
6. 変換を有効にします。
7. 有効にした後、Brazeのユーザー検索ツールを使用して、Webhookに基づいてユーザープロファイルが更新されていることを確認し、必要に応じて変換コードを編集できます。

{% alert tip %}
変換コードの例を作成する際は、Brazeに送信するWebhookのタイプごとに変換を作成することをお勧めします。
{% endalert %}