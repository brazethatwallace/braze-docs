---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Erfahren Sie, wie Sie Zendesk Chat mit Braze integrieren und eine beidseitige SMS-Konversation einrichten können."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat](https://www.zendesk.com/service/messaging/) verwendet Webhooks von jeder Plattform, um eine beidseitige SMS-Konversation einzurichten. Wenn Nutzer:innen Support anfordern, wird ein Ticket in Zendesk erstellt. Die Antworten der Agenten werden über eine API-getriggerte SMS-Campaign an Braze weitergeleitet, und die Antworten der Nutzer:innen werden an Zendesk zurückgesendet.

## Voraussetzungen {#prerequisites}


| Voraussetzung | Beschreibung |
|---|---|
| Ein Zendesk-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zendesk-Konto. |
| Ein Zendesk Basic Authorization Token | Ein Zendesk Basic Authorization Token wird verwendet, um eine ausgehende Webhook-Anfrage von Braze an Zendesk zu stellen. |
| Ein Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `campaigns.trigger.send`-Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Verbessern Sie die Effizienz des Kundensupports, indem Sie die SMS-Funktionen von Braze mit den Antworten von Zendesk-Live-Agenten kombinieren, um Nutzer:innen bei Anfragen umgehend mit menschlichem Support zu unterstützen.

## Integration von Zendesk Chat {#integrating-zendesk-chat}

### 1. Schritt: Erstellen Sie einen Webhook in Zendesk {#step-1-create-a-webhook-in-zendesk}

1. Gehen Sie in der Zendesk-Entwicklungskonsole zu Webhooks: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. Wählen Sie unter **Create Webhook** die Option **Trigger or automation** aus.
3. Fügen Sie als **Endpoint URL** den Endpunkt **/campaign/trigger/send** hinzu.
4. Wählen Sie unter **Authentication** die Option **Bearer Token** aus und fügen Sie den Braze REST-API-Schlüssel mit den Berechtigungen `campaigns.trigger.send` hinzu.

![Ein Beispiel für einen Zendesk-Webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### 2. Schritt: Erstellen Sie eine ausgehende SMS-Campaign {#step-2-create-an-outbound-sms-campaign}

Als Nächstes erstellen Sie eine SMS-Campaign, die auf Webhooks von Zendesk wartet und eine angepasste SMS-Antwort an Ihre Kund:innen sendet.

#### Schritt 2.1: Verfassen Sie Ihre Nachricht {#step-21-compose-your-message}

Wenn Zendesk den Inhalt einer Nachricht über die API sendet, hat dieser das folgende Format:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Wir müssen also die gewünschten Details aus diesem String extrahieren, um sie in der Nachricht anzuzeigen – andernfalls sehen Nutzer:innen alle Details.

![Eine Beispiel-SMS ohne Formatierung.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

Fügen Sie in das Textfeld **Message** den folgenden Liquid-Code sowie eine Opt-out-Sprache oder andere statische Inhalte ein:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk:
{{msg[2]}}

Feel free to respond directly to this number!
```
{% endraw %}

![Eine Beispiel-SMS mit Formatierung.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### Schritt 2.2: Zeitplan für die Zustellung {#step-22-schedule-the-delivery}

Wählen Sie als Zustellungsart **API-Triggered delivery** aus und kopieren Sie dann die Campaign-ID, die in den nächsten Schritten verwendet wird.

![API-getriggerte Zustellung]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

Aktivieren Sie abschließend unter **Delivery Controls** die Wiederzulassung.

![Wiederzulassung unter „Delivery Controls“ aktiviert.]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### 3. Schritt: Erstellen Sie einen Trigger in Zendesk, um Antworten von Agenten an Braze weiterzuleiten {#step-3-create-a-trigger-in-zendesk-to-forward-agent-replies-to-braze}

Gehen Sie zu **Objects and rules** > **Business rules** > **Triggers**.

1. Erstellen Sie eine neue **Kategorie** (z. B. **Trigger a message**).
2. Erstellen Sie einen neuen **Trigger** (z. B. **Respond via SMS Braze**).
3. Wählen Sie unter **Conditions**:
- **Ticket>Comment** ist **Present and requester can see comment**, sodass die Nachricht immer dann getriggert wird, wenn ein neuer öffentlicher Kommentar in einem Ticket-Update enthalten ist
- **Ticket>Update** *ist nicht* **Web service (API)**, sodass eine Nachricht, die Nutzer:innen von Braze aus senden, nicht an ihr Mobiltelefon zurückgeleitet wird. Es werden nur Nachrichten weitergeleitet, die von Zendesk stammen.

![Respond via SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

Wählen Sie unter **Actions** die Option **Notify by Webhook** aus und wählen Sie den Endpunkt, den Sie in [Schritt 1](#step-1-create-a-webhook-in-zendesk) erstellt haben. Geben Sie als Nächstes den Body des API-Aufrufs an. Tragen Sie die `campaign_id` aus [Schritt 2.2](#step-22-schedule-the-delivery) in den Anfrage-Body ein.

![Respond via SMS Braze – JSON-Body.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### 4. Schritt: Erstellen Sie einen Trigger in Zendesk, um Nutzer:innen zu aktualisieren, wenn ein Ticket geschlossen wird {#step-4-create-a-trigger-in-zendesk-to-update-a-user-when-a-ticket-is-closed}

Wenn Sie Nutzer:innen benachrichtigen möchten, dass das Ticket geschlossen wurde, erstellen Sie in Braze eine neue Campaign mit dem Template für den Antwort-Body.

![Nutzer:innen aktualisieren, wenn ein Ticket geschlossen wird.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

Wählen Sie **API-Triggered delivery** und kopieren Sie die Campaign-ID.

Richten Sie als Nächstes einen Trigger ein, der Braze benachrichtigt, wenn das Ticket geschlossen wird:
- Kategorie: **Trigger a message**
- Wählen Sie unter Bedingungen **Ticket>Ticket Status** und ändern Sie ihn in **Solved**

![Gelöstes Ticket in Zendesk einrichten.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

Wählen Sie unter **Actions** die Option **Notify by Webhook** aus und wählen Sie den zweiten Endpunkt, den Sie gerade erstellt haben. Von dort aus müssen Sie den Body des API-Aufrufs angeben:

![JSON-Body für gelöstes Ticket.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### 5. Schritt: Angepasstes Nutzerfeld in Zendesk hinzufügen {#step-5-add-a-custom-user-field-in-zendesk}

Wählen Sie im Admin Center in der Seitenleiste **People** und dann **Configuration** > **User fields**. Fügen Sie das angepasste Nutzerfeld `braze_external_id` hinzu.

### 6. Schritt: Eingehende SMS-Weiterleitung einrichten {#step-6-set-up-inbound-sms-forwarding}

Als Nächstes erstellen Sie zwei neue Webhook-Campaigns in Braze, damit Sie eingehende SMS von Kund:innen an den Zendesk-Posteingang weiterleiten können.

| Campaign | Zweck |
|--------------------|--------------------------------------------------------------------------------------|
| Webhook-Campaign 1 | Erstellt ein neues Ticket in Zendesk. |
| Webhook-Campaign 2 | Leitet alle konversationellen SMS-Antworten weiter, die eingehend von Kund:innen an Zendesk gesendet werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 6: Eingehende SMS-Weiterleitung einrichten" }

#### Schritt 6.1: Erstellen Sie eine SMS-Schlüsselwortkategorie {#step-61-create-an-sms-keyword-category}

Gehen Sie im Braze-Dashboard auf **Audience**, wählen Sie Ihre **SMS subscription group** und wählen Sie dann **Add Custom Keyword**. Füllen Sie die folgenden Felder aus, um eine exklusive SMS-Schlüsselwortkategorie für Zendesk zu erstellen.

| Feld | Beschreibung |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Keyword Category | Der Name Ihrer Schlüsselwortkategorie, z. B. `ZendeskSMS1`. |
| Keywords | Ihre angepassten Schlüsselwörter, z. B. `SUPPORT`. |
| Reply Message | Die Nachricht, die gesendet wird, wenn ein Schlüsselwort erkannt wird, z. B. „Ein Kundenservice-Mitarbeiter wird sich in Kürze bei Ihnen melden.“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 6.1: Erstellen Sie eine SMS-Schlüsselwortkategorie" }

![Ein Beispiel für eine SMS-Schlüsselwortkategorie in Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### Schritt 6.2: Erstellen Sie Ihre erste Webhook-Campaign {#step-62-create-your-first-webhook-campaign}

Erstellen Sie im Braze-Dashboard Ihre erste Webhook-Campaign. Diese Nachricht signalisiert Zendesk, dass Support angefragt wird.

Füllen Sie im Webhook-Composer die folgenden Felder aus:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP Method: POST
- Request Headers:
- Content-Type: application/json
- Authorization: Basic {{Token}}
- Request Body:

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Eine Beispielanfrage mit den beiden erforderlichen Headern.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### Schritt 6.3: Zeitplan für die erste Zustellung {#step-63-schedule-the-first-delivery}

Wählen Sie für **Schedule Delivery** die Option **Action-Based Delivery** aus und wählen Sie dann als Trigger-Typ **Send an SMS Inbound Message**. Fügen Sie außerdem die SMS-Abo-Gruppe und die Schlüsselwortkategorie hinzu, die Sie zuvor eingerichtet haben.

![Die Seite „Schedule Delivery“ für die erste Webhook-Campaign.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

Aktivieren Sie unter **Delivery Controls** die Wiederzulassung.

![Wiederzulassung unter „Delivery Controls“ für die erste Webhook-Campaign ausgewählt.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### Schritt 6.4: Erstellen Sie Ihre zweite Webhook-Campaign {#step-64-create-your-second-webhook-campaign}

Richten Sie eine Webhook-Campaign ein, um verbleibende SMS-Nachrichten von Nutzer:innen an Zendesk weiterzuleiten:

Da Zendesk die Ticket-ID als String sendet, erstellen Sie einen Content-Block, um den String in eine Ganzzahl umzuwandeln, damit Sie ihn im Zendesk-Webhook verwenden können.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Im Webhook-Composer:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Request: PUT
- KVPs:
    - Content-Type: application/JSON
    - Authorization: Basic {{Token}}

Beispiel-Body:

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Schritt 6.5: Einrichtung der zweiten Webhook-Campaign abschließen {#step-65-complete-second-webhook-campaign-setup}
- Richten Sie einen aktionsbasierten Trigger für Nutzer:innen ein, die eine eingehende Nachricht in der Kategorie „Other“ senden.
- Legen Sie Kriterien für die Wiederzulassung fest.
- Fügen Sie die entsprechenden Zielgruppen hinzu (in diesem Fall ist das angepasste Attribut **zendesk_ticket_open** auf **true** gesetzt).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}