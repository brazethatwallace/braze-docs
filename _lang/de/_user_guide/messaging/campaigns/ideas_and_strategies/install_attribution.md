---
nav_title: Nutzer:innen-Installationen verstehen
article_title: Nutzer:innen-Installationen verstehen
page_order: 7
page_type: reference
description: "Dieser Referenzartikel beschreibt Nutzer:innen-Installationen (Install-Attribution-Tracking) und verschiedene Möglichkeiten, diese Informationen in Ihren Campaigns einzusetzen."
tool:
  - Campaigns
  - Segments
---

# Nutzer:innen-Installationen verstehen {#understanding-user-installs}

> Install-Attribution-Tracking ist eine hervorragende Möglichkeit, die anfängliche Beziehung zu Ihren Nutzer:innen zu verbessern. Zu wissen, wie, wo und – noch wichtiger – warum Nutzer:innen Ihre App installieren, ermöglicht es Ihnen, besser zu verstehen, wer Ihre Nutzer:innen sind und wie Sie ihnen Ihre App am besten vorstellen sollten.

Braze bietet zwar kein Install-Attribution-Tracking an, lässt sich aber mit [Diensten]({{site.baseurl}}/partners/message_orchestration) wie Branch und AppsFlyer integrieren, um Ihnen nahtlos Install-Daten bereitzustellen.

## Segmentieren Sie Ihre Nutzer:innen {#segment-your-users}

Sobald Nutzer:innen Ihre App installiert haben, können Sie sie anhand der folgenden [Install-Attribution-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#install-attribution) segmentieren. Eine Reise-App könnte beispielsweise Nutzer:innen, die über eine Anzeige zu Strandurlaubs-Angeboten gekommen sind, einem Segment „Strandliebhaber:innen“ hinzufügen. Ebenso könnte eine Musik-App Nutzer:innen basierend auf dem Musikgenre segmentieren, das in der Anzeige angezeigt wurde, die zur Installation geführt hat.

## Best Practices {#best-practices}

### Personalisiertes Onboarding {#personalized-onboarding}

Jetzt, da Sie mehr Informationen über Ihre Nutzer:innen haben, können Sie deren Onboarding-Prozess personalisieren. Das kann so einfach sein wie das Ändern der Bilder in Ihren Nachrichten entsprechend den Präferenzen, oder so komplex wie das Erstellen eines einzigartigen Nutzer:innen-Onboardings für jede Anzeige, die zu einer Installation führen könnte. Um eine umfassende Abfolge von Nachrichten zu skalieren, die das Nutzer:innenverhalten berücksichtigt, lesen Sie unsere Dokumentation zu [Canvas]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

### Referenzdaten aus der Anzeige {#reference-data-from-the-ad}

Nutzer:innen können durch ein Werbeangebot oder eine Aktion auf Ihre App aufmerksam werden. Mithilfe von Install-Attribution-Daten können Sie Campaigns mit Rabattcodes oder Angeboten ausschließlich an jene Nutzer:innen senden, die Ihre App aufgrund dieser Aktionen installiert haben. Auf ähnliche Weise können Sie, wenn Ihre Anzeige Informationen zu einem bestimmten Produkt enthält (z. B. einen bestimmten Film in einer Video-App oder einen Sale in einer E-Commerce-App), Campaigns senden, die Nutzer:innen zur richtigen Seite in Ihrer App weiterleiten.

## Werbeaufwand bewerten {#evaluate-advertising-efforts}

Install-Attribution-Daten können wertvoll sein, um die Effektivität verschiedener Marketing-Campaigns zu bewerten. Durch die Analyse, welche Anzeigen und Campaigns die meisten Installationen generieren und welche hinterherhinken, können Sie Ihre Ressourcen auf die überzeugendsten Anzeigen konzentrieren.