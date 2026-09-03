---
nav_title: DataGrail
article_title: DataGrail
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und DataGrail, einer Plattform zur Verwaltung des Datenschutzes, die es Ihnen ermöglicht, in Braze erfasste und gespeicherte Verbraucher:innendaten zu erkennen, um DSRs schnell zu verarbeiten."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), eine Plattform zur Verwaltung des Datenschutzes, hilft dabei, das Vertrauen der Verbraucher:innen aufzubauen und riskante Geschäftspraktiken zu vermeiden. Mit kontinuierlicher Systemerkennung und automatisierter Erfüllung von Betroffenenanfragen (DSR) unterstützt DataGrail Datenschutzprogramme und fördert die Einhaltung sich weiterentwickelnder Datenschutzgesetze und -vorschriften wie DSGVO, CCPA und CPRA.

_Diese Integration wird von DataGrail gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und DataGrail ermöglicht es Ihnen, die in Braze erfassten und gespeicherten Verbraucher:innendaten zu erkennen, um DSRs (Zugriffs-, Lösch- und Nichtverkaufsanfragen) schnell zu verarbeiten. Braze wird mithilfe automatisierter Datenabbildung zu einer genauen Übersicht darüber hinzugefügt, wo sich Verbraucher:innendaten in Ihrem Unternehmen befinden – es sind keine Umfragen oder Tabellenkalkulationen mehr erforderlich, um einen Datenschutzrahmen aufrechtzuerhalten oder ein Verzeichnis der Verarbeitungstätigkeiten (RoPA) zu erstellen.

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
|---|---|
| DataGrail-Konto | Ein DataGrail-Konto ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen.<br>Wenden Sie sich bei Problemen oder Fragen zur Integration an Ihren Administrator oder senden Sie eine E-Mail an support@datagrail.io. |
| Braze-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den Berechtigungen `events.list`, `users.export.ids`, `users.delete` und `users.track`.<br><br>Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager:in oder auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Melden Sie sich beim DataGrail-Portal an und wählen Sie auf der Integrationsseite für Braze **Connect** aus. Geben Sie als Nächstes Ihre Instanz und den Braze-API-Schlüssel ein und wählen Sie **Connect Braze**.

Wenn weitere Braze-Konten integriert werden sollen:
1. Wählen Sie auf der Integrationsseite für Braze **Edit Connection** aus.
2. Wählen Sie aus dem Dropdown-Menü **+Add New Connection**.
3. Geben Sie unter **Connection Name** einen neuen Namen ein, um dieses separate Konto zu identifizieren (z. B. Braze Training Account).
4. Geben Sie eine separate Braze-Instanz und einen API-Schlüssel für dieses neue Konto ein.
5. Wählen Sie **Connect**.

Senden Sie bei Problemen oder Fragen zu Ihrer Integration eine E-Mail an DataGrail unter support@datagrail.io.