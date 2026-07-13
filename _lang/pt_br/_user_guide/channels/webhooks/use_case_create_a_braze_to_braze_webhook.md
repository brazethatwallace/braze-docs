---
nav_title: "Caso de uso: Criar um webhook Braze-para-Braze"
article_title: "Caso de uso: Criar um webhook Braze-para-Braze"
page_order: 2
channel:
  - webhooks
description: "Este artigo de referência aborda quando usar a Atualização de usuário em vez de webhooks Braze-para-Braze e como criar um webhook Braze-para-Braze."

---

# Criar um webhook Braze-para-Braze {#create-a-braze-to-braze-webhook}

> Os webhooks Braze-para-Braze permitem chamar a [REST API da Braze]({{site.baseurl}}/api/basics) de dentro da Braze usando um [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) em uma [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou [Canvas]({{site.baseurl}}/user_guide/messaging/canvas). Use isso para tarefas de orquestração, como disparar um [Canvas acionado por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Para atualizar [atributos de usuário]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou [compras]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) a partir do Canvas, use a [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em vez disso. Ela foi projetada para alterações no perfil de usuário e processa atualizações de forma mais eficiente.

Para aproveitar ao máximo este artigo, você deve estar familiarizado com [como os webhooks funcionam]({{site.baseurl}}/user_guide/channels/webhooks) e como [criar um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) na Braze.

## Use Enviar para Destino para disparar outro Canvas {#use-send-to-destination-for-triggering-another-canvas}

Para disparar um segundo Canvas de dentro de um Canvas, use [Enviar para Destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) em vez de um webhook Braze-para-Braze. Esse componente do Canvas foi projetado especificamente para conectar jornadas do Canvas e oferece uma maneira mais simples e eficiente de enviar usuários de um Canvas para outro.

Enviar para Destino avalia os usuários em relação aos critérios de entrada e público do Canvas de destino quando eles atingem a etapa, sem exigir configuração de webhook ou chaves de API. Os usuários que atendem aos critérios entram no Canvas de destino e podem continuar sua jornada no Canvas de origem se houver etapas adicionais.

{% alert tip %}
Adicione [Enviar para Destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) ao seu Canvas para enviar usuários a outra jornada do Canvas sem configurar webhooks ou chamadas de API.
{% endalert %}

## Use a Atualização de usuário para alterações em dados de usuários {#use-user-update-for-user-data-changes}

Para atualizar perfis de usuário de dentro de um Canvas, incluindo modificar [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), registrar [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou registrar [compras]({{site.baseurl}}/user_guide/data/activation/events/purchase_events), use a [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em vez de um webhook Braze-para-Braze.

A Atualização de usuário agrupa várias alterações e as envia em lotes, tornando-a mais rápida do que webhooks. É mais fácil de configurar do que um webhook e suporta atualizações complexas por meio do [criador avançado de JSON]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-composer). Por exemplo, para contar quantas vezes um usuário viu uma mensagem, use o [recurso de incremento e decremento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values) da Atualização de usuário em vez de um webhook Braze-para-Braze.

{% alert tip %}
Adicione a [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) ao seu Canvas para atualizar atributos, eventos e compras de um usuário usando um criador de JSON.
{% endalert %}

## Quando usar um webhook Braze-para-Braze {#when-to-use-a-braze-to-braze-webhook}

A Atualização de usuário pode lidar com quase todas as mesmas tarefas que um webhook Braze-para-Braze para atualizar perfis de usuário. Para atualizações complexas além de atributos personalizados simples, você pode usar o [criador avançado de JSON]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-composer).

Enviar para Destino oferece uma maneira mais simples de disparar um segundo Canvas de dentro do Canvas sem precisar de configuração de webhook.

Você pode usar um webhook Braze-para-Braze quando precisar chamar a [REST API]({{site.baseurl}}/api/basics) da Braze de dentro da Braze para cenários que não possuem um componente dedicado do Canvas. Exemplos comuns incluem:

- Disparar uma [Campaign acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) a partir de um Canvas
- Chamar outros [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) para padrões de orquestração em que um fluxo de trabalho na Braze precisa invocar uma API que não possui um componente dedicado do Canvas

Para atualizações de usuário dentro do Canvas, use a [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Para disparar outro Canvas, use [Enviar para Destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).

## Pré-requisitos {#prerequisites}

Para criar um webhook Braze-para-Braze, você precisa de uma [chave de API]({{site.baseurl}}/api/api_key) com permissões para o endpoint que deseja acessar. Por exemplo, para disparar um Canvas acionado por API, você precisa de uma chave de API com a permissão `canvas.trigger.send`.

## Configurando seu webhook Braze-para-Braze {#setting-up-your-braze-to-braze-webhook}

O fluxo de trabalho geral para criar um webhook Braze-para-Braze segue estas etapas:

1. [Crie um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) como uma Campaign ou componente do Canvas.
2. Escolha **Blank Template**.
3. Na guia **Compose**, especifique a **Webhook URL** e o **Request Body** para o seu caso de uso da API.
4. Na guia **Settings**, especifique o **HTTP Method** e os **Request Headers** conforme exigido pelo endpoint.
5. Configure quaisquer definições adicionais de entrega (por exemplo, disparo a partir de um evento personalizado) e construa o restante da sua Campaign ou Canvas.

## Disparar um segundo Canvas a partir de um Canvas inicial {#trigger-a-second-canvas-from-an-initial-canvas}

Neste caso de uso, você cria dois Canvas e usa um webhook Braze-para-Braze para disparar o segundo Canvas a partir do primeiro. Isso funciona como um gatilho de entrada para quando um usuário atinge um determinado ponto em outro Canvas.

1. Comece criando seu segundo Canvas — o Canvas que deve ser disparado pelo seu Canvas inicial.
2. Para o **Cronograma de entrada** do Canvas, selecione **API-Triggered**.
3. Anote o **Canvas ID**. Você precisará dele em uma etapa posterior.
4. Continue construindo as etapas do seu segundo Canvas e salve o Canvas.
5. Por fim, crie seu primeiro Canvas. Encontre a etapa em que deseja disparar o segundo Canvas e crie uma nova etapa com um webhook.

Consulte as informações a seguir ao configurar seu webhook:

- **Webhook URL:** A [URL do endpoint REST]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) seguida de `/canvas/trigger/send`. Por exemplo, para a instância `US-06`, a URL seria `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Request Body:** Raw Text

### Cabeçalhos e método da solicitação {#request-headers-and-method}

A Braze requer um cabeçalho HTTP para autorização que inclua sua chave de API e outro que declare o tipo de conteúdo.

- **Cabeçalhos da solicitação:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTP Method:** `POST`

Substitua `YOUR_API_KEY` por uma chave de API da Braze que tenha permissões `canvas.trigger.send`. Você pode criar uma chave de API no dashboard da Braze acessando **Configurações** > **Chaves de API**.

![Cabeçalhos da solicitação para o webhook mostrando os campos Authorization e Content-Type no dashboard da Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corpo da solicitação {#request-body}

Adicione sua solicitação `/canvas/trigger/send` no campo de texto. Para mais detalhes, consulte [Envio de mensagens do Canvas via entrega acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). A seguir está um exemplo do corpo da solicitação para este endpoint, onde `your_canvas_id` é o Canvas ID do seu segundo Canvas:

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

Quando um usuário atinge esta etapa de webhook no primeiro Canvas, a Braze dispara o segundo Canvas para esse usuário via API.

## Considerações {#considerations}

- **Atualizações de usuário:** Para atualizar perfis de usuário a partir do Canvas (atributos, eventos, compras), use a [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em vez de webhooks Braze-para-Braze para maior eficiência e custo-benefício.
- Os webhooks Braze-para-Braze estão sujeitos aos [limites de frequência]({{site.baseurl}}/api/api_limits) dos endpoints.
- Atualizações no perfil de usuário consomem [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points) que contam para o seu consumo total, enquanto disparar outra mensagem por meio dos endpoints de envio de mensagens não consome.
- Para segmentar [usuários anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles), use `braze_id` em vez de `external_id` no corpo da solicitação do seu webhook.
- Você pode salvar seu webhook Braze-para-Braze como um [modelo de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) para reutilização.
- Você pode verificar o [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para visualizar e solucionar problemas de falhas de webhook.