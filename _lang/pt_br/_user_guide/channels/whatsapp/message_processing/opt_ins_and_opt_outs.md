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

> Gerenciar opt-ins e descadastramentos do WhatsApp é fundamental, pois o WhatsApp monitora a [classificação de qualidade do seu número de telefone](https://www.facebook.com/business/help/896873687365001), e classificações baixas podem resultar na redução dos seus limites de mensagens. <br><br>Uma forma de manter uma classificação de alta qualidade é evitar que os usuários bloqueiem ou denunciem sua empresa. Isso pode ser feito fornecendo [mensagens de alta qualidade](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) (como valor para seus usuários), controlando a frequência de mensagens e permitindo que os clientes cancelem o recebimento de comunicações futuras. <br><br>Esta página explica como configurar opt-ins e descadastramentos, e as diferenças entre os modificadores "regex" e "is".

Os opt-ins podem vir de fontes externas ou de métodos da Braze, como SMS ou mensagens no app e no navegador. Os descadastramentos podem ser tratados usando palavras-chave configuradas na Braze e botões de marketing do WhatsApp. Consulte os métodos a seguir para orientações sobre como configurar opt-ins e descadastramentos.

## Métodos de opt-in {#opt-in-methods}
- [Métodos de opt-in externos à Braze](#external-to-braze-opt-in-methods)
  - [Lista de opt-in criada externamente](#externally-built-opt-in-list)
  - [Mensagem de saída no canal de suporte ao cliente do WhatsApp](#outbound-message-in-customer-support-whatsapp-channel)
  - [Mensagem de entrada do WhatsApp](#inbound-whatsapp-message)
- [Métodos de opt-in com a Braze](#braze-powered-opt-in-methods)

### Métodos de descadastramento {#opt-out-methods}
- [Palavras-chave gerais de descadastramento](#general-opt-out-keywords)
- [Seleção de descadastramento de marketing](#marketing-opt-out-selection)

## Configurar opt-ins para o seu canal WhatsApp da Braze {#set-up-opt-ins-for-your-braze-whatsapp-channel}

Para opt-ins do WhatsApp, você deve cumprir os [requisitos do WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Você também precisará fornecer à Braze as seguintes informações:
- Um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) e um status de inscrição atualizado para cada usuário. Isso pode ser feito usando o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) ou por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para atualizar o número de telefone e o status de inscrição.

{% alert note %}
A Braze lançou uma melhoria no endpoint `/users/track` que permite atualizações no status de inscrição. Saiba mais em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status). No entanto, se você já criou protocolos de opt-in usando o [endpoint `/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2), pode continuar usando-o.
{% endalert %}

### Métodos de opt-in externos à Braze {#external-to-braze-opt-in-methods}

Seu app ou site (registro de conta, página de checkout, configurações da conta, terminal de cartão de crédito) para a Braze.

Onde quer que você já tenha consentimento de marketing para e-mail ou mensagens de texto, inclua uma seção adicional para o WhatsApp. Depois que um usuário fizer opt-in, ele precisará de um `external_id`, um [número de telefone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) e um status de inscrição atualizado. Para fazer isso, dependendo de como sua instalação da Braze está configurada, use o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) ou o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/).

#### Lista de opt-in criada externamente {#externally-built-opt-in-list}

Se você já usou o WhatsApp anteriormente, pode já ter criado uma lista de usuários com opt-ins conforme os requisitos do WhatsApp. Nesse caso, faça upload de um CSV ou use a API com as [seguintes informações]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) na Braze.

#### Mensagem de saída no canal de suporte ao cliente do WhatsApp {#outbound-message-in-customer-support-whatsapp-channel}

No seu canal de suporte ao cliente, faça um acompanhamento de problemas resolvidos com uma mensagem automática perguntando se desejam fazer opt-in para mensagens de marketing. A funcionalidade aqui depende da disponibilidade de recursos na ferramenta de suporte ao cliente escolhida e de onde você mantém as informações dos usuários.

1. Forneça um [link de mensagem](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) do seu número de telefone do WhatsApp Business.
2. Forneça [ações de resposta rápida]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#quick-replies) onde o cliente responde "Sim" para indicar opt-in.
3. Configure um gatilho de palavra-chave personalizada.
4. Para qualquer uma dessas ideias, você provavelmente precisará concluir o fluxo com o seguinte:
	- Chamar o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para atualizar ou criar um usuário
	- Usar o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) ou o [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Mensagem de entrada do WhatsApp {#inbound-whatsapp-message}

Faça com que os clientes enviem uma mensagem de entrada para o número do WhatsApp.

Isso pode ser configurado como um Canvas ou uma Campaign, dependendo se você deseja que o usuário receba uma mensagem de confirmação no novo canal.

1. Crie uma Campaign com o gatilho de entrega baseada em ação de uma mensagem de entrada.
2. Crie uma Campaign de webhook. Para um exemplo de webhook, consulte [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#step-2-update-the-users-profile).

{% alert tip %}
Você pode criar uma URL ou código QR para entrar em um canal do WhatsApp dentro do [gerenciador do WhatsApp](https://business.facebook.com/wa/manage/phone-numbers/) em **Phone Number** > **Message Links**.<br>![Criador de código QR do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Métodos de opt-in com a Braze {#braze-powered-opt-in-methods}

#### Mensagem SMS {#sms-message}

No Canvas, configure uma Campaign que pergunte aos clientes se desejam fazer opt-in para receber mensagens do WhatsApp usando um dos seguintes métodos:
- Segment de clientes: grupo de marketing inscrito fora dos EUA
- Configuração de gatilho de palavra-chave personalizada

Saiba mais sobre como atualizar o status de inscrição dos perfis de usuário em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

#### Mensagem no app ou no navegador {#in-app-or-in-browser-message}

Crie uma mensagem no app ou um pop-up no navegador solicitando que os clientes façam opt-in para o uso do WhatsApp.

Use a [mensagem no app em HTML](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) com o ["bridge" JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge) para fazer interface com o SDK da Braze. Certifique-se de usar o ID do grupo de inscrições do WhatsApp.

#### Formulário de captura de número de telefone {#phone-number-capture-form}

Use o modelo de [formulário de captura de número de telefone]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) no editor de arrastar e soltar para mensagens no app para coletar números de telefone dos usuários e expandir seus grupos de inscrições do WhatsApp.

## Configurar descadastramentos para o seu canal WhatsApp da Braze {#set-up-opt-outs-for-your-braze-whatsapp-channel}

### Botão "Ofertas e Anúncios" do WhatsApp {#whatsapp-offers-and-announcements-toggle}

O WhatsApp oferece um botão "Ofertas e Anúncios" nas configurações do app que permite aos usuários cancelar o recebimento de mensagens de marketing. Esse botão funciona de forma independente dos grupos de inscrições da Braze:

- **Grupos de inscrições da Braze** são gerenciados por meio da sua integração com a Braze (API, Central de Preferências ou SDK) e controlam quais usuários você segmenta para envio de mensagens.
- **O botão nativo do WhatsApp** é controlado pela Meta e aplicado no nível da plataforma, fora da Braze.

Essas duas camadas não sincronizam automaticamente por design. Quando um usuário desativa o botão "Ofertas e Anúncios" no WhatsApp, a Meta bloqueia a entrega de mensagens de marketing no nível da plataforma, mesmo que o status de inscrição do usuário na Braze mostre como "Subscribed". A preferência do usuário é respeitada no momento da entrega.

{% alert note %}
Como a Braze não recebe um sinal de descadastramento até que uma tentativa de envio seja feita e a Meta retorne um erro, as contagens de inscrições na Braze podem não refletir os usuários que cancelaram pelo botão do WhatsApp até que uma mensagem seja tentada. Isso significa que as estimativas de alcance podem ser ligeiramente superestimadas até que esse ciclo de feedback ocorra.
{% endalert %}

### Palavras-chave gerais de descadastramento {#general-opt-out-keywords}

Você pode configurar uma Campaign ou Canvas que permita que usuários que enviem determinadas palavras cancelem o recebimento de mensagens futuras. Canvas pode ser especialmente benéfico, pois permite incluir uma mensagem de acompanhamento confirmando o descadastramento bem-sucedido.

#### Etapa 1: Criar um Canvas com o gatilho "Mensagem de entrada do WhatsApp" {#step-1-create-a-canvas-with-a-trigger-of-inbound-whatsapp-message}

![Etapa de entrada do Canvas baseada em ação que insere usuários que enviam uma mensagem de entrada do WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Ao selecionar gatilhos de palavras-chave, inclua palavras como "Parar" ou "Sem mensagem". Se você escolher esse método, certifique-se de que seus clientes conheçam suas palavras de descadastramento. Por exemplo, após receber o opt-in inicial, inclua uma resposta de acompanhamento como "Para cancelar o recebimento dessas mensagens, envie "Parar" a qualquer momento."

![Etapa de mensagem para enviar uma mensagem de entrada do WhatsApp onde o corpo da mensagem é "STOP" ou "NO MESSAGE".]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Etapa 2: Atualizar o perfil do usuário {#step-2-update-the-users-profile}

Atualize o perfil do usuário usando um dos métodos descritos em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

### Seleção de descadastramento de marketing {#marketing-opt-out-selection}

No criador de modelos de mensagem do WhatsApp, você pode incluir a opção "descadastramento de marketing". Sempre que incluir essa opção, certifique-se de que o modelo seja usado em um Canvas com uma etapa subsequente para alteração do grupo de inscrições.

1. Crie um modelo de mensagem com a resposta rápida "descadastramento de marketing".<br>![Modelo de mensagem com uma opção de rodapé "Descadastramento de marketing"]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Seção para configurar um botão de descadastramento de marketing.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Crie um Canvas que use esse modelo de mensagem.<br><br>
3. Siga as etapas do exemplo anterior, mas com o texto de gatilho "STOP PROMOTIONS".<br><br>
4. Atualize o status de inscrição do usuário usando um dos métodos descritos em [Grupos de inscrições]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#update-subscription-status).

## Configurar fluxos de trabalho de opt-in e descadastramento {#set-up-opt-in-and-opt-out-workflows}

Você pode configurar fluxos de trabalho de resposta às palavras-chave "START" e "STOP" para o WhatsApp com estes dois métodos:

- [Etapa de Atualização de usuário](#user-update-step)
- [Campaign de webhook para acionar uma segunda Campaign do WhatsApp](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Etapa de Atualização de usuário {#user-update-step}

A [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) pode adicionar o número de telefone do usuário ao grupo de inscrições do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de inscrições.

A etapa de Atualização de usuário evita condições de corrida porque o usuário não avançará para a próxima etapa no Canvas antes que seu número de telefone seja adicionado ao grupo de inscrições. Ela também tem menos etapas de configuração do que os outros métodos, então a Braze geralmente recomenda esse método.

1. Crie um Canvas com a etapa baseada em ação **Send a WhatsApp Inbound Message**. Selecione **Where the message body** e insira "START" para **Is**.

{% alert important %}
Para mensagens "STOP", inverta a etapa de mensagem que confirma o descadastramento e a etapa de Atualização de usuário. Se você não fizer isso, o usuário será descadastrado do grupo de inscrições primeiro e não será elegível para receber a mensagem de confirmação.
{% endalert %}

![Uma etapa de mensagem do WhatsApp onde o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2. No Canvas, crie uma etapa **Set Up User Update** e para **Action** selecione **Advanced JSON Editor**. <br><br>![Etapa de Atualização de usuário com a ação "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
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
4. Adicione uma etapa subsequente de mensagem do WhatsApp. <br><br>![Etapa de Atualização de usuário em um Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Considerações {#considerations}

A atualização pode ser concluída em velocidades variáveis porque a Braze agrupa as solicitações da [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em lotes.

### Campaign de webhook para acionar uma segunda Campaign do WhatsApp {#webhook-campaign-to-trigger-a-second-whatsapp-campaign}

Uma Campaign de webhook pode acionar a entrada em uma segunda Campaign após adicionar o número de telefone do usuário ao grupo de inscrições do WhatsApp quando o usuário envia uma palavra-chave para o número de telefone do grupo de inscrições.

{% alert important %}
Você não precisa usar esse método para mensagens STOP. A mensagem de confirmação será enviada antes que o usuário seja removido do grupo de inscrições, então você pode usar uma das outras duas etapas.
{% endalert %}

1. Crie uma Campaign ou Canvas com uma etapa baseada em ação **Send a WhatsApp Inbound Message**. Selecione **Where the message body** e insira "START" para **Is**.

![Etapa de mensagem do WhatsApp onde o corpo da mensagem é "START".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

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
5. Crie uma Campaign do WhatsApp (sua segunda Campaign) e defina o gatilho como API. Certifique-se de copiar esse `campaign_id` na carga útil JSON da sua primeira Campaign.

#### Considerações

- Atualizações de atributos a partir da carga útil JSON do gatilho de API do Canvas ainda não são suportadas, então você só pode acionar uma Campaign do WhatsApp para a mensagem de resposta do WhatsApp (como na etapa 2).
- Um modelo do WhatsApp deve ser aprovado para enviá-lo como mensagem de resposta. Isso porque uma resposta rápida exige que o gatilho de mensagem de entrada esteja dentro da mesma Campaign ou Canvas. Se você usar uma [etapa de Atualização de usuário](#user-update-step), poderá enviar uma mensagem de resposta rápida sem aprovação da Meta.

## Entendendo a diferença entre os modificadores "regex" e "is" {#understanding-the-difference-between-regex-and-is-modifiers}

Nesta tabela, `STOP` é usado como exemplo de palavra de gatilho para demonstrar como os modificadores funcionam.

| Modificador | Palavra de gatilho | Ação |
| --- | --- | --- |
| `Is` | `STOP` | Captura qualquer uso da palavra inteira "stop", independentemente de maiúsculas ou minúsculas. Por exemplo, captura "stop", mas não "please stop". |
| `Matches regex` | `STOP` | Captura qualquer uso de "STOP" exatamente nessa formatação de maiúsculas. Por exemplo, captura "STOP" e "PLEASE STOP", mas não "stop". |
| `Matches regex` | `(?i)STOP(?-i)` | Captura qualquer uso de "STOP" em qualquer formatação de maiúsculas ou minúsculas. Por exemplo, captura "stop", "please stop" e "never stop sending me messages". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Entendendo a diferença entre os modificadores regex e is" }