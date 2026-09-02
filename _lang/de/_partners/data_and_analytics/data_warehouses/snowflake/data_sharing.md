---
nav_title: "Datenfreigabe"
article_title: Snowflake Datenfreigabe
page_order: 0
description: "Dieser Referenzartikel behandelt die Snowflake Secure Data Sharing-Integration, mit der Sie direkt in Ihrer Snowflake-Instanz auf Braze-Engagement- und Kampagnendaten zugreifen können."
page_type: partner
search_tag: Partner

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake Datenfreigabe {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsnowflake-secure-data-sharing-via-braze-stylefloatrightwidth120pxborder0-classnoimgbordersnowflake-data-sharing}

> Snowflake [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) ermöglicht es Braze, Ihnen sicheren Zugriff auf Daten in unserem Snowflake-Portal zu gewähren – ohne Reibungsverluste oder Verzögerungen im Workflow, Fehlerquellen und unnötige Kosten, die bei typischen Datenanbieter-Beziehungen entstehen. Data Sharing kann über die folgende Integration oder über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts) eingerichtet werden.

Snowflake Data Sharing ist Teil der Braze-Datenverteilung. Einen vollständigen Überblick über die Optionen der Datenverteilung finden Sie unter [Datenverteilung]({{site.baseurl}}/user_guide/data/distribution).

{% alert tip %}
**Sie möchten auf Snowflake-Daten zugreifen, ohne ein Snowflake-Konto zu benötigen?**<br>Informieren Sie sich über [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts). Mit Reader Accounts erstellt Braze ein Konto, teilt Ihre Daten darin und stellt Ihnen Zugangsdaten zur Verfügung, mit denen Sie sich anmelden und auf Ihre Daten zugreifen können. Dabei werden sämtliche Kosten für Data Sharing und Nutzung vollständig von Braze übernommen.
{% endalert %}

## Berechtigungen für die Datenverteilung {#data-distribution-entitlements}

Ihre Berechtigung für die Datenverteilung legt fest, welche Event-Typen in Ihrem Daten-Share verfügbar sind. Braze organisiert Events in die folgenden Kategorien:

| Berechtigung | Event-Kategorie | Beschreibung | Referenz zum Event-Glossar |
|------------|----------------|-------------|--------------------------|
| **Engagement-Events** | Nachrichten-Engagement-Events | Events im Zusammenhang mit Nachrichtenversand, Zustellung, Öffnungen, Klicks, Bounces und anderen Messaging-Kanal-Interaktionen | [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **Kundenverhalten-Events** | Nachrichten-Engagement-Events und Kundenverhalten-Events | Umfasst alle Nachrichten-Engagement-Events sowie Events im Zusammenhang mit Käufen, angepassten Events, Sitzungen, Attribution und In-App-Nutzeraktionen | [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten- und Nutzer-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **Nutzerprofile und Attribute** | Nachrichten-Engagement-Events, Kundenverhalten-Events und Nutzerprofil-Events | Umfasst Nachrichten-Engagement-Events und Kundenverhalten-Events sowie Events im Zusammenhang mit Änderungen an Nutzerprofilen und Attributen | [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten- und Nutzer-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [Nutzerprofil-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Berechtigungen für die Datenverteilung" }

Bei Fragen dazu, welche Events in Ihrer Berechtigung enthalten sind, wenden Sie sich an Ihren Braze-Konto- oder Customer-Success-Manager.

## Über Secure Data Sharing {#about-secure-data-sharing}

Beim Data Sharing werden keine tatsächlichen Daten zwischen Konten kopiert oder übertragen. Die gesamte Freigabe erfolgt über die einzigartige Dienstschicht und den Metadaten-Store von Snowflake. Dies ist ein wichtiges Konzept, da freigegebene Daten keinen Speicherplatz in Ihrem Konto belegen und somit nicht zu Ihren monatlichen Datenspeicherkosten beitragen. Die **einzigen** Kosten entstehen durch die Rechenressourcen (z. B. virtuelle Warehouses), die zum Abfragen der freigegebenen Daten verwendet werden.

Darüber hinaus kann der Zugriff auf von Braze freigegebene Daten mithilfe der integrierten Rollen- und Berechtigungsfunktionen von Snowflake über die bereits für Ihr Snowflake-Konto und die darin enthaltenen Daten vorhandenen Zugriffskontrollen gesteuert und verwaltet werden. Der Zugriff kann auf die gleiche Weise wie bei Ihren eigenen Daten eingeschränkt und überwacht werden.

- **Schneller zu Insights**<br>Verabschieden Sie sich von ETL-Prozessen, deren Aufbau Wochen dauert. Die einzigartigen Architekturen von Braze und Snowflake machen alle Customer-Engagement- und Campaign-Daten sofort zugänglich und abfragbar, sobald sie im Data Lake eintreffen. Es werden keine Daten kopiert oder verschoben, sodass Sie Kundenerlebnisse basierend auf den relevantesten und aktuellsten Informationen bereitstellen können.
- **Datensilos aufbrechen**<br>Erstellen Sie eine ganzheitliche Sicht auf Ihre Kund:innen über alle Kanäle und Plattformen hinweg. Data Sharing erleichtert es mehr denn je, Ihre Braze-Customer-Engagement-Daten mit all Ihren anderen Snowflake-Daten zu verknüpfen – und so umfassendere Insights aus einer einzigen, zuverlässigen Datenquelle zu gewinnen.
- **Sehen Sie, wie Ihr Engagement abschneidet**<br>Optimieren Sie Ihre Customer-Engagement-Strategien mit Braze Benchmarks. Dieses interaktive Tool, bereitgestellt von Braze und Snowflake, ermöglicht es Ihnen, die Engagement-Daten Ihrer Marke mit Benchmarks über verschiedene Kanäle, Branchen und Geräteplattformen hinweg zu vergleichen.

Weitere Informationen zum Data Sharing von Snowflake finden Sie unter [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Kontaktieren Sie Ihre:n Braze-Konto- oder Customer-Success-Manager:in, um Data Sharing einzurichten. |
| Snowflake-Konto | Ein Snowflake-Konto mit `admin`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Einrichten der sicheren Datenfreigabe {#setting-up-secure-data-sharing}

Bei Snowflake erfolgt die Datenfreigabe zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Datenverbraucher](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). In diesem Kontext ist Ihr Braze-Konto der Datenanbieter, da es die Datenfreigabe erstellt und sendet&#8212;während Ihr Snowflake-Konto der Datenverbraucher ist, da es die Datenfreigabe nutzt, um eine Datenbank zu erstellen. Weitere Informationen finden Sie unter [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Schritt 1: Datenfreigabe von Braze senden {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Schritt 2: Datenbank in Snowflake erstellen {#step-2-create-the-database-in-snowflake}

1. Nach einigen Minuten sollten Sie die eingehende Datenfreigabe in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mithilfe der eingehenden Datenfreigabe eine Datenbank, um die Tabellen anzuzeigen und abzufragen. Zum Beispiel:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Vergeben Sie Berechtigungen, um die neue Datenbank abzufragen.

{% alert warning %}
Wenn Sie eine Freigabe im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank verwerfen und mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um die eingehende Freigabe abzufragen.
Wenn Sie mehrere Workspaces haben, die Daten an dasselbe Snowflake-Konto freigeben, finden Sie in den [Snowflake Data Sharing FAQs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) Hinweise zur Verwaltung von Multi-Workspace-Konfigurationen.
{% endalert %}

## Nutzung und Visualisierung {#usage-and-visualization}

Nachdem der Datenfreigabe-Zugang bereitgestellt wurde, erstellen Sie eine Datenbank aus der eingehenden Datenfreigabe, sodass alle freigegebenen Tabellen in Ihrer Snowflake-Instanz erscheinen und genauso abgefragt werden können wie alle anderen Daten, die Sie in Ihrer Instanz speichern. Beachten Sie jedoch, dass die freigegebenen Daten schreibgeschützt sind und nur abgefragt, aber in keiner Weise geändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Ihr Snowflake Secure Data Sharing nutzen, um:

{% multi_lang_include partners/data_sharing_use_cases.md %}

[Laden Sie die Rohtabellen-Schemas herunter.](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

{% alert note %}
Der Download der Rohschemas enthält keine Nutzerprofilattribut-Ansichten. Die vollständigen Schemas und Nutzungshinweise für `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`, `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` und verwandte Nutzerattribut-Ansichten finden Sie unter [Nutzerprofilattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

### Nutzer-ID-Schema {#user-id-schema}

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Nutzer-IDs.

| Braze-Schema | Snowflake-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von der Kundschaft festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer-ID-Schema" }

## Wichtige Informationen und Einschränkungen {#important-information-and-limitations}

### Abwärtskompatible versus nicht abwärtskompatible Änderungen {#breaking-versus-non-breaking-changes}

#### Nicht abwärtskompatible Änderungen {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Da neue Spalten als nicht abwärtskompatible Änderungen gelten, empfiehlt Braze dringend, in jeder Abfrage die gewünschten Spalten explizit aufzulisten, anstatt `SELECT *`-Abfragen zu verwenden. Alternativ können Sie Views erstellen, die Spalten explizit benennen, und dann diese Views anstelle der Tabellen direkt abfragen.
{% endalert %}

#### Abwärtskompatible Änderungen {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflake-Regionen {#snowflake-regions}

Braze hostet derzeit alle Daten auf Nutzer:innen-Ebene in diesen Snowflake-AWS-Regionen:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Northeast-1 (Tokio)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)

Für Nutzer:innen außerhalb dieser Regionen kann Braze gemeinsamen Kund:innen Data Sharing bereitstellen, die ihre Snowflake-Infrastruktur in einer beliebigen AWS-, Azure- oder GCP-Region betreiben.

### Datenaufbewahrung {#data-retention}

#### Aufbewahrungsrichtlinie {#retention-policy}

Alle Daten, die älter als zwei Jahre sind, werden archiviert und in den Langzeitspeicher verschoben. Im Rahmen des Archivierungsprozesses werden alle Events anonymisiert und alle personenbezogenen (PII) sensiblen Felder entfernt (dies umfasst auch optional personenbezogene Felder wie `properties`). Archivierte Daten enthalten weiterhin das Feld `user_id`, das eine Analyse pro Nutzer:in über alle Event-Daten hinweg ermöglicht.

Sie können die aktuellsten zwei Jahre an Daten für jedes Event in der entsprechenden `USERS_*_SHARED`-View abfragen. Zusätzlich verfügt jedes Event über eine `USERS_*_SHARED_ALL`-View, die abgefragt werden kann, um sowohl anonymisierte als auch nicht anonymisierte Daten abzurufen.

#### Historische Daten {#historical-data}

Das Archiv historischer Event-Daten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake gespeichert hat, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten leicht anders aussehen oder Nullwerte aufweisen (da zu diesem Zeitpunkt nicht alle verfügbaren Felder mit Daten befüllt wurden). Es empfiehlt sich davon auszugehen, dass Ergebnisse, die Daten vor August 2019 enthalten, leicht von den Erwartungen abweichen können.

### Einhaltung der Datenschutz-Grundverordnung (DSGVO) {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### Geschwindigkeit, Performance und Kosten von Abfragen {#speed-performance-cost-of-queries}

Die Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, werden durch die Warehouse-Größe bestimmt, die Sie zur Abfrage der Daten verwenden. In einigen Fällen kann es je nach Datenmenge, auf die Sie für Analysen zugreifen, erforderlich sein, eine größere Warehouse-Größe zu verwenden, damit die Abfrage erfolgreich ausgeführt werden kann. Snowflake bietet hervorragende Ressourcen dazu, wie Sie die optimale Größe bestimmen, darunter [Übersicht über Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Überlegungen zu Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Beispielabfragen, die Sie beim Einrichten von Snowflake als Referenz verwenden können, finden Sie in unseren Beispielen für [Beispielabfragen]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) und [ETL-Event-Pipeline-Einrichtung]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).
{% endalert %}