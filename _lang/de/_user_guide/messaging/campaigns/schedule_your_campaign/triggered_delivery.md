---
nav_title: Aktionsbasierte Zustellung
article_title: Aktionsbasierte Zustellung
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Kampagnen so einrichten, dass sie nach Abschluss eines bestimmten Events durch Nutzer:innen gesendet werden."
tool: Campaigns

---

# Aktionsbasierte Zustellung {#action-based-delivery}

> Kampagnen mit aktionsbasierter Zustellung oder Event-getriggerte Kampagnen sind sehr effektiv für transaktionale oder leistungsbasierte Nachrichten. Anstatt Ihre Kampagne an bestimmten Tagen zu senden, können Sie sie so einrichten, dass sie nach Abschluss eines bestimmten Events durch Nutzer:innen getriggert werden.

## Eine getriggerte Kampagne einrichten {#setting-up-a-triggered-campaign}

### 1. Schritt: Trigger-Event auswählen {#step-1-select-a-trigger-event}

Wählen Sie ein Trigger-Event aus. Dies kann Folgendes umfassen:
- Einen Kauf tätigen
- Eine Sitzung starten
- Ein angepasstes Event ausführen
- Das primäre Konversions-Event der Kampagne ausführen
- Eine E-Mail-Adresse zu einem Nutzerprofil hinzufügen
- Einen angepassten Attributwert ändern
- Einen Abo-Status aktualisieren
- Einen Abo-Gruppenstatus aktualisieren
- Mit anderen Kampagnen interagieren
    - In-App-Nachricht ansehen
    - In-App-Nachricht anklicken
    - Buttons der In-App-Nachricht anklicken
    - E-Mail anklicken
    - Alias in E-Mail anklicken
    - Alias in einer beliebigen Kampagne oder einem Canvas-Schritt angeklickt
    - E-Mail öffnen
    - E-Mail öffnen (maschinelle Öffnungen)
    - E-Mail öffnen (andere Öffnungen)
    - Push-Benachrichtigung direkt öffnen
    - Button der Push-Benachrichtigung anklicken
    - Push-Story-Seite anklicken
    - Konversions-Event ausführen
    - E-Mail erhalten
    - SMS erhalten
    - Verkürzten SMS-Link anklicken
    - Push-Benachrichtigung erhalten
    - Webhook erhalten
    - In Kontrollgruppe aufgenommen werden
    - Content-Card ansehen
    - Content-Card anklicken
    - Content-Card schließen
- Einen Standort betreten
- Das Ausnahme-Event einer anderen Kampagne ausführen
- Mit einem Canvas-Schritt interagieren
- Einen Geofence triggern
- Eine eingehende SMS-Nachricht senden
- Eine eingehende WhatsApp-Nachricht senden

Sie können Trigger-Events zusätzlich über [angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events) von Braze filtern, was anpassbare Event-Eigenschaften für angepasste Events und In-App-Käufe ermöglicht. Dieses Feature erlaubt es Ihnen, genauer festzulegen, welche Nutzer:innen eine Nachricht erhalten – basierend auf den spezifischen Attributen des angepassten Events. So erreichen Sie eine stärkere Personalisierung Ihrer Kampagnen und eine differenziertere Datenerfassung.

Nehmen wir zum Beispiel an, wir haben eine Kampagne mit einem angepassten Event für Warenkorb-Abbruch, die zusätzlich durch den Eigenschaftsfilter „Warenkorbwert“ eingeschränkt wird. Diese Kampagne erreicht nur Nutzer:innen, die Waren im Wert von 100 bis 200 $ in ihrem Warenkorb zurückgelassen haben.

![Warenkorb-Abbruch-Kampagne, gefiltert nach einer angepassten Event-Eigenschaft für einen Warenkorbwert zwischen 100 und 200 $.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
Das Trigger-Event „Sitzung starten“ kann das allererste Öffnen der App sein, wenn das Segment Ihrer Kampagne auf neue Nutzer:innen zutrifft (z. B. wenn Ihr Segment aus Nutzer:innen ohne Sitzungen besteht).
{% endalert %}

Beachten Sie, dass Sie eine getriggerte Kampagne weiterhin an ein bestimmtes Segment von Nutzer:innen senden können. Nutzer:innen, die nicht Teil des Segments sind, erhalten die Kampagne also nicht, selbst wenn sie das Trigger-Event abschließen.

Bezüglich des Trigger-Events, wenn Nutzer:innen eine E-Mail-Adresse zu ihrem Profil hinzufügen, gelten folgende Regeln:

- Das Trigger-Event wird ausgelöst, nachdem das Nutzerprofilattribut aktualisiert wurde. Das bedeutet, dass die Auswertung der Segmente und Filter der Kampagne nach allen Attribut-Updates erfolgt. Dies ist vorteilhaft, da Sie Filter wie „E-Mail-Adresse enthält gmail.com“ einrichten können, um eine Trigger-Kampagne zu erstellen, die nur an Gmail-Nutzer:innen gesendet wird und sofort ausgelöst wird, wenn diese ihre E-Mail-Adresse hinzufügen.
- Das Trigger-Event wird ausgelöst, wenn eine E-Mail-Adresse zu einem Nutzerprofil hinzugefügt wird. Wenn Sie mehrere Nutzerprofile mit derselben E-Mail-Adresse erstellt haben, kann die Kampagne mehrfach ausgelöst werden – einmal für jedes Nutzerprofil.

Darüber hinaus halten sich getriggerte In-App-Nachrichten weiterhin an die Zustellungsregeln für In-App-Nachrichten und erscheinen zu Beginn einer App-Sitzung.

![Zeitplan für aktionsbasierte Kampagnenzustellung mit Konfigurationsoptionen für Trigger-Events.]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### 2. Schritt: Verzögerungsdauer auswählen {#step-2-select-delay-length}

Wählen Sie aus, wie lange nach Erfüllung der Trigger-Kriterien gewartet werden soll, bevor die Kampagne gesendet wird. Wenn die gewählte Verzögerungsdauer länger ist als der Sendezeitraum der Nachricht, erhalten keine Nutzer:innen die Kampagne.

{% alert important %}
Braze verwendet den mit dem angepassten Event gesendeten Zeitstempel, um die Verzögerung für eine aktionsbasierte Kampagne zu berechnen. Wenn dieser Zeitstempel rückdatiert ist, kann Braze die Verzögerung als bereits abgelaufen betrachten und die Nachricht sofort oder früher als erwartet senden. Um unbeabsichtigte Zustellungszeitpunkte zu vermeiden, senden Sie den Zeitstempel des angepassten Events mit der aktuellen Uhrzeit.
{% endalert %}

Zusätzlich sind die ersten Nutzer:innen, die die Nachricht nach Ablauf der Verzögerung erhalten, diejenigen, die das Trigger-Event nach dem Start Ihrer Kampagne abgeschlossen haben. Nutzer:innen, die das Trigger-Event vor dem Kampagnenstart abgeschlossen haben, qualifizieren sich nicht für den Empfang der Kampagne.

![Screenshot zu Schritt 2: Verzögerungsdauer auswählen.]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Sie können auch wählen, die Kampagne an einem bestimmten Wochentag zu senden (indem Sie „am nächsten“ und dann einen Tag auswählen) oder nach einer bestimmten Anzahl von Tagen (indem Sie „in“ auswählen). Alternativ können Sie Ihre Nachricht mit dem Feature [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) senden, anstatt manuell einen Zustellungszeitpunkt auszuwählen.

![Sie können auch wählen, die Kampagne an einem bestimmten Wochentag zu senden (indem Sie „am nächsten“ und dann einen Tag auswählen) oder nach einer bestimmten Anzahl von Tagen (indem Sie „in“ auswählen). Alternativ können Sie Ihre Nachricht mit dem Feature „Intelligentes Timing“ senden, anstatt manuell einen Zustellungszeitpunkt auszuwählen.]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![Sie können auch wählen, die Kampagne an einem bestimmten Wochentag zu senden (indem Sie „am nächsten“ und dann einen Tag auswählen) oder nach einer bestimmten Anzahl von Tagen (indem Sie „in“ auswählen). Alternativ können Sie Ihre Nachricht mit dem Feature „Intelligentes Timing“ senden, anstatt manuell einen Zustellungszeitpunkt auszuwählen.]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### 3. Schritt: Ausnahme-Events auswählen {#step-3-select-exception-events}

Wählen Sie ein Ausnahme-Event aus, das Nutzer:innen vom Empfang dieser Kampagne ausschließt. Dies ist nur möglich, wenn Ihre getriggerte Nachricht nach einer Zeitverzögerung gesendet wird. [Ausnahme-Events]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) können ein Kauf, der Start einer Sitzung, die Ausführung eines der festgelegten [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) einer Kampagne oder die Ausführung eines angepassten Events sein. Wenn Nutzer:innen das Trigger-Event abschließen, aber dann vor dem Nachrichtenversand aufgrund der Zeitverzögerung das Ausnahme-Event ausführen, erhalten sie die Kampagne nicht. Nutzer:innen, die die Kampagne aufgrund des Ausnahme-Events nicht erhalten, sind automatisch berechtigt, sie in Zukunft zu erhalten, wenn sie das nächste Mal das Trigger-Event abschließen – auch wenn Sie keine [erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) aktiviert haben.

![Wählen Sie ein Ausnahme-Event aus, das Nutzer:innen vom Empfang dieser Kampagne ausschließt. Dies ist nur möglich, wenn Ihre getriggerte Nachricht nach einer Zeitverzögerung gesendet wird. Ausnahme-Events können ein Kauf, der Start einer Sitzung, die Ausführung eines der festgelegten Konversions-Events einer Kampagne oder die Ausführung eines angepassten Events sein. Wenn Nutzer:innen das Trigger-Event abschließen, aber dann vor dem Nachrichtenversand aufgrund der Zeitverzögerung das Ausnahme-Event ausführen, erhalten sie die Kampagne nicht. Nutzer:innen, die die Kampagne aufgrund des Ausnahme-Events nicht erhalten, sind automatisch berechtigt, sie in Zukunft zu erhalten, wenn sie das nächste Mal das Trigger-Event abschließen – auch wenn Sie keine erneute Berechtigung aktiviert haben.]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Weitere Informationen zur Verwendung von Ausnahme-Events finden Sie in unserem Abschnitt zu [Anwendungsfällen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#use-cases).

> Wenn Sie eine Kampagne mit einem Trigger-Event senden, das dem Ausnahme-Event entspricht, storniert Braze die Kampagne und plant automatisch eine neue Kampagne basierend auf dem Zustellungszeitpunkt des Ausnahme-Events. Wenn Ihr erstes Trigger-Event beispielsweise bei fünf Minuten beginnt und das Ausnahme-Event bei 10 Minuten, wird der Zustellungszeitpunkt des Ausnahme-Events von 10 Minuten als offizieller Zustellungszeitpunkt der Kampagne verwendet.

{% alert note %}
Sie können „Sitzungsstart“ nicht gleichzeitig als Trigger-Event und Ausnahme-Event für eine Kampagne festlegen. Sie haben jedoch immer die Möglichkeit, ein anderes angepasstes Event außerhalb dieser Option auszuwählen.
{% endalert %}

### 4. Schritt: Dauer festlegen {#step-4-assign-duration}

Legen Sie die Dauer der Kampagne fest, indem Sie eine Startzeit und eine optionale Endzeit angeben.

![Screenshot zu Schritt 4: Dauer festlegen.]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Wenn Nutzer:innen ein Trigger-Event innerhalb des festgelegten Zeitraums abschließen, sich aber aufgrund einer geplanten Verzögerung erst außerhalb des Zeitraums für die Nachricht qualifizieren, erhalten sie die Kampagne nicht. Wenn Sie also eine Zeitverzögerung festlegen, die länger als der Nachrichtenzeitraum ist, erhalten keine Nutzer:innen Ihre Kampagne. Darüber hinaus können Sie wählen, die Nachricht in der [Ortszeit]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) der Nutzer:innen zu senden.

### 5. Schritt: Zeitfenster auswählen {#step-5-select-time-frame}

Wählen Sie aus, ob Nutzer:innen die Kampagne während eines bestimmten Tagesabschnitts erhalten sollen. Wenn Sie der Nachricht ein Zeitfenster zuweisen und Nutzer:innen entweder das Trigger-Event außerhalb des Zeitfensters abschließen oder die Nachrichtenverzögerung dazu führt, dass sie das Zeitfenster verpassen, erhalten sie Ihre Nachricht standardmäßig nicht.

![Wählen Sie aus, ob Nutzer:innen die Kampagne während eines bestimmten Tagesabschnitts erhalten sollen. Wenn Sie der Nachricht ein Zeitfenster zuweisen und Nutzer:innen entweder das Trigger-Event außerhalb des Zeitfensters abschließen oder die Nachrichtenverzögerung dazu führt, dass sie das Zeitfenster verpassen, erhalten sie Ihre Nachricht standardmäßig nicht.]({% image_buster /assets/img_archive/schedule_triggered5.png %})

Falls Nutzer:innen das Trigger-Event innerhalb des Zeitfensters abschließen, die Nachrichtenverzögerung sie aber aus dem Zeitfenster herausfallen lässt, können Sie das folgende Kontrollkästchen aktivieren, damit diese Nutzer:innen die Kampagne trotzdem erhalten.

![Screenshot zu Schritt 5: Zeitfenster auswählen.]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Wenn Nutzer:innen die Nachricht nicht erhalten, weil sie das Zeitfenster verpasst haben, sind sie trotzdem berechtigt, sie beim nächsten Abschluss des Trigger-Events zu erhalten – auch wenn Sie keine [erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) aktiviert haben. Wenn Sie die erneute Berechtigung aktivieren, können Nutzer:innen die Kampagne jedes Mal erhalten, wenn sie das Trigger-Event abschließen, vorausgesetzt, sie qualifizieren sich innerhalb des festgelegten Zeitfensters.

Wenn Sie der Kampagne auch eine bestimmte Dauer zugewiesen haben, müssen Nutzer:innen sich sowohl innerhalb der Dauer als auch innerhalb des spezifischen Tagesabschnitts qualifizieren, um die Nachricht zu erhalten.

### 6. Schritt: Erneute Berechtigung festlegen {#step-6-determine-re-eligibility}

Legen Sie fest, ob Nutzer:innen [erneut berechtigt]({% image_buster /assets/img_archive/ReEligible.png %}) für die Kampagne werden können. Wenn Sie die erneute Berechtigung zulassen, können Sie eine Zeitverzögerung festlegen, bevor Nutzer:innen die Kampagne erneut erhalten können. Dies verhindert, dass Ihre getriggerten Kampagnen als „Spam“ wahrgenommen werden.

![Screenshot zu Schritt 6: Erneute Berechtigung festlegen.]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Anwendungsfälle {#use-cases}

Getriggerte Kampagnen sind sehr effektiv für transaktionale oder leistungsbasierte Nachrichten.

Transaktionale Kampagnen umfassen Nachrichten, die gesendet werden, nachdem Nutzer:innen einen Kauf getätigt oder einen Artikel in ihren Warenkorb gelegt haben. Letzterer Fall ist ein gutes Beispiel für eine Kampagne, die von einem Ausnahme-Event profitiert. Angenommen, Ihre Kampagne erinnert Nutzer:innen an Artikel in ihrem Warenkorb, die sie noch nicht gekauft haben. Das Ausnahme-Event wäre in diesem Fall der Kauf der Produkte im Warenkorb. Für leistungsbasierte Kampagnen können Sie eine Nachricht 5 Minuten nach Abschluss einer Conversion oder dem Bestehen eines Spiellevels senden.

Darüber hinaus können Sie beim Erstellen von Willkommenskampagnen Nachrichten so einrichten, dass sie nach der Registrierung oder Kontoeinrichtung gesendet werden. Durch zeitversetztes Senden von Nachrichten an verschiedenen Tagen nach der Registrierung können Sie einen umfassenden Onboarding-Prozess gestalten.

## Warum hat ein:e Nutzer:in meine getriggerte Kampagne nicht erhalten? {#why-did-a-user-not-receive-my-triggered-campaign}

Jeder der folgenden Punkte kann verhindern, dass Nutzer:innen, die das Trigger-Event abgeschlossen haben, die Kampagne erhalten:

- Die Nutzer:innen haben das Ausnahme-Event abgeschlossen, bevor die Zeitverzögerung vollständig abgelaufen war.
- Die Liquid-Logik [`abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) wurde verwendet und die Nachricht wurde basierend auf der `abort_message`-Logik oder den Regeln abgebrochen.
- Die Zeitverzögerung hat dazu geführt, dass sich die Nutzer:innen erst nach Ablauf der Dauer für die Kampagne qualifiziert haben.
- Die Zeitverzögerung hat dazu geführt, dass sich die Nutzer:innen außerhalb des festgelegten Tagesabschnitts für die Kampagne qualifiziert haben.
- Die Nutzer:innen haben die Kampagne bereits erhalten (einschließlich Attribution über gemeinsame Kanal-Bezeichner – z. B. wenn sie eine E-Mail-Adresse mit jemandem teilen, der die Nachricht erhalten, geöffnet oder angeklickt hat), und die erneute Berechtigung ist nicht aktiviert.
- Obwohl Nutzer:innen erneut berechtigt sind, die Kampagne zu erhalten, können sie diese erst nach einer bestimmten Zeitspanne erneut triggern, und diese Zeitspanne ist noch nicht abgelaufen.

Die [Segmentierung]({{site.baseurl}}/user_guide/audience/segments) einer getriggerten Kampagne basierend auf Nutzerdaten, die zum Zeitpunkt des Events erfasst wurden, kann eine [Race-Condition]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions) verursachen. Dies geschieht, wenn das Nutzerattribut, auf dem die Kampagne segmentiert ist, geändert wird, die Änderung aber noch nicht verarbeitet wurde, wenn die Kampagne gesendet wird. Da Kampagnen die Segmentzugehörigkeit beim Eintritt prüfen, kann dies dazu führen, dass Nutzer:innen die Kampagne nicht erhalten.

Stellen Sie sich zum Beispiel vor, Sie möchten eine Event-getriggerte Kampagne an männliche Nutzer senden, die sich gerade registriert haben. Bei der Registrierung erfassen Sie ein angepasstes Event `registration` und setzen gleichzeitig das Attribut `gender` der Nutzer:innen. Das Event kann die Kampagne triggern, bevor Braze das Geschlecht der Nutzer:innen verarbeitet hat, was dazu führt, dass sie die Kampagne nicht erhalten.

Als Best Practice sollten Sie sicherstellen, dass das Attribut, auf dem die Kampagne segmentiert ist, an die Braze-Server übermittelt wird, bevor das Event gesendet wird. Wenn dies nicht möglich ist, ist der beste Weg zur Sicherstellung der Zustellung die Verwendung von [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#custom-event-properties), um die relevanten Nutzereigenschaften an das Event anzuhängen und einen Eigenschaftsfilter für die spezifische Event-Eigenschaft anstelle eines Segmentierungsfilters anzuwenden. In unserem Beispiel würden Sie dem angepassten Event `registration` eine `gender`-Eigenschaft hinzufügen, damit Braze garantiert über die benötigten Daten verfügt, wenn Ihre Kampagne getriggert wird.

Wenn eine Kampagne aktionsbasiert ist und eine Verzögerung hat, können Sie zusätzlich die Option **Segmentzugehörigkeit zum Sendezeitpunkt erneut prüfen** aktivieren, um sicherzustellen, dass Nutzer:innen zum Zeitpunkt des Nachrichtenversands noch Teil der Zielgruppe sind.

### Auswertung der Zielgruppenkriterien {#audience-criteria-evaluation}

Bei Kampagnen mit einer Verzögerung vor dem Versand (einschließlich Rate-Limiting, Ortszeit, intelligentem Timing oder einem Trigger-Zeitplan) hängt der Zeitpunkt der erneuten Segmentauswertung vom Kampagnentyp und den Einstellungen ab.

Bei aktionsbasierten Kampagnen mit Verzögerung werden Nutzer:innen, wenn Sie **Segmentzugehörigkeit zum Sendezeitpunkt erneut prüfen** auswählen, vor dem Nachrichtenversand erneut ausgewertet, sodass nur Nutzer:innen die Nachricht erhalten, die zum Sendezeitpunkt noch die Segmentkriterien erfüllen.

Wenn Ihre Kampagne durch ein bestimmtes angepasstes Event getriggert wird und Sie ein Segment als Zielgruppe auswählen, müssen Nutzer:innen dasselbe angepasste Event ausführen, um in das Segment aufgenommen zu werden. Das bedeutet, dass Nutzer:innen Teil der Zielgruppe sein müssen, bevor eine aktionsbasierte Kampagne getriggert werden kann. Der allgemeine Ablauf für eine getriggerte Kampagne ist wie folgt:

1. **Der Zielgruppe beitreten:** Wenn Nutzer:innen das angepasste Event ausführen, werden sie zur Zielgruppe der Kampagne hinzugefügt.
2. **E-Mail triggern:** Nutzer:innen müssen das angepasste Event erneut ausführen, um die E-Mail zu triggern, da sie Teil der Zielgruppe sein müssen, bevor die E-Mail gesendet werden kann.

Wir empfehlen, entweder die Zielgruppe so zu ändern, dass alle Nutzer:innen eingeschlossen sind, oder sicherzustellen, dass die Nutzer:innen, von denen erwartet wird, dass sie das Event ausführen, bereits Teil der Kampagnenzielgruppe sind, damit die Nachricht getriggert wird.

![Screenshot zur Auswertung der Zielgruppenkriterien.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Fehlerbehebung bei angepassten Events {#troubleshooting-custom-events}

Bestätigen Sie zunächst, dass das angepasste Event an Braze übermittelt wird. Gehen Sie zu **Analytics** > **Bericht zu angepassten Events**, und wählen Sie dann das entsprechende angepasste Event und den Zeitraum aus. Wenn das Event nicht angezeigt wird, überprüfen Sie, ob es korrekt eingerichtet ist und ob die Nutzer:innen die richtige Aktion ausgeführt haben.

Wenn das angepasste Event angezeigt wird, führen Sie die folgenden weiteren Schritte zur Fehlerbehebung durch:

- Überprüfen Sie den Profildownload der Nutzer:innen, um zu bestätigen, dass sie das Event getriggert haben und wann dies geschehen ist. Wenn das Event getriggert wurde, vergleichen Sie den Zeitstempel des Event-Triggers mit dem Zeitpunkt, zu dem die Kampagne live ging. Das Event könnte vor dem Kampagnenstart getriggert worden sein.
- Überprüfen Sie die Changelogs der Kampagne und aller beim Targeting verwendeten Segmente, um festzustellen, ob die Nutzer:innen zum Zeitpunkt des Triggers ihres angepassten Events im Segment waren. Wenn sie nicht im Segment waren, hätten sie die Kampagne nicht erhalten.
- Überprüfen Sie, ob die Nutzer:innen durch Segmentierung in eine Kontrollgruppe aufgenommen wurden und dadurch am Empfang der Kampagne gehindert wurden.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event der Nutzer:innen vor der Verzögerung getriggert wurde. Wenn das Event vor der Verzögerung getriggert wurde, hätten sie die Kampagne nicht erhalten.

{% alert note %}
In-App-Nachrichten können nur durch Events getriggert werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}