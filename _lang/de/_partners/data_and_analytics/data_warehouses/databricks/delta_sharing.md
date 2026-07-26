---
nav_title: "Delta Sharing"
article_title: Databricks Delta Sharing
page_order: 0
description: "Dieser Referenzartikel behandelt Databricks Delta Sharing mit Braze (geschlossene Beta), mit dem Sie in Ihrem Databricks-Konto auf Braze-Engagement- und Campaign-Daten zugreifen können."
page_type: partner
search_tag: Partner
permalink: /delta_sharing/
hidden: true
---

# Databricks Delta Sharing

> Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) ermöglicht es Ihnen, Live-Daten zu Braze-Engagement und Campaigns sicher in Ihre Databricks-Umgebung zu teilen. Dieser Artikel beschreibt, wie die Datenfreigabe von Braze als Datenanbieter an Ihr Databricks-Konto als Empfänger funktioniert und wie Sie freigegebene Tabellen abfragen können.

{% alert important %}
Databricks Delta Sharing mit Braze befindet sich in der **geschlossenen Beta**. Verfügbarkeit, unterstützte Regionen und Produktverhalten können sich ändern. Kontaktieren Sie Ihren Braze-geschäftskunden-Success-Manager, um teilzunehmen oder zu bestätigen, ob dieses Feature für Ihren Workspace aktiviert ist.
{% endalert %}

Databricks Delta Sharing ist Teil der Braze-Datenverteilung. Einen vollständigen Überblick über die Optionen der Datenverteilung finden Sie unter [Datenverteilung]({{site.baseurl}}/user_guide/data/distribution).

## Delta Sharing einrichten {#set-up-delta-sharing}

Bei Databricks erfolgt die Datenfreigabe zwischen einem Datenanbieter und einem Datenempfänger. Ihr Braze-Konto ist der **Datenanbieter**, da es die Freigabe erstellt und sendet, und Ihr Databricks-Konto ist der **Datenempfänger**, da es die Freigabe nutzt, um einen Katalog zu erstellen, den Sie abfragen können. Weitere Details finden Sie in der Databricks-Dokumentation zum [Lesen von Daten, die über Databricks-zu-Databricks Delta Sharing geteilt werden (für Empfänger:innen)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html).

### Schritt 1: Freigabe in Braze konfigurieren {#step-1-configure-sharing-from-braze}

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenfreigabe** > **Databricks Delta Sharing**.
2. Geben Sie Ihren Databricks-Freigabebezeichner ein.
3. Wenn Sie fertig sind, wählen Sie **Create Datashare**. Braze sendet die Freigabe an Ihr Databricks-Konto.

### Schritt 2: Katalog in Databricks erstellen {#step-2-create-a-catalog-in-databricks}

1. Nach einigen Minuten sollten Sie die eingehende Freigabe in Ihrem Databricks-Konto erhalten.
2. Erstellen Sie mithilfe der eingehenden Freigabe einen Katalog, um die Tabellen anzuzeigen und abzufragen. Zum Beispiel:
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. Vergeben Sie Berechtigungen, damit die richtigen Nutzer:innen und Gruppen den neuen Katalog abfragen können.

{% alert warning %}
Freigegebene Daten sind in Ihrem Databricks-Workspace schreibgeschützt. Sie können sie wie andere Daten abfragen, aber Sie können Zeilen in den freigegebenen Tabellen über die Freigabe nicht ändern oder löschen.
{% endalert %}

## Nutzung und Visualisierung {#usage-and-visualization}

Nachdem die Datenfreigabe bereitgestellt wurde, erstellen Sie einen Katalog aus der eingehenden Freigabe, damit freigegebene Tabellen in Ihrem Databricks-Workspace erscheinen und wie andere dort gespeicherte Daten abgefragt werden können. Die freigegebenen Daten bleiben schreibgeschützt.

Ähnlich wie bei Currents können Sie Databricks Delta Sharing nutzen, um:

{% multi_lang_include partners/data_sharing_use_cases.md %}

Eine vollständige Liste der in Databricks verfügbaren Tabellen und Spalten finden Sie im Download der [Databricks-Rohtabellenschemata](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt) als Textdatei. Diese Datei spiegelt das Databricks-Delta-Sharing-Schema wider (zum Beispiel `DB_CREATED_AT` für den Aufnahmezeitpunkt). Sie ist nicht austauschbar mit den [Snowflake-Rohtabellenschemata](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) oder der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables), die Snowflake-Benennungen und -Felder beschreiben.

{% alert note %}
Während der geschlossenen Beta ist möglicherweise nicht jede in der Databricks-Schemadatei aufgeführte Tabelle in Ihrer Freigabe verfügbar. Spaltennamen und -typen können sich ebenfalls von der Snowflake-Datenfreigabe unterscheiden (zum Beispiel `DB_CREATED_AT` statt `SF_CREATED_AT`). Kontaktieren Sie Ihren Braze-geschäftskunden-Success-Manager, wenn Sie die aktuelle Tabellenliste für Ihren Workspace benötigen.
{% endalert %}

### Nutzer-ID-Schema {#user-id-schema}

Beachten Sie die folgenden Unterschiede zwischen den Benennungskonventionen von Braze und Databricks für Nutzer-IDs.

| Braze-Schema | Databricks-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | Der eindeutige Bezeichner, den Braze automatisch zuweist. |
| `external_id` | `EXTERNAL_USER_ID` | Der eindeutige Bezeichner eines Nutzerprofils, den Sie in Braze festlegen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Nutzer-ID-Schema" }

## Wichtige Informationen und Einschränkungen {#important-information-and-limitations}

### Verfügbarkeit der geschlossenen Beta {#closed-beta-availability}

Während der geschlossenen Beta enthält Ihre Freigabe möglicherweise nicht jede Tabelle in der Datei der [Databricks-Rohtabellenschemata](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt). Freigegebene Daten können sich auch in Spaltennamen und -typen von der Snowflake-Datenfreigabe unterscheiden. Zum Beispiel verwenden Databricks-Freigaben `DB_CREATED_AT` für den Aufnahmezeitpunkt, während Snowflake-Freigaben `SF_CREATED_AT` verwenden.

### Nicht abwärtskompatible versus abwärtskompatible Änderungen {#breaking-versus-non-breaking-changes}

#### Abwärtskompatible Änderungen {#non-breaking-changes}

Abwärtskompatible Änderungen können jederzeit auftreten und bieten in der Regel zusätzliche Funktionalität. Beispiele für abwärtskompatible Änderungen:

- Hinzufügen einer neuen Tabelle oder Ansicht
- Hinzufügen einer Spalte zu einer bestehenden Tabelle oder Ansicht

{% alert important %}
Da neue Spalten als abwärtskompatible Änderungen gelten, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzulisten, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie Ansichten erstellen, die Spalten explizit benennen, und diese Ansichten abfragen, anstatt die freigegebenen Tabellen direkt abzufragen.
{% endalert %}

#### Nicht abwärtskompatible Änderungen {#breaking-changes}

Wenn möglich, werden nicht abwärtskompatible Änderungen durch eine Ankündigung und eine Migrationsphase eingeleitet. Beispiele für nicht abwärtskompatible Änderungen:

- Entfernen einer Tabelle oder Ansicht
- Entfernen einer Spalte aus einer bestehenden Tabelle oder Ansicht
- Ändern des Typs oder der Nullbarkeit einer bestehenden Spalte

### Databricks-Regionen {#databricks-regions}

Während der geschlossenen Beta können unterstützte Cloud-Anbieter und Regionen je nach Workspace und Rollout variieren. Kontaktieren Sie Ihren Braze-geschäftskunden-Success-Manager für die Optionen, die für Ihr Konto gelten.

### Aufbewahrungsrichtlinie {#retention-policy}

Während der geschlossenen Beta kann das historische Backfill über das Standard-Aufbewahrungsfenster hinaus eingeschränkt sein.

Sie können die Daten der letzten zwei Jahre für jedes Ereignis in der entsprechenden `USERS_*_SHARED`-Ansicht abfragen.

### Einhaltung der Datenschutz-Grundverordnung (DSGVO) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Abfrage freigegebener Daten: `TIME` und Abfrage-Performance {#querying-shared-data-time-and-query-performance}

Ereignisdaten in den Datenfreigabe-Ansichten (zum Beispiel `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) sind nach dem Feld `TIME` geclustert. Wenn Sie nach dem Zeitpunkt des Ereignisses filtern, verwenden Sie `TIME` als bevorzugten Filter. Abfragen, die Zeilen mithilfe von `TIME` einschränken, sind in der Regel performanter als Abfragen, die nach `DB_CREATED_AT` filtern, da das Clustering am Ereigniszeitpunkt ausgerichtet ist.

| Feld | Bedeutung |
| ----- | ------- |
| `TIME` | Unix-Zeitstempel, zu dem das Ereignis stattfand. Bevorzugen Sie dieses Feld beim Filtern nach Vorkommen. |
| `DB_CREATED_AT` | Zeitstempel, zu dem die Zeile in Databricks geladen wurde (Aufnahmezeitpunkt). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abfrage freigegebener Daten: TIME und Abfrage-Performance" }

### Geschwindigkeit, Performance und Kosten von Abfragen {#speed-performance-and-cost-of-queries}

Geschwindigkeit, Performance und Kosten jeder Abfrage, die Sie auf den Daten ausführen, hängen von der Größe des SQL-Warehouse ab, das Sie verwenden. Je nachdem, auf wie viele Daten Sie zugreifen, benötigen Sie möglicherweise ein größeres Warehouse, damit die Abfrage erfolgreich abgeschlossen werden kann. Weitere Informationen finden Sie in der Databricks-Dokumentation zum [Erstellen und Konfigurieren eines SQL-Warehouse](https://docs.databricks.com/en/compute/sql-warehouse/create.html) (einschließlich Clustergröße und Skalierung).