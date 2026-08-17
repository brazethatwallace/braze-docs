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

衣料小売ブランドのFlash & Threadは、Connected Contentのレスポンス、キャンバスコンテキスト変数、またはオブジェクト配列のプロファイルデータに依存するメッセージを作成しています。反復のたびに実際のAPI呼び出しをトリガーしたりキャンペーンを起動したりすると、開発が遅くなります。

このパターンでは、モックJSONペイロードをメッセージ本文に埋め込み、`capture` で格納してから `json_parse` で解析します。これにより、ライブのConnected Content呼び出し、APIトリガーのキャンバスエントリ、テスト送信なしに、**プレビュー**セクションでLiquidが構造化フィールドを参照できるようになります。

これはメッセージ開発中に使用してください。実際のトリガー、テスト送信、またはキャンバスの[ユーザーパスのプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)によるエンドツーエンドのテストの代わりにはなりません。

## 考慮事項 {#considerations}

- このアプローチは、開発中のメッセージ作成画面プレビューをサポートします。顧客に配信する前に、テスト送信とライブパスチェックを実行してください。
- `capture` ブロック単体ではJSONを文字列として格納します。**`json_parse`** を適用した後にのみフィールドを参照してください。適用しないと、プレビュー出力が空白になることがあります。
- モックJSONは有効な形式である必要があります。無効なJSONは `json_parse` の失敗や予期しない構造の返却を引き起こします。
- 起動前にモックブロックを置き換えるか削除するか、本番環境のLiquidをガードしてモックデータがプレビューでのみ使用されるようにしてください（たとえば、公開前に削除するコメントフラグを使用します）。
- この記事のLiquidスニペットは例です。ご利用のチャネルと実際のペイロード形式でテストしてください。
- 本番環境のConnected Contentでは、モックブロックを削除してライブURLタグを使用してください。[API呼び出しの実行]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を参照してください。

## 設定 {#setup}

この例では、`listings` をループするメールのConnected Contentスタイルの商品リストレスポンスをモックします。

### ステップ1: メッセージ内でモックJSONをキャプチャする {#step-1-capture-mock-json-in-the-message}

`capture` を使用してJSON文字列を保持します。ブロック内では有効なJSON構文（キーと文字列値にダブルクォート）を使用してください。

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

### ステップ2: json_parseでJSONを解析する {#step-2-parse-json-with-json_parse}

解析された構造をメッセージの残りの部分で参照する変数に割り当てます。

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

`json_parse` を使用しないと、キャプチャされた文字列に対するドット記法（たとえば {% raw %}`{{ mock_response.listings }}`{% endraw %}）は、プレビューで通常空白として表示されます。

### ステップ3: Liquidで解析済みフィールドを参照する {#step-3-reference-parsed-fields-in-liquid}

解析された配列をループし、ライブAPIレスポンスの場合と同様にフィールドをレンダリングします。

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

メッセージ作成画面の**プレビュー**セクションに移動し、フィールドがレンダリングされることを確認します。

### ステップ4: 他のJSON形式にも同じパターンを適用する {#step-4-apply-the-same-pattern-to-other-json-shapes}

同じ `capture` + `json_parse` フローを使用して、以下をモックします。

| テストしたいデータ | モックJSONの形式 |
| --- | --- |
| キャンバスコンテキスト変数 | メッセージが期待するプロパティキーを持つオブジェクト |
| プロファイル上のオブジェクト配列 | カスタム属性と同じキーを持つオブジェクトのJSON配列 |
| Connected Contentレスポンス | 以前の成功した呼び出しから保存したサンプルAPI JSON |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テストしたいデータとJSONの形式" }

起動前に、モック変数を本番環境のLiquid（キャンバスコンテキスト変数、カスタム属性、またはConnected Contentタグ）に置き換えてください。

## 関連記事 {#related-articles}

- [テストメッセージを送信する]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [キャンバスでユーザーパスをプレビューする]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [高度なLiquidフィルター（`json_parse`）]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [オブジェクト配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [コンテキスト変数]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)