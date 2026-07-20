---
nav_title: "GET : Exporter les informations relatives au segment"
article_title: "GET : Exporter les informations relatives au segment"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter les informations relatives au segment."

---
{% api %}
# Exporter les informations relatives au segment {#export-segment-details}
{% apimethod get %}
/segments/details
{% endapimethod %}

> Utilisez cet endpoint pour récupérer des informations pertinentes sur un segment, qui peut être identifié par le `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `segments.details`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre    | Obligatoire | Type de données | Description            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Obligatoire | Chaîne de caractères | Voir [Identifiant API de segment]({{site.baseurl}}/api/identifier_types).<br><br> Le `segment_id` d'un segment donné se trouve sur la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) de votre compte Braze, ou vous pouvez utiliser l'[endpoint Exporter la liste des segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse {#response}

```json
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description,
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}