---
nav_title: カタログの使用
article_title: カタログの使用
page_order: 1.5
description: "この参照記事では、Liquidを通してBrazeのキャンペーンで非ユーザーデータを参照するためにカタログを使用する方法について説明します。"
---

# カタログの使用 {#using-catalogs}

> カタログを作成した後、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用して、Brazeのキャンペーンで非ユーザーデータを参照できます。Liquidがサポートされているドラッグ＆ドロップエディター内の任意の場所を含む、すべてのメッセージングチャネルでカタログを使用できます。

## メッセージでのカタログの使用 {#using-catalogs-in-a-message}

以下の動画では、メッセージでカタログを使用する方法について説明します。

{% multi_lang_include video.html id="4yc2jkyn6w" source="wistia" %}

### ステップ1：パーソナライゼーションタイプを追加する {#step-one-personalization}

任意のメッセージ作成画面で、<i class="fas fa-plus-circle"></i>**パーソナライゼーションを追加**を選択し、**パーソナライゼーションタイプ**として**カタログアイテム**を選択します。次に、カタログ名を選択します。前の例を使用して、「Games」カタログを選択します。

![「カタログアイテム」が選択され、Gamesカタログが選ばれ、catalog_itemsタグを表示するLiquidプレビューが表示されている「パーソナライゼーションを追加」モーダル。]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

すぐに以下のLiquidプレビューが表示されます。

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### ステップ2：カタログアイテムを選択する {#step-2-select-catalog-items}

次に、カタログアイテムを追加します。ドロップダウンを使用して、カタログアイテムと表示する情報を選択します。この情報は、カタログの生成に使用されたアップロード済みCSVファイルの列に対応しています。

たとえば、Talesゲームのタイトルと価格を参照するには、カタログアイテムとしてTalesの`id`（1234）を選択し、表示情報として`title`と`price`をリクエストします。

{% raw %}
```liquid
{% catalog_items Games 1234 %}

Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

これは以下のように表示されます。

> Get Tales for just 7.49!

## カタログのエクスポート {#exporting-catalogs}

ダッシュボードからカタログをエクスポートするには、2つの方法があります。

- **カタログ**セクションでカタログの行にカーソルを合わせます。次に、**カタログをエクスポート**ボタンを選択します。
- カタログを選択します。次に、カタログの**プレビュー**タブで**カタログをエクスポート**ボタンを選択します。

エクスポートを開始すると、CSVファイルをダウンロードするためのメールが届きます。このファイルの取得には最大4時間かかる場合があります。

## その他のユースケース {#additional-use-cases}

### 複数のアイテム {#multiple-items}

メッセージ内のアイテムは1つに限定されません。**パーソナライゼーションを追加**モーダルを使用して、一度に最大3つのカタログアイテムを追加できます。さらに追加するには、メッセージ作成画面で再度**パーソナライゼーションを追加**を選択し、追加のカタログアイテムと表示する情報を選択します。

以下の例では、Tales、Teslagrad、Acaratusの3つのゲームの`id`を**カタログアイテム**に追加し、**表示する情報**に`title`を選択しています。

![3つのカタログアイテムIDが選択され、表示する情報にタイトルが選択されたパーソナライゼーション追加モーダル。各アイテムタイトルを一覧表示するLiquidプレビュー付き。]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Liquidの周囲にテキストを追加して、メッセージをさらにパーソナライズできます：

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

これは次のように表示されます：

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

この例では、`catalog_items`タグが`Games`カタログからアイテム`1234`を取得し、`if`ステートメントが`on_sale`フィールドをチェックして異なるメッセージを表示します。

#### カタログセレクションの場合

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters.
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer.
{% else %}
{% abort_message('no venue_name') %}
{% endif %}
```
{% endraw %}

この例では、`venue_name`フィールドが10文字を超えるかどうかに基づいて異なるメッセージが表示されます。`venue_name`が空白の場合、メッセージは中止されます。

セレクションが返すアイテムの数を出力するには、タグの後の`items`配列に対してLiquidの`size`フィルターを使用します（単一のフィールドに対してではありません）：

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}{{ items | size }}
```
{% endraw %}

{% alert tip %}
Liquid構文エラーを回避するには、メッセージ作成画面の**+**ボタンを選択して、カタログのLiquidタグを自動的に挿入してください。
{% endalert %}

### 画像の使用 {#using-images}

カタログ内の画像を参照してメッセージングで使用することもできます。これを行うには、画像のLiquidフィールドで`catalogs`タグと`item`オブジェクトを使用します。

たとえば、GamesカタログのTalesのプロモーションメッセージに`image_link`を追加するには、**カタログアイテム**フィールドに`id`を、**表示する情報**フィールドに`image_link`を選択します。これにより、画像フィールドに次のLiquidタグが追加されます：

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![画像フィールドにカタログのLiquidタグが使用されたContent カードメッセージ作成画面。]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Liquidがレンダリングされると次のようになります：

![カタログのLiquidタグがレンダリングされたContent カードの例。]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

{% alert important %}
メールなどの**HTML**チャネルでは、`{% raw %}{% catalog_items ... %}{% endraw %}`の閉じタグと画像URLを出力するLiquid（例：`{% raw %}{{ items[0].image_link }}{% endraw %}`）の間に余分なスペースや改行を入れないでください。テンプレート内の余分な空白は、レンダリングされたメッセージで画像URLが正しく解決されない原因となる場合があります。次のように、URL式をカタログタグの直後に配置してください：`{% raw %}<img src="{% catalog_items Games 1234 %}{{ items[0].image_link }}">{% endraw %}`。
{% endalert %}

### カタログアイテムのテンプレート化

テンプレートを使用して、カスタム属性に基づいてカタログアイテムを動的に取得することもできます。たとえば、ユーザーがカタログのゲームIDの配列を含むカスタム属性`wishlist`を持っているとします。

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
カタログ内のJSONオブジェクトはAPIを通じてのみ取り込まれます。CSVファイルを使用してJSONオブジェクトをアップロードすることはできません。
{% endalert %}

Liquidテンプレートを使用して、ウィッシュリストIDを動的に取り出し、メッセージで使用できます。これを行うには、カスタム属性に[変数を割り当て]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables)、**パーソナライゼーションを追加**モーダルを使用して配列から特定のアイテムを取得します。カタログアイテムIDとして参照される変数は、正しく参照されるように中括弧で囲む必要があります（例：`{{result}}`）。

{% alert tip %}
配列は`1`ではなく`0`から始まることを忘れないでください。
{% endalert %}

たとえば、Tales（ユーザーがウィッシュリストに追加したカタログ内のアイテム）がセール中であることをユーザーに知らせるには、メッセージ作成画面に次を追加します：

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

これは次のように表示されます：
> Get Tales now for just 7.49!

テンプレートを使用すると、各ユーザーの個別のカスタム属性、イベントプロパティ、またはその他のテンプレート可能なフィールドに基づいて、異なるカタログアイテムをレンダリングできます。

### CSVのアップロード

新しいカタログアイテムを追加したり、カタログアイテムを更新したりするためにCSVをアップロードできます。アイテムのリストを削除するには、アイテムIDのCSVをアップロードして削除できます。

### Liquidの使用

Liquidロジックを使用して手動でカタログを構成することもできます。ただし、存在しないIDを入力した場合、Brazeはオブジェクトのないitems配列を返すことに注意してください。配列のサイズを確認し、空の配列ケースに対応するために`if`ステートメントを使用するなど、エラーハンドリングを含めることをお勧めします。

#### Liquidを含むカタログアイテムのテンプレート化

[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)と同様に、カタログアイテムのLiquidコンテンツをレンダリングするには、Liquidタグで`:rerender`フラグを使用する必要があります。`:rerender`フラグは1レベルの深さのみであり、ネストされたLiquidタグの呼び出しには適用されません。

カタログアイテムにユーザープロファイルフィールド（Liquidパーソナライゼーションタグ内）が含まれている場合、Liquidを正しくレンダリングするために、これらの値はメッセージ内でテンプレートの前に先にLiquidで定義する必要があります。`:rerender`フラグが提供されない場合、生のLiquidコンテンツがレンダリングされます。

たとえば、「Messages」というカタログに次のLiquidを含むアイテムがある場合：

![idがgreet_msgで、Welcome_Message列にLiquid変数による名を含む「Welcome to our store」というテキストが表示されたカタログテーブル行。]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

次のLiquidコンテンツをレンダリングするには：

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

これは次のように表示されます：

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
カタログのLiquidタグは、カタログ内で再帰的に使用することはできません。
{% endalert %}

## カタログパーソナライゼーションのトラブルシューティング

カタログまたはセレクションのLiquidがメッセージやキャンバスステップで期待どおりに表示されない場合は、以下を確認してください。

| 症状 | 確認事項 |
| --- | --- |
| プレビューではアイテムが表示されるが、実際の送信では空になる | 送信時にカタログの**アイテムID**が存在することを確認してください。Liquid内のIDが行と一致しない場合、Brazeは空のアイテム配列を返します。[Liquidの使用](#using-liquid)を参照してください。タイプミスや、トリガーまたはユーザープロファイルに存在しないIDソース（イベントプロパティなど）がないか確認してください。 |
| メッセージ作成画面のプレビューはキャンペーンでは動作するがキャンバスでは動作しない | 正しいLiquidコンテキスト（**キャンバスコンテキストプロパティ**と**イベントプロパティ**）を使用しているか、またそれらのフィールドがトリガーに存在するか確認してください。[コンテキストプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を参照してください。 |
| セレクションがアイテムを返さない | [セレクションフィルター]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)と制限を確認してください。カタログデータが同期されていること、およびカラム名がフィルターと一致していることを確認してください。 |
| `:rerender`またはテンプレート配信が正しく表示されない | カタログフィールド内のネストされたLiquidには、`:rerender`と変数の正しい順序が必要です。[Liquidを含むカタログアイテムのテンプレート化](#templating-catalog-items-including-liquid)を参照してください。テンプレートアプリ内メッセージはトリガー時に解決されます。[テンプレートアプリ内メッセージとは？]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages)を参照してください。一部のチャネルではカタログタグが制限されています（例：バナーでの特定の**:rerender**の使用）。バナーFAQの[すべてのLiquidタグがサポートされていますか？]({{site.baseurl}}/user_guide/channels/banners/faq#are-all-liquid-tags-supported)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カタログパーソナライゼーションのトラブルシューティング" }

一般的なLiquidの動作については、[Liquidユースケース]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)および[Liquidの使用]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)を参照してください。

## カタログデータの構造化

カタログデータの構造を計画する際は、意図するユースケースから始めて、それに合わせてカタログを設計します。カタログの各行は1つのアイテム（一意の`id`を持つ）を表します。列にはそのアイテムの属性（URL、説明文、画像URL、価格、評価、サイズ、色など）を含める必要があります。

### 標準カタログ呼び出しを使用する場合

標準カタログ呼び出しでは、`id`列に対して値をマッチングします。カスタム属性またはイベントプロパティ（ID文字列として）をカタログのLiquidタグに挿入することで、1つのアイテムの複数の属性をメッセージに取り込むことができます。一般的なユースケースには以下が含まれます：

- 最近閲覧した商品またはサービス
- ウィッシュリストのアイテム
- 場所別のお得情報
- 購入済みの商品
- ライフサイクルステージのコンテンツ
- 最近検索した商品またはサービス

### カタログセレクションを使用する場合

[カタログセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を使用すると、カタログの任意の列をフィルタリングし、最大50件のマッチするアイテムを返すことができます。カスタム属性またはイベントプロパティをセレクションフィルターに挿入することで、結果は各ユーザーにパーソナライズされます。一般的なユースケースには以下が含まれます：

- カテゴリがユーザーの好みと一致するアイテム
- ユーザーが好むブランド、料理ジャンル、またはサイズに一致するアイテム
- サブスクリプションタイプまたはロイヤルティティアのコンテンツ
- ユーザーの平均注文額の範囲内にある商品

主な違いは、標準カタログ呼び出しは`id`で単一の既知のアイテムを検索するのに対し、カタログセレクションはカタログ全体をクエリしてフィルター条件に一致する複数のアイテムを返す点です。

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}