---
nav_title: "POST : Ajouter des e-mails à la liste noire"
article_title: "POST : Ajouter des e-mails à la liste noire"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "Cet article présente en détail l'endpoint Braze Ajouter des e-mails à la liste noire."

---
{% api %}
# Ajouter des e-mails à la liste noire {#blacklist-emails}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Braze a publié l'[endpoint `/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/) avec la même fonctionnalité que l'endpoint `/email/blacklist`. Nous vous recommandons d'utiliser l'endpoint `/email/blocklist` à la place.
{% endalert %}

> Utilisez cet endpoint pour désinscrire un utilisateur des e-mails et le marquer comme ayant subi un échec d'envoi définitif.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `email.blacklist`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Paramètres de demande {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| -----------|----------| --------|------- |
| `email` | Requis | Chaîne de caractères ou tableau | Adresse e-mail sous forme de chaîne de caractères à ajouter à la liste noire, ou un tableau de 50 adresses e-mail maximum à ajouter à la liste noire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## Exemple de demande {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}