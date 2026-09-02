---
nav_title: Nexla
article_title: Nexla
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Nexla, einer einheitlichen Plattform für Datenoperationen, die es Nutzer:innen von Braze-Currents erlaubt, Data-Lake-Daten zu extrahieren, zu transformieren und in einem angepassten Format an andere Ziele zu laden."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) ist ein führendes Unternehmen im Bereich einheitlicher Datenoperationen und ein Gartner Cool Vendor 2021. Die Nexla-Plattform bietet Tools für die Erstellung skalierbarer Datenströme, die einen geregelten Datenbetrieb, Zusammenarbeit und Agilität für Geschäfts- und Datenteams ermöglichen. Teams, die mit Daten arbeiten, erhalten eine einheitliche No-/Low-Code-Erfahrung, um Daten für jeden Anwendungsfall zu integrieren, zu transformieren, bereitzustellen und zu überwachen.

Die Braze- und Nexla-Integration erlaubt es Kund:innen, die [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents) verwenden, Nexla zu nutzen, um Data-Lake-Daten zu extrahieren, zu transformieren und in einem angepassten Format an andere Ziele zu laden, sodass Daten in Ihrem gesamten Ökosystem leicht zugänglich sind.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Nexla-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Nexla-Konto](https://www.nexla.com/get-demo). |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Nexlas Daten-als-Produkt, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), ermöglicht die Arbeit mit Daten jeglichen Formats ohne Verwaltung von Metadaten. Wenn Sie mit Nexla Datenströme zu oder von Braze einrichten, sind No-Code-Tools innerhalb weniger Minuten verfügbar. Nachdem der Datenfluss auf ein Ziel eingestellt ist, überwacht Nexla den Fluss und skaliert auf jede Datenmenge.

## Integration

### Schritt 1: Erstellen Sie ein Nexla-Konto {#step-1-create-a-nexla-account}

Wenn Sie noch kein Nexla-Konto haben, gehen Sie auf die [Website](https://www.nexla.com) von Nexla, um eine kostenlose Demo und einen Test zu beantragen. Melden Sie sich anschließend bei [www.dataops.nexla.io](https://www.dataops.nexla.io) mit Ihren neuen Zugangsdaten an.

### Schritt 2: Fügen Sie Ihre Quelle hinzu {#step-2-add-your-source}

#### Wenn Braze Ihre Datenquelle ist {#if-braze-is-your-data-source}
1. Navigieren Sie in der Nexla-Plattform in der Navigationsleiste zu **Flows > Create a New Flow**.
2. Klicken Sie auf **Create New Source**, wählen Sie den Braze-Konnektor aus und klicken Sie auf **Next**.
3. Wählen Sie **Add a New Credential**, benennen Sie die Zugangsdaten, fügen Sie Ihren Braze-API-Schlüssel und den REST-Endpunkt hinzu und klicken Sie auf **Save**.
4. Wählen Sie abschließend Ihre Daten aus und klicken Sie auf **Save**.

Nexla durchsucht die Quelle nach verfügbaren Daten und generiert ein [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) zur Transformation oder zum Senden an ein Ziel.

#### Wenn Braze Ihr Ziel ist {#if-braze-is-your-destination}

Besuchen Sie die Dokumentation von Nexla zur [Anbindung von Quellen an Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Schritt 3: Transformieren (optional) {#step-3-transform-optional}

Wenn Sie angepasste [Transformationen](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) an Ihren Daten vornehmen oder die vorgefertigten Konnektoren von Nexla verwenden möchten, klicken Sie auf den Button **Transform** auf dem Datensatz, um den Transform Builder aufzurufen. Eine Anleitung zur Verwendung des Transform Builders finden Sie in der [Dokumentation von Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Schritt 4: An Ziel senden {#step-4-send-to-destination}

Um Daten an ein Ziel zu senden, klicken Sie auf den Pfeil **Send to Destination** im Datensatz und wählen Sie einen der Ziel-Konnektoren von Nexla oder Braze aus, wenn Sie eine andere Quelle verwendet haben. Geben Sie Ihre Zugangsdaten ein, konfigurieren Sie die Zieloptionen und klicken Sie auf **Save**. Die Daten werden sofort in dem von Ihnen angegebenen Format an das Ziel Ihrer Wahl übertragen.

## Verwendung dieser Integration {#using-this-integration}

Sobald der Fluss eingerichtet ist, ist nichts weiter erforderlich. Nexla verarbeitet alle Änderungen an den Quelldaten, skaliert auf neue Daten und benachrichtigt Sie bei Schemaänderungen oder Fehlern zur Triage. Wenn Sie Änderungen an den Transformationen, der Quelle oder dem Ziel vornehmen möchten, können Sie in diese Optionen klicken und die Änderung vornehmen. Nexla aktualisiert den Fluss dann sofort.