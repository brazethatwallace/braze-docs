---
nav_title: Slideup
article_title: Slideup-In-App-Nachrichten
page_order: 3
channel:
  - in-app messages
tool:
  - Media
description: "Dieser Referenzartikel behandelt die Nachrichten- und Designanforderungen von Slideup-In-App-Nachrichten."

---

# Slideup-In-App-Nachrichten {#slideup-in-app-messages}

> Unsere Slideups erscheinen in der Regel am oberen oder unteren Rand des App-Bildschirms (Sie können dies beim Erstellen Ihrer Nachricht festlegen). Sie eignen sich hervorragend, um Ihre Nutzer:innen über neue Nutzungsbedingungen, Cookies und andere Informations-Snippets zu informieren. Sie sind unaufdringlich und ermöglichen es Ihren Nutzer:innen, weiterhin mit Ihrer App zu interagieren, während die Nachricht angezeigt wird.

Dieser Nachrichtentyp ist im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) verfügbar.

![Zwei Slideup-In-App-Nachrichten, eine erscheint am oberen Bildschirmrand und die andere am unteren, mit Bild- und Textempfehlungen. Siehe folgende Abschnitte für Details.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Bild- und Textverhalten {#image-and-copy-behavior}

Slideup-Nachrichten können bis zu drei Textzeilen enthalten, bevor sie mit Auslassungspunkten abgeschnitten werden. Bilder in Slideups werden niemals beschnitten oder abgeschnitten – sie werden immer so herunterskaliert, dass sie in den 50 x 50 Pixel großen Bildcontainer passen.

{% multi_lang_include in-app_messages/image_requirements.md %}

{% alert tip %} Erstellen Sie Assets mit Zuversicht! Unsere Bildvorlagen und Safe-Zone-Overlays für In-App-Nachrichten sind so konzipiert, dass sie auf Geräten aller Größen gut funktionieren. [Design-Vorlagen-ZIP herunterladen]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Layout | Asset-Größe | Hinweise |
|--- | --- | --- |
| Bild + Text | Seitenverhältnis 1:1<br>Hochauflösend 150 x 150&nbsp;px<br> Minimum 50 x 50&nbsp;px | Bilder mit verschiedenen Seitenverhältnissen passen ohne Beschnitt in einen quadratischen Bildcontainer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Bild- und Textverhalten" }

Sie sollten Ihre Nachrichten immer auf verschiedenen Geräten [in der Vorschau anzeigen und testen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message), um sicherzustellen, dass die wichtigsten Bereiche Ihres Bildes und Ihrer Nachricht wie erwartet erscheinen. Beachten Sie, dass die tatsächliche Darstellung auf Geräten von der Vorschau Ihrer Nachricht im Composer abweichen kann.

## Hyperlinks und Ankertext {#hyperlinks-and-anchor-text}

Um einen Link in einem Slideup hinzuzufügen, geben Sie den Nachrichtentext im Feld **Body** ein und legen Sie das Ziel unter **On-Klick, der or klicken behavior** fest (zum Beispiel **Redirect to URL**). Wenn **On-Klick, der or klicken behavior** konfiguriert ist, löst ein Tippen auf eine beliebige Stelle der Nachricht – außer auf das Schließen-Steuerelement – diese Aktion aus.

Für angepasste HTML-In-App-Nachrichten können Sie HTML-Links direkt verwenden. Siehe [Angepasste HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html).

## Mobilgeräte {#mobile-devices}

Auf Mobilgeräten erscheinen Slideups am oberen oder unteren Rand des App-Bildschirms. Sie können dies beim Erstellen Ihrer Nachricht festlegen. Nutzer:innen können wischen, um das Slideup zu schließen, oder darauf tippen, um es zu öffnen, wenn eine Klick-Aktion enthalten ist. Wenn dem Slideup eine Klick-Aktion hinzugefügt wird, wird ein Chevron „>“ angezeigt.

## Größere Bildschirme {#larger-screens}

{% tabs %}
{% tab Desktop %}

In einem Desktop-Browser wird eine Slideup-In-App-Nachricht in der Ecke des Bildschirms angezeigt, wie im folgenden Screenshot dargestellt (sofern beim Erstellen der In-App-Nachricht nichts anderes festgelegt wurde). Nutzer:innen können auf die Schließen-Schaltfläche „X“ klicken, um das Slideup zu schließen.

![Slideup-In-App-Nachricht, wie sie in einem Desktop-Browser erscheint. Die Nachricht wird in der unteren rechten Ecke des Bildschirms angezeigt und nimmt nicht die gesamte Bildschirmbreite ein.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

Auf einem Tablet erscheint eine Slideup-In-App-Nachricht am unteren Bildschirmrand. Ähnlich wie auf Mobilgeräten können Nutzer:innen wischen, um das Slideup zu schließen, oder darauf tippen, um es zu öffnen, wenn eine Klick-Aktion enthalten ist. Wenn dem Slideup eine Klick-Aktion hinzugefügt wird, wird ein Chevron „>“ angezeigt. Eine Schließen-Schaltfläche „X“ wird standardmäßig nicht angezeigt.

![Slideup-In-App-Nachricht, wie sie auf einem Tablet-Bildschirm erscheint. Die Nachricht wird unten in der Mitte des Bildschirms angezeigt und nimmt nicht die gesamte Bildschirmbreite ein.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}