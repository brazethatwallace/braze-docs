---
nav_title: NiftyImages
article_title: NiftyImages
description: "Erfahren Sie, wie Sie NiftyImages mit Braze verbinden, um personalisierte dynamische Visuals zu erstellen, Kontakteigenschaften zu synchronisieren und Assets als wiederverwendbare Content Blocks zu veröffentlichen."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com) unterstützt Braze-Kund:innen bei der Erstellung personalisierter Realtime-Inhalte für E-Mail, Mobilgeräte und In-App-Messaging. Durch die Verknüpfung von Live-Kunden-, Produkt- und Geschäftsdaten mit dynamischen Bildern und Inhalten können Marken zeitnahe, relevante Erlebnisse wie Countdown-Timer, personalisierte Empfehlungen, lokalisierte Nachrichten, Bestandsaktualisierungen und Aktionsangebote bereitstellen, die Engagement und Conversions steigern.

_Diese Integration wird von NiftyImages gepflegt._

## Über die Integration {#about-the-integration}

Die NiftyImages-Integration für Braze hilft Ihnen, personalisierte, dynamische Visuals mithilfe von Braze-Kontaktdaten zu erstellen. Teams können Assets wie personalisierte Bilder, Countdown-Timer, Karten, Kalender, Loyalty-Visuals und mehr erstellen und sie anschließend als wiederverwendbare Braze [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) für den Einsatz in Kampagnen und Canvase veröffentlichen. Das spart Zeit, reduziert Fehler und vereinfacht die Verwaltung personalisierter Inhalte.

## Anwendungsfälle {#use-cases}

Sie können NiftyImages verwenden, um:

- **Bilder zu personalisieren:** Erstellen Sie Bilder, die den Namen, den Loyalty-Status, das Prämienguthaben, den Standort, die Produktpräferenz, die Mitgliedschaftsstufe, Kontodetails oder andere Braze-Kontakteigenschaften jeder Kund:in enthalten.
- **Countdown-Timer hinzuzufügen:** Fügen Sie Realtime-Countdown-Timer für Verkaufsaktionen, Produktlaunches, Events, zeitlich begrenzte Angebote, Termine, Onboarding-Fristen und personalisierte Ablaufdaten hinzu.
- **Dynamische Karten anzuzeigen:** Zeigen Sie den nächstgelegenen Shop, Veranstaltungsort, Servicebereich, Händler, Club, Branch oder Abholort basierend auf Kundenstandortdaten oder Braze-Kontakteigenschaften an.
- **Kalender anzuzeigen:** Zeigen Sie personalisierte Termine, Events, Buchungen, Verlängerungszeiträume, Campaign-Momente oder Kunden-Meilensteine direkt in Campaign-Visuals an.
- **Live-Umfragen durchzuführen:** Fügen Sie interaktive Umfragen zu Kampagnen hinzu und zeigen Sie live aktualisierte Ergebnisse an, nachdem Kund:innen abgestimmt haben.
- **Rubbellose zu erstellen:** Erstellen Sie gamifizierte Rubbellos-Erlebnisse, die eine personalisierte Belohnung, einen Rabatt, ein Angebot, ein Bild oder eine Nachricht enthüllen.
- **Loyalty-Daten zu visualisieren:** Verwandeln Sie Kundendaten in Fortschrittsbalken, Kontozusammenfassungen, Loyalty-Visuals, Charts und Diagramme, die für jede Empfänger:in personalisiert sind.
- **Regelbasierten Content anzuwenden:** Zeigen Sie verschiedene Visuals basierend auf Zeit, Standort, Gerät, Kundendaten, Zielgruppen-Segment oder Campaign-Logik an.
- **Dynamischen Content wiederzuverwenden:** Veröffentlichen Sie fertige NiftyImages-Assets in Braze Content Blocks, damit Teams sie in Marketing-E-Mails, Templates, Kampagnen und gemeinsamen Marken-Assets wiederverwenden können.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Anforderung | Beschreibung |
| ------------ | ----------- |
| NiftyImages-Konto | Ein [NiftyImages-Konto](https://niftyimages.com/Signup) ist erforderlich, um personalisierte Bilder, Timer, Karten, Kalender, Rubbellose, Charts und andere dynamische Visuals zu erstellen und zu verwalten. |
| Braze-Konto | Ein Braze-Konto ist erforderlich, um NiftyImages in Braze Campaigns, Canvase, E-Mail-Templates und Messaging-Kanälen zu verwenden. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit den Berechtigungen `custom_attributes.get` und `content_blocks.create`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** erstellt werden. |
| Braze Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Verbinden Sie Ihr Braze-Konto in NiftyImages, um Kontakteigenschaften zu synchronisieren und Assets in Braze Content Blocks zu veröffentlichen.

### 1. Schritt: Integrationen in NiftyImages öffnen {#step-1-open-integrations-in-niftyimages}

1. Gehen Sie in NiftyImages zu **Settings** > **Integrations**.
2. Wählen Sie **Braze** aus.
3. Wählen Sie **Connect Braze** aus.

### 2. Schritt: Ihren Braze Representational State Transfer-API-Schlüssel erstellen {#step-2-create-your-braze-rest-api-key}

1. Gehen Sie in Braze zu **Einstellungen** > **APIs und Bezeichner**.
2. Erstellen oder wählen Sie einen Representational State Transfer-API-Schlüssel für die NiftyImages-Integration aus.
3. Wählen Sie unter **angepasste Attribute** die Option `custom_attributes.get` aus.
4. Wählen Sie unter **Content Blocks** die Option `content_blocks.create` aus.
5. Speichern Sie den API-Schlüssel und kopieren Sie dann den Representational State Transfer-API-Schlüssel und Ihren [Representational State Transfer-Endpunkt]({{site.baseurl}}/api/basics#endpoints).

### 3. Schritt: Ihr Braze-Konto in NiftyImages verbinden {#step-3-connect-your-braze-account-in-niftyimages}

1. Kehren Sie zum Braze-Integrationsbildschirm in NiftyImages zurück.
2. Fügen Sie den Braze Representational State Transfer-API-Schlüssel ein.
3. Geben Sie Ihren Braze Representational State Transfer-Endpunkt ein.
4. Bestätigen Sie die Verbindung.
5. Überprüfen Sie, ob Ihr Braze-Konto unter **Connected Braze accounts** mit dem Status **Active** oder **Connected** angezeigt wird.

Sie können bei Bedarf mehrere Braze-Konten verbinden, was für Agenturen, Multi-Marken-Teams oder Organisationen nützlich ist, die mehrere Braze-Instanzen verwalten.

## Assets in NiftyImages anpassen {#customize-assets-in-niftyimages}

Nachdem Sie Braze verbunden haben, verwenden Sie Contact Variable Sync und die Content-Block-Veröffentlichung, um personalisierte Visuals zu verwalten.

### Contact Variable Sync verwenden {#use-contact-variable-sync}

Contact Variable Sync ermöglicht es Ihnen, vorhandene Braze-Kontakteigenschaften direkt in NiftyImages zu verwenden, ohne Merge-Tags manuell einzugeben oder neu zu erstellen.

1. Erstellen oder bearbeiten Sie ein personalisiertes Bild oder ein anderes NiftyImages-Asset.
2. Öffnen Sie den Merge-Tag- oder Personalisierungs-Picker.
3. Wählen Sie **Pick from connected integrations** und dann die Braze-Eigenschaften aus, die Sie verwenden möchten.
4. Fügen Sie diese Werte zu Text-, Bild-, Timer-, Karten-, Chart-, Kalender- oder dynamischen Content-Ebenen hinzu.
5. Speichern Sie das Bild.

Gespeicherte Bilder, die Braze-Variablen verwenden, enthalten diese Personalisierungswerte automatisch in der NiftyImages-Bild-URL.

### In Braze Content Blocks veröffentlichen {#publish-to-braze-content-blocks}

1. Stellen Sie Ihr NiftyImages-Asset fertig.
2. Wählen Sie **Send to Braze** aus.

## NiftyImages in Braze verwenden {#use-niftyimages-in-braze}

Verwenden Sie veröffentlichte Content Blocks in Braze E-Mail-Templates, Kampagnen und Canvase.

### Ein NiftyImages-Asset zu einer Braze-E-Mail hinzufügen {#add-a-niftyimages-asset-to-a-braze-email}

1. Öffnen Sie ein E-Mail-Template, eine Kampagne oder eine Canvas-E-Mail-Nachricht in Braze.
2. Öffnen Sie im Nachrichteneditor das Personalisierungsmenü und wählen Sie **Content Blocks** als Personalisierungstyp aus.
3. Wählen Sie den NiftyImages Content Block aus, den Sie aus NiftyImages veröffentlicht haben.

### NiftyImages-Assets in Braze wiederverwenden {#reuse-niftyimages-assets-across-braze}

1. Verwenden Sie den veröffentlichten Content Block in Marketing-E-Mails, E-Mail-Templates, Kampagnen, gemeinsamen Marken-Assets und automatisierten Flows.
2. Wenn ein NiftyImages-Asset dynamische Variablen verwendet, übergibt Braze die Kontaktwerte basierend auf der Nachricht und dem Kanal.
3. Update or aktualisieren or aktualisieren Sie das Quell-Asset in NiftyImages, wenn Sie kreative Änderungen benötigen.

### Ein Braze-Konto trennen {#disconnect-a-braze-account}

1. Kehren Sie in NiftyImages zu **Settings** > **Integrations** zurück.
2. Öffnen Sie die Braze-Verbindungsseite.
3. Wählen Sie das Symbol zum Entfernen oder Trennen für das Konto aus, das Sie entfernen möchten.
4. Bestätigen Sie die Trennung.

## Hinweise {#considerations}

- **Representational State Transfer-API-Berechtigungen:** Der Braze Representational State Transfer-API-Schlüssel muss `custom_attributes.get` für die Synchronisierung von Kontakteigenschaften und `content_blocks.create` für die Veröffentlichung von Assets in Braze Content Blocks enthalten.
- **Verfügbarkeit von Kontakteigenschaften:** Nur Kontakteigenschaften, die dem verbundenen Braze-Konto zur Verfügung stehen, können in NiftyImages synchronisiert werden.
- **Fallback-Werte:** Verwenden Sie Fallback-Werte beim Erstellen personalisierter Visuals, damit jede Kund:in ein ansprechendes Bild sieht, auch wenn eine Kontakteigenschaft fehlt.
- **Wiederverwendbare Content Blocks:** Die Veröffentlichung in Braze Content Blocks hilft Teams, manuelles Kopieren und Einfügen von HTML zu vermeiden, Merge-Tag-Fehler zu reduzieren und Assets in Kampagnen und Templates wiederzuverwenden.
- **Mehrere Braze-Konten:** NiftyImages unterstützt mehrere verbundene Braze-Konten, was für Agenturen, Multi-Marken-Teams und Teams hilfreich ist, die mehrere Braze-Instanzen verwalten.
- **Testen:** Testen Sie die endgültige Braze-Nachricht mit Beispiel-Kundenprofilen, bevor Sie eine Kampagne oder ein Canvas starten.

## Fehlerbehebung {#troubleshooting}

Sehen Sie sich die folgende Tabelle an, wenn bei der NiftyImages-Integration Probleme auftreten.

| Problem | Lösung |
| ----- | ---------- |
| Braze-Konto lässt sich nicht verbinden | Stellen Sie sicher, dass der Representational State Transfer-API-Schlüssel gültig ist, der Representational State Transfer-Endpunkt korrekt ist und der Schlüssel die erforderlichen Berechtigungen enthält. |
| Braze-Kontakteigenschaften werden in NiftyImages nicht angezeigt | Stellen Sie sicher, dass der API-Schlüssel `custom_attributes.get` enthält. Update or aktualisieren or aktualisieren Sie dann die Braze-Verbindung in NiftyImages. |
| Das Asset wird nicht in Braze Content Blocks veröffentlicht | Stellen Sie sicher, dass der API-Schlüssel `content_blocks.create` enthält und dass das verbundene Braze-Konto die Erstellung von Content Blocks erlaubt. |
| Personalisierung wird nicht korrekt angezeigt | Überprüfen Sie, ob die ausgewählte Braze-Kontakteigenschaft einen Wert für die Testnutzer:in enthält. Fügen Sie bei Bedarf Fallback-Werte in NiftyImages hinzu. |
| Das Bild wird in Braze nicht gerendert | Stellen Sie sicher, dass das NiftyImages-Asset gespeichert, aktiv und korrekt veröffentlicht ist. Senden Sie eine Braze-Testnachricht, um das Bild im vorgesehenen Kanal zu überprüfen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }