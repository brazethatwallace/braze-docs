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

Mit Braze können Sie zusätzliche Daten-Nutzlasten über Content Cards an Nutzer:innengeräte senden, indem Sie Schlüssel-Wert-Paare verwenden. Diese können Ihnen helfen, interne Metriken zu tracken, App-Inhalte zu aktualisieren und Eigenschaften anzupassen. [Fügen Sie Schlüssel-Wert-Paare über das Dashboard hinzu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional).

{% alert note %}
Wir raten davon ab, verschachtelte JSON-Werte als Schlüssel-Wert-Paare zu senden. Stattdessen sollten die JSON-Werte vor dem Senden durch Flatten vereinfacht werden.
{% endalert %}

{% tabs %}
{% tab web %}

Schlüssel-Wert-Paare werden in Objekten des Typs <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Karte zur weiteren Bearbeitung durch die Anwendung zu senden. Rufen Sie `card.extras` auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% tab android %}

Schlüssel-Wert-Paare werden in Objekten des Typs <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Karte zur weiteren Bearbeitung durch die Anwendung zu senden. Rufen Sie <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% tab swift %}

Schlüssel-Wert-Paare werden in Objekten des Typs <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> als `extras` gespeichert. Diese können verwendet werden, um Daten zusammen mit einer Karte zur weiteren Bearbeitung durch die Anwendung zu senden. Rufen Sie <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> auf, um auf diese Werte zuzugreifen.

{% endtab %}
{% endtabs %}

{% alert tip %}
Es ist wichtig, dass sich Ihre Marketing- und Entwicklerteams darüber abstimmen, welche Schlüssel-Wert-Paare verwendet werden sollen (z. B. `feed_type = brand_homepage`), denn alle Schlüssel-Wert-Paare, die Marketer in das Braze-Dashboard eingeben, müssen exakt mit den Schlüssel-Wert-Paaren übereinstimmen, die die Entwickler:innen in die App-Logik einbauen.
{% endalert %}

## Content Cards als ergänzender Inhalt {#content-cards-as-supplemental-content}

![Feed mit einer hybriden Liste, die lokale Daten und Braze Content Cards kombiniert.]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Sie können Content Cards nahtlos in einen bestehenden Feed einfügen, sodass Daten aus mehreren Feeds gleichzeitig geladen werden können. Dadurch entsteht ein zusammenhängendes, harmonisches Erlebnis mit Braze Content Cards und vorhandenen Feed-Inhalten.

Das nebenstehende Beispiel zeigt einen Feed mit einer hybriden Liste von Artikeln, die über lokale Daten und von Braze bereitgestellte Content Cards gefüllt werden. Auf diese Weise können Content Cards ununterscheidbar neben bestehenden Inhalten stehen.

### API-getriggerte Schlüssel-Wert-Paare {#api-triggered-key-value-pairs}

[API-getriggerte Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) sind eine gute Strategie, wenn die Werte einer Karte von externen Faktoren abhängen, um zu bestimmen, welche Inhalte den Nutzer:innen angezeigt werden sollen. Um zum Beispiel ergänzende Inhalte anzuzeigen, legen Sie Schlüssel-Wert-Paare mit Liquid fest. Beachten Sie, dass `class_type` zum Zeitpunkt der Einrichtung bekannt sein sollte.

![Die Schlüssel-Wert-Paare für den Anwendungsfall mit ergänzenden Content Cards. In diesem Beispiel werden verschiedene Aspekte der Karte, wie z. B. „tile_id“, „tile_deeplink“ und „tile_title“, mit Liquid festgelegt.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Content Cards als interaktive Inhalte {#content-cards-as-interactive-content}
![Unten links im Bildschirm erscheint eine interaktive Content-Card mit einer 50-Prozent-Rabattaktion. Nach dem Klick wird die Aktion auf den Warenkorb angewendet.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"}

Content Cards können genutzt werden, um dynamische und interaktive Erlebnisse für Ihre Nutzer:innen zu schaffen. Im nebenstehenden Beispiel erscheint an der Kasse ein Content-Card-Popup, das den Nutzer:innen Last-Minute-Aktionen bietet. Gut platzierte Karten wie diese sind eine großartige Möglichkeit, den Nutzer:innen einen „Anstoß“ zu bestimmten Aktionen zu geben.

Die Schlüssel-Wert-Paare für diesen Anwendungsfall umfassen einen `discount_percentage`, der als gewünschter Rabattbetrag festgelegt ist, und einen `class_type`, der als `coupon_code` festgelegt ist. Mit diesen Schlüssel-Wert-Paaren können Sie typspezifische Content Cards im Checkout-Bildschirm filtern und anzeigen. Weitere Informationen zur Verwendung von Schlüssel-Wert-Paaren zur Verwaltung mehrerer Feeds finden Sie unter [Anpassen des Standard-Content-Card-Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed#multiple-feeds).
<br>
<br>

![Interaktive Content-Card mit einer Checkout-Aktion.]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"}

## Content-Card-Badges {#content-card-badges}

![Ein iPhone-Startbildschirm, auf dem eine Braze-Beispiel-App namens „Swifty“ mit einem roten Badge angezeigt wird, auf dem die Zahl 7 zu sehen ist]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Badges sind kleine Symbole, die ideal dazu geeignet sind, die Aufmerksamkeit von Nutzer:innen zu gewinnen. Mithilfe von Badges, die Nutzer:innen auf neue Content-Card-Inhalte aufmerksam machen, können Sie Ihre App wieder in das Bewusstsein der Nutzer:innen rücken und die Anzahl der Sitzungen erhöhen.

### Anzeige der Anzahl ungelesener Content Cards als Badge {#displaying-the-number-of-unread-content-cards-as-a-badge}

Sie können die Anzahl der ungelesenen Content Cards, die Ihre Nutzer:innen haben, als Badge auf dem Symbol Ihrer App anzeigen.

{% tabs %}
{% tab web %}

Sie können die Anzahl der ungelesenen Karten jederzeit abfragen, indem Sie Folgendes aufrufen:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Anhand dieser Informationen können Sie dann ein Badge anzeigen, das die Anzahl der ungelesenen Content Cards angibt. Weitere Informationen finden Sie in der <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">SDK-Referenzdokumentation</a>.

{% endtab %}
{% tab android %}

Sie können die Anzahl der ungelesenen Karten jederzeit abfragen, indem Sie Folgendes aufrufen:

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

Anhand dieser Informationen können Sie dann ein Badge anzeigen, das die Anzahl der ungelesenen Content Cards angibt. Weitere Informationen finden Sie in der <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">SDK-Referenzdokumentation</a>.


{% endtab %}
{% tab swift %}

Das folgende Beispiel verwendet `braze.contentCards`, um die Anzahl der ungelesenen Content Cards abzufragen und anzuzeigen. Nachdem die App geschlossen und die Sitzung der Nutzer:innen beendet wurde, fordert dieser Code eine Kartenzählung an und filtert die Anzahl der Karten anhand der Eigenschaft `viewed`.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, wenn Nutzer:innen in einer bestimmten Sitzung Karten ansehen:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, wenn Nutzer:innen in einer bestimmten Sitzung Karten ansehen:

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