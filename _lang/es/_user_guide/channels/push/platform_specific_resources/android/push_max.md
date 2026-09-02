---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Max amplifica las notificaciones push de Android rastreando las notificaciones push fallidas y reenviando el push cuando es más probable que el usuario lo reciba."

permalink: /user_guide/channels/push/platform_specific_resources/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Aprende sobre Push Max y cómo puedes usar esta característica para mejorar potencialmente la capacidad de entrega de las notificaciones push de Android en [dispositivos OEM chinos]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability).

## ¿Qué es Push Max? {#what-is-push-max}

Push Max amplifica las notificaciones push de Android rastreando las notificaciones push fallidas y reenviando el push cuando es más probable que el usuario lo reciba.

Algunos dispositivos Android fabricados por fabricantes de equipos originales (OEM) chinos, como Xiaomi, OPPO y Vivo, emplean un esquema robusto de optimización de batería para prolongar la vida útil de la batería. Este comportamiento puede tener la consecuencia no deseada de cerrar el procesamiento de aplicaciones en segundo plano, lo que reduce la capacidad de entrega de las notificaciones push en estos dispositivos si la aplicación no está en primer plano. Esta circunstancia ocurre con mayor frecuencia en los mercados de Asia-Pacífico (APAC).

## Disponibilidad {#availability}

- Disponible solo para notificaciones push de Android
- No es compatible con mensajes basados en acciones o desencadenados por API
- No es compatible cuando se selecciona la opción de [enviar solo al último dispositivo utilizado por el usuario]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#most-recently-used-device)

## Requisitos previos {#prerequisites}

Las notificaciones push enviadas con Push Max solo se entregarán a dispositivos que tengan al menos la siguiente [versión mínima del SDK]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions):

{% sdk_min_versions android:29.0.1 %}

## Uso de Push Max {#using-push-max}

{% tabs %}
{% tab Campaigns %}

Para usar Push Max en tu campaña:

1. Crea una campaña push.
2. Selecciona **Android Push** como tu plataforma.
3. Ve al paso **Schedule Delivery**.
4. Selecciona **Send using Push Max**.

![Sección de capacidad de entrega de push de Android del paso Schedule Delivery con la opción "Send using Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

Para usar Push Max en tu Canvas:

1. Añade un paso de mensaje a tu Canvas.
2. Selecciona **Android Push** como tu plataforma.
3. Ve a la pestaña **Delivery Settings**.
4. Selecciona **Send using Push Max**.

![Pestaña Delivery Settings de un paso de mensaje de push de Android con la opción "Send using Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

Las dos características siguientes, sincronización inteligente y TTL, se pueden usar junto con Push Max para mejorar potencialmente la capacidad de entrega de tus notificaciones push de Android.

### Sincronización inteligente {#intelligent-timing}

Push Max funciona mejor cuando la [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) está activada. La sincronización inteligente puede calcular y enviar la notificación push en el momento en que es más probable que el usuario esté usando la aplicación y que el push se entregue.

### TTL (TTL) {#time-to-live-ttl}

El TTL (TTL) puede rastrear las notificaciones push fallidas a Firebase Cloud Messaging (FCM) y reintentar la notificación cuando es probable que el usuario la reciba.

De forma predeterminada, el TTL está configurado en 28 días, que es el máximo. Puedes reducir el TTL predeterminado para todos los nuevos mensajes push de Android desde **Configuración** > **Configuración del espacio de trabajo** > **Configuración de push**, o puedes configurar el número de días por mensaje en la pestaña **Settings** al redactar una notificación push de Android.

![Campo de TTL configurado en 28 días.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## Cosas que debes saber {#things-to-know}

### Códigos promocionales {#promotion-codes}

Recomendamos que no uses los [códigos promocionales]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) de Braze en mensajes donde Push Max esté activado.

Esto se debe a que los códigos promocionales son únicos. Si una notificación push que contiene un código promocional no se entrega, cuando esa notificación se reenvíe debido a Push Max, se enviará un nuevo código promocional. Esto puede hacer que consumas códigos promocionales más rápido de lo esperado.

### Propiedades del evento y propiedades de entrada de Canvas {#canvas-event-properties-and-entry-properties}

Es posible que Push Max no funcione como se espera si incluyes referencias Liquid a [propiedades de entrada de Canvas o propiedades del evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) en tu mensaje. Esto se debe a que las propiedades de entrada y del evento no están disponibles cuando Push Max intenta reenviar el mensaje.