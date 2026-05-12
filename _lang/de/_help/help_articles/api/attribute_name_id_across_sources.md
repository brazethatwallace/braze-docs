---
nav_title: Unterschiede zwischen Campaign- und Canvas-Attributen in Braze
article_title: Unterschiede zwischen Campaign- und Canvas-Attributen in Braze
page_order: 1

page_type: reference
description: "Dieser Hilfeartikel vergleicht die Namen und IDs von Campaign- und Canvas-Attributen in verschiedenen Quellen in Braze."
platform: API
---

# Wie sich Campaign- und Canvas-Attribute zwischen den Quellen in Braze unterscheiden {#how-campaign-and-canvas-attributes-differ-across-sources-in-braze}

Die Namen und IDs von Campaigns, Canvases und Canvas-Schritten sind alle in Liquid, unserer REST API und Currents verfügbar. Diese Attribute werden in allen drei Quellen auf denselben Wert abgebildet, können aber unterschiedlich benannt sein. Diese Seite soll Ihnen helfen, Verbindungen zwischen den drei Bereichen herzustellen.

## Anwendungsfälle {#use-cases}

### Liquid

Campaign- und Canvas-Attribute sind als Liquid-Tags in unserem Dashboard {% raw %}(wie `{{campaign.${api_id}}}`){% endraw %} verfügbar. Sie können Liquid verwenden, um diese Attribute in der Nachricht selbst, in einem Connected-Content-Aufruf oder als Schlüssel-Wert-Paare zu übergeben. Dies geschieht in der Regel zu Tracking-Zwecken.

### REST API

Campaign- und Canvas-Attribute sind auch im [Endpunkt „Campaign-Details exportieren“]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) oder im [Endpunkt „Canvas-Details exportieren“]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) verfügbar. Sie können unsere REST API verwenden, um Abbildungen zu erstellen – also eine Liste aller Canvas-Namen und ihrer entsprechenden IDs.

### Currents

Campaign- und Canvas-Attribute sind mit [Nachrichten-Engagement-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) von Currents verknüpft. Beachten Sie, dass nur Nachrichten-Schritte Zugriff auf Campaign-Attribute haben und andere Canvas-Schritte nur Zugriff auf Canvas-Attribute haben. Dies ist wichtig, damit Sie feststellen können, welcher Campaign oder Canvas-Komponente eine Push-Sendung oder eine E-Mail-Öffnung zuzuordnen ist.

## Campaign-Attribute {#campaign-attributes}

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Campaign-Name | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Campaign-ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (wird als Eingabe für den API-Aufruf selbst verwendet) | `campaign_id` |
| Variantenname | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (Abbildung des Variantennamens auf die Varianten-ID mithilfe des Endpunkts „Campaign-Details exportieren“) |
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
| Nachrichtenkanal | N/A | `steps.messages.message_variation_id.channel` | N/A (abhängig vom Event-Typ, z. B. Push-Sendung oder E-Mail-Öffnung) |
| Nachrichten-ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas-Attribute" }