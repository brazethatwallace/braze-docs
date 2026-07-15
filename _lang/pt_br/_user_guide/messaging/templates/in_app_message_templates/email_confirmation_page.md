---
nav_title: Cadastro de e-mail com confirmação
article_title: Cadastro de e-mail com página de confirmação
alias: "/email_confirmation_page/"
page_order: 7
description: "Esta página explica como usar o editor de arrastar e soltar de mensagens no app para criar um formulário de cadastro de e-mail com uma página de confirmação."
---

# Cadastro de e-mail com página de confirmação {#email-sign-up-with-confirmation-page}

> Use o editor de arrastar e soltar de mensagens no app para criar um formulário de cadastro de e-mail com uma página de confirmação.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criando um formulário de cadastro de e-mail com uma página de confirmação {#creating-an-email-sign-up-form-with-a-confirmation-page}

### Etapa 1: Escolha seu modelo {#step-1-choose-your-template}

Ao criar uma mensagem no app de arrastar e soltar, selecione **Email sign-up with confirmation page** como seu modelo e, em seguida, selecione **Build message**. Esse modelo é compatível com apps para dispositivos móveis e navegadores web.

![O editor de mensagens no app com o modelo para um formulário de cadastro de e-mail com página de confirmação.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### Etapa 2: Configure os estilos da sua mensagem {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize o componente de cadastro de e-mail {#step-3-customize-your-email-sign-up-component}

Para começar a criar seu formulário de cadastro de e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de inscrições global **Subscribed**. Para fazer opt-in de usuários em grupos de inscrições específicos, consulte [Atualizando estados de inscrição de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Você pode personalizar o texto de espaço reservado e o texto do rótulo do elemento de captura de e-mail.

![O editor de mensagens no app com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### Validação de e-mail {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Etapa 4: Adicione um texto de aviso legal (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem {#step-5-style-your-message}

Personalize a aparência do seu formulário de cadastro de e-mail e da página de confirmação usando os [componentes de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) de arrastar e soltar.

## Analisando os resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Práticas recomendadas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}