---
nav_title: "GET : Requête de la liste des adresses e-mail désabonnées"
article_title: "GET : Requête de la liste des adresses e-mail désabonnées"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze permettant de récupérer la liste ou d'interroger les désabonnements par e-mail."

---
{% api %}
# Requête de la liste des adresses e-mail désabonnées {#query-list-of-unsubscribed-email-addresses}
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer les derniers e-mails désabonnés pendant la période allant de `start_date` à `end_date`. Pour un historique complet de l'état d'abonnement, utilisez [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) pour suivre ces données.

Vous pouvez utiliser cet endpoint pour configurer une synchronisation bidirectionnelle entre Braze et d'autres systèmes de messagerie ou votre propre base de données.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `email.unsubscribe`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ---------|------ |
| `start_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format AAAA-MM-JJ | Date de début de la plage de récupération des désabonnements, qui doit être antérieure à end_date. L'API considère que cette date correspond à minuit (heure UTC). |
| `end_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format AAAA-MM-JJ | Date de fin de la plage de récupération des désabonnements. L'API considère que cette date correspond à minuit (heure UTC). |
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. La valeur par défaut est 100, le maximum est 500. |
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste à partir duquel récupérer les résultats. |
| `sort_direction` | Facultatif | Chaîne de caractères | Indiquez la valeur `asc` pour trier les désabonnements du plus ancien au plus récent. Indiquez la valeur `desc` pour trier du plus récent au plus ancien. Si `sort_direction` n'est pas inclus, l'ordre par défaut est du plus récent au plus ancien. |
| `email` | Facultatif <br>(voir la note) | Chaîne de caractères | Si ce paramètre est fourni, l'endpoint indiquera si l'utilisateur s'est désabonné ou non. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert note %}
Vous devez fournir une `end_date`, ainsi qu'un `email` ou une `start_date`.
{% endalert %}

Si votre plage de dates contient plus de désabonnements que la valeur `limit`, vous devrez effectuer plusieurs appels API en augmentant à chaque fois le `offset`, jusqu'à ce qu'un appel renvoie un nombre de résultats inférieur à `limit` ou égal à zéro.

## Exemple de requête {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@example.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse {#response}

Les entrées sont répertoriées par ordre décroissant.

```json
{
  "emails": [
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}