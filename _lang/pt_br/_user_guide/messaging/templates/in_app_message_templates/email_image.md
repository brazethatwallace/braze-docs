---
nav_title: Inscrição de e-mail com imagem
article_title: Inscrição de e-mail com imagem de fundo
alias: "/email_image/"
page_order: 5
description: "Esta página explica como usar o editor de arrastar e soltar de mensagens no app para destacar o estilo da sua marca com uma mensagem simples e construir sua lista de e-mails."
---

# Inscrição de e-mail com imagem de fundo {#email-sign-up-with-background-image}

> Use o editor de arrastar e soltar de mensagens no app para destacar o estilo da sua marca com uma mensagem simples e construir sua lista de e-mails.

{% multi_lang_include drag_and_drop/templates.md section='SDK or kit de desenvolvimento de software requirements' %}

## Criando um formulário de inscrição de e-mail com imagem de fundo {#creating-an-email-sign-up-form-with-a-background-image}

### Etapa 1: Escolha seu modelo {#step-1-choose-your-template}

Ao criar uma mensagem no app de arrastar e soltar, selecione **Email sign-up with background image** como modelo e, em seguida, selecione **Build message**. Este modelo é compatível com apps para dispositivos móveis e navegadores web.

![O editor de mensagens no app com o modelo para um formulário de inscrição de e-mail com imagem de fundo.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_image.png %})

### Etapa 2: Configure os estilos da sua mensagem {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize o componente de inscrição de e-mail {#step-3-customize-your-email-sign-up-component}

Para começar a criar seu formulário de inscrição de e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de inscrições global **Subscribed**. Para fazer opt-in de usuários em grupos de inscrições específicos, consulte [Atualizando estados de inscrição de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Você pode personalizar o texto de espaço reservado e o texto do rótulo do elemento de captura de e-mail.

![O editor de mensagens no app com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_image.png %})

#### Validação de e-mail {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Etapa 4: Adicione texto de aviso legal (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem {#step-5-style-your-message}

Personalize a aparência do seu formulário de inscrição usando os [componentes de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) de arrastar e soltar. Adicione sua própria imagem de fundo substituindo a URL da imagem de fundo padrão no menu **Message container** ou remova a URL e selecione sua imagem na [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).

## Analisando os resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Práticas recomendadas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}