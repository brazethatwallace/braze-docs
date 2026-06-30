---
nav_title: "POST : Supprimer les adresses e-mail de la liste des courriers indésirables"
article_title: "POST : Supprimer les adresses e-mail de la liste des courriers indésirables"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Supprimer les adresses e-mail de la liste des courriers indésirables."

---
{% api %}
# Supprimer les adresses e-mail de la liste des courriers indésirables {#remove-email-addresses-from-spam-list}
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> Utilisez cet endpoint pour supprimer des adresses e-mail de votre liste de courriers indésirables Braze et de la liste de courriers indésirables gérée par votre fournisseur d'e-mails.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `email.spam.remove`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com"
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| --------|------- |
| `email` | Requis | Chaîne de caractères ou tableau | Adresse e-mail sous forme de chaîne de caractères à modifier, ou tableau de 50 adresses e-mail maximum à modifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@example.com"
}'
```
{% endapi %}