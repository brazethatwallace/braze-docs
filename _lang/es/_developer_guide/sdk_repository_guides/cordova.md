---
nav_title: SDK de Cordova
article_title: Guía del repositorio del SDK de Cordova
page_order: 5
description: "Referencia del README del SDK de Braze para Cordova reflejada desde GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guía del repositorio del SDK de Cordova {#cordova-sdk-repository-guide}

## Acerca del SDK de Braze para Cordova {#about-the-braze-cordova-sdk}

El SDK de Braze para Cordova te ayuda a integrar las funciones de mensajería, análisis y participación de usuarios de Braze en tu aplicación.

Para comenzar, consulta los siguientes recursos:

- [Guía del usuario de Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guía del desarrollador de Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova)

## Requisitos mínimos de versión {#minimum-version-requirements}

La siguiente tabla enumera las versiones mínimas compatibles con el SDK de Braze para Cordova.

| Complemento Braze | Cordova Android | Cordova iOS |
| ------------------ | --------------- | ----------- |
| 10.0.0+            | >= 13.0.0       | >= 5.0.0    |
| 2.31.0+            | >= 12.0.0       | >= 5.0.0    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Requisitos mínimos de versión" }

Este SDK también hereda los requisitos de los SDK nativos de Braze subyacentes. Asegúrate de cumplir también con la información de compatibilidad de versiones definida en [braze-inc/braze-android-sdk](https://github.com/braze-inc/braze-android-sdk) y [braze-inc/braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk).

## Instalación del SDK {#installing-the-sdk}

{% alert important %}
Añade el SDK de Braze para Cordova utilizando únicamente los siguientes métodos. El uso de otros métodos puede introducir riesgos de seguridad.
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