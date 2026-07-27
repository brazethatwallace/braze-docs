---
nav_title: Octolis
article_title: Octolis
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Octolis, einer Datenaktivierungsplattform, die es Ihnen ermöglicht, Ihre Daten in Braze zu integrieren."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com) ist eine leistungsstarke Plattform zur Aktivierung von Daten (oder headless CDP). Octolis basiert auf einer Datenbank, die Sie besitzen, und ist eine einfache Möglichkeit, Daten in Ihren Geschäftsanwendungen zu vereinheitlichen, aufzubereiten, zu bewerten und zu synchronisieren.

_Diese Integration wird von Octolis gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Octolis fungiert als Middleware zwischen Ihren Rohdatenquellen und Braze und ermöglicht es Ihnen, Daten aus verschiedenen Quellen, online und offline, abzurufen und zu vereinheitlichen:
1. Vereinheitlichen und kombinieren Sie Daten aus Quellen wie Eshop, CRM, POS-System usw.
2. Normalisieren und bewerten
3. Realtime-Synchronisation von berechneten Feldern und Ereignissen mit Braze

![Architekturdiagramm, das die Datenquellen, die Verarbeitung und den Synchronisationsfluss von Octolis nach Braze zeigt.]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Octolis-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Octolis-Konto. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track)-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze-App-Schlüssel | Ihr Bezeichner für die App. Diesen finden Sie im **Braze-Dashboard > Einstellungen verwalten > API-Schlüssel**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Bevor Sie mit der Integration beginnen, lesen Sie die folgenden Abschnitte über Verbindungen, Quellen, Zielgruppen und Synchronisationen.

Weitere Informationen finden Sie im Abschnitt [Erste Schritte](https://help.octolis.com/) von Octolis.

### Schritt 1: Octolis mit Ihren Datenquellen verbinden {#step-1-connect-octolis-to-your-data-sources}

Um Daten an Braze zu senden, müssen Sie sicherstellen, dass Sie mindestens eine [Zielgruppe](https://help.octolis.com/audiences/create-a-no-code-audience) erstellt haben. Eine Zielgruppe kombiniert mehrere Datenquellen, wendet sie auf Vorbereitungsschritte an und fügt berechnete Felder hinzu.

Diese Zielgruppen müssen auf der Grundlage mehrerer Datenquellen erstellt werden. Eine Quelle kann einer der folgenden Punkte sein:
- Ein Salesforce-Objekt (Kontakte, Konten usw.)
- Ein Zendesk-Objekt (Tickets)
- Eine Datei innerhalb eines SFTP (CSV-Datei mit einigen Kontakten, JSON-Datei mit Ereignissen …)
- Eine Tabelle/Ansicht in einer Datenbank.
- Eines Ihrer Systeme sendet uns Datensätze über Webhooks oder API-Aufrufe.

### Schritt 2: Braze als Ziel hinzufügen {#step-2-add-braze-as-a-destination}

Um Braze als neues Ziel festzulegen, wählen Sie im Hauptbildschirm oben auf Ihrem aktuellen Ziel **+ Add more** und wählen Sie **Braze** aus den verfügbaren Business-Tools aus.

![Octolis-Zielauswahl mit Braze als Option aus den verfügbaren Business-Tools.]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

Sobald Sie die Auswahl getroffen haben, geben Sie Folgendes an:

- Ihren Braze-API-Schlüssel: Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.
- Zeitfenster: Octolis wendet das Rate-Limiting für den angegebenen Zeitraum an.
- Anfragevolumen: Anzahl der Anfragen, die Sie innerhalb dieses Zeitrahmens stellen können.
- Angepasste Attribute: Geben Sie hier die neuen Felder an, die Sie an Braze senden möchten, ihr Format (String, Ganzzahl, Gleitkommazahl), und markieren Sie **Required for syncs**, wenn Sie möchten, dass eines der Felder für eine Synchronisation ein Pflichtfeld ist.

![Octolis-Konfigurationsfelder für das Braze-Ziel mit API-Schlüssel, Rate-Limits und angepassten Attributen.]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

Nach der Konfiguration erscheint Braze als neues Ziel auf dem Startbildschirm.

### Schritt 3: Eine neue Synchronisierung erstellen {#step-3-create-a-new-sync}

Klicken Sie im Menü auf **Syncs** und wählen Sie in der Aktionsleiste **Add sync**. Wählen Sie die gewünschte Zielgruppe aus den zuvor erstellten Zielgruppen aus.
Wählen Sie anschließend **Braze** als Ziel und die Entität aus, an die Sie die Daten senden möchten.

![Octolis-Bildschirm zur Erstellung einer Synchronisierung mit Auswahl von Zielgruppe und Braze als Ziel.]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### Schritt 4: Ausgabeeinstellungen festlegen {#step-4-set-output-settings}

Standardmäßig erstellt Braze alle Attribute, die Sie senden würden, aber Sie müssen die Liste der zu synchronisierenden Felder dokumentieren.

![Octolis-Bildschirm für Ausgabeeinstellungen mit Feldzuordnung und Synchronisierungsplanung für Braze.]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

Hier finden Sie eine spezifische Definition der Einstellungsfelder.

| Feld | Beschreibung |
| --- | --- |
| Wohin möchten Sie die Zielgruppe synchronisieren? | Die Braze-Entität, in der Sie Datensätze erstellen oder aktualisieren werden. |
| Welches Feld wird zur Identifizierung eines Datensatzes verwendet? | Das Feld, das Octolis verwendet, um einen Datensatz zu identifizieren, wenn er bereits in Braze existiert. |
| Wie oft möchten Sie jeden Datensatz senden? | Standardmäßig erfolgt die Synchronisierung für alle Integrationen (API, Datenbank, FTP) inkrementell. Das bedeutet, dass nur neue Werte seit dem letzten Update aktualisiert werden. Bei Bedarf können Sie auch ganze Tabellen in regelmäßigen Abständen versenden. Bei der Initiierung sendet Octolis die vollständige Tabelle. |
| Welche Felder sollen synchronisiert werden? | Abbildung von Octolis- auf Braze-Felder. Die Liste aller verfügbaren Felder wird im Dropdown-Menü angezeigt. Um ein berechnetes Feld an Braze zu senden, müssen Sie zunächst sicherstellen, dass Sie die entsprechende Spalte in Ihrer Braze-Entität erstellt haben. |
| Wann möchten Sie die Zielgruppe synchronisieren? | Wie die Daten an Braze gesendet werden sollen: manuell, in Realtime oder programmiert. |
| Synchronisieren, wenn der Datensatz … | Erstellen: Für Opt-ins ist es wichtig, dass die Braze-Tabelle Master bleibt. Sie möchten nicht, dass Octolis eine Synchronisierung triggert, wenn das Feld aktualisiert wird.<br><br>Update: Andererseits möchten Sie z. B. bei einem Feld für den Vornamen in der Lage sein, das Feld in Ihrer Braze-Tabelle jedes Mal zu aktualisieren, wenn eine Kund:in Ihnen einen neuen Eintrag gibt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 4: Ausgabeeinstellungen festlegen" }

## Deduplizierung mit mehreren Schlüsseln {#multi-keys-deduplication}

Die Deduplizierung ist eine große Herausforderung beim Abgleich von Daten aus verschiedenen Quellen, insbesondere online und offline. Durch das fortschrittliche No-Code-Modul von Octolis können Sie mehrere Schlüssel für die [Deduplizierung](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work) verwenden. Dieses Modul ist für jede Stammtabelle verfügbar, d. h. Sie können die Logik an jede Entität anpassen.