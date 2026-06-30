---
nav_title: Campaign- und Canvas-Attribute über Quellen hinweg
article_title: Campaign- und Canvas-Attribute über Quellen hinweg
page_order: 1.5
page_type: reference
description: "Dieser Referenzartikel vergleicht die Attributnamen und IDs von Campaigns und Canvas über Liquid, die REST API und Currents hinweg."
---

# Campaign- und Canvas-Attribute über Quellen hinweg {#campaign-and-canvas-attributes-across-sources}

> Campaign-, Canvas- und Canvas-Schritt-Namen und -IDs sind alle in Liquid, der Braze REST API und Currents verfügbar. Diese Attribute bilden in allen drei Quellen denselben Wert ab, können jedoch unterschiedlich benannt sein. Verwenden Sie diese Seite, um die Zusammenhänge zwischen den drei Quellen herzustellen.

## Anwendungsfälle {#use-cases}

### Liquid

Campaign- und Canvas-Attribute sind als Liquid-Tags im Dashboard verfügbar {% raw %}(z. B. `{{campaign.${api_id}}}`){% endraw %}. Verwenden Sie Liquid, um diese Attribute in der Nachricht selbst, in einem Connected-Content-Aufruf oder als Schlüssel-Wert-Paare zu übergeben. Dies wird in der Regel zu Tracking-Zwecken durchgeführt.

### REST API

Campaign- und Canvas-Attribute sind auch im [Endpunkt „Campaign-Details exportieren“]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) oder im [Endpunkt „Canvas-Details exportieren“]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) verfügbar. Verwenden Sie die Braze REST API, um Abbildungen zu erstellen – also eine Liste aller Canvas-Namen und ihrer zugehörigen IDs.

### Currents

Campaign- und Canvas-Attribute sind mit [Nachrichten-Engagement-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) aus Currents verknüpft. Beachten Sie, dass nur Nachrichten-Schritte Zugriff auf Campaign-Attribute haben und andere Canvas-Schritte nur Zugriff auf Canvas-Attribute haben. Dies ist wichtig, damit Sie bestimmen können, mit welcher Campaign oder welcher Canvas-Komponente ein Push-Versand oder eine E-Mail-Öffnung verknüpft ist.

## Campaign-Attribute {#campaign-attributes}

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Campaign-Name | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Campaign-ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (wird als Eingabe für den API-Aufruf selbst verwendet) | `campaign_id` |
| Variantenname | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (Variantenname über den Endpunkt „Campaign-Details exportieren“ der Varianten-ID zuordnen) |
| Varianten-ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaign-Attribute" }

## Canvas-Attribute {#canvas-attributes}

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Canvas-Name | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| Canvas-ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (wird als Eingabe für den API-Aufruf selbst verwendet) | `canvas_id` |
| Variantenname | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| Varianten-ID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Schrittname (nur für Nachrichten-Schritte) | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| Schritt-ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Nachrichtenkanal | N/A | `steps.messages.message_variation_id.channel` | N/A (ergibt sich aus dem Event-Typ, z. B. Push-Versand oder E-Mail-Öffnung) |
| Nachrichten-ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas-Attribute" }