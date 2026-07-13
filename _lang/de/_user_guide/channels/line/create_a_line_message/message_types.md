---
nav_title: Nachrichtentypen
article_title: LINE-Nachrichtentypen
page_order: 0
description: "Dieser Artikel behandelt die verschiedenen Typen von LINE-Nachrichten."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# LINE-Nachrichtentypen {#line-message-types}

> Dieser Artikel behandelt die LINE-Nachrichtentypen, die Sie verfassen können, einschließlich ihrer Eigenschaften und Einschränkungen.

Wenn Sie eine LINE-Nachricht verfassen, können Sie Nachrichtentypen per Drag-and-Drop in den Composer ziehen und sie dann anpassen.

![Panel mit Nachrichtentypen zum Ziehen in den Composer-Editor, darunter Text, Bild, Rich-Nachricht und kartenbasierte Nachricht.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Text {#text}

Eine LINE-Textnachricht kann bis zu 5.000 Zeichen enthalten und Emojis sowie Liquid-Personalisierung einschließen.

Anwendungsfälle umfassen:
- Ankündigung einer zeitlich begrenzten Aktion für Restposten
- Versand personalisierter Geburtstagsgrüße mit einzigartigen Aktionskarten
- Teilen schneller Updates zu bevorstehenden Events

![Eine Textnachricht, die Nutzer:innen daran erinnert, die Black-Friday-Party nicht zu vergessen und bis zu 80 % vor Mitternacht zu sparen.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Bild {#image}

Eine LINE-Bildnachricht kann über die [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), eine URL oder Liquid hinzugefügt werden. Diese Bilder sind eigenständig und enthalten keine klickbaren Links.

Anwendungsfälle umfassen:
- Präsentation eines Urlaubsziels, um Nutzer:innen zum Kauf von Flugtickets zu inspirieren
- Hervorhebung von Saisonschlussaktionen, um Nutzer:innen zu ermutigen, sich mit günstiger Winterkleidung für nächstes Jahr einzudecken
- Start eines visuellen Countdowns zu einem jährlichen shopweiten Sale

![Eine Bildnachricht, die eine Toaster-Aktion bewirbt.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### URL-Bild {#url-image}

Verwenden Sie URL-Bilder für Anwendungsfälle, die Folgendes beinhalten:
- Dynamische Liquid-Bilder, indem Sie Liquid in Ihr Bildquellattribut einfügen. Zum Beispiel können Sie {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} als Bild-URL einfügen, um den Vornamen einer Nutzerin oder eines Nutzers in das Bild einzubinden
- [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), indem Bilder direkt von Ihrem Webserver oder öffentlich zugänglichen APIs abgerufen werden
- [Braze-Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs), indem auf Bilder aus importierten CSV-Dateien und API-Endpunkten zugegriffen wird

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Länge der Bilddatei-URL | Maximal 2.000 Zeichen  |
| Bildformat          | PNG, JPEG             |
| Dateigröße     |  Maximal 10&nbsp;MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL-Bild" }

## Rich-Nachrichten (Image Map) {#rich-messages-image-map}

Eine LINE-Rich-Nachricht ist ein Bild, das einen oder mehrere Links enthält, die durch Auswahl bestimmter Bereiche auf dem Bild geöffnet werden. Wählen Sie ein Rich-Nachrichten-Template aus, um festzulegen, wie die Links auf das Bild abgebildet werden.

Anwendungsfälle umfassen:
- Anzeige eines Rasters neu eingetroffener Handtaschen mit Links zu den jeweiligen Produktseiten
- Präsentation eines interaktiven Menüs, das eine Kombi-Bestellung durch Auswahl eines Artikels startet
- Darstellung mehrerer Aktionen, aus denen Nutzer:innen durch Auswahl eines Rasterfeldes wählen können

![Eine Rich-Nachricht mit sechs Feldern und einem Foto eines Schwarz-Weiß-Rasters, auf das Nutzer:innen tippen können, um ein zufälliges Angebot zu erhalten.]({% image_buster /assets/img/line/line_rich_message.png %})

### Image Map {#image-map}

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Länge der Bilddatei-URL | Maximal 2.000 Zeichen  |
| Bildformat          | PNG (kann transparent sein), JPEG             |
| Seitenverhältnis          | 1:1 (Breite:Höhe)
| Dateigröße     |  Maximal 10&nbsp;MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image Map" }

### URI-Link {#uri-link}

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Zeichenanzahl      | Maximal 1.000 |
| Schemata              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URI-Link" }

### Text

Eine Text-Rich-Nachricht kann bis zu 400 Zeichen enthalten.

## Kartenbasiert (Karussell) {#card-based-carousel}

Eine LINE-kartenbasierte Nachricht ermöglicht es Nutzer:innen, wie bei einem Karussell durch mehrere Nachrichten zu scrollen und auf die für sie relevantesten Nachrichten zu reagieren, indem sie eine Karte oder die Buttons einer Karte auswählen.

Anwendungsfälle umfassen:
- Anzeige von Aktionen für bestimmte Menüartikel
- Hervorhebung der meistverkauften Jacken der Saison
- Präsentation einer Auswahl an Kochwerkzeugen und Gadgets, die in einem Set enthalten sind

![Eine kartenbasierte Nachricht mit mindestens zwei Karten, die Sandwiches bewerben, im Composer-Editor.]({% image_buster /assets/img/line/line_card_message.png %})

### Nachricht {#message}

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Spalten                  | Maximal 10 |
| Seitenverhältnis             | Rechteck: 1,51:1 <br> Quadrat: 1:1  |
| Titel                    | Maximal 40 Zeichen
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nachricht" }


### Bild

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Bild-URL                 | Maximal 2.000 Zeichen |
| Bildformat              | JPEG oder PNG |
| Breite                     | 1.024 Pixel  |
| Dateigröße                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bild" }


### Text

| **Spezifikationen** | **Empfohlene Eigenschaften** |
|-------------------------|----------------------------|
| Zeichen              | Maximal 120 (ohne Bild oder Titel) <br> Maximal 60 (Nachricht mit Bild oder Titel)  |
| Aktionen                 | Maximal 3 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Text" }