---
nav_title: LiveRamp
article_title: LiveRamp
description: "Erfahren Sie, wie Sie LiveRamp, Snowflake und Braze miteinander verbinden, um hochgradig personalisierte und relevante Kampagnen zu erstellen."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp, Snowflake und Braze verbinden {#connect-liveramp-snowflake-and-braze}

> Erfahren Sie, wie Sie LiveRamp, Snowflake und Braze miteinander verbinden, um hochgradig personalisierte und relevante Kampagnen zu erstellen – indem Sie die Zeit bis zu Insights verkürzen, Datensilos aufbrechen und das Customer-Engagement optimieren. Diese Integration verbessert datengestütztes Marketing, indem sie verwertbare personenbezogene Erkenntnisse liefert und Verbraucher-Touchpoints konsolidiert, um eine bessere Zielgruppensegmentierung und zeitnahe Kampagnen zu ermöglichen. Außerdem nutzt sie die von Snowflake bereitgestellten Benchmarks, um Ihre Marketingstrategien im Vergleich zu Branchenstandards zu verfeinern.

{% alert important %}
Die [sichere Datenfreigabe](https://docs.snowflake.com/en/user-guide/data-sharing-intro) von Snowflake überträgt keine Daten zwischen LiveRamp, Snowflake und Braze. Daten werden nur über die Dienste und den Metadaten-Store von Snowflake ausgetauscht, d. h. es werden keine Daten kopiert und es fallen keine zusätzlichen Speichergebühren an. Der Zugriff auf gemeinsam genutzte Daten wird über die Zugriffskontrollen Ihres Snowflake-Kontos gesteuert und geregelt.
{% endalert %}

## Anwendungsfälle {#use-cases}

- **Datenminimierung:** Die Aktivierungs-App von LiveRamp nutzt das Feature Secure Data Share von Snowflake, um die Tabellen direkt von Ihrer Instanz zu lesen. Bis zum Zeitpunkt der Zustellung an den nachgelagerten Partner werden keine Daten von Snowflake verschoben.
- **Sichere 1st-Party-Aktivierung:** Durch die Verwendung der oben genannten Anwendung zur Identitätsauflösung nutzt die Aktivierungsanwendung von LiveRamp nur die RampID-basierten Tabellen in Ihrer Snowflake-Instanz, sodass PII niemals Ihre Umgebung verlassen müssen.
- **Schnellere Time-to-Live:** Da die Daten direkt in Ihrer Umgebung in RampID aufgelöst werden, kann die Zustellung an ein Ziel innerhalb weniger Stunden erfolgen – im Gegensatz zu mehreren Tagen bei der herkömmlichen dateibasierten Methode von LiveRamp. So können Sie die Performance Ihrer Kampagnen zeitnah optimieren.
- **Operative Einsparungen:** Ähnlich wie oben beschrieben sparen Kund:innen durch den Einsatz des Snowflake-Features für die sichere Datenfreigabe Zeit und Geld im Vergleich zur Koordinierung der Übertragung von Dateien an LiveRamp oder direkt an ein beliebiges Ziel.

## Voraussetzungen {#prerequisites}

| Voraussetzung | Beschreibung |
|---|---|
| Snowflake-Konto | Sie benötigen ein Snowflake-Konto mit Admin-Rechten. |
| LiveRamp-Konto | Wenden Sie sich an Ihr LiveRamp-Kontoteam oder an [snowflake@liveramp.com](mailto:snowflake@liveramp.com), um die erforderlichen LiveRamp-Anwendungen in Snowflake zu besprechen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Einrichten der Integration {#setting-up-the-integration}

### 1. Schritt: Datenfreigabe bei Braze anfragen {#step-1-request-a-data-share-from-braze}

Wenden Sie sich zunächst an Ihren Braze Account Manager oder Customer-Success-Manager, um einen Snowflake Data Share Connector für Ihr Braze-Konto zu erwerben. Wenn Sie eine Datenfreigabe anfragen, stellt Braze die Freigabe aus dem/den Workspace(s) bereit, für den/die die Freigabe erworben wurde. Nachdem die Freigabe bereitgestellt wurde, sind alle Daten sofort von Ihrer Snowflake-Instanz aus in Form einer eingehenden Datenfreigabe zugänglich. Sobald die Freigabe in Ihrer Instanz sichtbar ist, erstellen Sie eine Datenbank aus der Freigabe, damit Sie die Tabellen sehen und abfragen können.

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
{: .reset-td-br-1 .reset-td-br-2 aria-label="3. Schritt: Datentabelle erstellen" }

#### Braze-Bezeichner {#braze-identifiers}

Die Ereignisprotokolle von Braze enthalten Bezeichner, die Sie in der nativen LiveRamp-App verwenden können. Eine vollständige Liste der verfügbaren Bezeichner für jeden Event-Typ finden Sie in den [Braze-Ereignisschemata und -Bezeichnern]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).

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
{% tab example input %}
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

{% tab example output %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Nächste Schritte {#next-steps}

Da Ihre Daten nun mit Ihrer eigenen RampID-Kodierung pseudonymisiert sind, haben Sie die Möglichkeit, die RampID-basierten Tabellen an die Managed Activation Application von LiveRamp weiterzugeben, um die Abwicklung mit Ihren wichtigsten Werbeplattform-Partnern zu optimieren. Die Aktivierungsanwendung enthält eine benutzerfreundliche Schnittstelle für die zusätzliche Segmentierung und Auswahl/Konfiguration von nachgelagerten Zielpartnern. Weitere Einzelheiten zur Anwendung erhalten Sie von Ihrem LiveRamp Account Team oder unter [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Fehlerbehebung {#troubleshooting}

{% alert note %}
Wenn Sie spezifischere Probleme oder Fragen haben, wenden Sie sich an [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Snowflake-Regionen {#snowflake-regions}

Derzeit ist diese Anwendung nur für die folgenden US-basierten Regionen verfügbar:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Datenschutz und Spaltenwerte {#privacy-column-values}

Der Prozess wertet die Kombination aller Spaltenwerte pro Zeile auf eindeutige Werte aus. Wenn eine bestimmte Kombination von Spaltenwerten 3 Mal oder weniger vorkommt, sind die Zeilen mit diesen Spaltenwerten nicht zuordenbar und werden in der Ausgabetabelle nicht zurückgegeben. Um den Datenschutz zu gewährleisten, prüft der LiveRamp-Dienst außerdem die Eindeutigkeit der Kombinationen von Spaltenwerten und stellt sicher, dass der Auftrag fehlschlägt, wenn mehr als 5 % der Zeilen in der Datei aufgrund seltener Kombinationen nicht zuordenbar sind.

### Historische Daten {#historical-data}

Die historischen Daten in Snowflake reichen bis April 2019 zurück. Aufgrund von Produktänderungen kann es jedoch zu leichten Abweichungen bei den Daten vor August 2019 kommen.

### Geschwindigkeit, Performance und Kosten {#speed-performance-cost}

Die Geschwindigkeit und die Kosten der Abfragen hängen von der Größe des verwendeten Warehouses ab. Berücksichtigen Sie beim Auswählen der Warehouse-Größe Ihre Anforderungen an den Datenzugriff.

### Braze-Benchmarks

Benchmarks ermöglichen es Ihnen, Ihre Metriken mit Branchenstandards zu vergleichen, die direkt im Snowflake Data Exchange verfügbar sind.

### Breaking- vs. Non-Breaking-Änderungen {#breaking-vs-non-breaking-changes}

Achten Sie auf Änderungen, die sich auf Ihre Integration auswirken können. Einschneidenden Änderungen gehen eine Ankündigung und eine Migrationsphase voraus.