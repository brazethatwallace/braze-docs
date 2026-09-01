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

Ihre Berechtigung für die Datenverteilung bestimmt, welche Event-Typen in Ihrem Daten-Share verfügbar sind. Braze organisiert Events in die folgenden Kategorien:

| Berechtigung | Event-Kategorie | Beschreibung | Referenz zum Event-Glossar |
|------------|----------------|-------------|--------------------------|
| **Engagement-Events** | Nachrichten-Engagement-Events | Events im Zusammenhang mit Nachrichtenversand, Zustellungen, Öffnungen, Klicks, Bounces und anderen Messaging-Kanal-Interaktionen | [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **Kundenverhalten-Events** | Nachrichten-Engagement-Events und Kundenverhalten-Events | Umfasst alle Nachrichten-Engagement-Events sowie Events im Zusammenhang mit Käufen, angepassten Events, Sitzungen, Attribution und In-App-Nutzeraktionen | [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten- und Nutzer-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **Nutzerprofile und Attribute** | Nachrichten-Engagement-Events, Kundenverhalten-Events und Nutzerprofil-Events | Umfasst Nachrichten-Engagement-Events und Kundenverhalten-Events sowie Events im Zusammenhang mit Änderungen an Nutzerprofilen und Attributen | [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Kundenverhalten- und Nutzer-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [Nutzerprofil-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Berechtigungen für die Datenverteilung" }

Bei Fragen dazu, welche Events in Ihrer Berechtigung enthalten sind, wenden Sie sich an Ihr Braze-Konto oder Ihren Customer-Success-Manager.

## Über Secure Data Sharing {#about-secure-data-sharing}

Beim Data Sharing werden keine tatsächlichen Daten zwischen Konten kopiert oder übertragen. Das gesamte Sharing erfolgt über die einzigartige Dienstschicht und den Metadaten-Store von Snowflake. Dies ist ein wichtiges Konzept, da geteilte Daten keinen Speicherplatz in Ihrem Konto belegen und daher nicht zu Ihren monatlichen Datenspeicherkosten beitragen. Die **einzigen** Kosten entstehen durch die Computing-Ressourcen (z. B. virtuelle Warehouses), die zum Abfragen der geteilten Daten verwendet werden.

Darüber hinaus kann der Zugriff auf von Braze geteilte Daten mithilfe der integrierten Rollen und Berechtigungsfunktionen von Snowflake über die bereits für Ihr Snowflake-Konto vorhandenen Zugriffskontrollen gesteuert und verwaltet werden. Der Zugriff kann auf die gleiche Weise wie bei Ihren eigenen Daten eingeschränkt und überwacht werden.

- **Schneller zu Insights**<br>Verabschieden Sie sich von ETL-Prozessen, deren Aufbau Wochen dauert. Die einzigartigen Architekturen von Braze und Snowflake machen alle Customer-Engagement- und Kampagnendaten sofort zugänglich und abfragbar, sobald sie im Data Lake eintreffen. Es werden keine Daten kopiert oder verschoben, sodass Sie Kundenerlebnisse auf Basis der relevantesten und aktuellsten Informationen bereitstellen können.
- **Datensilos aufbrechen**<br>Erstellen Sie eine ganzheitliche Sicht auf Ihre Kund:innen über alle Kanäle und Plattformen hinweg. Data Sharing erleichtert es, Ihre Braze-Customer-Engagement-Daten mit all Ihren anderen Snowflake-Daten zu verknüpfen – für umfassendere Insights auf Basis einer einzigen, zuverlässigen „Source of Truth“.
- **Sehen Sie, wie Ihr Engagement abschneidet**<br>Optimieren Sie Ihre Customer-Engagement-Strategien mit Braze Benchmarks. Dieses interaktive Tool, powered by Braze und Snowflake, ermöglicht es Ihnen, die Engagement-Daten Ihrer Marke mit Benchmarks über Kanäle, Branchen und Geräteplattformen hinweg zu vergleichen.

Weitere Informationen zum Data Sharing von Snowflake finden Sie unter [Einführung in Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-Zugang | Wenden Sie sich an Ihren Braze-Konto- oder Customer-Success-Manager, um die Datenfreigabe einzurichten. |
| Snowflake-Konto | Ein Snowflake-Konto mit `admin`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Einrichtung von Secure Data Sharing {#setting-up-secure-data-sharing}

Bei Snowflake erfolgt Data Sharing zwischen einem [Datenanbieter](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) und einem [Datenkonsumenten](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). In diesem Zusammenhang ist Ihr Braze-Konto der Datenanbieter, da es den Datashare erstellt und sendet&#8212;während Ihr Snowflake-Konto der Datenkonsument ist, da es den Datashare nutzt, um eine Datenbank zu erstellen. Weitere Einzelheiten finden Sie unter [Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Schritt 1: Datashare von Braze senden {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Schritt 2: Datenbank in Snowflake erstellen {#step-2-create-the-database-in-snowflake}

1. Nach einigen Minuten sollten Sie den eingehenden Datashare in Ihrem Snowflake-Konto erhalten.
2. Erstellen Sie mithilfe des eingehenden Datashare eine Datenbank, um die Tabellen anzuzeigen und abzufragen. Zum Beispiel:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Erteilen Sie Berechtigungen, um die neue Datenbank abzufragen.

{% alert warning %}
Wenn Sie einen Share im Braze-Dashboard löschen und neu erstellen, müssen Sie die zuvor erstellte Datenbank verwerfen und mit `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` neu erstellen, um den eingehenden Share abzufragen.
Wenn Sie mehrere Workspaces haben, die Daten an dasselbe Snowflake-Konto teilen, lesen Sie die [Snowflake Data Sharing FAQs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) für Hinweise zur Verwaltung von Multi-Workspace-Konfigurationen.
{% endalert %}

## Nutzung und Visualisierung {#usage-and-visualization}

Nachdem die Datenfreigabe bereitgestellt wurde, erstellen Sie eine Datenbank aus der eingehenden Datenfreigabe, sodass alle freigegebenen Tabellen in Ihrer Snowflake-Instanz erscheinen und wie alle anderen Daten, die Sie in Ihrer Instanz speichern, abgefragt werden können. Beachten Sie jedoch, dass die freigegebenen Daten schreibgeschützt sind und nur abgefragt, aber in keiner Weise geändert oder gelöscht werden können.

Ähnlich wie bei Currents können Sie Snowflake Secure Data Sharing verwenden, um:

{% multi_lang_include partners/data_sharing_use_cases.md %}

[Laden Sie die Rohtabellenschemata herunter.](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

### Nutzer:innen-ID-Schema {#user-id-schema}

Beachten Sie die folgenden Unterschiede zwischen den Namenskonventionen von Braze und Snowflake für Nutzer:innen-IDs.

| Braze-Schema | Snowflake-Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner eines Nutzerprofils, der von der Kundschaft festgelegt wird. |
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

Braze hostet derzeit alle Daten auf Nutzer:innen-Ebene in diesen Snowflake-AWS-Regionen:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Northeast-1 (Tokyo)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)

Für Nutzer:innen außerhalb dieser Regionen kann Braze gemeinsamen Kund:innen, die ihre Snowflake-Infrastruktur in einer beliebigen AWS-, Azure- oder GCP-Region betreiben, Data Sharing bereitstellen.

### Datenaufbewahrung {#data-retention}

#### Aufbewahrungsrichtlinie {#retention-policy}

Alle Daten, die älter als zwei Jahre sind, werden archiviert und in den Langzeitspeicher verschoben. Im Rahmen des Archivierungsprozesses werden alle Events anonymisiert und alle Felder mit personenbezogenen Daten (PII) entfernt (dies umfasst auch optional PII-Felder wie `properties`). Archivierte Daten enthalten weiterhin das Feld `user_id`, das nutzer:innenbezogene Analysen über alle Event-Daten hinweg ermöglicht.

Sie können die aktuellsten zwei Jahre an Daten für jedes Event in der entsprechenden `USERS_*_SHARED`-View abfragen. Zusätzlich verfügt jedes Event über eine `USERS_*_SHARED_ALL`-View, die abgefragt werden kann, um sowohl anonymisierte als auch nicht anonymisierte Daten zurückzugeben.

#### Historische Daten {#historical-data}

Das Archiv historischer Event-Daten in Snowflake reicht bis April 2019 zurück. In den ersten Monaten, in denen Braze Daten in Snowflake gespeichert hat, wurden Produktänderungen vorgenommen, die dazu geführt haben können, dass einige dieser Daten geringfügig anders aussehen oder Nullwerte enthalten (da zu diesem Zeitpunkt nicht alle verfügbaren Felder befüllt wurden). Es ist davon auszugehen, dass Ergebnisse, die Daten vor August 2019 beinhalten, geringfügig von den Erwartungen abweichen können.

### Konformität mit der Datenschutz-Grundverordnung (DSGVO) {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### Geschwindigkeit, Performance und Kosten von Abfragen {#speed-performance-cost-of-queries}

Geschwindigkeit, Performance und Kosten jeder Abfrage, die auf den Daten ausgeführt wird, werden durch die Warehouse-Größe bestimmt, die Sie zur Abfrage der Daten verwenden. In einigen Fällen kann es je nach der Menge der Daten, auf die Sie für Analytics zugreifen, erforderlich sein, eine größere Warehouse-Größe zu verwenden, damit die Abfrage erfolgreich ausgeführt werden kann. Snowflake bietet hervorragende Ressourcen darüber, wie Sie die richtige Größe bestimmen, darunter [Übersicht über Warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) und [Warehouse-Überlegungen](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Für eine Sammlung von Beispielabfragen, die Sie beim Einrichten von Snowflake als Referenz nutzen können, sehen Sie sich unsere [Beispielabfragen]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) und Beispiele zur [ETL-Event-Pipeline-Einrichtung]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup) an.
{% endalert %}