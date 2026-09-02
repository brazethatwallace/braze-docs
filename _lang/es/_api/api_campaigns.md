---
nav_title: Campañas API
article_title: Campañas de API
page_order: 5
description: "Este artículo de referencia explica cómo generar un campaign_id para incluirlo en tus llamadas a la API y cómo configurar esa campaña."
page_type: reference
tool: Campaigns
---

# Campañas API {#api-campaigns}

> Este artículo de referencia explica cómo generar un `campaign_id` para incluirlo en tus llamadas a la API y cómo configurar esa campaña.

Las campañas de API suelen utilizarse para mensajería transaccional. Al crear campañas API (no [campañas activadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)), el panel de Braze solo se utiliza para generar un `campaign_id`, que te permite hacer un seguimiento de los análisis para los informes de campaña. También puedes generar un ID de variante del mensaje, que es diferente para cada variante de tu campaña.

A continuación, envía esa información a tu equipo de desarrollo para que la utilice en la solicitud de API, junto con lo siguiente:
- Texto de la campaña
- Pertenencia a la audiencia
- Activos

Una vez iniciada la campaña, puedes ver los resultados en el panel. Las campañas API utilizan las [API de mensajería]({{site.baseurl}}/api/endpoints/messaging) de Braze, que tienen las mismas opciones detalladas de informes y reorientación que las campañas creadas completamente a través del panel.

Dado que las campañas API siempre incluyen un `campaign_id`, sus envíos se reflejan en las estadísticas del panel. Si llamas a [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) sin un `campaign_id`, Braze no incrementa esas métricas: los envíos siguen apareciendo en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), pero no en las métricas de rendimiento de correo electrónico del panel.

{% alert warning %}
Como las campañas API suelen ser transaccionales, todos los usuarios son elegibles para las campañas API, incluso los de tu grupo de control global. No se añade un encabezado de [cancelar suscripción con un clic]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) a estos envíos de forma predeterminada. Para añadir un encabezado de cancelación de suscripción con un solo clic a una campaña de API, consulta [Añadir cancelación de suscripción con un clic a campañas de API](#add-one-click-list-unsubscribe-to-api-campaigns). Para añadir un encabezado de cancelación de suscripción con un solo clic a todas las campañas de API, ponte en contacto con tu administrador de éxito de cliente.
{% endalert %}

## Crear una nueva Campaign {#create-a-new-campaign}

Ve a **Mensajería** > **Campaigns** y selecciona **Crear Campaign**, luego selecciona **API Campaigns**. Ahora puedes pasar a configurar tu Campaign de API.

Una [Campaign activada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) es diferente de una Campaign de API.

## Configura tu Campaign {#configure-your-campaign}

Para configurar tu Campaign, sigue estos pasos:

1. Añade un título descriptivo para que puedas encontrar los resultados en la página de Campaigns después de enviar tus mensajes.
2. Selecciona **Add Message** y añade los tipos de mensaje incluidos en tu Campaign de API. Esto te permite generar un `campaign_id` y un ID de variante de mensaje, que difiere para cada canal que incluyas.
3. Opcionalmente, puedes añadir un evento de conversión para realizar un seguimiento de las conversiones de los usuarios en una acción o un objetivo de Campaign específico.
4. Selecciona **Save Campaign** para iniciar tu Campaign de API.

## Llamadas a la API {#api-calls}

Después de guardar tu Campaign de API, incluye lo siguiente en tu solicitud de API:

- Los campos `campaign_id` generados con tu solicitud de API donde se indique en los [endpoints de envío de mensajes]({{site.baseurl}}/api/endpoints/messaging).
- Un [objeto de mensaje]({{site.baseurl}}/api/objects_filters#messaging-objects) para cada plataforma incluida en la Campaign. En el objeto de mensaje, proporciona el ID de variante del mensaje. Esto especifica que las estadísticas deben recopilarse y mostrarse bajo esa variante. Se admiten los siguientes objetos de mensaje: Android, Content Cards, correo electrónico, iOS, Kindle, SMS/MMS, notificación push web y webhook.

## Añadir la cancelación de suscripción con un clic en lista a las Campaigns de API {#add-one-click-list-unsubscribe-to-api-campaigns}

{% raw %}
De forma predeterminada, Braze no añade el encabezado de cancelación de suscripción con un clic en lista a las Campaigns de API. Puedes añadir este encabezado a envíos individuales de Campaigns de API incluyendo la etiqueta de Liquid `{{${set_user_to_one_click_list_unsubscribe}}}` en el campo de encabezados de correo electrónico de tu solicitud de API.
{% endraw %}

Para cumplir con [RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058) para la cancelación de suscripción con un clic en lista, incluye los encabezados `List-Unsubscribe` y `List-Unsubscribe-Post` en tu solicitud de API:

{% raw %}
```json
{
  "external_user_ids": ["user_id"],
  "messages": {
    "email": {
      "app_id": "your_app_id",
      "subject": "Your Subject",
      "from": "Sender Name <sender@example.com>",
      "body": "<p>Email body content</p>",
      "headers": {
        "List-Unsubscribe": "<{{${set_user_to_one_click_list_unsubscribe}}}>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
      }
    }
  }
}
```
{% endraw %}

{% alert note %}
La inclusión de estos encabezados no garantiza que el cliente de correo electrónico muestre un botón para cancelar la suscripción. Los clientes de correo electrónico deciden si muestran la opción de cancelación de suscripción en función de factores como la reputación del remitente y el contenido del mensaje.
{% endalert %}

### Añadir archivos adjuntos de correo electrónico {#add-email-attachments}

Para añadir archivos adjuntos a los correos electrónicos de Campaigns de API, incluye un array `attachments` en el [objeto de correo electrónico]({{site.baseurl}}/api/objects_filters/messaging/email_object). Puedes hacer referencia a una plantilla de correo electrónico creada en el editor de arrastrar y soltar o en el editor HTML proporcionando su `email_template_id` en el objeto de correo electrónico y, a continuación, añadir los archivos adjuntos a través de la llamada a la API.

Para obtener detalles sobre archivos adjuntos, límites de tamaño y prácticas recomendadas, consulta [Ejemplo de objeto de correo electrónico con archivo adjunto]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).