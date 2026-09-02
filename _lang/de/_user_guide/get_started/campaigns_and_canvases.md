---
nav_title: Campaigns und Canvases
article_title: "Erste Schritte: Campaigns und Canvases"
page_order: 3
page_type: reference
description: "Dieser Artikel bietet einen Überblick über die verschiedenen Möglichkeiten, wie Sie mit Braze Nachrichten versenden können."
---

# Erste Schritte: Campaigns und Canvases {#get-started-campaigns-and-canvases}

> Dieser Artikel bietet einen Überblick über die verschiedenen Möglichkeiten, wie Sie mit Braze Nachrichten versenden können. In Braze können Sie Nachrichten entweder über eine [Campaign](#campaigns) oder ein [Canvas](#canvas) versenden.

- Wählen Sie eine Campaign, um eine einzelne, gezielte Nachricht an eine Gruppe von Nutzer:innen zu senden. Eine Campaign ist ein einzelner Nachrichtenschritt, um mit Ihren Nutzer:innen über verschiedene Messaging-Kanäle in Kontakt zu treten.
- Für das Versenden einer Reihe von fortlaufenden Nachrichten im Rahmen einer übergreifenden Customer Journey empfehlen wir Canvas, unser Tool für die Journey-Orchestrierung. Während Campaigns gut geeignet sind, um einfache, zielgerichtete Nachrichten zu versenden, können Sie mit Canvases Ihre Beziehungen zu Kund:innen auf die nächste Stufe heben.

## Campaigns {#campaigns}

Campaigns können je nach Kanal individuell erstellt werden, doch es gibt vier Haupttypen von Campaigns in Braze, die Sie kennen sollten:

| Campaign-Typ | Beschreibung |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard | Dies ist der häufigste Campaign-Typ. Sie können je nach Ihren Messaging-Zielen einen oder mehrere Kanäle ansprechen und Ihre Inhalte direkt in Braze mit unseren visuellen Editoren entwerfen, anpassen und testen. Erfahren Sie, wie Sie [eine Campaign erstellen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign). |
| A/B-Tests | Bei Campaigns, die auf einen einzelnen Kanal abzielen, können Sie mehr als eine Version derselben Campaign senden und sehen, welche am besten abschneidet. Sie können Text, Personalisierung und mehr für bis zu acht verschiedene Versionen mit einer [multivariaten Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing) testen. |
| API | [API-Campaigns]({{site.baseurl}}/api/api_campaigns) ermöglichen es Ihnen, zeitkritische Nachrichten so schnell wie möglich zu versenden. Anders als bei anderen Campaign-Typen legen Sie die Nachricht, die Empfänger:innen oder den Zeitplan nicht im Braze-Dashboard fest. Stattdessen übergeben Sie diese Bezeichner in Ihren API-Aufrufen. Sie werden in der Regel für Realtime-Transaktionsnachrichten oder aktuelle Eilmeldungen verwendet. |
| Transaktions-E-Mails | Braze [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/email) sind speziell für den Versand automatisierter, nicht werblicher E-Mail-Nachrichten konzipiert, um eine vereinbarte Transaktion zwischen Ihnen und Ihren Kund:innen abzuwickeln. Sie senden geschäftskritische Benachrichtigungen an einzelne Nutzer:innen, bei denen Geschwindigkeit höchste Priorität hat. *Verfügbar für ausgewählte Pakete.* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

{% alert note %}
Standard- und A/B-Test-Campaigns können zeitgesteuert (z. B. um eine Liste von Nutzer:innen über ein bevorstehendes Event zu informieren) oder automatisiert als Reaktion auf eine Aktion der Nutzer:innen gesendet werden (z. B. eine E-Mail senden, wenn sich jemand für Ihren Newsletter anmeldet). Erfahren Sie mehr über das [Planen von Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).
{% endalert %}

Unabhängig davon, welchen Campaign-Typ Sie erstellen – Ihre Campaigns können auf die Bedürfnisse Ihrer Nutzer:innen eingehen und eine durchdachte, personalisierte Antwort liefern. Nachdem Sie Ihre Campaign gesendet haben, nutzen Sie unsere [integrierten Analytics-Tools]({{site.baseurl}}/user_guide/analytics/reports), um die Performance zu analysieren und zu sehen, wie viele Nutzer:innen basierend auf Ihren [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) konvertiert haben.

Entdecken Sie diese zusätzlichen Ressourcen, um mehr über Campaigns in Braze zu erfahren:

- Braze Lernangebote: [Campaign-Einrichtung](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Eine Campaign erstellen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- [Ideen und Strategien]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies)

## Canvas {#canvas}

Anstatt über mehrere Campaigns vereinzelte Nachrichten zu versenden, schaffen Canvases eine fortlaufende, fließende Konversation mit Nutzer:innen. Das liegt daran, dass die Journey einer Nutzer:in durch ein Canvas sich je nach ihren Aktionen (oder Inaktionen) mit Ihrer Marke in verschiedene Pfade aufteilen kann, sodass Sie Nutzer:innen automatisch in Echtzeit durch einen bestimmten Ablauf voranbringen können.

![Flussdiagramm für den beschriebenen Prozess.]({% image_buster /assets/img/getting_started/canvas_flow.png %})

Auf diese Weise eignen sich Canvases hervorragend, um ein breites Netz auszuwerfen und Nutzer:innen aufzufangen, die vom Weg zur Konversion abkommen, und sie in die effektivsten Outreach-Initiativen einzubinden.

Wenn Sie ein Canvas erstellen, folgen Sie vielen der gleichen Schritte wie beim Einrichten einer Campaign: Sie legen eine übergeordnete Zielgruppe, Entry-Bedingungen und Zustellungseinstellungen fest. Ihr Canvas beginnt, wenn jemand Ihre Trigger-Bedingung erfüllt. Anschließend bewegt sich die Person durch einen Pfad im Canvas, bis sie Ihre Exit-Bedingungen erfüllt.

Ihr Canvas kann eine beliebige Kombination aus [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), [Verzögerungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Experimenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) und mehr enthalten. Sie können über jeden unterstützten Messaging-Kanal senden und sogar [Integrationen mit sozialen Netzwerken und Werbeplattformen]({{site.baseurl}}/partners/canvas_audience_sync/overview) wie Facebook, Google oder TikTok nutzen.

Sehen Sie sich diese zusätzlichen Ressourcen an, um mehr über Canvas zu erfahren:

- Braze-Lernangebote: [Journey-Orchestrierung mit Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Ein Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- [Canvas-Entwürfe]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines)

## Messaging-Kanäle {#messaging-channels}

Messaging-Kanäle sind die verschiedenen Kommunikationskanäle, über die Sie mit Ihren Kund:innen interagieren und gezielte Nachrichten übermitteln können.

![Diagramm der über das SDK verfügbaren Braze-Messaging-Kanäle.]({% image_buster /assets/img/getting_started/channels.png %})

Die folgende Tabelle gibt einen Überblick über unsere unterstützten Kanäle.

| Kanal                                                                                              | Beschreibung                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-Mail]({{site.baseurl}}/user_guide/channels/email)                        | Senden Sie personalisierte E-Mails an die Posteingänge Ihrer Nutzer:innen.                                                                                                       |
| [Mobiler Push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)                   | Übermitteln Sie Nachrichten direkt als Benachrichtigungen auf die Mobilgeräte der Nutzer:innen.                                                                                   |
| [Web-Push]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)                         | Übermitteln Sie Benachrichtigungen an die Webbrowser der Nutzer:innen, auch wenn diese nicht aktiv auf Ihrer Website sind.                                                         |
| [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)    | Zeigen Sie Nachrichten innerhalb Ihrer mobilen App an, während die Nutzer:innen sie aktiv verwenden.                                                                             |
| [SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)*                   | Senden Sie Textnachrichten an die Mobiltelefone der Nutzer:innen.                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)*              | Senden Sie Nachrichten über die beliebte Messaging-Plattform WhatsApp, um Ihre Nutzer:innen zu erreichen und mit ihnen zu interagieren.                                                   |
| [Banner]({{site.baseurl}}/user_guide/channels/banners)*       | Betten Sie Nachrichten direkt in Ihre App oder Website ein. |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)*       | Stellen Sie einen Posteingang in Ihrer App oder Website bereit, in dem Nutzer:innen Nachrichten empfangen und mit ihnen interagieren können, oder zeigen Sie Nachrichten in einem Karussell, als Banner und mehr an. |
| [Connected TV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott)                           | Interagieren Sie mit Nutzer:innen auf Connected-TV-Plattformen.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) | Ermöglichen Sie Realtime-Kommunikation und Integration mit externen Systemen über angepasste HTTP-Callbacks.                                                    |
| [LINE]({{site.baseurl}}/user_guide/channels/line) | Interagieren Sie mit Nutzer:innen auf LINE, der beliebtesten Messaging-App in Japan.                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messaging-Kanäle" }

<sup>*Als Add-on-Feature verfügbar.*</sup>

{% alert tip %}
Für kurze und dringende Nachrichten, die über die meisten Kanäle (E-Mail, SMS, Push) kommuniziert werden können, nutzen Sie den Filter [Intelligenter Kanal]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel), um die Nachricht automatisch über den besten Kanal für jede:n Nutzer:in zu senden.
{% endalert %}