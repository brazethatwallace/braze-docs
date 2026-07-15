---
nav_title: "POST : Créer un nouvel alias utilisateur"
article_title: "POST : Créer un nouvel alias utilisateur"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Créer un nouvel alias utilisateur."

---
{% api %}
# Créer un nouvel alias utilisateur {#create-new-user-alias}
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Utilisez cet endpoint pour ajouter de nouveaux alias d'utilisateur pour les utilisateurs identifiés existants, ou pour créer de nouveaux utilisateurs non identifiés.

Vous pouvez spécifier jusqu'à 50 alias d'utilisateur par requête.

L'**ajout d'un alias d'utilisateur pour un utilisateur existant** nécessite qu'un `external_id` soit inclus dans le nouvel objet alias d'utilisateur. Si l'`external_id` est présent dans l'objet mais qu'aucun utilisateur ne possède cet `external_id`, l'alias ne sera ajouté à aucun utilisateur. En l'absence d'un `external_id`, un utilisateur sera tout de même créé, mais il devra être identifié ultérieurement. Vous pouvez le faire en utilisant la fonctionnalité « Identification des utilisateurs » et l'endpoint `users/identify`.

**La création d'un nouvel utilisateur alias uniquement** nécessite que l'`external_id` soit omis du nouvel objet alias d'utilisateur. Une fois l'utilisateur créé, utilisez l'endpoint `/users/track` pour associer l'utilisateur alias uniquement à des attributs, des événements et des achats, et l'endpoint `/users/identify` pour identifier l'utilisateur avec un `external_id`.

## Lorsque `alias_label` et `alias_name` existent déjà {#when-alias_label-and-alias_name-already-exist}

La combinaison de `alias_label` et `alias_name` doit être unique dans l'ensemble de votre base d'utilisateurs. Pour plus d'informations, consultez [Alias d'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases).

Si vous envoyez une requête dans laquelle la paire `alias_label` et `alias_name` existe déjà pour un utilisateur (que ce soit le même utilisateur ou un autre), l'endpoint renvoie tout de même une réponse de succès (par exemple, `"aliases_processed": 1`, `"message": "success"`). Dans ce cas, aucun nouvel alias n'est ajouté à l'utilisateur de la requête. Étant donné que la paire `alias_label` et `alias_name` est déjà utilisée, la requête n'effectue aucune modification, et il peut sembler que l'alias n'a jamais été ajouté à l'utilisateur en question.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `users.alias.new`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Requis | Tableau d'objets nouvel alias d'utilisateur | Voir l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object).<br><br> Pour plus d'informations sur `alias_name` et `alias_label`, consultez notre documentation sur les [alias d'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

### Corps de requête de l'endpoint avec spécification de l'objet nouvel alias d'utilisateur {#endpoint-request-body-with-new-user-alias-object-specification}

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Réponse {#response}

Lorsqu'un alias est ignoré parce que la même combinaison `alias_label` et `alias_name` existe déjà pour un utilisateur, le corps de la réponse peut tout de même indiquer un succès. Consultez [Lorsque le libellé d'alias et le nom existent déjà](#when-the-alias-label-and-name-already-exist) pour plus de détails.

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}