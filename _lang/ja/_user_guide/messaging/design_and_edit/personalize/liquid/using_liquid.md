---
nav_title: Liquidの使用
article_title: Liquidの使用
page_order: 0
description: "このリファレンス記事では、一般的なLiquidのユースケースの概要と、メッセージングにLiquidタグを含める方法について説明します。"
search_rank: 2
---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Liquidの使用 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdynamic-personalization-with-liquid-stylefloatrightwidth120pxborder0-classnoimgborderuse-liquid}

> この記事では、さまざまなユーザー属性を使用して、メッセージングにパーソナル情報をダイナミックに挿入する方法を説明します。

Liquidは、Shopifyが開発し、Rubyで記述されたオープンソースのテンプレート言語です。Brazeでは、Liquidを使用してユーザープロファイルデータをメッセージに取り込み、そのデータをカスタマイズできます。たとえば、Liquidタグを使用して条件付きメッセージを作成し、ユーザーの購読記念日に基づいて異なるオファーを送信できます。さらに、フィルターを使用してデータを操作できます。たとえば、ユーザーの登録日をタイムスタンプから「2022年1月15日」のようなより読みやすい形式にフォーマットできます。Liquidの構文と機能の詳細については、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照してください。

## 仕組み {#how-it-works}

Liquidタグはメッセージ内のプレースホルダーとして機能し、ユーザーのアカウントから同意済みの情報を取得して、パーソナライゼーションや適切なメッセージング手法を実現します。

以下のブロックでは、Liquidタグを2つの用途で使用しています。1つはユーザーの名を呼び出すため、もう1つはユーザーの名が登録されていない場合のデフォルトタグです。

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Janet Doe というユーザーの場合、メッセージは次のいずれかで表示されます。

```
Hi Janet, thanks for using the App!
```

または...

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
HTMLコメント（`<!-- -->`）はLiquidが読み込まれる前に削除されるため、HTMLコメント内のLiquidタグはメッセージに**レンダリングされません**。正しくレンダリングするには、使用したいすべてのLiquidタグがHTMLコメントの外側にあることを確認してください。
{% endalert %}

## 代入可能なサポート対象の値 {#supported-values-to-substitute}

利用可能な場合、以下の値をメッセージに代入できます。

- [基本的なユーザー情報]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)（例: `first_name`、`last_name`、`email_address`）
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
    - [階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#liquid-templating)
- [カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [最後に使用したデバイスの情報]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information)
- [ターゲットデバイスの情報]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information)

また、Brazeの[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を使用して、Webサーバーからコンテンツを直接取得することもできます。

{% alert important %}
Brazeは現在、ShopifyのLiquid 5までをサポートしています。
{% endalert %}

## Liquidの使用 {#using-liquid}

[Liquidタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を使用すると、パーソナルなタッチでメッセージを充実させ、メッセージの品質を高めることができます。

### Liquidの構文 {#liquid-syntax}

Liquidには特定の構造、つまり構文があり、ダイナミックなパーソナライゼーションを作成する際に留意する必要があります。以下にいくつかの基本的なルールを示します。

- **Brazeではストレートクォートを使用してください：** カーリークォート（**' '**）とストレートクォート（**&#39; &#39;**）には違いがあります。BrazeのLiquidではストレートクォート（**&#39; &#39;**）を使用してください。特定のテキストエディターからコピー＆ペーストすると、カーリークォートが表示される場合があり、Liquidで問題が発生する可能性があります。Brazeダッシュボードに直接クォートを入力する場合は問題ありません。
- **ブラケットはペアで使用します：** すべてのブラケットは開きと閉じの両方が必要です **{ }**。必ず波括弧を使用してください。
- **if文はペアで使用します：** すべての`if`に対して、`if`文が終了したことを示す`endif`が必要です。
- **case文はペアで使用します：** すべての`case`に対して、ブロックを閉じる`endcase`が必要です。
- **変数名にはASCII文字を使用してください：** Liquid変数名（`assign`または`capture`で作成）は、ASCII文字、数字、アンダースコアのみをサポートしています。Brazeパーソナライゼーション属性名（`custom_attribute.${...}`や`event_properties.${...}`内）には非ASCII文字を含めることができます。
- **複数行の`assign`タグではBraze Liquid変数を囲んでください：** `assign`が複数行にまたがる場合は、Braze Liquid変数を二重波括弧{% raw %}（`{{ }}`）{% endraw %}で囲んでください。

#### 複数行の`assign`タグ {#multi-line-assign-tags}

`assign`を複数行に分割できます（たとえば、閉じタグの前に`|`でフィルターを続ける場合）。ただし、すべてのBraze Liquid変数を二重波括弧{% raw %}（`{{ }}`）{% endraw %}で囲む必要があります。これらの波括弧がないと、複数行のassign文で予期しないレンダリングが発生する可能性があり、カスタム属性のテンプレート化に失敗することがあります。以下は、動作する複数行assignの例です。

{% raw %}
```liquid
{%- assign color = {{custom_attribute.${favorite_color}}}
| default: {{custom_attribute.${fav_color}}}
| default: 'blue'
%}
```

`assign`全体を1行で記述することもできます。

```liquid
{%- assign color = custom_attribute.${favorite_color} | default: custom_attribute.${fav_color} | default: 'blue' %}
```
{% endraw %}

#### 演算子とフィルターの使用場所 {#where-to-use-operators-and-filters}

演算子（`==`、`!=`、`>`、`and`、`or`など）とフィルター（`| size`、`| plus`など）は、それぞれ特定のLiquidコンテキストでのみ使用できます。

| コンテキスト | 演算子 | フィルター |
|-----------|-----------|---------|
| `assign` | サポートされていません | サポートされています |
| `if`、`elsif`、`unless` | サポートされています | サポートされていません |
| `case`、`when` | 等価一致のみ[^case_when_ops] | サポートされていません |
| `for` | サポートされていません | サポートされていません |
| 配列アクセス（`[ ]`） | サポートされていません | サポートされていません |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="演算子とフィルターの使用場所" }

[^case_when_ops]: `case`タグと`when`タグでは、Liquidは`case`式を各`when`値と等価比較します（`if`と`elsif`を`==`で連鎖させるのと同様です）。`if`や`elsif`のように、`when`句内で任意の比較演算子や論理演算子を使用することはできません。例については、[条件付きメッセージングロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when)を参照してください。

フィルターをサポートしていないコンテキストでフィルター処理された値が必要な場合は、まず結果を変数に代入してください。

{% raw %}

##### 条件文でフィルター結果を使用する {#use-a-filter-result-in-a-conditional}

条件文でフィルターを直接使用することはできません。以下は正しくありません。

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

代わりに、フィルター結果を変数に代入してください。

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### forループでフィルター結果を使用する {#use-a-filter-result-in-a-for-loop}

`for`ループのイテラブルにフィルターを適用することはできません。以下は正しくありません。

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

代わりに、フィルター処理された値を変数に代入してください。

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### 配列アクセスでフィルター結果を使用する {#use-a-filter-result-for-array-access}

角括弧内でフィルターを使用することはできません。以下は正しくありません。

```liquid
{{ my_array[my_var | minus: 1] }}
```

代わりに、まずフィルター処理された値を代入してください。

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### 比較結果を変数に格納する {#store-a-comparison-result-in-a-variable}

`assign`文で演算子を使用することはできません。以下は正しくありません。

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

代わりに、条件文を使用して変数を設定してください。

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### デフォルト属性とカスタム属性 {#default-attributes-and-custom-attributes}

{% raw %}

メッセージに`{{${first_name}}}`というテキストを含めると、メッセージ送信時にユーザーの名（ユーザープロファイルから取得）が置換されます。他のデフォルトユーザー属性にも同じ形式を使用できます。

カスタム属性の値を使用する場合は、変数に「custom_attribute」という名前空間を追加する必要があります。たとえば、「zip code」というカスタム属性を使用するには、メッセージに`{{custom_attribute.${zip code}}}`を含めます。

### タグの挿入 {#inserting-tags}

任意のメッセージで2つの開き波括弧`{{`を入力すると、タグを挿入できます。これにより、入力に応じて更新され続けるオートコンプリート機能がトリガーされます。入力中に表示されるオプションから変数を選択することもできます。

カスタムタグを使用している場合は、タグをコピーして任意のメッセージに貼り付けることができます。

#### 二重括弧の例外 {#exceptions-for-double-brackets}

`{% assign %}`や`{% if %}`などの別のLiquidタグ内でタグを使用する場合、二重括弧を使用するか、括弧なしで使用できます。タグが単独で使用される場合のみ、二重括弧で囲む必要があります。簡単にするために、常に二重括弧を使用できます。

以下のタグはすべて正しいです。

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

メールメッセージでLiquidを使用する場合は、以下の点に注意してください。

1. クラシックエディターではなく、HTMLエディターを使用して挿入してください。クラシックエディターではLiquidがプレーンテキストとして解析される場合があります。たとえば、Liquidはユーザーの名をテンプレート化する代わりに、{% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %}として解析されます。
2. Liquidコードは`<body>`タグ内にのみ配置してください。このタグの外に配置すると、配信時にレンダリングが不安定になる可能性があります。

{% endalert %}

### HTMLエディターとクラシックエディターの切り替え {#switching-between-html-and-classic-editors}

HTMLエディターとクラシックエディターを切り替えると、LiquidスニペットやContent Blocksがメッセージ内で位置がずれる場合があります。エディターを切り替えた後にテンプレートを確認してください。より予測可能なレイアウト制御が必要な場合は、ドラッグ＆ドロップエディターを使用してください。

### 事前フォーマットされた変数の挿入 {#inserting-pre-formatted-variables}

テンプレート化されたテキストフィールドの近くにある**パーソナライゼーションを追加**モーダルから、デフォルト値付きの事前フォーマットされた変数を挿入できます。

![パーソナライゼーションの挿入を選択した後に表示される「パーソナライゼーションを追加」モーダル。モーダルには、パーソナライゼーションタイプ、属性、オプションのデフォルト値のフィールドがあり、Liquid構文のプレビューが表示されます。]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

モーダルは、カーソルがあった位置に指定したデフォルト値を含むLiquidを挿入します。挿入位置はプレビューボックスでも指定され、前後のテキストが表示されます。テキストブロックがハイライトされている場合、ハイライトされたテキストが置換されます。

![「パーソナライゼーションを追加」モーダルのGIF。ユーザーがデフォルト値として「fellow traveler」を挿入し、モーダルがコンポーザー内のハイライトされたテキスト「name」をLiquidスニペットに置換する様子を示しています。]({% image_buster /assets/img_archive/insert_var_shot.gif %})