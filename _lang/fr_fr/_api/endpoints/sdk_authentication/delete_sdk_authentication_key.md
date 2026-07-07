---
nav_title: "DELETE : Supprimer la clé d'authentification SDK"
article_title: "DELETE : Supprimer la clé d'authentification SDK"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Supprimer la clé d'authentification SDK."
---

{% api %}
# Supprimer la clé d'authentification SDK {#delete-sdk-authentication-key}
{% apimethod delete %}
/app_group/sdk_authentication/delete
{% endapimethod %}

> Utilisez cet endpoint pour supprimer une clé d'authentification SDK pour votre application.

{% alert important %}
La clé primaire ne peut pas être supprimée. Si vous tentez de supprimer la clé primaire, cet endpoint renverra une erreur.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `sdk_authentication.delete`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API Identifier",
  "key_id": "key id"
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Requis | Chaîne de caractères | L'identifiant API de l'application. |
| `key_id` | Requis | Chaîne de caractères | L'ID de la clé d'authentification SDK à supprimer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/app_group/sdk_authentication/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "key_id": "fedcba98-7654-3210-fedc-ba9876543210"
}'
```

## Réponse {#response}

```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    }
  ]
}
```

## Paramètres de réponse {#response-parameters}

| Paramètre | Type de données | Description |
| --------- | --------- | ----------- |
| `keys` | Tableau | Tableau des objets de clés d'authentification SDK restants. |
| `keys[].id` | Chaîne de caractères | L'ID de la clé d'authentification SDK. |
| `keys[].rsa_public_key` | Chaîne de caractères | La chaîne de caractères de la clé publique RSA. |
| `keys[].description` | Chaîne de caractères | Description de la clé d'authentification SDK. |
| `keys[].is_primary` | Valeur booléenne | Indique si cette clé est la clé d'authentification SDK primaire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres de réponse" }

### Règles de validation {#validation-rules}

Les règles de validation suivantes s'appliquent à cet endpoint :

- Le `key_id` doit être un ID de clé d'authentification SDK valide.
- Le `app_id` doit être un identifiant API d'application valide.
- La clé d'authentification SDK doit exister pour l'application spécifiée.
- La clé d'authentification SDK primaire ne peut pas être supprimée.

{% endapi %}