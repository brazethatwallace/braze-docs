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

Braze ermöglicht es Ihnen, den Marketingdruck zu steuern, indem Sie Ihre Campaigns mit Rate-Limiting versehen und den Umfang des ausgehenden Traffics von Ihrer Plattform regulieren. Sie können zwei verschiedene Arten von Rate-Limiting für Ihre Campaigns implementieren:

1. [Nutzer:innenzentriertes Rate-Limiting:](#user-centric-rate-limiting) Konzentriert sich darauf, die beste Erfahrung für Nutzer:innen zu bieten.
2. [Zustellgeschwindigkeits-Rate-Limiting:](#delivery-speed-rate-limiting) Berücksichtigt die Bandbreite Ihrer Server.

Braze unterstützt kein Rate-Limit pro Sekunde. Braze versucht, den Nachrichtenversand gleichmäßig über die Minute zu verteilen, kann dies aber nicht garantieren. Wenn Sie beispielsweise eine Campaign mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), aber es kann zu Abweichungen bei der Rate pro Sekunde kommen.

### Nutzer:innenzentriertes Rate-Limiting {#user-centric-rate-limiting}

Wenn Sie mehr Segmente erstellen, wird es Fälle geben, in denen sich die Mitgliedschaft dieser Segmente überschneidet. Wenn Sie Campaigns an diese Segmente senden, möchten Sie sicherstellen, dass Sie Ihre Nutzer:innen nicht zu häufig kontaktieren. Wenn Nutzer:innen innerhalb eines kurzen Zeitraums zu viele Nachrichten erhalten, fühlen sie sich überlastet und deaktivieren entweder Push-Benachrichtigungen oder deinstallieren Ihre App.

#### Relevante Segment-Filter {#relevant-segment-filters}

Braze bietet die folgenden Filter, um Ihnen zu helfen, die Rate zu begrenzen, mit der Ihre Nutzer:innen Nachrichten erhalten:

- Letzte Interaktion mit Nachricht
- Letzte empfangene Nachricht
- Letzter empfangener Push
- Letzte empfangene E-Mail
- Letzte empfangene SMS

#### Filter implementieren {#implementing-filters}

Nehmen wir an, wir haben ein Segment namens „Retargeting Filter Showcase“ mit dem Filter „App zuletzt vor mehr als 7 Tagen verwendet“ erstellt, um Nutzer:innen anzusprechen. Dies wäre ein standardmäßiges Segment zur erneuten Interaktion.

Wenn Sie andere, gezieltere Segmente haben, die kürzlich Benachrichtigungen erhalten haben, möchten Sie möglicherweise nicht, dass Ihre Nutzer:innen von allgemeineren Campaigns angesprochen werden, die auf dieses Segment ausgerichtet sind. Durch Hinzufügen des Filters „Letzter empfangener Push“ zu diesem Segment hat der:die Nutzer:in sichergestellt, dass er:sie, wenn er:sie in den letzten 24 Stunden eine andere Benachrichtigung erhalten hat, für die nächsten 24 Stunden aus diesem Segment herausfällt. Wenn er:sie 24 Stunden später immer noch die anderen Kriterien des Segments erfüllt und keine weiteren Benachrichtigungen erhalten hat, wird er:sie wieder in das Segment aufgenommen.

![Ein Segment namens „Retargeting Filter Showcase“ mit der Filtergruppe „App zuletzt vor mehr als 7 Tagen verwendet“.]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Das Hinzufügen dieses Filters zu allen Segmenten, die von Campaigns angesprochen werden, würde dazu führen, dass Ihre Nutzer:innen maximal einen Push alle 24 Stunden erhalten. Sie könnten dann Ihr Messaging priorisieren, indem Sie sicherstellen, dass Ihre wichtigsten Nachrichten vor weniger wichtigen Nachrichten zugestellt werden.

#### Maximale Nutzer:innenobergrenze festlegen {#setting-a-maximum-user-cap}

Im Schritt **Target Audiences** Ihres Campaign-Composers können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten. Dies dient als Prüfung, die unabhängig von Ihren Campaign-Filtern ist.

![Zielgruppen-Zusammenfassung mit einem ausgewählten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Campaign erhalten.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Durch Auswahl der maximalen Nutzer:innenobergrenze können Sie das Nachrichtenvolumen auf Kanalbasis oder global über alle Nachrichtentypen hinweg begrenzen. Braze versendet keine Nachrichten an Nutzer:innen, die Kontrollgruppen zugewiesen sind, sodass diese nicht auf das Limit angerechnet werden.

{% alert note %}
Die maximale Nutzer:innenobergrenze begrenzt die Anzahl der versendeten Nutzer:innen, nicht die Anzahl der erfolgreich zugestellten Nachrichten. Da abgebrochene Nachrichten auf diese Obergrenze angerechnet werden, kann die tatsächliche Anzahl gesendeter Nachrichten niedriger sein als das konfigurierte Limit. Wenn Sie beispielsweise eine Obergrenze von 10.000 festlegen und 2.000 Nachrichten aufgrund von Liquid-Logik oder anderen Bedingungen abgebrochen werden, werden nur 8.000 Nachrichten gesendet.
{% endalert %}

##### Maximale Nutzer:innenobergrenze für Multichannel-Kampagnen {#maximum-user-cap-for-multichannel-campaigns}

Für Multichannel-Kampagnen wählt Braze zunächst eine Zielgruppe bis zu Ihrer konfigurierten maximalen Nutzer:innenobergrenze aus. Braze bewertet dann jede:n Nutzer:in in dieser begrenzten Zielgruppe für jeden Kanal in der Campaign.

Dadurch bleibt die begrenzte Zielgruppengröße gleich, aber die Versendungen pro Kanal können je nach Kanalberechtigung variieren. Wenn Sie beispielsweise eine maximale Nutzer:innenobergrenze von 500.000 festlegen und ein:e Nutzer:in nur für Push und Content Cards berechtigt ist, erhält diese:r Nutzer:in diese Kanäle, aber keine E-Mail.

Wenn Sie diese Kanäle in separate Campaigns aufteilen, die jeweils dasselbe Segment ansprechen und jeweils eine eigene maximale Nutzer:innenobergrenze haben, bewertet und begrenzt jede Campaign Nutzer:innen unabhängig. Braze garantiert nicht, dass jede Campaign genau dieselbe Teilmenge von Nutzer:innen auswählt.

Wenn Sie Folge-Campaigns benötigen, die Nutzer:innen ansprechen, denen eine frühere Campaign gesendet wurde, erstellen Sie ein Segment mit dem Filter **Campaign erhalten** und verwenden Sie dieses Segment dann für die Folge-Campaigns.

##### Maximale Nutzer:innenobergrenze mit Optimierungen {#maximum-user-cap-with-optimizations}

Wenn Sie eine Optimierung wie Gewinnervariante oder Personalisierte Variante verwenden, besteht die Campaign aus zwei Versendungen: dem anfänglichen Experiment und dem endgültigen Versand.

Um eine maximale Nutzer:innenobergrenze in diesem Szenario einzurichten, wählen Sie **Anzahl der Personen begrenzen, die diese Campaign erhalten**, dann wählen Sie **Insgesamt soll diese Campaign** und geben Sie ein Zielgruppenlimit ein. Ihr Zielgruppenlimit wird nach den im **A/B-Tests**-Panel angezeigten Prozentsätzen aufgeteilt.

Wenn Sie **Jedes Mal, wenn die Campaign geplant ist** auswählen, werden diese beiden Phasen separat auf die festgelegte Anzahl begrenzt. Dies ist in der Regel nicht erwünscht.

#### Maximale Impressionen-Obergrenze für Campaigns festlegen {#setting-a-maximum-impression-cap-on-campaigns}

Für In-App-Nachrichten können Sie den Marketingdruck steuern, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Nutzerbasis angezeigt werden, wonach Braze keine weiteren Nachrichten mehr an Ihre Nutzer:innen sendet. Es ist jedoch wichtig zu beachten, dass diese Obergrenze nicht exakt ist.

In-App-Nachrichtenregeln werden bei Sitzungsbeginn an eine App gesendet, was bedeutet, dass Braze eine Nachricht an Nutzer:innen senden kann, bevor die Obergrenze erreicht ist, aber bis Nutzer:innen die Nachricht auslösen, wurde die Obergrenze bereits erreicht. In dieser Situation zeigt das Gerät die Nachricht trotzdem an.

Nehmen wir beispielsweise an, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn Nutzer:innen ein Level abschließen, und Sie begrenzen sie auf 100 Impressionen. Es gab bisher 99 Impressionen. Alice und Bob öffnen beide das Spiel, und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu erhalten, wenn sie ein Level abschließen. Alice schließt zuerst ein Level ab und erhält die Nachricht. Bob schließt als Nächstes das Level ab, aber da sein Gerät seit Sitzungsbeginn nicht mit den Braze-Servern kommuniziert hat, weiß sein Gerät nicht, dass die Nachricht ihre Obergrenze erreicht hat, und er erhält die Nachricht ebenfalls. Wenn jedoch eine Impressionen-Obergrenze erreicht wurde, sendet das System beim nächsten Mal, wenn ein Gerät die Liste der berechtigten In-App-Nachrichten anfordert, diese Nachricht nicht und entfernt die Nachricht von diesem Gerät.

### Rate-Limiting und A/B-Tests {#rate-limiting-and-ab-testing}

Bei der Verwendung von Rate-Limiting mit einem A/B-Test wird das Rate-Limit nicht auf die gleiche Weise auf die Kontrollgruppe angewendet wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen darstellt. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Konversionsfenster.

### Zustellgeschwindigkeits-Rate-Limiting {#delivery-speed-rate-limiting}

Wenn Sie erwarten, dass große Campaigns einen Anstieg der Nutzer:innenaktivität verursachen und Ihre Server überlasten, können Sie ein Rate-Limit pro Minute für den Nachrichtenversand festlegen, was bedeutet, dass Braze innerhalb einer Minute nicht mehr als Ihre Rate-Limit-Einstellung sendet.

Beim Targeting von Nutzer:innen während der Campaign-Erstellung können Sie zu **Target Audiences** (für Campaigns) oder **Send Settings** (für Canvas) navigieren, um ein Rate-Limit auszuwählen (in verschiedenen Abstufungen von nur 10 bis zu 500.000 Nachrichten pro Minute).

Beachten Sie, dass Campaigns ohne Rate-Limit diese Zustellungslimits überschreiten können. Seien Sie sich jedoch bewusst, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger verzögert werden. Wenn das Rate-Limit zu niedrig ist, erhält der:die Ersteller:in der Campaign Warnungen im Dashboard und per E-Mail.

{% alert tip %}
Legen Sie ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) fest, um ein Rate-Limit für einen gesamten Workspace durchzusetzen.
{% endalert %}

#### Beispiel {#example}

Wenn Sie versuchen, 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute zu senden, wird die Zustellung über acht Minuten verteilt. Ihre Campaign liefert in jeder der ersten sieben Minuten nicht mehr als 10.000 Nachrichten und 5.000 in der letzten Minute.

#### Anzahl der Versendungen {#number-of-sends}

Beachten Sie, dass Nachrichten mit Rate-Limit möglicherweise nicht gleichmäßig über den Verlauf jeder Minute gesendet werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Dies könnte bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten in der ersten Hälfte der Minute gesendet wird als in der zweiten Hälfte.

Das Rate-Limit wird zu Beginn des Nachrichtenversandversuchs angewendet. Wenn es Schwankungen in der Zeit gibt, die für den Abschluss des Versands benötigt wird, kann die Anzahl der abgeschlossenen Versendungen das Rate-Limit für einige Minuten leicht überschreiten. Im Laufe der Zeit wird die Anzahl der Versendungen pro Minute im Durchschnitt nicht mehr als das Rate-Limit betragen.

{% alert important %}
Seien Sie vorsichtig, zeitkritische Nachrichten mit dieser Form des Rate-Limitings in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment zu verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen enthält, wir aber das Rate-Limit auf 10.000 pro Minute setzen, wird ein großer Teil Ihrer Nutzerbasis die Nachricht erst am folgenden Tag erhalten.
{% endalert %}

#### Multichannel-Kampagnen und Canvases {#multichannel-campaigns-and-canvases}

Beim Festlegen eines Zustellgeschwindigkeits-Rate-Limits für eine Multichannel-Kampagne oder ein Canvas können Sie wählen, ob Sie ein gemeinsames Rate-Limit oder ein kanalbasiertes Limit festlegen möchten.

Wenn eine Multichannel-Kampagne oder ein Canvas ein gemeinsames Rate-Limit verwendet, bedeutet dies, dass die Gesamtzahl der pro Minute gesendeten Nachrichten aus der Campaign oder dem Canvas das Rate-Limit nicht überschreitet. Wenn Ihr Canvas beispielsweise ein Rate-Limit von 500.000 pro Minute hat und E-Mail- und SMS-Nachrichtenschritte enthält, sendet Braze insgesamt 500.000 Nachrichten pro Minute über E-Mail und SMS.

![Die Option zur Begrenzung der Rate, mit der die Campaign sendet, ausgewählt mit 500.000 Nachrichten pro Minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Wenn eine Multichannel-Kampagne oder ein Canvas kanalbasiertes Rate-Limiting verwendet, wird das Rate-Limit auf jeden Ihrer ausgewählten Kanäle angewendet. Sie können beispielsweise Ihre Campaign oder Ihr Canvas so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die Campaign oder das Canvas gesendet werden.

![Separate Rate-Limits für zwei Kanäle, Webhook und SMS/MMS/RCS, mit 5.000 bzw. 2.500 Nachrichten pro Minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Push-Benachrichtigungen {#push-notifications}

Für Campaigns oder Canvases mit Push-Plattformen (wie Android, iOS, Web-Push oder Kindle) können Sie **Push-Benachrichtigungen** auswählen, um ein Rate-Limit durchzusetzen, das zwischen allen Push-Plattformen in Ihrer Campaign oder Ihrem Canvas geteilt wird.

![Das Kanal-Dropdown mit Optionen für Push-Plattformen und Push-Benachrichtigungen.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Wenn Sie ein Limit für Push-Benachrichtigungen auswählen, können Sie keine individuellen Push-Kanal-Rate-Limits festlegen. Ebenso können Sie, wenn Sie Limits für einzelne Push-Kanäle auswählen, keine gemeinsamen Push-Benachrichtigungslimits festlegen.

{% alert important %}
**Aktualisierungen der Rate-Limiting-Oberfläche**<br>
Braze hat die Rate-Limiting-Oberfläche aktualisiert, um mehr Transparenz und Kontrolle darüber zu bieten, wie Rate-Limits auf Multichannel-Kampagnen und Canvases angewendet werden.<br><br>

- **Bestehende Campaigns und Canvases:** Alle bestehenden Campaigns und Canvases wurden auf diese Oberfläche migriert. Ihr Zustellverhalten bleibt gleich. Das Dashboard zeigt an, ob die Campaign gemeinsame oder kanalbasierte Logik verwendet.<br>
- **Neue Campaigns und Canvases:** Für alle neuen Campaigns und Canvases gibt es einen manuellen Umschalter, um Ihre bevorzugte Rate-Limit-Logik auszuwählen. Stellen Sie sicher, dass Sie das Rate-Limiting-Verhalten auswählen, das mit Ihrem beabsichtigten Verhalten übereinstimmt, wenn Sie ein Campaign- oder Canvas-Rate-Limit festlegen oder aktualisieren.
{% endalert %}

##### Überlegungen zum Rate-Limiting {#rate-limiting-considerations}

Einige Hinweise, die Sie bei der Konfiguration von Rate-Limits beachten sollten, und welches Verhalten Sie erwarten können:

- SMS-Versendungen unterliegen einem Rate-Limit von 50.000 pro Abo-Gruppe. Einige SMS-Anbieter können andere Limits durchsetzen.
- Die folgenden Nachrichten werden nicht durch das Rate-Limit gedrosselt oder darauf angerechnet:
    - Testversendungen
    - Seed-Gruppen
    - Content Cards, die so konfiguriert sind, dass sie „bei erster Impression“ erstellt werden (Dies wird durch die Rate der App-Impressionen gesteuert. Weitere Informationen zu den Unterschieden zwischen den Optionen zur Card-Erstellung finden Sie unter [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences).)
- Zustellgeschwindigkeits-Rate-Limits werden für Folgendes nicht unterstützt:
    - SMS-Autoantworten
    - SLA-gestützte Nachrichten (wie [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - In-App-Nachrichten
    - Feature-Flags
    - Banner

#### Rate-Limiting und Connected-Content-Wiederholungen {#rate-limiting-and-connected-content-retries}

Wenn die [Connected-Content-Wiederholung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) aktiviert ist, wiederholt Braze fehlgeschlagene Aufrufe unter Einhaltung des Rate-Limits, das Sie für jede erneute Versendung festgelegt haben. Betrachten wir das Szenario des Versands von 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute. Stellen Sie sich vor, dass in der ersten Minute der Aufruf fehlschlägt oder langsam ist und nur 4.000 Nachrichten sendet.

Anstatt zu versuchen, die Verzögerung auszugleichen und die verbleibenden 6.000 Nachrichten in der zweiten Minute zu senden oder sie zu den 10.000 hinzuzufügen, die bereits zum Versand vorgesehen sind, verschiebt Braze diese 6.000 Nachrichten ans „Ende der Warteschlange“ und fügt bei Bedarf eine Minute zur Gesamtzeit hinzu, die für den Versand Ihrer Nachricht benötigt wird.

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

Connected-Content-Anfragen werden nicht unabhängig mit Rate-Limits versehen und folgen dem Webhook-Rate-Limit. Das bedeutet, wenn es einen Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook gibt, würden Sie 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufe pro Minute erwarten. Beachten Sie, dass Caching dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Darüber hinaus können Wiederholungen die Connected-Content-Aufrufe erhöhen, daher empfehlen wir zu überprüfen, ob der Connected-Content-Endpunkt einige Schwankungen hier bewältigen kann.

{% alert note %}
**Rate-Limits sind Geschwindigkeitsbegrenzungen und definieren keine exakte Versandgeschwindigkeit.** Im Allgemeinen werden Nachrichten innerhalb einer gegebenen Minute gleichmäßig verteilt, und in der überwiegenden Mehrheit der Fälle werden sie mit oder sehr nahe am konfigurierten Limit gesendet. Dies ist nicht immer der Fall – zum Beispiel wenn Nachrichten sehr groß sind (wie E-Mails mit vielen Content Blocks, Connected-Content-Tags oder Katalog-Artikel-Tags) oder wenn es viele Liquid-Abbrüche gibt (abgebrochene Nachrichten belegen trotzdem einen Platz und können die effektive Versandrate reduzieren).<br><br>
In der Praxis kann die nachhaltige Versandrate (abgeschlossene Nachrichten pro Minute) aufgrund von Wiederholungen, Netzwerkvariabilität, Latenz nachgelagerter Endpunkte und Glättung pro Minute niedriger sein als das konfigurierte Rate-Limit. Wenn Sie durchgehend einen deutlich niedrigeren Durchsatz als erwartet feststellen, überprüfen Sie die Connected-Content-Antwortzeiten, Fehlerraten (wie `429`) und das Wiederholungsverhalten.
{% endalert %}

## Über Frequency-Capping {#about-frequency-capping}

Wenn Ihre Nutzerbasis weiter wächst und Ihr Messaging auf Lifecycle-, getriggerte, transaktionale und Konversions-Campaigns ausgeweitet wird, ist es wichtig, dass Ihre Benachrichtigungen nicht als „Spam“ oder störend wahrgenommen werden. Durch eine bessere Kontrolle über die Erfahrung Ihrer Nutzer:innen ermöglicht Ihnen Frequency-Capping, die gewünschten Campaigns zu erstellen, ohne Ihre Zielgruppe zu überfordern.

### Rate-Limiting und Frequency-Capping gemeinsam verwenden {#use-rate-limiting-and-frequency-capping-together}

Wenn Sie sowohl Rate-Limiting als auch Frequency-Capping für eine Campaign aktivieren, wendet Braze diese in der folgenden Reihenfolge an:

1. **Rate-Limit** wird zuerst angewendet, um den anfänglichen Pool von Nutzer:innen auszuwählen, die Nachrichten erhalten können.
2. **Frequency-Cap** wird als Zweites angewendet, um Nutzer:innen aus diesem Pool herauszufiltern.
3. **Nachrichten werden gesendet** an die verbleibenden Nutzer:innen.

{% alert important %}
Wenn viele Nutzer:innen in Ihrem Rate-Limited-Pool vom Frequency-Capping betroffen sind, senden Sie möglicherweise weniger Nachrichten als Ihr Rate-Limit-Wert. Braze füllt keine zusätzlichen Nutzer:innen aus dem Rate-Limit nach, sobald das Frequency-Capping Nutzer:innen aus dem Sendepool entfernt hat.
{% endalert %}

#### Beispiel

Bei einem Rate-Limit von 500 Nutzer:innen und aktiviertem Frequency-Capping werden nur 300 Nachrichten gesendet – nicht 500 –, wenn 200 dieser 500 Rate-Limited-Nutzer:innen vom Frequency-Capping betroffen sind.

#### Empfehlungen {#recommendations}

Wenn Sie bei gleichzeitiger Verwendung beider Features eine bestimmte Anzahl von Nutzer:innen erreichen müssen, ziehen Sie die folgenden Ansätze in Betracht:

- **Erhöhen Sie Ihr Rate-Limit:** Um Nutzer:innen zu berücksichtigen, die vom Frequency-Capping betroffen sind. Wenn Sie beispielsweise 500 Nutzer:innen erreichen möchten, aber erwarten, dass einige vom Frequency-Capping betroffen sind, setzen Sie Ihr Rate-Limit höher an (z. B. 1.000 Nutzer:innen).
- **Verwenden Sie Rate-Limiting allein:** Wenn Ihr Ziel darin besteht, das Volumen der pro Campaign gesendeten Nachrichten zu steuern.
- **Wenden Sie sich an Ihren Customer-Success-Manager:** Für Hilfe bei der Gestaltung einer robusten Messaging-Strategie, die sowohl geschäftliche Anforderungen als auch technische Überlegungen in Einklang bringt.

### Feature-Übersicht {#freq-cap-feat-over}

Frequency-Capping wird auf der Sende-Ebene der Campaign oder Canvas-Komponente angewendet und kann für jeden Workspace unter **Einstellungen** > **Frequency-Capping-Regeln** eingerichtet werden.

Standardmäßig ist Frequency-Capping aktiviert, wenn neue Campaigns erstellt werden. Von hier aus können Sie Folgendes auswählen:

- Den Messaging-Kanal, den Sie begrenzen möchten: Push, E-Mail, SMS, Webhook, WhatsApp, LINE oder einen beliebigen dieser Kanäle.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente erhalten soll, die über einen Kanal innerhalb eines bestimmten Zeitraums gesendet wird.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente erhalten soll, die nach [Tag](#frequency-capping-by-tag) innerhalb eines bestimmten Zeitraums gesendet wird.

Dieser Zeitraum kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, mit einer maximalen Dauer von 30 Tagen.

Jede Zeile der Frequency-Caps ist mit dem `AND`-Operator verbunden, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Sie können mehrere Caps für dieselben Nachrichtentypen einschließen. Beispielsweise können Sie Nutzer:innen auf nicht mehr als einen Push pro Tag und nicht mehr als drei Pushes pro Woche begrenzen. Beachten Sie, dass abgebrochene Nachrichten nicht auf das Frequency-Capping angerechnet werden.

![Frequency-Capping-Bereich mit Listen von Campaigns und Canvases, auf die Regeln angewendet werden und nicht angewendet werden.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Verhalten, wenn Nutzer:innen vom Frequency-Capping betroffen sind oder eine Nachricht in einem Canvas-Schritt abgebrochen wird {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

Globales Frequency-Capping allein lässt Nutzer:innen nicht aus einem Canvas aussteigen. Bei [Nachrichtenschritten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) kommen Nutzer:innen weiterhin voran, wenn eine Nachricht aufgrund des globalen Frequency-Cappings nicht gesendet wird, entsprechend der Logik, [wie Nutzer:innen vorankommen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Dasselbe gilt, wenn eine Nachricht abgebrochen wird (z. B. durch eine Liquid-Abbruchbedingung): Die:der Nutzer:in durchläuft den Canvas weiter, als ob die Nachricht gesendet worden wäre.

Dies ist getrennt von den **Zustellungsvalidierungen** in einem Nachrichtenschritt. Wenn ein:e Nutzer:in Ihre Zustellungsvalidierungskriterien zum Sendezeitpunkt nicht erfüllt, kann sie:er den Canvas an diesem Schritt verlassen.

### Zustellungsregeln {#delivery-rules}

Es kann einige Campaigns geben, wie z. B. transaktionale Nachrichten, die Sie immer an die:den Nutzer:in zustellen möchten, auch wenn sie:er bereits das Frequency-Cap erreicht hat. Beispielsweise möchte eine Liefer-App möglicherweise eine E-Mail oder einen Push senden, wenn ein Artikel zugestellt wurde, unabhängig davon, wie viele Campaigns die:der Nutzer:in bereits erhalten hat.

Wenn Sie möchten, dass eine bestimmte Campaign die Frequency-Capping-Regeln überschreibt, können Sie dies im Braze-Dashboard einrichten, indem Sie bei der Planung der Zustellung dieser Campaign **Frequency-Capping** auf **AUS** umschalten.

Danach werden Sie gefragt, ob diese Campaign trotzdem auf Ihr Frequency-Cap angerechnet werden soll. Nachrichten, die auf das Frequency-Capping angerechnet werden, sind in den Berechnungen für den Filter „Intelligenter Kanal“ enthalten.

Beim Senden von [API-Campaigns]({{site.baseurl}}/developer_guide/rest_api/messaging#messaging), die häufig transaktional sind, haben Sie die Möglichkeit anzugeben, dass eine Campaign die Frequency-Capping-Regeln ignorieren soll, indem Sie `override_frequency_capping` in der API-Anfrage auf `true` setzen.

Standardmäßig werden neue Campaigns und Canvases, die das Frequency-Capping nicht einhalten, auch nicht darauf angerechnet. Dies ist für jede Campaign und jeden Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie das Frequency-Capping für eine Campaign oder einen Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und wirken sich nicht auf Nachrichten aus, die derzeit aktiv sind.
{% endalert %}

![Bereich „Zustellungskontrollen“ mit aktiviertem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Wie Sendungen auf Caps angerechnet werden {#how-sends-count-toward-caps}

Frequency-Capping wird pro Versand angewendet: Jedes Mal, wenn Braze eine Campaign oder Canvas-Komponente an eine:n Nutzer:in sendet, wird dies auf Ihre Caps angerechnet – nicht jede Nachrichtenvariante oder Plattform innerhalb dieses Versands. Wenn Nutzer:innen beispielsweise auf fünf Push-Campaigns pro Woche begrenzt sind, erhalten sie nach dem fünften Versand keine weiteren Push-Campaigns, bis das Cap zurückgesetzt wird.

##### Multichannel-Sendungen {#multichannel-sends}

Wenn ein einzelner Versand mehrere Kanäle verwendet, wird dieser Versand höchstens einmal pro geltender Frequency-Capping-Regel gezählt. Wenn Sie beispielsweise eine Multichannel-Campaign erstellen, die E-Mail, iOS-Push und Android-Push in einer Zustellung sendet, und Ihr Workspace Regeln für Push und E-Mail sowie eine Regel für alle Kanäle hat, wird diese Zustellung einmal auf die Push-Regel, einmal auf die E-Mail-Regel und einmal auf die Alle-Kanäle-Regel angerechnet – sie wird nicht einmal pro Push-Plattform oder pro Nachricht innerhalb des Versands gezählt. Wenn Nutzer:innen auf eine Push- und eine E-Mail-Campaign pro Tag begrenzt sind und sie diese Multichannel-Campaign erhalten, sind sie für den Rest des Tages nicht für weitere Push- oder E-Mail-Campaigns berechtigt, es sei denn, eine Campaign ignoriert die Frequency-Capping-Regeln.

In-App-Nachrichten und Content Cards werden nicht als Caps für Campaigns oder Canvas-Komponenten jeglichen Typs gezählt oder darauf angerechnet.

##### Push-Benachrichtigungen mit mehreren Geräten {#push-notifications-with-multiple-devices}

Bei Push-Campaigns wird das Frequency-Capping auf Campaign- oder Canvas-Komponentenebene gezählt, nicht pro einzelnem Gerät. Wenn ein Nutzerprofil mehrere für Push registrierte Geräte hat (z. B. ein iPhone und ein iPad), zählt ein Frequency-Cap auf Campaign-Ebene dies als einen Versand, unabhängig davon, wie viele Geräte die Benachrichtigung erhalten. Dies ist vergleichbar damit, wie eine wiederkehrende Campaign mit täglicher Kadenz als ein Versand pro Tag zählt, auch wenn sie im Laufe der Woche mehrmals wiederholt wird.

{% alert important %}
Globales Frequency-Capping wird basierend auf der Zeitzone der:des Nutzer:in geplant und nach Kalendertagen berechnet, nicht nach 24-Stunden-Zeiträumen. Wenn Sie beispielsweise eine Frequency-Capping-Regel einrichten, die nicht mehr als eine Campaign pro Tag sendet, kann ein:e Nutzer:in um 23 Uhr in ihrer:seiner lokalen Zeitzone eine Nachricht erhalten und wäre eine Stunde später für eine weitere Nachricht berechtigt.
{% endalert %}

#### Anwendungsfälle {#use-cases}

{% tabs %}
{% tab Anwendungsfall 1 %}

Nehmen wir an, Sie richten eine Frequency-Capping-Regel ein, sodass Ihre Nutzer:innen nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte pro Woche von allen Campaigns oder Canvas-Schritten erhalten.

Wenn Ihre:Ihr Nutzer:in in dieser Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content-Card erhalten soll, wird sie:er alle diese Nachrichten erhalten.

{% endtab %}
{% tab Anwendungsfall 2 %}

Dieses Szenario verwendet eine Frequency-Capping-Regel, bei der Nutzer:innen nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte pro Woche von allen Campaigns oder Canvas-Schritten erhalten.

**Wenn das folgende Szenario eintritt:**

- Ein:e Nutzer:in triggert dieselbe Campaign `Campaign ABC` dreimal im Laufe einer Woche.
- Diese:r Nutzer:in triggert `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Frequency-Capping-Bereich mit der Regel, nicht mehr als 2 Push-Benachrichtigungs-Campaigns/Canvas-Schritte von allen Campaigns/Canvas-Schritten an eine:n Nutzer:in pro Woche zu senden.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann ist das erwartete Verhalten:**

- Diese:r Nutzer:in erhält die Campaign-Sendungen, die am Montag und Mittwoch getriggert wurden.
- Diese:r Nutzer:in erhält die dritte Campaign-Sendung am Donnerstag nicht, da die:der Nutzer:in in dieser Woche bereits zwei Push-Campaign-Sendungen erhalten hat.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag {#frequency-capping-by-tag}

[Frequency-Capping-Regeln](#delivery-rules) können auf Workspaces angewendet werden, indem bestimmte Tags verwendet werden, die Sie auf Ihre Campaigns und Canvases angewendet haben. So können Sie Ihr Frequency-Capping im Wesentlichen auf benutzerdefiniert benannte Gruppen basieren.

Beim Frequency-Capping nach Tag können Regeln auf Haupt- und verschachtelte Tags angewendet werden, sodass Braze alle Tags berücksichtigt. Wenn Sie beispielsweise den Haupt-Tag A als Frequency-Cap ausgewählt haben, beziehen wir auch Informationen aus allen verschachtelten Tags (z. B. Tags B und C) bei der Bestimmung des Limits ein.

Sie können auch reguläres Frequency-Capping mit Frequency-Capping nach Tags kombinieren. Betrachten Sie die folgenden Regeln:

1. Nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten. <br>**UND**
2. Nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit zwei Regeln, die begrenzen, wie viele Push-Benachrichtigungs-Campaigns/Canvases pro Woche an eine:n Nutzer:in gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Nutzer:innen nicht mehr als drei Campaign-Sendungen pro Woche über alle Campaigns und Canvas-Schritte hinweg und nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Canvases werden auf Canvas-Ebene getaggt, im Gegensatz zum Tagging nach Komponente. Daher erbt jede Canvas-Komponente alle Tags auf Canvas-Ebene.
{% endalert %}

#### Widersprüchliche Regeln {#conflicting-rules}

Wenn Regeln in Konflikt stehen, wird die restriktivste, anwendbare Frequency-Capping-Regel auf Ihre Nutzer:innen angewendet. Nehmen wir beispielsweise an, Sie haben die folgenden Regeln:

1. Nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente pro Woche von allen Campaigns und Canvas-Komponenten. <br>**UND**
2. Nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit widersprüchlichen Regeln, die begrenzen, wie viele Push-Benachrichtigungs-Campaigns/Canvas-Schritte pro Woche an eine:n Nutzer:in gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel erhält Ihre:Ihr Nutzer:in nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente mit dem Tag „promotional“ in einer bestimmten Woche, da Sie festgelegt haben, dass Nutzer:innen nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente von allen Campaigns und Canvas-Komponenten erhalten sollen. Mit anderen Worten: Die restriktivste anwendbare Frequency-Regel ist die Regel, die auf eine:n bestimmte:n Nutzer:in angewendet wird.

#### Tag-Zählung {#tag-count}

Frequency-Capping-nach-Tag-Regeln werden zum Zeitpunkt des Nachrichtenversands berechnet. Das bedeutet, dass Frequency-Capping nach Tag nur Tags zählt, die sich derzeit auf den Campaigns oder Canvases befinden, die ein:e Nutzer:in in der Vergangenheit erhalten hat. Es zählt nicht die Tags, die sich zum Zeitpunkt des Versands auf den Campaigns oder Canvases befanden, aber seitdem entfernt wurden. Es zählt, wenn ein Tag später zu einer Nachricht hinzugefügt wird, die ein:e Nutzer:in in der Vergangenheit erhalten hat, aber bevor die neueste getaggte Nachricht gesendet wird.

##### Anwendungsfall {#use-case}

Betrachten Sie die folgenden Campaigns und die Frequency-Capping-nach-Tag-Regel:

**Campaigns**:

- **Campaign A** ist eine Push-Campaign mit dem Tag `promotional`. Sie ist für den Versand am Montag um 9 Uhr geplant.
- **Campaign B** ist eine Push-Campaign mit dem Tag `promotional`. Sie ist für den Versand am Mittwoch um 9 Uhr geplant.

**Frequency-Capping-nach-Tag-Regel:**

- Ihre:Ihr Nutzer:in sollte nicht mehr als eine Push-Benachrichtigungs-Campaign pro Woche mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Der Tag `promotional` wird von **Campaign A** entfernt, nachdem Ihre:Ihr Nutzer:in die Nachricht erhalten hat, aber bevor **Campaign B gesendet wurde.** | Ihre:Ihr Nutzer:in erhält **Campaign B**. |
| Der Tag `promotional` wird versehentlich von **Campaign A** entfernt, nachdem Ihre:Ihr Nutzer:in die Nachricht erhalten hat. <br> Der Tag wird am Dienstag wieder zu **Campaign A** hinzugefügt, bevor **Campaign B** gesendet wird. | Ihre:Ihr Nutzer:in erhält **Campaign B** nicht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfall" }

#### Versand in großem Umfang {#sending-at-large-scales}

Frequency-Capping-nach-Tag-Regeln werden bei großem Umfang möglicherweise nicht korrekt angewendet, z. B. bei 100 Nachrichten pro Kanal von Campaigns oder Canvas-Komponenten.

Wenn Ihre Frequency-Capping-nach-Tag-Regel beispielsweise lautet:

> Nicht mehr als zwei E-Mail-Campaigns oder Canvas-Komponenten mit dem Tag `Promotional` an eine:n Nutzer:in pro Woche.

Und Sie der:dem Nutzer:in im Laufe einer Woche mehr als 100 E-Mails von Campaigns und Canvas-Schritten mit aktiviertem Frequency-Capping senden, werden möglicherweise mehr als zwei E-Mails an die:den Nutzer:in gesendet.

Da 100 Nachrichten pro Kanal mehr sind, als die meisten Marken an ihre Nutzer:innen senden, ist es unwahrscheinlich, dass Sie von dieser Einschränkung betroffen sind. Um diese Einschränkung zu vermeiden, können Sie ein Cap für die maximale Anzahl von E-Mails festlegen, die Ihre Nutzer:innen im Laufe einer Woche erhalten sollen.

Beispielsweise könnten Sie die folgende Regel einrichten:

> Nicht mehr als drei E-Mail-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten.

Diese Regel stellt sicher, dass keine:r Ihrer Nutzer:innen mehr als 100 E-Mails pro Woche erhält, da Nutzer:innen höchstens drei E-Mails pro Woche von Campaigns oder Canvas-Komponenten mit aktiviertem Frequency-Capping erhalten.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wenn ich eine Sendedrosselung in einem aktiven Canvas ändere, wirkt sich das auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Ja. Wenn Sie ein Canvas-Rate-Limit erhöhen oder verringern, gilt das aktualisierte Limit für neue Nachrichten innerhalb von etwa 30 Sekunden nach der Änderung aufgrund von Caching.

### Führt Frequency-Capping dazu, dass Nutzer:innen ein Canvas verlassen? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Nein. Wenn ein:e Canvas-Nutzer:in aufgrund globaler Frequency-Capping-Einstellungen begrenzt wird, wird die:der Nutzer:in sofort zum nächsten Canvas-Schritt weitergeleitet. Die:der Nutzer:in verlässt das Canvas **nicht** aufgrund des Frequency-Cappings.

### Wie kann ich Nutzer:innen identifizieren, die in einem Canvas durch Frequency-Capping begrenzt wurden? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Nutzer:innen, die durch Frequency-Capping begrenzt werden, erzeugen kein Sendeereignis für diesen Schritt. Um diese Nutzer:innen zu identifizieren, können Sie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) verwenden, um Ereignisse für durch Frequency-Capping begrenzte Nachrichten zu verfolgen. Alternativ können Sie eine [Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension) erstellen, um Nutzer:innen zu analysieren, die das Canvas betreten haben, aber die erwartete Nachricht nicht erhalten haben.

### Warum zeigt das Dashboard einen Rate-Limit-Fehler für meine Kampagne an? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Das bedeutet in der Regel, dass das [Rate-Limit für die Zustellgeschwindigkeit](#delivery-speed-rate-limiting) der Kampagne für die Zielgruppengröße zu niedrig eingestellt ist, sodass der Versand länger dauern würde als das zulässige Zeitfenster und Braze eine Warnung anzeigt. Erhöhen Sie das Rate-Limit für die Zustellgeschwindigkeit, reduzieren Sie die Zielgruppe oder verwenden Sie **Sendevolumen begrenzen**, damit jeder geplante Versand innerhalb des zulässigen Sendefensters abgeschlossen wird. Sie können auch ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) festlegen, um ein Limit über Campaigns hinweg durchzusetzen.

**Sendevolumen begrenzen** steuert, wie viele Nutzer:innen für einen Versand berechtigt sind, nicht wie viele Nachrichten Braze pro Minute sendet. Nur ein Rate-Limit für die Zustellgeschwindigkeit legt den Durchsatz pro Minute fest.

### Was bedeutet „Gesendet“ für Frequency-Capping? {#what-does-sent-mean-for-frequency-capping}

In Analytics und beim Frequency-Capping bezieht sich _Gesendet_ auf den Zeitpunkt, an dem Braze die Nachricht versendet (der Versand wird erfasst), nicht auf die garantierte endgültige Zustellung an das Gerät oder den Posteingang. Frequency-Capping und Sendezähler verwenden diese erfassten Sendeereignisse, die von nachgelagerten „zugestellt“-Metriken abweichen können.

### Warum sehe ich E-Mail-Bounces oder -Zurückstellungen? {#why-am-i-seeing-email-bounces-or-deferrals}

E-Mail-Bounce- und Zurückstellungsnachrichten verwenden viele verschiedene Codes und anbieterspezifische Texte. Behandeln Sie einen bestimmten Code nicht als Anzeichen für ein Rate-Limiting-Problem, da die Ursache von Ihrem Sendekontext und dem Feedback des Postfachanbieters abhängt.

Wenn Nachrichten vorübergehend zurückgestellt werden, kann es kurzfristig helfen, weniger zu senden. Verwenden Sie ein [Rate-Limit für die Zustellgeschwindigkeit](#delivery-speed-rate-limiting), **Sendevolumen begrenzen** oder beides.

Arbeiten Sie für eine langfristige Lösung mit einem Zustellbarkeitsexperten zusammen, um Ihre Bounce- und Zurückstellungsdaten zu überprüfen.