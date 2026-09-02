---
nav_title: Auf iOS 18 upgraden
article_title: Auf iOS 18 upgraden
page_order: 7.1
platform:
  - iOS
description: "Dieser Artikel enthält Insights zum Release von iOS 18, damit Sie Ihr SDK nahtlos upgraden können."
---

# Auf iOS 18 upgraden {#upgrading-to-ios-18}

> Sind Sie neugierig, wie Braze sich auf das kommende iOS-Release vorbereitet? Dieser Artikel fasst unsere Insights zum iOS 18 Release zusammen, um Ihnen und Ihren Nutzer:innen ein nahtloses Erlebnis zu ermöglichen.

Die [WWDC](https://developer.apple.com/wwdc24/) von Apple fand vom 9. bis 11. Juni 2024 statt. Erfahren Sie mehr über die Ankündigungen in unserem [Blogbeitrag](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18) oder lesen Sie weiter, um zu erfahren, wie Sie iOS 18 mit Braze nutzen können.

## Änderungen in iOS 18 {#changes-in-ios-18}

### Live Activities auf der Apple Watch {#live-activities-on-apple-watch}

[Live Activities]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift) werden auf watchOS 11 unterstützt. Es ist keine zusätzliche Einrichtung erforderlich. Apple bietet jedoch die Möglichkeit, die Watch-Oberfläche anzupassen.

### Apple Vision Pro

Die Vision Pro ist jetzt in China, Japan, Singapur, Australien, Kanada, Frankreich, Deutschland und Großbritannien verfügbar. Lesen Sie unseren Blog, um zu erfahren, wie [Braze visionOS unterstützt](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### iPhone-Benachrichtigungen auf macOS {#iphone-notifications-on-macos}

Die neue [iPhone-Spiegelung](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) von Apple ermöglicht es Nutzer:innen, iPhone-Benachrichtigungen auf ihren macOS-Geräten zu empfangen. Beachten Sie, dass einige Medientypen wie Push-Story-Bilder und GIFs nicht unterstützt werden, da sie nicht als macOS-Benachrichtigung dargestellt werden können.

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) ist jetzt für Geräte mit iOS 18.1 und höher verfügbar.

Als Braze-Nutzer:in ist das wichtigste neue Feature, das Sie kennen sollten, die [Benachrichtigungszusammenfassungen](https://support.apple.com/en-us/108781). Diese verwenden geräteinterne Verarbeitung, um verwandte Push-Benachrichtigungen einer einzelnen App automatisch zu gruppieren und Textzusammenfassungen zu erstellen. Endnutzer:innen können auf eine Zusammenfassung tippen, um sie zu erweitern und jede Push-Benachrichtigung in ihrer ursprünglich gesendeten Form anzuzeigen.

Da diese Zusammenfassungen automatisch generiert werden, haben Sie keine Kontrolle über deren spezifisches Verhalten oder den generierten Text. Dies hat jedoch keine Auswirkungen auf Analytics- oder Reporting-Features wie das Push-Klick-Tracking.

![Ein Beispiel-Screenshot einer Vorschau einer Push-Benachrichtigungszusammenfassung.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})