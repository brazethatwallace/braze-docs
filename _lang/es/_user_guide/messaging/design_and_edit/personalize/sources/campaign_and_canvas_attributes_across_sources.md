---
nav_title: Atributos de Campaign y Canvas en distintas fuentes
article_title: Atributos de Campaign y Canvas en distintas fuentes
page_order: 1.5
page_type: reference
description: "Este artículo de referencia compara los nombres e ID de atributos de Campaign y Canvas en Liquid, la REST API y Currents."
---

# Atributos de Campaign y Canvas en distintas fuentes {#campaign-and-canvas-attributes-across-sources}

> Los nombres e ID de Campaign, Canvas y pasos en Canvas están disponibles en Liquid, la REST API de Braze y Currents. Estos atributos se corresponden con el mismo valor en las tres fuentes, pero pueden tener nombres diferentes. Usa esta página para establecer las conexiones entre las tres.

## Casos de uso {#use-cases}

### Liquid

Los atributos de Campaign y Canvas están disponibles como etiquetas de Liquid en el dashboard {% raw %}(como `{{campaign.${api_id}}}`){% endraw %}. Usa Liquid para pasar estos atributos en el propio mensaje, en una llamada de contenido conectado o como pares clave-valor. Esto se hace normalmente con fines de seguimiento.

### REST API

Los atributos de Campaign y Canvas también están disponibles en el [punto de conexión Exportar detalles de Campaign]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) o en el [punto de conexión Exportar detalles de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/). Usa la REST API de Braze para crear mapeados, es decir, una lista de todos los nombres de Canvas y sus ID correspondientes.

### Currents

Los atributos de Campaign y Canvas están vinculados a los [eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) de Currents. Ten en cuenta que solo los pasos de mensaje tienen acceso a los atributos de Campaign, y los demás pasos en Canvas solo tienen acceso a los atributos de Canvas. Esto es importante para poder determinar con qué Campaign o componente de Canvas está asociado un envío push o una apertura de correo electrónico.

## Atributos de Campaign {#campaign-attributes}

| Atributo | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Nombre de Campaign | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| ID de Campaign | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (se usa como entrada para la propia llamada a la API) | `campaign_id` |
| Nombre de variante | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (mapea el nombre de variante al ID de variante usando el punto de conexión Exportar detalles de Campaign) |
| ID de variante | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaign attributes" }

## Atributos de Canvas {#canvas-attributes}

| Atributo | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Nombre de Canvas | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| ID de Canvas | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (se usa como entrada para la propia llamada a la API) | `canvas_id` |
| Nombre de variante | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| ID de variante | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Nombre de paso (solo para pasos de mensaje) | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ID de paso | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Canal de mensaje | N/A | `steps.messages.message_variation_id.channel` | N/A (inherente al tipo de evento, como envío push o apertura de correo electrónico) |
| ID de mensaje | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas attributes" }