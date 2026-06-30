---
nav_title: ネストされたオブジェクト
article_title: カスタムイベント内の階層化オブジェクト
page_order: 1
page_type: reference
description: "この記事では、カスタムイベントや購入のプロパティとして階層化された JSON データを送信する方法と、メッセージングでそれらの階層化オブジェクトを使用する方法について説明します。"
---

# カスタムイベント内の階層化オブジェクト {#nested-objects-in-custom-events}

> このページでは、カスタムイベントや購入のプロパティとして階層化された JSON データを送信する方法と、メッセージングでそれらの階層化オブジェクトを使用する方法について説明します。

階層化オブジェクト（別のオブジェクトの内部にあるオブジェクト）を使用して、カスタムイベントや購入のプロパティとして階層化された JSON データを送信できます。この階層化データは、メッセージ内のパーソナライズ情報のテンプレート化、メッセージ送信のトリガー、ユーザーのセグメンテーションに使用できます。

## 考慮事項 {#considerations}

- 階層化データは[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)と[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)の両方でサポートされていますが、その他のイベントタイプではサポートされていません。
- 配列またはオブジェクト値を含むイベントプロパティオブジェクトは、最大 100 KB のイベントプロパティペイロードを持つことができます。
- 購入イベントに対してイベントプロパティスキーマを生成することはできません。
- イベントプロパティスキーマは、過去 24 時間のカスタムイベントをサンプリングして生成されます。

### 最小のSDKバージョン {#minimum-sdk-versions}

以下のSDKバージョンが階層化オブジェクトをサポートしています。

{% sdk_min_versions swift:5.0.0 android:20.0.0 web:3.3.0 %}

## ステップ 1: スキーマを生成する {#step-1-generate-a-schema}

カスタムイベント内の階層化データにアクセスするには、階層化イベントプロパティを持つ各イベントのスキーマを生成します。スキーマを生成するには:

1. **データ設定** > **カスタムイベント**に移動します。
2. 階層化プロパティを持つイベントの**プロパティを管理**を選択します。
3. <i class="fas fa-arrows-rotate"></i> ボタンを選択してスキーマを生成します。スキーマを表示するには、<i class="fas fa-plus"></i> プラスボタンを選択します。

![ボタンを選択してスキーマを生成します。スキーマを表示するには、プラスボタンを選択します。]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

今後新しいプロパティが送信された場合、スキーマが再生成されるまでスキーマには含まれません。スキーマは24時間ごとに再生成できます。

## ステップ 2: 階層化オブジェクトを使用する {#step-2-use-the-nested-object}

セグメンテーションやパーソナライゼーションの際に階層化データを参照できます。スキーマは必須ではありません。使用例については以下のセクションを参照してください。

- [APIリクエストボディ](#api-request-body)
- [Liquidテンプレート](#liquid-templating)
- [メッセージトリガー](#message-triggering)
- [セグメンテーション](#segmentation)
- [パーソナライゼーション](#personalization)

### APIリクエストボディ {#api-request-body}

{% tabs %}
{% tab Music Example %}

以下は、「Created Playlist」カスタムイベントを使用した `/users/track` の例です。プレイリストが作成された後、以下を送信してプレイリストのプロパティをキャプチャします。
- 「songs」をプロパティとしてリストするAPIリクエスト
- 曲の階層化プロパティの配列

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

以下は、「Ordered」カスタムイベントを使用した `/users/track` の例です。注文が完了した後、以下を送信してその注文のプロパティをキャプチャします。
- `r_details` をプロパティとしてリストするAPIリクエスト
- その注文の階層化プロパティ

```
...
"properties": {
  "r_details": {
    "name": "SandwichEmperor",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
階層化カスタムイベントプロパティの場合、年が0未満または3000より大きい場合、Brazeはこれらの値をユーザーに保存しません。
{% endalert %}

### Liquidテンプレート {#liquid-templating}

以下は、[前述のAPIリクエスト](#api-request-body)からリクエストされた階層化プロパティを参照するLiquidテンプレートの作成方法を示しています。

{% tabs %}
{% tab Music Example %}
「Created Playlist」イベントによってトリガーされるメッセージでのLiquidテンプレート:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
「Ordered」イベントによってトリガーされるメッセージでのLiquidテンプレート:

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### メッセージトリガー {#message-triggering}

これらのプロパティを使用してCampaignをトリガーするには、カスタムイベントまたは購入を選択し、**階層化プロパティ**フィルターを追加します。メッセージトリガーはアプリ内メッセージではまだサポートされていませんが、メッセージ内のLiquidパーソナライゼーションの階層化プロパティは引き続き表示されます。

{% tabs %}
{% tab Music Example %}

「Created Playlist」イベントの階層化プロパティを使用してCampaignをトリガーする:

![カスタムイベントのプロパティフィルターに階層化プロパティを選択するユーザー。]({% image_buster /assets/img/nested_object2.png %})

トリガー条件 `songs[].album.yearReleased` が「1968」に「一致する」場合、曲のいずれかに1968年にリリースされたアルバムがあるイベントにマッチします。配列を走査するためにブラケット表記 `[]` を使用し、走査された配列内の**いずれかの**アイテムがイベントプロパティに一致する場合にマッチします。

{% alert important %}
**該当しない**フィルターは、配列内のプロパティのいずれも指定された値と一致しない場合にのみマッチします。<br><br>例えば、Canvas Aにアクションベースのカスタムイベント階層化プロパティフィルター**一致する**「smartwatch」があり、Canvas Bにアクションベースのカスタムイベント階層化プロパティフィルター**該当しない**「simphone」があるとします。プロパティに「smartwatch」と「simphone」がある場合、両方のCanvasesがトリガーされます。ただし、いずれかのプロパティに「simphone」または「sim only」がある場合、どちらのCanvasもトリガーされません。
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

「Ordered」イベントの階層化プロパティを使用してCampaignをトリガーする:

![カスタムイベントにプロパティフィルター r_details.name が SandwichEmperor であることを追加するユーザー。]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "SandwichEmperor"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
イベントプロパティに `[]` または `.` 文字が含まれている場合、その部分をダブルクォートで囲んでエスケープしてください。例えば、`"songs[].album".yearReleased` はリテラルプロパティ `"songs[].album"` を持つイベントにマッチします。
{% endalert %}

### セグメンテーション {#segmentation}

階層化イベントプロパティに基づいてユーザーをセグメント化するには、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を使用する必要があります。スキーマを生成すると、セグメンテーションセクションに階層化オブジェクトエクスプローラーが表示されます。

![セグメンテーションに関連するスクリーンショット。]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

セグメンテーションはトリガーと同じ表記法を使用します（[メッセージトリガー](#message-triggering)を参照）。

セグメントエクステンションを編集または作成するには、「Edit Segments」権限が必要です。

### パーソナライゼーション {#personalization}

**パーソナライゼーションを追加**モーダルを使用して、パーソナライゼーションタイプとして**高度なイベントプロパティ**を選択します。これにより、スキーマが生成された後に階層化イベントプロパティを追加するオプションが利用可能になります。

![パーソナライゼーションを追加モーダルを使用して、パーソナライゼーションタイプとして高度なイベントプロパティを選択します。これにより、スキーマが生成された後に階層化イベントプロパティを追加するオプションが利用可能になります。]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## メッセージでの階層化オブジェクトのテスト {#testing-nested-objects-in-messages}

ダッシュボードの**プレビューとテスト**ツールは、階層化オブジェクトや階層化カスタム属性のモックデータの追加をサポートしていません。Liquidを通じて階層化データを参照するメッセージをテストするには、その階層化属性を持つ既存のユーザーとしてメッセージをプレビューするか、テストユーザーにライブCampaignを起動してカスタムイベントプロパティを含むメッセージをプレビューできます。

### 階層化カスタム属性 {#nested-custom-attributes}

1. APIを通じてテストユーザープロファイルに階層化属性をインポートします。
2. CampaignまたはCanvasで、**プレビューとテスト**に移動します。
3. **ユーザーとしてプレビュー**を選択し、テストユーザーを検索します。Liquidはそのユーザーのプロファイル上の実際の階層化属性を使用して解決されます。

### 階層化イベントプロパティ {#nested-event-properties}

階層化イベントプロパティは、ライブイベントトリガーが必要なため、ダッシュボードでプレビューできません。テストするには:

1. テストユーザーのみをターゲットとし、階層化プロパティを持つカスタムイベントによってトリガーされる（または参照する）CampaignまたはCanvasステップを作成します。
2. テストオーディエンスにCampaignを起動します。
3. 階層化オブジェクトペイロードを含むカスタムイベントをテストユーザーのプロファイルに記録します（APIまたはSDKを使用）。
4. メッセージが階層化プロパティ値で正しくレンダリングされることを確認します。

## よくある質問 {#frequently-asked-questions}

### 階層化オブジェクトを使用すると追加のデータポイントが記録されますか？ {#does-using-nested-objects-log-additional-data-points}

この機能の追加によるデータポイントの記録方法に変更はありません。階層化オブジェクトに基づくセグメンテーションはセグメントエクステンションを使用しますが、追加のデータポイントは使用しません。

### どのくらいの階層化データを送信できますか？ {#how-much-nested-data-can-be-sent}

イベントのプロパティの1つ以上に階層化データが含まれている場合、イベント上のすべてのプロパティを合わせた最大ペイロードは100 KBです。そのサイズ制限を超えるリクエストは拒否されます。