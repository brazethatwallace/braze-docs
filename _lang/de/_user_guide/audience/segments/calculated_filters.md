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
Berechnete Filter befinden sich derzeit im Early Access. Wenn Sie am Early Access teilnehmen möchten, wenden Sie sich an Ihren Account Manager:in.
{% endalert %}

## Funktionsweise {#how-it-works}

Braze Segments bieten Ihnen leistungsstarke Targeting-Tools, um dynamische Gruppen von Nutzer:innen zu erstellen. Für die meisten Anwendungsfälle reicht dies aus, um Ihre Zielgruppe effektiv zu erreichen. Berechnete Filter sind für fortgeschrittene Anwendungsfälle konzipiert, bei denen Sie Verhaltensweisen von bis zu zwei Jahren analysieren oder komplexe Logik anwenden müssen – ohne die Datenaufbewahrung oder die Systemleistung zu beeinträchtigen. Verwenden Sie **Nutzeraktivitätsfilter** für Kauf- und E-Commerce-Event-Kriterien oder **Datenobjektfilter** für das Targeting von Konten und angepassten Objekten.

Beispielsweise findet die Braze-Standardsegmentierung Nutzer:innen, die bestimmte von Ihnen definierte Kriterien erfüllen, wie z. B. die Identifizierung von Nutzer:innen, die kürzlich eines Ihrer Produkte gekauft haben. Mit berechneten Filtern können Sie tiefer gehen – etwa Nutzer:innen identifizieren, die eine bestimmte Farbe eines bestimmten Produkts mindestens zweimal vor 18 bis 24 Monaten gekauft haben. Berechnete Filter sind eine Erweiterung, keine Voraussetzung. Wenn Sie fortgeschrittenere Filter oder ein längeres historisches Zeitfenster benötigen, sind sie ein hervorragendes Tool, das Ihnen hilft und gleichzeitig Ihre Datennutzung optimiert hält.

## Berechnete Filter und SQL-Segmenterweiterungen {#calculated-filters-and-sql-segment-extensions}

[SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) und berechnete Filter helfen Ihnen beide dabei, Zielgruppen auf Basis von Kaufverhalten zu erstellen, sie verwenden jedoch unterschiedliche Werkzeuge und Datenquellen. SQL-Segmenterweiterungen nutzen SQL, das Sie gegen Ihre verbundenen Snowflake-Daten schreiben.

| Verhalten | Berechnete Filter | SQL-Segmenterweiterungen |
|---|---|---|
| Wie Sie die Zielgruppe definieren | Wählen Sie Käufe oder empfohlene E-Commerce-Events aus, sowie Anzahlen, Zeitfenster und optionale Eigenschaftsfilter | Schreiben Sie SQL gegen Ihre Snowflake-Verbindung; nutzen Sie Templates, inkrementelle oder vollständige Aktualisierung |
| Wo die Logik ausgeführt wird | Kriterien und Aktualisierung werden in Braze als berechnete Filter verwaltet | Die Abfrage wird in Ihrem Data-Warehouse-Kontext gemäß Ihrer Erweiterungskonfiguration ausgeführt |
| Filterlistenseite | Eine gemeinsame Liste für Nutzer:innenaktivitäts- und Datenobjektfilter; die Spalte **Segments** zeigt, wie viele Segmente jeden Filter verwenden, und Verarbeitungsstatusanzeigen spiegeln den Generierungsstatus wider | Enthält eine Spalte **Type** und Filter, die je nach Erweiterungstyp variieren |
| Typische Anwendungsfälle | Kaufhäufigkeit, Gesamtausgaben und eigenschaftsbasierte Regeln über Ihr ausgewähltes Zeitfenster | Warehouse-gestützte Logik, Joins über Tabellen hinweg und historische Zeitfenster oder Aggregationen, die über das Formular des berechneten Filters hinausgehen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechnete Filter und SQL-Segmenterweiterungen" }

### Wann Sie berechnete Filter verwenden sollten {#when-to-use-calculated-filters}

Verwenden Sie berechnete Filter, wenn Dashboard-gestützte Nutzer:innenaktivitäts- oder Datenobjektregeln ausreichen und Sie kein beliebiges SQL über Data-Warehouse-Tabellen hinweg benötigen.

### Wann Sie andere Segmenterweiterungstypen verwenden sollten {#when-to-use-other-segment-extension-types}

Verwenden Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), wenn Sie vollständiges SQL, Snowflake-gestützte Daten, Templates oder Aktualisierungsmodi benötigen, die für große oder komplexe Data-Warehouse-Abfragen konzipiert sind. Verwenden Sie [CDI-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments), wenn Sie SQL benötigen, das Ihr Data Warehouse direkt über Verbindungen aus der [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) abfragt.

### Berechnete Filter und Segmenterweiterungen zusammen verwenden {#use-calculated-filters-and-segment-extensions-together}

Ein Segment kann einen berechneten Filter zusammen mit einer SQL- oder CDI-Segmenterweiterung referenzieren – zum Beispiel eine im Data Warehouse definierte Kohorte aus einer Erweiterung plus Kaufregeln, die Sie im Builder für berechnete Filter pflegen.

## Berechneten Filter erstellen {#create-a-calculated-filter}

Um einen berechneten Filter zu erstellen, wählen Sie einen Filtertyp aus (falls aufgefordert), definieren Sie Ihre Kriterien und speichern und aktivieren Sie den Filter, bevor Sie ihn in einem Segment verwenden.

### Schritt 1: Details einrichten {#step-1-set-up-details}

1. Gehen Sie zu **Audience** > **Calculated Filters**.
2. Wählen Sie **Create filter** aus.
3. Wenn in Ihrem Workspace [Accounts]({{site.baseurl}}/user_guide/data/activation/accounts) aktiviert sind, wählen Sie einen Filtertyp aus:
   - **User activity filters:** Aktionen und Verhaltensweisen von Nutzer:innen.
   - **Data Object filters:** Attribute und Beziehungen für Datenobjekte.
4. Geben Sie einen Namen ein, der die Zielgruppe beschreibt, die Sie ansprechen möchten. Ein beschreibender Name erleichtert das Auffinden des Filters, wenn Sie ihn einem Segment hinzufügen.
5. (Optional) Fügen Sie [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu, um berechnete Filter in Ihrem Workspace zu organisieren.

Wählen Sie bei **User activity filters** die Option **Enable recurring audience update** aus, um den Filter nach einem wiederkehrenden Zeitplan zu aktualisieren. Wenn Sie diese Einstellung nicht aktivieren, wird der Filter nur aktualisiert, wenn Sie ihn manuell bearbeiten oder **Update audience** auswählen. **Data Object filters** werden stündlich aktualisiert.

### Schritt 2: Kriterien festlegen {#step-2-choose-your-criteria}

{% tabs %}
{% tab Data Object filters %}

Wenn Sie **Data Object filters** ausgewählt haben, wählen Sie ein Datenobjekt und fügen Sie dann Attribut-, Beziehungs- oder Filtergruppenbedingungen hinzu. Informationen zum kontobasierten Targeting finden Sie unter [Account-Objekte]({{site.baseurl}}/user_guide/data/activation/accounts).

{% endtab %}
{% tab User activity filters %}

Wenn **Create filter** den User-Activity-Builder direkt öffnet oder Sie **User activity filters** auswählen, wählen Sie eine der folgenden **Criterion**-Optionen für das Targeting aus:

- **Made a Purchase**
- **Performed an eCommerce event**

Nachdem Sie einen Ereignistyp ausgewählt haben, wählen Sie das spezifische Ereignis, wie oft die Nutzer:innen es abgeschlossen haben müssen (mehr als, weniger als oder gleich) und den Zeitraum.

{% alert note %}
Die Filter **mehr als** und **weniger als** sind exklusiv – sie schließen die angegebene Zahl nicht ein. Zum Beispiel umfasst ein Filter für **mehr als 4 Mal und weniger als 16 Mal** Nutzer:innen, die 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 oder 15 Mal gezählt wurden.
{% endalert %}

Bei der Auswahl Ihres Zeitraums können Sie einen relativen Datumsbereich (die letzten X Tage), ein Startdatum, ein Enddatum oder einen exakten Datumsbereich angeben. Geben Sie für relative Bereiche **1** bis **730** Tage (zwei Jahre) ein. Bei absoluten Datumsbereichen muss das Startdatum innerhalb der letzten zwei Jahre liegen und das Enddatum innerhalb der nächsten zwei Jahre.

#### Event-Eigenschafts-Segmentierung {#event-property-segmentation}

Um die Targeting-Präzision zu erhöhen, wählen Sie **Add event property filters** aus. Damit können Sie nach Eigenschaften Ihres Kauf- oder E-Commerce-Ereignisses filtern. Braze unterstützt Event-Eigenschafts-Segmentierung basierend auf String-, numerischen, booleschen und Zeitobjekten.

Für String-Eigenschaften können Sie mehrere Werte gleichzeitig eingeben – zum Beispiel, um Nutzer:innen mit einem Status von „Gold“, „Silber“ oder „Bronze“ anzusprechen. Bei empfohlenen E-Commerce-Ereignissen wird das Eigenschafts-Dropdown mit den für das jeweilige Ereignis verfügbaren Eigenschaften gefüllt.

{% alert note %}
Sie benötigen keine berechneten Filter, um Event-Eigenschaften in Ihrem Segment zu verwenden. Berechnete Filter erweitern lediglich das historische Zeitfenster, das zum Erstellen eines Standard-Segments verwendet wird. Sie können ein Realtime-Standard-[Segment]({{site.baseurl}}/user_guide/audience/segments) erstellen, das Event-Eigenschaften der letzten 30 Tage nutzt. Ebenso können Sie [Ihre Nachricht planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery), um sie in Echtzeit basierend auf einer Event-Eigenschaft auszulösen – ganz ohne berechneten Filter.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 3: Filter speichern und aktivieren {#step-3-save-and-activate-your-filter}

Wählen Sie **Save as draft** aus, um einen neuen berechneten Filter zu speichern, ohne ihn zu aktivieren. Wählen Sie bei einem bereits aktivierten Filter **Save changes** aus, um Ihre Änderungen zu speichern. Sie müssen **Activate filter** auswählen, bevor der Filter im Segment-Builder verfügbar ist.

Nachdem Sie einen berechneten Filter aktiviert haben, beginnt Braze mit der Berechnung der Zielgruppe. Sobald die Verarbeitung abgeschlossen ist, können Sie den Filter beim Erstellen einer Zielgruppe auswählen.

## Einen berechneten Filter in einem Segment verwenden {#use-a-calculated-filter-in-a-segment}

Nachdem Sie einen berechneten Filter erstellt und aktiviert haben, fügen Sie ihn beim Erstellen eines Segments oder beim Definieren einer Zielgruppe für eine Campaign oder ein Canvas hinzu.

1. Öffnen Sie im Segment-Builder die Filterliste.
2. Wählen Sie unter **Andere Filter** die Option **Vorhandener berechneter Filter** aus.
3. Wählen Sie den berechneten Filter aus, der in die Segmentdefinition aufgenommen werden soll.

Nachdem Sie den Filter hinzugefügt haben, wählen Sie das Symbol neben dem Filter-Dropdown aus, um die Details des Filters anzuzeigen und die auf Ihre Zielgruppe angewendeten Kriterien zu bestätigen.

![Berechneter Filter in einem Segment-Builder mit einem Symbol zum Anzeigen weiterer Details.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Weitere Informationen zum Erstellen von Segments finden Sie unter [Ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Berechnete Filter verwalten {#manage-calculated-filters}

Gehen Sie zu **Audience** > **Calculated Filters**, um berechnete Filter in Ihrem Workspace anzuzeigen, zu bearbeiten und zu verwalten.

Die Seite **Calculated Filters** listet Filter für Nutzer:innenaktivitäten und Datenobjekte gemeinsam auf. Sie können die Liste mit den verfügbaren Steuerelementen eingrenzen, aber die Seite enthält keine Filterfunktion nach Typ und keine Spalte **Type**. Verwenden Sie die Spalte **Segments**, um zu sehen, wie viele Segments jeden berechneten Filter verwenden.

### Statusbezeichnungen {#status-labels}

Jeder berechnete Filter zeigt einen der folgenden Status an. **Processing** und **Processing failed** werden angezeigt, wenn die Mitgliedschaftsgenerierung gerade läuft oder nicht erfolgreich abgeschlossen wurde.

| Status | Beschreibung |
|---|---|
| Active | Der Filter ist aktiviert und kann in Segments verwendet werden. |
| Draft | Der Filter ist gespeichert, aber nicht aktiviert. |
| Archived | Der Filter ist archiviert. |
| Refresh disabled | Wiederkehrende Zielgruppen-Updates sind deaktiviert. Braze kann diesen Status automatisch setzen, wenn ein Filter mit geplanter Aktualisierung nicht verwendet wird. |
| Processing | Braze verarbeitet ein Update des Filters. |
| Processing failed | Der letzte Verarbeitungsversuch wurde nicht erfolgreich abgeschlossen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statusbezeichnungen" }

### Einzelne Filter bearbeiten und verwalten {#edit-and-manage-individual-filters}

Öffnen Sie das Zeilenmenü eines berechneten Filters, um eine Aktion auszuführen. Die verfügbaren Aktionen hängen vom Status des Filters ab.

Für Filter, die nicht archiviert sind, enthält das Zeilenmenü **Edit**, **Messaging use**, **Archive** und **Update audience**. **Update audience** ist für aktive Filter verfügbar, die gerade nicht verarbeitet werden. Sie können einen berechneten Filter während der Verarbeitung bearbeiten, Ihre Änderungen jedoch erst speichern, wenn die Verarbeitung abgeschlossen ist.

{% alert note %}
Ihr Workspace kann gleichzeitig bis zu 100 aktive berechnete Filter enthalten. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie dieses Limit erhöhen müssen.
{% endalert %}

#### Archivierung aufheben {#unarchive}

Sie können die Archivierung eines Filters auf eine der folgenden Arten aufheben:

- Wählen Sie **Unarchive** im Zeilenmenü des Filters.
- Wählen Sie einen oder mehrere archivierte Filter aus und wählen Sie dann **Unarchive**.
- Öffnen Sie einen archivierten berechneten Filter und wählen Sie **Unarchive** auf dessen Seite.

Wenn Sie die Archivierung eines Filters aufheben, kehrt sein Status zu dem zurück, was er vor der Archivierung war:

- Ein Entwurf kehrt zu **Draft** zurück.
- Ein aktivierter Filter kehrt zu **Active** zurück, wird auf das Limit aktiver Filter angerechnet, und Braze startet eine Zielgruppenaktualisierung.

Warten Sie, bis die Verarbeitung abgeschlossen ist, bevor Sie die Archivierung eines Filters aufheben, der **Processing** anzeigt. Wenn Sie das Limit aktiver Filter erreicht haben, archivieren Sie einen aktiven Filter, bevor Sie die Archivierung eines anderen aktiven Filters aufheben.

#### Speichern versus Aktivieren {#save-versus-activate}

Sie können einen berechneten Filter speichern, ohne ihn zu aktivieren. Inaktive Filter verbleiben in Ihrem Workspace, können aber erst zu Segments hinzugefügt werden, wenn Sie sie aktivieren. Wählen Sie **Activate filter**, um den Filter in der Segmentierung zu verwenden.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich einen berechneten Filter archivieren, wenn er in Verwendung ist? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

Nein. Bevor Sie einen berechneten Filter archivieren können, müssen Sie ihn aus allen Campaigns, Canvases und Segments entfernen, die ihn verwenden. Sie können einen Filter auch nicht archivieren, während sein Status **Verarbeitung** lautet; warten Sie, bis die Verarbeitung abgeschlossen ist.

### Kann ich Arrays in berechneten Filtern verwenden? {#can-i-use-arrays-in-calculated-filters}

Ja. Um Arrays zu verwenden, hängen Sie eckige Klammern (`[]`) an Ihren Eigenschaftsnamen an. Wenn Ihre Eigenschaft `location_code` lautet, würden Sie `location_code[]` eingeben.

Braze verwendet `[]`, um Arrays zu durchlaufen und zu prüfen, ob ein Element im durchlaufenen Array mit der Event-Eigenschaft übereinstimmt. Sie könnten beispielsweise einen berechneten Filter für Nutzer:innen erstellen, die mit mindestens einem Wert einer Array-Eigenschaft übereinstimmen.

### Wie berechnet Braze den Zeitraum für einen relativen Zeitraum von „letzte X Tage“? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Wenn berechnete Filter den relativen Zeitraum („letzte X Tage“) berechnen, wird die Startzeit auf Mitternacht UTC festgelegt. Bei einem berechneten Filter, der am 16.09.2024 um 21:00 UTC aktualisiert wird und 10 Tage angibt, wird die Startzeit beispielsweise auf den 06.09.2024 00:00 UTC festgelegt, nicht auf den 06.09.2024 21:00 UTC. Berechnete Filter verwenden für Zeitfenster immer UTC; die Zeitzone Ihres Workspace wird nicht berücksichtigt.

Sie können jedoch Zeitzonen angeben, indem Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) verwenden, um Nutzer:innen zu identifizieren, die ein Event vor 10 Tagen basierend auf Mitternacht in der Unternehmenszeit durchgeführt haben, oder Nutzer:innen, die das Event vor 10 Tagen basierend auf der aktuellen Uhrzeit durchgeführt haben.