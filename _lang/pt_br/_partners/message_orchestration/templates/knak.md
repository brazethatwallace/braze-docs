---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Este artigo de referência descreve a parceria entre a Braze e a Knak, uma plataforma de criação de campanhas que permite criar e-mails totalmente responsivos em minutos ou horas, em vez de dias ou semanas, e exportá-los como modelos prontos para uso na Braze."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) é a primeira plataforma de criação de campanhas construída para equipes de marketing empresarial usarem internamente. A plataforma de arrastar e soltar permite que qualquer pessoa crie e-mails e landing pages bonitos e alinhados à marca em minutos, sem precisar de código ou ajuda externa.

_Essa integração é mantida pela Knak._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Knak permite que você crie e-mails totalmente responsivos em minutos ou horas, em vez de dias ou semanas, e os exporte como modelos prontos para uso na Braze. A Knak é feita para profissionais de marketing que desejam aprimorar a criação de e-mails para campanhas gerenciadas na Braze, sem a necessidade de agências externas ou codificação manual.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Knak | É necessário ter uma conta Knak para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de **Modelos**. <br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

A Knak é feita para profissionais de marketing que desejam aprimorar a criação de seus e-mails, sem necessidade de codificação ou ajuda externa. É ótima para quem:
- Usa modelos simples para e-mails e quer mudar de patamar
- Depende de agências externas ou desenvolvedores para criar e-mails para a Braze
- Quer retomar o controle criativo sobre a criação de ativos e chegar ao mercado consideravelmente mais rápido

## Integração {#integration}

### Etapa 1: Configure sua integração {#step-1-configure-your-integration}

Na Knak, navegue para **Integrations** > **Platforms** > **+ Add New Integration**.

![Botão de adicionar integração]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

Em seguida, selecione a plataforma **Braze** e forneça a chave de API e o endpoint REST da Braze. Clique em **Create New Integration** para concluir sua integração.

![Criar nova integração]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### Etapa 2: Sincronize seus modelos Knak {#step-2-sync-your-knak-templates}

Na Knak, localize um e-mail que você gostaria de sincronizar com a Braze e selecione **Publish** e depois **Sync**.

![Integração 1 da Knak]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

Em seguida, verifique o nome do e-mail e clique em **Sync**.

![Integração 2 da Knak]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## Usando a integração {#using-the-integration}

Você pode encontrar os e-mails da Knak enviados na Braze em **Engajamento** > **Modelos e mídia**. Eles serão bonitos, alinhados à marca e totalmente responsivos. O único limite é a sua própria criatividade!