---
nav_title: Seguimiento de clics en KakaoTalk
article_title: Seguimiento de clics en KakaoTalk
page_order: 3
description: "Esta página explica cómo activar el seguimiento de clics en tus mensajes de KakaoTalk, probar enlaces acortados, usar tu dominio personalizado en enlaces rastreados y más."
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# Seguimiento de clics en KakaoTalk {#kakaotalk-click-tracking}

> Esta página explica cómo activar el seguimiento de clics en tus mensajes de KakaoTalk, probar enlaces acortados, usar tu dominio personalizado en enlaces rastreados y más.

Cuando el seguimiento de clics en KakaoTalk está activado, Braze acorta automáticamente tus URL, añade mecanismos de seguimiento y registra los clics en tiempo real. Estos datos te permiten crear estrategias de segmentación y reorientación más específicas, como segmentar usuarios según su comportamiento de clics y desencadenar mensajes en respuesta a clics específicos.

El seguimiento de clics en KakaoTalk se puede usar para mensajes de texto, imagen y elementos de lista. Admite enlaces dentro de botones y acciones de clic en imágenes. También puedes personalizar las URL usando Liquid y dominios personalizados.

## Cómo funciona {#how-it-works}

Puedes administrar la configuración del seguimiento de clics en KakaoTalk en la sección **Link options** del creador de mensajes. Cuando está activado, las URL se acortarán usando el dominio predeterminado de Braze (`https://brz.ai`) o el dominio personalizado especificado para el grupo de suscripción, y se personalizarán para el usuario.

Cualquier URL que comience con `http://` o `https://` se acortará. Puedes tener hasta 25 URL en un mensaje. Las URL acortadas que contengan personalización con Liquid (como seguimiento a nivel de usuario o parámetros UTM) serán válidas durante dos meses.

## Configurar el seguimiento de clics {#set-up-click-tracking}

### Mensajes de texto {#text-messages}

Para configurar el seguimiento de clics en un mensaje de texto:

1. Redacta un mensaje de **Text** y añade una URL al campo de texto o al botón.
2. En la sección **Link options** del creador de mensajes, confirma que **Click Tracking** esté marcado. El seguimiento de clics está activado de forma predeterminada para todos los mensajes nuevos.

![Creador de mensajes de texto de KakaoTalk mostrando la sección Link options con Click Tracking marcado.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### Mensajes de imagen {#image-messages}

Para configurar el seguimiento de clics en un mensaje de imagen:

1. Redacta un mensaje de **Image** y configura el comportamiento de clic para abrir una URL.
2. Introduce una URL en el campo de URL.
3. En la sección **Link options** del creador de mensajes, confirma que **Click Tracking** esté marcado.

### Mensajes de elementos de lista {#list-item-messages}

Para configurar el seguimiento de clics en un mensaje de elementos de lista:

1. Redacta un mensaje de **List item** y añade una URL al campo **Website URL** de cualquier elemento.
2. En la sección **Link options** del creador de mensajes, confirma que **Click Tracking** esté marcado.

## Dominios personalizados {#custom-domains}

El seguimiento de clics en KakaoTalk te permite usar tu propio dominio para personalizar la apariencia de tus URL acortadas, ayudando a proyectar una imagen de marca consistente. Para más información, consulta [Dominios personalizados]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/).

## Personalización con Liquid en las URL {#liquid-personalization-in-urls}

Puedes construir dinámicamente tu URL directamente dentro del creador de mensajes de Braze, lo que te permite añadir parámetros UTM dinámicos a tus URL o enviar a los usuarios enlaces únicos (como dirigirlos a su carrito abandonado o a un producto específico que vuelve a estar disponible).

Las URL se pueden generar dinámicamente mediante el uso de cualquier etiqueta de personalización con Liquid compatible.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También puedes acortar variables de Liquid definidas de forma personalizada, como se muestra en el siguiente ejemplo:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

Braze acorta las URL que son renderizadas por Liquid, incluso aquellas incluidas en propiedades de desencadenamiento por API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, Braze acortará y rastreará esa URL antes de enviar el mensaje de KakaoTalk.

## Pruebas {#testing}

Antes de lanzar tu Campaign o Canvas, es una buena práctica previsualizar y probar tu mensaje primero. Para hacerlo, ve a la pestaña **Test** para previsualizar y enviar un mensaje de KakaoTalk a grupos de prueba de contenido o a un usuario individual.

La vista previa se actualizará con la personalización relevante y la URL acortada.

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando el borrador del Canvas se activa.
{% endalert %}

## Informes {#reporting}

La tabla de rendimiento de KakaoTalk incluye la columna **Total Clicks** que muestra un recuento de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre las métricas de KakaoTalk, consulta [Informes de KakaoTalk]({{site.baseurl}}/kakaotalk_reporting/).

Los datos de clics se reportarán automáticamente en el dashboard de análisis.

## Reorientar usuarios {#retarget-users}

Puedes reorientar a los usuarios que han hecho clic en una URL en un mensaje de KakaoTalk usando los siguientes filtros de segmentación y desencadenadores:

- Desencadenadores basados en acciones
    - Interact with Campaign
    - Interact with Step

- Filtros de segmentación
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Los enlaces que recibo al enviar una prueba son URL reales? {#are-the-links-i-receive-when-test-sending-real-urls}

Sí, se generarán URL reales al enviar una prueba. Sin embargo, la URL exacta enviada en una Campaign lanzada puede diferir de la enviada en un envío de prueba.

### ¿Puedo añadir parámetros UTM a una URL antes de que se acorte? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Sí, se pueden añadir tanto parámetros estáticos como dinámicos.

### ¿Cuánto tiempo permanecen válidas las URL acortadas? {#how-long-do-shortened-urls-remain-valid}

Las URL personalizadas son válidas durante dos meses a partir del momento del registro de la URL.

### ¿Es necesario instalar el SDK de Braze para acortar URL? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

No, el seguimiento de clics funciona sin ninguna integración de SDK.

### ¿Puedo saber qué usuarios individuales están haciendo clic en una URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sí. Cuando el seguimiento de clics está activado, puedes reorientar a los usuarios que han hecho clic en URL usando los [filtros de reorientación de KakaoTalk](#retargeting-users).

### ¿El seguimiento de clics funciona con vínculos profundos o enlaces universales? {#does-click-tracking-work-with-deep-links-or-universal-links}

El seguimiento de clics se aplica a URL web. Para vínculos profundos, puedes configurar un vínculo profundo directamente como el tipo de acción de clic para botones en KakaoTalk; estos no pasan por el acortamiento de URL ni el seguimiento de clics. Si prefieres usar enlaces universales de proveedores como Branch o Appsflyer, estos se pueden acortar, pero Braze no puede solucionar problemas que puedan surgir (como interrumpir la atribución o fallar en la redirección).