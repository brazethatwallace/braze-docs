---
nav_title: Entrega disparada por API
article_title: Entrega disparada por API
page_order: 2
page_type: reference
description: "Este artigo de referência descreve como programar e configurar uma campanha disparada por API."
tool: Campaigns
platform: API

---

# Entrega disparada por API

> Campanhas disparadas por API ou campanhas disparadas por servidor são ideais para casos de uso transacionais mais avançados. As campanhas disparadas por API da Braze permitem que profissionais de marketing gerenciem o texto da campanha, testes multivariantes e regras de reelegibilidade dentro do dashboard da Braze, enquanto disparam a entrega desse conteúdo a partir de seus próprios servidores e sistemas. A requisição de API para disparar a mensagem também pode incluir dados adicionais para serem inseridos na mensagem em tempo real por meio de templates.

## Configurando uma campanha disparada por API

Configurar uma campanha disparada por API requer algumas etapas. Primeiro, crie uma nova campanha multicanal ou de canal individual (com testes multivariantes).

{% alert note %}
Uma campanha disparada por API é diferente de uma [campanha da API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Em seguida, configure seu texto e notificações da mesma forma que faria normalmente para notificações agendadas e selecione **API-Triggered Delivery**. Para saber mais sobre como disparar essas campanhas a partir do seu servidor, confira este artigo sobre [envio de campanhas disparadas por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

![Captura de tela da configuração de campanha com a opção de entrega disparada por API selecionada.]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Usando o conteúdo de template incluído em uma requisição de API

Além de disparar a mensagem, você também pode incluir conteúdo na requisição de API para ser inserido na mensagem como template dentro do objeto `trigger_properties`. Esse conteúdo pode ser referenciado no corpo da mensagem. Por exemplo, você pode incluir:
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}``. Veja o exemplo de notificação social a seguir para mais contexto:

![A propriedade de gatilho mencionada acima incluída na mensagem para preencher automaticamente o nome do usuário, seguida pelo texto: "liked your photo! Click here to see what they've been up to.".]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Reelegibilidade em campanhas disparadas por API

O número de vezes que um usuário recebe uma campanha disparada por API pode ser limitado usando as configurações de reelegibilidade. Isso significa que o usuário receberá a campanha apenas uma vez ou uma vez dentro de um determinado período, independentemente de quantas vezes o gatilho da API for acionado.

Por exemplo, digamos que você esteja usando uma campanha disparada por API para enviar ao usuário uma campanha sobre um item que ele visualizou recentemente. Nesse caso, você pode limitar a campanha para enviar no máximo uma mensagem por dia, independentemente de quantos itens o usuário visualizou enquanto o gatilho da API era acionado para cada item. Por outro lado, se sua campanha disparada por API for transacional, você vai querer garantir que o usuário receba a campanha toda vez que realizar a transação, definindo a postergação como zero minutos.

![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})