---
nav_title: "Formatos de mensajes e imágenes"
article_title: "Formatos de mensajes e imágenes"
page_order: 1
page_type: reference
description: "Este artículo describe los formatos de mensajes e imágenes para las notificaciones push."
channel: push

---

# Formatos de mensajes e imágenes push {#push-message-and-image-formats}

> Este artículo de referencia describe los formatos de mensajes e imágenes para las notificaciones push.

Para obtener los mejores resultados, consulta las siguientes directrices sobre tamaño de imagen y longitud de mensaje al crear tus mensajes push. Puede haber cierta variación dependiendo de la presencia de una imagen, el estado de la notificación (iOS) y la configuración de visualización del dispositivo del usuario, así como del tamaño del dispositivo. En caso de duda, mantén tu texto breve y conciso.

## Push en iOS y Android {#ios-and-android-push}

{% tabs local %}
{% tab Imágenes %}

**Tipo de imagen** | **Tamaño de imagen recomendado** | **Tamaño máximo de imagen** | **Tipos de archivo**
--- | --- | --- | ---
(iOS) 2:1 *Recomendado* | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG, GIF
(Android) Icono push | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
(Android) Notificación expandida | 500&nbsp;KB | 5&nbsp;MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="iOS and Android push" }

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

{% endtab %}
{% tab Texto %}

| Tipo de mensaje | Longitud de mensaje recomendada (solo texto) | Longitud de mensaje recomendada (enriquecido)
--- | ---
(iOS) Pantalla de bloqueo | 160 caracteres | 130 caracteres
(iOS) Centro de notificaciones | 160 caracteres | 130 caracteres
(iOS) Alerta de banner | 80 caracteres | 65 caracteres
(Android) Pantalla de bloqueo | 49 caracteres | N/A
(Android) Panel de notificaciones | 597 caracteres | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS and Android push" }

¿Te preguntas cuántos caracteres puedes usar en una notificación push de iOS sin que se trunque? Consulta nuestras [directrices de recuento de caracteres en iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/#character-count).

{% endtab %}
{% tab Tamaño de carga útil %}

**Plataforma** | **Tamaño**
--- | ---
pre iOS 8 | 0,256 KB
post iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 aria-label="iOS and Android push" }

{% endtab %}
{% tab Ejemplo de imagen %}
{% subtabs %}
{% subtab iOS %}

![Notificación push de iOS con texto que dice: "Hi! This is an iOS Push with an image" con un emoji. Hay una imagen pequeña junto al texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificación push de iOS en un push completo con el mismo texto que el mensaje anterior con una imagen expandida antes del texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

![Notificación push de Android con una imagen grande debajo del texto del mensaje.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Las notificaciones con imágenes grandes se muestran mejor cuando se utiliza una imagen de al menos 600x300 píxeles.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Ejemplo de texto %}
{% subtabs %}
{% subtab iOS %}

![Notificación push de iOS con texto que dice: "Hi! This is an iOS Push".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
![Notificación push de Android mostrada en la pantalla de inicio.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Notificación push web {#web-push}

{% tabs local %}
{% tab Imágenes %}

| **Navegador** | **Tamaño de icono recomendado**
| --- | ---
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web push" }
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Los iconos se pueden configurar por campaña con Safari 16+ en macOS 13+)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web push" }

| **Navegador** | **Plataforma** | **Tamaño de imagen grande**
| --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web push" }
Chrome | Android | Relación de aspecto 2:1
Firefox | Android | N/A
Chrome | Windows | Relación de aspecto 2:1
Edge | Windows | Relación de aspecto 2:1
Firefox | Windows | N/A
Firefox | Windows | Relación de aspecto 2:1
Safari | macOS | N/A
Chrome | macOS | N/A
Firefox | macOS | N/A
Opera | macOS | N/A
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web push" }

{% endtab %}
{% tab Texto %}

| **Navegador** | **Plataforma** | **Longitud máxima del título**  | **Longitud máxima del cuerpo del mensaje**
| --- | --- | --- | ---
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Web push" }
Chrome | Android | 35 | 50
Firefox | Android | 35 | 50
Chrome | Windows | 50 | 120
Edge | Windows | 50 | 120
Firefox | Windows | 54 | 200
Opera | Windows | 50 | 120
Chrome | macOS | 35 | 50
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Web push" }

{% endtab %}
{% endtabs %}