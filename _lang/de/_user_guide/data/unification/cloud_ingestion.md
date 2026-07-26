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

Mit Braze Cloud Data Ingestion (CDI) richten Sie eine Integration zwischen Ihrer Data-Warehouse-Instanz und dem Braze-Workspace ein, um Daten auf wiederkehrender Basis zu synchronisieren. Diese Synchronisierung läuft nach einem von Ihnen festgelegten Zeitplan, und jede Integration kann einen anderen Zeitplan haben. Die Synchronisierung kann so häufig wie alle 15 Minuten oder so selten wie einmal im Monat erfolgen. Wenn Sie Synchronisierungen häufiger als alle 15 Minuten benötigen, wenden Sie sich an Ihren geschäftskunden-Success-Manager oder ziehen Sie die Verwendung von REST-API-Aufrufen für die Echtzeitdatenaufnahme in Betracht.

{% alert note %}
Die Synchronisierungshäufigkeit im Dashboard steuert, wie oft Braze eine Synchronisierung ausführt (z. B. stündlich oder häufiger innerhalb einer Stunde). Sie legt kein benutzerdefiniertes Intervall fest, das länger als eine Stunde zwischen den Ausführungen ist. Um eine Synchronisierung außerhalb des geplanten Rhythmus auszuführen – etwa on demand nach Abschluss Ihres Warehouse-Ladevorgangs – verwenden Sie den Endpunkt [Synchronisierung triggern]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) mit Ihrer Integrations-ID.
{% endalert %}

Bei einer Synchronisierung stellt Braze eine direkte Verbindung zu Ihrer Data-Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und aktualisiert die entsprechenden Daten in Ihrem Braze-Dashboard. Bei jeder Synchronisierung werden alle aktualisierten Daten in Braze übernommen.

### Ihre Integrations-ID finden {#finding-your-integration-id}

Sie finden Ihre Integrations-ID in der URL, wenn Sie eine Integration im Braze-Dashboard anzeigen. Navigieren Sie zu **Data Settings** > **Cloud Data Ingestion** und wählen Sie eine Integration aus. Die Integrations-ID wird in der URL im Format `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]` angezeigt. Wenn Ihre URL beispielsweise `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz` lautet, ist Ihre Integrations-ID `abc123xyz`. Sie können diese ID verwenden, wenn Sie API-Aufrufe durchführen, um Synchronisierungen zu triggern oder den Synchronisierungsstatus zu überprüfen.

## Anwendungsfälle {#use-cases}

Mit den Funktionen der Braze Cloud-Datenaufnahme können Sie:

- In wenigen Minuten eine einfache Integration direkt von Ihrer Data-Warehouse- oder Dateispeicher-Lösung zu Braze erstellen.
- Nutzerdaten, einschließlich Attributen, Events und Käufen, sicher von Ihrem Data Warehouse mit Braze synchronisieren.
- Die Datenschleife mit Braze schließen, indem Sie die Cloud-Datenaufnahme mit Currents oder Snowflake Data Sharing kombinieren.

Darüber hinaus stellen [Verbundene Quellen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) eine Zero-Copy-Alternative dar. Sie können Braze direkt Ihre Data-Warehouse- oder Dateispeicher-Lösung abfragen lassen, um CDI-Segmente zu erstellen – ohne die zugrunde liegenden Daten nach Braze zu kopieren.

## Unterstützte Datenquellen {#supported-data-sources}

Cloud-Datenaufnahme kann Daten synchronisieren aus:

   - Amazon Redshift
   - Databricks
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## Unterstützte Datentypen {#supported-data-types}

Cloud-Datenaufnahme unterstützt die folgenden Datentypen:

### Nutzerdaten {#user-data}
- Nutzerattribute, einschließlich:
   - Verschachtelte angepasste Attribute
   - Arrays von Objekten
   - Abo-Status
- Angepasste Events
- Kauf-Events
- Anfragen zur Löschung von Nutzer:innen

### Nicht-Nutzer-Objekte {#non-user-objects}
- Katalogartikel

### Zero-Copy-Messaging {#zero-copy-messaging}
- Verbundene Quellen

## Nutzer-Bezeichner für die Datenaufnahme {#user-identifiers-for-data-ingestion}

Bei der Synchronisierung von Nutzerdaten über die Cloud-Datenaufnahme können Sie Nutzer:innen anhand eines oder mehrerer der folgenden Bezeichnertypen identifizieren. Jede Zeile in Ihrer Quelltabelle sollte jeweils nur einen Wert für einen Bezeichnertyp enthalten, jedoch kann Ihre Tabelle Spalten für einen, zwei, drei, vier oder alle fünf Bezeichnertypen enthalten.

| Bezeichner | Beschreibung |
|------------|-------------|
| `EXTERNAL_ID` | Die externe ID, die das zu erstellende oder zu aktualisierende Nutzerprofil identifiziert. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der vom Braze SDK generierte Braze-Bezeichner für Nutzer:innen. Neue Nutzer:innen können nicht mithilfe einer Braze-ID über die Cloud-Datenaufnahme erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail-Adresse der Nutzer:in. Sollten mehrere Profile mit derselben E-Mail-Adresse vorhanden sein, wird das zuletzt aktualisierte Profil für Updates priorisiert. Wenn Sie sowohl E-Mail-Adresse als auch Telefonnummer angeben, wird die E-Mail-Adresse als primärer Bezeichner verwendet. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Sollten mehrere Profile mit derselben Telefonnummer vorhanden sein, wird das zuletzt aktualisierte Profil für Updates priorisiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzer-Bezeichner für die Datenaufnahme" }

Ausführliche Informationen zum Einrichten von Tabellenspalten und den Anforderungen an die Payload-Formatierung finden Sie unter [Tabellen-Setup für die Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).

Quellspezifische Einrichtungsanleitungen und SQL-Beispiele finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

## Datenpunkt-Nutzung {#data-point-usage}

Für Kund:innen mit datenpunktbasierter Abrechnung entspricht die Datenpunkt-Abrechnung für die Cloud-Datenaufnahme der Abrechnung von Updates über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Weitere Informationen finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

{% alert important %}
Braze Cloud-Datenaufnahme wird auf das verfügbare Rate-Limit angerechnet. Wenn Sie also Daten mit einer anderen Methode senden, wird das Rate-Limit zwischen der Braze API und der Cloud-Datenaufnahme kombiniert.
{% endalert %}

## Produktbeschränkungen {#product-limitations}

| Beschränkung | Beschreibung |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anzahl der Integrationen | Es gibt keine Begrenzung für die Anzahl der Integrationen, die Sie einrichten können. Es ist jedoch nur eine Integration pro Tabelle oder Ansicht möglich. |
| Anzahl der Zeilen | Standardmäßig können pro Lauf bis zu 500 Millionen Zeilen synchronisiert werden. Synchronisierungen mit mehr als 500 Millionen neuen Zeilen werden gestoppt. Wenn Sie ein höheres Limit benötigen, wenden Sie sich an Ihren geschäftskunden-Success-Manager von Braze oder an den Braze Support. |
| Attribute pro Zeile | Jede Zeile sollte eine einzelne Nutzer-ID und ein JSON-Objekt mit bis zu 250 Attributen enthalten. Jeder Schlüssel im JSON-Objekt zählt als ein Attribut (d. h. ein Array zählt als ein Attribut). |
| Payload-Größe | Jede Zeile kann eine Payload von bis zu 1 MB enthalten. Payloads, die größer als 1 MB sind, werden abgelehnt, und der Fehler „Payload was greater than 1MB“ wird zusammen mit der zugehörigen externen ID und der gekürzten Payload im Synchronisierungsprotokoll vermerkt. |
| Datentyp | Sie können Nutzerattribute, Events und Käufe über die Cloud-Datenaufnahme synchronisieren. |
| Braze-Region | Dieses Produkt ist in allen Braze-Regionen verfügbar. Jede Braze-Region kann sich mit jeder Quelldatenregion verbinden. |
| Quellregion | Braze stellt eine Verbindung zu Ihrem Data Warehouse oder Ihrer Cloud-Umgebung in jeder Region und bei jedem Cloud-Anbieter her. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Produktbeschränkungen" }