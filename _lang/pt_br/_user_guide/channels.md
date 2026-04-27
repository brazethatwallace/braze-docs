---
nav_title: Canais
article_title: Canais
page_order: 5
layout: dev_guide
guide_top_header: "Canais"
guide_top_text: "Alcance seus usuários pelo canal certo, no momento certo. Escolha entre canais dentro do produto, como mensagens no app, Cartões de conteúdo e Banners, ou canais fora do produto, como push, e-mail, SMS e WhatsApp."

page_type: landing
description: "Alcance seus usuários por meio de canais de envio de mensagens dentro e fora do produto na Braze."

guide_featured_title: "Canais dentro do produto"
guide_featured_list:
  - name: Mensagens no app
    link: /docs/user_guide/channels/in_app_messages
    image: /assets/img/braze_icons/phone-02.svg
  - name: Cartões de conteúdo
    link: /docs/user_guide/channels/content_cards
    image: /assets/img/braze_icons/sticker-square.svg
  - name: Banners
    link: /docs/user_guide/channels/banners
    image: /assets/img/braze_icons/layout-top.svg

guide_menu_title: "Canais fora do produto"
guide_menu_list:
  - name: E-mail
    link: /docs/user_guide/channels/email
    image: /assets/img/braze_icons/mail-01.svg
  - name: E-mail de transação
    link: /docs/user_guide/channels/transactional_email
    image: /assets/img/braze_icons/bank-note-02.svg
  - name: Landing pages
    link: /docs/user_guide/messaging/landing_pages
    image: /assets/img/braze_icons/file-02.svg
  - name: LINE
    link: /docs/user_guide/channels/line
    image: /assets/img/braze_icons/message-chat-circle.svg
  - name: Notificações ao vivo
    link: /docs/developer_guide/live_notifications/
    image: /assets/img/braze_icons/phone-02.svg
  - name: Push
    link: /docs/user_guide/channels/push
    image: /assets/img/braze_icons/marker-pin-05.svg
  - name: "SMS, MMS e RCS"
    link: /docs/user_guide/channels/sms_mms_and_rcs
    image: /assets/img/braze_icons/message-text-circle-01.svg
  - name: Webhooks
    link: /docs/user_guide/channels/webhooks
    image: /assets/img/braze_icons/brackets.svg
  - name: WhatsApp
    link: /docs/user_guide/channels/whatsapp
    image: /assets/img/braze_icons/whatsapp.svg
---

## Escolhendo um canal de envio de mensagens {#choosing-a-message-channel}

Ao decidir qual canal de envio de mensagens é o melhor para suas Campaigns e Canvas, sempre considere o conteúdo e a urgência da sua mensagem:

- **Conteúdo** é o quão visualmente envolvente a sua mensagem é. Você pode adicionar multimídia e outros ativos ao seu texto para tornar o conteúdo mais rico.
- **Urgência** é uma medida de quão rapidamente uma mensagem consegue notificar o usuário e atrair sua atenção. Notificações que o usuário pode visualizar imediatamente têm alta urgência, enquanto mensagens que exigem que o usuário faça login no app têm baixa urgência.

A Matriz de Envio de Mensagens da Braze simplifica a seleção de canais ao mapear a **Complexidade do Conteúdo** em relação à **Urgência da Entrega**. Ao equilibrar esses dois fatores, você ajuda sua mensagem a gerar impacto em vez de interromper.

![Push para celular/web tem conteúdo simples e alta urgência; e-mails têm conteúdo rico e alta urgência; mensagens no app/navegador têm conteúdo simples e baixa urgência; Content Cards têm baixa urgência e conteúdo rico]({% image_buster /assets/img_archive/messaging_matrix.png %})

Embora a matriz destaque os canais principais, ela é adaptável: SMS e WhatsApp, por exemplo, são ferramentas de alta urgência que escalam para conteúdo rico ao utilizar formatos multimídia. Para saber mais sobre como aproveitar essa matriz, confira nosso curso do Braze Learning sobre [Envio de mensagens entre canais](https://learning.braze.com/cross-channel-messaging).

## Recursos de acessibilidade {#accessibility-resources}

Você pode usar a Braze para criar campanhas de mensagens acessíveis em cada canal. Trabalhe com seus engenheiros para garantir que os padrões de acessibilidade sejam atendidos na sua implementação. Se quiser orientações adicionais, recomendamos:

- [Fundamentos de mensagens acessíveis](https://learning.braze.com/accessible-messaging-foundations): Aprenda os princípios fundamentais de acessibilidade aplicáveis às comunicações de marca neste curso do Braze Learning.
- [Criando mensagens acessíveis]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/): Aprenda a adicionar texto alternativo e estruturar seu conteúdo para tecnologias assistivas diretamente na Braze.

Se você tiver feedback sobre a acessibilidade da Braze ou de mensagens enviadas pela Braze, adoraríamos ouvir você. Abra o menu **Suporte** no cabeçalho global e selecione **Compartilhar feedback** para nos enviar suas opiniões.