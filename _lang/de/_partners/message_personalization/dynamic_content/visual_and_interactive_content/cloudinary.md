---
nav_title: Cloudinary
article_title: Cloudinary
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Cloudinary."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page) ist eine Bild- und Videoplattform zum Verwalten, Bearbeiten, Optimieren und Zustellen von Bildern und Videos in großem Umfang für jede Campaign über alle Kanäle und Customer Journeys hinweg. Bei Integration und Aktivierung ermöglicht das Medienmanagement von Cloudinary eine dynamische, kontextuelle und personalisierte Zustellung von Assets für Ihre Braze-Campaigns und Canvases.

## Über diese Integration {#about-this-integration}

Durch die Verbindung von Cloudinary mit Braze erhalten Marken Zugriff auf visuelle Medien, die in Cloudinary Assets gespeichert sind und in Braze-Messaging-Kanälen verwendet werden können. Mit den dynamischen Links von Cloudinary können Sie Bilder und Videos in Echtzeit auf der Grundlage von Braze-Nutzer:innen-Attributen auswählen und anpassen. Gemeinsam unterstützen Cloudinary und Braze die Erstellung visuell reichhaltiger, personalisierter Campaigns, die die Story jedes Produkts erzählen und einzigartige Erlebnisse in großem Maßstab liefern.

Auf dieser Seite werden vier mögliche, aber nicht erschöpfende Integrationsmethoden zwischen Cloudinary und Braze beschrieben. Diese Integrationsmethoden beruhen in erster Linie auf der manuellen Änderung von Asset-Links, die aus der Medienbibliothek von Cloudinary kopiert wurden.

{% alert important %}
Fortgeschrittenere Integrationsmethoden, einschließlich der Verwendung von [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) zum Aufrufen der [Admin-API](https://cloudinary.com/documentation/admin_api#banner) von Cloudinary, sind möglich, aber die Vorgehensweise variiert von Kund:in zu Kund:in. Wenden Sie sich an Ihren Customer-Success-Manager von Cloudinary und Braze, wenn Sie Hilfe benötigen.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|-----------------------|-----------------|
| Cloudinary-Konto | Ein [Cloudinary-Konto](https://cloudinary.com/users/register_free?utm_source=braze+docs+page) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrationsmethoden {#integration-methods}

{% alert tip %}
Einige dieser Integrationsmethoden nutzen die `f_auto`- und `q_auto`-Cloudinary-Transformationen, die eine tiefere Anpassung des Verhaltens und des Aussehens von [Bild-](https://cloudinary.com/documentation/image_transformations#banner) und [Video-Assets](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner) ermöglichen. Weitere Informationen zum Ändern eines Cloudinary-Asset-Links, um Transformationen einzubeziehen, finden Sie unter [URL-Struktur für Transformationen](https://cloudinary.com/documentation/image_transformations#transformation_url_structure).
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## Campaign-Assets über Cloudinary DAM auswählen {#select-campaign-assets-through-cloudinary-dam}

Der direkteste Weg, Bilder und Videos direkt aus dem DAM von Cloudinary in Ihren Braze-Campaigns und Canvases zu verwenden, besteht darin, die URL von der **Asset**-Seite der Cloudinary-Medienbibliothek zu kopieren.

![Eine Rasteransicht der Bild-Asset-Bibliothek von Cloudinary, wobei oben rechts bei einem der Bilder ein Tooltip „URL kopieren“ hervorgehoben ist.]({% image_buster /assets/img/cloudinary/one.png %})

### Bilder und GIFs einrichten {#images-and-gifs-setup}

1. Kopieren Sie die Bild- oder GIF-URL aus dem DAM in Cloudinary, indem Sie zu **Assets** > **Media Library** > **Assets** > **Copy URL** gehen.
2. Erstellen Sie den Bild-Tag in HTML und fügen Sie dann `f_auto,q_auto` zur kopierten URL hinzu, um das Bild oder GIF zu optimieren.

#### Beispiel-Bild-URL {#example-image-url}

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### Videos einrichten {#videos-setup}

1. Kopieren Sie den Bild- oder GIF-Link aus dem DAM in Cloudinary, indem Sie zu **Assets** > **Media Library** > **Assets** > **Copy URL** gehen.
2. Erstellen Sie den Video-Tag in HTML und fügen Sie dann `f_auto,q_auto` zur kopierten URL hinzu, um das Format und die Qualität des Videos automatisch zu optimieren.

#### Beispiel-Video-URL {#example-video-url}

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

Siehe [Video]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/video_in_custom_html/) für spezielle Überlegungen zu Android und iOS.

{% endtab %}
{% tab Videos in GIFs umwandeln %}

## Videos in GIFs für E-Mails umwandeln {#convert-videos-to-gifs-for-emails}

Verwenden Sie die `f_auto:animated`-[Cloudinary-Transformation](https://cloudinary.com/documentation/image_transformations/), um Video-Assets automatisch in GIFs zu konvertieren. Dies ist besonders wertvoll, wenn Sie den Braze-E-Mail-Kanal verwenden, da GIFs optimiert sind, um die E-Mail-Nutzlast zu reduzieren, die bei zu hohem Umfang zu Problemen bei der Zustellbarkeit führen kann.

### Konversion einrichten {#conversion-setup}

1. Kopieren Sie die Video-URL aus dem Cloudinary DAM.
2. Erstellen Sie den Bild-Tag und fügen Sie `f_auto:animated,fl_lossy` hinzu, um die GIF-Größe zu reduzieren und das beste Animationsformat für den Client auszuwählen.
3. Fügen Sie `c_scale,w_nnn` hinzu, um der gewünschten GIF-Breite im E-Mail-Layout zu entsprechen.
4. Fügen Sie `e_loop` hinzu, um die Animation zu wiederholen.

#### Beispiel-GIF-URL {#example-gif-url}

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab Targeting-Attribute %}

## Campaign-Assets dynamisch auf Basis von Targeting-Attributen auswählen {#dynamically-select-campaign-assets-based-on-targeting-attributes}

Diese Integrationsmethode ermöglicht eine dynamische Medienpersonalisierung, indem sie für jede:n Nutzer:in auf der Grundlage ihrer/seiner Attribute in Echtzeit das beste Asset auswählt.

Wenn Sie Liquid-Tags als Parameter in einen Cloudinary-Link innerhalb einer Braze-Campaign-Nachricht einfügen, werden die zugehörigen Braze-Attribute beim Senden der Nachricht die Liquid-Tags dynamisch ersetzen. Dabei kann es sich um nutzerspezifische Daten wie Sprache oder Kundenstufe handeln. Cloudinary ermittelt dann anhand dieser Attribute, welches Campaign-Asset am besten zu dieser/diesem Nutzer:in passt, und liefert automatisch das richtige Bild oder Video zurück. Dies führt dazu, dass Empfänger:innen nur kontextuell relevante und von der Marke genehmigte Assets erhalten.

### Funktionsweise {#how-it-works}

Cloudinary organisiert Campaign-Assets mit [Tags](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) und [strukturierten Metadaten (SMD)](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata), um sie durchsuchbar zu machen.

Jedes Campaign-Asset wird unter einem Campaign-Tag gruppiert (z. B. `spring_launch`) und mit strukturierten Metadatenfeldern angereichert, die Braze-Attributen wie `language=en` oder `tier=gold` entsprechen. Wenn Braze den Cloudinary-Link aufruft, verarbeitet eine [benutzerdefinierte Funktion](https://cloudinary.com/documentation/custom_functions#javascript_filters) die eingehenden Attribute, sucht nach dem Asset mit übereinstimmenden Tags und Metadaten und gibt dann die am besten passende Übereinstimmung zurück.

Wenn keine exakte Übereinstimmung gefunden wird, wählt die Funktion automatisch eine Fallback- oder „nächstbeste“ Option aus, um die Kontinuität in jedem Erlebnis zu gewährleisten. Wenn das Asset ausgewählt ist, optimiert die Transformationsebene von Cloudinary (zum Beispiel `f_auto` oder `q_auto`) die Medien für die Zustellung. Diese Kombination aus Tags, Metadaten und angepassten Funktionen bietet Entwickler:innen eine flexible, API-gesteuerte Möglichkeit zur Automatisierung der personalisierten Zustellung von Assets.

{% alert tip %}
Eine Anleitung zum Erstellen und Anwenden angepasster Funktionen sowie ein Beispiel für eine angepasste Funktion zur Auswahl von Assets und Fallback-Optionen für eine bestimmte Campaign finden Sie im [`braze-personalization`-GitHub-Repo](https://github.com/cloudinary-devs/braze-personalization) von Cloudinary. Für weitere Unterstützung wenden Sie sich bitte an Ihr Cloudinary-Support-Team.
{% endalert %}

### Voraussetzungen

Um eine dynamische Auswahl von Assets zu ermöglichen, muss Cloudinary in der Lage sein, eine Reihe von Assets auf der Grundlage von Tags und Metadaten zurückzugeben. Wenn der Zustellungstyp „Liste“ eingeschränkt ist, kann Cloudinary nicht die dynamische Liste bereitstellen, die für die personalisierte Auswahl von Assets in Braze-Campaigns benötigt wird.
- Heben Sie die Einschränkung des Zustellungstyps „Liste“ auf: Öffnen Sie die Sicherheitseinstellungen in Ihrer Cloudinary-Konsole und deaktivieren Sie den Eintrag „Ressourcenliste“ unter „Eingeschränkte Bildtypen“.

### Dynamische Auswahl einrichten {#dynamic-selection-setup}

1. Richten Sie den Tag und die Metadaten für Assets in Cloudinary ein.
2. Laden Sie Ihre angepasste Funktion in das Cloudinary DAM hoch.
3. Erstellen Sie die Cloudinary-URL für den gewünschten Tag.
4. Fügen Sie auf Basis der Tag-URL dynamische Liquid-Tags für Bilder hinzu, um die Braze-Attribute und die angepasste Funktion einzubinden.

#### Beispiel-URL {#example-url}

In diesem Beispiel wird davon ausgegangen, dass Assets in Cloudinary über zwei definierte SMD-Felder („locale“ und „audience“) verfügen, die mit den erwarteten Werten entsprechend den Braze-Attributen gefüllt sind. Außerdem wurden die für die Campaign benötigten Assets mit dem Tag „samples“ versehen, und die angepasste Funktion `segmentedBanner.js` wurde in das Cloudinary-Konto hochgeladen.

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %}
{% assign locale = {{${language}}}%}

// The URL for the "samples" tag used in the campaign is https://solutions-demo-res.cloudinary.com/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://solutions-demo-res.cloudinary.com/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner">
```
{% endraw %}

##### Ausgabe-URLs {#output-urls}

- Ausgabe-URL für Nutzer:innen mit Zielgruppe `internal` und Lokalisierung `en`:
```
https://solutions-demo-res.cloudinary.com/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- Ausgabe-URL für Nutzer:innen mit Zielgruppe `external` und Lokalisierung `es`:
```
https://solutions-demo-res.cloudinary.com/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- Fallback-Bild-URL:
```
https://solutions-demo-res.cloudinary.com/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab Personalisierte Bilderstellung %}

## Personalisierte Bilderstellung {#personalized-image-generation}

Die [Text-Overlay-Transformationen](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/) von Cloudinary verwenden Nutzerdaten aus Braze direkt in einem Cloudinary-Asset.

Das folgende Beispiel zeigt, wie die `l_text`-Transformation verwendet werden kann, um den Namen einer/eines Nutzers:in in ein Asset einzufügen. Weitere Anpassungen können Sie vornehmen, indem Sie bei der Entwicklung von Campaigns und Canvases Liquid-Tags nutzen, um festzulegen, welcher Text in die `l_text`-Parameter eingefügt werden soll.

Wenn Sie mehr darüber erfahren möchten, wie Transformations-Parameter zur Gestaltung eines Assets verwendet werden können, wenden Sie sich an Ihr Cloudinary-Support-Team.

### Beispiel einer `l_text`-Transformation {#example-l_text-transformation}

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%}
{% assign second_name = {{${last_name}}}%}

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### Beispiel einer Ausgabe-URL {#example-output-url}

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![Eine weiße Kirche mit blauem Dach und Blick auf das Meer. Oben links im Bild sind die Worte „John Smith“ auf einem halbtransparenten dunklen Rechteck zu sehen.]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}