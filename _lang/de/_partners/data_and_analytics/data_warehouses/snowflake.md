---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Snowflake und behandelt sowohl Data Sharing (Braze zu Snowflake) als auch Cloud-Datenaufnahme."
page_type: partner
search_tag: Partner
---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) ist ein speziell entwickeltes SQL Data Warehouse in der Cloud, das als SaaS or Software-as-a-Service or Software-as-a-Service (SaaS or Software-as-a-Service) angeboten wird. Snowflake bietet ein Data Warehouse, das schneller, benutzerfreundlicher und wesentlich flexibler ist als herkömmliche Data-Warehouse-Angebote. Mit der einzigartigen und patentierten Architektur von Snowflake ist es ein Leichtes, all Ihre Daten zu sammeln, schnelle Analytics zu ermöglichen und datengestützte Insights für alle Ihre Nutzer:innen zu gewinnen.

Braze bietet zwei Integrationen mit Snowflake an. Zusammen ermöglichen sie eine vollständige, bidirektionale Datenpipeline zwischen Ihren Braze- und Snowflake-Umgebungen.

## Eine Integration auswählen {#choosing-an-integration}

### Datenfreigabe (Braze an Snowflake) {#data-sharing-braze-to-snowflake}

Snowflake [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) bietet Ihnen sicheren Realtime-Zugriff auf Braze-Engagement- und Kampagnendaten direkt in Ihrer Snowflake-Instanz. Es werden keine Daten zwischen Konten kopiert oder übertragen – die gesamte Freigabe erfolgt über die einzigartige Services-Schicht und den Metadatenspeicher von Snowflake.

**Verwenden Sie Datenfreigabe, wenn Sie Folgendes möchten:**
- Braze-Ereignis- und Kampagnendaten mit Snowflake SQL abfragen
- Komplexe Berichte erstellen und Attribution-Modelle durchführen
- Braze-Daten mit anderen Daten in Ihrem Snowflake Data Warehouse verknüpfen
- Ihre Engagement-Daten über Kanäle, Branchen und Geräteplattformen hinweg benchmarken

Eine Einrichtungsanleitung finden Sie unter [Snowflake Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing).

### Cloud-Datenaufnahme (Snowflake an Braze) {#cloud-data-ingestion-snowflake-to-braze}

[Cloud-Datenaufnahme (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) ermöglicht es Ihnen, Daten aus Ihrer Snowflake-Instanz direkt mit Braze zu synchronisieren. So können Sie Nutzer:innen-Attribute, Ereignisse und Käufe in Braze stets mit Ihrem Data Warehouse als zentraler Datenquelle auf dem neuesten Stand halten.

**Verwenden Sie Cloud-Datenaufnahme, wenn Sie Folgendes möchten:**
- Nutzer:innen-Attribute von Snowflake mit Braze-Nutzerprofilen synchronisieren
- Ereignis- oder Kaufdaten aus Snowflake an Braze senden
- Braze mit Datentransformationen synchron halten, die in Ihrem Data Warehouse stattfinden
- Die Erstellung und Wartung benutzerdefinierter ETL or Extract, Transform, Load-Pipelines von Snowflake zu Braze vermeiden

Weitere Informationen zur Datenfreigabe von Snowflake finden Sie unter [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Feature nutzen können, müssen Sie Folgendes abschließen:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Um auf dieses Feature in Braze zuzugreifen, müssen Sie sich an Ihren Braze-Konto- oder CSM or Customer-Success-Manager or Customer-Success-Manager:in wenden. |
| Snowflake-Konto | Ein Snowflake-Konto mit `admin`-Berechtigungen. Für Nicht-HIPAA-Kund:innen wird die Snowflake Standard oder Enterprise Edition unterstützt. Für HIPAA-konforme Datenfreigabe ist die Business Critical Edition erforderlich. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Einrichtung von Secure Data Sharing {#setting-up-secure-data-sharing}

Bei Snowflake erfolgt die Datenfreigabe zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Datenkonsumenten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). In diesem Kontext ist Ihr Braze-Konto der Datenanbieter, da es den Datashare erstellt und sendet – während Ihr Snowflake-Konto der Datenkonsument ist, da es den Datashare nutzt, um eine Datenbank zu erstellen. Weitere Informationen finden Sie unter [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Schritt 1: Den Datashare von Braze senden {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Schritt 2: Die Datenbank in Snowflake erstellen {#step-2-create-the-database-in-snowflake}

1. Nach einigen Minuten sollten Sie den eingehenden Datashare in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mithilfe des eingehenden Datashares eine Datenbank, um die Tabellen anzuzeigen und abzufragen. Zum Beispiel:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Erteilen Sie Berechtigungen, um die neue Datenbank abzufragen.

{% alert warning %}
Wenn Sie einen Share im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank verwerfen und sie mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um den eingehenden Share abzufragen.
Wenn Sie mehrere Workspaces haben, die Daten an dasselbe Snowflake-Konto freigeben, lesen Sie die [Snowflake FAQ zur Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) für Hinweise zur Verwaltung von Multi-Workspace-Konfigurationen.
{% endalert %}

## Nutzung und Visualisierung {#usage-and-visualization}

Nachdem der Data Share bereitgestellt wurde, müssen Sie eine Datenbank aus dem eingehenden Data Share erstellen, damit alle freigegebenen Tabellen in Ihrer Snowflake-Instanz erscheinen und wie alle anderen Daten, die Sie in Ihrer Instanz speichern, abgefragt werden können. Beachten Sie jedoch, dass die freigegebenen Daten schreibgeschützt sind und nur abgefragt, aber in keiner Weise geändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Snowflake Secure Data Sharing verwenden, um:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Eine vollständige Liste der verfügbaren Tabellen und Spalten finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Snowflake Data Sharing umfasst alle Tabellen in dieser Referenz sowie zusätzliche Snowflake-exklusive Tabellen für Snapshots, Campaign- und Canvas-Changelogs, Agent-Konsolen-Ereignisse und Nachrichten-Wiederholungsereignisse.

Sie können auch [die Rohtabellenschemata herunterladen](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) als Textdatei.

### Nutzer:innen-ID-Schema {#user-id-schema}

Beachten Sie die folgenden Unterschiede zwischen den Braze- und Snowflake-Benennungskonventionen für Nutzer:innen-IDs.

| Braze-Schema | Snowflake-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von den Kund:innen festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer:innen-ID-Schema" }

## Wichtige Informationen und Einschränkungen {#important-information-and-limitations}

### Nicht-kompatible versus kompatible Änderungen {#breaking-versus-non-breaking-changes}

#### Kompatible Änderungen {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Da neue Spalten als kompatible Änderungen gelten, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzulisten, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie Views erstellen, die Spalten explizit benennen, und dann diese Views anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Nicht-kompatible Änderungen {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflake-Regionen {#snowflake-regions}

Braze hostet derzeit alle Daten auf Nutzer:innen-Ebene in den Snowflake-Regionen AWS US East-1, EU-Central (Frankfurt), AP-Northeast-1 (Tokio), AP-Southeast-2 (Sydney) und AP-Southeast-3 (Jakarta). Für Nutzer:innen außerhalb dieser Regionen kann Braze Data Sharing für gemeinsame Kund:innen bereitstellen, die ihre Snowflake-Infrastruktur in beliebigen AWS-, Azure- oder GCP-Regionen betreiben.

### Datenaufbewahrung {#data-retention}

#### Aufbewahrungsrichtlinie {#retention-policy}

Alle Daten, die älter als zwei Jahre sind, werden archiviert und in den Langzeitspeicher verschoben. Im Rahmen des Archivierungsprozesses werden alle Ereignisse anonymisiert und alle Felder mit persönlich identifizierbaren Informationen (PII) entfernt (dazu gehören auch optionale PII-Felder wie `properties`). Archivierte Daten enthalten weiterhin das Feld `user_id`, das nutzer:innenbezogene Analysen über alle Ereignisdaten hinweg ermöglicht.

Sie können die jeweils letzten zwei Jahre an Daten für jedes Ereignis in der entsprechenden `USERS_*_SHARED`-View abfragen. Zusätzlich verfügt jedes Ereignis über eine `USERS_*_SHARED_ALL`-View, die abgefragt werden kann, um sowohl anonymisierte als auch nicht-anonymisierte Daten zurückzugeben.

#### Historische Daten {#historical-data}

Das Archiv historischer Ereignisdaten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake gespeichert hat, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten leicht anders aussehen oder Nullwerte enthalten (da wir zu diesem Zeitpunkt nicht alle verfügbaren Felder befüllt haben). Gehen Sie am besten davon aus, dass Ergebnisse, die Daten vor August 2019 umfassen, leicht von den Erwartungen abweichen können.

### Einhaltung der Datenschutz-Grundverordnung (DSGVO) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Abfrage gemeinsam genutzter Daten: `TIME` und Abfrage-Performance {#querying-shared-data-time-and-query-performance}

Ereignisdaten in den Data-Sharing-Views (z. B. `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) sind **nach dem Feld `TIME` geclustert**. Wenn Sie nach dem **Zeitpunkt des Ereignisses** filtern, verwenden Sie **`TIME`** als bevorzugten Filter. Abfragen, die Zeilen mithilfe von **`TIME`** einschränken, sind in der Regel **performanter** als Abfragen, die auf **`SF_CREATED_AT`** filtern, da das Clustering an der Ereigniszeit ausgerichtet ist.

| Feld | Bedeutung |
| ----- | ------- |
| `TIME` | Unix-Zeitstempel, zu dem das Ereignis stattgefunden hat. Bevorzugen Sie dieses Feld, wenn Sie nach dem Zeitpunkt des Vorkommens filtern. |
| `SF_CREATED_AT` | Zeitstempel, zu dem die Zeile in Snowflake geladen wurde (Aufnahmezeit). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abfrage gemeinsam genutzter Daten: TIME und Abfrage-Performance" }

### Geschwindigkeit, Performance und Kosten von Abfragen {#speed-performance-cost-of-queries}

Die Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, werden durch die Warehouse-Größe bestimmt, die Sie für die Abfrage verwenden. In einigen Fällen – abhängig davon, wie viel Daten Sie für Analysen abrufen – kann es notwendig sein, eine größere Warehouse-Größe zu verwenden, damit die Abfrage erfolgreich ausgeführt werden kann. Snowflake bietet hervorragende Ressourcen dazu, wie Sie die richtige Größe bestimmen, darunter [Übersicht über Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Warehouse-Überlegungen](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Beispielabfragen, die Sie bei der Einrichtung von Snowflake als Referenz verwenden können, finden Sie in unseren Beispielen für [Beispielabfragen]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) und die [ETL or Extract, Transform, Load-Ereignis-Pipeline einrichten]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).

Anweisungen zur Einrichtung finden Sie unter [Cloud Data Ingestion: Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).