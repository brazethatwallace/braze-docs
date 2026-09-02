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

## Einrichten einer getriggerten Campaign {#setting-up-a-triggered-campaign}

### Schritt 1: Trigger-Event auswählen {#step-1-select-a-trigger-event}

Wählen Sie ein Trigger-Event aus. Events sind nach Kategorien organisiert und je nach Ihrem Workspace und den aktivierten Kanälen verfügbar.

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

Die Gruppe **E-Commerce** listet auch empfohlene E-Commerce-Events auf, wie z. B. **Perform Product Viewed Event**, **Perform Order Cancelled Event** und **Perform Order Refunded Event**. Diese Optionen verwenden **Perform Custom Event** mit vorausgefülltem Event-Namen.

In-App-Nachricht-Kampagnen unterstützen eine kleinere Auswahl an Triggern: **Make Purchase**, **Place Order**, **Start Session**, **Perform Custom Event** und **Interact With Campaign**. Bei In-App-Nachricht-Kampagnen umfasst **Interact With Campaign** nur das Öffnen eines Push aus einer beliebigen oder einer bestimmten Campaign. Die folgende Liste der Campaign-Interaktionen ist nicht enthalten.

Für Kampagnen, die keine In-App-Nachrichten sind, wählen Sie bei Auswahl von **Interact With Campaign**, **Interact With Step** oder **Interact with Landing Page** die Interaktion aus, die den Trigger auslösen soll. Jeder dieser Trigger bietet eigene Interaktionen, und die verfügbaren Interaktionen hängen von Ihren aktivierten Kanälen ab.

{% details Interaktionen für Interact With Campaign %}

- **View in-app message**
- **Klick, der in-app message**
- **Klick, der in-app message button 1**
- **Klick, der in-app message button 2**
- **Submit in-app message survey**
- **Klick, der email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Klick, der alias in email**
- **Clicked Alias in any campaign or Canvas-Schritt**
- **Directly open push notification**
- **Klick, der push notification button**
- **Klick, der push story page**
- **Perform conversion event**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Klick, der shortened SMS link**
- **View content card**
- **Klick, der content card**
- **Dismiss content card**
- **View banner**
- **Klick, der banner**
- **Dismiss banner**
- **Klick, der tracked WhatsApp link**
- **Klick, der tracked LINE link**
- **Klick, der tracked KakaoTalk link**
- **Are enrolled in control group**

{% enddetails %}

{% details Interaktionen für Interact With Step %}

- **View in-app message**
- **Start in-app message availability window**
- **Submit in-app message survey**
- **Klick, der email**
- **Open email**
- **Open email (machine opens)**
- **Open email (other opens)**
- **Klick, der alias in email**
- **Clicked Alias in any campaign or Canvas-Schritt**
- **Directly open push notification**
- **Klick, der push notification button**
- **Klick, der push story page**
- **Receive email**
- **Receive push notification**
- **Receive webhook**
- **Receive SMS**
- **Klick, der shortened SMS link**
- **View content card**
- **Klick, der content card**
- **Dismiss content card**
- **View banner**
- **Klick, der banner**
- **Dismiss banner**
- **Klick, der tracked WhatsApp link**
- **Klick, der tracked LINE link**
- **Klick, der tracked KakaoTalk link**

{% enddetails %}

{% details Interaktionen für Interact with Landing Page %}

- **Submit form**
- **Submit survey**

{% enddetails %}

Sie können Trigger-Events auch über die [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events) von Braze weiter filtern, was anpassbare Event-Eigenschaften für angepasste Events und In-App-Käufe ermöglicht. Dieses Feature erlaubt es Ihnen, genauer zu bestimmen, welche Nutzer:innen eine Nachricht erhalten, basierend auf den spezifischen Attributen des angepassten Events, was eine größere Personalisierung der Campaign und eine anspruchsvollere Datenerfassung ermöglicht.

Nehmen wir beispielsweise an, wir haben eine Campaign mit einem angepassten Warenkorb-Abbruch-Event, das zusätzlich nach der Eigenschaft „Warenkorbwert“ gefiltert wird. Diese Campaign erreicht nur Nutzer:innen, die Waren im Wert von 100 $ bis 200 $ in ihrem Warenkorb gelassen haben.

![Warenkorb-Abbruch-Campaign gefiltert nach einer angepassten Event-Eigenschaft für einen Warenkorbwert zwischen 100 $ und 200 $.]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
Das Trigger-Event **Start Session** kann das allererste Öffnen der App durch eine:n Nutzer:in sein, wenn das Segment Ihrer Campaign auf neue Nutzer:innen zutrifft (z. B. wenn Ihr Segment aus Nutzer:innen ohne Sitzungen besteht).
{% endalert %}

Beachten Sie, dass Sie eine getriggerte Campaign weiterhin an ein bestimmtes Segment von Nutzer:innen senden können, sodass Nutzer:innen, die nicht Teil des Segments sind, die Campaign nicht erhalten, selbst wenn sie das Trigger-Event abschließen.

Hinsichtlich des Trigger-Events, wenn eine:r Nutzer:in eine E-Mail-Adresse zu ihrem/seinem Profil hinzufügt, gelten die folgenden Regeln:

- Das Trigger-Event wird ausgelöst, nachdem das Kundenprofil-Attribut aktualisiert wurde. Das bedeutet, dass die Auswertung der Segmente und Filter der Campaign nach allen Attribut-Aktualisierungen erfolgt. Dies ist vorteilhaft, da Sie so Filter wie „E-Mail-Adresse stimmt mit gmail.com überein“ einrichten können, um eine Trigger-Campaign zu erstellen, die nur an Gmail-Nutzer:innen gesendet wird und sofort ausgelöst wird, wenn diese ihre E-Mail-Adresse hinzufügen.
- Das Trigger-Event wird ausgelöst, wenn eine E-Mail-Adresse zu einem Kundenprofil hinzugefügt wird. Wenn Sie mehrere Nutzerprofile mit derselben E-Mail-Adresse erstellen, kann die Campaign mehrfach ausgelöst werden, einmal für jedes Kundenprofil.

Darüber hinaus unterliegen getriggerte In-App-Nachrichten weiterhin den Zustellungsregeln für In-App-Nachrichten und werden zu Beginn einer App-Sitzung angezeigt.

### Schritt 2: Verzögerungsdauer auswählen {#step-2-select-delay-length}

Wählen Sie aus, wie lange nach Erfüllung der Trigger-Kriterien gewartet werden soll, bevor die Campaign gesendet wird. Wenn die gewählte Verzögerungsdauer länger ist als der Sendezeitraum der Nachricht, erhalten keine Nutzer:innen die Campaign.

In-App-Nachricht-Kampagnen können die Zustellung nach dem Trigger-Event um bis zu zwei Stunden (7.200 Sekunden) verzögern. Die Verzögerungsoptionen sind **Sofort** und **Nach einer Verzögerung**. Für eine längere Wartezeit fügen Sie einen [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) vor einem In-App-Nachricht-Schritt in einem Canvas hinzu.

{% alert important %}
Braze verwendet den mit dem angepassten Event gesendeten Zeitstempel, um die Verzögerung für eine aktionsbasierte Campaign auszuwerten. Wenn dieser Zeitstempel rückdatiert ist, kann Braze die Verzögerung als bereits abgelaufen betrachten und die Nachricht sofort oder früher als erwartet senden. Um unbeabsichtigte Zustellungszeiten zu vermeiden, senden Sie den Zeitstempel des angepassten Events mit der aktuellen Uhrzeit.
{% endalert %}

Darüber hinaus sind die ersten Nutzer:innen, die das Trigger-Event abschließen, nachdem Ihre Campaign gestartet wurde, die ersten, die die Nachricht nach Ablauf der Verzögerung erhalten. Nutzer:innen, die das Trigger-Event vor dem Start der Campaign abgeschlossen haben, qualifizieren sich nicht für den Empfang der Campaign.

Sie können die Campaign auch an einem bestimmten Wochentag senden, indem Sie **Am nächsten Wochentag** auswählen, oder eine bestimmte Anzahl von Tagen in der Zukunft, indem Sie **Nach einer Anzahl von Kalendertagen** auswählen. Alternativ können Sie Ihre Nachricht mit [intelligentem Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) senden, anstatt manuell eine Zustellungszeit festzulegen.

### Schritt 3: Ausnahme-Events auswählen {#step-3-select-exception-events}

Wählen Sie ein Ausnahme-Event aus, das Nutzer:innen vom Empfang dieser Campaign ausschließt. Dies ist nur möglich, wenn Ihre getriggerte Nachricht nach einer zeitlichen Verzögerung gesendet wird. [Ausnahme-Events]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events) können ein Kauf, der Start einer Sitzung, die Durchführung eines der festgelegten [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) einer Campaign oder die Durchführung eines angepassten Events sein.

Wenn eine:r Nutzer:in das Trigger-Event abschließt, aber dann das Ausnahme-Event durchführt, bevor die Nachricht aufgrund der zeitlichen Verzögerung gesendet wird, erhält diese:r Nutzer:in die Campaign nicht. Nutzer:innen, die die Campaign aufgrund des Ausnahme-Events nicht erhalten, sind automatisch berechtigt, sie in Zukunft zu erhalten, wenn sie das nächste Mal das Trigger-Event abschließen, auch wenn Sie nicht festlegen, dass Nutzer:innen [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) werden.

Weitere Informationen zur Verwendung von Ausnahme-Events finden Sie unter [Beispiele](#examples).

Wenn Sie eine Campaign mit einem Trigger-Event senden, das mit dem Ausnahme-Event übereinstimmt, storniert Braze die Campaign und plant automatisch eine neue Campaign basierend auf der Zustellungszeit der Nachricht des Ausnahme-Events. Wenn beispielsweise Ihr erstes Trigger-Event bei fünf Minuten beginnt und das Ausnahme-Event bei 10 Minuten, wird die Zustellungszeit des Ausnahme-Events von 10 Minuten als offizielle Zustellungszeit der Campaign verwendet.

{% alert note %}
Sie können einen „Sitzungsstart“ nicht gleichzeitig als Trigger-Event und Ausnahme-Event für eine Campaign festlegen. Sie haben jedoch immer die Möglichkeit, ein anderes angepasstes Event außerhalb dieser Option auszuwählen.
{% endalert %}

### Schritt 4: Dauer zuweisen {#step-4-assign-duration}

Weisen Sie die Dauer der Campaign zu, indem Sie eine Startzeit und eine optionale Endzeit festlegen.

Wenn eine:r Nutzer:in ein Trigger-Event innerhalb des festgelegten Zeitrahmens abschließt, sich aber aufgrund einer geplanten Verzögerung außerhalb des Zeitrahmens für die Nachricht qualifiziert, erhält diese:r Nutzer:in die Campaign nicht. Wenn Sie daher eine zeitliche Verzögerung festlegen, die länger als der Zeitrahmen der Nachricht ist, erhalten keine Nutzer:innen Ihre Campaign. Darüber hinaus können Sie festlegen, die Nachricht in den [Ortszeiten]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery#local-time-zone-campaigns) der Nutzer:innen zu senden.

### Schritt 5: Zeitfenster auswählen {#step-5-select-time-frame}

Wählen Sie aus, ob die Nutzer:innen die Campaign während eines bestimmten Teils des Tages erhalten sollen. Wenn Sie der Nachricht ein Zeitfenster zuweisen und die:der Nutzer:in entweder das Trigger-Event außerhalb des Zeitfensters abschließt oder die Nachrichtenverzögerung dazu führt, dass das Zeitfenster verpasst wird, erhält die:der Nutzer:in standardmäßig Ihre Nachricht nicht.

Falls eine:r Nutzer:in das Trigger-Event innerhalb des Zeitfensters abschließt, die Nachrichtenverzögerung aber dazu führt, dass die:der Nutzer:in aus dem Zeitfenster fällt, können Sie das Kontrollkästchen **Zum nächsten verfügbaren Zeitpunkt senden, wenn die Zustellungszeit außerhalb des festgelegten Tagesabschnitts liegt** aktivieren, damit diese Nutzer:innen die Campaign dennoch erhalten.

Wenn eine:r Nutzer:in die Nachricht nicht erhält, weil das Zeitfenster verpasst wurde, ist die:der Nutzer:in dennoch berechtigt, sie beim nächsten Abschluss des Trigger-Events zu erhalten, auch wenn Sie nicht festgelegt haben, dass Nutzer:innen [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) werden. Wenn Sie festlegen, dass Nutzer:innen erneut berechtigt werden, können Nutzer:innen die Campaign jedes Mal erhalten, wenn sie das Trigger-Event abschließen, vorausgesetzt, sie qualifizieren sich innerhalb des festgelegten Zeitfensters.

Wenn Sie der Campaign auch eine bestimmte Dauer zugewiesen haben, muss sich eine:r Nutzer:in sowohl innerhalb der Dauer als auch innerhalb des bestimmten Tagesabschnitts qualifizieren, um die Nachricht zu erhalten.

### Schritt 6: Erneute Berechtigung festlegen {#step-6-determine-re-eligibility}

Legen Sie fest, ob Nutzer:innen für die Campaign [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) werden können. Wenn Sie Nutzer:innen erlauben, erneut berechtigt zu werden, können Sie eine zeitliche Verzögerung festlegen, bevor die:der Nutzer:in die Campaign erneut erhalten kann. Dies verhindert, dass Ihre getriggerten Kampagnen als „Spam“ wahrgenommen werden.

## Beispiele {#examples}

Getriggerte Kampagnen sind sehr effektiv für transaktionsbezogene oder leistungsbasierte Nachrichten.

Transaktionsbezogene Kampagnen umfassen Nachrichten, die gesendet werden, nachdem Nutzer:innen einen Kauf abgeschlossen oder einen Artikel in ihren Warenkorb gelegt haben. Letzterer Fall ist ein gutes Beispiel für eine Campaign, die von einem Ausnahme-Event profitiert. Angenommen, Ihre Campaign erinnert Nutzer:innen an Artikel in ihrem Warenkorb, die sie noch nicht gekauft haben. Das Ausnahme-Event ist in diesem Fall der Kauf der Produkte im Warenkorb durch die Nutzer:innen. Für leistungsbasierte Kampagnen können Sie eine Nachricht fünf Minuten nach Abschluss einer Konversion oder nach dem Bestehen eines Spiellevels senden.

Darüber hinaus können Sie beim Erstellen von Willkommenskampagnen Nachrichten triggern, die gesendet werden, nachdem sich Nutzer:innen registriert oder ein Konto eingerichtet haben. Durch das zeitversetzte Senden von Nachrichten an verschiedenen Tagen nach der Registrierung können Sie einen umfassenden Onboarding-Prozess gestalten.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Welche maximale Verzögerung gibt es nach einem Trigger für In-App-Nachricht-Kampagnen? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Zwei Stunden (7.200 Sekunden). Informationen zu den verfügbaren Verzögerungsoptionen und wie Sie eine längere Wartezeit einstellen, finden Sie unter [Schritt 2: Verzögerungsdauer auswählen](#step-2-select-delay-length).

### Warum hat ein:e Nutzer:in meine getriggerte Campaign nicht erhalten? {#why-did-a-user-not-receive-my-triggered-campaign}

Folgende Gründe können verhindern, dass ein:e Nutzer:in, die/der das Trigger-Event abgeschlossen hat, die Campaign erhält:

- Die/der Nutzer:in hat das Ausnahme-Event abgeschlossen, bevor die Verzögerungszeit vollständig abgelaufen war.
- Liquid-[`abort_message`-Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) wurde verwendet, und die Nachricht wurde basierend auf der `abort_message`-Logik oder -Regeln abgebrochen.
- Die Verzögerung führte dazu, dass die/der Nutzer:in sich erst nach Ablauf der Kampagnendauer für den Empfang qualifizierte.
- Die Verzögerung führte dazu, dass die/der Nutzer:in sich erst außerhalb des angegebenen Tageszeitraums für den Empfang qualifizierte.
- Die/der Nutzer:in hat die Campaign bereits erhalten (einschließlich Attribution über gemeinsame Kanal-Bezeichner – z. B. wenn sie/er eine E-Mail-Adresse mit jemandem teilt, der die Nachricht erhalten, geöffnet oder angeklickt hat), und Nutzer:innen werden nicht erneut berechtigt.
- Obwohl Nutzer:innen erneut berechtigt sind, die Campaign zu erhalten, können sie diese erst nach einer bestimmten Zeitspanne erneut triggern, und diese Zeitspanne ist noch nicht abgelaufen.

Das [Segmentieren]({{site.baseurl}}/user_guide/audience/segments) einer getriggerten Campaign anhand von Nutzerdaten, die zum Zeitpunkt des Events erfasst wurden, kann eine [Race-Condition]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) verursachen. Dies geschieht, wenn das Nutzerattribut, nach dem die Campaign segmentiert wird, geändert wurde, die Änderung aber noch nicht für die/den Nutzer:in verarbeitet wurde, wenn die Campaign gesendet wird. Da Campaigns die Segment-Zugehörigkeit beim Eintritt prüfen, kann dies dazu führen, dass die/der Nutzer:in die Campaign nicht erhält.

Stellen Sie sich beispielsweise vor, Sie möchten eine Event-getriggerte Campaign an männliche Nutzer senden, die sich gerade registriert haben. Wenn sich der/die Nutzer:in registriert, erfassen Sie ein angepasstes Event `registration` und setzen gleichzeitig das `gender`-Attribut der Nutzerin/des Nutzers. Das Event kann die Campaign triggern, bevor Braze das Geschlecht verarbeitet hat, wodurch die/der Nutzer:in die Campaign nicht erhält.

Als Best Practice stellen Sie sicher, dass das Attribut, nach dem die Campaign segmentiert wird, an die Braze-Server gesendet wird, bevor das Event ausgelöst wird. Wenn dies nicht möglich ist, ist der beste Weg zur Sicherstellung der Zustellung die Verwendung von [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties), um die relevanten Nutzereigenschaften an das Event anzuhängen und einen Eigenschaftsfilter für die spezifische Event-Eigenschaft anstelle eines Segmentierungsfilters anzuwenden. Fügen Sie in unserem Beispiel eine `gender`-Eigenschaft zum angepassten Event `registration` hinzu, damit Braze die benötigten Daten garantiert hat, wenn Ihre Campaign getriggert wird.

Wenn eine Campaign zusätzlich aktionsbasiert ist und eine Verzögerung hat, können Sie die Option **Segment-Zugehörigkeit zum Sendezeitpunkt erneut prüfen** aktivieren, um sicherzustellen, dass Nutzer:innen zum Sendezeitpunkt der Nachricht noch Teil der Zielgruppe sind.

#### Auswertung der Zielgruppenkriterien {#audience-criteria-evaluation}

Bei Campaigns mit einer Verzögerung vor dem Senden (einschließlich Rate-Limiting, Ortszeit, intelligentem Timing oder einem Trigger-Zeitplan) hängt der Zeitpunkt der erneuten Segment-Auswertung vom Kampagnentyp und den Einstellungen ab.

Bei aktionsbasierten Campaigns mit Verzögerung werden Nutzer:innen erneut ausgewertet, bevor die Nachricht gesendet wird, wenn Sie **Segment-Zugehörigkeit zum Sendezeitpunkt erneut prüfen** auswählen. Nur Nutzer:innen, die die Segmentkriterien zum Sendezeitpunkt noch erfüllen, erhalten die Nachricht.

Wenn Ihre Campaign durch ein bestimmtes angepasstes Event getriggert wird und Sie ein Segment als Zielgruppe auswählen, müssen Nutzer:innen dasselbe angepasste Event ausführen, um in das Segment aufgenommen zu werden. Das bedeutet, Nutzer:innen müssen Teil der Zielgruppe sein, bevor eine aktionsbasierte Campaign getriggert werden kann. Der allgemeine Ablauf für eine getriggerte Campaign ist wie folgt:

1. **Der Zielgruppe beitreten:** Wenn ein:e Nutzer:in das angepasste Event ausführt, wird sie/er zur Zielgruppe der Campaign hinzugefügt.
2. **E-Mail triggern:** Ein:e Nutzer:in muss das angepasste Event erneut ausführen, um die E-Mail zu triggern, da sie/er Teil der Zielgruppe sein muss, bevor die E-Mail gesendet werden kann.

Wir empfehlen, entweder die Zielgruppe so zu ändern, dass alle Nutzer:innen eingeschlossen werden, oder zu überprüfen, ob die Nutzer:innen, die das Event voraussichtlich ausführen, bereits Teil der Campaign-Zielgruppe sind, damit die Nachricht getriggert werden kann.

![Screenshot zur Auswertung der Zielgruppenkriterien.]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

#### Fehlerbehebung bei angepassten Events {#troubleshooting-custom-events}

Bestätigen Sie zunächst, dass das angepasste Event an Braze übergeben wird. Gehen Sie zu **Analytics** > **Bericht zu angepassten Events**, und wählen Sie dann das entsprechende angepasste Event und den Zeitraum aus. Wenn das Event nicht angezeigt wird, bestätigen Sie, dass es korrekt eingerichtet ist und der/die Nutzer:in die richtige Aktion ausgeführt hat.

Wenn das angepasste Event angezeigt wird, führen Sie zur weiteren Fehlerbehebung folgende Schritte durch:

- Überprüfen Sie den Profildownload der Nutzerin/des Nutzers, um zu bestätigen, dass sie/er das Event getriggert hat und wann dies geschehen ist. Wenn das Event getriggert wurde, vergleichen Sie den Zeitstempel des Event-Triggers mit dem Zeitpunkt, zu dem die Campaign live ging. Das Event könnte vor dem Go-Live der Campaign getriggert worden sein.
- Überprüfen Sie die Changelogs der Campaign und aller beim Targeting verwendeten Segmente, um festzustellen, ob die/der Nutzer:in zum Zeitpunkt des Triggers des angepassten Events im Segment war. War sie/er nicht im Segment, hätte sie/er die Campaign nicht erhalten.
- Prüfen Sie, ob die/der Nutzer:in durch Segmentierung in eine Kontrollgruppe aufgenommen wurde und daher am Empfang der Campaign gehindert wurde.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event der Nutzerin/des Nutzers vor der Verzögerung getriggert wurde. Wurde das Event vor der Verzögerung getriggert, hätte sie/er die Campaign nicht erhalten.

{% alert note %}
In-App-Nachrichten können nur durch Events getriggert werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

### Wann wird die Zielgruppen-Zugehörigkeit bei aktionsbasierten Campaigns ausgewertet? {#when-do-action-based-campaigns-evaluate-audience-membership}

Braze wertet die Zielgruppen-Zugehörigkeit aus, wenn das Trigger-Event verarbeitet wird, bevor die Nachricht gesendet wird. Standardmäßig prüft Braze, ob die/der Nutzer:in zum Zeitpunkt der Einreihung in die Warteschlange zur Zielgruppe gehört. Wenn die Campaign eine Verzögerung hat, können Sie **Segment-Zugehörigkeit zum Sendezeitpunkt erneut prüfen** auswählen, um die Zielgruppenkriterien unmittelbar vor dem Senden erneut zu prüfen – zum Beispiel, wenn ein:e Nutzer:in die Trigger-Aktion ausführen und dann die Zielgruppe verlassen könnte, bevor der Versand abgeschlossen ist.

Weitere Informationen finden Sie unter [Auswertung der Zielgruppenkriterien](#audience-criteria-evaluation).