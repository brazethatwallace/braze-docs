---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Este artigo de referência descreve a parceria entre a Braze e a Dyspatch, um construtor de e-mail de arrastar e soltar que permite criar e-mails bonitos, responsivos e envolventes sem a necessidade de escrever código."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) oferece um construtor de e-mail intuitivo de arrastar e soltar usado para criar e-mails bonitos, responsivos e envolventes sem precisar escrever código. Colabore com sua equipe para criar e aprovar e-mails na Dyspatch e, em seguida, exportá-los para a Braze, tudo em apenas algumas etapas!

_Essa integração é mantida pela Dyspatch._

## Sobre a integração {#about-the-integration}

A integração entre a Dyspatch e a Braze permite simplificar o ciclo de vida da criação de e-mails exportando modelos de e-mail da Dyspatch diretamente para a Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Dyspatch | Uma [conta Dyspatch](https://www.dyspatch.io/login/) com uma [função de proprietário ou administrador](https://docs.dyspatch.io/administration/dyspatch_roles/) é necessária para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de **Templates**. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A integração entre a Braze e a Dyspatch permite que você exporte modelos de e-mail da Dyspatch diretamente para sua Biblioteca de mídia na Braze ou baixe seu modelo e faça o upload manualmente.

### Etapa 1: Crie a integração com a Braze {#step-1-create-the-braze-integration}

No portal de administração da Dyspatch, abra o menu suspenso do seu nome de usuário e selecione **Integrations**. Crie uma nova integração, selecione **Braze** e insira sua chave de API da Braze.

No campo **Localize Exports By**, você pode escolher como gostaria de gerenciar a localização. Este campo permite que você [localize seus modelos de e-mail](https://docs.dyspatch.io/localization/localizing_a_template/) e os exporte para a Braze para enviar e-mails personalizados por idioma ou localidade com facilidade.

![Modelo de exportação da Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Etapa 2: Exportar modelo para a Braze {#step-2-export-template-to-braze}

Depois de concluir um e-mail na Dyspatch, para enviar seu modelo para a Braze, visualize o modelo de e-mail publicado e clique em **Download/Export** e depois em **Export to Integration**.

Se você quiser fazer upload do seu modelo manualmente, visualize o modelo de e-mail publicado e clique em **Download/Export** e depois em **Download HTML**. Em seguida, na seção **Templates & Media > Email Templates** da sua conta na Braze, selecione **From File** para fazer upload do seu modelo.

![Modelo de exportação da Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Não selecione **Inline CSS** na seção **Sending Info** para qualquer modelo de e-mail da Dyspatch na Braze. A Dyspatch cuida disso, garantindo que seus e-mails sejam robustos, responsivos e prontos para enviar.
{% endalert %}

### Uso {#usage}

Encontre o modelo da Dyspatch que você enviou na seção **Templates & Media > Email Templates** da sua conta na Braze. Agora você pode usar este modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!