---
nav_title: FAQ
article_title: FAQ zur Cloud-Datenaufnahme
page_order: 10
page_type: FAQ
description: "Diese Seite beantwortet häufig gestellte Fragen zur Cloud-Datenaufnahme."
toc_headers: h2
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zur Cloud-Datenaufnahme.

## Warum habe ich eine E-Mail erhalten: „Error in CDI Sync“? {#why-was-i-emailed-error-in-cdi-sync}

Diese Art von E-Mail bedeutet normalerweise, dass es ein Problem mit Ihrer CDI-Einrichtung gibt. Hier sind einige häufige Probleme und wie Sie sie beheben können:

### CDI kann mit Ihren Zugangsdaten nicht auf das Data Warehouse oder die Tabelle zugreifen {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

Dies könnte bedeuten, dass die Zugangsdaten in CDI falsch sind oder im Data Warehouse falsch konfiguriert wurden. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

### Die Tabelle kann nicht gefunden werden {#the-table-cannot-be-found}

Versuchen Sie, Ihre Integration mit der richtigen Datenbankkonfiguration zu aktualisieren, oder erstellen Sie passende Ressourcen im Data Warehouse, z. B. `database/table`.

### Der Katalog kann nicht gefunden werden {#the-catalog-cannot-be-found}

Der in der Integration eingerichtete Katalog ist im Braze-Katalog nicht vorhanden. Ein Katalog kann entfernt werden, nachdem die Integration eingerichtet wurde. Um das Problem zu beheben, aktualisieren Sie entweder die Integration, um einen anderen Katalog zu verwenden, oder erstellen Sie einen neuen Katalog, der dem Katalognamen in der Integration entspricht.

## Warum habe ich eine E-Mail erhalten: „Row errors in your CDI sync“? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

Diese Art von E-Mail bedeutet, dass einige Ihrer Daten während der Synchronisierung nicht verarbeitet werden konnten. Um den spezifischen Fehler herauszufinden, können Sie die Protokolle in Braze einsehen, indem Sie zu **CDI** > **Sync Log** gehen.

## Wie behebe ich Fehler bei Test Connection und Support-E-Mails? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### Test Connection läuft langsam {#test-connection-runs-slow}

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Fehler bei der Verbindung zur Snowflake-Instanz: Eingehende Anfrage mit IP ist für den Zugriff auf Snowflake nicht zulässig {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Versuchen Sie, die offiziellen Braze-IPs zu Ihrer IP-Zulassungsliste hinzuzufügen. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/), oder erlauben Sie die entsprechenden IPs:

{% multi_lang_include data_centers.md datacenters='ips' %}

### Fehler bei der Ausführung von SQL aufgrund der Kund:innen-Konfiguration: 002003 (42S02): SQL-Kompilierungsfehler: existiert nicht oder ist nicht autorisiert {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

Wenn die Tabelle nicht existiert, erstellen Sie die Tabelle. Wenn die Tabelle existiert, überprüfen Sie, ob Nutzer:in und Rolle die Berechtigung haben, aus der Tabelle zu lesen.

### Schema konnte nicht verwendet werden {#could-not-use-schema}

Wenn Sie diesen Fehler erhalten, gewähren Sie der angegebenen Nutzer:in oder Rolle Zugriff auf dieses Schema.

### Rolle konnte nicht verwendet werden {#could-not-use-role}

Wenn Sie diese Fehlermeldung erhalten, erlauben Sie der Nutzer:in, die angegebene Rolle zu verwenden.

### Nutzer:innen-Zugriff deaktiviert {#user-access-disabled}

Wenn Sie diesen Fehler erhalten, erlauben Sie der Nutzer:in den Zugriff auf Ihr Snowflake-Konto.

### Fehler bei der Verbindung zur Snowflake-Instanz mit aktuellem und altem Schlüssel {#error-connecting-to-snowflake-instance-with-current-and-old-key}

Wenn Sie diese Fehlermeldung erhalten, vergewissern Sie sich, dass die Nutzer:in den aktuellen Public Key verwendet, der in Ihrem Braze-Dashboard angezeigt wird.
{% endtab %}

{% tab Redshift %}
### Test Connection läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Zugriff auf die Relation verweigert {table_name} {#permission-denied-for-relation-tablename}

Wenn Sie diesen Fehler erhalten:

  - Erteilen Sie der Nutzer:in die Berechtigung `usage` für das Schema.
  - Erteilen Sie der Nutzer:in die Berechtigung `select` für die Tabelle.

### Fehler beim Erstellen der Verbindung {#create-connection-error}

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob der Redshift-Endpunkt und der Port korrekt sind.

### Fehler beim Erstellen des SSH-Tunnels {#create-ssh-tunnel-error}

Wenn Sie diesen Fehler erhalten:

  - Überprüfen Sie, ob der Public Key in Ihrem Braze-Dashboard auf dem für das SSH-Tunneling verwendeten EC2-Host vorhanden ist.
  - Überprüfen Sie, ob Ihr Benutzername korrekt ist.
  - Überprüfen Sie, ob der SSH-Tunnel korrekt ist.
{% endtab %}

{% tab BigQuery %}
### Test Connection läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Nutzer:in hat keine Berechtigung, die Tabelle abzufragen {#user-does-not-have-permission-to-query-table}

Wenn Sie diesen Fehler erhalten, fügen Sie der Nutzer:in die Berechtigung zur Abfrage der Tabelle hinzu.

### Ihre Nutzung hat das angepasste Kontingent überschritten {#your-usage-exceeded-the-custom-quota}

Wenn Sie diese Fehlermeldung erhalten, muss Ihr Kontingent aktualisiert werden, damit Sie die Synchronisierung mit Ihrer aktuellen Rate fortsetzen können.

### Tabelle wurde am Standort {region} nicht gefunden {#table-was-not-found-in-location-region-location}

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob sich Ihre Tabelle im richtigen Projekt und Datensatz befindet.

### Ungültige JWT-Signatur {#invalid-jwt-signature}

Wenn Sie diese Fehlermeldung erhalten, überprüfen Sie, ob der BigQuery-API-Dienst für Ihr Konto aktiviert ist.
{% endtab %}

{% tab Databricks %}
### Test Connection läuft langsam

Test Connection läuft auf Ihrem Data Warehouse, sodass eine Erhöhung der Data-Warehouse-Kapazität die Geschwindigkeit verbessern kann. Bei Databricks kann es zu einer Aufwärmzeit von zwei bis fünf Minuten kommen, wenn Braze eine Verbindung zu Classic- und Pro-SQL-Instanzen herstellt, was zu Verzögerungen beim Verbindungsaufbau und beim Testen sowie zu Beginn geplanter Synchronisierungen führt. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.

### Befehl fehlgeschlagen, da das Warehouse gestoppt wurde {#command-failed-because-warehouse-was-stopped}

Wenn Sie diese Fehlermeldung erhalten, stellen Sie sicher, dass das Databricks-Warehouse läuft.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden {#service-amazon-s3-status-code-403-error-code-403-forbidden}

Wenn Sie diesen Fehler erhalten, lesen Sie [Databricks: Forbidden-Fehler beim Zugriff auf S3-Daten](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Wie aktualisiere ich meine E-Mail-Benachrichtigungseinstellungen für CDI-Integrationen? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

Jede Integration hat ihre eigene Benachrichtigungspräferenz. Gehen Sie auf die CDI-Seite und wählen Sie den Namen der Integration aus, die Sie aktualisieren möchten. Im Abschnitt **Notification preferences** können Sie festlegen, wie Sie Benachrichtigungen über die ausgewählte Integration erhalten.

## Was passiert, wenn ein zukünftiger `UPDATED_AT`-Wert mit einer Integration synchronisiert wird? {#what-happens-if-a-future-updatedat-gets-synced-with-an-integration}

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Daten neu sind. Nachdem ein zukünftiger `UPDATED_AT`-Wert synchronisiert wurde, werden Daten, die vor diesem zukünftigen Datum und Zeitpunkt liegen, nicht mehr verarbeitet. Um dies zu beheben:

1. Korrigieren Sie `UPDATED_AT`.
2. Entfernen Sie alle alten Daten, die bereits mit Braze synchronisiert wurden.
3. Erstellen Sie eine neue Integration, um diese Tabelle erneut zu verarbeiten.

## Warum stimmt „Rows Synced“ nicht mit der Anzahl in meinem Warehouse überein? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Datensätze bei einer Synchronisierung übernommen werden sollen. Sehen Sie sich [diese Illustration]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/#what-gets-synced) an, um zu verstehen, wie es funktioniert. Zu Beginn eines Synchronisierungslaufs fragt CDI Ihr Warehouse ab, um alle Datensätze zu erhalten, deren `UPDATED_AT`-Zeitstempel später als der zuvor verarbeitete `UPDATED_AT`-Wert ist. Datensätze an der exakten Grenz-Zeitstempel-Marke können ebenfalls erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel haben. Jeder Datensatz, der zum Zeitpunkt der Abfrageausführung erfasst wird, wird mit Braze synchronisiert. Hier sind häufige Fälle, in denen ein Datensatz möglicherweise nicht synchronisiert wird:

- Sie fügen der Tabelle Datensätze mit einem `UPDATED_AT`-Wert hinzu, der bereits verarbeitet wurde.
- Sie aktualisieren Datensatzwerte, nachdem sie durch eine Synchronisierung verarbeitet wurden, lassen aber `UPDATED_AT` unverändert.
- Sie fügen Datensätze hinzu oder aktualisieren sie, während eine Synchronisierung läuft. Je nachdem, wann die CDI-Abfrage ausgeführt wird, kann es zu Race-Conditions kommen, die dazu führen, dass Datensätze nicht erfasst werden.

{% alert tip %}
Um dieses Verhalten in Zukunft zu vermeiden, empfehlen wir, monoton ansteigende `UPDATED_AT`-Werte zu verwenden und die Tabelle während Ihres geplanten Synchronisierungslaufs nicht zu aktualisieren.
{% endalert %}

## Benötige ich überwiegend eindeutige `UPDATED_AT`-Werte für große CDI-Importe? {#do-i-need-mostly-distinct-updatedat-values-for-large-cdi-imports}

Ja. Bei Läufen mit hohem Volumen (z. B. mehr als ca. 10 Millionen Zeilen) sollten Sie sicherstellen, dass Ihre Quelldaten überwiegend eindeutige `UPDATED_AT`-Werte aufweisen. Wenn zu viele Zeilen denselben Zeitstempel haben, ist es wahrscheinlicher, dass CDI Zeilen an Grenz-Zeitstempeln in späteren Läufen erneut auswählt. Dies kann zu doppelten Synchronisierungen und einem erhöhten Datenpunktverbrauch führen.

Weitere Informationen zum CDI-Grenzverhalten finden Sie unter [Erneutes Synchronisieren von Zeilen mit doppelten Zeitstempeln vermeiden]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps).

### Wo führe ich diese SQL-Prüfungen aus? {#where-do-i-run-these-sql-checks}

Führen Sie die Prüfungen direkt im SQL-Editor Ihres Data Warehouse aus, gegen dieselbe Tabelle oder View, die von Ihrer CDI-Integration verwendet wird:

- Snowflake: **Projects** > **Worksheets** (weitere Informationen finden Sie unter [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs))
- Redshift: Query Editor v2 (weitere Informationen finden Sie unter [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html))
- BigQuery: BigQuery Studio SQL Workspace (weitere Informationen finden Sie unter [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction))
- Databricks: SQL-Editor (SQL Warehouse) (weitere Informationen finden Sie unter [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/))
- Fabric: SQL-Abfrage-Editor

Verwenden Sie diesen Prozess, bevor Sie eine große Synchronisierung aktivieren oder skalieren:

1. Identifizieren Sie die genaue CDI-Quelltabelle oder -View und das Synchronisierungsfenster, das Sie validieren möchten.
2. Öffnen Sie den SQL-Editor Ihres Warehouse und wählen Sie dieselbe Datenbank und dasselbe Schema aus, die von CDI verwendet werden. Verwenden Sie dann eine Rolle mit Lesezugriff auf die Quelltabelle oder -View.
3. Führen Sie die Abfrage zur Zählung eindeutiger Zeitstempel aus, um zu messen, wie viele eindeutige `UPDATED_AT`-Werte in diesem Fenster vorhanden sind.
4. Führen Sie die Abfrage aus, die nach `UPDATED_AT` gruppiert und Zeilen zählt, um Zeitstempel mit ungewöhnlich hoher Zeilenanzahl zu finden.
5. Wenn viele Zeilen identische Zeitstempel haben, passen Sie Ihren Aufnahmeprozess so an, dass aufeinanderfolgende Batches progressiv neuere `UPDATED_AT`-Werte verwenden, oder erhöhen Sie die Zeitstempel-Präzision, damit die Zeilen besser verteilt sind.
6. Führen Sie beide Abfragen erneut aus, bis die Konzentration reduziert ist, und starten oder skalieren Sie dann Ihre Synchronisierung.
7. Überwachen Sie nach dem Start unter **CDI** > **Sync Log** das unerwartete Volumen erneuter Synchronisierungen an Grenz-Zeitstempeln.

Verwenden Sie Prüfungen wie diese in Ihrem Warehouse:

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT UPDATED_AT) AS distinct_timestamps,
  ROUND(COUNT(*) * 1.0 / NULLIF(COUNT(DISTINCT UPDATED_AT), 0), 2) AS avg_rows_per_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP);
```

```sql
SELECT
  UPDATED_AT,
  COUNT(*) AS rows_at_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP)
GROUP BY UPDATED_AT
ORDER BY rows_at_timestamp DESC
LIMIT 20;
```

Wenn Ihr Warehouse `LIMIT` nicht unterstützt (z. B. Fabric), verwenden Sie eine äquivalente Syntax wie `TOP`.

## Warum kann eine CDI-Synchronisierung mit einer kleinen Zeilenanzahl trotzdem mehrere Minuten dauern? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

Eine CDI-Synchronisierung umfasst eine feste Anlaufphase, bevor die Zeilenverarbeitung beginnt. Da diese Anlaufzeit bei allen Synchronisierungsgrößen ähnlich ist, kann eine kleine Synchronisierung trotzdem mehrere Minuten dauern und in Zeilen pro Minute langsamer erscheinen. Die gesamte Synchronisierungszeit hängt weiterhin von der Komplexität Ihrer Quellabfrage, der Datenstruktur und der verfügbaren Kapazität in Ihrem Data Warehouse ab. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).

## Wird bei einer Synchronisierung die Reihenfolge beibehalten, wenn mehrere Datensätze dieselbe ID haben? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

Die Verarbeitungsreihenfolge ist nicht zu 100 % vorhersehbar. Wenn zum Beispiel während einer Synchronisierung mehrere Zeilen mit derselben `EXTERNAL_ID` in der Tabelle vorhanden sind, können wir nicht garantieren, welcher Wert im endgültigen Profil landet. Wenn Sie dieselbe `EXTERNAL_ID` mit verschiedenen Attributen in der Nutzlastspalte aktualisieren, werden alle Änderungen übernommen, wenn die Synchronisierung abgeschlossen ist.

## Warum werden bei meiner CDI-Synchronisierung keine neuen Nutzer:innen angelegt? {#why-are-new-users-not-being-created-from-my-cdi-sync}

Wenn in Ihrer CDI-Integration die Option **Update existing users only** aktiviert ist, werden nur Nutzer:innen aktualisiert, die bereits in Braze vorhanden sind, und es werden keine neuen Nutzer:innen erstellt. Das bedeutet, dass eine Zeile in Ihrer Synchronisierungstabelle, die eine `EXTERNAL_ID` referenziert, die mit keiner vorhandenen Braze-Nutzer:in übereinstimmt, übersprungen wird.

Um über CDI neue Nutzer:innen anzulegen, deaktivieren Sie die Option **Update existing users only** in Ihren Integrationseinstellungen. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** und wählen Sie eine Integration aus.

## Welche Sicherheitsmaßnahmen gibt es für CDI? {#what-are-the-security-measures-for-cdi}

### Unsere Maßnahmen {#our-measures}

Braze hat die folgenden Maßnahmen für CDI implementiert:

- Alle Zugangsdaten werden in unserer Datenbank verschlüsselt, und nur bestimmte Mitarbeitende haben authentifizierten Zugang zu ihnen.
- Wir verwenden verschlüsselte Verbindungen, um Daten aus Kund:innen-Warehouses abzurufen.
- Wir stellen Anfragen an die Braze-API-Endpunkte mit denselben API-Schlüsseln und TLS-Verbindungen, die wir unseren Kund:innen empfehlen.
- Wir aktualisieren unsere Bibliotheken regelmäßig und beziehen alle Sicherheits-Patches.

### Ihre Maßnahmen {#your-measures}

Wir empfehlen Ihnen und Ihrem Team, die folgenden Sicherheitsmaßnahmen auf Ihrer Seite einzurichten:

- Beschränken Sie den Zugriff auf Zugangsdaten auf das für den Betrieb von CDI erforderliche Minimum. Das liegt daran, dass wir in der Lage sein müssen, select (und count) auf den spezifischen Tabellen und Views auszuführen.
- Beschränken Sie die IPs, die auf die Tabellen zugreifen können, auf offiziell veröffentlichte [Braze-IPs]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).