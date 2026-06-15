---
nav_title: オブジェクト配列
article_title: オブジェクト配列
alias: "/array_of_objects/"
page_order: 2
page_type: reference
description: "このリファレンス記事では、オブジェクト配列をカスタム属性のデータタイプとして使用する方法について、制限事項や使用例も含めて説明します。"
---

# オブジェクト配列 {#array-of-objects}

> このページでは、オブジェクトの配列を使って関連する属性をグループ化する方法を説明します。例えば、1人のユーザーに属するペットオブジェクト、曲オブジェクト、アカウントオブジェクトをすべて含むグループがあるとします。これらのオブジェクト配列を使用して、Liquidでメッセージングをパーソナライズしたり、オブジェクト内のいずれかの要素が条件に一致する場合にオーディエンスSegmentを作成したりできます。

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 考慮事項 {#considerations}

- オブジェクトの配列は、APIを通じて送信されるカスタム属性を対象としています。CSVアップロードはサポートされていません。これは、CSVファイル内のカンマが列区切りとして解釈され、値内のカンマがパースエラーを引き起こすためです。
- オブジェクトの配列にはアイテム数の制限はありませんが、最大サイズは100&nbsp;KBです。更新（`$add`や`$update`など）によって配列がこの制限を超える場合、Brazeはその更新を破棄し、属性は変更されません。APIリクエスト自体は成功レスポンスを返します。新しいアイテムを追加できるように配列を制限内に収めるには、まず`$remove`を使用して配列からアイテムを削除してください。
- すべてのBrazeパートナーがオブジェクト配列をサポートしているわけではありません。連携がこの機能をサポートしているかどうかは、[パートナードキュメント]({{site.baseurl}}/partners/home/)を参照して確認してください。

配列内のアイテムを更新または削除するには、キーと値でアイテムを識別する必要があるため、配列内の各アイテムに一意の識別子を含めることを検討してください。一意性は配列内のみにスコープされ、配列から特定のオブジェクトを更新および削除する場合に役立ちます。これはBrazeによって強制されるものではありません。

{% alert important %}
リクエスト内の階層化カスタム属性に無効な値（無効な時刻形式や`null`値など）が含まれている場合、Brazeはそのリクエスト内のすべての階層化カスタム属性の更新を処理から除外します。これは、その特定の属性内のすべての階層化構造に適用されます。送信前に、階層化カスタム属性内のすべての値が有効であることを確認してください。詳細については、[ユーザーの作成と更新]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#how-does-userstrack-handle-invalid-nested-custom-attributes)を参照してください。
{% endalert %}

{% alert tip %}
ユーザー属性オブジェクトでのオブジェクト配列の使用について詳しくは、[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens)を参照してください。
{% endalert %}

## APIの例 {#api-example}

これらの例は、オブジェクトの配列として保存される階層化カスタム属性を作成または更新する`/users/track`リクエストを送信する際に使用します。ペイロードは`$add`、`$remove`、`$update`演算子を使用するため、リクエストごとに配列全体を再構築することなく、特定のオブジェクトを変更できます。

{% tabs local %}
{% tab 作成 %}

以下は、`pets`配列を使用した`/users/track`の例です。ペットのプロパティをキャプチャするには、`pets`をオブジェクトの配列としてリストするAPIリクエストを送信します。各オブジェクトには、後で更新を行う際に参照できる一意の`id`が割り当てられていることに注意してください。

この形式は、属性を初めて作成する場合や、配列全体を新しいベースラインのオブジェクトセットで置き換える場合に使用します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab 追加 %}

`$add`演算子を使用して、配列に別のアイテムを追加します。以下の例は、ユーザーの`pets`配列にさらに3つのペットオブジェクトを追加する方法を示しています。

`$add`は、1つ以上の新しいオブジェクトを追加し、既存のオブジェクトを変更しない場合に使用します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab 更新 %}

`_merge_objects`パラメーターと`$update`演算子を使用して、配列内の特定のオブジェクトの値を更新します。他の[階層化カスタム属性]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body)オブジェクトの更新と同様に、ディープマージが実行されます。

`$update`は、配列内のオブジェクトからネストされたプロパティを削除するためには使用できないことに注意してください。これを行うには、配列からアイテム全体を削除し、その特定のキーを含まないオブジェクトを追加する必要があります（`$remove`と`$add`の組み合わせを使用）。

`$update`は、オブジェクトが既に存在し、`$identifier_key`と`$identifier_value`で一致させて1つ以上のフィールドを変更する場合に使用します。

以下の例は、`id`が`4`のオブジェクトの`breed`プロパティを`goldfish`に更新する方法を示しています。このリクエスト例では、`id`が`5`のオブジェクトの`name`も`Annette`に更新しています。`_merge_objects`パラメーターが`true`に設定されているため、これら2つのオブジェクトの他のすべてのフィールドはそのまま維持されます。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
`_merge_objects`をtrueに設定する必要があります。設定しない場合、オブジェクトが上書きされます。`_merge_objects`はデフォルトでfalseです。
{% endalert %}

{% endtab %}
{% tab 削除 %}

`$remove`演算子を一致するキー（`$identifier_key`）と値（`$identifier_value`）と組み合わせて使用し、配列からオブジェクトを削除します。

`$remove`は、`id = 2`や`type = dog`など、既知の識別子ペアに一致するすべてのオブジェクトを削除する場合に使用します。

以下の例は、`pets`配列内で`id`の値が`1`のオブジェクト、`id`の値が`2`のオブジェクト、および`type`の値が`dog`のオブジェクトを削除する方法を示しています。`type`の値が`dog`のオブジェクトが複数ある場合、一致するすべてのオブジェクトが削除されます。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### 処理順序 {#processing-order}

単一の`/users/track`リクエストに同じ配列属性に対する`$add`、`$remove`、`$update`操作が含まれている場合、Brazeは以下の順序で処理します。

1. `$add`
2. `$remove`
3. `$update`

この順序は、1つのリクエスト内の単一の属性更新オブジェクト内で適用され、すべての操作が評価された後の配列の最終状態を決定します。

`$add`が`$remove`より先に実行されるため、単一のリクエスト内で`$remove`の後に`$add`を行うアップサートメカニズムは使用できません。`$add`が最初に処理され、その後`$remove`がアイテムを削除します。アップサートを行うには、`$add`の前に別のリクエストで`$remove`を送信してください。

### タイムスタンプ {#timestamps}

オブジェクトの配列にタイムスタンプなどのフィールドを含める場合は、プレーンな文字列やUnixエポック整数ではなく、`$time`形式を使用してください。

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/)を参照してください。
{% endalert %}

## SDKの例 {#sdk-example}

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab 作成 %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab 追加 %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab 更新 %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab 削除 %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab 作成 %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Gus"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab 追加 %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Doug"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Larry"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Mary"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab 更新 %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab 削除 %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
階層化カスタム属性はAppboyKitではサポートされていません。
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab 作成 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab 追加 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab 更新 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab 削除 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Liquidテンプレート {#liquid-templating}

この`pets`配列を使用してメッセージをパーソナライズできます。以下のLiquidテンプレートの例は、前述のAPIリクエストから保存されたカスタム属性オブジェクトのプロパティを参照し、メッセージングで使用する方法を示しています。

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %}

{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %}
```
{% endraw %}

このシナリオでは、Liquidを使用して`pets`配列をループし、各ペットについてのステートメントを出力できます。`pets`カスタム属性に[変数を割り当て]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#assigning-variables)、ドット記法を使用してオブジェクトのプロパティにアクセスします。オブジェクト名の後にピリオド`.`を付け、その後にプロパティ名を指定します。

## セグメンテーション {#segmentation}

オブジェクトの配列に基づいてユーザーをセグメント化する場合、配列内のいずれかのオブジェクトが条件に一致すると、そのユーザーはSegmentの対象となります。

新しいSegmentを作成し、フィルターとして**階層化カスタム属性**を選択します。次に、オブジェクト配列の名前を検索して選択します。

![オブジェクト配列でフィルタリング。]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

ドット記法を使用して、オブジェクトの配列内のどのフィールドを使用するかを指定します。テキストフィールドの先頭に空の角括弧`[]`を付けて、オブジェクトの配列内を検索していることをBrazeに伝えます。その後、ピリオド`.`を追加し、使用するフィールド名を続けます。

たとえば、`type`フィールドに基づいて`top_3_movies`オブジェクト配列をフィルタリングする場合は、`[].type`と入力し、`Fantasy Movie`などフィルタリングする映画を選択します。


### ネストのレベル {#levels-of-nesting}

配列のネストは1レベルまで（配列内の配列）でSegmentを作成できます。たとえば、以下の属性の場合、`pets[].name`に`Gus`が含まれるSegmentは作成できますが、`pets[].nicknames[]`に`Gugu`が含まれるSegmentは作成できません。

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## データポイント {#data-points}

データポイントは、プロパティの作成、更新、削除のいずれを行うかによって、異なる方法で記録されます。

{% tabs local %}
{% tab 作成 %}

新しい配列を作成すると、オブジェクト内の各属性に対して1データポイントが記録されます。この例では8データポイントを消費します。各ペットオブジェクトには4つの属性があり、オブジェクトが2つあるためです。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab 更新 %}

既存の配列を更新すると、追加された各プロパティに対して1データポイントが記録されます。この例では、2つのオブジェクトそれぞれで1つのプロパティのみを更新しているため、2データポイントを消費します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab 削除 %}

配列からオブジェクトを削除すると、送信した各削除条件に対して1データポイントが記録されます。この例では、このステートメントで複数の犬を削除する可能性がありますが、3データポイントを消費します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}