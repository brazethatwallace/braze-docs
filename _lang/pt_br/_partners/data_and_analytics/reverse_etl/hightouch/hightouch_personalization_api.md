---
nav_title: API de Personalização Hightouch
article_title: API de Personalização Hightouch
description: "Este artigo de referência descreve a integração entre a Braze e a API de Personalização da Hightouch, um serviço gerenciado para hospedar uma API de dados de baixa latência baseada em qualquer conjunto de dados dentro do seu data warehouse na nuvem. Este artigo de referência aborda os casos de uso que a API de Personalização da Hightouch resolve, os dados com os quais ela trabalha, como configurá-la e como integrá-la com a Braze."
page_type: partner
search_tag: Partner
---

# API de Personalização Hightouch {#hightouch-personalization-api}

> A [API de Personalização](https://hightouch.com/docs/destinations/personalization-api) da Hightouch é um serviço gerenciado que permite hospedar uma API de dados de baixa latência baseada em qualquer conjunto de dados no seu data warehouse na nuvem.

![]({% image_buster /assets/img/hightouch/cohort7.png %})

A integração da Braze com a Hightouch permite que você use a API com o [Conteúdo conectado da Braze]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) para obter dados atualizados de clientes ou objetos em suas Campaigns ou Canvas no momento do envio.

A API de Personalização da Hightouch fornece um endpoint REST para usar na sua configuração da Braze. Especificamente, você pode usar a oferta de Conteúdo conectado da Braze para fazer uma solicitação GET à API de Personalização e recuperar todas as informações relacionadas a um identificador específico. Os dados expostos por essa API podem representar dados de clientes, produtos ou qualquer outro objeto.

![]({% image_buster /assets/img/hightouch/cohort6.png %})

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| [Conta Hightouch](https://app.hightouch.com/login) com API de Personalização ativada | É necessária uma conta [Business Tier](https://hightouch.com/pricing) da Hightouch para aproveitar essa parceria. |
| Casos de uso definidos | Antes de configurar a API, determine seu caso de uso para essa integração. Consulte a lista a seguir para ver os casos de uso comuns. |
| Dados armazenados em um data warehouse na nuvem ou outra fonte | A Hightouch tem integração com [mais de 25 fontes de dados](https://hightouch.com/integrations) |
| Chave de API Hightouch | Pode ser criada em **Hightouch > Settings > API keys > Add API key**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Casos de uso %}

### Casos de uso {#use-cases}

Antes de começar, é útil planejar exatamente como você deseja usar a API de Personalização.

Casos de uso comuns incluem:
- **Recomendações de produtos** para simplificar a incorporação de recomendações de produtos personalizadas em modelos de e-mail, Campaigns ou experiências no app
- **Impulsionar Campaigns de marketing personalizadas** ao enriquecer os pontos de contato de marketing com recomendações de produtos dinâmicas
- **Oferecer personalização no app ou na web**, por exemplo, resultados de pesquisa personalizados, preços baseados em coorte e envio de mensagens, recomendações de artigos ou localizações de lojas mais próximas
- **Recomendações baseadas em dados financeiros ou médicos** — dados financeiros têm requisitos rigorosos que a Hightouch atende por meio de suas [políticas rigorosas de segurança de dados](https://hightouch.com/docs/security/overview#compliance). Com a Hightouch, você pode criar segmentos de clientes com base em dados financeiros ou médicos sem expor os atributos subjacentes usados em seus critérios de segmentação.

{% endtab %}
{% tab Conjuntos de dados %}

### Conjuntos de dados {#datasets}

A API de Personalização atua como um cache para os dados selecionados no seu warehouse, então você já deve ter os dados de recomendação armazenados lá. Você pode usar a Hightouch para transformá-los de acordo com um modelo, se necessário. Esse tipo de dados inclui:
- Metadados do usuário, como região geográfica, idade ou outras informações demográficas
- Ações ou eventos do usuário, incluindo compras anteriores, visualizações de páginas, cliques, etc.

{% endtab %}
{% endtabs %}

## Integração {#integration}

### Etapa 1: Conectar a fonte de dados à Hightouch {#step-1-connect-data-source-to-hightouch}

As [fontes](https://hightouch.com/docs/getting-started/concepts#sources) da Hightouch são onde os dados comerciais da sua organização residem. Neste caso, é onde seus dados de usuários são armazenados.
1. Na Hightouch, acesse **Sources Overview > Add Source**. Selecione seu data warehouse como a fonte.<br><br>
2. Insira as credenciais relevantes; elas variarão dependendo da fonte.

Para mais detalhes, consulte a [documentação](https://hightouch.com/docs) relevante.

### Etapa 2: Modelar os dados {#step-2-model-data}

Os modelos da Hightouch definem quais dados extrair da sua fonte. Para configurar um novo modelo, siga estas etapas:

1. Na Hightouch, acesse [**Models overview**](https://app.hightouch.com/models) > **Add model** e selecione a fonte que você acabou de conectar.<br><br>
2. Em seguida, escolha um [método de modelagem](https://hightouch.com/docs/models/creating-models). Como todas as suas informações devem ser reunidas em uma única tabela, você pode usar o seletor de tabela visual para defini-la. Alternativamente, você pode escrever SQL para incluir apenas as colunas que deseja ou utilizar seus modelos dbt existentes, Looker Looks ou workbooks da Sigma.<br><br>
3. Antes de continuar, visualize seu modelo para confirmar se ele está consultando os dados de seu interesse. Por padrão, a Braze limita a pré-visualização aos primeiros 100 registros. Depois de validar seus dados, clique em **Continue**.<br><br>
4. Dê um nome ao seu modelo, por exemplo, "Recomendações do usuário".<br><br>
5. Por fim, selecione uma chave primária e clique em **Finish**. Uma chave primária deve ser uma coluna com identificadores únicos. Este é também o campo que você usará para chamar a API de Personalização e recuperar as recomendações de um usuário específico.

### Etapa 3: Configurar a API de Personalização {#step-3-configure-personalization-api}

A preparação da API para receber solicitações tem duas etapas:
- Ativar a API de Personalização nas regiões mais próximas da sua infraestrutura
- Criar sincronizações para definir quais modelos devem ser materializados no cache gerenciado pela Hightouch

Siga estas instruções para completar ambas:

1. Na Hightouch, acesse [**Destinations**](https://app.hightouch.com/destinations) e selecione a API de Personalização da Hightouch criada para você. Se você não tiver esse destino ativado, entre em contato com o [suporte da Hightouch](mailto:friends@hightouch.com).<br><br>
2. Em seguida, selecione a região apropriada. Selecionar a região mais próxima da sua infraestrutura reduzirá seus tempos de resposta. Se você não vir uma região próxima à sua infraestrutura, entre em contato com o [suporte da Hightouch](mailto:friends@hightouch.com).<br><br>
3. Acesse a [página de visão geral de **Syncs**](https://app.hightouch.com/syncs) e clique no botão **Add sync**. Em seguida, selecione o modelo relevante e o destino que você configurou anteriormente.<br><br>
4. Digite um nome de coleção alfanumérico. Coleções são conceitualmente semelhantes a tabelas de banco de dados. Cada uma deve representar um tipo de dado específico, como clientes ou faturas. Os nomes das coleções devem ser alfanuméricos e farão parte do seu endpoint da API de Personalização.<br><br>
5. Em seguida, especifique qual coluna do seu modelo deve servir como índice principal para consultas de registros. Esse campo deve identificar exclusivamente cada registro na coleção e muitas vezes é o mesmo que a chave primária do seu modelo. A API de Personalização suporta pesquisas em vários índices. Por exemplo, pode ser do seu interesse recuperar perfis de clientes usando `user_id`, `anonymous_id` ou `email_address`. Para ativar vários índices, entre em contato com o [suporte da Hightouch](mailto:friends@hightouch.com).<br><br>
6. Use o mapeador de campos para especificar quais colunas do seu modelo devem ser incluídas na carga útil da resposta da API. Você pode renomear esses campos e usar o mapeador avançado para aplicar transformações usando a linguagem de modelo Liquid.<br><br>
7. Selecione o [comportamento de exclusão](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) apropriado para o seu caso de uso.<br><br>
8. Por fim, clique em **Continue** e depois selecione um [cronograma de sincronização](https://hightouch.com/docs/syncs/schedule-sync-ui).

A Hightouch agora sincronizará os dados do seu warehouse para um banco de dados gerenciado e os exporá por meio da API de Personalização.

### Etapa 4: Chamar a API de Personalização por meio do Conteúdo conectado da Braze {#step-4-call-personalization-api-through-braze-connected-content}

Depois de configurar sua instância da API de Personalização, você pode usá-la como um endpoint de Conteúdo conectado da Braze.

A API está acessível em `https://personalization.{region}.hightouch.com`, por exemplo, `https://personalization.us-west-2.hightouch.com`.

As informações estão disponíveis usando este endpoint `/v1/collections/:collection_name/records/:index_key/:index_value`.

Por exemplo, você poderia incluir este trecho em uma Campaign ou Canvas:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Você pode usar a modelagem Liquid para referenciar as propriedades retornadas na carga útil JSON e usá-las no seu envio de mensagens.

Para a carga útil de exemplo abaixo:

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ]
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    }
}
```

As seguintes referências Liquid retornariam estes dados de exemplo:

| Modelo Liquid | Exemplo retornado |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %} | Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %} | San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %} | Universal Language |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solução de problemas {#troubleshooting}

Se você tiver dúvidas, entre em contato com o [suporte da Hightouch](mailto:friends@hightouch.com) para obter assistência.