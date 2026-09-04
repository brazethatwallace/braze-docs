---
nav_title: コネクテッドコンテンツのリトライ
article_title: コネクテッドコンテンツのリトライ
page_order: 5
description: "このリファレンス記事では、コネクテッドコンテンツのリトライの処理方法について説明します。"

---

# コネクテッドコンテンツのリトライロジックを使用する {#use-retry-logic-for-connected-content}

> このページでは、コネクテッドコンテンツの呼び出しにリトライを追加する方法について説明します。

## リトライの仕組み {#how-retries-work}

Connected Contentは API からのデータ受信に依存しているため、Brazeが呼び出しを行う際に API が一時的に利用できなくなる場合があります。この場合、Brazeは指数バックオフを使用してリクエストを再試行するリトライロジックをサポートしています。

{% alert note %}
Connected Contentの`:retry`はアプリ内メッセージでは利用できません。
{% endalert %}

## リトライロジックの使用 {#using-retry-logic}

リトライロジックを使用するには、以下のコードスニペットに示すように、Connected Content呼び出しに`:retry`タグを追加します。

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Connected Content呼び出しに`:retry`タグが含まれている場合、Brazeは最大5回まで呼び出しのリトライを試みます。

### プレビューの動作 {#preview-behavior}

リトライロジックはライブ送信（テスト送信を含む）にのみ適用され、プレビューには適用されません。`:retry`を含むConnected Content呼び出しがプレビュー中に失敗した場合、コンテンツがレンダリングされる代わりに「This message would not have been shown because retry functionality was triggered」というメッセージが表示されることがあります。これは想定された動作であり、Braze内の問題を示すものではありません。

### リトライの結果 {#retry-outcomes}

#### リトライが成功した場合 {#when-a-retry-succeeds}

リトライが成功した場合、メッセージは送信され、そのメッセージに対するそれ以上のリトライは試行されません。

#### API呼び出しが失敗し、リトライが有効な場合 {#when-the-api-call-fails-and-retries-are-enabled}

API呼び出しが失敗し、リトライが有効になっている場合、Brazeは再送信ごとに設定された[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)を遵守しながら呼び出しをリトライします。Brazeは失敗したメッセージをキューの末尾に移動し、必要に応じてメッセージの送信にかかる合計時間に追加の分数を加えます。

Connected Content呼び出しが5回を超えてエラーになった場合、[メッセージ中止タグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)がトリガーされた場合と同様に、メッセージは中止されます。

{% multi_lang_include connected_content/abort_and_retry_logic.md %}