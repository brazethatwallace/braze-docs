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

## 階層化属性について {#about-nested-attributes}

階層化属性を使用すると、単一のカスタム属性オブジェクトのデータを活用して、より高度なセグメントを構築し、メッセージをパーソナライズできます。

次の例では、カスタム属性`favorite_book`に、階層化属性`title`、`author`、`publishing_date`が含まれています。このオブジェクトを使用して、著者別にユーザーをターゲットにしたり、出版日でフィルターしたり、書籍のタイトルをメッセージに直接挿入したりできます。

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```


{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 注意事項 {#considerations}

- 階層化カスタム属性は、Braze SDKまたはAPIを通じて送信されるカスタム属性を対象としています。
- オブジェクトの最大サイズは100&nbsp;KBです。更新によりオブジェクトが100&nbsp;KBを超える場合、Brazeはその更新を破棄し、属性は変更されません。
- キー名と文字列値のサイズ上限は255文字です。
- キー名にスペースを含めることはできません。
- ユーザープロファイルに階層化カスタム属性を送信する場合、APIペイロードではピリオド（`.`）とドル記号（`$`）はサポートされていません。
- すべてのBrazeパートナーが階層化カスタム属性をサポートしているわけではありません。特定のパートナー連携がこの機能をサポートしているかどうかは、[パートナードキュメント]({{site.baseurl}}/partners/home)を参照してください。
- 階層化カスタム属性は、Connected Audience API呼び出し時のフィルターとして使用できません。
- デフォルトでは、**階層化カスタム属性**セグメントフィルターには、オブジェクト型カスタム属性、オブジェクト配列属性、および配列型カスタム属性が含まれます。属性を選択すると、プロパティスキーマセレクターにネストされた配列フィールドの配列パス（`[]`表記を使用）が表示されます。トップレベルの配列カスタム属性をそのフィルターから非表示にするには、[Brazeサポート]({{site.baseurl}}/braze_support)にお問い合わせください。
- ダッシュボードで**カスタムユーザーとしてプレビュー**を使用してメッセージをプレビューする場合、モックデータは文字列または文字列の配列としてのみ入力できます。ネストされたオブジェクトはサポートされていません。階層化カスタム属性を参照するメッセージをプレビューするには、プロファイルに階層化属性がすでに設定されている既存のユーザーを選択してください。ネストされたカスタムイベントプロパティについては、レンダリングを確認するために、テストユーザーをターゲットにしたライブキャンペーンを開始する必要があります。

## APIの例 {#api-example}

{% tabs local %}
{% tab 作成 %}
以下は、「Most Played Song」オブジェクトを使用した`/users/track`の例です。曲のプロパティをキャプチャするために、`most_played_song`をオブジェクトとしてリストし、オブジェクトプロパティのセットとともにAPIリクエストを送信します。

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
既存のオブジェクトを更新するには、リクエストに`_merge_objects`パラメーターを含めて`users/track`にPOSTを送信します。これにより、更新内容が既存のオブジェクトデータとディープマージされます。ディープマージにより、最初のレベルだけでなく、オブジェクトのすべてのレベルが別のオブジェクトにマージされます。この例では、Brazeにすでに`most_played_song`オブジェクトがあり、`most_played_song`オブジェクトに新しいフィールド`year_released`を追加します。

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
`_merge_objects`を`true`に設定する必要があります。設定しない場合、オブジェクトは上書きされます。`_merge_objects`はデフォルトで`false`です。
{% endalert %}

{% endtab %}
{% tab 削除 %}
カスタム属性オブジェクトを削除するには、カスタム属性オブジェクトを`null`に設定して`users/track`にPOSTを送信します。

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
このアプローチは、[オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)内のネストされたキーを削除するためには使用できません。
{% endalert %}

{% endtab %}
{% endtabs %}

## SDKの例 {#sdk-example}

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 unity:5.1.0 %}

以下のサンプルでは、各SDKで同じ階層化カスタム属性オブジェクト（`most_played_song`）を作成、マージ更新、削除する方法を示しています。

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
{% tab Unity SDK %}

**作成**
```csharp
Dictionary<string, object> attributes = new Dictionary<string, object>();
attributes.Add("song_name", "Solea");
attributes.Add("artist_name", "Miles Davis");
attributes.Add("album_name", "Sketches of Spain");
attributes.Add("genre", "Jazz");

Dictionary<string, object> playAnalytics = new Dictionary<string, object>();
playAnalytics.Add("count", 1000);
playAnalytics.Add("top_10_listeners", true);
attributes.Add("play_analytics", playAnalytics);

AppboyBinding.SetCustomUserAttribute("most_played_song", attributes);
```

**更新**
```csharp
Dictionary<string, object> attributes = new Dictionary<string, object>();
attributes.Add("year_released", 1960);

AppboyBinding.SetCustomUserAttribute("most_played_song", attributes, true);
```

**削除**
```csharp
AppboyBinding.UnsetCustomUserAttribute("most_played_song");
```

{% endtab %}
{% endtabs %}

## オブジェクトプロパティとしての日付のキャプチャ {#capturing-dates-as-object-properties}

日付をオブジェクトプロパティとしてキャプチャするには、`$time` キーを使用する必要があります。次の例では、「Important Dates」オブジェクトを使用して、`birthday` と `wedding_anniversary` というオブジェクトプロパティのセットをキャプチャしています。これらの日付の値は `$time` キーを持つオブジェクトであり、null 値にすることはできません。

{% alert note %}
最初に日付をオブジェクトプロパティとしてキャプチャしていなかった場合は、すべてのユーザーに対して `$time` キーを使用してこのデータを再送信することをお勧めします。そうしないと、`$time` 属性を使用する際にセグメントが不完全になる可能性があります。ただし、階層化カスタム属性の `$time` の値が正しくフォーマットされていない場合、階層化カスタム属性全体が更新されません。
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

## Liquid テンプレート {#liquid-templating}

以下の Liquid テンプレートの例では、前述の API リクエストから保存されたカスタム属性オブジェクトのプロパティを参照し、メッセージングで使用する方法を示しています。

`custom_attribute` パーソナライゼーションタグとドット表記を使用して、オブジェクトのプロパティにアクセスします。オブジェクト名（オブジェクトの配列を参照する場合は配列内の位置）を指定し、その後にドット（ピリオド）、続いてプロパティ名を記述します。

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

メッセージで階層化カスタム属性の Liquid を使用するには:

1. キャンペーンまたはキャンバスに移動し、パーソナライゼーションを追加したいメッセージステップを開きます。
2. メッセージ作成画面で、値を表示したい場所に Liquid スニペットを挿入します。
3. **プレビュー＆テスト**を使用して、プロファイルに階層化カスタム属性がすでに設定されている既存のユーザーで、値が期待どおりにレンダリングされることを確認します。

### パーソナライゼーション {#personalization}

**パーソナライゼーションを追加**を使用して、階層化カスタム属性をメッセージに挿入できます。

**パーソナライゼーションを追加**を開くには:

1. キャンペーンまたはキャンバスに移動し、パーソナライゼーションを追加したいメッセージステップを開きます。
2. メッセージ作成画面で、**パーソナライゼーション**を選択して**パーソナライゼーションを追加**サイドバーを開き、パーソナライゼーションオプションを選択します。

階層化カスタム属性のパーソナライゼーションを設定するには:

1. **パーソナライゼーションタイプ**で、**階層化カスタム属性**を選択します。
2. **トップレベル属性**で、挿入したい階層化カスタム属性のパスを選択します。
   例えば、`preferences.neighborhood_office` を選択します。
3. オプション: **デフォルト値**に、その属性に独自の値が設定されていないユーザー向けのフォールバック値を入力します。
4. 生成された **Liquid スニペット**を確認し、期待するパスと一致していることを確認します。
5. **挿入**を選択します。

この例では、Brazeはメッセージに `preferences.neighborhood_office` の階層化された値を挿入します。デフォルト値は、属性に独自の値が設定されていないユーザー向けにメッセージに含まれるフォールバックです。

{% alert tip %}
階層化カスタム属性を挿入するオプションが表示されない場合は、スキーマが生成されているかどうかを確認してください。
{% endalert %}

## スキーマの生成と再生成 {#regenerate-schema}

セグメンテーションやパーソナライゼーションで階層化カスタム属性を使用するには、その属性のスキーマを生成する必要があります。スキーマが生成された後、必要に応じて再生成できます。スキーマの詳細については、[ネストされたオブジェクトエクスプローラーを使用してスキーマを生成する]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema)を参照してください。

### スキーマを生成する {#generate-a-schema}

階層化カスタム属性を作成してBrazeにデータを送信した後、スキーマを生成できます。

1. **データ設定** > **カスタム属性**に移動します。
2. 階層化カスタム属性を検索します。
3. 属性の**属性名**列で、<i class="fas fa-arrows-rotate"></i> **スキーマを生成**を選択します。

スキーマが生成されると、<i class="fas fa-arrows-rotate"></i> アイコンが <i class="fas fa-plus"></i> プラスアイコンに変わり、それを選択してスキーマを表示・管理できます。

### スキーマを再生成する {#regenerate-a-schema}

階層化カスタム属性のスキーマを再生成するには：

1. **データ設定** > **カスタム属性**に移動します。
2. 階層化カスタム属性を検索します。
3. 属性の**属性名**列で、<i class="fas fa-plus"></i> **スキーマを管理**を選択してスキーマを管理します。
4. モーダルが表示されます。**スキーマを再生成**を選択します。

スキーマジョブがすでに**進行中**の場合（ステータスが**生成中**の間はオプションが利用できません）、別の再生成を開始することはできません。1つの会社につき、一度に実行できるスキーマ生成ジョブは1つだけです。スキーマの再生成では新しいオブジェクトのみが検出され、スキーマに現在存在するオブジェクトは削除されません。

{% alert important %}
既存のオブジェクトを持つオブジェクト配列のスキーマをリセットするには、新しいカスタム属性を作成する必要があります。スキーマの再生成では既存のオブジェクトは削除されません。
{% endalert %}

スキーマを再生成した後にデータが期待どおりに表示されない場合、その属性が十分な頻度で取り込まれていない可能性があります。ユーザーデータは、指定された階層化属性についてBrazeに送信された過去のデータからサンプリングされます。属性が十分に取り込まれていない場合、スキーマに反映されません。

## 階層化カスタム属性の変更をトリガーする {#trigger-nested-custom-attribute-changes}

階層化カスタム属性オブジェクトが変更されたときにトリガーできます。このオプションは、オブジェクト配列の変更には使用できません。パスエクスプローラーを表示するオプションが見つからない場合は、スキーマが生成されているか確認してください。

たとえば、アクションベースのキャンペーンでは、**カスタム属性値の変更**の新しいトリガーアクションを追加して、近隣オフィスの設定を変更したユーザーをターゲットにできます。

アクションベースのキャンペーンでこのトリガーを設定するには:

1. キャンペーンを作成または編集し、配信タイプを**アクションベース配信**に設定します。
2. トリガー設定で、**カスタム属性値の変更**を選択します。
3. 監視したい階層化カスタム属性のパスを選択します。
   たとえば、`preferences.neighborhood_office` を選択します。
4. **任意の新しい値**など、目的のトリガー条件を選択します。
5. キャンペーンのメッセージとオーディエンスの設定を完了し、キャンペーンを開始します。

## トラブルシューティング {#troubleshooting}

### 階層化カスタム属性の値が一貫して適用されない {#nested-custom-attribute-values-not-applied-consistently}

階層化カスタム属性の値がユーザープロファイルに一貫して追加されていないことに気づいた場合、多くの場合、データ型の不一致が原因です。

この問題を診断して解決するには、以下の手順に従ってください。

1. **ユーザーの例を比較する:** 階層化カスタム属性が設定されているはずのユーザーについて、成功した例と失敗した例をそれぞれ1つずつ取得します。
2. **データ構造を確認する:** 両方のプロファイルのカスタム属性値を表示して比較します。
   - プロパティはオブジェクトの下に格納されていますか？
   - プロパティはプロパティの配列として格納されていますか？
3. **セグメンテーションフィルターを確認する:** 格納されているデータ構造と、セグメンテーションフィルターで階層化カスタム属性がどのように参照されているかを比較します。
4. **データ型を確認する:** カスタム属性のデータ型を特定するには、以下の手順に従います。
   - **データ設定** > **カスタム属性**に移動します。
   - 確認したい階層化属性を含むトップレベルのカスタム属性を検索します。
   - 行に**スキーマを生成**と表示されている場合は、それを選択してまずスキーマを生成します。
   - スキーマが生成されたら、その属性の**属性名**列にあるプラスアイコンを選択します。
   - **スキーマを編集**モーダルで、階層化属性と**データ型**列の対応する値を確認します。

データ型がユーザープロファイル間で意図した形式と一致しない場合は、影響を受けるユーザープロファイルから不正な形式の値を削除し、適切なAPIリクエストまたはSDKメソッドを使用して正しい形式で属性を再送信してください。

## オブジェクト配列でのセグメンテーション動作 {#segmentation-behavior-with-arrays-of-objects}

複数の`Nested Custom Attribute`フィルターをANDロジックで使用してオブジェクト配列に対するセグメンテーションを行う場合、各フィルターは配列内のすべてのアイテムに対して独立に評価されます。配列内の*いずれかの*アイテムが個々のフィルター条件を満たしていれば、そのユーザーはセグメントの対象となります。フィルターが*同じ*アイテムに一致する必要はありません。

たとえば、あるユーザーが以下の配列を持っているとします。

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

以下のANDフィルターを持つセグメント：

- `orders[].price`が50より大きい
- `orders[].price`が30より小さい

このユーザーは、最初のフィルターが「Shoes」アイテム（80 > 50）に一致し、2番目のフィルターが「Hat」アイテム（25 < 30）に一致するため、条件を満たします。単一のアイテムが両方の条件を満たしていなくても、このユーザーはセグメントに入ります。

すべての条件を配列内の同じアイテムに一致させる必要がある場合は、同じパスで[マルチ条件セグメンテーション]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#use-multi-criteria-segmentation)を使用するか、アイテム間のクロスマッチングを避けるようにデータを再構成してください。

## データポイント {#data-points}

送信されるキーはすべてデータポイントを消費します。たとえば、ユーザープロファイルで初期化された以下のオブジェクトは、7つのデータポイントとしてカウントされます。

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
カスタム属性オブジェクトを `null` に更新した場合も、データポイントを消費します。
{% endalert %}