---
nav_title: Seguimiento de clics
article_title: Seguimiento de clics
page_order: 2
description: "Este artículo de referencia cubre cómo activar el seguimiento de clics en tus mensajes de WhatsApp, probar enlaces acortados, usar tu dominio personalizado en enlaces rastreados y más."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Seguimiento de clics {#click-tracking}

> Esta página cubre cómo activar el seguimiento de clics en tus mensajes de WhatsApp, probar enlaces acortados, usar tu dominio personalizado en enlaces rastreados y más.

El seguimiento de clics te permite medir cuándo alguien toca un enlace en tu mensaje de WhatsApp, dándote una visión clara de qué contenido está impulsando la interacción. Braze acorta tus URL, añade seguimiento en segundo plano y registra los eventos de clic a medida que ocurren.

Puedes activar el seguimiento de clics tanto en mensajes de respuesta como en mensajes de plantilla. Funciona con enlaces en botones y en el cuerpo del texto, y es compatible con URL personalizadas y dominios personalizados. Una vez activado, verás los datos de clics en tus informes de rendimiento de WhatsApp y podrás segmentar usuarios en función de quién hizo clic en qué.

{% alert note %}
El seguimiento de clics no funciona con vínculos profundos. Puedes acortar enlaces universales de proveedores como Branch o Appsflyer, pero Braze no puede solucionar problemas que puedan surgir al hacerlo (como romper la atribución o causar una redirección).
{% endalert %}

## Cómo funciona {#how-it-works}

### Mensajes de respuesta {#response-messages}

Para configurar el seguimiento de clics en mensajes de respuesta:
1. Crea un mensaje de respuesta que incluya un botón de llamada a la acción (CTA) con una URL de sitio web.
2. Habilita el seguimiento de clics haciendo clic en el botón designado en la interfaz.

El enlace se acortará al dominio de Braze, o al dominio personalizado especificado para el grupo de suscripción, y se personalizará para el usuario.

Cualquier URL estática que comience con `http://` o `https://` se acortará. Las URL acortadas que contengan personalización con Liquid (como seguimiento a nivel de usuario) serán válidas durante dos meses.

![Creador de mensajes de WhatsApp con cuerpo de contenido y un botón.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Mensajes de plantilla {#template-messages}

Para los mensajes de plantilla, la URL base debe enviarse correctamente al crear la plantilla para activar el seguimiento de clics.

#### Paso 1: Crea una plantilla compatible con el seguimiento de clics en WhatsApp {#step-1-build-a-click-tracking-supported-template-in-whatsapp}

1. En tu WhatsApp Manager, crea una URL base que sea tu dominio personalizado o `brz.ai`.
2. Asegúrate de que los enlaces incluidos en la plantilla sean compatibles con el seguimiento de clics.
3. No cambies las variables de la plantilla después de configurarla como campaña en Braze; los cambios posteriores no se pueden incorporar.
4. Para los enlaces de botones CTA, selecciona **Dynamic** y luego proporciona la URL base (`brz.ai` o tu dominio personalizado).<br><br>![Sección para crear una llamada a la acción.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Para los enlaces en el cuerpo del texto, al escribir la plantilla en tu WhatsApp Manager, elimina cualquier espacio insertado en los enlaces contenidos en el cuerpo que quieras rastrear.<br><br>![Cuadro de texto para introducir el cuerpo de contenido de la llamada a la acción.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Paso 2: Completa tu plantilla en Braze {#step-2-complete-your-template-in-braze}

Al redactar, Braze detectará automáticamente qué plantillas tienen dominios de URL compatibles, tanto en el cuerpo del texto como en los botones CTA. El estado se mostrará en la parte inferior de la plantilla.

![Sección "Link Status" que muestra un estado activo para el seguimiento de clics.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Enlaces compatibles:** Los enlaces que se envíen con la URL base correspondiente tendrán el seguimiento de clics habilitado.
- **Enlaces parcialmente compatibles:** Si algunos enlaces de una plantilla se envían como URL completas, el seguimiento de clics **no** se aplicará a esos enlaces.
- **Enlaces no compatibles:** Los enlaces sin una URL base aprobada **no** tendrán capacidades de seguimiento de clics.

La URL de destino deberá proporcionarse para cualquier enlace con una URL base que coincida con `brz.ai` o tu dominio personalizado.

![Sección "Buttons" con campos para el nombre del botón, la URL del sitio web y la URL de seguimiento de clics.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**Envío de mensajes de plantilla a través de la API**: El seguimiento de clics de WhatsApp (usando `brz.ai` o un dominio de seguimiento personalizado y el campo **Click tracking URL** en el creador de mensajes) no es compatible cuando se envían mensajes de plantilla de WhatsApp a través del [punto de conexión `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

Si envías un mensaje de plantilla a través de la API, puedes rellenar las variables de URL del CTA (usando `button_variables`), pero Braze no genera una URL de seguimiento de clics ni un enlace de redirección en el flujo de solicitud de la API. Para usar el seguimiento de clics, envía la plantilla desde el panel de Braze o mediante un desencadenador de campaña de Braze.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Personalización con Liquid en las URL {#liquid-personalization-in-urls}

Puedes construir dinámicamente tu URL directamente dentro del compositor de Braze, lo que te permite añadir parámetros UTM dinámicos a tus URL o enviar a los usuarios enlaces únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que vuelve a estar en stock).
Las URL se pueden generar dinámicamente mediante el uso de cualquier etiqueta de personalización Liquid compatible.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También admitimos el acortamiento de variables Liquid definidas de forma personalizada, como en estos ejemplos:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Acortar URL generadas por variables Liquid {#shorten-urls-rendered-by-liquid-variables}

Braze acorta las URL generadas por Liquid, incluso las incluidas en propiedades de desencadenadores de API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, acortaremos y rastrearemos esa URL antes de enviar el mensaje de WhatsApp.

## Pruebas {#testing}

Antes de lanzar tu campaña o Canvas, es una buena práctica previsualizar y probar tu mensaje primero. Para hacerlo, ve a la pestaña **Test** para previsualizar y enviar un WhatsApp a grupos de prueba de contenido o a un usuario individual.

Esta vista previa se actualizará con la personalización relevante y la URL acortada.

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando el borrador del Canvas se activa.
{% endalert %}

## Informes {#reporting}

Cuando el seguimiento de clics está activado o se usa con plantillas compatibles, la tabla de rendimiento de WhatsApp incluye la columna **Total Clicks** que muestra un recuento de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre las métricas de WhatsApp, consulta [Rendimiento de mensajes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/reporting/).

![Paso de Canvas de mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Los datos de clics se reportarán automáticamente en el dashboard de análisis.

![Tabla de rendimiento de mensajes de WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Reorientar usuarios {#retargeting-users}

Puedes usar el filtro `Clicked/Opened Step` y la interacción `clicked tracked WhatsApp link` para segmentar usuarios en función de sus interacciones con los enlaces.

![Grupo de filtros con un filtro para "clicked tracked WhatsApp link".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### ¿Puedo saber qué usuarios individuales están haciendo clic en una URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sí. Cuando el seguimiento de clics está activado (o habilitado según la configuración de la plantilla), puedes reorientar a los usuarios que han hecho clic en URL aprovechando los filtros de reorientación de WhatsApp o los eventos de clic de WhatsApp (`users.messages.whatsapp.Click`) enviados por Currents.

### ¿Las vistas previas en el dispositivo de WhatsApp cuentan como clics? {#do-previews-on-the-whatsapp-device-count-as-clicks}

No, no contribuyen a la tasa de clics de los mensajes de WhatsApp.