---
nav_title: ユーザープロファイルデータの取得
article_title: Connected Content呼び出しでのユーザープロファイルデータの取得
page_order: 3
description: "この記事では、Connected Content呼び出しにユーザープロファイルを取り込む方法と、Liquidテンプレートに関するベストプラクティスについて説明します。"
toc_headers: h2
---

# Connected Content呼び出しでのユーザープロファイルデータの取得 {#pull-user-profile-data-in-connected-content-calls}

> このページでは、Connected Content呼び出しにユーザープロファイルを取り込む方法と、Liquidテンプレートに関するベストプラクティスについて説明します。

## 前提条件 {#prerequisites}

Connected Contentの応答にユーザープロファイルフィールド（Liquidパーソナライゼーションタグ内）が含まれている場合、Liquidのパスバックを正しくレンダリングするために、これらの値はConnected Content呼び出しの前に、メッセージ内でLiquidを使用してあらかじめ定義しておく必要があります。同様に、リクエストには`:rerender`フラグを含める必要があります。`:rerender`フラグは1階層のみ有効であり、ネストされたConnected Contentタグには適用されないことに注意してください。

## Connected Content呼び出しでのLiquidテンプレート {#liquid-templating-in-connected-content-calls}

パーソナライゼーションでは、Brazeはユーザープロファイルフィールドを取得してからLiquidに渡します。そのため、Connected Contentからの応答にユーザープロファイルフィールドが含まれている場合は、事前に定義しておく必要があります。

例えば、以下のようなConnected Content呼び出しがあるとします。
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

Connected Contentの応答が{% raw %}`Your language is ${language}`{% endraw %}の場合、この例で表示されるコンテンツは`Hi Jon, your language is`となります。

言語自体はテンプレート化されません。これは、BrazeがConnected Content呼び出しを行う前に、ユーザーからどのフィールドを取得するかを把握しておく必要があるためです。

Liquidのパスバックを正しくレンダリングするには、以下のコードスニペットに示すように、リクエストのどこかに{% raw %}`${language}`{% endraw %}タグを含める必要があります。Liquidプリプロセッサーは、応答のテンプレート化に備えて、ユーザーから「language」属性を取得することを認識します。

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
`:rerender`フラグオプションは1階層のみ有効であることを忘れないでください。Connected Contentの応答自体にさらにConnected Contentタグやカタログタグが含まれている場合、Brazeはそれらの追加タグを再レンダリングしません。
{% endalert %}

## ベストプラクティス {#best-practices}

### JSON形式を壊す可能性のあるLiquidタグには`json_escape`を使用する {#use-json_escape-with-liquid-tags-that-could-break-the-json-format}

`:rerender`を使用する場合、JSON形式を壊す可能性のあるLiquidタグには`json_escape`フィルターを追加してください。LiquidタグにJSON形式を壊す文字が含まれていると、Connected Contentの応答全体がテキストとして解釈されてメッセージにテンプレート化され、変数は一切保存されません。

例えば、以下のセクションの例で`message`イベントプロパティにJSON形式を壊す可能性のある文字が含まれている場合、この例のように`json_escape`フィルターを追加します。

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}