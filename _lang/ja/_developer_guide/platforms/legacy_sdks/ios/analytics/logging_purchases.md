---
nav_title: 購入記録
article_title: iOS向け購入記録
platform: iOS
page_order: 4
description: "このリファレンス記事では、アプリ内購入と売上をトラッキングし、iOSアプリケーションで購入プロパティを割り当てる方法を説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS向けの購入記録 {#log-purchases-for-ios}

アプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Brazeは複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

実装前に、[ベストプラクティス]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#user-data-collection)のカスタムイベント、カスタム属性、および購入イベントによって提供されるセグメンテーションオプションの例と、[イベント命名規則]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)に関する注意事項を必ず確認しておいてください。

## 購入と売上のトラッキング {#tracking-purchases-and-revenue}

この機能を使用するには、アプリ内購入が正常に完了した後でこのメソッド呼び出しを追加します。

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

- サポートされている通貨コードはUSD、CAD、EUR、GBP、JPY、AUD、CHF、NOK、MXN、NZD、CNY、RUB、TRY、INR、IDR、ILS、SAR、ZAR、AED、SEK、HKD、SPD、DKKなどです。
  - これ以外の通貨コードを指定すると警告が記録され、SDKでその他のアクションは実行されません。
- 商品IDは最大255文字です。
- 製品IDが空の場合、購入はBrazeに記録されないことに注意してください。

### プロパティの追加 {#properties-purchases}

購入に関するメタデータを追加するには、[イベントプロパティ配列]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects)を渡すか、`NSNumber`、`NSString`、または`NSDate`の値が挿入された`NSDictionary`を渡します。

詳細については、[iOSクラスのドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc)を参照してください。

### 数量の追加 {#adding-quantity}
顧客が1回のチェックアウト手続きで同じ購入を複数回行う場合は、購入に数量を追加できます。これを行うには、数量として`NSUInteger`を渡します。

* SDKで購入を記録するには、数量入力が [0, 100] の範囲内である必要があります。
* 数量入力のないメソッドは、デフォルトの数量値が1になります。
* 数量入力のあるメソッドにはデフォルト値がないため、SDKで購入を記録するには数量入力を受け取る**必要があります**。

詳細については、[iOSクラスのドキュメント](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa)を参照してください。

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
10米ドルという値と数量3を渡すと、10ドルの購入3件、合計30ドルとしてユーザーのプロフィールに記録されます。
{% endalert %}

### 注文レベルでの購入記録 {#log-purchases-at-the-order-level}
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを`product_id`として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions)を参照してください。

### 予約済みのキー {#reserved-keys}

以下のキーは予約されているため、購入プロパティとして使用できません。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### REST API

REST APIを使用して購入を記録することもできます。詳細については、[ユーザーAPIのドキュメント]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data)を参照してください。