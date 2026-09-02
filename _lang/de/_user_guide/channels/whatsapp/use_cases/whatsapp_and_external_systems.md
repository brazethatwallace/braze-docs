---
nav_title: "WhatsApp und externe Systeme"
article_title: "WhatsApp und externe Systeme"
page_order: 2
description: "Dieser Referenzartikel bietet eine Schritt-für-Schritt-Anleitung für die Integration von Braze und WhatsApp mit einem externen KI- oder Kommunikationssystem."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Braze und WhatsApp mit einem externen KI- oder Kommunikationssystem integrieren {#integrate-braze-and-whatsapp-with-an-external-ai-or-communication-system}

> Nutzen Sie die Leistungsfähigkeit von KI-Chatbots und Live-Agent-Übergaben auf dem WhatsApp-Kanal, um Ihren Kundensupport zu optimieren. Durch die Automatisierung von Routineanfragen und die nahtlose Übergabe an menschliche Mitarbeitende bei Bedarf können Sie die Antwortzeiten erheblich verbessern und das gesamte Kundenerlebnis steigern.

## Voraussetzungen {#prerequisites}

| Anforderungen | Beschreibung |
| - | - |
| Externes System | Ein KI- oder Kommunikationssystem eines Drittanbieters, das in der Lage ist, Chatbots und automatisierte Kundenservice-Systeme über APIs zu erstellen und zu verwalten, oder beides. |
| Braze- und WhatsApp-Integration | Eine von Braze verwaltete WhatsApp-Nummer |
| Braze-REST-API-Schlüssel | Ein REST-API-Schlüssel mit `campaigns.trigger.send`-Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## So funktioniert es {#how-it-works}

Die Integration zwischen Braze und dem externen KI- oder Kommunikationssystem funktioniert als Zweibahnstraße, wobei Braze der Kommunikationskanal ist und das externe System die „Intelligenz“, die Nachrichten verarbeitet und Antworten formuliert.

Der Integrations-Workflow lässt sich in zwei zentrale Abläufe unterteilen:
**Eingehender Ablauf:** Die Nachricht einer Nutzerin oder eines Nutzers trifft in Braze ein und wird dann zur Verarbeitung an Ihr externes System weitergeleitet.
**Ausgehender Ablauf:** Nach der Verarbeitung der Nachricht sendet Ihr externes System eine Antwort an Braze, das die Nachricht dann an die Endnutzer:in zustellt.

Um diese Kommunikation effizient zu automatisieren, nutzt diese Integration zwei zentrale Braze-Features: [Webhook-Campaigns]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) und [API-getriggerte Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

![Architektur der Integration zwischen dem Braze-WhatsApp-Kanal und einem externen System.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
## Integration konfigurieren {#configuring-the-integration}

### 1. Schritt: Webhook-Campaign für eingehende Nachrichten erstellen {#step-1-create-a-webhook-campaign-for-inbound-messages}

Erstellen Sie zunächst eine Webhook-Campaign, um eine Möglichkeit zu schaffen, von Braze empfangene WhatsApp-Nachrichten an Ihr externes System zu senden.

1. Erstellen Sie in Braze eine Webhook-Campaign.
2. Wählen Sie im Webhook-Editor **Compose webhook** aus.
3. Geben Sie im Feld **Webhook URL** den API-Endpunkt (URL) für das externe System ein, das die Nachricht empfangen soll.
4. Wählen Sie **Raw text** für den Anfrage-Body und geben Sie einen Payload mit Personalisierung ein, der die `external_id` und Telefonnummer der Nutzerin oder des Nutzers, den Nachrichteninhalt und andere relevante Informationen enthält, wie zum Beispiel:

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5. Wählen Sie im Schritt **Schedule Delivery** Ihres Campaign-Editors **Action-Based** als Zustellungstyp und **Send a WhatsApp inbound message** als Campaign-Trigger.

![Aktionsbasierte Zustellung mit einem Trigger zum Senden einer eingehenden WhatsApp-Nachricht.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. Schließen Sie die Erstellung Ihrer Campaign ab, speichern und starten Sie sie. Nach dem Start der Campaign sendet Braze jedes Mal, wenn eine Nachricht empfangen wird, einen Webhook an Ihr externes System.

### 2. Schritt: API-getriggerte Campaign für ausgehende Nachrichten erstellen {#step-2}

Erstellen Sie als Nächstes eine API-getriggerte Campaign, um Ihrem externen System eine Möglichkeit zu geben, Nachrichten über WhatsApp an Nutzer:innen zurückzusenden.

1. Erstellen Sie in Braze eine WhatsApp-Campaign.
2. Wählen Sie im Nachrichten-Editor entweder **WhatsApp Template Message** oder **Response Message** und dann das Template oder das Layout der Antwortnachricht aus. Sie können jedes Layout für Antwortnachrichten auswählen, da die eingehende Nachricht das 24-Stunden-WhatsApp-Fenster geöffnet hat.

![Nachrichten-Editor mit Optionen zur Auswahl des Nachrichtentyps und des Nachrichtenlayouts.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3. Fügen Sie die API-Trigger-Eigenschaft zum Nachrichtentext hinzu, wie zum Beispiel {% raw %}`{{api_trigger_properties.${external_system_msg+body}}}`{% endraw %}. Dadurch kann Ihr KI-System die zu sendende Nachricht befüllen.

![Nachrichten-Editor mit Nachrichtentext, der Trigger-Eigenschaften enthält.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. Wählen Sie im Schritt **Schedule Delivery** Ihres Campaign-Editors **Action-Based** als Zustellungstyp.
5. Speichern Sie die Campaign und notieren Sie sich die eindeutige `campaign_id`, die Braze für diese Campaign generiert. Sie benötigen die ID für den nächsten Schritt.

### 3. Schritt: Das externe System mit der API-getriggerten Campaign verbinden {#step-3-connect-the-external-system-to-the-api-triggered-campaign}

Konfigurieren Sie abschließend Ihr externes System so, dass es Braze aufruft und die Antwort sendet.

1. Führen Sie im Code Ihres externen Systems nach der Verarbeitung der empfangenen Nachricht und der Generierung der Antwort eine POST-Anfrage an den Braze-Endpunkt `/messages/send` durch.
2. Fügen Sie im Body der `/messages/send`-Anfrage die `campaign_id` aus [Schritt 2](#step-2), die `external_id` der Nutzerin oder des Nutzers und den Inhalt der Antwort des externen Systems ein.
3. Verwenden Sie die API-Trigger-Eigenschaft aus [Schritt 2](#step-2), um die Antwort des externen Systems einzufügen, und vergessen Sie nicht, Ihren API-Schlüssel im Anfrage-Header zur Authentifizierung anzugeben, wie in diesem cURL-Beispiel:

{% raw %}
```bash
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

Jetzt haben Sie eine solide Grundlage für den Aufbau eines KI-Chatbot-Workflows!

### Ihren Workflow anpassen {#customizing-your-workflow}

Sie können Ihre Integrationslogik erweitern, um:
- Verschiedene Schlüsselwörter zu verwenden, um unterschiedliche Webhook-Campaigns zu triggern.
- Komplexere Konversationsabläufe mit mehrstufigen API-getriggerten Campaigns zu erstellen.
- Chat-Informationen in Braze als angepasste Attribute zu speichern, um das Kundenprofil anzureichern und zukünftige Campaigns zu segmentieren.