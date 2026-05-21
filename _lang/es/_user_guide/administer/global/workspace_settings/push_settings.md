---
nav_title: Configuración de push
article_title: Configuración de push
page_order: 5
page_type: reference
description: "Este artículo ofrece un resumen de la configuración de push en el panel de Braze."
channel: push

---

# Configuración de push {#push-settings}

> La página de **Configuración de push** te permite configurar los ajustes clave para tus notificaciones push, incluido el tiempo de vida de push (TTL) y la prioridad predeterminada de FCM para Campaigns de Android. Estas configuraciones ayudan a optimizar la entrega y la eficacia de tus notificaciones push, garantizando una mejor experiencia para tus usuarios.

## ¿Qué es el TTL de push? {#what-is-push-ttl}

El TTL para notificación push controla el tiempo que Braze intentará entregar una notificación push a los dispositivos que estén desconectados en el momento en que se envía la campaña. Si un dispositivo vuelve a conectarse después de que expire el TTL, el mensaje no se entregará. Esta configuración no eliminará una notificación si el dispositivo del usuario ya la ha recibido; solo controla el tiempo que el proveedor de push intenta entregar una notificación.

## Configuración predeterminada de los valores de TTL de push {#setting-default-push-ttl-values}

Por defecto, Braze establece el TTL de push al máximo para cada servicio de mensajería push.

| Servicio de mensajería push | TTL máximo |
| --- | --- |
| Web (a través de los servicios FCM o Web Push) | 28 días |
| Firebase Cloud Messaging (FCM) | 28 días |
| Kindle (ADM) | 31 días |
| Huawei (HMS) | 15 días |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración predeterminada de los valores de TTL de push" }

Estas configuraciones se aplican globalmente a todas las campañas push, a menos que se establezca un TTL diferente para un mensaje específico. Para ajustar el TTL de un mensaje, consulta [Configuración avanzada de campaña]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#ttl).

Para establecer un TTL de push predeterminado diferente:

1. Ve a **Settings** > **Manage Settings** > **Push Settings**.
2. Para cada plataforma Android, define un valor predeterminado de tiempo de vida. Puedes establecer incrementos más pequeños, como horas o segundos, para un control más preciso.
3. Selecciona **Save** para aplicar tus cambios.

![Configuración de TTL de push para dispositivos Firebase, Web, Kindle y Huawei.]({% image_buster /assets/img/push_ttl.png %})

## Prioridad predeterminada de FCM para Campaigns de Android {#default-fcm-priority-for-android-campaigns}

Puedes establecer la prioridad predeterminada de Firebase Cloud Messaging (FCM) para todas las campañas push de Android. Esta prioridad determina cómo se entrega la notificación push a los dispositivos de los usuarios.

Las opciones de prioridad de FCM incluyen:

| Prioridad | Descripción | Caso de uso |
| --- | --- | --- |
| Normal | Prioridad de entrega estándar que optimiza el uso de batería | Contenido que no requiere atención inmediata |
| Alta | Los mensajes se envían de inmediato | Notificaciones urgentes que requieren entrega rápida |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prioridad predeterminada de FCM para Campaigns de Android" }

Para establecer la prioridad predeterminada de FCM:

1. Ve a **Settings** > **Manage Settings** > **Push Settings**.
2. En la sección de prioridad de FCM, selecciona "Normal" o "High" como configuración predeterminada.
3. Selecciona **Save** para aplicar tus cambios.

![Configuración de prioridad de entrega de Android.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Esta configuración se aplica globalmente a todas las nuevas campañas push de Android, a menos que se seleccione una prioridad diferente al crear una campaña específica.

{% alert note %}
Si FCM detecta que tu aplicación envía con frecuencia mensajes de alta prioridad que no generan notificaciones visibles para el usuario ni interacción, esos mensajes pueden ser degradados automáticamente a prioridad normal.
{% endalert %}

Para obtener información más detallada sobre los niveles de prioridad de FCM y la degradación de prioridad, consulta [Configuración avanzada de campaña]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#fcm-priority).