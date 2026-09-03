---
nav_title: Bildspezifikationen
article_title: Bildspezifikationen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt die empfohlenen Bildgrößen und Spezifikationen für jeden Kanaltyp."
tool:
  - Templates
  - Media

---

# Bildspezifikationen {#image-specifications}

> Generell laden kleinere, qualitativ hochwertige Bilder schneller. Wir empfehlen daher, die kleinstmögliche Datei zu verwenden, die das gewünschte Ergebnis liefert. Um die Bildnutzung in bestimmten Kanälen zu optimieren, lesen Sie die Details in diesem Artikel.

Sie sollten Ihre Nachrichten immer auf verschiedenen Geräten [in der Vorschau anzeigen und testen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages), um sicherzustellen, dass die wichtigsten Bereiche Ihres Bildes und Ihrer Nachricht wie erwartet dargestellt werden.

## Bildverhalten {#image-behavior}

{% multi_lang_include channels/image_specs.md variable_name='image behavior' %}

## Video {#video}

Videos, die in die Medienbibliothek hochgeladen werden, können nur in WhatsApp-Nachrichten verwendet werden. Weitere Informationen finden Sie unter [Erstellen einer WhatsApp-Nachricht]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#outbound-messages).

## GIFs {#gifs}

GIFs werden in iOS-Push, In-App Messages, E-Mail, Content Cards und MMS- oder RCS-Nachrichten unterstützt. GIFs mit sehr langgestreckten Formen (zum Beispiel 3000 x 2 Pixel) oder 300 oder mehr Frames können möglicherweise nicht hochgeladen werden, selbst wenn die Gesamtdateigröße klein ist.

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

## Kanalrichtlinien {#channel-guidance}

### Content Cards

{% multi_lang_include channels/image_specs.md variable_name='content cards' %}

### E-Mail {#email}

{% multi_lang_include channels/image_specs.md variable_name='email' %}

### In-App-Nachrichten {#in-app-messages}

{% multi_lang_include channels/image_specs.md variable_name='in-app messages' %}

{% alert tip %} Erstellen Sie Assets mit Zuversicht! Unsere Bildvorlagen und Safe-Zone-Overlays für In-App-Nachrichten sind so gestaltet, dass sie auf Geräten aller Größen gut funktionieren. [Design-Templates-ZIP herunterladen]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

Weitere Informationen finden Sie unter [Kreative Details für In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

#### Font Awesome

Braze unterstützt die Verwendung von [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) für modale In-App-Nachrichten-Icons.

### Push-Benachrichtigungen {#push-notifications}

{% multi_lang_include channels/image_specs.md variable_name='payload size' %}

{% multi_lang_include channels/image_specs.md variable_name='push notifications' %}

#### Empfohlene Nachrichtenlängen {#recommended-message-lengths}

Für optimale Ergebnisse beachten Sie die folgenden Richtlinien zur Nachrichtenlänge beim Verfassen von Push-Nachrichten. Es kann je nach Vorhandensein eines Bildes, dem Benachrichtigungsstatus (iOS) und der Anzeigeeinstellung des Geräts der Nutzer:innen sowie der Gerätegröße zu Abweichungen kommen.

| Nachrichtentyp | Empfohlene Länge (nur Text) | Empfohlene Länge (Rich) |
| --- | --- | --- |
| iOS-Sperrbildschirm | 160 Zeichen | 130 Zeichen |
| iOS Notification Center | 160 Zeichen | 130 Zeichen |
| iOS-Bannerbenachrichtigung | 80 Zeichen | 65 Zeichen |
| Android-Sperrbildschirm | 49 Zeichen | N/A |
| Android-Benachrichtigungsleiste | 597 Zeichen | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Empfohlene Nachrichtenlängen" }

Weitere Informationen zu iOS-Zeichenanzahlen finden Sie unter [iOS-Richtlinien zur Zeichenanzahl]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count).

#### Web-Push {#web-push}

{% tabs %}
{% tab Bilder %}

| Browser | Empfohlene Symbolgröße |
| --- | --- |
| Chrome | 192 x 192 px oder größer |
| Firefox | 192 x 192 px oder größer |
| Safari | 192 x 192 px oder größer (pro Campaign konfigurierbar mit Safari 16 auf macOS 13+) |
| Opera | 192 x 192 px oder größer |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web-Push" }

| Browser | Plattform | Große Bildgröße |
| --- | --- | --- |
| Chrome | Android | 2:1 Seitenverhältnis |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 Seitenverhältnis |
| Edge | Windows | 2:1 Seitenverhältnis |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 Seitenverhältnis |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web-Push" }

{% endtab %}
{% tab Text %}

| Browser | Plattform | Maximale Titellänge | Maximale Textlänge |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Web-Push" }

{% endtab %}
{% endtabs %}

#### Beispiele für Push-Benachrichtigungen {#push-notification-examples}

{% tabs %}
{% tab iOS %}

![iOS-Push-Benachrichtigung mit dem Text „Hi! This is an iOS Push with an image“ und einem Emoji. Neben dem Text befindet sich ein kleines Bild.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS-Push-Benachrichtigung als Hard Push mit demselben Text wie die vorherige Nachricht und einem erweiterten Bild vor dem Text.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Android-Push-Benachrichtigung mit einem großen Bild unter dem Nachrichtentext.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Benachrichtigungen mit großen Bildern werden am besten mit einem Bild von mindestens 600 x 300 Pixeln angezeigt.
{% endalert %}

{% endtab %}
{% endtabs %}

Weitere Ressourcen finden Sie unter [Bild- und Textspezifikationen für Push-Benachrichtigungen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats).

### SMS und MMS {#sms-and-mms}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Informationen zum Verfassen von MMS-Nachrichten finden Sie unter [SMS-, MMS- oder RCS-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).