---
nav_title: Cadastro de e-mail com desconto
article_title: Cadastro de e-mail com desconto
alias: "/email_discount/"
page_order: 4
description: "Esta página de referência explica como usar o editor de arrastar e soltar de mensagens no app para criar um formulário de cadastro de e-mail que oferece um desconto para novos inscritos."
---

# Cadastro de e-mail com desconto {#email-sign-up-with-discount}

> Use o editor de arrastar e soltar de mensagens no app para criar um formulário de cadastro de e-mail que oferece um desconto para novos inscritos.

{% multi_lang_include drag_and_drop/templates.md section='SDK or kit de desenvolvimento de software requirements' %}

## Criando um formulário de cadastro de e-mail com desconto {#creating-an-email-sign-up-form-with-a-discount}

### Etapa 1: Escolha seu modelo {#step-1-choose-your-template}

Ao criar uma mensagem no app de arrastar e soltar, selecione **Email sign-up with welcome discount** como seu modelo e, em seguida, selecione **Build message**. Esse modelo é compatível com apps móveis e navegadores web.

![O editor de mensagens no app com o modelo para um formulário de cadastro de e-mail com desconto.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_discount.png %})

### Etapa 2: Configure os estilos da sua mensagem {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize o componente de cadastro de e-mail {#step-3-customize-your-email-sign-up-component}

Para começar a criar seu formulário de cadastro de e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de inscrições global **Subscribed**. Para fazer opt-in de usuários em grupos de inscrições específicos, consulte [Atualizando estados de inscrição de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Você pode personalizar o texto de placeholder e o texto do rótulo do elemento de captura de e-mail.

![O editor de mensagens no app com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field.png %})

#### Validação de e-mail {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Etapa 4: Adicione texto de aviso legal (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem {#step-5-style-your-message}

Personalize a aparência do seu formulário de cadastro e desconto usando os [componentes de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) de arrastar e soltar.

## Analisando os resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Práticas recomendadas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}