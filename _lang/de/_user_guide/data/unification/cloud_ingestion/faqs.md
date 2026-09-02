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

## Warum habe ich eine E-Mail erhalten: „Fehler bei der CDI-Synchronisierung“? {#why-was-i-emailed-error-in-cdi-sync}

Diese Art von E-Mail bedeutet in der Regel, dass ein Problem mit Ihrer CDI-Einrichtung vorliegt. Hier sind einige häufige Probleme und wie Sie diese beheben können:

### CDI kann mit Ihren Zugangsdaten nicht auf das Data Warehouse oder die Tabelle zugreifen {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

Dies könnte bedeuten, dass die Zugangsdaten in CDI falsch sind oder im Data Warehouse fehlerhaft konfiguriert wurden. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

### Die Tabelle kann nicht gefunden werden {#the-table-cannot-be-found}

Versuchen Sie, Ihre Integration mit der korrekten Datenbankkonfiguration zu Update or aktualisieren or aktualisieren, oder erstellen Sie passende Ressourcen im Data Warehouse, z. B. `database/table`.

### Der Katalog kann nicht gefunden werden {#the-catalog-cannot-be-found}

Der in der Integration eingerichtete Katalog existiert nicht im Braze-Katalog. Ein Katalog kann nach der Einrichtung der Integration entfernt worden sein. Um das Problem zu beheben, Update or aktualisieren or aktualisieren Sie entweder die Integration, um einen anderen Katalog zu verwenden, oder erstellen Sie einen neuen Katalog, der dem Katalognamen in der Integration entspricht.

## Warum habe ich eine E-Mail erhalten: „Zeilenfehler in Ihrer CDI-Synchronisierung“? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

Diese Art von E-Mail bedeutet, dass einige Ihrer Daten während der Synchronisierung nicht verarbeitet werden konnten. Um den spezifischen Fehler herauszufinden, können Sie die Protokolle in Braze überprüfen, indem Sie zu **CDI** > **Sync Log** navigieren.

## Wie behebe ich den Fehler „Time must be string in ISO8601 Format“ bei der CDI-Einrichtung? {#how-do-i-fix-time-must-be-string-in-iso8601-format-in-cdi-setup}

Dieser Fehler bedeutet, dass der `time`-Wert des Ereignisses in Ihrem CDI-Payload nicht in einem unterstützten Datums-/Zeitformat vorliegt.

Formatieren Sie `time` für Ereignis- und Kauf-Payloads wie folgt:

- Als ISO-8601-String oder
- `yyyy-MM-dd'T'HH:mm:ss:SSSZ`

Wenn `time` nicht angegeben wird, verwendet Braze `UPDATED_AT` als Ereigniszeit.

Die vollständigen Payload-Anforderungen finden Sie unter [Tabelleneinrichtung für Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

## Wie behebe ich Fehler bei „Verbindung testen“ und Support-E-Mails? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### „Verbindung testen“ ist langsam {#test-connection-runs-slow}

„Verbindung testen“ wird in Ihrem Data Warehouse ausgeführt. Eine Erhöhung der Warehouse-Kapazität kann die Geschwindigkeit verbessern. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann jedoch zu etwas höheren Integrationskosten führen.

### Fehler beim Verbinden mit der Snowflake-Instanz: Eingehende Anfrage mit IP darf nicht auf Snowflake zugreifen {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

Versuchen Sie, die offiziellen Braze-IPs zu Ihrer IP-Zulassungsliste hinzuzufügen. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations), oder erlauben Sie die relevanten IPs:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Fehler beim Ausführen von SQL aufgrund der Kundenkonfiguration: 002003 (42S02): SQL-Kompilierungsfehler: existiert nicht oder nicht autorisiert {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

Wenn die Tabelle nicht existiert, erstellen Sie die Tabelle. Wenn die Tabelle existiert, überprüfen Sie, ob Nutzer:in und Rolle über Berechtigungen zum Lesen der Tabelle verfügen.

### Schema konnte nicht verwendet werden {#could-not-use-schema}

Wenn Sie diesen Fehler erhalten, gewähren Sie dem/der angegebenen Nutzer:in oder der Rolle Zugriff auf dieses Schema.

### Rolle konnte nicht verwendet werden {#could-not-use-role}

Wenn Sie diesen Fehler erhalten, erlauben Sie dem/der Nutzer:in die Verwendung der angegebenen Rolle.

### Nutzerzugriff deaktiviert {#user-access-disabled}

Wenn Sie diesen Fehler erhalten, erlauben Sie dem/der Nutzer:in den Zugriff auf Ihr Snowflake-Konto.

### Fehler beim Verbinden mit der Snowflake-Instanz mit aktuellem und altem Schlüssel {#error-connecting-to-snowflake-instance-with-current-and-old-key}

Wenn Sie diesen Fehler erhalten, stellen Sie sicher, dass der/die Nutzer:in den aktuellen Public Key verwendet, wie er in Ihrem Braze-Dashboard angezeigt wird.
{% endtab %}

{% tab Redshift %}
### „Verbindung testen“ ist langsam

„Verbindung testen“ wird in Ihrem Data Warehouse ausgeführt. Eine Erhöhung der Warehouse-Kapazität kann die Geschwindigkeit verbessern. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann jedoch zu etwas höheren Integrationskosten führen.

### Berechtigung für Relation {table_name} verweigert {#permission-denied-for-relation-table_name}

Wenn Sie diesen Fehler erhalten:

  - Gewähren Sie dem/der Nutzer:in die `usage`-Berechtigung für das Schema.
  - Gewähren Sie dem/der Nutzer:in die `select`-Berechtigung für die Tabelle.

### Fehler beim Erstellen der Verbindung {#create-connection-error}

Wenn Sie diesen Fehler erhalten, überprüfen Sie, ob der Redshift-Endpunkt und der Port korrekt sind.

### Fehler beim Erstellen des SSH-Tunnels {#create-ssh-tunnel-error}

Wenn Sie diesen Fehler erhalten:

  - Überprüfen Sie, ob der Public Key in Ihrem Braze-Dashboard auf dem EC2-Host vorhanden ist, der für das SSH-Tunneling verwendet wird.
  - Überprüfen Sie, ob Ihr Nutzername korrekt ist.
  - Überprüfen Sie, ob der SSH-Tunnel korrekt ist.
{% endtab %}

{% tab BigQuery %}
### „Verbindung testen“ ist langsam

„Verbindung testen“ wird in Ihrem Data Warehouse ausgeführt. Eine Erhöhung der Warehouse-Kapazität kann die Geschwindigkeit verbessern. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann jedoch zu etwas höheren Integrationskosten führen.

### Nutzer:in hat keine Berechtigung zum Abfragen der Tabelle {#user-does-not-have-permission-to-query-table}

Wenn Sie diesen Fehler erhalten, fügen Sie Nutzerberechtigungen zum Abfragen der Tabelle hinzu.

### Ihre Nutzung hat das benutzerdefinierte Kontingent überschritten {#your-usage-exceeded-the-custom-quota}

Wenn Sie diesen Fehler erhalten, muss Ihr Kontingent aktualisiert werden, damit Sie weiterhin mit Ihrer aktuellen Rate synchronisieren können.

### Tabelle wurde am Standort {region} nicht gefunden {#table-was-not-found-in-location-region-location}

Wenn Sie diesen Fehler erhalten, überprüfen Sie, ob sich Ihre Tabelle im richtigen Projekt und Datensatz befindet.

### Ungültige JWT-Signatur {#invalid-jwt-signature}

Wenn Sie diesen Fehler erhalten, überprüfen Sie, ob der BigQuery-API-Dienst für Ihr Konto aktiviert ist.
{% endtab %}

{% tab Databricks %}
### „Verbindung testen“ ist langsam

„Verbindung testen“ wird in Ihrem Data Warehouse ausgeführt. Eine Erhöhung der Warehouse-Kapazität kann die Geschwindigkeit verbessern. Bei Databricks kann es zwei bis fünf Minuten Aufwärmzeit geben, wenn Braze eine Verbindung zu Classic- und Pro-SQL-Instanzen herstellt, was zu Verzögerungen bei der Verbindungseinrichtung und beim Testen sowie zu Beginn geplanter Synchronisierungen führt. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann jedoch zu etwas höheren Integrationskosten führen.

### Befehl fehlgeschlagen, da das Warehouse gestoppt wurde {#command-failed-because-warehouse-was-stopped}

Wenn Sie diesen Fehler erhalten, stellen Sie sicher, dass das Databricks-Warehouse ausgeführt wird.

### Service: Amazon S3; Status Code: 403; Error Code: 403 Forbidden

Wenn Sie diesen Fehler erhalten, lesen Sie [Databricks: Forbidden error while accessing S3 data](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## Wie aktualisiere ich meine E-Mail-Benachrichtigungseinstellungen für CDI-Integrationen? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

Jede Integration hat ihre eigenen Benachrichtigungseinstellungen. Navigieren Sie zur CDI-Seite und wählen Sie den Namen der Integration aus, die Sie Update or aktualisieren or aktualisieren möchten. Im Abschnitt **Notification preferences** können Sie festlegen, wie Sie Benachrichtigungen zur ausgewählten Integration erhalten.

## Was passiert, wenn ein zukünftiger `UPDATED_AT`-Wert mit einer Integration synchronisiert wird? {#what-happens-if-a-future-updated_at-gets-synced-with-an-integration}

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Daten neu sind. Nachdem ein zukünftiger `UPDATED_AT`-Wert synchronisiert wurde, werden alle Daten vor diesem zukünftigen Datum und Zeitpunkt nicht verarbeitet. Um dies zu beheben:

1. Korrigieren Sie `UPDATED_AT`.
2. Entfernen Sie alle alten Daten, die bereits mit Braze synchronisiert wurden.
3. Erstellen Sie eine neue Integration, um diese Tabelle erneut zu verarbeiten.

## Warum stimmt „Synchronisierte Zeilen“ nicht mit der Anzahl in meinem Data Warehouse überein? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDI verwendet `UPDATED_AT`, um zu entscheiden, welche Datensätze während einer Synchronisierung abgerufen werden. Sehen Sie sich [diese Darstellung]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion#how-it-works) an, um zu verstehen, wie es funktioniert. Zu Beginn eines Synchronisierungslaufs fragt CDI Ihr Data Warehouse ab, um alle Datensätze mit einem `UPDATED_AT`-Wert abzurufen, der nach dem zuletzt verarbeiteten `UPDATED_AT`-Wert liegt. Datensätze am exakten Grenz-Zeitstempel können ebenfalls erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen. Jeder Datensatz, der zum Zeitpunkt der Abfrageausführung abgerufen wird, wird in Braze synchronisiert. Hier sind häufige Fälle, in denen ein Datensatz möglicherweise nicht synchronisiert wird:

- Sie fügen der Tabelle Datensätze mit einem `UPDATED_AT`-Wert hinzu, der bereits verarbeitet wurde.
- Sie Update or aktualisieren or aktualisieren Datensatzwerte, nachdem sie durch eine Synchronisierung verarbeitet wurden, lassen `UPDATED_AT` jedoch unverändert.
- Sie fügen Datensätze hinzu oder Update or aktualisieren or aktualisieren sie, während eine Synchronisierung läuft. Je nachdem, wann die CDI-Abfrage ausgeführt wird, können Race-Conditions auftreten, die dazu führen, dass Datensätze nicht abgerufen werden.

{% alert tip %}
Um dieses Verhalten in Zukunft zu vermeiden, empfehlen wir die Verwendung monoton steigender `UPDATED_AT`-Werte und keine Aktualisierung der Tabelle während Ihres geplanten Synchronisierungslaufs.
{% endalert %}

## Benötige ich überwiegend eindeutige `UPDATED_AT`-Werte für große CDI-Importe? {#do-i-need-mostly-distinct-updated_at-values-for-large-cdi-imports}

Ja. Stellen Sie bei Importen mit hohem Volumen (z. B. mehr als ca. 10 Millionen Zeilen) sicher, dass Ihre Quelldaten überwiegend eindeutige `UPDATED_AT`-Werte aufweisen. Wenn zu viele Zeilen denselben Zeitstempel haben, ist es wahrscheinlicher, dass CDI bei späteren Durchläufen Zeilen an Grenz-Zeitstempeln erneut auswählt. Dies kann zu vermehrten doppelten Synchronisierungen und einem höheren Datenpunktverbrauch führen.

Weitere Informationen zum Grenzverhalten von CDI finden Sie unter [Erneutes Synchronisieren von Zeilen mit doppelten Zeitstempeln vermeiden]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

### Wo führe ich diese SQL-Prüfungen aus? {#where-do-i-run-these-sql-checks}

Führen Sie die Prüfungen direkt im SQL-Editor Ihres Data Warehouse aus, gegen dieselbe Tabelle oder Ansicht, die von Ihrer CDI-Integration verwendet wird:

- Snowflake: **Projects** > **Worksheets** (weitere Informationen finden Sie unter [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs))
- Redshift: Query Editor v2 (weitere Informationen finden Sie unter [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html))
- BigQuery: BigQuery Studio SQL workspace (weitere Informationen finden Sie unter [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction))
- Databricks: SQL editor (SQL warehouse) (weitere Informationen finden Sie unter [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/))
- Fabric: SQL query editor

Verwenden Sie diesen Prozess, bevor Sie eine große Synchronisierung aktivieren oder skalieren:

1. Identifizieren Sie die genaue CDI-Quelltabelle oder -Ansicht und das Synchronisierungsfenster, das Sie validieren möchten.
2. Öffnen Sie den SQL-Editor Ihres Data Warehouse und wählen Sie dieselbe Datenbank und dasselbe Schema aus, die von CDI verwendet werden. Verwenden Sie dann eine Rolle mit Lesezugriff auf die Quelltabelle oder -Ansicht.
3. Führen Sie die Abfrage zur Zählung eindeutiger Zeitstempel aus, um zu messen, wie viele eindeutige `UPDATED_AT`-Werte in diesem Fenster vorhanden sind.
4. Führen Sie die Abfrage aus, die nach `UPDATED_AT` gruppiert und Zeilen zählt, um Zeitstempel mit ungewöhnlich hoher Zeilenanzahl zu finden.
5. Wenn viele Zeilen identische Zeitstempel haben, passen Sie Ihren Aufnahmeprozess so an, dass aufeinanderfolgende Batches fortlaufend neuere `UPDATED_AT`-Werte verwenden, oder erhöhen Sie die Zeitstempelpräzision, damit die Zeilen gleichmäßiger verteilt sind.
6. Führen Sie beide Abfragen erneut aus, bis die Konzentration reduziert ist, und starten oder skalieren Sie dann Ihre Synchronisierung.
7. Überwachen Sie nach dem Start unter **CDI** > **Sync Log** das Volumen unerwarteter erneuter Synchronisierungen an Grenz-Zeitstempeln.

Verwenden Sie Prüfungen wie diese in Ihrem Data Warehouse:

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

Wenn Ihr Data Warehouse `LIMIT` nicht unterstützt (z. B. Fabric), verwenden Sie eine gleichwertige Syntax wie `TOP`.

## Warum kann eine CDI-Synchronisierung mit einer kleinen Anzahl von Zeilen trotzdem mehrere Minuten dauern? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

Eine CDI-Synchronisierung umfasst eine feste Anlaufphase, bevor die Zeilenverarbeitung beginnt. Da diese Anlaufzeit bei allen Synchronisierungsgrößen ähnlich ist, kann eine kleine Synchronisierung trotzdem mehrere Minuten dauern und in Zeilen pro Minute langsamer erscheinen. Die Gesamtdauer der Synchronisierung hängt weiterhin von der Komplexität Ihrer Quellabfrage, der Datenstruktur und der verfügbaren Kapazität in Ihrem Data Warehouse ab. Weitere Informationen finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Wird bei einer Synchronisierung die Reihenfolge beibehalten, wenn mehrere Datensätze dieselbe ID haben? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

Die Verarbeitungsreihenfolge ist nicht zu 100 % vorhersagbar. Wenn beispielsweise während einer Synchronisierung mehrere Zeilen mit derselben `EXTERNAL_ID` in der Tabelle vorhanden sind, kann nicht garantiert werden, welcher Wert letztendlich im Profil landet. Wenn Sie dieselbe `EXTERNAL_ID` mit unterschiedlichen Attributen in der Payload-Spalte Update or aktualisieren or aktualisieren, werden alle Änderungen nach Abschluss der Synchronisierung übernommen.

## Warum werden durch meinen CDI-Sync keine neuen Nutzer:innen erstellt? {#why-are-new-users-not-being-created-from-my-cdi-sync}

Wenn in Ihrer CDI-Integration die Option **Nur bestehende Nutzer:innen Update or aktualisieren or aktualisieren** aktiviert ist, werden nur Nutzer:innen aktualisiert, die bereits in Braze vorhanden sind, und es werden keine neuen Nutzer:innen erstellt. Das bedeutet, dass eine Zeile in Ihrer Sync-Tabelle übersprungen wird, wenn sie eine `EXTERNAL_ID` referenziert, die keinem bestehenden Braze-Kundenprofil or Nutzerprofil entspricht.

Um neue Nutzer:innen über CDI zu erstellen, deaktivieren Sie den Schalter **Nur bestehende Nutzer:innen Update or aktualisieren or aktualisieren** in Ihren Integrationseinstellungen. Navigieren Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** und wählen Sie eine Integration aus.

## Welche Sicherheitsmaßnahmen gibt es für CDI? {#what-are-the-security-measures-for-cdi}

### Unsere Maßnahmen {#our-measures}

Braze hat die folgenden Maßnahmen für CDI implementiert:

- Alle Zugangsdaten werden in unserer Datenbank verschlüsselt gespeichert, und nur bestimmte Mitarbeitende haben authentifizierten Zugriff darauf.
- Wir verwenden verschlüsselte Verbindungen, um Daten an die Data Warehouses der Kund:innen zu übertragen.
- Wir senden Anfragen an die Braze-API-Endpunkte mit denselben API-Schlüsseln und TLS-Verbindungen, die wir auch unseren Kund:innen empfehlen.
- Wir Update or aktualisieren or aktualisieren regelmäßig unsere Bibliotheken und installieren alle Sicherheitspatches.

### Ihre Maßnahmen {#your-measures}

Wir empfehlen Ihnen und Ihrem Team, die folgenden Sicherheitsmaßnahmen auf Ihrer Seite einzurichten:

- Beschränken Sie den Zugriff auf Zugangsdaten auf das Minimum, das für den Betrieb von CDI erforderlich ist. Das liegt daran, dass wir in der Lage sein müssen, Select- (und Count-)Abfragen auf den jeweiligen Tabellen und Views auszuführen.
- Beschränken Sie die IPs, die auf die Tabellen zugreifen können, auf die offiziell veröffentlichten [Braze-IPs]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).