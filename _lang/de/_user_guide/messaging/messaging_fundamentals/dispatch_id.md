---
nav_title: Versand-ID
article_title: Verhalten der Versand-ID
page_order: 5.2
page_type: reference
description: "Dieser Referenzartikel beschreibt das Verhalten der Versand-ID für Campaigns, Canvas, Liquid und Currents."
---

# Verhalten der Versand-ID {#dispatch-id-behavior}

> Die `dispatch_id` ist eine eindeutige ID für jeden Nachrichtenversand, also jede „Übertragung“, die von Braze gesendet wird.

## Verhalten der Versand-ID in Campaigns {#dispatch-id-behavior-in-campaigns}

Geplante Campaign-Nachrichten erhalten dieselbe `dispatch_id`. Aktionsbasierte oder API-getriggerte Campaign-Nachrichten können eine eindeutige `dispatch_id` pro Nutzer:in erhalten, oder die `dispatch_id` kann für mehrere Nutzer:innen dieselbe sein, wenn sie in unmittelbarer Nähe oder mit demselben API-Aufruf gesendet werden. Zwei Nutzer:innen in Ihrer geplanten Campaign-Zielgruppe haben beispielsweise bei jeder Planung der Campaign dieselbe `dispatch_id`. Zwei Nutzer:innen in der Zielgruppe einer API-getriggerten Campaign können jedoch unterschiedliche Versand-IDs haben, wenn die Campaigns in separaten API-Aufrufen und nicht in unmittelbarer Nähe zueinander gesendet wurden.

Multichannel-Campaigns verhalten sich für ihren Zustellungstyp genauso.

{% alert warning %}
Eine `dispatch_id` wird für alle Canvas-Schritte zufällig generiert, da Braze Canvas-Schritte als getriggerte Ereignisse behandelt, auch wenn sie „geplant“ sind. Dies kann zu Inkonsistenzen bei der Generierung der IDs führen. Manchmal hat eine Canvas-Komponente eine eindeutige `dispatch_id` pro Nutzer:in pro Versand, oder sie kann gemeinsame Versand-IDs für mehrere Nutzer:innen pro Versand haben.
{% endalert %}

## Versand-ID mit Liquid in Nachrichten einbinden {#template-dispatch-id-into-messages-with-liquid}

Wenn Sie den Versand einer Nachricht innerhalb der Nachricht nachverfolgen möchten (z. B. in einer URL), können Sie die `dispatch_id` als Template einbinden. Die Formatierung dafür finden Sie unter Canvas-Attribute in der Liste der [unterstützten Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Dies verhält sich wie die `api_id`: Da die `api_id` bei der Campaign-Erstellung nicht verfügbar ist, setzt Braze sie als Platzhalter ein, der in der Vorschau als `dispatch_id_for_unsent_campaign` angezeigt wird. Die ID wird vor dem Senden der Nachricht generiert und zum Sendezeitpunkt eingefügt.

{% alert warning %}
Das Liquid-Templating von `dispatch_id_for_unsent_campaign` funktioniert nicht mit In-App-Nachrichten, da In-App-Nachrichten keine `dispatch_id` haben.
{% endalert %}

## Currents-Feld „Versand-ID“ für E-Mail {#dispatch-id-currents-field-for-email}

Das Feld `dispatch_id` ist in Currents-E-Mail-Ereignissen für alle Konnektor-Typen verfügbar. Die `dispatch_id` ist die eindeutige ID, die für jede Übertragung bzw. jeden Versand generiert wird, der von der Braze-Plattform gesendet wird.

Während alle Kund:innen, die eine geplante Nachricht erhalten, dieselbe `dispatch_id` bekommen, erhalten Kund:innen, die aktionsbasierte oder API-getriggerte Nachrichten empfangen, eine eindeutige `dispatch_id` pro Nachricht. Das Feld `dispatch_id` ermöglicht es Ihnen, festzustellen, welche Instanz einer wiederkehrenden Campaign für eine Conversion verantwortlich ist, sodass Sie sehen können, welche Arten von Campaigns Ergebnisse erzielen.

Sie können die `dispatch_id` als [Personalisierungs-Tag]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), in [Nachrichten-Engagement-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) oder bei der Verwendung von [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents#email-events) oder [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents) für Currents nutzen.