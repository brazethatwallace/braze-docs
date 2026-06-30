---
nav_title: イベント
article_title: イベント
page_order: 0
hidden: true
page_type: reference
description: "この記事では、Brazeのさまざまなイベント（標準イベント、購入イベント、カスタムイベント）とその目的について説明します。"
---

# イベント {#events}

> このページでは、Brazeのさまざまなイベントとその目的について説明します。

Brazeでは、ユーザーの行動やブランドとのエンゲージメントを包括的に理解するために、いくつかの異なるイベントタイプを使用しています。各イベントタイプにはそれぞれ固有の目的があります。

- [標準イベント](#standard-events): アプリやサイトに対するユーザーエンゲージメントの基本的な理解を提供します。
- [購入イベント](#purchase-events): ユーザーの購買行動を理解し、収益をトラッキングするために不可欠です。
- [カスタムイベント](#custom-events): アプリやビジネスに固有のユーザー行動について、より深いインサイトを提供します。

これらの異なるタイプのイベントをトラッキングすることで、ユーザーについてより深く理解でき、マーケティング戦略の策定、アプリの最適化、よりパーソナライズされたユーザー体験の提供に役立てることができます。それでは詳しく見ていきましょう！

## 標準イベント {#standard-events}

Brazeの標準イベントは、Brazeがプラットフォーム全体で認識する定義済みのアクションです。[カスタムイベント](#custom-events)とは異なり、標準イベントを作成したり名前を付けたりする必要はありません。組み込みで提供されています。ただし、すべての標準イベントが同じ方法でトラッキングされるわけではありません。

以下のイベントは、SDK統合後に自動的にトラッキングされます。

- セッション開始
- セッション終了

以下のイベントは、追加のセットアップ後にトラッキングされます。

- [購入イベント](#purchase-events): 開発チームがSDKの購入メソッドを使用してログに記録します。詳細については、購入イベントのセクションを参照してください。
- メールエンゲージメントイベント（メール開封やリンククリックなど）: Brazeメールを設定し、メールトラッキングを有効にすると、Brazeによってトラッキングされます。
- プッシュエンゲージメントイベント（プッシュ通知の開封やクリックなど）: Brazeでプッシュを設定し、アプリでBraze SDKとプッシュ処理を統合した後にトラッキングされます。

マーケターとして、標準イベントを使用してユーザーの行動やエンゲージメントを理解できます。たとえば、セッションデータはユーザーがアプリやサイトを開く頻度を示し、購入イベントは時間の経過に伴う収益のトラッキングに役立ちます。

## 購入イベント {#purchase-events}

購入イベントは、ユーザーが行った購入を記録しトラッキングします。Braze SDKを統合した後、開発チームはSDKの購入メソッドを使用して購入をログに記録できます。購入イベントを使用して購入をトラッキングすると、Brazeから直接、時間の経過やさまざまな収益ソースにわたる収益を監視できます。

購入イベントは、購入に関する以下の主要な情報を記録します。

- 製品ID（通常は製品名またはカテゴリ）
- 通貨
- 価格
- 数量

このデータを使用して、ライフタイムバリュー、購入頻度、特定の購入などに基づいてユーザーをセグメント化できます。

Brazeは複数通貨での購入もサポートしています。USD以外の通貨で購入が報告された場合、購入が報告された日付の為替レートに基づいて、BrazeダッシュボードではUSDで表示されます。

詳細については、専用の[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)の記事をご覧ください。

{% details 実装例 %}

購入イベントの実際の実装には、Braze SDKをアプリに統合する技術的な知識が必要です。カスタマーサクセスマネージャーがオンボーディングの一環としてチームにこのプロセスを説明しますが、一般的な手順は以下のとおりです。

1. **Braze SDKを統合する:** イベントをログに記録する前に、Braze SDKをアプリに統合する必要があります。
2. **購入イベントをログに記録する:** SDKが統合されたら、ユーザーがアプリ内で購入するたびに購入イベントをログに記録できます。これは通常、購入が完了したときに呼び出される関数またはメソッド内で行います。

以下は、Swiftを使用してiOSアプリで購入イベントをログに記録する例です。

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

この例では、「product_name」は購入された製品の名前、「USD」は購入の通貨、「1.99」は製品の価格、「1」は購入数量です。

{:start="3"}
3. **Brazeダッシュボードで購入イベントを確認する:** 購入イベントがログに記録されたら、Brazeダッシュボードで確認できます。このデータを使用して、収益の分析、ユーザーのセグメント化などを行うことができます。

実際の実装は、プラットフォーム（iOS、Android、Web）やアプリの具体的な要件によって異なる場合があります。

{% enddetails %}

## カスタムイベント {#custom-events}

カスタムイベントは、アプリやサイト内でトラッキングしたい特定のアクションに基づいて定義するイベントです。Brazeはこれらを自動的にトラッキングしないため、Braze SDKの実装でこれらのイベントを手動でセットアップする必要があります。カスタムイベントは、ゲームでユーザーがレベルをクリアすることから、ユーザーがプロファイル情報を更新することまで、さまざまなアクションに対応できます。

以下は、Swiftを使用してiOSアプリでカスタムイベントをログに記録する例です。

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

この例では、「completed_level」は、ユーザーがゲームでレベルをクリアしたときにログに記録されるカスタムイベントの名前です。このカスタムイベントはBrazeのユーザープロファイルに記録され、Campaignのトリガーやメッセージングのパーソナライズに使用できます。

詳細については、専用の[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)の記事をご覧ください。

{% details 実装例 %}

購入イベントと同様に、カスタムイベントにも追加のセットアップが必要です。以下は、Brazeでカスタムイベントを実装する一般的なプロセスです。

1. **Braze SDKを統合する:** イベントをログに記録する前に、Braze SDKをアプリに統合する必要があります。
2. **カスタムイベントを定義する:** アプリ内のどのアクションをカスタムイベントとしてトラッキングするかを決定します。ゲームでユーザーがレベルをクリアすること、ユーザーがプロファイルを更新すること、ユーザーが特定の種類の購入を行うことなど、アプリにとって重要なアクションであれば何でも構いません。
3. **カスタムイベントをログに記録する:** カスタムイベントを定義したら、アプリのコード内でログに記録できます。これは通常、アクションが発生したときに呼び出される関数またはメソッド内で行います。

以下は、Swiftを使用してiOSアプリでカスタムイベントをログに記録する例です。

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

この例では、「updated_profile」は、ユーザーがプロファイルを更新したときにログに記録されるカスタムイベントの名前です。

{:start="4"}
4. **カスタムイベントにプロパティを追加する（オプション）:** カスタムイベントに関する追加の詳細をキャプチャしたい場合は、プロパティを追加できます。これは、イベントをログに記録する際にプロパティのディクショナリを渡すことで行います。

以下は、Swiftを使用してiOSアプリでプロパティ付きのカスタムイベントをログに記録する例です。

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

この例では、カスタムイベントに「Property Name」というプロパティがあり、その値は「Property Value」です。

{:start="5"}
5. **Brazeダッシュボードでカスタムイベントを確認する:** カスタムイベントがログに記録されたら、Brazeダッシュボードで確認できます。このデータを使用して、ユーザー行動の分析、ユーザーのセグメント化などを行うことができます。

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->