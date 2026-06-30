---
nav_title: "GET : Liste des clés d'authentification SDK"
article_title: "GET : Liste des clés d'authentification SDK"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze permettant de lister les clés d'authentification SDK."
---

{% api %}
# Liste des clés d'authentification SDK {#list-sdk-authentication-keys}
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> Utilisez cet endpoint pour récupérer toutes les clés d'authentification SDK pour votre application.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `sdk_authentication.keys`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Requis | Chaîne de caractères | L'identifiant API de l'application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## Paramètres de réponse {#response-parameters}

| Paramètre | Type de données | Description |
| --------- | --------- | ----------- |
| `keys` | Tableau | Tableau d'objets de clés d'authentification SDK. |
| `keys[].id` | Chaîne de caractères | L'ID de la clé d'authentification SDK. |
| `keys[].rsa_public_key` | Chaîne de caractères | La chaîne de caractères de la clé publique RSA. |
| `keys[].description` | Chaîne de caractères | Description de la clé d'authentification SDK. |
| `keys[].is_primary` | Valeur booléenne | Indique si cette clé est la clé d'authentification SDK principale. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paramètres de réponse" }

### Règles de validation {#validation-rules}

Les règles de validation suivantes s'appliquent à cet endpoint :

- Le paramètre `app_id` doit être un identifiant API d'application valide.
- L'application doit exister dans votre espace de travail.

{% endapi %}