---
nav_title: Cordova SDK
article_title: Cordova SDK Repository-Leitfaden
page_order: 5
description: "Braze Cordova SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Cordova SDK Repository-Leitfaden {#cordova-sdk-repository-guide}

## Über das Braze Cordova SDK {#about-the-braze-cordova-sdk}

Das Braze Cordova SDK hilft Ihnen dabei, Braze-Messaging, Analytics und Nutzer:innen-Engagement-Funktionen in Ihre App zu integrieren.

Nutzen Sie die folgenden Ressourcen für den Einstieg:

- [Braze-Benutzerhandbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Mindestanforderungen an die Version {#minimum-version-requirements}

Die folgende Tabelle zeigt die unterstützten Mindestversionen für das Braze Cordova SDK.

| Braze-Plugin | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mindestanforderungen an die Version" }

Dieses SDK übernimmt außerdem die Anforderungen der zugrunde liegenden nativen Braze SDKs. Beachten Sie auch die Informationen zur Versionsunterstützung in [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) und [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).

## SDK installieren {#installing-the-sdk}

{% alert important %}
Fügen Sie das Braze Cordova SDK nur mit den folgenden Methoden hinzu. Die Verwendung anderer Methoden kann Sicherheitsrisiken mit sich bringen.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## Ausführen der Beispielanwendung {#running-the-sample-application}
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

Details zum Repository und Beispielprojekte finden Sie unter [https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk).