---
nav_title: FAQ
article_title: よくある質問
page_order: 12
description: "この記事では、Liquid に関するよくある質問への回答を提供します。"

---

# よくある質問

> このページでは、Liquid に関するよくある質問への回答を紹介します。<br><br>Braze は現在、Shopify の Liquid を100%サポートしているわけではなく、ドキュメントで概要を説明している特定の部分のみをサポートしています。エラーやサポートされていない Liquid の使用リスクを軽減するために、送信前に Liquid を使用したすべてのメッセージをテストすることを強くお勧めします。

### Braze で Liquid スニペットを使用するにはどうすればよいですか？

多くの場合、キャンペーンやキャンバスに移動し、メール本文やセグメントなどの領域でパーソナライゼーションモーダルに Liquid を挿入することで、Liquid スニペットを組み込むことができます。

#### 詳しくはどこで学べますか？

Liquid の詳細については、ガイド付きの [Dynamic Personalization with Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze Learning パスをご覧ください！また、[Liquid ユースケースライブラリー]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/)を参照して、Liquid を使用したパーソナライゼーションの例やインスピレーションを得ることもできます。

### パーソナライゼーションにおける Liquid とコネクテッドコンテンツの違いは何ですか？

Braze のコネクテッドコンテンツは Liquid タグの一例です。パーソナライゼーションにも使用されますが、このデータは Braze 内に保存されたデータではなく、外部エンドポイントから取得されます。メッセージのパーソナライズ方法を拡張する方法について詳しくは、専用の[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)セクションをご覧ください。

### Liquid テンプレートとは何ですか？

これは Braze で Liquid を使用する最も一般的な方法です。Liquid テンプレートでは、ユーザープロファイルからメッセージにデータを取り込みます。このデータは、ユーザーの名からトリガーメッセージのカスタムイベントまで多岐にわたります。

サポートされている Liquid タグの完全なリストについては、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)を参照してください。

### Liquid で変数を割り当てるにはどうすればよいですか？

`assign` タグを使用して変数を作成し、割り当てることができます。これにより、メッセージ作成画面で変数が作成され、メッセージ全体で参照することもできます。

### Liquid を使用するとデータポイントが記録されますか？

いいえ。

### Liquid を使用してパーソナライズされた挨拶を送信するにはどうすればよいですか？

ユーザーの名を使用したパーソナライズされた挨拶には、{% raw %} `{{${first_name}}}`、`{{${last_name}}}` などの標準ユーザープロファイル属性を取り込むことができます。

また、Liquid の `{% if X %}` {% endraw %}ステートメントを使用して、曜日やカスタム属性など、あらゆる条件に基づいた条件付きレンダリングを行うこともできます。条件文で使用できるサポートされている Liquid 演算子の詳細については、[演算子]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/)をご覧ください。

### 顧客のロケーションに基づいてメッセージをパーソナライズするにはどうすればよいですか？

{% raw %}
ユーザーのロケーションにはデフォルト属性があります：`{{${most_recent_location}}}`。

### {{campaign.${name}}} と {{campaign.${message_name}}} の違いは何ですか？

`{{campaign.${name}}}` と `{{campaign.${message_name}}}` はどちらもサポートされている Liquid パーソナライゼーションタグです。どちらのタグもキャンペーン属性を参照します。`{{campaign.${name}}}` はキャンペーンの名前を示し、`{{campaign.${message_name}}}` はメッセージバリアントの名前です。
{% endraw %}

### ネストされたオブジェクトで Liquid を使用するにはどうすればよいですか？

Braze には、メッセージで使用できるセグメント用の Liquid コードを生成する組み込み機能があります。具体的には、オブジェクト内の複数の条件に一致するセグメントを作成できます。

詳細については、[マルチ条件セグメンテーション]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#multi-criteria-segmentation)をご覧ください。

### イベント属性を使用して、イベントがトリガーするメッセージをパーソナライズするにはどうすればよいですか？

{% raw %}
`api_triggered_property` タグを使用して、API トリガーイベントのプロパティにアクセスできます：`{{api_trigger_properties.${attribute_key}}}`。
{% endraw %}

### 中止ロジックとは何ですか？また、どのように使用できますか？

中止ロジックを使用すると、条件が満たされた場合にメッセージの送信を停止できます。これは、不完全なメッセージがユーザーに送信されるのを防ぐのに特に役立ちます。マーケティングキャンペーンでの中止ロジックの例については、[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)で詳しくご覧ください。

### for ループロジックとは何ですか？また、どのように使用できますか？

for ループは[反復タグ](https://shopify.github.io/liquid/tags/iteration/)とも呼ばれます。Liquid スニペットで for ループロジックを使用すると、条件が満たされるまで Liquid ブロックを繰り返し処理できます。

Braze では、配列カスタム属性のアイテムのチェック、または[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)呼び出しの応答で返される値やオブジェクトのリストのチェックに使用できます。具体的には、for ループロジックを使用して、製品が在庫にあるかどうか、または製品が最低評価を満たしているかどうかをメッセージングの一部として確認できます。

例えば、「Games」というカタログに「cheap_games」というセレクションがあるとします。「cheap_games」のゲームタイトルを取得するには、次の Liquid スニペットを使用できます：

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

設定した条件が満たされると、メッセージを続行できます。このロジックを使用すると、異なる条件に対して Liquid ブロックを繰り返す代わりに時間を節約できます。

### コンテンツブロックを使用するメッセージに余分なスペースが入るのはなぜですか？

Liquid を使用するコンテンツブロックで送信されたメッセージに余分なスペースがある場合、条件文内に不要な段落や改行が含まれている可能性があります。条件文は複数行にまたがるのではなく、1行で記述してください。

#### 例

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
{% endraw %}

### When should I use `assign` versus `capture`?

Both `assign` and `capture` create Liquid variables, but they serve different purposes:

- `assign` is for simple variables that store a single value, such as a boolean, number, or simple string. You can also apply a single filter in the same line.
- `capture` is for storing a block of text that may include multiple variables, strings, or complex expressions. Use `capture` when the value is too complex for a single `assign` statement, such as URLs that utilize other Liquid variables or custom attributes as parameters. `capture` is also preferred when implementing Liquid variables in the body of Connected Content calls.

#### Examples

{% raw %}
```liquid
{% comment %} Valid assign usage {% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %} Use capture for complex strings {% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}
```
{% endraw %}