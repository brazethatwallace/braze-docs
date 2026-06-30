---
nav_title: "GET: Integrationen auflisten"
article_title: "GET: Integrationen auflisten"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten über den Braze-Endpunkt „Integrationen auflisten“."

---
{% api %}
# Integrationen auflisten {#list-integrations}
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der vorhandenen Integrationen zurückzugeben.


{% alert note %}
Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `cdi.integration_list` erstellen.
{% endalert %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## Abfrageparameter {#query-parameters}

Jeder Aufruf dieses Endpunkts gibt 10 Einträge zurück. Bei einer Liste mit mehr als 10 Integrationen verwenden Sie den `Link`-Header, um die Daten auf der nächsten Seite abzurufen, wie in der Beispielantwort gezeigt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung der Integrationsliste. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

## Beispielanfrage {#example-request}

### Ohne Cursor {#without-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwortkörper zurückgeben.

{% alert note %}
Der `Link`-Header ist nicht vorhanden, wenn es insgesamt weniger als oder gleich 10 Integrationen gibt. Bei Aufrufen ohne Cursor wird `prev` nicht angezeigt. Wenn Sie sich die letzte Seite der Einträge ansehen, wird `next` nicht angezeigt.
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601
    }
  ],
  "message": "success"
}
```

## Fehlerbehebung {#troubleshooting}

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlerbehebung |
| --- | --- |
| `400 Invalid cursor` | Prüfen Sie, ob Ihr `cursor` gültig ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

Weitere Statuscodes und zugehörige Fehlermeldungen finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors#fatal-errors).

{% endapi %}