---
nav_title: August
page_order: 5
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für August 2017."
---

# August 2017

## Update für Push-Action-Buttons {#update-to-push-action-buttons}

Wir haben unseren REST API Messaging-Endpunkten Unterstützung für [Push-Action-Buttons]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons) hinzugefügt.

## Update für Liquid-Templating {#update-to-liquid-templating}

Sie können jetzt [eine Nachricht personalisieren]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/), und zwar auf der Grundlage von:
- dem Gerät, an das sie gesendet wurde,
- Geräte-ID,
- Mobilfunkanbieter,
- IDFA,
- Modell,
- OS und
- Plattform

## API-getriggertes Canvas {#api-triggered-canvas}

Sie können jetzt ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) über API-Endpunkte (Senden, Zeitplan, Update, Löschen) triggern, die mit den bereits vorhandenen für Campaigns übereinstimmen, was eine weitere Automatisierung und Optimierung Ihres Marketings ermöglicht.

## Web-Push-Action-Buttons

Wir haben das Web SDK für Chrome um Unterstützung für Push-Action-Buttons erweitert, die es Ihnen ermöglichen, Ihr Engagement zu steigern, indem Sie Ihren Nutzer:innen kontextuelle Auswahlmöglichkeiten bieten, die ihr geschäftiges Leben vereinfachen. Informieren Sie sich über die [Best Practices für Push-Benachrichtigungen]({{site.baseurl}}/user_guide/channels/push/best_practices/).

## Neue API-Endpunkte {#new-api-endpoints}

Wir haben neue API-Endpunkte veröffentlicht: /email/hard_bounces, mit dem Sie Hard Bounces nach E-Mail-Adresse oder in einem bestimmten Datumsbereich abrufen können, und /messages/scheduled_broadcasts, mit dem Sie den nächsten Zeitpunkt abrufen können, zu dem geplante Campaigns und Canvases mit geplantem Eingang starten. Diese neuen Endpunkte ermöglichen Ihnen eine weitere Anpassung und Optimierung Ihrer Campaigns. Erfahren Sie mehr über unsere [API-Endpunkte]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Geofences

Wir haben ein neues Feature – Geofences – hinzugefügt, das es Ihnen ermöglicht, Nachrichten in Realtime zu triggern, wenn Kund:innen ein bestimmtes geografisches Gebiet betreten oder verlassen, und so eine personalisierte, relevante Kommunikation mit Ihren Kund:innen zu ermöglichen. Erfahren Sie mehr über [Standort-Marketing]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

## Update für den E-Mail-Editor {#update-to-email-editor}

Wir haben unseren neuen E-Mail-Editor mit einer dynamischen Autovervollständigung ausgestattet, sodass Sie bei der Verwendung von Liquid nun automatisch die tatsächlichen angepassten Attribute und Events Ihrer Kund:innen vervollständigen können, was Ihnen das Leben leichter macht. Erfahren Sie mehr über die [Best Practices für E-Mails]({{site.baseurl}}/user_guide/channels/email/best_practices/).

## Update für Datumsfilter {#update-to-date-filters}

Wir haben einen „Nie“-Datumsfilter hinzugefügt, mit dem Sie gezielt Kund:innen ansprechen können, die noch nie eine Ihrer Nachrichten erhalten oder mit ihnen interagiert haben. So können Sie saubere Kund:innenlisten führen und die Zustellbarkeit von E-Mails sicherstellen. Erfahren Sie mehr über [Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Update für Canvas {#update-to-canvas}

Wir haben am oberen Rand jeder Canvas-Variante Prozentzahlen hinzugefügt, damit Sie auf einen Blick sehen können, welche Varianten eine bessere Performance aufweisen. Erfahren Sie mehr über [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

## Canvas mit Intelligenter Auswahl {#canvas-with-intelligent-selection}

Canvas verfügt jetzt über Intelligente Auswahl, die es Ihnen ermöglicht, Ihre Canvases mit größerer Effizienz zu testen. Erfahren Sie mehr über unsere [Intelligence Suite]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

## Update für E-Mail-Anzeigenamen {#update-to-email-display-names}

Wir haben die Unterstützung von UTF-8-Sonderzeichen in E-Mail-Anzeigenamen hinzugefügt, sodass Sie noch personalisiertere E-Mails für Ihre Kund:innen erstellen können. Erfahren Sie mehr über die [Best Practices für E-Mails]({{site.baseurl}}/user_guide/channels/email/best_practices/).

## Engagement-Berichte – CSV-Aggregation {#engagement-reports-csv-aggregation}

Jetzt können Sie konsolidierte Daten für jede Campaign und jedes Canvas in zwei separaten Dateien erhalten, unabhängig davon, wie viele Campaigns oder Canvases ausgewählt sind. So haben Sie alle Daten, die Sie benötigen, immer zur Hand. Erfahren Sie mehr über [Engagement-Berichte]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/).

> Wie in unseren [Versionshinweisen vom September 2017]({{site.baseurl}}/releases/2017/september/) erwähnt, können Sie jetzt Daten aus einem bestimmten Zeitraum aggregieren und Exporte so planen, dass sie regelmäßig ausgeführt werden.