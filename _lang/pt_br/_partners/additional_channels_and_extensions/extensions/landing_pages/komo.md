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

A integração entre a Braze e a Komo permite coletar dados primários e dados voluntários por meio dos Komo Engagement Hubs. Esses hubs são microsites dinâmicos que oferecem conteúdo interativo e recursos de gamificação. Os dados de usuários coletados nesses hubs são então transmitidos para a API or interface de programação do aplicativo (API) da Braze.

{% multi_lang_include partners/extensions/landing_pages/komo_integration_bullets.md %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Komo | Você precisará de uma conta Komo ativa para aproveitar essa parceria. Acesse [Komo](https://komo.tech/) para iniciar um teste agora. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [URL do seu endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Seu endpoint dependerá da URL da Braze para a sua instância.<br><br>Por exemplo, deve ser algo como: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

{% tabs local %}
{% tab Captura de dados - Envio de formulário %}

Quando um usuário envia um formulário de captura de dados personalizável no Komo, os campos do Komo mapeados na integração com a Braze são enviados para a Braze por meio da chamada de API or interface de programação do aplicativo (API) `/users/track/`.

Os formulários de captura de dados existem no início ou no final dos Cards.

{% endtab %}
{% tab Pesquisa de mercado - Em breve %}

O Komo também permite transmitir dados de pesquisa de mercado capturados quando um usuário responde a uma pergunta de quiz, enquete, teste de personalidade, swiper e similares. Esses dados permitem enriquecer o perfil de um usuário além dos dados capturados nos envios de formulários.

{% endtab %}
{% endtabs %}

## Integração {#integration}

### Etapa 1: Publicar um Hub de Engajamento e um cartão no Komo {#step-1-publish-a-komo-engagement-hub-and-card}

Você precisará publicar um Hub do Komo com pelo menos um cartão contendo um formulário de captura de dados. Após a publicação, você pode testar a experiência do usuário de ponta a ponta e verificar se a integração está funcionando corretamente.

![Hub do Komo.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Etapa 2: Adicionar o app conectado da Braze {#step-2-add-the-braze-connected-app}

No Komo, acesse a guia **Company Settings** e selecione a seção **Connected Apps**.

Em seguida, encontre a integração da Braze na lista e selecione o botão **Connect** para ativar a integração.

![Conectar a integração da Braze.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Conectar a integração da Braze, etapa 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Configurar a integração por meio de um Workflow {#configure-the-integration-via-a-workflow}

Agora você precisa configurar um workflow, dentro de um Workspace, Site ou Card, para sincronizar dados com a Braze.

Se você define o escopo do workflow para todo o Workspace, um Site (que contém vários Cards) ou um único Card, depende de se você deseja que o workflow seja disparado em vários Cards ou Campaigns.

Depois de criar um Workflow, defina seu gatilho, procure por Braze no menu de etapas e adicione a etapa "Track User".

![Configuração do Track User.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

A partir daqui, configure os eventos, atribuições e inscrições que você deseja sincronizar do Komo para a Braze.

![Lista de blocos de conteúdo.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Usando a integração {#using-the-integration}

Agora sua integração está configurada e funcionando, e você pode monitorar cada execução na guia Workflow Runs.