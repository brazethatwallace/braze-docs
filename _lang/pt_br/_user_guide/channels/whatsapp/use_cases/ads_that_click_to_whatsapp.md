---
nav_title: "Anúncios que direcionam ao WhatsApp"
article_title: "Anúncios que direcionam ao WhatsApp"
page_order: 1
description: "Este artigo de referência fornece um guia passo a passo para configurar e usar Anúncios que direcionam ao WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Anúncios que direcionam ao WhatsApp {#ads-that-click-to-whatsapp}

> Esta página fornece um guia passo a passo para configurar e usar Anúncios que direcionam ao WhatsApp, para que você e sua equipe possam elevar o nível do seu programa de WhatsApp.

Anúncios que direcionam ao WhatsApp são uma forma eficiente de trazer clientes novos e existentes a partir de anúncios Meta no Facebook, Instagram ou outras plataformas. Use esses anúncios para promover seus produtos e serviços enquanto informa os usuários sobre sua presença no WhatsApp.

![Um anúncio do Facebook da Calorie Rocket que anuncia entrega grátis, e a respectiva conversa no WhatsApp que ocorre quando um usuário seleciona o botão do anúncio.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Configurando anúncios que direcionam para o WhatsApp {#setting-up-ads-that-click-to-whatsapp}

1. No Meta Ads Manager, crie um anúncio no Facebook, Instagram ou outras plataformas seguindo o guia passo a passo [Como criar anúncios que direcionam para o WhatsApp](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp). **Não** configure respostas automáticas; você configurará as respostas na Braze.

![Ads Manager com um criador para criar um anúncio de engajamento.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Ao configurar a mensagem pré-preenchida, que será enviada pelo usuário para a sua conta WhatsApp Business, inclua uma palavra ou frase específica que você usará para disparar uma resposta específica para aquele anúncio. Neste exemplo, um app de delivery de comida está usando "entrega grátis" porque é isso que está sendo promovido no anúncio.

![Criador de modelo do Ads Manager com uma mensagem pré-preenchida de "Eu quero entrega grátis".]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Deixe claro na descrição do anúncio que clicar nele iniciará uma conversa com a sua marca, usando frases como "Converse agora pelo WhatsApp".
{% endalert %}

{: start="2"}
2. Na Braze, configure um Canvas baseado em ação onde a opção baseada em ação seja **Send a WhatsApp inbound message** e o corpo da mensagem seja "SUA_PALAVRA_GATILHO". Neste exemplo, um app de delivery de comida está usando "entrega grátis".

![Cronograma de entrada para um Canvas baseado em ação da Braze, com o evento-gatilho de "Send a WhatsApp inbound message" e um corpo de mensagem que corresponde ao regex de "free delivery".]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3. Configure uma mensagem de resposta no Canvas que seja enviada imediatamente após o cliente entrar no Canvas (por exemplo, sem postergação). Embora clicar no anúncio tecnicamente constitua aceitação, recomendamos configurar sua mensagem de resposta para perguntar ao usuário se ele gostaria de receber futuras mensagens de marketing pelo WhatsApp.

{% alert tip %}
Configure sua mensagem de resposta com respostas rápidas (como "Sim" ou "Não, obrigado") para que os usuários possam indicar rapidamente se gostariam de aceitar.
{% endalert %}

Não se esqueça de também fornecer qualquer código de desconto, oferta ou outra informação prometida no anúncio!

![Criador de mensagem do WhatsApp com botões de resposta "Sim" e "Não, obrigado".]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![Etapa do Canvas com um grupo "Aceitando" com um evento-gatilho de "Sent inbound WhatsApp to subscription group" e uma palavra-gatilho de "YES".]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4. Faça a aceitação dos usuários atualizando o status de inscrição dos perfis de usuário com um dos seguintes métodos de atualização:
    - Crie um webhook Braze-para-Braze que atualize o status de inscrição por meio da REST or transferir estado representacional API or interface de programação do aplicativo (API).
    - Use o editor JSON avançado para atualizar o perfil de usuário com o modelo para [atualizar o status de inscrição de um usuário para um Canvas do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-opt-in-and-opt-out-process).

![Etapa de atualização de usuário do Canvas que usa o editor JSON avançado para atualizar o perfil de usuário.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![Canvas mostrando o fluxo de trabalho para enviar anúncios que direcionam para o WhatsApp, incluindo três jornadas de ação: Aceitando, Recusando e Todos os outros.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Considerações {#considerations}

Conversas iniciadas a partir de um anúncio que direciona para o WhatsApp são gratuitas se as seguintes condições forem atendidas:

- Se um usuário enviar uma mensagem para você por meio de um [Ponto de entrada gratuito](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), como um anúncio que direciona para o WhatsApp, uma [janela de atendimento ao cliente](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows) de 24 horas é aberta, permitindo que você envie qualquer tipo de mensagem para esse usuário.
- Se você responder dentro da janela de atendimento ao cliente (dentro de 24 horas), um ponto de entrada gratuito é aberto por 72 horas, e todas as mensagens dentro dessa janela de 72 horas serão gratuitas.