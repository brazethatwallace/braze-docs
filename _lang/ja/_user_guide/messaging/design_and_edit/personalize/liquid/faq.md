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

多くの場合、キャンペーンやキャンバスに移動し、メール本文やセグメントなどの領域でパーソナライゼーションモーダルにLiquidを挿入することで、Liquidスニペットを組み込むことができます。

#### 詳しくはどこで学べますか？ {#where-can-i-learn-more}

Liquidの詳細については、Braze Learningのガイド付きパス「[Dynamic Personalization with Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid)」をご覧ください。また、[Liquidユースケースライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)を参照して、Liquidを使用したさまざまなパーソナライゼーションの例やインスピレーションを得ることもできます。

### パーソナライゼーションにおけるLiquidとConnected Contentの違いは何ですか？ {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

Braze Connected Contentは、Liquidタグの一例です。パーソナライゼーションにも使用されますが、このデータはBraze内に保存されたデータではなく、外部エンドポイントから取得されます。メッセージのパーソナライズ方法を拡張する方法については、専用の[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)セクションをご覧ください。

### Liquidテンプレートとは何ですか？ {#what-is-liquid-templating}

これは、BrazeでLiquidを使用する最も一般的な方法です。Liquidテンプレートでは、ユーザープロファイルからメッセージにデータを取り込みます。このデータは、ユーザーの名からトリガーメッセージのカスタムイベントまで多岐にわたります。

サポートされているLiquidタグの完全なリストについては、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照してください。

### Liquidを使用するとデータポイントが記録されますか？ {#does-using-liquid-log-data-points}

いいえ。

## パーソナライゼーションタグとデータソース {#personalization-tags-and-data-sources}

### Liquidを使用してパーソナライズされた挨拶を送信するにはどうすればよいですか？ {#how-can-i-use-liquid-to-send-a-personalized-greeting}

ユーザーの名を使用したパーソナライズされた挨拶には、{% raw %}`{{${first_name}}}`や`{{${last_name}}}`{% endraw %}などの標準ユーザープロファイル属性を使用します。

また、Liquidの{% raw %}`{% if X %}`{% endraw %}ステートメントを使用して、曜日やカスタム属性など、あらゆる条件に基づいた条件付きレンダリングを行うこともできます。条件文で使用できるサポートされているLiquid演算子の詳細については、[演算子]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators)を参照してください。

### ユーザーの位置情報に基づいてメッセージをパーソナライズするにはどうすればよいですか？ {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
ユーザーの位置情報にはデフォルト属性があります：`{{${most_recent_location}}}`。
{% endraw %}

{% raw %}
### {{campaign.${name}}}と{{campaign.${message_name}}}の違いは何ですか？ {#whats-the-difference-between-campaignname-and-campaignmessage_name}

`{{campaign.${name}}}`と`{{campaign.${message_name}}}`はどちらもサポートされているLiquidパーソナライゼーションタグです。どちらのタグもキャンペーン属性を参照します。`{{campaign.${name}}}`はキャンペーンの名前を示し、`{{campaign.${message_name}}}`はメッセージバリアントの名前です。
{% endraw %}

URLやクエリ文字列での使用（例えば、名前に`%`やスペースが含まれる場合）については、[URL内のキャンペーン名]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls)を参照してください。

### ネストされたオブジェクトでLiquidを使用するにはどうすればよいですか？ {#how-do-i-use-liquid-with-nested-objects}

Brazeには、メッセージで使用できるセグメント用のLiquidコードを生成する組み込み機能があります。具体的には、オブジェクト内の複数の条件に一致するセグメントを作成できます。

詳細については、[複数条件セグメンテーション]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects)を参照してください。

### イベント属性を使用して、イベントがトリガーするメッセージをパーソナライズするにはどうすればよいですか？ {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
APIトリガーイベントのプロパティには、`api_triggered_property`タグを使用してアクセスできます：`{{api_trigger_properties.${attribute_key}}}`。
{% endraw %}

### BrazeはLiquidで配列の配列をサポートしていますか？ {#does-braze-support-an-array-of-arrays-in-liquid}

Liquidは配列の配列をネイティブにサポートしていません。値をカンマ区切りの文字列の配列として保存し、必要に応じて`split`フィルターを使用して解析してください。

## 変数と構文 {#variables-and-syntax}

### Liquidで変数を割り当てるにはどうすればよいですか？ {#how-do-i-assign-variables-with-liquid}

`assign`タグを使用して変数を作成し、割り当てることができます。これにより、メッセージ作成画面で変数が作成され、メッセージ全体で参照することもできます。

すべてのBraze Liquid変数を二重波括弧（`{{ }}`）で囲めば、`assign`を複数行に分割できます。これらの波括弧がない場合、複数行のassignステートメントは、テンプレート化に失敗するカスタム属性を含む予期しないレンダリングを引き起こす可能性があります。例と関連する構文ルールについては、[Liquidの使用]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax)を参照してください。

### `assign`と`capture`はどのように使い分けるべきですか？ {#when-should-i-use-assign-versus-capture}

`assign`と`capture`はどちらもLiquid変数を作成しますが、目的が異なります。

- `assign`は、ブール値、数値、単純な文字列など、単一の値を格納するシンプルな変数に使用します。同じ行で単一のフィルターを適用することもできます。
- `capture`は、複数の変数、文字列、または複雑な式を含む可能性のあるテキストブロックを格納するために使用します。

他のLiquid変数やカスタム属性をパラメーターとして使用するURLなど、単一の`assign`ステートメントでは複雑すぎる値の場合は`capture`を使用してください。`capture`は、Connected Content呼び出しの本文にLiquid変数を実装する場合にも推奨されます。

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

いいえ。Brazeは各メッセージコンポーネント（件名、HTML本文、プリヘッダー、プッシュタイトルなど）を個別にレンダリングします。あるフィールドで行った割り当てやキャプチャは、別のフィールドでは使用できません。値が必要な各フィールドでLiquidまたはConnected Content呼び出しを繰り返してください。

### forループロジックとは何ですか？どのように使用できますか？ {#what-is-for-loop-logic-and-how-can-i-use-it}

forループは[反復タグ](https://shopify.github.io/liquid/tags/iteration/)とも呼ばれます。Liquidスニペットでforループロジックを使用すると、条件が満たされるまでLiquidブロックを繰り返し処理できます。

Brazeでは、配列カスタム属性の項目、または[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)呼び出しのレスポンスから返される値やオブジェクトのリストを確認するために使用できます。具体的には、forループロジックをメッセージングの一部として使用して、商品が在庫にあるかどうか、または商品が最低評価を満たしているかどうかを確認できます。

例えば、「Games」というカタログに「cheap_games」というセレクションがあるとします。「cheap_games」のゲームタイトルを取得するには、次のLiquidスニペットを使用できます。

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

設定した条件が満たされると、メッセージは処理を続行できます。このロジックを使用すると、異なる条件に対してLiquidブロックを繰り返す代わりに時間を節約できます。

### 中止ロジックとは何ですか？どのように使用できますか？ {#what-is-abort-logic-and-how-can-i-use-it}

中止ロジックを使用すると、条件が満たされた場合にメッセージの送信を停止できます。これは、不完全なメッセージがユーザーに送信されるのを防ぐのに特に役立ちます。マーケティングキャンペーンでの中止ロジックの例については、[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)を参照してください。

### `abort_message`タグ内でLiquidを使用できますか？ {#can-i-use-liquid-inside-the-abort_message-tag}

いいえ。{% raw %}`{% abort_message %}`{% endraw %}タグは引用符で囲まれた静的な文字列を受け付けますが、Liquidパーソナライゼーションは受け付けません。条件付きの中止動作が必要な場合は、タグの前に他のLiquidロジックを使用してください。

### Liquidで電話番号をマスクするにはどうすればよいですか？ {#how-do-i-mask-phone-numbers-with-liquid}

`slice`フィルターを使用して特定の数字を抽出し、`append`フィルターを使用してマスク文字と組み合わせることで、電話番号をマスクできます。

#### 下4桁以外をすべてマスクする {#mask-all-but-the-last-four-digits}

10桁の電話番号を`******7890`として表示するには：

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | split: '' %}
{% assign masked_phone = '' %}
{% for i in (0..5) %}
  {% assign masked_phone = masked_phone | append: '*' %}
{% endfor %}
{% for i in (6..9) %}
  {% assign masked_phone = masked_phone | append: phone[i] %}
{% endfor %}
{{ masked_phone }}
```
{% endraw %}

#### 最初の3桁と最後の4桁を表示する {#show-the-first-three-and-last-four-digits}

10桁の電話番号を`123***7890`として表示するには：

{% raw %}
```liquid
{% assign first_part = {{${phone_number}}} | slice: 0, 3 %}
{% assign last_part = {{${phone_number}}} | slice: -4, 4 %}
{% assign masked_phone_number = first_part | append: "***" | append: last_part %}
{{ masked_phone_number }}
```
{% endraw %}

## キャンバス、カタログ、およびトリガープロパティ {#canvas-catalogs-and-trigger-properties}

### APIトリガーのLiquidがBrazeで失敗するのはなぜですか？ {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
余分な波括弧のペアが一般的な原因です。例えば、`{{{api_trigger_properties.${attribute_key}}}}` は有効なBrazeパーソナライゼーション構文ではありません。開き波括弧2つと閉じ波括弧2つを正確に使用してください：`{{api_trigger_properties.${attribute_key}}}`。
{% endraw %}

### キャンバスコンテキストプロパティにサイズ制限はありますか？ {#are-there-size-limits-for-canvas-context-properties}

Brazeは[キャンバスコンテキストプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)にハードリミットを設けていませんが、ペイロードは約1 KB（約1,000文字）以下に抑えてください。大きなオブジェクトはメモリ使用量を増加させ、大量送信時にメッセージのレンダリングを遅延させる可能性があります。

### ダッシュボードで特定のデータ型をプレビューするとLiquidエラーが発生するのはなぜですか？ {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

一部の[キャンバスコンテキストプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)の型は、比較や計算で使用する前にLiquidでの型変換が必要です。例えば、数値としての動作が必要な場合は以下のようにします：

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### カタログのLiquidスニペットが中止メッセージを返すのはなぜですか？ {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

カタログのLiquidスニペットが送信中に中止される場合は、一括選択や完全にダイナミックな選択を使用する代わりに、パーソナライゼーションメニューから個々のカタログアイテムを選択してスニペットを再作成してください。詳細については、[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)および[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を参照してください。

## Content Blocksとメッセージ作成画面 {#content-blocks-and-the-message-composer}

### Content Blocksを使用するメッセージに余分なスペースが入るのはなぜですか？ {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Liquidを使用したContent Blocksで送信されたメッセージに余分なスペースが入る場合、条件文内に不要な段落や改行が含まれている可能性があります。条件文は複数行にまたがらず、1行で記述してください。

#### 例 {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}


### ドラッグ＆ドロップエディターで複数行のLiquidが予期しない空白を生成するのはなぜですか？ {#why-does-multi-line-liquid-create-unexpected-whitespace-in-the-drag-and-drop-editors}

アプリ内メッセージのドラッグ＆ドロップエディターやメールのドラッグ＆ドロップエディターでLiquidコードが複数行にまたがっている場合、各{% raw %}`{% %}`{% endraw %}ブロックは非表示テキストとしてレンダリングされます。改行は表示される出力の前に空行として保持されるため、予期しない空白が発生します。

#### 解決策1：空白制御タグを使用する（推奨） {#solution-1-use-whitespace-control-tags-recommended}

タグの区切り文字の内側にハイフンを追加して、コードの可読性を保ちながら周囲の空白を除去します。

{% raw %}
```liquid
{%- assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" -%}
{%- assign today = 'now' | date: "%s" -%}
{%- assign difference = event_date | minus: today -%}
{%- assign difference_days = difference | divided_by: 86400 -%}
Only {{ difference_days }} days until your move!
```
{% endraw %}

#### 解決策2：Liquidを1行にまとめる {#solution-2-consolidate-liquid-onto-a-single-line}

すべての改行を削除して、Liquidを1つの連続した行にします。

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" %}{% assign today = 'now' | date: "%s" %}{% assign difference = event_date | minus: today %}{% assign difference_days = difference | divided_by: 86400 %}Only {{ difference_days }} days until your move!
```
{% endraw %}

どちらの方法でも、レンダリングされたメッセージ内の不要な空行を防ぐことができます。これはアプリ内メッセージのドラッグ＆ドロップエディター、メールのドラッグ＆ドロップエディター、およびLiquidを使用したContent Blocksに適用されます。詳細については、Shopifyの[Whitespace control](https://shopify.github.io/liquid/basics/whitespace/)ドキュメントおよびBrazeの[Liquid構文]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax)を参照してください。

### ドラッグ＆ドロップの検索ツールで**行**にContent Blockが表示されないのはなぜですか？ {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

一部のContent Blocksは、ドラッグ＆ドロップエディターの検索で**行**の下に表示されません。**コンテンツ**タブ（**詳細**）からHTMLブロックを追加し、そのHTMLブロック内にContent BlockのLiquidタグを挿入してブロックコンテンツをレンダリングしてください。

### ドラッグ＆ドロップのContent Blockプレビューが作成ビューと異なるのはなぜですか？ {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Content BlockをLiquidでテンプレート化する場合、ブロック内のモバイルメディアクエリは、ブロックを直接メッセージにドラッグした場合と同じようにプレビューに適用されないことがあります。ブロックをドラッグするとレイアウトは保持されますが、ソースブロックから切り離されるため、今後のブロック編集がメッセージに自動的に反映されなくなります。

### メッセージ作成画面でイベントプロパティの値をプレビューするにはどうすればよいですか？ {#how-do-i-preview-event-property-values-in-message-composer}

**カスタムユーザーとしてプレビュー**を使用し、プレビューするユーザーのサンプルカスタムイベントプロパティ値を入力してください。これは、中止ロジックを含むメッセージで、中止をトリガーしないプレビュー値が必要な場合にも便利です。

## メールメッセージでのLiquid {#liquid-in-email-messages}

### 「Invalid from email address for recipient:」でメッセージが中止されるのはなぜですか？ {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

この中止は、**差出人**アドレス内のLiquidが無効な構文を生成した場合に発生します。例えば、変数の欠落、余分なスペース、許可されていない文字などが原因です。テストユーザーでプレビューし、レンダリングされた**差出人**アドレスが設定済みの送信ドメインと一致していることを確認してください。

### 動的な返信先アドレスを作成するにはどうすればよいですか？ {#how-do-i-create-a-dynamic-reply-to-address}

ワークスペースが動的な返信先設定をサポートしている場合、**返信先**フィールドでLiquidを使用してください。必要に応じて、**差出人**の表示名設定と組み合わせてください。ワークスペース固有のオプションについては、[メール設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)を参照してください。

## Liquidエラーのトラブルシューティング {#troubleshooting-liquid-errors}

### Liquidコードが正しく見えるのに動作しないのはなぜですか？ {#why-is-my-liquid-code-not-working-when-it-looks-correct}

Liquidコードの構文が正しいように見えるのに動作しない場合、ストレート引用符（`' '`や`" "`）やハイフン（`-`）の代わりに、スマート引用符（`' '`や`" "`のような丸い引用符）やスマートダッシュ（`—`のようなemダッシュ）が使用されていないか確認してください。LiquidはストレートASCII文字のみを認識するため、スマート引用符やダッシュはパースエラーの原因になります。

これは、macOSのキーボード設定で**スマート引用符とダッシュを使用**が有効になっている場合によく発生します。この設定により、Brazeダッシュボードで入力する際に文字が自動的に変換されます。

macOSでこの設定を無効にするには：

1. **システム設定** > **キーボード** > **テキスト入力** > **編集**に移動します。
2. **スマート引用符とダッシュを使用**のチェックを外します。

| 例 | 丸い引用符（動作しない） | ストレート引用符（動作する） |
| --- | --- | --- |
| デフォルト値 | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} |
| 条件分岐 | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="スマート引用符の例" }

これはデフォルト値、条件分岐、および引用符を使用するその他すべてのLiquidに適用されます。丸い引用符とストレート引用符は画面上では同じように見えることがあるため、コードを注意深く比較するか、プレーンテキストエディタに貼り付けて確認してください。

Liquidでの引用符の使用方法の詳細については、[Liquid構文]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax)を参照してください。

### 「Unexpected end token」というLiquidエラーが表示されるのはなぜですか？ {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

このエラーは通常、波括弧が余分にあるか不足していることを示しています。{% raw %}`{{ }}`{% endraw %}を別のLiquidタグ式の中にネストしないでください。例えば、属性参照を追加の波括弧で囲むのではなく、{% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %}を使用してください。

### アプリ内メッセージでConnected Contentのリトライが利用できないのはなぜですか？ {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
リトライ付きの`{% connected_content %}`タグは、一部のアプリ内メッセージ形式を含むすべてのメッセージタイプでサポートされているわけではありません。リトライパラメータを削除するか、リトライ付きConnected Content呼び出しに対応しているチャネルを使用してください。
{% endraw %}

### 「Liquid Error: Comparison of Time with String Failed」と表示されるのはなぜですか？ {#why-am-i-seeing-liquid-error-comparison-of-time-with-string-failed}

このエラーは、時間型のカスタム属性またはイベントプロパティを空の値（空文字列）と直接比較した場合に発生します。Liquidは、時間オブジェクトと文字列など、異なるデータ型間の直接比較をサポートしていません。

以下は、このエラーを引き起こす一般的な例です：

{% raw %}
```liquid
{% if {{custom_attribute.${expiration_date}}} == blank %}
  <a>Some words</a>
{% endif %}
```
{% endraw %}

これは、データ型が時間であるカスタム属性を文字列（`blank`）と比較できないため失敗します。

これを解決するには、時間属性を変数に割り当て、レンダリング時に属性が空と評価される場合に`default`フィルターを使用して文字列に変換します：

{% raw %}
```liquid
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% endif %}
```
{% endraw %}


時間型のカスタム属性を現在の時刻や将来の日付と比較する場合も、同じアプローチを使用します：

{% raw %}
```liquid
{% assign today = 'now' | date: '%s' %}
{% assign month = 'now' | date: '%s' | plus: 2592000 %}
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% elsif expiration_date >= today and expiration_date >= month %}
  <a>More Words</a>
{% endif %}
```
{% endraw %}