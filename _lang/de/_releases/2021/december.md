---
nav_title: Dezember
page_order: 0
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Dezember 2021."
alias: "/help/release_notes/2022/january/"
---
# Dezember 2021 {#december-2021}

## Update zum Exportieren von Nutzer:innen nach Segment-Endpunkt {#update-to-export-users-by-segment-endpoint}

Ab Dezember 2021 treten die folgenden Änderungen für den [Endpunkt „Nutzer:innen nach Segment exportieren“]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) in Kraft:

1. Das Feld `fields_to_export` in dieser API-Anfrage wird erforderlich. Die Option, standardmäßig alle Felder zu verwenden, wird entfernt.
2. Die Felder für `custom_events`, `purchases`, `campaigns_received` und `canvases_received` enthalten nur Daten aus den letzten 90 Tagen.

## Neue Eigenschaften für Currents Nachrichten-Engagement-Ereignisse {#new-properties-for-currents-message-engagement-events}

Es wurden neue Eigenschaften für ausgewählte [Nachrichten-Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) hinzugefügt. Dieses Update gilt für die folgenden Currents Nachrichten-Engagement-Ereignisse und alle Partner, die sie verwenden:

- `LINK_ID`, `LINK_ALIAS` hinzugefügt zu:
  - E-Mail-Klick (alle Ziele)
- `USER_AGENT` hinzugefügt zu:
  - E-Mail-Öffnung
  - E-Mail-Klick
  - E-Mail als Spam markieren
- `MACHINE_OPEN` hinzugefügt zu:
  - E-Mail-Öffnung

## Neuer Liquid-Tag zur Personalisierung {#new-liquid-personalization-tag}

Wir unterstützen jetzt das Targeting von Nutzer:innen, die auf ihrem Gerät Vordergrund-Push aktiviert haben, mit den folgenden Liquid-Tags:

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

Weitere Informationen finden Sie unter [Unterstützte Tags für die Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## Über Webhooks {#about-webhooks}

Webhooks sind leistungsstarke, flexible Tools – aber sie können auch ein wenig verwirrend sein. Wenn Sie sich fragen, was Webhooks sind und wie Sie sie in Braze verwenden können, lesen Sie unseren neuen Artikel [Über Webhooks]({{site.baseurl}}/about_webhooks/).

## Amazon Personalize

Amazon Personalize ist so, als hätten Sie Ihr eigenes Empfehlungssystem für maschinelles Lernen, das den ganzen Tag läuft. Basierend auf mehr als 20 Jahren Erfahrung mit Empfehlungen ermöglicht Ihnen Amazon Personalize, das geschäftskunden-Engagement zu verbessern, indem es personalisierte Produkt- und Inhaltsempfehlungen in Realtime sowie gezielte Marketing-Aktionen bereitstellt.

Wenn Sie mehr erfahren möchten, lesen Sie unseren neuen Artikel über [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize/). Dort erfahren Sie, welche Anwendungsfälle Amazon Personalize bietet, mit welchen Daten es arbeitet, wie Sie den Dienst konfigurieren und wie Sie ihn in Braze integrieren können.

## Neue Braze-Partnerschaften {#new-braze-partnerships}

### Yotpo – E-Commerce {#yotpo-ecommerce}

Die Integration von [Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) und Braze erlaubt es Ihnen, Sternebewertungen, Top-Rezensionen und visuelle nutzergenerierte Inhalte zu Produkten in E-Mails und anderen Kommunikationskanälen innerhalb von Braze dynamisch abzurufen und anzuzeigen. Sie können auch Daten zur Kundentreue in E-Mails und andere Kommunikationsmethoden einbeziehen, um eine personalisierte Interaktion zu schaffen, die den Umsatz und die Loyalität steigert.

### Zeotap – geschäftskunden Data Platform (CDP) {#zeotap-customer-data-platform}

Mit der Integration von [Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) und Braze können Sie den Umfang und die Reichweite Ihrer Campaigns erweitern, indem Sie Zeotap-Kundensegmente synchronisieren, um Zeotap-Nutzerdaten Braze-Nutzer:innen-Konten zuzuordnen. Sie können dann auf diese Daten reagieren und Ihren Nutzer:innen personalisierte Targeting-Erlebnisse bereitstellen.