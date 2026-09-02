---
nav_title: Android SDK or Software-Development-Kit
article_title: Leitfaden zum Android SDK or Software-Development-Kit-Repository
page_order: 2
description: "Braze Android SDK or Software-Development-Kit README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Leitfaden zum Android SDK or Software-Development-Kit-Repository {#android-sdk-repository-guide}

## Über das Braze Android SDK or Software-Development-Kit {#about-the-braze-android-sdk}

Das Braze Android SDK or Software-Development-Kit hilft Ihnen, Braze Messaging-, Analytics- und Nutzer:innen-Engagement-Funktionen in Ihre Anwendung zu integrieren.

Für den Einstieg können Sie die folgenden Ressourcen nutzen:

- [Braze-Benutzerhandbuch](https://www.braze.com/docs/user_guide/introduction/)
- [Braze-Entwicklerhandbuch](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android)

## Schnellstart {#quickstart}

Die folgenden Snippets zeigen die minimale Konfiguration, die erforderlich ist, um das Braze Android SDK or Software-Development-Kit zu Ihrer App hinzuzufügen.

``` groovy
// build.gradle

// ...
repositories {
  mavenCentral()
}
// ...
dependencies {
  `implementation 'com.braze:android-sdk-ui:43.1.+'`
  `implementation 'com.braze:android-sdk-location:43.1.+'`
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

Weitere Informationen zu erweiterten Integrationsoptionen finden Sie im [Braze Developer Guide](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android).

## Versionsunterstützung {#version-support}

{% alert important %}
Das Braze Android SDK or Software-Development-Kit deklariert eine `minSdkVersion` von API 21+, wodurch das SDK or Software-Development-Kit in Apps kompiliert werden kann, die ab API 21 unterstützt werden. Obwohl das SDK or Software-Development-Kit für diese Versionen kompiliert wird, bietet Braze keine formale Unterstützung für API-Versionen unter 25, und das SDK or Software-Development-Kit funktioniert auf Geräten mit diesen Versionen möglicherweise nicht wie vorgesehen.

Wenn Ihre App diese Versionen unterstützt, gehen Sie wie folgt vor:

- Überprüfen Sie, dass Ihre Integration des SDK or Software-Development-Kit auf physischen Geräten (nicht nur Emulatoren) für diese API-Versionen wie vorgesehen funktioniert.
- Wenn Sie das erwartete Verhalten nicht validieren können, müssen Sie entweder [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) aufrufen oder die Initialisierung des SDK or Software-Development-Kit auf diesen Versionen überspringen. Andernfalls können unbeabsichtigte Nebeneffekte oder eine verschlechterte Performance auf den Geräten Ihrer Nutzer:innen auftreten.
{% endalert %}
Die folgende Tabelle listet die minimal unterstützten Versionen für Tools auf, die vom Braze Android SDK or Software-Development-Kit verwendet werden.

Tool | Minimal unterstützte Version
:----|:----
minSdk|5.0+ / API 21+ (Lollipop und höher)
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|25.1.1
Font Awesome|4.3.0

## Module {#modules}

Die folgende Tabelle beschreibt jedes Modul im Braze Android SDK or Software-Development-Kit.

Modul | Beschreibung
:----|:----
`android-sdk-base`|Die Braze SDK or Software-Development-Kit Basis-Analytics-Bibliothek.
`android-sdk-ui`|Die Braze SDK or Software-Development-Kit Benutzeroberflächen-Bibliothek für In-App Messages, Push, Content Cards und Banner.
`android-sdk-location`|Die Braze SDK or Software-Development-Kit Standort-Bibliothek für Standorte und Geofences.
`android-sdk-jetpack-compose`|Die Braze SDK or Software-Development-Kit Bibliothek für Jetpack Compose-Unterstützung.
`droidboy`|Eine Beispiel-App, die zeigt, wie Sie Braze im Detail nutzen können.
`android-sdk-unity`|Eine Bibliothek, die Braze SDK or Software-Development-Kit-Integrationen auf Unity ermöglicht.
`samples`|Ein Ordner mit Beispiel-Apps für verschiedene Integrationsoptionen.

## Kontakt {#contact}

Bei Fragen wenden Sie sich an den technischen Support von Braze.
<!-- END GENERATED README CONTENT -->

Informationen zum Repository und Beispielprojekte finden Sie unter [https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk).