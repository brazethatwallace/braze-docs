---
nav_title: Kampagnen und Canvases
article_title: "Erste Schritte: Kampagnen und Canvases"
page_order: 3
page_type: reference
description: "Dieser Artikel bietet einen Überblick über die verschiedenen Möglichkeiten, wie Sie mit Braze Nachrichten versenden können."

---

# Erste Schritte: Kampagnen und Canvases

In Braze können Sie Nachrichten entweder über eine [Kampagne](#campaigns) oder ein [Canvas](#canvas) versenden.

- Wählen Sie eine Kampagne, um eine einzelne, gezielte Nachricht an eine Gruppe von Nutzer:innen zu senden. Eine Kampagne ist ein einzelner Nachrichtenschritt, um mit Ihren Nutzer:innen über verschiedene Messaging-Kanäle in Kontakt zu treten.
- Für das Versenden einer Reihe von fortlaufenden Nachrichten im Rahmen einer übergreifenden Customer Journey empfehlen wir Canvas, unser Tool für die Journey-Orchestrierung. Während Kampagnen gut geeignet sind, um einfache, zielgerichtete Nachrichten zu versenden, können Sie mit Canvases Ihre Beziehungen zu Kund:innen auf die nächste Stufe heben.

## Kampagnen

Obwohl Kampagnen je nach Kanal unterschiedlich gestaltet werden können, gibt es in Braze vier Haupttypen von Kampagnen, die Sie kennen sollten:

| Kampagnentyp        | Beschreibung                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regulär              | Dies ist der häufigste Kampagnentyp. Sie können je nach Kommunikationszielen einen oder mehrere Kanäle ansprechen und Ihre Inhalte mit unseren visuellen Editoren direkt in Braze gestalten, anpassen und testen. Erfahren Sie, wie Sie [eine Kampagne erstellen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/). |
| A/B-Tests          | Bei Kampagnen, die auf einen einzelnen Kanal abzielen, können Sie mehr als eine Version derselben Kampagne versenden und sehen, welche am besten abschneidet. Mit einer [multivariaten Kampagne]({{site.baseurl}}/user_guide/messaging/ab_testing/) können Sie Texte, Personalisierung und mehr in bis zu acht verschiedenen Varianten testen. |
| API                  | Mit [API-Kampagnen]({{site.baseurl}}/api/api_campaigns/) können Sie zeitkritische Nachrichten so schnell wie möglich versenden. Im Gegensatz zu anderen Kampagnentypen legen Sie im Braze-Dashboard weder die Nachricht noch die Empfänger:innen oder den Zeitplan fest. Stattdessen übergeben Sie diese Bezeichner in Ihren API-Aufrufen. Diese werden in der Regel für Realtime-Transaktionsnachrichten oder aktuelle Meldungen verwendet.  |
| Transaktions-E-Mails | [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/email/) von Braze sind speziell für den Versand automatisierter, nicht werblicher E-Mail-Nachrichten konzipiert, um eine vereinbarte Transaktion zwischen Ihnen und Ihren Kund:innen zu ermöglichen. Sie senden geschäftskritische Benachrichtigungen an einzelne Nutzer:innen, bei denen Geschwindigkeit von größter Bedeutung ist. *Verfügbar für ausgewählte Pakete.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Reguläre Kampagnen und A/B-Test-Kampagnen können geplant werden (z. B. um eine Liste von Nutzer:innen über eine bevorstehende Veranstaltung zu informieren) oder automatisch als Reaktion auf eine Nutzeraktion versendet werden (z. B. um eine E-Mail zu senden, wenn jemand Ihren Newsletter abonniert). Erfahren Sie mehr über die [Planung von Kampagnen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).
{% endalert %}

Unabhängig vom Kampagnentyp können Ihre Kampagnen auf die Bedürfnisse Ihrer Nutzer:innen eingehen und eine durchdachte, personalisierte Antwort liefern. Nachdem Sie Ihre Kampagne versendet haben, können Sie mit unseren [integrierten Analytics-Tools]({{site.baseurl}}/user_guide/analytics/reports/) sehen, wie sie abgeschnitten hat und wie viele Nutzer:innen basierend auf Ihren [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) konvertiert haben.

Hier finden Sie weitere Ressourcen, um mehr über Kampagnen in Braze zu erfahren:

- Braze Learning: [Kampagnen einrichten](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Eine Kampagne erstellen]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)
- [Ideen und Strategien]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)

## Canvas

Anstatt sporadische Nachrichten über mehrere Kampagnen hinweg zu versenden, schaffen Canvases eine kontinuierliche, fließende Konversation mit Nutzer:innen. Das liegt daran, dass sich die Journey einer Nutzerin oder eines Nutzers durch ein Canvas in verschiedene Pfade aufteilen kann – je nachdem, wie sie oder er mit Ihrer Marke interagiert (oder nicht). So können Sie Nutzer:innen automatisch und in Echtzeit durch einen bestimmten Flow voranbringen.

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

Auf diese Weise eignen sich Canvases hervorragend, um Nutzer:innen aufzufangen, die den Conversion-Pfad verlassen haben, und sie in die wirksamsten Outreach-Initiativen einzubinden.

Wenn Sie ein Canvas erstellen, folgen Sie vielen der gleichen Schritte wie bei der Einrichtung einer Kampagne: Sie legen eine allgemeine Zielgruppe, Einstiegsbedingungen und Sendeeinstellungen fest. Ihr Canvas startet, wenn jemand Ihre Trigger-Bedingung erfüllt. Dann durchläuft die Person einen Pfad im Canvas, bis Ihre Exit-Bedingungen erfüllt sind.

Ihr Canvas kann eine beliebige Kombination aus [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/), [Verzögerungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), [Experimenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) und mehr enthalten. Sie können auf allen unterstützten Messaging-Kanälen senden und sogar [soziale Netzwerke und Werbeplattformen integrieren]({{site.baseurl}}/partners/canvas_audience_sync/overview/) – wie Facebook, Google oder TikTok.

Hier finden Sie weitere Ressourcen, um mehr über Canvas zu erfahren:

- Braze Learning: [Journey-Orchestrierung mit Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Ein Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)
- [Canvas-Entwürfe]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines/)

## Messaging-Kanäle

Messaging-Kanäle sind die verschiedenen Kommunikationskanäle, über die Sie mit Ihren Kund:innen in Kontakt treten und gezielte Nachrichten übermitteln können. 

![]({% image_buster /assets/img/getting_started/channels.png %})

Die folgende Tabelle gibt einen Überblick über die unterstützten Kanäle.

| Kanal                                                                                              | Beschreibung                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-Mail]({{site.baseurl}}/user_guide/channels/email/)                        | Senden Sie personalisierte E-Mails an die Posteingänge Ihrer Nutzer:innen.                                                                                                       |
| [Mobile Push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)                   | Liefern Sie Nachrichten als Benachrichtigungen direkt auf die Mobilgeräte Ihrer Nutzer:innen.                                                                                   |
| [Web-Push]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/)                         | Senden Sie Benachrichtigungen an die Webbrowser Ihrer Nutzer:innen – auch wenn diese Ihre Website gerade nicht aktiv besuchen.                                                         |
| [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/)    | Zeigen Sie Nachrichten innerhalb Ihrer mobilen App an, während Nutzer:innen sie aktiv verwenden.                                                                             |
| [SMS, MMS und RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)*                   | Senden Sie Textnachrichten an die Mobiltelefone Ihrer Nutzer:innen.                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)*              | Senden Sie Nachrichten über die beliebte Messaging-Plattform WhatsApp, um Ihre Nutzer:innen zu erreichen und mit ihnen in Kontakt zu treten.                                                   |
| [Banner]({{site.baseurl}}/user_guide/channels/banners/)*       | Betten Sie Nachrichten direkt in Ihre App oder Website ein. |
| [Content-Cards]({{site.baseurl}}/user_guide/channels/content_cards/)*       | Bieten Sie einen Posteingang in Ihrer App oder Website an, in dem Nutzer:innen Nachrichten empfangen und mit ihnen interagieren können, oder zeigen Sie Nachrichten in einem Karussell, als Banner und mehr an. |
| [Connected TV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | Interagieren Sie mit Nutzer:innen auf vernetzten Fernsehplattformen.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) | Ermöglichen Sie Realtime-Kommunikation und Integration mit externen Systemen durch benutzerdefinierte HTTP-Callbacks.                                                    |
| [LINE]({{site.baseurl}}/user_guide/channels/line/) | Treten Sie mit Nutzer:innen auf LINE in Kontakt, der beliebtesten Messaging-App in Japan.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>Als Add-on-Feature verfügbar.</sup>

{% alert tip %}
Für kurze und dringende Nachrichten, die über die meisten Kanäle (E-Mail, SMS, Push) übermittelt werden können, nutzen Sie den Filter [Intelligenter Kanal]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/), um die Nachricht automatisch über den besten Kanal für jede Nutzerin und jeden Nutzer zu senden.
{% endalert %}