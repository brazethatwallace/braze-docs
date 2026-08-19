---
nav_title: モック JSON でメッセージをテストする
article_title: プレビューでモック JSON を使用してメッセージをテストする
page_order: 1
page_type: reference
description: "Liquidのcaptureとjson_parseを使用して、キャンペーンの起動やテストメッセージの送信なしに、メッセージ作成画面のプレビューでConnected Contentやエントリスタイルの JSON をモックできます。"
---

# プレビューでモック JSON を使用してメッセージをテストする {#test-messages-with-mock-json-in-preview}

> `capture` と `json_parse` を使用して、メッセージ内でAPIやエントリスタイルのJSONをモックすることで、キャンペーンの起動、キャンバスのトリガー、Connected Contentのライブ呼び出しを行う前に、メッセージ作成画面のプレビューでLiquidとレイアウトを検証できます。

## この例について {#about-this-example}

架空の衣料小売ブランド Flash & Thread は、Connected Contentのレスポンス、キャンバスのコンテキスト変数、またはオブジェクト配列のプロファイルデータに依存するメッセージを作成しています。イテレーションのたびに実際のAPI呼び出しをトリガーしたりキャンペーンを起動したりすると、開発が遅くなります。

このパターンでは、モックJSONペイロードをメッセージ本文に埋め込み、`capture` で保存してから `json_parse` で解析することで、ライブのConnected Content呼び出し、APIトリガーのキャンバスエントリ、またはテスト送信なしに、**プレビュー**セクションでLiquidが構造化フィールドを参照できるようにします。

このパターンはメッセージ開発中に使用してください。実際のトリガー、テスト送信、またはキャンバスでの[ユーザーパスのプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)を使ったエンドツーエンドのテストに代わるものではありません。

## 注意事項 {#considerations}

- このアプローチは、開発中のメッセージ作成画面プレビューをサポートします。顧客に配信する前に、テスト送信とライブパスの確認を実行してください。
- `capture` ブロック単体では JSON を文字列として保存します。フィールドを参照するのは **`json_parse`** を適用した後にしてください。適用しない場合、プレビュー出力が空白になることがあります。
- モック JSON は有効な形式である必要があります。無効な JSON は `json_parse` の失敗や予期しない構造の返却を引き起こします。
- 配信前にモックブロックを置き換えるか削除するか、本番環境の Liquid でモックデータがプレビューでのみ使用されるようにガードしてください（例えば、本番稼働前に削除するコメントフラグを使用するなど）。
- この記事の Liquid スニペットは例です。ご利用のチャネルと実際のペイロード構造でテストしてください。
- 本番環境の Connected Content では、モックブロックを削除してライブ URL タグを使用してください。詳しくは [API コールの実行]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を参照してください。

## 設定 {#setup}

この例では、`listings` をループするメールのために、Connected Content スタイルの商品リスト応答をモックします。

### ステップ1: メッセージ内でモック JSON をキャプチャする {#step-1-capture-mock-json-in-the-message}

`capture` を使用して JSON 文字列を保持します。ブロック内では有効な JSON 構文（キーと文字列値にダブルクォート）を使用してください。

{% raw %}
```liquid
{% capture mock_response %}
{
  "success": true,
  "listings": [
    {
      "id": 45731,
      "name": "Summit Trail Jacket",
      "image_url": "https://example.com/images/trail-jacket.png",
      "price": {
        "actual": "89.00",
        "currency": "USD"
      },
      "link": "https://example.com/products/trail-jacket",
      "product_category": "Outerwear",
      "properties": {
        "size": "L",
        "colour": "Navy",
        "limited_edition": false
      },
      "out_of_stock": false
    }
  ]
}
{% endcapture %}
```
{% endraw %}

### ステップ2: json_parse で JSON を解析する {#step-2-parse-json-with-json_parse}

解析された構造を変数に割り当て、メッセージの残りの部分で参照します。

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

`json_parse` を使用しない場合、キャプチャした文字列に対するドット記法（例: {% raw %}`{{ mock_response.listings }}`{% endraw %}）は、プレビューで通常空白として表示されます。

### ステップ3: Liquid で解析済みフィールドを参照する {#step-3-reference-parsed-fields-in-liquid}

解析された配列をループし、ライブ API レスポンスの場合と同様にフィールドをレンダリングします。

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

メッセージ作成画面の**プレビュー**セクションに移動し、フィールドが正しくレンダリングされることを確認します。

### ステップ4: 他の JSON 形状にも同じパターンを適用する {#step-4-apply-the-same-pattern-to-other-json-shapes}

同じ `capture` + `json_parse` フローを使用して、以下をモックします。

| テストしたいデータ | モック JSON の形状 |
| --- | --- |
| キャンバスコンテキスト変数 | メッセージが期待するプロパティキーを持つオブジェクト |
| プロファイル上のオブジェクト配列 | カスタム属性と同じキーを持つオブジェクトの JSON 配列 |
| Connected Content レスポンス | 以前の成功した呼び出しから保存したサンプル API JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テストしたいデータと JSON の形状" }

ローンチ前に、モック変数を本番用の Liquid（キャンバスコンテキスト変数、カスタム属性、または Connected Content タグ）に置き換えてください。

## 関連記事 {#related-articles}

- [テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [キャンバスでユーザーパスをプレビューする]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [高度なLiquidフィルター (`json_parse`)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [コンテキスト変数]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)