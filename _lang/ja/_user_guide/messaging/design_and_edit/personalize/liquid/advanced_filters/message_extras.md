---
nav_title: メッセージエクストラタグ
article_title: メッセージエクストラタグ
page_order: 1
description: "この記事では、メッセージエクストラ Liquidタグの使用方法と構文の確認方法について説明します。"
alias: "/message_extras_tag/"
---

# メッセージエクストラ Liquidタグ {#message-extras-liquid-tag}

> `message_extras` Liquidタグを使用して、Connected Content、カタログ、カスタム属性（言語、国など）、キャンバスエントリプロパティ、またはその他のデータソースからのダイナミックなデータで送信イベントにアノテーションを付けます。

`message_extras` Liquidタグは、Currentsおよび Snowflake データ共有の対応する送信イベントにキーと値のペアを追加します。

ダイナミックなデータまたは追加データをCurrentsまたは Snowflake データ共有の送信イベントに返すには、メッセージ本文に適切な Liquidタグを挿入します。

以下は、`message_extras` の標準的な Liquidタグ形式の例です。

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

これらのタグは、メッセージ本文のキーと値のペアに必要に応じて追加できます。ただし、すべてのキーと値の長さの合計は1,000バイト（1&nbsp;KB）を超えないようにしてください。Currentsおよび Snowflake データ共有では、送信イベントに `message_extras` という新しいイベントフィールドが表示されます。これにより、1つのフィールドに JSONシリアライズされた文字列が生成されます。

## Currentsを使用したメッセージエクストラデータの送信方法 {#how-message-extras-data-is-sent-using-currents}

**メッセージエクストラ**は、送信時に付加されるキーと値のペアです。設定はチャネルによって異なります。メールの場合、ヘッダーを使用して追加されます。iOSプッシュの場合、プッシュペイロードに含まれます。サポートされているすべての送信イベントは、メッセージが送信されると、Currents（および Snowflake）で同じ `message_extras` フィールドを表示します。

## サポートされているチャネル {#supported-channels}

`message_extras` タグは、送信イベントを持つすべてのメッセージタイプと、アプリ内メッセージのインプレッションイベントでサポートされています。アプリ内メッセージで `message_extras` を使用するには、特定の[最小SDKバージョン](#iam-sdk)を満たす必要があります。

## `message_extras` タグの使用方法 {#how-to-use-the-message_extras-tag}

1. チャネルのメッセージ本文に、`message_extras` Liquidタグを入力します。または、**パーソナライゼーションを追加**モーダルを使用して、パーソナライゼーションタイプとして**メッセージエクストラ**を選択することもできます。

![パーソナライゼーションタイプとしてメッセージエクストラが選択されたパーソナライゼーションを追加モーダル。]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. 各 `message_extras` タグの[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を入力します。

![メッセージエクストラタグのキーと値のペアの例。タイトルフィールドには「Your New Favorites」と表示されています。メッセージにはメッセージエクストラタグのキーと値のペアと、次の文が表示されています：「We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites」]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. キャンペーンまたはキャンバスが送信された後、Brazeは送信時にCurrentsまたは Snowflake データ共有の送信イベントを通じて、ダイナミックなデータを `message_extras` フィールドに付加します。

## 構文の確認 {#checking-syntax}

上記のタグ標準に一致しないその他の入力は、Currentsまたは Snowflake に渡されない場合があります。構文やフォーマットに以下のいずれかが含まれていないことを確認してください。

- 存在しない、空の、または誤入力されたデリミタ
- 重複するキー（Brazeはデフォルトで最初に検出されたキーと値のペアを送信します）
- キーまたは値が定義される前の余分なテキスト
- 順序が正しくないキーと値
  - {% raw %}例：`{% message_extras :value 123 :key test %}`{% endraw %}

## プロモーションコード情報をCurrentsに送信する {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## 考慮事項 {#considerations}

- 1,000バイト（1&nbsp;KB）を超えるキーと値は切り捨てられます。
- 空白は文字数にカウントされます。Brazeは先頭と末尾の空白を省略することに注意してください。
- 結果のJSONは文字列値のみを出力します。
- Liquid変数をキーまたは値として含めることができますが、`message_extras` 内に追加のLiquidタグをネストすることはできません。
  - 例えば、次のLiquidを使用できます：{% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## よくある質問 {#frequently-asked-questions}

### 送信イベントのmessage_extrasフィールドを、開封やクリックなどのエンゲージメントイベントに関連付けるにはどうすればよいですか？ {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

`dispatch_id` が生成され、送信イベントに提供されます。これは、特定のクリック、開封、または配信イベントに紐付けるためのユニークな識別子として使用できます。このフィールドはCurrentsまたは Snowflake でクエリできます。詳しくは、[Dispatch IDの動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)をご覧ください。

#### アプリ内メッセージでmessage_extrasを使用できますか？ {#iam-sdk}

はい、ユーザーのデバイスが以下の最小SDKバージョンを満たしている限り、アプリ内メッセージで `message_extras` を使用できます。

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}