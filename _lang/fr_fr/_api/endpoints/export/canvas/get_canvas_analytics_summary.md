---
nav_title: "GET : Exporter le résumé analytique des données de Canvas"
article_title: "GET : Exporter le résumé analytique des données de Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article décrit l'endpoint Braze permettant d'exporter le résumé analytique des données de Canvas."

---
{% api %}
# Exporter le résumé analytique des données de Canvas {#export-canvas-data-summary-analytics}
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> Utilisez cet endpoint pour exporter des synthèses de données chronologiques pour un Canvas, fournissant ainsi un résumé concis des résultats du Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `canvas.data_summary`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Requis | Chaîne de caractères | Voir [Identifiant API Canvas]({{site.baseurl}}/api/identifier_types). |
| `ending_at` | Requis | Datetime <br>(chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date de fin de l'exportation des données. Par défaut, correspond à l'heure de la requête. |
| `starting_at` | Facultatif* | Datetime <br>(chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date de début de l'exportation des données. <br><br>* `length` ou `starting_at` est requis. |
| `length` | Facultatif* | Chaîne de caractères | Nombre maximal de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 14 (inclus). <br><br>* `length` ou `starting_at` est requis. |
| `include_variant_breakdown` | Facultatif | Valeur booléenne | Indique s'il faut inclure les statistiques des variantes (par défaut `false`). |
| `include_step_breakdown` | Facultatif | Valeur booléenne | Indique s'il faut inclure les statistiques par étape (par défaut `false`). |
| `include_deleted_step_data` | Facultatif | Valeur booléenne | Indique s'il faut inclure les statistiques des étapes supprimées (par défaut `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert important %}
Les analyses Canvas sont agrégées par jour dans le fuseau horaire configuré pour votre société dans Braze (le même fuseau horaire utilisé par le tableau de bord). L'API normalise `starting_at` et `ending_at` à minuit dans ce fuseau horaire. Assurez-vous que vos horodatages correspondent au fuseau horaire de votre société afin que vos statistiques concordent avec le tableau de bord. Par exemple, si le fuseau horaire de votre société est UTC+2, l'horodatage doit être 0 h 00 UTC+2.
{% endalert %}

## Exemple de requête {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse {#response}

### Champs d'événement de conversion {#conversion-event-fields}

La réponse inclut une paire de champs de conversion pour chaque événement de conversion configuré sur le Canvas. L'événement de conversion principal utilise `conversions` et `conversions_by_entry_time`. Chaque événement supplémentaire utilise le même nom de base avec un suffixe numérique commençant à `1` pour le deuxième événement, puis incrémenté de un pour chaque événement suivant.

| Ordre de l'événement de conversion sur le Canvas | Champ de conversions | Champ par heure d'entrée |
| --- | --- | --- |
| Principal | `conversions` | `conversions_by_entry_time` |
| Deuxième | `conversions1` | `conversions1_by_entry_time` |
| Troisième | `conversions2` | `conversions2_by_entry_time` |
| Quatrième | `conversions3` | `conversions3_by_entry_time` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ordre de conversion" }

Le cinquième événement et les suivants respectent le même schéma (par exemple, `conversions4` et `conversions4_by_entry_time`). Ces champs apparaissent dans `total_stats` et, lorsque vous demandez des ventilations, dans `variant_stats` et `step_stats` sous les mêmes noms.

{% alert note %}
Dans `total_stats`, `variant_stats` et `step_stats`, `conversions` correspond au nombre de conversions pour l'[événement de conversion principal]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) du Canvas. Lorsque vous configurez des événements de conversion supplémentaires, le payload peut également inclure `conversions1`, `conversions2` et des champs indexés supérieurs pour le deuxième, le troisième événement et les suivants. Cela est similaire à la [réponse multivariée]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics#multivariate-response) pour l'endpoint `/campaigns/data_series`. Lorsqu'ils sont présents, les champs se terminant par `_by_entry_time` attribuent ces conversions en fonction de l'heure d'entrée dans le Canvas.
{% endalert %}

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "entries": (int) the number of entries,
      "conversions": (int) the number of conversions for the primary conversion event,
      "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
      "conversions1": (optional, int) the number of conversions for the second conversion event,
      "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
      "conversions2": (optional, int) the number of conversions for the third conversion event,
      "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
      "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (optional, int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (string) returns 'success' when the request completes without errors
}
```

{% alert important %}
Dans la réponse de l'API, le champ `influenced_opens` représente le nombre total d'ouvertures (ouvertures directes et ouvertures influencées combinées). Dans le tableau de bord de Braze, le terme « ouvertures influencées » désigne uniquement les ouvertures influencées, à l'exclusion des ouvertures directes. Cela est dû à une convention de nommage héritée dans l'API.
{% endalert %}

## Articles connexes {#related-articles}

- [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)


{% endapi %}