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

In diesem Abschnitt erfahren Sie, wie Sie einen Karussell-Feed mit mehreren Karten implementieren, bei dem Nutzer:innen horizontal wischen können, um weitere vorgestellte Karten anzuzeigen. Für die Integration einer Karussell-Ansicht müssen Sie eine vollständig angepasste Content-Card-Implementierung verwenden – die „Run“-Phase des [Crawl-Walk-Run-Ansatzes]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

Bei diesem Ansatz verwenden Sie nicht die Braze-Ansichten und die Standardlogik, sondern zeigen die Content Cards auf eine völlig angepasste Weise an, indem Sie Ihre eigenen Ansichten verwenden, die mit Daten aus den Braze-Modellen befüllt werden.

Die wichtigsten Unterschiede im Hinblick auf den Entwicklungsaufwand zwischen der Basis-Implementierung und der Karussell-Implementierung sind:

- Erstellen eigener Ansichten
- Protokollierung der Content-Card-Analytics
- Einführung zusätzlicher clientseitiger Logik, um zu bestimmen, wie viele und welche Karten im Karussell angezeigt werden sollen

## Implementierung {#implementation}

### Schritt 1: Erstellen Sie einen benutzerdefinierten View Controller {#step-1-create-a-custom-view-controller}

Um das Content-Cards-Karussell zu erstellen, erstellen Sie Ihren eigenen benutzerdefinierten View Controller (z. B. `UICollectionViewController`) und [abonnieren Sie Datenaktualisierungen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#getting-the-data). Beachten Sie, dass Sie unseren Standard-`ABKContentCardTableViewController` nicht erweitern oder ableiten können, da dieser nur unsere Standard-Content-Card-Typen verarbeiten kann.

### Schritt 2: Implementieren Sie Analytics {#step-2-implement-analytics}

Wenn Sie einen vollständig benutzerdefinierten View Controller erstellen, werden Content-Card-Impressionen, Klicks und Schließungen nicht automatisch protokolliert. Sie müssen die entsprechenden Analytics-Methoden implementieren, um sicherzustellen, dass Impressionen, Schließungsereignisse und Klicks ordnungsgemäß in die Analytics des Braze-Dashboards zurückgemeldet werden.

Informationen zu den Analytics-Methoden finden Sie unter [Kartenmethoden]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
Auf derselben Seite werden auch die verschiedenen Eigenschaften beschrieben, die von unserer generischen Content-Card-Modellklasse geerbt werden und die bei der Implementierung Ihrer Ansicht nützlich sein können.
{% endalert %}

### Schritt 3: Erstellen Sie einen Content-Card-Observer {#step-3-create-a-content-card-observer}

Erstellen Sie einen [Content-Card-Observer]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener), der für die Verarbeitung eingehender Content Cards zuständig ist, und implementieren Sie bedingte Logik, um eine bestimmte Anzahl von Karten gleichzeitig im Karussell anzuzeigen. Standardmäßig werden Content Cards nach Erstellungsdatum sortiert (neueste zuerst), und Nutzer:innen sehen alle Karten, für die sie berechtigt sind.

Sie können die Reihenfolge und zusätzliche Anzeigelogik jedoch auf verschiedene Arten festlegen und anwenden. Beispielsweise könnten Sie die ersten fünf Content-Card-Objekte aus dem Array auswählen oder Schlüssel-Wert-Paare (die `extras`-Eigenschaft im Datenmodell) verwenden, um bedingte Logik aufzubauen.

Wenn Sie ein Karussell als sekundären Content-Cards-Feed implementieren, lesen Sie [Mehrere Content-Card-Feeds verwenden]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds), um sicherzustellen, dass Karten basierend auf Schlüssel-Wert-Paaren dem richtigen Feed zugeordnet werden.

{% alert important %}
Es ist wichtig, dass Ihre Marketing- und Entwicklerteams abstimmen, welche Schlüssel-Wert-Paare verwendet werden (z. B. `feed_type = brand_homepage`), da alle Schlüssel-Wert-Paare, die Marketer im Braze-Dashboard eingeben, genau mit den Schlüssel-Wert-Paaren übereinstimmen müssen, die die Entwickler:innen in die App-Logik integrieren.
{% endalert %}

Die iOS-spezifische Entwicklerdokumentation zur Content-Cards-Klasse, zu Methoden und Attributen finden Sie in der [iOS `ABKContentCard`-Klassenreferenz](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Überlegungen {#considerations}

- Wenn Sie vollständig angepasste Ansichten verwenden, können Sie die in `ABKContentCardsController` verwendeten Methoden nicht erweitern oder als Unterklasse verwenden. Stattdessen müssen Sie die Methoden und Eigenschaften des Datenmodells selbst integrieren.
- Die Logik und Implementierung der Karussell-Ansicht ist kein Standardtyp von Content Cards in Braze. Daher muss die Logik zur Umsetzung des Anwendungsfalls von Ihrem Entwicklungsteam bereitgestellt und unterstützt werden.
- Sie müssen eine clientseitige Logik implementieren, um eine bestimmte Anzahl von Cards gleichzeitig im Karussell anzuzeigen.