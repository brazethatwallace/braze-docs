---
nav_title: SDK-Übersicht
article_title: SDK-Übersicht
page_order: 9
page_type: reference
description: "Dieser Referenzartikel behandelt die Grundlagen des Braze SDK."
---

# SDK-Übersicht {#sdk-overview}

> Das Braze SDK erfasst Sitzungsdaten, identifiziert Nutzer:innen und zeichnet Käufe und angepasste Events über Ihre Website oder App auf. Sie können das SDK auch nutzen, um das Engagement mit Nutzer:innen zu fördern, indem Sie In-App Messages und Push-Benachrichtigungen direkt über das Braze-Dashboard versenden.

Kurz gesagt, das Braze SDK:
* Sammelt und synchronisiert Nutzerdaten in einem konsolidierten Nutzerprofil
* Erfasst Marketingdaten und angepasste Daten speziell für Ihr Unternehmen
* Unterstützt Push-Benachrichtigungen, In-App Messages und Content-Card-Nachrichtenkanäle

## Was ist ein SDK? {#what-is-an-sdk}
Ein Software-Development-Kit (SDK) ist ein Satz vorgefertigter Tools&mdash;nur kleine Code-Blöcke&mdash;, die digitalen Anwendungen hinzugefügt werden können, um neue Funktionen zu unterstützen. Das Braze SDK wird zum Senden und Abrufen von Informationen zu und von Ihrer App oder Website verwendet. Es ist so konzipiert, dass es von Anfang an wichtige Funktionen bietet: Erstellen von Nutzerprofilen, Protokollieren von angepassten Events, Auslösen von Push-Benachrichtigungen usw.

Da diese Funktionen standardmäßig von Braze bereitgestellt werden, können sich Ihre Entwickler:innen auf Ihr Kerngeschäft konzentrieren. Ohne ein SDK müsste jeder Braze-Kunde die gesamte Infrastruktur und die Tools für die Datenverarbeitung, die Segmentierungslogik, die Zustelloptionen, die Behandlung anonymer Nutzer:innen, die Campaign-Analytics und vieles mehr von Grund auf neu erstellen. Das würde viel länger dauern und wäre viel mühsamer als die Stunde, die es dauert, unser SDK einzubinden.

## Implementierung {#implementation}

Um ein SDK in Ihre App oder Website einzubinden, muss jemand den Code des SDKs in die allgemeine Codebasis der Anwendung einfügen. Das bedeutet, dass Ihr Entwicklerteam daran beteiligt sein wird, unsere Apps miteinander zu verbinden, damit Informationen und Aktionen zwischen ihnen fließen. Doch obwohl Ihre Entwickler:innen daran beteiligt sind, ist das SDK so konzipiert, dass es schlank und nutzerfreundlich zu integrieren ist.

Um Zeit zu sparen und eine reibungslose Integration zu gewährleisten, empfehlen wir, dass Sie und Ihr Entwicklerteam Ihre angepassten Events, angepassten Attribute und das SDK zur gleichen Zeit einrichten. Erfahren Sie mehr über die Schritte, die Ihre Marketing- und Entwicklerteams gemeinsam durchdenken müssen, indem Sie unseren [Artikel zur Implementierung]({{site.baseurl}}/user_guide/get_started/integrations) lesen.

## Datenaggregation {#data-aggregation}

Das Braze SDK erfasst automatisch Daten auf Nutzerebene und liefert Ihnen wichtige Metriken für Ihre App und Ihre Nutzerbasis. Gruppieren Sie ähnliche Apps in einem einzigen Workspace (z. B. iOS- und Android-Versionen zusammen), um die gesammelten Daten plattformübergreifend anzuzeigen und ein vollständiges Bild der Nutzeraktivitäten zu erhalten. Weitere Informationen finden Sie im Artikel zur [Startseite]({{site.baseurl}}/user_guide/analytics/dashboards/home).

## In-App Messages {#in-app-messaging}

Verwenden Sie das SDK, um In-App Messages direkt zu verfassen und zu versenden. Sie können je nach Ihrer Campaign-Strategie zwischen Slideup-, Modal- oder Vollbild-Nachrichten wählen. Einzelheiten zur Erstellung finden Sie unter [In-App-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

![Push-Benachrichtigung in einem Webbrowser]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Push-Benachrichtigungen {#push-notifications}

Push-Benachrichtigungen sind eine weitere großartige Möglichkeit, mit Ihren Nutzer:innen in Kontakt zu treten, und eignen sich besonders für zeitkritische Handlungsaufforderungen. Mobile Push-Benachrichtigungen erscheinen auf den Geräten Ihrer Nutzer:innen, und Web-Push-Benachrichtigungen erscheinen auch dann, wenn Ihre Website nicht geöffnet ist. Weitere Informationen zur Verwendung von Push-Benachrichtigungen finden Sie in unserem [Artikel über Push-Benachrichtigungen]({{site.baseurl}}/user_guide/channels/push).

Die Nutzer:innen Ihrer Website oder App müssen sich für den Empfang von Push-Benachrichtigungen per Opt-in entscheiden. Weitere Einzelheiten finden Sie unter [Push-Priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Segmentierung und Zustellregeln {#segmentation-and-delivery-rules}

Eine Campaign, die In-App Messages enthält, wird standardmäßig an alle Versionen der App in diesem Workspace gesendet. Zum Beispiel wird die Nachricht sowohl an Web- als auch an mobile Nutzer:innen gesendet. Um eine In-App-Nachricht ausschließlich an Web- oder Mobilnutzer:innen zu senden, müssen Sie Ihre Campaign entsprechend segmentieren, was standardmäßig durch das Braze SDK unterstützt wird.

Sie können ein Segment Ihrer Webnutzer:innen erstellen, indem Sie **Apps and websites targeted** auf **Users from specific apps** setzen und dann nur Ihre Website für die **Specific Apps** auswählen.

![Segmentdetails-Seite mit Fokus auf der Web-App]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Dies ermöglicht es Ihnen, Nutzer:innen auf der Grundlage ihres Verhaltens auf intelligente Weise anzusprechen. Wenn Sie Webnutzer:innen ansprechen möchten, um sie zum Herunterladen Ihrer mobilen App zu bewegen, würden Sie dieses Segment als Ihre Zielgruppe erstellen. Wenn Sie eine Messaging-Campaign versenden möchten, die eine mobile In-App-Nachricht, aber keine Web-Nachricht enthält, deaktivieren Sie das Symbol für Ihre Website in Ihrem Segment.

## Unterstützte Plattformen {#supported-platforms}

Braze stellt SDKs für verschiedene Plattformen bereit, darunter Web, Android und Swift. Die vollständige Liste finden Sie im [Braze Developer Guide]({{site.baseurl}}/developer_guide/home).