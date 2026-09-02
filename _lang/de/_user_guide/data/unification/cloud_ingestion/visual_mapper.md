---
nav_title: Visueller Mapper
article_title: "Cloud-Datenaufnahme: Visueller Mapper"
description: "Erfahren Sie, wie Sie eine Tabelle oder Ansicht aus Ihrem Data Warehouse mit dem visuellen Mapper der Cloud-Datenaufnahme synchronisieren können, ohne SQL zu schreiben."
page_order: 12
page_type: reference
toc_headers: h2
---

# Cloud-Datenaufnahme: Visueller Mapper {#cloud-data-ingestion-visual-mapper}

> Diese Seite beschreibt, wie Sie den visuellen Mapper verwenden, um eine Tabelle oder Ansicht aus Ihrem Data Warehouse mit Braze zu synchronisieren, ohne SQL zu schreiben oder Ihre Daten umzustrukturieren.

{% alert important %}
Der visuelle Mapper befindet sich derzeit in der Beta-Phase. Der visuelle Mapper ist für Nutzerattribut-Synchronisierungen aus allen Data-Warehouse-Quellen der Cloud-Datenaufnahme verfügbar, und weitere Synchronisierungstypen werden im Laufe der Beta-Phase hinzugefügt. Wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in oder Account Manager:in, um Zugang zu erhalten.
{% endalert %}

Mit dem visuellen Mapper können Sie eine vorhandene Tabelle oder Ansicht aus Ihrem Data Warehouse synchronisieren, ohne SQL zu schreiben oder Ihre Daten umzustrukturieren. Anstatt eine Braze-spezifische Tabelle mit den Spalten `EXTERNAL_ID`, `UPDATED_AT` und `PAYLOAD` zu erstellen, ordnen Sie die Spalten Ihrer vorhandenen Tabelle direkt im Dashboard den Braze-Feldern zu.

## Voraussetzungen {#prerequisites}

Bevor Sie eine Synchronisierung mit dem visuellen Mapper erstellen, benötigen Sie:

- Eine aktive Data-Warehouse-Quelle für die Cloud-Datenaufnahme. Falls Sie noch keine eingerichtet haben, lesen Sie [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- Den Namen der Tabelle oder Ansicht, die Sie synchronisieren möchten, so wie er in Ihrem Data Warehouse erscheint.
- Eine Spalte in Ihrer Tabelle, die einen unterstützten Nutzer-Bezeichner enthält, und eine Spalte mit einem Zeitstempel, den Braze für die inkrementelle Synchronisierung verwenden kann.

{% alert note %}
Braze führt nur schreibgeschützte Abfragen gegen Ihre Daten aus und ändert Ihre zugrunde liegenden Tabellen nicht. Temporäre Objekte können während der Abfrageausführung erstellt werden, werden aber nicht dauerhaft gespeichert.
{% endalert %}

## Eine Synchronisierung mit dem visuellen Mapper erstellen {#creating-a-sync-with-the-visual-mapper}

### Schritt 1: Synchronisierung konfigurieren {#step-1-configure-the-sync}

1. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Syncs** und wählen Sie **Create data sync**.
2. Wählen Sie einen Namen für Ihre Synchronisierung und wählen Sie eine aktive Datenquelle aus. Nur aktive Quellen können verwendet werden.
3. Wählen Sie unter **Data destination** die Option **Braze Data Platform**.
4. Wählen Sie unter **Data Type** die Option **User Attributes**.
5. Wählen Sie **Next: Data definition**.

### Schritt 2: Quellschema zuordnen {#step-2-map-your-source-schema}

1. Wählen Sie im Schritt **Data definition** die Option **Visual mapper**.
2. Geben Sie im Feld **Table** den Tabellen- oder Ansichtsnamen ein, wie er in Ihrem Data Warehouse erscheint.
3. Wählen Sie **Map source schema**. Braze liest das Schema Ihrer Tabelle oder Ansicht und listet jede Spalte mit ihrem erkannten Datentyp auf.

### Schritt 3: Zuordnungen überprüfen {#step-3-review-your-mappings}

Der Abschnitt **Review mapping** verfolgt zwei erforderliche Zuordnungen. Ihre Synchronisierung kann erst erstellt werden, wenn beide abgeschlossen sind:

- Ordnen Sie eine Spalte einem unterstützten Nutzer-Bezeichner zu: `external_id`, `braze_id`, `email`, `phone` oder einem Nutzer-Alias. Bezeichner-Optionen erscheinen unter **Identifiers** im Dropdown-Menü des Zielfelds.
- Ordnen Sie eine Spalte `updated_at` zu. Braze verwendet diesen Zeitstempel für die inkrementelle Synchronisierung bei wiederkehrenden Synchronisierungen, wobei jeder Synchronisierungslauf Zeilen importiert, bei denen `updated_at` später als der zuletzt synchronisierte Wert ist.

Für jede verbleibende Spalte können Sie:

- **Die Standardzuordnung beibehalten.** Jede Spalte wird einem Braze-Feld mit demselben Namen zugeordnet. Wenn das Feld in Ihrem Workspace noch nicht existiert, wird es als **New attribute** markiert und beim ersten Lauf der Synchronisierung erstellt.
- **Einem vorhandenen Feld zuordnen.** Durchsuchen Sie das Dropdown-Menü des Zielfelds, um eine Spalte einem vorhandenen Standard- oder angepassten Attribut in Ihrem Workspace zuzuordnen.
- **Einem neuen Feld zuordnen.** Geben Sie direkt im Dropdown-Menü des Zielfelds einen Namen ein, um eine Spalte einem neuen angepassten Attribut zuzuordnen.
- **Die Spalte ausschließen.** Deaktivieren Sie das Kontrollkästchen **Import**, um eine Spalte von der Synchronisierung auszuschließen.

{% alert tip %}
Bevor Sie ein neues Attribut erstellen, durchsuchen Sie das Ziel-Dropdown nach einem vorhandenen. Wenn Ihre Tabelle beispielsweise eine Spalte `fav_color` hat, Ihr Workspace aber bereits `favorite_color` erfasst, sollten Sie `fav_color` auf `favorite_color` zuordnen, anstatt ein weiteres Attribut zu erstellen.
{% endalert %}

{% alert note %}
Felder, deren Datentyp nicht mit dem erkannten Typ Ihrer Spalte übereinstimmt, zeigen eine Warnung **Type mismatch** an. Sie können trotzdem fortfahren, aber nicht übereinstimmende Werte können als Zeilenfehler bei der Synchronisierung fehlschlagen. Sie können Zeilenfehler in den Laufdetails einer Synchronisierung einsehen.
{% endalert %}

### Schritt 4: Vorschau und Validierung {#step-4-preview-and-validate}

Wählen Sie **Preview and validate**, um eine schreibgeschützte Prüfung gegen Ihre Tabelle oder Ansicht durchzuführen. Die Vorschau zeigt die ersten 10 Zeilen mit Ihren zugeordneten Feldnamen und enthält nur Spalten, die Sie importieren.

### Schritt 5: Synchronisierung abschließen {#step-5-finish-creating-the-sync}

1. Geben Sie im Schritt **Notifications** mindestens eine Kontakt-E-Mail-Adresse für Benachrichtigungen bei Synchronisierungsfehlern ein. Optional können Sie **Row Error**-Benachrichtigungen (werden gesendet, wenn ein Prozentsatz der Zeilen nicht aktualisiert werden kann) und **Sync success**-Benachrichtigungen aktivieren.
2. Aktivieren Sie im Schritt **Schedule** die Option **Recurring sync**, um die Synchronisierung nach einem Zeitplan auszuführen, oder lassen Sie sie deaktiviert für eine einmalige Synchronisierung.
3. Überprüfen Sie den Schritt **Summary**. Er listet Ihre Konfiguration auf, welche Attribute neu oder bereits vorhanden sind und welche Spalten aufgrund von Datentypenproblemen oder Ihrer Auswahl vom Import ausgeschlossen wurden.
4. Wählen Sie **Create sync**. Sie können auch in jedem Schritt **Save as draft** wählen, um später fortzufahren.

## Umgang mit Schemaänderungen {#handling-schema-changes}

Der visuelle Mapper prüft das Schema Ihrer Tabelle oder Ansicht bei jedem Synchronisierungslauf und reagiert je nach Art der Änderung:

| Änderung in Ihrer Quelltabelle | Synchronisierungsverhalten |
|---|---|
| Eine neue Spalte wird hinzugefügt | Die Synchronisierung wird fortgesetzt, aber neue Spalten werden nicht automatisch synchronisiert. Um eine einzubeziehen, bearbeiten Sie die Synchronisierung und ordnen Sie sie zu. |
| Eine zugeordnete Spalte wird entfernt | Der Synchronisierungslauf schlägt fehl und die Synchronisierung wird pausiert. Die Schemaänderung wird in den Laufdetails der Synchronisierung angezeigt, und Ihre Benachrichtigungskontakte erhalten eine E-Mail-Benachrichtigung. |
| Eine zugeordnete Spalte wird umbenannt | Wird behandelt wie eine entfernte Spalte plus eine neue Spalte. |
| Der Datentyp einer Spalte ändert sich | Wird nicht als Schemaänderung erkannt. Inkompatible Werte werden als Zeilenfehler in den Synchronisierungsprotokollen gemeldet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umgang mit Schemaänderungen" }

Um eine pausierte Synchronisierung nach dem Entfernen einer Spalte fortzusetzen, wählen Sie **Edit sync** und überprüfen Sie Ihre Zuordnungen. Die entfernte Spalte ist markiert und erscheint nicht mehr im Mapper. Das Speichern Ihrer Zuordnungen bestätigt, dass die Synchronisierung ohne diese Spalte fortgesetzt werden soll. Alternativ können Sie, wenn die Daten in eine andere Spalte verschoben wurden, die neue Spalte zuordnen, bevor Sie speichern.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich meine Zuordnungen nach dem Erstellen einer Synchronisierung bearbeiten? {#can-i-edit-my-mappings-after-a-sync-is-created}

Ja. Bearbeiten Sie die Synchronisierung und wählen Sie **View and edit mapping**. Das aktuelle Schema der Quelltabelle wird geladen, wobei Ihre vorherigen Zuordnungen aus der Erstellung der Synchronisierung gespeichert sind. Sie können Ihre Zuordnungen von dort aus bearbeiten.

### Kann ich meine Daten im visuellen Mapper transformieren? {#can-i-transform-my-data-in-the-visual-mapper}

Nein. Der visuelle Mapper synchronisiert Spaltenwerte genau so, wie sie in Ihrer Quelle erscheinen. Er unterstützt keine Transformationen, bedingte Logik oder Joins über Tabellen hinweg. Für diese Anwendungsfälle verwenden Sie die SQL-Option im Schritt „Data definition“, um Ihre Daten mit einer Abfrage zu formen. Weitere Informationen finden Sie unter [Cloud-Datenaufnahme: SQL-Editor]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor).

### Ändern sich meine bestehenden CDI-Synchronisierungen? {#do-my-existing-cdi-syncs-change}

Nein. Synchronisierungen, die das bestehende Tabellenformat mit den Spalten `EXTERNAL_ID`, `UPDATED_AT` und `PAYLOAD` verwenden, funktionieren weiterhin, und Sie können sie weiterhin erstellen, indem Sie im Schritt **Data definition** die Option **Table** auswählen. Eine Migration ist nicht erforderlich.

### Wie wird meine Braze-Nutzung beeinflusst? {#how-is-my-braze-usage-affected}

Jede Spalte, die Sie importieren, wird als Attribut-Aktualisierung geschrieben, und die Datenpunkt-Abrechnung funktioniert genauso wie bei anderen CDI-Nutzerdaten-Synchronisierungen. Das Ausschließen von Spalten, die Sie nicht benötigen, hält Ihre Synchronisierungen effizient. Weitere Informationen finden Sie unter [Best Practices für die Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).