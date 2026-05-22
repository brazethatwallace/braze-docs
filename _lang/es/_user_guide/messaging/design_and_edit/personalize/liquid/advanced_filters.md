---
nav_title: Filtros avanzados
article_title: Filtros avanzados de Liquid
page_order: 4
description: "Este artículo de referencia enumera los filtros avanzados, ejemplos y cómo pueden usarse en tu campaña."

---

# Filtros avanzados {#advanced-filters}

> Este artículo de referencia ofrece un resumen de los filtros avanzados en Liquid y cómo pueden usarse.

## Filtros de codificación {#encoding-filters}

{% raw %}
| Nombre del filtro | Descripción del filtro | Ejemplo de entrada | Ejemplo de salida |
|---|---|---|---|
| `md5` | Devuelve una cadena codificada en md5 | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
| `sha1` | Devuelve una cadena codificada en sha1 | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
| `sha2` | Devuelve una cadena codificada en sha2 (256 bits, también conocido como SHA-256) | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
| `base64` | Devuelve una cadena codificada en base64 | `{{'blah' | base64_encode}}` | YmxhaA== |
| `hmac_sha1_hex` (anteriormente `hmac_sha1`) | Devuelve una firma hmac-sha1, codificada como cadena hexadecimal | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
| `hmac_sha1_base64` | Devuelve una firma hmac-sha1, codificada como cadena base64 | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
| `hmac_sha256_hex` | Devuelve una firma hmac-sha256, codificada como cadena hexadecimal | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
| `hmac_sha256_base64` | Devuelve una firma hmac-sha256, codificada como cadena base64 | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Encoding filters" }

## Filtros de URL {#url-filters}

| Nombre del filtro | Descripción del filtro | Ejemplo de entrada | Ejemplo de salida |
|---|---|---|---|
| `url_escape` | Identifica todos los caracteres de una cadena que no están permitidos en URLs y los reemplaza con sus variantes escapadas | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | Reemplaza todos los caracteres de una cadena que no están permitidos en URLs con sus variantes escapadas, incluido el ampersand (&) | `{{'hey<&>hi' | url_param_escape}}` | hey%3C%26%3Ehi |
| `url_encode` | Codifica una cadena de forma compatible con URLs | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="URL filters" }

{% endraw %}
{% alert tip %}
La etiqueta `assign` puede combinarse con HTML para ahorrarte tiempo y esfuerzo al crear múltiples hipervínculos.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Filtro de acceso a propiedades {#property-accessor-filter}

| Nombre del filtro | Descripción del filtro |
| --- | --- |
| `property_accessor` | Toma un hash y una clave de hash y devuelve el valor en ese hash para esa clave |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Property accessor filter" }

**Hash de ejemplo:** `{"a" => 42, "b" => 0}`
**Entrada de ejemplo:** `{{hash | property_accessor: 'a'}}`
**Salida de ejemplo:** `42`

Además, el filtro de acceso a propiedades te permite usar un atributo personalizado como plantilla de clave de hash para acceder a un valor de hash particular.

{% endraw %}

{% alert note %}
No hay forma de instanciar un hash como variable (como una expresión) en Liquid dentro de Braze.
{% endalert %}

{% raw %}

## Filtros de formato numérico {#number-formatting-filters}

| Nombre del filtro | Descripción del filtro | Ejemplo de entrada | Ejemplo de salida |
|---|---|---|---|
| `number_with_delimiter` | Da formato a un número con comas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number formatting filters" }

## Filtro de escape JSON o escape de cadena {#json-escape-or-string-escape-filter}

| Nombre del filtro | Descripción del filtro |
|---|---|
| `json_escape` | Escapa cualquier carácter especial en una cadena (como las comillas dobles `""` y la barra invertida '\'). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON escape or string escape filter" }

Este filtro siempre debe usarse al personalizar una cadena en un diccionario JSON y es especialmente útil para webhooks.

## Filtros de formato JSON {#json-formatting-filters}

| Nombre del filtro | Descripción del filtro |
|---|---|
| `json_parse` | Convierte una cadena JSON en una estructura de datos correspondiente, como un objeto o un array. |
| `as_json_string` | Convierte una estructura de datos, como un objeto o un array, en una cadena JSON correspondiente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON-formatting filters" }

{% endraw %}

{% details Ejemplo de entrada y salida de json_parse %}

### Entrada {#input}

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### Salida {#output}

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details Ejemplo de entrada y salida de as_json_string %}

### Entrada

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### Salida

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values