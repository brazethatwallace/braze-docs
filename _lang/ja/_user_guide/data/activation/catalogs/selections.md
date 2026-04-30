---
nav_title: セレクション
article_title: セレクション
page_order: 5
alias: /catalog_selections/
description: "このリファレンス記事では、Braze Campaignでデータを参照するために、カタログでセレクションを作成し使用する方法について説明します。"
---

# セレクション {#selections}

> このページでは、[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)でセレクションを作成し使用する方法について説明します。

## 仕組み {#how-it-works}

セレクションは、Campaignの各ユーザーに対してメッセージをパーソナライズするために使用できるデータのグループです。セレクションを使用すると、カタログの特定の列に基づいてカスタムフィルターを設定することになります。これには、ブランド、サイズ、ロケーション、追加日などのフィルターが含まれます。アイテムが最初に満たすべき基準を定義できるため、ユーザーに何を表示するかをコントロールできます。

カタログを作成した後、Braze Campaignやおすすめにセレクションを組み込むことで、カタログデータをさらに参照できます。

![カタログ例のセレクションセクション。]({% image_buster /assets/img_archive/catalog_selections1.png %})

## 知っておくべきこと {#things-to-know}

- カタログごとに最大30個のセレクションを作成できます。
- セレクションごとに最大10個のフィルターを追加できます。
- セレクションは、Brazeのカタログデータからおすすめを絞り込むのに最適です。インスピレーションをお探しの場合は、[アイテムのおすすめについて]({{site.baseurl}}/user_guide/brazeai/item_recommendations/)にあるユースケースの例を参照してください。

## セレクションの作成 {#creating-a-selection}

セレクションを作成するには、以下の手順に従います。

1. **カタログ**に移動し、リストからカタログを選択します。
2. **セレクション**タブを選択し、**セレクションを作成**をクリックします。
3. セレクションに名前とオプションの説明を入力します。
4. **Filter Field**で、フィルターしたいカタログの列を選択します。1,000文字を超える文字列フィールドはフィルターとして選択できません。
5. 関連する演算子（例:「equals」や「does not equal」）と属性を選択して、フィルター基準の定義を完了します。
6. **Sort type**セクションで、結果のソート方法を決定します。デフォルトでは、結果は順不同で返されます。特定のフィールドでソートするには、**Randomize Sort Order**をオフにし、**Sort Field**と**Sort Order**（昇順または降順）を指定します。
7. **Results limit**セクションで、結果数を入力します（最大50件）。
8. **Create Selection**を選択します。

### テストとプレビュー {#test-and-preview}

セレクションを作成した後、**Preview for user**セクションを使用して、ランダムなユーザーまたは特定のユーザーに対してセレクションが返す結果を確認できます。パーソナライゼーションを使用したセレクションでは、ユーザーを選択した後にのみプレビューを表示できます。

### セレクション結果内のLiquid {#liquid-in-selection-results}

カスタム属性やカスタムイベントなど、カタログ内でLiquidを使用すると、セレクション内のユーザーごとに異なる結果が返される可能性があります。

{% alert note %}
これらのフィルター設定ではコネクテッドコンテンツのLiquidはサポートされていません。
{% endalert %}

![属性がLiquidカスタム属性に設定されているカタログセレクションのフィルター設定。]({% image_buster /assets/img_archive/catalog_selections7.png %})

## メッセージングでセレクションを使用する {#using-selections-in-messaging}

セレクションを作成したら、Liquidでメッセージをパーソナライズし、そのカタログからフィルタリングされたアイテムを挿入します。メッセージ作成画面にあるパーソナライゼーションウィンドウから、BrazeにLiquidを生成させることができます。

1. パーソナライゼーションをサポートするメッセージ作成画面で、<i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="パーソナライゼーションを追加"></i>を選択してパーソナライゼーションウィンドウを開きます。
2. **Personalization Type**で**Catalog Items**を選択します。
3. カタログ名を選択します。
4. **Item selection method**で**Use a selection**を選択します。
4. リストからセレクションを選択します。
5. **Information to Display**で、各アイテムに含めるカタログのフィールドを選択します。
6. **Copy**アイコンを選択し、メッセージ内の必要な場所にLiquidを貼り付けます。

![以下の選択がある「Add Personalization」モーダル:「Personalization Type」に「Catalog Items」、「Catalog Name」に「Games」、「Selection Type」に「Selections」、「Selection」に「game_selection」、「Information to Display」に「title」と「description_en」。]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## ユースケース {#use-case}

例えば、食事の宅配サービスを運営していて、最近閲覧した食品カテゴリーに基づいて特定の食事の好みを持つユーザーにパーソナライズされたメッセージを送りたいとします。

食事宅配サービスの食事名、価格、画像、食事のカテゴリーなどの情報をカタログに使用し、ユーザーが最近閲覧したカテゴリーに基づいて3つの食事をおすすめするセレクションを作成できます。

![食事宅配サービスのセレクション例。2つのフィルターがあり、1つは商品タイプを食事として識別するもの、もう1つはカテゴリーを最近閲覧されたものとして識別するものです。セレクションは、3つの結果が返される順番をランダムにするよう設定されています。]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

このカタログとセレクションをCampaignで使用するには、Campaign構築時のメッセージ作成セクションで**Add Personalization**モーダルを使用します。この例では、食事宅配サービスの情報が含まれるカタログと、最近閲覧したカテゴリーに基づく食事のおすすめセレクションを選択しました。これにより、食事名と価格を表示できます。メッセージをさらに充実させるには、セレクションを使って最初のおすすめ料理の画像を追加することもできます。

![ヘッダーが「You will LOVE these highly rated meals!」のコンテンツカード。メッセージ作成セクションでセレクション「recommendations_be_recent_category」を使用しています。]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

例えば、最近閲覧したカテゴリーが「チキン」のユーザーがいるとします。設定したパーソナライゼーションとコンテンツカードCampaignを使って、このユーザーにチキンを含む3つのおすすめ料理を送ることができます。

![チャーグリルレモンチキンの画像が表示されたコンテンツカードと、ユーザーが最近閲覧したカテゴリーに基づいたチキンを含む3つのおすすめ料理のリスト。]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

同じパーソナライゼーションを使えば、最近閲覧したカテゴリーが「ビーフ」のユーザーに対しても、3つのおすすめ料理を送ることができます。

![ビーフストロガノフの画像が表示されたコンテンツカードと、ユーザーが最近閲覧したカテゴリーに基づいたビーフを含む2つのおすすめ料理のリスト。]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}