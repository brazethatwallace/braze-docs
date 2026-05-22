---
nav_title: Erweiterte Filter
article_title: Erweiterte Liquid-Filter
page_order: 4
description: "Dieser Referenzartikel listet erweiterte Filter, Beispiele und deren Verwendung in Ihrer Campaign auf."

---

# Erweiterte Filter {#advanced-filters}

> Dieser Referenzartikel bietet eine Übersicht über erweiterte Filter in Liquid und wie sie verwendet werden können.

## Codierungsfilter {#encoding-filters}

{% raw %}
| Filtername | Filterbeschreibung | Beispieleingabe | Beispielausgabe |
|---|---|---|---|
| `md5` | Gibt einen MD5-codierten String zurück | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
| `sha1` | Gibt einen SHA1-codierten String zurück | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
| `sha2` | Gibt einen SHA2-codierten (256-Bit, auch bekannt als SHA-256) String zurück | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
| `base64` | Gibt einen Base64-codierten String zurück | `{{'blah' | base64_encode}}` | YmxhaA== |
| `hmac_sha1_hex` (zuvor `hmac_sha1`) | Gibt eine HMAC-SHA1-Signatur zurück, codiert als Hex-String | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
| `hmac_sha1_base64` | Gibt eine HMAC-SHA1-Signatur zurück, codiert als Base64-String | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
| `hmac_sha256_hex` | Gibt eine HMAC-SHA256-Signatur zurück, codiert als Hex-String | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
| `hmac_sha256_base64` | Gibt eine HMAC-SHA256-Signatur zurück, codiert als Base64-String | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Encoding filters" }

## URL-Filter {#url-filters}

| Filtername | Filterbeschreibung | Beispieleingabe | Beispielausgabe |
|---|---|---|---|
| `url_escape` | Identifiziert alle Zeichen in einem String, die in URLs nicht zulässig sind, und ersetzt sie durch ihre escapten Varianten | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | Ersetzt alle Zeichen in einem String, die in URLs nicht zulässig sind, durch ihre escapten Varianten, einschließlich des kaufmännischen Und-Zeichens (&) | `{{'hey<&>hi' | url_param_escape}}` | hey%3C%26%3Ehi |
| `url_encode` | Codiert einen String in ein URL-freundliches Format | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="URL filters" }

{% endraw %}
{% alert tip %}
Das `assign`-Tag kann mit HTML kombiniert werden, um Ihnen Zeit und Aufwand beim Erstellen mehrerer Hyperlinks zu sparen.
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## Eigenschaftszugriffs-Filter {#property-accessor-filter}

| Filtername | Filterbeschreibung |
| --- | --- |
| `property_accessor` | Nimmt einen Hash und einen Hash-Schlüssel entgegen und gibt den Wert in diesem Hash an diesem Schlüssel zurück |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Property accessor filter" }

**Beispiel-Hash:** `{"a" => 42, "b" => 0}`
**Beispieleingabe:** `{{hash | property_accessor: 'a'}}`
**Beispielausgabe:** `42`

Darüber hinaus ermöglicht Ihnen der Eigenschaftszugriffs-Filter, ein angepasstes Attribut als Hash-Schlüssel zu verwenden, um auf einen bestimmten Hash-Wert zuzugreifen.

{% endraw %}

{% alert note %}
Es gibt keine Möglichkeit, einen Hash als Variable (z. B. als Ausdruck) in Liquid innerhalb von Braze zu instanziieren.
{% endalert %}

{% raw %}

## Zahlenformatierungs-Filter {#number-formatting-filters}

| Filtername | Filterbeschreibung | Beispieleingabe | Beispielausgabe |
|---|---|---|---|
| `number_with_delimiter` | Formatiert eine Zahl mit Kommas | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Number formatting filters" }

## JSON-Escape- oder String-Escape-Filter {#json-escape-or-string-escape-filter}

| Filtername | Filterbeschreibung |
|---|---|
| `json_escape` | Escapet alle Sonderzeichen in einem String (wie doppelte Anführungszeichen `""` und Backslash '\'). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON escape or string escape filter" }

Dieser Filter sollte immer verwendet werden, wenn ein String in einem JSON-Wörterbuch personalisiert wird, und ist besonders nützlich für Webhooks.

## JSON-Formatierungs-Filter {#json-formatting-filters}

| Filtername | Filterbeschreibung |
|---|---|
| `json_parse` | Konvertiert einen JSON-String in eine entsprechende Datenstruktur, wie ein Objekt oder Array. |
| `as_json_string` | Konvertiert eine Datenstruktur, wie ein Objekt oder Array, in einen entsprechenden JSON-String. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JSON-formatting filters" }

{% endraw %}

{% details json_parse – Beispieleingabe und -ausgabe %}

### Eingabe {#input}

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### Ausgabe {#output}

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details as_json_string – Beispieleingabe und -ausgabe %}

### Eingabe

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### Ausgabe

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values