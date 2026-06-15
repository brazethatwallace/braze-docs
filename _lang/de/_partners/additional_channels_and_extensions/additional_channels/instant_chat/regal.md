---
nav_title: Regal
article_title: Regal
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Regal, einer Voice-KI-Agenten-Plattform, mit der Sie personalisierte, Omnichannel-Customer-Journeys mithilfe von Braze-Daten und Regal-Gesprächen orchestrieren können."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) ist eine Voice-KI-Agenten-Plattform, die Unternehmen dabei unterstützt, durch intelligente Echtzeit-Gespräche über verschiedene Kanäle hinweg bessere Kundenerlebnisse zu schaffen.

_Diese Integration wird von Regal gepflegt._

Durch die Integration von Regal mit Braze können Sie Verhaltensdaten und konversationelle KI vereinen, um personalisierte, Omnichannel-Customer-Journeys zu orchestrieren. Braze erfasst Signale über den gesamten Kundenlebenszyklus, die Regal nutzt, um KI-Agenten-Gespräche, Routing und Echtzeit-Entscheidungen zu steuern.

Verwenden Sie Braze-Daten, um zu bestimmen, was Ihre KI-Agenten sagen, wie sie reagieren und wann sie aktiv werden. Senden Sie Gesprächsergebnisse und Insights zurück an Braze, um Targeting und Lifecycle-Marketing zu verbessern. Lösen Sie KI-gestützte Anrufe und SMS an wichtigen Punkten der Customer Journey aus und setzen Sie in Braze basierend auf dem Gesprächsverlauf nach.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Regal-Konto | Ein Regal-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Regal-API-Schlüssel | Ein Regal-API-Schlüssel ermöglicht das Senden von Events von Braze an Regal.<br><br>Senden Sie eine E-Mail an [support@regal.io](mailto:support@regal.io), um diesen Schlüssel zu erhalten. |
| Braze-Datentransformation | Eine [Datentransformation]({{site.baseurl}}/data_transformation/) ist erforderlich, um Daten von Regal zu empfangen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration: Daten von Braze an Regal senden {#integration-sending-data-from-braze-to-regal}

Verwenden Sie Braze-Canvas- oder Campaign-Webhooks, um Kundenprofil- und Event-Daten von Braze an Regal zu senden.

### 1. Schritt: Neue Kontakte in Regal erstellen {#step-1-create-new-contacts-in-regal}

Erstellen Sie ein Canvas oder eine Campaign, die jedes Mal einen Webhook an Regal sendet, wenn ein neues Braze-Profil erstellt wird, das für Anrufe und SMS in Regal verfügbar sein soll.

1. Erstellen Sie ein Canvas oder eine Campaign mit dem Titel „Neuen Kontakt für Regal erstellen“ und wählen Sie **Aktionsbasiert** als Eingangstyp aus.

2. Legen Sie die Triggerlogik als **Angepasstes Event** fest und wählen Sie das Event aus, das ausgelöst wird, wenn ein Profil mit einer Telefonnummer erstellt wird. Regal empfiehlt außerdem, einen Filter hinzuzufügen, der sicherstellt, dass das Telefonfeld gesetzt ist.

3. Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
   - **Webhook-URL**: <https://events.regalvoice.com/events>
   - **Anfragetext**: Rohtext

#### Anfrage-Header und Methode {#request-headers-and-method}

Regal erfordert außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paare im Tab **Einstellungen** im Template enthalten:
{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Anfragetext {#request-body}

Der einzige erforderliche Bezeichner ist eine Telefonnummer innerhalb von `traits.phones`. Verwenden Sie das Objekt `traits.phones`, um einem Kontakt eine oder mehrere Telefonnummern zuzuordnen. Jede Telefonnummer kann ein eigenes Label, eine primäre Kennzeichnung sowie den Opt-in-Status für Sprache und SMS speichern. Diese Struktur ist besonders nützlich, wenn ein Kontakt mehrere Telefonnummern hat.

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "custom1": "<custom1>",
    "custom2": "<custom2>"
  },
  "eventSource": "braze"
}
```

Das obige Payload-Beispiel geht davon aus, dass die aufgeführten Telefonnummern den aktuellen Opt-in-Status für Sprache und SMS enthalten. Wenn das nicht der Fall ist, können Sie `voiceOptIn` und `smsOptIn` beim Erstellen des Kontakts weglassen und ein separates Canvas oder eine Campaign einrichten, um die Einwilligung für die jeweilige Telefonnummer zu aktualisieren, sobald das Opt-in erfasst wird.

### 2. Schritt: Opt-in-Informationen aktualisieren {#step-2-update-opt-in-information}

Wenn Opt-in und Opt-out an verschiedenen Stellen Ihrer App stattfinden können, aktualisieren Sie Regal, wenn Nutzer:innen ihren Abostatus ändern.

Regal empfiehlt die Verwendung des `traits.phones`-Schemas, damit Sie Opt-in und Opt-out pro Telefonnummer verwalten können, anstatt auf Kontaktebene.

Verwenden Sie das folgende Canvas-Setup, um aktuelle Opt-in-Informationen an Regal zu senden.

1. Erstellen Sie ein neues Canvas oder eine Campaign mit dem Titel „Opt-in oder Opt-out an Regal senden“.

2. Wählen Sie eine der folgenden Trigger-Optionen und wählen Sie das Feld aus, das den Opt-in-Status der Nutzer:innen darstellt:
    - **Nutzerprofilfeld aktualisiert**
    - **Abo-Gruppenstatus aktualisieren**
    - **Abostatus**

3. Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
   - **Webhook-URL**: <https://events.regalvoice.com/events>
   - **Anfragetext**: Rohtext

#### Anfrage-Header und Methode

Regal erfordert außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paare im Tab **Einstellungen** im Template enthalten:
{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Anfragetext

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<phoneNumber>": {
        "voiceOptIn": {
          "subscribed": "<voice_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": "<sms_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    }
  },
  "eventSource": "braze"
}
```

Sie können auch zusätzliche Nutzerprofil-Attribute in diesen Payload aufnehmen, um weitere Attribute gleichzeitig auf dem neuesten Stand zu halten.

### 3. Schritt: Angepasste Events senden {#step-3-send-custom-events}

Richten Sie ein Canvas oder eine Campaign für jedes wichtige Event ein, das Sie an Regal senden möchten.

Diese Events dienen nicht nur dazu, Kontaktaufnahmen auszulösen (z. B. eine Bestätigungs-SMS, wenn ein Lead die Registrierung abschließt). Sie liefern den Echtzeit-Kontext, der bestimmt, wie Regal-KI-Agenten sprechen, Entscheidungen treffen und Gespräche über die gesamte Customer Journey hinweg weiterleiten. Indem Sie Event-Daten und Attribute von Braze senden, ermöglichen Sie KI-Agenten, Gespräche basierend auf dem Verhalten, den Präferenzen und der Lifecycle-Phase jeder Nutzer:in anzupassen.

Beispielsweise können Braze-Events und -Attribute in Regal verwendet werden, um:

- **KI-Agenten-Sprache zu personalisieren**: Aktuelles Verhalten oder Produktinteresse direkt in Gesprächen referenzieren.
  - Beispiel: Wenn eine Nutzer:in Lebensversicherungsoptionen erkundet hat, kann der Agent `contact.firstName` und `contact.brazeProductInterest` im Gespräch referenzieren.
- **Dynamische Gesprächslogik zu steuern**: In Echtzeit anpassen, was der Agent priorisiert.
  - Beispiel: Wenn `contact.brazeAge` größer als 65 ist, Medicare-Abdeckung priorisieren; andernfalls auf ACA-Pläne und den aktuellen Versicherungsstatus fokussieren.
- **Intelligentes Routing und Eskalation zu ermöglichen**: Gespräche basierend auf Wert oder Absicht weiterleiten.
  - Beispiel: Wenn `contact.brazeLeadTier` „High Value“ ist, nach der Qualifizierung an einen Senior-Agenten weiterleiten; andernfalls mit dem KI-Agenten fortfahren.
- **Messaging und Angebote abzustimmen**: Anpassen, was der Agent basierend auf dem Campaign-Kontext präsentiert.
  - Beispiel: Wenn `contact.brazeCampaignName` „Spring Mortgage Promo“ ist, das Werbeangebot während des Gesprächs hervorheben.

Erstellen Sie ein neues Canvas oder eine Campaign mit dem Titel „Produktinteresse-Event an Regal senden“.

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "brazeProductInterest": "Life Insurance",
    "brazeAge": 68,
    "brazeLeadTier": "High Value",
    "brazeCampaignName": "Spring Insurance Promo"
  },
  "name": "Product Interest Captured",
  "properties": {
    "action": "Viewed Product Comparison",
    "productCategory": "Life Insurance",
    "intentScore": "High",
    "lastPage": "Compare Life Insurance Plans",
    "readyToCommit": true
  },
  "eventSource": "braze"
}
```

#### Aktuelle Kontaktattribute {#up-to-date-contact-attributes}

Regal empfiehlt außerdem, wichtige Nutzerprofil-Attribute in den Event-Payloads mitzusenden, damit Regal bei wichtigen Ereignissen über aktuelle Kontaktattribute verfügt.

{% alert note %}
Wenn Sie Fragen dazu haben, welche Events Sie an Regal senden sollten oder wie Sie diese Canvases und Campaigns einrichten, senden Sie eine E-Mail an [support@regal.io](mailto:support@regal.io).
{% endalert %}

## Integration: Daten von Regal an Braze senden {#integration-sending-data-from-regal-to-braze}

Verwenden Sie Regal Reporting Webhooks und Braze-Datentransformation, um Regal-Reporting-Events (wie `SMS.sent` und `call.completed`) an Braze zu senden. Nachdem Sie diese Events zugeordnet haben, erscheinen sie in Nutzerprofilen und stehen für Segmentierung, Canvas und Campaigns zur Verfügung.

### 1. Schritt: Eine Datentransformation in Braze erstellen {#step-1-create-a-data-transformation-in-braze}

Erstellen Sie eine Datentransformation für jeden Regal-Webhook, den Sie an Braze senden möchten.

So erstellen Sie eine Datentransformation:
1. Navigieren Sie zur Seite **Transformationen** in Ihrem Braze-Dashboard.
2. Geben Sie Ihrer Transformation einen Namen und klicken Sie auf **Transformation erstellen**.
3. Wählen Sie in der Liste der Transformationen <i class="fa-solid fa-ellipsis-vertical" title="Aktionen anzeigen"></i> **Aktionen anzeigen** und wählen Sie **Webhook-URL kopieren**.

![]({% image_buster /assets/img/regal/copy_webhook_url.png %})

### 2. Schritt: Reporting-Webhooks in Regal aktivieren {#step-2-enable-reporting-webhooks-in-regal}

So richten Sie Reporting-Webhooks ein:
1. Öffnen Sie die Regal-App und navigieren Sie zur Seite **Einstellungen**.

2. Klicken Sie im Bereich **Reporting Webhooks** auf **Webhooks erstellen**.

3. Fügen Sie in der Eingabe für den Webhook-Endpunkt die Webhook-URL der Braze-Datentransformation für die zugehörige Datentransformation hinzu.

![]({% image_buster /assets/img/regal/edit_webhook.png %}){: style="max-width:60%;"}

#### Aktualisierung eines Endpunkts {#updating-an-endpoint}

Wenn Sie einen Endpunkt bearbeiten, kann es bis zu 5 Minuten dauern, bis der Cache aktualisiert ist und Events an Ihren neuen Endpunkt gesendet werden.

#### Wiederholungsversuche {#retries}

Derzeit führt Regal keine Wiederholungsversuche für diese Events durch. Wenn Braze nicht innerhalb von 5 Sekunden antwortet, verwirft Regal das Event. Regal plant, Wiederholungsversuche in einer zukünftigen Version hinzuzufügen.

#### Events
Die vollständige Liste der Reporting-Events, Eigenschaftsdefinitionen und Beispiel-Payloads finden Sie im [Reporting-Webhooks-Leitfaden](https://developer.regal.io/docs/reporting-webhooks#events) von Regal.

### 3. Schritt: Regal-Events in Braze-Events transformieren {#step-3-transform-regal-events-into-braze-events}

Mit dem Feature [Datentransformation]({{site.baseurl}}/data_transformation/) von Braze können Sie eingehende Regal-Events in das Format abbilden, das erforderlich ist, um sie als Attribute, Events oder Käufe in Braze hinzuzufügen.

1. Benennen Sie Ihre Datentransformation. Es wird empfohlen, eine Datentransformation pro Event-Webhook einzurichten.

2. Um die Verbindung zu testen, tätigen Sie einen ausgehenden Anruf vom Regal Agent Desktop zu Ihrem Telefon und übermitteln Sie das Formular „Gesprächszusammenfassung“, um ein `call.completed`-Event zu erstellen.

3. Legen Sie fest, welche Bezeichner Sie für die Zuordnung Ihrer Regal-Kontakte zu Ihren Braze-Profilen verwenden möchten. Zu den verfügbaren Bezeichnern in Regal-Events gehören:
   - `userId` – nur bei Events gesetzt, wenn Sie diesen Bezeichner zuvor für einen Kontakt gesendet haben
   - `traits.phone`
   - `traits.email` – nur bei Events gesetzt, wenn Sie diesen Bezeichner zuvor für einen Kontakt gesendet haben

In Braze-zu-Regal-Event-Payloads empfiehlt Regal die Verwendung von `traits.phones`, um mehrere Telefonnummern und Einwilligungen auf Telefonnummernebene zu unterstützen. In Regal-Reporting-Events, die an Braze zurückgesendet werden, kann `traits.phone` weiterhin als Bezeichner in Event-Payloads erscheinen.

#### Von Braze unterstützte Bezeichner {#braze-supported-identifiers}
- Braze unterstützt keine Telefonnummern als Bezeichner. Um diese als Bezeichner zu verwenden, kann die Telefonnummer in Braze als [Nutzer-Alias]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) festgelegt werden.
- Bei der Verwendung von Braze-Datentransformation kann die E-Mail-Adresse als Bezeichner verwendet werden. Wenn die E-Mail-Adresse als Profil in Braze existiert, wird das bestehende Profil aktualisiert. Wenn die E-Mail-Adresse in Braze noch nicht existiert, wird ein reines E-Mail-Profil erstellt.

## Anwendungsfälle {#use-cases}

{% tabs %}
{% tab E-Mail triggern %}

**Eine E-Mail von Braze basierend auf einer Anrufdisposition in Regal triggern**

Nachfolgend sehen Sie einen Beispiel-Payload für ein `call.completed`-Event in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie eine Beispiel-Datentransformation, um dies einem angepassten Event in Braze zuzuordnen.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Profilattribute aktualisieren %}

**Profilattribute in Braze basierend auf `contact.attribute.edited`-Events von Regal aktualisieren**

Nachfolgend sehen Sie einen Beispiel-Payload für ein `contact.attribute.edited`-Event in Regal. Regal sendet dieses Event, wenn ein Agent während eines Gesprächs ein Attribut im Profil eines Kontakts aktualisiert.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie eine Beispiel-Datentransformation, um die neuen angepassten Eigenschaftswerte den entsprechenden Attributen in Ihren Braze-Profilen zuzuordnen:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Experimente synchron halten %}

**Halten Sie Ihre Experimente in Braze und Regal mithilfe von `contact.experiment.assigned`-Events synchron**

Nachfolgend sehen Sie einen Beispiel-Payload für ein `contact.experiment.assigned`-Event in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie eine Beispiel-Datentransformation, um dies einem angepassten Event in Braze zuzuordnen.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Kontakt abmelden %}

**Einen Kontakt in Braze basierend auf `contact.unsubscribed`-Events von Regal abmelden**

Nachfolgend sehen Sie einen Beispiel-Payload für ein `contact.unsubscribed`-Event in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Nachfolgend finden Sie eine Beispiel-Datentransformation, um den Kontakt in Braze abzumelden.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Follow-up aus Anrufanalyse triggern %}

**Maßgeschneiderte Follow-up-Journeys in Braze basierend auf `call.analysis.available`-Events von Regal triggern**

Verwenden Sie das `call.analysis.available`-Event von Regal, um den Hauptgrund zu identifizieren, warum eine Kund:in nicht konvertiert hat, und eine maßgeschneiderte Follow-up-Journey in Braze auszulösen.

Zum Beispiel:

- Wenn der Haupteinwand der Preis ist, eine wertorientierte Follow-up-E-Mail senden.
- Wenn der Haupteinwand das Timing ist, die Nutzer:in in eine Nurture-Sequenz für eine spätere Überlegung aufnehmen.
- Wenn der Haupteinwand Vertrauen ist, Testimonials, Bewertungen oder Compliance-Zusicherungen senden.
- Wenn `needs_human_agent` „true“ ist, ein Vertriebs- oder Support-Team benachrichtigen und weitere automatisierte Nachrichten unterdrücken.

Nachfolgend sehen Sie einen Beispiel-Payload für ein `call.analysis.available`-Event in Regal.

```json
{
  "traits": {
    "phone": "+1XXXXXXXXXX",
    "email": "xxx@gmail.com"
  },
  "name": "call.analysis.available",
  "brand": "circle-bank",
  "contact_email": "xxx@gmail.com",
  "contact_phone": "+1XXXXXXXXXX",
  "created_at": "1754079836",
  "entity_type": "event",
  "event_id": "9f5d8dbb2973b0e2359c6fd34111111",
  "event_type": "regal_voice_event",
  "external_id": "41dd1aa2-1111-f011-a2d5-00505611111",
  "original_timestamp": "1754079835",
  "profile_id": "62653af1111111173af128291e92",
  "properties": {
    "agent_email": "xxx@yourbrand.com",
    "call_analysis": {
      "purchase_intent": "medium",
      "primary_objection": "price",
      "secondary_objection": "needs_to_compare",
      "product_interest": "Life Insurance",
      "follow_up_required": true,
      "follow_up_email_text": "Thanks for speaking with us today. I know cost is top of mind, so I wanted to send over a simple summary of the life insurance options we discussed and what may fit your budget.",
      "recommended_next_action": "send_value_oriented_follow_up",
      "needs_human_agent": false,
      "customer_sentiment_label": "interested_but_hesitant"
    },
    "contact_phone": "+1XXXXXXXXXX",
    "incoming_sip_headers": {
      "Via": "SIP/2.0/UDP srv1.example.com;branch=z9hG4bK776asdhds",
      "From": "<sip:customer@example.com>;tag=1928301774",
      "Call-ID": "a84b4c76e66710"
    },
    "is_ai_agent": true,
    "outgoing_sip_headers": {
      "Via": "SIP/2.0/TCP srv2.example.com;branch=z9hG4bKgsdh7723",
      "To": "<sip:agent@yourbrand.com>",
      "User-Agent": "RegalVoiceAI/1.0"
    },
    "task_id": "WT7f3ea47fa6e6055aa847f0a62111111"
  },
  "originalTimestamp": "1754079835",
  "source": "Regal Voice"
}
```

Verwenden Sie eine Datentransformation, um `call_analysis`-Felder (wie `primary_objection` und `needs_human_agent`) auf angepasste Braze-Events oder Profilattribute abzubilden. Erstellen Sie dann Canvas- oder Campaign-Logik in Braze, die basierend auf diesen Werten verzweigt.

{% endtab %}
{% tab Anruftranskript-Links speichern %}

**Profilattribute mit Transkript-Links aus `call.transcript.available`-Events aktualisieren**

Verwenden Sie das `call.transcript.available`-Event, um einen Link zum vollständigen Anruftranskript an Braze zu senden. Ordnen Sie die Transkript-URL mithilfe der Datentransformation einem Braze-Nutzerprofil-Attribut zu, damit Ihr Team Gespräche direkt aus dem Nutzerprofil aufrufen und überprüfen kann.

Nachfolgend sehen Sie einen Beispiel-Payload für ein `call.transcript.available`-Event in Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625551796",
    "email": "xxx@gmail.com"
  },
  "name": "call.transcript.available",
  "properties": {
    "agent_email": "xxx@yourbrand.com",
    "task_id": "WT953358e8822dd9333fc38dfbac25e1e1",
    "call_summary": "The agent Zoe explained insurance options to Joe and he said he'll need to think about it before moving forward Agent politely ended the call.",
    "contact_name": "Joe Smith",
    "contact_phone": "+13523182825",
    "is_voicemail": false,
    "moments_count": 18,
    "recording_id": "RE0118052841b7299d0630d1dff610c1fb",
    "recording_link": "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Recordings/xxx.mp3",
    "recording_duration": 78.75987,
    "request_timestamp": 1657799128,
    "response_timestamp": 1657799136,
    "sentiments": {
      "contact_sentiment": 70,
      "agent_sentiment": 75,
      "agent_sentiment_reason": "Zoe was polite and attentive, effectively gathering information and providing a resource, which contributed to a positive interaction.",
      "contact_sentiment_reason": "Joe was satisfied with the information provided but may have wanted more assistance regarding insurance options."
    },
    "trackers": [
      {
        "tracker_id": "4be87957-9140-4451-894a-bdbaed1f2460",
        "tracker_name": "Refinance"
      },
      {
        "tracker_id": "eb2577c6-5e23-4c65-9e04-5cc5d49eee7e",
        "tracker_name": "High Intent"
      }
    ],
    "transcript": "[handling agent]: Hi Joe, this is Zoe with BrightCover Insurance. I'll be going over some insurance options with you today. [contact]: Sounds good. [handling agent]: Before we start, I'm going to transfer you to a specialist for a moment. One sec. [transfer agent]: Hi Joe, this is Mark. Just verifying a few details before sending you back to Zoe. [contact]: Okay. [handling agent]: Thanks, Joe. Based on what you shared, here are some plan options... [contact]: I'll need to think about it. [handling agent]: Totally understandable. Feel free to reach out anytime. Have a great day! END OF TRANSCRIPT",
    "transcript_is_truncated": false,
    "transcript_url": "https://app.regalvoice.com/transcripts/WT953358e8822dd9333fc38dfbac25e1e1"
  },
  "originalTimestamp": "1657843308",
  "eventSource": "Regal Voice",
  "eventId": "f49a3cf9cb1336683bd5f19dwe4c61147"
}
```

{% endtab %}
{% endtabs %}