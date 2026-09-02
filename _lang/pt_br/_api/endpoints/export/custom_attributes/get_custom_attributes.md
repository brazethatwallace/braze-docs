---
nav_title: "GET: Exportar atributos personalizados"
article_title: "GET: Exportar atributos personalizados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Exportar atributos personalizados\"."

---
{% API or interface de programação do aplicativo (API) %}
# Exportar atributos personalizados {#export-custom-attributes}
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> Use esse endpoint para exportar uma lista de atributos personalizados registrados para o seu app. Os atributos são retornados em grupos de 50, classificados em ordem alfabética.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_attributes.get`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## Parâmetros de consulta {#query-parameters}

Note que cada chamada a esse endpoint retornará 50 atributos. Para mais de 50 atributos, use o cabeçalho `Link` para recuperar os dados na próxima página, conforme mostrado no exemplo de resposta a seguir.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `cursor` | Opcional | String | Determina a paginação dos atributos personalizados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta" }

## Exemplos de solicitações {#example-requests}

### Sem cursor {#without-cursor}

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Com cursor {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
        },
        ...
    ]
}
```

### Códigos de resposta a erros fatais {#fatal-export}

Para obter os códigos de status e as mensagens de erro associadas que serão retornadas se sua solicitação encontrar um erro fatal, consulte [Erros fatais]({{site.baseurl}}/api/errors#fatal-errors).

{% alert tip %}
Para obter ajuda com exportações de CSV e API or interface de programação do aplicativo (API), acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}