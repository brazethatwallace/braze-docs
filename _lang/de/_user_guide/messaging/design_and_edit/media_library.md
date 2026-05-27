---
nav_title: Medienbibliothek
article_title: Medienbibliothek
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die Medienbibliothek. Hier erfahren Sie, wie Sie Ihre Assets an einem einzigen, zentralen Ort verwalten, Bilder mithilfe von KI generieren und im Nachrichten-Editor auf Medien zugreifen können."
tool: Media

---

# Medienbibliothek {#media-library}

> Die Medienbibliothek ermöglicht es Ihnen, Ihre Assets an einem einzigen, zentralen Ort zu verwalten.

## Medienbibliothek versus CDN {#media-library-versus-cdn}

Die Verwendung der Medienbibliothek anstelle eines Content Delivery Network (CDN) bietet besseres Caching und bessere Performance für In-App-Nachrichten. Alle Medienbibliothek-Assets, die in einer In-App-Nachricht enthalten sind, werden für eine schnellere Anzeige vorab zwischengespeichert und stehen auch offline zur Verfügung. Darüber hinaus ist die Medienbibliothek in die Braze-Editoren integriert, sodass Marketer Bilder auswählen oder taggen können, anstatt Bild-URLs kopieren und einfügen zu müssen.

## Zugriff auf die Medienbibliothek {#accessing-the-media-library}

In der Medienbibliothek können Sie den Asset-Typ, die Größe, die Abmessungen, die URL, das Datum des Hinzufügens zur Bibliothek und weitere Informationen einsehen. Um auf Ihre Braze-Medienbibliothek zuzugreifen, gehen Sie zu **Content** > **Media Library**. Hier können Sie:

* Mehrere Bilder gleichzeitig hochladen
* Virtual Contact Files (.vcf) hochladen
* Videodateien zur Verwendung in WhatsApp-Nachrichten hochladen
* Einen Ordner mit Ihren Bildern hochladen (bis zu 50 Bilder)
* [Ein Bild mithilfe von KI generieren](#generate-ai) und in der Medienbibliothek speichern
* Ein vorhandenes Bild zuschneiden, um das richtige Seitenverhältnis für Ihre Nachrichten zu erstellen
* Tags oder Teams hinzufügen, um Ihre Bilder besser zu organisieren
* In der Medienbibliothek-Übersicht nach Tags oder Teams suchen
* Bilder oder Ordner per Drag-and-Drop hochladen
* Bilder löschen

![Medienbibliothek-Seite mit einem Bereich „Upload To Library“ zum Ziehen, Ablegen oder Hochladen von Dateien. Darunter befindet sich eine Liste der hochgeladenen Inhalte in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_main.png %})

Wenn Sie später eine Nachricht in Braze verfassen, können Sie Ihre Bilder aus der Medienbibliothek einfügen.

![Zwei gängige Möglichkeiten, auf die Medienbibliothek zuzugreifen, je nach Nachrichten-Editor. Eine zeigt den E-Mail-Drag-and-Drop-Editor mit dem Titel „Images and GIFs“ und einem Button „Add from Media Library“. Die andere zeigt die Standard-Editoren, z. B. für Push und In-App-Nachrichten, mit dem Titel „Media“ und einem Button „Add Image“.]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Weitere Hilfe zur Medienbibliothek finden Sie in unseren [FAQ zur Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq/). {% endalert %}

## Bildspezifikationen {#image-specifications}

Alle in die Medienbibliothek hochgeladenen Bilder müssen kleiner als 5&nbsp;MB sein. Unterstützte Dateitypen sind PNG, JPEG, GIF, SVG und WebP. Empfohlene Bildgrößen und Spezifikationen nach Messaging-Kanal finden Sie unter [Bildspezifikationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/).

{% alert important %}
GIFs mit sehr langgestreckten Formen (z. B. 3000 x 2 Pixel) oder 300 oder mehr Frames können beim Hochladen fehlschlagen, selbst wenn die Gesamtdateigröße klein ist.
{% endalert %}

## Bilder mit BrazeAI<sup>TM</sup> generieren {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Bevor Sie dieses Feature verwenden, lesen Sie, [wie Ihre Daten verwendet und an OpenAI gesendet werden]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}