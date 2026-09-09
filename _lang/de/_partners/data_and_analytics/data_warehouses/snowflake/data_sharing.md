---
nav_title: "Datenfreigabe"
article_title: Snowflake Datenfreigabe
page_order: 0
description: "Dieser Referenzartikel behandelt die Snowflake Secure Data Sharing-Integration, mit der Sie direkt in Ihrer Snowflake-Instanz auf Braze-Engagement- und Kampagnendaten zugreifen können."
page_type: partner
search_tag: Partner

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake Datenfreigabe

> Snowflake [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) ermöglicht es Braze, Ihnen sicheren Zugriff auf Daten in unserem Snowflake-Portal zu gewähren – ohne Reibungsverluste oder Verzögerungen im Workflow, Fehlerquellen und unnötige Kosten, die bei typischen Datenanbieter-Beziehungen entstehen. Data Sharing kann über die folgende Integration oder über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts) eingerichtet werden.

Snowflake Data Sharing ist Teil der Braze-Datenverteilung. Einen vollständigen Überblick über die Optionen der Datenverteilung finden Sie unter [Datenverteilung]({{site.baseurl}}/user_guide/data/distribution).

{% alert tip %}
**Sie möchten auf Snowflake-Daten zugreifen, ohne ein Snowflake-Konto zu benötigen?**<br>Informieren Sie sich über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts). Mit Reader Accounts erstellt Braze ein Konto, teilt Ihre Daten darin und stellt Ihnen Zugangsdaten zur Verfügung, mit denen Sie sich anmelden und auf Ihre Daten zugreifen können. Dabei werden sämtliche Kosten für Data Sharing und Nutzung vollständig von Braze übernommen.
{% endalert %}

## Berechtigungen für die Datenverteilung {#data-distribution-entitlements}

Ihre Berechtigung für die Datenverteilung bestimmt, welche Ereignistypen in Ihrem Data Share verfügbar sind. Braze organisiert Ereignisse in die folgenden Kategorien:

| Berechtigung | Ereigniskategorie | Beschreibung | Referenz zum Ereignis-Glossar |
|------------|----------------|-------------|--------------------------|
| **Engagement-Ereignisse** | Nachrichten-Engagement-Ereignisse | Ereignisse im Zusammenhang mit Nachrichtenversand, Zustellungen, Öffnungen, Klicks, Bounces und anderen Messaging-Kanal-Interaktionen | [Nachrichten-Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **Kundenverhalten-Ereignisse** | Nachrichten-Engagement-Ereignisse und Kundenverhalten-Events | Umfasst alle Nachrichten-Engagement-Ereignisse sowie Ereignisse im Zusammenhang mit Käufen, angepassten Events, Sitzungen, Attribution und In-App-Nutzeraktionen | [Nachrichten-Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten und Nutzerereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **Nutzerprofile und Attribute** | Nachrichten-Engagement-Ereignisse, Kundenverhalten-Events und Nutzerprofil-Ereignisse | Umfasst Nachrichten-Engagement-Ereignisse und Kundenverhalten-Events sowie Ereignisse im Zusammenhang mit Änderungen an Nutzerprofilen und Attributen | [Nachrichten-Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten und Nutzerereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [Nutzerprofil-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Berechtigungen für die Datenverteilung" }

Bei Fragen dazu, welche Ereignisse in Ihrer Berechtigung enthalten sind, wenden Sie sich an Ihren Braze-Konto- oder Customer-Success-Manager.

## Über Secure Data Sharing {#about-secure-data-sharing}

Beim Data Sharing werden keine Daten zwischen Konten kopiert oder übertragen. Das gesamte Sharing wird über die einzigartige Dienstschicht und den Metadatenspeicher von Snowflake realisiert. Dies ist ein wichtiges Konzept, da gemeinsam genutzte Daten keinen Speicherplatz in Ihrem Konto belegen und daher nicht zu Ihren monatlichen Speichergebühren beitragen. Die **einzigen** Kosten entstehen durch die Computing-Ressourcen (z. B. virtuelle Warehouses), die für die Abfrage der gemeinsam genutzten Daten verwendet werden.

Darüber hinaus kann der Zugriff auf von Braze geteilte Daten mithilfe der integrierten Rollen- und Berechtigungsfunktionen von Snowflake über die bereits für Ihr Snowflake-Konto und die darin enthaltenen Daten vorhandenen Zugriffskontrollen gesteuert und verwaltet werden. Der Zugriff kann auf die gleiche Weise wie bei Ihren eigenen Daten eingeschränkt und überwacht werden.

- **Schneller zu Insights**<br>Verabschieden Sie sich von ETL-Prozessen, deren Aufbau Wochen dauert. Die einzigartigen Architekturen von Braze und Snowflake machen alle Customer-Engagement- und Campaign-Daten sofort zugänglich und abfragbar, sobald sie im Data Lake eintreffen. Es werden keine Daten kopiert oder verschoben, sodass Sie Kundenerlebnisse nur auf Basis der relevantesten und aktuellsten Informationen bereitstellen können.
- **Datensilos aufbrechen**<br>Erstellen Sie eine ganzheitliche Sicht auf Ihre Kund:innen über alle Kanäle und Plattformen hinweg. Data Sharing macht es einfacher denn je, Ihre Braze-Customer-Engagement-Daten mit all Ihren anderen Snowflake-Daten zu verknüpfen – und so umfassendere Insights aus einer einzigen, zuverlässigen Quelle der Wahrheit zu gewinnen.
- **Sehen Sie, wie Ihr Engagement im Vergleich abschneidet**<br>Optimieren Sie Ihre Customer-Engagement-Strategien mit Braze Benchmarks. Dieses interaktive Tool, unterstützt von Braze und Snowflake, ermöglicht es Ihnen, die Engagement-Daten Ihrer Marke mit Benchmarks über Kanäle, Branchen und Geräteplattformen hinweg zu vergleichen.

Weitere Informationen zum Data Sharing von Snowflake finden Sie unter [Einführung in Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Wenden Sie sich an Ihre:n Braze-Kundenbetreuer:in oder Customer-Success-Manager:in, um Data Sharing einzurichten. |
| Braze-Workspace-Berechtigungen | [View Currents Integrations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), um Data Sharing anzuzeigen. [Edit Currents Integrations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), um eine Datenfreigabe zu erstellen, zu aktualisieren oder zu löschen. |
| Snowflake-Konto | Ein Snowflake-Konto mit `admin`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Einrichtung von Secure Data Sharing {#setting-up-secure-data-sharing}

Bei Snowflake erfolgt Data Sharing zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Datenkonsumenten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). In diesem Kontext ist Ihr Braze-Konto der Datenanbieter, da es den Datashare erstellt und sendet&#8212;während Ihr Snowflake-Konto der Datenkonsument ist, da es den Datashare nutzt, um eine Datenbank zu erstellen. Weitere Details finden Sie unter [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Schritt 1: Datashare von Braze senden {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Schritt 2: Datenbank in Snowflake erstellen {#step-2-create-the-database-in-snowflake}

1. Nach einigen Minuten sollten Sie den eingehenden Datashare in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mithilfe des eingehenden Datashare eine Datenbank, um die Tabellen anzuzeigen und abzufragen. Beispiel:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Vergeben Sie Berechtigungen, um die neue Datenbank abzufragen.

{% alert warning %}
Wenn Sie einen Share im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank löschen und mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um den eingehenden Share abzufragen.
Wenn Sie Daten aus mehreren Workspaces an dasselbe Snowflake-Konto teilen, lesen Sie die [Snowflake Data Sharing FAQs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) für Hinweise zur Verwaltung von Multi-Workspace-Konfigurationen.
{% endalert %}

## Nutzung und Visualisierung {#usage-and-visualization}

Nachdem der Datenzugriff eingerichtet wurde, erstellen Sie eine Datenbank aus dem eingehenden Data Share, sodass alle geteilten Tabellen in Ihrer Snowflake-Instanz erscheinen und genauso abgefragt werden können wie alle anderen Daten, die Sie in Ihrer Instanz speichern. Beachten Sie jedoch, dass die geteilten Daten schreibgeschützt sind und nur abgefragt, aber in keiner Weise geändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Ihr Snowflake Secure Data Sharing verwenden, um:

{% multi_lang_include partners/data_sharing_use_cases.md %}

[Laden Sie die Rohdaten-Tabellenschemata herunter.](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

{% alert note %}
Der Download der Rohdatenschemata enthält keine Ansichten für Nutzerprofilattribute. Die vollständigen Schemata und Nutzungshinweise für `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`, `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` und verwandte Nutzerattribut-Ansichten finden Sie unter [Nutzerprofilattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

### Nutzer-ID-Schema {#user-id-schema}

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Nutzer-IDs.

| Braze-Schema | Snowflake-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von dem/der Kund:in festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer-ID-Schema" }

## Wichtige Informationen und Einschränkungen {#important-information-and-limitations}

### Nicht rückwärtskompatible versus rückwärtskompatible Änderungen {#breaking-versus-non-breaking-changes}

#### Rückwärtskompatible Änderungen {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Da neue Spalten als rückwärtskompatible Änderungen gelten, empfiehlt Braze dringend, die gewünschten Spalten in jeder Abfrage explizit aufzulisten, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie Views erstellen, die Spalten explizit benennen, und dann diese Views anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Nicht rückwärtskompatible Änderungen {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflake-Regionen {#snowflake-regions}

Braze hostet derzeit alle nutzerbezogenen Daten in diesen Snowflake-AWS-Regionen:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Northeast-1 (Tokio)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)

Für Nutzer:innen außerhalb dieser Regionen kann Braze Data Sharing für gemeinsame Kund:innen bereitstellen, die ihre Snowflake-Infrastruktur in einer beliebigen AWS-, Azure- oder GCP-Region betreiben.

### Datenaufbewahrung {#data-retention}

#### Aufbewahrungsrichtlinie {#retention-policy}

Alle Daten, die älter als zwei Jahre sind, werden archiviert und in den Langzeitspeicher verschoben. Im Rahmen des Archivierungsprozesses werden alle Events anonymisiert und alle personenbezogenen (PII) sensiblen Felder entfernt (dies umfasst auch optional personenbezogene Felder wie `properties`). Archivierte Daten enthalten weiterhin das Feld `user_id`, das nutzerbezogene Analytics über alle Event-Daten hinweg ermöglicht.

Sie können die aktuellsten zwei Jahre an Daten für jedes Event in der entsprechenden `USERS_*_SHARED`-View abfragen. Zusätzlich verfügt jedes Event über eine `USERS_*_SHARED_ALL`-View, die sowohl anonymisierte als auch nicht anonymisierte Daten zurückgibt.

#### Historische Daten {#historical-data}

Das Archiv historischer Event-Daten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake gespeichert hat, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten leicht anders aussehen oder Null-Werte aufweisen (da zu diesem Zeitpunkt noch nicht alle verfügbaren Felder befüllt wurden). Es ist davon auszugehen, dass Ergebnisse, die Daten vor August 2019 enthalten, leicht von den Erwartungen abweichen können.

### Konformität mit der Datenschutz-Grundverordnung (DSGVO) {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### Geschwindigkeit, Performance und Kosten von Abfragen {#speed-performance-cost-of-queries}

Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, werden durch die Warehouse-Größe bestimmt, die Sie zur Abfrage der Daten verwenden. In einigen Fällen, abhängig davon, wie viele Daten Sie für die Analyse abrufen, kann es erforderlich sein, eine größere Warehouse-Größe zu verwenden, damit die Abfrage erfolgreich ist. Snowflake bietet hervorragende Ressourcen darüber, wie Sie die geeignete Größe bestimmen können, darunter [Übersicht über Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Überlegungen zu Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Für eine Sammlung von Beispielabfragen, die Sie bei der Einrichtung von Snowflake als Referenz verwenden können, sehen Sie sich unsere Beispiele für [Beispielabfragen]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) und [ETL-Event-Pipeline-Einrichtung]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup) an.
{% endalert %}