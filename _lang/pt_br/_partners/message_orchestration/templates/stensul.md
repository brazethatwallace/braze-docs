---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Este artigo de referência descreve a parceria entre a Braze e a Stensul, uma plataforma de e-mail corporativo para a criação de modelos de e-mail responsivos a dispositivos móveis em todos os canais."
page_type: partner
search_tag: Partner

---

# Stensul

> A [Stensul](https://stensul.com/) fornece aos profissionais de marketing de e-mail ferramentas para criar e-mails responsivos a dispositivos móveis e alinhados à marca na Stensul antes de enviá-los para a Braze em tempo real para a criação de campanhas.

_Essa integração é mantida pela Stensul._

## Sobre a integração {#about-the-integration}

A integração da Braze com a Stensul permite exportar seus e-mails da Stensul formatados em HTML e fazer upload deles como modelos na Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ------------| ----------- |
| Conta da Stensul | É necessário ter uma conta da Stensul para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões completas de **Templates**. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Instância do cluster | Sua [instância de cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze está alinhada com o dashboard e o endpoint REST or transferir estado representacional da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Forneça sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional e a instância do cluster da Braze para a equipe de sucesso do cliente da Stensul. A equipe configurará a integração inicial para você.

{% alert important %}
Essa é uma configuração única, e todas as exportações futuras utilizarão automaticamente essa chave de API or interface de programação do aplicativo (API).
{% endalert %}

### Etapa 1: criar o e-mail na Stensul {#step-1-create-stensul-email}

Crie um e-mail na plataforma Stensul e clique em **Complete**.

![Opções de salvamento da Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Etapa 2: exportar modelo para a Braze {#step-2-export-template-to-braze}
Na nova caixa de diálogo que aparece na página de conclusão, selecione **Upload to ESP**.

![Opções de upload da Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Em seguida, insira o **template name**, o **subject** e o **preheader** do e-mail e selecione **Upload**. Você receberá uma confirmação de que o upload foi bem-sucedido e um histórico de uploads anteriores do arquivo, se aplicável.

![Upload bem-sucedido da Stensul]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Uso {#usage}

Encontre o modelo da Stensul que você enviou na seção **Templates & Media > Email Templates** da sua conta na Braze. Agora você pode usar esse modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!