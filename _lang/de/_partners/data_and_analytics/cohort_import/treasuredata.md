---
nav_title: Treasure Data
article_title: Treasure Data-Kohortenimport
description: "Dieser Referenzartikel beschreibt die Kohortenimport-Funktion von Treasure Data."
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# Treasure Data-Kohortenimport {#treasure-data-cohort-import}

> Dieser Artikel beschreibt, wie Sie Kohorten von Treasure Data nach Braze importieren, damit Sie zielgerichtete Kampagnen auf der Grundlage von Daten versenden können, die möglicherweise nur in Ihrem Warehouse vorhanden sind.

{% alert important %}
Dieses Feature befindet sich derzeit in der Beta-Phase. Für weitere Informationen wenden Sie sich bitte an Ihre Vertretung von Treasure Data und Braze.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Treasure Data-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Treasure Data](https://www.treasuredata.com/)-Konto. |
| Braze-Datenimport-Schlüssel | Diesen finden Sie im Braze-Dashboard unter **Partnerintegrationen** > **Technologie-Partner** und dann **Treasure Data** auswählen. |
| Braze-REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Statische IP-Adresse von Treasure Data | Die statische IP-Adresse von Treasure Data ist der Zugangspunkt und die Quelle der Verknüpfung für diese Integration. Um die statische IP-Adresse zu ermitteln, wenden Sie sich an Ihre Treasure Data-Kundenerfolgs-Vertretung oder an den technischen Support von Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Datenimport-Integration {#data-import-integration}

### 1. Schritt: Braze-Datenimport-Schlüssel abrufen {#step-1-get-your-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Treasure Data** aus. Hier finden Sie Ihren REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.

### 2. Schritt: Datenverbindung erstellen {#step-2-create-a-data-connection}

Bevor Sie Ihre Datenverbindung in Treasure Data erstellen, müssen Sie sich authentifizieren. Wählen Sie zunächst **Integrations Hub** und dann **Catalog**.

![Treasure Data Integrations-Hub-Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %})

Suchen Sie im **Catalog** nach der Braze-Integration, bewegen Sie dann den Mauszeiger über das Symbol und wählen Sie **Create Authentication**. Geben Sie Ihre Zugangsdaten ein, vergeben Sie einen Namen für Ihre Authentifizierung und wählen Sie dann **Done**.

![Treasure Data Integrations-Hub-Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %})

### 3. Schritt: Kohorten-Zielgruppe definieren {#step-3-define-your-cohort-audience}

Synchronisieren Sie Ihre Kohorten mit Braze durch eine Aktivierung im **Audience Studio** oder durch Ausführen einer Abfrage in der **Data Workbench**.

{% alert important %}
Es werden nur Nutzer:innen aus einer Kohorte hinzugefügt oder entfernt, die bereits in Braze existieren. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### Schritt 3.1: Abfrage definieren {#step-31-define-your-query}

{% alert note %}
Abfragespalten müssen mit den genauen Spaltennamen und dem Datentyp angegeben werden. Die Abfragespalten müssen mindestens eine der Spalten enthalten: `user_ids`, `device_ids` oder eine Braze-Alias-Spalte, die mit der Konfiguration auf der UI übereinstimmt. Nur Nutzer:innen-Profile, die in Braze existieren, werden zu einer Kohorte hinzugefügt. Der Kohortenimport erstellt keine neuen Nutzer:innen-Profile.
{% endalert %}

1. Navigieren Sie zu **Data Workbench** > **Queries**.
2. Wählen Sie **New Query**.
3. Führen Sie die Abfrage aus, um die Ergebnismenge zu überprüfen.

![Treasure Data Integrations-Hub-Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Anwendungsfall: Kohorten nach Bezeichner synchronisieren {#use-case-syncing-cohorts-by-identifier}

{% subtabs local %}
{% subtab Syncing External IDs %}
Hier sehen Sie eine Beispieltabelle in Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
Der Spaltenname muss `user_ids` lauten, sonst schlägt die Synchronisierung fehl.
{% endalert %}

Um Kohorten unter Verwendung der externen ID zu synchronisieren, führen Sie die folgende Abfrage aus:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Nach Ausführung der Abfrage werden diese Nutzer-Aliase der Kohorte in Braze hinzugefügt:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Hier sehen Sie eine Beispieltabelle in Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

Um Kohorten mit dem Nutzer-Alias zu synchronisieren, führen Sie die folgende Abfrage aus:

```sql
SELECT
  email
FROM
  example_cohort_table
```

Nach Ausführung der Abfrage werden diese Nutzer-Aliase der Kohorte in Braze hinzugefügt:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Hier sehen Sie eine Beispieltabelle in Treasure Data:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
Der Spaltenname muss `device_ids` lauten, sonst schlägt die Synchronisierung fehl.
{% endalert %}

Um Kohorten unter Verwendung der Geräte-ID zu synchronisieren, führen Sie die folgende Abfrage aus:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Nach Ausführung der Abfrage werden diese Geräte-IDs der Kohorte in Braze hinzugefügt:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Schritt 3.2: Ziel des Ergebnisexports festlegen {#step-32-specify-the-result-export-target}

Sobald die Abfrage erstellt wurde, wählen Sie **Export Results**. Sie können eine vorhandene Authentifizierung auswählen, z. B. die in den vorherigen Schritten erstellte, oder eine neue Authentifizierung für die Ausgabe erstellen.

![Treasure Data Integrations-Hub-Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %})


| Ergebnisexport-Abbildung |	Beschreibung	|
| ----------- | ----------- |
| Kohorten-ID	| Dies ist der Backend-Kohorten-Bezeichner, der an Braze gesendet wird. 	|
| Kohortenname (optional)	| Dies ist der Name, der innerhalb des Kohorten-Filters im Braze-Segmentierungs-Tool angezeigt wird. Wenn dieser nicht festgelegt ist, wird die `Cohort ID` als `Cohort Name` verwendet.	|
| Operation	| Wird verwendet, um zu bestimmen, ob die Abfrage Profile aus der Kohorte in Braze hinzufügen oder entfernen soll.	|
| Aliase (optional) | Wenn definiert, wird der Name der entsprechenden Spalte innerhalb Ihrer Abfrage als `alias_label` gesendet und die Werte jeder Zeile in der Spalte werden als `alias_name` gesendet.	|
| Thread-Anzahl | Anzahl der gleichzeitigen API-Aufrufe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3.2: Ziel des Ergebnisexports festlegen" }

Folgen Sie den [Schritten von Treasure Data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget), um Ihren Export für Ihren Anwendungsfall zu konfigurieren.

#### Schritt 3.3: Abfrage ausführen {#step-33-execute-the-query}

Speichern Sie die Abfrage unter einem Namen und führen Sie sie aus, oder führen Sie die Abfrage einfach aus. Nach erfolgreichem Abschluss der Abfrage wird das Abfrageergebnis automatisch nach Braze exportiert.

{% endtab %}
{% tab Audience Studio %}
#### Schritt 3.1: Aktivierung erstellen {#step-31-create-an-activation}

Erstellen Sie ein neues Segment oder wählen Sie ein bestehendes Segment, um es als Kohorte mit Braze zu synchronisieren. Wählen Sie innerhalb des Segments **Create activation**.

#### Schritt 3.2: Aktivierungsdetails ausfüllen {#step-32-fill-out-your-activation-details}

![Treasure Data Integrations – Aktivierungsdetails]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %})

| Einstellung der Aktivierungsdetails |	Beschreibung	|
| ----------- | ----------- |
| Aktivierungsname	| Der Name Ihrer Aktivierung.	|
| Aktivierungsbeschreibung| Eine kurze Beschreibung der Aktivierung.	|
| Authentifizierung	| Wählen Sie die in [Schritt 2](#schritt-2-datenverbindung-erstellen) erstellte Braze-Kohorten-Authentifizierung.	|
| Kohorten-ID	| Dies ist der Backend-Kohorten-Bezeichner, der an Braze gesendet wird. 	|
| Kohortenname (optional)	| Dies ist der Name, der innerhalb des Kohorten-Filters im Braze-Segmentierungs-Tool angezeigt wird. Wenn dieser nicht festgelegt ist, wird die `Cohort ID` als `Cohort Name` verwendet.	|
| Operation	| Wird verwendet, um zu bestimmen, ob die Abfrage Profile aus der Kohorte in Braze hinzufügen oder entfernen soll.	|
| Aliase (optional) | Wenn definiert, wird der Name der entsprechenden Spalte innerhalb Ihrer Abfrage als `alias_label` gesendet und die Werte jeder Zeile in der Spalte werden als `alias_name` gesendet.	|
| Thread-Anzahl | Anzahl der gleichzeitigen API-Aufrufe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3.2: Aktivierungsdetails ausfüllen" }

#### Schritt 3.3: Ausgabe-Abbildung einrichten {#step-33-set-up-output-mapping}

![Treasure Data Integrations – Aktivierung Ausgabe-Abbildung]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %})

| Aktivierung Ausgabe-Abbildung |	Beschreibung	|
| ----------- | ----------- |
| Attribut-Spalten	| Bestimmen Sie die Spalten aus Ihrer Segmentdatenbank, die bei der Synchronisierung von Profilen mit einer Braze-Kohorte als Bezeichner abgebildet werden sollen.	|
| String Builder| Der String Builder ist für die Braze-Integration nicht erforderlich.	|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3.3: Ausgabe-Abbildung einrichten" }

{% alert important %}
 - Wenn Sie `device_id` als Bezeichner verwenden, muss der **Name der Ausgabespalte** `device_ids` lauten.
 - Wenn Sie Aliase als Bezeichner verwenden, muss der **Name der Ausgabespalte** der Name der entsprechenden Spalte innerhalb Ihrer Abfrage sein, die als `alias_label` gesendet wird, und die Werte jeder Zeile in der Spalte werden als `alias_name` gesendet.
 - Wenn Sie `external_id` als Bezeichner verwenden, muss der **Name der Ausgabespalte** `user_ids` lauten.
{% endalert %}

Alle nicht relevanten oder falsch benannten Spaltennamen werden ignoriert. Sie können mehr als einen Bezeichner für Ihre Synchronisierungen verwenden.

#### Schritt 3.4: Aktivierungszeitplan definieren {#step-34-define-your-activation-schedule}

Definieren Sie den gewünschten Synchronisierungszeitplan und speichern Sie Ihre Aktivierung.

![Treasure Data Integrations – Aktivierungszeitplan]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### 4. Schritt: Braze-Segment aus dem Treasure Data-Export erstellen {#step-4-create-a-braze-segment-from-the-treasure-data-export}

Navigieren Sie in Braze zu **Segments**, erstellen Sie ein neues Segment und wählen Sie **Treasure Data Cohorts** als Filter. Von hier aus können Sie wählen, welche Treasure Data-Kohorte Sie einbeziehen möchten. Nachdem Ihr Treasure Data-Kohorten-Segment erstellt wurde, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.

![Treasure Data Integrations-Hub-Katalog]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %})

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder ihren `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden und müssen über ihre `external_id` oder ihren `alias` identifiziert werden.