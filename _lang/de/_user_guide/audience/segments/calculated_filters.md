---
nav_title: Berechnete Filter
article_title: Berechnete Filter
page_order: 5.5
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie berechnete Filter funktionieren, wie sie sich von SQL-Segmenterweiterungen unterscheiden und wie Sie berechnete Filter erstellen und verwalten."
tool: Segments
---

# Berechnete Filter {#calculated-filters}

> Mit berechneten Filtern können Sie sehr präzise Segmente über einen längeren Zeitraum der Nutzer:innenhistorie erstellen. Verwenden Sie berechnete Filter beispielsweise, um Nutzer:innen anzusprechen, die in den letzten 16 Monaten ein bestimmtes Produkt gekauft oder einen bestimmten Betrag für Ihren Dienst ausgegeben haben. Verfeinern Sie diese Zielgruppe mithilfe von Event-Eigenschaften, um das Targeting noch granularer zu gestalten.

{% alert important %}
Berechnete Filter befinden sich derzeit im Early Access. Wenn Sie am Early Access teilnehmen möchten, wenden Sie sich an Ihren geschäftskunden-Success-Manager.
{% endalert %}

## Funktionsweise {#how-it-works}

Braze Segments bieten Ihnen leistungsstarke Targeting-Tools, um dynamische Nutzer:innengruppen zu erstellen. Für die meisten Anwendungsfälle reicht dies aus, um Ihre Zielgruppe effektiv zu erreichen. Berechnete Filter sind für fortgeschrittene Anwendungsfälle konzipiert, bei denen Sie Verhaltensweisen von bis zu zwei Jahren analysieren oder komplexe Logik anwenden müssen – ohne die Datenaufbewahrung oder Systemleistung zu beeinträchtigen. Sie können Daten aus Ihrem eigenen [Data Warehouse]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) verwenden, um Ihre Zielgruppe weiter zu verfeinern.

Beispielsweise findet die Standard-Segmentierung von Braze Nutzer:innen, die bestimmte von Ihnen definierte Kriterien erfüllen, wie z. B. Nutzer:innen, die kürzlich eines Ihrer Produkte gekauft haben. Berechnete Filter ermöglichen es Ihnen, tiefer zu gehen – etwa Nutzer:innen zu identifizieren, die eine bestimmte Farbe eines bestimmten Produkts mindestens zweimal zwischen 18 und 24 Monaten gekauft haben. Berechnete Filter sind eine Erweiterung, keine Voraussetzung. Wenn Sie fortgeschrittenere Filter oder ein längeres historisches Zeitfenster benötigen, sind sie ein großartiges Werkzeug, das Ihnen hilft und gleichzeitig Ihre Datennutzung optimiert.

## Berechnete Filter und SQL-Segmenterweiterungen {#calculated-filters-and-sql-segment-extensions}

[SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und berechnete Filter helfen Ihnen beide, Zielgruppen basierend auf Kauf- und angepasstem Event-Verhalten zu erstellen, verwenden jedoch unterschiedliche Tools und Datenquellen. SQL-Segmenterweiterungen verwenden SQL, das Sie gegen Ihre verbundenen Snowflake-Daten schreiben.

| Verhalten | Berechnete Filter | SQL-Segmenterweiterungen |
|---|---|---|
| Wie Sie die Zielgruppe definieren | Wählen Sie Käufe, empfohlene E-Commerce-Events, Nachrichteninteraktionen oder angepasste Events sowie Anzahlen, Zeitfenster und optionale Eigenschaftsfilter | Schreiben Sie SQL gegen Ihre Snowflake-Verbindung; verwenden Sie Templates, inkrementelle Aktualisierung oder vollständige Aktualisierung |
| Wo die Logik ausgeführt wird | Kriterien und Aktualisierung werden in Braze als berechnete Filter verwaltet | Die Abfrage wird in Ihrem Warehouse-Kontext gemäß Ihrer Erweiterungskonfiguration ausgeführt |
| Filterlistenseite | Ein berechneter Filtertyp, die Spalte **Segments** zeigt, wie viele Segmente jeden Filter verwenden, die Status **Processing** und **Processing Failed** spiegeln den Generierungsstatus wider | Enthält eine Spalte **Type** und Filter, die je nach Erweiterungstyp variieren |
| Typische Anwendungsfälle | Kaufhäufigkeit, Gesamtausgaben, Anzahl angepasster Events und eigenschaftsbasierte Regeln über Ihr ausgewähltes Zeitfenster | Warehouse-gestützte Logik, Joins über Tabellen hinweg und historische Zeitfenster oder Aggregationen, die über das Formular für berechnete Filter hinausgehen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechnete Filter und SQL-Segmenterweiterungen" }

### Wann Sie berechnete Filter verwenden sollten {#when-to-use-calculated-filters}

Verwenden Sie berechnete Filter, wenn Dashboard-gesteuerte Kauf-, E-Commerce-, Nachrichteninteraktions- und angepasste Event-Regeln ausreichen und Sie kein beliebiges SQL über Warehouse-Tabellen benötigen.

### Wann Sie andere Segmenterweiterungstypen verwenden sollten {#when-to-use-other-segment-extension-types}

Verwenden Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), wenn Sie vollständiges SQL, Snowflake-gestützte Daten, Templates oder Aktualisierungsmodi benötigen, die für große oder komplexe Warehouse-Abfragen konzipiert sind. Verwenden Sie [CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments), wenn Sie SQL benötigen, das Ihr Data Warehouse direkt mit Daten aus [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)-Verbindungen abfragt.

### Berechnete Filter und Segmenterweiterungen gemeinsam verwenden {#use-calculated-filters-and-segment-extensions-together}

Ein Segment kann einen berechneten Filter zusammen mit einer SQL- oder CDI-Segmenterweiterung referenzieren – beispielsweise eine Warehouse-definierte Kohorte aus einer Erweiterung plus Kauf- oder angepasste Event-Regeln, die Sie im Builder für berechnete Filter pflegen.

## Einen berechneten Filter erstellen {#create-a-calculated-filter}

Um einen berechneten Filter zu erstellen, definieren Sie Kriterien basierend auf dem Nutzer:innenverhalten, speichern und aktivieren Sie dann den Filter, bevor Sie ihn in einem Segment verwenden.

### 1. Schritt: Details einrichten {#step-1-set-up-details}

1. Gehen Sie zu **Audience** > **Calculated Filters**.
2. Wählen Sie **Create Calculated Filter**.
3. Benennen Sie Ihren berechneten Filter, indem Sie die Nutzer:innen beschreiben, die Sie ansprechen möchten. Ein beschreibender Name erleichtert das Auffinden des Filters, wenn Sie ihn einem Segment hinzufügen.
4. (Optional) Fügen Sie [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu, um berechnete Filter in Ihrem Workspace zu organisieren.

Sie können auch **Enable recurring audience update** auswählen, um den Filter nach einem wiederkehrenden Zeitplan zu aktualisieren. Wenn Sie diese Einstellung nicht aktivieren, wird der berechnete Filter nur aktualisiert, wenn Sie den Filter bearbeiten oder **Update audience** auswählen.

### 2. Schritt: Kriterien auswählen {#step-2-choose-your-criteria}

Wählen Sie ein Kauf-, E-Commerce-, angepasstes oder Nachrichteninteraktions-Event-Kriterium für das Targeting. Nachdem Sie einen Event-Typ ausgewählt haben, wählen Sie das spezifische Event, wie oft die Nutzer:innen es abgeschlossen haben müssen (mehr als, weniger als oder gleich) und den Zeitraum.

Bei der Auswahl Ihres Zeitraums können Sie einen relativen Datumsbereich (die letzten X Tage), ein Startdatum, ein Enddatum oder einen exakten Datumsbereich angeben.

![Kriterien für berechnete Filter für Nutzer:innen, die ein angepasstes Event mehr als null Mal im Datumsbereich vom 21. Juni 2026 bis 27. Juni 2026 durchgeführt haben.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Event-Eigenschafts-Segmentierung {#event-property-segmentation}

Um die Targeting-Präzision zu erhöhen, wählen Sie **Add Property Filters**. Damit können Sie nach Eigenschaften Ihres Kauf-, E-Commerce- oder angepassten Events filtern. Braze unterstützt Event-Eigenschafts-Segmentierung basierend auf String-, numerischen, booleschen und Zeitobjekten.

Für String-Eigenschaften können Sie mehrere Werte auf einmal eingeben – beispielsweise Nutzer:innen mit einem Status gleich Gold, Silber oder Bronze ansprechen. Für empfohlene E-Commerce-Events wird das Eigenschafts-Dropdown mit den für dieses Event verfügbaren Eigenschaften befüllt.

{% alert note %}
Sie benötigen keine berechneten Filter, um Event-Eigenschaften in Ihrem Segment zu verwenden. Berechnete Filter erweitern lediglich das historische Zeitfenster, das zur Erstellung eines Standard-Segments verwendet wird. Sie können ein Realtime-Standard-[Segment]({{site.baseurl}}/user_guide/audience/segments) erstellen, das Event-Eigenschaften der letzten 30 Tage verwendet. Ebenso können Sie [Ihre Nachricht planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), um in Realtime basierend auf einer Event-Eigenschaft zu triggern – kein berechneter Filter erforderlich.
{% endalert %}

### 3. Schritt: Filter speichern und aktivieren {#step-3-save-and-activate-your-filter}

Wählen Sie **Save**, um Ihren berechneten Filter zu speichern. Sie können einen Filter speichern, ohne ihn zu aktivieren, aber Sie müssen einen Filter aktivieren, bevor er als Option beim Erstellen eines Segments erscheint.

Nachdem Sie einen berechneten Filter aktiviert haben, wertet Braze ihn in Realtime aus, wenn ein Segment, eine Kampagne oder ein Canvas, das darauf verweist, ausgewertet wird.

## Einen berechneten Filter in einem Segment verwenden {#use-a-calculated-filter-in-a-segment}

Nachdem Sie einen berechneten Filter erstellt und aktiviert haben, fügen Sie ihn beim Erstellen eines Segments oder beim Definieren einer Zielgruppe für eine Kampagne oder ein Canvas hinzu.

1. Öffnen Sie im Segment-Builder die Filterliste.
2. Wählen Sie unter **Other Filters** die Option **Existing Calculated Filter**.
3. Wählen Sie den berechneten Filter aus, den Sie in die Segmentdefinition aufnehmen möchten.

Nachdem Sie den Filter hinzugefügt haben, wählen Sie das Symbol neben dem Filter-Dropdown, um die Details des Filters anzuzeigen und die auf Ihre Zielgruppe angewendeten Kriterien zu bestätigen.

![Berechneter Filter in einem Segment-Builder mit einem Symbol zum Anzeigen weiterer Details.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Weitere Informationen zum Erstellen von Segmenten finden Sie unter [Ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Berechnete Filter verwalten {#manage-calculated-filters}

Gehen Sie zu **Audience** > **Calculated Filters**, um berechnete Filter in Ihrem Workspace anzuzeigen, zu bearbeiten und zu verwalten.

Die Seite **Calculated Filters** listet alle berechneten Filter in Ihrem Workspace auf. Sie können die Liste mit den verfügbaren Steuerelementen eingrenzen. Da es nur einen berechneten Filtertyp gibt, gibt es keine Option zum Filtern nach Typ, und die Tabelle enthält keine Spalte **Type**. Verwenden Sie die Spalte **Segments**, um zu sehen, wie viele Segmente jeden berechneten Filter verwenden.

### Statusbezeichnungen {#status-labels}

Jeder berechnete Filter zeigt einen der folgenden Status an. **Processing** und **Processing Failed** werden angezeigt, wenn die Mitgliedschaftsgenerierung läuft oder nicht erfolgreich abgeschlossen wurde.

| Status | Beschreibung |
|---|---|
| Active | Der Filter ist aktiviert und kann in Segmenten verwendet werden. |
| Draft | Der Filter ist gespeichert, aber nicht aktiviert. |
| Archived | Der Filter ist archiviert. |
| Processing | Braze verarbeitet ein Update des Filters. |
| Processing Failed | Der letzte Verarbeitungsversuch wurde nicht erfolgreich abgeschlossen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statusbezeichnungen" }

### Einzelne Filter bearbeiten und verwalten {#edit-and-manage-individual-filters}

Öffnen Sie das Zeilenmenü eines berechneten Filters, um ihn zu bearbeiten, zu archivieren, die Zielgruppe zu aktualisieren oder zu sehen, wie er im Messaging verwendet wird. Sie können einen berechneten Filter nicht bearbeiten, während er verarbeitet wird.

{% alert note %}
Ihr Workspace kann gleichzeitig bis zu 500 aktivierte berechnete Filter haben. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie dieses Limit erhöhen müssen.
{% endalert %}

#### Speichern versus Aktivieren {#save-versus-activate}

Sie können einen berechneten Filter speichern, ohne ihn zu aktivieren. Inaktive Filter verbleiben in Ihrem Workspace, können aber erst zu Segmenten hinzugefügt werden, wenn Sie sie aktivieren. Wählen Sie **Activate filter**, um den Filter in der Segmentierung zu verwenden.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich einen berechneten Filter erstellen, der mehrere angepasste Events verwendet? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

Bei der Verwendung berechneter Filter können Sie ein angepasstes Event, ein Kauf-Event, ein E-Commerce-Event oder eine Kanalinteraktion auswählen. Sie können jedoch mehrere berechnete Filter mit AND oder OR beim Erstellen des Segments kombinieren.

Sie können mehrere Events hinzufügen oder mehrere Snowflake-Tabellen referenzieren, wenn Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) verwenden.

### Kann ich berechnete Filter archivieren, wenn sie in einer aktiven Kampagne existieren? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

Nein. Bevor Sie einen berechneten Filter archivieren können, müssen Sie ihn aus allen aktiven Nachrichten entfernen.

### Kann ich Arrays in berechneten Filtern verwenden? {#can-i-use-arrays-in-calculated-filters}

Ja. Um Arrays zu verwenden, hängen Sie eckige Klammern (`[]`) an Ihren Eigenschaftsnamen an. Wenn Ihre Eigenschaft `location_code` ist, würden Sie `location_code[]` eingeben.

Braze verwendet `[]`, um Arrays zu durchlaufen und zu prüfen, ob ein Element im durchlaufenen Array mit der Event-Eigenschaft übereinstimmt. Beispielsweise könnten Sie einen berechneten Filter für Nutzer:innen erstellen, die mindestens einem Wert einer Array-Eigenschaft entsprechen.

### Wie berechnet Braze den Zeitraum für einen relativen Zeitraum von „letzte X Tage“? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Wenn berechnete Filter den relativen Zeitraum („letzte X Tage“) berechnen, wird die Startzeit auf Mitternacht UTC gesetzt. Beispielsweise wird für einen berechneten Filter, der am 16.09.2024 um 21:00 UTC aktualisiert wird und 10 Tage angibt, die Startzeit auf 06.09.2024 00:00 UTC gesetzt, nicht auf 06.09.2024 21:00 UTC.

Sie können jedoch die Zeitzonen angeben, indem Sie SQL-Segmente verwenden, um Nutzer:innen zu identifizieren, die das angepasste Event vor 10 Tagen basierend auf Mitternacht in der Unternehmenszeit durchgeführt haben, oder Nutzer:innen, die das Event vor 10 Tagen basierend auf der aktuellen Uhrzeit durchgeführt haben.