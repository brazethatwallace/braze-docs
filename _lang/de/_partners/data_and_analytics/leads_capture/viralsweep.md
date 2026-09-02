---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und ViralSweep, einem Software-Dienst, der es Marken erlaubt, digitale Marketingaktionen wie Gewinnspiele, Wettbewerbe, Sofortgewinne, Wartelisten, Empfehlungsaktionen und mehr zu erstellen, durchzuführen und zu verwalten."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) ist ein Software-Dienst, der es Marken erlaubt, digitale Marketingaktionen wie Gewinnspiele, Wettbewerbe, Sofortgewinne, Wartelisten, Empfehlungsaktionen und mehr zu erstellen, durchzuführen und zu verwalten.

_Diese Integration wird von ViralSweep gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und ViralSweep ermöglicht es Ihnen, Gewinnspiele und Wettbewerbe auf der ViralSweep-Plattform zu veranstalten (und so Ihre E-Mail- und Kurzmitteilungsdienst or SMS-Listen zu erweitern) und dann die Teilnahmeinformationen aus Gewinnspielen oder Wettbewerben an Braze zu senden, um sie in Campaigns oder Canvase zu verwenden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| ViralSweep-Konto | Um diese Partnerschaft zu nutzen, ist ein ViralSweep-Konto mit dem Unternehmensplan erforderlich. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit allen Nutzerdaten- und E-Mail-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | Ihre Representational State Transfer-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Verbindung mit Braze in ViralSweep herstellen {#step-1-connect-to-braze-within-viralsweep}

Navigieren Sie in ViralSweep zu **Integrations > Email & Kurzmitteilungsdienst or SMS > Add Service** und wählen Sie **Braze** aus.

![ViralSweep-Integrationsseite mit Braze als ausgewähltem Dienst unter E-Mail- und SMS-Diensten.]({% image_buster /assets/img/viralsweep/connect.gif %})

### 2. Schritt: Braze-Zugangsdaten hinzufügen {#step-2-add-braze-credentials}

Geben Sie im Konfigurationsfenster für die Integration Ihren Braze-Representational State Transfer-API-Schlüssel und den Representational State Transfer-Endpunkt an. Stellen Sie sicher, dass der von Ihnen angegebene Endpunkt nicht `https://` enthält, zum Beispiel `dashboard-03.braze.com`.

![ViralSweep-Seite zur Dienstintegration, die Nutzer:innen zur Eingabe des Braze-API-Schlüssels und der Braze-Dashboard-URL auffordert.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Klicken Sie auf **Connect**.

### 3. Schritt: Verbindung bestätigen {#step-3-add-braze-credentials}
Sie sind verbunden! Die Aktion ist jetzt mit Braze verbunden, und alle von ViralSweep gesammelten Einträge werden automatisch an Braze gesendet.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Welche Felder übergibt ViralSweep an Braze? {#what-fields-does-viralsweep-pass-to-braze}
- Vorname
- Nachname
- E-Mail-Adresse
- Adresse
- Adresse 2
- Ort
- Bundesland
- Postleitzahl
- Land
- Geburtsdatum
- Telefon
- Aktions-ID
- Empfehlungslink
- Name der Tracking-Kampagne

### Aktualisiert ViralSweep Abonnent:innen? {#does-viralsweep-update-subscribers}
Ja. Wenn Sie eine Aktion durchführen und ViralSweep jemanden an Braze übergibt und Sie in Zukunft eine weitere Aktion durchführen, an der dieselbe Person teilnimmt, werden die Informationen dieser Person automatisch in Braze aktualisiert (sofern neue Informationen bereitgestellt werden). Hauptsächlich wird die Empfehlungs-URL mit der neuesten URL für jede Aktion aktualisiert, an der die Person teilnimmt, und das Aktions-ID-Feld enthält die IDs aller Aktionen, an denen sie teilgenommen hat.

## Fehlerbehebung {#troubleshooting}

Wenn Sie eine Verbindung zu Braze hergestellt haben und Ihrem Konto keine Daten hinzugefügt werden, kann das folgende Ursachen haben:

- **E-Mail existiert bereits in Braze**<br>
Die für die Aktion eingegebene E-Mail-Adresse befindet sich möglicherweise bereits in Ihrem Braze-Konto und wird daher nicht erneut hinzugefügt. Sie wird nur aktualisiert, wenn neue Informationen für diesen Kontakt bereitgestellt werden.<br><br>
- **E-Mail bereits in ViralSweep eingegeben**<br>
Die für die Aktion eingegebene E-Mail-Adresse wurde bereits zuvor eingegeben und wird daher nicht erneut an Braze übermittelt. Dies kann passieren, wenn Sie Ihre Braze-Integration einrichten, nachdem Sie die Aktion bereits gestartet haben.