---
nav_title: Flybuy
article_title: Flybuy
alias: /partners/flybuy/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Flybuy, einer Plattform für Standortdienste, mit der Sie Standortintelligenz in Ihre Betriebs- und Marketingfähigkeiten integrieren können."
page_type: partner
search_tag: Partner

---

# Flybuy

> [Flybuy](https://www.flybuy.com/) von Radius Networks ist die führende Omnichannel-Standortplattform, die KI-gestützte Technologie nutzt, um die Servicegeschwindigkeit bei Abholung, Lieferung, Drive-Thru und Vor-Ort-Bestellungen zu optimieren. Über die integrierte Marketing Suite ermöglicht Flybuy Marken außerdem, hochgradig zielgerichtete, momentbasierte Nachrichten zu senden, die das Engagement steigern, den Bestellwert erhöhen und umfassendere Loyalty-Initiativen unterstützen.

_Diese Integration wird von Flybuy gepflegt._

## Über die Integration {#about-the-integration}

Flybuy liefert umfangreiche User-Intelligence-Events an Braze und ermöglicht es Marken, hochrelevante, standortbezogene Nachrichten mit dem höchsten Grad an Personalisierung zu senden. Wenn Nutzer:innen ein Event in Flybuy auslösen, werden angepasste Events mit umfangreichen Nutzerattributen an Braze übermittelt. Diese Events und Attribute können genutzt werden, um Omnichannel-Abläufe zu steuern und standortbasierte Nachrichten zu triggern.

## Voraussetzungen {#prerequisites}

Folgendes ist erforderlich, bevor Sie die Integration aktivieren:

| Anforderung | Beschreibung |
|---|---|
| Flybuy-Konto | Ein Flybuy-Konto mit mindestens einem Projekt. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit `users.track`-Berechtigungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Um die Integration zu aktivieren, führen Sie die folgenden Schritte aus:

1. Navigieren Sie im Flybuy-Merchant-Portal zu **Project Info** und klicken Sie auf **Events Engine**.
2. Klicken Sie auf **Add a Destination** und wählen Sie dann **Braze** aus.
3. Fügen Sie Ihren Braze-API-Schlüssel und -Endpunkt hinzu und wählen Sie die Events aus, die Sie aktivieren möchten.
4. Klicken Sie auf **Finish Setup**.

{% alert important %}
Flybuy ordnet `loyalty_id` der Braze-`external_id` für eingeloggte Nutzer:innen zu.
{% endalert %}

## Anwendungsfälle {#use-cases}

- [Abholung](https://www.flybuy.com/flybuypickup)
- [Lieferung](https://www.flybuy.com/flybuydelivery)
- [Drive-Thru](https://www.flybuy.com/flybuydrivethru)
- [Tischservice](https://www.flybuy.com/flybuytableservice)
- [Mobiler Hotel-Check-in und Bestellung](https://www.flybuy.com/industries/hospitality)
- [Marketing Suite](https://www.flybuy.com/flybuy-marketing-suite)

## Beispiele für event- und attributbasierte Trigger {#event-and-attribute-based-trigger-examples}

Angepasste Events und angepasste Attribute können genutzt werden, um eine Vielzahl personalisierter Erlebnisse zu ermöglichen.

### Ein Zielgruppensegment von Kund:innen mit schlechter Abholerfahrung erstellen {#build-an-audience-segment-of-customers-who-had-a-bad-pickup-experience}

Sprechen Sie beispielsweise alle Kund:innen an, die ihre Abholerfahrung mit weniger als 5 Sternen bewertet haben.

![Segment für schlechte Abholerfahrung]({% image_buster /assets/img/flybuy/flybuy1.png %})

### Eine Benachrichtigung triggern, wenn Kund:innen einen virtuellen Abholbereich betreten {#trigger-an-alert-when-a-customer-enters-a-virtual-pickup-area}

Senden Sie eine personalisierte SMS an Kund:innen ohne Loyalty-Konto, um sie zum Herunterladen der App und zur Erstellung eines Loyalty-Kontos aufzufordern.

![Eine Benachrichtigung triggern, wenn Kund:innen einen virtuellen Abholbereich betreten]({% image_buster /assets/img/flybuy/flybuy2.png %})

![Nachricht bei Betreten eines virtuellen Abholbereichs]({% image_buster /assets/img/flybuy/flybuy2a.png %})

### Ein Zielgruppensegment von Kund:innen mit langer Wartezeit erstellen {#build-an-audience-segment-of-customers-who-had-a-long-wait-time}

Sprechen Sie beispielsweise alle Kund:innen an, die beim Verlassen eines virtuellen Filialbereichs eine Wartezeit von über zwei Minuten hatten.

![Ein Zielgruppensegment von Kund:innen mit langer Wartezeit erstellen]({% image_buster /assets/img/flybuy/flybuy3.png %})

### Eine Kurskorrektur-Benachrichtigung triggern, wenn Kund:innen zum falschen Standort unterwegs sind {#trigger-a-course-correction-alert-when-a-customer-is-headed-to-the-wrong-location}

Senden Sie eine Push-Benachrichtigung an Kund:innen, wenn sie zu einem anderen Standort unterwegs sind oder dort angekommen sind als dem, an dem sie ihre Bestellung aufgegeben haben.

### Sonderangebote basierend auf Fahrt-Meilensteinen senden {#deliver-special-offers-based-on-trip-milestones}

Senden Sie beispielsweise ein Sonderangebot, wenn VIP-Kund:innen an ihren Lieblingsstandorten ankommen.

### Ein Zielgruppensegment von Kund:innen mit fehlenden Artikeln in der Bestellung erstellen {#build-an-audience-segment-of-customers-who-were-missing-items-in-their-order}

Sprechen Sie beispielsweise alle Kund:innen an, die kommentiert haben, dass Artikel in ihrer digitalen Bestellung gefehlt haben.

Weitere Details zu APIs und SDKs finden Sie in der [Flybuy-Entwicklerdokumentation](https://www.radiusnetworks.com/developers/flybuy/#/).