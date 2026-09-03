---
nav_title: Aktionsbasierte Zustellung
article_title: Aktionsbasierte Zustellung
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Kampagnen so einrichten, dass sie nach Abschluss eines bestimmten Events durch Nutzer:innen gesendet werden."
tool: Campaigns
local_redirect:
  use-cases: '/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#examples'

---

# Aktionsbasierte Zustellung {#action-based-delivery}

> Kampagnen mit aktionsbasierter Zustellung oder Event-getriggerte Kampagnen sind sehr effektiv für transaktionale oder leistungsbasierte Nachrichten. Anstatt Ihre Kampagne an bestimmten Tagen zu senden, können Sie sie so einrichten, dass sie nach Abschluss eines bestimmten Events durch Nutzer:innen getriggert werden.

## Eine getriggerte Campaign einrichten {#setting-up-a-triggered-campaign}

### Schritt 1: Trigger-Event auswählen {#step-1-select-a-trigger-event}

Wählen Sie ein Trigger-Event aus. Events sind nach Kategorie geordnet und stehen je nach Ihrem Workspace und den aktivierten Kanälen zur Verfügung.

- **E-Commerce**
    - **Place Order**
    - **Perform Cart Updated Event**
    - **Perform Checkout Started Event**
    - **Perform Checkout Completed Event**
    - **Make Purchase**
- **Allgemeine Aktivität**
    - **Interact With Campaign**
    - **Interact With Step**
    - **Interact with Landing Page**
    - **Perform Conversion Event**
    - **Perform Custom Event**
    - **Perform Exception Event For Campaign**
    - **Start Session**
- **Eingehende Nachrichten**
    - **Send an SMS inbound message**
    - **Send a WhatsApp inbound message**
    - **Send a LINE inbound message**
- **Standort**
    - **Enter a Location**
    - **Trigger a Geofence**
- **Profilaktualisierungen**
    - **Add an Email Address**
    - **Change Custom Attribute Value**
    - **Update Subscription Status**
    - **Update Subscription Group Status**

Die Gruppe **E-Commerce** listet auch empfohlene E-Commerce-Events auf, wie z. B. **Perform Product Viewed Event**, **Perform Order Cancelled Event** und **Perform Order Refunded Event**. Diese Optionen verwenden **Perform Custom Event** mit einem vorausgefüllten Event-Namen.

In-App-Nachricht-Kampagnen unterstützen eine kleinere Auswahl an Triggern: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event** und **Interact With Campaign**. Für In-App-Nachricht-Kampagnen deckt **Interact With Campaign** nur das Öffnen einer Push-Benachrichtigung aus einer beliebigen oder bestimmten Campaign ab. Die folgende Liste der Campaign-Interaktionen ist dabei nicht enthalten.

Für Kampagnen, die keine In-App-Nachrichten sind, wählen Sie bei **Interact With Campaign**, **Interact With Step** oder **Interact with Landing Page** die Interaktion aus, die den Trigger auslösen soll. Jeder dieser Trigger bietet eigene Interaktionen, und die verfügbaren Interaktionen hängen von Ihren aktivierten Kanälen ab.

{% details Interaktionen für „Interact With Campaign“ %}

- **View in-app message**
- **Click in-app message**
- **Click in-app message button 1**
- **Click in-app message button 2**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Perform conversion event**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Click shortened SMS link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**
- **Are enrolled in control group**

{% enddetails %}

{% details Interaktionen für „Interact With Step“ %}

- **View in-app message**
- **Start in-app message availability window**
- **Submit in-app message survey**
- **Click email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Click alias in email**
- **Clicked Alias in any campaign or canvas step**
- **Directly open push notification**
- **Click push notification button**
- **Click push story page**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Click shortened SMS link**
- **View content card**
- **Click content card**
- **Dismiss content card**
- **View banner**
- **Click banner**
- **Dismiss banner**
- **Click tracked WhatsApp link**
- **Click tracked LINE link**
- **Click tracked KakaoTalk link**

{% enddetails %}

{% details Interaktionen für „Interact with Landing Page“ %}

- **Submit form**
- **Submit survey**

{% enddetails %}

Sie können Trigger-Events auch mithilfe von [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events) in Braze weiter filtern, was anpassbare Event-Eigenschaften für angepasste Events und In-App-Käufe ermöglicht. Mit diesem Feature können Sie genauer festlegen, welche Nutzer:innen eine Nachricht erhalten – basierend auf den spezifischen Attributen des angepassten Events. Das ermöglicht eine stärkere Personalisierung der Campaign und eine differenziertere Datenerfassung.

Nehmen wir zum Beispiel an, wir haben eine Campaign mit einem angepassten Warenkorb-Abbruch-Event, das zusätzlich durch den Eigenschaftsfilter „Warenkorbwert“ eingegrenzt wird. Diese Campaign erreicht nur Nutzer:innen, die Waren im Wert von 100 bis 200 $ in ihrem Warenkorb zurückgelassen haben.

![Warenkorb-Abbruch-Campaign, gefiltert nach einer angepassten Event-Eigenschaft für einen Warenkorbwert zwischen 100 und 200 $.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
Das Trigger-Event **Start Session** kann das allererste Öffnen der App durch Nutzer:innen sein, wenn das Segment Ihrer Campaign auf neue Nutzer:innen zutrifft (zum Beispiel, wenn Ihr Segment aus Nutzer:innen ohne Sitzungen besteht).
{% endalert %}

Beachten Sie, dass Sie eine getriggerte Campaign weiterhin an ein bestimmtes Segment von Nutzer:innen senden können. Nutzer:innen, die nicht Teil des Segments sind, erhalten die Campaign nicht, selbst wenn sie das Trigger-Event ausführen.

Hinsichtlich des Trigger-Events, wenn Nutzer:innen eine E-Mail-Adresse zu ihrem Profil hinzufügen, gelten die folgenden Regeln:

- Das Trigger-Event wird ausgelöst, nachdem das Nutzerprofilattribut aktualisiert wurde. Das bedeutet, dass die Auswertung der Segmente und Filter der Campaign nach allen Attribut-Aktualisierungen erfolgt. Dies ist vorteilhaft, da Sie damit Filter wie „E-Mail-Adresse enthält gmail.com“ einrichten können, um eine Trigger-Campaign zu erstellen, die nur an Gmail-Nutzer:innen gesendet wird und sofort beim Hinzufügen der E-Mail-Adresse ausgelöst wird.
- Das Trigger-Event wird ausgelöst, wenn eine E-Mail-Adresse zu einem Nutzerprofil hinzugefügt wird. Wenn Sie mehrere Nutzerprofile mit derselben E-Mail-Adresse erstellt haben, kann die Campaign mehrfach ausgelöst werden – einmal für jedes Nutzerprofil.

Darüber hinaus unterliegen getriggerte In-App-Nachrichten weiterhin den Zustellungsregeln für In-App-Nachrichten und werden zu Beginn einer App-Sitzung angezeigt.

### Schritt 2: Verzögerungsdauer festlegen {#step-2-select-delay-length}

Wählen Sie aus, wie lange nach Erfüllung der Trigger-Kriterien gewartet werden soll, bevor die Campaign gesendet wird. Wenn die gewählte Verzögerungsdauer länger ist als die Sendedauer der Nachricht, erhalten keine Nutzer:innen die Campaign.

In-App-Nachricht-Kampagnen können die Zustellung nach dem Trigger-Event um bis zu zwei Stunden (7.200 Sekunden) verzögern. Die Verzögerungsoptionen sind **Sofort** und **Nach einer Verzögerung**. Für eine längere Wartezeit fügen Sie in einem Canvas einen [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) vor einem In-App-Nachricht-Schritt hinzu.

{% alert important %}
Braze verwendet den mit dem angepassten Event gesendeten Zeitstempel, um die Verzögerung für eine aktionsbasierte Campaign zu berechnen. Wenn dieser Zeitstempel in der Vergangenheit liegt, kann Braze die Verzögerung als bereits abgelaufen betrachten und die Nachricht sofort oder früher als erwartet senden. Um unbeabsichtigtes Zustellungs-Timing zu vermeiden, senden Sie den Zeitstempel des angepassten Events mit der aktuellen Uhrzeit.
{% endalert %}

Außerdem erhalten Nutzer:innen, die das Trigger-Event nach dem Start Ihrer Campaign abschließen, die Nachricht als Erste, nachdem die Verzögerung abgelaufen ist. Nutzer:innen, die das Trigger-Event vor dem Start der Campaign abgeschlossen haben, qualifizieren sich nicht für den Empfang der Campaign.

Sie können die Campaign auch an einem bestimmten Wochentag senden, indem Sie **Am nächsten Wochentag** auswählen, oder nach einer bestimmten Anzahl von Tagen in der Zukunft, indem Sie **Nach einer Anzahl von Kalendertagen** auswählen. Alternativ können Sie Ihre Nachricht mit [intelligentem Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) senden, anstatt manuell eine Zustellungszeit festzulegen.

### Schritt 3: Ausnahme-Events auswählen {#step-3-select-exception-events}

Wählen Sie ein Ausnahme-Event aus, das Nutzer:innen vom Erhalt dieser Campaign disqualifiziert. Sie können dies nur tun, wenn Ihre getriggerte Nachricht nach einer Zeitverzögerung gesendet wird. [Ausnahme-Events]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) können ein Kauf, ein Sitzungsstart, die Durchführung eines der festgelegten [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) der Campaign oder die Durchführung eines angepassten Events sein.

Wenn Nutzer:innen das Trigger-Event abschließen, dann aber ihr Ausnahme-Event ausführen, bevor die Nachricht aufgrund der Zeitverzögerung gesendet wird, erhalten sie die Campaign nicht. Nutzer:innen, die die Campaign aufgrund des Ausnahme-Events nicht erhalten, sind automatisch berechtigt, sie in Zukunft zu erhalten – beim nächsten Mal, wenn sie das Trigger-Event ausführen –, selbst wenn Sie keine [erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) aktiviert haben.

Weitere Informationen zur Verwendung von Ausnahme-Events finden Sie unter [Beispiele](#examples).

Wenn Sie eine Campaign mit einem Trigger-Event senden, das dem Ausnahme-Event entspricht, bricht Braze die Campaign ab und plant automatisch eine neue Campaign basierend auf der Nachrichtenzustellungszeit des Ausnahme-Events. Wenn beispielsweise Ihr erstes Trigger-Event nach fünf Minuten startet und das Ausnahme-Event nach 10 Minuten, gilt die 10-Minuten-Zustellungszeit des Ausnahme-Events als offizielle Nachrichtenzustellungszeit der Campaign.

{% alert note %}
Sie können „Sitzungsstart“ nicht gleichzeitig als Trigger-Event und Ausnahme-Event für eine Campaign verwenden. Sie haben jedoch immer die Möglichkeit, ein anderes angepasstes Event auszuwählen.
{% endalert %}

### Schritt 4: Dauer zuweisen {#step-4-assign-duration}

Legen Sie die Dauer der Campaign fest, indem Sie eine Startzeit und eine optionale Endzeit angeben.

Wenn Nutzer:innen ein Trigger-Event innerhalb des festgelegten Zeitraums abschließen, sich aber aufgrund einer geplanten Verzögerung außerhalb des Zeitraums für die Nachricht qualifizieren, erhalten sie die Campaign nicht. Wenn Sie daher eine Zeitverzögerung festlegen, die länger als der Nachrichtenzeitraum ist, erhält niemand Ihre Campaign. Darüber hinaus können Sie die Nachricht in den [Ortszeiten]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) der Nutzer:innen senden.

### Schritt 5: Zeitfenster auswählen {#step-5-select-time-frame}

Wählen Sie aus, ob Nutzer:innen die Campaign während eines bestimmten Tagesabschnitts erhalten sollen. Wenn Sie der Nachricht ein Zeitfenster zuweisen und Nutzer:innen das Trigger-Event außerhalb des Zeitfensters abschließen oder die Nachrichtenverzögerung dazu führt, dass sie das Zeitfenster verpassen, erhalten sie Ihre Nachricht standardmäßig nicht.

Falls Nutzer:innen das Trigger-Event innerhalb des Zeitfensters abschließen, die Nachrichtenverzögerung sie jedoch außerhalb des Zeitfensters fallen lässt, können Sie die Checkbox **Zum nächsten verfügbaren Zeitpunkt senden, wenn die Zustellungszeit außerhalb des festgelegten Tagesabschnitts liegt** aktivieren, damit diese Nutzer:innen die Campaign dennoch erhalten.

Wenn Nutzer:innen die Nachricht nicht erhalten, weil sie das Zeitfenster verpasst haben, sind sie dennoch berechtigt, sie beim nächsten Mal zu erhalten, wenn sie das Trigger-Event abschließen – selbst wenn Sie keine [erneute Berechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) aktiviert haben. Wenn Sie die erneute Berechtigung aktivieren, können Nutzer:innen die Campaign jedes Mal erhalten, wenn sie das Trigger-Event abschließen, vorausgesetzt, sie qualifizieren sich innerhalb des festgelegten Zeitfensters.

Wenn Sie der Campaign auch eine bestimmte Dauer zugewiesen haben, müssen Nutzer:innen sich sowohl innerhalb der Dauer als auch innerhalb des bestimmten Tagesabschnitts qualifizieren, um die Nachricht zu erhalten.

### Schritt 6: Erneute Berechtigung festlegen {#step-6-determine-re-eligibility}

Legen Sie fest, ob Nutzer:innen [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) werden können, die Campaign zu erhalten. Wenn Sie die erneute Berechtigung aktivieren, können Sie eine Zeitverzögerung festlegen, bevor Nutzer:innen die Campaign erneut erhalten können. Dies verhindert, dass Ihre getriggerten Kampagnen als „Spam“ wahrgenommen werden.

## Beispiele {#examples}

Getriggerte Kampagnen sind sehr effektiv für transaktionale oder erfolgsbasierte Nachrichten.

Transaktionale Kampagnen umfassen Nachrichten, die gesendet werden, nachdem Nutzer:innen einen Kauf abgeschlossen oder einen Artikel in ihren Warenkorb gelegt haben. Letzteres ist ein gutes Beispiel für eine Kampagne, die von einem Ausnahme-Event profitiert. Angenommen, Ihre Kampagne erinnert Nutzer:innen an Artikel in ihrem Warenkorb, die sie noch nicht gekauft haben. Das Ausnahme-Event wäre in diesem Fall der Kauf der Produkte im Warenkorb. Für erfolgsbasierte Kampagnen können Sie fünf Minuten nach Abschluss einer Konversion oder nach dem Erreichen eines Spiellevels eine Nachricht senden.

Darüber hinaus können Sie bei der Erstellung von Willkommenskampagnen Nachrichten triggern, die gesendet werden, nachdem sich Nutzer:innen registriert oder ein Konto eingerichtet haben. Indem Sie Nachrichten zeitversetzt an verschiedenen Tagen nach der Registrierung senden, können Sie einen umfassenden Onboarding-Prozess gestalten.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was ist die maximale Verzögerung nach einem Trigger für In-App-Nachricht-Kampagnen? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Zwei Stunden (7.200 Sekunden). Informationen zu den verfügbaren Verzögerungsoptionen und wie Sie eine längere Wartezeit festlegen, finden Sie unter [Schritt 2: Verzögerungsdauer auswählen](#step-2-select-delay-length).

### Warum hat eine Nutzerin oder ein Nutzer meine getriggerte Campaign nicht erhalten? {#why-did-a-user-not-receive-my-triggered-campaign}

Jeder der folgenden Punkte kann dazu führen, dass Nutzer:innen, die das Trigger-Event abgeschlossen haben, die Campaign nicht erhalten:

- Die Nutzerin oder der Nutzer hat das Ausnahme-Event abgeschlossen, bevor die Zeitverzögerung vollständig abgelaufen war.
- Es wurde Liquid-[`abort_message`-Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) verwendet, und die Nachricht wurde basierend auf der `abort_message`-Logik oder den Regeln abgebrochen.
- Die Zeitverzögerung führte dazu, dass die Nutzerin oder der Nutzer sich erst nach Ablauf der Campaign-Dauer für den Empfang qualifizierte.
- Die Zeitverzögerung führte dazu, dass die Nutzerin oder der Nutzer sich außerhalb des festgelegten Tagesabschnitts für den Empfang der Campaign qualifizierte.
- Die Nutzerin oder der Nutzer hat die Campaign bereits erhalten (einschließlich Zuordnung über gemeinsam genutzte Kanal-Bezeichner – zum Beispiel, wenn sie eine E-Mail mit jemandem teilen, der sie erhalten, geöffnet oder angeklickt hat), und Nutzer:innen werden nicht erneut qualifiziert.
- Obwohl Nutzer:innen erneut für den Empfang der Campaign qualifiziert werden können, können sie diese erst nach einer bestimmten Zeitspanne erneut triggern, und diese Zeitspanne ist noch nicht abgelaufen.

Die [Segmentierung]({{site.baseurl}}/user_guide/audience/segments) einer getriggerten Campaign auf Basis von Nutzerdaten, die zum Zeitpunkt des Events erfasst wurden, kann eine [Race-Condition]({{site.baseurl}}/help/best_practices/race_conditions#race-conditions) verursachen. Dies geschieht, wenn das Nutzerattribut, auf dem die Campaign segmentiert ist, geändert wird, die Änderung aber noch nicht für die Nutzerin oder den Nutzer verarbeitet wurde, als die Campaign gesendet wird. Da Campaigns die Segment-Zugehörigkeit beim Eintritt prüfen, kann dies dazu führen, dass die Nutzerin oder der Nutzer die Campaign nicht erhält.

Stellen Sie sich zum Beispiel vor, Sie möchten eine Event-getriggerte Campaign an männliche Nutzer senden, die sich gerade registriert haben. Bei der Registrierung erfassen Sie ein angepasstes Event `registration` und setzen gleichzeitig das `gender`-Attribut der Nutzerin oder des Nutzers. Das Event kann die Campaign triggern, bevor Braze das Geschlecht verarbeitet hat, wodurch die Nutzerin oder der Nutzer die Campaign nicht erhält.

Als Best Practice sollten Sie sicherstellen, dass das Attribut, auf dem die Campaign segmentiert ist, an die Braze-Server übertragen wird, bevor das Event ausgelöst wird. Wenn dies nicht möglich ist, ist der beste Weg zur Sicherstellung der Zustellung die Verwendung von [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties), um die relevanten Nutzereigenschaften an das Event anzuhängen und einen Eigenschaftsfilter für die spezifische Event-Eigenschaft anstelle eines Segmentierungsfilters anzuwenden. Für unser Beispiel fügen Sie eine `gender`-Eigenschaft zum angepassten Event `registration` hinzu, damit Braze garantiert über die benötigten Daten verfügt, wenn Ihre Campaign getriggert wird.

Wenn eine Campaign darüber hinaus aktionsbasiert ist und eine Verzögerung hat, können Sie die Option **Segment-Zugehörigkeit zum Sendezeitpunkt erneut bewerten** aktivieren, um sicherzustellen, dass Nutzer:innen zum Sendezeitpunkt noch Teil der Zielgruppe sind.

#### Bewertung der Zielgruppenkriterien {#audience-criteria-evaluation}

Bei Campaigns mit einer Verzögerung vor dem Senden (einschließlich Rate-Limiting, Ortszeit, intelligentem Timing oder einem Trigger-Zeitplan) hängt die erneute Bewertung des Segments vom Campaign-Typ und den Einstellungen ab.

Bei aktionsbasierten Campaigns mit Verzögerung werden Nutzer:innen erneut bewertet, bevor die Nachricht gesendet wird, wenn Sie **Segment-Zugehörigkeit zum Sendezeitpunkt erneut bewerten** auswählen. So erhalten nur Nutzer:innen die Nachricht, die zum Sendezeitpunkt noch die Segmentkriterien erfüllen.

Wenn Ihre Campaign durch ein bestimmtes angepasstes Event getriggert wird und Sie ein Segment als Zielgruppe auswählen, müssen Nutzer:innen dasselbe angepasste Event ausführen, um in das Segment aufgenommen zu werden. Das bedeutet, dass Nutzer:innen Teil der Zielgruppe sein müssen, bevor eine aktionsbasierte Campaign getriggert werden kann. Der allgemeine Ablauf für eine getriggerte Campaign ist wie folgt:

1. **Der Zielgruppe beitreten:** Wenn eine Nutzerin oder ein Nutzer das angepasste Event ausführt, wird sie oder er zur Zielgruppe der Campaign hinzugefügt.
2. **E-Mail triggern:** Eine Nutzerin oder ein Nutzer muss das angepasste Event erneut ausführen, um die E-Mail zu triggern, da sie oder er Teil der Zielgruppe sein muss, bevor die E-Mail gesendet werden kann.

Wir empfehlen, entweder die Zielgruppe so zu ändern, dass alle Nutzer:innen eingeschlossen sind, oder sicherzustellen, dass die Nutzer:innen, von denen erwartet wird, dass sie das Event ausführen, bereits Teil der Campaign-Zielgruppe sind, damit die Nachricht getriggert wird.

![Screenshot zur Bewertung der Zielgruppenkriterien.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Fehlerbehebung bei angepassten Events {#troubleshooting-custom-events}

Bestätigen Sie zunächst, dass das angepasste Event an Braze übergeben wird. Gehen Sie zu **Analytics** > **Bericht über angepasste Events** und wählen Sie das entsprechende angepasste Event und den Zeitraum aus. Wenn das Event nicht angezeigt wird, bestätigen Sie, dass es korrekt eingerichtet ist und die Nutzerin oder der Nutzer die richtige Aktion ausgeführt hat.

Wenn das angepasste Event angezeigt wird, führen Sie zur weiteren Fehlerbehebung folgende Schritte durch:

- Prüfen Sie den Profil-Download der Nutzerin oder des Nutzers, um zu bestätigen, dass das Event getriggert wurde und wann dies geschah. Wenn das Event getriggert wurde, vergleichen Sie den Zeitstempel der Event-Auslösung mit dem Zeitpunkt, zu dem die Campaign live ging. Das Event wurde möglicherweise getriggert, bevor die Campaign live war.
- Überprüfen Sie die Changelogs für die Campaign und alle bei der Zielgruppenansprache verwendeten Segmente, um festzustellen, ob die Nutzerin oder der Nutzer im Segment war, als das angepasste Event getriggert wurde. Wenn sie oder er nicht im Segment war, hätte sie oder er die Campaign nicht erhalten.
- Überprüfen Sie, ob die Nutzerin oder der Nutzer durch Segmentierung in eine Kontrollgruppe aufgenommen wurde und dadurch am Empfang der Campaign gehindert wurde.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event der Nutzerin oder des Nutzers vor der Verzögerung getriggert wurde. Wenn das Event vor der Verzögerung getriggert wurde, hätte sie oder er die Campaign nicht erhalten.

{% alert note %}
In-App-Nachrichten können nur durch Events getriggert werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

### Wann bewerten aktionsbasierte Campaigns die Zielgruppen-Zugehörigkeit? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze bewertet die Zielgruppen-Zugehörigkeit, wenn das Trigger-Event verarbeitet wird, bevor die Nachricht gesendet wird. Standardmäßig prüft Braze, ob die Nutzerin oder der Nutzer zum Zeitpunkt des Einreihens in die Warteschlange zur Zielgruppe gehört. Wenn die Campaign eine Verzögerung hat, können Sie **Segment-Zugehörigkeit zum Sendezeitpunkt erneut bewerten** auswählen, um die Zielgruppenkriterien unmittelbar vor dem Senden erneut zu prüfen – zum Beispiel, wenn eine Nutzerin oder ein Nutzer die Trigger-Aktion ausführen und dann die Zielgruppe verlassen könnte, bevor der Versand abgeschlossen ist.

Weitere Informationen finden Sie unter [Bewertung der Zielgruppenkriterien](#audience-criteria-evaluation).