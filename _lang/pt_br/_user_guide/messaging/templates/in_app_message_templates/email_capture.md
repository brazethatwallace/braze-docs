---
nav_title: Formulário de inscrição por e-mail
article_title: Formulário de inscrição por e-mail
alias: "/email_capture/"
page_order: 3
description: "Esta página explica como criar um formulário de inscrição por e-mail com o editor de arrastar e soltar de mensagens no app."
---

# Formulário de inscrição por e-mail {#email-sign-up-form}

> Use o modelo de mensagem no app de inscrição por e-mail com arrastar e soltar para coletar endereços de e-mail dos usuários e expandir seus grupos de inscrições.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criando um formulário de inscrição por e-mail {#creating-an-email-sign-up-form}

### Etapa 1: Escolha seu modelo {#step-1-choose-your-template}

Ao criar uma mensagem no app de arrastar e soltar, selecione **Email sign-up** como modelo e, em seguida, selecione **Build message**. Esse modelo é compatível com apps para dispositivos móveis e navegadores web.

![O editor de mensagens no app com o modelo para um formulário de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Etapa 2: Configure os estilos da sua mensagem {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize o componente de inscrição por e-mail {#step-3-customize-your-email-sign-up-component}

Para começar a criar seu formulário de inscrição por e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de inscrições global **Subscribed**. Para fazer opt-in de usuários em grupos de inscrições específicos, consulte [Atualizando estados de inscrição de e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states).

Você pode personalizar o texto de placeholder e o texto do rótulo do elemento de captura de e-mail.

![O editor de mensagens no app com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Validação de e-mail {#email-validation}

Se o usuário inserir um endereço de e-mail que inclua caracteres especiais não aceitos, ele verá um indicador de erro genérico e não conseguirá enviar o formulário. Essa mensagem de erro não é personalizável. Você pode visualizar o comportamento de erro na guia **Preview & Test** e no seu dispositivo de teste. Saiba mais sobre como a Braze formata endereços de e-mail em [Validação de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation).

### Etapa 4: Adicione um texto de aviso legal (opcional) {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem {#step-5-style-your-message}

Personalize a aparência do seu formulário de inscrição usando os [componentes de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components) de arrastar e soltar.

## Analisando os resultados {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Práticas recomendadas {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}