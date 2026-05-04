---
nav_title: Verhalten der Versand-ID
article_title: Verhalten der Versand-ID
page_order: 0

page_type: solution
description: "Dieser Hilfeartikel befasst sich mit dem Verhalten der Versand-ID, einschließlich ihrer Verwendung, Auswirkungen und Einschränkungen."
---

# Verhalten der Versand-ID {#dispatch-id-behavior}

Eine `dispatch_id` ist die ID des Nachrichtenversands – eine eindeutige ID für jede von Braze gesendete „Übertragung“. Nutzer:innen, die eine geplante Nachricht erhalten, erhalten dieselbe `dispatch_id`. Normalerweise erhalten aktionsbasierte oder API-getriggerte Nachrichten eine eindeutige `dispatch_id` pro Nutzer:in, aber Nachrichten, die in engem zeitlichen Abstand zueinander gesendet werden, können dieselbe `dispatch_id` für mehrere Nutzer:innen verwenden.

Dies kann dazu führen, dass zwei verschiedene Nutzer:innen unterschiedliche Versand-IDs für eine einzige Campaign haben, wenn die Nachrichten zu zwei verschiedenen Zeitpunkten gesendet wurden. Das liegt oft daran, dass die API-Anfragen separat gestellt wurden. Wenn beide Nutzer:innen in einer einzigen Sendung zur gleichen Campaign-Zielgruppe gehören, sind ihre Versand-IDs identisch.

## Verhalten der Versand-ID in Campaigns {#dispatch-id-behavior-in-campaigns}

Geplante Campaign-Nachrichten erhalten dieselbe `dispatch_id`. Aktionsbasierte oder API-getriggerte Campaign-Nachrichten können eine eindeutige `dispatch_id` pro Nutzer:in erhalten, oder die `dispatch_id` kann für mehrere Nutzer:innen dieselbe sein, wenn sie in unmittelbarer Nähe oder mit demselben API-Aufruf gesendet werden, wie oben beschrieben. Zwei Nutzer:innen in Ihrer geplanten Campaign-Zielgruppe haben beispielsweise jedes Mal, wenn die Campaign geplant wird, dieselbe `dispatch_id`. Zwei Nutzer:innen in der Zielgruppe einer API-getriggerten Campaign können jedoch unterschiedliche Versand-IDs haben, wenn sie in separaten API-Aufrufen gesendet wurden und nicht in unmittelbarer zeitlicher Nähe zueinander liegen.

Campaigns mit mehreren Kanälen verhalten sich genauso wie für ihren Zustellungstyp beschrieben.

{% alert warning %}
Eine `dispatch_id` wird für alle Canvas-Schritte zufällig generiert, da Braze Canvas-Schritte als getriggerte Ereignisse behandelt, auch wenn sie „geplant“ sind. Dies kann zu Inkonsistenzen bei der Generierung der IDs führen. Manchmal hat eine Canvas-Komponente eine eindeutige `dispatch_id` pro Nutzer:in und pro Sendung, oder sie hat gemeinsame Versand-IDs für alle Nutzer:innen pro Sendung.
{% endalert %}

## Versand-ID mit Liquid in Nachrichten einfügen {#template-dispatch-id-into-messages-with-liquid}

Wenn Sie den Versand einer Nachricht aus der Nachricht heraus verfolgen möchten (z. B. in einer URL), können Sie die `dispatch_id` als Template einfügen. Die Formatierung dafür finden Sie unter Canvas-Attribute in unserer Liste der [unterstützten Tags für die Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

Dies verhält sich genauso wie `api_id`: Da die `api_id` bei der Erstellung der Campaign nicht verfügbar ist, wird sie als Platzhalter eingefügt und in der Vorschau als `dispatch_id_for_unsent_campaign` angezeigt. Die ID wird generiert, bevor die Nachricht gesendet wird, und zum Sendezeitpunkt eingefügt.

{% alert warning %}
Das Liquid-Templating von `dispatch_id_for_unsent_campaign` funktioniert nicht mit In-App-Nachrichten, da In-App-Nachrichten keine `dispatch_id` haben.
{% endalert %}

## Versand-ID als Currents-Feld für E-Mail {#dispatch-id-currents-field-for-email}

Im Bestreben, unsere Currents-Funktionen weiter zu verbessern, ist `dispatch_id` auch ein Feld in Currents-E-Mail-Ereignissen für alle Konnektor-Typen. Die `dispatch_id` ist die eindeutige ID, die für jede von der Braze-Plattform gesendete Übertragung bzw. Sendung generiert wird.

Während alle Kund:innen, die eine geplante Nachricht erhalten, dieselbe `dispatch_id` erhalten, bekommen Kund:innen, die aktionsbasierte oder API-getriggerte Nachrichten erhalten, eine eindeutige `dispatch_id` pro Nachricht. Mit dem Feld `dispatch_id` können Sie feststellen, welche Instanz einer wiederkehrenden Campaign für die Conversion verantwortlich ist. So erhalten Sie mehr Insights und Informationen darüber, welche Arten von Campaigns dazu beitragen, Ihre Geschäftsziele zu erreichen.

Sie können `dispatch_id` als [Tag für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), in [Ereignissen für das Nachrichten-Engagement]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) oder bei der Verwendung von [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) oder [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) für Currents verwenden.

_Zuletzt aktualisiert am 15. Juli 2021_