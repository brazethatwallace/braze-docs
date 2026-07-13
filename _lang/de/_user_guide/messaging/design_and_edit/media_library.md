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

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Berechtigung „View Media Library Assets“ | Medienbibliothek-Assets anzeigen |
| Berechtigung „Edit Media Library Assets“ | Medienbibliothek-Assets erstellen und aktualisieren |
| Berechtigung „Delete Media Library Assets“ | Medienbibliothek-Assets aus der UI entfernen. Gelöschte Assets werden weiterhin von Braze gehostet, um zu verhindern, dass Nachrichten, die auf sie verweisen, fehlerhaft werden. Um ein Asset dauerhaft zu löschen, wenden Sie sich an den Braze-Support. |
| Berechtigung „Replace Media Library Assets“ | Die Datei eines vorhandenen Medienbibliothek-Assets ersetzen, wobei URL und Asset-ID stabil bleiben |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen für die Medienbibliothek" }

Weitere Informationen finden Sie unter [Nutzer:innenberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

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
* Die Datei eines vorhandenen Assets ersetzen, wobei die URL stabil bleibt
* Tags oder Teams hinzufügen, um Ihre Bilder besser zu organisieren
* In der Medienbibliothek-Übersicht nach Tags oder Teams suchen
* Bilder oder Ordner per Drag-and-Drop hochladen
* Bilder löschen

![Medienbibliothek-Seite mit einem Bereich „Upload To Library“ zum Ziehen, Ablegen oder Hochladen von Dateien. Darunter befindet sich eine Liste der hochgeladenen Inhalte in der Medienbibliothek.]({% image_buster /assets/img_archive/media_library_main.png %})

Wenn Sie später eine Nachricht in Braze verfassen, können Sie Ihre Bilder aus der Medienbibliothek einfügen.

![Zwei gängige Möglichkeiten, auf die Medienbibliothek zuzugreifen, je nach Nachrichten-Editor. Eine zeigt den E-Mail-Drag-and-Drop-Editor mit dem Titel „Images and GIFs“ und einem Button „Add from Media Library“. Die andere zeigt die Standard-Editoren, z. B. für Push und In-App-Nachrichten, mit dem Titel „Media“ und einem Button „Add Image“.]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Weitere Hilfe zur Medienbibliothek finden Sie in unseren [FAQ zur Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq). {% endalert %}

## Datei ersetzen {#replace-a-file}

Sie können die Datei eines vorhandenen Assets in der Medienbibliothek ersetzen, wobei URL und Asset-ID stabil bleiben. Da sich die URL nicht ändert, spiegelt jede Nachricht oder Campaign, die auf dieses Asset verweist – einschließlich bereits gesendeter E-Mails – automatisch die aktualisierte Datei wider. Dies ist nützlich, wenn Sie ein gemeinsam genutztes Asset (z. B. ein Logo) an einer einzigen Stelle aktualisieren möchten, anstatt jede Campaign einzeln zu bearbeiten.

Um ein Asset zu ersetzen, benötigen Sie die Berechtigung „Replace Media Library Assets“:

1. Gehen Sie zu **Content** > **Media Library**.
2. Wählen Sie das Asset aus, das Sie ersetzen möchten.
3. Wählen Sie im Modal **Replace file** aus.
4. Laden Sie die Ersatzdatei hoch.

![Modal zum Bearbeiten eines Medienbibliothek-Assets mit den Buttons „Replace file“, „Crop image“ und „Delete“.]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### Anforderungen und Einschränkungen {#requirements-and-limitations}

- Die Ersatzdatei muss dieselbe Dateierweiterung wie das Original haben. Beispielsweise können Sie ein `.png`-Asset nicht durch eine `.jpg`-Datei ersetzen.
- Video-Assets können nicht ersetzt werden.
- Nach dem Ersetzen kann es aufgrund von CDN-Caching einige Zeit dauern, bis die aktualisierte Datei allen Nutzer:innen angezeigt wird.

### Kanäle mit verarbeiteten Bildkopien {#channels-with-processed-image-copies}

Einige Kanäle erstellen beim Einrichten der Nachricht eine optimierte Kopie des Bildes, was zu einer separaten URL führt. Das Ersetzen des ursprünglichen Medienbibliothek-Assets aktualisiert nicht, was Nutzer:innen bei Nachrichten sehen, die über diese Kanäle erstellt wurden, einschließlich In-App-Nachrichten, Content Cards, Push-Benachrichtigungen und Banner.

Sie können ein Asset auch programmatisch über den Endpunkt [`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) ersetzen.

## Bildspezifikationen {#image-specifications}

Alle in die Medienbibliothek hochgeladenen Bilder müssen kleiner als 5&nbsp;MB sein. Unterstützte Dateitypen sind PNG, JPEG, GIF, SVG und WebP. Empfohlene Bildgrößen und Spezifikationen nach Messaging-Kanal finden Sie unter [Bildspezifikationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications).

{% alert important %}
GIFs mit sehr langgestreckten Formen (z. B. 3000 x 2 Pixel) oder 300 oder mehr Frames können beim Hochladen fehlschlagen, selbst wenn die Gesamtdateigröße klein ist.
{% endalert %}

## Bilder mit BrazeAI<sup>TM</sup> generieren {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Bevor Sie dieses Feature verwenden, lesen Sie, [wie Ihre Daten verwendet und an OpenAI gesendet werden]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#ai-policy).
{% endalert %}

Wenn Sie **AI Image Generator** auf der Seite **Media Library** nicht sehen, bestätigen Sie, dass Sie die Berechtigung **Edit Media Library Assets** haben. Falls die Option weiterhin fehlt, wenden Sie sich an Ihr Braze-Kundenteam, um zu bestätigen, dass Ihr Workspace Zugriff auf die BrazeAI-Bildgenerierung hat. Falls die Generierung fehlschlägt, lesen Sie die [OpenAI-Inhaltsrichtlinie]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#ai-policy).