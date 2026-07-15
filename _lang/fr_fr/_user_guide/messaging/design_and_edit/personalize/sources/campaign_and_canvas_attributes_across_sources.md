---
nav_title: Attributs de Campaign et Canvas selon les sources
article_title: Attributs de Campaign et Canvas selon les sources
page_order: 1.5
page_type: reference
description: "Cet article de référence compare les noms et ID des attributs de Campaign et Canvas dans Liquid, la REST API et Currents."
---

# Attributs de Campaign et Canvas selon les sources {#campaign-and-canvas-attributes-across-sources}

> Les noms et ID de Campaign, Canvas et des étapes du Canvas sont tous disponibles dans Liquid, la REST API de Braze et Currents. Ces attributs correspondent à la même valeur dans les trois sources, mais peuvent être nommés différemment. Utilisez cette page pour établir les correspondances entre les trois.

## Cas d'utilisation {#use-cases}

### Liquid

Les attributs de Campaign et Canvas sont disponibles sous forme d'étiquettes Liquid dans le tableau de bord {% raw %}(par exemple `{{campaign.${api_id}}}`){% endraw %}. Utilisez Liquid pour transmettre ces attributs dans le message lui-même, dans un appel de contenu connecté ou sous forme de paires clé-valeur. Cela est généralement fait à des fins de suivi.

### REST API

Les attributs de Campaign et Canvas sont également disponibles dans l'[endpoint Exporter les détails d'une campagne]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) ou l'[endpoint Exporter les détails d'un Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details). Utilisez la REST API de Braze pour créer des mappages, c'est-à-dire une liste de tous les noms de Canvas et de leurs ID correspondants.

### Currents

Les attributs de Campaign et Canvas sont liés aux [événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) de Currents. Notez que seules les étapes Message ont accès aux attributs de Campaign, et les autres étapes du Canvas n'ont accès qu'aux attributs de Canvas. Cela est important pour déterminer à quelle Campaign ou à quel composant Canvas un envoi push ou une ouverture d'e-mail est associé.

## Attributs de Campaign {#campaign-attributes}

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Nom de la Campaign | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| ID de la Campaign | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (utilisé comme entrée pour l'appel API lui-même) | `campaign_id` |
| Nom de la variante | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (mapper le nom de la variante à l'ID de la variante à l'aide de l'endpoint Exporter les détails d'une campagne) |
| ID de la variante | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs de Campaign" }

## Attributs de Canvas {#canvas-attributes}

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Nom du Canvas | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| ID du Canvas | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (utilisé comme entrée pour l'appel API lui-même) | `canvas_id` |
| Nom de la variante | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| ID de la variante | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Nom de l'étape (pour les étapes Message uniquement) | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ID de l'étape | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Canal du message | N/A | `steps.messages.message_variation_id.channel` | N/A (inhérent au type d'événement, comme un envoi push ou une ouverture d'e-mail) |
| ID du message | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs de Canvas" }