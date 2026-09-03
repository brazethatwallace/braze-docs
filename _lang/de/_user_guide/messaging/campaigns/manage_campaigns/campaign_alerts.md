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

> Wir möchten Sie benachrichtigen, wenn etwas nicht ganz wie erwartet läuft, und Ihnen die Gewissheit geben, dass alles reibungslos funktioniert. Schwellenwert-Benachrichtigungen für Campaigns sorgen für Sicherheit – erfahren Sie als Erste:r, wenn eine wichtige Campaign mehr oder weniger Nachrichten sendet als erwartet.

Suchen Sie nach der gleichen Funktion für Canvas? Lesen Sie den Artikel [Canvas-Schwellenwert-Benachrichtigungen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

Kampagnenbenachrichtigungen sind für die folgenden Campaigns verfügbar:

- Wiederkehrende geplante Campaigns
- Aktionsbasierte Campaigns
- API-getriggerte Campaigns

## Einrichten Ihrer Campaign-Benachrichtigung {#setting-up-your-campaign-alert}

Navigieren Sie zur Analytics-Seite Ihrer Campaign, um mit der Einrichtung Ihrer Benachrichtigung zu beginnen. Wenn Sie **Set Up Alert** auswählen, können Sie obere und untere Schwellenwerte für Benachrichtigungen sowie die Empfänger:innen und Kanäle der Benachrichtigungen festlegen.

![Dialogfeld für Campaign-Monitoring mit zwei Buttons: „Cancel“ und „Save“.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Für eine geplante wiederkehrende Campaign können Sie obere und untere Schwellenwerte für die Anzahl der gesendeten Nachrichten bei jedem Versand der Campaign festlegen. Für eine getriggerte Campaign können Sie obere und untere Schwellenwerte für die Anzahl der stündlich und täglich gesendeten Nachrichten festlegen.

Sie können eine E-Mail-Benachrichtigung, eine Webhook-Benachrichtigung oder beides einrichten. Webhook-Benachrichtigungen können sehr nützlich sein, da sie es Ihnen ermöglichen, eine Benachrichtigung an einen Slack-Kanal zu senden. Weitere Informationen zur Integration von Campaign-Benachrichtigungen mit Slack finden Sie in der Slack-Dokumentation unter [Nachrichten über eingehende Webhooks senden](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

{% alert note %}
Wenn Sie Campaign-Benachrichtigungen für zukünftige Campaigns einrichten, erhalten Sie möglicherweise Aktualisierungen, bevor die Campaign startet und nachdem sie endet. Dies liegt daran, dass Campaign-Benachrichtigungen weiterhin gesendet werden, bis die Campaign manuell gestoppt wurde.
{% endalert %}

## Webhook-Payload für Campaign-Benachrichtigungen {#campaign-alert-webhook-payload}

Das Folgende ist ein Beispiel-Payload für den Body eines Webhook für Campaign-Benachrichtigungen. Dieses Beispiel verwendet eine Benachrichtigung, die so konfiguriert ist, dass sie gesendet wird, wenn die Anzahl gesendeter Nachrichten bei einem bestimmten Campaign-Versand unter 500 fällt.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

