---
nav_title: 購入記録
article_title: iOS向け購入記録
platform: iOS
page_order: 4
description: "このリファレンス記事では、iOSアプリケーションでアプリ内購入と売上をトラッキングし、購入プロパティを割り当てる方法について説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS向けの購入記録 {#log-purchases-for-ios}

アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Brazeは複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

実装前に、[ベストプラクティス]({{site.baseurl}}/developer_guide/analytics)のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)に関する注意事項を必ず確認しておいてください。

## 購入と売上のトラッキング {#tracking-purchases-and-revenue}

この機能を使用するには、アプリ内で購入が正常に完了した後にこのメソッド呼び出しを追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- サポートされている通貨記号は、USD、CAD、EUR、GBP、JPY、AUD、CHF、NOK、MXN、NZD、CNY、RUB、TRY、INR、IDR、ILS、SAR、ZAR、AED、SEK、HKD、SPD、DKK などです。
  - その他の通貨記号が提供された場合、警告がログに記録され、SDKではそれ以上のアクションは実行されません。
- 商品IDは最大255文字です。
- 商品識別子が空の場合、購入はBrazeに記録されません。

### プロパティの追加 {#properties-purchases}

購入に関するメタデータを追加するには、[イベントプロパティ配列]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#nested-objects)を渡すか、`NSNumber`、`NSString`、または`NSDate`の値が入った`NSDictionary`を渡します。

詳細については、[iOSクラスドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc)を参照してください。

### 数量の追加 {#adding-quantity}
顧客が1回の会計で同じ商品を複数回購入した場合、購入に数量を追加できます。これは`NSUInteger`を数量として渡すことで実現できます。

* SDKが購入を記録するには、数量の入力値は[0, 100]の範囲内である必要があります。
* 数量の入力がないメソッドは、デフォルトの数量値が1になります。
* 数量の入力があるメソッドにはデフォルト値がなく、SDKが購入を記録するために数量の入力を**必ず**受け取る必要があります。

詳細については、[iOSクラスドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa)を参照してください。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
```

{% endtab %}
{% endtabs %}

{% alert tip %}
10 USDの値と数量3を渡すと、ユーザーのプロファイルには10ドルの購入が3件、合計30ドルとして記録されます。
{% endalert %}

### 注文レベルでの購入記録 {#log-purchases-at-the-order-level}
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを`product_id`として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions)を参照してください。

### 予約キー {#reserved-keys}

以下のキーは予約されており、購入プロパティとして使用できません。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

REST APIを使用して購入を記録することもできます。詳細については、[ユーザーAPIドキュメント]({{site.baseurl}}/api/endpoints/user_data)を参照してください。