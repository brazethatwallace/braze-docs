---
nav_title: Filtros avançados
article_title: Filtros avançados de Liquid
page_order: 4
description: "Este artigo de referência lista filtros avançados, exemplos e como eles podem ser usados na sua campanha."

---

# Filtros avançados {#advanced-filters}

> Este artigo de referência fornece uma visão geral dos filtros avançados em Liquid e como eles podem ser usados.

## Filtros de codificação {#encoding-filters}

{% raw %}
| Nome do filtro | Descrição do filtro | Exemplo de entrada | Exemplo de saída |
|---|---|---|---|
| `md5` | Retorna uma string codificada em md5 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
| `sha1` | Retorna uma string codificada em sha1 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
| `sha2` | Retorna uma string codificada em sha2 (256 bits, também conhecido como SHA-256) | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
| `base64` | Retorna uma string codificada em base64 | `{{'blah' | base64_encode}}` | YmxhaA== |
| `hmac_sha1_hex` (anteriormente `hmac_sha1`) | Retorna a assinatura hmac-sha1, codificada como uma string hexadecimal | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
| `hmac_sha1_base64` | Retorna a assinatura hmac-sha1, codificada como uma string base64 | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
| `hmac_sha256_hex` | Retorna a assinatura hmac-sha256, codificada como uma string hexadecimal | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
| `hmac_sha256_base64` | Retorna a assinatura hmac-sha256, codificada como uma string base64 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Encoding filters" }

## Filtros de URL {#url-filters}

| Nome do filtro | Descrição do filtro | Exemplo de entrada | Exemplo de saída |
|---|---|---|---|
| `url_escape` | Identifica todos os caracteres em uma string que não são permitidos em URLs e os substitui por suas variantes escapadas | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | Substitui todos os caracteres em uma string que não são permitidos em URLs por suas variantes escapadas, incluindo o e comercial (&) | `{{'hey<&>hi' | url_param_escape}}` | hey%3C%26%3Ehi |
| `url_encode` | Codifica uma string de forma compatível com URLs | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="URL filters" }

{% endraw %}
{% alert tip %}
A tag `assign` pode ser combinada com HTML para economizar tempo e esforço ao criar múltiplos hyperlinks.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filtro de acesso a propriedades {#property-accessor-filter}

| Nome do filtro | Descrição do filtro |
| --- | --- |
| `property_accessor` | Recebe um hash e uma chave de hash e retorna o valor correspondente àquela chave no hash |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Property accessor filter" }

**Exemplo de hash:** `{"a" => 42, "b" => 0}`
**Exemplo de entrada:** `{{hash | property_accessor: 'a'}}`
**Exemplo de saída:** `42`

Além disso, o filtro de acesso a propriedades permite usar um atributo personalizado como modelo em uma chave de hash para acessar um valor específico do hash.

{% endraw %}

{% alert note %}
Não é possível instanciar um hash como uma variável (como uma expressão) em Liquid na Braze.
{% endalert %}

{% raw %}

## Filtros de formatação de números {#number-formatting-filters}

| Nome do filtro | Descrição do filtro | Exemplo de entrada | Exemplo de saída |
|---|---|---|---|
| `number_with_delimiter` | Formata um número com vírgulas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number formatting filters" }

## Filtro de escape JSON ou escape de string {#json-escape-or-string-escape-filter}

| Nome do filtro | Descrição do filtro |
|---|---|
| `json_escape` | Escapa quaisquer caracteres especiais em uma string (como aspas duplas `""` e barra invertida '\'). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON escape or string escape filter" }

Esse filtro deve ser sempre usado ao personalizar uma string em um dicionário JSON e é especialmente útil para webhooks.

## Filtros de formatação JSON {#json-formatting-filters}

| Nome do filtro | Descrição do filtro |
|---|---|
| `json_parse` | Converte uma string JSON em uma estrutura de dados correspondente, como um objeto ou array. |
| `as_json_string` | Converte uma estrutura de dados, como um objeto ou array, em uma string JSON correspondente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON-formatting filters" }

{% endraw %}

{% details Exemplo de entrada e saída de json_parse %}

### Entrada {#input}

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### Saída {#output}

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details Exemplo de entrada e saída de as_json_string %}

### Entrada

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### Saída

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values