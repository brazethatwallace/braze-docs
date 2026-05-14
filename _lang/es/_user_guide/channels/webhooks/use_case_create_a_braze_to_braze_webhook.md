---
nav_title: "Caso de uso: Crear un webhook de Braze a Braze"
article_title: "Caso de uso: Crear un webhook de Braze a Braze"
page_order: 2
channel:
  - webhooks
description: "Este artículo de referencia cubre cuándo usar Actualización de usuario frente a webhooks de Braze a Braze y cómo crear un webhook de Braze a Braze."

---

# Crear un webhook de Braze a Braze {#create-a-braze-to-braze-webhook}

> Los webhooks de Braze a Braze te permiten llamar a la [REST API de Braze]({{site.baseurl}}/api/basics/) desde dentro de Braze usando un [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) en una [campaña]({{site.baseurl}}/user_guide/messaging/campaigns/) o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/). Úsalos para tareas de orquestación como desencadenar un [Canvas activado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Para actualizar [atributos de usuario]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) o [compras]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/) desde Canvas, usa [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) en su lugar. Está diseñado para cambios en el perfil de usuario y procesa las actualizaciones de forma más eficiente.

Para sacar el máximo provecho de este artículo, deberías estar familiarizado con [cómo funcionan los webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) y cómo [crear un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) en Braze.

## Usa Actualización de usuario para cambios en datos de usuario {#use-user-update-for-user-data-changes}

Para actualizar perfiles de usuario desde dentro de un Canvas, incluyendo la modificación de [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), el registro de [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) o el registro de [compras]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/), usa [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) en lugar de un webhook de Braze a Braze.

Actualización de usuario agrupa múltiples cambios y los envía en lotes, lo que lo hace más rápido que los webhooks. Es más fácil de configurar que un webhook y admite actualizaciones complejas a través de su [compositor JSON avanzado]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#advanced-json-composer). Por ejemplo, para contar cuántas veces un usuario ha visto un mensaje, usa la [función de incremento y decremento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#increasing-and-decreasing-values) de Actualización de usuario en lugar de un webhook de Braze a Braze.

{% alert tip %}
Añade [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) a tu Canvas para actualizar los atributos, eventos y compras de un usuario usando un compositor JSON.
{% endalert %}

## Cuándo usar un webhook de Braze a Braze {#when-to-use-a-braze-to-braze-webhook}

Actualización de usuario puede manejar casi todas las mismas tareas que un webhook de Braze a Braze para actualizar perfiles de usuario. Para actualizaciones complejas más allá de atributos personalizados simples, puedes usar el [compositor JSON avanzado]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/#advanced-json-composer).

Puedes usar un webhook de Braze a Braze cuando necesites llamar a la [REST API]({{site.baseurl}}/api/basics/) de Braze desde dentro de Braze para escenarios distintos a las actualizaciones directas de usuario desde pasos en Canvas. Ejemplos comunes incluyen:

- Desencadenar un [Canvas activado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) desde otro Canvas
- Llamar a otros [puntos de conexión de mensajería]({{site.baseurl}}/api/endpoints/messaging/) para patrones de orquestación donde un flujo de trabajo en Braze necesita invocar una API que no tiene un componente de Canvas dedicado

Para actualizaciones de usuario dentro de Canvas, el método recomendado es usar [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/).

## Requisitos previos {#prerequisites}

Para crear un webhook de Braze a Braze, necesitas una [clave de API]({{site.baseurl}}/api/api_key/) con permisos para el punto de conexión al que deseas acceder. Por ejemplo, para desencadenar un Canvas activado por API, necesitas una clave de API con el permiso `canvas.trigger.send`.

## Configurar tu webhook de Braze a Braze {#setting-up-your-braze-to-braze-webhook}

El flujo de trabajo general para crear un webhook de Braze a Braze sigue estos pasos:

1. [Crea un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) como campaña o componente de Canvas.
2. Elige **Blank Template**.
3. En la pestaña **Compose**, especifica la **Webhook URL** y el **Request Body** para tu caso de uso de API.
4. En la pestaña **Settings**, especifica tu **HTTP Method** y los **Request Headers** según lo requiera el punto de conexión.
5. Configura cualquier ajuste de entrega adicional (por ejemplo, desencadenar desde un evento personalizado) y completa el resto de tu campaña o Canvas.

## Desencadenar un segundo Canvas desde un Canvas inicial {#trigger-a-second-canvas-from-an-initial-canvas}

En este caso de uso, creas dos Canvas y usas un webhook de Braze a Braze para desencadenar el segundo Canvas desde el primero. Esto actúa como un desencadenante de entrada para cuando un usuario alcanza un punto determinado en otro Canvas.

1. Comienza creando tu segundo Canvas, el Canvas que debería ser desencadenado por tu Canvas inicial.
2. Para el **Entry Schedule** del Canvas, selecciona **API-Triggered**.
3. Toma nota de tu **Canvas ID**. Lo necesitarás en un paso posterior.
4. Continúa construyendo los pasos de tu segundo Canvas y luego guarda el Canvas.
5. Finalmente, crea tu primer Canvas. Encuentra el paso donde deseas desencadenar el segundo Canvas y crea un nuevo paso con un webhook.

Consulta lo siguiente al configurar tu webhook:

- **Webhook URL:** Tu [URL del punto de conexión REST]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/) seguida de `/canvas/trigger/send`. Por ejemplo, para la instancia `US-06`, la URL sería `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Request Body:** Raw Text

#### Encabezados de solicitud y método {#request-headers-and-method}

Braze requiere un encabezado HTTP para autorización que incluya tu clave de API y otro que declare tu tipo de contenido.

- **Request Headers:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTP Method:** `POST`

Reemplaza `YOUR_API_KEY` con una clave de API de Braze que tenga permisos `canvas.trigger.send`. Puedes crear una clave de API en el panel de Braze yendo a **Settings** > **API Keys**.

![Encabezados de solicitud para el webhook mostrando los campos Authorization y Content-Type en el panel de Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud {#request-body}

Añade tu solicitud `/canvas/trigger/send` en el campo de texto. Para más detalles, consulta [Enviar mensajes de Canvas mediante entrega activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). El siguiente es un ejemplo del cuerpo de la solicitud para este punto de conexión, donde `your_canvas_id` es el Canvas ID de tu segundo Canvas:

{% raw %}
```json
{
  "canvas_id": "your_canvas_id",
  "recipients": [
    {
      "external_user_id": "{{${user_id}}}"
    }
  ]
}
```
{% endraw %}

Cuando un usuario alcanza este paso de webhook en el primer Canvas, Braze desencadena el segundo Canvas para ese usuario a través de la API.

## Consideraciones {#considerations}

- **Actualizaciones de usuario:** Para actualizar perfiles de usuario desde Canvas (atributos, eventos, compras), usa [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/) en lugar de webhooks de Braze a Braze para mayor eficiencia y rentabilidad.
- Los webhooks de Braze a Braze están sujetos a los [límites de velocidad]({{site.baseurl}}/api/api_limits/) de los puntos de conexión.
- Las actualizaciones al perfil de usuario generan [puntos de datos]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) que cuentan para tu consumo total, mientras que desencadenar otro mensaje a través de los puntos de conexión de mensajería no lo hace.
- Para dirigirte a [usuarios anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#anonymous-user-profiles), usa `braze_id` en lugar de `external_id` en el cuerpo de la solicitud de tu webhook.
- Puedes guardar tu webhook de Braze a Braze como una [plantilla de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates/) para reutilizarlo.
- Puedes consultar el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) para ver y solucionar errores de webhooks.