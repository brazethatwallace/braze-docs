---
nav_title: ローカライズされたカタログコンテンツ
article_title: Brazeカタログでローカライズされたコンテンツを管理する
page_order: 3
page_type: reference
description: "ローカライズされた商品コピー、価格、画像URLをBrazeカタログに保存し、送信時に正しい言語を解決します。"
---

# Brazeカタログでローカライズされたコンテンツを管理する {#manage-localized-content-with-braze-catalogs}

> ローカライズされた文字列やURLをカタログに保存することで、ロケールごとに個別のバリアントを作成することなく、1つのキャンペーンやキャンバスから各ユーザーに適切な言語のコピーを配信できます。

## この例について {#about-this-example}

架空の衣料品小売店であるPantsLabyrinthは、北米とヨーロッパで商品を販売しています。商品名、価格、ヒーロー画像は言語によって異なりますが、マーケティングチームは送信時にパーソナライズする1つのメールまたはプッシュテンプレートを使用したいと考えています。

この例では、SDKがデバイスロケールから収集したユーザーの{% raw %}`${language}`{% endraw %} [標準属性項目]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を読み取る3つのカタログパターンを紹介します。

- JSONオブジェクトフィールド：1アイテムにつき1行にすべてのロケールを格納
- フラットな言語別カラム：`header_en`、`header_fr` など
- 言語ごとに個別のカタログ：`pantslabyrinth-promo-en` のようなダイナミックなカタログ名

カタログは、ローカライズされたコンテンツが構造化データ（商品、プロモーション、画像URLなど）の場合に使用します。メールやプッシュの自由形式メッセージコピーには、チャネルがサポートしている場合は[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)をご利用ください。ローカライゼーションパターンをより広く比較するには、[翻訳管理]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management)を参照してください。

## 考慮事項 {#considerations}

- 例は説明目的です。カタログキーやサフィックスに名前を付ける前に、ユーザー群内の{% raw %}`${language}`{% endraw %}の大文字・小文字と形式を確認してください。
- 方法1と方法2では、{% raw %}`${language}`{% endraw %}が空白であるか、カタログキーまたはフィールドと一致しない場合、ローカライズされた出力が空になることがあります。各フィールドを個別にチェックし、デフォルト（例：英語）にフォールバックしてください。
- 方法3では、カタログ名を構築する前にサポートされている言語コードを許可リストに登録してください。カタログが存在しない場合、メッセージは中止されます。
- カタログ内の[JSONオブジェクト]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types)は、APIまたは[カタログ向けCloud Data Ingestion（CDI）]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)を通じて作成・更新できますが、CSVアップロードではできません。
- 方法2はCSVでのメンテナンスをサポートしますが、言語が増えるとカラム数が増加します。CSVファイルは最大[1,000カラム]({{site.baseurl}}/user_guide/data/activation/catalogs/create#step-1-review-your-csv-file)をサポートしています。
- 方法3では、`catalog_items`タグに到達するすべての言語コードに対応するカタログが必要です。カタログが存在しない場合、Brazeはメッセージを中止します。既存のカタログ内にアイテムIDが存在しない場合は、空のアイテム配列が返されます。
- カタログのLiquidタグは[再帰的に]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid)使用することはできません。
- [カタログセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)は最大10個のフィルターをサポートし、最大50アイテムを返します。カタログスキーマに対してフィルターを検証してください。
- 大規模なマルチロケール商品フィードを管理する場合は、[カタログストレージティア]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers)を確認してください。

## 設定 {#setup}

### ステップ1：カタログ構造を選択する {#step-1-choose-a-catalog-structure}

以下の表のガイダンスを参考にカタログ構造を選択してください。

| 方法 | 最適なケース | トレードオフ |
| --- | --- | --- |
| JSONオブジェクトフィールド | 中規模のカタログサイズ、1アイテムにつき1行、APIまたはCDI経由の更新 | 言語の追加時にAPIですべてのアイテムを更新する必要がある。JSONフィールドにはCSVが使用不可 |
| フラットな言語別フィールド | 少数の言語とフィールド、開発チーム以外がCSVを使用 | 言語追加ごとにカラムが増える。フィールド命名の一貫性が必要 |
| 言語ごとのカタログ | ロケールごとの大規模フィードまたは個別のロケール管理者、言語ごとのCSV | 許可リストに登録されたすべての言語コードにカタログが必要。カタログが存在しない場合、送信が中止される |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カタログ構造を選択する" }

### ステップ2：カタログとアイテムを作成する {#step-2-create-the-catalog-and-items}

1. **データ設定** > **カタログ**に移動し、カタログを作成します（方法3の場合は複数のカタログ）。
2. 選択した構造に基づいてフィールドとアイテムを追加します。[カタログの作成]({{site.baseurl}}/user_guide/data/activation/catalogs/create)を参照してください。
3. （オプション）[カタログセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を作成してアイテムをフィルタリングします。例えば、ユーザーのカスタム属性に一致する`category`でフィルタリングできます。

{% tabs local %}
{% tab 方法1：JSONフィールド %}
カタログ`PantsLabyrinth_Product_Copy`のアイテム例：

| アイテム | 値 |
| --- | --- |
| `id` | `trail-runner-001` |
| `name` | `{"EN":"Trail Runner","FR":"Chaussure de trail","DE":"Trailrunner"}` |
| `category` | `footwear` |
| `url` | `https://pantslabyrinth.shop/products/trail-runner-001` |
| `price` | `{"EN":"$120 USD","FR":"112 EUR","DE":"112 EUR"}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSONロケールフィールドを含むカタログアイテムの例" }

{% endtab %}
{% tab 方法2：フラットフィールド %}
カタログ`PantsLabyrinth_Promo_Copy`のアイテム例：

| アイテム | 値 |
| --- | --- |
| `id` | `spring-sale` |
| `header_en` | `Spring trail sale` |
| `header_fr` | `Soldes de printemps` |
| `body_en` | `Save on trail runners this week.` |
| `body_fr` | `Économisez sur les chaussures de trail cette semaine.` |
| `cta_text_en` | `Shop now` |
| `cta_text_fr` | `Acheter` |
| `img_src_en` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
| `img_src_fr` | `https://cdn.pantslabyrinth.shop/fr/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="フラットな言語別フィールドを含むカタログアイテムの例" }

{% endtab %}
{% tab 方法3：言語ごとのカタログ %}
言語ごとに同じフィールドを持つカタログを1つずつ作成します。例えば、`pantslabyrinth-promo-fr`と`pantslabyrinth-promo-de`で同じ`id`とフィールドをローカライズされた値で繰り返します。

`pantslabyrinth-promo-en`のアイテム例：

| アイテム | 値 |
| --- | --- |
| `id` | `spring-sale` |
| `header` | `Spring trail sale` |
| `body` | `Save on trail runners this week.` |
| `cta_text` | `Shop now` |
| `img_src` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="英語の言語別カタログのアイテム例" }

{% endtab %}
{% endtabs %}

### ステップ3：メッセージにLiquidを追加する {#step-3-add-liquid-to-your-message}

ステップ1で選択したカタログ構造に一致するLiquidパターンを選択します。

{% tabs local %}
{% tab 方法1：JSONフィールド %}
すべてのロケールを単一のカタログ行のJSONオブジェクトフィールドに保存し、`property_accessor`フィルターを使用して{% raw %}`${language}`{% endraw %}（大文字に正規化）に一致する`name`と`price`キーを読み取ります。各フィールドを個別にチェックし、そのフィールドが空白の場合は`EN`にフォールバックすることで、名前はあるが価格がないロケールでも英語の価格が表示されます。

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Product_Copy trail-runner-001 %}
{% assign lang = ${language} | upcase %}
{% assign localized_name = items[0].name | property_accessor: lang %}
{% assign localized_price = items[0].price | property_accessor: lang %}
{% if localized_name == blank %}
  {% assign localized_name = items[0].name | property_accessor: 'EN' %}
{% endif %}
{% if localized_price == blank %}
  {% assign localized_price = items[0].price | property_accessor: 'EN' %}
{% endif %}
Product: {{ localized_name }}
Price: {{ localized_price }}
```
{% endraw %}

[プロパティアクセサーフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)を参照してください。
{% endtab %}
{% tab 方法2：フラットフィールド %}
{% raw %}`${language}`{% endraw %}（小文字に正規化）からダイナミックなフィールド名を構築し、ブラケット参照でアイテムからそれらのフィールドを読み取ります。例えば、{% raw %}`items[0][header_field]`{% endraw %}は解決された言語のヘッダーを読み取ります。各フィールドを個別にチェックし、そのフィールドが空白の場合は英語のカラムにフォールバックすることで、ヘッダーはあるが本文がないロケールでも英語の本文が表示されます。

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Promo_Copy spring-sale %}
{% assign lang = ${language} | downcase %}
{% assign header_field = 'header_' | append: lang %}
{% assign body_field = 'body_' | append: lang %}
{% assign cta_field = 'cta_text_' | append: lang %}
{% assign img_field = 'img_src_' | append: lang %}
{% assign header_val = items[0][header_field] %}
{% assign body_val = items[0][body_field] %}
{% assign cta_val = items[0][cta_field] %}
{% assign img_val = items[0][img_field] %}
{% if header_val == blank %}
  {% assign header_val = items[0].header_en %}
{% endif %}
{% if body_val == blank %}
  {% assign body_val = items[0].body_en %}
{% endif %}
{% if cta_val == blank %}
  {% assign cta_val = items[0].cta_text_en %}
{% endif %}
{% if img_val == blank %}
  {% assign img_val = items[0].img_src_en %}
{% endif %}
<img src="{{ img_val }}" alt="" />
<h2>{{ header_val }}</h2>
<p>{{ body_val }}</p>
<a href="#">{{ cta_val }}</a>
```
{% endraw %}
{% endtab %}
{% tab 方法3：言語ごとのカタログ %}
{% alert warning %}
`catalog_items`に渡すカタログ名が存在しない場合、Brazeはメッセージを中止します。カタログ名を構築する前にサポートされている言語コードを許可リストに登録してください。既存のカタログ内にアイテムIDが存在しない場合は空のアイテム配列が返されます。その場合のみ英語のカタログにフォールバックできます。
{% endalert %}

一致するカタログを持つ言語コード（ここでは`en`、`fr`、`de`）を許可リストに登録し、サポートされていないまたは空白の値は`en`にデフォルト設定してからアイテムを検索します。そのカタログにアイテムIDが存在しない場合は、英語のカタログにフォールバックします。

{% raw %}
```liquid
{% assign lang = ${language} | downcase %}
{% assign supported = 'en,fr,de' | split: ',' %}
{% if supported contains lang %}{% else %}{% assign lang = 'en' %}{% endif %}
{% assign theCatalog = 'pantslabyrinth-promo-' | append: lang %}
{% catalog_items {{ theCatalog }} spring-sale %}
{% if items[0] == blank %}
  {% catalog_items pantslabyrinth-promo-en spring-sale %}
{% endif %}
<img src="{{ items[0].img_src }}" alt="" />
<h2>{{ items[0].header }}</h2>
<p>{{ items[0].body }}</p>
<a href="#">{{ items[0].cta_text }}</a>
```
{% endraw %}

[カタログ名でのテンプレートの使用]({{site.baseurl}}/user_guide/data/activation/catalogs/create#template-catalog-names)および[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)を参照してください。
{% endtab %}
{% endtabs %}

#### オプション：カテゴリ別のカタログセレクション {#optional-catalog-selection-by-category}

パーソナライゼーションの前にアイテムをフィルタリングします。例えば、`preferred_category = footwear`のユーザーに対するフットウェアプロモーション：

{% raw %}
```liquid
{% catalog_selection_items PantsLabyrinth_Product_Copy footwear_promos %}
{% for item in items %}
  {{ item.name }}
{% endfor %}
```
{% endraw %}

ダッシュボードで`category`カラムに対するフィルターと、必要に応じてユーザー属性を使用してセレクションを定義します。

### ステップ4：プレビューとテスト {#step-4-preview-and-test}

1. 異なる{% raw %}`${language}`{% endraw %}値を持つユーザープロファイルで**ユーザーとしてプレビュー**を使用します。
2. 言語が存在しないまたはサポートされていない場合（例：名前はあるが価格がないなどの部分的なロケールを含む）のフォールバックコピーを確認します。
3. 方法3の場合、許可リストに登録されたすべての言語に対応するカタログがあること、およびサポートされていない言語コードが送信を中止することなくデフォルトカタログにマッピングされることを確認します。

## 関連記事 {#related-articles}

- [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [カタログの使用]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [カタログの作成]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [高度なLiquidフィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)
- [ローカライゼーション]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)
- [Liquidメッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)