---
nav_title: "イベントオブジェクト"
article_title: "イベントオブジェクト"
page_order: 6
page_type: reference
description: "このリファレンス記事では、イベントオブジェクトとは何か、イベントベースのキャンペーン戦略においていかに重要な役割を果たすかについて解説します。"
---

# イベントオブジェクト {#event-object}

> この記事では、イベントオブジェクトのさまざまな構成要素、このオブジェクトの使用方法、および参考となる使用例について説明します。

## イベントオブジェクトとは？ {#what-is-an-event-object}

イベントオブジェクトは、特定のイベントが発生した際にAPIを通じて渡されるオブジェクトです。イベントオブジェクトはイベント配列に格納されます。イベント配列内の各イベントオブジェクトは、指定された時間値における特定のユーザーによるカスタムイベントの単一の発生を表します。イベントオブジェクトにはさまざまなフィールドがあり、イベントプロパティを設定して使用することで、メッセージ、データ収集、パーソナライゼーションをカスタマイズできます。

特定のプラットフォームにカスタムイベントを設定する手順については、[開発者ガイド]({{site.baseurl}}/developer_guide/home)のプラットフォーム統合ガイドを参照してください。お使いのプラットフォームに基づいて関連する記事を参照してください。

- [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### オブジェクト本体 {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

{% alert note %}
将来のタイムスタンプを持つイベントは、デフォルトで現在の時刻に設定されます。これにより、カスタムイベントが正確なタイミングで記録されます。
{% endalert %}

- [外部ユーザー ID]({{site.baseurl}}/api/basics#user-ids)
- [アプリ識別子]({{site.baseurl}}/api/identifier_types)
- [ISO 8601 タイムコード](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
一部の識別子の組み合わせは、単一のリクエストで同時に使用できません。`email` と `phone` の両方が提供された場合、`email` が `phone` よりも優先されます。詳細については、[識別子の解決]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)を参照してください。
{% endalert %}

#### 既存のプロファイルのみを更新する {#update-existing-profiles-only}

Brazeで既存のユーザープロファイルのみを更新するには、リクエストの本体に `_update_existing_only` キーを `true` の値で渡す必要があります。この値が省略された場合、`external_id` がまだ存在しなければ、Brazeは新しいユーザープロファイルを作成します。

{% alert note %}
`/users/track` エンドポイントを通じてエイリアスのみのユーザープロファイルを作成する場合、`_update_existing_only` は `false` に設定する必要があります。この値が省略された場合、エイリアスのみのプロファイルは作成されません。
{% endalert %}

## イベントプロパティオブジェクト {#event-properties-object}

カスタムイベントと購入にはイベントプロパティを設定できます。「properties」の値は、キーがプロパティ名、値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、先頭にドル記号（$）を含まない、255文字以下の空でない文字列でなければなりません。

プロパティ値には、以下のデータ型を使用できます。

| データ型 | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)のいずれか |
| ブール値 | `true` または `false` |
| 日時 | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 形式の文字列、または以下のいずれかの形式でフォーマットされている必要があります。 <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>配列内ではサポートされていません。 <br><br>「T」は時刻指定子であり、プレースホルダーではないため、変更や削除をしないでください。 <br><br> タイムゾーンのない時刻属性は、デフォルトで UTC の午前0時になります（ダッシュボードでは、会社のタイムゾーンにおける UTC 午前0時に相当する時刻としてフォーマットされます）。 <br><br> 未来のタイムスタンプを持つイベントは、デフォルトで現在の時刻になります。 |
| 文字列 | 255文字以下。 |
| 配列 | 配列に日時を含めることはできません。 |
| オブジェクト | オブジェクトは文字列として取り込まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="イベントプロパティオブジェクト" }

配列やオブジェクトの値を含むイベントプロパティオブジェクトには、最大100&nbsp;KBのイベントプロパティペイロードを設定できます。

### 予約キー {#reserved-keys}

以下のキーは予約されており、カスタムイベントプロパティとして使用できません。

- `time`
- `event_name`

{% alert important %}
予約キーをカスタムイベントプロパティ名として使用すると、`/users/track` エンドポイントへのリクエスト送信時にAPIエラーが発生します。
{% endalert %}

### イベントプロパティの永続化 {#event-property-persistence}

イベントプロパティは、親イベントによってトリガーされるメッセージのフィルタリングやLiquidパーソナライゼーションのために設計されています。デフォルトでは、Brazeユーザープロファイルには保持されません。セグメンテーションでイベントプロパティ値を使用するには、イベントプロパティ値を長期的に保存するためのさまざまなアプローチについて説明している[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を参照してください。

#### イベントリクエストの例 {#event-example-request}

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 タイムコード Wiki](http://en.wikipedia.org/wiki/ISO_8601)

## イベントオブジェクト {#event-objects}

提供された例を使用すると、ある人が最近トレーラーを視聴し、その後映画をレンタルしたことがわかります。キャンペーンに移動してこれらのプロパティに基づいてユーザーをセグメント化することはできませんが、これらのプロパティをレシートの形式で戦略的に使用し、Liquidを使用してチャネル経由でカスタムメッセージを送信できます。例:「こんにちは、**Alex**さん。**Alex Smith** 制作の**The Sad Egg**をレンタルいただきありがとうございます。レンタルに基づいたおすすめの映画をご紹介します…」