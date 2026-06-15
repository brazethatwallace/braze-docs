---
nav_title: おすすめを使用する
article_title: メッセージングでアイテムのおすすめを活用する
description: "この記事では、メッセージでアイテムのおすすめを使用する方法について説明します。"
page_order: 1.2
---

# メッセージングでアイテムのおすすめを活用する {#use-item-recommendations-in-your-messaging}

> おすすめのトレーニングが完了したら、Liquidを使用して`product_recommendation` Liquidオブジェクトを直接操作することで、メッセージ内のおすすめアイテムをフェッチして表示できます。

{% alert tip %}
ステップバイステップのウォークスルーについては、Brazeラーニングコースをご覧ください：[Crafting Personalized Experiences with AI](https://learning.braze.com/ai-item-recommendations-use-case/1996254)。
{% endalert %}

## 前提条件 {#prerequisites}

メッセージングでおすすめを使用する前に、[レコメンデーションエンジンを作成してトレーニングする]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/)必要があります。トレーニングには10分から36時間かかります&#8212;完了時またはエラー発生時にメールが届きます。

## メッセージングでのおすすめの使用 {#using-recommendations-in-your-messaging}

### ステップ 1:Liquidコードの追加 {#step-1-add-liquid-code}

おすすめのトレーニングが完了したら、Liquidでメッセージをパーソナライズして、そのカタログで最も人気のある製品を挿入できます。

{% tabs local %}
{% tab pre-formatted code %}
![パーソナライゼーションタイプとしてアイテムのおすすめを使用した「パーソナライゼーションを追加」モーダル]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

メッセージ作成画面の**Add personalization**セクションからLiquidを生成できます。

1. パーソナライゼーションをサポートするメッセージ作成画面で、<i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="パーソナライゼーションを追加"></i> **Add personalization**を選択してパーソナライゼーションウィンドウを開きます。
2. **Personalization Type**で、**Item Recommendation**を選択します。
3. **Item Recommendation Name**で、先ほど作成したおすすめを選択します。
4. **Number of Predicted Items**で、挿入する上位製品の数を入力します。たとえば、購入数の多い上位3つのアイテムを表示できます。
5. **Information to Display**で、カタログのどのフィールドを各アイテムに含めるかを選択します。各アイテムのこれらのフィールドの値は、このおすすめに関連付けられたカタログから取得されます。
6. **Copy**アイコンを選択し、メッセージ内の必要な場所にLiquidを貼り付けます。
{% endtab %}

{% tab custom code %}
カタログの`product_recommendation`オブジェクトを参照することで、カスタムのLiquidコードを記述できます。これには、そのカタログのダイナミックに生成されたすべての製品レコメンデーションデータが含まれ、オブジェクトの配列として構造化されます。各オブジェクトはおすすめアイテムを表します。

| 仕様 | 詳細 |
|-------------|-------|
| **構造** | 各アイテムは`items[index]`としてアクセスされます。インデックスは0（最初のアイテム）から始まり、後続のアイテムごとにインクリメントされます。|
| **カタログフィールド** | 配列内の各アイテムには、カタログ内のフィールド（列）に対応するキーと値のペアが含まれます。たとえば、製品レコメンデーションの一般的なカタログフィールドには次のようなものがあります：<br>- `name`または`title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 1:Liquidコードの追加" }

`assign`タグを使用して`product_recommendation`データをフェッチし、変数に割り当てます。

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

次のように置き換えます：

| プレースホルダー | 説明 |
|-----------|-----------|
| `recommendation_name` | Brazeで作成したAIレコメンデーションの名前。|
| `items` | おすすめアイテム配列を格納する変数。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 1:Liquidコードの追加" }

次に、配列インデックスとドット表記を使用して、特定のアイテムとそのフィールドを参照します：

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

複数のアイテムを含めるには、各アイテムをインデックスで個別に参照します。`.name`と`.price`は、対応するフィールドをカタログからプルします。

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

AIレコメンデーションは複数の製品を配列として返します。`items[0]`は最初のアイテム、`items[1]`は2番目のアイテム、というようになります。レコメンデーションが1つのアイテムのみを返す場合、`items[1]`を参照しようとすると空のフィールドが返されます。
{% endtab %}
{% endtabs %}

### ステップ 2:画像を参照する（オプション） {#step-2-reference-an-image-optional}

おすすめのカタログに画像リンクが含まれている場合は、メッセージで参照できます。

{% tabs %}
{% tab Drag-and-drop%}
メールのドラッグ＆ドロップエディターで、メールに画像ブロックを追加し、画像ブロックを選択して**Image properties**を開きます。

![ドラッグ＆ドロップエディターの画像プロパティパネル]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

**Image with Liquid**を切り替え、**Dynamic URL**フィールドに以下を追加します（URLフィールドは改行をサポートしていないため、コードが1行で表示されていることを確認してください）：

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}{{ items[0].image_url_field }}
```
{% endraw %}

次のように置き換えます：

| プレースホルダー | 説明 |
|-----------|-----------|
| `recommendation_name` | おすすめの名前。|
| `image_url_field` | 画像URLを含むカタログ内のフィールドの名前。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2:画像を参照する（オプション）" }

プレビューおよびテストメールにプレースホルダー画像を含めるには、**Choose image**を選択し、メディアライブラリから画像を選択するか、ホスティングサイトの画像URLを入力します。
{% endtab %}

{% tab HTML %}
HTML画像参照の場合、画像の`src`属性をカタログの画像URLフィールドに設定します。製品名や説明など、別のフィールドをaltテキストとして使用することもできます。

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

次のように置き換えます：

| プレースホルダー | 説明 |
|-----------|-----------|
| `recommendation_name` | おすすめの名前。|
| `image_url_field` | 画像URLを含むカタログ内のフィールドの名前。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2:画像を参照する（オプション）" }
{% endtab %}
{% endtabs %}