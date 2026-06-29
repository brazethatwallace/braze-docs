---
nav_title: "イベントオブジェクト"
article_title: APIイベントオブジェクト
page_order: 6
page_type: reference
description: "このリファレンス記事では、イベントオブジェクトとは何か、イベントベースのCampaign戦略においていかに重要な役割を果たすかについて解説します。"

---

# イベントオブジェクト {#event-object}

> この記事では、イベントオブジェクトのさまざまな構成要素、このオブジェクトの使用方法、および参考となる使用例について説明します。

## イベントオブジェクトとは {#what-is-an-event-object}

イベントオブジェクトは、特定のイベントが発生したときにAPIを通じて渡されるオブジェクトです。イベントオブジェクトはイベント配列に格納されます。イベント配列内の各イベントオブジェクトは、指定された時間値における特定のユーザーによるカスタムイベントの単一の発生を表します。イベントオブジェクトにはさまざまなフィールドがあり、メッセージ、データ収集、パーソナライゼーションにおいてイベントプロパティを設定・使用することでカスタマイズできます。

特定のプラットフォームにカスタムイベントを設定する手順については、[開発者ガイド]({{site.baseurl}}/developer_guide/home)のプラットフォーム統合ガイドを参照してください。ご使用のプラットフォームに基づいて、関連する記事を参照してください。

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

- [外部ユーザーID]({{site.baseurl}}/api/basics#user-ids)
- [アプリ識別子]({{site.baseurl}}/api/identifier_types)
- [ISO 8601タイムコード](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
一部の識別子ペアは、単一のリクエスト内で同時に使用できません。`email`と`phone`の両方が指定された場合、`email`が`phone`より優先されます。詳細については、[識別子の解決]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)を参照してください。
{% endalert %}

#### 既存のプロファイルのみを更新する {#update-existing-profiles-only}

Brazeで既存のユーザープロファイルのみを更新するには、リクエストの本文内で`_update_existing_only`キーに`true`の値を渡す必要があります。この値を省略すると、`external_id`がまだ存在しない場合、Brazeは新しいユーザープロファイルを作成します。

{% alert note %}
`/users/track`エンドポイントを使用してエイリアスのみのユーザープロファイルを作成する場合は、`_update_existing_only`を`false`に設定する必要があります。この値が省略された場合、エイリアスのみのプロファイルは作成されません。
{% endalert %}

## イベントプロパティオブジェクト {#event-properties-object}

カスタムイベントと購入にはイベントプロパティを含めることができます。「プロパティ」値は、キーがプロパティ名で値がプロパティ値であるオブジェクトである必要があります。プロパティ名は、255文字以下の空でない文字列でなければならず、先頭にドル記号（$）を付けることはできません。

プロパティ値は、次のデータタイプのいずれでもかまいません。

| データタイプ | 説明 |
| --- | --- |
| 数値 | [整数](https://en.wikipedia.org/wiki/Integer)または[浮動小数点数](https://en.wikipedia.org/wiki/Floating-point_arithmetic)として |
| ブール値 | `true`または`false` |
| 日時 | 文字列として[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式または以下のいずれかの形式でフォーマットする必要があります。<br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>配列内ではサポートされていません。<br><br>「T」は時間指定子であり、プレースホルダーではないことに注意してください。変更または削除しないでください。<br><br>タイムゾーンのない時間属性はデフォルトでUTCの真夜中になります（ダッシュボード上では会社のタイムゾーンにおけるUTCの真夜中に相当する形式で表示されます）。<br><br> タイムスタンプが未来のイベントはデフォルトで現在の時刻になります。  |
| 文字列 | 255文字以下。 |
| 配列 | 配列に日時を含めることはできません。 |
| オブジェクト | オブジェクトは文字列として取り込まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="イベントプロパティオブジェクト" }

配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大100&nbsp;KBのイベントプロパティペイロードを設定できます。

### 予約済みのキー {#reserved-keys}

以下のキーは予約されているため、カスタムイベントプロパティとして使用できません。

- `time`
- `event_name`

{% alert important %}
予約済みキーをカスタムイベントのプロパティ名として使用すると、`/users/track`エンドポイントへのリクエスト送信時にAPIエラーが発生します。
{% endalert %}

### イベントプロパティの永続性 {#event-property-persistence}

イベントプロパティは、親イベントによってトリガーされるメッセージのフィルタリングおよびLiquidパーソナライゼーションのために設計されています。デフォルトでは、Brazeユーザープロファイルでは永続化されません。セグメンテーションでイベントプロパティ値を使用するには、イベントプロパティ値を長期的に保存するためのさまざまなアプローチについて詳述している[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を参照してください。

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
- [ISO 8601タイムコード Wiki](http://en.wikipedia.org/wiki/ISO_8601)

## イベントオブジェクト {#event-objects}

上記の例を使うと、誰かが最近予告編を見て、映画をレンタルしたことがわかります。Campaignに入ってこれらのプロパティに基づいてユーザーをセグメントすることはできませんが、Liquidを使用してチャネル経由でカスタムメッセージを送信するための受領書の形でこれらのプロパティを戦略的に活用できます。例えば、「こんにちは、**Alex**さん。**Alex Smith**監督の**The Sad Egg**をレンタルしていただきありがとうございます。お客様のレンタル履歴に基づいて、おすすめの映画をご紹介します...」のように使用できます。