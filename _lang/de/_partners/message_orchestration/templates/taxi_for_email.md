---
nav_title: Taxi for Email for Email
article_title: Taxi for Email for Email
alias: /partners/taxi_for_email
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Taxi for Email for Email, einem Online-Tool für E-Mail-Marketing, das es Braze-Kund:innen erlaubt, intelligente E-Mail-Templates mit Hilfe der Drag-and-Drop-Schnittstelle und einer einfachen, aber leistungsstarken Syntax zu erstellen."
page_type: partner
search_tag: Partner

---

# Taxi for Email for Email

> [Taxi for Email for Email](http://taxiforemail.com/) ist ein Online-Tool für E-Mail-Marketing, das einen intuitiven visuellen Drag-and-Drop-Editor für E-Mails bietet. Taxi for Email ermöglicht Teams eine einfache Zusammenarbeit bei E-Mail-Campaigns und gibt Texter:innen und Redakteur:innen den Zugriff auf die Ressourcen, die sie für die Erstellung von E-Mails benötigen – ganz ohne Code.

_Diese Integration wird von Taxi for Email for Email gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Taxi for Email nutzt die einfache, aber leistungsstarke Syntax von Taxi for Email, um intelligente E-Mail-Templates zu erstellen und nach Braze zu exportieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ------------| ----------- |
| Taxi for Email for Email-Konto | Um diese Partnerschaft zu nutzen, ist ein Taxi for Email for Email-Konto erforderlich. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit vollständigen **Templates**-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Endpunkt | [Ihr Braze-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) entspricht der URL Ihres Braze-Dashboards.<br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Taxi for Email-E-Mail-Template erstellen {#step-1-create-a-taxi-email-template}

Erstellen Sie ein Taxi for Email-Template auf der Taxi for Email-Plattform. Nachdem das Template erstellt wurde, navigieren Sie zu Ihren **Organisationseinstellungen** und wählen Sie den Tab **E-Mail-Anbieter Connectors** aus.

### 2. Schritt: Braze-Konnektor erstellen {#step-2-create-braze-connector}

1. Wählen Sie in dem daraufhin angezeigten Dialog den Button **Add New** und dann **Braze** aus der Dropdown-Liste aus.
2. Wählen Sie **Braze**, um die Einstellungen für den Braze-Konnektor zu bearbeiten.
3. Geben Sie Ihren Braze-Endpunkt und Ihren Braze-API-Schlüssel ein.

Das Feld für Ihren Konnektor ändert seine Farbe, nachdem die Details mit den richtigen Berechtigungen angegeben wurden. Wenn sich dieses Feld nicht ändert, überprüfen Sie, ob Ihre Felder mit den aufgeführten Anforderungen übereinstimmen.

## Nutzung {#usage}

Ihr hochgeladenes Taxi for Email-Template finden Sie in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail-Templates**. Sie können dieses E-Mail-Template jetzt verwenden, um ansprechende E-Mail-Nachrichten an Ihre Kund:innen zu versenden!