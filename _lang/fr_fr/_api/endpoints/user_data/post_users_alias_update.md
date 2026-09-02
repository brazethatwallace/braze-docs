---
nav_title: "POST : Mettre à jour l'alias d'utilisateur"
article_title: "POST : Mettre à jour l'alias d'utilisateur"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Mettre à jour les alias d'utilisateur."
---
{% api %}
# Mettre à jour l'alias d'utilisateur {#update-user-alias}
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour les alias d'utilisateur existants.

Vous pouvez spécifier jusqu'à 50 alias d'utilisateur par requête.

La mise à jour d'un alias d'utilisateur nécessite que `alias_label`, `old_alias_name` et `new_alias_name` soient inclus dans l'objet de mise à jour d'alias d'utilisateur. Si aucun alias d'utilisateur n'est associé au `alias_label` et au `old_alias_name`, aucun alias ne sera mis à jour. Si le `alias_label` et le `old_alias_name` sont trouvés, le `old_alias_name` sera mis à jour vers le `new_alias_name`.

{% alert note %}
Cet endpoint ne garantit pas l'ordre de mise à jour des objets `alias_updates`.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics) avec l'autorisation `users.alias.update`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | Requis | Tableau d'objets de mise à jour d'alias d'utilisateur | Voir l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object).<br><br> Pour plus d'informations sur `old_alias_name`, `new_alias_name` et `alias_label`, consultez la section [Alias d'utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

### Corps de requête de l'endpoint avec spécification de l'objet de mise à jour d'alias d'utilisateur {#endpoint-request-body-with-update-user-alias-object-specification}

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}