---
nav_title: "GET : Exporter l'analyse d'envoi"
article_title: "GET : Exporter l'analyse d'envoi"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter l'analyse d'envoi."

---
{% api %}
# Exporter l'analyse d'envoi {#export-send-analytics}
{% apimethod get %}
/sends/data_series
{% endapimethod %}

> Utilisez cet endpoint pour récupérer une série quotidienne de diverses statistiques pour un `send_id` suivi dans le cadre de Campaigns API.

Braze stocke les analyses d'envoi pendant 14 jours après l'envoi. Les conversions de la Campaign seront attribuées au `send_id` le plus récent qu'un utilisateur donné a reçu de cette Campaign.

{% multi_lang_include api/export_data_series_analytics_dashboard_note.md type='send' %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## Conditions préalables {#prerequisites}

Cet endpoint est réservé aux Campaigns API. Pour l'utiliser, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `sends.data_series`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- |------------ |
| `campaign_id` | Requis | Chaîne de caractères | Voir [identifiant API de campagne]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Requis | Chaîne de caractères | Voir [identifiant API d'envoi]({{site.baseurl}}/api/identifier_types). |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `ending_at` | Facultatif | Datetime <br>(chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, correspond à l'heure de la requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time": (string) the date as ISO 8601 date,
            "messages": {
                "ios_push" : [
                    {
                      "variation_name": (string) variation name,
                      "sent": (int) the number of sends,
                      "delivered": (int) the number of messages successfully delivered,
                      "undelivered": (int) the number of undelivered,
                      "delivery_failed": (int) the number of rejected,
                      "direct_opens": (int) the number of direct opens,
                      "total_opens": (int) the number of total opens,
                      "bounces": (int) the number of bounces,
                      "body_clicks": (int) the number of body clicks,
                      "revenue": (float) the number of dollars of revenue (USD),
                      "unique_recipients": (int) the number of unique recipients at the campaign-level,
                      "conversions": (int) the number of conversions,
                      "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                      "conversions1": (optional, int) the number of conversions for the second conversion event,
                      "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                      "conversions2": (optional, int) the number of conversions for the third conversion event,
                      "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                      "conversions3_by_send_time": (optional, int) the number of conversions for the fourth, conversion event attributed to the date the campaign was sent
                      }
                  ]
            },
        "conversions_by_send_time": (optional, int),
        "conversions1_by_send_time": (optional, int),
        "conversions2_by_send_time": (optional, int),
        "conversions3_by_send_time": (optional, int),
        "conversions": (int),
        "conversions1": (optional, int),
        "conversions2": (optional, int),
        "conversions3": (optional, int),
        "unique_recipients": (int),
        "revenue": (optional, float)
      }
    ],
  "message": "success"
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}