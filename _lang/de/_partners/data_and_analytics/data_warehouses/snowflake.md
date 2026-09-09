---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Snowflake und behandelt sowohl Data Sharing (Braze zu Snowflake) als auch Cloud-Datenaufnahme."
page_type: partner
search_tag: Partner
---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) ist ein speziell entwickeltes SQL Data Warehouse in der Cloud, das als SaaS (SaaS) angeboten wird. Snowflake bietet ein Data Warehouse, das schneller, benutzerfreundlicher und wesentlich flexibler ist als herkömmliche Data-Warehouse-Angebote. Mit der einzigartigen und patentierten Architektur von Snowflake ist es ein Leichtes, all Ihre Daten zu sammeln, schnelle Analytics zu ermöglichen und datengestützte Insights für alle Ihre Nutzer:innen zu gewinnen.

Braze bietet zwei Integrationen mit Snowflake an. Zusammen ermöglichen sie eine vollständige, bidirektionale Datenpipeline zwischen Ihren Braze- und Snowflake-Umgebungen.

## Eine Integration auswählen {#choosing-an-integration}

### Datenfreigabe (Braze an Snowflake) {#data-sharing-braze-to-snowflake}

Snowflake [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) bietet Ihnen sicheren Realtime-Zugriff auf Braze-Engagement- und Kampagnendaten direkt in Ihrer Snowflake-Instanz. Es werden keine Daten zwischen Konten kopiert oder übertragen – die gesamte Freigabe erfolgt über die einzigartige Dienstschicht und den Metadatenspeicher von Snowflake.

**Verwenden Sie Datenfreigabe, wenn Sie Folgendes tun möchten:**
- Braze-Ereignis- und Kampagnendaten mit Snowflake SQL abfragen
- Komplexe Berichte erstellen und Attribution-Modellierung durchführen
- Braze-Daten mit anderen Daten in Ihrem Snowflake Data Warehouse verknüpfen
- Ihre Engagement-Daten über Kanäle, Branchen und Geräteplattformen hinweg vergleichen

Einrichtungsanweisungen finden Sie unter [Snowflake Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing).

### Cloud-Datenaufnahme (Snowflake an Braze) {#cloud-data-ingestion-snowflake-to-braze}

[Cloud-Datenaufnahme (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) ermöglicht es Ihnen, Daten aus Ihrer Snowflake-Instanz direkt mit Braze zu synchronisieren. So können Sie Nutzer:innen-Attribute, Ereignisse und Käufe in Braze mit Ihrem Data Warehouse als zentraler Datenquelle aktuell halten.

**Verwenden Sie Cloud-Datenaufnahme, wenn Sie Folgendes tun möchten:**
- Nutzer:innen-Attribute von Snowflake mit Braze-Nutzerprofilen synchronisieren
- Ereignis- oder Kaufdaten von Snowflake an Braze senden
- Braze mit Datentransformationen synchron halten, die in Ihrem Data Warehouse stattfinden
- Den Aufbau und die Wartung benutzerdefinierter ETL-Pipelines von Snowflake zu Braze vermeiden

Weitere Informationen zur Datenfreigabe von Snowflake finden Sie unter [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie Folgendes erfüllen:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Um auf dieses Feature in Braze zuzugreifen, müssen Sie sich an Ihren Braze-Konto- oder Customer-Success-Manager wenden. |
| Braze-Workspace-Berechtigungen | [Currents-Integrationen anzeigen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), um die Datenfreigabe anzuzeigen. [Currents-Integrationen bearbeiten]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), um eine Datenfreigabe zu erstellen, zu aktualisieren oder zu löschen. |
| Snowflake-Konto | Ein Snowflake-Konto mit `admin`-Berechtigungen. Für Kund:innen ohne HIPAA-Anforderungen wird die Snowflake Standard oder Enterprise Edition unterstützt. Für HIPAA-konforme Datenfreigabe ist die Business Critical Edition erforderlich. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Secure Data Sharing einrichten {#setting-up-secure-data-sharing}

Bei Snowflake erfolgt die Datenfreigabe zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Datenkonsumenten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). In diesem Kontext ist Ihr Braze-Konto der Datenanbieter, da es den Datashare erstellt und sendet – während Ihr Snowflake-Konto der Datenkonsument ist, da es den Datashare nutzt, um eine Datenbank zu erstellen. Weitere Informationen finden Sie unter [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Schritt 1: Datashare von Braze senden {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Schritt 2: Datenbank in Snowflake erstellen {#step-2-create-the-database-in-snowflake}

1. Nach einigen Minuten sollten Sie den eingehenden Datashare in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mithilfe des eingehenden Datashare eine Datenbank, um die Tabellen anzuzeigen und abzufragen. Zum Beispiel:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Vergeben Sie Berechtigungen, um die neue Datenbank abzufragen.

{% alert warning %}
Wenn Sie einen Share im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank entfernen und sie mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um den eingehenden Share abzufragen.
Wenn Sie mehrere Workspaces haben, die Daten an dasselbe Snowflake-Konto freigeben, finden Sie in den [Snowflake FAQ zur Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) Hinweise zur Verwaltung von Multi-Workspace-Konfigurationen.
{% endalert %}

## Nutzung und Visualisierung {#usage-and-visualization}

Nachdem die Datenfreigabe bereitgestellt wurde, müssen Sie eine Datenbank aus der eingehenden Datenfreigabe erstellen, damit alle freigegebenen Tabellen in Ihrer Snowflake-Instanz angezeigt werden und genauso abgefragt werden können wie alle anderen Daten, die Sie in Ihrer Instanz speichern. Beachten Sie jedoch, dass die freigegebenen Daten schreibgeschützt sind und nur abgefragt, aber in keiner Weise geändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Snowflake Secure Data Sharing verwenden, um:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Eine vollständige Liste der verfügbaren Tabellen und Spalten finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Snowflake Data Sharing umfasst alle Tabellen in dieser Referenz sowie zusätzliche Snowflake-exklusive Tabellen für Snapshots, Campaign- und Canvas-Changelogs, Agent-Konsolenereignisse und Nachrichtenwiederholungsereignisse.

Sie können auch [die Rohtabellenschemata herunterladen](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) (als Textdatei).

### Nutzer:innen-ID-Schema {#user-id-schema}

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Nutzer:innen-IDs.

| Braze-Schema | Snowflake-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von der Kundschaft festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen-ID-Schema" }

## Wichtige Informationen und Einschränkungen {#important-information-and-limitations}

### Nicht-unterbrechende vs. unterbrechende Änderungen {#breaking-versus-non-breaking-changes}

#### Nicht-unterbrechende Änderungen {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Da neue Spalten als nicht-unterbrechende Änderungen gelten, empfiehlt Braze dringend, in jeder Abfrage die gewünschten Spalten explizit aufzulisten, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie Ansichten erstellen, die Spalten explizit benennen, und dann diese Ansichten anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Unterbrechende Änderungen {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflake-Regionen {#snowflake-regions}

Braze hostet derzeit alle Daten auf Nutzer:innen-Ebene in den Snowflake-AWS-Regionen US East-1, EU-Central (Frankfurt), AP-Northeast-1 (Tokio), AP-Southeast-2 (Sydney) und AP-Southeast-3 (Jakarta). Für Nutzer:innen außerhalb dieser Regionen kann Braze gemeinsamen Kund:innen, die ihre Snowflake-Infrastruktur in einer beliebigen AWS-, Azure- oder GCP-Region betreiben, Data Sharing bereitstellen.

### Datenaufbewahrung {#data-retention}

#### Aufbewahrungsrichtlinie {#retention-policy}

Alle Daten, die älter als zwei Jahre sind, werden archiviert und in den Langzeitspeicher verschoben. Im Rahmen des Archivierungsprozesses werden alle Ereignisse anonymisiert und alle Felder mit persönlich identifizierbaren Informationen (PII) entfernt (dies umfasst auch optional PII-Felder wie `properties`). Archivierte Daten enthalten weiterhin das Feld `user_id`, das nutzer:innenübergreifende Analysen über alle Ereignisdaten ermöglicht.

Sie können für jedes Ereignis die aktuellsten zwei Jahre an Daten in der entsprechenden `USERS_*_SHARED`-Ansicht abfragen. Zusätzlich verfügt jedes Ereignis über eine `USERS_*_SHARED_ALL`-Ansicht, die abgefragt werden kann, um sowohl anonymisierte als auch nicht-anonymisierte Daten abzurufen.

#### Historische Daten {#historical-data}

Das Archiv historischer Ereignisdaten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake gespeichert hat, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten leicht anders aussehen oder Nullwerte enthalten (da zu diesem Zeitpunkt nicht alle verfügbaren Felder befüllt wurden). Es ist davon auszugehen, dass Ergebnisse, die Daten vor August 2019 enthalten, leicht von den Erwartungen abweichen können.

### Einhaltung der Datenschutz-Grundverordnung (DSGVO) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Abfrage gemeinsam genutzter Daten: `TIME` und Abfrage-Performance {#querying-shared-data-time-and-query-performance}

Ereignisdaten in den Data-Sharing-Ansichten (z. B. `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) sind **nach dem Feld `TIME` geclustert**. Wenn Sie nach dem **Zeitpunkt des Ereignisses** filtern, verwenden Sie **`TIME`** als bevorzugten Filter. Abfragen, die Zeilen mit **`TIME`** einschränken, sind in der Regel **performanter** als Abfragen, die nach **`SF_CREATED_AT`** filtern, da das Clustering auf der Ereigniszeit basiert.

| Feld | Bedeutung |
| ----- | ------- |
| `TIME` | Unix-Zeitstempel, zu dem das Ereignis stattgefunden hat. Bevorzugen Sie dieses Feld, wenn Sie nach dem Zeitpunkt des Auftretens filtern. |
| `SF_CREATED_AT` | Zeitstempel, zu dem die Zeile in Snowflake geladen wurde (Aufnahmezeit). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abfrage gemeinsam genutzter Daten: TIME und Abfrage-Performance" }

### Geschwindigkeit, Performance und Kosten von Abfragen {#speed-performance-cost-of-queries}

Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, werden durch die Warehouse-Größe bestimmt, die Sie zur Abfrage der Daten verwenden. In einigen Fällen kann es je nach Umfang der für die Analyse abgerufenen Daten erforderlich sein, eine größere Warehouse-Größe zu verwenden, damit die Abfrage erfolgreich ist. Snowflake bietet hervorragende Ressourcen dazu, wie Sie die optimale Größe bestimmen können, darunter [Overview of warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Warehouse considerations](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Beispielabfragen, die Sie bei der Einrichtung von Snowflake als Referenz verwenden können, finden Sie in unseren [Beispielabfragen]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) und [ETL-Ereignis-Pipeline einrichten]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).

Anweisungen zur Einrichtung finden Sie unter [Cloud-Datenaufnahme: Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).