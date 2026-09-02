---
nav_title: Anleitung zum Upgrade or upgraden für iOS 17
article_title: Anleitung zum Upgrade or upgraden für iOS 17
page_order: 7
platform:
  - iOS
description: "Dieser Artikel enthält Insights zum Release von iOS 17, damit Sie Ihr SDK or Software-Development-Kit nahtlos upgraden können."
hidden: true
noindex: true
---

# Anleitung zum Upgrade or upgraden für iOS 17 {#ios-17-upgrade-guide}

> Sind Sie neugierig, wie Braze sich auf das kommende iOS-Release vorbereitet? Dieser Artikel fasst unsere Insights zum iOS 17 Release zusammen, um Ihnen und Ihren Nutzer:innen ein nahtloses Erlebnis zu ermöglichen.

## Kompatibilität mit iOS 17 und Xcode 15 {#ios-17-and-xcode-15-compatibility}

Das Braze Swift SDK or Software-Development-Kit und das Objective-C SDK or Software-Development-Kit sind beide rückwärtskompatibel mit Xcode 14 und Xcode 15 sowie mit iOS 17-Geräten.

## Änderungen in iOS 17 {#changes-in-ios-17}

### Link-Tracking und UTM-Parameter-Stripping {#link-tracking-and-utm-parameter-stripping}

Eine der wichtigsten Änderungen in iOS 17 ist das Blockieren von UTM-Parametern in Safari. UTM-Parameter sind Code-Abschnitte, die zu URLs hinzugefügt werden. Sie werden häufig in Marketingkampagnen verwendet, um die Effektivität von E-Mail, Kurzmitteilungsdienst or SMS und anderen Messaging-Kanälen zu messen.

Diese Änderung wirkt sich nicht auf das Braze E-Mail-Klick-Tracking und Kurzmitteilungsdienst or SMS-Linkverkürzungen aus.

### App-Tracking-Transparenz {#app-tracking-transparency}

Apple kündigte an, den Anwendungsbereich von [Ad Tracking Transparency (ATT)](https://support.apple.com/en-us/HT212025) zu erweitern, mit dem Nutzer:innen kontrollieren können, ob eine App auf ihre Aktivitäten auf Apps und Websites anderer Unternehmen zugreifen kann. Das iOS 17 Release enthält zwei wichtige ATT-Features: Datenschutzmanifeste und Code Signing.

#### Datenschutzmanifeste {#privacy-manifests}

Apple verlangt jetzt eine Datenschutzmanifest-Datei, die den Grund für die Datenerfassung durch Ihre App und SDKs von Drittanbietern sowie deren Methoden zur Datenerfassung beschreibt. Ab iOS 17.2 blockiert Apple alle deklarierten Tracking-Endpunkte in Ihrer App, bis die Endnutzer:innen die ATT-Aufforderung akzeptieren.

Braze hat ein eigenes Datenschutzmanifest veröffentlicht, zusammen mit neuen flexiblen APIs, die deklarierte Tracking-Daten automatisch an spezielle `-tracking`-Endpunkte umleiten. Weitere Informationen finden Sie im [Datenschutzmanifest von Braze]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest).

#### Code Signing {#code-signing}

Code Signing erlaubt es Entwickler:innen, die ein SDK or Software-Development-Kit eines Drittanbieters in ihrer Anwendung verwenden, zu überprüfen, ob derselbe Entwickler bzw. dieselbe Entwicklerin es signiert hat wie frühere Versionen in Xcode.

### Braze SDK or Software-Development-Kit und Datenschutz {#braze-sdk-and-privacy}

Apple hat außerdem angekündigt, Ende 2023 eine Liste der SDKs von Drittanbietern zu veröffentlichen, die als „datenschutzrelevant“ gelten. Es wird erwartet, dass diese SDKs nach Einschätzung von Apple einen besonders großen Einfluss auf die Privatsphäre der Nutzer:innen haben.

Anders als herkömmliche Tracking-SDKs, die darauf ausgelegt sind, Nutzer:innen über mehrere Websites und Anwendungen hinweg zu überwachen, konzentriert sich das Braze SDK or Software-Development-Kit auf First-Party-Daten-Messaging und Nutzererlebnisse.

Wir gehen zwar nicht davon aus, dass das Braze SDK or Software-Development-Kit in diese Liste aufgenommen wird, aber wir werden die Situation genau beobachten und gegebenenfalls Updates veröffentlichen.