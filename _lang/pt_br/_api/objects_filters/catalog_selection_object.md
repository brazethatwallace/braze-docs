---
nav_title: "Objeto de seleção de catálogo"
article_title: Objeto de seleção de catálogo da API
page_order: 12
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de seleção de catálogo."
tool: Catalogs

---

# Objeto de seleção de catálogo {#catalog-selection-object}

> Ao criar uma seleção de catálogo, você pode fornecer um objeto de seleção para definir os critérios de filtragem, ordenação e limitação para os itens retornados do seu catálogo.

O objeto `selection` permite que você especifique quais itens do seu catálogo devem ser incluídos na seleção com base em filtros, como eles devem ser ordenados e quantos resultados retornar. Use este objeto ao criar seleções de catálogo pela API.

## Corpo do objeto {#object-body}

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Detalhes do objeto {#object-details}

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | -------- | --------- | ----------- |
| `name` | Obrigatória | String | O nome da seleção de catálogo. |
| `description` | Opcional | String | Uma descrição da seleção de catálogo. |
| `external_id` | Opcional | String | Um identificador exclusivo para a seleção. |
| `source` | Opcional | String | A origem dos dados do catálogo. Para catálogos Shopify, defina como `"Shopify"`. Os valores aceitos são `"Shopify"` e `"Braze"`. |
| `filters` | Obrigatória | Array de objetos | Um array de objetos de filtro a serem aplicados aos itens do catálogo. Você pode especificar até dez filtros por solicitação. Se um array vazio de filtros for fornecido, todos os itens do catálogo serão incluídos. |
| `results_limit` | Obrigatória | Inteiro | O número máximo de resultados a serem retornados. Deve ser um número entre 1 e 50. |
| `sort_field` | Opcional | String | O campo pelo qual classificar os resultados. Deve ser combinado com `sort_order`. Se `sort_field` e `sort_order` não estiverem presentes, os resultados serão retornados em ordem aleatória. |
| `sort_order` | Opcional | String | A ordem de classificação dos resultados. Os valores aceitos são `"asc"` (crescente) ou `"desc"` (decrescente). Deve ser combinado com `sort_field`. Se `sort_field` e `sort_order` não estiverem presentes, os resultados serão retornados em ordem aleatória. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalhes do objeto" }

### Objeto de filtro {#filter-object}

Cada objeto de filtro no array `filters` contém os campos descritos na tabela a seguir.

| Chave | Obrigatória | Tipo de dados                                   | Descrição |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Obrigatória | String                                      | O campo do catálogo pelo qual filtrar. |
| `operator` | Obrigatória | String                                      | O operador de comparação a ser usado para filtragem. Exemplos incluem `"includes value"` e `"does not include value"`. |
| `value`    | Obrigatória | Varia (string, número, booleano, hora)     | O valor a ser comparado. Deve corresponder ao tipo de dados do campo subjacente do catálogo (por exemplo, string, número, booleano, hora). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objeto de filtro" }

{% alert note %}
A API suporta no máximo dez filtros por solicitação de seleção. Os filtros são aplicados na ordem em que aparecem no array.
{% endalert %}