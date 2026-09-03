---
nav_title: "PUT: Substituir vários itens do catálogo"
article_title: "PUT: Substituir vários itens do catálogo"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para substituir vários itens do catálogo."

---
{% api %}
# Substituir itens do catálogo {#replace-catalog-items}
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use este endpoint para substituir vários itens no seu catálogo.

Se um item de catálogo não existir, esse endpoint criará o item no seu catálogo. Cada solicitação pode suportar até 50 itens de catálogo. Esse endpoint é assíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `catalogs.replace_items`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Parâmetros de jornada {#path-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatório | String | Nome do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de jornada" }

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Vetor | Um vetor que contém objetos de item. Cada objeto deve ter um ID. Os objetos de item devem conter campos existentes no catálogo. Até 50 objetos de item são permitidos por solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

{% alert note %}
O campo `Location` usa o tipo de dados `geo`, que espera um vetor formatado como `[longitude, latitude]`.
{% endalert %}

## Resposta {#response}

Há três respostas de código de status para esse endpoint: `202`, `400` e `404`.

{% alert note %}
O sistema também pode retornar uma resposta `400` se a sua empresa tiver atingido o limite de armazenamento do catálogo. A versão gratuita dos catálogos tem um limite de 500&nbsp;MB. Para saber mais sobre os níveis de armazenamento e como fazer upgrade, consulte [Limitações de armazenamento de dados]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations).
{% endalert %}

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `202` poderia retornar o seguinte corpo de resposta.

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Solução de problemas {#troubleshooting}

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `company-size-limit-already-reached` | O limite de armazenamento do catálogo foi atingido. Para saber mais sobre os níveis de armazenamento, consulte [Limitações de armazenamento de dados]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `company-size-limit-surge` | A solicitação excede o armazenamento restante de catálogo da sua empresa. Tente novamente com uma atualização menor. Para saber mais sobre os níveis de armazenamento, consulte [Limitações de armazenamento de dados]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `ids-not-string` | Confirme que cada ID de item é uma string. |
| `ids-not-unique` | Verifique se cada ID de item é exclusivo. |
| `ids-too-large` | O limite de caracteres para cada ID de item é de 250 caracteres. |
| `item-array-invalid` | `items` deve ser um vetor de objetos. |
| `items-missing-ids` | Alguns itens não têm IDs de item. Confirme que cada item tem um ID. |
| `items-too-large` | Os valores dos itens não podem exceder 5.000 caracteres. |
| `invalid-ids` | Os caracteres compatíveis com os nomes de ID de item são letras, números, hífens e sublinhados. |
| `invalid-fields` | Confirme que todos os campos que está enviando na solicitação de API já existem no catálogo. Isso não está relacionado ao campo ID mencionado no erro. |
| `invalid-keys-in-value-object` | As chaves de objeto do item não podem incluir `.` ou `$`. |
| `too-deep-nesting-in-value-object` | Os objetos de item não podem ter mais de 50 níveis de aninhamento. |
| `request-includes-too-many-items` | Sua solicitação tem muitos itens. O limite de itens por solicitação é de 50. |
| `unable-to-coerce-value` | Os tipos de itens não podem ser convertidos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

{% endapi %}