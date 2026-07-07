---
nav_title: 条件付きメッセージングロジック
article_title: 条件付き Liquid メッセージングロジック
page_order: 6
description: "このリファレンス記事では、キャンペーンでタグをどのように使用できるか、また使用すべきかについて説明します。"

---

# 条件付きメッセージングロジック {#conditional-messaging-logic}

> [タグ](https://docs.shopify.com/themes/liquid-documentation/tags)を使用すると、メッセージングキャンペーンにプログラミングロジックを含めることができます。タグは、条件文の実行や、変数の割り当てやコードブロックの反復処理などの高度なユースケースに使用できます。<br><br>このページでは、null、nil、blankの属性値の処理方法やカスタム属性の参照方法など、タグの使用方法について説明します。

## タグのフォーマット {#formatting-tags}

{% raw %}
タグは `{% %}` で囲む必要があります。
{% endraw %}

作業を少し楽にするために、Brazeでは Liquid 構文が正しくフォーマットされている場合に緑色と紫色で表示されるカラーフォーマットが含まれています。緑色のフォーマットはタグの識別に役立ち、紫色のフォーマットはパーソナライゼーションを含む領域をハイライトします。

条件付きメッセージングの使用に苦労している場合は、カスタム属性やその他の Liquid 要素を挿入する前に、条件構文を書き出してみてください。

たとえば、まず以下をメッセージフィールドに追加します:
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

緑色でハイライトされることを確認してから、`X` をメッセージフィールドの角にある青い `+` を使って選択した Liquid またはコネクテッドコンテンツに置き換え、`0` を希望の値に置き換えます。
<br><br>
次に、`else` 条件の間に必要に応じてメッセージバリエーションを追加します:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## 条件ロジック {#conditional-logic}

[メッセージ内にインテリジェントロジック](http://docs.shopify.com/themes/liquid-documentation/basics)を多数含めることができます（条件文など）。以下の例では、[条件](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags)を使用してキャンペーンを国際化しています:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### 条件タグ {#conditional-tags}

#### `if` と `elsif` {#if-and-elsif}

条件ロジックは `if` タグで始まり、最初にチェックする条件を記述します。後続の条件は `elsif` タグを使用し、前の条件が満たされない場合にチェックされます。この例では、ユーザーのデバイスが英語に設定されていない場合、このコードはユーザーのデバイスがスペイン語に設定されているかどうかをチェックし、それも該当しない場合はデバイスが中国語に設定されているかどうかをチェックします。ユーザーのデバイスがこれらの条件のいずれかを満たす場合、ユーザーは該当する言語でメッセージを受け取ります。

#### `else`

条件ロジックに `{% else %}` 文を含めることもできます。設定した条件のいずれも満たされない場合、`{% else %}` 文は送信すべきメッセージを指定します。この例では、ユーザーの言語が英語、スペイン語、中国語のいずれでもない場合、デフォルトで英語になります。

#### `case` と `when` {#case-and-when}

`{% case %}`、`{% when %}`、`{% endcase %}` は switch 文のように機能します。`case` の後に1つの式を設定し、各 `when` ブランチはその式がリストされた値と等しい場合に実行されます（Liquidは内部的に等価比較を使用しており、`if` と `elsif` を `==` で連鎖させるのと同様です）。1つの `when` タグにカンマまたは `or` で区切って複数の値をリストできます。何も一致しない場合のフォールバックには `{% else %}` を使用し、`{% endcase %}` で閉じます。

`when` の値のフォーマットをデータタイプに合わせてください。テキスト（言語コードなど）の場合は引用符を使用します: `{% when 'es' %}`。数値の場合は引用符を省略します: `{% when 2 %}`。

```liquid
{% assign handle = 'cake' %}
{% case handle %}
{% when 'cake' %}
This is a cake
{% when 'cookie' %}
This is a cookie
{% else %}
This is not a cake nor a cookie
{% endcase %}
```

`handle` の代わりにBrazeのパーソナライゼーションタグやその他の Liquid 式を使用して同じパターンを適用できます。構文オプションの詳細については、Shopifyの [`case` タグドキュメント](https://shopify.dev/docs/api/liquid/tags/case)を参照してください。

#### `endif`

`{% endif %}` タグは `if` ブロックが終了したことを示します。そのチェーン内で `if`、`elsif`、`unless`、または `else` を使用するすべてのメッセージに `{% endif %}` タグを含める必要があります。`{% endif %}` タグを含めないと、Brazeがメッセージを解析できないためエラーが発生します。`{% case %}` を使用する場合は、`{% endif %}` ではなく `{% endcase %}` でブロックを閉じてください。

{% alert note %}
`if`、`elsif`、`unless` タグでは演算子を使用できますが、フィルターは使用できません。`case` と `when` タグでは、`case` 式が `when` の値と等しい場合に各ブランチが一致します。これらの式でもフィルターはサポートされていません。フィルター処理された値を評価するには、まずフィルター結果を変数に割り当ててから、その変数を `case` または `when` 句で参照してください。詳細については、[演算子とフィルターの使用場所]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#where-to-use-operators-and-filters)を参照してください。
{% endalert %}

### チュートリアル: ロケーションベースのコンテンツを配信する {#tutorial-deliver-location-based-content}

このチュートリアルを完了すると、「if」、「elsif」、「else」文を含むタグを使用して、ユーザーのロケーションに基づいたコンテンツを配信できるようになります。

1. まず `if` タグで、ユーザーの市区町村がニューヨークの場合に送信するメッセージを設定します。ユーザーの市区町村がニューヨークの場合、この最初の条件が満たされ、ユーザーはニューヨーカーであることを示すメッセージを受け取ります。

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at your local Sandwich Emperor.
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2. 次に、`elseif` タグを使用して、ユーザーの市区町村がロサンゼルスの場合に送信するメッセージを設定します。

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3. もう1つ `elseif` タグを使用して、ユーザーの市区町村がシカゴの場合に送信するメッセージを設定しましょう。

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
```

{: start="4"}
4. 次に、`{% else %}` タグを使用して、ユーザーの市区町村がサンフランシスコ、ニューヨーク、シカゴのいずれでもない場合に送信するメッセージを指定しましょう。

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5. 最後に、`{% endif %}` タグを使用して条件ロジックが完了したことを指定します。

```liquid
{% endif %}
```

{% endraw %}

{% details 完全な Liquid コード %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at our New York location.
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## null、nil、blankの属性値の処理 {#accounting-for-null-nil-and-blank-attribute-values}

条件ロジックは、ユーザープロファイルに設定されていない属性値を処理するのに便利な方法です。

### nullおよびnilの属性値 {#null-and-nil-attribute-values}

nullまたはnilの値は、カスタム属性の値が設定されていない場合に発生します。たとえば、まだ名を設定していないユーザーは、Brazeに名が記録されていません。

状況によっては、名が設定されているユーザーと名が設定されていないユーザーに、まったく異なるメッセージを送信したい場合があります。

以下のタグを使用すると、「名」属性がnullのユーザーに対するメッセージを指定できます:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %}

![Brazeダッシュボードでの、nullの「名」属性を使用したメッセージの例。]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

nullの属性値は、値の型に厳密に関連付けられていないことに注意してください（たとえば、「null」の文字列は「null」の配列と同じです）。そのため、上記の例では、nullの属性値は未設定の名を参照しており、これは文字列になります。

{% endraw %}

### blankの属性値 {#blank-attribute-values}

blankの値は、ユーザープロファイルの属性が設定されていない場合、空白文字列（` `）で設定されている場合、または `false` として設定されている場合に発生します。blankの値は、Liquid 処理エラーを回避するために、他の変数より先にチェックする必要があります。

以下のタグを使用すると、「名」属性がblankのユーザーに対するメッセージを指定できます。

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %}

## カスタム属性の参照 {#referencing-custom-attributes}

[カスタム属性を作成]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes)した後、Liquid メッセージングでこれらのカスタム属性を参照できます。

条件ロジックを使用する場合、正しい構文を使用するために、カスタム属性のデータタイプを知る必要があります。ダッシュボードの**カスタム属性**ページから、カスタム属性に関連付けられたデータタイプを確認し、各データタイプに対して以下に記載されている例を参照してください。

![カスタム属性のデータタイプの選択。この例では、Favorite_Category という属性がデータタイプ string で表示されています。]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
文字列と配列はストレートアポストロフィで囲む必要がありますが、ブール値と整数にはアポストロフィは不要です。
{% endalert %}

#### ブール値 {#boolean}

[ブール値]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#booleans)はバイナリ値で、`registration_complete: true` のように `true` または `false` に設定できます。ブール値にはアポストロフィは付きません。

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

#### 数値 {#number}

[数値]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#numbers)は整数または浮動小数点数の数値です。たとえば、ユーザーは `shoe_size: 10` や `levels_completed: 287` を持つことがあります。数値にはアポストロフィは付きません。

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

整数に対しては、小なり（<）や大なり（>）などの他の[基本演算子](https://shopify.dev/docs/themes/liquid/reference/basics/operators)も使用できます:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

#### 文字列 {#string}

[文字列]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#strings)は英数字で構成され、ユーザーに関するデータを格納します。たとえば、`favorite_color: red` や `phone_number: 3025981329` などがあります。文字列の値はアポストロフィで囲む必要があります。

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

文字列の場合、Liquidで「==」と「contains」の両方を使用できます。

#### 配列 {#array}

[配列]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#arrays)は、ユーザーに関する情報のリストです。たとえば、ユーザーは `last_viewed_shows: stranger things, planet earth, westworld` を持つことがあります。配列の値はアポストロフィで囲む必要があります。

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

配列の場合、「contains」を使用する必要があり、「==」は使用できません。

#### 時間 {#time}

イベントが発生した時点のタイムスタンプです。[時間]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#time)の値を条件ロジックで使用するには、[数学フィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#math-filters)を適用する必要があります。

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %}
```

{% endraw %}