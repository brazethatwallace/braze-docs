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

Brazeでは、キーと値のペアを使用して、Content Cardsを介して追加のデータペイロードをユーザーデバイスに送信できます。これらは、内部指標の追跡、アプリコンテンツの更新、プロパティのカスタマイズに役立ちます。[ダッシュボードを使用してキーと値のペアを追加します]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional)。

{% alert note %}
ネストされたJSON値をキーと値のペアとして送信することは推奨しません。代わりに、送信する前にJSONを平坦化してください。
{% endalert %}

{% tabs %}
{% tab web %}

キーと値のペアは、`extras`として<a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> オブジェクトに格納されます。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用できます。`card.extras`を呼び出して、これらの値にアクセスします。

{% endtab %}
{% tab android %}

キーと値のペアは、`extras`として<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> オブジェクトに格納されます。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用できます。<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> を呼び出して、これらの値にアクセスします。

{% endtab %}
{% tab swift %}

キーと値のペアは、`extras`として<a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> オブジェクトに格納されます。これらは、カードと一緒にデータを送信し、アプリケーションでさらに処理するために使用できます。<a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> を呼び出して、これらの値にアクセスします。

{% endtab %}
{% endtabs %}

{% alert tip %}
マーケターがBrazeダッシュボードに入力するキーと値のペアは、開発者がアプリのロジックに組み込むキーと値のペアと正確に一致する必要があるため、マーケティングチームと開発チームが使用するキーと値のペア（たとえば`feed_type = brand_homepage`）について確実に調整することが重要です。
{% endalert %}

## 補足コンテンツとしてのContent Cards {#content-cards-as-supplemental-content}

![ローカルデータとBraze Content Cardsを組み合わせたハイブリッドリストを持つフィード。]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Content Cardsを既存のフィードにシームレスにブレンドし、複数のフィードからのデータを同時に読み込むことができます。これにより、Braze Content Cardsと既存のフィードコンテンツとの一貫性のある、調和のとれたエクスペリエンスが生まれます。

右の例は、ローカルデータとBrazeを活用したContent Cardsによるハイブリッドなアイテムリストを持つフィードを示しています。これにより、Content Cardsは既存のコンテンツと区別がつかなくなります。

### APIトリガーのキーと値のペア {#api-triggered-key-value-pairs}

[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)は、カードの値が外部要因に依存してユーザーに表示するコンテンツを決定する場合に使用するのに適した戦略です。たとえば、補足的なコンテンツを表示するには、Liquidを使用してキーと値のペアを設定します。なお、`class_type`はセットアップ時に把握しておく必要があります。

![補足Content Cardsのユースケースのキーと値のペア。この例では、「tile_id」、「tile_deeplink」、「tile_title」などカードのさまざまな要素がLiquidを使って設定されています。]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## インタラクティブコンテンツとしてのContent Cards {#content-cards-as-interactive-content}
![画面左下に50%のプロモーションを示すインタラクティブなContent Cardが表示されている。クリックすると、カートにプロモーションが適用されます。]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Content Cardsを活用して、ユーザーのためのダイナミックでインタラクティブな体験を作成できます。右の例では、Content Cardsのポップアップがチェックアウト時に表示され、ユーザーに最新のプロモーションを提供しています。このようなカードをうまく配置することで、ユーザーを特定のアクションに「後押し」することができます。

このユースケースのキーと値のペアには、希望する割引額として設定された`discount_percentage`と、`coupon_code`として設定された`class_type`が含まれます。これらのキーと値のペアによって、チェックアウト画面でタイプ別のContent Cardsをフィルタリングして表示できます。キーと値のペアを使用して複数のフィードを管理する方法の詳細については、[デフォルトのContent Cardsフィードのカスタマイズ]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds)を参照してください。
<br>
<br>

![チェックアウトプロモーションを表示するインタラクティブなContent Card。]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Content Cardsバッジ {#content-card-badges}

![Brazeのサンプルアプリ「Swifty」が表示されたiPhoneのホーム画面に、赤いバッジで数字の7が表示されている]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

バッジは小さなアイコンで、ユーザーの注意を引くのに最適です。バッジを使って新しいContent Cardsのコンテンツをユーザーに知らせることで、ユーザーをアプリに呼び戻し、セッションを増やすことができます。

### Content Cardsの未読数をバッジで表示する {#displaying-the-number-of-unread-content-cards-as-a-badge}

Content Cardsの未読数をバッジとしてアプリのアイコンに表示できます。

{% tabs %}
{% tab web %}

未読カードの数は、以下を呼び出していつでもリクエストできます。

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

この情報を使って、未読Content Cardsの数を示すバッジを表示できます。詳細については、<a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDKリファレンスドキュメント</a> を参照してください。

{% endtab %}
{% tab android %}

未読カードの数は、以下を呼び出していつでもリクエストできます。

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

この情報を使って、未読Content Cardsの数を示すバッジを表示できます。詳細については、<a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDKリファレンスドキュメント</a> を参照してください。


{% endtab %}
{% tab swift %}

次のサンプルでは、`braze.contentCards`を使用して未読Content Cardsの数をリクエストして表示しています。アプリが閉じられ、ユーザーのセッションが終了した後、このコードはカードカウントをリクエストし、`viewed`プロパティに基づいてカードの数をフィルタリングします。

[`UIScene`ライフサイクル](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)を採用しているアプリ（[Xcode 27以降](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)でビルドされたアプリに必須）では、`AppDelegate.swift`の`applicationDidEnterBackground(_:)`ではなく、`SceneDelegate.swift`の`sceneDidEnterBackground(_:)`で実装する必要があります。

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

このメソッド内で、次のコードを実装します。これにより、ユーザーが特定のセッション中にカードを閲覧している間にバッジカウントがアクティブに更新されます。

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

このメソッド内で、次のコードを実装します。これにより、ユーザーが特定のセッション中にカードを閲覧している間にバッジカウントがアクティブに更新されます。

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