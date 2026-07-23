---
nav_title: Notificaciones push
article_title: Registrar datos de notificaciones push a través del SDK de Braze
page_order: 7.2
description: "Aprende a registrar datos de notificaciones push a través del SDK de Braze."
noindex: true
---

# Registrar datos de notificaciones push {#log-push-notification-data}

> Aprende a registrar datos de notificaciones push a través del SDK de Braze.

{% sdktabs %}
{% sdktab android %}
## Registrar datos con la API de Braze (recomendado) {#logging-data-with-the-braze-api-recommended}

Puedes registrar análisis en tiempo real haciendo llamadas al [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Para registrar análisis, envía el valor `braze_id` desde el panel de Braze para identificar qué perfil de usuario actualizar.

![Ejemplo de panel de push personalizado]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Registrar datos manualmente {#manually-logging-data}

Dependiendo de los detalles de tu carga útil, puedes registrar análisis manualmente dentro de tu implementación de `FirebaseMessagingService.onMessageReceived` o de tu actividad de inicio. Tu subclase de `FirebaseMessagingService` debe finalizar la ejecución en un plazo de 9 segundos desde la invocación para evitar ser [marcada o terminada](https://firebase.google.com/docs/cloud-messaging/android/receive) por el sistema Android.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}