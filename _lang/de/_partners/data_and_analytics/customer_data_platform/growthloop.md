---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und GrowthLoop, einer Plattform, die es Ihnen ermöglicht, Kundendaten direkt aus Data Warehouses zu segmentieren und an Braze zu senden."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) unterstützt Marketing-Teams bei der Aktivierung von Kundendaten aus dem Cloud Data Warehouse für Braze und andere Kanäle. Automatisieren, skalieren und messen Sie Marketing-Programme aus Ihrem Cloud Data Warehouse und halten Sie die Daten an einem einzigen, zentralen Ort.

_Diese Integration wird von GrowthLoop gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und GrowthLoop ermöglicht es Ihnen, Kundendaten direkt aus dem Data Warehouse zu segmentieren und an Braze zu senden – so können Nutzer:innen den umfangreichen Funktionsumfang von Braze in Verbindung mit ihrer einzigen Wahrheitsquelle optimal nutzen. Optimieren Sie Ihre Marketing-Aktivitäten für die Segmentierung und Aktivierung von Kund:innen und verkürzen Sie die Zeit, die für die Segmentierung, den Start, das Testen und die Messung der Ergebnisse gezielter Campaigns an Braze benötigt wird.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| GrowthLoop-Wachstums- oder Unternehmenskonto | Ein GrowthLoop-Konto ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit allen Berechtigungen.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Senden Sie Kundenlisten aus Ihrem Data Warehouse an Braze, richten Sie E-Mail- und Push-Benachrichtigungs-Campaigns mit einem Klick ein und halten Sie sie stets synchron.

- E-Mails basierend auf Registrierungsaktivierung – senden Sie E-Mails, um Nutzer:innen zu unterstützen, die in Ihrem Registrierungsablauf abspringen, und wandeln Sie sie in aktive Nutzer:innen um.
- E-Mails basierend auf beliebigem Nutzer:innen-Verhalten – senden Sie E-Mails basierend auf dem Nutzer:innen-Verhalten, wie z. B. „In den Warenkorb“.
- E-Mails an abgewanderte Kund:innen – binden Sie abgewanderte Kund:innen per E-Mail mit einem Angebot wieder ein.

## Integration

### Braze-Verbindung in GrowthLoop konfigurieren {#configure-braze-connection-in-growthloop}

Wenn Sie sich bei der Segmentierungsplattform in GrowthLoop anmelden, navigieren Sie zum Tab **Destinations** in der linken Seitenleiste und klicken Sie oben rechts auf **New Destination**.

Scrollen Sie, bis Sie Braze finden, und klicken Sie auf **Add Braze**.

Es wird ein Popup-Fenster angezeigt, in dem Sie die Verbindung zum Ziel konfigurieren können.

- **Destination name**: So wird das Ziel in der App künftig benannt und referenziert
- **Sync frequency**: Wählen Sie „Daily“ oder „Hourly“ aus; dies steuert, wie oft GrowthLoop Zielgruppen nach Braze exportiert
- **API key**: API-Schlüssel, der in den Voraussetzungen erstellt wurde und über die erforderlichen Berechtigungen verfügt
- **API URL**: URL wie in den Voraussetzungen definiert

Klicken Sie auf **Create**, und Sie können Ihre erste Zielgruppe nach Braze exportieren! Um eine Zielgruppe in GrowthLoop zu erstellen, besuchen Sie [Zielgruppe erstellen](https://www.growthloop.com/help-center-articles/create-an-audience).

### Nach dem Export {#post-export}

Sobald Ihre Zielgruppe exportiert wurde, erstellt GrowthLoop alle 15 Minuten eine aktualisierte Version Ihrer Kundenlisten und sendet diese an Braze.

Gleichzeitig entfernt GrowthLoop Nutzer:innen aus Ihrer Zielgruppe, die nicht mehr qualifiziert sind, und fügt neu qualifizierte Nutzer:innen zu Ihrer Zielgruppe hinzu.

Braze gleicht Nutzer:innen ab und erstellt eine Markierung, die anzeigt, dass sie Teil einer GrowthLoop-Zielgruppe sind.

Wenn Sie eine Campaign in Braze erstellen, können Sie Kund:innen in dieser GrowthLoop-Zielgruppe auswählen.

## Fehlerbehebung {#troubleshooting}

Wenden Sie sich an das GrowthLoop-Team unter solutions@growthloop.com, wenn Sie weitere Informationen oder Unterstützung benötigen.