---
nav_title: Android SDK
article_title: Guía del repositorio del Android SDK
page_order: 2
description: "Referencia del README del Android SDK de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del Android SDK {#android-sdk-repository-guide}

## Acerca de Braze Android SDK {#about-the-braze-android-sdk}

Braze Android SDK te ayuda a integrar las capacidades de mensajería, análisis y participación de usuarios de Braze en tu aplicación.

Para comenzar, consulta los siguientes recursos:

- [Guía del usuario de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android)

## Inicio rápido {#quickstart}

Los siguientes fragmentos de código muestran la configuración mínima necesaria para añadir el SDK de Braze para Android a tu aplicación.

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

Para obtener más información sobre las opciones de integración avanzada, consulta la [Guía para desarrolladores de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android).

## Compatibilidad de versiones {#version-support}

{% alert important %}
El SDK de Android de Braze declara un `minSdkVersion` de API 21+, lo que permite que el SDK se compile en aplicaciones que admiten desde la API 21. Aunque el SDK se compila para esas versiones, Braze no ofrece soporte formal para versiones de API inferiores a 25, y el SDK puede no funcionar como se espera en dispositivos que ejecuten esas versiones.

Si tu aplicación admite esas versiones, haz lo siguiente:

- Valida que tu integración del SDK funcione como se espera en dispositivos físicos (no solo en emuladores) para esas versiones de API.
- Si no puedes validar el comportamiento esperado, debes llamar a [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) o bien omitir la inicialización del SDK en esas versiones. De lo contrario, podrías provocar efectos secundarios no deseados o un rendimiento degradado en los dispositivos de tus usuarios.
{% endalert %}
La siguiente tabla enumera las versiones mínimas compatibles con las herramientas utilizadas por el SDK de Android de Braze.

Herramienta | Versión mínima compatible
:----|:----
minSdk|5.0+ / API 21+ (Lollipop y superior)
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|25.1.1
Font Awesome|4.3.0

## Módulos {#modules}

La siguiente tabla describe cada módulo del SDK de Braze para Android.

Módulo | Descripción
:----|:----
`android-sdk-base`|La biblioteca base de análisis del SDK de Braze.
`android-sdk-ui`|La biblioteca de interfaz de usuario del SDK de Braze para mensajes dentro de la aplicación, push, Content Cards y banners.
`android-sdk-location`|La biblioteca de ubicación del SDK de Braze para ubicación y geovallas.
`android-sdk-jetpack-compose`|La biblioteca del SDK de Braze para compatibilidad con Jetpack Compose.
`droidboy`|Una aplicación de ejemplo que demuestra cómo usar Braze en profundidad.
`android-sdk-unity`|Una biblioteca que habilita integraciones del SDK de Braze en Unity.
`samples`|Una carpeta que contiene aplicaciones de ejemplo para diversas opciones de integración.

## Contacto {#contact}

Si tienes preguntas, contacta con soporte técnico de Braze.
<!-- END GENERATED README CONTENT -->

Para más detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk).