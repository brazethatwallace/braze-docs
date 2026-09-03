---
nav_title: "POST : Supprimer les e-mails ayant reçu un échec d'envoi définitif"
article_title: "POST : Supprimer les e-mails ayant reçu un échec d'envoi définitif"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Supprimer les adresses e-mail ayant reçu un échec d'envoi définitif."

---
{% api %}
# Supprimer les e-mails ayant reçu un échec d'envoi définitif {#remove-hard-bounced-emails}
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

> Utilisez cet endpoint pour supprimer les adresses e-mail de votre liste d'échecs d'envoi définitifs Braze et de la liste d'échecs d'envoi définitifs gérée par votre fournisseur d'e-mails.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `email.bounce.remove`.

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

| Paramètre | Obligatoire | Type de données | Description |
| ----------|-----------| ---------|------ |
| `email` | Obligatoire | Chaîne de caractères ou tableau | Adresse e-mail sous forme de chaîne de caractères à modifier, ou tableau contenant jusqu'à 50 adresses e-mail à modifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@example.com"
}'
```

{% endapi %}