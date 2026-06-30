---
nav_title: Nachrichten senden
article_title: Versenden von Nachrichten über die REST API
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt die beiden Möglichkeiten, Nachrichten mithilfe der Braze REST API programmgesteuert zu versenden."
---

# Versenden von Nachrichten über die REST API {#sending-messages-using-the-rest-api}

> Sie können Nachrichten in Echtzeit über zwei verschiedene Braze-Endpunkte von Ihrem Backend aus versenden. Jeder hat eine andere Anfragestruktur: Einer erfordert den vollständigen Nachrichteninhalt in der Anfrage, der andere erfordert eine Campaign-ID und sendet den im Dashboard definierten Inhalt.

Dieser Ansatz funktioniert mit jedem von der API unterstützten Messaging-Kanal (WhatsApp, E-Mail, SMS, Push, Content Cards, Webhooks und mehr).

## Zwei Möglichkeiten zum Versenden {#two-ways-to-send}

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) |
| --- | --- | --- |
| **Campaign-ID** | Optional. Lassen Sie sie weg, um ohne Dashboard-Campaign-Tracking zu senden, oder geben Sie eine API-Campaign-ID plus `message_variation_id` in jeder Nachricht an, um im Dashboard zu tracken. | Erforderlich. |
| **Nachrichteninhalt** | Sie müssen ein `messages`-Objekt in die Anfrage einfügen (zum Beispiel `messages.whats_app`, `messages.email`). | Nicht akzeptiert. Der Nachrichteninhalt wird in der Campaign im Braze-Dashboard definiert. |
| **Anwendungsfall** | Senden Sie eine Nachricht, deren Inhalt vollständig in der API-Anfrage angegeben ist. | Triggern Sie eine vorgefertigte Campaign (Inhalt im Dashboard) an bestimmte Empfänger:innen über die API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zwei Möglichkeiten zum Versenden" }

Ausführliche Informationen zu Anfragen und Antworten finden Sie in den Endpunkt-Referenzen [Nachrichten sofort senden (nur API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) und [Campaigns über API-gesteuerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

---

## Option 1: Senden mit Nachrichteninhalt in der Anfrage (`/messages/send`) {#option-1-send-with-message-content-in-the-request-messagessend}

Verwenden Sie diesen Endpunkt, wenn Sie den vollständigen Nachrichteninhalt in der API-Anfrage angeben möchten. Sie **müssen** ein `messages`-Objekt einfügen (zum Beispiel `messages.whats_app`, `messages.email` oder `messages.sms`). Sie können `campaign_id` weglassen, um ohne Campaign-Tracking zu senden, oder eine API-Campaign-ID und `message_variation_id` in jede Nachricht einfügen, um Sendungen im Dashboard zu verfolgen (weitere Informationen finden Sie in der [Endpunkt-Referenz]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)).

**Erforderlich:** API-Schlüssel mit der Berechtigung `messages.send`.

{% alert important %}
Alle Empfänger:innen in `external_user_ids` müssen bereits in Braze vorhanden sein. Um Nutzer:innen im Rahmen eines Versands zu erstellen, verwenden Sie zunächst [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder nutzen Sie [Option 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (API-gesteuerte Campaign).
{% endalert %}

### Beispiel: WhatsApp-Template-Nachricht {#example-whatsapp-template-message}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Die vollständige Spezifikation des WhatsApp-Objekts finden Sie unter [WhatsApp-Objekt]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object).

{% alert note %}
Der Endpunkt `/messages/send` unterstützt ausschließlich WhatsApp-Templates mit TEXT- oder IMAGE-Headern. Für die Header-Typen DOCUMENT, VIDEO oder andere Medien verwenden Sie den [API-gesteuerten Campaign-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) oder das Braze-Dashboard.
{% endalert %}

### Beispiel: E-Mail {#example-email}

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Für andere Kanäle siehe [Messaging-Objekte]({{site.baseurl}}/api/objects_filters#messaging-objects).

---

## Option 2: Eine Campaign mit Inhalten im Dashboard triggern (`/campaigns/trigger/send`) {#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend}

Verwenden Sie diesen Endpunkt, wenn der Nachrichteninhalt im Braze-Dashboard erstellt wird (API-gesteuerte Campaign). Sie senden eine **erforderliche** `campaign_id` und Empfänger:innen; Sie senden **kein** `messages`-Objekt.

**Erforderlich:** API-Schlüssel mit der Berechtigung `campaigns.trigger.send`.

### 1. Schritt: Eine API-gesteuerte Campaign erstellen {#step-1-create-an-api-triggered-campaign}

1. Gehen Sie im Braze-Dashboard zu **Messaging** > **Campaigns**.
2. Wählen Sie **Kampagne erstellen** und dann **API-gesteuerte Kampagne** (nicht „API-Kampagne“).
3. Fügen Sie Ihren Messaging-Kanal hinzu (WhatsApp, E-Mail, SMS usw.) und erstellen Sie den Nachrichteninhalt im Dashboard.
4. Notieren Sie sich die **Campaign-ID** (und die **Sende-ID**, falls Sie mehrere Nachrichtenvarianten verwenden). Sie werden diese in der API-Anfrage verwenden.

Weitere Informationen zum Erstellen von API-gesteuerten Campaigns finden Sie unter [API-gesteuerte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

### 2. Schritt: Die Campaign über die API triggern {#step-2-trigger-the-campaign-via-the-api}

Senden Sie eine POST-Anfrage an `/campaigns/trigger/send` mit `campaign_id` und `recipients` (oder `broadcast`/`audience`). Fügen Sie kein `messages`-Objekt ein – der Inhalt stammt aus der Campaign.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Den vollständigen Anfragetext (einschließlich `trigger_properties`, `send_to_existing_only`, `attributes` usw.) finden Sie in der Endpunkt-Referenz [Campaigns über API-gesteuerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body).

---

## Integration überprüfen {#verify-your-integration}

1. Senden Sie eine Anfrage über eine der oben genannten Optionen und geben Sie Ihre eigene Nutzer-ID als Empfänger:in an.
2. Bestätigen Sie, dass die Nachricht zugestellt wurde.
3. Bei Verwendung von Option 2 überprüfen Sie die Campaign im Braze-Dashboard, um sicherzustellen, dass der Versand aufgezeichnet wurde.

## Hinweise {#considerations}

- Nutzen Sie die [Personalisierungs-Features]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) von Braze, um Inhalte anzupassen, sofern dies unterstützt wird.
- Stellen Sie sicher, dass Ihr Messaging den geltenden Vorschriften entspricht und die erforderlichen Abmeldeoptionen sowie Datenschutzhinweise enthält.
- Weitere Endpunkte (Zeitplan, Canvas-Trigger usw.) finden Sie unter [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging).