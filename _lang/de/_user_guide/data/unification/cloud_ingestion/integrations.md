---
nav_title: Integration von Data Warehouses
article_title: Data Warehouse-Speicherintegrationen
alias: /partners/databricks/
description: "Auf dieser Seite erfahren Sie, wie Sie Braze Cloud-Datenaufnahme verwenden, um relevante Daten mit Ihrer Snowflake-, Redshift-, BigQuery- und Databricks-Integration zu synchronisieren."
page_order: 3
page_type: reference
---

# Data Warehouse-Speicherintegrationen {#data-warehouse-storage-integrations}

> Auf dieser Seite erfahren Sie, wie Sie Braze Cloud-Datenaufnahme (CDI) verwenden, um relevante Daten mit Ihrer Snowflake-, Redshift-, BigQuery- und Databricks-Integration zu synchronisieren.

## Einrichtung von Data-Warehouse-Integrationen {#setting-up-data-warehouse-integrations}

Cloud Data Ingestion-Integrationen erfordern eine gewisse Einrichtung auf der Braze-Seite und in Ihrer Data-Warehouse-Instanz. Führen Sie die folgenden Schritte aus, um die Integration einzurichten:

{% tabs %}
{% tab Snowflake %}
1. Richten Sie in Ihrer Snowflake-Instanz die Tabellen oder Views ein, die Sie mit Braze synchronisieren möchten.
2. Erstellen Sie eine neue Snowflake-Quelle im Braze-Dashboard.
3. Rufen Sie den im Braze-Dashboard bereitgestellten Public Key ab und [hängen Sie ihn an den Snowflake-Nutzer zur Authentifizierung an](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Erstellen Sie eine Synchronisierung im Braze-Dashboard, testen Sie die Integration und starten Sie die Synchronisierung.

{% alert tip %}
Der [Snowflake-Schnellstartleitfaden](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) enthält Beispielcode und führt durch die erforderlichen Schritte, um eine automatisierte Pipeline mit Snowflake Streams und CDI zur Datensynchronisierung mit Braze zu erstellen.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Stellen Sie sicher, dass der Braze-Zugriff auf die Redshift-Tabellen erlaubt ist, die Sie synchronisieren möchten. Braze verbindet sich über das Internet mit Redshift.
2. Richten Sie in Ihrer Redshift-Instanz die Tabellen oder Views ein, die Sie mit Braze synchronisieren möchten.
3. Erstellen Sie eine neue Quelle und Synchronisierung im Braze-Dashboard.
4. Testen Sie die Integration und starten Sie die Synchronisierung.

{% alert note %}
Die pro Synchronisierung verarbeiteten Zeilen hängen von der Performance Ihres Warehouses, der Netzwerklatenz und der Menge neuer Daten ab, die der Synchronisierungsabfrage entsprechen. Verwenden Sie den **Synchronisierungsverlauf** der Integration im Dashboard, um Dauer und Zeilenanzahlen der letzten Durchläufe einzusehen.
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf die BigQuery-Projekte und -Datensätze, die die zu synchronisierenden Daten enthalten.
2. Richten Sie in Ihrem BigQuery-Konto die Tabellen oder Views ein, die Sie mit Braze synchronisieren möchten.
3. Erstellen Sie eine neue Quelle und Synchronisierung im Braze-Dashboard.
4. Testen Sie die Integration und starten Sie die Synchronisierung.
{% endtab %}
{% tab Databricks %}
1. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf die Databricks-Projekte und -Datensätze, die die zu synchronisierenden Daten enthalten.
2. Richten Sie in Ihrem Databricks-Konto die Tabellen oder Views ein, die Sie mit Braze synchronisieren möchten.
3. Erstellen Sie eine neue Quelle und Synchronisierung im Braze-Dashboard.
4. Testen Sie die Integration und starten Sie die Synchronisierung.

{% alert important %}
Es kann zwei bis fünf Minuten Aufwärmzeit geben, wenn Braze eine Verbindung zu Classic- und Pro-SQL-Instanzen herstellt, was zu Verzögerungen beim Verbindungsaufbau und -test sowie zu Beginn geplanter Synchronisierungen führen kann. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann jedoch zu geringfügig höheren Integrationskosten führen.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Erstellen Sie einen Dienstprinzipal und gewähren Sie Zugriff auf Fabric-APIs.
2. Richten Sie einen gemeinsam genutzten Workspace ein und gewähren Sie dem Dienstprinzipal Zugriff darauf.
3. Richten Sie im gemeinsam genutzten Fabric-Workspace die Tabellen oder Views ein, die Sie mit Braze synchronisieren möchten.
4. Erstellen Sie eine neue Quelle und Synchronisierung im Braze-Dashboard.
5. Testen Sie die Integration und starten Sie die Synchronisierung.
{% endtab %}
{% endtabs %}

### Schritt 1: Tabellen oder Views einrichten {#step-1-set-up-tables-or-views}

Bevor Sie beginnen, lesen Sie [Tabelleneinrichtung für Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup), um die Anforderungen an Quelltabellen im Vergleich zu den Formatierungsanforderungen für `PAYLOAD` zu verstehen.

{% alert note %}
Ihre Quelltabelle oder View kann Spalten enthalten, die nicht für Ihr Warehouse in den Tabs im folgenden Abschnitt aufgeführt sind (z. B. Auditing oder Hashing). Braze liest nur die in diesen Tabs beschriebenen Spalten; andere Spalten werden bei Cloud Data Ingestion-Synchronisierungen nicht verwendet.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### Schritt 1.1: Tabelle einrichten {#step-11-set-up-the-table}

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Sie können Datenbank, Schema und Tabelle beliebig benennen, die Spaltennamen sollten jedoch der obigen Definition entsprechen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen an der exakten Grenz-Zeitstempel-Grenze können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel verwenden.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen haben.
    - `EXTERNAL_ID` – Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen.
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese zwei Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Der Braze-Nutzer:innen-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht über eine Braze-ID durch Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe Nutzer:innen-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefon angeben, wird die E-Mail als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert.
- `PAYLOAD` – Dies ist ein JSON-String der Felder, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

#### Schritt 1.2: Rolle und Datenbankberechtigungen einrichten {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Aktualisieren Sie die Namen nach Bedarf, die Berechtigungen sollten jedoch dem obigen Beispiel entsprechen.

#### Schritt 1.3: Warehouse einrichten und Zugriff für die Braze-Rolle gewähren {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Das Warehouse muss die **Auto-Resume**-Funktion aktiviert haben. Falls nicht, gewähren Sie Braze zusätzliche `OPERATE`-Berechtigungen auf dem Warehouse, damit Braze es einschalten kann, wenn die Abfrage ausgeführt wird.
{% endalert %}

#### Schritt 1.4: Nutzer:in einrichten {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Teilen Sie nach diesem Schritt die Verbindungsinformationen mit Braze, um einen Public Key zu erhalten, der an die Nutzer:in angehängt wird.

{% alert note %}
Wenn Sie verschiedene Workspaces mit demselben Snowflake-Konto verbinden, müssen Sie für jeden Braze-Workspace, in dem Sie eine Integration erstellen, eine eindeutige Nutzer:in erstellen. Innerhalb eines Workspaces können Sie dieselbe Nutzer:in über verschiedene Integrationen hinweg wiederverwenden, die Integration schlägt jedoch fehl, wenn eine Nutzer:in im selben Snowflake-Konto über Workspaces hinweg dupliziert wird.
{% endalert %}

#### Schritt 1.5: Braze-IPs in der Snowflake-Netzwerkrichtlinie zulassen (optional) {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Abhängig von der Konfiguration Ihres Snowflake-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Snowflake-Netzwerkrichtlinie zulassen. Weitere Informationen zur Aktivierung finden Sie in der entsprechenden Snowflake-Dokumentation zum [Ändern einer Netzwerkrichtlinie](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Schritt 1.1: Tabelle einrichten

Optional können Sie eine neue Datenbank und ein neues Schema für Ihre Quelltabelle einrichten.
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Erstellen Sie eine Tabelle (oder View) für Ihre CDI-Integration.
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Sie können Datenbank, Schema und Tabelle beliebig benennen, die Spaltennamen sollten jedoch der obigen Definition entsprechen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen an der exakten Grenz-Zeitstempel-Grenze können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel verwenden.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen haben.
    - `EXTERNAL_ID` – Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen.
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese zwei Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Der Braze-Nutzer:innen-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht über eine Braze-ID durch Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe Nutzer:innen-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefon angeben, wird die E-Mail als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert.
- `PAYLOAD` – Dies ist ein JSON-String der Felder, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

#### Schritt 1.2: Nutzer:in erstellen und Berechtigungen erteilen {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Dies sind die Mindestberechtigungen für diese Nutzer:in. Wenn Sie mehrere CDI-Integrationen erstellen, möchten Sie möglicherweise Berechtigungen auf Schema-Ebene erteilen oder Berechtigungen über eine Gruppe verwalten.

#### Schritt 1.3: Zugriff für Braze-IPs erlauben {#step-13-allow-access-to-braze-ips}

Wenn Sie eine Firewall oder andere Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Redshift-Instanz gewähren. Ein Beispiel für den Redshift-URL-Endpunkt ist „example-cluster.ap-northeast-2.redshift.amazonaws.com“.

Einige wichtige Hinweise:
- Möglicherweise müssen Sie auch Ihre Sicherheitsgruppen ändern, um Braze den Zugriff auf Ihre Daten in Redshift zu ermöglichen.
- Stellen Sie sicher, dass Sie den eingehenden Datenverkehr auf den IPs in der Tabelle und auf dem Port, der für die Abfrage Ihres Redshift-Clusters verwendet wird (Standard ist 5439), explizit zulassen. Sie sollten die Redshift-TCP-Konnektivität auf diesem Port explizit zulassen, auch wenn die Eingangsregeln auf „Alle zulassen“ eingestellt sind.
- Der Endpunkt für den Redshift-Cluster muss öffentlich zugänglich sein, damit Braze sich mit Ihrem Cluster verbinden kann.
     - Wenn Sie nicht möchten, dass Ihr Redshift-Cluster öffentlich zugänglich ist, können Sie eine VPC und EC2-Instanz einrichten, um einen SSH-Tunnel für den Zugriff auf die Redshift-Daten zu verwenden. Weitere Informationen finden Sie im [Beitrag des AWS Knowledge Centers](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).

Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Schritt 1.1: Tabelle einrichten

Optional können Sie ein neues Projekt oder einen neuen Datensatz für Ihre Quelltabelle einrichten.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1.1: Tabelle einrichten" }

Sie können Projekt, Datensatz und Tabelle beliebig benennen, die Spaltennamen sollten jedoch der obigen Definition entsprechen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen an der exakten Grenz-Zeitstempel-Grenze können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel verwenden.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen haben.
    - `EXTERNAL_ID` – Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen.
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese zwei Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Der Braze-Nutzer:innen-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht über eine Braze-ID durch Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe Nutzer:innen-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefon angeben, wird die E-Mail als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert.
- `PAYLOAD` – Dies ist ein JSON-String der Felder, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

{% alert important %}
**BigQuery-Partitionierung**

CDI unterstützt Partitionen für BigQuery. Wenn Sie nach einer Funktion von `UPDATED_AT` partitionieren (z. B. auf Tages-, Wochen- oder Stundenebene, je nach Größe Ihres Datensatzes), kann BigQuery die zu scannenden Daten eingrenzen. Dies verbessert die Performance und Effizienz bei sehr großen Tabellen.

Partitionieren Sie nicht nach anderen Feldern. Testen Sie verschiedene Konfigurationen, um die beste Einstellung für Ihre spezifischen Daten zu finden.

Alle CDI-Abfragen filtern nach `UPDATED_AT`, dieses Verhalten kann sich jedoch ändern. Gestalten Sie Ihr Tabellenschema so, dass Abfragen _nicht_ zwingend diese Klausel enthalten müssen.

Weitere Informationen finden Sie in der [BigQuery-Partitionierungsdokumentation](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Schritt 1.2: Dienstkonto erstellen und Berechtigungen erteilen {#step-12-create-a-service-account-and-grant-permissions}

Erstellen Sie ein Dienstkonto in GCP, das Braze verwenden kann, um eine Verbindung herzustellen und Daten aus Ihren Tabellen zu lesen. Das Dienstkonto sollte die folgenden Berechtigungen haben:

- **BigQuery Connection User:** Ermöglicht Braze, Verbindungen herzustellen
- **BigQuery User:** Ermöglicht Braze den Zugriff zum Ausführen von Abfragen, Lesen von Datensatz-Metadaten und Auflisten von Tabellen.
- **BigQuery Data Viewer:** Ermöglicht Braze den Zugriff zum Anzeigen von Datensätzen und deren Inhalten.
- **BigQuery Job User:** Ermöglicht Braze den Zugriff zum Ausführen von Jobs

Generieren Sie nach der Erstellung des Dienstkontos und der Erteilung der Berechtigungen einen JSON-Schlüssel. Weitere Informationen finden Sie unter [Dienstkontoschlüssel erstellen und löschen](https://cloud.google.com/iam/docs/keys-create-delete). Laden Sie diesen Schlüssel in einem späteren Schritt im Braze-Dashboard hoch.

#### Schritt 1.3: Zugriff für Braze-IPs erlauben

Wenn Sie Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre BigQuery-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Schritt 1.1: Tabelle einrichten

Optional können Sie einen neuen Katalog oder ein neues Schema für Ihre Quelltabelle einrichten.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Feldname | Typ | Modus |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1.1: Tabelle einrichten" }

Sie können Schema und Tabelle beliebig benennen, die Spaltennamen sollten jedoch der obigen Definition entsprechen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen an der exakten Grenz-Zeitstempel-Grenze können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel verwenden.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen haben.
    - `EXTERNAL_ID` – Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen.
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese zwei Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Der Braze-Nutzer:innen-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht über eine Braze-ID durch Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe Nutzer:innen-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefon angeben, wird die E-Mail als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert.
- `PAYLOAD` – Dies ist ein String oder Struct der Felder, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

#### Schritt 1.2: Zugriffstoken erstellen {#step-12-create-an-access-token}

Damit Braze auf Databricks zugreifen kann, muss ein persönlicher Zugriffstoken erstellt werden.

1. Wählen Sie in Ihrem Databricks-Workspace Ihren Databricks-Nutzernamen in der oberen Leiste aus und wählen Sie dann **User Settings** aus dem Dropdown-Menü.
2. Wählen Sie auf dem Tab „Access tokens“ die Option **Generate new Token**.
3. Geben Sie einen Kommentar ein, der Ihnen hilft, dieses Token zu identifizieren, z. B. „Braze CDI“, und ändern Sie die Lebensdauer des Tokens auf unbegrenzt, indem Sie das Feld „Lifetime (days)“ leer lassen.
4. Wählen Sie **Generate**.
5. Kopieren Sie das angezeigte Token und wählen Sie dann **Done**.

Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es beim Schritt zur Erstellung der Zugangsdaten im Braze-Dashboard eingeben müssen.

#### Schritt 1.3: Zugriff für Braze-IPs erlauben

Wenn Sie Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze-Dashboards entsprechen.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Schritt 1.1: Dienstprinzipal einrichten und Zugriff gewähren {#step-11-set-up-the-service-principal-and-grant-access}
Braze verbindet sich mit Ihrem Fabric-Warehouse über einen Dienstprinzipal mit Entra-ID-Authentifizierung. Erstellen Sie einen neuen Dienstprinzipal, den Braze verwenden kann, und gewähren Sie bei Bedarf Zugriff auf Fabric-Ressourcen. Braze benötigt die folgenden Details zur Verbindung:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure erlaubt keine unbegrenzte Gültigkeit für Dienstprinzipal-Secrets. Denken Sie daran, die Zugangsdaten zu erneuern, bevor sie ablaufen, um den Datenfluss zu Braze aufrechtzuerhalten.
{% endalert %}

#### Schritt 1.2: Zugriff auf Fabric-Ressourcen gewähren {#step-12-grant-access-to-fabric-resources}
Gewähren Sie Braze Zugriff zur Verbindung mit Ihrer Fabric-Instanz. Navigieren Sie in Ihrem Fabric-Admin-Portal zu **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Aktivieren Sie unter **Developer settings** die Option **Service principals can use Fabric APIs**, damit Braze sich über Microsoft Entra ID verbinden kann.
* Aktivieren Sie unter **OneLake settings** die Option **Users can access data stored in OneLake with apps external to Fabric**, damit der Dienstprinzipal von einer externen App aus auf Daten zugreifen kann.

#### Schritt 1.3: Gemeinsam genutzten Workspace einrichten und Zugriff gewähren {#step-13-set-up-a-shared-workspace-and-grant-access}

Alle Fabric-Ressourcen, die Sie mit Braze verbinden möchten, müssen in einem gemeinsam genutzten Workspace platziert werden. Wenn Sie bisher nur den Standard-**My Workspace** verwendet haben, erstellen Sie einen neuen gemeinsam genutzten Workspace:

1. Wählen Sie im Navigationsmenü **Workspaces** und dann **+ New workspace**.
2. Geben Sie einen **Name** für den Workspace ein und wählen Sie dann **Apply**.

Nachdem Sie einen gemeinsam genutzten Workspace haben, gewähren Sie dem Dienstprinzipal Zugriff:

1. Wählen Sie den Workspace und dann **Manage Access**.
2. Wählen Sie **+ Add people or groups**.
3. Suchen und wählen Sie den Namen des Dienstprinzipals, den Sie in Schritt 1.1 erstellt haben. Wenn er nicht angezeigt wird, bestätigen Sie, dass Sie die Einstellung **Service principals can use Fabric APIs** in Schritt 1.2 aktiviert haben.
4. Wählen Sie im Rollen-Dropdown **Contributor**.

Der Dienstprinzipal kann nun über seine SQL-Endpunkte auf Fabric-Warehouse-Ressourcen in diesem Workspace zugreifen, einschließlich des Warehouses, das für Braze verwendet werden soll.

#### Schritt 1.4: Tabelle einrichten {#step-14-set-up-the-table}
Braze unterstützt sowohl Tabellen als auch Views in Fabric Warehouses. Wenn Sie ein neues Warehouse erstellen müssen, erstellen Sie es innerhalb des gemeinsam genutzten Workspaces aus Schritt 1.3. Gehen Sie im Fabric-Konsolenmenü zu **Create > Data Warehouse > Warehouse**.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Sie können Warehouse, Schema und Tabelle oder View beliebig benennen, die Spaltennamen sollten jedoch der obigen Definition entsprechen.

- `UPDATED_AT` – Der Zeitpunkt, zu dem diese Zeile in der Tabelle aktualisiert oder hinzugefügt wurde. Braze synchronisiert Zeilen, bei denen `UPDATED_AT` nach dem zuletzt synchronisierten Wert liegt. Zeilen an der exakten Grenz-Zeitstempel-Grenze können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel verwenden.
- **Nutzer:innen-Bezeichner-Spalten** – Ihre Tabelle kann eine oder mehrere Nutzer:innen-Bezeichner-Spalten enthalten. Jede Zeile sollte nur einen Bezeichner enthalten (entweder `external_id`, die Kombination aus `alias_name` und `alias_label`, `braze_id`, `email` oder `phone`). Eine Quelltabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen haben.
    - `EXTERNAL_ID` – Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen.
    - `ALIAS_NAME` und `ALIAS_LABEL` – Diese zwei Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` – Der Braze-Nutzer:innen-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht über eine Braze-ID durch Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe Nutzer:innen-ID oder einen Nutzer-Alias an.
    - `EMAIL` – Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefon angeben, wird die E-Mail als primärer Bezeichner verwendet.
    - `PHONE` – Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer existieren, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert.
- `PAYLOAD` – Dies ist ein JSON-String der Felder, die Sie mit der Nutzer:in in Braze synchronisieren möchten.


#### Schritt 1.5: Warehouse-Verbindungszeichenfolge abrufen {#step-15-get-warehouse-connection-string}
Um den SQL-Endpunkt für Ihr Warehouse abzurufen, gehen Sie zum **Workspace** in Fabric, bewegen Sie den Mauszeiger über den Warehouse-Namen in der Elementliste und wählen Sie **Copy SQL connection string**.

![Die Seite „Fabric Console“ in Microsoft Azure, auf der Nutzer:innen die SQL-Verbindungszeichenfolge abrufen sollten.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Schritt 1.6: Braze-IPs in der Firewall zulassen (optional) {#step-16-allow-braze-ips-in-firewall-optional}

Abhängig von der Konfiguration Ihres Microsoft-Fabric-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Firewall zulassen, um den Datenverkehr von Braze zu erlauben. Weitere Informationen zur Aktivierung finden Sie in der entsprechenden Dokumentation zu [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Schritt 2: Neue Quelle im Braze-Dashboard erstellen {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

Gehen Sie im Braze-Dashboard zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Snowflake**.

#### Schritt 2.1: Snowflake-Verbindungsinformationen hinzufügen {#step-21-add-snowflake-connection-information}

Wählen Sie einen Namen für Ihre Quelle und geben Sie Ihre Snowflake-Zugangsdaten und -Konfiguration ein. Fahren Sie dann mit dem nächsten Schritt fort.

Bevor Sie fortfahren, überprüfen Sie den Wert, den Sie im Feld **Snowflake Account Locator** eingeben.

Geben Sie für das Feld **Snowflake Account Locator** Ihren Snowflake-[Kontobezeichner](https://docs.snowflake.com/en/user-guide/admin-account-identifier) ein. Geben Sie nur den Kontobezeichner-Wert ein, z. B. `myorganization-myaccount`. Fügen Sie kein `https://`, `.snowflakecomputing.com` oder einen Pfad hinzu.

So finden Sie Ihren Snowflake-Kontobezeichner:

1. Wählen Sie in Snowsight Ihr Kontomenü.
2. Wählen Sie **View account details**.
3. Kopieren Sie den Wert **Account identifier**.
4. Wenn Sie von einer Snowflake-URL kopieren, verwenden Sie nur den Wert vor `.snowflakecomputing.com`.

#### Schritt 2.2: Public Key zur Braze-Nutzer:in hinzufügen {#step-22-add-a-public-key-to-the-braze-user}

Nachdem Sie Ihre Zugangsdaten und Konfiguration eingegeben haben, klicken Sie auf **Save credentials**, generieren Sie einen RSA-Schlüssel und gehen Sie zurück zu Snowflake, um die Einrichtung abzuschließen. Fügen Sie den im Dashboard angezeigten Public Key der Nutzer:in hinzu, die Sie für die Verbindung von Braze mit Snowflake erstellt haben.

Weitere Informationen dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt rotieren möchten, kann Braze ein neues Schlüsselpaar generieren und den neuen Public Key bereitstellen.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Gehen Sie im Braze-Dashboard zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Amazon Redshift**.

#### Schritt 2.1: Redshift-Verbindungsinformationen und Quelltabelle hinzufügen {#step-21-add-redshift-connection-information-and-source-table}

Wählen Sie einen Namen für Ihre Quelle und geben Sie Ihre Redshift-Zugangsdaten und -Konfiguration ein. Wenn Sie einen privaten Netzwerktunnel verwenden, aktivieren Sie den Schieberegler und geben Sie die Tunnelinformationen ein. Fahren Sie dann mit dem nächsten Schritt fort.

{% alert note %}
Im Braze-Dashboard akzeptiert das Feld **Database name** nur Buchstaben (A–Z, a–z), Zahlen (0–9) und Unterstriche (_), auch wenn Amazon Redshift zusätzliche Zeichen in Datenbankbezeichnern unterstützt.
{% endalert %}

#### Schritt 2.2: Verbindung testen und mit Quelle verbinden {#step-22-test-connection-and-connect-to-source}

Wählen Sie als Nächstes **Test connection**. Sobald der Test erfolgreich war, schließen Sie die verbleibenden Einstellungen ab und klicken Sie auf **Connect to Source**. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

#### Fehlerbehebung: Ungültiger Snapshot-Bezeichner {#troubleshooting-invalid-snapshot-identifier}

Wenn Braze während **Test connection** oder der Synchronisierungseinrichtung den Fehler `Invalid snapshot identifier` zurückgibt, kann Redshift die Snapshot-Referenz nicht auflösen, die beim Abfragen Ihres Quellobjekts verwendet wird.

In Redshift ist ein Snapshot eine zeitpunktbezogene Sicherung eines Clusters. Jeder Snapshot hat einen eindeutigen Bezeichner, den Redshift verwendet, um auf diesen Sicherungszustand zu verweisen. Weitere Informationen finden Sie unter [Amazon Redshift-Snapshots und -Backups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html).

Dieser Fehler kann auftreten, wenn sich Metadaten ändern, während Braze das Quellobjekt validiert, z. B. während Vorgängen zum Kopieren, Wiederherstellen oder Replizieren von Snapshots. Weitere Informationen finden Sie unter [Snapshots in eine andere AWS-Region kopieren](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) und [Einen Cluster aus einem Snapshot wiederherstellen](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html).

Zur Fehlerbehebung:

1. Überprüfen Sie die Quelleinstellungen in Braze, einschließlich Cluster-Endpunkt, Datenbank, Schema und Objektname.
2. Führen Sie dieselbe Abfrage direkt in Redshift aus, um zu bestätigen, dass die Tabelle oder View lesbar und stabil ist.
3. Versuchen Sie es erneut, nachdem aktive Snapshot-, Wiederherstellungs-, Größenänderungs- oder Replikationsaktivitäten abgeschlossen sind.
4. Wenn das Problem weiterhin besteht, fragen Sie stattdessen eine materialisierte View anstelle einer sich häufig ändernden Basistabelle ab.

Eine materialisierte View speichert vorberechnete Abfrageergebnisse, die Sie nach einem Zeitplan aktualisieren können, was Lesevorgänge für CDI-Synchronisierungen stabiler machen kann. Weitere Informationen finden Sie unter [Materialisierte Views in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html).

Beispiel:

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

Nachdem Sie die materialisierte View erstellt haben, verwenden Sie den Namen der materialisierten View als Quellobjekt in Ihrer Braze-CDI-Synchronisierung anstelle der Basistabelle.
{% endtab %}
{% tab BigQuery %}

Gehen Sie im Braze-Dashboard zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Google BigQuery**.

#### Schritt 2.1: BigQuery-Verbindungsinformationen und Quelltabelle hinzufügen {#step-21-add-bigquery-connection-information-and-source-table}

Wählen Sie einen Namen für Ihre Quelle. Laden Sie dann den JSON-Schlüssel hoch und geben Sie einen Namen für das Dienstkonto an. Geben Sie dann die verbleibenden Konfigurationsfelder ein.

#### Schritt 2.2: Verbindung testen und mit Quelle verbinden

Wählen Sie als Nächstes **Test connection**. Sobald der Test erfolgreich war, schließen Sie die verbleibenden Einstellungen ab und klicken Sie auf **Connect to Source**. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% endtab %}
{% tab Databricks %}

Gehen Sie im Braze-Dashboard zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Databricks**.

#### Schritt 2.1: Databricks-Verbindungsinformationen und Quelltabelle hinzufügen {#step-21-add-databricks-connection-information-and-source-table}

Wählen Sie einen Namen für Ihre Quelle und geben Sie Ihre Databricks-Zugangsdaten und -Konfiguration ein. Fahren Sie dann mit dem nächsten Schritt fort.

#### Schritt 2.2: Verbindung testen und mit Quelle verbinden

Wählen Sie als Nächstes **Test connection**. Sobald der Test erfolgreich war, schließen Sie die verbleibenden Einstellungen ab und klicken Sie auf **Connect to Source**. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% alert note %}
Sie müssen eine Quelle erfolgreich testen, bevor sie erstellt werden kann. Wenn Sie die Erstellungsseite schließen, wird Ihre Quelle nicht gespeichert.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Gehen Sie im Braze-Dashboard zu Data Settings > Cloud Data Ingestion > Sources, wählen Sie **Add data source** und dann **Microsoft Fabric**.

#### Schritt 2.1: Cloud Data Ingestion-Synchronisierung einrichten {#step-21-set-up-a-cloud-data-ingestion-sync}

Wählen Sie einen Namen für Ihre Quelle und geben Sie Ihre Microsoft-Fabric-Zugangsdaten und -Konfiguration ein.
- **Credentials Name** ist ein Label für diese Zugangsdaten in Braze; Sie können hier einen hilfreichen Wert festlegen.
- Einzelheiten zum Abrufen von Tenant-ID, Prinzipal-ID, Client-Secret und Verbindungszeichenfolge finden Sie in den Schritten in Abschnitt 1.

#### Schritt 2.2: Verbindung testen und mit Quelle verbinden

Wählen Sie als Nächstes **Test connection**. Sobald der Test erfolgreich war, schließen Sie die verbleibenden Einstellungen ab und klicken Sie auf **Connect to Source**. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% alert note %}
Sie müssen eine Quelle erfolgreich testen, bevor sie erstellt werden kann. Wenn Sie die Erstellungsseite schließen, wird Ihre Quelle nicht gespeichert.
{% endalert %}

{% endtab %}

{% endtabs %}

### Schritt 3: Neue Synchronisierung im Braze-Dashboard erstellen {#step-3-create-a-new-sync-in-the-braze-dashboard}
Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Syncs** und wählen Sie **Create data sync**.

{% tabs %}
{% tab Snowflake %}

#### Schritt 3.1: Synchronisierungsdetails konfigurieren und Verbindung testen {#step-31-configure-sync-details-and-test-connection}
Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann aus den aktiven Quellen aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und klicken Sie auf **Test Connection**.

Sobald der Test erfolgreich war, wird eine Vorschau der Daten angezeigt. Wählen Sie **Next: Notifications**, um fortzufahren. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% alert note %}
Sie müssen eine Synchronisierung erfolgreich testen, bevor Sie zu den nächsten Schritten fortfahren können. Wenn Sie die Erstellungsseite für die Synchronisierung schließen müssen, klicken Sie auf **Save as draft**, um Ihren Fortschritt zu speichern.
{% endalert %}

#### Schritt 3.2: Benachrichtigungseinstellungen hinzufügen {#step-32-add-notification-preferences}
Geben Sie Kontakt-E-Mail-Adressen für Synchronisierungs-Fehlerbenachrichtigungen ein. Braze verwendet diese Kontaktinformationen, um Benachrichtigungen über Integrationsfehler zu senden, z. B. unerwarteten Verlust des Tabellenzugriffs.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungs-Level-Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Probleme auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern.

Solche Probleme können Folgendes umfassen:

- Konnektivitätsprobleme
- Ressourcenmangel
- Berechtigungsprobleme
- (Nur für Katalog-Synchronisierungen) Katalogstufe hat keinen Speicherplatz mehr

#### Schritt 3.3: Zeitplanung {#step-33-scheduling}
Konfigurieren Sie abschließend Ihre Synchronisierung als einmalig oder wiederkehrend.

Einmalige Synchronisierungen können manuell oder über die API ausgelöst werden.

Wiederkehrende Synchronisierungen können eine Frequenz von alle 15 Minuten bis einmal pro Monat haben. Braze plant die wiederkehrende Synchronisierung in der UTC-Zeitzone.

{% endtab %}

{% tab Redshift %}

#### Schritt 3.1: Synchronisierungsdetails konfigurieren und Verbindung testen
Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann aus den aktiven Quellen aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und klicken Sie auf **Test Connection**.

Sobald der Test erfolgreich war, wird eine Vorschau der Daten angezeigt. Wählen Sie **Next: Notifications**, um fortzufahren. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% alert note %}
Sie müssen eine Synchronisierung erfolgreich testen, bevor Sie zu den nächsten Schritten fortfahren können. Wenn Sie die Erstellungsseite für die Synchronisierung schließen müssen, klicken Sie auf **Save as draft**, um Ihren Fortschritt zu speichern.
{% endalert %}

#### Schritt 3.2: Benachrichtigungseinstellungen hinzufügen
Geben Sie Kontakt-E-Mail-Adressen für Synchronisierungs-Fehlerbenachrichtigungen ein. Braze verwendet diese Kontaktinformationen, um Benachrichtigungen über Integrationsfehler zu senden, z. B. unerwarteten Verlust des Tabellenzugriffs.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungs-Level-Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Probleme auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern.

Solche Probleme können Folgendes umfassen:

- Konnektivitätsprobleme
- Ressourcenmangel
- Berechtigungsprobleme

(Nur für Katalog-Synchronisierungen) Katalogstufe hat keinen Speicherplatz mehr

#### Schritt 3.3: Zeitplanung
Konfigurieren Sie abschließend Ihre Synchronisierung als einmalig oder wiederkehrend.

Einmalige Synchronisierungen können manuell oder über die API ausgelöst werden.

Wiederkehrende Synchronisierungen können eine Frequenz von alle 15 Minuten bis einmal pro Monat haben. Braze plant die wiederkehrende Synchronisierung in der UTC-Zeitzone.

{% endtab %}

{% tab BigQuery %}

#### Schritt 3.1: Synchronisierungsdetails konfigurieren und Verbindung testen
Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann aus den aktiven Quellen aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und klicken Sie auf **Test Connection**.

Sobald der Test erfolgreich war, wird eine Vorschau der Daten angezeigt. Wählen Sie **Next: Notifications**, um fortzufahren. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% alert note %}
Sie müssen eine Synchronisierung erfolgreich testen, bevor Sie zu den nächsten Schritten fortfahren können. Wenn Sie die Erstellungsseite für die Synchronisierung schließen müssen, klicken Sie auf **Save as draft**, um Ihren Fortschritt zu speichern.
{% endalert %}

#### Schritt 3.2: Benachrichtigungseinstellungen hinzufügen
Geben Sie Kontakt-E-Mail-Adressen für Synchronisierungs-Fehlerbenachrichtigungen ein. Braze verwendet diese Kontaktinformationen, um Benachrichtigungen über Integrationsfehler zu senden, z. B. unerwarteten Verlust des Tabellenzugriffs.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungs-Level-Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Probleme auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern. Solche Probleme können Folgendes umfassen:

- Konnektivitätsprobleme
- Ressourcenmangel
- Berechtigungsprobleme

(Nur für Katalog-Synchronisierungen) Katalogstufe hat keinen Speicherplatz mehr

#### Schritt 3.3: Zeitplanung
Konfigurieren Sie abschließend Ihre Synchronisierung als einmalig oder wiederkehrend.

Einmalige Synchronisierungen können manuell oder über die API ausgelöst werden.

Wiederkehrende Synchronisierungen können eine Frequenz von alle 15 Minuten bis einmal pro Monat haben. Braze plant die wiederkehrende Synchronisierung in der UTC-Zeitzone.

{% endtab %}

{% tab Databricks %}

#### Schritt 3.1: Synchronisierungsdetails konfigurieren und Verbindung testen
Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann aus den aktiven Quellen aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und klicken Sie auf **Test Connection**.

Sobald der Test erfolgreich war, wird eine Vorschau der Daten angezeigt. Wählen Sie **Next: Notifications**, um fortzufahren. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% alert note %}
Sie müssen eine Synchronisierung erfolgreich testen, bevor Sie zu den nächsten Schritten fortfahren können. Wenn Sie die Erstellungsseite für die Synchronisierung schließen müssen, klicken Sie auf **Save as draft**, um Ihren Fortschritt zu speichern.
{% endalert %}

#### Schritt 3.2: Benachrichtigungseinstellungen hinzufügen
Geben Sie Kontakt-E-Mail-Adressen für Synchronisierungs-Fehlerbenachrichtigungen ein. Braze verwendet diese Kontaktinformationen, um Benachrichtigungen über Integrationsfehler zu senden, z. B. unerwarteten Verlust des Tabellenzugriffs.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungs-Level-Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Probleme auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern.

Solche Probleme können Folgendes umfassen:
- Konnektivitätsprobleme
- Ressourcenmangel
- Berechtigungsprobleme

(Nur für Katalog-Synchronisierungen) Katalogstufe hat keinen Speicherplatz mehr

#### Schritt 3.3: Zeitplanung
Konfigurieren Sie abschließend Ihre Synchronisierung als einmalig oder wiederkehrend.

Einmalige Synchronisierungen können manuell oder über die API ausgelöst werden.

Wiederkehrende Synchronisierungen können eine Frequenz von alle 15 Minuten bis einmal pro Monat haben. Braze plant die wiederkehrende Synchronisierung in der UTC-Zeitzone.

{% endtab %}
{% tab Microsoft Fabric %}

#### Schritt 3.1: Synchronisierungsdetails konfigurieren und Verbindung testen

Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann aus den aktiven Quellen aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und klicken Sie auf **Test Connection**.

Sobald der Test erfolgreich war, wird eine Vorschau der Daten angezeigt. Wählen Sie **Next: Notifications**, um fortzufahren. Wenn die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{% alert note %}
Sie müssen eine Synchronisierung erfolgreich testen, bevor Sie zu den nächsten Schritten fortfahren können. Wenn Sie die Erstellungsseite für die Synchronisierung schließen müssen, klicken Sie auf **Save as draft**, um Ihren Fortschritt zu speichern.
{% endalert %}

#### Schritt 3.2: Benachrichtigungseinstellungen hinzufügen
Geben Sie Kontakt-E-Mail-Adressen für Synchronisierungs-Fehlerbenachrichtigungen ein. Braze verwendet diese Kontaktinformationen, um Benachrichtigungen über Integrationsfehler zu senden, z. B. unerwarteten Verlust des Tabellenzugriffs.

Kontakt-E-Mails erhalten nur Benachrichtigungen über globale oder Synchronisierungs-Level-Fehler wie fehlende Tabellen, Berechtigungen und andere. Sie erhalten keine Benachrichtigungen über Probleme auf Zeilenebene. Globale Fehler weisen auf kritische Probleme mit der Verbindung hin, die die Ausführung von Synchronisierungen verhindern.

Solche Probleme können Folgendes umfassen:

- Konnektivitätsprobleme
- Ressourcenmangel
- Berechtigungsprobleme

(Nur für Katalog-Synchronisierungen) Katalogstufe hat keinen Speicherplatz mehr

#### Schritt 3.3: Zeitplanung
Konfigurieren Sie abschließend Ihre Synchronisierung als einmalig oder wiederkehrend.

Einmalige Synchronisierungen können manuell oder über die API ausgelöst werden.

Wiederkehrende Synchronisierungen können eine Frequenz von alle 15 Minuten bis einmal pro Monat haben. Braze plant die wiederkehrende Synchronisierung in der UTC-Zeitzone.

{% endtab %}
{% endtabs %}

{% alert note %}
Sie müssen eine Integration erfolgreich testen, bevor sie vom Entwurfs- in den aktiven Zustand wechseln kann. Wenn Sie die Erstellungsseite schließen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.
{% endalert %}

## Zusätzliche Integrationen oder Nutzer:innen einrichten (optional) {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert sein, dass sie eine andere Tabelle synchronisiert. Beim Erstellen zusätzlicher Synchronisierungen können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Snowflake-Konto verbinden.

Wenn Sie dieselbe:n Nutzer:in und dieselbe Rolle über mehrere Integrationen hinweg wiederverwenden, müssen Sie den Public Key nicht erneut hinzufügen.
{% endtab %}
{% tab Redshift %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert sein, dass sie eine andere Tabelle synchronisiert. Beim Erstellen zusätzlicher Synchronisierungen können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Snowflake- oder Redshift-Konto verbinden.

Wenn Sie dieselbe:n Nutzer:in über mehrere Integrationen hinweg wiederverwenden, können Sie diese:n Nutzer:in im Braze-Dashboard erst löschen, wenn er/sie aus allen aktiven Synchronisierungen entfernt wurde.
{% endtab %}
{% tab BigQuery %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert sein, dass sie eine andere Tabelle synchronisiert. Beim Erstellen zusätzlicher Synchronisierungen können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben BigQuery-Konto verbinden.

Wenn Sie dieselbe:n Nutzer:in über mehrere Integrationen hinweg wiederverwenden, können Sie diese:n Nutzer:in im Braze-Dashboard erst löschen, wenn er/sie aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% tab Databricks %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert sein, dass sie eine andere Tabelle synchronisiert. Beim Erstellen zusätzlicher Synchronisierungen können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Databricks-Konto verbinden.

Wenn Sie dieselbe:n Nutzer:in über mehrere Integrationen hinweg wiederverwenden, können Sie diese:n Nutzer:in im Braze-Dashboard erst löschen, wenn er/sie aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% tab Microsoft Fabric %}

Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert sein, dass sie eine andere Tabelle synchronisiert. Beim Erstellen zusätzlicher Synchronisierungen können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Fabric-Konto verbinden.

Wenn Sie dieselbe:n Nutzer:in über mehrere Integrationen hinweg wiederverwenden, können Sie diese:n Nutzer:in im Braze-Dashboard erst löschen, wenn er/sie aus allen aktiven Synchronisierungen entfernt wurde.

{% endtab %}
{% endtabs %}

## Synchronisierung ausführen {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
Nach der Aktivierung wird Ihre Synchronisierung gemäß dem während der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans ausführen oder die neuesten Daten abrufen möchten, wählen Sie **Sync Now** aus. Diese Ausführung hat keinen Einfluss auf regulär geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab Redshift %}
Nach der Aktivierung wird Ihre Synchronisierung gemäß dem während der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans ausführen oder die neuesten Daten abrufen möchten, wählen Sie **Sync Now** aus. Diese Ausführung hat keinen Einfluss auf regulär geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab BigQuery %}

Nach der Aktivierung wird Ihre Synchronisierung gemäß dem während der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans ausführen oder die neuesten Daten abrufen möchten, wählen Sie **Sync Now** aus. Diese Ausführung hat keinen Einfluss auf regulär geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab Databricks %}

Nach der Aktivierung wird Ihre Synchronisierung gemäß dem während der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans ausführen oder die neuesten Daten abrufen möchten, wählen Sie **Sync Now** aus. Diese Ausführung hat keinen Einfluss auf regulär geplante zukünftige Synchronisierungen.

{% endtab %}
{% tab Microsoft Fabric %}

Nach der Aktivierung wird Ihre Synchronisierung gemäß dem während der Einrichtung konfigurierten Zeitplan ausgeführt. Wenn Sie die Synchronisierung außerhalb des normalen Testzeitplans ausführen oder die neuesten Daten abrufen möchten, wählen Sie **Sync Now** aus. Diese Ausführung hat keinen Einfluss auf regulär geplante zukünftige Synchronisierungen.

{% endtab %}

{% endtabs %}