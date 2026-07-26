---
nav_title: Treasure Data für Currents
article_title: Treasure Data für Currents
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Treasure Data, einer geschäftskunden Data Platform (CDP) für Unternehmen, die Braze-Ereignisdaten in Treasure Data streamt, um sie dort zu analysieren und zu aktivieren."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data für Currents {#treasure-data-for-currents}

> [Treasure Data](https://www.treasuredata.com/) ist eine geschäftskunden Data Platform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Ziele in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und Treasure Data erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen zu steuern. Mit Currents können Sie Braze-Ereignisdaten in Treasure Data streamen und über den gesamten Growth Stack hinweg nutzbar machen.

Die empfohlene Methode ist der **Braze Currents Streaming**-Konnektor in Treasure Data in Kombination mit einem **Custom Currents Export** in Braze. Dieser Ansatz bietet:

- Realtime-Event-Streaming von Braze in Treasure Data
- Optionales automatisches Tabellenrouting nach Ereignistyp
- Ein flaches, SQL-abfragbares Schema, das kein JSON-Parsing erfordert

{% alert important %}
Der Braze Currents Streaming-Konnektor befindet sich in der Beta-Phase. Kontaktieren Sie den Treasure Data-Support, um ihn für Ihr Treasure Data-Konto zu aktivieren. Weitere Informationen zur partnerseitigen Einrichtung finden Sie in der Treasure Data-Dokumentation zur [Braze Currents Import Integration](https://docs.treasuredata.com/int/braze-currents-import-integration).
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Treasure Data-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein aktives [Treasure Data-Konto](https://console.treasuredata.com). |
| Currents | Um Daten in Treasure Data zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) für Ihr Konto einrichten lassen. |
| Braze Currents Streaming-Konnektor | Kontaktieren Sie den Treasure Data-Support, um den Braze Currents Streaming-Konnektor (Beta) für Ihr Treasure Data-Konto zu aktivieren. |
| Treasure Data Write-API-Schlüssel | Ein Treasure Data Write-API-Schlüssel authentifiziert den eingehenden Stream von Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Konnektor in Treasure Data konfigurieren {#step-1-configure-the-connector-in-treasure-data}

1. Navigieren Sie in der Treasure Data-Konsole zu **Connections** > **New Connection**.
2. Wählen Sie **Braze Currents Streaming** aus.
3. Geben Sie unter **Authentication** Ihren Treasure Data Write-API-Schlüssel ein.
4. Konfigurieren Sie unter **Source Settings** die folgenden Einstellungen:

| Feld | Beschreibung |
| ---- | ----------- |
| Source Name | Ein beschreibender Name für diese Verbindung |
| Datastore | Wählen Sie **Plazma** aus |
| Database | Die Treasure Data-Datenbank, in der Ereignisse gespeichert werden |
| Table | Die Standard-Zieltabelle |
| Multiple Tables | Aktivieren Sie diese Option, um jeden Braze-Ereignistyp in eine eigene Tabelle zu leiten |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quelleinstellungen" }

5. Kopieren Sie nach dem Speichern die **Unique ID** (`task_id`). Sie benötigen diesen Wert im nächsten Schritt.

### Schritt 2: Custom Currents Export in Braze erstellen {#step-2-create-a-custom-currents-export-in-braze}

Die Option **Treasure Data Export** in der Braze-Currents-UI verwendet die veraltete Postback-API-Methode und wird nicht mehr empfohlen. Verwenden Sie stattdessen **Custom Currents Export**.

1. Navigieren Sie in Braze zu **Partnerintegrationen** > **Data Export**.
2. Wählen Sie **Create New Current** > **Custom Currents Export** aus.
3. Geben Sie einen Integrationsnamen und eine Kontakt-E-Mail für Fehlerbenachrichtigungen ein.
4. Geben Sie unter **Credentials** die Endpunkt-URL für Ihre Treasure Data-Region ein. Geben Sie Ihren Treasure Data Write-API-Schlüssel als **Bearer Token** ein.

| Region | Endpunkt-URL |
| ------ | ------------ |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpunkt-URLs nach Region" }

Ersetzen Sie `{TASK_ID}` durch die Unique ID, die Sie in [Schritt 1](#step-1-configure-the-connector-in-treasure-data) kopiert haben.

5. Wählen Sie die Ereignistypen aus, die Sie exportieren möchten. Custom Currents-Verbindungen können Ereignisse für identifizierte Nutzer:innen und für Nutzer:innen ohne `external_user_id` senden. Treasure Data nimmt beide auf.
6. Wählen Sie **Launch Current** aus.

{% alert warning %}
Halten Sie Ihren Treasure Data Write-API-Schlüssel und die Endpunkt-URL auf dem neuesten Stand. Wenn der Endpunkt länger als **5&nbsp;Tage** nicht erreichbar ist, verwirft Braze die Ereignisse des Konnektors und die Daten gehen dauerhaft verloren.
{% endalert %}

## Daten abfragen {#query-your-data}

Sobald Ereignisse eintreffen, können Sie sie mit SQL abfragen. Treasure Data flacht die Payload ab, sodass kein JSON-Parsing erforderlich ist.

```sql
SELECT
  id AS event_id,
  event_type,
  user_external_user_id,
  properties_campaign_name,
  properties_email_address,
  time
FROM your_database.your_table
WHERE TD_INTERVAL(time, '-1d', 'JST')
```

{% alert note %}
Das Feld `time` in Treasure Data ist der Zeitstempel, zu dem Treasure Data das Ereignis empfangen und verarbeitet hat – nicht der ursprüngliche Zeitpunkt des Ereignisses in Braze.
{% endalert %}

Wenn Sie **Multiple Tables** ausgewählt haben, wird jeder Ereignistyp in einer eigenen Tabelle gespeichert (zum Beispiel `users_message_email_open` oder `users_behaviors_purchase`).

Um zu bestätigen, dass Daten eintreffen, führen Sie einige Minuten nach dem Start des Currents eine Zählabfrage aus:

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## Datenschema {#data-schema}

Treasure Data flacht verschachteltes JSON bis zu zwei Ebenen tief ab:

| JSON-Typ | Treasure Data-Spaltentyp |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object (Ebene 1) | `field_name` |
| object (Ebene 2) | `parent_field_name_field_name` |
| null | ausgelassen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datentypzuordnung" }

Spaltennamen verwenden ausschließlich Kleinbuchstaben und Unterstriche.

## Limits

| Element | Limit |
| ------- | ----- |
| Maximale Payload-Größe | 1&nbsp;MB pro Anfrage |
| Batch-Größe | 100 Ereignisse pro Batch (Standard) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limits" }

## Details zur Integration {#integration-details}

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data/distribution/braze_currents) aufgeführt sind, in Treasure Data. Dies umfasst alle Eigenschaften von [Nachrichten-Engagement-]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und [Kundenverhalten-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren. Beispiel-Payloads können Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen.

## Migration von der veralteten Postback-Methode {#migrate-from-the-legacy-postback-method}

Wenn Sie zuvor **Treasure Data Export** (Postback) in Braze verwendet haben:

1. Führen Sie die Einrichtung des Custom Currents Exports gemäß dieser Anleitung durch.
2. Bestätigen Sie, dass Ereignisse in die neue Tabelle fließen.
3. Deaktivieren Sie den alten Postback-basierten Current in Braze.

Ältere Daten, die als rohe JSON-Arrays gespeichert sind, können weiterhin mit `JSON_PARSE` und `UNNEST` abgefragt werden. Neue Daten, die über den Streaming-Konnektor aufgenommen werden, verwenden das flache Schema, das unter [Datenschema](#data-schema) beschrieben ist.