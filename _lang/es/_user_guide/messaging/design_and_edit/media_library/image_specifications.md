---
nav_title: Especificaciones de imágenes
article_title: Especificaciones de imágenes
page_order: 1
page_type: reference
description: "Este artículo de referencia describe los tamaños y especificaciones de imagen recomendados para cada tipo de canal."
tool:
  - Templates
  - Media

---

# Especificaciones de imágenes {#image-specifications}

> En general, las imágenes más pequeñas y de alta calidad se cargan más rápido, por lo que recomendamos usar el activo más pequeño posible para lograr el resultado deseado. Para maximizar el uso de tus imágenes en canales específicos, consulta los detalles en este artículo.

Siempre debes [previsualizar y probar tus mensajes]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) en una variedad de dispositivos para confirmar que las áreas más importantes de tu imagen y mensaje se muestren como se espera.

## Comportamiento de la imagen {#image-behavior}

{% multi_lang_include channels/image_specs.md variable_name='image behavior' %}

## Video {#video}

Los videos subidos a la biblioteca de medios solo se pueden usar en mensajes de WhatsApp. Para más información, consulta [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#outbound-messages).

## GIF {#gifs}

Los GIF son compatibles con push en iOS, mensajes dentro de la aplicación, correo electrónico, Content Cards y mensajes MMS o RCS. Los GIF con formas muy alargadas (por ejemplo, 3000 x 2 píxeles) o con 300 o más fotogramas pueden no cargarse, incluso si el tamaño total del archivo es pequeño.

{% multi_lang_include alerts/note_alerts.md alert='GIF platform support' %}

## Guía por canal {#channel-guidance}

### Content Cards

{% multi_lang_include channels/image_specs.md variable_name='content cards' %}

### Correo electrónico {#email}

{% multi_lang_include channels/image_specs.md variable_name='email' %}

### Mensajes dentro de la aplicación {#in-app-messages}

{% multi_lang_include channels/image_specs.md variable_name='in-app messages' %}

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes para mensajes dentro de la aplicación y las superposiciones de zona segura están diseñadas para funcionar bien con dispositivos de todos los tamaños. [Descargar ZIP de plantillas de diseño]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

Para más información, consulta [Detalles creativos de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

#### Font Awesome

Braze admite el uso de [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) para iconos de mensajes modales dentro de la aplicación.

### Notificaciones push {#push-notifications}

{% multi_lang_include channels/image_specs.md variable_name='payload size' %}

{% multi_lang_include channels/image_specs.md variable_name='push notifications' %}

#### Longitudes de mensaje recomendadas {#recommended-message-lengths}

Para obtener los mejores resultados, consulta las siguientes directrices de longitud de mensaje al redactar mensajes push. Puede haber cierta variación dependiendo de la presencia de una imagen, el estado de la notificación (iOS) y la configuración de pantalla del dispositivo del usuario, así como del tamaño del dispositivo.

| Tipo de mensaje | Longitud recomendada (solo texto) | Longitud recomendada (enriquecido) |
| --- | --- | --- |
| Pantalla de bloqueo de iOS | 160 caracteres | 130 caracteres |
| Centro de notificaciones de iOS | 160 caracteres | 130 caracteres |
| Alerta de banner de iOS | 80 caracteres | 65 caracteres |
| Pantalla de bloqueo de Android | 49 caracteres | N/A |
| Panel de notificaciones de Android | 597 caracteres | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Longitudes de mensaje recomendadas" }

Para más información sobre el conteo de caracteres en iOS, consulta las [directrices de conteo de caracteres en iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count).

#### Notificación push web {#web-push}

{% tabs %}
{% tab Imágenes %}

| Navegador | Tamaño de icono recomendado |
| --- | --- |
| Chrome | 192 x 192 px o mayor |
| Firefox | 192 x 192 px o mayor |
| Safari | 192 x 192 px o mayor (configurable por Campaign con Safari 16 en macOS 13+) |
| Opera | 192 x 192 px o mayor |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Notificación push web" }

| Navegador | Plataforma | Tamaño de imagen grande |
| --- | --- | --- |
| Chrome | Android | Relación de aspecto 2:1 |
| Firefox | Android | N/A |
| Chrome | Windows | Relación de aspecto 2:1 |
| Edge | Windows | Relación de aspecto 2:1 |
| Firefox | Windows | N/A |
| Opera | Windows | Relación de aspecto 2:1 |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Notificación push web" }

{% endtab %}
{% tab Texto %}

| Navegador | Plataforma | Longitud máxima del título | Longitud máxima del cuerpo |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Notificación push web" }

{% endtab %}
{% endtabs %}

#### Ejemplos de notificaciones push {#push-notification-examples}

{% tabs %}
{% tab iOS %}

![Notificación push de iOS con texto que dice: "Hi! This is an iOS Push with an image" con un emoji. Hay una imagen pequeña junto al texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificación push de iOS en un push expandido con el mismo texto que el mensaje anterior y una imagen ampliada antes del texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Notificación push de Android con una imagen grande debajo del texto del mensaje.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Las notificaciones con imágenes grandes se muestran mejor cuando se utiliza una imagen de al menos 600 x 300 píxeles.
{% endalert %}

{% endtab %}
{% endtabs %}

Para recursos adicionales, consulta [Especificaciones de imagen y texto para push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats).

### SMS y MMS {#sms-and-mms}

{% multi_lang_include channels/image_specs.md variable_name='sms and mms' %}

Para redactar mensajes MMS, consulta [Crear un mensaje SMS, MMS o RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).