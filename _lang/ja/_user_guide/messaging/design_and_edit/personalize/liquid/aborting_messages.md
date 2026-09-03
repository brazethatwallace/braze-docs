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

## `abort_message()` を使ったテスト送信 {#test-sends-with-abort_message}

`abort_message()` は、条件を満たさないユーザーへの送信を停止します。メッセージはユーザーのプロファイルに表示されず、配信数やフリークエンシーキャップのカウントにも含まれません。

テスト送信が届かない場合は、中止条件を満たすユーザーとしてプレビューし、**テスト送信**で**受信者の属性を現在のプレビューユーザーの属性で上書きする**を有効にしてください（または、条件を満たすコンテンツテストグループのメンバーを追加してください）。

## 「Number Games Attended」が0の場合にメッセージを中止する {#abort-message-if-number-games-attended-0}

例えば、試合に参加したことのない顧客にはメッセージを送信したくない場合を考えてみましょう。

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

## 英語を話す顧客のみにメッセージを送信する {#message-english-speaking-customers-only}

英語を話す顧客のみにメッセージを送信するには、顧客の言語が英語の場合に一致する「if」ステートメントと、英語を話さない顧客やプロファイルに言語が設定されていない顧客に対してメッセージを中止する「else」ステートメントを作成します。

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

デフォルトでは、Brazeはメッセージアクティビティログに汎用エラーメッセージを記録します。

```text
{% abort_message %} called
```

また、かっこの中に文字列を含めることで、メッセージアクティビティログに中止メッセージの内容を記録することもできます。

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![開発者コンソールのメッセージエラーログ。中止メッセージ「language was nil」が表示されています。]({% image_buster /assets/img_archive/developer_console.png %})

## 中止メッセージのクエリ {#query-for-abort-messages}

[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)、またはBrazeに接続されている自社のデータウェアハウスを使用して、Liquidロジックによってメッセージが中止された際にトリガーされる特定の中止メッセージをクエリできます。

## アボートロジックの評価タイミング {#when-abort-logic-is-evaluated}

アボートロジックの評価タイミングは、メッセージチャネルによって異なります。

### プッシュ、メール、SMS、webhook、Content Cards {#push-email-sms-webhooks-and-content-cards}

アボートロジックは、Brazeが配信のためにメッセージを処理する送信時に評価されます。

### アプリ内メッセージ {#in-app-messages}

アボートロジックは、[テンプレート化されたアプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated)に対してのみ、アプリ内メッセージがトリガーされた時点（例えば、ユーザーがトリガーイベントを実行した時やセッションを開始した時）で評価されます。メッセージが最初にデバイスに送信された時点では評価されません。アプリ内メッセージはセッション開始時にSDKに配信され、ローカルにキャッシュされます。Liquid（`abort_message()` の呼び出しを含む）は、トリガー条件が満たされた時点で実行されます。

## 高い中止率のトラブルシューティング {#troubleshooting-high-abort-rates}

キャンペーンやキャンバスステップで多くのユーザーがエントリしたにもかかわらず送信数が少ない場合、または配信数が予想より低い場合、中止ロジックが一般的な原因です。特に、Liquid が評価時に欠落している属性、カタログデータ、またはリスト値を必要とする場合に発生します。

### メッセージアクティビティログを確認する {#check-the-message-activity-log}

1. Braze ダッシュボードで、キャンペーンまたはキャンバスのメッセージステップの[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)を開きます。
2. 中止関連のエントリでフィルターします。デフォルトでは、Braze は呼び出された {% raw %}`{% abort_message %}`{% endraw %} をログに記録します。`abort_message()` に理由の文字列を渡した場合、代わりにそのテキストが表示されます。
3. 中止が1つのチャネル（例えばメールのみ）に集中しているのか、同じキャンバス内の複数のチャネルにわたって発生しているのかを確認します。

### 送信時に属性と Liquid を検証する {#verify-attributes-and-liquid-at-send-time}

プッシュ、メール、SMS、webhook、Content Cardsでは、中止ロジックは Braze がメッセージを配信処理するときに実行されます。ユーザーがキャンバスにエントリしたときやトリガーイベントが以前に発火したときではありません。

- 必要な[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)、イベントプロパティ、または[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)フィールドが、メッセージステップの実行前にユーザーに設定されていることを確認します。
- `abort_message()` を呼び出す前に、明示的な nil または空のチェックを追加します。値が欠落している場合に中止する `else` 分岐は、そのデータを持たないすべてのユーザーの送信を停止します。
- パーソナライゼーションがリスト、セグメント、または Connected Content のレスポンスに依存している場合、メッセージステップの実行時にそのデータが利用可能であることを確認します。リストメンバーシップや下流のデータが準備できる前に、ユーザーがキャンバスにエントリする可能性があります。

### キャンバス固有の動作 {#canvas-specific-behavior}

キャンバスでメッセージステップが中止された場合、ユーザーはキャンバスから退出しません。代わりに、次のステップに進みます。中止はそのメッセージステップの送信数にのみ影響します。

キャンバスの中止を診断する場合:

- メッセージステップのエントリしたユーザー数と、同じステップの送信済みユーザー数を比較します。
- 1つのチャネルのみが中止される場合、そのステップのチャネル固有の Liquid または購読ステータスを確認します。
- リストやカタログの更新後に中止が急増した場合、更新が完了する前にメッセージステップが実行されたかどうかを確認します。

### プレビューとテスト送信で検証する {#validate-with-preview-and-test-sends}

メッセージ作成画面で、影響を受けた受信者のプロファイルに一致するユーザーとしてプレビューします。テスト送信の場合、中止ロジックがプロファイルデータに依存しているときは、**受信者の属性を現在のプレビューユーザーの属性でオーバーライドする**を有効にします。

その他の中止の例については、[中止メッセージのクエリ](#query-for-abort-messages)を参照してください。

## 考慮事項 {#considerations}

`abort_message()` Liquid メッセージタグはユーザーへのメッセージ送信を防止します。つまり、メッセージはユーザープロファイルに表示されず、配信数やフリークエンシーキャップのカウントにも含まれません。