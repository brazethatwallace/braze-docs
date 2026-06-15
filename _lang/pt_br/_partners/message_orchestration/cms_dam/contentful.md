---
nav_title: Contentful
article_title: Contentful
description: "Este artigo de referência descreve a parceria entre a Braze e o Contentful, um sistema de gerenciamento de conteúdo que permite usar dinamicamente o Conteúdo conectado para extrair conteúdo do Contentful para suas Campaigns da Braze."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) é um sistema de gerenciamento de conteúdo headless que permite criar, gerenciar e distribuir conteúdo para qualquer plataforma. Ao contrário de um sistema de gerenciamento de conteúdo (CMS), o Contentful permite que você crie seu modelo de conteúdo para que possa decidir qual conteúdo deseja gerenciar.<br><br>Esta página fornece um guia passo a passo para configurar o Conteúdo conectado da Braze para buscar dados da API de Entrega de Conteúdo do Contentful.

Depois de integrado, você pode usar as APIs RESTful do Contentful para entregar seu conteúdo em vários canais, como sites, apps móveis (iOS, Android e Windows) ou muitas outras plataformas. Você também pode extrair dinamicamente conteúdo do Contentful para usar em suas Campaigns da Braze.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|-----------------------|------------------------------------|
| Uma conta Contentful | Você precisa de uma conta Contentful com acesso à API de Entrega de Conteúdo. |
| Uma conta Braze | Você precisa de uma conta Braze com acesso ao recurso de Conteúdo conectado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Obtenha suas credenciais da API do Contentful {#step-1-get-your-contentful-api-credentials}

1. [Faça login no Contentful](https://app.contentful.com/login) com suas credenciais.
2. Crie ou recupere tokens de acesso da API no dashboard do Contentful acessando **Settings** > **API keys**. Se você ainda não tiver uma chave de API, crie uma nova:<br>2.1 Selecione **Add API key**.<br>2.2 Insira os detalhes necessários e selecione o ambiente apropriado.<br>2.3 Selecione **Save** e anote o **Space ID** e o **Content Delivery API - access token**.
3. Identifique o modelo de conteúdo que você deseja acessar por meio da API do Contentful.

### Etapa 2: Configure o Conteúdo conectado da Braze {#step-2-configure-braze-connected-content}

1. [Faça login na Braze](https://dashboard.braze.com/sign_in) com suas credenciais.
2. No dashboard da Braze, acesse **Content** > **Content Block** > **Create Content Block** > **HTML code editor**.
3. Crie uma solicitação de Conteúdo conectado para a [URL da API de Entrega de Conteúdo do Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links). Um exemplo de URL da API de Entrega de Conteúdo do Contentful é `https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries`.<br><br> A recuperação de diferentes ativos requer a inclusão de variáveis específicas. A solicitação de URL de Conteúdo conectado do exemplo tem como alvo o endpoint [Entry](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) do Contentful. Esse endpoint precisa de variáveis como `{space_id}` e `{environment_id}`, ou `{entry_id}` e `{access_token}`. Esses valores podem ser obtidos da sua instância do Contentful. Neste exemplo de bloco de conteúdo, as variáveis devem ser substituídas pelo seu Space ID e Environment ID do Contentful.<br><br>A URL de exemplo da API de Entrega de Conteúdo usa apenas um dos endpoints disponíveis do Contentful. Diferentes casos de uso podem ser alcançados aproveitando diferentes URLs. Por exemplo, a [Image API](https://www.contentful.com/developers/docs/references/images-api/) pode ser usada para capturar imagens armazenadas no Contentful. Para saber mais, consulte a [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/).

{% alert note %}
Diferentes endpoints podem exigir novas variáveis; por exemplo, a Images API requer um `{asset_id}`, `{unique_id},` e `{name}`. Para mais orientações, entre em contato com o Contentful.
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4. Use "Test Endpoint" para testar se a Braze consegue se conectar com sucesso à API do Contentful e recuperar os dados desejados.
5. Selecione **Done** para salvar seu bloco de conteúdo.
6. Dê ao seu bloco de conteúdo um nome descritivo, como "API Contentful", e então selecione **Launch Content Block**.

### Etapa 3: Use o Conteúdo conectado em Campaigns e Canvas {#step-3-use-connected-content-in-campaigns-and-canvasses}

1. Na Braze, crie uma nova Campaign ou edite uma existente.
2. Use o bloco de Conteúdo conectado para inserir dados buscados do Contentful. Use os caminhos de dados que você definiu durante a configuração para preencher dinamicamente o conteúdo da Campaign.<br><br>
- **Caminho de resposta:** Após incluir o bloco de conteúdo em uma Campaign ou Canvas da Braze, a resposta se torna disponível quando você insere a variável `{response}` na sua mensagem.<br><br>A notação de ponto JSON permite que você especifique qual parte do corpo da resposta do Contentful deseja incluir na sua mensagem. Isso vai variar com base no seu caso de uso. Por exemplo, você pode usar o valor do título ({% raw %}`liquid{{response.items[0].fields.title}}`{% endraw %}) do endpoint de Entry do Contentful e receber uma resposta como esta:

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3. Visualize e teste sua Campaign para confirmar que os dados do Conteúdo conectado são exibidos corretamente.
4. Quando estiver satisfeito com a configuração, lance sua Campaign.

## Solução de problemas {#troubleshooting}

### Resposta da API {#api-response}

Certifique-se de que suas credenciais da API do Contentful e a URL do endpoint estão corretas. Verifique se há mensagens de erro na Braze que possam indicar problemas com a chamada da API.

### Mapeamento de dados {#data-mapping}

Verifique se os mapeamentos de caminho de resposta estão configurados corretamente e se a estrutura da resposta da API corresponde às suas expectativas.

## Recursos adicionais {#additional-resources}

- [Documentação da Content Delivery API do Contentful](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Conteúdo conectado da Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)
- [Content Blocks da Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)