---
nav_title: Nutzer:innen-Installationen verstehen
article_title: Nutzer:innen-Installationen verstehen
page_order: 7
page_type: reference
description: "Dieser Referenzartikel beschreibt Nutzer:innen-Installationen (Install-Attribution-Tracking) und verschiedene Möglichkeiten, diese Informationen in Ihren Kampagnen einzusetzen."
tool:
  - Campaigns
  - Segments
---

# Nutzer:innen-Installationen verstehen

> Install-Attribution-Tracking ist eine hervorragende Möglichkeit, die anfängliche Beziehung zu Ihren Nutzer:innen zu verbessern. Zu wissen, wie, wo und – noch wichtiger – warum Nutzer:innen Ihre App installieren, ermöglicht es Ihnen, besser zu verstehen, wer Ihre Nutzer:innen sind und wie Sie ihnen Ihre App am besten vorstellen sollten.

Braze bietet zwar kein Install-Attribution-Tracking an, lässt sich aber mit [Diensten]({{site.baseurl}}/partners/message_orchestration/) wie Branch und AppsFlyer integrieren, um Ihnen nahtlos Install-Daten bereitzustellen.

## Segmentieren Sie Ihre Nutzer:innen

Sobald Nutzer:innen Ihre App installiert haben, können Sie sie anhand der folgenden [Install-Attribution-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution) segmentieren. Eine Reise-App könnte beispielsweise Nutzer:innen, die über eine Anzeige zu Strandurlaubs-Angeboten gekommen sind, einem Segment „Strandliebhaber" hinzufügen. Ebenso könnte eine Musik-App Nutzer:innen basierend auf dem Musikgenre segmentieren, das in der Werbeanzeige angezeigt wurde, die zur Installation geführt hat.

## Best Practices

### Personalisiertes Onboarding

Da Sie nun mehr Informationen über Ihre Nutzer:innen haben, können Sie deren Onboarding-Prozess personalisieren. Das kann so einfach sein wie das Anpassen der Bilder in Ihren Nachrichten an die Vorlieben der Nutzer:innen, oder so komplex wie das Erstellen eines individuellen Onboardings für jede Anzeige, die zu einer Installation führen könnte. Um eine umfassende Abfolge von Nachrichten zu erstellen, die das Verhalten der Nutzer:innen berücksichtigt, lesen Sie unsere Dokumentation zu [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Daten aus der Anzeige referenzieren

Nutzer:innen werden möglicherweise durch eine Aktion oder ein Gewinnspiel auf Ihre App aufmerksam. Mithilfe von Install-Attribution-Daten können Sie Kampagnen mit Rabattcodes oder Angeboten ausschließlich an diejenigen Nutzer:innen senden, die aufgrund dieser Aktionen installiert haben. Auf ähnliche Weise können Sie, wenn Ihre Anzeige Informationen zu einem bestimmten Produkt enthält (z. B. einen bestimmten Film in einer Video-App oder einen Sale in einer E-Commerce-App), Kampagnen senden, die Nutzer:innen zur richtigen Seite Ihrer App weiterleiten.

## Werbemaßnahmen bewerten

Install-Attribution-Daten können wertvoll sein, um die Effektivität verschiedener Marketing-Kampagnen zu beurteilen. Zu analysieren, welche Anzeigen und Kampagnen zu den meisten Installationen führen und welche zurückbleiben, kann Ihnen helfen, Ihre Ressourcen auf die wirkungsvollsten Anzeigen zu konzentrieren.