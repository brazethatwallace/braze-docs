---
nav_title: "POST: Synchronisation auslösen"
article_title: "POST: Synchronisation auslösen"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Braze-Endpunkt „Synchronisation auslösen“."

---
{% api %}
# Eine Synchronisation auslösen {#trigger-a-sync}
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Synchronisation für eine bestimmte Integration zu Trigger or triggern or triggern.

{% alert note %}
Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `cdi.integration_sync` generieren.
{% endalert %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Pfad-Parameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `integration_id` | Erforderlich | String | Integrations-ID. Diese finden Sie in der URL, wenn Sie eine Integration im Braze-Dashboard anzeigen. Das URL-Format lautet `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Pfad-Parameter" }

## Beispielanfrage {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `202` könnte den folgenden Antwortkörper zurückgeben:

```json
{
  "message": "success"
}
```

## Fehlerbehebung {#troubleshooting}

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlerbehebung |
| --- | --- |
| `400 Invalid integration ID` | Prüfen Sie, ob Ihre `integration_id` gültig ist. |
| `404 Integration not found` | Für die angegebene Integrations-ID existiert keine Integration. Vergewissern Sie sich, dass Ihre Integrations-ID gültig ist. |
| `429 Another job is in progress` | Für diese Integration wird derzeit eine Synchronisation durchgeführt. Versuchen Sie es erneut, nachdem die Synchronisation abgeschlossen ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

Weitere Statuscodes und zugehörige Fehlermeldungen finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors#fatal-errors).

{% endapi %}