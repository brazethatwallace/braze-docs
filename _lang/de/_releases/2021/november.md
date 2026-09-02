---
nav_title: November
page_order: 1
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für November 2021."
---
# November 2021

## Berichtsmetrik Klick, der-to-Open Rate {#click-to-open-rate-reporting-metric}
Braze hat eine neue E-Mail-Metrik, die Klick, der-to-Open Rate, im [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder/) bereitgestellt. Diese Metrik gibt den Prozentsatz der geöffneten E-Mails an, die angeklickt wurden.

## Berichtsmetrik „Maschinelle Öffnungen“ {#machine-open-reporting-metric}

Auf den Canvas- und Campaign-Analytics-Seiten für E-Mails steht eine neue E-Mail-Metrik zur Verfügung: [Maschinelle Öffnungen]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens). Diese Metrik identifiziert E-Mail-Öffnungen, die nicht von Menschen stammen (z. B. von Apples Servern geöffnet), und wird als Teilmenge der gesamten Öffnungen angezeigt.

## Liquid-Variable random_bucket_number {#randombucketnumber-liquid-variable}
Die Liste der [unterstützten Liquid-Variablen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) für die Personalisierung von Nachrichten wurde um die Variable `random_bucket_number` erweitert.

## Richtlinien für Rich-Push-Benachrichtigungen in iOS 15 {#ios-15-rich-push-notification-guidelines}
Die Rich-Docs für iOS wurden um neue [Richtlinien für iOS-Push-Benachrichtigungen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) erweitert, darunter Informationen über Benachrichtigungszustände und eine Aufschlüsselung der Variablen für die Textkürzung.

## IPs, die in der EU für Webhooks und Connected-Content auf die Whitelist gesetzt werden sollen {#ips-to-whitelist-in-eu-for-webhooks-and-connected-content}
Weitere IPs, die in der EU für Webhooks und Connected-Content auf die Whitelist gesetzt werden können, wurden zu unserem Artikel über [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) und [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) hinzugefügt. Zu diesen neuen IPs gehören `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188` und `3.70.107.88`.

## Endpunkt „Käufe exportieren“ {#export-purchases-endpoint}
Ein neuer [`/purchases/product_list`-Endpunkt]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) wurde zu Braze hinzugefügt. Dieser Endpunkt gibt paginierte Listen von Produkt-IDs zurück.

## Neue Braze Partnerschaften {#new-braze-partnerships}

### Adobe – Customer Data Platform
Die Integration von Braze und [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) ermöglicht es Marken, ihre Adobe-Daten (angepasste Attribute und Segmente) in Realtime mit Braze zu verbinden und abzubilden. Marken können dann auf Basis dieser Daten handeln und diesen Nutzer:innen personalisierte, zielgerichtete Erlebnisse bieten.

### BlueConic – Customer Data Platform
Mit [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic) können Unternehmensnutzer:innen Daten in persistenten, individuellen Profilen vereinheitlichen und dann über Kunden-Touchpoints und Systeme hinweg synchronisieren, um eine breite Palette von wachstumsorientierten Initiativen zu unterstützen, einschließlich Orchestrierung des Kundenlebenszyklus, Modellierung und Analytics, digitale Produkte und Erlebnisse, zielgruppenbasierte Monetarisierung und mehr.

### Worthy – Dynamischer Content {#worthy-dynamic-content}
Die Integration von Braze und [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) ermöglicht es Ihnen, mit dem Drag-and-Drop-Editor für dynamischen Content von Worthy personalisierte, reichhaltige In-App-Erlebnisse zu erstellen und diese über Braze zuzustellen.

### Judo – Dynamischer Content {#judo-dynamic-content}
Die Integration von [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) und Braze erlaubt es Ihnen, Komponenten Ihrer Campaign zu überschreiben und durch Judo-Erlebnisse zu ersetzen. Daten von Braze können verwendet werden, um personalisierte Inhalte in einem Judo-Erlebnis zu unterstützen. Nutzer:innen-Events und Daten aus dem Erlebnis können für Attribution und Targeting in Braze zurückgeführt werden.

### Line – Messaging
Die Integration von [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) und Braze erlaubt es Ihnen, Braze-Webhooks, fortschrittliche Segmentierungs-, Personalisierungs- und Triggering-Features zu nutzen, um Ihren Nutzer:innen in Line über die [Line Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/) Nachrichten zu senden.

### RevenueCat – Zahlungen {#revenuecat-payments}
Die Integration von [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) und Braze ermöglicht es Ihnen, die Kauf- und Abo-Lebenszyklusereignisse Ihrer Kund:innen automatisch plattformübergreifend zu synchronisieren. So können Sie Campaigns erstellen, die auf die Abo-Lebenszyklusphase Ihrer Kund:innen reagieren, z. B. die Ansprache von Kund:innen, die sich während der kostenlosen Testphase abgemeldet haben, oder das Versenden von Erinnerungen an Kund:innen mit Rechnungsproblemen.

### Punchh – Loyalty
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) hat sich mit Braze zusammengetan, um Daten zwischen den beiden Plattformen für Geschenk- und Treuezwecke zu synchronisieren. In Braze veröffentlichte Daten stehen für die Segmentierung zur Verfügung und können über in Braze eingerichtete Webhook-Templates mit Nutzerdaten in Punchh synchronisiert werden.