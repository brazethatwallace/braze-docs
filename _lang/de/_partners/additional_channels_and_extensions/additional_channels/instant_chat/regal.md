---
nav_title: Regal
article_title: Regal
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Regal, einer Lösung für den Telefon- und SMS-Vertrieb, mit der Sie Daten aus beiden Quellen nutzen können, um personalisierte Erlebnisse für Ihre Kund:innen zu schaffen."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) ist die Lösung für den Telefon- und SMS-Vertrieb, mit der Sie mehr Gespräche führen und so Ihre Wachstumsziele deutlich schneller erreichen können.

Durch die Integration von Regal und Braze können Sie ein konsistenteres und personalisierteres Erlebnis an allen Ihren Kunden-Touchpoints schaffen.
- Senden Sie die nächstbeste E-Mail oder Push-Benachrichtigung von Braze auf Grundlage dessen, was in einem Telefongespräch auf Regal gesagt wurde.
- Lösen Sie einen Anruf in Regal aus, wenn eine hochwertige Kund:in auf eine Marketing-E-Mail von Braze klickt, aber nicht konvertiert.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Regal-Konto | Ein Regal-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Regal-API-Schlüssel | Ein Regal-API-Schlüssel ermöglicht das Senden von Events von Braze an Regal.<br><br>Senden Sie eine E-Mail an [support@regal.io](mailto:support@regal.io), um diesen Schlüssel zu erhalten. |
| Braze-Datentransformation | Die Datentransformation befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Customer-Success-Manager von Braze, wenn Sie an einer Teilnahme am Early Access interessiert sind. Dies ist erforderlich, um Daten von Regal zu empfangen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration: Daten von Braze an Regal senden {#integration-sending-data-from-braze-to-regal}

Im folgenden Abschnitt wird beschrieben, wie Sie Braze als Quelle verwenden, um Ihre Kundenprofil- und Event-Daten über Braze-Canvas- oder Campaign-Webhooks an Regal zu senden.

### 1. Schritt: Neue Kontakte in Regal erstellen {#step-1-create-new-contacts-in-regal}

Erstellen Sie ein Canvas oder eine Campaign, die jedes Mal einen Webhook an Regal sendet, wenn ein neuer Kontakt in Braze erstellt wird, der für Anrufe und SMS in Regal verfügbar sein soll.

1. Erstellen Sie ein Canvas oder eine Campaign mit dem Titel „Neuen Kontakt für Regal erstellen“ und wählen Sie **Aktionsbasiert** als Eingangstyp aus.

2. Legen Sie die Triggerlogik als **Angepasstes Event** fest und wählen Sie das Event aus, das ausgelöst wird, wenn ein Kontakt mit einer Telefonnummer angelegt wird. Regal empfiehlt außerdem, einen zusätzlichen Filter für das Telefonfeld hinzuzufügen, der sicherstellt, dass es gesetzt ist.

3. Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
   - **Webhook-URL**: <https://events.regalvoice.com/events>
   - **Anfragetext**: Rohtext

#### Anfrage-Header und Methode {#request-headers-and-method}

Regal.io erfordert außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paar im Tab **Einstellungen** im Template enthalten:
{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Anfragetext {#request-body}

Das einzige erforderliche Feld unten ist die Eigenschaft `traits.phone`. Der Rest ist optional. Wenn Sie jedoch `optIn` einschließen, müssen Sie `optIn.channel` und `optIn.subscribed` angeben.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

Das obige Payload-Beispiel geht davon aus, dass alle Ihre Kontakte dem Opt-in für Sprache und SMS zugestimmt haben. Wenn das nicht der Fall ist, können Sie die Eigenschaft `optIn` aus dem obigen Beispiel entfernen und ein separates Canvas oder eine Campaign einrichten, um einen Kontakt in Regal zu aktualisieren, wenn `optIn` erfasst wird.

### 2. Schritt: Opt-in-Informationen aktualisieren {#step-2-update-opt-in-information}

Wenn Opt-in und Opt-out an verschiedenen Stellen Ihres App-Erlebnisses stattfinden können, ist es wichtig, Regal zu aktualisieren, wenn Nutzer:innen sich an- oder abmelden. Nachfolgend finden Sie ein empfohlenes Canvas, um aktuelle Opt-in-Informationen an Regal zu senden. Es wird davon ausgegangen, dass Sie dies als Braze-Profilfeld speichern. Falls nicht, kann der Trigger genauso gut ein Event in Ihrem Braze-Konto sein, das ein Opt-in oder eine Abmeldung darstellt. (Das folgende Beispiel bezieht sich auf das Opt-in per Telefon, aber Sie können ein ähnliches Canvas oder eine Campaign für das Opt-in per SMS einrichten, wenn Sie diese separat erfassen.)

1. Erstellen Sie ein neues Canvas oder eine Campaign mit dem Titel „Opt-in oder Opt-out an Regal senden“.

2. Wählen Sie eine der folgenden Trigger-Optionen und wählen Sie das Feld aus, das den Opt-in-Status der Nutzer:innen darstellt. Wenn Sie ein Event an Braze senden, das ein Opt-in oder Opt-out darstellt, verwenden Sie stattdessen dieses Event als Trigger.
    - Nutzerprofilfeld aktualisiert
    - Abo-Gruppenstatus aktualisieren
    - Abostatus

3. Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
   - **Webhook-URL**: <https://events.regalvoice.com/events>
   - **Anfragetext**: Rohtext

#### Anfrage-Header und Methode

Regal.io erfordert außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paar im Template enthalten, und zwar im Tab **Einstellungen**:
{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Anfragetext

Sie können gerne weitere Nutzerprofil-Attribute in diesen Payload aufnehmen, wenn Sie sicherstellen möchten, dass mehrere Attribute gleichzeitig auf dem neuesten Stand sind.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### 3. Schritt: Angepasste Events senden {#step-3-send-custom-events}

Richten Sie abschließend ein Canvas oder eine Campaign für jedes wichtige Event ein, das Sie an Regal senden möchten. Regal empfiehlt, alle Events zu senden, die für das Triggern von SMS und Anrufen in Regal wichtig sind (z. B. ein Event bei jedem Schritt des Anmelde- oder Kaufprozesses) oder die als Ausstiegskriterium für Kontakte verwendet werden, die aus Regal-Campaigns herausfallen sollen.

Nachfolgend sehen Sie beispielsweise einen Workflow, bei dem Regal ein Event erhält, wenn Nutzer:innen den ersten Schritt eines Antrags abschließen.

1. Erstellen Sie ein neues Canvas oder eine neue Campaign mit dem Titel „Antrag Schritt 1 abgeschlossen – Event an Regal senden“.

2. Legen Sie die Logik des Triggerknotens als **Angepasstes Event** fest und wählen Sie den Namen des Events aus, das Sie an Regal senden möchten, z. B. „Application Step 1 Completed“.

3. Füllen Sie in Ihrem neuen Webhook-Template die folgenden Felder aus:
   - **Webhook-URL**: <https://events.regalvoice.com/events>
   - **Anfragetext**: Rohtext

#### Anfrage-Header und Methode

Regal.io erfordert außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paar im Template enthalten, und zwar im Tab **Einstellungen**:
{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Anfragetext

Sie können gerne weitere Nutzerprofil-Attribute in diesen Payload aufnehmen, wenn Sie sicherstellen möchten, dass mehr Attribute gleichzeitig aktuell sind.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### Aktuelle Kontaktattribute {#up-to-date-contact-attributes}

Es ist zwar nicht zwingend erforderlich, aber Regal empfiehlt, auch alle wichtigen Nutzerprofil-Datenfelder in den Event-Payloads Ihrer Event-Workflows mitzusenden, um sicherzustellen, dass Regal Zugriff auf die aktuellsten Kontaktattribute hat, wenn wichtige Events verfügbar werden.

{% alert note %}
Wenn Sie Fragen dazu haben, welche Events wichtig sind, um sie an Regal zu senden, oder wie Sie diese Canvases und Campaigns am besten einrichten, wenden Sie sich an support@regal.io.
{% endalert %}

## Integration: Daten von Regal an Braze senden {#integration-sending-data-from-regal-to-braze}

In diesem Abschnitt wird beschrieben, wie Sie Regal-Reporting-Events wie `SMS.sent` und `call.completed` in Braze übertragen, damit sie in Ihren Braze-Profilen erscheinen und im Segmentierungs-Tool, in Canvas und in Campaigns verfügbar sind. Diese Integration verwendet Regal Reporting Webhooks und Braze-Datentransformation, um den Datenfluss zu automatisieren.

### 1. Schritt: Eine Datentransformation in Braze erstellen {#step-1-create-a-data-transformation-in-braze}

{% alert important %}
Die Datentransformation befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Customer-Success-Manager von Braze, wenn Sie an einer Teilnahme am Early Access interessiert sind.
{% endalert %}

Braze empfiehlt, eine Transformation pro Regal-Webhook zu erstellen, den Sie an Braze senden möchten.

So erstellen Sie eine Datentransformation:
1. Navigieren Sie zur Seite **Transformationen** in Ihrem Braze-Dashboard.
2. Geben Sie Ihrer Transformation einen Namen und klicken Sie auf **Transformation erstellen**.
3. Klicken Sie in der Liste der Transformationen auf <i class="fa-solid fa-ellipsis-vertical" title="Aktionen anzeigen"></i> und wählen Sie **Webhook-URL kopieren**.

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
Derzeit gibt es keine Wiederholungsversuche für diese Events. Wenn innerhalb von 5 Sekunden keine Antwort eingeht, wird das Event verworfen und nicht erneut versucht. Regal wird in einer zukünftigen Version Wiederholungsversuche hinzufügen.
#### Events
Der Leitfaden [Reporting Webhooks von Regal](https://developer.regal.io/docs/reporting-webhooks#events) enthält die vollständige Liste der von Regal veröffentlichten Reporting-Events. Dort finden Sie auch Definitionen von Eigenschaften und Beispiel-Payloads.

### 3. Schritt: Regal-Events in Braze-Events transformieren {#step-3-transform-regal-events-into-braze-events}

Mit dem Feature [Datentransformation]({{site.baseurl}}/data_transformation/) von Braze können Sie eingehende Regal-Events in das Format abbilden, das erforderlich ist, um sie als Attribute, Events oder Käufe in Braze hinzuzufügen.

1. Benennen Sie Ihre Datentransformation. Es wird empfohlen, eine Datentransformation pro Event-Webhook einzurichten.

2. Um die Verbindung zu testen, tätigen Sie einen ausgehenden Anruf vom Regal Agent Desktop zu Ihrem Mobiltelefon und übermitteln Sie das Formular „Gesprächszusammenfassung“, um ein `call.completed`-Event zu erstellen.

3. Legen Sie fest, welche Bezeichner Sie für die Zuordnung Ihrer Regal-Kontakte zu Ihren Braze-Profilen verwenden möchten. Zu den verfügbaren Bezeichnern in Regal-Events gehören:
   - `userId` – nur bei Events gesetzt, wenn Sie diesen Bezeichner zuvor für einen Kontakt gesendet haben
   - `traits.phone`
   - `traits.email` – nur bei Events gesetzt, wenn Sie diesen Bezeichner zuvor für einen Kontakt gesendet haben

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

Nachfolgend sehen Sie einen Beispiel-Payload für ein `contact.attribute.edited`-Event in Regal. Dieses Event wird jedes Mal ausgelöst, wenn einer Ihrer Agenten in einem Gespräch etwas Neues erfährt und ein Attribut im Profil des Kontakts aktualisiert.

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

**Einen Kontakt in Braze basierend auf einem `contact.unsubscribed`-Event von Regal abmelden**

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
{% endtabs %}