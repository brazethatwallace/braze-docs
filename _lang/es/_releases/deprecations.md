---
nav_title: Depreciaciones
article_title: Depreciaciones
page_order: 9
page_type: reference
description: "Esta página incluye referencias a artículos obsoletos y proporciona una lista de características obsoletas y no compatibles."
---

# Depreciaciones {#deprecations}

La tecnología siempre está en movimiento, ¡dentro y fuera de Braze! Y hacemos todo lo posible para estar a la altura. Aquí encontrarás los orígenes de Braze y su tecnología: cómo apoyábamos a la gente en el "antes de los tiempos", es decir, antes de ahora...

Puede que hayas llegado hasta aquí buscando un término para una integración o característica que ya no existe. Este es nuestro intento de mantenerte informado sobre nuestros progresos y movimientos dentro de la industria tecnológica. Puedes encontrar una lista de características obsoletas y no compatibles y leer artículos obsoletos visitando los siguientes enlaces.

## Artículos obsoletos {#deprecated-articles}

- [Devolución de llamada push personalizada del receptor de difusión para Android]({{site.baseurl}}/releases/deprecations/custom_broadcast_receiver/)
- [Configuración del SDK or kit de desarrollo de software de Eclipse]({{site.baseurl}}/releases/deprecations/eclipse_setup_deprecated/)
- [Supresión de TLS 1.0 y 1.1]({{site.baseurl}}/releases/deprecations/tls_deprecation/)
- [Integración de webhook Twilio]({{site.baseurl}}/releases/deprecations/twilio/)
- [Asociación con Apptimize]({{site.baseurl}}/releases/deprecations/apptimize/)
- [Asociación con Grouparoo]({{site.baseurl}}/releases/deprecations/grouparoo/)
- [Supresión de `checkout.liquid` de Shopify]({{site.baseurl}}/releases/deprecations/shopify_checkout/)

## Registro de depreciaciones {#deprecations-log}

### Shopify `checkout.liquid`

**Soporte retirado**: agosto de 2024 (fase 1), agosto de 2025 (fase 2)

El soporte para Shopify `checkout.liquid` comenzará a quedar obsoleto en agosto de 2024 y finalizará en agosto de 2025. Shopify pasará a [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), que es más segura, tiene mayor rendimiento y es más personalizable.

### Receptor personalizado de difusión push para Android {#custom-push-broadcast-receiver-for-android}

**Soporte retirado**: octubre de 2022

El uso de un `BroadcastReceiver` personalizado para las notificaciones push ha quedado obsoleto. Utiliza [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) en su lugar.

### Asociación con Grouparoo {#grouparoo-partnership}

**Soporte retirado**: abril de 2022

La compatibilidad con Grouparoo se interrumpió a partir de abril de 2022.

### SDK or kit de desarrollo de software para Windows de Braze {#braze-windows-sdk}

**24 de marzo de 2022**: El SDK or kit de desarrollo de software de Windows de Braze está obsoleto, y no se pueden crear nuevas aplicaciones de Windows en el panel de Braze.<br>
**15 de septiembre de 2022**: No se pueden enviar mensajes nuevos a las aplicaciones de Windows. Los mensajes existentes y la recopilación de datos no se ven afectados.<br>
**11 de enero de 2024**: Braze ya no servirá mensajes ni recopilará datos de las aplicaciones de Windows.

### Integración push de Baidu {#baidu-push-integration}

**24 de marzo de 2022**: La integración push de Braze con Baidu está obsoleta, y no se pueden crear nuevas aplicaciones Baidu en el panel de Braze. <br>
**15 de septiembre de 2022**: No se pueden crear nuevos mensajes push de Baidu. Los mensajes existentes y la recopilación de datos no se ven afectados.<br>
**11 de enero de 2024**: Braze ya no servirá mensajes ni recopilará datos de las aplicaciones de Baidu.

### Variable global appboyBridge {#appboybridge-global-variable}

**Soporte retirado**: mayo de 2021<br>
**Sustituido por**: `brazeBridge`

La variable global `appboyBridge` queda obsoleta y se sustituye por `brazeBridge`. `appboyBridge` seguirá funcionando para los clientes existentes, pero te recomendamos que migres a `brazeBridge` si utilizas `appboyBridge`.

### Asociación con Amazon Moments {#amazon-moments-partnership}

**Soporte retirado**: junio de 2020

La compatibilidad con Amazon Moments se ha interrumpido a partir de junio de 2020. Amazon Moments se está fusionando con Amazon Advertising y ha dejado obsoletas sus API y nuestra integración.

### Asociación con Factual {#factual-partnership}

**Soporte retirado**: junio de 2020

El soporte para Factual se ha interrumpido a partir de junio de 2020. Factual fue adquirida recientemente por Foursquare y ya no se integra con la plataforma Braze.

### Integración de webhook Twilio {#twilio-webhook-integration}

**Soporte retirado**: enero de 2020

La compatibilidad con la [integración de webhook de Twilio]({{site.baseurl}}/partners/twilio/) se ha interrumpido a partir del 31 de enero de 2020. Si deseas seguir accediendo a los servicios servicio de mensajes cortos con Braze, consulta nuestra [documentación sobre servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/).

### Asociación con Apptimize {#apptimize-partnership}

**Soporte retirado**: agosto de 2019

Si actualmente utilizas [Apptimize con Braze]({{site.baseurl}}/releases/deprecations/apptimize/), no experimentarás una interrupción del servicio. Todavía puedes establecer atributos personalizados de Apptimize en los perfiles de usuario Braze. Sin embargo, no se proporcionará apoyo de escalada formal con el socio.

### Mensajes originales dentro de la aplicación {#original-in-app-messages}

**Soporte retirado:** febrero de 2019<br>
**Sustituido por**: [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

Braze ha mejorado el aspecto de los mensajes dentro de la aplicación para ajustarse a las buenas prácticas de UX y UI y ya no admite los mensajes dentro de la aplicación originales.

Braze pasó a una nueva forma de mensajes dentro de la aplicación con las siguientes versiones del SDK or kit de desarrollo de software:
- iOS: `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

Antes de estas versiones, Braze admitía "mensajes originales dentro de la aplicación". Anteriormente, se ofrecía soporte para mensajes dentro de la aplicación originales a cualquier cliente que hubiera realizado una campaña dentro de la aplicación antes de la nueva versión. Todas las estadísticas de la campaña no se vieron afectadas por el cambio, y quienes habían enviado mensajes originales dentro de la aplicación tuvieron la oportunidad de enviar otros a través del botón **Crear campaña** de la página **Campaign**.

### Widget de comentarios {#feedback-widget}

**Soporte retirado**: 1 de julio de 2019.

El SDK or kit de desarrollo de software de Braze proporcionaba un widget de comentarios que podía añadirse a tu aplicación para permitir a los usuarios dejar comentarios mediante el método `submitfeedback` y pasarlos a Desk.com o Zendesk, y que se gestionaba en el dashboard.

### Google Cloud Messaging (GCM)

**Soporte retirado**: retirada del soporte de Braze: julio de 2018, retirada del soporte por parte de Google: 29 de mayo de 2019<br>
**Sustituido por**: [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Google ha [eliminado la compatibilidad con GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) a partir del 29 de mayo de 2019. Braze ha dejado de ser compatible con GCM desde los SDK or kit de desarrollo de software de Android en julio de 2018, lo que se ha anotado en nuestros [registros de cambios del SDK or kit de desarrollo de software de Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md). Esto significa que los tokens de GCM existentes seguirán funcionando y podrás enviar mensajes a tus usuarios actuales. Sin embargo, no podrás enviar mensajes a nuevos usuarios.

Los clientes que aún no hayan migrado a [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) pueden verse afectados por este cambio.

Si no has pasado a FCM, fallarán todos los registros de tokens de notificaciones push de GCM. Si tus aplicaciones admiten actualmente GCM, tendrás que trabajar con tus equipos de desarrollo en la [transición de GCM a Firebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm).

### Eclipse

**Soporte retirado**: 2014-2015<br>
**Sustituido por**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

Braze ha dejado de ser compatible con el IDE de Eclipse debido a que Google [ha dejado de dar soporte](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) al plugin de Eclipse Android Developer Tools (ADT).

Si necesitas ayuda con tu integración en Eclipse antes de la migración, ponte en contacto con [soporte]({{site.baseurl}}/support_contact/).

### El flujo de eventos en bruto (RES) {#the-raw-event-stream-res}

**Soporte retirado**: julio de 2018<br>
**Sustituido por**: [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)

El flujo de eventos en bruto fue el predecesor de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) y quedó obsoleto para dejar espacio al futuro de los datos de Braze.

### Retraso en reposo - característica de GCM {#delay-while-idle-gcm-feature}

**Soporte retirado**: noviembre de 2016

Antes, el parámetro Delay While Idle formaba parte de las [opciones push de GCM](https://developers.google.com/cloud-messaging/http-server-ref). Google retiró la compatibilidad con esta opción el 15 de noviembre de 2016. Anteriormente, cuando se establecía en **true**, significaba que el mensaje no debía enviarse hasta que el dispositivo se activara.

### Puntos finales personalizados {#custom-endpoints}

**Soporte retirado**: diciembre de 2019

Eliminación de puntos finales personalizados. Si tienes un punto final personalizado, puedes seguir utilizándolo, pero Braze ya no los facilita.