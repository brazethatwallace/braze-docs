---
nav_title: メッセージエクストラタグ
article_title: メッセージエクストラタグ
page_order: 1
description: "この記事では、メッセージエクストラLiquidタグの使用方法と構文の確認方法について説明します。"
alias: "/message_extras_tag/"
---

# メッセージエクストラLiquidタグ {#message-extras-liquid-tag}

> `message_extras` Liquidタグを使用して、Connected Content、カタログ、カスタム属性（言語、国など）、キャンバスエントリプロパティ、またはその他のデータソースからのダイナミックなデータで送信イベントにアノテーションを付けます。

`message_extras` Liquidタグは、CurrentsおよびSnowflakeデータ共有の対応する送信イベントにキーと値のペアを追加します。

ダイナミックなデータまたは追加データをCurrentsまたはSnowflakeデータ共有の送信イベントに返すには、メッセージ本文に適切なLiquidタグを挿入します。

以下は、`message_extras` の標準的なLiquidタグ形式の例です。

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

これらのタグは、メッセージ本文のキーと値のペアに必要に応じて追加できます。ただし、すべてのキーと値の長さの合計は1,000バイト（1&nbsp;KB）を超えないようにしてください。CurrentsおよびSnowflakeデータ共有では、送信イベントに `message_extras` という新しいイベントフィールドが表示されます。これにより、1つのフィールドにJSONシリアライズされた文字列が生成されます。

{% alert note %}
メールエクストラはメールサービスプロバイダー（ESP）にメタデータを送信するもので、CurrentsやSnowflakeには公開されません。CurrentsやSnowflakeの送信イベントにメタデータやダイナミックな値を追加するには、`message_extras` Liquidタグを使用してください。
{% endalert %}

## メッセージエクストラデータがCurrentsを使用して送信される仕組み {#how-message-extras-data-is-sent-using-currents}

**メッセージエクストラ**は、送信時に付与されるキーと値のペアです。設定方法はチャネルによって異なります。メールの場合はヘッダーを使用して追加されます。iOSプッシュの場合はプッシュペイロードに含まれます。サポートされているすべての送信イベントでは、メッセージが送信されるとCurrents（およびSnowflake）で同じ`message_extras`フィールドが表示されます。

## サポートされているチャネル {#supported-channels}

`message_extras`タグは、送信イベントを持つすべてのメッセージタイプと、アプリ内メッセージのインプレッションイベントでサポートされています。アプリ内メッセージで`message_extras`を使用するには、特定の[最小SDKバージョン](#iam-sdk)を満たす必要があります。

## `message_extras`タグの使い方 {#how-to-use-the-message_extras-tag}

1. チャネルのメッセージ本文に`message_extras` Liquidタグを入力します。または、**パーソナライゼーションを追加**モーダルを使用して、パーソナライゼーションタイプとして**Message Extras**を選択することもできます。

![パーソナライゼーションタイプとしてMessage Extrasが選択されたパーソナライゼーションを追加モーダル。]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. 各`message_extras`タグの[キーと値のペア]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs)を入力します。

![message extrasタグのキーと値のペアの例。タイトルフィールドには「Your New Favorites」と表示されています。メッセージにはmessage extrasタグのキーと値のペアと、次の文が表示されています：「We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites」]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. キャンペーンまたはキャンバスが送信された後、Brazeは送信時にダイナミックなデータをCurrentsまたはSnowflakeデータ共有の送信イベントの`message_extras`フィールドに添付します。

## 構文の確認 {#checking-syntax}

このセクションで前述したタグ標準に一致しないその他の入力は、CurrentsやSnowflakeへの受け渡しに失敗する可能性があります。構文やフォーマットに以下のいずれかが含まれていないことを確認してください。

- 存在しない、空の、または誤入力されたデリミタ
- 重複するキー（Brazeはデフォルトで最初に検出されたキーと値のペアを送信します）
- キーや値が定義される前の余分なテキスト
- キーと値の順序の誤り
  - {% raw %}例: `{% message_extras :value 123 :key test %}`{% endraw %}

## Currentsへのプロモーションコード情報の送信 {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## 考慮事項 {#considerations}

- 1,000バイト（1&nbsp;KB）を超えるキーと値のペアは切り捨てられます。
- 空白は文字数にカウントされます。なお、Brazeは先頭と末尾の空白を省略します。
- 結果のJSON出力は文字列値のみです。
- Liquid変数をキーまたは値として含めることができますが、`message_extras`の中に追加のLiquidタグをネストすることはできません。
  - たとえば、次のLiquidを使用できます：{% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## よくある質問 {#frequently-asked-questions}

### 送信イベントのmessage_extrasフィールドを、開封やクリックなどのエンゲージメントイベントに関連付けるにはどうすればよいですか？ {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

`dispatch_id`が生成され、送信イベントに含まれます。これを一意の識別子として使用して、特定のクリック、開封、または配信イベントに紐付けることができます。このフィールドはCurrentsまたはSnowflakeでクエリできます。詳細については、[ディスパッチIDの動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id)を参照してください。

#### アプリ内メッセージでmessage_extrasを使用できますか？ {#iam-sdk}

はい、ユーザーのデバイスが以下の最小SDKバージョン以上であれば、アプリ内メッセージで`message_extras`を使用できます。

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}