---
nav_title: メッセージの中止
article_title: Liquid メッセージの中止
page_order: 7
description: "このリファレンス記事では、Liquid メッセージの中止と、いくつかのユースケースの例について説明します。"

---

# メッセージの中止 {#abort-messages}

> オプションとして、条件文内で `abort_message("optional reason for aborting")` Liquid メッセージタグを使用して、ユーザーへのメッセージ送信を防止できます。このリファレンス記事では、マーケティングキャンペーンでこの機能を使用する方法の例をいくつか紹介します。

{% alert note %}
キャンバスでメッセージステップが中止された場合、ユーザーはキャンバスから**退出せず**、次のステップに**進みます**。
{% endalert %}

## `abort_message()` を使用したテスト送信 {#test-sends-with-abort_message}

`abort_message()` は、条件を満たさないユーザーへの送信を停止します。メッセージはユーザーのプロファイルに表示されず、配信数やフリークエンシーキャップにもカウントされません。

テスト送信が届かない場合は、中止条件を満たすユーザーとしてプレビューし、**Test Send**で**Override recipients' attributes with current preview user's attributes**を有効にしてください（または条件を満たすコンテンツテストグループのメンバーを追加してください）。

## 「Number Games Attended」= 0 の場合にメッセージを中止する {#abort-message-if-number-games-attended-0}

たとえば、試合に参加したことがない顧客にはメッセージを送信したくない場合を考えてみましょう。

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

このメッセージは、試合に参加したことが確認されている顧客にのみ送信されます。

## 英語を話す顧客にのみメッセージを送信する {#message-english-speaking-customers-only}

顧客の言語が英語の場合に一致する「if」文と、英語を話さない、またはプロファイルに言語が設定されていない人に対してメッセージを中止する「else」文を作成することで、英語を話す顧客にのみメッセージを送信できます。

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

デフォルトでは、Brazeはメッセージアクティビティログに汎用的なエラーメッセージを記録します。

```text
{% abort_message %} called
```

また、かっこ内に文字列を含めることで、中止メッセージにメッセージアクティビティログへの記録内容を指定することもできます。

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![開発者コンソールのメッセージエラーログ。中止メッセージとして「language was nil」が表示されています。]({% image_buster /assets/img_archive/developer_console.png %})

## 中止メッセージのクエリ {#query-for-abort-messages}

[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)、またはBrazeに接続されている独自のデータウェアハウスを使用して、Liquidロジックによってメッセージが中止されたときにトリガーされる特定の中止メッセージをクエリできます。

## 中止ロジックが評価されるタイミング {#when-abort-logic-is-evaluated}

中止ロジックの評価タイミングは、メッセージチャネルによって異なります。

### プッシュ、メール、SMS、Webhook、Content Cards {#push-email-sms-webhooks-and-content-cards}

中止ロジックは、Brazeが配信のためにメッセージを処理する送信時に評価されます。

### アプリ内メッセージ {#in-app-messages}

中止ロジックは、[テンプレート化されたアプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated)に対してのみ、メッセージが最初にデバイスに送信されたときではなく、アプリ内メッセージがトリガーされたとき（たとえば、ユーザーがトリガーイベントを実行したときやセッションを開始したとき）に評価されます。アプリ内メッセージはセッション開始時にSDKに配信され、ローカルにキャッシュされます。`abort_message()` 呼び出しを含むLiquidは、トリガー条件が満たされたときに実行されます。

## 考慮事項 {#considerations}

`abort_message()` Liquidメッセージタグは、ユーザーへのメッセージ送信を防止します。つまり、メッセージはユーザープロファイルに表示されず、配信数やフリークエンシーキャップにもカウントされません。