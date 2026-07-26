---
nav_title: Snapshots versus Event-Streams
article_title: Snapshots versus Event-Streams
page_order: 4
page_type: reference
description: "Dieser Referenzartikel erläutert den Unterschied zwischen Snapshot-Daten und Event-Stream-Daten und wie diese jeweils strukturiert und an BrazeAI Decisioning Studio übermittelt werden sollten."
---

# Snapshots versus Event-Streams {#snapshots-versus-event-streams}

> Daten lassen sich in eine von zwei grundlegenden Kategorien einteilen: Snapshots (Zustand) und Event-Streams (was passiert ist). Dieses Unterscheidungsmerkmal zu verstehen und korrekt anzuwenden, ist einer der wichtigsten Schritte, um sicherzustellen, dass Ihr Decisioning-Studio-Agent effektiv lernt.

## Snapshot-Daten (Zustand) {#snapshot-data-state}

Ein Snapshot repräsentiert den Zustand einer geschäftskunden zu einem bestimmten Zeitpunkt. Er beantwortet die Frage: „Wie sieht diese geschäftskunden gerade aus?“

Ein Snapshot ist statisch und aggregiert. Er spiegelt das kumulative Ergebnis aller Änderungen bis zu diesem Zeitpunkt wider. Dies eignet sich am besten für Kundenprofile, berechnete Features (zum Beispiel „Tage seit dem letzten Kauf“, „Treuestufe“, „Churn-Score“).

### Erforderliche Felder {#required-fields}

| Feld | Zweck |
|------|-------|
| Kundenbezeichner | Wen dieser Datensatz beschreibt |
| Snapshot-Datum | Wann dieser Snapshot erstellt wurde |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erforderliche Felder" }

### Wie Snapshots aktualisiert werden sollten {#how-snapshots-should-be-updated}

- **Auslöser:** Zeitgesteuert, nicht ereignisgesteuert. Snapshots sollten nach einem festen Zeitplan generiert werden (zum Beispiel täglich), unabhängig davon, ob eine geschäftskunden an diesem Tag Aktivität hatte.
- **Umfang:** Jedes Update muss alle relevanten Kund:innen umfassen, einschließlich derjenigen, die kein Event hatten.
- **Methode:** Fügen Sie neue Snapshot-Datensätze zum Datensatz hinzu, anstatt vorherige Werte zu überschreiben. Dadurch bleibt der historische Zustand für das Modelltraining erhalten.

### Snapshot-Daten für die tägliche Zustellung abfragen {#query-snapshot-data-for-daily-delivery}

Decisioning Studio führt seine Empfehlungs-Pipeline einmal pro Tag aus. Wenn Sie Snapshot-Daten liefern, exportieren Sie bei jedem Pipeline-Lauf den Snapshot des Vortags:

```sql
SELECT *
FROM snapshot_data
WHERE snapshot_date = {t-1} -- on pipeline run date t, export the snapshot from t-1
```

## Event-Stream-Daten (Fluss) {#event-stream-data-flow}

Ein Event-Stream zeichnet diskrete Aktionen auf, sobald sie stattfinden. Er beantwortet die Frage: „Was hat diese geschäftskunden getan, und wann?“ Ein Event-Stream eignet sich ideal für rohe, unveränderliche, inkrementelle und chronologische Daten. Jeder Datensatz repräsentiert ein Ereignis, das zu einem bestimmten Zeitpunkt stattgefunden hat. Verwenden Sie diesen Datenstrom zum Beispiel für Aktivierungsdatensätze, Engagement-Protokolle (Öffnungen, Klicks), Konversions-Events oder Coupon-Einlösungen.

### Erforderliche Felder

| Feld | Zweck |
|------|-------|
| Kundenbezeichner | Auf wen sich dieses Event bezieht |
| Event-Typ | Was passiert ist (zum Beispiel Aktivierung, Conversion, Klick) |
| Event-Zeitstempel | Wann das Ereignis tatsächlich stattgefunden hat |
| Erstellungs-Zeitstempel | Wann dieser Datensatz in Ihrem System erstellt wurde (siehe Hinweis im folgenden Abschnitt) |
| Event-Eigenschaften | Zusätzliche Metadaten über das Event; je reichhaltiger diese sind, desto besser kann Decisioning Studio Events über die geschäftskunden Journey hinweg verknüpfen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erforderliche Felder" }

{% alert important %}
Der Event-Zeitstempel und der Erstellungs-Zeitstempel sind unterschiedliche Felder, und beide sind erforderlich. Der Event-Zeitstempel erfasst, wann die Aktion tatsächlich stattgefunden hat. Der Erstellungs-Zeitstempel erfasst, wann der Dateneintrag in Ihr System geschrieben wurde, was aufgrund von Verarbeitungsverzögerungen später sein kann. Verwechseln Sie die beiden nicht.
{% endalert %}

### Wie Event-Streams aktualisiert werden sollten {#how-event-streams-should-be-updated}

- **Auslöser:** Ereignisgesteuert. Neue Datensätze werden hinzugefügt, wenn neue Events auftreten.
- **Umfang:** Nur Kund:innen, die ein Event hatten, erhalten neue Datensätze.
- **Methode:** Bestehende Datensätze sind unveränderlich. Updates sind immer Einfügungen neuer Datensätze.

### Event-Daten für die tägliche Zustellung abfragen {#query-event-data-for-daily-delivery}

Verwenden Sie `create_timestamp`, nicht `event_timestamp`, um tägliche Exporte aufzuteilen. Events werden manchmal erst nach ihrem Auftreten in Ihr System geschrieben (verspätete Einträge). Wenn Sie nach `event_timestamp` aufteilen, werden diese verspätet eintreffenden Datensätze dauerhaft übersehen.

```sql
-- Correct: use create_timestamp to ensure late-arriving events are captured
SELECT *
FROM events_data
WHERE DATE(create_timestamp) = {t-1} -- on run date t, export all records created yesterday
```

```sql
-- Incorrect: slicing on event_timestamp will permanently lose late-arriving events
SELECT *
FROM events_data
WHERE DATE(event_timestamp) = {t-1}
```

Beispiel: Wenn ein Event am 1. Januar stattfand, aber erst am 2. Januar in Ihr System geschrieben wurde, würde eine Aufteilung nach `event_timestamp` am 2. Januar es vollständig übersehen. Eine Aufteilung nach `create_timestamp` erfasst es korrekt.

## Für native Braze-Integrationen {#for-native-braze-integrations}

Braze bietet zwei integrierte Mechanismen, die direkt diesen beiden Datentypen entsprechen.

### Angepasste Attribute: Snapshot-Daten {#custom-attributes-snapshot-data}

Angepasste Attribute speichern den Zustand auf Nutzer:innen-Ebene zu einem bestimmten Zeitpunkt. Sie sind das richtige Mittel für Kundenprofile und berechnete Features (zum Beispiel `churn_score`, `total_purchases_last_30d`). Sie sind **nicht** für rohe Event-Daten geeignet, da sie überschreiben statt zu akkumulieren.

### Braze-Currents: Event-Stream-Daten {#braze-currents-event-stream-data}

Braze-Currents liefert rohe, unveränderliche Event-Flussdaten. Die Tabelle `USER_BEHAVIOR_CUSTOM_EVENTS` erfasst jede Instanz eines angepassten Events, sobald es auftritt, und ist damit die richtige Quelle für Aktivierungs-, Engagement- und Konversions-Events.

{% alert tip %}
Behandeln Sie angepasste Attribute als Quelle des Kundenzustands und Braze-Currents als Quelle der Kundenverhalten-Events. Verwenden Sie keine angepassten Attribute, um rohe Event-Daten an Decisioning Studio zu übergeben.
{% endalert %}

## Häufige Probleme {#common-issues}

### Event-Daten als Snapshot übergeben {#pass-event-data-as-a-snapshot}

Das Aggregieren von Event-Daten in Snapshot-Felder vor dem Senden an Decisioning Studio verursacht mehrere Probleme:

- **Verlust der Granularität:** Sobald Daten auf eine tägliche Zusammenfassung auf Kund:innen-Ebene aggregiert sind, gehen die einzelnen Event-Datensätze verloren. Decisioning Studio kann sie nicht rekonstruieren.
- **Ungenaue Zeitstempel:** Ein Feld wie „last_email_sent“ zeigt Ihnen das letzte Vorkommen, verliert aber die vollständige Event-Historie und macht eine präzise Attribution unmöglich.
- **Phantom-Updates:** Selbst an Tagen, an denen keine Events aufgetreten sind, wird der Snapshot-Datensatz aktualisiert, wodurch doppelte Einträge entstehen, die schwer zu deduplizieren sind.

Wenn Sie Braze verwenden, nutzen Sie Currents-Exporte (nicht angepasste Attribute), um rohe Event-Daten an Decisioning Studio zu liefern.

### Snapshot-Daten bei einem Event-Auslöser aktualisieren {#update-snapshot-data-on-an-event-trigger}

Einige Implementierungen aktualisieren Snapshot-Daten nur dann, wenn ein Event auftritt – zum Beispiel wird ein Feature nur dann neu berechnet, wenn eine geschäftskunden einen Kauf tätigt. Dies führt dazu, dass Features, die vom Zeitverlauf abhängen, für Kund:innen veralten, die kein kürzliches Event hatten.

Beispiel: Ein Feature wie `days_since_last_purchase` hat jeden einzelnen Tag einen anderen korrekten Wert. Wenn es nur bei einem Kauf neu berechnet wird, bleibt es bei einem falschen Wert für alle Kund:innen eingefroren, die in letzter Zeit keinen Kauf getätigt haben. Aktualisieren Sie Snapshot-Daten immer nach einem zeitgesteuerten Zeitplan, der alle Kund:innen jeden Tag abdeckt.