---
nav_title: カスタムイベントをログに記録する
article_title: カスタムイベントをログに記録する
page_order: 3.1
description: "Braze SDKを通じてカスタムイベントを記録する方法を説明します。"
---

# カスタムイベントをログに記録する {#log-custom-events}

> Braze SDKを通じてカスタムイベントを記録する方法を説明します。

{% alert note %}
リストされていないラッパーSDKの場合は、代わりに関連するネイティブAndroidまたはSwiftメソッドを使用してください。
{% endalert %}

eコマースの推奨イベントについては、[eコマースイベントを記録する]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。

## カスタムイベントのログ記録 {#logging-a-custom-event}

カスタムイベントをログに記録するには、以下のイベントログ記録メソッドを使用します。

{% tabs %}
{% tab web %}
標準的なWeb SDKの実装では、以下のメソッドを使用できます。

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

代わりにGoogle Tag Managerを使用する場合は、**カスタムイベント**タグタイプを使用して[`logCustomEvent`メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を呼び出し、カスタムイベントをBrazeに送信できます。オプションでカスタムイベントプロパティを含めることも可能です。手順は以下のとおりです。

1. 変数を使用するか、イベント名を直接入力して**イベント名**を入力します。
2. **行を追加**ボタンを使用してイベントプロパティを追加します。

![Brazeアクションタグの設定を示すダイアログボックス。設定には「タグタイプ」（カスタムイベント）、「イベント名」（ボタンクリック）、「イベントプロパティ」が含まれています。]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab android %}
ネイティブAndroidの場合、以下のメソッドを使用できます。

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab cordova %}
Braze Cordovaプラグインのメソッドを使用します。

```javascript
BrazePlugin.logCustomEvent("YOUR_EVENT_NAME");
```

`logCustomEvent` APIは以下を受け付けます。
- `eventName`（必須の文字列）：最大255文字まで使用できます。名前を`$`で始めないでください。英数字と句読点を使用してください。
- `eventProperties`（オプションのオブジェクト）：イベントメタデータのキーと値のペアを追加します。キーは最大255文字で、`$`で始めないでください。

プロパティの値には、`string`（最大255文字）、`numeric`、`boolean`、配列、またはネストされたJSONオブジェクトを使用します。

実装の詳細については、Braze Cordova SDKのソースを参照してください。
- [`www/BrazePlugin.js`の`logCustomEvent`メソッド（138〜140行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L138-L140)
- [`www/BrazePlugin.js`のJSDoc（128〜140行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [`src/android/BrazePlugin.kt`のAndroidハンドラー（108〜115行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [`src/ios/BrazePlugin.m`のiOSハンドラー（308〜313行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
- [`src/ios/BrazePlugin.h`のiOSメソッド宣言（24行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.h#L24)
{% endtab %}

{% tab infillion %}
[Infillion Beacons](https://infillion.com/software/beacons/)をAndroidアプリに統合している場合、オプションで`visit.getPlace()`を使用して位置情報固有のイベントをログに記録できます。`requestImmediateDataFlush`は、アプリがバックグラウンドにある場合でもイベントが確実にログに記録されることを保証します。

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## メタデータプロパティの追加 {#adding-metadata-properties}

カスタムイベントを記録する際に、イベントと一緒にプロパティオブジェクトを渡すことで、そのカスタムイベントに関するメタデータを追加できます。プロパティはキーと値のペアとして定義されます。キーは文字列で、値は`string`、`numeric`、`boolean`、[`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp)オブジェクト、配列、またはネストされたJSONオブジェクトを指定できます。

メタデータプロパティを追加するには、以下のイベント記録メソッドを使用します。

{% tabs %}
{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can",
  pass: false,
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab cordova %}
プロパティオブジェクトを使用してカスタムイベントを記録します:

```javascript
var properties = {};
properties["key1"] = "value1";
properties["key2"] = ["value2", "value3"];
properties["key3"] = false;
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", properties);
```

プロパティをインラインで渡すこともできます:

```javascript
BrazePlugin.logCustomEvent("YOUR-EVENT-NAME", {
  "key": "value",
  "amount": 42,
});
```

公式のCordovaサンプルアプリには、文字列、数値、ブール値、配列、ネストされたオブジェクトのプロパティが含まれています:
- [`sample-project/www/js/index.js`（230〜251行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/sample-project/www/js/index.js#L230-L251)

サンプルプロジェクトの抜粋:

```javascript
var properties = {};
properties["One"] = "That's the Way of the World";
properties["Two"] = "After the Love Has Gone";
properties["Three"] = "Can't Hide Love";
BrazePlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
BrazePlugin.logCustomEvent("cordovaCustomEventWithoutProperties");
BrazePlugin.logCustomEvent("cordovaCustomEventWithFloatProperties", {
  "Cart Value": 4.95,
  "Cart Item Name": "Spicy Chicken Bites 5 pack"
});
BrazePlugin.logCustomEvent("cordovaCustomEventWithNestedProperties", {
  "array key": [1, "2", false],
  "object key": {
    "k1": "1",
    "k2": 2,
    "k3": false,
  },
  "deep key": {
    "key": [1, "2", true]
  }
});
```

APIおよびネイティブブリッジの詳細については、以下を参照してください:
- [`www/BrazePlugin.js` JSDoc（128〜140行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/www/BrazePlugin.js#L128-L140)
- [`src/android/BrazePlugin.kt`のAndroidハンドラー（108〜115行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/android/BrazePlugin.kt#L108-L115)
- [`src/ios/BrazePlugin.m`のiOSハンドラー（308〜313行目）](https://github.com/braze-inc/braze-cordova-sdk/blob/86132bc7f0b6ddf1b598b0e612db70f11744801c/src/ios/BrazePlugin.m#L308-L313)
{% endtab %}

{% tab react native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
`time`キーと`event_name`キーは予約されており、カスタムイベントプロパティとして使用できません。
{% endalert %}

## ベストプラクティス {#best-practices}

カスタムイベントプロパティが期待どおりに記録されるように、3つの重要な確認を行う必要があります。

* [記録されるイベントの確認](#verify-events)
* [ログの確認](#verify-log)
* [値の確認](#verify-values)

カスタムイベントが記録されるたびに、複数のプロパティが記録される場合があります。

### イベントの確認 {#verify-events}

どのイベントプロパティがトラッキングされているかを開発者に確認してください。すべてのイベントプロパティは大文字と小文字が区別される点にご注意ください。カスタムイベントのトラッキングに関する追加情報については、プラットフォームに応じて以下の記事をご確認ください。

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### ログの確認 {#verify-log}

イベントプロパティが正常にトラッキングされていることを確認するには、**カスタムイベント**ページからすべてのイベントプロパティを表示できます。

1. **データ設定** > **カスタムイベント**に移動します。
2. リストからカスタムイベントを見つけます。
3. 対象のイベントで**プロパティを管理**を選択し、イベントに関連付けられたプロパティの名前を表示します。

### 値の確認 {#verify-values}

[テストユーザーとして自分のユーザーを追加]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)した後、以下の手順で値を確認します。

1. アプリ内でカスタムイベントを実行します。
2. データがフラッシュされるまで約10秒間待ちます。
3. [イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)を更新して、カスタムイベントおよびそれとともに渡されたイベントプロパティの値を確認します。

## カスタムイベントのトラブルシューティング {#troubleshooting-custom-events}

以下のシナリオを使用して、SDK全体でのカスタムイベントのログ記録に関するトラブルシューティングを行います。

### カスタムイベントトリガーの確認 {#verifying-the-custom-event-trigger}

カスタムイベントが表示されない場合、アプリでトラッキングされているアクションが、テストしているアクションと一致していない可能性があります。

- 開発者チームに、どのアプリアクションがカスタムイベントをトリガーするかを確認してください。
- SDKアップグレード後に、`braze` ではなく `appboy` への参照など、非推奨のコードパスがないか確認してください。

### カスタムイベントが匿名プロファイルに記録される {#custom-events-are-logged-to-an-anonymous-profile}

カスタムイベントを記録する前にユーザーを識別しないと、Brazeはそのイベントを匿名プロファイルに関連付ける可能性があります。

- カスタムイベントを実行する前に `changeUser()` を呼び出して、Brazeが識別済みのユーザープロファイルにイベントを記録するようにしてください。
- 識別済みのテストユーザーでテストし、[イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)を確認してください。

### カスタムイベントのログ記録設定の確認 {#verifying-custom-event-logging-setup}

カスタムイベントが期待どおりに表示されない場合は、開発者チームが適切なアプリアクションに対してカスタムイベントのログ記録を実装していることを確認してください。

- 開発者チームに、イベントが正しく記録され、期待されるユーザーアクションからトリガーされていることを確認するよう依頼してください。
- チームがBrazeサポートにチケットを作成する際は、[詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)と関連するコードスニペットを含めてください。
- アプリがSwiftまたはAndroidを使用している場合、開発者チームは [SDKデバッガーの前提条件]({{site.baseurl}}/developer_guide/sdk_integration/debugging#prerequisites)を使用して、詳細ログの生成に役立てることができます。
- 開発者チームが問題を特定できない場合は、[Brazeサポートチケット]({{site.baseurl}}/user_guide/administer/personal/braze_support)を作成してください。