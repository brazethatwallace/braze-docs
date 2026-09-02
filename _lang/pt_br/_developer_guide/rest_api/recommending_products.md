---
nav_title: Recomendar produtos aos usuários
article_title: Recomendando produtos aos usuários
page_order: 4
page_type: reference
description: "Este artigo de referência explica como usar a REST API da Braze, catálogos e Conteúdo Conectado para recomendar produtos aos usuários em diferentes canais de envio de mensagens."
---

# Recomendando produtos aos usuários {#recommending-products-to-users}

> Use a REST API da Braze junto com [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/create) ou [Conteúdo Conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para exibir recomendações personalizadas de produtos nas suas mensagens. Essa abordagem permite que você conecte seu próprio mecanismo de recomendação ao ecossistema de envio de mensagens da Braze, para que usuários não técnicos possam gerenciar o conteúdo e as mensagens relacionadas a cada recomendação.

Com essa abordagem, você pode:

- Armazenar recomendações de produtos nos perfis de usuário a partir do seu backend usando a REST API.
- Recuperar metadados de produtos no momento do envio usando catálogos ou Conteúdo Conectado.
- Exibir recomendações personalizadas em qualquer canal de envio de mensagens, incluindo e-mail, push, mensagens no app e muito mais.

## Pré-requisitos {#prerequisites}

Para concluir este guia, você precisa de:

| Requisito | Descrição |
| --- | --- |
| Chave da API REST da Braze | Uma chave com a permissão `users.track` e, se estiver gerenciando catálogos via API, as permissões de catálogos relevantes. Para criar uma, acesse **Configurações** > **Chaves de API**. |
| Catálogo da Braze | Um catálogo contendo os metadados dos seus produtos (como nome, categoria, preço e URL da imagem). Para criar um, consulte [Criar um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create). |
| Conhecimento de Liquid | Familiaridade intermediária com [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) para criar modelos com variáveis personalizadas e usar Connected Content. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Etapa 1: Armazenar recomendações nos perfis de usuário {#step-1-store-recommendations-on-user-profiles}

Para começar, armazene as recomendações de produto geradas pelo seu mecanismo de recomendação nos perfis de usuário da Braze como atributos personalizados. Isso permite que você faça referência aos produtos recomendados de cada usuário no momento do envio da mensagem.

1. Determine quais dados de recomendação armazenar, como IDs de produtos ou categorias preferidas.
2. Use o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para gravar a recomendação como um atributo personalizado no perfil de usuário.

### Exemplo de requisição {#example-request}

```http
POST YOUR_REST_ENDPOINT/users/track
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Substitua `YOUR_REST_ENDPOINT` pela [URL do endpoint REST]({{site.baseurl}}/api/basics#endpoints) do seu espaço de trabalho.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "recommended_product_id": "1001"
    }
  ]
}
```

Use nomes de atributo significativos (como `recommended_product_id`) para que sejam fáceis de referenciar em modelos Liquid posteriormente. Mantenha as recomendações precisas atualizando-as regularmente à medida que seu mecanismo de recomendação produz novos resultados.

## Etapa 2: Recuperar metadados do produto {#step-2-retrieve-product-metadata}

Depois de armazenar um identificador de recomendação em cada perfil de usuário, você precisa recuperar os metadados completos do produto (nome, preço, imagem e assim por diante) para incluir na sua mensagem. Você tem duas opções:

- **Opção A:** [Catálogos da Braze](#option-a-braze-catalogs) — armazene informações de produtos diretamente na Braze para consultas rápidas e integradas.
- **Opção B:** [Connected Content](#option-b-connected-content) — busque informações de produtos de uma API externa no momento do envio.

### Opção A: Catálogos da Braze {#option-a-braze-catalogs}

Se você criou um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create) com seu inventário de produtos, pode consultar itens diretamente na sua mensagem usando Liquid. Para um passo a passo completo, consulte [Usando catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use).

#### Recomendar um item específico do catálogo {#recommend-a-specific-catalog-item}

{% raw %}
Para referenciar um produto específico por ID, use a Liquid tag `catalog_items`. Por exemplo, para recomendar o produto `1001` de um catálogo chamado `retail_products`:

```liquid
{% catalog_items retail_products 1001 %}

We have a new item we think you'll like:
Category: {{ items[0].category }}
Name: {{ items[0].name }}
Price: ${{ items[0].price }}
```
{% endraw %}

#### Recomendar múltiplos itens do catálogo {#recommend-multiple-catalog-items}

{% raw %}
Você também pode referenciar múltiplos itens em uma única tag. Por exemplo, para destacar três produtos:

```liquid
{% catalog_items retail_products 1001 1003 1005 %}

New items added in:
- {{ items[0].category }}
- {{ items[1].category }}
- {{ items[2].category }}

Visit our store to learn more!
```
{% endraw %}

#### Criar modelos de itens usando a recomendação de um usuário {#template-items-using-a-users-recommendation}

{% raw %}
Combine o atributo personalizado da [Etapa 1](#step-1-store-recommendations-on-user-profiles) com uma consulta de catálogo para personalizar a recomendação para cada usuário:

```liquid
{% catalog_items retail_products {{custom_attribute.${recommended_product_id}}} %}

Hi {{${first_name}}}, check out our pick for you:
{{ items[0].name }} — ${{ items[0].price }}
```
{% endraw %}

### Opção B: Connected Content {#option-b-connected-content}

Se os metadados do seu produto estão em um serviço externo em vez de um catálogo da Braze, use o [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) para buscá-los no momento do envio.

{% raw %}
Por exemplo, se sua API interna retorna detalhes do produto por ID:

```liquid
{% connected_content https://api.yourcompany.com/products/{{custom_attribute.${recommended_product_id}}} :save product %}

Hi {{${first_name}}}, we think you'll love:
{{ product.name }} — ${{ product.price }}
```
{% endraw %}

Para mais detalhes sobre como fazer chamadas de API a partir das suas mensagens, consulte [Fazendo uma chamada de API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

{% alert warning %}
Evite usar Connected Content para buscar uma lista grande de produtos e depois iterar por essa lista em Liquid no momento do envio. Cargas úteis de resposta grandes aumentam a latência de envio e podem causar timeouts de mensagem ou falhas na entrega em escala. Em vez disso, armazene apenas os IDs de produtos específicos que um usuário precisa no perfil dele (consulte a [Etapa 1](#step-1-store-recommendations-on-user-profiles)) e busque os metadados desses itens individuais ou use [catálogos](#option-a-braze-catalogs), que são otimizados para consultas rápidas.
{% endalert %}

## Etapa 3: Verifique sua integração {#step-3-verify-your-integration}

Após concluir a configuração, verifique sua integração:

1. Use o endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para gravar uma recomendação de teste no seu próprio perfil de usuário.
2. Envie uma mensagem de teste que faça referência ao produto recomendado usando Catalogs ou Connected Content.
3. Confirme se os detalhes do produto são renderizados corretamente na mensagem entregue.
4. No dashboard da Braze, acesse a página de resultados da Campaign ou do Canvas e confirme se o envio foi registrado.

## Considerações {#considerations}

- Mantenha os dados de recomendação precisos atualizando os atributos personalizados regularmente à medida que seu mecanismo de recomendação produz novos resultados.
- Use os [recursos de personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) da Braze para personalizar ainda mais as mensagens, como incorporar dados específicos do usuário junto com os detalhes do produto.
- Considere usar a [entrega disparada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) para disparar mensagens a partir do seu backend usando modelos definidos no dashboard da Braze.