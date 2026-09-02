---
nav_title: Kurzmitteilungsdienst or SMS-Nachrichten senden
article_title: Versenden von Kurzmitteilungsdienst or SMS-Nachrichten über die Representational State Transfer API
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Kurzmitteilungsdienst or SMS-Nachrichten mithilfe der Braze Representational State Transfer API und einer API-Kampagne versenden können."
channel:
  - SMS
---

# Versenden von Kurzmitteilungsdienst or SMS-Nachrichten über die Representational State Transfer API {#sending-sms-messages-using-the-rest-api}

> Verwenden Sie die Braze Representational State Transfer API, um Transaktions-Kurzmitteilungsdienst or SMS-Nachrichten in Echtzeit von Ihrem Backend aus zu versenden. Mit diesem Ansatz können Sie einen Dienst erstellen, der Kurzmitteilungsdienst or SMS-Nachrichten programmgesteuert versendet und gleichzeitig die Zustellungs-Analytics zusammen mit Ihren anderen Campaigns und Canvase im Braze-Dashboard verfolgt.

Dies kann insbesondere für transaktionsbasiertes Messaging mit hohem Volumen nützlich sein, bei dem der Inhalt in Ihren Backend-Systemen definiert ist. Sie können beispielsweise Verbraucher:innen benachrichtigen, wenn sie eine Nachricht von einer anderen Nutzer:in erhalten, und sie einladen, Ihre Website zu besuchen und ihren Posteingang zu überprüfen.

Mit diesem Ansatz können Sie:

- Kurzmitteilungsdienst or SMS-Nachrichten in Echtzeit von Ihrem Backend aus Trigger or triggern or triggern.
- Analytics-Daten zusammen mit all Ihren Marketing-Campaigns und Canvase verfolgen.
- Den Anwendungsfall mit zusätzlichen Braze-Features wie Nachrichtenverzögerungen, Follow-up-Retargeting und A/B-Tests erweitern.
- Optional zur [API-gesteuerten Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) wechseln, um Ihre Nachrichten-Templates im Braze-Dashboard zu definieren, während Sie den Versand weiterhin über Ihr Backend Trigger or triggern or triggern.

Um eine Kurzmitteilungsdienst or SMS-Nachricht über die Representational State Transfer API zu versenden, müssen Sie im Braze-Dashboard eine API-Kampagne einrichten und anschließend den [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)-Endpunkt verwenden, um die Nachricht zu versenden.

## Voraussetzungen {#prerequisites}

Um diese Anleitung abzuschließen, benötigen Sie:

| Anforderung | Beschreibung |
| --- | --- |
| Braze Representational State Transfer-API-Schlüssel | Ein Schlüssel mit der Berechtigung `messages.send`. Um einen zu erstellen, navigieren Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**. |
| Kurzmitteilungsdienst or SMS-Abo-Gruppe | Eine in Ihrem Braze-Workspace konfigurierte Kurzmitteilungsdienst or SMS-Abo-Gruppe. |
| Backend-Dienst | Ein Backend-Dienst oder eine Skriptumgebung, die HTTP-POST-Anfragen an die Braze Representational State Transfer API senden kann. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## 1. Schritt: Erstellen Sie eine API-Kampagne {#step-1-create-an-api-campaign}

1. Gehen Sie im Braze-Dashboard zu **Messaging** > **Campaigns**.
2. Wählen Sie **Kampagne erstellen** und anschließend **API-Kampagnen**.
3. Geben Sie einen Namen und eine Beschreibung für Ihre Kampagne ein, beispielsweise „Kurzmitteilungsdienst or SMS-Benachrichtigung“.
4. Fügen Sie relevante Tags zur Identifizierung und zum Tracking hinzu.
5. Wählen Sie **Messaging-Kanal hinzufügen** und anschließend **Kurzmitteilungsdienst or SMS**.
6. Notieren Sie sich die **Campaign-ID** und die **Message-Variation-ID**, die auf der Kampagnenseite angezeigt werden. Sie benötigen beide Werte, um Ihre API-Anfrage zu erstellen.

## 2. Schritt: Senden Sie eine Kurzmitteilungsdienst or SMS-Nachricht über die API {#step-2-send-an-sms-message-using-the-api}

Erstellen Sie eine POST-Anfrage an den [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)-Endpunkt. Geben Sie die Campaign-ID, die externe Nutzer-ID der Empfänger:in und den Kurzmitteilungsdienst or SMS-Inhalt in der Anfrage-Payload an.

{% alert important %}
Jede in `external_user_ids` referenzierte Empfänger:in muss bereits in Braze vorhanden sein. API-only-Sends erstellen keine neuen Nutzerprofile. Wenn Sie im Rahmen eines Versands Nutzer:innen anlegen müssen, verwenden Sie zunächst [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder alternativ eine [API-gesteuerte Kampagne]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).
{% endalert %}

### Beispielanfrage {#example-request}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Ersetzen Sie `YOUR_REST_ENDPOINT` durch die [Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/api/basics#endpoints) für Ihren Workspace.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Ersetzen Sie die Platzhalterwerte durch Ihre tatsächlichen IDs. Das Feld `body` unterstützt [Liquid-Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), sodass Sie den Inhalt der Nachricht individuell an jede Empfänger:in anpassen können. Die vollständige Liste der vom Kurzmitteilungsdienst or SMS-Messaging-Objekt unterstützten Parameter finden Sie unter [Kurzmitteilungsdienst or SMS-Objekt]({{site.baseurl}}/api/objects_filters/messaging/sms_object).

Nachdem Sie die Anfrage erstellt haben, senden Sie die POST-Anfrage von Ihrem Backend-Dienst an die Braze Representational State Transfer API.

## 3. Schritt: Überprüfen Sie Ihre Integration {#step-3-verify-your-integration}

Überprüfen Sie nach Abschluss der Einrichtung Ihre Integration:

1. Senden Sie eine API-Anfrage wie in [Schritt 2](#step-2-send-an-sms-message-using-the-api) beschrieben und verwenden Sie dabei Ihre eigene Nutzer-ID als Empfänger:in.
2. Bestätigen Sie, dass die Kurzmitteilungsdienst or SMS-Nachricht auf Ihrem Telefon zugestellt wurde.
3. Gehen Sie im Braze-Dashboard zur Seite mit den Kampagnenergebnissen und überprüfen Sie, ob der Versand aufgezeichnet wurde.
4. Überwachen Sie die Ergebnisse sorgfältig, während Sie Ihre Kampagne skalieren.

## Hinweise {#considerations}

- Stellen Sie sicher, dass Ihre Kurzmitteilungsdienst or SMS-Kampagnen den geltenden Vorschriften und Anforderungen der Netzbetreiber entsprechen. Fügen Sie in jede Nachricht eine Abmeldeanweisung ein (z. B. „Senden Sie STOP, um sich abzumelden“). Weitere Informationen finden Sie unter [Kurzmitteilungsdienst or SMS-Gesetze und -Vorschriften]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) sowie [Opt-in- und Opt-out-Schlüsselwörter]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout).
- Nutzen Sie die [Personalisierungs-Features]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) von Braze, um Kurzmitteilungsdienst or SMS-Inhalte individuell auf einzelne Verbraucher:innen zuzuschneiden, einschließlich dynamischem Content und nutzerspezifischen Daten.
- Die Braze Representational State Transfer API bietet zusätzliche [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) für die Zeitplanung von Nachrichten, das Trigger or triggern or triggern von Kampagnen und vieles mehr.