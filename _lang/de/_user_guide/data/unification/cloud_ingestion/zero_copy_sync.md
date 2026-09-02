---
nav_title: Zero-Copy-Personalisierung
article_title: Zero-Copy-Personalisierung mit CDI
page_order: 7
page_type: reference
description: "Diese Seite bietet eine Übersicht darüber, wie Sie Braze-Canvases mithilfe von CDI triggern können."
---

# Zero-Copy-Personalisierung mit CDI {#zero-copy-personalization-using-cdi}

> Erfahren Sie, wie Sie Canvas-Trigger mithilfe von CDI für eine Zero-Copy-Personalisierung synchronisieren können. Dieses Feature greift auf nutzerspezifische Informationen aus Ihrer Datenspeicher-Lösung zu und überträgt diese an einen Ziel-Canvas. Canvas-Schritte können optional Personalisierungsfelder enthalten, die nicht in Braze-Nutzerprofilen persistent gespeichert werden.

## Canvas-Trigger synchronisieren {#syncing-canvas-triggers}

### Schnellstart-Schritte {#quick-start-steps}

Falls Sie bereits mit Braze CDI vertraut sind, beachten Sie bitte, dass die Einrichtung einer Canvas-Trigger-Synchronisierung weitgehend dem Prozess für [CDI-Integrationen von Nutzerdaten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) entspricht, mit folgenden Einschränkungen:

- Es werden ausschließlich externe IDs oder Nutzer-Alias-Bezeichner unterstützt. E-Mail-Adressen und Telefonnummern werden nicht als Bezeichner unterstützt.
- Es können nur bestehende Braze-Nutzer:innen synchronisiert werden. Neue Nutzer:innen können nicht angelegt werden.
- `properties` ersetzt die Spalte `payload`. Dies ist ein JSON-String der Felder, die Sie als Canvas-Eingangs-Eigenschaften für die Personalisierung verwenden möchten.

Um zu beginnen, wählen Sie beim Erstellen einer neuen Synchronisierung den Datentyp **Canvas Triggers** aus.

### Verwendung von Canvas-Triggern {#using-canvas-triggers}

#### 1. Schritt: Datenquelle für Canvas-Trigger einrichten {#step-1-set-up-data-source-for-canvas-triggers}

{% tabs %}
{% tab Snowflake %}

##### Schritt 1.1: Quelltabelle in Snowflake einrichten {#step-11-set-up-your-source-table-in-snowflake}

Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine View oder eine Materialized View anstelle einer Tabelle verwenden.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

Sie können die Datenbank, das Schema und die Tabelle nach Ihren Wünschen benennen, jedoch sollten die Spaltennamen mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt, zu dem diese Zeile aktualisiert oder zur Tabelle hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt dem Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
* Entweder `external_id` oder `alias_name` und `alias_label` als Spalte für den Bezeichner der Nutzer:innen. Diese identifizieren die Nutzer:innen, für die Sie Canvas-Messaging triggern möchten.
  * `EXTERNAL_ID`: Identifiziert die Nutzer:in, die in den Canvas eintreten soll. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen.
  * `ALIAS_NAME` und `ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Alias-Typ an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen alias_name pro `alias_label`.
* `PROPERTIES`: Ein JSON-String mit Feldern, die als Personalisierungs-Eigenschaften in Ihrem Canvas verfügbar gemacht werden sollen. Dieser sollte nutzerspezifische Informationen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jede Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch ein gültiger JSON-String sein. Geben Sie einen leeren `{}`-String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
{% endalert %}

##### Schritt 1.2: Zugangsdaten einrichten {#step-12-set-up-credentials}

Richten Sie eine Rolle, ein Warehouse und eine Nutzer:in ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits Zugangsdaten aus einer bestehenden Synchronisierung haben, können Sie diese wiederverwenden. Stellen Sie jedoch sicher, dass Sie den Zugriff auf die Quelltabelle der Canvas-Trigger erweitern.

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### Schritt 1.3: Netzwerkrichtlinien konfigurieren {#step-13-configure-network-policies}

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Allowlist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).

{% endtab %}
{% tab Redshift %}

##### Schritt 1.1: Quelltabelle in Redshift einrichten {#step-11-set-up-your-source-table-in-redshift}

Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine View oder eine Materialized View anstelle einer Tabelle verwenden.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

Sie können die Datenbank, das Schema und die Tabelle nach Ihren Wünschen benennen, jedoch sollten die Spaltennamen mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt, zu dem diese Zeile aktualisiert oder zur Tabelle hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt dem Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
* Entweder `external_id` oder `alias_name` und `alias_label` als Spalte für den Bezeichner der Nutzer:innen. Diese identifizieren die Nutzer:innen, für die Sie Canvas-Messaging triggern möchten.
  * `EXTERNAL_ID`: Identifiziert die Nutzer:in, die in den Canvas eintreten soll. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen.
  * `ALIAS_NAME` und `ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Alias-Typ an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
* `PROPERTIES`: Ein JSON-String mit Feldern, die als Personalisierungs-Eigenschaften in Ihrem Canvas verfügbar gemacht werden sollen. Dieser sollte nutzerspezifische Informationen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jede Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch ein gültiger JSON-String sein. Geben Sie einen leeren `{}`-String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
{% endalert %}

##### Schritt 1.2: Zugangsdaten einrichten

Richten Sie eine Rolle, ein Warehouse und eine Nutzer:in ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits Zugangsdaten aus einer bestehenden Synchronisierung haben, können Sie diese wiederverwenden. Stellen Sie jedoch sicher, dass Sie den Zugriff auf die Quelltabelle der Canvas-Trigger erweitern.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### Schritt 1.3: Netzwerkrichtlinien konfigurieren

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Allowlist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=redshift#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab BigQuery %}

##### Schritt 1.1: Neues Projekt oder neuen Datensatz für Ihre Quelltabelle erstellen (optional) {#step-11-create-a-new-project-or-dataset-for-your-source-table-optional}

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### Schritt 1.2: Quelltabelle in BigQuery einrichten {#step-12-set-up-your-source-table-in-bigquery}
Beachten Sie beim Erstellen Ihrer Quelltabelle Folgendes:

| Feldname | Typ | Erforderlich? |
| :---- | :---- | :---- |
| **`UPDATED_AT`** | Timestamp | Ja |
| **`PROPERTIES`** | JSON | Ja |
| **`EXTERNAL_ID`** | STRING | NULLABLE |
| **`ALIAS_NAME`** | STRING | NULLABLE |
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1.2: Quelltabelle in BigQuery einrichten" }

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jede Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch ein gültiger JSON-String sein. Geben Sie einen leeren `{}`-String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### Schritt 1.3: Zugangsdaten einrichten {#step-13-set-up-credentials}

Erstellen Sie eine Nutzer:in und erteilen Sie Berechtigungen. Sollten Sie bereits Zugangsdaten aus einer anderen Synchronisierung besitzen, können Sie diese wiederverwenden, sofern sie Zugriff auf die Canvas-Trigger-Tabelle haben.

| Berechtigung | Zweck |
| :---- | :---- |
| BigQuery Connection User | Ermöglicht Braze die Verbindungsherstellung. |
| BigQuery User | Ermöglicht Braze, Abfragen auszuführen, Metadaten zu lesen und Tabellen aufzulisten. |
| BigQuery Data Viewer | Ermöglicht Braze, Datensätze und Inhalte einzusehen. |
| BigQuery Job User | Ermöglicht Braze, Jobs auszuführen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1.3: Zugangsdaten einrichten" }

Generieren Sie nach der Erteilung der Berechtigungen einen JSON-Schlüssel. Anweisungen finden Sie unter [Schlüssel erstellen und löschen](https://cloud.google.com/iam/docs/keys-create-delete). Sie laden ihn später im Braze-Dashboard hoch.

##### Schritt 1.4: Netzwerkrichtlinien konfigurieren {#step-14-configure-network-policies}
Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Allowlist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=bigquery#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Databricks %}

##### Schritt 1.1: Katalog oder Schema für Ihre Quelltabelle erstellen {#step-11-create-a-catalog-or-schema-for-your-source-table}

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### Schritt 1.2: Quelltabelle in Databricks einrichten {#step-12-set-up-your-source-table-in-databricks}

Beachten Sie beim Erstellen Ihrer Quelltabelle Folgendes:

| Feldname | Typ | Erforderlich |
| :---- | :---- | :---- |
| `UPDATED_AT` | Timestamp | Ja |
| `PROPERTIES` | JSON | Ja |
| `EXTERNAL_ID` | STRING | NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1.2: Quelltabelle in Databricks einrichten" }

Sie können das Schema und die Tabelle nach Belieben benennen, jedoch sollten die Spaltennamen mit der vorangegangenen Definition übereinstimmen.

* `UPDATED_AT`: Der Zeitpunkt, zu dem diese Zeile aktualisiert oder zur Tabelle hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen mit exakt dem Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.
* Entweder `external_id` oder `alias_name` und `alias_label` als Spalte für den Bezeichner der Nutzer:innen. Diese identifizieren die Nutzer:innen, für die Sie Canvas-Messaging triggern möchten.
  * `EXTERNAL_ID`: Identifiziert die Nutzer:in, die in den Canvas eintreten soll. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen.
  * `ALIAS_NAME` und `ALIAS_LABEL`: Diese Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Alias-Typ an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen alias_name pro `alias_label`.
* `PROPERTIES`: Ein String oder eine Struktur von Feldern, die als Personalisierungs-Eigenschaften in Ihrem Canvas verfügbar gemacht werden sollen. Dieser sollte nutzerspezifische Informationen enthalten.

{% alert note %}
Eigenschaften sind nicht für jede Zeile oder jede Nutzer:in erforderlich. Die Eigenschaftswerte müssen jedoch gültige JSON-Strings sein. Geben Sie einen leeren `{}`-String ein, wenn für die Zeile keine Eigenschaften vorhanden sind.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### Schritt 1.3: Zugangsdaten einrichten

Erstellen Sie ein persönliches Zugriffstoken in Databricks:

1. Wählen Sie Ihren Benutzernamen und dann **User Settings** aus.
2. Wählen Sie auf dem Tab **Access tokens** die Option **Generate new Token / Textbaustein** aus.
3. Fügen Sie einen Kommentar hinzu, um das Token / Textbaustein zu identifizieren, z. B. „Braze CDI“.
4. Lassen Sie das Feld **Lifetime (days)** leer, wenn keine Ablaufzeit festgelegt werden soll, und wählen Sie dann **Generate** aus.
5. Kopieren Sie das Token / Textbaustein und bewahren Sie es sicher auf, um es im Braze-Dashboard zu verwenden.

##### Schritt 1.4: Netzwerkrichtlinien konfigurieren

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Allowlist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=databricks#step-13-allow-access-to-braze-ips).

{% endtab %}
{% tab Fabric %}

##### Schritt 1.1: Quelltabelle in Fabric einrichten {#step-11-set-up-your-source-table-in-fabric}

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### Schritt 1.2: Zugangsdaten einrichten

Erstellen Sie einen Dienstprinzipal und erteilen Sie Berechtigungen. Falls Sie bereits Zugangsdaten aus einer anderen Synchronisierung besitzen, können Sie diese wiederverwenden – stellen Sie nur sicher, dass sie Zugriff auf die Kontentabelle haben.

##### Schritt 1.3: Netzwerkrichtlinien konfigurieren

Falls für Ihr Konto Netzwerkrichtlinien gelten, fügen Sie die IP-Adressen von Braze zur Allowlist hinzu, um die Verbindung zum CDI-Dienst zu ermöglichen. Die Liste der IP-Adressen finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional).

{% endtab %}
{% tab Dateispeicher %}

Um Canvas-Trigger aus dem Dateispeicher zu synchronisieren, erstellen Sie eine Quelldatei mit den folgenden Feldern.

| Feld | Erforderlich | Beschreibung |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | Ja, eines von `external_id` oder `alias_name` und `alias_label` | Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte dem in Braze verwendeten Wert `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Ja, eines von `external_id` oder `alias_name` und `alias_label` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `PROPERTIES` | Ja | JSON-String von Feldern, die als Personalisierungs-Eigenschaften in Ihrem Canvas verfügbar gemacht werden sollen. Dieser sollte nutzerspezifische Informationen enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1.3: Netzwerkrichtlinien konfigurieren" }

{% alert tip %}
Dateinamen müssen den AWS-Regeln entsprechen und eindeutig sein. Fügen Sie Zeitstempel hinzu, um die Eindeutigkeit sicherzustellen. Weitere Informationen zur Synchronisierung mit Amazon S3 finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).
{% endalert %}

{% endtab %}
{% endtabs %}

#### 2. Schritt: Ziel-Canvas konfigurieren {#step-2-configure-your-destination-canvas}

1. Richten Sie Ihren Ziel-Canvas für Canvas-Trigger ein. Erstellen Sie einen neuen oder wählen Sie einen vorhandenen API-getriggerten Canvas aus. Anweisungen zum Erstellen eines Canvas mit einem API-getriggerten Zustellungszeitplan finden Sie unter [Entry-Zeitplantypen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#entry-schedule-types).
2. Nachdem Sie den API-getriggerten Zustellungszeitplan ausgewählt haben, fahren Sie mit der Canvas-Einrichtung fort und erstellen Sie Ihren Canvas. Canvases können von einfachen Einzelnachrichten bis hin zu komplexen Kunden-Workflows mit mehreren Schritten reichen.
3. Verwenden Sie innerhalb Ihrer Canvas-Schritte [Canvas-Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), um Nachrichten mit Eigenschaftsfeldern zu personalisieren, die Sie aus Ihrer Quelltabelle synchronisieren möchten.
  * Wenn Sie beispielsweise in [Schritt 1](#step-1-set-up-data-source-for-canvas-triggers) ein Eigenschaftsfeld für `account_balance` eingerichtet haben, würden Sie die folgende Liquid-Vorlage verwenden, um Ihre Nachricht zu personalisieren: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Nachdem Sie Ihren Canvas erstellt haben, starten Sie ihn und fahren Sie mit [Schritt 3](#step-3-create-your-zero-copy-sync) fort.

#### 3. Schritt: Zero-Copy-Synchronisierung erstellen {#step-3-create-your-zero-copy-sync}

Nachdem Sie die Quellkonfiguration abgeschlossen und den Ziel-Canvas gestartet haben, erstellen Sie eine neue Datensynchronisierung:

1. Navigieren Sie in Braze zu **Dateneinstellungen** > **Cloud-Datenaufnahme**.
1. Richten Sie die Verbindung ein, indem Sie die Verbindungsdetails eingeben (oder vorhandene Zugangsdaten wiederverwenden) und die Quelltabelle aus [Schritt 1](#step-1-set-up-data-source-for-canvas-triggers) auswählen.
2. Geben Sie der Integration einen Namen.
3. Wählen Sie den Datentyp **Canvas Triggers** aus.
4. Wählen Sie Ihren Ziel-Canvas aus (aus [Schritt 2](#step-2-configure-your-destination-canvas)).
5. Wählen Sie eine Synchronisierungshäufigkeit aus.
6. Konfigurieren Sie Ihre Benachrichtigungseinstellungen.
7. Wählen Sie **Test Connection**, um zu bestätigen, dass alles wie erwartet funktioniert. Wenn Sie eine Verbindung zu Snowflake herstellen, fügen Sie zunächst den auf dem Dashboard angezeigten Public Key der Nutzer:in hinzu, die für die Braze-Verbindung zu Snowflake erstellt wurde. Um diesen Schritt abzuschließen, benötigen Sie in Snowflake mindestens **SECURITYADMIN**-Zugriff.
8. Speichern Sie die Synchronisierung, um mit der Synchronisierung der Canvas-Trigger zu beginnen.

Wenn die Synchronisierung ausgeführt wird, beginnen die Nutzer:innen in Ihrer Quelltabelle, in den Canvas einzutreten. Nutzen Sie die Canvas-Analytics und die Seite mit den Cloud-Datenaufnahme-Synchronisierungsprotokollen, um die Performance zu überwachen.

{% alert tip %}
Überprüfen Sie Ihre gesamte Konfiguration (vom Synchronisierungsverhalten bis zur Canvas-Einrichtung), um unerwartete Sendungen zu vermeiden. Canvas-Einstellungen wie Rate-Limiting, Frequency-Capping und Segmentierungs-Filter können die Nachrichtenzustellung weiter verfeinern.<br><br>Wir empfehlen, vor der Implementierung von Produktions-Anwendungsfällen einen Probelauf mit einer kleinen oder Test-Zielgruppe durchzuführen.
{% endalert %}

### Überlegungen {#considerations}

CDI Canvas-Trigger nutzen Ihr REST API-Rate-Limit für `/canvas/trigger/send`. Wenn Sie diesen Endpunkt gleichzeitig mit CDI Canvas-Triggern und Ihrer REST API-Integration verwenden, wird die kombinierte Nutzung auf Ihr Rate-Limit angerechnet.

Bei jedem Synchronisierungslauf werden Nutzer:innen mit einer maximalen Rate von etwa 3,75 Millionen Nutzer:innen pro Stunde in den jeweiligen Ziel-Canvas aufgenommen. Rechnen Sie mit längeren Zeiten zwischen Quelle und Canvas-Eintritt, wenn:

* Mehr als 3,75 Millionen Nutzer:innen pro Synchronisierungslauf synchronisiert werden.
* CDI Canvas-Trigger verwendet werden, während das [Rate-Limit Ihrer REST API für `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#rate-limit) bereits ausgeschöpft ist.

Beachten Sie Folgendes zur Zero-Copy-CDI, wenn die Nachrichtenarchivierung aktiviert ist:

* Die Ergebnisse der Tabelle werden während der Verarbeitung vorübergehend in Braze gespeichert. Sie werden außerdem für 30 Tage nach Snowflake exportiert, damit Sie genau nachvollziehen können, was synchronisiert wurde.
* Archivierte Nachrichten werden nirgendwo innerhalb von Braze gespeichert. Die Kopien werden ausschließlich in Ihrem konfigurierten Speicher abgelegt.
* Bei der Verwendung von Zero-Copy-CDI mit Canvas-Triggern speichert Braze keine Sicherungskopie der Abfrageergebnisse aus dem Data Warehouse, und es werden keine Daten in das Kundenprofil kopiert.
* Canvas-Kontext-Eigenschaften können bis zu 30 Tage lang in internen Systemen protokolliert werden.