---
nav_title: "GET : Extraire les numéros de téléphone non valides"
article_title: "GET : Extraire les numéros de téléphone non valides"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Extraire les numéros de téléphone non valides."
---
{% api %}
# Extraire les numéros de téléphone non valides {#query-invalid-phone-numbers}
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> Utilisez cet endpoint pour obtenir une liste des numéros de téléphone qui ont été marqués comme « invalides » dans un certain laps de temps. Pour plus d'informations, consultez la documentation sur la [gestion des numéros de téléphone non valides]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers#handling-invalid-phone-numbers).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `sms.invalid_phone_numbers`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format YYYY-MM-DD | Date de début de la plage pour récupérer les numéros de téléphone non valides, doit être antérieure à `end_date`. Ce paramètre est traité comme minuit (UTC) par l'API. |
| `end_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format YYYY-MM-DD | Date de fin de la plage pour récupérer les numéros de téléphone non valides. Ce paramètre est traité comme minuit (UTC) par l'API. |
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. La valeur par défaut est 100, le maximum est 500. |
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste où commencer la récupération. |
| `phone_numbers` | Facultatif <br>(voir la note) | Tableau de chaînes de caractères au format e.164 | S'il est fourni, nous renverrons le numéro de téléphone s'il s'avère non valide. |
| `reason` | Facultatif <br>(voir la note) | Chaîne de caractères | Les valeurs disponibles sont "provider_error" (une erreur de l'opérateur indique que le téléphone ne peut pas recevoir de SMS) ou "deactivated" (le numéro de téléphone a été désactivé). En cas d'omission, tous les motifs sont renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert note %}
Vous devez fournir une `start_date` et une `end_date`, OU un `phone_numbers`. Si vous fournissez les trois (`start_date`, `end_date` et `phone_numbers`), nous donnerons la priorité aux numéros de téléphone communiqués et ignorerons la plage de dates.
{% endalert %}

Si votre plage de dates contient plus de numéros de téléphone non valides que la valeur `limit`, vous devrez effectuer plusieurs appels API en augmentant le `offset` à chaque fois, jusqu'à ce qu'un appel renvoie un nombre de résultats inférieur à `limit` ou égal à zéro.

## Exemple de requête {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse {#response}
Les entrées sont répertoriées par ordre décroissant.

```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}