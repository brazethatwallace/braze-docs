---
nav_title: Visionos-Unterstützung
article_title: Visionos-Unterstützung
page_order: 7.2
platform:
  - iOS
description: "Dieser Artikel behandelt die Features, die von visionOS unterstützt werden."
---

# visionOS-Unterstützung {#visionos-support}

> Ab [Braze Swift SDK or Software-Development-Kit 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800) können Sie Braze mit [visionOS](https://developer.apple.com/visionos/) nutzen, Apples Spatial-Computing-Plattform für den Apple Vision Pro. Ein Beispiel für eine visionOS-App, die Braze verwendet, finden Sie unter [Beispiel-Apps]({{site.baseurl}}/developer_guide/references?tab=swift).

## Vollständig unterstützte Features {#fully-supported-features}

Die meisten Features, die unter iOS verfügbar sind, stehen auch unter visionOS zur Verfügung, darunter:

- Analytics (Sitzungen, angepasste Events, Käufe etc.)
- In-App Messaging (Datenmodelle und UI)
- Content Cards (Datenmodelle und UI)
- Push-Benachrichtigungen (für Nutzer:innen sichtbar mit Aktions-Buttons und stillen Benachrichtigungen)
- Feature-Flags
- Standort-Analytics

## Teilweise unterstützte Features {#partially-supported-features}

Einige Features werden von visionOS nur teilweise unterstützt, aber Apple wird diese wahrscheinlich in Zukunft adressieren:

- Rich-Push-Benachrichtigungen
  - Bilder werden unterstützt.
  - GIFs und Videos zeigen die Vorschau-Miniaturansicht an, können aber nicht abgespielt werden.
  - Die Audiowiedergabe wird nicht unterstützt.
- Push Stories
  - Das Blättern und Auswählen der Push-Story-Seite wird unterstützt.
  - Das Navigieren zwischen Push-Story-Seiten mit **Next** wird nicht unterstützt.

## Nicht unterstützte Features {#unsupported-features}

- Geofence-Monitoring wird nicht unterstützt. Apple hat die Core-Location-APIs für die Regionsüberwachung unter visionOS nicht zur Verfügung gestellt.
- Live Activities werden nicht unterstützt. Derzeit ist ActivityKit nur auf iOS und iPadOS verfügbar.