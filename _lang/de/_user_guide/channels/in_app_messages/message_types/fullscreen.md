---
nav_title: "Vollbild"
article_title: Vollbild-In-App-Nachrichten
description: "Dieser Referenzartikel behandelt die Nachrichten- und Designanforderungen von Vollbild-In-App-Nachrichten."
page_type: reference
page_order: 1
channel:
  - in-app messages
tool:
  - Media

---

# Vollbild-In-App-Nachrichten {#fullscreen-in-app-messages}

> Vollbild-Nachrichten nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer:innen wirklich benötigen, z. B. für Pflicht-App-Updates.

Dieser Nachrichtentyp ist sowohl im [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) als auch im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) verfügbar.

{% tabs %}
{% tab Hochformat %}

![Zwei Vollbild-In-App-Nachrichten nebeneinander im Hochformat mit Bild- und Textempfehlungen. Details finden Sie in den folgenden Abschnitten.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Querformat %}

![Zwei Vollbild-In-App-Nachrichten nebeneinander im Querformat mit Bild- und Textempfehlungen. Details finden Sie in den folgenden Abschnitten.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Bilder {#images}

Vollbild-In-App-Nachrichten füllen die gesamte Höhe eines Geräts aus und werden bei Bedarf horizontal (links und rechts) zugeschnitten. Bild-und-Text-Vollbildnachrichten füllen 50 % der Gerätehöhe aus. Alle Vollbild-In-App-Nachrichten füllen die Statusleiste auf Geräten mit „Notch“ aus.

- Alle Bilder müssen kleiner als 5&nbsp;MB sein.
- Wir akzeptieren nur die Dateitypen PNG, JPEG und [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs).
- Wir empfehlen eine Bildgröße von 500&nbsp;KB.

{% alert tip %} Erstellen Sie Assets mit Zuversicht! Unsere Bildvorlagen und Safe-Zone-Overlays für In-App-Nachrichten sind so konzipiert, dass sie auf Geräten aller Größen gut funktionieren. [Design-Templates-ZIP herunterladen]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Hochformat {#portrait}

| Layout | Asset-Größe | Hinweise |
|--- | --- | --- |
| Bild und Text | Seitenverhältnis 6:5<br> Hohe Auflösung 1200 x 1000&nbsp;px<br> Minimum 600 x 500&nbsp;px | Zuschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Viewports |
| Nur Bild | Seitenverhältnis 3:5<br> Hohe Auflösung 1200 x 2000&nbsp;px<br> Minimum 600 x 1000&nbsp;px | Zuschnitt kann an den linken und rechten Rändern auf höheren Geräten erfolgen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Hochformat" }

### Querformat {#landscape}

| Layout | Asset-Größe | Hinweise |
|--- | --- | --- |
| Bild und Text | Seitenverhältnis 10:3<br> Hohe Auflösung 2000 x 600px<br> Minimum 1000 x 300&nbsp;px | Zuschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Viewports |
| Nur Bild | Seitenverhältnis 5:3<br> Hohe Auflösung 2000 x 1200px<br> Minimum 1000 x 600&nbsp;px | Zuschnitt kann an den linken und rechten Rändern auf höheren Geräten erfolgen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Querformat" }

### Bildsicherer Bereich {#image-safe-zone}

Wenn Sie eine Vollbild-In-App-Nachricht in der Braze-Plattform in der Vorschau anzeigen, können Sie die bildsichere Zone aktivieren – den Bereich der Nachricht, der beim Anzeigen auf verschiedenen Geräten vor Zuschnitt geschützt ist. Zusätzlich zum Testen der bildsicheren Zone im Vorschaubereich empfehlen wir, wie immer [Ihre Nachricht zu testen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

![Vorschau einer In-App-Nachricht in Braze mit aktivierter Option „Bildsichere Zone anzeigen“. Die bildsichere Zone ist ein Overlay über dem Bild, das visualisiert, welche Teile des Bildes vor Zuschnitt geschützt sind.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Größere Bildschirme {#larger-screens}

Auf einem Tablet oder Desktop-Browser wird eine Vollbild-In-App-Nachricht in der Mitte des App-Bildschirms angezeigt, wie im folgenden Screenshot dargestellt.

{% tabs %}
{% tab Hochformat %}

![Vollbild-In-App-Nachricht, wie sie auf einem großen Bildschirm im Hochformat erscheinen würde. Die Nachricht wird als großes Modal in der Mitte des Bildschirms angezeigt.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Querformat %}

![Vollbild-In-App-Nachricht, wie sie auf einem großen Bildschirm im Querformat erscheinen würde. Die Nachricht wird als großes Modal in der Mitte des Bildschirms angezeigt.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}