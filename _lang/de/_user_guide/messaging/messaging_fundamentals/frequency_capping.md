---
nav_title: Rate-Limiting und Frequency-Capping
article_title: Rate-Limiting und Frequency-Capping
page_order: 6
tool: Campaigns
page_type: reference
description: "Dieser Referenzartikel behandelt die Konzepte Rate-Limiting und Frequency-Capping in Campaigns und wie Sie den Marketingdruck steuern können, um die Nutzererfahrung zu verbessern."

---

# Rate-Limiting und Frequency-Capping {#rate-limiting-and-frequency-capping}

> Rate-Limiting und Frequency-Capping können gemeinsam eingesetzt werden, um sicherzustellen, dass Ihre Nutzer:innen die Nachrichten erhalten, die sie benötigen.

## Über Rate-Limiting {#about-rate-limiting}

Braze ermöglicht es Ihnen, den Marketingdruck durch Rate-Limiting Ihrer Campaigns zu steuern und den ausgehenden Datenverkehr Ihrer Plattform zu regulieren. Sie können zwei verschiedene Arten von Rate-Limiting für Ihre Campaigns implementieren:

1. [Nutzer:innenzentriertes Rate-Limiting:](#user-centric-rate-limiting) Konzentriert sich darauf, die beste Erfahrung für die Nutzer:innen zu bieten.
2. [Zustellgeschwindigkeits-Rate-Limiting:](#delivery-speed-rate-limiting) Berücksichtigt die Bandbreite Ihrer Server.

Braze unterstützt kein sekundengenaues Rate-Limit. Braze versucht, den Nachrichtenversand gleichmäßig über die Minute zu verteilen, kann dies aber nicht garantieren. Wenn Sie beispielsweise eine Campaign mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), aber es kann zu Abweichungen bei der sekundengenauen Rate kommen.

### Nutzer:innenzentriertes Rate-Limiting {#user-centric-rate-limiting}

Wenn Sie mehr Segmente erstellen, wird es Fälle geben, in denen sich die Mitgliedschaften dieser Segmente überschneiden. Wenn Sie Campaigns an diese Segmente senden, möchten Sie sicherstellen, dass Sie Ihre Nutzer:innen nicht zu häufig kontaktieren. Wenn Nutzer:innen innerhalb eines kurzen Zeitraums zu viele Nachrichten erhalten, fühlen sie sich überlastet und deaktivieren entweder Push-Benachrichtigungen oder deinstallieren Ihre App.

#### Relevante Segment-Filter {#relevant-segment-filters}

Braze bietet die folgenden Filter, um Ihnen zu helfen, die Rate zu begrenzen, mit der Ihre Nutzer:innen Nachrichten erhalten:

- Last Engaged With Message
- Last Received Any Message
- Last Received Push
- Last Received Email
- Last Received SMS

#### Filter implementieren {#implementing-filters}

Nehmen wir an, wir haben ein Segment namens „Retargeting Filter Showcase“ mit dem Filter „App zuletzt vor mehr als 7 Tagen verwendet“ erstellt, um Nutzer:innen anzusprechen. Dies wäre ein standardmäßiges Segment zur erneuten Interaktion.

Wenn Sie andere, gezieltere Segmente haben, die kürzlich Benachrichtigungen erhalten haben, möchten Sie möglicherweise nicht, dass Ihre Nutzer:innen von allgemeineren Campaigns angesprochen werden, die auf dieses Segment ausgerichtet sind. Durch Hinzufügen des Filters „Last Received Push“ zu diesem Segment wird sichergestellt, dass Nutzer:innen, die in den letzten 24 Stunden eine andere Benachrichtigung erhalten haben, für die nächsten 24 Stunden aus diesem Segment herausfallen. Wenn sie 24 Stunden später immer noch die anderen Kriterien des Segments erfüllen und keine weiteren Benachrichtigungen erhalten haben, werden sie wieder in das Segment aufgenommen.

![Ein Segment namens „Retargeting Filter Showcase“ mit der Filtergruppe „App zuletzt vor mehr als 7 Tagen verwendet“.]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Wenn Sie diesen Filter an alle Segmente anhängen, die von Campaigns angesprochen werden, erhalten Ihre Nutzer:innen maximal einen Push alle 24 Stunden. Sie könnten dann Ihre Nachrichten priorisieren, indem Sie sicherstellen, dass Ihre wichtigsten Nachrichten vor weniger wichtigen Nachrichten zugestellt werden.

#### Maximale Nutzer:innenobergrenze festlegen {#setting-a-maximum-user-cap}

Im Schritt **Target Audiences** Ihres Campaign-Composers können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten. Dies dient als Kontrolle, die unabhängig von Ihren Campaign-Filtern ist.

![Zielgruppen-Zusammenfassung mit einem aktivierten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Campaign erhalten.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Durch Festlegen der maximalen Nutzer:innenobergrenze können Sie das Nachrichtenvolumen auf Kanalbasis oder global über alle Nachrichtentypen hinweg begrenzen. Braze versendet keine Nachrichten an Nutzer:innen, die Kontrollgruppen zugewiesen sind, sodass diese nicht auf das Limit angerechnet werden.

{% alert note %}
Die maximale Nutzer:innenobergrenze begrenzt die Anzahl der Nutzer:innen, an die versendet wird, nicht die Anzahl der erfolgreich zugestellten Nachrichten. Da abgebrochene Nachrichten auf diese Obergrenze angerechnet werden, kann die tatsächliche Anzahl gesendeter Nachrichten niedriger sein als das konfigurierte Limit. Wenn Sie beispielsweise eine Obergrenze von 10.000 festlegen und 2.000 Nachrichten aufgrund von Liquid-Logik oder anderen Bedingungen abgebrochen werden, werden nur 8.000 Nachrichten gesendet.
{% endalert %}

##### Maximale Nutzer:innenobergrenze mit Optimierungen {#maximum-user-cap-with-optimizations}

Wenn Sie eine Optimierung wie Gewinnervariante oder Personalisierte Variante verwenden, besteht die Campaign aus zwei Sendungen: dem anfänglichen Experiment und der finalen Sendung.

Um in diesem Szenario eine maximale Nutzer:innenobergrenze einzurichten, wählen Sie **Limit the number of people who will receive this campaign**, dann wählen Sie **In total this campaign should** und geben Sie ein Zielgruppenlimit ein. Ihr Zielgruppenlimit wird nach den im **A/B Testing**-Panel angezeigten Prozentsätzen aufgeteilt.

Wenn Sie **Every time the campaign is scheduled** auswählen, werden diese beiden Phasen separat auf die festgelegte Anzahl begrenzt. Dies ist in der Regel nicht erwünscht.

#### Maximale Impressionen-Obergrenze für Campaigns festlegen {#setting-a-maximum-impression-cap-on-campaigns}

Für In-App-Nachrichten können Sie den Marketingdruck steuern, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Nutzerbasis angezeigt werden, wonach Braze keine weiteren Nachrichten mehr an Ihre Nutzer:innen sendet. Es ist jedoch wichtig zu beachten, dass diese Obergrenze nicht exakt ist.

In-App-Nachrichtenregeln werden bei Sitzungsbeginn an eine App gesendet, was bedeutet, dass Braze eine Nachricht an die Nutzer:innen senden kann, bevor die Obergrenze erreicht ist, aber bis die Nutzer:innen die Nachricht auslösen, wurde die Obergrenze bereits erreicht. In dieser Situation zeigt das Gerät die Nachricht trotzdem an.

Nehmen wir beispielsweise an, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn Nutzer:innen ein Level abschließen, und Sie begrenzen es auf 100 Impressionen. Es gab bisher 99 Impressionen. Alice und Bob öffnen beide das Spiel, und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu erhalten, wenn sie ein Level abschließen. Alice schließt zuerst ein Level ab und erhält die Nachricht. Bob schließt als Nächstes das Level ab, aber da sein Gerät seit Sitzungsbeginn nicht mit den Braze-Servern kommuniziert hat, weiß sein Gerät nicht, dass die Nachricht ihre Obergrenze erreicht hat, und er erhält die Nachricht ebenfalls. Wenn jedoch eine Impressionen-Obergrenze erreicht wurde, wird das System beim nächsten Mal, wenn ein Gerät die Liste der berechtigten In-App-Nachrichten anfordert, diese Nachricht nicht senden und die Nachricht von diesem Gerät entfernen.

### Rate-Limiting und A/B-Tests {#rate-limiting-and-ab-testing}

Bei Verwendung von Rate-Limiting mit einem A/B-Test wird das Rate-Limit nicht auf die gleiche Weise auf die Kontrollgruppe angewendet wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen darstellt. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Conversion-Fenster.

### Zustellgeschwindigkeits-Rate-Limiting {#delivery-speed-rate-limiting}

Wenn Sie erwarten, dass große Campaigns einen Anstieg der Nutzeraktivität verursachen und Ihre Server überlasten, können Sie ein Rate-Limit pro Minute für den Nachrichtenversand festlegen, was bedeutet, dass Braze innerhalb einer Minute nicht mehr als Ihre Rate-Limit-Einstellung sendet.

Beim Targeting von Nutzer:innen während der Campaign-Erstellung können Sie zu **Target Audiences** (für Campaigns) oder **Sendeeinstellungen** (für Canvas) navigieren, um ein Rate-Limit auszuwählen (in verschiedenen Abstufungen von nur 10 bis zu 500.000 Nachrichten pro Minute).

Beachten Sie, dass Campaigns ohne Rate-Limit diese Zustellungslimits überschreiten können. Seien Sie sich jedoch bewusst, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger verzögert werden. Wenn das Rate-Limit zu niedrig ist, erhält die erstellende Person der Campaign Warnungen im Dashboard und per E-Mail.

{% alert tip %}
Legen Sie ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) fest, um ein Rate-Limit für einen gesamten Workspace durchzusetzen.
{% endalert %}

#### Beispiel {#example}

Wenn Sie versuchen, 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute zu senden, wird die Zustellung über acht Minuten verteilt. Ihre Campaign liefert in jeder der ersten sieben Minuten nicht mehr als 10.000 Nachrichten und 5.000 in der letzten Minute.

#### Anzahl der Sendungen {#number-of-sends}

Beachten Sie, dass Rate-limitierte Nachrichten möglicherweise nicht gleichmäßig über den Verlauf jeder Minute gesendet werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Dies könnte bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten in der ersten Hälfte der Minute gesendet wird als in der zweiten Hälfte.

Das Rate-Limit wird zu Beginn des Nachrichtensendeversuchs angewendet. Wenn es Schwankungen in der Zeit gibt, die für den Abschluss der Sendung benötigt wird, kann die Anzahl der abgeschlossenen Sendungen das Rate-Limit für einige Minuten leicht überschreiten. Im Laufe der Zeit wird die Anzahl der Sendungen pro Minute im Durchschnitt nicht mehr als das Rate-Limit betragen.

{% alert important %}
Seien Sie vorsichtig, zeitkritische Nachrichten mit dieser Form des Rate-Limitings in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment zu verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen enthält, wir aber das Rate-Limit auf 10.000 pro Minute setzen, wird ein großer Teil Ihrer Nutzerbasis die Nachricht erst am folgenden Tag erhalten.
{% endalert %}

#### Multichannel-Campaigns und Canvases {#multichannel-campaigns-and-canvases}

Beim Festlegen eines Zustellgeschwindigkeits-Rate-Limits für eine Multichannel-Campaign oder ein Canvas können Sie wählen, ob Sie ein gemeinsames Rate-Limit oder ein kanalbasiertes Limit festlegen möchten.

Wenn eine Multichannel-Campaign oder ein Canvas ein gemeinsames Rate-Limit verwendet, bedeutet dies, dass die Gesamtzahl der pro Minute gesendeten Nachrichten aus der Campaign oder dem Canvas das Rate-Limit nicht überschreitet. Wenn Ihr Canvas beispielsweise ein Rate-Limit von 500.000 pro Minute hat und E-Mail- und SMS-Nachrichtenschritte enthält, sendet Braze insgesamt 500.000 Nachrichten pro Minute über E-Mail und SMS.

![Die Option zur Begrenzung der Rate, mit der die Campaign sendet, ausgewählt mit 500.000 Nachrichten pro Minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Wenn eine Multichannel-Campaign oder ein Canvas kanalbasiertes Rate-Limiting verwendet, wird das Rate-Limit auf jeden Ihrer ausgewählten Kanäle angewendet. Sie können beispielsweise Ihre Campaign oder Ihr Canvas so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die Campaign oder das Canvas gesendet werden.

![Separate Rate-Limits für zwei Kanäle, Webhook und SMS/MMS/RCS, mit 5.000 bzw. 2.500 Nachrichten pro Minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Push-Benachrichtigungen {#push-notifications}

Für Campaigns oder Canvases mit Push-Plattformen (wie Android, iOS, Web-Push oder Kindle) können Sie **Push notifications** auswählen, um ein Rate-Limit durchzusetzen, das zwischen allen Push-Plattformen in Ihrer Campaign oder Ihrem Canvas geteilt wird.

![Das Kanal-Dropdown mit Optionen für Push-Plattformen und Push-Benachrichtigungen.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Wenn Sie ein Limit für Push-Benachrichtigungen auswählen, können Sie keine individuellen Push-Kanal-Rate-Limits festlegen. Ebenso können Sie keine gemeinsamen Push-Benachrichtigungslimits festlegen, wenn Sie Limits für einzelne Push-Kanäle auswählen.

{% alert important %}
**Aktualisierungen der Rate-Limiting-Oberfläche**<br>
Braze hat die Rate-Limiting-Oberfläche aktualisiert, um mehr Transparenz und Kontrolle darüber zu bieten, wie Rate-Limits auf Multichannel-Campaigns und Canvases angewendet werden.<br><br>

- **Bestehende Campaigns und Canvases:** Alle bestehenden Campaigns und Canvases wurden auf diese Oberfläche migriert. Ihr Zustellungsverhalten bleibt gleich. Das Dashboard zeigt an, ob die Campaign gemeinsame oder kanalbasierte Logik verwendet.<br>
- **Neue Campaigns und Canvases:** Für alle neuen Campaigns und Canvases gibt es einen manuellen Schalter, um Ihre bevorzugte Rate-Limit-Logik auszuwählen. Stellen Sie sicher, dass Sie das Rate-Limiting-Verhalten auswählen, das Ihrem beabsichtigten Verhalten entspricht, wenn Sie ein Rate-Limit für eine Campaign oder ein Canvas festlegen oder aktualisieren.
{% endalert %}

##### Überlegungen zum Rate-Limiting {#rate-limiting-considerations}

Einige Hinweise, die Sie bei der Konfiguration von Rate-Limits beachten sollten, und welches Verhalten Sie erwarten können:

- SMS-Sendungen unterliegen einem Rate-Limit von 50.000 pro Abo-Gruppe. Einige SMS-Anbieter können andere Limits durchsetzen.
- Die folgenden Nachrichten werden nicht durch das Rate-Limit gedrosselt oder darauf angerechnet:
    - Testsendungen
    - Seed-Gruppen
    - Content Cards, die so konfiguriert sind, dass sie „bei erster Impression“ erstellt werden (Dies wird durch die Rate der App-Impressionen gesteuert. Weitere Informationen zu den Unterschieden zwischen den Optionen zur Card-Erstellung finden Sie unter [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences).)
- Zustellgeschwindigkeits-Rate-Limits werden für Folgendes nicht unterstützt:
    - SMS-Autoantworten
    - SLA-gestützte Nachrichten (wie [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - In-App-Nachrichten
    - Feature-Flags
    - Banner

#### Rate-Limiting und Connected-Content-Wiederholungen {#rate-limiting-and-connected-content-retries}

Wenn die [Connected-Content-Wiederholung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) aktiviert ist, wiederholt Braze fehlgeschlagene Aufrufe unter Einhaltung des von Ihnen festgelegten Rate-Limits für jede erneute Sendung. Betrachten wir das Szenario des Sendens von 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute. Stellen Sie sich vor, dass in der ersten Minute der Aufruf fehlschlägt oder langsam ist und nur 4.000 Nachrichten sendet.

Anstatt zu versuchen, die Verzögerung auszugleichen und die verbleibenden 6.000 Nachrichten in der zweiten Minute zu senden oder sie zu den 10.000 hinzuzufügen, die bereits zum Senden vorgesehen sind, verschiebt Braze diese 6.000 Nachrichten ans „Ende der Warteschlange“ und fügt bei Bedarf eine Minute zur Gesamtzeit hinzu, die für den Versand Ihrer Nachricht benötigt wird.

| Minute | Kein Fehler | 6.000 Fehler in Minute 1 |
|--------|------------|---------------------------|
| 1      | 10.000     | 4.000                     |
| 2      | 10.000     | 10.000                    |
| 3      | 10.000     | 10.000                    |
| 4      | 10.000     | 10.000                    |
| 5      | 10.000     | 10.000                    |
| 6      | 10.000     | 10.000                    |
| 7      | 10.000     | 10.000                    |
| 8      | 5.000      | 10.000                    |
| 9      | 0          | 6.000                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Rate-Limiting und Connected-Content-Wiederholungen" }

Connected-Content-Anfragen werden nicht unabhängig Rate-limitiert und folgen dem Webhook-Rate-Limit. Das bedeutet, wenn es einen Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook gibt, würden Sie 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufe pro Minute erwarten. Beachten Sie, dass Caching dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Darüber hinaus können Wiederholungen die Connected-Content-Aufrufe erhöhen, daher empfehlen wir zu überprüfen, ob der Connected-Content-Endpunkt einige Schwankungen hier bewältigen kann.

{% alert note %}
**Rate-Limits sind Geschwindigkeitsbegrenzungen und definieren keine exakte Sendegeschwindigkeit.** Im Allgemeinen werden Nachrichten innerhalb einer gegebenen Minute gleichmäßig verteilt, und in der überwiegenden Mehrheit der Fälle werden sie mit oder sehr nahe am konfigurierten Limit gesendet. Dies ist nicht immer der Fall – zum Beispiel wenn Nachrichten sehr groß sind (wie E-Mails mit vielen Content Blocks, Connected-Content-Tags oder Katalog-Artikel-Tags) oder wenn es viele Liquid-Abbrüche gibt (abgebrochene Nachrichten belegen trotzdem einen Platz und können die effektive Senderate reduzieren).<br><br>
In der Praxis kann die nachhaltige Senderate (abgeschlossene Nachrichten pro Minute) aufgrund von Wiederholungen, Netzwerkvariabilität, Latenz nachgelagerter Endpunkte und minutenweiser Glättung niedriger sein als das konfigurierte Rate-Limit. Wenn Sie durchgehend einen deutlich niedrigeren Durchsatz als erwartet sehen, überprüfen Sie die Connected-Content-Antwortzeiten, Fehlerraten (wie `429`) und das Wiederholungsverhalten.
{% endalert %}

## Über Frequency-Capping {#about-frequency-capping}

Wenn Ihre Nutzerbasis weiter wächst und Ihr Messaging auf Lifecycle-, getriggerte, transaktionale und Conversion-Campaigns skaliert, ist es wichtig zu verhindern, dass Ihre Benachrichtigungen als „Spam“ oder störend empfunden werden. Durch größere Kontrolle über die Erfahrung Ihrer Nutzer:innen ermöglicht Ihnen Frequency-Capping, die gewünschten Campaigns zu erstellen, ohne Ihre Zielgruppe zu überfordern.

### Rate-Limiting und Frequency-Capping gemeinsam verwenden {#use-rate-limiting-and-frequency-capping-together}

Wenn Sie sowohl Rate-Limiting als auch Frequency-Capping für eine Campaign aktivieren, wendet Braze diese in der folgenden Reihenfolge an:

1. **Rate-Limit** wird zuerst angewendet, um den anfänglichen Pool von Nutzer:innen auszuwählen, die Nachrichten erhalten können.
2. **Frequency-Cap** wird als Zweites angewendet, um Nutzer:innen aus diesem Pool zu filtern.
3. **Nachrichten werden** an die verbleibenden Nutzer:innen gesendet.

{% alert important %}
Wenn viele Nutzer:innen in Ihrem Rate-limitierten Pool Frequency-gekappt sind, senden Sie möglicherweise weniger Nachrichten als Ihr Rate-Limit-Wert. Braze füllt keine zusätzlichen Nutzer:innen aus dem Rate-Limit nach, sobald Frequency-Capping Nutzer:innen aus dem Sendepool entfernt hat.
{% endalert %}

#### Beispiel

Mit einem Rate-Limit von 500 Nutzer:innen und aktiviertem Frequency-Capping: Wenn 200 dieser 500 Rate-limitierten Nutzer:innen Frequency-gekappt sind, werden nur 300 Nachrichten gesendet – nicht 500.

#### Empfehlungen {#recommendations}

Wenn Sie bei gleichzeitiger Verwendung beider Features eine bestimmte Anzahl von Nutzer:innen erreichen müssen, ziehen Sie die folgenden Ansätze in Betracht:

- **Erhöhen Sie Ihr Rate-Limit:** Um Nutzer:innen zu berücksichtigen, die Frequency-gekappt sind. Wenn Sie beispielsweise 500 Nutzer:innen erreichen möchten, aber erwarten, dass einige Frequency-gekappt werden, setzen Sie Ihr Rate-Limit höher (z. B. 1.000 Nutzer:innen).
- **Verwenden Sie Rate-Limiting allein:** Wenn Ihr Ziel darin besteht, das Volumen der pro Campaign gesendeten Nachrichten zu steuern.
- **Wenden Sie sich an Ihren geschäftskunden-Success-Manager:** Für Hilfe bei der Gestaltung einer robusten Messaging-Strategie, die sowohl geschäftliche Anforderungen als auch technische Überlegungen berücksichtigt.

### Feature-Übersicht {#freq-cap-feat-over}

Frequency-Capping wird auf der Sende-Ebene der Campaign oder Canvas-Komponente angewendet und kann für jeden Workspace unter **Einstellungen** > **Frequency-Capping-Regeln** eingerichtet werden.

Standardmäßig ist Frequency-Capping aktiviert, wenn neue Campaigns erstellt werden. Von hier aus können Sie Folgendes auswählen:

- Den Messaging-Kanal, den Sie begrenzen möchten: Push, E-Mail, SMS, Webhook, WhatsApp, LINE oder einen dieser Kanäle.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente erhalten soll, die von einem Kanal innerhalb eines bestimmten Zeitraums gesendet wird.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente erhalten soll, die nach [Tag](#frequency-capping-by-tag) innerhalb eines bestimmten Zeitraums gesendet wird.

Dieser Zeitraum kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, mit einer maximalen Dauer von 30 Tagen.

Jede Zeile der Frequency-Caps ist mit dem `AND`-Operator verbunden, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Sie können mehrere Obergrenzen für dieselben Nachrichtentypen einschließen. Sie können beispielsweise Nutzer:innen auf nicht mehr als einen Push pro Tag und nicht mehr als drei Pushes pro Woche begrenzen. Beachten Sie, dass abgebrochene Nachrichten nicht auf das Frequency-Capping angerechnet werden.

![Frequency-Capping-Bereich mit Listen von Campaigns und Canvases, auf die Regeln angewendet werden und nicht angewendet werden.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Verhalten, wenn Nutzer:innen bei einem Canvas-Schritt Frequency-gekappt werden oder eine Nachricht abgebrochen wird {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

Globales Frequency-Capping allein führt nicht dazu, dass Nutzer:innen ein Canvas verlassen. Bei [Nachrichtenschritten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) rücken Nutzer:innen weiterhin vor, wenn eine Nachricht aufgrund von globalem Frequency-Capping nicht gesendet wird, entsprechend der Art und Weise, [wie Nutzer:innen durch den Schritt vorrücken]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Dasselbe gilt, wenn eine Nachricht abgebrochen wird (z. B. durch eine Liquid-Abbruchbedingung): Die Nutzer:innen durchlaufen das Canvas weiter, als ob die Nachricht gesendet worden wäre.

Dies ist getrennt von den **Zustellungsvalidierungen** bei einem Nachrichtenschritt. Wenn Nutzer:innen Ihre Zustellungsvalidierungskriterien zum Sendezeitpunkt nicht erfüllen, können sie das Canvas bei diesem Schritt verlassen.

### Zustellungsregeln {#delivery-rules}

Es kann einige Campaigns geben, wie transaktionale Nachrichten, die Sie immer an die Nutzer:innen zustellen möchten, auch wenn sie ihr Frequency-Cap bereits erreicht haben. Beispielsweise möchte eine Liefer-App möglicherweise eine E-Mail oder einen Push senden, wenn ein Artikel geliefert wird, unabhängig davon, wie viele Campaigns die Nutzer:innen erhalten haben.

Wenn Sie möchten, dass eine bestimmte Campaign die Frequency-Capping-Regeln überschreibt, können Sie dies im Braze-Dashboard einrichten, wenn Sie die Zustellung dieser Campaign planen, indem Sie **Frequency Capping** auf **OFF** umschalten.

Danach werden Sie gefragt, ob diese Campaign trotzdem auf Ihr Frequency-Cap angerechnet werden soll. Nachrichten, die auf das Frequency-Capping angerechnet werden, sind in den Berechnungen für den Filter „Intelligenter Kanal“ enthalten.

Beim Senden von [API-Campaigns]({{site.baseurl}}/developer_guide/rest_api/messaging#messaging), die oft transaktional sind, haben Sie die Möglichkeit anzugeben, dass eine Campaign die Frequency-Capping-Regeln ignorieren soll, indem Sie `override_frequency_capping` in der API-Anfrage auf `true` setzen.

Standardmäßig werden neue Campaigns und Canvases, die Frequency-Caps nicht einhalten, auch nicht darauf angerechnet. Dies ist für jede Campaign und jedes Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie Frequency-Capping für eine Campaign oder ein Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und haben keinen Einfluss auf Nachrichten, die derzeit aktiv sind.
{% endalert %}

![Zustellungskontroll-Bereich mit aktiviertem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Wie Sendungen auf Obergrenzen angerechnet werden {#how-sends-count-toward-caps}

Frequency-Capping wird pro Versand angewendet: Jedes Mal, wenn Braze eine Campaign oder Canvas-Komponente an Nutzer:innen sendet, wird dies auf Ihre Obergrenzen angerechnet – nicht jede Nachrichtenvariante oder Plattform innerhalb dieser Sendung. Wenn Nutzer:innen beispielsweise auf fünf Push-Campaigns pro Woche begrenzt sind, erhalten sie nach dem fünften Versand keine weiteren Push-Campaigns mehr, bis die Obergrenze zurückgesetzt wird.

##### Multichannel-Sendungen {#multichannel-sends}

Wenn ein einzelner Versand mehrere Kanäle verwendet, wird dieser Versand höchstens einmal pro anwendbarer Frequency-Capping-Regel gezählt. Wenn Sie beispielsweise eine Multichannel-Campaign erstellen, die E-Mail, iOS-Push und Android-Push in einer Zustellung sendet, und Ihr Workspace Regeln für Push und E-Mail sowie eine Regel für alle Kanäle hat, zählt diese Zustellung einmal für die Push-Regel, einmal für die E-Mail-Regel und einmal für die Alle-Kanäle-Regel – sie zählt nicht einmal pro Push-Plattform oder pro Nachricht innerhalb der Sendung. Wenn Nutzer:innen auf eine Push- und eine E-Mail-Campaign pro Tag begrenzt sind und diese Multichannel-Campaign erhalten, sind sie für den Rest des Tages nicht mehr für zusätzliche Push- oder E-Mail-Campaigns berechtigt, es sei denn, eine Campaign ignoriert die Frequency-Capping-Regeln.

In-App-Nachrichten und Content Cards werden nicht als Obergrenzen für Campaigns oder Canvas-Komponenten beliebigen Typs gezählt oder darauf angerechnet.

##### Push-Benachrichtigungen mit mehreren Geräten {#push-notifications-with-multiple-devices}

Für Push-Campaigns wird Frequency-Capping auf Campaign- oder Canvas-Komponentenebene gezählt, nicht pro einzelnem Gerät. Wenn ein Nutzerprofil mehrere Geräte für Push registriert hat (z. B. ein iPhone und ein iPad), zählt ein Frequency-Cap auf Campaign-Ebene dies als eine Sendung, unabhängig davon, wie viele Geräte die Benachrichtigung erhalten. Dies ist vergleichbar damit, wie eine wiederkehrende Campaign mit täglicher Kadenz als eine Sendung pro Tag zählt, auch wenn sie im Laufe der Woche mehrmals wiederholt wird.

{% alert important %}
Globales Frequency-Capping wird basierend auf der Zeitzone der Nutzer:innen geplant und nach Kalendertagen berechnet, nicht nach 24-Stunden-Zeiträumen. Wenn Sie beispielsweise eine Frequency-Capping-Regel einrichten, die nicht mehr als eine Campaign pro Tag sendet, können Nutzer:innen um 23 Uhr in ihrer lokalen Zeitzone eine Nachricht erhalten und wären eine Stunde später für eine weitere Nachricht berechtigt.
{% endalert %}

#### Anwendungsfälle {#use-cases}

{% tabs %}
{% tab Anwendungsfall 1 %}

Nehmen wir an, Sie legen eine Frequency-Capping-Regel fest, sodass Ihre Nutzer:innen nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte pro Woche von allen Campaigns oder Canvas-Schritten erhalten.

Wenn Ihre Nutzer:innen diese Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content-Card erhalten sollen, werden sie alle diese Nachrichten erhalten.

{% endtab %}
{% tab Anwendungsfall 2 %}

Dieses Szenario verwendet eine Frequency-Capping-Regel, dass Nutzer:innen nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte pro Woche von allen Campaigns oder Canvas-Schritten erhalten.

**Wenn folgendes Szenario eintritt:**

- Nutzer:innen triggern dieselbe Campaign `Campaign ABC` dreimal im Laufe einer Woche.
- Diese Nutzer:innen triggern `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Frequency-Capping-Bereich mit der Regel, nicht mehr als 2 Push-Benachrichtigungs-Campaigns/Canvas-Schritte von allen Campaigns/Canvas-Schritten an Nutzer:innen pro 1 Woche zu senden.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann ist das erwartete Verhalten:**

- Diese Nutzer:innen erhalten die Campaign-Sendungen, die am Montag und Mittwoch getriggert wurden.
- Diese Nutzer:innen erhalten die dritte Campaign-Sendung am Donnerstag nicht, da sie bereits zwei Push-Campaign-Sendungen in dieser Woche erhalten haben.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag {#frequency-capping-by-tag}

[Frequency-Capping-Regeln](#delivery-rules) können auf Workspaces angewendet werden, indem bestimmte Tags verwendet werden, die Sie auf Ihre Campaigns und Canvases angewendet haben, sodass Sie Ihr Frequency-Capping im Wesentlichen auf benutzerdefiniert benannte Gruppen basieren können.

Beim Frequency-Capping nach Tag können Regeln auf Haupt- und verschachtelte Tags angewendet werden, sodass Braze alle Tags berücksichtigt. Wenn Sie beispielsweise den Haupt-Tag A als Frequency-Cap ausgewählt haben, berücksichtigen wir auch alle Informationen in den verschachtelten Tags (z. B. Tags B und C) bei der Bestimmung des Limits.

Sie können auch reguläres Frequency-Capping mit Frequency-Capping nach Tags kombinieren. Betrachten Sie die folgenden Regeln:

1. Nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten. <br>**UND**
2. Nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit zwei Regeln, die begrenzen, wie viele Push-Benachrichtigungs-Campaigns/Canvases pro 1 Woche an Nutzer:innen gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Nutzer:innen nicht mehr als drei Campaign-Sendungen pro Woche über alle Campaigns und Canvas-Schritte und nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Canvases werden auf Canvas-Ebene getaggt, im Gegensatz zum Tagging nach Komponente. Jede Canvas-Komponente erbt also alle Tags auf Canvas-Ebene.
{% endalert %}

#### Widersprüchliche Regeln {#conflicting-rules}

Wenn Regeln in Konflikt stehen, wird die restriktivste, anwendbare Frequency-Capping-Regel auf Ihre Nutzer:innen angewendet. Nehmen wir beispielsweise an, Sie haben die folgenden Regeln:

1. Nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente pro Woche von allen Campaigns und Canvas-Komponenten. <br>**UND**
2. Nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit widersprüchlichen Regeln zur Begrenzung, wie viele Push-Benachrichtigungs-Campaigns/Canvas-Schritte pro 1 Woche an Nutzer:innen gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel erhalten Ihre Nutzer:innen nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente mit dem Tag „promotional“ in einer bestimmten Woche, da Sie festgelegt haben, dass Nutzer:innen nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente von allen Campaigns und Canvas-Komponenten erhalten sollen. Mit anderen Worten: Die restriktivste anwendbare Frequency-Regel ist die Regel, die auf bestimmte Nutzer:innen angewendet wird.

#### Tag-Zählung {#tag-count}

Frequency-Capping-nach-Tag-Regeln werden zum Zeitpunkt des Nachrichtenversands berechnet. Das bedeutet, dass Frequency-Capping nach Tag nur Tags zählt, die derzeit auf den Campaigns oder Canvases sind, die Nutzer:innen in der Vergangenheit erhalten haben. Es zählt nicht die Tags, die auf den Campaigns oder Canvases zum Zeitpunkt des Versands waren, aber seitdem entfernt wurden. Es zählt, wenn ein Tag später zu einer Nachricht hinzugefügt wird, die Nutzer:innen in der Vergangenheit erhalten haben, aber bevor die neueste getaggte Nachricht gesendet wird.

##### Anwendungsfall {#use-case}

Betrachten Sie die folgenden Campaigns und die Frequency-Capping-nach-Tag-Regel:

**Campaigns**:

- **Campaign A** ist eine Push-Campaign mit dem Tag `promotional`. Sie ist für den Versand am Montag um 9 Uhr geplant.
- **Campaign B** ist eine Push-Campaign mit dem Tag `promotional`. Sie ist für den Versand am Mittwoch um 9 Uhr geplant.

**Frequency-Capping-nach-Tag-Regel:**

- Ihre Nutzer:innen sollen nicht mehr als eine Push-Benachrichtigungs-Campaign pro Woche mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Der Tag `promotional` wird von **Campaign A** entfernt, nachdem Ihre Nutzer:innen die Nachricht erhalten haben, aber bevor **Campaign B gesendet wurde.** | Ihre Nutzer:innen erhalten **Campaign B**. |
| Der Tag `promotional` wird versehentlich von **Campaign A** entfernt, nachdem Ihre Nutzer:innen die Nachricht erhalten haben. <br> Der Tag wird am Dienstag wieder zu **Campaign A** hinzugefügt, bevor **Campaign B** gesendet wird. | Ihre Nutzer:innen erhalten **Campaign B** nicht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfall" }

#### Versand in großem Umfang {#sending-at-large-scales}

Frequency-Capping-nach-Tag-Regeln werden bei großem Umfang möglicherweise nicht korrekt angewendet, z. B. bei 100 Nachrichten pro Kanal von Campaigns oder Canvas-Komponenten.

Wenn Ihre Frequency-Capping-nach-Tag-Regel beispielsweise lautet:

> Nicht mehr als zwei E-Mail-Campaigns oder Canvas-Komponenten mit dem Tag `Promotional` an Nutzer:innen pro Woche.

Und Sie den Nutzer:innen im Laufe einer Woche mehr als 100 E-Mails von Campaigns und Canvas-Schritten mit aktiviertem Frequency-Capping senden, können mehr als zwei E-Mails an die Nutzer:innen gesendet werden.

Da 100 Nachrichten pro Kanal mehr Nachrichten sind, als die meisten Marken an ihre Nutzer:innen senden, ist es unwahrscheinlich, dass Sie von dieser Einschränkung betroffen sind. Um diese Einschränkung zu vermeiden, können Sie eine Obergrenze für die maximale Anzahl von E-Mails festlegen, die Ihre Nutzer:innen im Laufe einer Woche erhalten sollen.

Sie könnten beispielsweise die folgende Regel einrichten:

> Nicht mehr als drei E-Mail-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten.

Diese Regel stellt sicher, dass keine Nutzer:innen mehr als 100 E-Mails pro Woche erhalten, da Nutzer:innen höchstens drei E-Mails pro Woche von Campaigns oder Canvas-Komponenten mit aktiviertem Frequency-Capping erhalten.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wenn ich eine Sendedrosselung in einem aktiven Canvas ändere, wirkt sich das auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Ja. Wenn Sie ein Canvas-Rate-Limit erhöhen oder verringern, gilt das aktualisierte Limit für neue Nachrichten innerhalb von etwa 30 Sekunden nach der Änderung aufgrund von Caching.

### Führt Frequency-Capping dazu, dass Nutzer:innen ein Canvas verlassen? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Nein. Wenn Nutzer:innen in einem Canvas aufgrund globaler Frequency-Capping-Einstellungen Frequency-gekappt werden, rücken sie sofort zum nächsten Canvas-Schritt vor. Die Nutzer:innen verlassen das Canvas **nicht** aufgrund des Frequency-Caps.

### Wie kann ich Nutzer:innen identifizieren, die in einem Canvas Frequency-gekappt wurden? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Nutzer:innen, die Frequency-gekappt werden, erzeugen kein Sende-Ereignis für diesen Schritt. Um diese Nutzer:innen zu identifizieren, können Sie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) verwenden, um Frequency-Capping-Ereignisse für Nachrichten zu verfolgen. Alternativ können Sie eine [Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension) erstellen, um Nutzer:innen zu analysieren, die das Canvas betreten haben, aber die erwartete Nachricht nicht erhalten haben.

### Warum zeigt das Dashboard einen Rate-Limit-Fehler für meine Campaign an? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Dies bedeutet in der Regel, dass das [Zustellgeschwindigkeits-Rate-Limit](#delivery-speed-rate-limiting) der Campaign für die Zielgruppengröße zu niedrig eingestellt ist, sodass der Abschluss der Sendung länger dauern würde als das zulässige Fenster und Braze eine Warnung anzeigt. Erhöhen Sie das Zustellgeschwindigkeits-Rate-Limit, reduzieren Sie die Zielgruppe oder verwenden Sie **Limit send volume**, damit jeder geplante Versand innerhalb des zulässigen Sendefensters abgeschlossen wird. Sie können auch ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) festlegen, um eine Obergrenze über alle Campaigns hinweg durchzusetzen.

**Limit send volume** steuert, wie viele Nutzer:innen für eine Sendung berechtigt sind, nicht wie viele Nachrichten Braze pro Minute sendet. Nur ein Zustellgeschwindigkeits-Rate-Limit legt den Durchsatz pro Minute fest.

### Was bedeutet „Gesendet“ für Frequency-Capping? {#what-does-sent-mean-for-frequency-capping}

In Analytics und Frequency-Capping bezieht sich _Gesendet_ darauf, wann Braze die Nachricht versendet (die Sendung wird erfasst), nicht auf die garantierte endgültige Zustellung an das Gerät oder den Posteingang. Frequency-Capping und Sendezählungen verwenden diese erfassten Sende-Ereignisse, die von nachgelagerten „Zugestellt“-Metriken abweichen können.

### Warum sehe ich E-Mail-Bounces oder Zurückstellungen? {#why-am-i-seeing-email-bounces-or-deferrals}

E-Mail-Bounce- und Zurückstellungsnachrichten verwenden viele verschiedene Codes und anbieterspezifische Texte. Behandeln Sie einen bestimmten Code nicht als Zeichen eines Rate-Limiting-Problems, da die Ursache von Ihrem Sendekontext und dem Feedback des Mailbox-Anbieters abhängt.

Wenn Nachrichten vorübergehend zurückgestellt werden, kann weniger Senden kurzfristig helfen. Verwenden Sie ein [Zustellgeschwindigkeits-Rate-Limit](#delivery-speed-rate-limiting), **Limit send volume** oder beides.

Für eine langfristige Lösung arbeiten Sie mit einem Zustellbarkeitsexperten zusammen, um Ihre Bounce- und Zurückstellungsdaten zu überprüfen.