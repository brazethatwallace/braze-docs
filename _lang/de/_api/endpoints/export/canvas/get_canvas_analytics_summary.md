---
nav_title: "GET: Canvas-Daten-Zusammenfassung Analytics exportieren"
article_title: "GET: Canvas-Daten-Zusammenfassung Analytics exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Exportieren der Canvas-Daten-Zusammenfassung Analytics."

---
{% api %}
# Canvas-Daten-Zusammenfassung Analytics exportieren {#export-canvas-data-summary-analytics}
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Rollups von Zeitreihendaten für ein Canvas zu exportieren und so eine prägnante Zusammenfassung der Canvas-Ergebnisse zu erhalten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.data_summary`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Erforderlich | String | Siehe [Canvas-API-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Erforderlich | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Enddatum für den Datenexport. Standardmäßig wird der Zeitpunkt der Anfrage verwendet. |
| `starting_at` | Optional* | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Startdatum für den Datenexport. <br><br>* Entweder `length` oder `starting_at` ist erforderlich. |
| `length` | Optional* | String | Maximale Anzahl von Tagen vor `ending_at`, die in die zurückgegebene Reihe aufgenommen werden. Muss zwischen 1 und 14 (einschließlich) liegen. <br><br>* Entweder `length` oder `starting_at` ist erforderlich. |
| `include_variant_breakdown` | Optional | Boolescher Wert | Ob Variantenstatistiken einbezogen werden sollen (Standardwert ist `false`).  |
| `include_step_breakdown` | Optional | Boolescher Wert | Ob Schrittstatistiken einbezogen werden sollen (Standardwert ist `false`). |
| `include_deleted_step_data` | Optional | Boolescher Wert | Ob Schrittstatistiken für gelöschte Schritte einbezogen werden sollen (Standardwert ist `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert important %}
**Zeitzonen-Abgleich:** Die Analytics-Daten des Braze-Dashboards werden täglich in der für Ihr Unternehmen konfigurierten Zeitzone im Dashboard aggregiert. Stellen Sie sicher, dass Ihre Zeitstempel mit der Zeitzone Ihres Unternehmens übereinstimmen, damit Ihre Statistiken mit dem Dashboard übereinstimmen. Wenn die Zeitzone Ihres Unternehmens beispielsweise UTC+2 ist, sollte der Zeitstempel 0:00 Uhr UTC+2 lauten.
{% endalert %}

## Beispielanfrage {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort {#response}

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "conversions": (int) the number of conversions,
      "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
      "entries": (int) the number of entries
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
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
  "message": (required, string) the status of the export, returns 'success' on successful completion
}
```

{% alert important %}
**Feld `influenced_opens`:** In der API-Antwort gibt das Feld `influenced_opens` die Gesamtzahl der Öffnungen an (sowohl direkte als auch beeinflusste Öffnungen zusammen). Im Braze-Dashboard bezieht sich „beeinflusste Öffnungen“ ausschließlich auf beeinflusste Öffnungen, wobei direkte Öffnungen ausgeschlossen sind. Dies ist auf eine veraltete Namenskonvention in der API zurückzuführen.
{% endalert %}

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}