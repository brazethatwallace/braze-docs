---
nav_title: Android SDK
article_title: Guía del repositorio del Android SDK
page_order: 2
description: "Referencia del README del Android SDK de Braze reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Acerca del Android SDK de Braze {#about-the-braze-android-sdk}

El Android SDK de Braze te ayuda a integrar las capacidades de mensajería, análisis e interacción con el usuario de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)

## Inicio rápido {#quickstart}

Los siguientes fragmentos de código muestran la configuración mínima necesaria para añadir el Android SDK de Braze a tu aplicación.

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

Para más información sobre opciones de integración avanzadas, consulta la [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

## Compatibilidad de versiones {#version-support}

{% alert important %}
El Android SDK de Braze declara un `minSdkVersion` de API 21+, lo que permite que el SDK se compile en aplicaciones compatibles desde la API 21. Aunque el SDK se compila para esas versiones, Braze no ofrece soporte formal para versiones de API inferiores a la 25, y es posible que el SDK no funcione como se espera en dispositivos que ejecuten esas versiones.

Si tu aplicación es compatible con esas versiones, haz lo siguiente:

- Valida que tu integración del SDK funcione como se espera en dispositivos físicos (no solo en emuladores) para esas versiones de API.
- Si no puedes validar el comportamiento esperado, debes llamar a [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) u omitir la inicialización del SDK en esas versiones. De lo contrario, podrías causar efectos secundarios no deseados o un rendimiento degradado en los dispositivos de tus usuarios.
{% endalert %}
La siguiente tabla enumera las versiones mínimas compatibles de las herramientas utilizadas por el Android SDK de Braze.

Herramienta | Versión mínima compatible
:----|:----
minSdk|5.0+ / API 21+ (Lollipop y superior)
targetSdk|37
Kotlin|`org.jetbrains.kotlin:kotlin-stdlib:2.2.20`
Firebase Cloud Messaging|24.1.2
Font Awesome|4.3.0

## Módulos {#modules}

La siguiente tabla describe cada módulo del Android SDK de Braze.

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

Si tienes preguntas, ponte en contacto con el soporte técnico de Braze.
<!-- END GENERATED README CONTENT -->

Para detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk).