---
nav_title: Swift SDK
article_title: Leitfaden zum Swift-SDK-Repository
page_order: 3
description: "Braze Swift SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Über das Braze Swift SDK {#about-the-braze-swift-sdk}

Das Braze Swift SDK hilft Ihnen, Braze-Messaging, Analytics und Funktionen zum Nutzer:innen-Engagement in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze-Benutzerhandbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwicklerleitfaden](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift)

## Schnellstart {#quickstart}

Die folgenden Snippets zeigen die Mindestkonfiguration, die erforderlich ist, um das Braze Swift SDK zu Ihrer App hinzuzufügen.

``` swift
// AppDelegate.swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  // ...
  static var braze: Braze? = nil

  // ...
   func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // ...
        let configuration = Braze.Configuration(
            apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
            endpoint: "YOUR-BRAZE-ENDPOINT"
        )
        let braze = Braze(configuration: configuration)

        AppDelegate.braze = braze
        // ...
    }
}
```

``` swift
AppDelegate.braze?.changeUser(userId: "Jane Doe")
```

Weitere Informationen zu erweiterten Integrationsoptionen finden Sie im [Braze-Entwicklerleitfaden](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift).

## Versionsunterstützung {#version-support}

Die folgende Tabelle listet die mindestens unterstützten Versionen für Tools auf, die vom Braze Swift SDK verwendet werden.

Tool | Mindestens unterstützte Version
:----|:----
iOS|12.0+
Mac Catalyst|16.0+
tvOS|12.0+
visionOS|1.0+
Xcode|26.0+ (17A324)

## Paketmanager {#package-managers}
- Swift-Paketmanager
- CocoaPods

## Bibliotheken {#libraries}

Die folgende Tabelle beschreibt jede Bibliothek im Braze Swift SDK.

<!-- Table generated with https://www.tablesgenerator.com/markdown_tables -->

|                                                                                                                                                    | iOS |     tvOS      | macCatalyst |   visionOS    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|:---:|:-------------:|:-----------:|:-------------:|
| **BrazeKit**<br/> _Haupt-SDK-Bibliothek mit Unterstützung für [Analytics] und [Push-Benachrichtigungen]._                                          |  ✅  | ✅<sup>1</sup> |      ✅      |       ✅       |
| **BrazeUI**<br/> _Von Braze bereitgestellte UI-Bibliothek für [In-App Messages] und [Content Cards]._                                              |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazeLocation**<br/> _Standort-Bibliothek mit Unterstützung für [Standort-Analytics und Geofence-Überwachung]._                                  |  ✅  | ✅<sup>2</sup> |      ✅      | ✅<sup>2</sup> |
| **BrazeNotificationService**<br/> _Notification-Service-Extension-Bibliothek mit Unterstützung für [Rich-Push-Benachrichtigungen]._                |  ✅  |      n/a      |      ✅      |       ✅       |
| **BrazePushStory**<br/> _Notification-Content-Extension-Bibliothek mit Unterstützung für [Push Stories]._                                          |  ✅  |      n/a      |      ✅      |       ✅       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Bibliotheken" }

<sup>1</sup> _Push-Benachrichtigungen werden auf tvOS nicht unterstützt_<br/>
<sup>2</sup> _Geofence-Überwachung wird auf tvOS und visionOS nicht unterstützt_

[Analytics]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/
[Push-Benachrichtigungen]: https://www.braze.com/docs/user_guide/message_building_by_channel/push
[In-App Messages]: https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages
[Content Cards]: https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards
[Standort-Analytics und Geofence-Überwachung]: https://www.braze.com/docs/user_guide/engagement_tools/locations_and_geofences
[Rich-Push-Benachrichtigungen]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/ios/rich_notifications/
[Push Stories]: https://www.braze.com/docs/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/

## Beispiele {#examples}

Erkunden Sie unser [Beispielprojekt](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples), das die Integration mehrerer Features veranschaulicht.

## Alternative Repositories {#alternative-repositories}

| Variante                              |                                     Repository | GH Issues, SDK-Info |
|---------------------------------------|-----------------------------------------------:|--------------------:|
| → **Sources und statische XCFrameworks** |                    [braze-inc/braze-swift-sdk] |                   ✓ |
| Statische XCFrameworks                |    [braze-inc/braze-swift-sdk-prebuilt-static] |                   ✗ |
| Dynamische XCFrameworks               |   [braze-inc/braze-swift-sdk-prebuilt-dynamic] |                   ✗ |
| Mergeable XCFrameworks (Early Access) | [braze-inc/braze-swift-sdk-prebuilt-mergeable] |                   ✗ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Alternative Repositories" }

## Kontakt {#contact}

Bei Fragen wenden Sie sich bitte an den technischen Support von Braze.

[braze-inc/braze-swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
[braze-inc/braze-swift-sdk-prebuilt-static]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-static
[braze-inc/braze-swift-sdk-prebuilt-dynamic]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic
[braze-inc/braze-swift-sdk-prebuilt-mergeable]: https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable
<!-- END GENERATED README CONTENT -->

Details zum Repository und Beispielprojekte finden Sie unter [https://github.com/braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).