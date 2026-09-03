---
nav_title: "GET: Versand-Analytics exportieren"
article_title: "GET: Versand-Analytics exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Versand-Analytics exportieren“."

---
{% api %}
# Versand-Analytics exportieren {#export-send-analytics}
{% apimethod get %}
/sends/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine tägliche Reihe verschiedener Statistiken für eine getrackte `send_id` für API-Kampagnen abzurufen.

Braze speichert Versand-Analytics für 14 Tage nach dem Versand. Campaign-Konversionen werden der letzten `send_id` zugeschrieben, die ein:e bestimmte:r Nutzer:in von der Campaign erhalten hat.

{% multi_lang_include api/export_data_series_analytics_dashboard_note.md type='send' %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## Voraussetzungen {#prerequisites}

Dieser Endpunkt ist nur für API-Kampagnen gedacht. Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `sends.data_series`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- |------------ |
| `campaign_id` | Erforderlich | String | Siehe [Campaign-API-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Erforderlich | String | Siehe [Versand-API-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `length` | Erforderlich | Integer | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Reihe enthalten sein sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `ending_at` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird der Zeitpunkt der Anfrage verwendet. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort {#response}

```json
{
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
  "message": (string) returns 'success' when the request completes without errors
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}