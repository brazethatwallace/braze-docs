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

## Einrichten einer getriggerten Campaign {#setting-up-a-triggered-campaign}

### Schritt 1: Trigger-Event auswählen {#step-1-select-a-trigger-event}

Wählen Sie ein Trigger-Event aus. Dies kann Folgendes umfassen:
- Eine Bestellung aufgeben
- Eine Sitzung starten
- Ein angepasstes Event durchführen
- Das primäre Konversions-Event der Campaign durchführen
- Eine E-Mail-Adresse zu einem Nutzerprofil hinzufügen
- Einen Wert eines angepassten Attributs ändern
- Einen Abo-Status aktualisieren
- Einen Abo-Gruppenstatus aktualisieren
- Mit anderen Campaigns interagieren
    - In-App-Nachricht ansehen
    - In-App-Nachricht anklicken
    - Buttons in In-App-Nachrichten anklicken
    - E-Mail anklicken
    - Alias in E-Mail anklicken
    - Alias in einer beliebigen Campaign oder einem Canvas-Schritt anklicken
    - E-Mail öffnen
    - E-Mail öffnen (maschinelle Öffnungen)
    - E-Mail öffnen (andere Öffnungen)
    - Push-Benachrichtigung direkt öffnen
    - Button einer Push-Benachrichtigung anklicken
    - Push-Story-Seite anklicken
    - Konversions-Event durchführen
    - E-Mail erhalten
    - SMS erhalten
    - Gekürzten SMS-Link anklicken
    - Push-Benachrichtigung erhalten
    - Webhook erhalten
    - In eine Kontrollgruppe aufgenommen werden
    - Content-Card ansehen
    - Content-Card anklicken
    - Content-Card schließen
- Einen Standort betreten
- Das Ausnahme-Event einer anderen Campaign durchführen
- Mit einem Canvas-Schritt interagieren
- Einen Geofence triggern
- Eine eingehende SMS senden
- Eine eingehende WhatsApp-Nachricht senden

Sie können Trigger-Events auch weiter über [angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events) von Braze filtern, die anpassbare Event-Eigenschaften für angepasste Events und In-App-Käufe ermöglichen. Mit diesem Feature können Sie weiter eingrenzen, welche Nutzer:innen eine Nachricht erhalten, basierend auf den spezifischen Attributen des angepassten Events. So wird eine stärkere Campaign-Personalisierung und eine anspruchsvollere Datenerfassung ermöglicht.

Nehmen wir zum Beispiel an, wir haben eine Campaign mit einem angepassten Event für Warenkorb-Abbruch, die zusätzlich über den Eigenschaftsfilter „Warenkorbwert“ gefiltert wird. Diese Campaign erreicht nur Nutzer:innen, die Waren im Wert zwischen 100 $ und 200 $ in ihrem Warenkorb zurückgelassen haben.

![Warenkorb-Abbruch-Campaign, gefiltert nach einer angepassten Event-Eigenschaft für den Warenkorbwert zwischen 100 $ und 200 $.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
Das Trigger-Event „Sitzung starten“ kann das allererste Öffnen der App durch Nutzer:innen sein, wenn das Segment Ihrer Campaign für neue Nutzer:innen gilt (zum Beispiel, wenn Ihr Segment aus Nutzer:innen ohne Sitzungen besteht).
{% endalert %}

Beachten Sie, dass Sie eine getriggerte Campaign weiterhin an ein bestimmtes Segment von Nutzer:innen senden können, sodass Nutzer:innen, die nicht Teil des Segments sind, die Campaign nicht erhalten, selbst wenn sie das Trigger-Event ausführen.

Bezüglich des Trigger-Events beim Hinzufügen einer E-Mail-Adresse zum Profil gelten die folgenden Regeln:

- Das Trigger-Event wird ausgelöst, nachdem das Nutzerprofilattribut aktualisiert wurde. Das bedeutet, dass die Auswertung der Segmente und Filter der Campaign nach allen Attributaktualisierungen erfolgt. Das ist vorteilhaft, da Sie so Filter wie „E-Mail-Adresse enthält gmail.com“ einrichten können, um eine Trigger-Campaign zu erstellen, die nur an Gmail-Nutzer:innen gesendet wird und sofort ausgelöst wird, wenn sie ihre E-Mail-Adresse hinzufügen.
- Das Trigger-Event wird ausgelöst, wenn eine E-Mail-Adresse zu einem Nutzerprofil hinzugefügt wird. Wenn Sie mehrere Nutzerprofile mit derselben E-Mail-Adresse erstellt haben, kann die Campaign mehrfach ausgelöst werden, einmal für jedes Nutzerprofil.

Darüber hinaus halten sich getriggerte In-App-Nachrichten weiterhin an die Zustellungsregeln für In-App-Nachrichten und erscheinen zu Beginn einer App-Sitzung.

![Aktionsbasierter Campaign-Zustellungszeitplan mit den Konfigurationsoptionen für Trigger-Events.]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Schritt 2: Verzögerungsdauer auswählen {#step-2-select-delay-length}

Wählen Sie aus, wie lange nach Erfüllung der Trigger-Kriterien mit dem Senden der Campaign gewartet werden soll. Wenn die gewählte Verzögerungsdauer länger ist als die Sendedauer der Nachricht, erhalten keine Nutzer:innen die Campaign.

In-App-Nachricht-Campaigns können die Zustellung nach dem Trigger-Event um bis zu zwei Stunden (7.200 Sekunden) verzögern. Die Verzögerungsoptionen sind **Sofort** und **Nach einer Verzögerung**. Für eine längere Wartezeit fügen Sie einen [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) vor einem In-App-Nachricht-Schritt in einem Canvas hinzu.

{% alert important %}
Braze verwendet den mit dem angepassten Event gesendeten Zeitstempel, um die Verzögerung für eine aktionsbasierte Campaign zu berechnen. Wenn dieser Zeitstempel zurückdatiert ist, kann Braze die Verzögerung als bereits abgelaufen betrachten und die Nachricht sofort oder früher als erwartet senden. Um unbeabsichtigte Zustellungszeitpunkte zu vermeiden, senden Sie den Zeitstempel des angepassten Events mit der aktuellen Uhrzeit.
{% endalert %}

Außerdem sind Nutzer:innen, die das Trigger-Event nach dem Start Ihrer Campaign abschließen, die Ersten, die die Nachricht nach Ablauf der Verzögerung erhalten. Nutzer:innen, die das Trigger-Event vor dem Start der Campaign abgeschlossen haben, sind nicht für den Erhalt der Campaign qualifiziert.

![Screenshot zu Schritt 2: Verzögerungsdauer auswählen.]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Sie können auch wählen, die Campaign an einem bestimmten Wochentag (indem Sie „am nächsten“ auswählen und dann einen Tag wählen) oder in einer bestimmten Anzahl von Tagen (indem Sie „in“ auswählen) in der Zukunft zu senden. Alternativ können Sie Ihre Nachricht mit dem Feature [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) senden, anstatt manuell einen Zustellungszeitpunkt auszuwählen.

![Sie können auch wählen, die Campaign an einem bestimmten Wochentag oder in einer bestimmten Anzahl von Tagen in der Zukunft zu senden. Alternativ können Sie das Feature „Intelligentes Timing“ verwenden, anstatt manuell einen Zustellungszeitpunkt auszuwählen.]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![Sie können auch wählen, die Campaign an einem bestimmten Wochentag oder in einer bestimmten Anzahl von Tagen in der Zukunft zu senden. Alternativ können Sie das Feature „Intelligentes Timing“ verwenden, anstatt manuell einen Zustellungszeitpunkt auszuwählen.]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Schritt 3: Ausnahme-Events auswählen {#step-3-select-exception-events}

Wählen Sie ein Ausnahme-Event aus, das Nutzer:innen vom Erhalt dieser Campaign ausschließt. Dies ist nur möglich, wenn Ihre getriggerte Nachricht nach einer Zeitverzögerung gesendet wird. [Ausnahme-Events]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) können ein Kauf, der Start einer Sitzung, die Durchführung eines der festgelegten [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) der Campaign oder die Durchführung eines angepassten Events sein. Wenn Nutzer:innen das Trigger-Event abschließen, aber dann ihr Ausnahme-Event vor dem Senden der Nachricht aufgrund der Zeitverzögerung durchführen, erhalten sie die Campaign nicht. Nutzer:innen, die die Campaign aufgrund des Ausnahme-Events nicht erhalten, sind automatisch berechtigt, sie in Zukunft zu erhalten, wenn sie das Trigger-Event das nächste Mal abschließen, auch wenn Sie keine [erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) für Nutzer:innen aktiviert haben.

![Wählen Sie ein Ausnahme-Event aus, das Nutzer:innen vom Erhalt dieser Campaign ausschließt. Ausnahme-Events können ein Kauf, der Start einer Sitzung, die Durchführung eines festgelegten Konversions-Events der Campaign oder die Durchführung eines angepassten Events sein.]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Weitere Informationen zur Verwendung von Ausnahme-Events finden Sie in unserem Abschnitt zu [Anwendungsfällen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#use-cases).

> Wenn Sie eine Campaign mit einem Trigger-Event senden, das dem Ausnahme-Event entspricht, storniert Braze die Campaign und plant automatisch eine neue Campaign basierend auf der Nachrichtenzustellungszeit des Ausnahme-Events. Wenn Ihr erstes Trigger-Event beispielsweise nach fünf Minuten beginnt und das Ausnahme-Event nach 10 Minuten, würde die 10-Minuten-Zustellungszeit des Ausnahme-Events als offizielle Nachrichtenzustellungszeit der Campaign gelten.

{% alert note %}
Sie können einen „Sitzungsstart“ nicht gleichzeitig als Trigger-Event und Ausnahme-Event für eine Campaign festlegen. Sie haben jedoch immer die Möglichkeit, ein anderes angepasstes Event außerhalb dieser Option auszuwählen.
{% endalert %}

### Schritt 4: Dauer zuweisen {#step-4-assign-duration}

Weisen Sie die Dauer der Campaign zu, indem Sie eine Startzeit und eine optionale Endzeit angeben.

![Screenshot zu Schritt 4: Dauer zuweisen.]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Wenn Nutzer:innen ein Trigger-Event innerhalb des angegebenen Zeitrahmens abschließen, sich aber aufgrund einer geplanten Verzögerung außerhalb des Zeitrahmens für die Nachricht qualifizieren, erhalten sie die Campaign nicht. Wenn Sie daher eine Zeitverzögerung festlegen, die länger als der Zeitrahmen der Nachricht ist, erhalten keine Nutzer:innen Ihre Campaign. Darüber hinaus können Sie wählen, die Nachricht in den [Ortszeiten]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) der Nutzer:innen zu senden.

### Schritt 5: Zeitfenster auswählen {#step-5-select-time-frame}

Wählen Sie aus, ob Nutzer:innen die Campaign während eines bestimmten Teils des Tages erhalten sollen. Wenn Sie der Nachricht ein Zeitfenster geben und Nutzer:innen entweder das Trigger-Event außerhalb des Zeitfensters abschließen oder die Nachrichtenverzögerung dazu führt, dass sie das Zeitfenster verpassen, erhalten Nutzer:innen Ihre Nachricht standardmäßig nicht.

![Wählen Sie aus, ob Nutzer:innen die Campaign während eines bestimmten Teils des Tages erhalten sollen. Wenn Sie der Nachricht ein Zeitfenster geben und Nutzer:innen das Trigger-Event außerhalb des Zeitfensters abschließen oder die Nachrichtenverzögerung dazu führt, dass das Zeitfenster verpasst wird, erhalten Nutzer:innen Ihre Nachricht standardmäßig nicht.]({% image_buster /assets/img_archive/schedule_triggered5.png %})

Für den Fall, dass Nutzer:innen das Trigger-Event innerhalb des Zeitfensters abschließen, die Nachrichtenverzögerung sie aber aus dem Zeitfenster fallen lässt, können Sie das folgende Kontrollkästchen aktivieren, damit diese Nutzer:innen die Campaign dennoch erhalten.

![Screenshot zu Schritt 5: Zeitfenster auswählen.]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Wenn Nutzer:innen die Nachricht nicht erhalten, weil sie das Zeitfenster verpasst haben, sind sie dennoch berechtigt, sie beim nächsten Abschließen des Trigger-Events zu erhalten, auch wenn Sie keine [erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) für Nutzer:innen aktiviert haben. Wenn Sie die erneute Berechtigung für Nutzer:innen aktivieren, können sie die Campaign jedes Mal erhalten, wenn sie das Trigger-Event abschließen, sofern sie sich innerhalb des angegebenen Zeitfensters qualifizieren.

Wenn Sie der Campaign auch eine bestimmte Dauer zugewiesen haben, müssen Nutzer:innen sich sowohl innerhalb der Dauer als auch innerhalb des bestimmten Teils des Tages qualifizieren, um die Nachricht zu erhalten.

### Schritt 6: Erneute Berechtigung festlegen {#step-6-determine-re-eligibility}

Legen Sie fest, ob Nutzer:innen für die Campaign erneut [berechtigt]({% image_buster /assets/img_archive/ReEligible.png %}) werden können. Wenn Sie Nutzer:innen die erneute Berechtigung ermöglichen, können Sie eine Zeitverzögerung festlegen, bevor sie die Campaign erneut erhalten können. Dies verhindert, dass Ihre getriggerten Campaigns als „Spam“ wahrgenommen werden.

![Screenshot zu Schritt 6: Erneute Berechtigung festlegen.]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Anwendungsfälle {#use-cases}

Getriggerte Kampagnen sind sehr effektiv für transaktionsbezogene oder leistungsbasierte Nachrichten.

Transaktionsbezogene Kampagnen umfassen Nachrichten, die gesendet werden, nachdem Nutzer:innen einen Kauf abgeschlossen oder einen Artikel in den Warenkorb gelegt haben. Letzteres ist ein gutes Beispiel für eine Kampagne, die von einem Ausnahme-Event profitieren würde. Angenommen, Ihre Kampagne erinnert Nutzer:innen an Artikel in ihrem Warenkorb, die sie noch nicht gekauft haben. Das Ausnahme-Event wäre in diesem Fall der Kauf der Produkte im Warenkorb. Für leistungsbasierte Kampagnen können Sie eine Nachricht 5 Minuten nach Abschluss einer Konversion oder dem Erreichen eines Spiellevels senden.

Darüber hinaus können Sie beim Erstellen von Willkommenskampagnen Nachrichten triggern, die gesendet werden, nachdem sich Nutzer:innen registriert oder ein Konto eingerichtet haben. Indem Sie Nachrichten zeitversetzt an verschiedenen Tagen nach der Registrierung versenden, können Sie einen umfassenden Onboarding-Prozess aufbauen.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was ist die maximale Verzögerung nach einem Trigger für In-App-Nachricht-Kampagnen? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

In-App-Nachricht-Kampagnen können die Zustellung nach dem Trigger-Event um bis zu zwei Stunden (7.200 Sekunden) verzögern. Die Verzögerungsoptionen sind **Sofort** und **Nach einer Verzögerung**. Für eine längere Wartezeit fügen Sie einen [Verzögerungs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Schritt vor einem In-App-Nachricht-Schritt in einem Canvas hinzu.

### Warum hat ein:e Nutzer:in meine getriggerte Campaign nicht erhalten? {#why-did-a-user-not-receive-my-triggered-campaign}

Jeder der folgenden Punkte kann dazu führen, dass ein:e Nutzer:in, die/der das Trigger-Event abgeschlossen hat, die Campaign nicht erhält:

- Die/der Nutzer:in hat das Ausnahme-Event abgeschlossen, bevor die Verzögerungszeit vollständig abgelaufen war.
- Es wurde Liquid-[`abort_message`-Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) verwendet, und die Nachricht wurde basierend auf der `abort_message`-Logik oder den Regeln abgebrochen.
- Die Verzögerung führte dazu, dass die/der Nutzer:in erst nach Ablauf der Dauer für die Campaign qualifiziert wurde.
- Die Verzögerung führte dazu, dass die/der Nutzer:in außerhalb des angegebenen Tagesabschnitts für die Campaign qualifiziert wurde.
- Die/der Nutzer:in hat die Campaign bereits erhalten (einschließlich Attribution über gemeinsam genutzte Kanal-Bezeichner – zum Beispiel, wenn sie/er eine E-Mail mit jemandem teilt, der sie erhalten, geöffnet oder angeklickt hat), und Nutzer:innen werden nicht erneut berechtigt.
- Obwohl Nutzer:innen erneut berechtigt sind, die Campaign zu erhalten, können sie diese erst nach einer bestimmten Zeitspanne erneut triggern, und diese Zeitspanne ist noch nicht abgelaufen.

Die [Segmentierung]({{site.baseurl}}/user_guide/audience/segments) einer getriggerten Campaign anhand von Nutzerdaten, die zum Zeitpunkt des Events erfasst wurden, kann zu einer [Race-Condition]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions) führen. Dies passiert, wenn das Nutzerattribut, auf dem die Campaign segmentiert ist, geändert wird, die Änderung aber noch nicht für die/den Nutzer:in verarbeitet wurde, wenn die Campaign gesendet wird. Da Campaigns die Segment-Zugehörigkeit beim Eintritt prüfen, kann dies dazu führen, dass die/der Nutzer:in die Campaign nicht erhält.

Stellen Sie sich zum Beispiel vor, Sie möchten eine event-getriggerte Campaign an männliche Nutzer:innen senden, die sich gerade registriert haben. Wenn sich die/der Nutzer:in registriert, erfassen Sie ein angepasstes Event `registration` und setzen gleichzeitig das `gender`-Attribut der/des Nutzer:in. Das Event kann die Campaign triggern, bevor Braze das Geschlecht der/des Nutzer:in verarbeitet hat, was dazu führt, dass sie/er die Campaign nicht erhält.

Als Best Practice sollten Sie sicherstellen, dass das Attribut, auf dem die Campaign segmentiert ist, an die Braze-Server übermittelt wird, bevor das Event ausgelöst wird. Wenn dies nicht möglich ist, ist der beste Weg, die Zustellung sicherzustellen, die Verwendung von [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties), um die relevanten Nutzer-Eigenschaften an das Event anzuhängen und einen Eigenschaftsfilter für die spezifische Event-Eigenschaft anstelle eines Segmentierungsfilters anzuwenden. In unserem Beispiel würden Sie dem angepassten Event `registration` eine `gender`-Eigenschaft hinzufügen, damit Braze garantiert die benötigten Daten hat, wenn Ihre Campaign getriggert wird.

Zusätzlich können Sie bei einer aktionsbasierten Campaign mit Verzögerung die Option **Segment-Zugehörigkeit zum Sendezeitpunkt erneut prüfen** aktivieren, um sicherzustellen, dass die Nutzer:innen zum Sendezeitpunkt noch Teil der Zielgruppe sind.

#### Bewertung der Zielgruppenkriterien {#audience-criteria-evaluation}

Bei Campaigns mit einer Verzögerung vor dem Versand (einschließlich Rate-Limiting, Ortszeit, intelligentem Timing oder einem Trigger-Zeitplan) hängt der Zeitpunkt der erneuten Segment-Bewertung vom Campaign-Typ und den Einstellungen ab.

Wenn Sie bei aktionsbasierten Campaigns mit Verzögerung die Option **Segment-Zugehörigkeit zum Sendezeitpunkt erneut prüfen** auswählen, werden die Nutzer:innen vor dem Versand der Nachricht erneut bewertet, sodass nur Nutzer:innen, die zum Sendezeitpunkt noch die Segment-Kriterien erfüllen, die Nachricht erhalten.

Wenn Ihre Campaign durch ein bestimmtes angepasstes Event getriggert wird und Sie ein Segment als Zielgruppe auswählen, müssen die Nutzer:innen dasselbe angepasste Event ausführen, um in das Segment aufgenommen zu werden. Das bedeutet, dass Nutzer:innen Teil der Zielgruppe sein müssen, bevor eine aktionsbasierte Campaign getriggert werden kann. Der allgemeine Ablauf für eine getriggerte Campaign ist wie folgt:

1. **Der Zielgruppe beitreten:** Wenn ein:e Nutzer:in das angepasste Event ausführt, wird sie/er zur Zielgruppe der Campaign hinzugefügt.
2. **Die E-Mail triggern:** Ein:e Nutzer:in muss das angepasste Event erneut ausführen, um die E-Mail zu triggern, da sie/er Teil der Zielgruppe sein muss, bevor die E-Mail gesendet werden kann.

Wir empfehlen, entweder die Zielgruppe so zu ändern, dass alle Nutzer:innen eingeschlossen werden, oder zu überprüfen, ob die Nutzer:innen, von denen erwartet wird, dass sie das Event ausführen, bereits Teil der Campaign-Zielgruppe sind, damit die Nachricht getriggert werden kann.

![Screenshot zur Bewertung der Zielgruppenkriterien.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Fehlerbehebung bei angepassten Events {#troubleshooting-custom-events}

Bestätigen Sie zunächst, dass das angepasste Event an Braze übergeben wird. Gehen Sie zu **Analytics** > **Bericht zu angepassten Events**, und wählen Sie dann das entsprechende angepasste Event und den Zeitraum aus. Wenn das Event nicht angezeigt wird, bestätigen Sie, dass es korrekt eingerichtet ist und die/der Nutzer:in die richtige Aktion ausgeführt hat.

Wenn das angepasste Event angezeigt wird, führen Sie folgende weitere Schritte zur Fehlerbehebung durch:

- Prüfen Sie den Profil-Download der/des Nutzer:in, um zu bestätigen, dass sie/er das Event getriggert hat und wann dies geschehen ist. Wenn das Event getriggert wurde, vergleichen Sie den Zeitstempel, wann das Event getriggert wurde, mit dem Zeitpunkt, zu dem die Campaign live ging. Das Event wurde möglicherweise getriggert, bevor die Campaign live war.
- Überprüfen Sie die Changelogs der Campaign und aller beim Targeting verwendeten Segmente, um festzustellen, ob die/der Nutzer:in zum Zeitpunkt des Triggerns ihres/seines angepassten Events im Segment war. Wenn sie/er nicht im Segment war, hätte sie/er die Campaign nicht erhalten.
- Überprüfen Sie, ob die/der Nutzer:in durch Segmentierung in eine Kontrollgruppe aufgenommen wurde und daher am Erhalt der Campaign gehindert wurde.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event der/des Nutzer:in vor der Verzögerung getriggert wurde. Wenn das Event vor der Verzögerung getriggert wurde, hätte sie/er die Campaign nicht erhalten.

{% alert note %}
In-App-Nachrichten können nur durch Events getriggert werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

### Wann bewerten aktionsbasierte Campaigns die Zielgruppen-Zugehörigkeit? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze bewertet die Zielgruppen-Zugehörigkeit, wenn es das Trigger-Event verarbeitet, bevor die Nachricht gesendet wird. Standardmäßig prüft Braze, ob die/der Nutzer:in zum Zeitpunkt des Einreihens in die Warteschlange zur Zielgruppe gehört. Wenn die Campaign eine Verzögerung hat, können Sie die Option **Segment-Zugehörigkeit zum Sendezeitpunkt erneut prüfen** auswählen, um die Zielgruppenkriterien unmittelbar vor dem Versand erneut zu prüfen – zum Beispiel, wenn ein:e Nutzer:in die Trigger-Aktion ausführen und dann die Zielgruppe verlassen könnte, bevor der Versand abgeschlossen ist.

Weitere Informationen finden Sie unter [Bewertung der Zielgruppenkriterien](#audience-criteria-evaluation).