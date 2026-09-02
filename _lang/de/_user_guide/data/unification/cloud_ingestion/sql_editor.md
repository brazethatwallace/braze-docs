---
nav_title: SQL-Editor
article_title: "Cloud-Datenaufnahme: SQL-Editor"
description: "Erfahren Sie, wie Sie Cloud-Datenaufnahme-Synchronisierungen mit SQL-Anfragen erstellen und validieren."
page_order: 11
page_type: reference
toc_headers: h2
---

# Cloud-Datenaufnahme: SQL-Editor {#cloud-data-ingestion-sql-editor}

> Auf dieser Seite erfahren Sie, wie Sie den SQL-Editor der Braze Cloud-Datenaufnahme (CDI) verwenden, um Synchronisierungen mit SQL-Anfragen zu erstellen und zu validieren.

Der SQL-Editor der Cloud-Datenaufnahme ermöglicht es Ihnen, Synchronisierungen zu erstellen, indem Sie SQL-Anfragen direkt gegen Ihr Data Warehouse schreiben. Dadurch entfällt die Notwendigkeit, eine dedizierte CDI-Tabelle zu erstellen oder zu pflegen, was zuvor in [Schritt 1.1 der Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) erforderlich war.

Verwenden Sie den SQL-Editor, wenn Sie:

- Daten synchronisieren möchten, ohne vorgelagerte Tabellen zu ändern
- Mit Rohdaten in Ihrem Warehouse arbeiten möchten
- Die Erstellung einer `PAYLOAD`-Spalte vermeiden möchten
- Komplexere Datenanwendungsfälle mit SQL bearbeiten möchten

## Voraussetzungen und Einschränkungen {#prerequisites-and-limitations}

Der SQL-Editor hat die folgenden Einschränkungen:

- Nur für Data-Warehouse-Quellen verfügbar: Snowflake, Redshift, BigQuery, Databricks und Fabric.
- Es werden nur einzelne, schreibgeschützte Abfragen unterstützt.

{% alert note %}
Braze führt nur schreibgeschützte Abfragen gegen Ihre Daten aus und ändert Ihre zugrunde liegenden Tabellen nicht. Während der Abfrageausführung können temporäre Objekte erstellt werden, diese werden jedoch nicht dauerhaft gespeichert.
{% endalert %}

## Erstellen einer neuen SQL-Editor-Synchronisierung {#create-a-new-sql-editor-sync}

Folgen Sie diesen Schritten, um zuerst eine Quelle und dann eine Synchronisierung mit dem SQL-Editor zu erstellen. Wenn Sie bereits eine Quelle für CDI eingerichtet haben, können Sie direkt zu Schritt 3 springen.

{% alert note %}
Beachten Sie, dass in diesen Schritten eine Snowflake-Quelle als Beispiel verwendet wird. Der Einrichtungsprozess für andere Data-Warehouse-Quellen ist ähnlich und kann unter [Schritt 2: Neue Quelle im Braze-Dashboard erstellen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-2-create-a-new-source-in-the-braze-dashboard) in der Dokumentation [Data-Warehouse-Integrationen einrichten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations) nachgelesen werden.
{% endalert %}

### Schritt 1: Snowflake-Rolle, Berechtigungen, Warehouse und Nutzer:in einrichten {#step-1-set-up-your-snowflake-role-permissions-warehouse-and-user}

Bevor Sie Ihre Snowflake-Quelle in CDI erstellen, stellen Sie sicher, dass die Snowflake-Nutzer:in, die Braze verwendet, Zugriff auf die Daten hat, die Sie abfragen möchten, sowie auf ein Warehouse zum Ausführen von Anfragen.

#### Schritt 1.1: (Optional) Datenbank und Schema erstellen {#step-11-optional-create-a-database-and-schema}

Erstellen Sie bei Bedarf eine dedizierte Datenbank und ein Schema für Ihre CDI-Daten:

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### Schritt 1.2: Rolle und Datenbankberechtigungen einrichten {#step-12-set-up-role-and-database-permissions}

Gewähren Sie Zugriff auf die Tabellen, die Sie synchronisieren möchten:

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

Sie können je nach Anwendungsfall auch Zugriff auf mehrere oder zukünftige Tabellen gewähren. Um beispielsweise Zugriff auf alle zukünftigen Tabellen in einem Schema zu gewähren:

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### Schritt 1.3: Warehouse einrichten und Zugriff für die Braze-Rolle gewähren {#step-13-set-up-the-warehouse-and-grant-access-to-the-braze-role}

Erstellen Sie ein Warehouse, in dem Braze Anfragen ausführen kann:

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Das Warehouse muss das Auto-Resume-Flag aktiviert haben. Falls nicht, gewähren Sie Braze zusätzliche `OPERATE`-Berechtigungen für das Warehouse, damit Braze es einschalten kann, wenn die Anfrage ausgeführt wird.
{% endalert %}

#### Schritt 1.4: Snowflake-Nutzer:in erstellen {#step-14-create-a-snowflake-user}

Erstellen Sie eine Nutzer:in für Braze und weisen Sie die Rolle zu:

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Sie verwenden diese Nutzer:in, wenn Sie Ihre Snowflake-Quelle in Braze konfigurieren.

### Schritt 2: Neue Quelle im Braze-Dashboard erstellen {#step-2-create-a-new-source-in-the-braze-dashboard}

In diesem Schritt erstellen Sie Ihre Snowflake-Quelle in Braze und validieren die Verbindung.

#### Schritt 2.1: Snowflake-Quelle hinzufügen {#step-21-add-a-snowflake-source}

1. Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Quellen**.
2. Wählen Sie **Datenquelle hinzufügen**.
3. Wählen Sie **Snowflake**.

#### Schritt 2.2: Verbindungsdetails eingeben {#step-22-enter-connection-details}

Wählen Sie einen Namen für Ihre Quelle und geben Sie Ihre Snowflake-Zugangsdaten und -Konfiguration ein.

{% alert note %}
Geben Sie im Feld **Snowflake Account Locator** Ihren Snowflake-[Account-Bezeichner](https://docs.snowflake.com/en/user-guide/admin-account-identifier) ein, der typischerweise einem Format wie `xy12345.us-east-1.aws` folgt. Dies ist nicht dasselbe wie ein Datenbankname oder Warehouse-Name.
{% endalert %}

#### Schritt 2.3: RSA-Schlüssel-Einrichtung abschließen {#step-23-complete-rsa-key-setup}

Nachdem Sie Ihre Zugangsdaten und Konfiguration eingegeben haben, wählen Sie **Zugangsdaten speichern** und generieren Sie einen RSA-Schlüssel. Gehen Sie dann zurück zu Snowflake, um die Einrichtung abzuschließen. Fügen Sie den im Dashboard angezeigten Public Key der Nutzer:in hinzu, die Sie für die Verbindung von Braze mit Snowflake erstellt haben.

Weitere Informationen finden Sie unter [Snowflake-Schlüsselpaar-Authentifizierung](https://docs.snowflake.com/en/user-guide/key-pair-auth). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt rotieren möchten, kann Braze ein neues Schlüsselpaar generieren und den neuen Public Key bereitstellen.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

Wählen Sie in Braze **Verbindung testen**, um den Quellzugriff zu überprüfen, und erstellen Sie dann die Quelle.

### Schritt 3: Neue Synchronisierung erstellen und SQL-Anfrage schreiben {#step-3-create-a-new-sync-and-write-your-sql-query}

1. Gehen Sie zu **Dateneinstellungen** > **Cloud-Datenaufnahme** > **Synchronisierungen**.
2. Wählen Sie **Datensynchronisierung erstellen**.
3. Wählen Sie eine beliebige Synchronisierung unter **Datentyp**.
4. Referenzieren Sie die Quelle aus Schritt 2.
5. Wählen Sie **SQL** und schreiben Sie eine SQL-Anfrage, die Nutzerdaten aus Ihrem Warehouse zurückgibt. Ihre SQL-Anfrage definiert die Daten, die mit Braze synchronisiert werden. Das Abfrageergebnis wird zum Schema für Ihre Synchronisierung.

Sie können den Source Explorer verwenden, um verfügbare Tabellen und Views zum Synchronisieren zu durchsuchen, oder den KI or künstliche Intelligenz-SQL-Generator nutzen, um Hilfe von Braze Operator für Ihre SQL-Anfrage zu erhalten.

{% alert note %}
Es werden nur schreibgeschützte Anfragen unterstützt, einschließlich `JOIN`-Klauseln. Weitere Details finden Sie unter [SQL-Einschränkungen](#sql-constraints).
{% endalert %}

### Schritt 4: Vorschau anzeigen und Anfrage validieren {#step-4-preview-and-validate-your-query}

Wählen Sie **Vorschau und Validierung**, um Ihre Anfrage auszuführen.

Die Vorschau:

- Zeigt Ergebnisse im Tabellenformat an
- Zeigt bis zu 100 Zeilen an
- Zeigt bis zu 250 Spalten an

Für eine erfolgreiche Validierung muss Ihre SQL-Anfrage verschiedene erforderliche Spalten zurückgeben:

| Synchronisierungsdatentyp | Erforderliche Spalten |
|---|---|
| Attribute | - Ein Nutzerbezeichner, einer von `external_id`, `braze_id`, `alias_name` und `alias_label`, E-Mail oder Telefonnummer.<br>- `UPDATED_AT`.<br>- Mindestens eine zusätzliche Spalte (Attribut) zum Synchronisieren. |
| Nutzer:innen löschen | - Ein Nutzerbezeichner, einer von `external_id`, `braze_id`, `alias_name` und `alias_label`, E-Mail oder Telefonnummer.<br>- `UPDATED_AT`. |
| Canvas-Trigger or triggern | - Ein Nutzerbezeichner, einer von `external_id`, `braze_id`, `alias_name` und `alias_label`, E-Mail oder Telefonnummer.<br>- `UPDATED_AT`. |
| Angepasste Events | - Ein Nutzerbezeichner, einer von `external_id`, `braze_id`, `alias_name` und `alias_label`, E-Mail oder Telefonnummer.<br>- `UPDATED_AT`.<br>- `NAME` zur Darstellung des Event-Namens.<br>- `TIME` zur Darstellung der Event-Zeit. Falls nicht verfügbar, verwendet CDI `UPDATED_AT` als Ersatz. |
| Kauf-Events | - Ein Nutzerbezeichner, einer von `external_id`, `braze_id`, `alias_name` und `alias_label`, E-Mail oder Telefonnummer.<br>- `UPDATED_AT`.<br>- `PRODUCT_ID`.<br>- `CURRENCY`.<br>- `PRICE`.<br>- `TIME` zur Darstellung der Kauf-Event-Zeit. Falls nicht verfügbar, verwendet CDI `UPDATED_AT` als Ersatz. |
| Katalog | - `ID` zur Darstellung des Katalogartikels-Bezeichners.<br>- `UPDATED_AT`.<br>- Mindestens eine zusätzliche Spalte (Katalogfeld) zum Synchronisieren. |
| Konten | - `ID` zur Darstellung des Kontobezeichners.<br>- `NAME` zur Darstellung des Kontonamens.<br>- `UPDATED_AT`.<br>- Mindestens eine zusätzliche Spalte (Kontofeld) zum Synchronisieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4: Vorschau anzeigen und Anfrage validieren" }

Zusätzliche Spalten außerhalb der erforderlichen Spalten werden als Attribute, Canvas-Kontexteigenschaften, Event-Eigenschaften, Katalogfelder bzw. Kontofelder synchronisiert. Siehe [Validierungsverhalten](#validation-behavior) und [Fehlerbehebung](#troubleshooting) für hilfreiche Tipps zu Vorschau- und Validierungsfehlern und deren Behebung.

### Schritt 5: Attribut-Zuordnung überprüfen und Synchronisierung erstellen {#step-5-review-attribute-mapping-and-create-sync}

Wenn die Validierung erfolgreich ist, fahren Sie mit **Weiter: Benachrichtigungen** fort und erstellen Sie Ihre Synchronisierung.

{% alert important %}
Eine ungenaue SQL-Konfiguration kann zu unbeabsichtigten Ergebnissen führen, einschließlich eines übermäßigen Verbrauchs von Datenpunkten und umfassenderer betrieblicher Risiken. Sie sind dafür verantwortlich, dass Ihre Abfragelogik korrekt ist, und sollten alle Ergebnisse sorgfältig in der Vorschau prüfen, bevor Sie eine Synchronisierung aktivieren.
{% endalert %}

## SQL-Einschränkungen {#sql-constraints}

### Nur `SELECT`-Anfragen verwenden {#use-select-queries-only}

Es werden nur lesende Anfragen unterstützt.

Sie können verwenden:

- `SELECT`
- `WITH` (CTEs)
- `JOIN`

Sie können nicht verwenden:

- `INSERT`, `UPDATE` oder `DELETE`
- `CREATE` oder `DROP`
- Mehrere Anweisungen, getrennt durch `;`

### Eine einzelne Anweisung verwenden {#use-a-single-statement}

Ihre Anfrage muss eine einzelne ausführbare Anweisung sein.

## Validierungsverhalten {#validation-behavior}

Der SQL-Editor validiert Ihre Anfrage, bevor Sie fortfahren können.

### SQL-Fehler {#sql-errors}

Wenn Ihre Anfrage Syntaxfehler enthält:

- Die Validierung schlägt fehl
- Es wird keine Vorschau angezeigt
- Ihr Warehouse gibt eine Fehlermeldung zurück

### Kompilierungsfehler {#compilation-errors}

Wenn Ihre Anfrage auf ungültige Tabellen, Spalten oder nicht autorisierte Objekte verweist:

- Die Validierung schlägt fehl
- Es wird keine Vorschau angezeigt
- Ihr Warehouse gibt eine Fehlermeldung zurück

### Verbindungsfehler {#connection-errors}

Wenn Braze keine Verbindung zu Ihrem Warehouse herstellen kann:

- Die Validierung schlägt fehl
- Es wird keine Vorschau angezeigt
- Eine Verbindungsfehlermeldung wird angezeigt

### Anfrage-Timeout {#query-timeout}

Wenn Ihre Anfrage zu lange läuft:

- Braze beendet die Anfrage
- Die Validierung schlägt fehl
- Ein Timeout-Fehler wird angezeigt

### Tabellenschema-Fehler {#table-schema-errors}

Wenn Ihre Anfrage kompiliert wird, kann die Validierung dennoch fehlschlagen, wenn:

- Keine Bezeichner-Spalte gefunden wird
- `UPDATED_AT` fehlt
- Andere erforderliche Spalten fehlen

In diesem Fall wird die Vorschau dennoch angezeigt, um Ihnen bei einer erfolgreichen Validierung zu helfen. Details zu den erforderlichen Spalten für jeden Synchronisierungsdatentyp finden Sie unter [Schritt 4 im vorherigen Abschnitt](#step-4-preview-and-validate-your-query).

### Ergebnisse mit null Zeilen {#zero-row-results}

Wenn Ihre Anfrage null Zeilen zurückgibt:

- Die Validierung ist **erfolgreich**
- Sie können die Synchronisierung trotzdem erstellen
- Es werden keine Nutzer:innen aktualisiert, bis Zeilen zurückgegeben werden

## PAYLOAD-Unterstützung (Legacy) {#payload-support-legacy}

Der SQL-Editor unterstützt [Legacy-CDI-Tabellen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-1-set-up-tables-or-views), in denen eine `PAYLOAD`-Spalte vorhanden ist.

Wenn Ihre Abfrage Folgendes enthält:

- Einen gültigen Bezeichner
- `UPDATED_AT`
- Eine `PAYLOAD`-Spalte
- Zusätzliche Spalten

Dann gilt:

- Braze synchronisiert nur die `PAYLOAD`-Spalte
- Braze ignoriert zusätzliche Spalten

## SQL-Sync bearbeiten {#edit-a-sql-sync}

Beim Bearbeiten eines bestehenden Syncs:

- Jede SQL-Änderung erfordert eine erneute Validierung
- Ungültige Änderungen können nicht gespeichert werden
- Gültige Änderungen werden nach dem Speichern wirksam

Wenn bereits ein Sync-Lauf ausgeführt wird, werden Ihre Änderungen beim nächsten Lauf wirksam.

## Fehlerbehebung {#troubleshooting}

Dieser Abschnitt enthält häufige Fehler und Hinweise zur Fehlerbehebung.

### Keine Vorschau verfügbar {#no-preview-available}

Wenn „Keine Vorschau verfügbar“ angezeigt wird, kann einer der folgenden zugrunde liegenden Fehlertypen die Ursache sein.

| Fehlertyp | Schritte zur Behebung |
|---|---|
| „Keine Vorschau verfügbar“ | Lesen Sie das Fehlerbanner für Hinweise. |
| „Verbindung zur Quelle nicht möglich“ | Überprüfen Sie den konfigurierten Nutzernamen, den Account Locator und die RSA-Schlüsselpaar-Authentifizierungseinrichtung.<br>Stellen Sie sicher, dass das Warehouse läuft.<br>Bestätigen Sie den Netzwerkzugriff. |
| „SQL-Syntaxfehler“ | Überprüfen Sie Ihre SQL-Syntax. |
| „Objekt existiert nicht oder nicht autorisiert“ | Stellen Sie sicher, dass die Rolle `SELECT`-Zugriff auf die Tabelle hat.<br>Bestätigen Sie die Datenbank- und Schemaberechtigungen.<br>Überprüfen Sie Tippfehler im Tabellennamen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Keine Vorschau verfügbar" }

### Bezeichner-Spalte erforderlich {#identity-column-required}

Stellen Sie sicher, dass Ihre Anfrage einen gültigen Bezeichner enthält, wie z. B. `external_id`.

### `UPDATED_AT`-Spalte fehlt {#updated_at-column-is-missing}

Fügen Sie eine Zeitstempel-Spalte für die inkrementelle Synchronisierung hinzu.

### Weitere Spalten hinzufügen … Es sind keine Attribute/Katalogfelder/Kontofelder zum Synchronisieren vorhanden {#add-more-columns-there-are-no-attributescatalog-fieldsaccount-fields-to-sync}

Fügen Sie mindestens eine zusätzliche Spalte neben dem Bezeichner und `UPDATED_AT` hinzu.

### Anfrageausführung hat das Zeitlimit überschritten {#query-execution-timed-out}

Optimieren Sie Ihre Anfrage oder verwenden Sie ein größeres Warehouse.