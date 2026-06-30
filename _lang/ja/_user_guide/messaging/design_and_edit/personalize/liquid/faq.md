---
nav_title: FAQ
article_title: よくある質問
page_order: 12
description: "この記事では、Liquidに関するよくある質問への回答を提供します。"
toc_headers: h2
---

# よくある質問 {#frequently-asked-questions}

> このページでは、Liquidに関するよくある質問への回答を紹介します。

{% alert note %}
Brazeは現在、ShopifyのLiquidを100%サポートしているわけではなく、ドキュメントで概要を説明している特定の部分のみをサポートしています。エラーやサポートされていないLiquidの使用リスクを軽減するために、送信前にLiquidを使用したすべてのメッセージをテストしてください。
{% endalert %}

## BrazeにおけるLiquidについて {#about-liquid-in-braze}

### BrazeでLiquidスニペットを使用するにはどうすればよいですか？ {#how-do-i-use-liquid-snippets-in-braze}

多くの場合、CampaignやCanvasesに移動し、メール本文やSegmentsなどの領域でパーソナライゼーションモーダルにLiquidを挿入することで、Liquidスニペットを組み込むことができます。

#### 詳しくはどこで学べますか？ {#where-can-i-learn-more}

Liquidの詳細については、ガイド付きの[Liquidによるダイナミックパーソナライゼーション](https://learning.braze.com/path/dynamic-personalization-with-liquid) Braze Learningパスをご覧ください。また、[Liquidユースケースライブラリー]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)を参照して、Liquidを使用したパーソナライゼーションの例やインスピレーションを得ることもできます。

### パーソナライゼーションにおけるLiquidとコネクテッドコンテンツの違いは何ですか？ {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

Brazeのコネクテッドコンテンツは、Liquidタグの一例です。パーソナライゼーションにも使用されますが、このデータはBraze内に保存されたデータではなく、外部エンドポイントから取得されます。メッセージのパーソナライズ方法を拡張する方法について詳しくは、専用の[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)セクションをご覧ください。

### Liquidテンプレートとは何ですか？ {#what-is-liquid-templating}

これはBrazeでLiquidを使用する最も一般的な方法です。Liquidテンプレートでは、ユーザープロファイルからメッセージにデータを取り込みます。このデータは、ユーザーの名からトリガーメッセージのカスタムイベントまで多岐にわたります。

サポートされているLiquidタグの完全なリストについては、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照してください。

### Liquidを使用するとデータポイントが記録されますか？ {#does-using-liquid-log-data-points}

いいえ。

## パーソナライゼーションタグとデータソース {#personalization-tags-and-data-sources}

### Liquidを使用してパーソナライズされた挨拶を送信するにはどうすればよいですか？ {#how-can-i-use-liquid-to-send-a-personalized-greeting}

ユーザーの名を使用したパーソナライズされた挨拶には、{% raw %}`{{${first_name}}}`や`{{${last_name}}}`{% endraw %}などの標準ユーザープロファイル属性を取り込むことができます。

また、Liquidの{% raw %}`{% if X %}`{% endraw %}ステートメントを使用して、曜日やカスタム属性など、あらゆる条件に基づいた条件付きレンダリングを行うこともできます。条件文で使用できるサポートされているLiquid演算子の詳細については、[演算子]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators)をご覧ください。

### ユーザーのロケーションに基づいてメッセージをパーソナライズするにはどうすればよいですか？ {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
ユーザーのロケーションにはデフォルト属性があります：`{{${most_recent_location}}}`。
{% endraw %}

{% raw %}
### {{campaign.${name}}}と{{campaign.${message_name}}}の違いは何ですか？ {#whats-the-difference-between-campaignname-and-campaignmessage_name}

`{{campaign.${name}}}`と`{{campaign.${message_name}}}`はどちらもサポートされているLiquidパーソナライゼーションタグです。どちらのタグもCampaignの属性を参照します。`{{campaign.${name}}}`はCampaignの名前を示し、`{{campaign.${message_name}}}`はメッセージバリアントの名前です。
{% endraw %}

URLやクエリ文字列での使用（名前に`%`やスペースが含まれる場合など）については、[URLでのCampaign名]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls)を参照してください。

### ネストされたオブジェクトでLiquidを使用するにはどうすればよいですか？ {#how-do-i-use-liquid-with-nested-objects}

Brazeには、メッセージで使用できるSegments用のLiquidコードを生成する組み込み機能があります。具体的には、オブジェクト内の複数の条件に一致するセグメントを作成できます。

詳細については、[マルチ条件セグメンテーション]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#multi-criteria-segmentation)をご覧ください。

### イベント属性を使用して、イベントがトリガーするメッセージをパーソナライズするにはどうすればよいですか？ {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
`api_triggered_property`タグを使用して、APIトリガーイベントのプロパティにアクセスできます：`{{api_trigger_properties.${attribute_key}}}`。
{% endraw %}

### BrazeはLiquidで配列の配列をサポートしていますか？ {#does-braze-support-an-array-of-arrays-in-liquid}

Liquidはネイティブで配列の配列をサポートしていません。値をカンマ区切りの文字列の配列として格納し、必要に応じて`split`フィルターを使用して解析してください。

## 変数と構文 {#variables-and-syntax}

### Liquidで変数を割り当てるにはどうすればよいですか？ {#how-do-i-assign-variables-with-liquid}

`assign`タグを使用して変数を作成し、割り当てることができます。これにより、メッセージ作成画面で変数が作成され、メッセージ全体で参照することもできます。

### `assign`と`capture`はいつ使い分けるべきですか？ {#when-should-i-use-assign-versus-capture}

`assign`と`capture`はどちらもLiquid変数を作成しますが、用途が異なります。

- `assign`は、ブール値、数値、単純な文字列など、単一の値を格納するシンプルな変数に使用します。同じ行で単一のフィルターを適用することもできます。
- `capture`は、複数の変数、文字列、または複雑な式を含む可能性のあるテキストブロックを格納するために使用します。

他のLiquid変数やカスタム属性をパラメーターとして利用するURLなど、単一の`assign`ステートメントでは複雑すぎる値の場合に`capture`を使用してください。`capture`は、コネクテッドコンテンツ呼び出しの本文でLiquid変数を実装する場合にも推奨されます。

#### 例 {#examples}

{% raw %}
```liquid
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

### Liquid変数は件名と本文の間で引き継がれますか？ {#do-liquid-variables-carry-between-subject-line-and-body}

いいえ。Brazeは各メッセージコンポーネント（件名、HTML本文、プリヘッダー、プッシュタイトルなど）を個別にレンダリングします。あるフィールドで行った割り当てやキャプチャは、別のフィールドでは使用できません。値が必要な各フィールドでLiquidまたはコネクテッドコンテンツの呼び出しを繰り返してください。

### forループロジックとは何ですか？また、どのように使用できますか？ {#what-is-for-loop-logic-and-how-can-i-use-it}

forループは[反復タグ](https://shopify.github.io/liquid/tags/iteration/)とも呼ばれます。Liquidスニペットでforループロジックを使用すると、条件が満たされるまでLiquidブロックを繰り返し処理できます。

Brazeでは、配列カスタム属性のアイテムのチェック、または[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)呼び出しの応答で返される値やオブジェクトのリストのチェックに使用できます。具体的には、forループロジックをメッセージングの一部として使用して、製品が在庫にあるかどうか、または製品が最低評価を満たしているかどうかを確認できます。

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

### 中止ロジックとは何ですか？また、どのように使用できますか？ {#what-is-abort-logic-and-how-can-i-use-it}

中止ロジックを使用すると、条件が満たされた場合にメッセージの送信を停止できます。これは、不完全なメッセージがユーザーに送信されるのを防ぐのに特に役立ちます。マーケティングCampaignでの中止ロジックの例については、[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)で詳しくご覧ください。

### `abort_message`タグ内でLiquidを使用できますか？ {#can-i-use-liquid-inside-the-abort_message-tag}

いいえ。{% raw %}`{% abort_message %}`{% endraw %}タグは引用符で囲まれた静的な文字列のみを受け付け、Liquidパーソナライゼーションは使用できません。条件付きの中止動作が必要な場合は、タグの前に他のLiquidロジックを使用してください。

## Canvas、カタログ、トリガープロパティ {#canvas-catalogs-and-trigger-properties}

### APIトリガーのLiquidがBrazeで失敗するのはなぜですか？ {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
よくある原因は、余分な波括弧のペアです。例えば、`{{{api_trigger_properties.${attribute_key}}}}`は有効なBrazeパーソナライゼーション構文ではありません。開き波括弧2つと閉じ波括弧2つを正確に使用してください：`{{api_trigger_properties.${attribute_key}}}`。
{% endraw %}

### Canvasコンテキストプロパティにサイズ制限はありますか？ {#are-there-size-limits-for-canvas-context-properties}

Brazeは[Canvasコンテキストプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)にハードリミットを設けていませんが、ペイロードは約1 KB（約1,000文字）以下に抑えてください。大きなオブジェクトはメモリ使用量を増加させ、大量送信時のメッセージレンダリングを遅延させる可能性があります。

### ダッシュボードで特定のデータタイプをプレビューするとLiquidエラーが発生するのはなぜですか？ {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

一部の[Canvasコンテキストプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)タイプは、比較や計算で使用する前にLiquidでの型変換が必要です。例えば、数値の動作が必要な場合：

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### カタログのLiquidスニペットが中止メッセージを返すのはなぜですか？ {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

カタログのLiquidスニペットが送信時に中止される場合は、一括またはフルダイナミックセレクションを使用する代わりに、パーソナライゼーションメニューから個別のカタログアイテムを選択してスニペットを再作成してください。詳細については、[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)と[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を参照してください。

## Content Blocksとメッセージ作成画面 {#content-blocks-and-the-message-composer}

### Content Blocksを使用するメッセージに余分なスペースが入るのはなぜですか？ {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Liquidを使用するContent Blocksで送信されたメッセージに余分なスペースがある場合、条件文内に不要な段落や改行が含まれている可能性があります。条件文は複数行にまたがるのではなく、1行で記述してください。

#### 例 {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### ドラッグ＆ドロップの検索ツールで**Row**にContent Blockが表示されないのはなぜですか？ {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

一部のContent Blocksは、ドラッグ＆ドロップエディターの検索で**Row**の下に表示されません。**コンテンツ**タブ（**Advanced**）からHTMLブロックを追加し、そのHTMLブロック内にContent BlockのLiquidタグを挿入して、ブロックのコンテンツをレンダリングしてください。

### ドラッグ＆ドロップのContent Blockプレビューが作成ビューと異なるのはなぜですか？ {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Content BlockをLiquidでテンプレート化すると、ブロック内のモバイルメディアクエリが、ブロックを直接メッセージにドラッグした場合と同じようにプレビューに適用されないことがあります。ブロックをドラッグするとレイアウトは保持されますが、ソースブロックから切り離されるため、今後のブロック編集はメッセージに自動的に反映されなくなります。

### メッセージ作成画面でイベントプロパティの値をプレビューするにはどうすればよいですか？ {#how-do-i-preview-event-property-values-in-message-composer}

**カスタムユーザーとしてプレビュー**を使用し、プレビューするユーザーのサンプルカスタムイベントプロパティ値を入力してください。これは、中止をトリガーしないプレビュー値が必要な中止ロジックを含むメッセージにも便利です。

## メールメッセージでのLiquid {#liquid-in-email-messages}

### メッセージが「Invalid from email address for recipient:」で中止されるのはなぜですか？ {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

この中止は、**差出人**アドレスのLiquidが無効な構文（変数の欠落、余分なスペース、許可されていない文字など）を生成した場合に発生します。テストユーザーでプレビューし、レンダリングされた**差出人**アドレスが設定済みの送信ドメインと一致していることを確認してください。

### ダイナミックな返信先アドレスを作成するにはどうすればよいですか？ {#how-do-i-create-a-dynamic-reply-to-address}

ワークスペースがダイナミックな返信先設定をサポートしている場合、**返信先**フィールドでLiquidを使用してください。必要に応じて**差出人**の表示名設定と組み合わせてください。ワークスペース固有のオプションについては、[メール設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)を参照してください。

## Liquidエラーのトラブルシューティング {#troubleshooting-liquid-errors}

### 「Unexpected end token」というLiquidエラーが表示されるのはなぜですか？ {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

このエラーは通常、波括弧の過不足を示しています。{% raw %}`{{ }}`{% endraw %}を別のLiquidタグ式の中にネストしないでください。例えば、属性参照を追加の波括弧で囲むのではなく、{% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %}を使用してください。

### アプリ内メッセージでコネクテッドコンテンツのリトライが利用できないのはなぜですか？ {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
リトライ付きの`{% connected_content %}`タグは、一部のアプリ内メッセージ形式を含むすべてのメッセージタイプでサポートされているわけではありません。リトライパラメーターを削除するか、リトライ付きコネクテッドコンテンツ呼び出しにサポートされているチャネルを使用してください。
{% endraw %}