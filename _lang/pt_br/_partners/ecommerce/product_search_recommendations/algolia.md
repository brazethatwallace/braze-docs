---
nav_title: Algolia
article_title: Algolia
description: "Saiba como usar a Algolia com o Conteúdo conectado da Braze para entregar dinamicamente resultados de pesquisa personalizados e recomendações de produtos nas suas mensagens da Braze."
alias: /partners/algolia/
page_type: partner
search_tag: Partner
---

# Algolia

> A [Algolia](https://www.algolia.com/) é uma plataforma de pesquisa e descoberta que ajuda desenvolvedores a criar experiências de pesquisa rápidas, relevantes e escaláveis. Com uma abordagem poderosa baseada em API or interface de programação do aplicativo (API), a Algolia combina algoritmos avançados de ranqueamento com insights orientados por IA para pesquisa em sites, navegação e descoberta de conteúdo personalizado de forma integrada.

A integração entre Algolia e Braze usa o [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) para preencher resultados de pesquisa e recomendações de produtos da Algolia nas suas mensagens da Braze. Ao consultar a API or interface de programação do aplicativo (API) da Algolia no momento do envio, você pode entregar conteúdo personalizado que direciona os usuários para páginas de detalhes de produtos ou landing pages de alta conversão.

## Casos de uso {#use-cases}

- **Promover produtos em alta:** Extraia automaticamente produtos em alta ou com melhor desempenho da Algolia para mensagens da Braze, promovendo itens de alto interesse e aumentando o engajamento.
- **Personalizar campanhas com inteligência de pesquisa:** Personalize Campaigns da Braze usando a inteligência de pesquisa e navegação da Algolia para entregar produtos ou categorias alinhados com os interesses de cada usuário.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|-------------|-------------|
| Conta na Algolia | Uma conta na Algolia é necessária para aproveitar essa parceria. |
| Credenciais de API or interface de programação do aplicativo (API) da Algolia | Sua chave de API or interface de programação do aplicativo (API) e ID de aplicativo da Algolia. |
| Índice de produtos da Algolia | Um índice da Algolia preenchido com os dados dos seus produtos. Isso é necessário para usar as APIs de Search ou Recommend. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Configure sua solicitação de API or interface de programação do aplicativo (API) da Algolia {#step-1-set-up-your-algolia-api-request}

Para saber mais sobre formatos de solicitação, estruturas de resposta e uso, consulte a documentação da [API or interface de programação do aplicativo (API) de Search da Algolia](https://www.algolia.com/doc/rest-api/search) e da [API or interface de programação do aplicativo (API) de Recommend da Algolia](https://www.algolia.com/doc/rest-api/recommend). Se precisar de ajuda com a configuração, entre em contato com a equipe da Algolia.

{% tabs local %}
{% tab Search API or interface de programação do aplicativo (API) %}

#### Exemplo de solicitação da Search API or interface de programação do aplicativo (API) {#example-search-api-request}

```
POST https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{INDEX_NAME}/query
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Exemplo de carga útil da consulta {#example-query-payload}

```json
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
```

Neste exemplo, a consulta recupera os quatro principais resultados de uma página que usa um filtro de categoria baseado em um atributo chamado `category_page_id`. O parâmetro `attributesToRetrieve` limita a resposta para manter a carga útil em um tamanho gerenciável.

**Exemplo de caso de uso:** Para exibir resultados de pesquisa de `https://www.yoursite.com/weekly-offers` em uma Campaign de ofertas semanais da Braze, consulte o índice correspondente da Algolia e aplique filtros para recuperar os principais resultados dessa página.

{% alert tip %}
Recupere campos adicionais usando `attributesToRetrieve` para aprimorar a personalização, como avaliações, reviews ou descontos.
{% endalert %}

{% endtab %}
{% tab Recommend API or interface de programação do aplicativo (API) %}

#### Exemplo de solicitação da Recommend API or interface de programação do aplicativo (API) {#example-recommend-api-request}

```
POST https://{ALGOLIA_APP_ID}.algolia.net/1/indexes/*/recommendations
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### Exemplo de carga útil da consulta

```json
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
```

A Recommend API or interface de programação do aplicativo (API) suporta múltiplos modelos, incluindo **Frequently Bought Together**, **Related Products**, **Trending Items**, **Trending Facet Values** e **Looking Similar**. Este exemplo usa o modelo **Trending Items**.

{% alert important %}
Se suas recomendações dependem de atributos específicos do usuário ou objectIDs, esteja atento aos limites de taxa definidos no seu contrato com a Algolia. Consulte a seção [Considerações](#considerations) para conhecer as melhores práticas.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 2: Implemente o Conteúdo conectado da Braze {#step-2-implement-braze-connected-content}

Use o recurso de Conteúdo conectado da Braze para fazer chamadas de API or interface de programação do aplicativo (API) para os endpoints da Algolia e injetar dinamicamente a resposta em uma mensagem. Para saber mais sobre configuração, formatação de solicitações e melhores práticas, consulte [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

{% tabs local %}
{% tab Search API or interface de programação do aplicativo (API) %}

#### Exemplo de solicitação de Conteúdo conectado para Search {#example-connected-content-search-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}-dsn.algolia.net/1/indexes/{{INDEX_NAME}}/query
  :method post
  :headers {"X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_search
%}
```
{% endraw %}

{% endtab %}
{% tab Recommend API or interface de programação do aplicativo (API) %}

#### Exemplo de solicitação de Conteúdo conectado para Recommend {#example-connected-content-recommend-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}.algolia.net/1/indexes/*/recommendations
  :method post
  :headers {"X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_recommendations
%}
```
{% endraw %}

{% endtab %}
{% endtabs %}

### Etapa 3: Formate os resultados de pesquisa nas mensagens da Braze {#step-3-format-search-results-in-braze-messages}

Após buscar os resultados da Algolia, use Liquid para analisar a resposta da API or interface de programação do aplicativo (API) e renderizar dinamicamente os resultados dentro da sua mensagem.

{% tabs local %}
{% tab Search API or interface de programação do aplicativo (API) %}

#### Exemplo de modelo de e-mail em Liquid para Search API or interface de programação do aplicativo (API) {#example-liquid-email-template-for-search-api}

{% raw %}
```liquid
{% for item in algolia_search.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

Isso gera uma lista de produtos a partir dos resultados da Search API or interface de programação do aplicativo (API) dentro do corpo da mensagem. Cada link de produto direciona os usuários para uma página de detalhes do produto (PDP) ou uma landing page específica da Campaign.

{% endtab %}
{% tab Recommend API or interface de programação do aplicativo (API) %}

#### Exemplo de modelo de e-mail em Liquid para Recommend API or interface de programação do aplicativo (API) {#example-liquid-email-template-for-recommend-api}

{% raw %}
```liquid
{% for item in algolia_recommendations.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

Isso gera uma lista de produtos recomendados a partir dos resultados da Recommend API or interface de programação do aplicativo (API) dentro do corpo da mensagem. Cada link de produto direciona os usuários para uma página de detalhes do produto (PDP) ou uma landing page específica da Campaign.

{% endtab %}
{% endtabs %}

## Considerações {#considerations}

### Evitar consultas únicas {#avoiding-unique-queries}

Esteja atento aos limites de taxa da Algolia definidos no seu contrato. Evite fazer consultas específicas por usuário, pois elas podem exceder rapidamente o número de solicitações permitidas. Para personalizar os resultados, direcione para um Segment or segmento or segmento em vez de um ID de usuário individual, ou filtre por categoria ou marca em vez de um objectID específico. Use atributos da Braze para personalizar ainda mais as recomendações.

### Armazenar em cache os resultados do Conteúdo conectado {#caching-connected-content-results}

Armazene em cache os resultados do Conteúdo conectado usando `cache_max_age` para minimizar as solicitações de API or interface de programação do aplicativo (API) para a Algolia e melhorar o desempenho. Para saber mais, consulte [Armazenamento de respostas em cache]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/).