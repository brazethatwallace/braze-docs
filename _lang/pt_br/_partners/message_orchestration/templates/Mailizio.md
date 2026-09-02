---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "Este artigo de referência descreve a parceria entre a Braze e a Mailizio, uma plataforma de criação e gerenciamento de e-mails que permite criar conteúdo reutilizável e seguro para a marca e exportá-lo para a Braze."
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio](https://mailizio.com/) é uma plataforma de criação e gerenciamento de e-mails que facilita a criação de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração da Mailizio à Braze, você pode exportar seus blocos de conteúdo e modelos de e-mail e, em seguida, gerar automaticamente mensagens no app a partir desses mesmos ativos, possibilitando uma implantação de campanha rápida e totalmente controlada.

*Essa integração é mantida pela Mailizio.*

## Sobre a integração {#about-the-integration}

A integração entre a Mailizio e a Braze permite que você crie modelos dinâmicos de e-mail usando o editor da Mailizio, aproveite as variáveis Liquid usadas nas configurações da Braze e envie-os para a Braze para agilizar a execução de campanhas.

## Casos de uso {#use-cases}

- Envie modelos de e-mail prontos para envio diretamente para a Braze para Campaigns e mensagens transacionais.
- Crie módulos de conteúdo reutilizáveis (cabeçalhos, rodapés, promoções e outros) para otimizar a produção em várias Campaigns e canais.
- Gere mensagens no app a partir de e-mails: a Mailizio identifica seções relevantes do seu e-mail e permite exportar o HTML para uso nas suas campanhas no app.
- Personalize em escala com variáveis Liquid compatíveis com a Braze em e-mails e mensagens no app.
- Mantenha a consistência da sua marca gerenciando ativos criativos na Mailizio e atualizando-os na Braze com uma única exportação.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Mailizio | É necessário ter uma conta Mailizio para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões completas de **Templates**.<br><br>Você pode criar uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint depende da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

Forneça sua chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze e a instância do cluster para o gerente de sucesso do cliente da Mailizio. A equipe da Mailizio configura a integração inicial para você.

{% alert important %}
Essa é uma configuração única, e todas as exportações futuras utilizarão automaticamente essa chave de API or interface de programação do aplicativo (API).
{% endalert %}

### Etapa 1: Criar um e-mail na Mailizio {#step-1-create-an-email-in-mailizio}

Na Mailizio, use o editor de arrastar e soltar para criar um e-mail que reflita a identidade da sua marca e, em seguida, clique em **Save** para salvar seu trabalho.

![Captura de tela do editor de arrastar e soltar]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### Etapa 2: Exportar seu modelo de e-mail para a Braze {#step-2-export-your-email-template-to-braze}

Quando estiver pronto, clique em **Export Newsletter**. Na janela pop-up, selecione **Braze-email** e confirme a exportação.

Se você atualizar seu conteúdo posteriormente, exporte-o novamente da Mailizio para atualizá-lo na Braze.

![Captura de tela do modal de exportação]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}
Você pode criar e exportar blocos de conteúdo da mesma forma usando o editor de **módulos** da Mailizio.
{% endalert %}

## Uso {#usage}

Localize o modelo da Mailizio que você fez upload na seção **Modelos e mídia** > **Modelos de e-mail** da sua conta na Braze. Agora você pode usar esse modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!