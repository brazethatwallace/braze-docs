---
nav_title: カタログの使用
article_title: カタログの使用
page_order: 1.5
description: "この参照記事では、Liquidを通してBrazeのCampaignで非ユーザーデータを参照するためにカタログを使用する方法について説明します。"
---

# カタログの使用 {#using-catalogs}

> カタログを作成した後、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を使用して、BrazeのCampaignで非ユーザーデータを参照できます。Liquidがサポートされているドラッグ＆ドロップエディター内の任意の場所を含む、すべてのメッセージングチャネルでカタログを使用できます。

## メッセージでカタログを使う {#using-catalogs-in-a-message}

以下の動画では、メッセージでカタログを使用する方法を説明しています。

{% multi_lang_include video.html id="4yc2jkyn6w" source="wistia" %}

### ステップ 1:パーソナライゼーションタイプを追加する {#step-one-personalization}

任意のメッセージ作成画面で、<i class="fas fa-plus-circle"></i>**Add Personalization**を選択し、**Personalization type**として**Catalog Items**を選択します。次に、カタログ名を選択します。先ほどの例を使って、「Games」カタログを選択します。

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

以下のLiquidプレビューがすぐに表示されます。

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### ステップ 2:カタログアイテムを選択する {#step-2-select-catalog-items}

次に、カタログアイテムを追加します。ドロップダウンを使って、カタログアイテムと表示する情報を選択します。この情報は、カタログを生成するために使用された、アップロード済みのCSVファイルの列に対応しています。

例えば、Talesゲームのタイトルと価格を参照するには、カタログアイテムとしてTalesの`id`（1234）を選択し、表示する情報として`title`と`price`をリクエストします。

{% raw %}
```liquid
{% catalog_items Games 1234 %}

Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

これは次のように表示されます。

> Get Tales for just 7.49!

## カタログのエクスポート {#exporting-catalogs}

ダッシュボードからカタログをエクスポートするには、次の2つの方法があります。

- **Catalogs**セクションのカタログ行にカーソルを合わせます。次に、**Export catalog**ボタンを選択します。
- カタログを選択します。次に、カタログの**Preview**タブで**Export catalog**ボタンを選択します。

エクスポートを開始すると、CSVファイルをダウンロードするためのメールが届きます。このファイルの取得期限は最大4時間です。

## その他のユースケース {#additional-use-cases}

### 複数のアイテム {#multiple-items}

メッセージで使用できるアイテムは1つだけではありません。**Add Personalization**モーダルを使って、一度に最大3つのカタログアイテムを追加できます。さらに追加するには、作成画面で再度**Add Personalization**を選択し、追加のカタログアイテムや表示する情報を選びます。

この例では、Tales、Teslagrad、Acaratusの3つのゲームの`id`を**Catalog Items**に追加し、**Information to Display**として`title`を選択します。

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Liquidの周りにテキストを追加することで、メッセージをさらにパーソナライズできます。

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

これは以下のように返されます。

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to create groups of data for more personalized messaging!
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

この例では、`venue_name`フィールドの文字数が10文字より多いか少ないかによって、異なるメッセージが表示されます。`venue_name`が空白の場合、メッセージは中止されます。

{% alert tip %}
Liquidの構文エラーを避けるには、メッセージ作成画面の**+**プラスボタンを選択して、カタログのLiquidタグを自動的に挿入してください。
{% endalert %}

### 画像の使用 {#using-images}

カタログ内の画像を参照してメッセージングで使用することもできます。そのためには、画像のLiquidフィールドで`catalogs`タグと`item`オブジェクトを使用します。

例えば、Gamesカタログの`image_link`をTalesのプロモーションメッセージに追加するには、**Catalog Items**フィールドで`id`を選択し、**Information to Display**フィールドで`image_link`を選択します。これにより、以下のLiquidタグが画像フィールドに追加されます。

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![画像フィールドで使用されるカタログのLiquidタグを含むコンテンツカード作成画面。]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Liquidがレンダリングされると、次のように表示されます。

![カタログのLiquidタグをレンダリングしたコンテンツカードの例。]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

{% alert important %}
メールなどの**HTML**チャネルでは、閉じタグ`{% raw %}{% catalog_items ... %}{% endraw %}`と画像URLを出力するLiquid（例: `{% raw %}{{ items[0].image_link }}{% endraw %}`）の間に余分なスペースや改行を入れないでください。テンプレート内の余分な空白により、レンダリングされたメッセージで画像URLが正しく解決されない場合があります。URL式はカタログタグのすぐ隣に配置してください。例: `{% raw %}<img src="{% catalog_items Games 1234 %}{{ items[0].image_link }}">{% endraw %}`
{% endalert %}

### カタログアイテムのテンプレート化

テンプレート化を使って、カスタム属性に基づいてカタログアイテムをダイナミックに取得することもできます。例えば、あるユーザーがカスタム属性`wishlist`（カタログのゲームIDの配列）を持っているとします。

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
カタログ内のJSONオブジェクトは、APIを介してのみ取り込まれます。CSVファイルを使用してJSONオブジェクトをアップロードすることはできません。
{% endalert %}

Liquidテンプレートを使用することで、ウィッシュリストのIDをダイナミックに取り出し、メッセージで使用できます。そのためには、カスタム属性に[変数を割り当て]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#assigning-variables)、**Add Personalization**モーダルを使用して、配列から特定のアイテムを取り出します。カタログアイテムIDとして参照する変数は、`{{result}}`のように中かっこで囲む必要があります。

{% alert tip %}
配列は`1`ではなく`0`から始まることを忘れないでください。
{% endalert %}

例えば、Tales（ウィッシュリストに含まれているカタログのアイテム）がセール中であることをユーザーに通知するために、メッセージ作成画面で以下を追加できます。

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

以下のように表示されます。
> Get Tales now for just 7.49!

テンプレート化により、各ユーザーのカスタム属性、イベントプロパティ、その他のテンプレート化可能なフィールドに基づいて、ユーザーごとに異なるカタログアイテムをレンダリングできます。

### CSVのアップロード

追加する新しいカタログアイテムや、更新するカタログアイテムのCSVをアップロードできます。アイテムのリストを削除するには、アイテムIDのCSVをアップロードして削除できます。

### Liquidの使用

Liquidロジックを使用してカタログを手動で組み立てることもできます。ただし、存在しないIDを入力しても、Brazeはオブジェクトのないitems配列を返すことに注意してください。配列のサイズをチェックしたり、`if`ステートメントを使用して配列が空の場合を考慮するなど、エラー処理を含めることをお勧めします。

#### Liquidを含むカタログアイテムのテンプレート化

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)と同様に、Liquidタグで`:rerender`フラグを使用してカタログアイテムのLiquidコンテンツをレンダリングする必要があります。`:rerender`フラグは1レベルの深さまでしか適用されないことに注意してください。つまり、ネストされたLiquidタグ呼び出しには適用されません。

カタログアイテムにユーザープロファイルフィールド（Liquidパーソナライゼーションタグ内）が含まれている場合は、Liquidを適切にレンダリングするために、テンプレート化の前にメッセージ内でこれらの値をLiquidで事前に定義する必要があります。`:rerender`フラグが指定されていない場合、生のLiquidコンテンツがそのままレンダリングされます。

例えば、「Messages」という名前のカタログに、このLiquidを含むアイテムがあるとします。

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

以下のLiquidコンテンツをレンダリングするには:

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

次のように表示されます。

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
カタログのLiquidタグは、カタログ内で再帰的に使用することはできません。
{% endalert %}

## カタログデータの構造化

カタログデータの構造を計画する際は、意図するユースケースから始めて、それに合わせてカタログを設計します。カタログの各行はアイテム（一意の`id`を持つ）を表します。列にはそのアイテムの属性（URL、説明文、画像URL、価格、評価、サイズ、色など）を含める必要があります。

### 標準カタログ呼び出しを使用する場合

標準カタログ呼び出しでは、`id`列に対して値をマッチングします。カスタム属性やイベントプロパティ（ID文字列として）をカタログのLiquidタグに挿入することで、1つのアイテムの複数の属性をメッセージに取り込むことができます。一般的なユースケースには以下が含まれます。

- 最近閲覧した製品やサービス
- ウィッシュリストのアイテム
- ロケーション別のお得な情報
- 購入した製品
- ライフサイクルステージのコンテンツ
- 最近検索した製品やサービス

### カタログセレクションを使用する場合

[カタログセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)を使用すると、カタログの任意の列でフィルタリングし、最大50件の一致するアイテムを返すことができます。カスタム属性やイベントプロパティをセレクションフィルターに挿入することで、結果がユーザーごとにパーソナライズされます。一般的なユースケースには以下が含まれます。

- カテゴリがユーザーの好みと一致するアイテム
- ユーザーの好みのブランド、料理、サイズに一致するアイテム
- サブスクリプションタイプやロイヤルティティアのコンテンツ
- ユーザーの平均注文額の範囲内の製品

主な違いは、標準カタログ呼び出しが`id`で単一の既知のアイテムを検索するのに対し、カタログセレクションはカタログ全体をクエリして、フィルター条件に一致する複数のアイテムを返すことです。

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}