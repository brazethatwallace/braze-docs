---
nav_title: Cordova SDK
article_title: Cordova SDK Repository-Leitfaden
page_order: 5
description: "Braze Cordova SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Cordova SDK Repository-Leitfaden {#cordova-sdk-repository-guide}

## Über das Braze Cordova SDK {#about-the-braze-cordova-sdk}

Das Braze Cordova SDK hilft Ihnen, Braze-Messaging, Analytics und Funktionen für Nutzer:innen-Engagement in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze-Nutzer:innen-Handbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwickler:innen-Leitfaden](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Mindestversionsanforderungen {#minimum-version-requirements}

| Braze Plugin | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mindestversionsanforderungen" }

Dieses SDK übernimmt zusätzlich die Anforderungen der zugrunde liegenden nativen Braze SDKs. Bitte beachten Sie auch die verlinkten Anforderungslisten:
* [Android SDK-Anforderungen](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [Swift SDK-Anforderungen](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## SDK installieren {#installing-the-sdk}
{% alert warning %}
Fügen Sie das Braze Cordova SDK ausschließlich mit den `cordova plugin add`-Befehlen unter **SDK installieren** hinzu. Versuchen Sie nicht, es auf andere Weise zu installieren, da dies zu einer Sicherheitslücke führen könnte.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## Beispielanwendung ausführen {#running-the-sample-application}
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk).