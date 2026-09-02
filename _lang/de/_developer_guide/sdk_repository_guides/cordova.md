---
nav_title: Cordova SDK or Software-Development-Kit
article_title: Cordova SDK or Software-Development-Kit Repository-Leitfaden
page_order: 5
description: "Braze Cordova SDK or Software-Development-Kit README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Cordova SDK or Software-Development-Kit Repository-Leitfaden {#cordova-sdk-repository-guide}

## Über das Braze Cordova SDK or Software-Development-Kit {#about-the-braze-cordova-sdk}

Das Braze Cordova SDK or Software-Development-Kit hilft Ihnen, Braze Messaging, Analytics und Nutzer:innen-Engagement-Funktionen in Ihre App zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze User Guide](https://www.braze.com/docs/user_guide/introduction/)
- [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Mindestanforderungen an die Version {#minimum-version-requirements}

| Braze Plugin | Cordova Android | Cordova iOS |
| ------------ | --------------- | ----------- |
| 10.0.0+      | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+      | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mindestanforderungen an die Version" }

Dieses SDK or Software-Development-Kit übernimmt zusätzlich die Anforderungen der zugrunde liegenden nativen Braze SDKs. Achten Sie darauf, auch die verlinkten Anforderungslisten für das Android und Swift SDK or Software-Development-Kit zu berücksichtigen:
* [Anforderungen des Android SDK or Software-Development-Kit](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [Anforderungen des Swift SDK or Software-Development-Kit](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## SDK or Software-Development-Kit installieren {#installing-the-sdk}
{% alert warning %}
Fügen Sie das Braze Cordova SDK or Software-Development-Kit nur mit den unten beschriebenen Methoden hinzu. Versuchen Sie nicht, es mit anderen Methoden zu installieren, da dies zu einer Sicherheitslücke führen könnte.
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