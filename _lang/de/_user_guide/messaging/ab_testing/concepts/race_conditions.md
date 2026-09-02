---
nav_title: Race-Conditions
article_title: Race-Conditions
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Dieser Artikel beschreibt Best Practices, um zu vermeiden, dass Race-Conditions Ihre Messaging-Kampagnen beeinträchtigen."
toc_headers: h2
---

# Race-Conditions {#race-conditions}

> Eine Race-Condition tritt auf, wenn ein Ergebnis von der Reihenfolge oder dem Timing mehrerer Ereignisse abhängt. Wenn beispielsweise die gewünschte Reihenfolge der Ereignisse „Event A“ und dann „Event B“ ist, aber manchmal „Event A“ zuerst kommt und manchmal „Event B“ zuerst – dann spricht man von einer Race-Condition. Dies kann zu unerwarteten Ergebnissen oder Fehlern führen, da diese Ereignisse um den Zugriff auf gemeinsame Ressourcen oder Daten konkurrieren.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

In Braze können Race-Conditions auftreten, wenn mehrere Aktionen gleichzeitig auf Basis von Nutzerdaten oder Events ausgelöst werden. Wenn beispielsweise eine Nutzer:in mehrere Campaigns triggert (wie die Anmeldung für einen Newsletter oder einen Kauf), erhält sie die Nachrichten möglicherweise nicht in der richtigen Reihenfolge.

## Arten von Race-Conditions {#types-of-race-conditions}

Die häufigsten Arten von Race-Conditions können auftreten, wenn Sie Folgendes tun:

- Targeting von neuen Nutzer:innen
- Mehrere API-Endpunkte verwenden
- Passende aktionsbasierte Trigger or triggern und Zielgruppenfilter
- Den „Interact with Step“-Trigger or triggern verwenden

Ziehen Sie die folgenden Szenarien in Betracht und wenden Sie Best Practices an, um diese Race-Conditions zu vermeiden.

## Szenario 1: Targeting von neuen Nutzer:innen {#scenario-1-targeting-new-users}

In Braze tritt eine der häufigsten Race-Conditions bei Nachrichten auf, die auf neu erstellte Nutzer:innen abzielen. Die erwartete Reihenfolge der Ereignisse ist:

1. Eine Nutzer:in wird erstellt;
2. Dieselbe Nutzer:in wird sofort für eine Nachricht angesprochen, führt ein angepasstes Event aus oder protokolliert ein angepasstes Attribut.

In einigen Fällen wird jedoch das zweite Ereignis zuerst ausgelöst. Das bedeutet, dass versucht wird, eine Nachricht an eine Nutzer:in zu senden, die noch nicht existiert. Infolgedessen erhält die Nutzer:in die Nachricht nie. Dies gilt auch für Events oder Attribute, bei denen versucht wird, das Event oder Attribut in einem Kundenprofil or Nutzerprofil zu protokollieren, das noch nicht erstellt wurde.

Bei In-App-Nachrichten muss die In-App-Nachricht auf dem Gerät geladen werden, bevor sie getriggert werden kann. Wenn das Trigger or triggern-Event Teil des Onboarding-Prozesses ist oder die Nutzer:in das Segment für das angepasste Event als Teil ihrer ersten Sitzung verlässt, wird sie die In-App-Nachricht wahrscheinlich nicht sehen.

### In-App-Nachrichten {#in-app-messages}

Bei In-App-Nachrichten kann die Situation differenzierter sein. Eine In-App-Nachricht muss an das SDK or Software-Development-Kit zugestellt und dort zwischengespeichert werden – typischerweise zu Beginn einer Sitzung – bevor sie getriggert werden kann. Wenn das Trigger or triggern-Event Teil des Erstellungsprozesses ist oder wenn die In-App-Nachrichten-Campaign zugestellt wird, bevor die Nutzer:in die Zielgruppenkriterien erfüllt (oder nachdem sie diese nicht mehr erfüllt) während ihrer ersten Sitzung, sieht sie die In-App-Nachricht möglicherweise nicht.

### Best Practices {#best-practices}

#### Verzögerungen einführen {#introduce-delays}

Nachdem eine neue Nutzer:in erstellt wurde, können Sie eine Verzögerung hinzufügen, bevor Sie gezielte Campaigns oder Canvase senden. Diese zeitliche Verzögerung ermöglicht es, das Kundenprofil or Nutzerprofil zu erstellen und alle relevanten Attribute zu Update or aktualisieren or aktualisieren, die die Berechtigung zum Empfang der Nachricht bestimmen können.

Beispielsweise können Sie nach der Registrierung einer Nutzer:in für Ihre App ein Werbeangebot nach 24 Stunden senden. Oder wenn Sie eine Nutzer:in erstellen oder ein angepasstes Attribut protokollieren, können Sie eine einminütige Verzögerung hinzufügen, bevor Sie in Ihrem Prozess fortfahren, um diese Race-Condition zu vermeiden.

Sie können diese Verzögerung auch im [Braze SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/sdk_integration) für das spezifische angepasste Event hinzufügen, das eine neue Nutzer:in dazu bringt, einen Canvas zu betreten.

## Szenario 2: Mehrere API-Endpunkte verwenden {#scenario-2-using-multiple-api-endpoints}

{% alert important %}
Wir verwenden asynchrone Verarbeitung, um Geschwindigkeit und Flexibilität zu maximieren. Das bedeutet, dass wir nicht garantieren können, dass API-Aufrufe, die separat an uns gesendet werden, in der Reihenfolge verarbeitet werden, in der sie gesendet wurden.
{% endalert %}

Es gibt einige Szenarien, in denen mehrere API-Endpunkte ebenfalls zu dieser Race-Condition führen können, beispielsweise wenn:

- Separate API-Endpunkte verwendet werden, um Nutzer:innen zu erstellen und Canvase oder Campaigns zu Trigger or triggern or triggern
- Mehrere separate Aufrufe an den `/users/track`-Endpunkt gemacht werden, um angepasste Attribute, Events oder Käufe zu Update or aktualisieren or aktualisieren

Wenn Nutzerinformationen über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) an Braze gesendet werden, kann die Verarbeitung gelegentlich einige Sekunden dauern. Das bedeutet, wenn gleichzeitig Anfragen an den `/users/track`- und Messaging-Endpunkte wie `/campaign/trigger/send` gestellt werden, gibt es keine Garantie, dass die Nutzerinformationen aktualisiert werden, bevor eine Nachricht gesendet wird.

{% alert note %}
Wenn Nutzerattribute und Events in derselben Anfrage gesendet werden (entweder über `/users/track` oder über das SDK or Software-Development-Kit), verarbeitet Braze Attribute vor Events oder bevor versucht wird, eine Nachricht zu senden.
{% endalert %}

### Best Practices

#### Bei Verwendung mehrerer Endpunkte Anfragen nacheinander senden {#when-using-multiple-endpoints-send-your-requests-one-at-a-time}

Wenn Sie mehrere Endpunkte verwenden, können Sie versuchen, Ihre Anfragen zu staffeln, sodass jede Anfrage abgeschlossen ist, bevor die nächste beginnt. Dies kann die Wahrscheinlichkeit einer Race-Condition verringern. Wenn Sie beispielsweise Nutzerattribute Update or aktualisieren or aktualisieren und eine Nachricht senden müssen, warten Sie zunächst, bis das Kundenprofil or Nutzerprofil vollständig aktualisiert ist, bevor Sie eine Nachricht über einen Endpunkt senden.

Wenn Sie eine geplante Nachrichten-API-Anfrage senden, müssen diese Anfragen separat sein, und eine Nutzer:in muss erstellt werden, bevor die geplante API-Anfrage gesendet wird.

#### Schlüsseldaten mit dem Trigger or triggern einschließen {#include-key-data-with-the-trigger}

Anstatt mehrere Endpunkte zu verwenden, können Sie die [Nutzerattribute]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) und [Trigger or triggern-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object) in einem einzigen API-Aufruf über den [`campaign/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) einschließen.

Wenn diese Objekte mit dem Trigger or triggern eingeschlossen werden, werden die Attribute zuerst verarbeitet, bevor die Nachricht getriggert wird, wodurch potenzielle Race-Conditions eliminiert werden. Beachten Sie, dass Trigger or triggern-Eigenschaften das Kundenprofil or Nutzerprofil nicht Update or aktualisieren or aktualisieren, sondern nur im Kontext der Nachricht verwendet werden.

#### Den POST: Track users (sync)-Endpunkt verwenden {#use-the-post-track-users-sync-endpoint}

Verwenden Sie den [`/users/track/sync/`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous), um angepasste Events und Käufe zu erfassen und Nutzerprofilattribute synchron zu Update or aktualisieren or aktualisieren. Die Verwendung dieses Endpunkts zur gleichzeitigen Aktualisierung von Nutzerprofilen in einem einzigen Aufruf kann helfen, potenzielle Race-Conditions zu vermeiden.

{% multi_lang_include alerts/early_access_beta_alert.md feature='This endpoint' type='beta' %}

## Szenario 3: Passende aktionsbasierte Trigger or triggern und Zielgruppenfilter {#scenario-3-matching-action-based-triggers-and-audience-filters}

Eine weitere häufige Race-Condition kann auftreten, wenn Sie eine aktionsbasierte Campaign oder einen Canvas mit demselben Trigger or triggern wie dem Zielgruppenfilter konfigurieren (z. B. ein geändertes Attribut oder ein ausgeführtes angepasstes Event). Die Nutzer:in befindet sich möglicherweise nicht in der Zielgruppe zu dem Zeitpunkt, an dem sie das Trigger or triggern-Event ausführt, was bedeutet, dass sie die Campaign nicht erhält oder den Canvas nicht betritt.

### Best Practices

#### Zielgruppe nach einer Verzögerung prüfen {#check-your-audience-after-a-delay}

Um die Verwendung von Zielgruppenfiltern zu vermeiden, die die Trigger or triggern-Kriterien enthalten, empfehlen wir, Ihre Zielgruppe vor der Zustellung zu prüfen. Sie können beispielsweise [Zustellungsvalidierungen verwenden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings) in Canvas-Nachrichtenschritten als zusätzliche Prüfung, um zu bestätigen, dass Ihre Zielgruppe die Zustellungskriterien beim Nachrichtenversand erfüllt. Sie können auch Exit-Kriterien für Canvas nutzen, um Nutzer:innen an jedem Punkt während der User Journey auszuschließen, wenn sie Ihre Kriterien erfüllen.

Für Campaigns können Sie Exit-Events verwenden, um Campaigns mit einem Trigger or triggern-Event zu ermöglichen, Nachrichten an Nutzer:innen abzubrechen, die das Exit-Event während der Verzögerung ausführen.

#### Eindeutige Filter mit dem Trigger or triggern-Event verwenden {#use-unique-filters-with-the-trigger-event}

Beim Konfigurieren Ihrer Filter möchten Sie möglicherweise einen redundanten Filter „zur Sicherheit“ hinzufügen. Diese Redundanz kann jedoch zu mehr Problemen führen. Vermeiden Sie stattdessen nach Möglichkeit die Verwendung eines Filters, der den Trigger or triggern enthält. Dies ist der sicherste Weg, um eine Race-Condition zu vermeiden.

Wenn beispielsweise Ihr Campaign-Trigger or triggern „Hat einen Kauf getätigt“ ist und Ihr Zielgruppenfilter „Hat irgendeinen Kauf getätigt“ lautet, kann diese Redundanz eine Race-Condition verursachen.

#### Zielgruppenfilter vermeiden, die davon ausgehen, dass das Trigger or triggern-Event aktualisiert wurde {#avoid-audience-filters-that-assume-the-trigger-event-has-been-updated}

Diese Best Practice ähnelt der Vermeidung redundanter Filter mit dem Trigger or triggern-Event. Normalerweise schlägt ein Filter fehl, der davon ausgeht, dass das Trigger or triggern-Event im Kundenprofil or Nutzerprofil aktualisiert wurde.

#### Liquid-Abbrüche verwenden (nur Attribute) {#use-liquid-aborts-attributes-only}

In Campaigns und Canvas-Schritten können Sie Liquid-Abbrüche verwenden, um die Verwendung von Zielgruppenfiltern zu vermeiden, die die Trigger or triggern-Attribute im Entry-Zeitplan enthalten. Nehmen wir beispielsweise an, Sie haben ein Array-Attribut „Lieblingsfarben“ und möchten jede Nutzer:in ansprechen, die das Attribut-Array mit einem beliebigen Wert aktualisiert und nach Abschluss des Updates auch die Farbe „Blau“ im Array hat. Wenn Sie in diesem Beispiel die Zielgruppenfilter verwenden, stoßen Sie auf eine Race-Condition und verpassen Nutzer:innen, die „Blau“ zum ersten Mal zum Array hinzufügen.

In diesem Fall können Sie eine Trigger or triggern-Verzögerung in einer Campaign implementieren oder einen Verzögerungsschritt in Canvas verwenden, um dem Kundenprofil or Nutzerprofil Zeit zur Aktualisierung zu geben, und dann die folgende Liquid-Abbruchlogik verwenden:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Bestätigen, wie Nutzerdaten verwaltet werden {#confirm-how-user-data-is-being-managed}

Wenn während der Canvas-Entry-Auswertung eine Race-Condition auftritt, können Nutzer:innen einen Canvas betreten, den sie nicht betreten sollten. Beispielsweise könnte das Profil so eingestellt sein, dass es in die Zielgruppe aufgenommen wird, und anschließend aktualisiert werden, nachdem der Canvas die Nutzer:innen in die Warteschlange eingereiht hat, sodass sie nicht mehr für die Zielgruppe berechtigt sind.

Wenn eine Nutzer:in das Canvas-Entry-Event mehrmals innerhalb derselben Sekunde auslöst, erlaubt Braze nur einen Eintritt für diese Sekunde (auch wenn der erneute Eintritt aktiviert ist). Dies verhindert doppelte Eintritte, sodass die Gesamtzahl der Canvas-Eintritte niedriger sein kann als die Gesamtzahl der Trigger or triggern-Events.

Wir empfehlen zu bestätigen, wie Nutzerdaten verwaltet und aktualisiert werden – insbesondere wann und wie bestimmte Attribute aktualisiert werden, z. B. per SDK or Software-Development-Kit, API, Batch-API und anderen Methoden. Dies kann helfen zu identifizieren und zu klären, warum eine Nutzer:in eine Campaign oder einen Canvas betreten hat, im Vergleich dazu, wann das Kundenprofil or Nutzerprofil aktualisiert wurde.

## Szenario 4: Den „Interact with Step“-Trigger or triggern verwenden {#scenario-4-using-the-interact-with-step-trigger}

Wenn in einem Canvas auf einen Nachrichtenschritt direkt ein Aktionspfad-Schritt folgt, der den „Interact With Step“-Trigger or triggern verwendet, kann eine Race-Condition auftreten. Da Nutzer:innen mit einer Nachricht interagieren können, sobald sie zugestellt wird, ist es möglich, dass eine Nutzer:in die getrackte Aktion abschließt, bevor sie offiziell den Aktionspfad-Schritt betritt.

In diesem Fall registriert der Aktionspfad-Schritt die Interaktion nicht, da er nur Events auswertet, die nach dem Eintritt in den Schritt auftreten. Das bedeutet, dass die Nutzer:in möglicherweise einen unbeabsichtigten Pfad durchläuft.

Ein Canvas sendet eine Push-Benachrichtigung in einem Nachrichtenschritt, gefolgt von einem Aktionspfad-Schritt, der prüft, ob die Nutzer:in diese Push-Benachrichtigung öffnet. Wenn eine Nutzer:in die Push-Benachrichtigung sofort nach dem Empfang öffnet (bevor sie den Aktionspfad-Schritt betritt), wird das Öffnungs-Event möglicherweise nicht erfasst. Die Nutzer:in könnte dann fälschlicherweise den „Nicht geöffnet“-Pfad durchlaufen, obwohl sie mit der Nachricht interagiert hat.

### Best Practices

#### Engagement über ein angepasstes Event tracken {#track-engagement-using-a-custom-event}

Vermeiden Sie es, sich auf „Interact With Step“ direkt nach einem Nachrichtenschritt zu verlassen, wenn Nutzerinteraktionen voraussichtlich schnell erfolgen. Tracken Sie Engagement stattdessen über ein angepasstes Event (z. B. ausgelöst von der App oder Website nach der Interaktion) und werten Sie dieses Event in einem nachfolgenden Schritt aus. So wird sichergestellt, dass das Event erfasst wird, nachdem die Nutzer:in den Schritt betreten hat.

#### Branches vermeiden, die von der Interaktion abhängen {#avoid-branches-that-are-dependent-on-interaction}

Gestalten Sie Ihren Canvas so, dass eine fehlende sofortige Interaktion die Nutzererfahrung nicht beeinträchtigt. Vermeiden Sie beispielsweise kritische Verzweigungsentscheidungen, die ausschließlich davon abhängen, ob die Interaktion im nächsten Schritt erfasst wird, oder fügen Sie Folgelogik hinzu, die die Pfade der Nutzer:innen korrigieren kann.