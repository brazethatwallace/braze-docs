---
nav_title: Kampagnenbenachrichtigungen
article_title: Kampagnenbenachrichtigungen
page_order: 6

page_type: reference
description: "Dieser Referenzartikel gibt eine Übersicht über Kampagnenbenachrichtigungen, ihre Vorteile und wie Sie diese einrichten, damit Sie stets beruhigt sein können."
tool: Campaigns
channel:
- email
- webhooks

---

# Kampagnenbenachrichtigungen {#campaign-alerts}

> Wir möchten Sie benachrichtigen, wenn etwas nicht ganz wie erwartet läuft, und Ihnen die Gewissheit geben, dass alles reibungslos funktioniert. Schwellenwert-Benachrichtigungen für Kampagnen sorgen für Sicherheit – erfahren Sie als Erste:r, wenn eine wichtige Kampagne mehr oder weniger Nachrichten sendet als erwartet.

Kampagnenbenachrichtigungen sind für die folgenden Kampagnen verfügbar:

- Wiederkehrende geplante Kampagnen
- Aktionsbasierte Kampagnen
- API-getriggerte Kampagnen

## Ihre Kampagnenbenachrichtigung einrichten {#setting-up-your-campaign-alert}

Navigieren Sie zur Analytics-Seite Ihrer Kampagne, um mit der Einrichtung Ihrer Benachrichtigung zu beginnen. Wenn Sie **Benachrichtigung einrichten** auswählen, können Sie obere und untere Schwellenwerte sowie die Empfänger:innen und Kanäle für die Benachrichtigung festlegen.

![Dialogfeld für Kampagnenüberwachung mit zwei Buttons: „Abbrechen“ und „Speichern“.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Für eine geplante wiederkehrende Kampagne können Sie obere und untere Schwellenwerte für die Nachrichten festlegen, die bei jedem Versand der Kampagne gesendet werden. Für eine getriggerte Kampagne können Sie obere und untere Schwellenwerte für die Anzahl der stündlich und täglich gesendeten Nachrichten festlegen.

Sie können eine E-Mail-Benachrichtigung, eine Webhook-Benachrichtigung oder beides einrichten. Webhook-Benachrichtigungen können sehr nützlich sein, da sie es Ihnen ermöglichen, eine Benachrichtigung an einen Slack-Kanal zu senden. Weitere Informationen zur Integration von Kampagnenbenachrichtigungen mit Slack finden Sie in der Slack-Dokumentation unter [Sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

{% alert note %}
Wenn Sie Kampagnenbenachrichtigungen für zukünftige Kampagnen einrichten, erhalten Sie möglicherweise Updates, bevor die Kampagne startet und nachdem sie endet. Das liegt daran, dass Kampagnenbenachrichtigungen weiterhin gesendet werden, bis die Kampagne manuell gestoppt wurde.
{% endalert %}

## Webhook-Payload für Kampagnenbenachrichtigungen {#campaign-alert-webhook-payload}

Im Folgenden finden Sie ein Beispiel-Payload für den Body eines Kampagnenbenachrichtigungs-Webhooks. Dieses Beispiel verwendet eine Benachrichtigung, die so konfiguriert ist, dass sie gesendet wird, wenn die Anzahl der gesendeten Nachrichten bei einem bestimmten Kampagnenversand unter 500 fällt.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

