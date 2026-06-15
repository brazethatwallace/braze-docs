---
nav_title: actionable.me
article_title: actionable.me
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und actionable.me, einer proprietären Software mit zugehörigen Prozessen, die es Ihnen ermöglicht, sofort das Beste aus Ihrer Braze-Investition herauszuholen."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), entwickelt vom Team bei Massive Rocket, einer Daten- und CRM-Agentur, ist ein standardisierter und automatisierter Ansatz für die Durchführung von CRM-Programmen, der Tools und Prozesse bereitstellt, die Braze-Kund:innen schnell, konsistent und vorhersehbar zu einem Mehrwert verhelfen sollen.

_Diese Integration wird von actionable.me gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und actionable.me erlaubt es Ihnen, einen Dienst einzurichten, um Ihre Fortschritte bei der Nutzung von Braze zu überwachen. Durch eine Kombination von Tools und Prozessen werden sie Ihre CRM-Performance schnell bewerten, neue Möglichkeiten identifizieren und Empfehlungen für eine bessere Performance geben.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| actionable.me-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein actionable.me-Konto. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den im nächsten Abschnitt aufgeführten Berechtigungen.<br><br> Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Um Braze und actionable.me zu integrieren, muss die actionable.me-Plattform konfiguriert und ein Braze-API-Schlüssel in Braze erstellt und im actionable.me-Dashboard konfiguriert werden.

### 1. Schritt: Erstellen Sie Ihren Braze-API-Schlüssel {#step-1-create-your-braze-api-key}

Navigieren Sie in Braze zu **Settings** > **API Keys**. Wählen Sie **Create New API Key** aus und stellen Sie sicher, dass die folgenden Berechtigungen hinzugefügt werden:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### 2. Schritt: Stellen Sie dem actionable.me-Team die erforderlichen Informationen bereit {#step-2-provide-information-to-the-actionableme-team}

Um die Integration abzuschließen, müssen Sie Ihrem actionable.me-Operations-Team Ihren REST-API-Schlüssel und die [REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) mitteilen. actionable.me wird dann die Verbindung herstellen, sich nach Abschluss der Einrichtung mit Ihnen in Verbindung setzen und mit dem Austausch von Insights beginnen.

![Die actionable.me-Seite „Plattform hinzufügen“, die das actionable.me-Operations-Team konfigurieren wird.]({% image_buster /assets/img/actionableme/image2.png %})

## Fehlerbehebung {#troubleshooting}

Kontaktieren Sie das actionable.me- oder Massive-Rocket-Team für weitere Unterstützung: [info@massiverocket.com](mailto:info@massiverocket.com)