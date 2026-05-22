---
nav_title: "GET : Extraire les e-mails ayant reçu un échec d'envoi définitif"
article_title: "GET : Extraire les e-mails ayant reçu un échec d'envoi définitif"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze permettant d'interroger ou de lister les adresses e-mail ayant reçu un échec d'envoi définitif."

---
{% api %}
# Extraire les e-mails ayant reçu un échec d'envoi définitif {#query-hard-bounced-emails}
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Utilisez cet endpoint pour extraire une liste d'adresses e-mail ayant rejeté définitivement vos e-mails au cours d'une certaine période.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `email.hard_bounces`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Facultatif* | Chaîne de caractères au format AAAA-MM-JJ | *L'un des paramètres `start_date` ou `email` est requis. Il s'agit de la date de début de la plage de récupération des échecs d'envoi définitifs, qui doit être antérieure à `end_date`. L'API traite cette valeur comme minuit (UTC). |
| `end_date` | Requis | Chaîne de caractères au format AAAA-MM-JJ | Date de fin de la période d'extraction des échecs d'envoi définitifs. L'API traite cette valeur comme minuit (UTC). |
| `limit` | Facultatif | Entier | Champ facultatif permettant de limiter le nombre de résultats renvoyés. La valeur par défaut est 100, le maximum est 500. |
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste à partir duquel récupérer les résultats. |
| `email` | Facultatif* | Chaîne de caractères | *L'un des paramètres `start_date` ou `email` est requis. Si ce paramètre est fourni, nous indiquerons si l'utilisateur a fait l'objet d'un échec d'envoi définitif. Vérifiez que les chaînes d'e-mails sont correctement formatées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Vous devez fournir un `end_date`, ainsi qu'un `email` ou un `start_date`. Si vous fournissez les trois, à savoir `start_date`, `end_date` et `email`, nous donnerons la priorité aux e-mails communiqués et ignorerons la plage de dates.
{% endalert %}

Si votre plage de dates contient plus d'échecs d'envoi définitifs que la valeur `limit`, vous devrez effectuer plusieurs appels API en augmentant à chaque fois le `offset`, jusqu'à ce qu'un appel renvoie un nombre de résultats inférieur à `limit` ou égal à zéro. L'inclusion des paramètres `offset` et `limit` avec `email` peut renvoyer une réponse vide.

## Exemple de requête {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse {#response}
Les entrées sont répertoriées par ordre décroissant.

```json
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}