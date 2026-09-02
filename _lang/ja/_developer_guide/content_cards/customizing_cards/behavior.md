---
nav_title: 動作
article_title: Content Cardsの動作をカスタマイズする
page_order: 2
description: "この実装ガイドでは、Content Cardsの動作の変更、ペイロードへのキーと値のペアなどの追加、一般的なカスタマイズのレシピについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cardsの動作をカスタマイズする {#customize-the-behavior-of-content-cards}

> この実装ガイドでは、Content Cardsの動作の変更、ペイロードへのキーと値のペアなどの追加、一般的なカスタマイズのレシピについて説明します。Content Cardsタイプの完全なリストについては、[Content Cardsについて]({{site.baseurl}}/developer_guide/content_cards)を参照してください。

## キーと値のペア {#key-value-pairs}

Brazeでは、キーと値のペアを使用して、Content Cardsを通じてユーザーデバイスに追加のデータペイロードを送信できます。これらは内部メトリクスの追跡、アプリコンテンツの更新、プロパティのカスタマイズに役立ちます。[ダッシュボードを使用してキーと値のペアを追加します]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#step-4-configure-additional-settings-optional)。

{% alert note %}
ネストされたJSONをキーと値のペアとして送信することは推奨しません。代わりに、送信前にJSONをフラット化してください。
{% endalert %}

{% tabs %}
{% tab web %}

キーと値のペアは、<a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> オブジェクトに`extras`として保存されます。これらを使用して、アプリケーションでさらに処理するためのデータをカードとともに送信できます。これらの値にアクセスするには`card.extras`を呼び出します。

{% endtab %}
{% tab Android %}

キーと値のペアは、<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> オブジェクトに`extras`として保存されます。これらを使用して、アプリケーションでさらに処理するためのデータをカードとともに送信できます。これらの値にアクセスするには<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> を呼び出します。

{% endtab %}
{% tab swift %}

キーと値のペアは、<a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> オブジェクトに`extras`として保存されます。これらを使用して、アプリケーションでさらに処理するためのデータをカードとともに送信できます。これらの値にアクセスするには<a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> を呼び出します。

{% endtab %}
{% endtabs %}

{% alert tip %}
マーケティングチームと開発者チームが使用するキーと値のペア（例：`feed_type = brand_homepage`）について連携することが重要です。マーケターがBrazeダッシュボードに入力するキーと値のペアは、開発者がアプリロジックに組み込むキーと値のペアと正確に一致する必要があります。
{% endalert %}

## 補足コンテンツとしてのContent Cards {#content-cards-as-supplemental-content}

![ローカルデータとBraze Content Cardsを組み合わせたハイブリッドリストのフィード。]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Content Cardsを既存のフィードにシームレスにブレンドして、複数のフィードからのデータを同時に読み込むことができます。これにより、Braze Content Cardsと既存のフィードコンテンツが一体となった、まとまりのある調和したエクスペリエンスを実現できます。

付属の例では、ローカルデータとBrazeを活用したContent Cardsの両方から生成されたアイテムのハイブリッドリストを持つフィードを示しています。この方法により、Content Cardsは既存のコンテンツと見分けがつかないように表示できます。

### APIトリガーのキーと値のペア {#api-triggered-key-value-pairs}

[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)は、カードの値がユーザーに表示するコンテンツを決定するために外部要因に依存する場合に有効な戦略です。たとえば、補足コンテンツを表示するには、Liquidを使用してキーと値のペアを設定します。`class_type`はセットアップ時に決定されている必要がある点に注意してください。

![補足Content Cardsのユースケースのキーと値のペア。この例では、「tile_id」、「tile_deeplink」、「tile_title」など、カードのさまざまな要素がLiquidを使用して設定されています。]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## インタラクティブコンテンツとしてのContent Cards {#content-cards-as-interactive-content}
![画面の左下隅に50パーセントのプロモーションを表示するインタラクティブなContent Card。クリックすると、プロモーションがカートに適用されます。]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Content Cardsを活用して、ユーザー向けにダイナミックなインタラクティブ体験を作成できます。この例では、チェックアウト時にContent Cardのポップアップが表示され、ユーザーに直前のプロモーションを提供します。このように適切に配置されたカードは、ユーザーに特定のアクションを促す「ナッジ」を与える優れた方法です。

このユースケースのキーと値のペアには、希望の割引額として設定された`discount_percentage`と、`coupon_code`として設定された`class_type`が含まれます。これらのキーと値のペアにより、チェックアウト画面でタイプ固有のContent Cardsをフィルタリングして表示できます。キーと値のペアを使用して複数のフィードを管理する方法の詳細については、[デフォルトのContent Cardフィードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds)を参照してください。
<br>
<br>

![チェックアウトプロモーションを表示するインタラクティブなContent Card。]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Content Cardsバッジ {#content-card-badges}

![赤いバッジに数字の7が表示されたSwiftyというBrazeサンプルアプリが映ったiPhoneのホーム画面]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

バッジは、ユーザーの注意を引くのに最適な小さなアイコンです。バッジを使用して新しいContent Cardsのコンテンツをユーザーに通知することで、ユーザーをアプリに呼び戻し、セッションを増やすことができます。

### 未読Content Cards数をバッジとして表示する {#displaying-the-number-of-unread-content-cards-as-a-badge}

未読Content Cardsの数をアプリのアイコンにバッジとして表示できます。

{% tabs %}
{% tab web %}

未読カード数は、以下を呼び出すことでいつでもリクエストできます。

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

この情報を使用して、未読Content Cardsの数を示すバッジを表示できます。詳細については、<a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDKリファレンスドキュメント</a> を参照してください。

{% endtab %}
{% tab android %}

未読カード数は、以下を呼び出すことでいつでもリクエストできます。

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

この情報を使用して、未読Content Cardsの数を示すバッジを表示できます。詳細については、<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDKリファレンスドキュメント</a> を参照してください。


{% endtab %}
{% tab swift %}

以下のサンプルでは、`braze.contentCards`を使用して未読Content Cardsの数をリクエストし、表示します。アプリが閉じられてユーザーのセッションが終了した後、このコードはカード数をリクエストし、`viewed`プロパティに基づいてカード数をフィルタリングします。

[`UIScene`ライフサイクル](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)を採用しているアプリ（[Xcode 27以降](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)でビルドされたアプリでは必須）では、`AppDelegate.swift`の`applicationDidEnterBackground(_:)`ではなく、`SceneDelegate.swift`の`sceneDidEnterBackground(_:)`に実装する必要があります。

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

このメソッド内で、特定のセッション中にユーザーがカードを閲覧する間、バッジカウントをアクティブに更新する以下のコードを実装します。

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

このメソッド内で、特定のセッション中にユーザーがカードを閲覧する間、バッジカウントをアクティブに更新する以下のコードを実装します。

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}