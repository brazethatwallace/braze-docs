---
nav_title: Intelligentes Timing
article_title: Intelligentes Timing
page_order: 1.3
description: "Dieser Artikel gibt Ihnen einen Überblick über intelligentes Timing (früher Intelligenter Versand) und wie Sie dieses Feature in Ihren Campaigns und Canvases nutzen können."

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligentes Timing {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomintelligent-timing-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-timing}

> Nutzen Sie intelligentes Timing, um Ihre Nachricht an jede:n Nutzer:in zu übermitteln, wenn Braze den optimalen Versandzeitpunkt ermittelt – also den Zeitpunkt, zu dem die Wahrscheinlichkeit für Engagement (Öffnung oder Klick) am höchsten ist. Dadurch können Sie leichter sicherstellen, dass Sie Ihre Nutzer:innen zu deren bevorzugter Zeit erreichen, was zu einem höheren Engagement führen kann.

## Über intelligentes Timing {#about-intelligent-timing}

Braze berechnet den optimalen Versandzeitpunkt auf Grundlage einer statistischen Analyse der bisherigen Interaktionen Ihrer Nutzer:innen mit Ihrer App und ihrer Interaktionen mit den einzelnen Messaging-Kanälen. Die folgenden Interaktionsdaten werden verwendet:

- Sitzungszeiten
- Push-Direktöffnungen
- Push-beeinflusste Öffnungen
- E-Mail-Klicks
- E-Mail-Öffnungen (ohne [maschinelle Öffnungen]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens))
- SMS-Klicks (nur wenn [Linkverkürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) und erweitertes Tracking aktiviert sind)

So öffnet Sam vielleicht morgens regelmäßig Ihre E-Mails, aber abends öffnet sie Ihre App und interagiert mit Benachrichtigungen. Das bedeutet, dass Sam eine E-Mail-Campaign mit intelligentem Timing am Morgen erhält, während sie Campaigns mit Push-Benachrichtigungen am Abend erhält, wenn die Wahrscheinlichkeit größer ist, dass sie sich engagiert.

Wenn für eine:n Nutzer:in keine relevanten Engagement-Daten vorliegen, anhand derer Braze den optimalen Versandzeitpunkt berechnen kann, können Sie einen Fallback-Zeitpunkt festlegen.

## Anwendungsfälle {#use-cases}

- Senden Sie wiederkehrende Campaigns, die nicht zeitkritisch sind
- Automatisieren Sie Campaigns mit Nutzer:innen aus verschiedenen Zeitzonen
- Wenn Sie Ihre am stärksten engagierten Nutzer:innen ansprechen (sie haben die meisten Engagement-Daten)

## Intelligentes Timing verwenden {#using-intelligent-timing}

In diesem Abschnitt wird beschrieben, wie Sie intelligentes Timing für Ihre Campaigns und Canvases konfigurieren.

{% tabs local %}
{% tab Campaign %}
### Schritt 1: Intelligentes Timing hinzufügen {#step-1-add-intelligent-timing}

1. Erstellen Sie eine Campaign und verfassen Sie Ihre Nachricht.
2. Wählen Sie **Scheduled Delivery** als Zustellungsart aus.
3. Wählen Sie unter **Time-Based Scheduling Options** die Option **Intelligent Timing**.
4. Legen Sie die Eingangshäufigkeit fest. Für einmalige Sendungen wählen Sie **Once** und wählen ein Sendedatum aus. Für wiederkehrende Sendungen wählen Sie **Daily**, **Weekly** oder **Monthly** und konfigurieren die Wiederholungsoptionen. Siehe [Hinweise](#considerations) für weitere Informationen.
5. Optional können Sie [Ruhezeiten](#quiet-hours) konfigurieren.
6. Geben Sie eine [Fallback-Zeit](#campaign-fallback) an. Diese wird verwendet, wenn das Profil einer Nutzerin oder eines Nutzers keine relevanten Ereignisse enthält, um einen optimalen Zeitpunkt zu berechnen.

![Zeitplan-Bildschirm für Campaigns mit intelligentem Timing, Fallback-Zeit und Einstellungen für Ruhezeiten]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Ruhezeiten {#quiet-hours}

Verwenden Sie Ruhezeiten, um zu verhindern, dass Nachrichten zu bestimmten Zeiten versendet werden. Dies ist hilfreich, wenn Sie vermeiden möchten, Nachrichten in den frühen Morgenstunden oder über Nacht zu versenden, und gleichzeitig intelligentem Timing erlauben, das beste Zustellungsfenster zu bestimmen.

{% alert note %}
Ruhezeiten haben die Einstellung **Only send within specific hours** ersetzt. Anstatt zu wählen, wann Nachrichten gesendet werden können, wählen Sie jetzt, wann sie nicht gesendet werden sollen. Wenn Sie z. B. Nachrichten zwischen 16 und 18 Uhr senden möchten, stellen Sie Ruhezeiten von 18 bis 16 Uhr am nächsten Tag ein.
{% endalert %}

1. Wählen Sie **Enable Quiet Hours**.
2. Wählen Sie die Start- und Endzeit, zu der **keine** Nachrichten gesendet werden sollen.

![Die Funktion „Ruhezeiten“ wurde aktiviert, wobei Start- und Endzeit so eingestellt sind, dass die Zustellung von Nachrichten während der Nachtstunden blockiert wird]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Wenn die Ruhezeiten aktiviert sind, sendet Braze während der Ruhezeit keine Nachrichten – selbst wenn diese Zeit mit der optimalen Sendezeit einer Nutzerin oder eines Nutzers übereinstimmt. Wenn die optimale Zeit in das Ruhezeitfenster fällt, wird die Nachricht stattdessen am nächstgelegenen Rand des Fensters gesendet.

Wenn zum Beispiel die Ruhezeiten von 22:00 Uhr bis 6:00 Uhr eingestellt sind und die optimale Zeit für eine:n Nutzer:in 5:30 Uhr ist, hält Braze die Nachricht zurück und stellt sie um 6:00 Uhr zu – die nächstgelegene Zeit außerhalb des Ruhezeitfensters.

Weitere Informationen finden Sie unter [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Vorschau der Zustellungszeiten {#preview-delivery-times}

Um eine Schätzung zu erhalten, wie viele Nutzer:innen die Nachricht in jeder Stunde des Tages erhalten werden, verwenden Sie das Vorschau-Chart (nur Campaigns).

1. Fügen Sie im Schritt „Zielgruppen“ Segmente oder Filter hinzu.
2. Wählen Sie im Abschnitt **Preview Delivery Times for** (der sowohl in den Schritten **Target Audiences** als auch **Schedule Delivery** erscheint) Ihren Kanal aus.
3. Klicken Sie auf **Refresh Data**.

![Das Vorschau-Chart für Android-Push zeigt, dass das höchste Engagement zwischen 12 und 14 Uhr liegt und die beliebteste App-Nutzungszeit 14 Uhr ist.]({% image_buster /assets/img/intel-timing-preview.png %})

### Schritt 2: Wählen Sie ein Sendedatum {#step-2-choose-a-send-date}

Wählen Sie dann ein Sendedatum für Ihre Campaign aus. Bitte beachten Sie beim Planen von Campaigns mit intelligentem Timing Folgendes:

#### Campaign 48 Stunden im Voraus starten {#launch-campaign-48-hours-in-advance}

Starten Sie Ihre Campaign mindestens 48 Stunden vor dem geplanten Versanddatum. Das liegt an den unterschiedlichen Zeitzonen. Braze berechnet die optimale Zeit um Mitternacht in Samoa-Zeit (UTC+13), einer der ersten Zeitzonen der Welt. Ein Tag umfasst weltweit etwa 48 Stunden. Wenn Sie also eine Campaign innerhalb dieses 48-Stunden-Puffers starten, ist es möglich, dass der optimale Zeitpunkt für eine:n Nutzer:in in der jeweiligen Zeitzone bereits verstrichen ist und die Nachricht nicht gesendet wird.

{% alert important %}
Wenn eine Campaign gestartet wird und die optimale Zeit einer Nutzerin oder eines Nutzers weniger als eine Stunde in der Vergangenheit liegt, wird die Nachricht sofort verschickt. Liegt die optimale Zeit mehr als eine Stunde zurück, wird die Nachricht gar nicht gesendet.
{% endalert %}

#### 3-Tage-Fenster für Segment-Filter {#3-day-window-for-segment-filters}

Wenn Sie eine Zielgruppe ansprechen, die in einem bestimmten Zeitraum eine Aktion durchgeführt hat, sollten Sie in Ihren Segment-Filtern ein Zeitfenster von mindestens 3 Tagen vorsehen. Verwenden Sie zum Beispiel statt `First used app more than 1 day ago` und `First used app less than 3 days ago` 1 Tag und 4 Tage.

![Filter für die Zielgruppe, wobei die Campaign auf Nutzer:innen ausgerichtet ist, die die App vor 1 bis 4 Tagen zum ersten Mal verwendet haben.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Dies liegt ebenfalls an den Zeitzonen – die Auswahl eines Zeitraums von weniger als 3 Tagen kann dazu führen, dass einige Nutzer:innen aus dem Segment herausfallen, bevor ihre optimale Sendezeit erreicht ist.

Weitere Informationen finden Sie unter [FAQ: Intelligentes Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Gewinnervariante 2 Tage nach dem A/B-Test planen {#schedule-winning-variants-2-days-after-ab-test}

Wenn Sie [A/B-Tests mit einer Optimierung]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) nutzen, z. B. die automatische Versendung der **Gewinnervariante** oder die Verwendung einer **personalisierten Variante**, kann intelligentes Timing die Dauer und das Timing Ihrer Campaign beeinflussen.

Wenn Sie intelligentes Timing verwenden, empfehlen wir, den Versand der Gewinnervariante mindestens **2 Tage nach** Beginn des A/B-Tests zu planen. Wenn Ihr A/B-Test beispielsweise am 16. April um 16:00 Uhr beginnt, planen Sie den Versand der Gewinnervariante frühestens für den 18. April um 16:00 Uhr. So hat Braze genügend Zeit, das Verhalten der Nutzer:innen zu bewerten und Nachrichten zum optimalen Zeitpunkt zu versenden.

![A/B-Tests mit ausgewählter Gewinnervariante, mit Gewinnerkriterien, Versanddatum und ausgewählter lokaler Versandzeit]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Schritt 3: Ruhezeiten konfigurieren (optional) {#step-3-configure-quiet-hours-optional}

Optional können Sie das Zustellungsfenster einschränken. Dies kann nützlich sein, wenn Ihre Campaign sich auf ein bestimmtes Ereignis, einen Verkauf oder eine Aktion bezieht, wird aber bei der Verwendung von intelligentem Timing im Allgemeinen nicht empfohlen. Weitere Informationen finden Sie unter [Hinweise](#considerations).

Ruhezeiten fungieren als Nicht-Senden-Fenster. Intelligentes Timing bestimmt weiterhin die optimale Sendezeit für jede:n Nutzer:in, aber wenn diese Zeit in die Ruhezeiten fällt, verzögert Braze die Nachricht bis zur nächsten verfügbaren Zeit außerhalb der Ruhezeiten.

So konfigurieren Sie Ruhezeiten:

1. Wählen Sie bei der Konfiguration von intelligentem Timing die Option **Enable Quiet Hours**.
2. Geben Sie die Start- und Endzeit des Ruhezeitfensters ein.

### Schritt 4: Fallback-Zeit wählen {#campaign-fallback}

Wählen Sie eine Fallback-Zeit, die verwendet wird, wenn das Profil einer Nutzerin oder eines Nutzers keine relevanten Ereignisse enthält, um eine optimale Zustellungszeit zu berechnen.

![Zeitplan für eine Campaign mit intelligentem Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Schritt 5: Vorschau der Zustellungszeiten {#step-5-preview-delivery-times}

Um eine Schätzung zu erhalten, wie viele Nutzer:innen die Nachricht in jeder Stunde des Tages erhalten werden, verwenden Sie das Vorschau-Chart:

1. Fügen Sie im Schritt **Target Audiences** Segmente oder Filter hinzu.
2. Wählen Sie im Abschnitt **Preview Delivery Times for** (der sowohl in den Schritten **Target Audiences** als auch **Schedule Delivery** erscheint) Ihren Kanal aus.
3. Wählen Sie **Refresh Data**.

Das Vorschau-Chart zeigt jede Stunde des Tages in Ihrer Ortszeit an. Die Beschriftungen sind nicht auf eine globale Zeitzone festgelegt.

![Beispielvorschau der Zustellungszeiten für Android-Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Wann immer Sie die Einstellungen für intelligentes Timing oder die Zielgruppe Ihrer Campaign ändern, aktualisieren Sie die Daten erneut, um ein aktualisiertes Chart anzuzeigen.

Das Chart zeigt in Blau die Nutzer:innen, für die relevante Ereignisse zur Berechnung einer optimalen Zeit vorlagen, und in Rot die Nutzer:innen, die die Fallback-Zeit verwenden werden. Verwenden Sie die Berechnungsfilter, um die Vorschau für einen detaillierteren Blick auf die einzelnen Nutzergruppen anzupassen.
{% endtab %}

{% tab Canvas %}

### Schritt 1: Intelligentes Timing hinzufügen

Fügen Sie in Ihrem Canvas einen [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hinzu, gehen Sie dann zu **Delivery Settings** und wählen Sie **Using Intelligent Timing**.

Nachrichten werden an Nutzer:innen gesendet, die den Schritt an diesem Tag betreten haben, zu ihrer optimalen Ortszeit. Wenn ihre optimale Zeit an diesem Tag jedoch bereits verstrichen ist, wird die Nachricht stattdessen am folgenden Tag zur optimalen Zeit zugestellt. Nachrichten-Schritte, die auf mehrere Kanäle abzielen, können Nachrichten zu verschiedenen Zeiten für verschiedene Kanäle senden oder versuchen zu senden. Wenn die erste Nachricht in einem Nachrichten-Schritt versucht zu senden, werden alle Nutzer:innen automatisch vorangebracht.

### Schritt 2: Fallback-Zeit wählen {#step-2-choose-a-fallback-time}

Wählen Sie eine Fallback-Zeit für die Nachricht, die an Nutzer:innen in Ihrer Zielgruppe gesendet werden soll, für die keine relevanten Engagement-Daten vorliegen, damit Braze eine optimale Sendezeit berechnen kann. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Schritt 4: Verzögerungsschritt hinzufügen {#step-4-add-a-delay-step}

Anders als bei Campaigns müssen Sie Ihr Canvas nicht 48 Stunden vor dem Versanddatum starten, da intelligentes Timing auf der Schritt-Ebene und nicht auf der Canvas-Ebene eingestellt wird.

Fügen Sie stattdessen einen [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) von mindestens zwei Kalendertagen zwischen dem Eintritt der Nutzerin oder des Nutzers in das Canvas und dem Erhalt des Schritts mit intelligentem Timing ein.

#### Kalendertage vs. 24-Stunden-Tage {#calendar-vs-24-hour-days}

Wenn Sie intelligentes Timing nach einem Verzögerungsschritt verwenden, kann das Zustellungsdatum variieren, je nachdem, wie Sie Ihre Verzögerung berechnen. Dies gilt nur, wenn Ihre Verzögerung auf **After a duration** eingestellt ist, da es einen Unterschied zwischen der Berechnung von „Tagen“ und „Kalendertagen“ gibt.

- **Tage:** 1 Tag sind 24 Stunden, gerechnet ab dem Zeitpunkt, an dem die:der Nutzer:in den Verzögerungsschritt betritt.
- **Kalendertage:** 1 Tag ist der Zeitraum vom Eintritt der Nutzerin oder des Nutzers in den Verzögerungsschritt bis Mitternacht in der jeweiligen Zeitzone. Das bedeutet, dass 1 Kalendertag nur wenige Minuten lang sein kann.

Bei der Verwendung von intelligentem Timing empfehlen wir, für Verzögerungen Kalendertage anstelle von 24-Stunden-Tagen zu verwenden. Dies liegt daran, dass bei Kalendertagen die Nachricht am letzten Tag der Verzögerung zum optimalen Zeitpunkt versendet wird. Bei einem 24-Stunden-Tag besteht die Möglichkeit, dass die optimale Zeit der Nutzerin oder des Nutzers vor dem Betreten des Schritts liegt, was bedeutet, dass ein zusätzlicher Tag zur Verzögerung hinzukommt.

Nehmen wir zum Beispiel an, Lukas optimale Zeit ist 14:00 Uhr. Er betritt den Verzögerungsschritt um 14:01 Uhr am 1. März und die Verzögerung ist auf 2 Tage eingestellt.

- Tag 1 endet am 2. März um 14:01 Uhr
- Tag 2 endet am 3. März um 14:01 Uhr

Intelligentes Timing soll jedoch um 14:00 Uhr zustellen, was bereits verstrichen ist. Luka wird die Nachricht also erst am nächsten Tag erhalten: am 4. März um 14:00 Uhr.

![Grafik, die den Unterschied zwischen Tagen und Kalendertagen veranschaulicht: Wenn die optimale Zeit einer Nutzerin oder eines Nutzers 14:00 Uhr ist, sie oder er jedoch um 14:01 Uhr in den Verzögerungsschritt eintritt und die Verzögerung auf 2 Tage eingestellt ist. „Tage“ liefert die Nachricht drei Tage später, da die:der Nutzer:in den Schritt nach der optimalen Zeit betreten hat, während „Kalendertage“ die Nachricht zwei Tage später, am letzten Tag der Verzögerung, liefert.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Hinweise {#considerations}

- In-App-Nachrichten und Webhooks werden sofort zugestellt und erhalten keine optimalen Zeiten.
- Intelligentes Timing ist nicht verfügbar für aktionsbasierte oder API-getriggerte Campaigns.
- Intelligentes Timing sollte in den folgenden Szenarien nicht verwendet werden:
    - **Rate-Limiting:** Wenn sowohl Rate-Limiting als auch intelligentes Timing verwendet werden, gibt es keine Garantie dafür, wann die Nachricht zugestellt wird. Täglich wiederkehrende Campaigns mit intelligentem Timing unterstützen keine genaue Obergrenze für den Gesamtnachrichtenversand.
    - **IP-Warming-Campaigns:** Einige Verhaltensweisen des intelligenten Timings können dazu führen, dass die täglichen Volumina, die beim ersten Aufwärmen Ihrer IP benötigt werden, nicht erreicht werden. Das liegt daran, dass intelligentes Timing die Segmente zweimal auswertet – einmal bei der Erstellung der Campaign oder des Canvas und ein zweites Mal vor dem Versand an die Nutzer:innen, um zu überprüfen, ob sie noch in diesem Segment sein sollten. Dies kann dazu führen, dass sich die Segmente verschieben und verändern, was oft dazu führt, dass einige Nutzer:innen bei der zweiten Auswertung aus dem Segment herausfallen. Diese Nutzer:innen werden nicht ersetzt, was sich darauf auswirkt, wie nah Sie an die maximale Nutzerobergrenze herankommen können.

## Fehlerbehebung {#troubleshooting}

### Vorschau-Chart zeigt wenige Nutzer:innen mit optimalen Zeiten {#preview-chart-showing-few-users-with-optimal-times}

Wenn für eine:n Nutzer:in keine relevanten Ereignisse vorliegen (z. B. bei neuen Nutzer:innen mit geringer oder keiner Interaktion), verwendet Braze die konfigurierte Fallback-Einstellung – entweder Ihre benutzerdefinierte Fallback-Zeit oder die beliebteste Zeit für die Nutzung der App unter allen Nutzer:innen.

### Auswirkungen der Zeitzone auf die Zustellung mit intelligentem Timing {#impact-of-time-zone-on-intelligent-timing-delivery}

Intelligentes Timing verwendet die Ortszeit und Kalendertage jeder Nutzerin und jedes Nutzers, um die optimale Zustellung zu bestimmen. Aus diesem Grund können Nutzer:innen in Zeitzonen, die der Referenzzeitzone Ihrer Campaign voraus oder hinterher sind, Nachrichten an einem anderen Kalendertag erhalten, als Sie es erwarten würden.

Wenn zum Beispiel eine Campaign für den 15. März geplant ist und die optimale Zeit einer Nutzerin oder eines Nutzers für dieses Datum berechnet wurde, kann eine:r Nutzer:in in einer Zeitzone, die der Referenzzeitzone voraus ist, die Nachricht spät am 14. März in der Referenzzeitzone erhalten, während eine:r Nutzer:in in einer Zeitzone hinter dem Referenzpunkt sie am 16. März erhalten kann.

Sollten Nutzer:innen Nachrichten nicht wie erwartet erhalten, überprüfen Sie, ob das Feld für die Zeitzone in ihrem Profil korrekt ausgefüllt ist. Wenn das Feld für die Zeitzone leer ist, kann es vorkommen, dass die Nutzer:innen Nachrichten erhalten, die sich nach der Zeitzone des Unternehmens richten und nicht nach ihrer Ortszeit.

### Versand nach dem geplanten Datum {#sending-past-the-scheduled-date}

Ihre Campaign mit intelligentem Timing sendet möglicherweise über das geplante Datum hinaus, wenn Sie [A/B-Tests mit einer Optimierung]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations) nutzen. Campaigns, die A/B-Testing-Optimierungen verwenden, können automatisch die Gewinnervariante senden, nachdem der erste Test abgeschlossen ist, wodurch sich die Dauer der Campaign verlängert. Standardmäßig wird bei Campaigns mit einer Optimierung die Gewinnervariante am Tag nach dem ersten Test an die verbleibenden Nutzer:innen gesendet, aber Sie können dieses Sendedatum ändern.

Wenn Sie intelligentes Timing verwenden, empfehlen wir, mehr Zeit für den Abschluss des A/B-Tests einzuplanen und den Versand der Gewinnervariante für 2 Tage nach dem ersten Test zu planen, anstatt für 1 Tag.

## Häufig gestellte Fragen (FAQ) {#faq}

### Allgemein {#general}

#### Was sagt intelligentes Timing voraus? {#what-does-intelligent-timing-predict}

Intelligentes Timing konzentriert sich auf die Vorhersage, wann eine:r Nutzer:in Ihre Nachrichten am ehesten öffnet oder anklickt, um sicherzustellen, dass Ihre Nachrichten die Nutzer:innen zu optimalen Engagement-Zeiten erreichen.

#### Wird intelligentes Timing für jeden Wochentag separat berechnet? {#is-intelligent-timing-calculated-separately-for-each-day-of-the-week}

Nein, intelligentes Timing ist nicht an bestimmte Tage gebunden. Stattdessen personalisiert es die Sendezeiten auf Grundlage der individuellen Engagement-Muster jeder Nutzerin und jedes Nutzers und des von Ihnen verwendeten Kanals, wie E-Mail oder Push-Benachrichtigungen. So können Sie sicherstellen, dass Ihre Nachrichten die Nutzer:innen dann erreichen, wenn sie am empfänglichsten sind.

### Berechnungen {#calculations}

#### Welche Daten werden verwendet, um die optimale Zeit für jede:n Nutzer:in zu berechnen? {#what-data-is-used-to-calculate-the-optimal-time-for-each-user}

Um die optimale Zeit zu berechnen, geht intelligentes Timing wie folgt vor:

1. Analysiert die Interaktionsdaten für jede:n Nutzer:in, die vom Braze SDK aufgezeichnet wurden. Dies beinhaltet:
  - Sitzungszeiten
  - Push-Direktöffnungen
  - Push-beeinflusste Öffnungen
  - E-Mail-Klicks
  - E-Mail-Öffnungen (ohne maschinelle Öffnungen)
2. Gruppiert diese Ereignisse nach Zeit und identifiziert die optimale Sendezeit für jede:n Nutzer:in.

#### Werden maschinelle Öffnungen bei der Berechnung der optimalen Zeit berücksichtigt? {#are-machine-opens-included-when-calculating-optimal-time}

Nein, [maschinelle Öffnungen]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) sind von den Berechnungen für die optimale Zeit ausgeschlossen. Das bedeutet, dass die Sendezeiten ausschließlich auf echtem Nutzer-Engagement basieren, was eine genauere Zeitplanung für Ihre Campaigns ermöglicht.

#### Wie genau ist die optimale Zeit? {#how-precise-is-the-optimal-time}

Intelligentes Timing plant Nachrichten während der „engagiertesten Stunde“ jeder Nutzerin und jedes Nutzers, basierend auf Sitzungsstarts und Nachrichtenöffnungen. Innerhalb dieser Stunde wird der Nachrichtenzeitpunkt auf die nächsten fünf Minuten gerundet. Wenn beispielsweise die optimale Zeit einer Nutzerin oder eines Nutzers mit 16:58 Uhr berechnet wird, wird die Nachricht für 17:00 Uhr geplant. Es kann zu leichten Verzögerungen bei der Zustellung kommen, da das System in Stoßzeiten ausgelastet ist.

#### Wie werden die Fallback-Berechnungen durchgeführt, wenn keine relevanten Ereignisse vorliegen? {#what-are-the-fallback-calculations-if-there-are-no-relevant-events}

Wenn für eine:n Nutzer:in keine relevanten Ereignisse vorliegen, verwendet intelligentes Timing die in Ihren Nachrichteneinstellungen konfigurierte Fallback-Einstellung – entweder eine benutzerdefinierte Fallback-Zeit oder die beliebteste Zeit für die Nutzung der App unter allen Nutzer:innen.

### Campaigns {#campaigns}

#### Wie weit im Voraus sollte ich eine Campaign mit intelligentem Timing starten, um sie erfolgreich an alle Nutzer:innen in allen Zeitzonen zuzustellen? {#how-far-in-advance-should-i-launch-an-intelligent-timing-campaign-to-successfully-deliver-it-to-all-users-in-all-time-zones}

Braze berechnet die optimale Zeit um Mitternacht in Samoa-Zeit, einer der ersten Zeitzonen der Welt. An einem einzigen Tag erstreckt sich dies über etwa 48 Stunden. Zum Beispiel hat jemand, dessen optimale Zeit 0:01 Uhr ist und der in Australien lebt, seine optimale Zeit bereits überschritten, und es ist „zu spät“, um an diese Person zu senden. Aus diesen Gründen müssen Sie 48 Stunden im Voraus planen, um Ihre Nachricht erfolgreich an alle Nutzer:innen weltweit zuzustellen.

#### Warum werden in meiner Campaign mit intelligentem Timing nur wenige oder gar keine Sendungen angezeigt? {#why-is-my-intelligent-timing-campaign-showing-little-to-no-sends}

Wenn für eine:n Nutzer:in keine relevanten Interaktionsereignisse vorliegen (z. B. bei neuen Nutzer:innen mit wenigen oder keinen Klicks oder Öffnungen), verwendet intelligentes Timing die konfigurierte Fallback-Einstellung – entweder Ihre benutzerdefinierte Fallback-Zeit oder die beliebteste Zeit für die Nutzung der App unter allen Nutzer:innen.

#### Warum wird meine Campaign mit intelligentem Timing nach dem geplanten Datum gesendet? {#why-is-my-intelligent-timing-campaign-sending-past-the-scheduled-date}

Ihre Campaign mit intelligentem Timing versendet möglicherweise über das geplante Datum hinaus, weil Sie A/B-Tests nutzen. Campaigns, die A/B-Tests verwenden, können die Gewinnervariante automatisch versenden, nachdem der A/B-Test beendet ist, wodurch sich die Dauer des Campaign-Versands verlängert. Standardmäßig werden Campaigns mit intelligentem Timing so geplant, dass die Gewinnervariante am nächsten Tag an die verbleibenden Nutzer:innen versendet wird, aber Sie können dieses Versanddatum ändern.

Wir empfehlen, bei Campaigns mit intelligentem Timing mehr Zeit für den Abschluss des A/B-Tests einzuplanen und die Gewinnervariante für zwei Tage statt für einen Tag zu planen.

### Funktionsweise {#functionality}

#### Wann prüft Braze die Zulassungskriterien für Segment- und Zielgruppenfilter? {#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters}

Braze führt zwei Prüfungen durch, wenn eine Campaign gestartet wird:

1. **Erste Prüfung:** Um Mitternacht in der ersten Zeitzone am Tag des Versands.
2. **Prüfung zum geplanten Zeitpunkt:** Kurz vor dem Senden zu der von intelligentem Timing für die:den Nutzer:in ausgewählten Zeit.

Seien Sie vorsichtig, wenn Sie auf Grundlage anderer Campaign-Sendungen filtern, um das Targeting nicht geeigneter Segmente zu vermeiden. Wenn Sie z. B. zwei Campaigns am selben Tag zu unterschiedlichen Zeiten versenden und einen Filter hinzufügen, der es Nutzer:innen nur erlaubt, die zweite Campaign zu erhalten, wenn sie die erste erhalten haben, werden die Nutzer:innen die zweite Campaign nicht erhalten. Dies liegt daran, dass zum Zeitpunkt der Erstellung der Campaign und der Bildung der Segmente niemand berechtigt war.

#### Kann ich Ruhezeiten in meiner Campaign mit intelligentem Timing verwenden? {#can-i-use-quiet-hours-in-my-intelligent-timing-campaign}

Ruhezeiten können in einer Campaign verwendet werden, die intelligentes Timing einsetzt. Der Algorithmus des intelligenten Timings vermeidet Ruhezeiten, sodass die Nachricht trotzdem an alle in Frage kommenden Nutzer:innen gesendet wird. Wir empfehlen jedoch, die Ruhezeiten zu deaktivieren, es sei denn, es gibt Richtlinien-, Compliance- oder andere rechtliche Gründe dafür, wann Nachrichten gesendet werden können und wann nicht.

#### Was passiert, wenn die optimale Zeit für eine:n Nutzer:in innerhalb der Ruhezeiten liegt? {#what-happens-if-the-optimal-time-for-a-user-is-within-the-quiet-hours}

Wenn die ermittelte optimale Zeit in die Ruhezeiten fällt, findet Braze den nächstgelegenen Rand der Ruhezeiten und plant die Nachricht für die nächste zulässige Stunde vor oder nach den Ruhezeiten. Die Nachricht wird in die Warteschlange gestellt, um an der nächstgelegenen Grenze der Ruhezeiten relativ zur optimalen Zeit gesendet zu werden.

#### Kann ich intelligentes Timing und Rate-Limiting verwenden? {#can-i-use-intelligent-timing-and-rate-limiting}

Rate-Limiting kann bei einer Campaign verwendet werden, die intelligentes Timing einsetzt. Die Natur des Rate-Limitings bedeutet jedoch, dass einige Nutzer:innen ihre Nachrichten möglicherweise zu einem weniger als optimalen Zeitpunkt erhalten, insbesondere wenn eine große Anzahl von Nutzer:innen im Verhältnis zur Größe des Rate-Limits zur Fallback-Zeit eingeplant ist, weil sie keine relevanten Ereignisse haben.

Wir empfehlen die Verwendung von Rate-Limiting bei einer Campaign mit intelligentem Timing nur dann, wenn es technische Anforderungen gibt, die mit Rate-Limiting erfüllt werden müssen.

#### Kann ich intelligentes Timing während des IP-Warmings verwenden? {#can-i-use-intelligent-timing-while-ip-warming}

Braze rät davon ab, intelligentes Timing zu verwenden, wenn Sie zum ersten Mal IP-Warming betreiben, da einige seiner Verhaltensweisen zu Schwierigkeiten beim Erreichen der täglichen Volumina führen können. Das liegt daran, dass intelligentes Timing die Campaign-Segmente zweimal auswertet. Einmal bei der Erstellung der Campaign und ein zweites Mal vor dem Versand an die Nutzer:innen, um zu überprüfen, ob sie noch in diesem Segment sein sollten.

Dies kann dazu führen, dass sich die Segmente verschieben und verändern, was oft dazu führt, dass einige Nutzer:innen bei der zweiten Auswertung aus dem Segment herausfallen. Diese Nutzer:innen werden nicht ersetzt, was sich darauf auswirkt, wie nah Sie an die maximale Nutzerobergrenze herankommen können.

#### Wie wird die beliebteste App-Zeit ermittelt? {#how-is-the-most-popular-app-time-determined}

Die beliebteste App-Zeit wird durch die durchschnittliche Sitzungsstartzeit für den Workspace (in Ortszeit) bestimmt. Diese Metrik finden Sie im Dashboard bei der Vorschau der Zeiten für eine Campaign, dargestellt in Rot.

#### Berücksichtigt intelligentes Timing maschinelle Öffnungen? {#does-intelligent-timing-account-for-machine-opens}

Ja, maschinelle Öffnungen werden von intelligentem Timing herausgefiltert, sodass sie die Ausgabe nicht beeinflussen.

#### Wie kann ich sicherstellen, dass intelligentes Timing so gut wie möglich funktioniert? {#how-can-i-make-sure-intelligent-timing-works-as-well-as-possible}

Intelligentes Timing verwendet den individuellen Verlauf des Nachrichtenengagements jeder Nutzerin und jedes Nutzers, unabhängig davon, zu welchen Zeiten die Nachrichten empfangen wurden. Bevor Sie intelligentes Timing verwenden, stellen Sie sicher, dass Sie den Nutzer:innen Nachrichten zu verschiedenen Tageszeiten geschickt haben. Auf diese Weise können Sie „ausprobieren“, wann der beste Zeitpunkt für die einzelnen Nutzer:innen ist. Eine unzureichende Abdeckung verschiedener Tageszeiten kann dazu führen, dass intelligentes Timing eine suboptimale Sendezeit für eine:n Nutzer:in auswählt.

#### Wie aktiviere ich intelligentes Timing in einem Canvas-Schritt? {#how-do-i-enable-intelligent-timing-on-a-canvas-step}

Fügen Sie in Canvas einen [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) hinzu oder öffnen Sie einen vorhandenen, gehen Sie zu **Delivery Settings** und wählen Sie **Using Intelligent Timing**. Gemäß der Canvas-Einrichtungsanleitung in diesem Artikel fügen Sie einen [Verzögerungsschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) von mindestens zwei Kalendertagen zwischen dem Canvas-Eintritt und diesem Nachrichten-Schritt ein, damit intelligentes Timing über ausreichend Engagement-Verlauf zur Auswertung verfügt.