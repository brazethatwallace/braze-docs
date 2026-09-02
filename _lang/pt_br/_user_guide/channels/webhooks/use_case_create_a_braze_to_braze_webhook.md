---
nav_title: "Caso de uso: Criar um webhook Braze-para-Braze"
article_title: "Caso de uso: Criar um webhook Braze-para-Braze"
page_order: 2
channel:
  - webhooks
description: "Este artigo de referência aborda quando usar a Atualização de usuário em vez de webhooks Braze-para-Braze e como criar um webhook Braze-para-Braze."
---

# Criar um webhook Braze-para-Braze {#create-a-braze-to-braze-webhook}

> Os webhooks Braze-para-Braze permitem chamar a [REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze]({{site.baseurl}}/api/basics) de dentro da Braze usando um [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) em uma [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou [Canvas]({{site.baseurl}}/user_guide/messaging/canvas). Use isso para tarefas de orquestração, como disparar um [Canvas acionado por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Para atualizar [atributos de usuário]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou [compras]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) a partir do Canvas, use a [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em vez disso. Ela foi projetada para alterações no perfil de usuário e processa atualizações de forma mais eficiente.

Para aproveitar ao máximo este artigo, você deve estar familiarizado com [como os webhooks funcionam]({{site.baseurl}}/user_guide/channels/webhooks) e como [criar um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) na Braze.

## Use Enviar para destino para disparar outro Canvas {#use-send-to-destination-for-triggering-another-canvas}

Para disparar um segundo Canvas de dentro de um Canvas, use [Enviar para destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) em vez de um webhook Braze-to-Braze. Esse componente do Canvas foi projetado especificamente para conectar jornadas do Canvas e oferece uma maneira mais simples e eficiente de enviar usuários de um Canvas para outro.

O Enviar para destino avalia os usuários com base nos critérios de entrada e público do Canvas de destino quando eles chegam à etapa, sem precisar de configuração de webhook ou chaves de API or interface de programação do aplicativo (API). Os usuários que atendem aos critérios entram no Canvas de destino e podem continuar sua jornada no Canvas de origem se houver etapas adicionais.

{% alert tip %}
Adicione [Enviar para destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) ao seu Canvas para enviar usuários a outra jornada do Canvas sem configurar webhooks ou chamadas de API or interface de programação do aplicativo (API).
{% endalert %}

## Use User Update para alterações nos dados de usuários {#use-user-update-for-user-data-changes}

Para atualizar perfis de usuário de dentro de um Canvas, incluindo modificar [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), registrar [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou registrar [compras]({{site.baseurl}}/user_guide/data/activation/events/purchase_events), use o [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em vez de um webhook da Braze para a Braze.

O User Update agrupa várias alterações e as envia em lotes, tornando-o mais rápido do que webhooks. É mais fácil de configurar do que um webhook e oferece suporte a atualizações complexas por meio do seu [criador JSON avançado]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor). Por exemplo, para contar quantas vezes um usuário viu uma mensagem, use o [recurso de incremento e decremento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#increasing-and-decreasing-values) do User Update em vez de um webhook da Braze para a Braze.

{% alert tip %}
Adicione o [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) ao seu Canvas para atualizar atributos, eventos e compras de um usuário usando um criador JSON.
{% endalert %}

## Quando usar um webhook Braze-para-Braze {#when-to-use-a-braze-to-braze-webhook}

A Atualização de Usuário pode lidar com quase todas as mesmas tarefas que um webhook Braze-para-Braze para atualizar perfis de usuário. Para atualizações complexas além de atributos personalizados simples, você pode usar o [criador avançado de JSON]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#advanced-json-editor).

O Enviar para Destino oferece uma maneira mais simples de disparar um segundo Canvas de dentro de um Canvas sem precisar de configuração de webhook.

Você pode usar um webhook Braze-para-Braze quando precisar chamar a [REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics) da Braze de dentro da Braze para cenários que não têm um componente dedicado no Canvas. Exemplos comuns incluem:

- Disparar uma [Campaign acionada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) a partir de um Canvas
- Chamar outros [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) para padrões de orquestração em que um fluxo de trabalho na Braze precisa invocar uma API or interface de programação do aplicativo (API) que não tem um componente dedicado no Canvas

Para atualizações de usuário dentro do Canvas, use a [Atualização de Usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Para disparar outro Canvas, use [Enviar para Destino]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).

## Pré-requisitos {#prerequisites}

Para criar um webhook Braze-para-Braze, você precisa de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics) com permissões para o endpoint que deseja acessar. Por exemplo, para disparar um Canvas acionado por API or interface de programação do aplicativo (API), você precisa de uma chave de API or interface de programação do aplicativo (API) com a permissão `canvas.trigger.send`.

## Configurando seu webhook Braze-para-Braze {#setting-up-your-braze-to-braze-webhook}

O fluxo geral para criar um webhook Braze-para-Braze segue estas etapas:

1. [Crie um webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) como uma Campaign ou componente do Canvas.
2. Escolha **Blank Template**.
3. Na guia **Compose**, especifique a **Webhook URL** e o **Request Body** para seu caso de uso de API or interface de programação do aplicativo (API).
4. Na guia **Settings**, especifique seu **HTTP Method** e os **Request Headers** conforme exigido pelo endpoint.
5. Configure quaisquer definições adicionais de entrega (por exemplo, disparo a partir de um evento personalizado) e finalize o restante da sua Campaign ou Canvas.

## Disparar um segundo Canvas a partir de um Canvas inicial {#trigger-a-second-canvas-from-an-initial-canvas}

Neste caso de uso, você cria dois Canvas e usa um webhook Braze-to-Braze para disparar o segundo Canvas a partir do primeiro. Isso funciona como um gatilho de entrada para quando um usuário alcança um determinado ponto em outro Canvas.

{% alert note %}
O gatilho **Interact with Canvas Step** está disponível apenas para Campaigns, não para entrada de Canvas baseada em ação. Se você precisa disparar um Canvas com base em um usuário que alcançou uma etapa específica em outro Canvas, use esta abordagem de webhook Braze-to-Braze ou o componente de Canvas [Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination).
{% endalert %}

1. Comece criando o segundo Canvas — o Canvas que deve ser disparado pelo Canvas inicial.
2. Para o **Entry agendar/cronograma** do Canvas, selecione **API or interface de programação do aplicativo (API)-Triggered**.
3. Anote o **Canvas ID**. Você precisará dele em uma etapa posterior.
4. Continue criando as etapas do segundo Canvas e salve o Canvas.
5. Por fim, crie o primeiro Canvas. Encontre a etapa em que você deseja disparar o segundo Canvas e crie uma nova etapa com um webhook.

Consulte as informações a seguir ao configurar seu webhook:

- **URL do webhook:** A [URL do endpoint REST or transferir estado representacional]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) seguida de `/canvas/trigger/send`. Por exemplo, para a instância `US-06`, a URL seria `https://rest.iad-06.braze.com/canvas/trigger/send`.
- **Corpo da solicitação:** Texto bruto

### Cabeçalhos da solicitação e método {#request-headers-and-method}

A Braze requer um cabeçalho HTTP para autorização que inclui sua chave de API or interface de programação do aplicativo (API) e outro que declara o tipo de conteúdo.

- **Cabeçalhos da solicitação:**
  - **Authorization:** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **Método HTTP:** `POST`

Substitua `YOUR_API_KEY` por uma chave de API or interface de programação do aplicativo (API) da Braze que tenha permissões de `canvas.trigger.send`. Você pode criar uma chave de API or interface de programação do aplicativo (API) no dashboard da Braze acessando **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.

![Cabeçalhos da solicitação para o webhook mostrando os campos Authorization e Content-Type no dashboard da Braze.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Corpo da solicitação {#request-body}

Adicione a solicitação `/canvas/trigger/send` no campo de texto. Para mais detalhes, consulte [Envio de mensagens do Canvas via entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases). A seguir, um exemplo do corpo da solicitação para esse endpoint, onde `your_canvas_id` é o Canvas ID do segundo Canvas:

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

Quando um usuário alcança essa etapa do webhook no primeiro Canvas, a Braze dispara o segundo Canvas para esse usuário por meio da API or interface de programação do aplicativo (API).

## Considerações {#considerations}

- **Atualizações de usuários:** Para atualizar perfis de usuário a partir do Canvas (atributos, eventos, compras), use a [Atualização de Usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em vez de webhooks Braze-para-Braze para melhor eficiência e custo-benefício.
- Os webhooks Braze-para-Braze estão sujeitos aos [Limites de frequência]({{site.baseurl}}/api/api_limits) de endpoint.
- Atualizações no perfil de usuário geram [Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points) que contam para o seu consumo total, enquanto disparar outra mensagem por meio dos endpoints de envio de mensagens não gera.
- Para direcionar [Usuários anônimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles), use `braze_id` em vez de `external_id` no corpo da solicitação do seu webhook.
- Você pode salvar seu webhook Braze-para-Braze como um [modelo de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates) para reutilização.
- Você pode verificar o [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) para visualizar e solucionar falhas de webhook.