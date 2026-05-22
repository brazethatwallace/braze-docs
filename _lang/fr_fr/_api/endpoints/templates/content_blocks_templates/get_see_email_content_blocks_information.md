---
nav_title: "GET : Voir les informations sur les Content Blocks"
article_title: "GET : Voir les informations sur les Content Blocks"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Voir les informations sur les Content Blocks."
---

{% api %}
# Voir les informations sur les Content Blocks {#see-content-block-information}
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Utilisez cet endpoint pour appeler les informations relatives à vos [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/) existants.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Conditions préalables {#prerequisites}
Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l'autorisation `content_blocks.info`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `content_block_id`  | Requis | Chaîne de caractères | L'identifiant du Content Block. <br><br>Vous pouvez le trouver soit en listant les informations du Content Block par le biais d'un appel API, soit en vous rendant sur la page des [clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/), puis en défilant vers le bas et en recherchant l'identifiant API de votre Content Block.|
| `include_inclusion_data`  | Facultatif | Valeur booléenne | Lorsque ce paramètre est défini sur `true`, l'API renvoie l'identifiant API de la variation de message des Campaigns et des Canvas dans lesquels ce Content Block est inclus, afin qu'il puisse être utilisé dans les appels ultérieurs.  Les résultats excluent les Campaigns ou les Canvas archivés ou supprimés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse {#response}

```json
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Content Block ID cannot be blank` | Assurez-vous qu'un Content Block est répertorié dans votre requête et compris entre des guillemets (`""`). |
| `Content Block ID is invalid for this workspace` | Ce Content Block n'existe pas ou se trouve dans un compte de société ou un espace de travail différent. |
| `Content Block has been deleted—content not available` | Ce Content Block, bien qu'il ait pu exister auparavant, a été supprimé. |
| `Include Inclusion Data—error` | Ce paramètre accepte uniquement les valeurs booléennes (true ou false). Assurez-vous que la valeur de `include_inclusion_data` n'est pas comprise entre des guillemets (`""`), sinon la valeur est envoyée comme chaîne de caractères. Consultez les [paramètres de requête](#request-parameters) pour plus de détails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }


{% endapi %}