---
nav_title: "GET: Status der Auftragssynchronisation auflisten"
article_title: "GET: Status der Auftragssynchronisation auflisten"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Status der Auftragssynchronisation auflisten“."

---
{% api %}
# Status der Auftragssynchronisation auflisten {#list-job-sync-status}
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der vergangenen Synchronisierungsstatus für eine bestimmte Integration zurückzugeben.

{% alert note %}
Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `cdi.integration_job_status` erstellen.
{% endalert %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## Pfadparameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `integration_id` | Erforderlich | String | Integrations-ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfadparameter" }

## Abfrageparameter {#query-parameters}

Jeder Aufruf dieses Endpunkts gibt 10 Einträge zurück. Bei einer Integration mit mehr als 10 Synchronisierungen verwenden Sie den `Link`-Header, um die Daten auf der nächsten Seite abzurufen, wie in der folgenden Beispielantwort gezeigt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung des Synchronisationsstatus. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

## Beispielanfrage {#example-request}

### Ohne Cursor {#without-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antworttext zurückgeben.

{% alert note %}
Der `Link`-Header existiert nicht, wenn es insgesamt 10 oder weniger Synchronisierungen gibt. Bei Aufrufen ohne Cursor wird `prev` nicht angezeigt. Wenn Sie sich die letzte Seite der Einträge ansehen, wird `next` nicht angezeigt.
{% endalert %}

```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
        "job_status": (string) status of the sync, see below for explanation of different statuses,
        "sync_start_time": (string) time the sync started in ISO 8601,
        "sync_finish_time": (string) time the sync finished in ISO 8601,
        "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
        "rows_synced": (integer) number of rows successfully synced to Braze,
        "rows_failed_with_errors": (integer) number of rows failed because of errors
    }
  ],
  "message": "success"
}
```

| job_status | Erklärung |
| --- | --- |
| `running` | Der Auftrag wird gerade ausgeführt. |
| `success` | Alle Zeilen wurden erfolgreich synchronisiert. |
| `partial` | Einige Zeilen konnten aufgrund von Fehlern nicht synchronisiert werden. |
| `error` | Es wurden keine Zeilen synchronisiert. |
| `config_error` | Es ist ein Fehler in der Integrationskonfiguration aufgetreten. Überprüfen Sie Ihre Integrationseinstellungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel für eine erfolgreiche Antwort" }

## Fehlerbehebung {#troubleshooting}

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlerbehebung |
| --- | --- |
| `400 Invalid cursor` | Prüfen Sie, ob Ihr `cursor` gültig ist. |
| `400 Invalid integration ID` | Prüfen Sie, ob Ihre `integration_id` gültig ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

Weitere Statuscodes und zugehörige Fehlermeldungen finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors#fatal-errors).

{% endapi %}