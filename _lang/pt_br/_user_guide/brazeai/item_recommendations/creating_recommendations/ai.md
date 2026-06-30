---
nav_title: Recomendações da IA
article_title: Criar recomendações de itens de IA
description: "Este artigo de referência aborda como criar uma recomendação de item de IA para itens em um catálogo."
page_order: 1
---

# Criar recomendações de itens de IA {#create-ai-item-recommendations}

> Aprenda como criar um mecanismo de recomendação de IA a partir dos itens do seu catálogo.

## Sobre recomendações de itens de IA {#about-ai-item-recommendations}

Use recomendações de itens de IA para calcular os produtos mais populares ou criar recomendações personalizadas de IA para um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) específico. Depois de criar sua recomendação, você pode usar a personalização para inserir esses produtos em suas mensagens.

{% alert tip %}
[As recomendações de IA Personalizado](#recommendation-types) funcionam melhor com pelo menos algumas centenas de itens no catálogo, no máximo 100.000 itens e, normalmente, com pelo menos 30.000 usuários com dados de compra ou interação. Esse é apenas um guia aproximado e pode variar. Os outros tipos de recomendação podem trabalhar com menos dados, inclusive quando **Mais Popular** é usado como fallback.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Criação de uma recomendação de item de IA {#creating-an-ai-item-recommendation}

### Pré-requisitos {#prerequisites}

Antes de começar, você precisará ter o seguinte:

- Pelo menos um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) para usar qualquer um dos tipos de recomendação descritos abaixo.
- Dados de compra ou de evento na Braze (eventos personalizados, o evento de pedido realizado ou o objeto de compra) que incluam uma referência ao item e correspondam aos IDs dos itens do catálogo.

### Etapa 1: Criar uma nova recomendação {#step-1-create-a-new-recommendation}

Você pode criar uma recomendação de itens de IA a partir de qualquer lugar no dashboard:

{% tabs local %}
{% tab No menu de navegação %}
1. Acesse **Analytics** > **AI Item Recommendation**.
2. Selecione **Create Prediction** > **AI Item Recommendation**.
{% endtab %}

{% tab A partir de um catálogo %}
Você também pode optar por criar uma recomendação diretamente de um catálogo individual. Selecione seu catálogo na página **Catalogs** e, em seguida, selecione **Create Recommendation**.
{% endtab %}
{% endtabs %}

### Etapa 2: Adicionar detalhes da recomendação {#step-2-add-recommendation-details}

Dê um nome e uma descrição opcional à sua recomendação.

![Etapa "Detalhes da recomendação" com os campos de nome e descrição.]({% image_buster /assets/img/item_recs_1.png %})

### Etapa 3: Defina sua recomendação {#recommendation-type}

Selecione um tipo de recomendação. Cada tipo usa os últimos seis meses de dados de interação com itens, como dados de compra, pedido realizado ou evento personalizado. Para informações mais detalhadas e casos de uso para cada um, veja [Tipos e casos de uso]({{site.baseurl}}/user_guide/brazeai/item_recommendations).

{% alert tip %}
Ao usar **Mais Recente** ou **IA Personalizado**, os usuários com dados insuficientes para criar recomendações individualizadas receberão itens **Mais Popular** como fallback. Você pode ver uma aproximação da proporção de usuários que recebem o fallback **Mais Popular** exibida na página **Analytics**. O fallback **Mais Popular** retorna apenas itens que existem no catálogo vinculado.
{% endalert %}

#### Etapa 3.1: Excluir compras ou interações anteriores (opcional) {#step-31-exclude-prior-purchases-or-interactions-optional}

Para evitar sugerir itens que um usuário já tenha comprado ou com os quais já tenha interagido, selecione **Do not recommend items users have previously interacted with**. Essa opção só está disponível quando o **Type** de recomendação está definido como **AI Personalized**.

![Etapa "Defina sua recomendação" com "AI Personalized" como o tipo e a opção "Do not recommend items users have previously interacted with" selecionada.]({% image_buster /assets/img/item_recs_2-3.png %})

Essa configuração impede que as mensagens reutilizem os itens que um usuário já comprou ou com os quais interagiu, desde que a recomendação tenha sido atualizada recentemente. Os itens comprados ou com os quais houve interação entre as atualizações de recomendação ainda podem aparecer. Na versão gratuita das recomendações de itens, as atualizações ocorrem semanalmente. Na versão pro das recomendações de itens de IA, as atualizações ocorrem a cada 24 horas.

Por exemplo, ao usar a versão pro das recomendações de itens de IA, se um usuário comprar algo e receber um e-mail de marketing em 30 minutos, o item que acabou de comprar poderá não ser excluído do e-mail a tempo. No entanto, as mensagens enviadas após 24 horas não incluirão esse item.

#### Etapa 3.2: Selecione um catálogo {#step-32-select-a-catalog}

Se ainda não estiver preenchido, selecione o [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) do qual esta recomendação irá buscar itens.

#### Etapa 3.3: Adicionar uma seleção (opcional) {#step-33-add-a-selection-optional}

Se quiser ter mais controle sobre sua recomendação, escolha uma [seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) para aplicar filtros personalizados. As seleções filtram as recomendações por colunas específicas em seu catálogo, como marca, tamanho ou local. As seleções que contêm Liquid não podem ser usadas em sua recomendação.

![Um exemplo da seleção "in-stock" selecionada para a recomendação.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Caso não encontre sua seleção, lembre-se de que é preciso criá-la primeiro no catálogo.
{% endalert %}

### Etapa 4: Selecione a interação para conduzir as recomendações {#step-4-select-the-interaction-to-drive-recommendations}

Selecione o evento para o qual você deseja que essa recomendação seja otimizada. Esse evento geralmente é uma compra, mas também pode ser qualquer interação com um item.

Você pode otimizar para:

- Eventos de compra com o [objeto Purchase]({{site.baseurl}}/api/objects_filters/purchase_object)
- Eventos personalizados que representam uma compra
- Eventos personalizados que representam qualquer outra interação com itens (como visualizações de produtos, cliques ou reproduções de mídia)
- Pedidos realizados com o [evento de pedido realizado]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)

Se você escolher **Custom Event**, selecione seu evento na lista.

![O evento personalizado "purchase" selecionado como a forma como os eventos estão sendo rastreados atualmente.]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
Eventos personalizados devem ter dados suficientes antes de aparecerem na lista de eventos. Se seu evento personalizado não aparecer, pode ser porque o backend da Braze ainda não o processou ou ele não possui dados suficientes para o treinamento do modelo. Recomendações de IA dependem de dados históricos para gerar insights, portanto, eventos recém-criados ou raramente acionados não estarão disponíveis até que mais dados sejam coletados.
{% endalert %}

### Etapa 5: Selecione o nome da propriedade correspondente {#property-name}

Para criar uma recomendação, você precisa informar à Braze qual campo do seu evento de interação (evento de pedido realizado, objeto de compra ou evento personalizado) tem o identificador exclusivo que corresponde ao campo `id` de um item no catálogo. Não tem certeza? [Veja os requisitos](#requirements).

Selecione esse campo para o **Property Name**.

O campo **Property Name** será preenchido previamente com uma lista de campos enviados pelo SDK à Braze. Se forem fornecidos dados suficientes, essas propriedades também serão classificadas em ordem de probabilidade de serem a propriedade correta. Selecione a opção que corresponde ao campo `id` do catálogo.

![O nome da propriedade "purchase_item" selecionado que corresponde aos IDs dos itens no catálogo.]({% image_buster /assets/img/item_recs_4.png %})

#### Requisitos {#requirements}

Há alguns requisitos para selecionar sua propriedade:

- Deve ser mapeada para o campo `id` do seu catálogo selecionado.
- **Se você selecionou o evento de pedido realizado ou está usando [eventos de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) para treinar recomendações de itens:** Insira `products.product_id` para o ID do produto.
  - O campo pode estar dentro de um array de produtos ou terminar com um array de IDs. Em ambos os casos, cada ID de produto será tratado como um evento separado e sequencial com o mesmo registro de data e hora.
- **Se você selecionou o objeto Purchase:** Deve ser o `product_id` ou um campo do `properties` do evento de interação.
- **Se você selecionou Evento personalizado:** Deve ser um campo do `properties` do seu evento personalizado.
- Os campos aninhados devem ser digitados no menu suspenso **Property Name** em notação de ponto com o formato `event_property.nested_property`. Por exemplo, se estiver selecionando a propriedade aninhada `district_name` dentro da propriedade de evento `location`, você digitará `location.district_name`.

#### Exemplos de mapeamentos {#example-mappings}

Os exemplos de mapeamentos a seguir referem-se a este catálogo de amostra:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table aria-label="Exemplos de mapeamentos" class="tg">
  <caption>Exemplos de mapeamentos</caption>
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Black Size 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Red Size 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas White Size 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Purple Size 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Evento personalizado %}

Digamos que você queira usar o evento personalizado `added_to_cart` para poder recomendar produtos semelhantes antes que o cliente faça o checkout. O evento `added_to_cart` tem uma propriedade de evento chamada `product_sku`.

Então, a propriedade `product_sku` deve incluir pelo menos um dos valores da coluna `id` no catálogo de amostra: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" ou "ADI-PP-10". Você não precisa de eventos para cada item do catálogo, mas precisa de alguns deles para que o mecanismo de recomendação tenha conteúdo suficiente para trabalhar.

##### Exemplo de objeto de evento personalizado {#example-custom-event-object}

Esse evento tem `"product_sku": "ADI-BL-7"`, que corresponde ao primeiro item do catálogo de amostra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Exemplo de objeto de evento personalizado com um array de produtos {#example-custom-event-object-with-an-array-of-products}

Se as propriedades do evento contiverem vários produtos em um array, cada ID de produto será tratado como um evento separado e sequencial. Esse evento pode usar a propriedade `products.sku` para corresponder ao primeiro e ao terceiro itens do catálogo de amostra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Exemplo de objeto de evento personalizado com um objeto aninhado contendo um array de IDs de produto {#example-custom-event-object-with-a-nested-object-containing-a-product-id-array}

Se os IDs dos seus produtos forem valores em um array em vez de objetos, você poderá usar a mesma notação e cada ID de produto será tratado como um evento separado e sequencial. Isso pode ser combinado de forma flexível com objetos aninhados no evento a seguir, configurando a propriedade como `purchase.product_skus` para corresponder ao primeiro e ao terceiro itens no catálogo de amostra.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Objeto de compra %}

Um objeto de compra é passado pela API quando uma compra é feita.

Em termos de mapeamento, aplica-se uma lógica semelhante aos objetos de compra e aos eventos personalizados, exceto que você pode escolher entre usar o `product_id` do objeto de compra ou um campo no objeto `properties`.

Lembre-se de que você não precisa de eventos para cada item do catálogo, mas precisa de alguns deles para que o mecanismo de recomendação tenha conteúdo suficiente para trabalhar.

##### Exemplo de objeto de compra mapeado para o ID do produto {#example-purchase-object-mapped-to-product-id}

Esse evento tem `"product_id": "ADI-BL-7"`, que mapeia para o primeiro item do catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Exemplo de objeto de compra mapeado para um campo de propriedades {#example-purchase-object-mapped-to-a-properties-field}

Esse evento tem uma propriedade `"sku": "ADI-RD-8"`, que mapeia para o segundo item do catálogo.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% tab Evento de pedido realizado %}

##### Exemplo de objeto de pedido realizado mapeado para o ID do produto {#example-order-placed-object-mapped-to-product-id}

```json
{
  "name": "ecommerce.order_placed",
  "properties": {
    "order_id": "order_123",
    "total_value": 200.0,
    "currency": "USD",
    "products": [
      {
        "product_id": "ADI-BL-7",
        "product_name": "Adidas Black Size 7",
        "variant_id": "ADI-BL-7-default",
        "quantity": 1,
        "price": 100.0
      }
    ],
    "source": "storefront"
  }
}
```

{% endtab %}
{% endtabs %}

### Etapa 6: Treinar a recomendação {#step-6-train-the-recommendation}

Quando estiver pronto, selecione **Create Recommendation**. Esse processo pode levar de 10 minutos a 36 horas para ser concluído. Você receberá uma atualização por e-mail quando a recomendação for treinada com sucesso ou uma explicação do motivo pelo qual a criação pode ter falhado.

Você pode encontrar a recomendação na página **Predictions**, onde poderá editá-la ou arquivá-la conforme necessário. As recomendações serão retreinadas automaticamente uma vez por semana (pago) ou uma vez por mês (gratuito).