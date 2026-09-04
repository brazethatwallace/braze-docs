---
nav_title: LiveRamp
article_title: LiveRamp
description: "Erfahren Sie, wie Sie LiveRamp und Braze über Snowflake-Datenfreigabe oder Braze-Currents verbinden, um hochgradig personalisierte und relevante Kampagnen zu erstellen."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp

> Erfahren Sie, wie Sie LiveRamp und Braze über Snowflake-Datenfreigabe oder Braze-Currents verbinden, um hochgradig personalisierte und relevante Kampagnen zu erstellen – indem Sie die Zeit bis zu Insights verkürzen, Datensilos aufbrechen und das Customer-Engagement optimieren. Diese Integration verbessert datengestütztes Marketing, indem sie verwertbare personenbezogene Erkenntnisse liefert und Verbraucher-Touchpoints konsolidiert, um eine bessere Zielgruppensegmentierung und zeitnahe Kampagnen zu ermöglichen.

## Integrationsoptionen {#integration-options}

Sie können LiveRamp mit Braze über eine von zwei Methoden integrieren:

- **Snowflake-Datenfreigabe:** Teilen Sie Braze-Daten direkt über die sichere Datenfreigabe von Snowflake, ohne Daten zu verschieben. Diese Methode nutzt die von Snowflake bereitgestellten Benchmarks, um Ihre Marketingstrategien im Vergleich zu Branchenstandards zu verfeinern.
- **Braze-Currents:** Streamen Sie Realtime-Engagement-Daten auf Event-Ebene von Braze an ein Cloud-Speicherziel (Amazon S3, Google Cloud Storage oder Microsoft Azure Blob Storage), laden Sie diese Daten dann in Ihr Data Warehouse und nutzen Sie die Identitätsauflösungsfunktionen von LiveRamp in Ihrer Cloud-Umgebung.

{% alert important %}
Die [sichere Datenfreigabe](https://docs.snowflake.com/en/user-guide/data-sharing-intro) von Snowflake überträgt keine Daten zwischen LiveRamp, Snowflake und Braze. Daten werden nur über die Dienste und den Metadaten-Store von Snowflake ausgetauscht, d. h. es werden keine Daten kopiert und es fallen keine zusätzlichen Speichergebühren an. Der Zugriff auf gemeinsam genutzte Daten wird über die Zugriffskontrollen Ihres Snowflake-Kontos gesteuert und geregelt.
{% endalert %}

## Anwendungsfälle {#use-cases}

Diese Integration unterstützt die folgenden Anwendungsfälle in allen Data-Warehouse-Umgebungen:

- **Datenminimierung:** Die Lösungen von LiveRamp nutzen Features zur sicheren Datenfreigabe oder cloudnative Identitätsauflösung, um Tabellen direkt aus Ihrem Data Warehouse zu lesen. Bis zum Zeitpunkt der Zustellung an den nachgelagerten Partner werden keine Daten verschoben.
- **Sichere 1st-Party-Aktivierung:** Durch die Verwendung der Identitätsauflösung von LiveRamp nutzt die Aktivierungsanwendung von LiveRamp nur die RampID-basierten Tabellen in Ihrem Data Warehouse, sodass PII niemals Ihre Umgebung verlassen müssen.
- **Schnellere Time-to-Live:** Da die Daten direkt in Ihrer Umgebung in RampID aufgelöst werden, kann die Zustellung an ein Ziel innerhalb weniger Stunden erfolgen – im Gegensatz zu mehreren Tagen bei der herkömmlichen dateibasierten Methode von LiveRamp. So können Sie die Performance Ihrer Kampagnen zeitnah optimieren.
- **Operative Einsparungen:** Durch die sichere Datenfreigabe oder cloudnative Identitätsauflösung sparen Sie Zeit und Geld im Vergleich zur Koordinierung der Übertragung von Dateien an LiveRamp oder direkt an ein beliebiges Ziel.

## Integration mit Snowflake-Datenfreigabe {#integration-with-snowflake-data-sharing}

Die folgenden Schritte beschreiben, wie Sie LiveRamp über die Snowflake-Datenfreigabe mit Braze integrieren.

### Voraussetzungen {#prerequisites}

| Voraussetzung | Beschreibung |
|---|---|
| Snowflake-Konto | Sie benötigen ein Snowflake-Konto mit Admin-Rechten. |
| LiveRamp-Konto | Wenden Sie sich an Ihr LiveRamp-Kontoteam oder an [snowflake@liveramp.com](mailto:snowflake@liveramp.com), um die erforderlichen LiveRamp-Anwendungen in Snowflake zu besprechen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

### 1. Schritt: Datenfreigabe bei Braze anfragen {#step-1-request-a-data-share-from-braze}

Wenden Sie sich zunächst an Ihren Braze Account Manager:in oder CSM, um einen Snowflake Data Share Connector für Ihr Braze-Konto zu erwerben. Wenn Sie eine Datenfreigabe anfragen, stellt Braze die Freigabe aus dem/den Workspace(s) bereit, für den/die die Freigabe erworben wurde. Nachdem die Freigabe bereitgestellt wurde, sind alle Daten sofort von Ihrer Snowflake-Instanz aus in Form einer eingehenden Datenfreigabe zugänglich. Sobald die Freigabe in Ihrer Instanz sichtbar ist, erstellen Sie eine Datenbank aus der Freigabe, damit Sie die Tabellen sehen und abfragen können.

Eine vollständige Anleitung finden Sie in der [Anleitung zur Integration von Snowflake mit Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### 2. Schritt: LiveRamp-App in Snowflake einrichten {#step-2-set-up-the-liveramp-app-in-snowflake}

Die Funktionen zur Übersetzung und Identitätsauflösung sind in Snowflake über die native App LiveRamp Identity Resolution and Translation verfügbar, die eine Freigabe für Ihr Konto erstellt und eine Ansicht zur Abfrage des Referenzdatensatzes in Ihrer eigenen Snowflake-Umgebung öffnet.

Um die native App einzurichten, folgen Sie diesen Schritten in den LiveRamp-Dokumenten: [Einrichten der LiveRamp Native App in Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Wenn Sie fertig sind, fahren Sie mit dem nächsten Schritt fort.

### 3. Schritt: Datentabelle erstellen {#step-3-create-a-data-table}

{% alert warning %}
Bevor Sie PII-basierte Tabellen vorbereiten, sollten Sie sich mit dem [Datenschutzfilter von LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) vertraut machen, der während der Jobs ausgeführt wird, um sicherzustellen, dass die Attributspalten (Nicht-Bezeichner) in Ihren Eingabetabellen keine zu eindeutigen Werte enthalten. Dies ist entscheidend für die Wahrung der Privatsphäre der Verbraucher:innen und die Vermeidung einer erneuten Identifizierung.
{% endalert %}

Als Nächstes erstellen Sie eine Datentabelle mit dem [erforderlichen Format](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html), die in der nativen App von LiveRamp aufgerufen wird. Anhand der folgenden Kategorien können Sie feststellen, welche Ihrer Bezeichner für die Auflösung in Frage kommen:

| Bezeichner-Typ | Beschreibung |
|---|---|
| Vollständige PII | Zu den personenbezogenen Daten (PII) gehören der Name, die Postanschrift, die E-Mail-Adresse und die Telefonnummer der Nutzer:innen. **Hinweis:** Nicht alle Bezeichner sind für jeden Datensatz erforderlich. |
| Nur E-Mail | Die E-Mail-Adressen der Nutzer:innen, z. B. `alex-lee@email.com`. |
| Gerät | Dazu gehören Cookies von Drittanbietern, Mobile Advertising IDs (MAIDs), Connected TV IDs (CTV IDs) und RampIDs (aufgelöst in eine Household RampID). |
| CIDs | Dabei handelt es sich um Bezeichner eines Plattformpartners oder einer mit LiveRamp synchronisierten Identität, wie z. B. Ihre interne Kund:innen-ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datentabelle erstellen" }

#### Braze-Bezeichner {#braze-identifiers}

Die Event-Protokolle von Braze enthalten Bezeichner, die Sie in der nativen LiveRamp-App verwenden können. Eine vollständige Liste der verfügbaren Bezeichner für jeden Event-Typ finden Sie in den [Braze-Event-Schemata und -Bezeichnern](/docs/assets/download_file/data-sharing-raw-table-schemas.txt).

| Bezeichner-Typ | Beschreibung |
|---|---|
| `AD_ID` | Werbe-IDs wie `ios_idfa`, `google_ad_id`, `roku_ad_id`, die innerhalb bestimmter Event-Typen erfasst werden und in Verbindung mit den Diensten von LiveRamp zur Geräteauflösung verwendet werden können. Standardmäßig werden Werbe-IDs nicht erfasst&#8212;Sie können das Tracking jedoch aktivieren, indem Sie der [Braze-Dokumentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default) folgen. |
| `EMAIL_ADDRESS` | E-Mail-Adresse, die in Verbindung mit den Diensten von LiveRamp zur reinen E-Mail-Auflösung verwendet werden kann. |
| `TO_PHONE_NUMBER` | Telefonnummer, die in Verbindung mit den Diensten zur PII-Auflösung von LiveRamp verwendet werden kann. |
| `EXTERNAL_USER_ID` | Die einer Nutzer:in zugeordnete externe ID, die in Verbindung mit den Diensten von LiveRamp zur Geräteauflösung (CID) verwendet werden kann. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze-Bezeichner" }

{% alert important %}
Die Verwendung von client- oder markenspezifischen angepassten Bezeichnern innerhalb der LiveRamp-Anwendung erfordert eine [Identitätssynchronisierung mit LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### 4. Schritt: Variablen festlegen {#step-4-set-your-variables}

Als Nächstes legen Sie Ihre Variablen für den Auftrag im Arbeitsblatt „Ausführungsschritte“ fest, das in der App enthalten ist. Dazu gehören Details wie die Zieldatenbank, zugehörige Tabellen (Eingabedaten, Metriken, Protokollierung) und die Definition des Namens der Ausgabetabelle. Eine vollständige Übersicht finden Sie unter [LiveRamp: Variablen festlegen](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### 5. Schritt: Metadatentabelle für die PII-Auflösung erstellen {#step-5-create-the-metadata-table-for-pii-resolution}

Da Ihre Variablen nun festgelegt sind, erstellen Sie die Metadatentabelle für die PII-Auflösung. Hier finden Sie Einzelheiten zu der Art des auszuführenden Auftrags, basierend auf der Kategorie der beteiligten Bezeichner. Eine vollständige Übersicht finden Sie unter [LiveRamp: Metadatentabelle erstellen](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### 6. Schritt: Identitätsauflösung durchführen {#step-6-perform-the-identity-resolution-operation}

Führen Sie abschließend den Vorgang der Identitätsauflösung durch. Eine vollständige Übersicht finden Sie unter [LiveRamp: Identitätsauflösung durchführen](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab Beispiel-Eingabe %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab Beispiel-Ausgabe %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Nächste Schritte {#next-steps}

Da Ihre Daten nun mit Ihrer eigenen RampID-Kodierung pseudonymisiert sind, haben Sie die Möglichkeit, die RampID-basierten Tabellen an die Managed Activation Application von LiveRamp weiterzugeben, um die Abwicklung mit Ihren wichtigsten Werbeplattform-Partnern zu optimieren. Die Aktivierungsanwendung enthält eine benutzerfreundliche Schnittstelle für die zusätzliche Segmentierung und Auswahl/Konfiguration von nachgelagerten Zielpartnern. Weitere Einzelheiten zur Anwendung erhalten Sie von Ihrem LiveRamp Account Team oder unter [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Integration mit Braze-Currents {#integration-with-braze-currents}

Braze-Currents stellt einen Realtime-Stream von Engagement-Events bereit, die an Cloud-Speicherziele exportiert werden können. Sie können Currents mit LiveRamp verwenden, um Braze-Event-Daten an einen Cloud-Speicher zu streamen, diese in Ihr Data Warehouse zu laden und dann die Identitätsauflösungsfunktionen von LiveRamp in Ihrer Cloud-Umgebung anzuwenden.

### So funktioniert es {#how-it-works}

1. **Braze liefert Realtime-Daten auf Event-Ebene:** Braze streamt rohe Engagement-Daten über Currents an Ihr Data Warehouse oder Speicherziel.
2. **LiveRamp verbindet Daten mit RampID:** LiveRamp entfernt PII und verbindet Ihre Daten mit dem universellen Bezeichner Ihrer Marke, der RampID.
3. **Aktivieren und messen:** First-Party-Daten aus Braze können mit anderen Drittanbieter-Daten kombiniert werden, um präzisere Kundensegmente für Werbung zu erstellen. Pseudonymisierte Zielgruppen werden an LiveRamp zur nachgelagerten Aktivierung bei Plattformpartnern gesendet, und LiveRamp erhält Werbeexpositionsdaten von Partnern für die Messung auf personenbezogener Ebene.

### Unterstützte Cloud-Plattformen {#supported-cloud-platforms}

Die Identitätsauflösungsfunktionen von LiveRamp sind in den folgenden Cloud-Umgebungen verfügbar:

| Plattform | LiveRamp-Lösung | Beschreibung |
|---|---|---|
| Google BigQuery | [LiveRamp Embedded Identity in BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery) | Führen Sie Identitätsauflösung und RampID-Übersetzung nativ in BigQuery mithilfe des BigQuery Entity Resolution Framework durch. Laden Sie Currents-Daten aus Google Cloud Storage in BigQuery, bevor Sie die Identitätsauflösung ausführen. |
| AWS | [LiveRamp Identity in AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws) | Lösen Sie Bezeichner in RampIDs auf und führen Sie die Identitätsübersetzung mithilfe von AWS Entity Resolution oder über Amazon Data Exchange (ADX) Standalone durch. Laden Sie Currents-Daten aus Amazon S3, bevor Sie die Identitätsauflösung ausführen. |
| Microsoft Azure | LiveRamp kontaktieren | Azure Blob Storage wird als Currents-Ziel unterstützt. Wenden Sie sich an Ihre LiveRamp-Vertretung für Azure-spezifische Lösungen zur Identitätsauflösung. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Cloud-Plattformen" }

{% alert note %}
LiveRamp Embedded Identity in BigQuery befindet sich derzeit in der Beta-Phase. Wenden Sie sich an [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com), um die Teilnahme am Programm zu besprechen.
{% endalert %}

### Voraussetzungen

| Voraussetzung | Beschreibung |
|---|---|
| Braze-Currents | Um Event-Daten an einen Cloud-Speicher zu streamen, müssen [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) für Ihr Konto eingerichtet sein. |
| Cloud-Speicherkonto | Sie benötigen ein Cloud-Speicherkonto (Amazon S3, Google Cloud Storage oder Microsoft Azure Blob Storage), an das Currents Ihre Daten streamt. |
| LiveRamp-Konto | Wenden Sie sich an Ihr LiveRamp-Kontoteam oder an [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com), um die Identitätsauflösung von LiveRamp in Ihrer Cloud-Umgebung einzurichten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

### 1. Schritt: Braze-Currents einrichten {#step-1-set-up-braze-currents}

Richten Sie zunächst Braze-Currents ein, um Ihre Engagement-Daten an Ihr Cloud-Speicherziel zu streamen. Verwenden Sie je nach gewählter Plattform die folgenden Anleitungen:

- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

Konfigurieren Sie Currents so, dass die Events exportiert werden, die die für die LiveRamp-Identitätsauflösung benötigten Bezeichner enthalten. Eine vollständige Liste der verfügbaren Bezeichner für jeden Event-Typ finden Sie in den Glossaren [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) und [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

### 2. Schritt: LiveRamp-Identitätsauflösung einrichten {#step-2-set-up-liveramp-identity-resolution}

Nachdem Currents Daten an Ihren Cloud-Speicher streamt, arbeiten Sie mit Ihrer LiveRamp-Vertretung zusammen, um die Identitätsauflösung in Ihrer Cloud-Umgebung einzurichten:

- **Für BigQuery:** Folgen Sie der Einrichtungsanleitung [LiveRamp Embedded Identity in BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery), um die Identitätsauflösung und RampID-Übersetzung zu aktivieren. Stimmen Sie sich mit Ihrer LiveRamp-Vertretung ab, um die für das Beta-Programm erforderlichen Vereinbarungs- und Bereitstellungsschritte abzuschließen.
- **Für AWS:** Folgen Sie der Einrichtungsanleitung [LiveRamp Identity in AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws), um die RampID-Identitätsauflösung mithilfe von AWS Entity Resolution oder ADX Standalone zu konfigurieren.

### 3. Schritt: Daten laden und transformieren {#step-3-load-and-transform-your-data}

Erstellen Sie einen ETL-Prozess (ETL), um:

1. Die Currents-Daten aus Ihrem Cloud-Speicher in Ihre Data-Warehouse-Tabellen zu laden.
2. Die Daten in das von LiveRamps Identitätsauflösungsdienst benötigte Format zu transformieren.
3. Eingabetabellen mit den für die LiveRamp-Auflösung benötigten Bezeichnern vorzubereiten (z. B. E-Mail-Adressen, Geräte-IDs oder externe Nutzer-IDs).

### 4. Schritt: Identitätsauflösung durchführen {#step-4-perform-identity-resolution}

Verwenden Sie die cloudnative Identitätsauflösung von LiveRamp, um Ihre Braze-Bezeichner in RampIDs aufzulösen. Der Prozess:

1. Löst bereitgestellte Bezeichner (PII oder Gerät) in den pseudonymen personenbezogenen Bezeichner von LiveRamp, die RampID, auf.
2. Schreibt die Ausgabetabellen mit RampIDs zurück in Ihr Data Warehouse, wobei PII-Daten entfernt werden.

### 5. Schritt: Zielgruppen aktivieren {#step-5-activate-your-audiences}

Da Ihre Daten nun mit RampID pseudonymisiert sind, können Sie:

- First-Party-Daten aus Braze mit anderen Datenquellen kombinieren, um präzisere Kundensegmente zu erstellen.
- Pseudonymisierte Zielgruppen über die Aktivierungsplattform von LiveRamp für Werbekampagnen aktivieren.
- Werbeexpositionsdaten von Partnern für die Messung auf personenbezogener Ebene erhalten.

Weitere Einzelheiten zur Aktivierung erhalten Sie von Ihrem LiveRamp Account Team oder unter [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com).

## Fehlerbehebung {#troubleshooting}

{% alert note %}
Wenn Sie spezifischere Probleme oder Fragen haben, wenden Sie sich an [martech@liveramp.com](mailto:martech@liveramp.com) oder [LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com).
{% endalert %}

### Snowflake-Regionen {#snowflake-regions}

Die native Snowflake-App ist derzeit nur für die folgenden US-basierten Regionen verfügbar:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Datenschutz und Spaltenwerte {#privacy-column-values}

Der Identitätsauflösungsprozess von LiveRamp wertet die Kombination aller Spaltenwerte pro Zeile auf eindeutige Werte aus. Wenn eine bestimmte Kombination von Spaltenwerten 3 Mal oder weniger vorkommt, sind die Zeilen mit diesen Spaltenwerten nicht zuordenbar und werden in der Ausgabetabelle nicht zurückgegeben. Um den Datenschutz zu gewährleisten, prüft der LiveRamp-Dienst außerdem die Eindeutigkeit der Kombinationen von Spaltenwerten und stellt sicher, dass der Auftrag fehlschlägt, wenn mehr als 5 % der Zeilen in der Datei aufgrund seltener Kombinationen nicht zuordenbar sind.

### Historische Daten {#historical-data}

Die historischen Daten in Snowflake reichen bis April 2019 zurück. Aufgrund von Produktänderungen kann es jedoch zu leichten Abweichungen bei den Daten vor August 2019 kommen.

### Geschwindigkeit, Performance und Kosten {#speed-performance-cost}

Die Geschwindigkeit und die Kosten der Abfragen hängen von der Größe des verwendeten Warehouses ab. Berücksichtigen Sie beim Auswählen der Warehouse-Größe Ihre Anforderungen an den Datenzugriff.

### Braze-Benchmarks

Benchmarks ermöglichen es Ihnen, Ihre Metriken mit Branchenstandards zu vergleichen, die direkt im Snowflake Data Exchange verfügbar sind.

### Breaking- vs. Non-Breaking-Änderungen {#breaking-vs-non-breaking-changes}

Achten Sie auf Änderungen, die sich auf Ihre Integration auswirken können. Einschneidenden Änderungen gehen eine Ankündigung und eine Migrationsphase voraus.