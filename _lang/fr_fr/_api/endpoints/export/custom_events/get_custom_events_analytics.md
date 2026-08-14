---
nav_title: "GET : Exporter l'analyse d'événements personnalisés"
article_title: "GET : Exporter l'analyse d'événements personnalisés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter l'analyse d'événements personnalisés."

---
{% api %}
# Exporter l'analyse d'événements personnalisés {#export-custom-events-analytics}
{% apimethod get %}
/events/data_series
{% endapimethod %}

> Utilisez cet endpoint pour récupérer une série du nombre d'occurrences d'un événement personnalisé dans votre application sur une période donnée.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `events.data_series`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `event` | Requis | Chaîne de caractères | Le nom de l'événement personnalisé pour lequel renvoyer l'analyse. |
| `length` | Requis | Entier | Nombre maximum d'unités (jours ou heures) avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `unit` | Facultatif | Chaîne de caractères | Unité de temps entre les points de données. Peut être `day` ou `hour`, valeur par défaut `day`. |
| `ending_at` | Facultatif | Datetime <br>(chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête. |
| `app_id` | Facultatif | Chaîne de caractères | Identifiant API de l'application récupéré à partir de la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) pour limiter l'analyse à une application spécifique. |
| `segment_id` | Facultatif | Chaîne de caractères | Voir [Identifiant API de Segment]({{site.baseurl}}/api/identifier_types). ID de Segment indiquant le segment avec l'analyse activée pour lequel l'analyse d'événements doit être renvoyée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }


## Exemple de requête {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "data" : [
        {
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int) the number of occurrences of provided custom event
        },
        ...
    ]
}
```

### Codes de réponse des erreurs fatales {#fatal-export}

Pour connaître les codes d'état et les messages d'erreur associés qui seront renvoyés si votre requête rencontre une erreur fatale, reportez-vous à la rubrique [Erreurs fatales et réponses]({{site.baseurl}}/api/errors#fatal-errors).

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}