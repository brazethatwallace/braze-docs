---
nav_title: 高度なフィルター
article_title: 高度な Liquid フィルター
page_order: 4
description: "このリファレンス記事では、高度なフィルター、例、およびキャンペーンでの使用方法について説明します。"

---

# 高度なフィルター {#advanced-filters}

> このリファレンス記事では、Liquidの高度なフィルターの概要と使用方法について説明します。

## エンコーディングフィルター {#encoding-filters}

{% raw %}
| フィルター名 | フィルターの説明 | 入力例 | 出力例 |
|---|---|---|---|
| `md5` | md5 エンコードされた文字列を返します | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
| `sha1` | sha1 エンコードされた文字列を返します | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
| `sha2` | sha2（256ビット、SHA-256とも呼ばれます）エンコードされた文字列を返します | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
| `base64` | base64 エンコードされた文字列を返します | `{{'blah' | base64_encode}}` | YmxhaA== |
| `hmac_sha1_hex`（以前は `hmac_sha1`） | 16進文字列としてエンコードされた hmac-sha1 署名を返します | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
| `hmac_sha1_base64` | base64 文字列としてエンコードされた hmac-sha1 署名を返します | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
| `hmac_sha256_hex` | 16進文字列としてエンコードされた hmac-sha256 署名を返します | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
| `hmac_sha256_base64` | base64 文字列としてエンコードされた hmac-sha256 署名を返します | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Encoding filters" }

## URL フィルター {#url-filters}

| フィルター名 | フィルターの説明 | 入力例 | 出力例 |
|---|---|---|---|
| `url_escape` | URLで許可されていない文字列内のすべての文字を識別し、エスケープされた形式に置き換えます | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | URLで許可されていない文字列内のすべての文字を、アンパサンド（&）を含め、エスケープされた形式に置き換えます | `{{'hey<&>hi' | url_param_escape}}` | hey%3C%26%3Ehi |
| `url_encode` | URLに適した形式で文字列をエンコードします | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="URL filters" }

{% endraw %}
{% alert tip %}
`assign` タグをHTMLと組み合わせることで、複数のハイパーリンクを作成する際の時間と手間を節約できます。
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## プロパティアクセサーフィルター {#property-accessor-filter}

| フィルター名 | フィルターの説明 |
| --- | --- |
| `property_accessor` | ハッシュとハッシュキーを受け取り、そのキーに対応するハッシュ内の値を返します |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Property accessor filter" }

**ハッシュの例:** `{"a" => 42, "b" => 0}`
**入力例:** `{{hash | property_accessor: 'a'}}`
**出力例:** `42`

さらに、プロパティアクセサーフィルターを使用すると、カスタム属性をハッシュキーにテンプレート化して、特定のハッシュ値にアクセスできます。

{% endraw %}

{% alert note %}
Braze内のLiquidでは、ハッシュを変数（式など）としてインスタンス化する方法はありません。
{% endalert %}

{% raw %}

## 数値フォーマットフィルター {#number-formatting-filters}

| フィルター名 | フィルターの説明 | 入力例 | 出力例 |
|---|---|---|---|
| `number_with_delimiter` | 数値をカンマ区切りでフォーマットします | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number formatting filters" }

## JSON エスケープ / 文字列エスケープフィルター {#json-escape-or-string-escape-filter}

| フィルター名 | フィルターの説明 |
|---|---|
| `json_escape` | 文字列内の特殊文字（ダブルクォート `""` やバックスラッシュ '\' など）をエスケープします。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON escape or string escape filter" }

このフィルターは、JSON ディクショナリ内の文字列をパーソナライズする際に常に使用する必要があり、特にWebhookで役立ちます。

## JSON フォーマットフィルター {#json-formatting-filters}

| フィルター名 | フィルターの説明 |
|---|---|
| `json_parse` | JSON 文字列を、オブジェクトや配列などの対応するデータ構造に変換します。 |
| `as_json_string` | オブジェクトや配列などのデータ構造を、対応する JSON 文字列に変換します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON-formatting filters" }

{% endraw %}

{% details json_parse の入力例と出力例 %}

### 入力 {#input}

{% raw %}
`````````liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### 出力 {#output}

`````````liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details as_json_string の入力例と出力例 %}

### 入力

{% raw %}
`````````liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### 出力

`````````liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values