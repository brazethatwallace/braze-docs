---
nav_title: Seguimiento de clics en LINE
article_title: Seguimiento de clics en LINE
page_order: 2
description: "Esta página explica cómo activar el seguimiento de clics en tus mensajes de LINE, probar enlaces acortados, usar tu dominio personalizado en enlaces rastreados y más."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# Seguimiento de clics en LINE {#line-click-tracking}

> Esta página explica cómo activar el seguimiento de clics en tus mensajes de LINE, probar enlaces acortados, usar tu dominio personalizado en enlaces rastreados y más.


Cuando el seguimiento de clics en LINE está activado, Braze acorta automáticamente tus URL, añade mecanismos de seguimiento y registra los clics en tiempo real. Aunque LINE te ofrece datos de clics agregados, Braze proporciona información granular del usuario que es oportuna y accionable. Estos datos te permiten crear estrategias de segmentación y reorientación más específicas, como segmentar usuarios según su comportamiento de clics y desencadenar mensajes en respuesta a clics específicos.

El seguimiento de clics en LINE se puede usar para mensajes de texto, enriquecidos y basados en tarjetas. Admite enlaces dentro de botones y áreas mapeadas de imágenes que tienen una URL como acción al hacer clic. También puedes personalizar las URL usando Liquid y dominios personalizados.

## Cómo funciona {#how-it-works}

Puedes gestionar la configuración de seguimiento de clics de LINE en la pestaña **Configuración** mientras redactas un mensaje. Cuando está activado, las URL se acortarán usando el dominio predeterminado de Braze (`https://brz.ai`) o el dominio personalizado especificado para el grupo de suscripción, y se personalizarán para el usuario.

Cualquier URL que comience con `http://` o `https://` se acortará. Puedes tener hasta 25 URL en un mensaje. Las URL acortadas que contengan personalización con Liquid (como seguimiento a nivel de usuario o parámetros UTM) serán válidas durante dos meses.

## Configuración del seguimiento de clics {#setting-up-click-tracking}

### Mensajes de texto {#text-messages}

Para configurar el seguimiento de clics en un mensaje de texto:

1. Arrastra un mensaje de **Texto** al creador y añade una URL al campo de texto.

![Creador de mensajes LINE con un mensaje de texto que contiene una URL larga antes del acortamiento.]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. Ve a la pestaña **Settings** y confirma que **Click Tracking** está activado. El seguimiento de clics está activado de forma predeterminada para todos los mensajes nuevos.

{% alert note %}
Puedes ver vistas previas del enlace acortado en la pestaña **Settings** o **vista previa & Test**. El enlace completo se mostrará en el creador mientras construyes tu mensaje.
{% endalert %}

![Pestaña "Settings" del creador de mensajes LINE con "Click Tracking" activado y una vista previa del mensaje de texto con una URL acortada: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Mensajes enriquecidos {#rich-messages}

Para configurar el seguimiento de clics en un mensaje enriquecido:

1. Arrastra un **Mensaje enriquecido** al creador y selecciona una plantilla.
2. Selecciona **URI** como **Comportamiento al hacer clic** para el área táctil correspondiente.
3. Introduce una URL en el campo **Open URL**.

![Creador de mensajes LINE con un mensaje enriquecido con dos áreas táctiles, cada una con una URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. Ve a la pestaña **Settings** y confirma que **Click Tracking** está activado. El seguimiento de clics está activado de forma predeterminada para todos los mensajes nuevos.

### Mensajes basados en tarjetas {#card-based-messages}

Para configurar el seguimiento de clics en un mensaje basado en tarjetas:

1. Arrastra un **Mensaje basado en tarjetas** al creador.
2. Selecciona **URI** como **Comportamiento al hacer clic** para las áreas de tarjeta o botón correspondientes.

![Creador de mensajes LINE con un mensaje basado en tarjetas con dos botones, cada uno con una URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. Ve a la pestaña **Settings** y confirma que **Click Tracking** está activado. El seguimiento de clics está activado de forma predeterminada para todos los mensajes nuevos.

{% alert note %}
Las URL en los campos **Title** o **Description** no se acortarán porque estos campos no son clicables dentro de LINE.
{% endalert %}

## Dominios personalizados {#custom-domains}

El seguimiento de clics de LINE te permite usar tu propio dominio para personalizar la apariencia de tus URL acortadas, lo que ayuda a proyectar una imagen de marca consistente. Para más información, consulta [Dominios personalizados]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains).

## Personalización con Liquid en URLs {#liquid-personalization-in-urls}

Puedes construir dinámicamente tu URL directamente dentro del creador de Braze, lo que te permite añadir parámetros UTM dinámicos a tus URLs o enviar a los usuarios vínculos únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que ha vuelto a estar disponible).
Puedes generar URLs dinámicamente utilizando cualquier etiqueta de personalización con Liquid compatible.

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

## Acortar URLs renderizadas por variables de Liquid {#shorten-urls-rendered-by-liquid-variables}

Braze acorta las URLs que se renderizan mediante Liquid, incluso aquellas incluidas en las propiedades de desencadenamiento de API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, acortamos y hacemos seguimiento de esa URL antes de enviar el mensaje de LINE.

## Pruebas {#testing}

Antes de lanzar tu Campaign o Canvas, se recomienda previsualizar y probar tu mensaje primero. Para hacerlo, ve a la pestaña **Prueba** para previsualizar y enviar un mensaje de LINE a grupos de prueba de contenido o a un usuario individual.

Esta vista previa se actualizará con la personalización relevante y la URL acortada.

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando el borrador del Canvas se activa.
{% endalert %}

## Informes {#reporting}

La tabla de rendimiento de LINE incluye la columna **Total de clics** que muestra un recuento de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre las métricas de LINE, consulta [Rendimiento de mensajes de LINE]({{site.baseurl}}/user_guide/channels/line/reporting).

![Rendimiento de un paso en Canvas de LINE.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Los datos de clics se reportarán automáticamente en el panel de análisis.

![Panel de análisis de rendimiento de LINE.]({% image_buster /assets/img/line/line_performance.png %})

## Reorientar usuarios {#retargeting-users}

Puedes reorientar a los usuarios que han hecho clic en una URL de un mensaje LINE utilizando los siguientes filtros de segmentación y desencadenantes:

- Desencadenantes basados en acciones
    - Interactuar con Campaign
    - Interactuar con paso

![Desencadenante de entrega basada en acciones de LINE.]({% image_buster /assets/img/line/line_action_based.png %})

- Filtros de segmentación
    - Hizo clic en/Abrió Campaign
    - Hizo clic en/Abrió Campaign o Canvas con etiqueta
    - Hizo clic en/Abrió paso

![Grupo de filtros que muestra los tres filtros de segmentación: "Hizo clic en/Abrió Campaign", "Hizo clic en/Abrió Campaign o Canvas con etiqueta" y "Hizo clic en/Abrió paso".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Los enlaces que recibo al enviar pruebas son URL reales? {#are-the-links-i-receive-when-test-sending-real-urls}

Sí, se generarán URL reales al enviar pruebas. Sin embargo, la URL exacta enviada en una Campaign lanzada puede diferir de la enviada en un envío de prueba.

### ¿Puedo agregar parámetros UTM a una URL antes de que se acorte? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Sí, se pueden agregar tanto parámetros estáticos como dinámicos.

### ¿Cuánto tiempo permanecen válidas las URL acortadas? {#how-long-do-shortened-urls-remain-valid}

Las URL personalizadas son válidas durante dos meses a partir del momento del registro de la URL.

### ¿Es necesario tener instalado el SDK or kit de desarrollo de software de Braze para acortar URL? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

No, el seguimiento de clics funciona sin ninguna integración de SDK or kit de desarrollo de software.

### ¿Puedo saber qué usuarios individuales están haciendo clic en una URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sí. Cuando el seguimiento de clics está activado, puedes reorientar a los usuarios que han hecho clic en las URL utilizando los [filtros de reorientación de LINE](#retargeting-users).

### ¿El seguimiento de clics funciona con vínculos profundos o enlaces universales? {#does-click-tracking-work-with-deep-links-or-universal-links}

El seguimiento de clics no funciona con vínculos profundos. Puedes acortar enlaces universales de proveedores como Branch o Appsflyer, pero Braze no puede solucionar los problemas que puedan surgir al hacerlo (como interrumpir la atribución o no redirigir correctamente).

### ¿Las vistas previas en la aplicación de LINE cuentan como clics? {#do-previews-on-the-line-app-count-as-clicks}

No, no contribuyen a la tasa de clics de los mensajes de LINE.