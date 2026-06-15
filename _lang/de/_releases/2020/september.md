---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2020."
---

# September

## Funnel-Berichte {#funnel-reporting}

Funnel Reporting bietet einen visuellen Bericht, mit dem Sie die Journeys Ihrer Kund:innen nach dem Erhalt einer [Campaign]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) oder eines [Canvas]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) analysieren können.

## Anleitung zum Upgrade auf iOS 14 {#ios-14-upgrade-guide}

In Übereinstimmung mit den Änderungen, die in Apples neuem iOS 14 angekündigt wurden, gibt es einige Braze-bezogene Änderungen und Maßnahmen, die für Braze iOS SDK-Integrationen erforderlich sind. Weitere Informationen finden Sie in dieser [Anleitung zum Upgrade]({{site.baseurl}}/ios_14/).

## Änderungen an IDFA und IDFV für iOS 14 {#changes-to-idfa-and-idfv-for-ios-14}

In iOS 14 müssen Nutzer:innen entscheiden, ob sie dem Ad-Tracking zustimmen und Apps und Werbenetzwerke ihre IDFA lesen lassen wollen, wenn sie eine App besuchen. Daher besteht die Strategie von Braze darin, stattdessen den „Identifier for Vendors“ (z. B. IDFV) zu verwenden, damit Sie weiterhin Nutzer:innen über verschiedene Geräte hinweg tracken können. Weitere Informationen finden Sie in der [Anleitung zum Upgrade auf iOS 14]({{site.baseurl}}/ios_14/).

## E-Mail-Validierung {#email-validation}

Dieser neue Prozess zur Validierung der E-Mail-Syntax ist ein Upgrade des bestehenden Prozesses von Braze. Damit wird überprüft, ob die in Braze aktualisierten oder importierten E-Mails korrekt sind. Weitere Informationen finden Sie in [diesen Richtlinien und Hinweisen]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/).

## Zufälliges Bucket-Nutzer:innen-Event in Currents {#random-bucket-user-event-in-currents}

Die zufällige Bucket-Nummer (z. B. RBN) wird jedes Mal erzeugt, wenn ein:e neue:r Nutzer:in in einem Workspace angelegt wird. Dabei wird jeder/jedem neuen Nutzer:in eine zufällige Bucket-Nummer zugewiesen, mit der Sie dann gleichmäßig verteilte Segmente aus zufälligen Nutzer:innen erstellen können. Verwenden Sie dies, um eine Reihe von zufälligen Bucket-Nummern zu gruppieren und die Performance Ihrer Campaigns und Kampagnenvarianten zu vergleichen. Um zu sehen, ob dieses Event für Sie verfügbar ist, werfen Sie einen Blick in das Currents-[Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).

## Canvas-Komponenten – Demnächst verfügbar! {#canvas-components-coming-soon}

Braze hat vier neue Canvas-Komponenten hinzugefügt, mit denen Sie die Flexibilität und Funktionalität Ihrer Canvases erhöhen können. Diese neuen Komponenten umfassen: [Decision-Split-Schritt]({{site.baseurl}}/decision_split/), [Verzögerungsschritt]({{site.baseurl}}/delay_step/), [Messaging-Schritte]({{site.baseurl}}/message_step/) und [Audience Sync mit Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Canvas Decision-Split, Verzögerung und Messaging-Schritte**<br>Decision-Splits können verwendet werden, um Canvas-Branches zu erstellen, je nachdem, ob ein:e Nutzer:in einer definierten Abfrage entspricht. Mit Verzögerungsschritten können Sie eine eigenständige Verzögerung zu Ihrem Canvas hinzufügen, ohne dass eine entsprechende Nachricht erforderlich ist. Messaging-Schritte erlauben es Ihnen, eine eigenständige Nachricht an der gewünschten Stelle in Ihrem Canvas-Ablauf einzufügen.
- **Audience Sync mit Facebook**<br>Mit Braze Audience Sync to Facebook können Marken die Daten ihrer eigenen Nutzer:innen aus ihrer eigenen Braze-Integration zu Facebook Custom Audiences hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr auszuliefern. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt dazu verwendet werden, über Custom Audiences eine Anzeige für diese:n Nutzer:in in Facebook auszulösen.

## Eingehende SMS-Events {#sms-inbound-received-events}

Currents wurde ein neues Messaging-Engagement-Event hinzugefügt. Dieses Event tritt ein, wenn eine:r Ihrer Nutzer:innen eine SMS an eine Telefonnummer in einer Ihrer Braze SMS-Abo-Gruppen sendet. Weitere Informationen finden Sie in unserem Currents-[Glossar zu Messaging- und Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).