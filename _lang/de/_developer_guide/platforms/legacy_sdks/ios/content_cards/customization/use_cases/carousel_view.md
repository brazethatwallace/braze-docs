---
nav_title: Karussell-Ansicht
article_title: Content-Card-Karussell-Ansicht für iOS
platform: iOS
page_order: 5
description: "Dieser Artikel beschreibt, wie Sie einen Anwendungsfall für eine Content-Card-Karussell-Ansicht in iOS-Anwendungen implementieren."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Anwendungsfall: Karussell-Ansicht {#use-case-carousel-view}

![Beispiel einer Nachrichten-App, die ein Karussell von Content Cards in einem Artikel anzeigt.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

In diesem Abschnitt erfahren Sie, wie Sie einen Karussell-Feed mit mehreren Karten implementieren, bei dem Nutzer:innen horizontal wischen können, um weitere vorgestellte Karten anzuzeigen. Für die Integration einer Karussell-Ansicht müssen Sie eine vollständig angepasste Content-Card-Implementierung verwenden – die „Run“-Phase des [Crawl-Walk-Run-Ansatzes]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize#customization-approaches).

Bei diesem Ansatz verwenden Sie nicht die Braze-Ansichten und die Standardlogik, sondern zeigen die Content Cards auf eine völlig angepasste Weise an, indem Sie Ihre eigenen Ansichten verwenden, die mit Daten aus den Braze-Modellen befüllt werden.

Die wichtigsten Unterschiede im Hinblick auf den Entwicklungsaufwand zwischen der Basis-Implementierung und der Karussell-Implementierung sind:

- Erstellen eigener Ansichten
- Protokollierung der Content-Card-Analytics
- Einführung zusätzlicher clientseitiger Logik, um zu bestimmen, wie viele und welche Karten im Karussell angezeigt werden sollen

## Implementierung {#implementation}

### 1. Schritt: Einen angepassten View Controller erstellen {#step-1-create-a-custom-view-controller}

Um das Content-Card-Karussell zu erstellen, erstellen Sie Ihren eigenen angepassten View Controller (z. B. `UICollectionViewController`) und [abonnieren Sie Datenaktualisierungen]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#getting-the-data). Beachten Sie, dass Sie den standardmäßigen `ABKContentCardTableViewController` nicht erweitern oder als Unterklasse verwenden können, da er nur die standardmäßigen Content-Card-Typen verarbeiten kann.

### 2. Schritt: Analytics implementieren {#step-2-implement-analytics}

Wenn Sie einen vollständig angepassten View Controller erstellen, werden Content-Card-Impressionen, -Klicks und -Ausblendungen nicht automatisch protokolliert. Sie müssen die entsprechenden Analytics-Methoden implementieren, um sicherzustellen, dass Impressionen, Ausblende-Ereignisse und Klicks ordnungsgemäß in den Analytics des Braze-Dashboards aufgezeichnet werden.

Informationen zu den Analytics-Methoden finden Sie unter [Kartenmethoden]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
Auf derselben Seite finden Sie auch die verschiedenen Eigenschaften, die von unserer generischen Content-Card-Modellklasse geerbt werden und die Sie bei der Implementierung Ihrer Ansicht nützlich finden könnten.
{% endalert %}

### 3. Schritt: Einen Content-Card-Beobachter erstellen {#step-3-create-a-content-card-observer}

Erstellen Sie einen [Content-Card-Beobachter]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener), der für das Eintreffen von Content Cards verantwortlich ist, und implementieren Sie bedingte Logik, um eine bestimmte Anzahl von Karten gleichzeitig im Karussell anzuzeigen. Standardmäßig werden Content Cards nach dem Erstellungsdatum sortiert (neueste zuerst), und Nutzer:innen sehen alle Karten, für die sie berechtigt sind.

Sie können die Sortierung und zusätzliche Anzeigelogik jedoch auf verschiedene Weisen anpassen. Zum Beispiel könnten Sie die ersten fünf Content-Card-Objekte aus dem Array auswählen oder Schlüssel-Wert-Paare (die Eigenschaft `extras` im Datenmodell) einführen, um bedingte Logik aufzubauen.

Wenn Sie ein Karussell als sekundären Content-Card-Feed implementieren, lesen Sie den Abschnitt [Mehrere Content-Card-Feeds verwenden]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds), um sicherzustellen, dass Sie die Karten anhand von Schlüssel-Wert-Paaren in den richtigen Feed sortieren.

{% alert important %}
Es ist wichtig, dass sich Ihre Marketing- und Entwicklerteams darüber abstimmen, welche Schlüssel-Wert-Paare verwendet werden sollen (z. B. `feed_type = brand_homepage`), denn alle Schlüssel-Wert-Paare, die Marketer in das Braze-Dashboard eingeben, müssen exakt mit den Schlüssel-Wert-Paaren übereinstimmen, die die Entwickler:innen in die App-Logik einbauen.
{% endalert %}

Die iOS-spezifische Entwicklerdokumentation zur Content-Card-Klasse, den Methoden und Attributen finden Sie in der iOS-[`ABKContentCard`-Klassenreferenz](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Überlegungen {#considerations}

- Wenn Sie vollständig angepasste Ansichten verwenden, können Sie die in `ABKContentCardsController` verwendeten Methoden nicht erweitern oder als Unterklasse verwenden. Stattdessen müssen Sie die Methoden und Eigenschaften des Datenmodells selbst integrieren.
- Die Logik und Implementierung der Karussell-Ansicht ist kein standardmäßiger Content-Card-Typ in Braze. Daher muss die Logik zur Umsetzung dieses Anwendungsfalls von Ihrem Entwicklungsteam bereitgestellt und unterstützt werden.
- Sie müssen clientseitige Logik implementieren, um jeweils eine bestimmte Anzahl von Karten im Karussell anzuzeigen.