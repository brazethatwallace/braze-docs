---
nav_title: Cloud-Datenaufnahme
article_title: Braze Cloud-Datenaufnahme
alias: /cloud_ingestion/
description: "Dieser Referenzartikel behandelt die Quellen der Braze Cloud-Datenaufnahme und Empfehlungen zum Daten-Setup."
page_order: 1
toc_headers: h2
---

# Braze Cloud-Datenaufnahme {#braze-cloud-data-ingestion}

> Mit Braze Cloud Data Ingestion (CDI) können Sie eine direkte Verbindung von Ihrer Datenspeicherlösung einrichten, um relevante Nutzerdaten und andere Nicht-Nutzerdaten mit Braze zu synchronisieren. Diese Daten können anschließend für die Personalisierung oder Segmentierung verwendet werden, um Ihre Marketing-Anwendungsfälle zu optimieren. Die flexible Integration der Cloud-Datenaufnahme unterstützt komplexe Datenstrukturen, einschließlich verschachtelter JSON-Objekte und Objekt-Arrays.

## Funktionsweise {#how-it-works}

Mit Braze Cloud Data Ingestion (CDI) richten Sie eine Integration zwischen Ihrer Data-Warehouse-Instanz und Ihrem Braze-Workspace ein, um Daten regelmäßig zu synchronisieren. Diese Synchronisierung läuft nach einem von Ihnen festgelegten Zeitplan, und jede Integration kann einen eigenen Zeitplan haben. Synchronisierungen können so häufig wie alle 15 Minuten oder so selten wie einmal pro Monat ausgeführt werden. Wenn Sie häufigere Synchronisierungen als alle 15 Minuten benötigen, wenden Sie sich an Ihren Customer-Success-Manager oder erwägen Sie die Verwendung von REST-API-Aufrufen für die Echtzeitdaten-Aufnahme.

Amazon-S3-Dateispeicher-Integrationen sind ereignisgesteuert. Braze nimmt neue Dateien auf, wenn S3/SQS-Benachrichtigungen eintreffen. Weitere Informationen zur Einrichtung finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).

{% alert note %}
Die Synchronisierungshäufigkeit im Dashboard steuert, wie oft Braze eine Synchronisierung ausführt (z. B. Optionen wie stündlich oder häufigere Ausführungen innerhalb einer Stunde). Sie legt kein benutzerdefiniertes Intervall von mehr als einer Stunde zwischen den Ausführungen fest. Um eine Synchronisierung außerhalb des geplanten Rhythmus auszuführen – z. B. auf Anforderung, nachdem Ihr Warehouse-Ladevorgang abgeschlossen ist – verwenden Sie den Endpunkt [Synchronisierung triggern]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) mit Ihrer Integrations-ID.
{% endalert %}

Bei einer Synchronisierung stellt Braze eine direkte Verbindung zu Ihrer Data-Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und aktualisiert die entsprechenden Daten in Ihrem Braze-Dashboard. Bei jeder Synchronisierung werden alle aktualisierten Daten in Braze widergespiegelt.

### Ihre Integrations-ID finden {#finding-your-integration-id}

Sie finden Ihre Integrations-ID in der URL, wenn Sie eine Integration im Braze-Dashboard anzeigen. Navigieren Sie zu **Data Settings** > **Cloud Data Ingestion** und wählen Sie eine Integration aus. Die Integrations-ID erscheint in der URL im Format `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. Wenn Ihre URL beispielsweise `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz` lautet, ist Ihre Integrations-ID `abc123xyz`. Sie können diese ID verwenden, wenn Sie API-Aufrufe zum Triggern von Synchronisierungen oder zur Überprüfung des Synchronisierungsstatus durchführen.

## Anwendungsfälle {#use-cases}

Mit den Funktionen der Braze Cloud-Datenaufnahme können Sie:

- Eine einfache Integration direkt von Ihrem Data Warehouse oder Ihrer Dateispeicherlösung zu Braze in nur wenigen Minuten erstellen.
- Nutzerdaten, einschließlich Attributen, Events und Käufen, sicher von Ihrem Data Warehouse zu Braze synchronisieren.
- Den Datenkreislauf mit Braze schließen, indem Sie die Cloud-Datenaufnahme mit Currents oder Snowflake Data Sharing kombinieren.

Darüber hinaus sind [Verbundene Quellen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) eine Zero-Copy-Alternative. Sie können Braze direkt Ihr Data Warehouse oder Ihre Dateispeicherlösung abfragen lassen, um CDI-Segmente zu erstellen &#8212; und das alles, ohne die zugrunde liegenden Daten nach Braze zu kopieren.

## Unterstützte Datenquellen {#supported-data-sources}

Die Cloud-Datenaufnahme kann Daten aus folgenden Quellen synchronisieren:

   - Amazon Redshift
   - Databricks
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Unterstützte Datentypen {#supported-data-types}

Die Cloud-Datenaufnahme unterstützt die folgenden Datentypen:

### Nutzerdaten {#user-data}
- Nutzerattribute, einschließlich:
   - Verschachtelte angepasste Attribute
   - Arrays von Objekten
   - Abo-Status
- Angepasste Events
- Kauf-Events
- Anfragen zum Löschen von Nutzer:innen

### Nicht-Nutzer-Objekte {#non-user-objects}
- Katalogartikel

### Zero-Copy-Messaging {#zero-copy-messaging}
- Verbundene Quellen

## Nutzerbezeichner für die Datenaufnahme {#user-identifiers-for-data-ingestion}

Wenn Sie Nutzerdaten über die Cloud-Datenaufnahme synchronisieren, können Sie Nutzer:innen mithilfe eines oder mehrerer der folgenden Bezeichnertypen identifizieren. Jede Zeile in Ihrer Quelltabelle sollte jeweils nur einen Wert für einen Bezeichnertyp enthalten, aber Ihre Tabelle kann Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen umfassen.

| Bezeichner | Beschreibung |
|------------|-------------|
| `EXTERNAL_ID` | Die externe ID, die das Nutzerprofil identifiziert, das erstellt oder aktualisiert werden soll. Dieser Wert sollte mit dem in Braze verwendeten `external_id`-Wert übereinstimmen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasse mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der Braze-Nutzerbezeichner, der vom Braze SDK generiert wird. Neue Nutzer:innen können nicht über eine Braze-ID durch die Cloud-Datenaufnahme erstellt werden. Um neue Nutzer:innen zu erstellen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. Wenn Sie sowohl E-Mail als auch Telefonnummer angeben, wird die E-Mail als primärer Bezeichner verwendet. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil für Aktualisierungen priorisiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzerbezeichner für die Datenaufnahme" }

Ausführliche Informationen zum Einrichten von Tabellenspalten und zu den Anforderungen an die Payload-Formatierung finden Sie unter [Tabellen-Setup für die Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Quellspezifische Einrichtungsanweisungen und SQL-Beispiele finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Datenpunkt-Nutzung {#data-point-usage}

Für Kund:innen mit datenpunktbasierter Abrechnung entspricht die Datenpunkt-Abrechnung für die Cloud-Datenaufnahme der Abrechnung für Aktualisierungen über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

{% alert important %}
Die Cloud-Datenaufnahme von Braze wird auf das verfügbare Rate-Limit angerechnet. Wenn Sie Daten also über eine andere Methode senden, wird das Rate-Limit zwischen der Braze-API und der Cloud-Datenaufnahme kombiniert.
{% endalert %}

## Produktbeschränkungen {#product-limitations}

| Beschränkung            | Beschreibung                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anzahl der Integrationen | Es gibt keine Begrenzung für die Anzahl der Integrationen, die Sie einrichten können. Allerdings können Sie pro Tabelle oder View nur eine Integration einrichten.                                             |
| Anzahl der Zeilen         | Standardmäßig kann jeder Lauf bis zu 500 Millionen Zeilen synchronisieren. Synchronisierungen mit mehr als 500 Millionen neuen Zeilen werden gestoppt. Wenn Sie ein höheres Limit benötigen, wenden Sie sich an Ihren Braze Customer-Success-Manager oder den Braze-Support. |
| Attribute pro Zeile     | Jede Zeile sollte eine einzelne Nutzer-ID und ein JSON-Objekt mit bis zu 250 Attributen enthalten. Jeder Schlüssel im JSON-Objekt zählt als ein Attribut (d. h. ein Array zählt als ein Attribut). |
| Payload-Größe           | Jede Zeile kann einen Payload von bis zu 1 MB enthalten. Payloads über 1 MB werden abgelehnt, und der Fehler „Payload was greater than 1MB“ wird zusammen mit der zugehörigen externen ID und dem gekürzten Payload im Synchronisierungsprotokoll protokolliert. |
| Datentyp              | Sie können Nutzerattribute, Events und Käufe über die Cloud-Datenaufnahme synchronisieren.                                                                                                  |
| Braze-Region           | Dieses Produkt ist in allen Braze-Regionen verfügbar. Jede Braze-Region kann sich mit jeder Quelldatenregion verbinden.                                                                              |
| Quellregion       | Braze verbindet sich mit Ihrem Data Warehouse oder Ihrer Cloud-Umgebung in jeder Region oder bei jedem Cloud-Anbieter.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Produktbeschränkungen" }