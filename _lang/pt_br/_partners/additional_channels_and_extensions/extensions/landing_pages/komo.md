---
nav_title: Komo
article_title: Komo
description: "Este artigo de referência descreve a parceria entre a Braze e a Komo, uma plataforma de engajamento com clientes especializada em gamificação, conteúdo interativo, competições, prêmios e fidelidade. Por meio dessa integração, dados primários e dados voluntários capturados na Komo podem ser publicados na Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [A Komo](https://komo.tech/) é uma plataforma de engajamento com clientes especializada em gamificação, conteúdo interativo, competições, prêmios e fidelidade.

_Essa integração é mantida pela Komo._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Komo permite coletar dados primários e dados voluntários por meio dos hubs de engajamento da Komo. Esses hubs são microsites dinâmicos que oferecem conteúdo interativo e recursos de gamificação. Os dados de usuários coletados nesses hubs são então transmitidos para a API da Braze.

- Ingestão em tempo real na Braze de dados primários e dados voluntários de usuários coletados da Komo
- Ingerir dados de pesquisas de marketing e de preferências dos usuários quando eles respondem a pesquisas, enquetes e perguntas de questionários
- Criar progressivamente perfis de usuário na Braze ao longo do tempo, à medida que o usuário continua a se engajar e a compartilhar mais dados sobre si mesmo
- Padronizar a aparência dos e-mails de transação enviados pela Braze

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Komo | Você precisará de uma conta Komo ativa para aproveitar essa parceria. Visite a [Komo](https://komo.tech/) para iniciar um teste agora. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância.<br><br>Por exemplo, deve ficar parecido com: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

{% tabs local %}
{% tab Data Capture - Form Submission %}

Quando um usuário envia um formulário de captura de dados personalizável na Komo, os campos da Komo mapeados na integração da Braze são passados para a Braze por meio da chamada de API `/users/track/`.

Os formulários de captura de dados existem no início ou no final dos cartões.

{% endtab %}
{% tab Market Research - Coming soon %}

A Komo também permite transmitir dados de pesquisa de marketing capturados quando um usuário responde a uma pergunta de questionário, enquete, teste de personalidade, swiper e similares. Esses dados permitem aprimorar o perfil de um usuário além dos dados capturados nos envios de formulários.

{% endtab %}
{% endtabs %}

## Integração {#integration}

### Etapa 1: Publicar um hub e um cartão de engajamento da Komo {#step-1-publish-a-komo-engagement-hub-and-card}

Você precisará publicar um Komo Hub com pelo menos um cartão contendo um formulário de captura de dados. Após a publicação, é possível testar a experiência do usuário de ponta a ponta e verificar se a integração está funcionando corretamente.

![Komo Hub.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Etapa 2: Adicionar o app conectado da Braze {#step-2-add-the-braze-connected-app}

Na Komo, acesse a guia **Configurações da empresa** e selecione a seção **Connected Apps**.

Em seguida, localize a integração da Braze na lista e selecione o botão **Connect** para ativar a integração.

![Conectar a integração da Braze.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Conectar a integração da Braze, etapa 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Configurar a integração por meio de um fluxo de trabalho {#configure-the-integration-via-a-workflow}

Agora você precisa configurar um fluxo de trabalho, dentro de um espaço de trabalho, site ou cartão, para sincronizar os dados com a Braze.

O escopo do fluxo de trabalho — se abrange todo o espaço de trabalho, um site (que contém vários cartões) ou um único cartão — depende de você querer que o fluxo de trabalho seja disparado em vários cartões ou campanhas.

Depois de criar um fluxo de trabalho, defina seu gatilho, procure a Braze no menu de etapas e adicione a etapa "Track User".

![Configuração de Track User.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

A partir daqui, configure os eventos, as atribuições e as inscrições que você deseja sincronizar da Komo para a Braze.

![Lista de blocos de conteúdo.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Usando a integração {#using-the-integration}

Agora sua integração está funcionando e você pode monitorar cada execução na guia de execuções do fluxo de trabalho.