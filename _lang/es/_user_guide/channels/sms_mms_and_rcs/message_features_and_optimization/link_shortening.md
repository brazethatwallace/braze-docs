---
nav_title: Acortamiento de enlaces
article_title: Acortamiento de enlaces
page_order: 1
description: "Este artículo de referencia explica cómo activar el acortamiento de enlaces en tus mensajes SMS y algunas preguntas frecuentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Acortamiento de enlaces {#link-shortening}

> Esta página explica cómo activar el acortamiento de enlaces en tus mensajes SMS y RCS, probar enlaces acortados, usar tu dominio personalizado en enlaces acortados y más.

{% alert important %}
Braze está implementando gradualmente el [acortamiento de enlaces unificado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening?sdktab=unified), que consolida todos los enlaces acortados de SMS y RCS en un único formato de enlace personalizado (por ejemplo, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

El acortamiento de enlaces y el seguimiento de clics te permiten acortar automáticamente las URL contenidas en mensajes SMS o RCS y recopilar análisis de tasa de clics, proporcionando métricas de participación adicionales para ayudarte a comprender cómo los usuarios interactúan con tus Campaigns.

El acortamiento de enlaces y el seguimiento de clics se pueden activar a [nivel de variante de mensaje]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) tanto en Campaigns como en Canvas.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

La longitud de la URL está determinada por el tipo de seguimiento que se activa:
- **Seguimiento básico** habilita el seguimiento de clics a nivel de campaña. Las URL estáticas tienen una longitud de 20 caracteres y las URL personalizadas tienen una longitud de 25 caracteres.
- **Seguimiento avanzado** habilita el seguimiento de clics a nivel de campaña y a nivel de usuario, y permite el uso de capacidades de segmentación y reorientación que dependen de los clics. Los clics también generan un [evento de clic de SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) enviado a través de Currents. Las URL estáticas con seguimiento avanzado tienen una longitud de 27-28 caracteres, lo que te permite crear segmentos de usuarios que han hecho clic en las URL. Las URL personalizadas tienen una longitud de 32-33 caracteres.

Los enlaces se acortan usando nuestro dominio corto compartido (`brz.ai`) o tu dominio personalizado de acortamiento de enlaces. Un ejemplo de URL podría verse así: `https://brz.ai/8jshX` (básico, estático) o `https://brz.ai/p/8jshX/2dj8d` (avanzado, personalizado). Consulta [Pruebas](#legacy_testing) para más información.

Cualquier URL estática que comience con `http://` o `https://` se acorta. Las URL estáticas acortadas son válidas durante un año a partir de la fecha en que fueron creadas. Las URL acortadas que contienen personalización con Liquid son válidas durante dos meses.

{% alert note %}
Los enlaces acortados de Braze siempre incluyen el protocolo `https://` y no se pueden configurar para usar un protocolo diferente.
{% endalert %}

## Uso del acortamiento de enlaces {#using-link-shortening}

Para usar el acortamiento de enlaces, asegúrate de que el interruptor de acortamiento de enlaces en el creador de mensajes esté activado. Luego, elige usar seguimiento básico o avanzado.

![Creador de mensajes con un interruptor para el acortamiento de enlaces.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %}){: width="1614" height="994"}

Braze solo reconoce las URL que comienzan con `http://` o `https://`. Cuando se reconoce una URL, la sección de **vista previa** se actualiza con una URL de marcador de posición. Braze estima la longitud de la URL después del acortamiento, pero una advertencia te solicita seleccionar un usuario de prueba y guardar el mensaje como borrador para obtener una estimación más precisa.

![Creador de mensajes con una URL larga en el cuadro "Mensaje" y un enlace acortado generado en la vista previa.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %}){: width="1569" height="516"}

{% alert note %}
Si planeas usar el [filtro de canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) de BrazeAI<sup>TM</sup> y quieres que los canales SMS y RCS sean seleccionables, activa el acortamiento de enlaces con seguimiento avanzado.
{% endalert %}

### Agregar parámetros UTM {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalización con Liquid en las URL {#liquid-personalization-in-urls}

Puedes construir dinámicamente tu URL directamente dentro del creador de Braze, lo que te permite agregar parámetros UTM dinámicos a tus URL o enviar a los usuarios enlaces únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que volvió a estar disponible).

### Crear una URL con etiquetas de personalización con Liquid compatibles {#create-a-url-with-supported-liquid-personalization-tags}

Las URL se pueden generar dinámicamente mediante el uso de cualquier [etiqueta de personalización con Liquid compatible]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Braze también admite el acortamiento de variables Liquid definidas de forma personalizada, como en los siguientes ejemplos:

### Crear una URL usando variables Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Acortar URL renderizadas por variables Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canales compatibles:** KakaoTalk, LINE, SMS, RCS, WhatsApp

Braze acorta las URL que son renderizadas por Liquid, incluso aquellas incluidas en propiedades de desencadenamiento por API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, Braze acorta y rastrea esa URL antes de enviar el mensaje.

### Acortar URL en el endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

El acortamiento de enlaces también está activado para mensajes solo por API a través del [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Para activar también el seguimiento básico o avanzado, usa los parámetros de solicitud `link_shortening_enabled` o `user_click_tracking_enabled`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Opcional | Booleano | Establece `link_shortening_enabled` en `true` para activar el acortamiento de enlaces y el seguimiento de clics a nivel de campaña. Para usar el seguimiento, deben estar presentes un `campaign_id` y un `message_variation_id`. |
| `user_click_tracking_enabled` | Opcional | Booleano | Establece `user_click_tracking_enabled` en `true` para activar el acortamiento de enlaces, y el seguimiento de clics a nivel de campaña y a nivel de usuario. Puedes usar los datos rastreados para crear segmentos de usuarios que hicieron clic en las URL.<br><br> Para usar este parámetro, `link_shortening_enabled` debe ser `true`, y deben estar presentes un `campaign_id` y un `message_variation_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Acortar URL en el endpoint /messages/send" }

Para obtener una lista completa de parámetros de solicitud, ve a [parámetros de solicitud]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

## Pruebas {#testing}

Antes de lanzar tu Campaign o Canvas, es una buena práctica previsualizar y probar tu mensaje primero. Para hacerlo, ve a la pestaña **Prueba** para previsualizar y enviar un mensaje SMS o RCS a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) o a un usuario individual.

Esta vista previa se actualiza con la personalización relevante y la URL acortada. El número de caracteres y los [segmentos facturables]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) también se actualizan para reflejar la personalización renderizada y la URL acortada.

Asegúrate de guardar la Campaign o el Canvas antes de enviar un mensaje de prueba para recibir una representación de la URL acortada que se envía en tu mensaje. Si la Campaign o el Canvas no se guardan antes de un envío de prueba, el envío de prueba incluirá una URL de marcador de posición.

Para que los Canvas aparezcan en el filtro "Hizo clic en enlace SMS acortado", el paso en Canvas que contiene el enlace corto también debe estar habilitado con seguimiento avanzado, que permite el seguimiento de clics a nivel de usuario. Si el enlace corto está configurado con seguimiento básico, la opción de filtrar eventos de clic en enlaces SMS cortos no está disponible. El mismo requisito de seguimiento avanzado se aplica cuando configuras la entrada del Canvas o las Rutas de Acción que dependen de enlaces SMS acortados en los que se hizo clic.

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando el borrador del Canvas se activa.
{% endalert %}

![Pestaña "Prueba" del mensaje con campos para seleccionar destinatarios de prueba.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %}){: width="1569" height="947"}

{% alert note %}
La personalización con Liquid y las URL acortadas se procesan en la pestaña **Prueba** después de que se haya seleccionado un usuario. Asegúrate de seleccionar un usuario para recibir un recuento de caracteres preciso.
{% endalert %}

## Seguimiento de clics {#click-tracking}

Cuando el acortamiento de enlaces está activado, la tabla de **rendimiento de SMS/MMS/RCS** incluye una columna titulada **Clics totales** que muestra un recuento de eventos de clic por variante y una tasa de clics asociada. **Clics totales** excluye los clics sospechosos de bots de los recuentos del panel. Para más detalles sobre las métricas, consulta [Rendimiento de mensajes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) y [Filtrado de clics de bots]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).

![Tabla de métricas de rendimiento de SMS y MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %}){: width="1586" height="191"}

Las tablas de **Rendimiento histórico** y **Rendimiento de SMS/MMS/RCS** también incluyen una opción para **Clics totales** y muestran una serie temporal diaria de eventos de clic. Los clics se incrementan en la redirección (como cuando un usuario visita un enlace) y pueden incrementarse más de una vez por usuario.

## Reorientación de usuarios {#retargeting-users}

Para obtener orientación sobre la reorientación, visita [Reorientación]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### ¿Sé qué usuarios individuales están haciendo clic en una URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sí. Cuando el **seguimiento avanzado** está activado, puedes reorientar a los usuarios que han hecho clic en las URL aprovechando los [filtros de reorientación de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) o los eventos de clic de SMS (`users.messages.sms.ShortLinkClick`) enviados por Currents.

### ¿Funciona el acortamiento de enlaces con vínculos profundos o enlaces universales? {#does-link-shortening-work-with-deep-links-or-universal-links}

El acortamiento de enlaces no funciona con vínculos profundos. Alternativamente, puedes acortar enlaces universales de proveedores externos como Branch o Appsflyer, pero los usuarios pueden experimentar una breve redirección o efecto de "parpadeo". Esto ocurre porque el enlace acortado se enruta primero a través de la web antes de resolverse al enlace universal que admite la apertura de la aplicación. Además, Braze no puede solucionar problemas que puedan surgir al acortar enlaces universales, como romper la atribución o causar redirecciones inesperadas.

{% alert note %}
Prueba la experiencia del usuario antes de implementar el acortamiento de enlaces con enlaces universales para confirmar que cumple con tus expectativas.
{% endalert %}

### ¿Los `send_ids` están asociados con los eventos de clic de SMS? {#are-send_ids-associated-with-sms-click-events}

No. Sin embargo, si tienes habilitado el seguimiento avanzado, generalmente puedes atribuir `send_ids` con eventos de clic usando [Query Builder]({{site.baseurl}}/query_builder) para consultar datos de Currents con esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```


{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include channels/sms/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}