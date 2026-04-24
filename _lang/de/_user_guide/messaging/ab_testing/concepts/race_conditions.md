---
nav_title: Race-Conditions
article_title: Race-Conditions
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Dieser Artikel behandelt Best Practices, um Race-Conditions zu vermeiden, die Ihre Messaging-Kampagnen beeinträchtigen können."
toc_headers: h2
---

# Race-Conditions

> Eine Race-Condition tritt auf, wenn ein Ergebnis von der Reihenfolge oder dem Timing mehrerer Ereignisse abhängt. Wenn beispielsweise die gewünschte Reihenfolge der Ereignisse „Event A" und dann „Event B" ist, aber manchmal „Event A" zuerst kommt und manchmal „Event B" zuerst – dann spricht man von einer Race-Condition. Dies kann zu unerwarteten Ergebnissen oder Fehlern führen, da diese Ereignisse um den Zugriff auf gemeinsame Ressourcen oder Daten konkurrieren.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

In Braze können Race-Conditions auftreten, wenn mehrere Aktionen gleichzeitig auf Basis von Nutzerdaten oder Events ausgelöst werden. Wenn beispielsweise eine Nutzer:in mehrere Kampagnen auslöst (wie die Anmeldung für einen Newsletter oder einen Kauf), erhält sie die Nachrichten möglicherweise nicht in der richtigen Reihenfolge.

## Arten von Race-Conditions

Die häufigsten Arten von Race-Conditions können auftreten, wenn Sie Folgendes tun:

- Neue Nutzer:innen ansprechen
- Mehrere API-Endpunkte verwenden
- Aktionsbasierte Trigger und Zielgruppen-Filter abgleichen

Betrachten Sie die folgenden Szenarien und implementieren Sie Best Practices, um diese Race-Conditions zu vermeiden.

## Szenario 1: Neue Nutzer:innen ansprechen

In Braze tritt eine der häufigsten Race-Conditions bei Nachrichten auf, die auf neu erstellte Nutzer:innen abzielen. Die erwartete Reihenfolge der Ereignisse ist:

1. Eine Nutzer:in wird erstellt;
2. Dieselbe Nutzer:in wird sofort für eine Nachricht angesprochen, führt ein angepasstes Event aus oder protokolliert ein angepasstes Attribut.

In einigen Fällen wird jedoch das zweite Ereignis zuerst ausgelöst. Das bedeutet, dass versucht wird, eine Nachricht an eine Nutzer:in zu senden, die noch nicht existiert. Infolgedessen erhält die Nutzer:in die Nachricht nie. Dies gilt auch für Events oder Attribute, bei denen versucht wird, das Event oder Attribut in einem Nutzerprofil zu protokollieren, das noch nicht erstellt wurde.

Bei In-App-Nachrichten muss die In-App-Nachricht auf dem Gerät geladen werden, bevor sie getriggert werden kann. Wenn das Trigger-Event Teil des Onboarding-Prozesses ist oder die Nutzer:in das Segment für das angepasste Event als Teil ihrer ersten Sitzung verlässt, wird sie die In-App-Nachricht wahrscheinlich nicht sehen.

### In-App-Nachrichten

Bei In-App-Nachrichten kann die Situation differenzierter sein. Eine In-App-Nachricht muss an das SDK zugestellt und dort zwischengespeichert werden – typischerweise zu Beginn einer Sitzung – bevor sie getriggert werden kann. Wenn das Trigger-Event Teil des Erstellungsprozesses ist oder wenn die In-App-Nachrichten-Kampagne zugestellt wird, bevor die Nutzer:in die Zielgruppenkriterien erfüllt (oder nachdem sie diese nicht mehr erfüllt), sieht sie die In-App-Nachricht möglicherweise nicht.

### Best Practices

#### Verzögerungen einführen

Nachdem eine neue Nutzer:in erstellt wurde, können Sie eine Verzögerung hinzufügen, bevor Sie gezielte Kampagnen oder Canvases senden. Diese zeitliche Verzögerung ermöglicht es, das Nutzerprofil zu erstellen und alle relevanten Attribute zu aktualisieren, die die Berechtigung zum Empfang der Nachricht bestimmen können.

Beispielsweise können Sie nach der Registrierung einer Nutzer:in für Ihre App ein Werbeangebot nach 24 Stunden senden. Oder wenn Sie eine Nutzer:in erstellen oder ein angepasstes Attribut protokollieren, können Sie eine einminütige Verzögerung hinzufügen, bevor Sie in Ihrem Prozess fortfahren, um diese Race-Condition zu vermeiden.

Sie können diese Verzögerung auch im [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration) für das spezifische angepasste Event hinzufügen, das eine neue Nutzer:in dazu bringt, einen Canvas zu betreten.

## Szenario 2: Mehrere API-Endpunkte verwenden

{% alert important %}
Wir verwenden asynchrone Verarbeitung, um Geschwindigkeit und Flexibilität zu maximieren. Das bedeutet, dass wir nicht garantieren können, dass API-Aufrufe, die separat an uns gesendet werden, in der Reihenfolge verarbeitet werden, in der sie gesendet wurden.
{% endalert %}

Es gibt einige Szenarien, in denen mehrere API-Endpunkte ebenfalls zu dieser Race-Condition führen können, beispielsweise wenn:

- Separate API-Endpunkte verwendet werden, um Nutzer:innen zu erstellen und Canvases oder Kampagnen zu triggern
- Mehrere separate Aufrufe an den `/users/track`-Endpunkt gemacht werden, um angepasste Attribute, Events oder Käufe zu aktualisieren

Wenn Nutzerinformationen über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) an Braze gesendet werden, kann die Verarbeitung gelegentlich einige Sekunden dauern. Das bedeutet, wenn gleichzeitig Anfragen an den `/users/track`- und Messaging-Endpunkte wie `/campaign/trigger/send` gestellt werden, gibt es keine Garantie, dass die Nutzerinformationen aktualisiert werden, bevor eine Nachricht gesendet wird.

{% alert note %}
Wenn Nutzerattribute und Events in derselben Anfrage gesendet werden (entweder über `/users/track` oder über das SDK), verarbeitet Braze Attribute vor Events oder bevor versucht wird, eine Nachricht zu senden.
{% endalert %}

### Best Practices

#### Bei Verwendung mehrerer Endpunkte Anfragen nacheinander senden

Wenn Sie mehrere Endpunkte verwenden, können Sie versuchen, Ihre Anfragen zu staffeln, sodass jede Anfrage abgeschlossen ist, bevor die nächste beginnt. Dies kann die Wahrscheinlichkeit einer Race-Condition verringern. Wenn Sie beispielsweise Nutzerattribute aktualisieren und eine Nachricht senden müssen, warten Sie zunächst, bis das Nutzerprofil vollständig aktualisiert ist, bevor Sie eine Nachricht über einen Endpunkt senden.

Wenn Sie eine geplante Nachrichten-API-Anfrage senden, müssen diese Anfragen separat sein, und eine Nutzer:in muss erstellt werden, bevor die geplante API-Anfrage gesendet wird.

#### Schlüsseldaten mit dem Trigger einschließen

Anstatt mehrere Endpunkte zu verwenden, können Sie die [Nutzerattribute]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) und [Trigger-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object) in einem einzigen API-Aufruf über den [`campaign/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) einschließen.

Wenn diese Objekte mit dem Trigger eingeschlossen werden, werden die Attribute zuerst verarbeitet, bevor die Nachricht getriggert wird, wodurch potenzielle Race-Conditions eliminiert werden. Beachten Sie, dass Trigger-Eigenschaften das Nutzerprofil nicht aktualisieren, sondern nur im Kontext der Nachricht verwendet werden.

#### Den POST: Track users (sync)-Endpunkt verwenden

Verwenden Sie den [`/users/track/sync/`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous), um angepasste Events und Käufe zu erfassen und Nutzerprofilattribute synchron zu aktualisieren. Die Verwendung dieses Endpunkts zur gleichzeitigen Aktualisierung von Nutzerprofilen in einem einzigen Aufruf kann helfen, potenzielle Race-Conditions zu vermeiden.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' type='beta' %}

## Szenario 3: Aktionsbasierte Trigger und Zielgruppen-Filter abgleichen

Eine weitere häufige Race-Condition kann auftreten, wenn Sie eine aktionsbasierte Kampagne oder einen Canvas mit demselben Trigger wie dem Zielgruppen-Filter konfigurieren (z. B. ein geändertes Attribut oder ein ausgeführtes angepasstes Event). Die Nutzer:in befindet sich möglicherweise nicht in der Zielgruppe zu dem Zeitpunkt, an dem sie das Trigger-Event ausführt, was bedeutet, dass sie die Kampagne nicht erhält oder den Canvas nicht betritt.

### Best Practices

#### Zielgruppe nach einer Verzögerung prüfen

Um die Verwendung von Zielgruppen-Filtern zu vermeiden, die die Trigger-Kriterien enthalten, empfehlen wir, Ihre Zielgruppe vor der Zustellung zu prüfen. Sie können beispielsweise [Zustellungsvalidierungen verwenden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#edit-delivery-settings) in Canvas-Nachrichtenschritten als zusätzliche Prüfung, um zu bestätigen, dass Ihre Zielgruppe die Zustellungskriterien beim Nachrichtenversand erfüllt. Sie können auch Exit-Kriterien für Canvas nutzen, um Nutzer:innen an jedem Punkt während der User Journey auszuschließen, wenn sie Ihre Kriterien erfüllen.

Für Kampagnen können Sie Exit-Events verwenden, um Kampagnen mit einem Trigger-Event zu ermöglichen, Nachrichten an Nutzer:innen abzubrechen, die das Exit-Event während der Verzögerung ausführen.

#### Eindeutige Filter mit dem Trigger-Event verwenden

Beim Konfigurieren Ihrer Filter möchten Sie möglicherweise einen redundanten Filter „zur Sicherheit" hinzufügen. Diese Redundanz kann jedoch zu mehr Problemen führen. Vermeiden Sie stattdessen nach Möglichkeit die Verwendung eines Filters, der den Trigger enthält. Dies ist der sicherste Weg, um eine Race-Condition zu vermeiden.

Wenn beispielsweise Ihr Kampagnen-Trigger „Hat einen Kauf getätigt" ist und Ihr Zielgruppen-Filter „Hat irgendeinen Kauf getätigt" lautet, kann diese Redundanz eine Race-Condition verursachen.

#### Zielgruppen-Filter vermeiden, die davon ausgehen, dass das Trigger-Event aktualisiert wurde

Diese Best Practice ähnelt der Vermeidung redundanter Filter mit dem Trigger-Event. Normalerweise schlägt ein Filter fehl, der davon ausgeht, dass das Trigger-Event im Nutzerprofil aktualisiert wurde.

#### Liquid-Abbrüche verwenden (nur Attribute)

In Kampagnen und Canvas-Schritten können Sie Liquid-Abbrüche verwenden, um die Verwendung von Zielgruppen-Filtern zu vermeiden, die die Trigger-Attribute im Entry-Zeitplan enthalten. Nehmen wir beispielsweise an, Sie haben ein Array-Attribut „Lieblingsfarben" und möchten jede Nutzer:in ansprechen, die das Attribut-Array mit einem beliebigen Wert aktualisiert und nach Abschluss des Updates auch die Farbe „Blau" im Array hat. Wenn Sie in diesem Beispiel die Zielgruppen-Filter verwenden, stoßen Sie auf eine Race-Condition und verpassen Nutzer:innen, die „Blau" zum ersten Mal zum Array hinzufügen.

In diesem Fall können Sie eine Trigger-Verzögerung in einer Kampagne implementieren oder einen Verzögerungsschritt in Canvas verwenden, um dem Nutzerprofil Zeit zur Aktualisierung zu geben, und dann die folgende Liquid-Abbruchlogik verwenden:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Bestätigen, wie Nutzerdaten verwaltet werden

Wenn während der Canvas-Entry-Auswertung eine Race-Condition auftritt, können Nutzer:innen einen Canvas betreten, den sie nicht betreten sollten. Beispielsweise könnte das Profil so eingestellt sein, dass es in die Zielgruppe aufgenommen wird, und anschließend aktualisiert werden, nachdem der Canvas die Nutzer:innen in die Warteschlange eingereiht hat, sodass sie nicht mehr für die Zielgruppe berechtigt sind.

Wenn eine Nutzer:in das Canvas-Entry-Event mehrmals innerhalb derselben Sekunde auslöst, erlaubt Braze nur einen Eintritt für diese Sekunde (auch wenn der erneute Eintritt aktiviert ist). Dies verhindert doppelte Eintritte, sodass die Gesamtzahl der Canvas-Eintritte niedriger sein kann als die Gesamtzahl der Trigger-Events.

Wir empfehlen zu bestätigen, wie Nutzerdaten verwaltet und aktualisiert werden – insbesondere wann und wie bestimmte Attribute aktualisiert werden, z. B. per SDK, API, Batch-API und anderen Methoden. Dies kann helfen zu identifizieren und zu klären, warum eine Nutzer:in eine Kampagne oder einen Canvas betreten hat, im Vergleich dazu, wann das Nutzerprofil aktualisiert wurde.