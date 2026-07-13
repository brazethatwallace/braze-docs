---
nav_title: "POST : Annuler les exportations par segment"
article_title: "POST : Annuler les exportations par segment"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Annuler les exportations par segment."

---
{% api %}
# Annuler les exportations par segment {#cancel-exports-by-segment}
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> Utilisez cet endpoint pour annuler toutes les exportations en cours associées à un ID de segment spécifié.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `segments.list`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Requis | Chaîne de caractères | Le `segment_id` dont vous souhaitez annuler les exportations en cours. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}