---
nav_title: Entrega disparada por API or interface de programação do aplicativo (API)
article_title: Entrega disparada por API or interface de programação do aplicativo (API)
page_order: 2
page_type: reference
description: "Este artigo de referência descreve como agendar e configurar uma campanha disparada por API or interface de programação do aplicativo (API)."
tool: Campaigns
platform: API

---

# Entrega disparada por API or interface de programação do aplicativo (API) {#api-triggered-delivery}

> Campanhas disparadas por API or interface de programação do aplicativo (API) ou campanhas disparadas por servidor são ideais para casos de uso transacionais mais avançados. As campanhas disparadas por API or interface de programação do aplicativo (API) da Braze permitem que profissionais de marketing gerenciem o texto da campanha, testes multivariantes e regras de reelegibilidade dentro do dashboard da Braze, enquanto disparam a entrega desse conteúdo a partir de seus próprios servidores e sistemas. A requisição de API or interface de programação do aplicativo (API) para disparar a mensagem também pode incluir dados adicionais para serem inseridos na mensagem em tempo real por meio de templates.

## Configurando uma Campaign disparada por API or interface de programação do aplicativo (API) {#setting-up-an-api-triggered-campaign}

Configurar uma Campaign disparada por API or interface de programação do aplicativo (API) envolve algumas etapas. Primeiro, crie uma nova Campaign multicanal ou de canal único (com testes multivariantes).

{% alert note %}
Uma Campaign disparada por API or interface de programação do aplicativo (API) é diferente de uma [Campaign de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_campaigns).
{% endalert %}

Em seguida, configure seu texto e notificações da mesma forma que faria normalmente para notificações agendadas e selecione **API or interface de programação do aplicativo (API)-Triggered Delivery**. Para saber mais sobre como disparar essas Campaigns a partir do seu servidor, confira este artigo sobre [envio de Campaigns disparadas por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

![Configure seu texto e notificações da mesma forma que faria normalmente para notificações agendadas e selecione API or interface de programação do aplicativo (API)-Triggered Delivery. Para saber mais sobre como disparar essas Campaigns a partir do seu servidor, confira o artigo sobre envio de Campaigns disparadas por API or interface de programação do aplicativo (API).]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Reduzindo a postergação entre o disparo da API or interface de programação do aplicativo (API) e o envio {#reducing-delay-between-your-api-trigger-and-send}

Se as mensagens demorarem mais do que o esperado para serem enviadas após você chamar o endpoint de disparo, verifique se o perfil de usuário está pronto no momento do disparo.

Por padrão, `send_to_existing_only` é `true` em [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). A Braze envia apenas para usuários existentes e não cria perfis novos nessa chamada. Para criar ou atualizar um usuário e enviar na mesma requisição, defina `send_to_existing_only` como `false` e inclua um objeto `attributes` em cada destinatário.

Para Campaigns de e-mail, inclua também `email` (e quaisquer outros campos de entrega obrigatórios) dentro de `attributes`. Se o perfil não tiver um endereço de e-mail quando você disparar o envio, a Braze faz novas tentativas por aproximadamente 2 horas enquanto aguarda a chegada dos dados do perfil. Incluir `email` na mesma chamada evita essa postergação.

Para ver os parâmetros completos da requisição, exemplos e o comportamento de novas tentativas, consulte [Enviar Campaigns disparadas por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#recipient-limits-and-profile-creation) e o [objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object).

{% alert note %}
Esta orientação se aplica a Campaigns disparadas por API or interface de programação do aplicativo (API) (`/campaigns/trigger/send`). O [endpoint de e-mail de transação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) usa um formato de requisição diferente (`recipient`, singular) e não suporta `send_to_existing_only`. Para criar um usuário de forma inline com envios de transação, passe `attributes` no objeto `recipient`.
{% endalert %}

## Usando o conteúdo modelado incluído em uma solicitação de API or interface de programação do aplicativo (API) {#using-the-templated-content-included-with-an-api-request}

Além de disparar a mensagem, você também pode incluir conteúdo na solicitação de API or interface de programação do aplicativo (API) para ser modelado na mensagem dentro do objeto `trigger_properties`. Esse conteúdo pode ser referenciado no corpo da mensagem.

Use exatamente duas chaves por Liquid tag em `trigger_properties` e no texto da mensagem. Um exemplo é: {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} Um `{` ou `}` extra é uma causa comum de [falhas de personalização disparadas por API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).

Veja o exemplo de notificação social a seguir para mais contexto.

![A propriedade de disparo mencionada acima incluída na mensagem para preencher automaticamente o nome do usuário, seguida do texto: "curtiu sua foto! Clique aqui para ver o que ele anda fazendo.".]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Reelegibilidade com Campaigns disparadas por API or interface de programação do aplicativo (API) {#re-eligibility-with-api-triggered-campaigns}

O número de vezes que um usuário recebe uma Campaign disparada por API or interface de programação do aplicativo (API) pode ser limitado usando as configurações de reelegibilidade. Isso significa que o usuário recebe a Campaign apenas uma vez ou uma vez em um determinado intervalo, independentemente de quantas vezes o disparo da API or interface de programação do aplicativo (API) for acionado.

Por exemplo, digamos que você está usando uma Campaign disparada por API or interface de programação do aplicativo (API) para enviar ao usuário uma Campaign sobre um item que ele visualizou recentemente. Nesse caso, você pode limitar a Campaign para enviar no máximo uma mensagem por dia, independentemente de quantos itens ele visualizou, enquanto dispara o gatilho da API or interface de programação do aplicativo (API) para cada item. Se a sua Campaign disparada por API or interface de programação do aplicativo (API) for transacional, certifique-se de que o usuário receba a Campaign toda vez que realizar a transação, definindo a postergação como zero minutos.

![Captura de tela relacionada à reelegibilidade com Campaigns disparadas por API or interface de programação do aplicativo (API).]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})