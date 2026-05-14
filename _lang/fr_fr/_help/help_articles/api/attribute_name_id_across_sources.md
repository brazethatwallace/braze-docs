---
nav_title: Différences entre les attributs de campagne et de Canvas dans Braze
article_title: Différences entre les attributs de campagne et de Canvas dans Braze
page_order: 1

page_type: reference
description: "Cet article d'aide compare les noms et ID d'attributs de campagne et de Canvas selon les différentes sources dans Braze."
platform: API
---

# Comment les attributs de campagne et de Canvas diffèrent selon les sources dans Braze {#how-campaign-and-canvas-attributes-differ-across-sources-in-braze}

Les noms et ID de campagne, de Canvas et d'étape du canvas sont tous disponibles dans Liquid, notre REST API et Currents. Ces attributs correspondent à la même valeur dans les trois sources, mais peuvent avoir des noms différents. Cette page est destinée à vous aider à établir les liens entre ces trois sources.

## Cas d'utilisation {#use-cases}

### Liquid

Les attributs de campagne et de Canvas sont disponibles sous forme d'étiquettes Liquid dans notre tableau de bord {% raw %}(comme `{{campaign.${api_id}}}`){% endraw %}. Vous pouvez utiliser Liquid pour transmettre ces attributs dans le message lui-même, dans un appel de contenu connecté ou en tant que paires clé-valeur. Cela est généralement fait à des fins de suivi.

### REST API

Les attributs de campagne et de Canvas sont également disponibles dans l'[endpoint Exporter les détails de la campagne]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) ou l'[endpoint Exporter les détails du Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/). Vous pouvez utiliser notre REST API pour créer des mappages, c'est-à-dire une liste de tous les noms de Canvas et de leurs ID correspondants.

### Currents

Les attributs de campagne et de Canvas sont liés aux [événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) de Currents. Notez que seules les étapes Message ont accès aux attributs de campagne, et les autres étapes du canvas n'ont accès qu'aux attributs de Canvas. Cela est important pour pouvoir déterminer à quelle campagne ou à quel composant Canvas un envoi push ou une ouverture d'e-mail est associé.

## Attributs de campagne {#campaign-attributes}

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Nom de la campagne | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| ID de la campagne | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | S.O. (utilisé comme entrée pour l'appel API lui-même) | `campaign_id` |
| Nom de la variante | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | S.O. (mappez le nom de la variante à l'ID de la variante à l'aide de l'endpoint Exporter les détails de la campagne) |
| ID de la variante | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs de campagne" }

## Attributs de Canvas {#canvas-attributes}

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Nom du Canvas | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| ID du Canvas | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | S.O. (utilisé comme entrée pour l'appel API lui-même) | `canvas_id` |
| Nom de la variante | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| ID de la variante | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Nom de l'étape (pour les étapes Message uniquement) | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ID de l'étape | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Canal de message | S.O. | `steps.messages.message_variation_id.channel` | S.O. (inhérent au type d'événement, par exemple envoi push ou ouverture d'e-mail) |
| ID de message | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Attributs de Canvas" }