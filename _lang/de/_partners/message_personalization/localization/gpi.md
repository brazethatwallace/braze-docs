---
nav_title: GPI
article_title: Globalization Partners International
date_published: "2026-09-09"
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Globalization Partners International (GPI), einem Anbieter von Übersetzungsdienstleistungen. Der GPI Translation Services Connector extrahiert Braze-Inhalte zur Übersetzung und importiert fertige Übersetzungen über die Translation API von Braze zurück."
alias: /partners/gpi/
page_type: partner
search_tag: Partner
---

# Globalization Partners International

> [Globalization Partners International](https://www.globalizationpartners.com/) (GPI) stellt den GPI Translation Services Connector für Braze bereit. Der Konnektor extrahiert Inhalte aus Campaigns, Canvases, E-Mail-Templates und Content Blocks zur Übersetzung und importiert fertige Übersetzungen anschließend über die Translation API wieder in Braze. GPI unterstützt menschliche Übersetzung, KI-gestützte Übersetzung und KI-Übersetzung mit professionellem Post-Editing in mehr als 200 Sprachen.

_Diese Integration wird von Globalization Partners International gepflegt._

## Über die Integration {#about-the-integration}

Der GPI Translation Services Connector ist in das native Mehrsprachen-Modell und die Translation API von Braze integriert. Sie extrahieren übersetzbare Inhalte über das GPI Translation Portal, senden sie an GPI zur Übersetzung und importieren fertige Übersetzungen ohne manuelles Kopieren und Einfügen wieder in Braze. GPI bewahrt Liquid-Tags und Personalisierung während des gesamten Workflows.

## Anwendungsfälle {#use-cases}

### Globaler Campaign-Launch {#global-campaign-launch}

Wählen Sie Campaigns, Canvases oder E-Mail-Templates in Braze aus, legen Sie Quell- und Zielsprachen fest und übermitteln Sie die Inhalte an GPI für professionelle menschliche Übersetzung. GPI übernimmt Lokalisierung und Qualitätssicherung in Entwurfsvorschauen vor dem Launch.

### Zeitkritische oder umfangreiche Lokalisierung {#time-sensitive-or-high-volume-localization}

Leiten Sie Flash-Sales, dringende Lifecycle-Nachrichten oder große Mengen von Content Blocks über den Konnektor weiter und erhalten Sie automatisch in Braze importierte Übersetzungen. Die Bearbeitungszeit hängt vom gewählten Workflow ab und kann von Wochen bis Minuten reichen.

### Unterstützung bei der Internationalisierung {#internationalization-support}

GPI bietet Beratung zu Formatierung und Best Practices für die Braze-Lokalisierung, einschließlich Rechts-nach-links-Sprachen (RTL) wie Arabisch, Hebräisch und Persisch.

### Laufende Lokalisierung im großen Maßstab {#ongoing-localization-at-scale}

GPI nutzt Translation Memory, um frühere Übersetzungen für Terminologie- und Stilkonsistenz wiederzuverwenden und Kosten bei exakten, wiederholten und unscharfen Übereinstimmungen zu reduzieren. Aktualisieren Sie Campaigns in der Ausgangssprache in Braze und senden Sie die überarbeiteten Inhalte an GPI, um die entsprechenden Übersetzungen zu aktualisieren.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
| --- | --- |
| Ein Globalization Partners International-Konto | Für die Nutzung dieser Integration ist ein GPI-Konto erforderlich. |
| Ein Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den folgenden Berechtigungen:<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br>- `content_blocks.list`<br>- `content_blocks.info`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.list`<br>- `templates.email.info`<br>- `templates.email.translations.get`<br>- `templates.email.translations.update`<br><br>Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. Weitere Informationen finden Sie unter [REST-API-Schlüssel erstellen]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Ein Braze-REST-Endpunkt | [Die URL Ihres REST-Endpunkts]({{site.baseurl}}/api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. |
| Braze-Mehrsprachigkeitseinstellungen | Ziel-Locales müssen in Braze unter **Einstellungen** > **Lokalisierungseinstellungen** konfiguriert sein. Weitere Informationen finden Sie unter [Mehrsprachigkeitseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Braze-REST-API-Schlüssel erstellen {#step-1-create-a-braze-rest-api-key}

1. Gehen Sie in Braze zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Erstellen Sie einen REST-API-Schlüssel mit den unter [Voraussetzungen](#prerequisites) aufgeführten Berechtigungen.
3. Kopieren Sie den API-Schlüssel und notieren Sie sich den REST-Endpunkt Ihrer Instanz.

### Schritt 2: Einstellungen an GPI senden {#step-2-send-settings-to-gpi}

1. Senden Sie Ihren API-Schlüssel und REST-Endpunkt an Ihre:n GPI-Account-Manager:in.
2. Senden Sie die Liste der Nutzer:innen, die Zugang zum Konnektor benötigen, damit GPI ihn für sie aktivieren kann.
3. GPI konfiguriert den Konnektor mit Ihren Zugangsdaten und validiert die Verbindung.

### Schritt 3: Lokalisierungseinstellungen in Braze konfigurieren {#step-3-configure-localization-settings-in-braze}

1. Gehen Sie in Braze zu **Einstellungen** > **Lokalisierungseinstellungen** und bestätigen Sie, dass Ihre Ziel-Locales aktiviert sind.
2. Stellen Sie sicher, dass für die Inhalte, die Sie zur Übersetzung senden, die erforderlichen Locales aktiviert sind. Inhalte ohne aktivierte Locales können keine importierten Übersetzungen erhalten.
3. Fügen Sie [Übersetzungs-Liquid-Tags]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) um die Inhalte hinzu, die übersetzt werden müssen.
4. Fügen Sie für RTL-Sprachen Liquid-Tags hinzu, um die Inhaltsrichtung je nach Sprache zu unterstützen. Vermeiden Sie Ausrichtungs-Styling-Direktiven, es sei denn, Sie haben bestätigt, dass sie das RTL-Rendering nicht beeinträchtigen.

## GPI mit Braze verwenden {#use-gpi-with-braze}

Nur Inhalte im Entwurfs- oder Post-Launch-Entwurfsstatus können in Braze übersetzt werden.

### Schritt 1: Inhalte für die Übersetzung exportieren {#step-1-export-content-for-translation}

1. Öffnen Sie im [GPI Translation Portal](https://www.translationportal.com) den **Braze**-Konnektor und wählen Sie **New Request** aus.
2. Füllen Sie den Tab **Information** aus und öffnen Sie dann den Tab **Content**. Wählen Sie unter **Categories** die Option **Campaign**, **Canvas**, **Email Template** oder **Content Block** aus und wählen Sie dann die zu exportierenden Elemente aus.
3. Wählen Sie **Submit** aus, um eine Angebotsanfrage an GPI zu senden. Ihre:r GPI-Account-Manager:in kontaktiert Sie, wenn das Angebot zur Überprüfung und Genehmigung bereit ist.

### Schritt 2: Übersetzungen in Braze importieren {#step-2-import-translations-into-braze}

1. Suchen Sie im **Braze**-Konnektor das Projekt, das Sie importieren möchten.
2. Wählen Sie das **Import**-Symbol in der Spalte **Actions** aus.
3. Warten Sie auf die Importbestätigungsnachricht. Den Status des Importauftrags können Sie auf der Seite **Jobs** überprüfen.

### Schritt 3: Status der Übersetzungsanfrage prüfen {#step-3-check-translation-request-status}

1. Gehen Sie zum [GPI Translation Portal](https://www.translationportal.com).
2. Wählen Sie **Sign In** aus und geben Sie Ihre Zugangsdaten ein.
3. Wählen Sie in der Navigation des GPI Translation Portal **Braze** aus, um das Konnektor-Dashboard zu öffnen. Überprüfen Sie die Tabellen **Quotes** und **Projects** für den Anfrage- und Projektstatus.

### Schritt 4: Übersetzungen in Braze in der Vorschau ansehen {#step-4-preview-translations-in-braze}

Nachdem Sie Übersetzungen importiert haben, sehen Sie sich diese in Braze in der Vorschau an:

1. Öffnen Sie den Bildschirm **Bearbeiten** für die Campaign oder Nachricht, die Sie übersetzt haben.
2. Gehen Sie im **Nachrichten-Editor** zum Tab **Vorschau und Test** oder **Test**.
3. Wählen Sie unter **Nachricht als Nutzer:in in Vorschau anzeigen** die Option **Mehrsprachige:r Nutzer:in** aus und wählen Sie dann das Locale aus, das Sie ansehen möchten.
4. Bestätigen Sie die Vorschau in der Zielsprache. Um sie mit externen Prüfer:innen zu teilen, generieren Sie einen Vorschau-Link.

## Hinweise {#considerations}

- Der GPI Translation Services Connector für Braze wird kostenlos bereitgestellt.

## Fehlerbehebung {#troubleshooting}

Für Unterstützung mit dem GPI Translation Services Connector für Braze oder einem beliebigen GPI-Übersetzungsprojekt wenden Sie sich an Ihre:n GPI-Projektmanager:in, rufen Sie +1-866-272-5874 an oder schreiben Sie eine E-Mail an [support@globalizationpartners.com](mailto:support@globalizationpartners.com).