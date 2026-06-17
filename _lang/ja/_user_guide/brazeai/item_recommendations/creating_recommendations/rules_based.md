---
nav_title: ルールベースのレコメンデーション
article_title: ルールベースのアイテムレコメンデーションを作成する
description: "このリファレンス記事では、カタログ内のアイテムに対してAI 項目のレコメンデーションを作成する方法について説明します。"
page_order: 2
---

# ルールベースのアイテムレコメンデーションを作成する {#create-rules-based-item-recommendations}

> カタログ内のアイテムからルールベースのレコメンデーションエンジンを作成する方法について説明します。

## ルールベースのアイテムレコメンデーションについて {#about-rules-based-item-recommendations}

ルールベースのレコメンデーションエンジンは、ユーザーデータと商品情報を使用して、メッセージ内でユーザーに関連アイテムを提案します。[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)と、Brazeの[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)または[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)のいずれかを使用して、ユーザーの動作と属性に基づいてコンテンツをダイナミックにパーソナライズします。

{% alert important %}
ルールベースのレコメンデーションは、手動で設定する必要がある固定ロジックに基づいています。つまり、ロジックを更新しない限り、ユーザーの購入履歴や嗜好に合わせてレコメンデーションが調整されることはありません。<br><br>ユーザーの履歴に合わせて自動的に調整されるパーソナライズされたAIレコメンデーションを作成するには、[AI 項目のレコメンデーション]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai/)を参照してください。
{% endalert %}

## レコメンデーションエンジンのオプション {#recommendation-engine-options}

利用可能なリソースやユースケースに適したレコメンデーションエンジンを判断する際には、以下の検討事項表を参考にしてください。

<table aria-label="Recommendation engine options" style="text-align: center;">
  <caption>レコメンデーションエンジンのオプション</caption>
  <thead>
    <tr>
      <th>レコメンデーションエンジン</th>
      <th>データポイントの記録なし</th>
      <th>ノーコードソリューション</th>
      <th>高度なLiquid不要</th>
      <th>製品フィードの自動更新</th>
      <th>Braze UIで生成</th>
      <th>データホスティングやトラブルシューティング不要</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>カタログCSV</strong></td>
      <td>&#10004;</td>
      <td>はい（事前に生成されたLiquidを使用する場合）</td>
      <td>&#10004;</td>
      <td>はい（レコメンデーションが頻繁に更新<strong>されない</strong>場合）</td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
    <tr>
      <td><strong>カタログAPI</strong></td>
      <td>&#10004;</td>
      <td></td>
      <td>&#10004;</td>
      <td>はい（レコメンデーションが1時間ごとに更新される場合）</td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
    <tr>
      <td><strong>コネクテッドコンテンツ</strong></td>
      <td>&#10004;</td>
      <td></td>
      <td></td>
      <td>&#10004;<br>（レコメンデーションはリアルタイムで更新されます）</td>
      <td>はい（Brazeの外部で生成された場合）</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Liquid</strong></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>&#10004;</td>
      <td>&#10004;</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Recommendation engine options" }

## レコメンデーションエンジンの作成 {#creating-a-recommendation-engine}

カタログまたはコネクテッドコンテンツのいずれかを使用して、レコメンデーションエンジンを作成します。

{% tabs local %}
{% tab using a catalog %}
カタログを使用してレコメンデーションエンジンを作成するには、以下の手順に従います。

1. 製品の[カタログを作成]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)します。
2. 各製品について、推奨製品のリストを区切り文字（パイプ`|`など）で区切った文字列として「product_recommendations」という名前の列に追加します。
3. レコメンデーションを検索したい製品IDをカタログに渡します。
4. そのカタログアイテムの`product_recommendations`値を取得し、Liquidのsplitフィルターを使用して区切り文字で分割します。
5. それらのIDの1つ以上をカタログに渡して、他の製品の詳細を収集します。

### 例 {#example}

健康食品アプリを運営していて、ユーザーがアプリに登録してからの期間に応じて異なるレシピを送信するコンテンツカードキャンペーンを作成したいとします。まず、以下の情報を含むCSVファイルを使用してカタログを作成し、アップロードします。

| フィールド | 説明 |
|-----|-----------|
| **id** | ユーザーがアプリに登録してからの日数に対応する一意の数値。例えば、`3`は3日間に相当します。 |
| **type** | `comfort`、`fresh`などのレシピカテゴリー。 |
| **title** | 各IDに対して送信されるコンテンツカードのタイトル。「今週のランチ用の作り置き」や「タコスについて話そう」などです。 |
| **link** | レシピ記事へのリンク。 |
| **image_url** | レシピに対応する画像。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example" }

カタログがBrazeにアップロードされたら、一部のカタログアイテムのプレビューを確認して、情報が正確にインポートされたことを確認してください。プレビューではアイテムがランダムに表示される場合がありますが、レコメンデーションエンジンの出力には影響しません。


コンテンツカードキャンペーンを作成します。作成画面で、キャンペーンを受信するユーザーと、表示するレシピおよび画像を決定するLiquidロジックを入力します。このユースケースでは、Brazeがユーザーの`start_date`（登録日）を取得し、現在の日付と比較します。日数の差によって、送信されるコンテンツカードが決まります。

{% subtabs local %}
{% subtab title %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}
{% endsubtab %}

{% subtab message %}
{% raw %}
`````````liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}
{% endsubtab %}

{% subtab image %}
{% raw %}
`````````liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}

以下に例を示します。

![コンテンツカードキャンペーンのメッセージ作成画面の例。]({% image_buster /assets/img/recs/content_card_preview.png %})

**On click behavior**セクションで、iOS、Android、Webデバイスでユーザーがコンテンツカードをクリックしたときにリダイレクトされる先のLiquidロジックを入力します。

{% raw %}
`````````liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

以下に例を示します。

![作成画面でのクリック時の動作ブロックの例。]({% image_buster /assets/img/recs/on_click_behavior.png %}){: style="max-width:60%;"}<br><br>

**Test**タブに移動し、**Preview message as user**で**Custom user**を選択します。**Custom attribute**フィールドに日付を入力して、その日にサインアップしたユーザーに送信されるコンテンツカードをプレビューします。<br><br>

![「start_date」というカスタム属性の例。]({% image_buster /assets/img/recs/custom_attributes_test.png %})
{% endtab %}

{% tab using Connected Content %}
コネクテッドコンテンツを使用してレコメンデーションエンジンを作成するには、まず以下のいずれかの方法を使用して新しいエンドポイントを作成します。

| オプション | 説明 |
|------|-----------|
| **スプレッドシートの変換** | SheetDPなどのサービスを使用してスプレッドシートをJSON APIエンドポイントに変換し、生成されるAPI URLを控えておきます。 |
| **カスタムエンドポイントの作成** | カスタムビルドの社内エンドポイントを構築し、ホスティングおよびメンテナンスを行います。 |
| **サードパーティエンジンの使用** | [Alloyパートナー]({{site.baseurl}}/partners/message_personalization/)などのサードパーティレコメンデーションエンジンを使用します。[Amazon Personalise]({{site.baseurl}}/partners/amazon_personalize/)、[Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/certona/)、[Dynamic Yield]({{site.baseurl}}/partners/dynamic_yield/)などが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example" }

次に、メッセージ内でLiquidを使用してエンドポイントを呼び出し、カスタム属性値をユーザーのプロファイルと照合して、対応するレコメンデーションを取得します。

{% raw %}
`````````liquid
{% connected_content YOUR_API_URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

以下を置き換えてください。

| 属性 | 置き換え内容 |
| --- | --- |
| `YOUR_API_URL` | 実際のAPIのURLに置き換えます。 |
| `RECOMMENDED_ITEM_IDS` | 推奨アイテムのIDを含むカスタム属性の実際の名前に置き換えます。この属性は、セミコロンで区切られたIDの文字列であることが想定されています。 |
| `ITEM_ID` | アイテムIDに対応するAPIレスポンス内の実際の属性名に置き換えます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example" }

{% alert note %}
これは基本的な例であり、特定のニーズやデータ構造に基づいてさらに修正が必要になる場合があります。詳細なガイダンスについては、[Liquidのドキュメント]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)を参照するか、開発者に相談してください。
{% endalert %}

### 例

Zomato Restaurantsデータベースからおすすめのレストランを取得し、その結果を`restaurants`というローカル変数として保存したいとします。次のコネクテッドコンテンツの呼び出しを行うことができます。

{% raw %}
`````````liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

次に、ユーザーの市区町村と食べ物の種類に基づいておすすめのレストランを取得したいとします。ユーザーの市区町村と料理の種類のカスタム属性を呼び出しの冒頭にダイナミックに挿入し、`restaurants`の値を変数`city_food.restaurants`に代入することで実現できます。

コネクテッドコンテンツの呼び出しは次のようになります。

{% raw %}
`````````liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

レストラン名と評価だけを取得するようにレスポンスを調整したい場合は、次のように呼び出しの最後にフィルターを追加できます。

{% raw %}
`````````liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

最後に、おすすめのレストランを評価別にグループ化したいとします。以下の手順を実行します。

1. `assign`を使用して、「Excellent」、「Very Good」、「Good」の評価カテゴリー用の空の配列を作成します。
2. リスト内の各レストランの評価を調べる`for`ループを追加します。
- 評価が「Excellent」の場合、レストラン名を`excellent_restaurants`文字列に追加し、各レストラン名を区切るために末尾に*文字を追加します。
- 評価が「Very Good」の場合、レストラン名を`very_good_restaurants`文字列に追加し、末尾に*文字を追加します。
- 評価が「Good」の場合、レストラン名を`good_restaurants`文字列に追加し、末尾に*文字を追加します。
3. 返されるおすすめレストランの数を各カテゴリーで4件に制限します。

最終的な呼び出しは次のようになります。

{% raw %}
`````````liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elsif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elsif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

ユーザーのデバイスでのレスポンスの表示例については、以下のスクリーンショットを参照してください。

![最終呼び出しの例によって生成されたレストランリストのレンダリング。]({% image_buster /assets/img/recs/sample_response.png %}){: style="max-width:30%;"}
{% endtab %}
{% endtabs %}