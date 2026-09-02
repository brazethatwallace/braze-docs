---
nav_title: Verhalten
article_title: Verhalten von Content Cards anpassen
page_order: 2
description: "In diesem Implementierungsleitfaden werden Änderungen am Verhalten von Content Cards, das Hinzufügen von Extras wie Schlüssel-Wert-Paaren zur Nutzlast und Vorgehensweisen für gängige Anpassungen erläutert."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Verhalten von Content Cards anpassen {#customize-the-behavior-of-content-cards}

> In diesem Implementierungsleitfaden werden Änderungen am Verhalten von Content Cards, das Hinzufügen von Extras wie Schlüssel-Wert-Paaren zur Nutzlast und Vorgehensweisen für gängige Anpassungen erläutert. Eine vollständige Liste der Content-Card-Typen finden Sie unter [Über Content Cards]({{site.baseurl}}/developer_guide/content_cards).

## Schlüssel-Wert-Paare {#key-value-pairs}

Braze ermöglicht es Ihnen, zusätzliche Daten-Payloads über Content Cards mithilfe von Schlüssel-Wert-Paaren an die Geräte der Nutzer:innen zu senden. Diese können Ihnen helfen, interne Metriken zu verfolgen, App-Inhalte zu aktualisieren und Eigenschaften anzupassen. [Fügen Sie Schlüssel-Wert-Paare über das Dashboard hinzu]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#step-4-configure-additional-settings-optional).

{% alert note %}
Wir empfehlen nicht, verschachtelte JSON-Werte als Schlüssel-Wert-Paare zu senden. Stattdessen sollten Sie das JSON vor dem Senden flach strukturieren.
{% endalert %}

{% tabs %}
{% tab Internet %}

Schlüssel-Wert-Paare werden auf <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a>-Objekten als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Card zur weiteren Verarbeitung durch die App zu senden. Rufen Sie `card.extras` auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% tab Android %}

Schlüssel-Wert-Paare werden auf <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a>-Objekten als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Card zur weiteren Verarbeitung durch die App zu senden. Rufen Sie <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% tab Swift %}

Schlüssel-Wert-Paare werden auf <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a>-Objekten als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Card zur weiteren Verarbeitung durch die App zu senden. Rufen Sie <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% endtabs %}

{% alert tip %}
Es ist wichtig, dass Ihre Marketing- und Entwickler:innen-Teams abstimmen, welche Schlüssel-Wert-Paare verwendet werden (zum Beispiel `feed_type = brand_homepage`), da alle Schlüssel-Wert-Paare, die Marketer im Braze-Dashboard eingeben, genau mit den Schlüssel-Wert-Paaren übereinstimmen müssen, die Entwickler:innen in die App-Logik einbauen.
{% endalert %}

## Content Cards als ergänzende Inhalte {#content-cards-as-supplemental-content}

![Feed mit einer hybriden Liste, die lokale Daten und Braze Content Cards kombiniert.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Sie können Content Cards nahtlos in einen bestehenden Feed einbinden, sodass Daten aus mehreren Feeds gleichzeitig geladen werden. Dies schafft ein stimmiges, harmonisches Erlebnis mit Braze Content Cards und bestehenden Feed-Inhalten.

Das nebenstehende Beispiel zeigt einen Feed mit einer hybriden Liste von Artikeln, die sowohl mit lokalen Daten als auch mit Content Cards von Braze befüllt werden. Auf diese Weise sind Content Cards von bestehenden Inhalten nicht zu unterscheiden.

### API-getriggerte Schlüssel-Wert-Paare {#api-triggered-key-value-pairs}

[API-getriggerte Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) sind eine gute Strategie, wenn die Werte einer Card von externen Faktoren abhängen, die bestimmen, welche Inhalte den Nutzer:innen angezeigt werden sollen. Um beispielsweise ergänzende Inhalte anzuzeigen, legen Sie Schlüssel-Wert-Paare mit Liquid fest. Beachten Sie, dass `class_type` zum Zeitpunkt der Einrichtung bekannt sein sollte.

![Die Schlüssel-Wert-Paare für den Anwendungsfall „Ergänzende Content Cards“. In diesem Beispiel werden verschiedene Aspekte der Card wie „tile_id“, „tile_deeplink“ und „tile_title“ mithilfe von Liquid festgelegt.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards als interaktive Inhalte {#content-cards-as-interactive-content}
![Eine interaktive Content Card mit einer 50-Prozent-Aktion, die in der unteren linken Ecke des Bildschirms erscheint. Nach dem Klick wird die Aktion auf den Warenkorb angewendet.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Content Cards können genutzt werden, um dynamische und interaktive Erlebnisse für Ihre Nutzer:innen zu schaffen. Im nebenstehenden Beispiel erscheint ein Content-Card-Pop-up an der Kasse, um Nutzer:innen Last-Minute-Aktionen anzubieten. Gut platzierte Cards wie diese sind eine großartige Möglichkeit, Nutzer:innen einen „Nudge“ in Richtung bestimmter Aktionen zu geben.

Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen einen `discount_percentage`, der als gewünschter Rabattbetrag festgelegt wird, und einen `class_type`, der als `coupon_code` festgelegt wird. Diese Schlüssel-Wert-Paare ermöglichen es Ihnen, typspezifische Content Cards auf dem Checkout-Bildschirm zu filtern und anzuzeigen. Weitere Informationen zur Verwendung von Schlüssel-Wert-Paaren zur Verwaltung mehrerer Feeds finden Sie unter [Anpassen des Standard-Content-Card-Feeds]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#implementing-multiple-feeds).
<br>
<br>

![Interaktive Content Card mit einer Checkout-Aktion.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Content-Card-Badges {#content-card-badges}

![Ein iPhone-Startbildschirm, der eine Braze-Beispiel-App namens Swifty mit einem roten Badge zeigt, das die Zahl 7 anzeigt]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Badges sind kleine Symbole, die sich ideal eignen, um die Aufmerksamkeit von Nutzer:innen zu gewinnen. Mithilfe von Badges können Sie Nutzer:innen auf neue Content-Card-Inhalte aufmerksam machen, sie zurück in Ihre App locken und die Anzahl der Sitzungen steigern.

### Anzahl ungelesener Content Cards als Badge anzeigen {#displaying-the-number-of-unread-content-cards-as-a-badge}

Sie können die Anzahl ungelesener Content Cards als Badge auf dem App-Symbol anzeigen lassen.

{% tabs %}
{% tab web %}

Sie können die Anzahl ungelesener Karten jederzeit abfragen, indem Sie Folgendes aufrufen:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Anschließend können Sie diese Information verwenden, um ein Badge mit der Anzahl ungelesener Content Cards anzuzeigen. Weitere Informationen finden Sie in den <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDK-Referenzdokumenten</a>.

{% endtab %}
{% tab android %}

Sie können die Anzahl ungelesener Karten jederzeit abfragen, indem Sie Folgendes aufrufen:

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

Anschließend können Sie diese Information verwenden, um ein Badge mit der Anzahl ungelesener Content Cards anzuzeigen. Weitere Informationen finden Sie in den <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDK-Referenzdokumenten</a>.


{% endtab %}
{% tab swift %}

Das folgende Beispiel verwendet `braze.contentCards`, um die Anzahl ungelesener Content Cards abzufragen und anzuzeigen. Nachdem die App geschlossen wurde und die Sitzung der Nutzer:innen beendet ist, fragt dieser Code die Kartenanzahl ab und filtert die Anzahl der Karten basierend auf der Eigenschaft `viewed`.

Apps, die den [`UIScene`-Lebenszyklus](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) übernommen haben (erforderlich für Apps, die mit [Xcode 27 und höher](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) erstellt wurden), sollten dies in `sceneDidEnterBackground(_:)` von `SceneDelegate.swift` implementieren anstatt in `applicationDidEnterBackground(_:)` von `AppDelegate.swift`.

{% subtabs %}
{% subtab Swift %}

```swift
func sceneDidEnterBackground(_ scene: UIScene)
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, während Nutzer:innen während einer bestimmten Sitzung Karten ansehen:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)sceneDidEnterBackground:(UIScene *)scene
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, während Nutzer:innen während einer bestimmten Sitzung Karten ansehen:

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