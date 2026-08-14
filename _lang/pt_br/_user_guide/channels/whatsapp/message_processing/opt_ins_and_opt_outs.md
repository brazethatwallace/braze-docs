---
nav_title: "Opt-ins e descadastramento"
article_title: "Opt-ins e descadastramento"
description: "Este artigo de referência aborda diferentes métodos de opt-in e descadastramento do WhatsApp."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
---

# Opt-in e descadastramento {#opt-in-and-opt-out}

> Gerenciar opt-ins e descadastramentos do WhatsApp é fundamental, pois o WhatsApp monitora a [classificação de qualidade do seu número de telefone](https://www.facebook.com/business/help/896873687365001), e classificações baixas podem resultar na redução dos seus limites de mensagens. <br><br>Uma forma de manter uma classificação de alta qualidade é evitar que os usuários bloqueiem ou denunciem sua empresa. Isso pode ser feito fornecendo [mensagens de alta qualidade](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (como valor para seus usuários), controlando a frequência de mensagens e permitindo que os clientes cancelem o recebimento de comunicações futuras. <br><br>Para uma visão geral entre canais do status de inscrição do WhatsApp, consulte [Status de inscrição]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp). Esta página explica como configurar opt-ins e descadastramentos, e as diferenças entre os modificadores "regex" e "is".

Os opt-ins podem vir de fontes externas ou de métodos da Braze, como SMS ou mensagens no app e no navegador. Os descadastramentos podem ser tratados usando palavras-chave configuradas na Braze e botões de marketing do WhatsApp. Consulte os métodos a seguir para orientações sobre como configurar opt-ins e descadastramentos.

## Métodos de aceitação {#opt-in-methods}
- [Métodos de aceitação externos à Braze](#external-to-braze-opt-in-methods)
  - [Lista de aceitação criada externamente](#externally-built-opt-in-list)
  - [Mensagem de saída no canal de suporte ao cliente do WhatsApp](#outbound-message-in-customer-support-whatsapp-channel)
  - [Mensagem de entrada do WhatsApp](#inbound-whatsapp-message)
- [Métodos de aceitação com a Braze](#braze-powered-opt-in-methods)

### Métodos de cancelamento {#opt-out-methods}
- [Palavras-chave gerais de cancelamento](#general-opt-out-keywords)
- [Seleção de cancelamento de marketing](#marketing-opt-out-selection)

## Configure aceitações para o seu canal WhatsApp da Braze {#set-up-opt-ins-for-your-braze-whatsapp-channel}

Para aceitações do WhatsApp, você deve cumprir os [requisitos do WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Você também precisará fornecer à Braze as seguintes informações:
- Um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) e um status de inscrição atualizado para cada usuário. Isso pode ser feito usando o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) ou por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para atualizar o número de telefone e o status de inscrição.

Uma mensagem de entrada do WhatsApp não inscreve automaticamente um usuário no seu grupo de inscrições do WhatsApp. Você deve atualizar explicitamente o status de inscrição com uma [etapa de atualização de usuário](#user-update-step), [webhook](#webhook-campaign-to-trigger-a-second-whatsapp-campaign) ou chamada de API.

A Meta exige que o texto de aceitação:

- Declare claramente que a pessoa está aceitando receber mensagens da sua empresa
- Inclua o nome da sua empresa (não uma linguagem genérica como "enviaremos mensagens para você")
- Esteja em conformidade com as leis locais aplicáveis

{% alert note %}
A Braze lançou uma melhoria no endpoint `/users/track` que permite atualizações no status de inscrição. Saiba mais em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status). No entanto, se você já criou protocolos de aceitação usando o [endpoint `/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2), pode continuar usando-o.
{% endalert %}

### Métodos de aceitação externos à Braze {#external-to-braze-opt-in-methods}

Seu app ou website (registro de conta, página de checkout, configurações da conta, terminal de cartão de crédito) para a Braze.

Onde quer que você já tenha consentimento de marketing para e-mail ou mensagens de texto, inclua uma seção adicional para o WhatsApp. Depois que um usuário aceitar, ele precisará de um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) e um status de inscrição atualizado. Para fazer isso, dependendo de como sua instalação da Braze está configurada, use o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) ou o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Lista de aceitação criada externamente {#externally-built-opt-in-list}

Se você já usou o WhatsApp anteriormente, pode já ter criado uma lista de usuários com aceitações conforme os requisitos do WhatsApp. Nesse caso, faça upload de um CSV ou use a API com as [seguintes informações]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) na Braze.

#### Mensagem de saída no canal de suporte ao cliente do WhatsApp {#outbound-message-in-customer-support-whatsapp-channel}

No seu canal de suporte ao cliente, faça o acompanhamento de problemas resolvidos com uma mensagem automática perguntando se desejam aceitar receber mensagens de marketing. A funcionalidade aqui depende da disponibilidade de recursos na ferramenta de suporte ao cliente escolhida e de onde você mantém as informações dos usuários.

1. Forneça um [link de mensagem](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) do seu número de telefone do WhatsApp Business.
2. Forneça [ações de resposta rápida]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies) em que o cliente responde "Sim" para indicar a aceitação.
3. Configure um disparador de palavra-chave personalizada.
4. Para qualquer uma dessas ideias, você provavelmente precisará concluir a jornada com o seguinte:
	- Chamar o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para atualizar ou criar um usuário
	- Usar o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) ou o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Mensagem de entrada do WhatsApp {#inbound-whatsapp-message}

Faça com que os clientes enviem uma mensagem de entrada para o número do WhatsApp.

Isso pode ser configurado como um Canvas ou uma Campaign, dependendo se você deseja que o usuário receba uma mensagem de confirmação no novo canal.

1. Crie uma Campaign com o disparador de entrega baseada em ação de uma mensagem de entrada.
2. Crie uma Campaign de webhook. Para um exemplo de webhook, consulte [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#step-2-update-the-users-profile).

{% alert tip %}
Você pode criar uma URL ou código QR para entrar em um canal do WhatsApp dentro do [gerenciador do WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/) em **Phone Number** > **Message Links**.<br>![Criador de código QR do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Métodos de aceitação com a Braze {#braze-powered-opt-in-methods}

#### Mensagem SMS {#sms-message}

No Canvas, configure uma Campaign que pergunte aos clientes se desejam aceitar receber mensagens do WhatsApp usando um dos seguintes métodos:
- Segment de clientes: grupo de marketing inscrito fora dos EUA
- Configuração de disparador de palavra-chave personalizada

Saiba mais sobre como atualizar o status de inscrição dos perfis de usuário em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

#### Mensagem no app ou no navegador {#in-app-or-in-browser-message}

Crie uma mensagem no app ou um pop-up no navegador solicitando que os clientes aceitem o uso do WhatsApp.

Use a [mensagem no app em HTML](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) com a ["ponte" JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge) para fazer interface com o SDK da Braze. Certifique-se de usar o ID do grupo de inscrições do WhatsApp.

#### Formulário de captura de número de telefone {#phone-number-capture-form}

Use o modelo de [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) no editor de arrastar e soltar para mensagens no app para coletar números de telefone dos usuários e expandir seus grupos de inscrições do WhatsApp.

## Configure a desativação para o seu canal WhatsApp da Braze {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### Alternância "Ofertas e Anúncios" do WhatsApp {#whatsapp-offers-and-announcements-toggle}

O WhatsApp oferece uma alternância de "Ofertas e Anúncios" nas configurações do app que permite aos usuários desativar mensagens de marketing. Essa alternância funciona de forma independente dos grupos de inscrições da Braze:

- **Os grupos de inscrições da Braze** são gerenciados por meio da sua integração com a Braze (API, Central de Preferências ou SDK) e controlam quais usuários você segmenta para envio de mensagens.
- **A alternância nativa do WhatsApp** é controlada pela Meta e aplicada no nível da plataforma, fora da Braze.

Essas duas camadas não sincronizam automaticamente por design. Quando um usuário desativa a alternância de "Ofertas e Anúncios" no WhatsApp, a Meta bloqueia a entrega de mensagens de marketing no nível da plataforma, mesmo que o status de inscrição do usuário na Braze mostre como "Subscribed". A preferência do usuário é respeitada no momento da entrega.

{% alert note %}
Como a Braze não recebe um sinal de desativação até que uma tentativa de envio seja feita e a Meta retorne um erro, as contagens de inscrição na Braze podem não refletir os usuários que optaram por sair por meio da alternância do WhatsApp até que uma mensagem seja tentada. Isso significa que as estimativas de alcance podem ser ligeiramente superestimadas até que esse ciclo de feedback ocorra.
{% endalert %}

### Palavras-chave gerais de desativação {#general-opt-out-keywords}

Você pode configurar uma Campaign ou Canvas que permita aos usuários que enviem determinadas palavras desativar mensagens futuras. Canvas pode ser especialmente benéfico, pois permite incluir uma mensagem de acompanhamento que confirma a desativação bem-sucedida.

#### Etapa 1: Crie um Canvas com um disparador de "Mensagem de entrada do WhatsApp" {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![Etapa de entrada de Canvas baseada em ação que insere usuários que enviam uma mensagem de entrada do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Ao selecionar disparadores de palavras-chave, inclua palavras como "Parar" ou "Sem Mensagem". Se você escolher esse método, certifique-se de que seus clientes conheçam suas palavras de desativação. Por exemplo, após receber a aceitação inicial, inclua uma resposta de acompanhamento como "Para desativar essas mensagens, envie 'Parar' a qualquer momento."

![Etapa de mensagem para enviar uma mensagem de entrada do WhatsApp onde o corpo da mensagem é "STOP" ou "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Etapa 2: Atualize o perfil do usuário {#step-2-update-the-users-profile}

Atualize o perfil do usuário usando um dos métodos descritos em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

### Seleção de desativação de marketing {#marketing-opt-out-selection}

Dentro do criador de modelos de mensagem do WhatsApp, você pode incluir a opção de "desativação de marketing". Sempre que incluir essa opção, certifique-se de que o modelo seja usado em um Canvas com uma etapa subsequente para alteração do grupo de inscrições.

1. Crie um modelo de mensagem com a resposta rápida de "desativação de marketing".<br>![Modelo de mensagem com uma opção de rodapé de "Desativação de marketing"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Seção para configurar um botão de desativação de marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Crie um Canvas que use esse modelo de mensagem.<br><br>
3. Siga as etapas do exemplo anterior, mas com o texto de disparo "STOP PROMOTIONS".<br><br>
4. Atualize o status de inscrição do usuário usando um dos métodos descritos em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

## Configure fluxos de aceitação e recusa {#set-up-opt-in-and-opt-out-workflows}

Você pode configurar fluxos de resposta por palavra-chave "START" e "STOP" para o WhatsApp com estes dois métodos:

- [Etapa de Atualização do Usuário](#user-update-step)
- [Campaign de webhook para disparar uma segunda Campaign de WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Etapa de Atualização do Usuário {#user-update-step}

A [etapa de Atualização do Usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) pode adicionar o número de telefone do usuário ao grupo de inscrições do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de inscrições.

A etapa de Atualização do Usuário evita condições de corrida porque o usuário não avançará para a próxima etapa no Canvas antes que seu número de telefone seja adicionado ao grupo de inscrições. Ela também tem menos etapas de configuração do que os outros métodos, então a Braze geralmente recomenda este método.

1. Crie um Canvas com a etapa baseada em ação **Send a WhatsApp Inbound Message**. Selecione **Where the message body** e insira "START" em **Is**.

{% alert important %}
Para mensagens "STOP", inverta a etapa de mensagem que confirma a recusa e a etapa de Atualização do Usuário. Se você não fizer isso, o usuário será removido do grupo de inscrições primeiro e não será elegível para receber a mensagem de confirmação.
{% endalert %}

![Uma etapa de mensagem do WhatsApp em que o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. No Canvas, crie uma etapa **Set Up User Update** e, em **Action**, selecione **Advanced JSON Editor**. <br><br>![Etapa de Atualização do Usuário com a ação "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3. Preencha o **User Update object** com a seguinte carga útil JSON, substituindo `XXXXXXXXXXX` pelo ID do seu grupo de inscrições:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4. Adicione uma etapa de mensagem do WhatsApp subsequente. <br><br>![Etapa de Atualização do Usuário em um Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considerações {#considerations}

A atualização pode ser concluída em velocidades variáveis porque a Braze agrupa as solicitações da [etapa de Atualização do Usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em lotes. Para fluxos de aceitação sensíveis ao tempo em que a confirmação precisa ser enviada imediatamente após a atualização da inscrição, use o [método de webhook](#webhook-campaign-to-trigger-a-second-whatsapp-campaign) em vez de uma etapa de Atualização do Usuário.

### Campaign de webhook para disparar uma segunda Campaign de WhatsApp {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Uma Campaign de webhook pode disparar a entrada em uma segunda Campaign após adicionar o número de telefone do usuário ao grupo de inscrições do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de inscrições.

{% alert important %}
Você não precisa usar este método para mensagens STOP. A mensagem de confirmação será enviada antes que o usuário seja removido do grupo de inscrições, então você pode usar uma das outras duas etapas.
{% endalert %}

1. Crie uma Campaign ou Canvas com uma etapa baseada em ação **Send a WhatsApp Inbound Message**. Selecione **Where the message body** e insira "START" em **Is**.

![Etapa de mensagem do WhatsApp em que o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2. Na Campaign ou Canvas, crie uma etapa de mensagem de webhook e altere o **Request Body** para **Raw Text**.

![Etapa de mensagem para um webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3. Insira a [URL do endpoint]({{site.baseurl}}/api/basics) do cliente no campo **Webhook URL**, seguida do link do endpoint `campaigns/trigger/send`. Por exemplo, `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Campo de URL do webhook na seção "Compose Webhook".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4. No texto bruto, insira a seguinte carga útil JSON e substitua `XXXXXXXXXXX` pelo ID do seu grupo de inscrições. Você precisará substituir o `campaign_id` após criar sua segunda Campaign.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5. Crie uma Campaign de WhatsApp (sua segunda Campaign) e defina o disparo como API. Certifique-se de copiar este `campaign_id` na carga útil JSON da sua primeira Campaign.

#### Considerações

- Atualizações de atributos a partir da carga útil JSON de disparo da API do Canvas ainda não são suportadas, então você só pode disparar uma Campaign de WhatsApp para a mensagem de resposta do WhatsApp (como na etapa 2).
- Um modelo de WhatsApp precisa ser aprovado para ser enviado como mensagem de resposta. Isso ocorre porque uma resposta rápida exige que o disparo de mensagem de entrada esteja dentro da mesma Campaign ou Canvas. Se você usar uma [etapa de Atualização do Usuário](#user-update-step), poderá enviar uma mensagem de resposta rápida sem a aprovação da Meta.

## Entendendo a diferença entre os modificadores "regex" e "is" {#understanding-the-difference-between-regex-and-is-modifiers}

Nesta tabela, `STOP` é usado como exemplo de palavra-gatilho para demonstrar como os modificadores funcionam.

| Modificador | Palavra-gatilho | Ação |
| --- | --- | --- |
| `Is` | `STOP` | Captura qualquer uso da palavra inteira "stop", independentemente de maiúsculas ou minúsculas. Por exemplo, captura "stop", mas não "please stop". |
| `Matches regex` | `STOP` | Captura qualquer uso de "STOP" exatamente nessa combinação de maiúsculas e minúsculas. Por exemplo, captura "STOP" e "PLEASE STOP", mas não "stop". |
| `Matches regex` | `(?i)STOP(?-i)` | Captura qualquer uso de "STOP" em qualquer combinação de maiúsculas e minúsculas. Por exemplo, captura "stop", "please stop" e "never stop sending me messages". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Entendendo a diferença entre os modificadores regex e is" }