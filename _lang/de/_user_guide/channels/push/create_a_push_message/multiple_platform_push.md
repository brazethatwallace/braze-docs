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

- Mobile Push-Campaigns und Canvas-Nachrichtenschritte, die an mehrere Gerätetypen gesendet werden müssen (z. B. sowohl iOS als auch Android).
- Zeitkritische Push-Benachrichtigungen, die schnell und präzise mehrere Plattformen ansprechen müssen, wobei der Inhalt plattformübergreifend identisch ist (z. B. Eilmeldungen oder Live-Spielupdates).

## Eine Push-Campaign oder ein Canvas für mehrere Plattformen erstellen {#creating-a-multiple-platform-push-campaign-or-canvas}

So erstellen Sie eine Campaign, die mehrere Plattformen und Geräte anspricht:

1. Erstellen Sie eine Campaign oder fügen Sie einem Canvas einen [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hinzu.
2. Wählen Sie **Push-Benachrichtigung** aus.
3. Wählen Sie Ihre gewünschten Plattformen (Mobilgerät, Internet, Kindle) und mobilen Geräte (iOS, Android) aus. Wenn Sie mehrere Geräte auswählen, steht für Ihre Campaign kein multivariates Testen zur Verfügung.

### Plattformen für eine Campaign auswählen {#selecting-platforms-for-a-campaign}
![Optionen zur Auswahl mehrerer Plattformen für eine Push-Campaign, wie Mobilgerät, Internet und Kindle, sowie mehrerer Geräte, wie iOS und Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Plattformen für einen Canvas-Schritt auswählen {#selecting-platforms-for-a-canvas-step}
![Optionen zur Auswahl mehrerer Plattformen für einen Push-Nachrichtenschritt, wie Mobilgerät, Internet und Kindle, sowie mehrerer Geräte, wie iOS und Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. Wählen Sie **Bestätigen**. Nachdem Sie **Bestätigen** ausgewählt haben, können Sie Ihre ausgewählten Plattformen oder Geräte nicht mehr ändern.
5. Fahren Sie mit der Einrichtung Ihrer Campaign oder Ihres Canvas fort.

## Einen Multiplattform-Multivarianten-Test durchführen {#running-a-multi-platform-multivariate-test}

Multivariates Testen wird bei Multiplattform-Campaigns unterstützt. Wählen Sie einfach das Plus-Symbol neben dem Variantennamen aus, wie Sie es normalerweise bei Einzelplattform-Campaigns tun würden. Wir empfehlen Ihnen, [unseren Leitfaden]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) zum Erstellen multivariater Tests zu lesen und die [BrazeAI<sup>TM</sup>-Variantenauswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) zu nutzen, um Ihr Engagement zu automatisieren und zu maximieren.

![Einfache Multiplattform-Multivarianten-Tests]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## Wissenswertes {#things-to-know}

### Einheitliches Messaging {#unified-messaging}
Auf dem Tab **Verfassen** können Sie einen Titel, eine Nachricht und ein Klickverhalten für alle Ihre ausgewählten Plattformen und Geräte festlegen.

Der Vorschaubereich zeigt eine Annäherung daran, wie Ihre Nachricht auf jeder Plattform aussieht. Obwohl er Ihnen einen guten Hinweis darauf geben kann, wo Sie möglicherweise Zeichenlimits erreichen, sollten Sie Ihre Nachrichten immer auf einem echten Gerät testen, bevor Sie Ihre Campaign senden.

![Einzelne Bearbeitungsansicht mit einem Titel-, Nachrichten- und Klickverhaltensfeld für drei Push-Typen: iOS, Android und Internet.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### Separate Assets {#separate-assets}
Im Abschnitt **Assets** wählen oder laden Sie die Bilder hoch, die für jede Plattform angezeigt werden sollen. Beachten Sie, dass verschiedene Geräte unterschiedliche Spezifikationen für Bilder und Zeichenanzahlen haben. Weitere Hilfe finden Sie unter [Push-Nachrichten- und Bildformate]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats).

![Assets-Abschnitt der einzelnen Bearbeitungsansicht mit Feldern für Push-Icon-Bild, iOS-Benachrichtigungsbild, Android-Benachrichtigungsbild und Internet-Benachrichtigungsbild.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### Benachrichtigungstyp {#notification-type}

Der Benachrichtigungstyp ist standardmäßig auf „Standard-Push“ eingestellt und kann nicht geändert werden. Wenn Sie einen anderen Push-Typ erstellen möchten, wie Push Stories oder Inline-Bild (Android), erstellen Sie separate Campaigns für jeden Gerätetyp.

### Gerätespezifische Einstellungen {#device-specific-settings}

Sie können plattformspezifische Einstellungen im Editor bearbeiten. Dazu gehören Einstellungen wie [Push-Action-Buttons]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), Benachrichtigungskanäle und -gruppen, TTL, Anzeigepriorität, Töne und mehr.

Weitere Informationen zu gerätespezifischen Einstellungen finden Sie in den folgenden Artikelsammlungen:

- [iOS-Optionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Android-Optionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push Stories sind multiplattformfähig nur auf Android und iOS verfügbar. Wenn Sie Internet oder Kindle als Sendeplattform auswählen, ist diese Option nicht verfügbar.