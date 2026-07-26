---
nav_title: Refiner
article_title: Refiner
alias: /partners/refiner/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Refiner, mit der Sie Umfrageereignisse und Antwortdaten an Braze senden können, um Campaigns zu triggern, Nutzer:innen zu segmentieren und Nutzerprofile zu aktualisieren."
page_type: partner
search_tag: Partner

---

# Refiner

> [Refiner](https://refiner.io) ist eine In-App-Umfrageplattform für SaaS- und mobile Apps. Sie ermöglicht es Produkt- und Voice-of-geschäftskunden-Teams, gezielte In-App-Umfragen zu starten und kontinuierlich NPS-, CSAT-, CES-, Produktfeedback- und Zero-Party-Nutzerdaten zu erfassen.

_Diese Integration wird von Refiner gepflegt._

## Über die Integration {#about-the-integration}

Verwenden Sie die Integration von Refiner und Braze, um Umfrageereignisse und Antwortdaten von Refiner an Ihr Braze-Konto zu senden. Nutzen Sie diese Daten, um Braze-Campaigns basierend auf Umfrageinteraktionen zu triggern (z. B. eine abgeschlossene Umfrage), Nutzer:innen anhand von Antworten zu segmentieren und Braze-Nutzerprofile mit aus Umfrageantworten abgeleiteten Merkmalen zu aktualisieren.

## Anwendungsfälle {#use-cases}

- Nutzer:innen anhand von Umfrageantworten segmentieren, z. B. NPS-Werte oder CSAT-Bewertungen.
- Personalisierte Campaigns in Braze basierend auf Umfrageergebnissen triggern.
- Kanalübergreifende Journeys mit Braze-Canvas oder anderen Orchestrierungstools steuern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Refiner-Konto | Ein [Refiner](https://refiner.io)-Konto ist erforderlich, um diese Integration zu nutzen. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL Ihrer Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Ihr Braze-Konto verbinden {#step-1-connect-your-braze-account}

Wählen Sie im Bereich **Integrations** Ihres Refiner-Projekts **Connect Braze** aus. Geben Sie Ihren Braze-REST-API-Schlüssel und Ihren Braze-Instanzbezeichner ein.

### Schritt 2: Nutzerbezeichner zuordnen {#step-2-map-user-identifiers}

Ordnen Sie den Refiner-Nutzerbezeichner dem von Ihnen verwendeten Braze-Bezeichner zu, z. B. einer Braze-`external_id` oder E-Mail-Adresse. So wird sichergestellt, dass Ereignisse dem richtigen Nutzerprofil in Braze zugeordnet werden.

### Schritt 3: Zu synchronisierende Daten auswählen {#step-3-choose-data-to-sync}

- Wählen Sie die Umfragen aus, deren Daten Sie mit Braze synchronisieren möchten.
- Wählen Sie aus, welche Refiner-Ereignisse an Braze gesendet werden sollen, z. B. **Survey Seen**, **Survey Dismissed** und **Survey Completed**.

![Das Refiner-Panel für Integrationseinstellungen mit Optionen zur Umfrageauswahl und Ereigniszuordnung.]({% image_buster /assets/img/refiner.jpg %})

## Refiner anpassen {#customize-refiner}

- Legen Sie fest, ob die an Braze gesendeten Daten nur Umfrageantworten oder auch zusätzliche Kontaktdatenfelder enthalten sollen.
- Legen Sie fest, ob synchronisierte Datenfelder mit dem Präfix `refiner_` versehen werden sollen, um sie in Ihrem Braze-Konto leichter identifizieren zu können.

## Umfragedaten in Braze verwenden {#use-survey-data-in-braze}

Nach der Verbindung von Braze und Refiner erscheinen Umfrageereignisse wie **Saw Survey** oder **Completed Survey** in den Nutzerprofilen Ihres Braze-Kontos. Verwenden Sie diese Ereignisse, um Nachrichten in Braze zu triggern und zu personalisieren, oder nutzen Sie Umfrageantwortdaten, um Nutzer:innen zu segmentieren.

{% alert note %}
Sie können Refiner-Umfragen auch per E-Mail über Braze versenden. Weitere Informationen finden Sie in der [Integrationsdokumentation von Refiner](https://refiner.io/docs/kb/integrations/braze-integration/).
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Falls Probleme mit der Integration auftreten, nutzen Sie die folgenden Ressourcen:

- [Integrationsleitfaden für Refiner und Braze](https://refiner.io/docs/kb/integrations/braze-integration/)
- [Refiner-Support kontaktieren](https://refiner.io/docs/kb/getting-started/contact-support/)