---
nav_title: Okendo
article_title: Okendo
description: "Erfahren Sie, wie Sie Okendo in Braze integrieren können."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) ist eine einheitliche Plattform für das Kundenmarketing, die Tools zur Pflege der Kundenbindung, zum Ausbau der Mundpropaganda und zur Maximierung des LTV or Lifetime-Value or Lifetime-Value bietet, um Ihre Kund:innen für ein schnelleres und effizienteres Wachstum zu mobilisieren.

*Diese Integration wird von Okendo gepflegt.*

## Über die Integration {#about-the-integration}

Die Integration von Braze mit Okendo funktioniert über mehrere Produkte der Okendo-Plattform, darunter Reviews, Loyalty, Referrals, Umfragen und Quizze. Okendo sendet angepasste Events und Nutzerattribute an Braze, die zur Personalisierung und zum Trigger or triggern or triggern von Nachrichten verwendet werden können.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Okendo-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein Okendo-Konto. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | [Ihre URL für den Representational State Transfer-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1. Schritt: Braze-Konnektor in Okendo einrichten {#step-1-set-up-braze-connector-in-okendo}

1. Gehen Sie in Okendo zu **Settings** > **Integrations** > **Email & Kurzmitteilungsdienst or SMS** > **Braze**.
2. Fügen Sie den API-Endpunkt und den API-Schlüssel zu den **Integration**-Einstellungen hinzu.

### 2. Schritt: Bezeichner konfigurieren {#step-2-configure-your-identifier}

Das Feld `external_id` dient zur Identifizierung der Nutzer:innen, die mit jedem Event verknüpft sind. Aktivieren Sie **Use Shopify Customer ID for Braze user identification**, um das Feld mit Shopify-Kunden-IDs zu verknüpfen. Andernfalls deaktivieren Sie die Option, um es mit der E-Mail-Adresse der jeweiligen Nutzer:innen zu verknüpfen.

## Synchronisierung von Okendo-Events und -Attributen mit Braze {#syncing-okendo-events-and-attributes-to-braze}

### Angepasste Events {#custom-events}

{% alert note %}
Beispiele für Event-Daten finden Sie in der [Dokumentation von Okendo](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c).
{% endalert %}

#### Review-Events

- Okendo Review Created
- Okendo Review Request

#### Referral-Events

- Sent Okendo Referral
- Opted In to Okendo Referrals
- Okendo Referral Invitation
- Received Okendo Referral Coupon
- Redeemed Okendo Referral Coupon
- Okendo Referral Rejected

#### Loyalty-Events

- Enrolled in Okendo Loyalty
- Okendo Loyalty Points Awarded
- Okendo Loyalty Points Redeemed
- Okendo Loyalty Tier Changed
- Okendo Loyalty Points Adjusted

#### Umfrage-Event {#survey-event}

- Submitted Okendo Survey

#### Quiz-Event

- Submitted Okendo Quiz

### Angepasste Attribute {#custom-attributes}

Okendo sendet Kundenprofil or Nutzerprofil-Daten als angepasste Attribute in Braze, die zur Erstellung von Zielgruppen-Segmenten verwendet werden können. Beispiele hierfür sind:

- Profilfragen, die in Umfragen und bei der Einreichung einer Bewertung gestellt werden, wie Alter, Geburtstag, Hauttyp und Haarfarbe
- Review-Metriken wie _Average Review Rating_ und _Average Review Sentiment_
- Loyalty-Metriken wie _Points Balance_ und _VIP Tier_
- Referral-Metriken wie die _Number of Successful Referrals_ und _Total Referral Revenue_
- Net Promoter Score-Score aus einer Umfrage

## Verwendung von Braze mit Okendo-Produkten {#using-braze-with-okendo-products}

Je nach Okendo-Produkt müssen Sie zusätzliche Schritte durchführen, um Braze und Okendo zusammen zu verwenden. Weitere Einzelheiten finden Sie in den folgenden Artikeln:

- [Integration von Reviews mit Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Integration von Loyalty mit Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Integration von Referrals mit Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Integration von Umfragen mit Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Integration von Quizzen mit Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Wenn Sie Hilfe bei der Konfiguration der Integration benötigen, wenden Sie sich an das Okendo-Support-Team.
{% endalert %}