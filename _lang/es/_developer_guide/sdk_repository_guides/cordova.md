---
nav_title: SDK or kit de desarrollo de software de Cordova
article_title: Guía del repositorio del SDK or kit de desarrollo de software de Cordova
page_order: 5
description: "Referencia del README del SDK or kit de desarrollo de software de Braze para Cordova reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del SDK or kit de desarrollo de software de Cordova {#cordova-sdk-repository-guide}

## Acerca del SDK or kit de desarrollo de software de Braze para Cordova {#about-the-braze-cordova-sdk}

El SDK or kit de desarrollo de software de Braze para Cordova te ayuda a integrar las funcionalidades de mensajería, análisis y participación de usuarios de Braze en tu aplicación.

Para empezar, consulta los siguientes recursos:

- [Guía del usuario de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Requisitos mínimos de versión {#minimum-version-requirements}

| Plugin de Braze | Cordova Android | Cordova iOS |
| --------------- | --------------- | ----------- |
| 10.0.0+         | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+         | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos mínimos de versión" }

Este SDK or kit de desarrollo de software también hereda los requisitos de los SDK or kit de desarrollo de software nativos de Braze subyacentes. Asegúrate de cumplir también con las listas de requisitos de los SDK or kit de desarrollo de software de Android y Swift enlazadas:
* [Requisitos del SDK or kit de desarrollo de software de Android](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
* [Requisitos del SDK or kit de desarrollo de software de Swift](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

## Instalación del SDK or kit de desarrollo de software {#installing-the-sdk}
{% alert warning %}
Añade el SDK or kit de desarrollo de software de Braze para Cordova únicamente mediante los métodos que se indican a continuación. No intentes instalarlo mediante otros métodos, ya que podría provocar una brecha de seguridad.
{% endalert %}
``` text
# To use the base SDK functionality, install using the `master` branch.

cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To use location collection and geofences in addition to the base SDK functionality, install using `geofence-branch`.
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```

## Ejecución de la aplicación de ejemplo {#running-the-sample-application}
``` text
cordova plugin remove cordova-plugin-braze
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master

# To run android
cordova run android

# To run iOS
cordova run ios
```
<!-- END GENERATED README CONTENT -->

Para obtener detalles del repositorio y proyectos de ejemplo, consulta [https://github.com/braze-inc/braze-cordova-sdk](https://github.com/braze-inc/braze-cordova-sdk).