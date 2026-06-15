---
nav_title: optilyz
article_title: optilyz
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und optilyz, die es Ihnen ermöglicht, kundenorientiertere, nachhaltigere und gewinnbringendere Direkt-Mailing-Kampagnen durchzuführen."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz](https://optilyz.com) ist eine Plattform zur Automatisierung von Direkt-Mailings, mit der Sie kundenorientiertere, nachhaltigere und gewinnbringendere Direkt-Mailing-Kampagnen durchführen können.

_Diese Integration wird von optilyz gepflegt._

## Über die Integration {#about-the-integration}

Nutzen Sie die Webhook-Integration von optilyz und Braze, um Ihren Kund:innen Direkt-Mailings wie Briefe, Postkarten und Selfmailer zu senden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| optilyz-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein optilyz-Konto. |
| optilyz-API-Schlüssel<br><br>`<OPTILYZ_API_KEY>` | Ihr optilyz-Customer-Success-Manager stellt Ihnen Ihren optilyz-API-Schlüssel zur Verfügung.<br><br>Dieser API-Schlüssel ermöglicht es Ihnen, Ihre Braze- und optilyz-Konten zu verbinden. |
| optilyz-Automatisierungs-ID<br><br>`<OPTILYZ_AUTOMATION_ID>` | Die Automatisierungs-ID finden Sie in einem Feld in der Kopfzeile der Seite.<br><br>Wenn Sie bei optilyz angemeldet sind, können Sie zu der Automatisierung navigieren, an die Sie Daten senden möchten.<br>Die Automatisierung muss zuerst aktiviert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Direkt-Mailing wie einen digitalen Kanal zu betreiben bedeutet, sich von Massenmailings zu lösen und den Kanal als Teil Ihrer (digitalen) Customer Journeys zu nutzen. Die Vorteile eines modernen Ansatzes für Direkt-Mailing sind:
- Gesteigerte Conversion-Rates durch erhöhte Relevanz, zusätzliche Anwendungsfälle, einfachere A/B-Tests und kanalübergreifende Effekte
- Geringerer Aufwand durch Automatisierung und eine End-to-End-Lösung
- Geringere Kosten durch Rahmenverträge und Kostentransparenz

## Integration

Für die Integration mit optilyz verwenden Sie die [optilyz-API](https://www.optilyz.com/doc/api/), um Empfänger:innen-Daten an den Braze-Webhook zu senden.

### 1. Schritt: Erstellen Sie Ihr Braze-Webhook-Template {#step-1-create-your-braze-webhook-template}

Um ein optilyz-Webhook-Template zu erstellen, das Sie in zukünftigen Campaigns oder Canvases verwenden können, navigieren Sie in der Braze-Plattform zu **Content** > **Webhook**. Wählen Sie dann **Create webhook template** aus.

Wenn Sie eine einmalige optilyz-Webhook-Campaign erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
- **Webhook-URL**: Die Webhook-URL ist für jede Kund:in eindeutig und wird Ihnen von Ihrem optilyz-Customer-Success-Manager zur Verfügung gestellt.
- **Anfragetext**: Rohtext

#### Anfrage-Header und Methode {#request-headers-and-method}

optilyz benötigt außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar im Template enthalten, aber im Tab **Einstellungen** müssen Sie `<OPTILYZ_API_KEY>` durch Ihren optilyz-API-Schlüssel ersetzen. Dieser Schlüssel muss ein „:“ direkt nach dem Schlüssel enthalten und in Base 64 kodiert sein.

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Die Anfrage-Header und die HTTP-Methode, die im Braze-Webhook-Builder angezeigt werden.]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### Anfragetext {#request-body}

Im folgenden Anfragetext können Sie beliebige Liquid-Personalisierungs-Tags verwenden und ein angepasstes Anfrage-Template gemäß der [API-Dokumentation](https://www.optilyz.com/doc/api/) von optilyz erstellen.

Das Feld `variation` ist optional und kann festlegen, welches Design innerhalb der Automatisierung verwendet werden soll. Wird eine Variante ausgelassen, weist optilyz eine der definierten Varianten nach dem Zufallsprinzip zu.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Ein Bild des Anfragetext-Codes und der Webhook-URL, die im Tab „Verfassen“ des Braze-Webhook-Builders angezeigt werden.]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### 2. Schritt: Vorschau Ihrer Anfrage {#step-2-preview-your-request}

Sehen Sie sich als Nächstes eine Vorschau Ihrer Anfrage im Panel **Vorschau** an oder wechseln Sie zum Tab **Test**, wo Sie eine:n zufällige:n Nutzer:in, eine:n bestehende:n Nutzer:in auswählen oder eigene Daten anpassen können, um Ihren Webhook zu testen. Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen!

![Verschiedene Testfelder, die im Tab „Test“ des Braze-Webhook-Builders verfügbar sind.]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) erstellen.
{% endalert %}