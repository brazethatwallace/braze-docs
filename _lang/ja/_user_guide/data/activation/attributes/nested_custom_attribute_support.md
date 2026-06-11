---
nav_title: 階層化カスタム属性
article_title: 階層化カスタム属性
alias: "/nested_custom_attribute_support/"
page_order: 3
page_type: reference
description: "このリファレンス記事では、階層化カスタム属性をカスタム属性のデータ型として使用する方法について、制限事項や使用例を含めて説明します。"
---

# 階層化カスタム属性 {#nested-custom-attributes}

> このページでは、階層化カスタム属性について説明します。これにより、属性のセットを別の属性のプロパティとして定義できます。つまり、カスタム属性オブジェクトを定義するときに、そのオブジェクトに一連の追加属性を定義できます。

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 考慮事項 {#considerations}

- 階層化カスタム属性は、Braze SDKまたはAPIを介して送信されるカスタム属性を対象としています。
- オブジェクトの最大サイズは100&nbsp;KBです。更新によりオブジェクトが100&nbsp;KBを超える場合、Brazeはその更新を破棄し、属性は変更されません。
- キー名と文字列値のサイズ上限は255文字です。
- キー名にスペースを含めることはできません。
- ピリオド（`.`）とドル記号（`$`）は、階層化カスタム属性をユーザープロファイルに送信しようとする場合、APIペイロードではサポートされていない文字です。
- すべてのBrazeパートナーが階層化カスタム属性をサポートしているわけではありません。特定のパートナー連携がこの機能をサポートしているかどうかを確認するには、[パートナーのドキュメント]({{site.baseurl}}/partners/home/)を参照してください。
- 階層化カスタム属性は、Connected AudienceのAPI呼び出しを行うときのフィルターとして使用できません。
- デフォルトでは、**階層化カスタム属性**のSegmentフィルターには、オブジェクト型カスタム属性、オブジェクト配列属性、および配列型カスタム属性が含まれます。属性を選択すると、プロパティスキーマセレクターにネストされた配列フィールドの配列パス（`[]` 表記を使用）が含まれます。そのフィルターからトップレベルの配列カスタム属性を非表示にするには、[Brazeサポート]({{site.baseurl}}/braze_support/)にお問い合わせください。

## APIの例 {#api-example}

{% tabs local %}
{% tab 作成 %}
以下は、「再生回数が最も多い曲」オブジェクトを使用した `/users/track` の例です。曲のプロパティをキャプチャするために、`most_played_song` をオブジェクトとして、一連のオブジェクトプロパティとともにリストするAPIリクエストを送信します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab 更新 %}
既存のオブジェクトを更新するには、リクエストに `_merge_objects` パラメーターを含めたPOSTを `users/track` に送信します。これにより、更新内容が既存のオブジェクトデータとディープマージされます。ディープマージにより、最初のレベルだけでなく、オブジェクトのすべてのレベルが別のオブジェクトにマージされます。この例では、Brazeにすでに `most_played_song` オブジェクトがあり、`most_played_song` オブジェクトに新しいフィールド `year_released` を追加します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

このリクエストが受信されると、カスタム属性オブジェクトは次のようになります。

```json
{"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}}
```

{% alert warning %}
`_merge_objects` を `true` に設定する必要があります。設定しない場合、オブジェクトは上書きされます。`_merge_objects` はデフォルトで `false` です。
{% endalert %}

{% endtab %}
{% tab 削除 %}
カスタム属性オブジェクトを削除するには、カスタム属性オブジェクトを `null` に設定して `users/track` にPOSTを送信します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
このアプローチは、[オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/)内のネストされたキーを削除するためには使用できません。
{% endalert %}

{% endtab %}
{% endtabs %}

## SDKの例 {#sdk-example}

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**作成**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**更新**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**削除**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**作成**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**更新**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**削除**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**作成**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**更新**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**削除**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## オブジェクトプロパティとしての日付のキャプチャ {#capturing-dates-as-object-properties}

オブジェクトプロパティとして日付をキャプチャするには、`$time` キーを使用する必要があります。以下の例では、「Important Dates」オブジェクトを使用して、`birthday` と `wedding_anniversary` というオブジェクトプロパティのセットをキャプチャしています。これらの日付の値は `$time` キーを持つオブジェクトであり、null値にすることはできません。

{% alert note %}
最初にオブジェクトプロパティとして日付をキャプチャしていなかった場合は、すべてのユーザーに対して `$time` キーを使用してこのデータを再送信することをお勧めします。そうしないと、`$time` 属性を使用する際にSegmentが不完全になる可能性があります。ただし、階層化カスタム属性内の `$time` の値が正しくフォーマットされていない場合、階層化カスタム属性全体が更新されません。
{% endalert %}

```json
{
  "attributes": [
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
階層化カスタム属性の場合、年が0未満または3000より大きい場合、Brazeはこれらの値をユーザーに保存しません。
{% endalert %}

## Liquidテンプレート {#liquid-templating}

以下のLiquidテンプレートの例では、前述のAPIリクエストから保存されたカスタム属性オブジェクトのプロパティを参照し、メッセージングで使用する方法を示しています。

`custom_attribute` パーソナライゼーションタグとドット表記を使用して、オブジェクトのプロパティにアクセスします。オブジェクトの名前（オブジェクトの配列を参照する場合は配列内の位置）を指定し、その後にドット（ピリオド）、そしてプロパティ名を続けます。

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

![Liquidを使用して曲名とリスナーがその曲を再生した回数をメッセージにテンプレート化する]({% image_buster /assets/img_archive/nca_liquid_2.png %})

### パーソナライゼーション {#personalization}

**パーソナライゼーションを追加**モーダルを使用して、階層化カスタム属性をメッセージングに挿入することもできます。パーソナライゼーションタイプとして**階層化カスタム属性**を選択します。次に、トップレベルの属性と属性キーを選択します。

例えば、以下のパーソナライゼーションモーダルでは、ユーザーの設定に基づいて、地域のオフィスの階層化カスタム属性を挿入しています。

![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
階層化カスタム属性を挿入するオプションが表示されない場合は、スキーマが生成されているか確認してください。
{% endalert %}

## スキーマの再生成 {#regenerate-schema}

スキーマが生成された後、**1暦日に1回**（会社のタイムゾーンに基づく）再生成できます。このセクションでは、スキーマを再生成する方法について説明します。スキーマの詳細については、[ネストされたオブジェクトエクスプローラーを使用してスキーマを生成する]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes/#generate-schema)を参照してください。

階層化カスタム属性のスキーマを再生成するには：

1. **データ設定** > **カスタム属性**に移動します。
2. 階層化カスタム属性を検索します。
3. 属性の**Attribute Name**列で、<i class="fas fa-plus"></i>を選択してスキーマを管理します。
4. モーダルが表示されます。**Regenerate Schema**を選択します。

**Regenerate Schema**アクションは、会社のタイムゾーンで**1暦日に1回**に制限されています。スキーマジョブがすでに**進行中**の場合（ステータスが**Generating**の間はオプションが利用できません）、別の再生成を開始することはできません。スキーマの再生成では新しいオブジェクトのみが検出され、スキーマに現在存在するオブジェクトは削除されません。

{% alert important %}
既存のオブジェクトを持つオブジェクト配列のスキーマをリセットするには、新しいカスタム属性を作成する必要があります。スキーマの再生成では既存のオブジェクトは削除されません。
{% endalert %}

スキーマを再生成した後にデータが期待どおりに表示されない場合、その属性が十分な頻度で取り込まれていない可能性があります。ユーザーデータは、指定された階層化属性についてBrazeに送信された過去のデータからサンプリングされます。属性が十分に取り込まれていない場合、スキーマに反映されません。

## 階層化カスタム属性の変更をトリガーする {#trigger-nested-custom-attribute-changes}

階層化カスタム属性オブジェクトが変更されたときにトリガーできます。このオプションはオブジェクト配列の変更には使用できません。パスエクスプローラーを表示するオプションが表示されない場合は、スキーマが生成されているか確認してください。

例えば、アクションベースのCampaignでは、**Change Custom Attribute Value**の新しいトリガーアクションを追加して、地域のオフィスの設定を変更したユーザーをターゲットにできます。

![階層化された設定に対するカスタム属性値の変更トリガーを使用したアクションベースのCampaign配信設定]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

## オブジェクト配列でのセグメンテーション動作 {#segmentation-behavior-with-arrays-of-objects}

複数の `Nested Custom Attribute` フィルターをANDロジックで使用してオブジェクト配列をセグメントする場合、各フィルターは配列内のすべてのアイテムに対して独立して評価されます。配列内の*いずれかの*アイテムが各個別フィルターを満たす場合、ユーザーはそのSegmentの対象となります。フィルターが*同じ*アイテムに一致する必要はありません。

例えば、ユーザーが以下の配列を持っているとします。

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

以下のANDフィルターを持つSegment：

- `orders[].price` が50より大きい
- `orders[].price` が30より小さい

このユーザーは対象となります。最初のフィルターは「Shoes」アイテム（80 > 50）に一致し、2番目のフィルターは「Hat」アイテム（25 < 30）に一致するためです。単一のアイテムが両方の条件を満たしていなくても、ユーザーはSegmentに入ります。

配列内の同じアイテムにすべての条件を一致させる必要がある場合は、同じパスで[マルチクライテリアセグメンテーション]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes/#use-multi-criteria-segmentation)を使用するか、クロスアイテムマッチングを避けるようにデータを再構成してください。

## データポイント {#data-points}

送信されるキーごとに1データポイントを消費します。例えば、ユーザープロファイルで初期化されたこのオブジェクトは7データポイントとしてカウントされます。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
カスタム属性オブジェクトを `null` に更新する場合も、1データポイントを消費します。
{% endalert %}