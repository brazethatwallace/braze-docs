---
nav_title: Shopify商品同期
article_title: Shopify商品同期
alias: /shopify_catalogs/
page_order: 5
description: "このリファレンス記事では、ShopifyからBrazeカタログに商品をインポートする方法について説明します。"
---

# Shopify商品同期 {#shopify-product-sync}

> Shopifyストアのすべての商品をBrazeの[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)に同期し、より深いメッセージングパーソナライゼーションを実現できます。

Shopifyカタログは、Shopifyストア内の商品に編集や変更を加えると、ほぼリアルタイムで更新されます。カート放棄や注文確認などを、最新の商品詳細や情報で強化できます。

[コアのShopify商品データ](#supported-shopify-catalog-data)のサポートに加えて、Shopifyコレクション、商品タグ、商品メタフィールドをBrazeカタログに同期できます。これらの追加フィールドにより、よりリッチなパーソナライゼーション、より正確なカタログセレクション、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を通じたより強力なセグメンテーションが可能になります。

## Shopify商品同期を設定する {#set-up}

Shopifyストアがすでにインストールされている場合でも、以下の手順に従って商品を同期できます。

### ステップ1: 同期をオンにする {#step-1-turn-on-the-sync}

Shopifyのインストールフローまたはshopifyパートナーページで、商品をBrazeカタログに同期できます。

![設定プロセスのステップ3。「カタログの商品識別子」に「Shopify Variant ID」が設定されている。]({% image_buster /assets/img/shopify/sync_products_step1.png %})

### ステップ2: 商品識別子を選択する {#step-2-select-your-product-identifier}

カタログIDとして使用する商品識別子を選択します。
- ShopifyバリアントID
- SKU

選択する商品識別子のIDとヘッダーの値には、文字、数字、ハイフン、アンダースコアのみを使用できます。商品識別子がこの形式に従っていない場合、Brazeはカタログの同期からその識別子を除外します。

これは、Brazeカタログ情報を参照するときに使用する主要な識別子です。

{% alert note %}
カタログIDとしてSKUを選択する場合は、ストア内のすべての商品とバリアントにSKUが設定されており、それらが一意であることを確認してください。<br><br>
- アイテムにSKUが設定されていない場合、Brazeはその商品をカタログに同期できません。
- 同じSKUを持つ複数の商品がある場合、予期しない動作が発生したり、重複したSKUによって意図せず商品情報が上書きされる可能性があります。
{% endalert %}

### ステップ3: 追加の商品データを設定する（オプション） {#step-3}

オプションで、商品タグ、Shopifyコレクション、メタフィールドの同期を有効にできます。初回同期後にShopifyパートナーページからこれらの設定を有効化または変更できます。

{% alert note %}
まずShopifyで商品タグ、Shopifyコレクション、メタフィールドを追加してください。Shopifyに存在しない場合、Brazeには表示されません。
{% endalert %}

![Shopifyの商品とバリアントをBrazeに同期するための設定。]({% image_buster /assets/img/shopify/additional_product_data.png %})

{% tabs global %}
{% tab 商品タグ %}

1. **商品データをBrazeに同期**ページで、**商品タグを同期**チェックボックスを選択して**商品タグを選択**モーダルを開きます。
2. Brazeカタログに同期する商品タグを最大20個選択します。選択したタグのみが同期されます。

![タグのセレクションが表示された商品タグ選択モーダル。]({% image_buster /assets/img/shopify/select_product_tags.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab 商品メタフィールド %}

1. 既存のShopifyインテグレーションがある場合は、Braze Shopifyアプリを再認証して、商品を同期するために必要な新しいスコープをインストールします。新規のお客様の場合は、次のステップに進んでください。

![Braze Shopifyアプリの再認証を促すバナー。]({% image_buster /assets/img/shopify/banner_to_reauthorize.png %})

{: start="2"}
2. **商品メタフィールドを同期**を選択して、メタフィールド設定モーダルを開きます。

![コレクションを含む複数の設定から選択できるオプションがある「商品データをBrazeに同期」セクション。]({% image_buster /assets/img/shopify/select_collections.png %})

{: start="3"}
3. 同期する検索可能なメタフィールドを最大20個選択します。各メタフィールドはカタログ内の個別の列となり、カタログセレクションやセグメントエクステンションなどの機能で使用できます。
- メタフィールドの命名時、スペースは「_」に変換され、すべての特殊文字はBrazeカタログのフィールド命名制限に対応するために削除されます。

![商品メタフィールドを選択するモーダル。]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

{% subtabs %}
{% subtab サポートされているメタフィールド %}

Brazeは以下のメタフィールドオブジェクトとそれぞれのタイプの一部をサポートしています。

| メタフィールドタイプ | データタイプ |
|--------------------------------------------------|--------------------------------------------------------|
| `boolean`                                        | ブール値                                                |
| `color`, `list.color`                            | 文字列（16進カラーコード、例: `#FFF123`）、文字列の配列 |
| `date`, `list.date`                              | 文字列（ISO 8601日付）、文字列の配列（ISO 8601日付）    |
| `date_time`, `list.date_time`                    | 文字列（ISO 8601日時）、文字列の配列（ISO 8601日時）    |
| `id`, `list.id`                                  | 文字列、文字列の配列                                    |
| `multi_line_text_field`                          | 文字列                                                 |
| `number_decimal`                                 | 文字列                                                 |
| `number_integer`                                 | 整数                                                   |
| `single_line_text_field`, `list.single_line_text_field` | 文字列、文字列の配列                              |
| `url`, `list.url`                                | 文字列（URL）、文字列の配列（URL）                      |
| `metaobject_reference`, `list.metaobject_reference` | 文字列、文字列の配列                                |
| `mixed_reference`, `list.mixed_reference`        | 文字列、文字列の配列                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ3: 追加の商品データを設定する（オプション） #step-3" }

{% endsubtab %}
{% subtab サポートされていないメタフィールド %}

Brazeは、一部のリストタイプを含む以下のメタフィールドオブジェクトをサポートしていません。

- `dimension` (`list.dimension`)
- `weight` (`list.weight`)
- `link` (`list.link`)
- `json`
- `list.number_decimal`
- `list.number_integer`
- `money`
- `rating` (`list.rating`)
- `volume` (`list.volume`)
- `rich_text_field`

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab コレクション %}

1. **Shopifyコレクションを同期**を選択して、コレクション設定モーダルを開きます。
2. 同期するコレクションを最大20個選択します。
  - モーダルには、Shopifyストアから最近作成または更新されたコレクションのうち、最大5,000件の検索可能なリストが表示されます。
  - 上位5,000件に含まれなくなった以前選択したコレクションも、選択内容に引き続き表示されます。

{% alert note %}
Brazeは同期されたコレクションの識別にShopifyコレクションIDを使用し、カタログセレクションやセグメントフィルターの構築時に使用されます。
{% endalert %}

![ドロップダウンからコレクションを選択するモーダル。]({% image_buster /assets/img/shopify/selected_collections.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{% alert tip %}
各商品データタイプの使用例については、[Shopifyカタログのユースケース]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/?tab=shopify%20product%20metafields#shopify-catalog-use-cases)を参照してください。
{% endalert %}

### ステップ4: 同期の進捗を追跡する {#step-4-track-your-sync-progress}

設定を保存すると、Brazeは商品の同期を開始し、Shopifyパートナーページのステータスを**進行中**に更新します。同期にかかる時間は、ストア内の商品とバリアントの数によって異なります。

同期が進行中であればページを離れることができます。同期が完了するとBrazeからダッシュボード通知が届きます。完了後、ステータスが**アクティブ**に更新され、Shopifyパートナーページでカタログ名を選択して商品を表示できます。

![商品同期ステータスが表示されたインテグレーション設定ページ。]({% image_buster /assets/img/shopify/track_sync_progress.png %})

Shopifyカタログ内で、同期された商品タグ、メタフィールド、コレクションを新しい列として表示することもできます。

![同期されたデータが表示されたShopifyカタログ。]({% image_buster /assets/img/shopify/synced_catalog.png %})

{% alert important %}
同期がカタログのストレージ制限を超えた場合、Brazeは同期を停止し、新しい商品の更新は反映されなくなります。必要に応じてティアのアップグレードについてカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

### ステップ5: 設定を管理する {#step-5-manage-your-configuration}

各同期タイプには、Shopifyパートナーページに同期された合計数、現在のステータス、カタログへのリンクを表示するサマリーカードがあります。表示アイコンを選択して、アクティブな設定を表示・編集できます。

Shopifyパートナーページから、商品タグ、コレクション、商品メタフィールドの管理を含むShopify商品同期をいつでも変更できます。

![アクティブな商品カタログ同期が表示されたインテグレーション設定ページ。]({% image_buster /assets/img/shopify/active_catalog_sync.png %})

{% alert important %}
同期するセレクションを変更すると、それらを参照しているアクティブなCampaigns、Canvases、またはカタログセレクションに影響する可能性があります。変更を適用する際は、アクティブなコンテンツが正しく動作するように更新してください。
{% endalert %}

## サポートされているShopifyカタログデータ {#supported-shopify-catalog-data}

| フィールド | データタイプ | 例 |
|----------------------|----------------|-----------------------------------------------------------------------------------|
| `id`                 | 文字列         | カタログの商品識別子が**ShopifyバリアントID**の場合は`45264808411274`<br><br>カタログの商品識別子が**SKU**の場合は`12345`（[ステップ2](#step-2-select-your-product-identifier)で選択した値と一致します） |
| `store_name`         | 文字列         | "your-store"（Shopifyストアのサブドメイン、`.myshopify.com`なし）                |
| `shopify_product_id` | 数値           | `7939032613002`（Brazeカタログでは数値として保存されます。Shopify APIはこのIDを文字列として返す場合があります） |
| `shopify_variant_id` | 数値           | `45264808411274`（Brazeカタログでは数値として保存されます。Shopify APIはこのIDを文字列として返す場合があります） |
| `product_title`      | 文字列         | "Classic leather jacket"                                                      |
| `variant_title`      | 文字列         | "Large / Red"、"Medium"、または単一バリアント商品の場合は"Default Title"     |
| `status`             | 文字列         | "active"、"draft"、"archived"                                                     |
| `product_image_url`  | 文字列         | "https://cdn.shopify.com/s/files/1/0641/0970/7402/files/t_shir.jpg?v=1736538760" |
| `variant_image_url`  | 文字列         | バリアント画像が存在しない場合は商品画像と同じCDNスタイルのURL。それ以外の場合はバリアント固有の画像URL |
| `vendor`             | 文字列         | "Flash and Thread"、"PantsLabyrinth"                                            |
| `product_type`       | 文字列         | "Outerwear"、"T-Shirts"（Shopifyの商品の**Product type**から取得）      |
| `product_url`        | 文字列         | "https://your-store.myshopify.com/products/classic-leather-jacket"            |
| `product_handle`     | 文字列         | "classic-leather-jacket"                                                          |
| `published_scope`    | 文字列         | "web"、"global"                                                                   |
| `price`              | 数値           | `10.00`、`24.99`<br><br>Shopifyは価格を文字列として返すことが多いです（例: REST Admin APIでの`"199.00"`）。Brazeはこのカタログフィールドでは数値に変換します。 |
| `compare_at_price`   | 数値           | Shopifyで**Compare at price**が設定されている場合は`15.00`<br><br>Shopifyに比較価格が設定されていない場合は`0`。Shopify APIは未設定の比較価格に対して通常`null`を返しますが、Brazeはフィールドが常に数値になるようにカタログに`0`を保存します（これはBrazeのデフォルトであり、Shopifyが`0`として送信する値ではありません）。 |
| `inventory_quantity` | 数値           | `20`、`0`、または過剰販売が許可されている場合は負の値（例: `-18`）   |
| `options`            | 文字列         | "Size,Color"<br><br>Shopifyでは商品ごとに最大3つのオプションタイプを設定できます（例: Size、Color、Material）。`options`の値はそれらの名前のカンマ区切りリストです。 |
| `option_values`      | 文字列         | "Medium,Red"、"Large,Red"<br><br>各値は`options`と同じ順序に対応します（最大3つの値）。 |
| `sku`                | 文字列         | "12345"、"SKU-001-RED-L"                                                    |
| `product_tags`       | 配列           | `["Summer", "Sale", "New"]`<br><br>商品タグの同期が必要です。                 |
| `collection_ids`     | 配列           | `[123456789012, 987654321098]`（ShopifyコレクションID）<br><br>Shopifyコレクションの同期が必要です。 |
| メタフィールド列     | タイプにより異なる | 同期された各メタフィールドは、そのキーで名前が付けられた個別の列として表示されます。詳細については、ステップ3の「商品メタフィールド」タブの[サポートされているメタフィールド](#step-3)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされているShopifyカタログデータ" }

{% alert warning %}
Shopifyカタログは、Shopifyによって管理されています。カタログを更新するには、Shopifyストアで直接変更を行ってください。変更は自動的にBrazeに同期されます。Shopifyカタログを削除するには、BrazeのShopifyパートナーページに移動し、[同期を非アクティブにしてください](#deactivate)。
{% endalert %}

## Shopifyカタログのユースケース {#shopify-catalog-use-cases}

これらのユースケースでは、同期されたShopifyカタログデータを使用してメッセージをパーソナライズする方法を示します。

{% alert warning %}
Brazeは各Shopify商品につき最大250のバリアントをカタログに同期します。この制限を超えるバリアントは同期されません。1商品あたり250を超えるバリアントが必要な場合は、Brazeカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% tabs %}
{% tab 商品タグ %}

商品タグを使用して、Shopifyでの商品のカテゴリ分けに基づいてメッセージをパーソナライズできます。例えば、[カタログセレクション]({{site.baseurl}}/catalog_selections/)を通じて「Summer Sale」タグが付いたすべての商品を紹介するプロモーションを送信したり、「Premium」タグが付いた商品を購入したユーザーのセグメントを構築したりできます。

商品タグは、各カタログアイテムの配列フィールドとして保存されます。商品タグの同期を設定するには、[Shopify商品タグ](#shopify-product-tags)を参照してください。

### カタログセレクション {#catalog-selection}

1. Shopifyで、関連する商品に「Women's」の商品タグを付けます。

![商品タイプが「Women's - Sweaters」で、タグが「Women's」、「Sweaters」、「Men」の商品。]({% image_buster /assets/img/shopify/product_tag_womens.png %}){: style="max-width:40%;"}

{: start="2"}
2. Brazeで、タグの同期を有効にし、「Women's」の商品タグを選択します。

![「Women's」を含む15個の衣料品関連タグが選択されたShopify商品タグ選択モーダル。]({% image_buster /assets/img/shopify/select_product_tags_womens.png %}){: style="max-width:80%;"}

### パーソナライゼーション {#personalization}

{% alert note %}
カタログセレクションで商品タグやコレクションを参照する場合は、カタログデータに表示される配列の角括弧`[]`や引用符`""`を含めず、値そのものだけを使用してください。例えば、商品タグがカタログで`["Women's"]`と表示されている場合、セレクションフィルターには`Women's`と入力します。
{% endalert %}

1. 「Women's」などの該当する商品タグを持つ商品をフィルタリングするカタログセレクションを作成します。単一のカタログセレクション内で使用できるユニークな配列フィールドは1つのみで、カタログセレクション内の商品は最大50個です。

![属性「Women's」を持つ商品タグでフィルタリングするカタログセレクション。]({% image_buster /assets/img/shopify/edit_product_tags_selection.png %})

{: start="2"}
2. メッセージ作成画面で、「Women's」タグが付いたカタログセレクションの商品をテンプレートに挿入したい場所にセレクションを追加します。例えば、次のようなHTML商品ブロックを使用できます。

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

または、「Women's」タグが付いた特定の商品をプッシュ通知で紹介したい場合は、**パーソナライゼーションを追加**ツールを使用してカタログアイテムを指定できます。

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog womens_clothing %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![商品タグを使用してカタログセレクションから3つのアイテムを取得しているプッシュ通知作成画面。]({% image_buster /assets/img/shopify/add_personalization_product_tags.png %})

### カタログセグメンテーション（SQL） {#catalog-segmentation-sql}

[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を使用して、商品タグとインタラクションしたユーザーに基づいてセグメントを構築します。例えば、特定の商品タグを含むカタログアイテムとエンゲージしたユーザーを見つけるには、次のクエリを使用します。

{% raw %}
```liquid
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific product tag. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'product_tags' AND ARRAY_CONTAINS('<product_tag_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% tab 商品メタフィールド %}

商品メタフィールドを使用して、Shopifyの標準フィールドを超えたカスタム商品詳細でメッセージをパーソナライズできます。例えば、注文確認にケア方法を含めたり、おすすめメールに原産国を表示したり、特定の素材の商品を購入したユーザーをセグメント化したりできます。

同期された各メタフィールドは、カタログ内の個別の列となり、データタイプはメタフィールドタイプによって決まります。メタフィールドの同期を設定するには、[Shopify商品メタフィールド](#shopify-product-metafields)を参照してください。

### カタログセレクション

1. Shopifyで、関連する商品の`seasonal`商品メタフィールドを`summer`に設定します（これはメタフィールドの値であり、商品タグではありません）。

![seasonalメタフィールドの値がsummerに設定された商品メタフィールド追加モーダル。]({% image_buster /assets/img/shopify/summer_product_metafield.png %}){: style="max-width:80%;"}

{: start="2"}
2. Brazeで、メタフィールドの同期を有効にし、`custom.seasonal`（またはShopifyメタフィールドに一致するネームスペースとキー）を選択します。

![custom.seasonalを含む4つのアイテムが選択された展開ドロップダウンがある商品メタフィールド選択モーダル。]({% image_buster /assets/img/shopify/select_metafields.png %}){: style="max-width:80%;"}

### パーソナライゼーション

1. 該当する値を含むメタフィールドでフィルタリングする[カタログセレクション]({{site.baseurl}}/catalog_selections/)を作成します。

![属性summerを持つメタフィールドでフィルタリングするカタログセレクション。]({% image_buster /assets/img/shopify/metafields_selection.png %})

{: start="2"}
2. メッセージ作成画面で、商品メタフィールドをテンプレートに挿入したい場所にセレクションを追加します。例えば、次のようなHTML商品ブロックを使用できます。

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
        {% if url == blank %}
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        {% else %}
        <a href="{{ url }}" style="text-decoration:none;">
          <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
        </a>
        {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

または、特定のメタフィールド値を持つ商品をプッシュ通知で紹介したい場合は、**パーソナライゼーションを追加**ツールを使用してカタログアイテムを指定できます。

{% raw %}
```liquid
Check out the latest summer products:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog seasonal_summer %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![メタフィールドベースのセレクションを使用してカタログセレクションから3つのアイテムを取得しているプッシュ通知作成画面。]({% image_buster /assets/img/shopify/add_personalization_metafields.png %})

### カタログセグメンテーション（SQL）

[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を使用して、商品メタフィールドとインタラクションしたユーザーに基づいてセグメントを構築します。例えば、メタフィールド配列に特定の値を含む商品でeコマースイベントをトリガーしたユーザーを見つけるには、次のクエリを使用します。

{% raw %}
```sql
-- -----------------------------------------------------------------------------
-- When the metafield is stored as a JSON array in catalog field_value (for example,
-- '["winter","summer"]' or a list-type Shopify metafield serialized to JSON),
-- use ARRAY_CONTAINS like product_tags. Cast the element you search for to
-- VARIANT so types match the parsed array elements.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product whose
-- metafield array contains a specific value (for example, segment on "seasonal").
-- For a date range, add events.time >= $start_date AND events.time <= $end_date.
-- For first/last triggered, reuse the CTE pattern from Template 3 with this
-- ARRAY_CONTAINS predicate instead of items.field_value = '<metafield_value>'.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND ARRAY_CONTAINS('<array_element_value>'::VARIANT, TRY_PARSE_JSON(items.field_value));
```
{% endraw %}

特定の商品メタフィールドを持つ注文を行った顧客をセグメント化したい場合は、以下のSQLセグメントエクステンションテンプレート（全期間、特定の期間、最初または最後にイベントをトリガー）のいずれかを使用してください。

{% raw %}
```sql
-- =============================================================================
-- Segment Extension: Metafields × Ecommerce Events — Example SQL Templates
-- =============================================================================
-- Metafield column names in CATALOGS_ITEMS_SHARED follow:
--   field_name = 'metafield_<namespace>_<key>'
-- Replace placeholders: app_group_id, catalog_id, event name, and the metafield
-- field_name + value. For array-type metafield values, use ARRAY_CONTAINS
-- with TRY_PARSE_JSON(items.field_value) similar to the product_tags example.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Template 1: Map metafields to event triggers (all time)
-- -----------------------------------------------------------------------------
-- Users who have ever triggered the ecommerce event with a product that has
-- the given metafield value. Event-agnostic: change events.name for the
-- desired event (e.g. ecommerce.order_placed, ecommerce.product_viewed).
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who have engaged with catalog items that have a specific
-- product metafield. Joins the catalog to custom events by matching
-- events.properties.products (e.g. variant_id) to catalog items.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 2: Map metafields to event triggers (for a specific period)
-- -----------------------------------------------------------------------------
-- Same as Template 1, restricted to events within a time window. Use
-- $start_date and $end_date (Segment Extension parameters) or literal
-- Unix timestamps.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users who triggered the ecommerce event with a product that has
-- the given metafield value within the specified time range.
SELECT
    DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
            items.field_name = 'id'
            AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
        )
        OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    AND events.app_group_id = '<app_group_id>'
    AND events.time >= $start_date
    AND events.time <= $end_date
    AND items.catalog_id = '<catalog_id>'
    AND items.field_name = '<metafield_name>'
    AND items.field_value = '<metafield_value>';


-- -----------------------------------------------------------------------------
-- Template 3: Map metafields — first or last triggered an event
-- -----------------------------------------------------------------------------
-- Users for whom the *first* (earliest) or *last* (most recent) matching
-- event (by time) involved a product with the given metafield. Switch
-- ORDER BY to time ASC for first, time DESC for last.
-- -----------------------------------------------------------------------------

-- Description:
-- Fetches users whose first (or last) occurrence of the ecommerce event
-- involved a catalog item with the specified metafield value.
WITH events_with_catalog_metafield AS (
    SELECT
        events.user_id,
        events.time,
        events.id AS event_id,
        ROW_NUMBER() OVER (
            PARTITION BY events.user_id
            ORDER BY events.time ASC   -- use DESC for "last triggered"
        ) AS rn
    FROM
        USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
        LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
        JOIN CATALOGS_ITEMS_SHARED AS items ON (
            (
                items.field_name = 'id'
                AND items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
            items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
        )
    WHERE
        events.name = 'ecommerce.order_placed'
        AND events.app_group_id = '<app_group_id>'
        AND items.catalog_id = '<catalog_id>'
        AND items.field_name = '<metafield_name>'
        AND items.field_value = '<metafield_value>'
)
SELECT
    user_id
FROM
    events_with_catalog_metafield
WHERE
    rn = 1;
```
{% endraw %}

{% endtab %}
{% tab コレクション %}

Shopifyコレクションを使用して、Shopifyサイトやアプリ体験でも使用されているキュレートされた商品グループをメッセージに取り込みます。例えば、プロモーションメールで「New Arrivals」を紹介したり、カート放棄Canvasで「Best Sellers」をクロスセルしたり、季節限定コレクションを閲覧したユーザーをターゲットにしたりできます。

### カタログセレクション

1. Shopifyで、トップパフォーマンスの商品を含む「New Women's Products - In Stock」コレクションを作成します。

![「New Women's Products - In Stock」を含むShopifyコレクションのリスト。]({% image_buster /assets/img/shopify/shopify_collections.png %})

{: start="2"}
2. Brazeで、コレクションの同期を有効にし、「Women's Products - In Stock」を選択します。

![4つのコレクションが選択された展開ドロップダウンがあるコレクション選択モーダル。]({% image_buster /assets/img/shopify/select_collections_id.png %})

{% alert note %}
Shopifyコレクションの場合、コレクションを表示したときのURLに含まれる**コレクションID**を使用する必要があります。例えば、URLが`https://admin.shopify.com/store/se-team-ecommerce/collections/470645342446`の場合、コレクションIDは`470645342446`です。
{% endalert %}

### パーソナライゼーション

{% alert note %}
カタログセレクションでコレクションIDを参照する場合は、カタログデータに表示される配列の角括弧`[]`を含めず、数値IDの値のみを使用してください。例えば、コレクションIDがカタログで`[123456789012, 987654321098]`と表示されている場合、セレクションフィルターには数値ID（例: `470645342446`）のみを入力します。
{% endalert %}

1. そのコレクションのIDを持つ商品でフィルタリングされた「New Women's Products - In Stock」というカタログセレクションを作成します。単一のカタログセレクション内で使用できるユニークな配列フィールドは1つのみで、コレクション内の商品は最大50個です。
 - **Collections**フィールドでフィルタリングして、独自のカスタムセレクションを作成することもできます。

![コレクションID属性「470645342446」を持つコレクションでフィルタリングするカタログセレクション。]({% image_buster /assets/img/shopify/collections_selection.png %})

{: start="2"}
2. メッセージで、作成したセレクションを使用するか、コレクションを直接参照してテンプレートに挿入します。例えば、次のようなHTML商品ブロックを使用できます。

{% raw %}
```liquid
{% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}

{% if items[0] == blank %}
{% abort_message('Catalog selection returned no items') %}
{% endif %}

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
  {% for item in items %}
  {% if forloop.index0 < 3 %}
  {% assign title = item.product_title | default: '' %}
  {% assign image_url = item.variant_image_url | default: '' %}
  {% assign price = item.price | default: '' %}
  {% assign url = item.product_url | default: '' %}

  <tr>
    <td width="200" valign="top" style="padding:12px 12px 12px 0;">
      {% if image_url == blank %}
      <div style="width:200px;height:200px;background:#f2f2f2;line-height:200px;text-align:center;font-family:Arial,sans-serif;font-size:12px;color:#666;">
        No image
      </div>
      {% else %}
      {% if url == blank %}
      <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      {% else %}
      <a href="{{ url }}" style="text-decoration:none;">
        <img src="{{ image_url }}" width="200" height="200" alt="{{ title | escape }}" style="display:block;border:0;outline:none;text-decoration:none;" />
      </a>
      {% endif %}
      {% endif %}
    </td>

    <td valign="top" style="padding:12px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#111;">
      {% if title != blank %}<div style="font-weight:600;">{{ title | escape }}</div>{% endif %}
      {% if price != blank %}<div>Price: ${{ price }}</div>{% endif %}
      {% if url != blank %}<div><a href="{{ url }}" style="color:#F84B09;">View product</a></div>{% endif %}
    </td>
  </tr>
  {% endif %}
  {% endfor %}
</table>
```
{% endraw %}

または、特定の新商品をプッシュ通知で紹介したい場合は、**パーソナライゼーションを追加**ツールを使用してカタログアイテムを指定できます。

{% raw %}
```liquid
Checkout the latest women's clothing:
    {% catalog_selection_items se-team-ecommerce_shopify_catalog shopify_collection_womens_instock %}
    {{ items[0].product_title}}{{items[0].price}}
    {{ items[1].product_title}}{{items[1].price}}
    {{ items[2].product_title}}{{items[2].price}}
```
{% endraw %}

![商品タグを使用してカタログセレクションから3つのアイテムを取得しているプッシュ通知作成画面。]({% image_buster /assets/img/shopify/add_personalization_collections.png %})

### カタログセグメンテーション（SQL）

コレクションとインタラクションしたユーザーのセグメントを作成します。[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を使用して、コレクションメンバーシップに基づいてセグメントを構築します。例えば、過去1年間に特定のコレクションの商品を購入したユーザーを見つけるには、次のクエリを使用します。

{% raw %}
```json
-- Description:
-- This query fetches users who have engaged with catalog items that contain a specific collection ID. It joins the catalog
-- to custom events by matching any element in an array within events.properties.products (e.g. any product
-- with variant_id equal to a catalog item), using Snowflake LATERAL FLATTEN to explode the array.
SELECT
DISTINCT(events.user_id)
FROM
    USERS_BEHAVIORS_CUSTOMEVENT_SHARED AS events,
    LATERAL FLATTEN(input => GET_PATH(TRY_PARSE_JSON(events.properties), 'products'), outer => false) AS event_item
    JOIN CATALOGS_ITEMS_SHARED AS items ON (
        (
                items.field_name = 'id'
                    AND
                items.field_value = GET_PATH(event_item.value, 'variant_id')::STRING
            )
            OR
        items.item_id = GET_PATH(event_item.value, 'variant_id')::STRING
    )
WHERE
    events.name = 'ecommerce.order_placed'
    and events.app_group_id = '<app_group_id>'
    AND items.catalog_id = '<catalog_id>'
    AND (items.field_name = 'collection_ids' AND ARRAY_CONTAINS('<collection_ids_value>'::VARIANT, TRY_PARSE_JSON(items.field_value)));
```
{% endraw %}

{% endtab %}
{% endtabs %}

{% alert tip %}
[値下げ通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/)や[再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/)も設定できます！<br><br>各ユースケースでは、ユーザーのサブスクリプションステータスをカタログにキャプチャするカスタムイベントを作成する必要があります。カスタムイベントには、Shopify商品同期の一部として選択した[SKUまたはShopifyバリアントID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/#step-2-select-your-product-identifier)のいずれかにマップされるイベントプロパティが必要です。
{% endalert %}

## 商品同期を非アクティブにする {#deactivate}

Shopify商品同期機能を非アクティブにすると、カタログと商品がすべて削除されます。この操作は、このカタログの商品データをアクティブに使用しているメッセージにも影響する可能性があります。商品詳細のないメッセージが送信される可能性があるため、非アクティブ化する前にCampaignsまたはCanvasesを更新または一時停止していることを確認してください。カタログページでShopifyカタログを直接削除しないでください。

## トラブルシューティング {#troubleshooting}

Shopify商品同期でエラーが発生した場合は、次のいずれかのエラーが原因である可能性があります。問題を修正し、同期を解決する方法については、以下の手順に従ってください。

| エラー | 理由 | ソリューション |
| --- | --- | --- |
| サーバーエラー | 商品を同期しようとしたときに、Shopify側でサーバーエラーが発生した場合に起こります。 | [同期を非アクティブにし](#deactivate)、商品の在庫全体を再同期します。 |
| 重複するSKU | カタログアイテムIDとしてSKUを使用している場合に、複数の商品に同じSKUが設定されていると発生します。カタログアイテムIDは一意である必要があるため、すべての商品に一意のSKUが必要です。 | Shopifyで商品とバリアントの一覧をすべて監査して、重複するSKUがないことを確認します。SKUが重複している場合は、Shopifyストアアカウントで一意のSKUに更新します。修正後、[同期を非アクティブにし](#deactivate)、商品の在庫全体を再同期します。 |
| カタログ制限の超過 | カタログ制限を超えた場合に発生します。Brazeは、利用可能なストレージがないため、同期を完了することや、同期をアクティブな状態で維持することができなくなります。 | この問題には2つのソリューションがあります。<br><br>1. アカウントマネージャーに連絡してティアをアップグレードし、カタログ制限を増やします。<br><br>2. 次のいずれかを削除して、ストレージ領域を解放します。<br>- 他のカタログからのカタログアイテム<br>- 他のカタログ<br>- 作成されたセレクション<br><br> いずれのソリューションを取った場合でも、同期を非アクティブにしてから再同期を実行する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="トラブルシューティング" }