---
nav_title: Katalogdaten synchronisieren und löschen
article_title: Katalogdaten synchronisieren und löschen
page_order: 6
page_type: reference
description: "Diese Seite bietet eine Übersicht darüber, wie Sie Katalogdaten synchronisieren können."

---

# Katalogdaten synchronisieren und löschen {#sync-and-delete-catalog-data}

> Diese Seite beschreibt, wie Sie Katalogdaten synchronisieren können.

## Schritt 1: Einen neuen Katalog erstellen {#step-1-create-a-new-catalog}

Bevor Sie eine neue Cloud Data Ingestion (CDI)-Integration für [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) erstellen, müssen Sie einen neuen Katalog erstellen oder einen vorhandenen Katalog identifizieren, den Sie für die Integration verwenden möchten. Es gibt mehrere Möglichkeiten, einen neuen Katalog zu erstellen, und jede davon funktioniert für die CDI-Integration:
- Laden Sie eine [CSV-Datei]({{site.baseurl}}/user_guide/data/activation/catalogs/create) hoch
- Erstellen Sie einen Katalog im [Braze-Dashboard]({{site.baseurl}}/user_guide/data/activation/catalogs/create) oder während der CDI-Einrichtung.
- Erstellen Sie einen Katalog über den [Endpunkt „Katalog erstellen“]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)

Alle Änderungen am Katalogschema (z. B. das Hinzufügen neuer Felder oder das Ändern von Feldtypen) müssen über das Katalog-Dashboard vorgenommen werden, bevor aktualisierte Daten über CDI synchronisiert werden. Wir empfehlen, diese Aktualisierungen vorzunehmen, wenn die Synchronisierung pausiert ist oder nicht geplant ist, um Konflikte zwischen Ihren Data-Warehouse-Daten und dem Schema in Braze zu vermeiden.

## Schritt 2: Cloud-Datenaufnahme mit Katalogdaten integrieren {#step-2-integrate-cloud-data-ingestion-with-catalog-data}
Das Setup für eine Katalogsynchronisation folgt weitgehend dem Prozess für [CDI-Integrationen für Nutzerdaten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

{% tabs %}
{% tab Snowflake %}

1. Richten Sie eine Quelltabelle in Snowflake ein. Sie können die Namen im folgenden Beispiel verwenden oder eigene Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Richten Sie eine Rolle, ein Warehouse und eine:n Nutzer:in ein und vergeben Sie die entsprechenden Berechtigungen. Falls Sie bereits Zugangsdaten aus einer bestehenden Synchronisation haben, können Sie diese wiederverwenden – stellen Sie jedoch sicher, dass der Zugriff auf die Katalog-Quelltabelle erweitert wird.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Wenn Ihr Snowflake-Konto Netzwerkrichtlinien hat, setzen Sie die Braze-IPs auf die Zulassungsliste, damit der CDI-Dienst eine Verbindung herstellen kann. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
4. Navigieren Sie im Braze-Dashboard zu **Technologie-Partner** > **Snowflake** und erstellen Sie eine neue Synchronisation.
5. Geben Sie die Verbindungsdetails ein (oder verwenden Sie bestehende Zugangsdaten) sowie die Quelltabelle.
6. Fahren Sie mit Schritt 2 des Setup-Ablaufs fort, wählen Sie den Synchronisationstyp „Catalogs“ aus und geben Sie den Integrationsnamen und den Zeitplan ein. Beachten Sie, dass der Name der Integration **exakt dem Namen** des zuvor erstellten Katalogs entsprechen muss.
7. Wählen Sie eine Synchronisationsfrequenz und fahren Sie mit dem nächsten Schritt fort.
8. Fügen Sie den im Dashboard angezeigten Public Key dem/der Nutzer:in hinzu, den/die Sie für die Verbindung von Braze mit Snowflake erstellt haben. Für diesen Schritt benötigen Sie eine Person mit `SECURITYADMIN`-Zugriff oder höher in Snowflake.
9. Wählen Sie **Verbindung testen**, um sicherzustellen, dass alles wie erwartet funktioniert.
10. Speichern Sie die Synchronisation und nutzen Sie die synchronisierten Katalogdaten für all Ihre Personalisierungs-Anwendungsfälle.
{% endtab %}
{% tab Redshift %}

1. Richten Sie eine Quelltabelle in Redshift ein. Sie können die Namen im folgenden Beispiel verwenden oder eigene Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Richten Sie eine:n Nutzer:in ein und vergeben Sie die entsprechenden Berechtigungen. Falls Sie bereits Zugangsdaten aus einer bestehenden Synchronisation haben, können Sie diese wiederverwenden – stellen Sie jedoch sicher, dass der Zugriff auf die Katalog-Quelltabelle erweitert wird.
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Wenn Sie eine Firewall oder andere Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Redshift-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Richten Sie optional ein neues Projekt oder Dataset für Ihre Quelltabelle ein.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| FELDNAME | TYP | MODUS |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | JSON | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | OPTIONAL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Cloud-Datenaufnahme mit Katalogdaten integrieren" }

{:start="2"}

2. Richten Sie eine:n Nutzer:in ein und vergeben Sie die entsprechenden Berechtigungen. Falls Sie bereits Zugangsdaten aus einer bestehenden Synchronisation haben, können Sie diese wiederverwenden – stellen Sie jedoch sicher, dass der Zugriff auf die Katalog-Quelltabelle erweitert wird.
Das Dienstkonto sollte die folgenden Berechtigungen besitzen:
- BigQuery Connection User: Dies ermöglicht Braze, Verbindungen herzustellen.
- BigQuery User: Dies gibt Braze Zugriff zum Ausführen von Abfragen, Lesen von Dataset-Metadaten und Auflisten von Tabellen.
- BigQuery Data Viewer: Dies gibt Braze Zugriff zum Anzeigen von Datasets und deren Inhalten.
- BigQuery Job User: Dies gibt Braze Zugriff zum Ausführen von Jobs.<br><br>Nachdem Sie das Dienstkonto erstellt und die Berechtigungen vergeben haben, generieren Sie einen JSON-Schlüssel. Weitere Informationen finden Sie unter [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete). Sie laden diesen später im Braze-Dashboard hoch.

{:start="3"}
3. Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre BigQuery-Instanz gewähren. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Richten Sie eine Quelltabelle in Databricks ein. Sie können die Namen im folgenden Beispiel verwenden oder eigene Katalog-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| FELDNAME | TYP | MODUS |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | STRING, STRUCT, or MAP | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Cloud-Datenaufnahme mit Katalogdaten integrieren" }

{:start="2"}

2. Erstellen Sie ein persönliches Zugriffstoken in Ihrem Databricks-Workspace.

- a. Wählen Sie Ihren Databricks-Nutzernamen aus und wählen Sie dann **User Settings** aus dem Dropdown-Menü.
- b. Wählen Sie auf dem Tab **Access tokens** die Option **Generate new Token**.
- c. Geben Sie einen Kommentar ein, der Ihnen hilft, dieses Token zu identifizieren, z. B. „Braze CDI“.
- d. Ändern Sie die Lebensdauer des Tokens auf unbegrenzt, indem Sie das Feld **Lifetime (days)** leer lassen. Wählen Sie **Generate**.
- e. Kopieren Sie das angezeigte Token und wählen Sie dann **Done**.
- f. Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es im Schritt zur Erstellung der Zugangsdaten im Braze-Dashboard eingeben müssen.

{:start="3"}
3. Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Eine Liste der IPs finden Sie auf der Seite [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. Richten Sie einen Dienstprinzipal ein und vergeben Sie die entsprechenden Berechtigungen. Falls Sie bereits Zugangsdaten aus einer bestehenden Synchronisation haben, können Sie diese wiederverwenden – stellen Sie jedoch sicher, dass der Zugriff auf die Katalog-Quelltabelle erweitert wird. Weitere Informationen zur Erstellung eines neuen Dienstprinzipals und der Zugangsdaten finden Sie auf der Seite [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{:start="3"}
3. Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre Microsoft-Fabric-Instanz gewähren. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Erstellen Sie Quelldateien in S3 im JSON- oder CSV-Format. Jede Datei muss die folgenden Felder enthalten:

| Feld | Erforderlich? | Beschreibung |
| --- | --- | --- |
| `ID` | Ja | Die ID des Katalogartikels, der erstellt oder aktualisiert werden soll. |
| `PAYLOAD` | Ja | Ein JSON-String der Felder, die mit dem Katalogartikel in Braze synchronisiert werden sollen. |
| `DELETED` | Optional | Wenn auf `true` gesetzt, wird der zugehörige Katalogartikel aus dem Katalog entfernt. |
| `UPDATED_AT` | *Nicht unterstützt* | Dateispeicher unterstützt keine `UPDATED_AT`-Spalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Cloud-Datenaufnahme mit Katalogdaten integrieren" }

{% alert note %}
Dateinamen müssen den AWS-Regeln entsprechen und eindeutig sein. Hängen Sie Zeitstempel an, um die Eindeutigkeit sicherzustellen.
{% endalert %}

Das vollständige S3-Setup erfordert einen S3-Bucket, eine Amazon-SQS-Warteschlange sowie eine AWS-IAM-Rolle und -Richtlinie. Braze verarbeitet nur Dateien, die nach der Erstellung der Synchronisation hochgeladen werden. Laden Sie also vorhandene Dateien, die Sie aufnehmen möchten, erneut hoch.

Für den vollständigen S3-Setup-Ablauf lesen Sie [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations), insbesondere:

- [Cloud-Datenaufnahme in AWS einrichten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-aws)
- [Cloud-Datenaufnahme in Braze einrichten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)
- [Fehlerbehebung]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#troubleshooting)

Für häufige Benachrichtigungs- und Berechtigungsprobleme auf AWS-Seite lesen Sie [Granting permissions to publish event notification messages to a destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html).

Die folgenden Beispiele zeigen gültige JSON- und CSV-Formate für die Synchronisation von Katalogdaten aus dem Dateispeicher.

{% subtabs %}
{% subtab JSON Catalogs %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, andernfalls wird die Datei übersprungen.
{% endalert %}
{% endsubtab %}
{% subtab CSV Catalogs with Delete %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% subtab CSV Catalogs without Delete %}
```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"
```
{% endsubtab %}
{% endsubtabs %}

Weitere Dateibeispiele finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).

{% endtab %}
{% endtabs %}

## So funktioniert die Integration {#how-the-integration-works}

{% alert note %}
Die Synchronisierungsansichten in diesem Abschnitt gelten nur für Data-Warehouse-Integrationen. Für S3-Dateispeicher verarbeitet Braze neue Dateien, sobald sie in Ihren Bucket hochgeladen werden. Weitere Informationen finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).
{% endalert %}

Bei jeder Synchronisierung ruft Braze alle Zeilen ab, bei denen `UPDATED_AT` später als der zuletzt synchronisierte Wert ist. Zeilen mit exakt demselben Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen. Wir empfehlen, in Ihrem Data Warehouse eine Ansicht (View) aus Ihren Katalogdaten zu erstellen, um eine Quelltabelle einzurichten, die bei jeder Synchronisierung vollständig aktualisiert wird. Mit Ansichten müssen Sie die Abfrage nicht jedes Mal neu schreiben.

Wenn Sie beispielsweise eine Tabelle mit Produktdaten (`product_catalog_1`) mit `product_id` und drei zusätzlichen Attributen haben, könnten Sie die folgende Ansicht synchronisieren:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Die aus der Integration abgerufenen Daten werden verwendet, um Artikel im Zielkatalog basierend auf der angegebenen `id` zu erstellen oder zu aktualisieren.
- Wenn DELETED auf `true` gesetzt ist, wird der entsprechende Katalogartikel gelöscht.
- Die Synchronisierung protokolliert keine Datenpunkte, aber alle synchronisierten Daten werden auf Ihre gesamte Katalognutzung angerechnet. Diese Nutzung wird anhand der insgesamt gespeicherten Daten gemessen, sodass Sie sich keine Gedanken darüber machen müssen, nur geänderte Daten zu synchronisieren.