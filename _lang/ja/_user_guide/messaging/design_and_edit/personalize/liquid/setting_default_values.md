---
nav_title: デフォルト値の設定
article_title: Liquid のデフォルト値の設定
page_order: 5
description: "この参照記事では、メッセージで使用するパーソナライゼーション属性にデフォルトのフォールバック値を設定する方法について説明します。"

---

# デフォルト値の設定

{% raw %}

> メッセージで使用するすべてのパーソナライゼーション属性に、デフォルトのフォールバック値を設定できます。この記事では、デフォルト値の仕組み、設定方法、およびメッセージでの使用方法について説明します。

## 仕組み

デフォルト値は、"default" という名前の [Liquid フィルター](http://docs.shopify.com/themes/liquid-documentation/filters)を指定することで追加できます（以下に示すように、`|` を使用してフィルターをインラインで区別します）。

```
| default: 'Insert Your Desired Default Here'
```

デフォルト値が指定されておらず、フィールドがユーザーに存在しないか設定されていない場合、メッセージ内のそのフィールドは空白になります。

以下の例は、デフォルト値を追加するための正しい構文を示しています。この場合、ユーザーの `first_name` フィールドが空または利用できない場合、属性 `{{ ${first_name} }}` の代わりに「Valued User」という文字が表示されます。

`````````liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Janet Doe というユーザーの場合、メッセージは次のいずれかとして表示されます。

```
Hi Janet, thanks for using the App!
```

または...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
デフォルト値は空の値（empty）に対して表示されますが、ブランクの値（blank）に対しては表示されません。空の値は何も含まれていませんが、ブランクの値にはスペースなどの空白文字のみが含まれ、その他の文字は含まれていません。たとえば、空の文字列は `""` のようになり、ブランクの文字列は `" "` のようになります。
{% endalert %}

## さまざまなデータタイプのデフォルト値の設定

上記の例は、文字列のデフォルト値を設定する方法を示しています。`empty`、`nil`（未定義）、または `false` の値を持つ任意の Liquid データタイプに対してデフォルト値を設定できます。これには文字列、ブール値、配列、オブジェクト、数値が含まれます。

### ユースケース: ブール値

`premium_user` というブール値のカスタム属性があり、ユーザーのプレミアムステータスに基づいてパーソナライズされたメッセージを送信したいとします。一部のユーザーにはプレミアムステータスが設定されていないため、それらのユーザーを捕捉するためにデフォルト値を設定する必要があります。

1. `is_premium_user` という変数を `premium_user` 属性に割り当て、デフォルト値を `false` にします。これにより、`premium_user` が `nil` の場合、`is_premium_user` の値はデフォルトで `false` になります。

{% raw %}
`````````liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2. 次に、条件ロジックを使用して、`is_premium_user` が `true` の場合に送信するメッセージを指定します。つまり、`premium_user` が `true` の場合に何を送信するかを指定します。ユーザーの名前がない場合に備えて、名にもデフォルト値を割り当てます。

`````````liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3. 最後に、`is_premium_user` が `false` の場合（つまり `premium_user` が `false` または `nil` の場合）に送信するメッセージを指定します。その後、条件ロジックを閉じます。

`````````liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### ユースケース: 数値

`reward_points` という数値のカスタム属性があり、ユーザーの報酬ポイントを含むメッセージを送信したいとします。一部のユーザーには報酬ポイントが設定されていないため、それらのユーザーに対応するデフォルト値を設定する必要があります。

1. ユーザーの名、または名前がない場合のデフォルト値 `Valued User` でメッセージを開始します。

{% raw %}
`````````liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. `reward_points` というカスタム属性を使用し、デフォルト値を `0` にして、ユーザーの報酬ポイント数でメッセージを終了します。`reward_points` が `nil` の値を持つすべてのユーザーには、メッセージ内で報酬ポイントが `0` と表示されます。

{% raw %}
`````````liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### ユースケース: オブジェクト

`city` と `state` のプロパティを含む `location` という階層化カスタム属性オブジェクトがあるとします。これらのプロパティのいずれかが設定されていない場合、ユーザーに提供を促したいとします。

1. ユーザーの名で呼びかけ、名前がない場合のデフォルト値を含めます。

{% raw %}
`````````liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. ユーザーのロケーションを確認したい旨のメッセージを記述します。

{% raw %}
`````````liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3. ユーザーのロケーションをメッセージに挿入し、住所プロパティが設定されていない場合のデフォルト値を割り当てます。

{% raw %}
`````````liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### ユースケース: 配列

`upcoming_trips` という配列のカスタム属性があり、`destination` と `departure_date` のプロパティを持つ旅行が含まれているとします。旅行がスケジュールされているかどうかに基づいて、ユーザーにパーソナライズされたメッセージを送信したいとします。

1. `upcoming_trips` が `empty` の場合にメッセージを送信しないように条件ロジックを記述します。

{% raw %}
`````````liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2. `upcoming_trips` にコンテンツがある場合に送信するメッセージを指定します。<br><br>**2a.** ユーザーに呼びかけ、名前がない場合のデフォルト値を含めます。<br>**2b.** `for` タグを使用して、`upcoming_trips` に含まれる各旅行のプロパティ（情報）を取得することを指定します。<br>**2c.** メッセージにプロパティを一覧表示し、`departure_date` が設定されていない場合のデフォルト値を含めます。（旅行を作成するには `destination` が必須であるため、そのデフォルト値を設定する必要はありません。）<br>**2d.** `for` タグを閉じ、条件ロジックを閉じます。

{% raw %}
`````````liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
`````````liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values