---
nav_title: Treasure Data
article_title: Treasure Data
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Treasure Data, einer geschäftskunden Data Platform (CDP) für Unternehmen, die es Ihnen erlaubt, Auftragsergebnisse direkt in Braze zu schreiben."
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# Treasure Data

> [Treasure Data](https://www.treasuredata.com/) ist eine geschäftskunden Data Platform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Standorte in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und Treasure Data erlaubt es Ihnen, Auftragsergebnisse aus Treasure Data direkt in Braze zu schreiben, wodurch Sie die Möglichkeit haben:
* **Externe IDs abbilden**: Ordnen Sie IDs dem Braze-Nutzerkonto von Ihrem CRM-System zu.
* **Opt-out verwalten**: Wenn Endnutzer:innen ihre Zustimmung aktualisieren und sich dafür entscheiden, nicht teilzunehmen.
* **Ihr Tracking von Events, Käufen oder angepassten Profilattributen hochladen**. Diese Informationen können Ihnen helfen, präzise Kundensegmente zu erstellen, die das Nutzererlebnis Ihrer Campaigns verbessern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Treasure Data-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Treasure Data-Konto](https://www.treasuredata.com/custom-demo/). |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track`, `users.delete`, `users.alias.new`, `users.identify`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Sie können Ihre konsolidierten Kundenprofile aus Treasure Data mit Braze synchronisieren, um Targeting-Segmente zu erstellen. Treasure Data unterstützt First-Party-Cookie-Daten, Mobile IDs, Drittanbieter-Systeme wie Ihr CRM und vieles mehr.

## Integration

### Schritt 1: Erstellen Sie eine neue Verbindung {#step-1-create-a-new-connection}

Navigieren Sie in Treasure Data zum **Catalog** unter dem **Integrations Hub**, suchen Sie nach **Braze** und wählen Sie es aus.

In der daraufhin angezeigten Eingabeaufforderung **New Authentication** geben Sie Ihrer Verbindung einen Namen und den Braze REST-API-Schlüssel sowie den REST-Endpunkt an. Wählen Sie **Done**, wenn Sie fertig sind.

![Treasure Data Braze-Authentifizierungsformular mit Feldern für REST-API-Schlüssel und Endpunkt.]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### Schritt 2: Definieren Sie Ihre Abfrage {#step-2-define-your-query}

Navigieren Sie in Treasure Data zu **Queries** unter Ihrer **Data Workbench** und wählen Sie eine Abfrage aus, für die Sie Daten exportieren möchten. Führen Sie diese Abfrage aus, um die Ergebnismenge zu überprüfen.

{% alert note %}
Für Nutzer:innen, die HIVE zum Erstellen von Abfragen verwenden, verlangt HIVE, dass alle Spalten oder Tabellen, die mit einem Unterstrich beginnen, in Backticks gesetzt werden. Zum Beispiel: `_merge_objects`.
{% endalert %}

Als Nächstes wählen Sie **Export Results** und wählen eine vorhandene Integrations-Authentifizierung aus.

![Treasure Data Abfrageergebnisseite mit ausgewähltem „Export Results“ und Braze-Integration.]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

Definieren Sie zusätzliche Parameter für die Exportergebnisse, wie im folgenden [Abschnitt über die Anpassung](#customization) beschrieben. Überprüfen Sie die Integrationsparameter in den Inhalten Ihrer Export-Integration.

![Die Seite „Export Results“. Auf dieser Seite befinden sich Felder für „mode“, „track record type“ und „pre-formatted fields“. In diesem Beispiel sind „User-Track“ und „Custom Events“ auf diese Felder eingestellt.]({% image_buster /assets/img/treasure_data/braze_export_configuration.png %}){: style="max-width:80%;"}

Wählen Sie schließlich **Done**, führen Sie Ihre Abfrage aus und überprüfen Sie, ob Ihre Daten nach Braze verschoben wurden.

### Anpassung {#customization}

Die Parameter der Exportergebnisse sind in der folgenden Tabelle aufgeführt:

| Parameter                 | Werte | Beschreibung |
|---------------------------|---|---|
| `mode`                    | User - New Alias<br>User - Identifying<br>User - Track<br>User - Delete | Konnektor-Modus |
| `pre_formatted_fields`    | String | Verwenden Sie diese Option für Array- oder JSON-Spalten, um das Format beizubehalten. |
| `track_record_type`       | Custom Events<br>Purchases<br>User Profile Attributes | Datensatztyp für den Modus **User - Track** |
| `skip_on_invalid_records` | Boolescher Wert | Falls aktiviert, fahren Sie fort und ignorieren alle ungültigen Datensätze für die JSON-Spalte. <br> Andernfalls wird der Auftrag abgebrochen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Anpassung" }

{% alert note %}
Besuchen Sie [Treasure Data](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration) für weitere Informationen über vorformatierte Felder, Beispielabfragen, Parameterdetails und die Zeitplanung von Abfrageexportaufträgen.
{% endalert %}

## Webhooks

Nutzer:innen von Treasure Data können Daten über die öffentliche REST API aufnehmen. Sie können Treasure Data verwenden, um angepasste Webhooks für Ihre Daten zu erstellen. Um mehr zu erfahren, besuchen Sie [Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API).