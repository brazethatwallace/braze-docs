---
nav_title: Smartling
article_title: Smartling
description: "Este artigo de referência descreve a parceria entre a Braze e o Smartling, um software baseado em nuvem para localização. O Braze Connector oferece suporte à tradução de modelos de e-mail HTML, Content Blocks, Canvas e mensagens de e-mail de Campaigns."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> O [Smartling](https://www.smartling.com/) é um software de gerenciamento de tradução em nuvem de ponta a ponta para clientes que buscam automatizar a tradução de sites, aplicativos e experiências do cliente.

_Essa integração é mantida pela Smartling._

## Sobre a integração {#about-the-integration}

O Braze Connector oferece suporte a traduções para mensagens em Campaigns e Canvas (e-mail, push, mensagens no app e banners), modelos de e-mail e Content Blocks. Consulte a tabela a seguir para saber quais tipos de editor são compatíveis com cada canal ou recurso.

| Canal/Recurso | Editor tradicional (ex. HTML) | Editor de arrastar e soltar |
| --------------- | ----------------------------- | -------------------- |
| [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [Mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | n/a |
| Modelo de e-mail | ✅ | ✅ |
| Banners | n/a | ✅ |
| Content Blocks | ✅ | ✅ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="About the integration" }


## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conta do Smartling | É necessário ter uma [conta Smartling](https://dashboard.smartling.com/) para aproveitar essa parceria. |
| Projeto de tradução Smartling | Para conectar sua conta da Braze ao Smartling, primeiro você deve fazer login e [criar um projeto de tradução](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as seguintes permissões: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional.]({{site.baseurl}}/api/basics/#endpoints) Seu endpoint depende da URL da Braze para sua instância. |
| Configurações multilíngues da Braze | [Conclua as configurações multilíngues na Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integração {#integration}

### Etapa 1: Definir as configurações multilíngues na Braze {#step-1-set-up-multi-language-settings-in-braze}

Consulte [as instruções de configuração multilíngue da Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) para configurar as localizações na Braze.

### Etapa 2: Configurar o projeto Braze no Smartling TMS {#step-2-set-up-the-braze-project-in-smartling-tms}

Consulte a [documentação do Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) para obter detalhes sobre a configuração do conector.

### Como conectar a Braze ao Smartling {#connecting-braze-to-smartling}

1. Em sua [conta Smartling](https://dashboard.smartling.com/), crie um tipo de projeto [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093).

![Conexão da Braze no Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. Nesse projeto, selecione **Settings** > **Braze Settings** > **Connect to Braze**.
3. Preencha os campos obrigatórios, como URL da API or interface de programação do aplicativo (API) e chave de API or interface de programação do aplicativo (API). Se a conexão de teste for bem-sucedida, salve a conexão. Se o teste não for bem-sucedido, confirme se você inseriu a URL da API or interface de programação do aplicativo (API) e a chave de API or interface de programação do aplicativo (API) corretas.

![Configurações de API da conexão da Braze no Smartling.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. Adicione outros idiomas ao projeto.

![Idiomas de projeto da conexão da Braze no Smartling.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. Em Braze Settings, verifique se os valores na coluna **Target Language (Braze)** correspondem às localizações configuradas nas configurações multilíngues da Braze. A convenção de nomenclatura da localização deve corresponder exatamente.

![Confirmação de idiomas da conexão da Braze no Smartling.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Etapa 3: Adicionar tags de tradução à sua mensagem da Braze {#step-3-add-translation-tags-to-your-braze-message}

Consulte [as instruções da Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) sobre como adicionar tags de tradução às suas mensagens:

- [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [Mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Aqui está um exemplo de uma Campaign de e-mail em HTML com tags de tradução.

![E-mail da Braze com tags de tradução.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Você deve salvar a mensagem como rascunho antes de selecionar as localizações.

### Etapa 4: Gerenciar traduções no Smartling {#step-4-manage-translations-in-smartling}

Depois de conectar e configurar o conector da Braze, encontre o conteúdo da Braze na guia Braze em seu projeto Smartling. Para saber mais, consulte a [documentação do Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

O Smartling oferece recursos avançados para pesquisar e selecionar conteúdo por:
- Pesquisa por palavra-chave
- Tipo de conteúdo da Braze
- Tags da Braze

1. Neste exemplo, a Campaign de e-mail de promoção de Ano Novo foi criada na [etapa 3](#step-3-add-translation-tags-to-your-braze-message).

![E-mail da Braze com tags de tradução.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. Depois de localizar a Campaign que deseja traduzir, selecione a pasta, escolha as variantes e selecione **Request Translation**.

![Solicitar traduções.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. Crie um novo trabalho para a tradução.

![Crie um novo trabalho para a tradução.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. Depois que o trabalho for autorizado, edite cada tradução na ferramenta CAT.

![Ferramenta CAT de tradução.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. Depois que as traduções forem concluídas, salve e envie sua tradução para a Braze.

![Enviar a tradução para a Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Etapa 5: Pré-visualizar a mensagem como um usuário multilíngue na Braze {#step-5-preview-the-message-as-a-multi-language-user-in-braze}

Na Braze, faça uma pré-visualização da sua Campaign como um usuário multilíngue para confirmar que as traduções foram aplicadas corretamente.

![Pré-visualização do usuário multilíngue.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Perguntas frequentes {#frequently-asked-questions}

### Há suporte para tags de tradução no editor de arrastar e soltar? {#are-translation-tags-supported-for-the-drag-and-drop-editor}

Para o editor de arrastar e soltar (e-mail, Content Block, mensagem no app), você deve adicionar manualmente as tags de tradução como Liquid tags.

### Como traduzir o texto dentro de uma Liquid tag? {#how-do-you-translate-text-within-a-liquid-tag}

O Smartling reconhece as Liquid tags e as torna variáveis não editáveis no criador. Qualquer outro texto dentro da Liquid tag, como texto padrão ou filtros como join, também se torna não editável no Smartling. No entanto, remova a Liquid tag no Smartling e recrie a Liquid tag com o texto padrão traduzido. Um aviso é exibido ao salvar a tradução.