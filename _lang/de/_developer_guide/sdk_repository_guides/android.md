---
nav_title: Android SDK
article_title: Leitfaden zum Android SDK-Repository
page_order: 2
description: "Braze Android SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Über das Braze Android SDK {#about-the-braze-android-sdk}

Das Braze Android SDK hilft Ihnen, Braze-Messaging, Analytics und Funktionen zur Nutzer:innen-Interaktion in Ihre Anwendung zu integrieren.

Für den Einstieg stehen Ihnen die folgenden Ressourcen zur Verfügung:

- [Braze-Benutzerhandbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android)

## Schnellstart {#quickstart}

Die folgenden Snippets zeigen die minimale Konfiguration, die erforderlich ist, um das Braze Android SDK zu Ihrer App hinzuzufügen.

``` groovy
// build.gradle

// ...
repositories {
  mavenCentral()
}
// ...
dependencies {
  `implementation 'com.braze:android-sdk-ui:42.3.+'`
  `implementation 'com.braze:android-sdk-location:42.3.+'`
}
// ...
```

``` xml
<!-- res/values/braze.xml -->
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

``` kotlin
Braze.getInstance(context).changeUser("Jane Doe");
```

Weitere Informationen zu erweiterten Integrationsoptionen finden Sie im [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android).

## Versionsunterstützung {#version-support}

{% alert important %}
Das Braze Android SDK deklariert eine `minSdkVersion` von API 21+, wodurch das SDK in Apps kompiliert werden kann, die bereits ab API 21 unterstützt werden. Obwohl das SDK für diese Versionen kompiliert wird, bietet Braze keinen formellen Support für API-Versionen unter 25, und das SDK funktioniert auf Geräten mit diesen Versionen möglicherweise nicht wie vorgesehen.

Wenn Ihre App diese Versionen unterstützt, gehen Sie wie folgt vor:

- Überprüfen Sie, dass Ihre Integration des SDK auf physischen Geräten (nicht nur Emulatoren) für diese API-Versionen wie vorgesehen funktioniert.
- Wenn Sie das erwartete Verhalten nicht validieren können, müssen Sie entweder [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) aufrufen oder die Initialisierung des SDK auf diesen Versionen überspringen. Andernfalls können unbeabsichtigte Nebeneffekte oder eine verschlechterte Performance auf den Geräten Ihrer Nutzer:innen auftreten.
{% endalert %}
Die folgende Tabelle listet die minimal unterstützten Versionen für Tools auf, die vom Braze Android SDK verwendet werden.

Tool | Minimal unterstützte Version
:----|:----
minSdk|5.0+ / API 21+ (Lollipop und höher)
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|24.1.2
Font Awesome|4.3.0

## Module {#modules}

Die folgende Tabelle beschreibt jedes Modul im Braze Android SDK.

Modul | Beschreibung
:----|:----
`android-sdk-base`|Die Braze SDK Basis-Analytics-Bibliothek.
`android-sdk-ui`|Die Braze SDK Benutzeroberflächen-Bibliothek für In-App-Nachrichten, Push, Content Cards und Banner.
`android-sdk-location`|Die Braze SDK Standort-Bibliothek für Standort und Geofences.
`android-sdk-jetpack-compose`|Die Braze SDK Bibliothek für Jetpack Compose-Unterstützung.
`droidboy`|Eine Beispiel-App, die zeigt, wie Sie Braze umfassend nutzen können.
`android-sdk-unity`|Eine Bibliothek, die Braze SDK-Integrationen auf Unity ermöglicht.
`samples`|Ein Ordner mit Beispiel-Apps für verschiedene Integrationsoptionen.

## Kontakt {#contact}

Bei Fragen kontaktieren Sie den technischen Support von Braze.
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk).