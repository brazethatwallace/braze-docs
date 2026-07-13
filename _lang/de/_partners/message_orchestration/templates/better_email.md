---
nav_title: Better Email
article_title: Better Email
alias: /partners/better_email/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Better Email, einer kollaborativen E-Mail-Erstellungsplattform, die auf einem E-Mail-Design-System basiert und es ermöglicht, produktionsfertige Templates nach Braze zu exportieren."
page_type: partner
search_tag: Partner
---

# Better Email

> [Better Email](https://better.email) ist eine kollaborative E-Mail-Erstellungsplattform, die auf einem E-Mail-Design-System basiert. Teams können produktionsfertige E-Mails aus einem gemeinsamen System von Blöcken und Stilen entwerfen, verwalten und exportieren – und so Markenkonsistenz im großen Maßstab sicherstellen, ohne auf Entwickler:innen oder Agenturen angewiesen zu sein.

_Diese Integration wird von Better Email gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Better Email ermöglicht es Ihnen, E-Mail-Templates im kollaborativen Editor von Better Email zu erstellen und zu verwalten und sie direkt als einsatzbereite E-Mail-Templates nach Braze zu exportieren.

Beim erneuten Export wird das bestehende Braze-Template aktualisiert, anstatt ein Duplikat zu erstellen, sodass Ihre Template-Bibliothek übersichtlich bleibt.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Better-Email-Konto | Ein Better-Email-Konto mit Administratorzugriff zum Erstellen von Integrationen |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit vollständigen **Templates**-Berechtigungen.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Verwenden Sie den REST-Host, nicht die Dashboard-URL – zum Beispiel `rest.fra-01.braze.eu`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Better Email ist für Marketing-Teams konzipiert, die E-Mails über ein Design-System verwalten und ohne manuelle HTML-Arbeit nach Braze exportieren möchten. Es eignet sich besonders für Teams, die:

- Eine große Bibliothek von E-Mail-Templates pflegen und Konsistenz über alle Templates hinweg sicherstellen müssen
- Markenrichtlinien über ein gemeinsames E-Mail-Design-System durchsetzen möchten
- Teamübergreifend zusammenarbeiten – Designer:innen, Marketer und Entwickler:innen – bei der E-Mail-Produktion
- Braze für die Kampagnenausführung nutzen und den Übergabe-Engpass zwischen Design und Deployment beseitigen möchten

## Better Email mit Braze integrieren {#integrate-better-email-with-braze}

### 1. Schritt: Ihre Braze-Werte ermitteln {#step-1-find-your-braze-values}

Sammeln Sie in Ihrem Braze-Dashboard die folgenden Informationen:

- **Instanz-URL** – Verwenden Sie den REST-Host, nicht die Dashboard-URL (zum Beispiel `rest.fra-01.braze.eu`).
- **API-Schlüssel** – Ein REST-API-Schlüssel mit vollständigen **Templates**-Berechtigungen, erstellt unter **Einstellungen** > **API-Schlüssel**.

### 2. Schritt: Die Integration in Better Email einrichten {#step-2-set-up-the-integration-in-better-email}

1. Gehen Sie zu **Integrations**.
2. Erstellen Sie eine neue Integration.
3. Geben Sie einen Namen für die Integration ein (zum Beispiel `Braze`).
4. Wählen Sie **Braze** als Typ aus.
5. Optional können Sie die Integration unter **Access** auf bestimmte Nutzer:innen oder Gruppen beschränken.
6. Wählen Sie **Save** aus.
7. Geben Sie die **Instance URL** und den **API Key** ein.
8. Aktivieren Sie die Integration.
9. Wählen Sie erneut **Save** aus.

### 3. Schritt: Nach Braze exportieren {#step-3-export-to-braze}

Wenn die Integration aktiv ist, öffnen Sie eine beliebige E-Mail in Better Email und wählen Sie **Export** > **Braze** aus.

Better Email erstellt oder aktualisiert das entsprechende Braze-E-Mail-Template. Nach dem ersten Export speichert Better Email die Braze-Template-ID – ein erneuter Export derselben E-Mail aktualisiert dieses Template, anstatt ein Duplikat zu erstellen.

### Empfängerfelder aus Braze synchronisieren (optional) {#sync-recipient-fields-from-braze-optional}

Better Email kann angepasste Braze-Attribute synchronisieren, um sie als Merge-Tags und Segmentierungsfelder zu verwenden.

1. Öffnen Sie die Braze-Integration in Better Email.
2. Aktivieren Sie **Sync recipient fields**.
3. Wählen Sie **Save** aus.
4. Gehen Sie zu **Recipient Fields**.
5. Wählen Sie **Sync from** neben Ihrer Integration aus.

Better Email liest die verfügbaren angepassten Braze-Attribute und ordnet sie den Empfängerfeldern zu.

## Fehlerbehebung {#troubleshooting}

Wenn ein Export oder eine Synchronisierung fehlschlägt, überprüfen Sie Folgendes:

- Die **Instanz-URL** ist die REST-URL, nicht die Dashboard-URL.
- Der API-Schlüssel ist noch aktiv und verfügt über die erforderlichen **Templates**-Berechtigungen.
- Die Integration ist in Better Email aktiviert.
- Nutzer:innen oder Gruppen, die die Integration benötigen, haben unter **Access** Zugriff.

Für weitere Hilfe [kontaktieren Sie den Better-Email-Support](mailto:support@better.email).

## Die Integration verwenden {#use-the-integration}

Sie finden Ihre exportierten Better-Email-Templates in Braze unter **Templates und Medien** > **E-Mail-Templates**. Verwenden Sie sie in jeder Braze-Kampagne oder jedem Canvas.