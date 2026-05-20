---
nav_title: FAQ
article_title: よくある質問
page_order: 12
description: "この記事では、Liquidに関するよくある質問への回答を提供します。"

---

# よくある質問 {#frequently-asked-questions}

> このページでは、Liquidに関するよくある質問への回答を紹介します。<br><br>Brazeは現在、ShopifyのLiquidを100%サポートしているわけではなく、ドキュメントで概要を説明している特定の部分のみをサポートしています。エラーやサポートされていないLiquidの使用リスクを軽減するために、送信前にLiquidを使用したすべてのメッセージをテストすることを強くお勧めします。

### BrazeでLiquidスニペットを使用するにはどうすればよいですか？ {#how-do-i-use-liquid-snippets-in-braze}

多くの場合、キャンペーンやキャンバスに移動し、メール本文やセグメントなどの領域でパーソナライゼーションモーダルにLiquidを挿入することで、Liquidスニペットを組み込むことができます。

#### 詳しくはどこで学べますか？ {#where-can-i-learn-more}

Liquidの詳細については、ガイド付きの[Liquidによるダイナミックパーソナライゼーション](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze Learningパスをご覧ください！また、[Liquidユースケースライブラリー]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/)を参照して、Liquidを使用したパーソナライゼーションの例やインスピレーションを得ることもできます。

### パーソナライゼーションにおけるLiquidとコネクテッドコンテンツの違いは何ですか？ {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

Brazeのコネクテッドコンテンツは、Liquidタグの一例です。パーソナライゼーションにも使用されますが、このデータはBraze内に保存されたデータではなく、外部エンドポイントから取得されます。メッセージのパーソナライズ方法を拡張する方法について詳しくは、専用の[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)セクションをご覧ください。

### Liquidテンプレートとは何ですか？ {#what-is-liquid-templating}

これはBrazeでLiquidを使用する最も一般的な方法です。Liquidテンプレートでは、ユーザープロファイルからメッセージにデータを取り込みます。このデータは、ユーザーの名からトリガーメッセージのカスタムイベントまで多岐にわたります。

サポートされているLiquidタグの完全なリストについては、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)を参照してください。

### Liquidで変数を割り当てるにはどうすればよいですか？ {#how-do-i-assign-variables-with-liquid}

`assign` タグを使用して変数を作成し、割り当てることができます。これにより、メッセージ作成画面で変数が作成され、メッセージ全体で参照することもできます。

### Liquidを使用するとデータポイントが記録されますか？ {#does-using-liquid-log-data-points}

いいえ。

### Liquidを使用してパーソナライズされた挨拶を送信するにはどうすればよいですか？ {#how-can-i-use-liquid-to-send-a-personalized-greeting}

ユーザーの名を使用したパーソナライズされた挨拶には、{% raw %} `{{${first_name}}}`、`{{${last_name}}}` などの標準ユーザープロファイル属性を取り込むことができます。

また、Liquidの `{% if X %}` {% endraw %}ステートメントを使用して、曜日やカスタム属性など、あらゆる条件に基づいた条件付きレンダリングを行うこともできます。条件文で使用できるサポートされているLiquid演算子の詳細については、[演算子]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/)をご覧ください。

### 顧客のロケーションに基づいてメッセージをパーソナライズするにはどうすればよいですか？ {#how-can-i-personalize-a-message-based-on-a-customers-location}

{% raw %}
ユーザーのロケーションにはデフォルト属性があります：`{{${most_recent_location}}}`。

### {{campaign.${name}}} と {{campaign.${message_name}}} の違いは何ですか？ {#whats-the-difference-between-campaignname-and-campaignmessagename}

`{{campaign.${name}}}` と `{{campaign.${message_name}}}` はどちらもサポートされているLiquidパーソナライゼーションタグです。どちらのタグもキャンペーン属性を参照します。`{{campaign.${name}}}` はキャンペーンの名前を示し、`{{campaign.${message_name}}}` はメッセージバリアントの名前です。
{% endraw %}

### ネストされたオブジェクトでLiquidを使用するにはどうすればよいですか？ {#how-do-i-use-liquid-with-nested-objects}

Brazeには、メッセージで使用できるセグメント用のLiquidコードを生成する組み込み機能があります。具体的には、オブジェクト内の複数の条件に一致するセグメントを作成できます。

詳細については、[マルチ条件セグメンテーション]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#multi-criteria-segmentation)をご覧ください。

### イベント属性を使用して、イベントがトリガーするメッセージをパーソナライズするにはどうすればよいですか？ {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
`api_triggered_property` タグを使用して、APIトリガーイベントのプロパティにアクセスできます：`{{api_trigger_properties.${attribute_key}}}`。
{% endraw %}

### APIトリガーのLiquidがBrazeで失敗するのはなぜですか？ {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
よくある原因は、余分な波括弧のペアです。例えば、`{{{api_trigger_properties.${attribute_key}}}}` は有効なBrazeパーソナライゼーション構文ではありません。開き波括弧2つと閉じ波括弧2つを正確に使用してください：`{{api_trigger_properties.${attribute_key}}}`。
{% endraw %}

### 中止ロジックとは何ですか？また、どのように使用できますか？ {#what-is-abort-logic-and-how-can-i-use-it}

中止ロジックを使用すると、条件が満たされた場合にメッセージの送信を停止できます。これは、不完全なメッセージがユーザーに送信されるのを防ぐのに特に役立ちます。マーケティングキャンペーンでの中止ロジックの例については、[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)で詳しくご覧ください。

### forループロジックとは何ですか？また、どのように使用できますか？ {#what-is-for-loop-logic-and-how-can-i-use-it}

forループは[反復タグ](https://shopify.github.io/liquid/tags/iteration/)とも呼ばれます。Liquidスニペットでforループロジックを使用すると、条件が満たされるまでLiquidブロックを繰り返し処理できます。

Brazeでは、配列カスタム属性のアイテムのチェック、または[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)呼び出しの応答で返される値やオブジェクトのリストのチェックに使用できます。具体的には、forループロジックをメッセージングの一部として使用して、製品が在庫にあるかどうか、または製品が最低評価を満たしているかどうかを確認できます。

例えば、「Games」というカタログに「cheap_games」というセレクションがあるとします。「cheap_games」のゲームタイトルを取得するには、次のLiquidスニペットを使用できます：

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

設定した条件が満たされると、メッセージを続行できます。このロジックを使用すると、異なる条件に対してLiquidブロックを繰り返す代わりに時間を節約できます。

### Content Blocksを使用するメッセージに余分なスペースが入るのはなぜですか？ {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Liquidを使用するContent Blocksで送信されたメッセージに余分なスペースがある場合、条件文内に不要な段落や改行が含まれている可能性があります。条件文は複数行にまたがるのではなく、1行で記述してください。

#### 例 {#example}

{% raw %}
`````````liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### `assign` と `capture` はいつ使い分けるべきですか？ {#when-should-i-use-assign-versus-capture}

`assign` と `capture` はどちらもLiquid変数を作成しますが、用途が異なります。

- `assign` は、ブール値、数値、単純な文字列など、単一の値を格納するシンプルな変数に使用します。同じ行で単一のフィルターを適用することもできます。
- `capture` は、複数の変数、文字列、または複雑な式を含む可能性のあるテキストブロックを格納するために使用します。

他のLiquid変数やカスタム属性をパラメーターとして利用するURLなど、単一の `assign` ステートメントでは複雑すぎる値の場合に `capture` を使用してください。`capture` は、コネクテッドコンテンツ呼び出しの本文でLiquid変数を実装する場合にも推奨されます。

#### 例 {#examples}

{% raw %}
`````````liquid
{% comment %}Use assign for custom attributes{% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %}Use assign for a simple variable{% endcomment %}
{% assign discount_label = "20% off" %}
Hello {{ customer.first_name | default: "there" }}, enjoy {{ discount_label }} on your next order!

{% comment %}Use capture for complex strings{% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}

{% comment %}Use capture to create conditional content{% endcomment %}
{% capture promo_block %}
{% if customer.vip == true %}
As a VIP member, you get free shipping.
{% else %}
Join our VIP program to unlock free shipping.
{% endif %}
{% endcapture %}
```
{% endraw %}