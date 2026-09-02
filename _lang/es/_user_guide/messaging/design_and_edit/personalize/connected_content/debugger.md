---
nav_title: Depurador de contenido conectado
article_title: Depurador de contenido conectado
page_order: 3.5
description: "Este artículo de referencia explica cómo usar el depurador de contenido conectado para solucionar problemas antes de lanzar tu mensaje."
---

# Depurador de contenido conectado {#connected-content-debugger}

> Usa el depurador de contenido conectado para ver la solicitud y la respuesta en vivo de cada llamada de contenido conectado, de modo que puedas verificar tu endpoint, encabezados y etiquetas de Liquid antes de lanzar una Campaign o un Canvas.

## Acerca del depurador {#about-the-debugger}

El contenido conectado te permite enriquecer los mensajes con datos en tiempo real realizando una llamada HTTP a una API externa en el momento de la representación, e insertando luego la respuesta en tu mensaje con Liquid. Como esa llamada ocurre fuera de Braze, puede ser difícil ver exactamente qué solicitud envió Braze, qué devolvió el endpoint o por qué falló una llamada, antes de que una Campaign o un Canvas esté en vivo.

El depurador de contenido conectado ayuda a solucionar esos problemas antes del lanzamiento. Te muestra la solicitud y la respuesta en vivo de cada llamada de contenido conectado en tu mensaje en la sección **Vista previa y prueba**. De esta manera, puedes confirmar que tu endpoint, encabezados y etiquetas de Liquid están configurados correctamente, todo dentro del panel de Braze.

### Áreas compatibles {#supported-areas}

El depurador de contenido conectado está disponible para las siguientes áreas:

- Pasos de contexto de Canvas
- Content Cards
- Correo electrónico
    - Incluye plantillas
    - Excluye pies de página y páginas de suscripción
- Mensajes dentro de la aplicación
- Notificaciones push
- servicio de mensajes cortos/MMS/RCS
- Webhooks
    - Incluye plantillas
- WhatsApp

{% alert note %}
El depurador está disponible para la mayoría de los canales, pero aún no para KakaoTalk, LINE, Banners ni superficies de composición no específicas de canal (como Content Blocks y el paso de actualización de usuario de Canvas). Si no ves el depurador, es posible que la depuración de contenido conectado aún no sea compatible con esa característica.
{% endalert %}

## Usa el depurador {#use-the-debugger}

Cada vez que ejecutas una vista previa, Braze renderiza automáticamente los resultados de la llamada de contenido conectado en la pestaña **Vista previa**. Para usar el depurador:

1. Configura tu mensaje con la etiqueta {% raw %}`{% connected_content %}`{% endraw %}.
2. Ve a la sección **vista previa & Test**. Si tu mensaje incluye una etiqueta de contenido conectado, puedes ver un resumen con el número de llamadas de contenido conectado y los estados de éxito y error.

![Sección de contenido conectado en la sección de pruebas.]({% image_buster /assets/img/connected_content/debugger1.png %})

{:start="3"}
3. Selecciona **View details** para abrir el depurador junto a tu vista previa. El panel muestra una tabla con la URL y el resultado de cada llamada de contenido conectado.

![Llamadas de contenido conectado con tres URLs para revisar.]({% image_buster /assets/img/connected_content/debugger3.png %})

{:start="4"}
4. Junto a cada URL y resultado, selecciona **View** para ver los encabezados de solicitud y respuesta, la carga útil, el método, la duración y la información de almacenamiento en caché.

![Llamada de contenido conectado con detalles de solicitud y respuesta.]({% image_buster /assets/img/connected_content/debugger4.png %})

{:start="5"}
5. Revisa los resultados, ajusta tu etiqueta, encabezados o endpoint según sea necesario. Luego, genera una nueva vista previa para confirmar la corrección.

Si tu plantilla contiene más de una etiqueta {% raw %}`{% connected_content %}`{% endraw %}, el depurador enumera cada llamada que se realizó. Para canales que renderizan múltiples cuerpos de mensaje a partir de una sola plantilla (por ejemplo, correo electrónico, que renderiza cuerpos separados de HTML, texto plano y páginas móviles aceleradas, o Quick Push, que renderiza cuerpos separados específicos para cada dispositivo), el depurador muestra cada llamada de contenido conectado realizada en todos los cuerpos, no solo en el que estás previsualizando activamente.

## Comprender la salida de depuración {#understand-the-debug-output}

Cada llamada de contenido conectado aparece con sus propias pestañas **Response** y **Request**. La pestaña **Response** se muestra de forma predeterminada, ya que generalmente es el primer indicador para confirmar si una llamada tuvo éxito.

### Detalles de la URL {#url-details}

| Campo | Descripción |
| --- | --- |
| URL | La URL completamente renderizada que Braze llamó, con todas las etiquetas de Liquid resueltas. |
| Method | El método HTTP utilizado (GET o POST). |
| Status code | El código de estado HTTP que devolvió tu endpoint (por ejemplo, `200`, `404`, `500`). Consulta [Códigos de respuesta para solución de problemas](#troubleshooting-response-codes) para los códigos específicos de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalles de la URL" }

### Pestaña Response {#response-tab}

| Campo | Descripción |
| --- | --- |
| Duration | Cuánto tiempo tardó la solicitud en completarse, en segundos. La duración solo se muestra para llamadas en vivo (no almacenadas en caché). |
| Served from cache | Indica si esta respuesta se sirvió desde la caché de contenido conectado de Braze en lugar de una llamada en vivo a tu endpoint (`Yes` o `No`). Un resultado almacenado en caché refleja una respuesta anterior, no necesariamente el estado actual de tu endpoint. |
| Response body | El cuerpo devuelto por tu endpoint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pestaña Response" }

### Pestaña Request {#request-tab}

| Campo | Descripción |
| --- | --- |
| Headers | Encabezados de tu etiqueta de contenido conectado (`:headers`, credenciales y opciones como `:content_type`). |
| Body | El cuerpo de la solicitud enviado, si lo hay (solicitudes POST). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pestaña Request" }

## Qué encabezados de solicitud aparecen en el depurador {#which-request-headers-appear-in-the-debugger}

La pestaña **Request** muestra los encabezados de tu etiqueta de contenido conectado: `:headers` personalizados, credenciales almacenadas y encabezados configurados por opciones de la etiqueta como `:content_type` y `:basic_auth`. Braze también añade encabezados estándar a la solicitud saliente hacia tu endpoint (por ejemplo, `User-Agent` y `Host`). Esos encabezados añadidos por Braze aparecen en el depurador cuando los configuras en `:headers`.

{% alert note %}
Para enviar un `User-Agent` consistente, configúralo en `:headers`. Braze usa tu valor y el depurador muestra ese encabezado.
{% endalert %}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

## Redacción de credenciales {#credential-redaction}

Si tu etiqueta de contenido conectado utiliza `:basic_auth`, encabezados secretos comunes, claves u otras [opciones de credenciales de autenticación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types), el depurador redacta esos valores en la pestaña **Request** y los reemplaza con una serie de asteriscos (*). Esto te permite confirmar que las credenciales se incluyeron en la solicitud sin exponer los valores en **vista previa & Test**.

Los errores de autenticación siguen siendo visibles incluso cuando las credenciales están redactadas: si tu endpoint devuelve un `401` o `403`, ese código de estado aparece normalmente en la pestaña **Response**, de modo que puedes saber que tu solicitud fue rechazada por autenticación aunque la credencial en sí esté oculta.

## Solución de problemas de códigos de respuesta {#troubleshooting-response-codes}

### Errores de endpoint frente a límites impuestos por Braze {#endpoint-errors-versus-braze-imposed-limits}

No todos los códigos de estado que no sean `2XX` en la pestaña **Respuesta** provienen de tu endpoint. Braze impone sus propios límites en las llamadas de contenido conectado, y estos pueden producir respuestas que se parecen a un error de endpoint.

Si ves [códigos de respuesta]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#start-here-match-your-symptom) como `408`, `429`, `502`, `503`, `504` o `599`, el problema suele estar del lado de Braze en la llamada, relacionado con el estado del host, el tiempo de espera o el tamaño de la carga útil. Si tu endpoint devuelve respuestas grandes de forma consistente, considera recortar la carga útil de respuesta para incluir solo los campos que tu mensaje necesita.

### El endpoint devolvió un código de estado inesperado {#endpoint-returned-an-unexpected-status-code}

Usa la pestaña **Solicitud** para confirmar la URL, los encabezados de tu etiqueta y el cuerpo. Una causa común de respuestas `4XX` inesperadas es una etiqueta de Liquid dentro de la URL, los encabezados o el cuerpo que no se resolvió como esperabas. Comprueba que todas las referencias {% raw %}`{{ }}`{% endraw %} apunten a campos que existan para el usuario o contexto con el que estás previsualizando.

### La respuesta parece obsoleta {#response-looks-stale}

Revisa **Served from cache** en la pestaña **Respuesta**. Si muestra `Yes`, el depurador está mostrando una respuesta previamente almacenada en caché en lugar de una llamada nueva. Añade `:no_cache` a tu etiqueta temporalmente, o espera a que la caché expire (según `:cache_max_age`), para confirmar el comportamiento actual del endpoint.

## Artículos relacionados {#related-articles}

- [Referencia de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Realizar una llamada a la API de contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Encabezados de solicitud salientes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#outgoing-request-headers)
- [Solución de problemas de solicitudes de webhooks y contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)