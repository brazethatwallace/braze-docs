---
nav_title: "Quick-Push-Nachrichten"
article_title: "Quick-Push-Nachrichten"
alias: "/quick_push/"
description: "Dieser Artikel beschreibt, was Sie beim Erstellen einer Push-Campaign oder eines Canvas mit der Quick-Push-Bearbeitungsoberfläche beachten sollten."
page_order: 4
---

# Quick-Push-Nachrichten {#quick-push-messages}

> Dieser Artikel beschreibt, was Sie wissen sollten, wenn Sie eine Push-Campaign oder ein Canvas mit der Quick-Push-Bearbeitungsoberfläche erstellen, um mehrere Plattformen und Geräte über einen einzigen Composer anzusprechen.

Wenn Sie eine Push-Campaign oder ein Canvas in Braze erstellen, können Sie mehrere Plattformen und Geräte auswählen, um eine Nachricht für alle Plattformen in einer einzigen Bearbeitungsoberfläche namens Quick Push zu verfassen.

## Anwendungsfälle {#use-cases}

Diese Bearbeitungsoberfläche eignet sich am besten für die folgenden Anwendungsfälle:

- Mobile Push-Campaigns und Canvas-Nachrichtenschritte, die an mehrere Gerätetypen gesendet werden müssen (z. B. sowohl iOS als auch Android).
- Zeitkritische Push-Benachrichtigungen, die schnell und präzise mehrere Plattformen ansprechen müssen und deren Inhalt plattformübergreifend identisch ist (z. B. Eilmeldungen oder Live-Spielupdates).

## Eine Quick-Push-Campaign oder ein Canvas erstellen {#creating-a-quick-push-campaign-or-canvas}

So erstellen Sie eine Campaign, die mehrere Plattformen und Geräte anspricht:

1. Erstellen Sie eine Campaign oder fügen Sie einem Canvas einen [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) hinzu.
2. Wählen Sie **Push notification** aus.
3. Wählen Sie Ihre gewünschten Plattformen (Mobile, Web, Kindle) und mobilen Geräte (iOS, Android) aus. Wenn Sie mehrere Geräte auswählen, steht multivariates Testen für Ihre Campaign nicht zur Verfügung.

### Plattformen für eine Campaign auswählen {#selecting-platforms-for-a-campaign}
![Optionen zur Auswahl mehrerer Plattformen für eine Push-Campaign, wie Mobile, Web und Kindle, sowie mehrerer Geräte, wie iOS und Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Plattformen für einen Canvas-Schritt auswählen {#selecting-platforms-for-a-canvas-step}
![Optionen zur Auswahl mehrerer Plattformen für einen Push-Nachrichtenschritt, wie Mobile, Web und Kindle, sowie mehrerer Geräte, wie iOS und Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. Wählen Sie **Confirm** aus. Nachdem Sie **Confirm** ausgewählt haben, können Sie Ihre ausgewählten Plattformen oder Geräte nicht mehr ändern.
5. Fahren Sie mit der Einrichtung Ihrer Campaign oder Ihres Canvas fort.

Ihr Composer wird etwas anders aussehen als gewohnt. Lesen Sie weiter, um zu erfahren, was sich unterscheidet.

### Was ist anders {#whats-different}

Auf dem Tab **Compose** können Sie einen Titel, eine Nachricht und ein Klickverhalten für alle Ihre ausgewählten Plattformen und Geräte festlegen.

Der Vorschaubereich zeigt eine Annäherung daran, wie Ihre Nachricht auf jeder Plattform aussehen wird. Obwohl er Ihnen einen guten Hinweis darauf geben kann, wo Sie Zeichenlimits erreichen könnten, denken Sie daran, Ihre Nachrichten immer auf einem echten Gerät zu testen, bevor Sie Ihre Campaign senden.

![Einzelne Bearbeitungsansicht mit einem Titel-, Nachrichten- und Klickverhaltensfeld für drei Push-Typen: iOS, Android und Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

Im Abschnitt **Assets** wählen oder laden Sie die Bilder hoch, die für jede Plattform angezeigt werden sollen. Beachten Sie, dass verschiedene Geräte unterschiedliche Spezifikationen für Bilder und Zeichenanzahlen haben. Weitere Hilfe finden Sie unter [Push-Nachrichten- und Bildformate]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/).

![Assets-Abschnitt der einzelnen Bearbeitungsansicht mit Feldern für Push-Icon-Bild, iOS-Benachrichtigungsbild, Android-Benachrichtigungsbild und Web-Benachrichtigungsbild.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Schließen Sie dann die Einrichtung Ihrer Push-Campaign wie gewohnt ab. Weitere Details finden Sie unter [Eine Push-Campaign erstellen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).

## Wissenswertes {#things-to-know}

### Benachrichtigungstyp {#notification-type}

Der Benachrichtigungstyp ist standardmäßig auf „Standard-Push“ eingestellt und kann nicht geändert werden. Wenn Sie einen anderen Push-Typ erstellen möchten, wie Push Stories oder Inline-Bild (Android), erstellen Sie separate Campaigns für jeden Gerätetyp.

### Multivariates Testen {#multivariate-testing}

Wenn Sie mehrere Geräte für mobile Plattformen auswählen, z. B. sowohl iOS als auch Android, steht multivariates Testen für Ihre Campaign nicht zur Verfügung. Wenn Sie multivariates Testen durchführen möchten, erstellen Sie separate Campaigns für jeden Gerätetyp.

### Gerätespezifische Einstellungen {#device-specific-settings}

Sie können plattformspezifische Einstellungen im Editor bearbeiten. Dazu gehören Einstellungen wie [Push-Action-Buttons]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/), Benachrichtigungskanäle und -gruppen, TTL, Anzeigepriorität, Töne und mehr.

Beachten Sie, dass Push-Action-Buttons nicht unterstützt werden, wenn Sie sowohl iOS als auch Android mit Quick-Push-Campaigns ansprechen. Weitere Informationen zu gerätespezifischen Einstellungen finden Sie in den folgenden Artikelsammlungen:

- [iOS-Optionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Android-Optionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)