---
nav_title: Nift
article_title: Nift
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Nift, einer zweiseitigen Plattform, die Unternehmen dabei hilft, Kund:innen zu gewinnen, zu binden und zu halten."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) hilft Unternehmen, Kund:innen zu gewinnen, zu binden und zu halten. Die zweiseitige Plattform hilft Partnern, sich bei ihren Kund:innen mit Nift-Geschenkkarten zu bedanken. Sich bei Kund:innen zu bedanken steigert den Lifetime-Value und generiert zusätzlichen Umsatz.

_Diese Integration wird von Nift gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Nift ermöglicht es Ihnen, zu wichtigen Zeitpunkten im Kundenlebenszyklus automatisch „Dankeschöns“ mit Nift-Geschenken auszulösen und zu erkennen, welche Kund:innen ihr Geschenk eingelöst haben. Nift-Geschenkkarten können verwendet werden, um auf Produkte und Dienste von Marken zuzugreifen, die auf die Matchmaking-Technologie von Nift setzen, um kostengünstig und in großem Umfang neue Kund:innen zu gewinnen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Nift-Konto | Um diese Partnerschaft zu nutzen, ist ein Nift-Konto erforderlich. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit allen Nutzerdaten-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Mit Braze in Nift verbinden {#step-1-connect-to-braze-in-nift}

Besuchen Sie Ihr [Nift-Dashboard](https://www.gonift.com/users/sign_in), navigieren Sie zu **Accounts** > **Integrations** > **Braze** und klicken Sie auf **Connect**.

### 2. Schritt: Braze-Zugangsdaten hinzufügen {#step-2-add-braze-credentials}

Geben Sie auf der Seite **Link your Braze Account** Ihren Braze-REST-API-Schlüssel ein und wählen Sie Ihren Braze-Endpunkt aus, der von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) abhängt.

Sie können den Parameternamen der Kunden-ID im Empfehlungslink ändern, der an Ihre Kund:innen gesendet wird. Nift verwendet diesen, um Ihre Kund:innen in Braze als verarbeitet zu markieren, sobald sie ein Geschenk von einer unserer Marken ausgewählt haben.

Klicken Sie auf **Link Account**.

![„Nift-Integrationsseite, die Nutzer:innen zur Eingabe des Braze-API-Schlüssels und der Braze-Dashboard-URL auffordert.“]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## Verwendung der Integration {#using-the-integration}

Um die Integration zu nutzen, verteilen Sie den Empfehlungslink in Ihren Nachrichten. Wenn Ihre Kund:innen den Empfehlungslink verwenden und ein Geschenk von einer unserer Marken auswählen, markiert Nift sie in Braze als verarbeitet.

Nach der Integration mit Braze sendet Nift automatisch Ereignisse mit den folgenden Daten an den bestehenden Braze-Datensatz der Kund:innen:

- Ereignisname: `nift_processed`
- Zeit: Der Zeitpunkt, zu dem die Kund:innen das Geschenk ausgewählt bzw. eingelöst haben