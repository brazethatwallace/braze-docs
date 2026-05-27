---
nav_title: Lob
article_title: Lob
alias: /partners/lob/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Lob.com, die es Ihnen ermöglicht, Direkt-Mailings wie Briefe, Postkarten und Schecks per Post zu versenden."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) ist ein Online-Dienst, der es Ihnen ermöglicht, Direkt-Mailings an Ihre Nutzer:innen zu senden.

_Diese Integration wird von Lob gepflegt._

## Über die Integration {#about-the-integration}

Mit dieser Integration können Sie:

- Briefe, Postkarten und Schecks über die Post versenden – mithilfe von Braze-Webhooks und der Lob API.
- Lob-Events als angepasste Attribute und Events über Braze-Datentransformation und Lob-Webhooks mit Braze teilen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Lob-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein Lob-Konto erforderlich. |
| Lob API-Schlüssel | Ihren Lob API-Schlüssel finden Sie im Abschnitt „Einstellungen“ unter Ihrem Namen im Lob-Dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Versenden von Post mit Braze-Webhooks {#sending-mail-using-braze-webhooks}

### 1. Schritt: Wählen Sie einen Lob-Endpunkt {#step-1-choose-a-lob-endpoint}

Je nachdem, was Sie in Lob tun möchten, müssen Sie den entsprechenden Endpunkt in der HTTP-Anfrage Ihres Webhooks verwenden. Ausführliche Informationen zu den einzelnen Endpunkten finden Sie in der [API-Referenzdokumentation von Lob](https://lob.com/docs#intro).

| Basis-URL | Verfügbare Endpunkte |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 2. Schritt: Erstellen Sie Ihr Braze-Webhook-Template {#step-2-create-your-braze-webhook-template}

Um ein Lob-Webhook-Template zu erstellen, das Sie in zukünftigen Campaigns oder Canvases verwenden können, navigieren Sie im Braze-Dashboard zu **Content** > **Webhook**. Wählen Sie dann **Create webhook template**.

Wenn Sie eine einmalige Lob-Webhook-Campaign erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:

- **Webhook-URL**: `<LOB_API_ENDPOINT>`
- **Anfrage-Body**: Rohtext

#### Anfrage-Header und Methode {#request-headers-and-method}

Lob benötigt einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paar im Template enthalten, aber auf dem Tab **Einstellungen** müssen Sie `<LOB_API_KEY>` durch Ihren Lob API-Schlüssel ersetzen. Dieser Schlüssel muss ein „:“ direkt nach dem Schlüssel enthalten und in Base 64 kodiert sein.

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Anfrage-Body-Code und Webhook-URL im Tab „Verfassen“ des Braze-Webhook-Builders.]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Anfrage-Body {#request-body}

Im Folgenden sehen Sie einen Beispiel-Anfrage-Body für den Lob-Postcards-Endpunkt. Dieser Anfrage-Body wird zwar im Basis-Lob-Template in Braze bereitgestellt, aber wenn Sie andere Endpunkte verwenden möchten, müssen Sie Ihre Liquid-Felder entsprechend anpassen.

{% raw %}
```json
{
  "description": "Demo Postcard",
  "to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
  },
  "front": "https://lob.com/postcardfront.pdf",
  "back": "https://lob.com/postcardback.pdf",
  "use_type": "marketing",
  "size": "6x11"
}
```
{% endraw %}

### 3. Schritt: Vorschau Ihrer Anfrage {#step-3-preview-your-request}

An diesem Punkt sollte Ihre Campaign bereit zum Testen und Versenden sein. Überprüfen Sie das Lob-Dashboard und die Fehlermeldungsprotokolle in der Braze-Entwicklungskonsole, wenn Fehler auftreten. Der folgende Fehler wurde beispielsweise durch einen falsch formatierten Authentifizierungs-Header verursacht.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) erstellen.
{% endalert %}

![Ein Fehlermeldungsprotokoll, das die Zeit, den App-Namen, den Kanal und die Fehlermeldung anzeigt. Die Fehlermeldung enthält den Nachrichtenhinweis und den Statuscode.]({% image_buster /assets/img_archive/error_log.png %})

## Events über Lob-Webhooks teilen {#sharing-events-using-lob-webhooks}

Mit [Braze-Datentransformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/) können Sie Webhooks zur Automatisierung des Datenflusses von externen Plattformen in Braze erstellen und verwalten. Jede Transformation erhält einen eindeutigen Endpunkt, den andere Plattformen als Ziel für ihren Webhook verwenden können.

{% alert important %}
Das Datentransformations-Template von Lob sendet Events über Ihren [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), der Datenpunkte protokolliert. Wir empfehlen, in Ihren Lob-Webhook-Einstellungen ein Rate-Limit festzulegen, um eine übermäßige Datenprotokollierung zu vermeiden.
{% endalert %}

### 1. Schritt: Erstellen Sie eine Transformation in Braze {#step-1-create-a-transformation-in-braze}

1. Navigieren Sie im Braze-Dashboard zu **Data Settings** > **Data Transformations**, und wählen Sie dann **Create Transformation**.
2. Geben Sie einen kurzen, beschreibenden Namen für Ihre Transformation ein.
3. Wählen Sie unter **Bearbeitungserfahrung** die Option **Template verwenden** aus, suchen Sie dann nach Lob und aktivieren Sie das Kontrollkästchen.
4. Wenn Sie fertig sind, wählen Sie **Transformation erstellen**. Sie werden zum Transformations-Editor weitergeleitet, den Sie im nächsten Schritt verwenden.

### 2. Schritt: Füllen Sie das Lob-Template aus {#step-2-fill-out-the-lob-template}

Mit diesem Template können Sie eines Ihrer Lob-Events in ein angepasstes Event oder Attribut transformieren, das in Braze verwendet werden kann. Folgen Sie den Inline-Kommentaren, um das Template fertigzustellen.

{% alert tip %}
Ausführliche Informationen über die Webhook-Payload-Struktur von Lob finden Sie unter [Lob: Webhooks verwenden](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### 3. Schritt: Erstellen Sie einen Webhook in Lob {#step-3-create-a-webhook-in-lob}

1. Wenn Sie mit der Erstellung Ihres Templates fertig sind, wählen Sie **Aktivieren** und kopieren Sie die **Webhook-URL** in Ihre Zwischenablage.
2. [Erstellen Sie in Lob einen neuen Webhook](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1) und verwenden Sie dann Ihre Webhook-URL von Braze, um den Webhook zu empfangen.