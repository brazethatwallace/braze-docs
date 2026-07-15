---
nav_title: "Nachrichten- und Bildformate"
article_title: "Nachrichten- und Bildformate"
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt Nachrichten- und Bildformate für Push-Benachrichtigungen."
channel: push

---

# Push-Nachrichten- und Bildformate {#push-message-and-image-formats}

> Dieser Referenzartikel beschreibt Nachrichten- und Bildformate für Push-Benachrichtigungen.

Für optimale Ergebnisse beachten Sie die folgenden Richtlinien zu Bildgrößen und Nachrichtenlängen beim Erstellen Ihrer Push-Nachrichten. Es kann je nach Vorhandensein eines Bildes, dem Benachrichtigungsstatus (iOS) und der Anzeigeeinstellung des Geräts der Nutzer:innen sowie der Gerätegröße zu Abweichungen kommen. Im Zweifelsfall halten Sie Ihren Text kurz und prägnant.

## iOS- und Android-Push {#ios-and-android-push}

{% tabs local %}
{% tab Bilder %}

**Bildtyp** | **Empfohlene Bildgröße** | **Maximale Bildgröße** | **Dateitypen**
--- | --- | --- | ---
(iOS) 2:1 *Empfohlen* | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG, GIF
(Android) Push-Symbol | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
(Android) Erweiterte Benachrichtigung | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="iOS- und Android-Push" }

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

{% endtab %}
{% tab Text %}

| Nachrichtentyp | Empfohlene Nachrichtenlänge (nur Text) | Empfohlene Nachrichtenlänge (Rich)
--- | ---
(iOS) Sperrbildschirm | 160 Zeichen | 130 Zeichen
(iOS) Mitteilungszentrale | 160 Zeichen | 130 Zeichen
(iOS) Banner-Hinweis | 80 Zeichen | 65 Zeichen
(Android) Sperrbildschirm | 49 Zeichen | N/A
(Android) Benachrichtigungsleiste | 597 Zeichen | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS- und Android-Push" }

Sie fragen sich, wie viele Zeichen Sie in einer iOS-Push-Benachrichtigung verwenden können, ohne dass sie abgeschnitten wird? Sehen Sie sich unsere [iOS-Zeichenanzahl-Richtlinien]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count) an.

{% endtab %}
{% tab Payload-Größe %}

**Plattform** | **Größe**
--- | ---
vor iOS 8 | 0,256 KB
ab iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 aria-label="iOS- und Android-Push" }

{% endtab %}
{% tab Bildbeispiel %}
{% subtabs %}
{% subtab iOS %}

![iOS-Push-Benachrichtigung mit dem Text „Hi! Dies ist ein iOS-Push mit einem Bild“ und einem Emoji. Neben dem Text befindet sich ein kleines Bild.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![iOS-Push-Benachrichtigung bei einem Hard Push mit demselben Text wie die vorherige Nachricht und einem erweiterten Bild vor dem Text.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Android-Push-Benachrichtigung mit einem großen Bild unter dem Nachrichtentext.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Benachrichtigungen mit großen Bildern werden am besten mit einem Bild von mindestens 600 x 300 Pixeln angezeigt.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Textbeispiel %}
{% subtabs %}
{% subtab iOS %}

![iOS-Push-Benachrichtigung mit dem Text „Hi! Dies ist ein iOS-Push“.]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Android-Push-Benachrichtigung auf dem Startbildschirm.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Web-Push {#web-push}

{% tabs local %}
{% tab Bilder %}

| **Browser** | **Empfohlene Symbolgröße**
| --- | ---
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web-Push" }
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Symbole sind pro Campaign konfigurierbar mit Safari 16+ auf macOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web-Push" }

| **Browser** | **Plattform** | **Große Bildgröße**
| --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web-Push" }
Chrome | Android | 2:1 Seitenverhältnis
Firefox | Android | N/A
Chrome | Windows | 2:1 Seitenverhältnis
Edge | Windows | 2:1 Seitenverhältnis
Firefox | Windows | N/A
Firefox | Windows | 2:1 Seitenverhältnis
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web-Push" }

{% endtab %}
{% tab Text %}

| **Browser** | **Plattform** | **Maximale Titellänge**  | **Maximale Nachrichtentextlänge**
| --- | --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Web-Push" }
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Web-Push" }

{% endtab %}
{% endtabs %}