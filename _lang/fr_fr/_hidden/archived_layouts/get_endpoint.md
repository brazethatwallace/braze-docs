---
nav_title: "GET : [Nom de l'endpoint]"
article_title: "Exemple de mise en page : GET : [Nom de l'endpoint]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "Cet article décrit l'utilisation et les paramètres de l'endpoint Braze GET [nom de l'endpoint]."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# Requête ou liste [Item Endpoint « Gets »] {#query-or-list-item-endpoint-gets}

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Utilisez cet endpoint pour récupérer une liste des numéros de téléphone considérés comme « non valides » au cours d'une période donnée.

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Limite de débit {#rate-limit}

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

<!--This is where you can give more information about your endpoint parameters. -->

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format YYYY-MM-DD | Date de début de la plage pour récupérer les numéros de téléphone non valides. Doit être antérieure à `end_date`. L'API traite cette valeur comme minuit (UTC). |
| `end_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format YYYY-MM-DD | Date de fin de la plage pour récupérer les numéros de téléphone non valides. L'API traite cette valeur comme minuit (UTC). |
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. Par défaut : 100, maximum : 500. |
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste à partir duquel récupérer les résultats. |
| `phone_numbers` | Facultatif <br>(voir la note) | Tableau de chaînes de caractères au format e.164 | Si ce paramètre est fourni, le numéro de téléphone sera renvoyé s'il s'avère non valide. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert note %}
Vous devez fournir soit une `start_date` et une `end_date`, soit un `phone_numbers`. Si vous fournissez les trois (`start_date`, `end_date` et `phone_numbers`), la priorité sera donnée aux numéros de téléphone fournis et la plage de dates sera ignorée.
{% endalert %}

## Exemple de requête {#example-request}

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse {#response}

<!-- An example response that defines the different variables returned-->
```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    }
  ],
  "message": "success"
}
```

{% endapi %}