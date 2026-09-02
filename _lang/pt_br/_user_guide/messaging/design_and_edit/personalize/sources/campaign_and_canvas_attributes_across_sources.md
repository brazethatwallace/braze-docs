---
nav_title: Atributos de Campaign e Canvas entre fontes
article_title: Atributos de Campaign e Canvas entre fontes
page_order: 1.5
page_type: reference
description: "Este artigo de referência compara nomes e IDs de atributos de Campaign e Canvas entre Liquid, a REST or transferir estado representacional API or interface de programação do aplicativo (API) e Currents."
---

# Atributos de Campaign e Canvas entre fontes {#campaign-and-canvas-attributes-across-sources}

> Nomes e IDs de Campaigns, Canvas e etapas do Canvas estão disponíveis em Liquid, na REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze e em Currents. Esses atributos correspondem ao mesmo valor nas três fontes, mas podem ter nomes diferentes. Use esta página para entender as conexões entre as três.

## Casos de uso {#use-cases}

### Liquid

Os atributos de Campaign e Canvas estão disponíveis como Liquid tags no dashboard {% raw %}(como `{{campaign.${api_id}}}`){% endraw %}. Use Liquid para passar esses atributos na própria mensagem, em uma chamada de Conteúdo conectado ou como pares de chave-valor. Isso geralmente é feito para fins de rastreamento.

### REST or transferir estado representacional API or interface de programação do aplicativo (API)

Os atributos de Campaign e Canvas também estão disponíveis no [endpoint Exportar detalhes da campanha]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) ou no [endpoint Exportar detalhes do Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details). Use a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze para criar mapeamentos — ou seja, uma lista de todos os nomes de Canvas e seus IDs correspondentes.

### Currents

Os atributos de Campaign e Canvas estão vinculados a [eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) do Currents. Observe que apenas etapas de Mensagem têm acesso aos atributos de Campaign, e outras etapas do Canvas têm acesso apenas aos atributos de Canvas. Isso é importante para que você possa determinar a qual Campaign ou componente do Canvas um envio de push ou abertura de e-mail está associado.

## Atributos de Campaign {#campaign-attributes}

| Atributo | Liquid | REST or transferir estado representacional API or interface de programação do aplicativo (API) | Currents |
| --- | --- | --- | --- |
| Nome da Campaign | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| ID da Campaign | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (usado como entrada para a própria chamada de API or interface de programação do aplicativo (API)) | campaign_id |
| Nome da variante | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (mapeie o nome da variante para o ID da variante usando o endpoint Exportar detalhes da campanha) |
| ID da variante | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos de Campaign" }

## Atributos de Canvas {#canvas-attributes}

| Atributo | Liquid | REST or transferir estado representacional API or interface de programação do aplicativo (API) | Currents |
| --- | --- | --- | --- |
| Nome do Canvas | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| ID do Canvas | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (usado como entrada para a própria chamada de API or interface de programação do aplicativo (API)) | canvas_id |
| Nome da variante | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| ID da variante | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Nome da etapa (apenas para etapas de Mensagem) | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| ID da etapa | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Canal da mensagem | N/A | `steps.messages.message_variation_id.channel` | N/A (inerente ao tipo de evento, como envio de push ou abertura de e-mail) |
| ID da mensagem | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos de Canvas" }