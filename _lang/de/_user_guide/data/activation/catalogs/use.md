---
nav_title: Verwendung von Katalogen
article_title: Kataloge verwenden
page_order: 1.5
description: "In diesem Referenzartikel erfahren Sie, wie Sie Kataloge verwenden, um Nicht-Nutzerdaten in Ihren Braze-Campaigns über Liquid zu referenzieren."
---

# Verwendung von Katalogen {#using-catalogs}

> Nachdem Sie einen Katalog erstellt haben, können Sie in Ihren Braze-Campaigns über [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) auf Nicht-Nutzerdaten verweisen. Sie können Kataloge in allen Ihren Messaging-Kanälen verwenden, auch überall dort, wo Liquid im Drag-and-Drop-Editor unterstützt wird.

## Kataloge in einer Nachricht verwenden {#using-catalogs-in-a-message}

Das folgende Video zeigt, wie Sie Kataloge in einer Nachricht verwenden können.

{% multi_lang_include video.html id="4yc2jkyn6w" source="wistia" %}

### Schritt 1: Personalisierungstyp hinzufügen {#step-one-personalization}

Wählen Sie im Nachrichten-Editor Ihrer Wahl <i class="fas fa-plus-circle"></i> **Personalisierung hinzufügen** und wählen Sie **Katalogartikel** als **Personalisierungstyp** aus. Wählen Sie dann Ihren Katalognamen aus. In unserem vorherigen Beispiel wählen wir den Katalog „Games“ aus.

![Modal „Personalisierung hinzufügen“ mit ausgewählten Katalogartikeln, ausgewähltem „Games“-Katalog und einer Liquid-Vorschau, die den catalog_items-Tag zeigt.]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Wir können sofort die folgende Liquid-Vorschau sehen:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Schritt 2: Katalogartikel auswählen {#step-2-select-catalog-items}

Als Nächstes fügen Sie Ihre Katalogartikel hinzu! Wählen Sie über das Dropdown-Menü die Katalogartikel und die anzuzeigenden Informationen aus. Diese Informationen entsprechen den Spalten in Ihrer hochgeladenen CSV-Datei, die zur Erstellung Ihres Katalogs verwendet wurde.

Um beispielsweise den Titel und den Preis unseres Spiels „Tales“ zu referenzieren, könnten wir die `id` für Tales (1234) als Katalogartikel auswählen und `title` und `price` als angezeigte Informationen anfordern.

{% raw %}
```liquid
{% catalog_items Games 1234 %}

Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Dies wird wie folgt dargestellt:

> Get Tales for just 7.49!

## Kataloge exportieren {#exporting-catalogs}

Es gibt zwei Möglichkeiten, Kataloge aus dem Dashboard zu exportieren:

- Fahren Sie im Bereich **Catalogs** mit dem Mauszeiger über die Katalogzeile. Wählen Sie dann den Button **Export catalog** aus.
- Wählen Sie Ihren Katalog aus. Wählen Sie dann den Button **Export catalog** im Tab **Preview** des Katalogs aus.

Sie erhalten eine E-Mail zum Herunterladen der CSV-Datei, nachdem Sie den Export gestartet haben. Sie haben bis zu vier Stunden Zeit, diese Datei abzurufen.

## Weitere Anwendungsfälle {#additional-use-cases}

### Mehrere Artikel {#multiple-items}

Sie sind nicht auf einen Artikel pro Nachricht beschränkt. Verwenden Sie das Modal **Personalisierung hinzufügen**, um bis zu drei Katalogartikel gleichzeitig hinzuzufügen. Um weitere hinzuzufügen, wählen Sie erneut **Personalisierung hinzufügen** im Editor und wählen Sie zusätzliche Katalogartikel und anzuzeigende Informationen aus.

Sehen Sie sich dieses Beispiel an, in dem wir die `id` von drei Spielen – Tales, Teslagrad und Acaratus – für **Katalogartikel** hinzufügen und `title` für **Anzuzeigende Informationen** auswählen.

![Modal „Personalisierung hinzufügen“ mit drei ausgewählten Katalogartikel-IDs und „title“ als anzuzeigende Information, mit einer Liquid-Vorschau, die jeden Artikeltitel auflistet.]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Wir können unsere Nachricht weiter personalisieren, indem wir Text um unser Liquid herum hinzufügen:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Dies wird wie folgt dargestellt:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

In diesem Beispiel ruft der `catalog_items`-Tag den Artikel `1234` aus dem `Games`-Katalog ab, und die `if`-Anweisung prüft das Feld `on_sale`, um unterschiedliche Nachrichten anzuzeigen.

#### Mit Katalog-Selections

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters.
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer.
{% else %}
{% abort_message('no venue_name') %}
{% endif %}
```
{% endraw %}

In diesem Beispiel werden unterschiedliche Nachrichten angezeigt, je nachdem, ob das Feld `venue_name` mehr oder weniger als 10 Zeichen hat. Wenn `venue_name` leer ist, wird die Nachricht abgebrochen.

Um auszugeben, wie viele Artikel eine Selection zurückgibt, verwenden Sie den Liquid-Filter `size` auf das `items`-Array nach dem Tag, nicht auf ein einzelnes Feld:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}{{ items | size }}
```
{% endraw %}

{% alert tip %}
Um Liquid-Syntaxfehler zu vermeiden, wählen Sie den **+**-Plus-Button im Nachrichten-Editor, um Katalog-Liquid-Tags automatisch einzufügen.
{% endalert %}

### Bilder verwenden {#using-images}

Sie können auch auf Bilder im Katalog verweisen, um sie in Ihren Nachrichten zu verwenden. Verwenden Sie dazu den `catalogs`-Tag und das `item`-Objekt im Liquid-Feld für Bilder.

Um zum Beispiel den `image_link` aus unserem Games-Katalog zu unserer Werbenachricht für Tales hinzuzufügen, wählen Sie die `id` für das Feld **Katalogartikel** und `image_link` für das Feld **Anzuzeigende Informationen**. Dies fügt die folgenden Liquid-Tags in unser Bildfeld ein:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Content-Card-Editor mit Katalog-Liquid-Tag im Bildfeld.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

So sieht es aus, wenn das Liquid gerendert wird:

![Beispiel einer Content-Card mit gerenderten Katalog-Liquid-Tags.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

{% alert important %}
In **HTML**-Kanälen wie E-Mail sollten Sie zusätzliche Leerzeichen oder Zeilenumbrüche zwischen dem schließenden `{% raw %}{% catalog_items ... %}{% endraw %}`-Tag und dem Liquid, das die Bild-URL ausgibt (zum Beispiel `{% raw %}{{ items[0].image_link }}{% endraw %}`), vermeiden. Zusätzlicher Whitespace im Template kann verhindern, dass die Bild-URL in der gerenderten Nachricht korrekt aufgelöst wird. Halten Sie den URL-Ausdruck direkt neben dem Katalog-Tag, wie in: `{% raw %}<img src="{% catalog_items Games 1234 %}{{ items[0].image_link }}">{% endraw %}`.
{% endalert %}

### Katalogartikel templaten

Sie können auch Templating verwenden, um Katalogartikel dynamisch basierend auf angepassten Attributen abzurufen. Nehmen wir zum Beispiel an, eine Nutzerin oder ein Nutzer hat das angepasste Attribut `wishlist`, das ein Array von Spiel-IDs aus Ihrem Katalog enthält.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
JSON-Objekte in Katalogen werden nur über die API aufgenommen. Sie können ein JSON-Objekt nicht über eine CSV-Datei hochladen.
{% endalert %}

Mit Liquid-Templating können Sie die Wunschlisten-IDs dynamisch abrufen und sie dann in Ihrer Nachricht verwenden. Dazu [weisen Sie eine Variable zu]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables) für Ihr angepasstes Attribut und verwenden dann das Modal **Personalisierung hinzufügen**, um einen bestimmten Artikel aus dem Array abzurufen. Variablen, die als Katalogartikel-ID referenziert werden, müssen in geschweifte Klammern eingeschlossen werden, um korrekt referenziert zu werden, wie z. B. `{{result}}`.

{% alert tip %}
Denken Sie daran, dass Arrays bei `0` beginnen, nicht bei `1`.
{% endalert %}

Um zum Beispiel Nutzer:innen darüber zu informieren, dass Tales (ein Artikel in unserem Katalog, den sie sich gewünscht haben) im Angebot ist, können wir Folgendes in unseren Nachrichten-Editor einfügen:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Dies wird wie folgt angezeigt:
> Get Tales now for just 7.49!

Mit Templating können Sie für jede Nutzerin und jeden Nutzer einen anderen Katalogartikel rendern, basierend auf deren individuellen angepassten Attributen, Event-Eigenschaften oder anderen templatefähigen Feldern.

### Eine CSV-Datei hochladen

Sie können eine CSV-Datei mit neuen Katalogartikeln zum Hinzufügen oder Katalogartikeln zum Update or aktualisieren or aktualisieren hochladen. Um eine Liste von Artikeln zu löschen, können Sie eine CSV-Datei mit Artikel-IDs hochladen, um sie zu löschen.

### Liquid verwenden

Sie können Kataloge auch manuell mit Liquid-Logik zusammensetzen. Beachten Sie jedoch, dass Braze, wenn Sie eine ID eingeben, die nicht existiert, trotzdem ein Items-Array ohne Objekte zurückgibt. Wir empfehlen, eine Fehlerbehandlung einzubauen, z. B. die Größe des Arrays zu prüfen und eine `if`-Anweisung zu verwenden, um den Fall eines leeren Arrays abzufangen.

#### Katalogartikel mit Liquid templaten

Ähnlich wie bei [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) müssen Sie das `:rerender`-Flag in einem Liquid-Tag verwenden, um den Liquid-Inhalt eines Katalogartikels zu rendern. Beachten Sie, dass das `:rerender`-Flag nur eine Ebene tief wirkt, d. h. es gilt nicht für verschachtelte Liquid-Tag-Aufrufe.

Wenn ein Katalogartikel Nutzerprofilfelder enthält (innerhalb eines Liquid-Personalisierungs-Tags), müssen diese Werte in Liquid zuvor in der Nachricht und vor dem Templating definiert werden, damit das Liquid korrekt gerendert wird. Wenn das `:rerender`-Flag nicht angegeben wird, wird der rohe Liquid-Inhalt gerendert.

Wenn beispielsweise ein Katalog namens „Messages“ einen Artikel mit folgendem Liquid enthält:

![Katalogtabellenzeile mit der ID „greet_msg“ und einer Spalte „Welcome_Message“, die eine Willkommensnachricht mit einer Liquid-Variablen für den Vornamen enthält.]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Um den folgenden Liquid-Inhalt zu rendern:

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Dies wird wie folgt angezeigt:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Katalog-Liquid-Tags können nicht rekursiv innerhalb von Katalogen verwendet werden.
{% endalert %}

## Fehlerbehebung bei der Katalog-Personalisierung

Wenn Katalog- oder Auswahl-Liquid in einer Nachricht oder einem Canvas-Schritt nicht wie erwartet angezeigt wird, überprüfen Sie Folgendes:

| Symptom | Was zu prüfen ist |
| --- | --- |
| Vorschau zeigt Artikel an, aber Live-Sendungen sind leer | Bestätigen Sie, dass die **Artikel-IDs** des Katalogs zum Sendezeitpunkt vorhanden sind. Wenn die ID in Ihrem Liquid nicht mit einer Zeile übereinstimmt, gibt Braze ein leeres Items-Array zurück — siehe [Liquid verwenden](#using-liquid). Prüfen Sie auf Tippfehler und auf ID-Quellen (wie Event-Eigenschaften), die beim Trigger or triggern oder im Kundenprofil or Nutzerprofil fehlen. |
| Editor-Vorschau funktioniert in einer Campaign, aber nicht in Canvas | Bestätigen Sie, dass Sie den richtigen Liquid-Kontext verwenden — **Canvas-Kontexteigenschaften** im Vergleich zu **Event-Eigenschaften** — und dass diese Felder beim Trigger or triggern vorhanden sind. Siehe [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties). |
| Eine Auswahl gibt keine Artikel zurück | Überprüfen Sie [Auswahlfilter]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) und Limits; bestätigen Sie, dass die Katalogdaten synchronisiert sind und die Spaltennamen mit Ihren Filtern übereinstimmen. |
| `:rerender` oder Template-basierte Zustellung sieht falsch aus | Für verschachteltes Liquid innerhalb von Katalogfeldern benötigen Sie `:rerender` und die korrekte Reihenfolge der Variablen — siehe [Katalogartikel mit Liquid als Template verwenden](#templating-catalog-items-including-liquid). Template-basierte In-App-Nachrichten werden zum Triggerzeitpunkt aufgelöst; siehe [Was sind Template-basierte In-App-Nachrichten?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages). Einige Kanäle schränken Katalog-Tags ein (zum Beispiel bestimmte **:rerender**-Verwendungen mit Banner) — siehe [Werden alle Liquid-Tags unterstützt?]({{site.baseurl}}/user_guide/channels/banners/faq#are-all-liquid-tags-supported) in den Banner-FAQ. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung bei der Katalog-Personalisierung" }

Allgemeine Informationen zum Liquid-Verhalten finden Sie unter [Liquid-Anwendungsfälle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) und [Liquid verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

## Strukturierung Ihrer Katalogdaten

Wenn Sie planen, wie Sie Ihre Katalogdaten strukturieren möchten, beginnen Sie mit Ihrem beabsichtigten Anwendungsfall und gestalten Sie den Katalog entsprechend. Jede Zeile im Katalog stellt einen Artikel dar (mit einer eindeutigen `id`). Die Spalten sollten die Attribute für diesen Artikel enthalten, wie URLs, Beschreibungstexte, Bild-URLs, Preis, Bewertung, Größe oder Farbe.

### Wann Sie standardmäßige Katalogaufrufe verwenden sollten

Bei standardmäßigen Katalogaufrufen gleichen Sie einen Wert mit der `id`-Spalte ab. Indem Sie ein angepasstes Attribut oder eine Event-Eigenschaft (als ID-String) in den Katalog-Liquid-Tag einfügen, können Sie mehrere Attribute für einen einzelnen Artikel in Ihre Nachricht einfügen. Häufige Anwendungsfälle sind:

- Zuletzt angesehenes Produkt oder zuletzt angesehener Dienst
- Wunschlisten-Artikel
- Angebote nach Standort
- Gekauftes Produkt
- Inhalte nach Lifecycle-Phase
- Zuletzt gesuchtes Produkt oder zuletzt gesuchter Dienst

### Wann Sie Katalogselektionen verwenden sollten

[Katalogselektionen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) ermöglichen es Ihnen, über jede Spalte in Ihrem Katalog zu filtern und bis zu 50 übereinstimmende Artikel zurückzugeben. Indem Sie angepasste Attribute oder Event-Eigenschaften in die Selektionsfilter einfügen, werden die Ergebnisse für jede Nutzer:in personalisiert. Häufige Anwendungsfälle sind:

- Artikel, bei denen die Kategorie der Präferenz einer Nutzer:in entspricht
- Artikel, die zur bevorzugten Marke, Küche oder Größe einer Nutzer:in passen
- Inhalte nach Abo-Typ oder Treuestufe
- Produkte innerhalb des durchschnittlichen Bestellwerts einer Nutzer:in

Der wesentliche Unterschied besteht darin, dass standardmäßige Katalogaufrufe einen einzelnen bekannten Artikel anhand der `id` nachschlagen, während Katalogselektionen den gesamten Katalog abfragen und mehrere Artikel zurückgeben, die Ihren Filterkriterien entsprechen.

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}