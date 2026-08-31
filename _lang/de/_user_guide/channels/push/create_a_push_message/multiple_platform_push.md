---
nav_title: "Push-Nachrichten für mehrere Plattformen"
article_title: "Nachrichten für mehrere Plattformen"
alias: "/multiple_platform_push/"
description: "Dieser Artikel beschreibt, was Sie beachten sollten, wenn Sie eine Push-Campaign oder ein Canvas mit mehreren ausgewählten Plattformen erstellen."
page_order: 4
---

# Push-Nachrichten für mehrere Plattformen {#multiple-platform-push-messages}

> Dieser Artikel beschreibt, was Sie wissen sollten, wenn Sie eine Push-Campaign oder ein Canvas erstellen, um mehrere Plattformen und Geräte über einen einzigen Composer anzusprechen.

Wenn Sie eine Push-Campaign oder ein Canvas in Braze erstellen, können Sie mehrere Plattformen und Geräte auswählen, um eine Nachricht für alle Plattformen in einer einzigen Bearbeitungsoberfläche zu verfassen.

## Anwendungsfälle {#use-cases}

Diese Bearbeitungsoberfläche eignet sich am besten für die folgenden Anwendungsfälle:

- Mobile Push-Campaigns und Canvas-Nachrichten-Schritte, die an mehrere Gerätetypen gesendet werden müssen (z. B. sowohl iOS als auch Android).
- Zeitkritische Push-Benachrichtigungen, die schnell und präzise auf mehrere Plattformen ausgerichtet werden müssen und deren Inhalt plattformübergreifend identisch ist (z. B. Eilmeldungen oder Live-Spielupdates).

## Erstellen einer plattformübergreifenden Push-Campaign oder eines Canvas {#creating-a-multiple-platform-push-campaign-or-canvas}

So erstellen Sie eine Campaign, die auf mehrere Plattformen und Geräte ausgerichtet ist:

1. Erstellen Sie eine Campaign oder fügen Sie einem Canvas einen [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hinzu.
2. Wählen Sie **Push-Benachrichtigung** aus.
3. Wählen Sie die gewünschten Plattformen (Mobil, Internet, Kindle) und mobilen Geräte (iOS, Android) aus. Wenn Sie mehrere Geräte auswählen, steht multivariates Testen für Ihre Campaign nicht zur Verfügung.

### Plattformen für eine Campaign auswählen {#selecting-platforms-for-a-campaign}
![Optionen zur Auswahl mehrerer Plattformen für eine Push-Campaign, wie Mobil, Internet und Kindle, sowie mehrerer Geräte, wie iOS und Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Plattformen für einen Canvas-Schritt auswählen {#selecting-platforms-for-a-canvas-step}
![Optionen zur Auswahl mehrerer Plattformen für einen Push-Nachrichtenschritt, wie Mobil, Internet und Kindle, sowie mehrerer Geräte, wie iOS und Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. Wählen Sie **Bestätigen** aus. Nachdem Sie **Bestätigen** ausgewählt haben, können Sie die ausgewählten Plattformen oder Geräte nicht mehr ändern.
5. Fahren Sie mit der Einrichtung Ihrer Campaign oder Ihres Canvas fort.

## Durchführung eines multiplattform-fähigen, multivariaten Tests {#running-a-multi-platform-multivariate-test}

Multivariates Testen wird bei Multiplattform-Campaigns unterstützt. Wählen Sie das Plus-Symbol neben dem Namen der Variante aus, wie Sie es auch bei einer Einzelplattform-Campaign tun würden. Informationen zu den Einrichtungsschritten finden Sie unter [Multivariate und A/B-Tests erstellen]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests).

Informationen zur automatischen Optimierung Ihrer Varianten finden Sie unter [A/B-Tests mit BrazeAI<sup>TM</sup> optimieren]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

![Einfache multiplattform-fähige, multivariate Tests]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## Wissenswertes {#things-to-know}

### Einheitliches Messaging {#unified-messaging}
Auf dem Tab **Compose** können Sie einen Titel, eine Nachricht und ein Klickverhalten für alle ausgewählten Plattformen und Geräte festlegen.

Der Vorschaubereich zeigt eine Annäherung daran, wie Ihre Nachricht auf jeder Plattform aussieht. Dies kann zwar ein guter Indikator dafür sein, wo Sie Zeichenlimits erreichen könnten, aber denken Sie daran, Ihre Nachrichten vor dem Versand Ihrer Campaign immer auf einem echten Gerät zu testen.

![Einzelne Bearbeitungsansicht mit je einem Feld für Titel, Nachricht und Klickverhalten für drei Push-Typen: iOS, Android und Internet.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### Separate Assets {#separate-assets}
Im Abschnitt **Assets** wählen oder laden Sie die Bilder, die für jede Plattform angezeigt werden sollen. Beachten Sie, dass verschiedene Geräte unterschiedliche Spezifikationen für Bilder und Zeichenanzahl haben. Unter [Push-Nachrichten- und Bildformate]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) finden Sie weitere Hilfe.

![Assets-Bereich der einzelnen Bearbeitungsansicht mit Feldern für Push-Symbolbild, iOS-Benachrichtigungsbild, Android-Benachrichtigungsbild und Internet-Benachrichtigungsbild.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### Benachrichtigungstyp {#notification-type}

Der Benachrichtigungstyp ist standardmäßig auf „Standard-Push“ eingestellt und kann nicht geändert werden. Wenn Sie einen anderen Push erstellen möchten, wie z. B. Push Stories oder Inline-Bild (Android), erstellen Sie separate Campaigns für jeden Gerätetyp.

### Gerätespezifische Einstellungen {#device-specific-settings}

Sie können plattformspezifische Einstellungen im Editor bearbeiten. Dazu gehören Einstellungen wie [Push-Action-Buttons]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), Benachrichtigungskanäle und -gruppen, TTL, Anzeigepriorität, Sounds und mehr.

Weitere Informationen zu gerätespezifischen Einstellungen finden Sie in den folgenden Artikelsammlungen:

- [iOS-Optionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Android-Optionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push Stories sind plattformübergreifend nur auf Android und iOS verfügbar. Wenn Sie Internet oder Kindle als Plattform für den Versand auswählen, ist diese Option nicht verfügbar.