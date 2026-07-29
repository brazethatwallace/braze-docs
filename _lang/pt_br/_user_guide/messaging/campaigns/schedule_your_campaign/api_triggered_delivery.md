---
nav_title: Entrega disparada por API
article_title: Entrega disparada por API
page_order: 2
page_type: reference
description: "Este artigo de referência descreve como agendar e configurar uma campanha disparada por API."
tool: Campaigns
platform: API

---

# Entrega disparada por API {#api-triggered-delivery}

> Campanhas disparadas por API ou campanhas disparadas por servidor são ideais para casos de uso transacionais mais avançados. As campanhas disparadas por API da Braze permitem que profissionais de marketing gerenciem o texto da campanha, testes multivariantes e regras de reelegibilidade dentro do dashboard da Braze, enquanto disparam a entrega desse conteúdo a partir de seus próprios servidores e sistemas. A requisição de API para disparar a mensagem também pode incluir dados adicionais para serem inseridos na mensagem em tempo real por meio de templates.

## Configurando uma campanha disparada por API {#setting-up-an-api-triggered-campaign}

Configurar uma campanha disparada por API requer algumas etapas. Primeiro, crie uma nova campanha multicanal ou de canal individual (com testes multivariantes).

{% alert note %}
Uma campanha disparada por API é diferente de uma [campanha da API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns#api-campaigns).
{% endalert %}

Em seguida, configure seu texto e notificações da mesma forma que faria normalmente para notificações agendadas e selecione **API-Triggered Delivery**. Para saber mais sobre como disparar essas campanhas a partir do seu servidor, confira este artigo sobre [envio de campanhas disparadas por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

![Configure seu texto e notificações da mesma forma que faria normalmente para notificações agendadas e selecione API-Triggered Delivery. Para saber mais sobre como disparar essas campanhas a partir do seu servidor, confira o artigo sobre envio de campanhas disparadas por API.]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Reduzindo a postergação entre o disparo da API e o envio {#reducing-delay-between-your-api-trigger-and-send}

Se as mensagens demorarem mais do que o esperado para serem enviadas após você chamar o endpoint de disparo, verifique se o perfil de usuário está pronto no momento do disparo.

Por padrão, `send_to_existing_only` é `true` em [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). A Braze envia apenas para usuários existentes e não cria perfis novos nessa chamada. Para criar ou atualizar um usuário e enviar na mesma requisição, defina `send_to_existing_only` como `false` e inclua um objeto `attributes` em cada destinatário.

Para campanhas de e-mail, inclua também `email` (e quaisquer outros campos de entrega obrigatórios) dentro de `attributes`. Se o perfil não tiver um endereço de e-mail quando você disparar o envio, a Braze faz novas tentativas por aproximadamente 2 horas enquanto aguarda a chegada dos dados do perfil. Incluir `email` na mesma chamada evita essa postergação.

Para ver todos os parâmetros da requisição, exemplos e comportamento de novas tentativas, consulte [Enviar campanhas disparadas por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#recipient-limits-and-profile-creation) e o [objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object).

{% alert note %}
Essa orientação se aplica a campanhas disparadas por API (`/campaigns/trigger/send`). O [endpoint de e-mail de transação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) usa um formato de requisição diferente (`recipient`, no singular) e não oferece suporte a `send_to_existing_only`. Para criar um usuário inline com envios transacionais, passe `attributes` no objeto `recipient`.
{% endalert %}

## Usando o conteúdo de template incluído em uma requisição de API {#using-the-templated-content-included-with-an-api-request}

Além de disparar a mensagem, você também pode incluir conteúdo na requisição de API para ser inserido na mensagem como template dentro do objeto `trigger_properties`. Esse conteúdo pode ser referenciado no corpo da mensagem. Use exatamente duas chaves por Liquid tag em `trigger_properties` e no texto da mensagem. Um exemplo é: {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} Uma `{` ou `}` extra é uma causa comum de [falhas de personalização disparadas por API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).

Veja o exemplo de notificação social a seguir para mais contexto.

![A propriedade de disparo mencionada acima incluída na mensagem para preencher automaticamente o nome do usuário, seguida pelo texto: "curtiu sua foto! Clique aqui para ver o que essa pessoa anda fazendo."]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Reelegibilidade em campanhas disparadas por API {#re-eligibility-with-api-triggered-campaigns}

O número de vezes que um usuário recebe uma campanha disparada por API pode ser limitado usando as configurações de reelegibilidade. Isso significa que o usuário receberá a campanha apenas uma vez ou uma vez dentro de um determinado período, independentemente de quantas vezes o gatilho da API for acionado.

Por exemplo, digamos que você esteja usando uma campanha disparada por API para enviar ao usuário uma campanha sobre um item que ele visualizou recentemente. Nesse caso, você pode limitar a campanha para enviar no máximo uma mensagem por dia, independentemente de quantos itens o usuário visualizou enquanto o gatilho da API era acionado para cada item. Por outro lado, se sua campanha disparada por API for transacional, você vai querer garantir que o usuário receba a campanha toda vez que realizar a transação, definindo a postergação como zero minutos.

![Captura de tela relacionada à reelegibilidade em campanhas disparadas por API.]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})