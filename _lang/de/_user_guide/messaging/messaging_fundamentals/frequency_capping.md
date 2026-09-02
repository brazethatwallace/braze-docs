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

Braze ermöglicht es Ihnen, den Marketingdruck zu steuern, indem Sie Ihre Campaigns mit Rate-Limiting versehen und den Umfang des ausgehenden Traffics Ihrer Plattform regulieren. Sie können zwei verschiedene Arten von Rate-Limiting für Ihre Campaigns implementieren:

1. [Nutzer:innenzentriertes Rate-Limiting:](#user-centric-rate-limiting) Konzentriert sich auf die bestmögliche Erfahrung für Nutzer:innen.
2. [Zustellgeschwindigkeits-Rate-Limiting:](#delivery-speed-rate-limiting) Berücksichtigt die Ressourcen Ihrer Server.

Braze unterstützt kein Rate-Limit auf Sekundenbasis. Braze versucht, den Nachrichtenversand gleichmäßig über die Minute zu verteilen, kann dies jedoch nicht garantieren. Wenn Sie beispielsweise eine Campaign mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), es kann jedoch zu Abweichungen bei der Rate pro Sekunde kommen.

### Nutzer:innenzentriertes Rate-Limiting {#user-centric-rate-limiting}

Wenn Sie mehr Segments erstellen, wird es Fälle geben, in denen sich die Mitgliedschaften dieser Segments überschneiden. Wenn Sie Campaigns an diese Segments senden, möchten Sie sicherstellen, dass Sie Ihren Nutzer:innen nicht zu häufig Nachrichten senden. Wenn Nutzer:innen innerhalb eines kurzen Zeitraums zu viele Nachrichten erhalten, fühlen sie sich überlastet und deaktivieren entweder Push-Benachrichtigungen oder deinstallieren Ihre App.

#### Relevante Segment-Filter {#relevant-segment-filters}

Braze stellt die folgenden Filter bereit, um Ihnen zu helfen, die Häufigkeit zu begrenzen, mit der Ihre Nutzer:innen Nachrichten erhalten:

- Zuletzt mit Nachricht interagiert
- Zuletzt eine Nachricht erhalten
- Zuletzt Push erhalten
- Zuletzt E-Mail erhalten
- Zuletzt Kurzmitteilungsdienst or SMS erhalten

#### Filter implementieren {#implementing-filters}

Angenommen, wir haben ein Segment mit dem Namen „Retargeting Filter Showcase“ mit dem Filter „App zuletzt vor mehr als 7 Tagen verwendet“ erstellt, um Nutzer:innen anzusprechen. Dies wäre ein Standard-Segment für die erneute Interaktion.

Wenn Sie andere, gezieltere Segments haben, die kürzlich Benachrichtigungen erhalten haben, möchten Sie möglicherweise nicht, dass Ihre Nutzer:innen zusätzlich von allgemeineren Campaigns dieses Segments angesprochen werden. Indem Sie den Filter „Zuletzt Push erhalten“ zu diesem Segment hinzufügen, haben Sie sichergestellt, dass Nutzer:innen, die in den letzten 24 Stunden eine weitere Benachrichtigung erhalten haben, für die nächsten 24 Stunden aus diesem Segment herausfallen. Wenn sie 24 Stunden später immer noch die anderen Kriterien des Segments erfüllen und keine weiteren Benachrichtigungen erhalten haben, werden sie wieder in das Segment aufgenommen.

![Ein Segment mit dem Namen „Retargeting Filter Showcase“ mit der Filtergruppe „App zuletzt vor mehr als 7 Tagen verwendet“.]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Wenn Sie diesen Filter zu allen Segments hinzufügen, die von Campaigns angesprochen werden, erhalten Ihre Nutzer:innen maximal einen Push alle 24 Stunden. Sie könnten dann Ihr Messaging priorisieren, indem Sie sicherstellen, dass Ihre wichtigsten Nachrichten vor weniger wichtigen Nachrichten zugestellt werden.

#### Eine maximale Nutzer:innen-Obergrenze festlegen {#setting-a-maximum-user-cap}

Im Schritt **Target Audiences** Ihres Campaign-Composers können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten werden. Dies dient als eine Kontrolle, die unabhängig von Ihren Campaign-Filtern ist.

![Zielgruppenzusammenfassung mit einem aktivierten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Campaign erhalten.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Durch das Festlegen einer maximalen Nutzer:innen-Obergrenze können Sie das Volumen der gesendeten Nachrichten auf Kanalbasis oder global über alle Nachrichtentypen hinweg begrenzen. Braze versendet keine Nachrichten an Nutzer:innen, die Kontrollgruppen zugewiesen sind, daher zählen diese nicht zur Obergrenze.

{% alert note %}
Die maximale Nutzer:innen-Obergrenze begrenzt die Anzahl der versendeten Nutzer:innen, nicht die Anzahl der erfolgreich zugestellten Nachrichten. Da abgebrochene Nachrichten auf diese Obergrenze angerechnet werden, kann die tatsächliche Anzahl gesendeter Nachrichten niedriger sein als das konfigurierte Limit. Wenn Sie beispielsweise eine Obergrenze von 10.000 festlegen und 2.000 Nachrichten aufgrund von Liquid-Logik oder anderen Bedingungen abgebrochen werden, werden nur 8.000 Nachrichten gesendet.
{% endalert %}

##### Maximale Nutzer:innen-Obergrenze für Multichannel-Kampagnen {#maximum-user-cap-for-multichannel-campaigns}

Für Multichannel-Kampagnen wählt Braze zunächst eine Zielgruppe bis zu Ihrer konfigurierten maximalen Nutzer:innen-Obergrenze aus. Braze bewertet dann jede:n Nutzer:in in dieser begrenzten Zielgruppe für jeden Kanal in der Campaign.

Dadurch bleibt die Größe der begrenzten Zielgruppe gleich, aber die Versendungen pro Kanal können je nach Kanalberechtigung variieren. Wenn Sie beispielsweise eine maximale Nutzer:innen-Obergrenze von 500.000 festlegen und ein:e Nutzer:in nur für Push und Content Cards berechtigt ist, erhält diese:r Nutzer:in diese Kanäle, aber keine E-Mail.

Wenn Sie diese Kanäle in separate Campaigns aufteilen, die jeweils dasselbe Segment ansprechen und jeweils eine eigene maximale Nutzer:innen-Obergrenze haben, bewertet und begrenzt jede Campaign Nutzer:innen unabhängig. Braze garantiert nicht, dass jede Campaign exakt dieselbe Teilmenge von Nutzer:innen auswählt.

Wenn Sie Folge-Campaigns benötigen, die Nutzer:innen ansprechen, denen eine frühere Campaign gesendet wurde, erstellen Sie ein Segment mit dem Filter **Received Campaign** und verwenden Sie dieses Segment dann für die Folge-Campaigns.

##### Maximale Nutzer:innen-Obergrenze mit Optimierungen {#maximum-user-cap-with-optimizations}

Für eine Einzelversand-Campaign mit **Optimize with BrazeAI<sup>TM</sup>** besteht die Campaign aus zwei Versendungen: dem anfänglichen Experiment und dem optimierten Versand.

Um in diesem Szenario eine maximale Nutzer:innen-Obergrenze einzurichten, wählen Sie **Limit send volume**, dann **Lifetime of the campaign** und geben Sie einen Wert für **Maximum sends** ein. Ihre Zielgruppenbegrenzung wird nach den im **A/B-Tests**-Panel angezeigten Prozentsätzen aufgeteilt.

Wenn Sie **Every time campaign is scheduled** auswählen, werden diese beiden Phasen separat auf die festgelegte Zahl begrenzt. Dies ist in der Regel nicht erwünscht.

#### Eine maximale Impressionen-Obergrenze für Campaigns festlegen {#setting-a-maximum-impression-cap-on-campaigns}

Für In-App-Nachrichten können Sie den Marketingdruck steuern, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Nutzerbasis angezeigt werden. Danach sendet Braze Ihren Nutzer:innen keine weiteren Nachrichten mehr. Es ist jedoch wichtig zu beachten, dass diese Obergrenze nicht exakt ist.

In-App-Nachrichtenregeln werden beim Sitzungsstart an eine App gesendet, was bedeutet, dass Braze eine Nachricht an Nutzer:innen senden kann, bevor die Obergrenze erreicht ist. Wenn Nutzer:innen die Nachricht dann jedoch auslösen, wurde die Obergrenze bereits erreicht. In dieser Situation zeigt das Gerät die Nachricht trotzdem an.

Angenommen, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn Nutzer:innen ein Level abschließen, und Sie begrenzen sie auf 100 Impressionen. Es gab bisher 99 Impressionen. Alice und Bob öffnen beide das Spiel, und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu erhalten, wenn sie ein Level abschließen. Alice schließt zuerst ein Level ab und erhält die Nachricht. Bob schließt als Nächstes das Level ab, aber da sein Gerät seit dem Sitzungsstart nicht mit den Braze-Servern kommuniziert hat, ist seinem Gerät nicht bekannt, dass die Nachricht ihre Obergrenze erreicht hat, und er erhält die Nachricht ebenfalls. Wenn eine Impressionen-Obergrenze jedoch erreicht wurde, wird das System beim nächsten Mal, wenn ein Gerät die Liste der berechtigten In-App-Nachrichten anfordert, diese Nachricht nicht senden und sie vom Gerät entfernen.

### Rate-Limiting und A/B-Tests {#rate-limiting-and-ab-testing}

Bei der Verwendung von Rate-Limiting mit einem A/B-Test wird das Rate-Limit nicht in derselben Weise auf die Kontrollgruppe angewendet wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen darstellt. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Konversionsfenster.

### Zustellgeschwindigkeits-Rate-Limiting {#delivery-speed-rate-limiting}

Wenn Sie davon ausgehen, dass große Campaigns einen Anstieg der Nutzer:innenaktivität verursachen und Ihre Server überlasten, können Sie ein Rate-Limit pro Minute für den Nachrichtenversand festlegen. Das bedeutet, Braze sendet innerhalb einer Minute nicht mehr als Ihre festgelegte Rate-Limit-Einstellung.

Bei der Zielgruppenauswahl während der Campaign-Erstellung können Sie zu **Target Audiences** (für Campaigns) oder **Send Settings** (für Canvas) navigieren, um ein Rate-Limit auszuwählen (in verschiedenen Abstufungen von nur 10 bis zu 500.000 Nachrichten pro Minute).

Beachten Sie, dass Campaigns ohne Rate-Limiting diese Zustellungslimits überschreiten können. Seien Sie sich jedoch bewusst, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger verzögert werden. Wenn das Rate-Limit zu niedrig ist, erhält der:die Ersteller:in der Campaign Warnungen im Dashboard und per E-Mail.

{% alert tip %}
Legen Sie ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) fest, um ein Rate-Limit über einen gesamten Workspace hinweg durchzusetzen.
{% endalert %}

#### Beispiel {#example}

Wenn Sie versuchen, 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute zu versenden, wird die Zustellung über acht Minuten verteilt. Ihre Campaign liefert in jeder der ersten sieben Minuten nicht mehr als 10.000 Nachrichten und 5.000 in der letzten Minute.

#### Anzahl der Versendungen {#number-of-sends}

Beachten Sie, dass mit Rate-Limit versendete Nachrichten möglicherweise nicht gleichmäßig über den Verlauf jeder Minute verteilt werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Dies könnte bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten in der ersten Hälfte der Minute gesendet wird als in der zweiten Hälfte.

Das Rate-Limit wird zu Beginn des Nachrichtenversandversuchs angewendet. Bei Schwankungen in der Zeit, die der Versand benötigt, kann die Anzahl der abgeschlossenen Versendungen das Rate-Limit für einige Minuten leicht überschreiten. Über die Zeit wird sich die Anzahl der Versendungen pro Minute auf nicht mehr als das Rate-Limit einpendeln.

{% alert important %}
Seien Sie vorsichtig, zeitkritische Nachrichten mit dieser Form des Rate-Limitings in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment zu verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen enthält, wir aber das Rate-Limit auf 10.000 pro Minute festlegen, wird ein großer Teil Ihrer Nutzerbasis die Nachricht erst am folgenden Tag erhalten.
{% endalert %}

#### Multichannel-Kampagnen und Canvase {#multichannel-campaigns-and-canvases}

Beim Festlegen eines Zustellgeschwindigkeits-Rate-Limits für eine Multichannel-Kampagne oder ein Canvas können Sie wählen, ob Sie ein gemeinsames Rate-Limit oder ein kanalbasiertes Limit festlegen.

Wenn eine Multichannel-Kampagne oder ein Canvas ein gemeinsames Rate-Limit verwendet, bedeutet dies, dass die Gesamtzahl der pro Minute von der Campaign oder dem Canvas gesendeten Nachrichten das Rate-Limit nicht überschreitet. Wenn Ihr Canvas beispielsweise ein Rate-Limit von 500.000 pro Minute hat und E-Mail- sowie Kurzmitteilungsdienst or SMS-Nachrichtenschritte enthält, sendet Braze insgesamt 500.000 Nachrichten pro Minute über E-Mail und Kurzmitteilungsdienst or SMS hinweg.

![Die Option zur Begrenzung der Versandrate der Campaign, ausgewählt mit 500.000 Nachrichten pro Minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Wenn eine Multichannel-Kampagne oder ein Canvas kanalbasiertes Rate-Limiting verwendet, wird das Rate-Limit auf jeden Ihrer ausgewählten Kanäle angewendet. Sie können beispielsweise Ihre Campaign oder Ihr Canvas so einstellen, dass maximal 5.000 Webhooks und 2.500 Kurzmitteilungsdienst or SMS-Nachrichten pro Minute über die Campaign oder das Canvas gesendet werden.

![Separate Rate-Limits für zwei Kanäle, Webhook und Kurzmitteilungsdienst or SMS/MMS/RCS, mit 5.000 bzw. 2.500 Nachrichten pro Minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Push-Benachrichtigungen {#push-notifications}

Für Campaigns oder Canvase mit Push-Plattformen (wie Android, iOS, Web-Push oder Kindle) können Sie **Push notifications** auswählen, um ein Rate-Limit durchzusetzen, das zwischen allen Push-Plattformen in Ihrer Campaign oder Ihrem Canvas geteilt wird.

![Das Kanal-Dropdown mit Optionen für Push-Plattformen und Push-Benachrichtigungen.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Wenn Sie ein Limit für Push-Benachrichtigungen auswählen, können Sie keine individuellen Push-Kanal-Rate-Limits festlegen. Ebenso können Sie, wenn Sie Limits für einzelne Push-Kanäle auswählen, keine gemeinsamen Push-Benachrichtigungslimits festlegen.

{% alert important %}
**Aktualisierungen der Rate-Limiting-Oberfläche**<br>
Braze hat die Rate-Limiting-Oberfläche aktualisiert, um mehr Transparenz und Kontrolle darüber zu bieten, wie Rate-Limits auf Multichannel-Kampagnen und Canvase angewendet werden.<br><br>

- **Bestehende Campaigns und Canvase:** Alle bestehenden Campaigns und Canvase wurden auf diese Oberfläche migriert. Ihr Zustellverhalten bleibt gleich. Das Dashboard zeigt an, ob die Campaign gemeinsame oder kanalbasierte Logik verwendet.<br>
- **Neue Campaigns und Canvase:** Für alle neuen Campaigns und Canvase gibt es einen manuellen Umschalter, um Ihre bevorzugte Rate-Limit-Logik auszuwählen. Stellen Sie sicher, dass Sie das Rate-Limiting-Verhalten auswählen, das mit Ihrem beabsichtigten Verhalten übereinstimmt, wenn Sie ein Rate-Limit für eine Campaign oder ein Canvas festlegen oder Update or aktualisieren or aktualisieren.
{% endalert %}

##### Überlegungen zum Rate-Limiting {#rate-limiting-considerations}

Einige Hinweise, die Sie bei der Konfiguration von Rate-Limits beachten sollten, und welches Verhalten Sie erwarten können:

- Kurzmitteilungsdienst or SMS-Versendungen unterliegen einem Rate-Limit von 50.000 pro Abo-Gruppe. Einige Kurzmitteilungsdienst or SMS-Anbieter können weitere Limits durchsetzen.
- Die folgenden Nachrichten werden nicht durch das Rate-Limit gedrosselt oder darauf angerechnet:
    - Testversendungen
    - Seed-Gruppen
    - Content Cards, die so konfiguriert sind, dass sie „bei erster Impression“ erstellt werden (dies wird durch die Rate der App-Impressionen gesteuert. Weitere Informationen zu den Unterschieden zwischen den Optionen zur Card-Erstellung finden Sie unter [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences).)
- Zustellgeschwindigkeits-Rate-Limits werden für Folgendes nicht unterstützt:
    - Kurzmitteilungsdienst or SMS-Autoantworten
    - SLA-gesicherte Nachrichten (wie [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - In-App-Nachrichten
    - Feature-Flags
    - Banner

#### Rate-Limiting und Connected-Content-Wiederholungen {#rate-limiting-and-connected-content-retries}

Wenn die [Connected-Content-Wiederholung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) aktiviert ist, wiederholt Braze fehlgeschlagene Aufrufe unter Einhaltung des von Ihnen für jede erneute Versendung festgelegten Rate-Limits. Betrachten wir das Szenario, 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute zu versenden. Stellen Sie sich vor, dass der Aufruf in der ersten Minute fehlschlägt oder langsam ist und nur 4.000 Nachrichten sendet.

Anstatt zu versuchen, die Verzögerung auszugleichen und die verbleibenden 6.000 Nachrichten in der zweiten Minute zu senden oder sie zu den 10.000 hinzuzufügen, die bereits für den Versand vorgesehen sind, verschiebt Braze diese 6.000 Nachrichten an das „Ende der Warteschlange“ und fügt bei Bedarf eine Minute zur Gesamtzahl der Minuten hinzu, die für den Versand Ihrer Nachricht benötigt werden.

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

Connected-Content-Anfragen werden nicht unabhängig mit einem Rate-Limit versehen und folgen dem Webhook-Rate-Limit. Das bedeutet, wenn es einen Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook gibt, würden Sie 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufe pro Minute erwarten. Beachten Sie, dass Caching dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Außerdem können Wiederholungen die Connected-Content-Aufrufe erhöhen, daher empfehlen wir zu überprüfen, dass der Connected-Content-Endpunkt gewisse Schwankungen verarbeiten kann.

{% alert note %}
**Rate-Limits sind Geschwindigkeitsbegrenzungen und definieren keine exakte Versandgeschwindigkeit.** Im Allgemeinen werden Nachrichten innerhalb einer bestimmten Minute gleichmäßig verteilt, und in der überwiegenden Mehrheit der Fälle werden sie beim oder sehr nahe am konfigurierten Limit gesendet. Dies ist nicht immer der Fall – beispielsweise wenn Nachrichten sehr groß sind (wie E-Mails mit vielen Content Blocks, Connected-Content-Tags oder Catalog-Artikel-Tags) oder wenn es viele Liquid-Abbrüche gibt (abgebrochene Nachrichten belegen trotzdem einen Platz und können die effektive Versandrate reduzieren).<br><br>
In der Praxis kann die anhaltende Versandrate (abgeschlossene Nachrichten pro Minute) aufgrund von Wiederholungen, Netzwerkvariabilität, Latenz nachgelagerter Endpunkte und Pro-Minuten-Glättung niedriger sein als das konfigurierte Rate-Limit. Wenn Sie durchgehend einen deutlich niedrigeren Durchsatz als erwartet feststellen, überprüfen Sie die Connected-Content-Antwortzeiten, Fehlerraten (wie `429`) und das Wiederholungsverhalten.
{% endalert %}

## Frequency-Capping im Detail {#about-frequency-capping}

Wenn Ihre Nutzerbasis weiter wächst und Ihr Messaging auf Lifecycle-, getriggerte, transaktionale und Konversions-Campaigns ausgeweitet wird, ist es wichtig zu verhindern, dass Ihre Benachrichtigungen als „Spam“ oder störend wahrgenommen werden. Durch eine bessere Kontrolle über das Erlebnis Ihrer Nutzer:innen können Sie mit Frequency-Capping die gewünschten Campaigns erstellen, ohne Ihre Zielgruppe zu überfordern.

### Rate-Limiting und Frequency-Capping gemeinsam verwenden {#use-rate-limiting-and-frequency-capping-together}

Wenn Sie sowohl Rate-Limiting als auch Frequency-Capping für eine Campaign aktivieren, wendet Braze diese in der folgenden Reihenfolge an:

1. **Rate-Limit** wird zuerst angewendet, um den anfänglichen Pool von Nutzer:innen auszuwählen, die Nachrichten empfangen können.
2. **Frequency-Cap** wird anschließend angewendet, um Nutzer:innen aus diesem Pool herauszufiltern.
3. **Nachrichten werden gesendet** an die verbleibenden Nutzer:innen.

{% alert important %}
Wenn viele Nutzer:innen in Ihrem Rate-Limited-Pool durch Frequency-Capping betroffen sind, kann es sein, dass weniger Nachrichten gesendet werden als Ihr Rate-Limit-Wert vorsieht. Braze füllt keine zusätzlichen Nutzer:innen aus dem Rate-Limit nach, sobald Frequency-Capping Nutzer:innen aus dem Sendepool entfernt hat.
{% endalert %}

#### Beispiel

Bei einem Rate-Limit von 500 Nutzer:innen und aktiviertem Frequency-Capping werden nur 300 Nachrichten gesendet – nicht 500 –, wenn 200 dieser 500 Rate-Limited-Nutzer:innen durch Frequency-Capping betroffen sind.

#### Empfehlungen {#recommendations}

Wenn Sie bei gleichzeitiger Nutzung beider Features eine bestimmte Anzahl von Nutzer:innen erreichen müssen, sollten Sie folgende Ansätze in Betracht ziehen:

- **Erhöhen Sie Ihr Rate-Limit:** Um Nutzer:innen zu berücksichtigen, die vom Frequency-Capping betroffen sind. Wenn Sie beispielsweise 500 Nutzer:innen erreichen möchten, aber erwarten, dass einige durch Frequency-Capping herausgefiltert werden, setzen Sie Ihr Rate-Limit höher an (z. B. 1.000 Nutzer:innen).
- **Verwenden Sie nur Rate-Limiting:** Wenn Ihr Ziel die Kontrolle des Nachrichtenvolumens pro Campaign ist.
- **Wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in:** Für Unterstützung bei der Entwicklung einer robusten Messaging-Strategie, die sowohl geschäftliche Anforderungen als auch technische Aspekte berücksichtigt.

### Feature-Übersicht {#freq-cap-feat-over}

Frequency-Capping wird auf der Sende-Ebene der Campaign oder Canvas-Komponente angewendet und kann für jeden Workspace unter **Einstellungen** > **Frequency-Capping-Regeln** konfiguriert werden.

Standardmäßig ist Frequency-Capping aktiviert, wenn neue Campaigns erstellt werden. Von hier aus können Sie Folgendes festlegen:

- Den Messaging-Kanal, den Sie begrenzen möchten: Push, E-Mail, Kurzmitteilungsdienst or SMS, Webhook, WhatsApp, LINE oder beliebige Kombinationen dieser Kanäle.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente erhalten soll, die über einen Kanal innerhalb eines bestimmten Zeitraums gesendet wird.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente erhalten soll, die nach [Tag](#frequency-capping-by-tag) innerhalb eines bestimmten Zeitraums gesendet wird.

Dieser Zeitraum kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, mit einer maximalen Dauer von 30 Tagen.

Jede Zeile der Frequency-Caps wird mit dem Operator `AND` verknüpft, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Sie können mehrere Begrenzungen für dieselben Nachrichtentypen einbeziehen. Zum Beispiel können Sie Nutzer:innen auf maximal einen Push pro Tag und maximal drei Pushes pro Woche begrenzen. Beachten Sie, dass abgebrochene Nachrichten nicht zum Frequency-Capping zählen.

![Frequency-Capping-Bereich mit Listen von Campaigns und Canvase, auf die Regeln angewendet werden und nicht angewendet werden.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Verhalten, wenn Nutzer:innen ihr Frequency-Cap erreicht haben oder eine Nachricht in einem Canvas-Schritt abgebrochen wird {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

Globales Frequency-Capping allein bewirkt nicht, dass Nutzer:innen ein Canvas verlassen. Bei [Nachrichtenschritten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) werden Nutzer:innen weiterhin vorangebracht, wenn eine Nachricht aufgrund des globalen Frequency-Cappings nicht gesendet wird – gemäß dem Prinzip, [wie Nutzer:innen vorankommen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Dasselbe gilt, wenn eine Nachricht abgebrochen wird (z. B. durch eine Liquid-Abbruchbedingung): Die:der Nutzer:in durchläuft das Canvas weiter, als ob die Nachricht gesendet worden wäre.

Dies ist getrennt von den **Zustellvalidierungen** eines Nachrichtenschritts. Wenn ein:e Nutzer:in Ihre Zustellvalidierungskriterien zum Sendezeitpunkt nicht erfüllt, kann er:sie das Canvas an diesem Schritt verlassen.

### Zustellregeln {#delivery-rules}

Es kann Campaigns geben, wie z. B. Transaktionsnachrichten, die Sie immer an Nutzer:innen zustellen möchten, auch wenn diese ihr Frequency-Cap bereits erreicht haben. Beispielsweise möchte eine Liefer-App möglicherweise eine E-Mail oder einen Push senden, wenn ein Artikel zugestellt wurde – unabhängig davon, wie viele Campaigns die:der Nutzer:in bereits erhalten hat.

Wenn Sie möchten, dass eine bestimmte Campaign die Frequency-Capping-Regeln umgeht, können Sie dies im Braze-Dashboard einrichten, indem Sie bei der Planung der Campaign-Zustellung **Frequency-Capping** auf **AUS** umschalten.

Danach werden Sie gefragt, ob diese Campaign trotzdem auf Ihr Frequency-Cap angerechnet werden soll. Nachrichten, die auf das Frequency-Capping angerechnet werden, fließen in die Berechnungen für den Filter „Intelligenter Kanal“ ein.

Beim Senden von [API-Campaigns]({{site.baseurl}}/api/endpoints/messaging), die häufig transaktional sind, haben Sie die Möglichkeit, festzulegen, dass eine Campaign die Frequency-Capping-Regeln ignorieren soll, indem Sie `override_frequency_capping` in der API-Anfrage auf `true` setzen.

Standardmäßig werden neue Campaigns und Canvase, die das Frequency-Capping nicht beachten, auch nicht darauf angerechnet. Dies ist für jede Campaign und jedes Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie Frequency-Capping für eine Campaign oder ein Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und haben keine Auswirkungen auf Nachrichten, die derzeit aktiv sind.
{% endalert %}

![Bereich „Zustellsteuerung“ mit aktiviertem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Wie Sendungen auf Caps angerechnet werden {#how-sends-count-toward-caps}

Frequency-Capping gilt pro Versand: Jedes Mal, wenn Braze eine Campaign oder Canvas-Komponente an eine:n Nutzer:in sendet, wird dies auf Ihre Caps angerechnet – nicht jede Nachrichtenvariante oder Plattform innerhalb dieses Versands. Wenn Nutzer:innen beispielsweise auf fünf Push-Campaigns pro Woche begrenzt sind, erhalten sie nach dem fünften Versand keine weiteren Push-Campaigns, bis das Cap zurückgesetzt wird.

##### Multichannel-Sendungen {#multichannel-sends}

Wenn ein einzelner Versand mehrere Kanäle nutzt, wird dieser Versand höchstens einmal pro anwendbarer Frequency-Capping-Regel gezählt. Wenn Sie beispielsweise eine Multichannel-Kampagne erstellen, die E-Mail, iOS-Push und Android-Push in einer Zustellung sendet, und Ihr Workspace Regeln für Push, E-Mail und eine Regel für alle Kanäle hat, zählt diese Zustellung einmal für die Push-Regel, einmal für die E-Mail-Regel und einmal für die Alle-Kanäle-Regel – sie zählt nicht einmal pro Push-Plattform oder pro Nachricht innerhalb des Versands. Wenn Nutzer:innen auf einen Push und eine E-Mail-Campaign pro Tag begrenzt sind und sie diese Multichannel-Kampagne erhalten, sind sie für den Representational State Transfer des Tages nicht für weitere Push- oder E-Mail-Campaigns berechtigt, es sei denn, eine Campaign ignoriert die Frequency-Capping-Regeln.

In-App-Nachrichten und Content Cards werden nicht als Caps auf Campaigns oder Canvas-Komponenten irgendeines Typs gezählt und zählen auch nicht dazu.

##### Push-Benachrichtigungen mit mehreren Geräten {#push-notifications-with-multiple-devices}

Für Push-Campaigns zählt Frequency-Capping auf der Campaign- oder Canvas-Komponenten-Ebene, nicht pro einzelnem Gerät. Wenn ein Kundenprofil or Nutzerprofil mehrere für Push registrierte Geräte hat (z. B. ein iPhone und ein iPad), zählt ein Campaign-Level-Frequency-Cap dies als einen Versand, unabhängig davon, wie viele Geräte die Benachrichtigung erhalten. Dies ähnelt dem Verhalten einer wiederkehrenden Campaign mit täglicher Kadenz, die als ein Versand pro Tag gezählt wird, auch wenn sie mehrmals während der Woche wiederholt wird.

{% alert important %}
Globales Frequency-Capping basiert auf der Zeitzone der:des Nutzer:in und wird nach Kalendertagen berechnet, nicht nach 24-Stunden-Zeiträumen. Wenn Sie beispielsweise eine Frequency-Capping-Regel einrichten, die den Versand auf maximal eine Campaign pro Tag begrenzt, könnte ein:e Nutzer:in um 23 Uhr in der eigenen Ortszeit eine Nachricht erhalten und wäre eine Stunde später bereits für eine weitere Nachricht berechtigt.
{% endalert %}

#### Anwendungsfälle {#use-cases}

{% tabs %}
{% tab Anwendungsfall 1 %}

Nehmen wir an, Sie richten eine Frequency-Capping-Regel ein, sodass Ihre Nutzer:innen maximal drei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte pro Woche von allen Campaigns oder Canvas-Schritten erhalten.

Wenn Ihre:Ihr Nutzer:in in dieser Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content-Card erhalten soll, werden alle diese Nachrichten zugestellt.

{% endtab %}
{% tab Anwendungsfall 2 %}

Dieses Szenario verwendet eine Frequency-Capping-Regel, damit Nutzer:innen maximal zwei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte pro Woche von allen Campaigns oder Canvas-Schritten erhalten.

**Wenn das folgende Szenario eintritt:**

- Ein:e Nutzer:in triggert dieselbe Campaign `Campaign ABC` dreimal im Laufe einer Woche.
- Diese:r Nutzer:in triggert `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Frequency-Capping-Bereich mit der Regel, maximal 2 Push-Benachrichtigungs-Campaigns/Canvas-Schritte von allen Campaigns/Canvas-Schritten pro Woche an eine:n Nutzer:in zu senden.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann ist das erwartete Verhalten:**

- Diese:r Nutzer:in erhält die Campaign-Sendungen, die am Montag und Mittwoch getriggert wurden.
- Diese:r Nutzer:in erhält den dritten Campaign-Versand am Donnerstag nicht, da er:sie bereits zwei Push-Campaign-Sendungen in dieser Woche erhalten hat.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag {#frequency-capping-by-tag}

[Frequency-Capping-Regeln](#delivery-rules) können auf Workspaces angewendet werden, indem bestimmte Tags verwendet werden, die Sie Ihren Campaigns und Canvase zugewiesen haben. Damit können Sie Ihr Frequency-Capping im Wesentlichen auf benutzerdefiniert benannte Gruppen basieren.

Beim Frequency-Capping nach Tag können Regeln auf übergeordnete und verschachtelte Tags angewendet werden, sodass Braze alle Tags berücksichtigt. Wenn Sie beispielsweise den übergeordneten Tag A als Frequency-Cap ausgewählt haben, werden auch alle Informationen der verschachtelten Tags (z. B. Tags B und C) bei der Bestimmung des Limits einbezogen.

Sie können auch reguläres Frequency-Capping mit Frequency-Capping nach Tags kombinieren. Betrachten Sie die folgenden Regeln:

1. Maximal drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten. <br>**UND**
2. Maximal zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit zwei Regeln, die begrenzen, wie viele Push-Benachrichtigungs-Campaigns/Canvases pro Woche an eine:n Nutzer:in gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Nutzer:innen maximal drei Campaign-Sendungen pro Woche über alle Campaigns und Canvas-Schritte hinweg und maximal zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Canvase werden auf Canvas-Ebene getaggt, nicht auf Komponentenebene. Daher erbt jede Canvas-Komponente alle Tags auf Canvas-Ebene.
{% endalert %}

#### Konflikte bei Regeln {#conflicting-rules}

Wenn Regeln in Konflikt stehen, wird die restriktivste anwendbare Frequency-Capping-Regel auf Ihre Nutzer:innen angewendet. Nehmen wir beispielsweise an, Sie haben folgende Regeln:

1. Maximal eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente pro Woche von allen Campaigns und Canvas-Komponenten. <br>**UND**
2. Maximal drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit sich widersprechenden Regeln zur Begrenzung, wie viele Push-Benachrichtigungs-Campaigns/Canvas-Schritte pro Woche an eine:n Nutzer:in gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel erhält Ihre:Ihr Nutzer:in nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente mit dem Tag „promotional“ in einer bestimmten Woche, da Sie festgelegt haben, dass Nutzer:innen nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente von allen Campaigns und Canvas-Komponenten erhalten sollen. Mit anderen Worten: Die restriktivste anwendbare Frequency-Regel wird auf eine:n bestimmte:n Nutzer:in angewendet.

#### Tag-Zählung {#tag-count}

Frequency-Capping nach Tag-Regeln wird zum Zeitpunkt des Nachrichtenversands berechnet. Das bedeutet, dass Frequency-Capping nach Tag nur Tags zählt, die aktuell auf den Campaigns oder Canvase vorhanden sind, die ein:e Nutzer:in in der Vergangenheit erhalten hat. Es zählt nicht die Tags, die zum Sendezeitpunkt auf den Campaigns oder Canvase vorhanden waren, aber seitdem entfernt wurden. Es zählt jedoch, wenn ein Tag nachträglich zu einer Nachricht hinzugefügt wird, die ein:e Nutzer:in in der Vergangenheit erhalten hat, solange dies geschieht, bevor die neueste getaggte Nachricht gesendet wird.

##### Anwendungsfall {#use-case}

Betrachten Sie die folgenden Campaigns und die Frequency-Capping nach Tag-Regel:

**Campaigns**:

- **Campaign A** ist eine Push-Campaign mit dem Tag `promotional`. Sie soll am Montag um 9 Uhr gesendet werden.
- **Campaign B** ist eine Push-Campaign mit dem Tag `promotional`. Sie soll am Mittwoch um 9 Uhr gesendet werden.

**Frequency-Capping nach Tag-Regel:**

- Ihre:Ihr Nutzer:in soll maximal eine Push-Benachrichtigungs-Campaign pro Woche mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Der Tag `promotional` wird von **Campaign A** entfernt, nachdem Ihre:Ihr Nutzer:in die Nachricht erhalten hat, aber bevor **Campaign B gesendet wurde.** | Ihre:Ihr Nutzer:in erhält **Campaign B**. |
| Der Tag `promotional` wird versehentlich von **Campaign A** entfernt, nachdem Ihre:Ihr Nutzer:in die Nachricht erhalten hat. <br> Der Tag wird am Dienstag wieder zu **Campaign A** hinzugefügt, bevor **Campaign B** gesendet wird. | Ihre:Ihr Nutzer:in erhält **Campaign B** nicht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfall" }

#### Versand in großem Maßstab {#sending-at-large-scales}

Frequency-Capping nach Tag-Regeln werden bei großem Maßstab, wie z. B. 100 Nachrichten pro Kanal von Campaigns oder Canvas-Komponenten, möglicherweise nicht korrekt angewendet.

Wenn Ihre Frequency-Capping nach Tag-Regel beispielsweise lautet:

> Maximal zwei E-Mail-Campaigns oder Canvas-Komponenten mit dem Tag `Promotional` pro Woche an eine:n Nutzer:in.

Und Sie der:dem Nutzer:in im Laufe einer Woche mehr als 100 E-Mails von Campaigns und Canvas-Schritten mit aktiviertem Frequency-Capping senden, könnten mehr als zwei E-Mails an die:den Nutzer:in gesendet werden.

Da 100 Nachrichten pro Kanal mehr sind, als die meisten Marken an ihre Nutzer:innen senden, ist es unwahrscheinlich, dass Sie von dieser Einschränkung betroffen sind. Um diese Einschränkung zu vermeiden, können Sie eine Obergrenze für die maximale Anzahl von E-Mails festlegen, die Ihre Nutzer:innen im Laufe einer Woche erhalten sollen.

Beispielsweise könnten Sie die folgende Regel einrichten:

> Maximal drei E-Mail-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten.

Diese Regel stellt sicher, dass keine Nutzer:innen mehr als 100 E-Mails pro Woche erhalten, da sie höchstens drei E-Mails pro Woche von Campaigns oder Canvas-Komponenten mit aktiviertem Frequency-Capping erhalten.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wenn ich eine Sendedrosselung in einem aktiven Canvas ändere, wirkt sich das auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Ja. Wenn Sie ein Canvas-Rate-Limit erhöhen oder verringern, gilt das aktualisierte Limit für neue Nachrichten innerhalb von etwa 30 Sekunden nach der Änderung aufgrund von Caching.

### Führt Frequency-Capping dazu, dass Nutzer:innen ein Canvas verlassen? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Nein. Wenn ein:e Canvas-Nutzer:in aufgrund globaler Frequency-Capping-Einstellungen begrenzt wird, rückt die:der Nutzer:in sofort zum nächsten Canvas-Schritt vor. Die:der Nutzer:in verlässt das Canvas **nicht** aufgrund des Frequency-Cappings.

### Wie kann ich Nutzer:innen identifizieren, die in einem Canvas durch Frequency-Capping begrenzt wurden? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Nutzer:innen, die durch Frequency-Capping begrenzt werden, erzeugen kein Sende-Event für diesen Schritt. Um diese Nutzer:innen zu identifizieren, können Sie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) verwenden, um Events für durch Frequency-Capping begrenzte Nachrichten zu verfolgen. Alternativ können Sie eine [Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension) erstellen, um Nutzer:innen zu analysieren, die das Canvas betreten haben, aber die erwartete Nachricht nicht erhalten haben.

### Warum zeigt das Dashboard einen Rate-Limit-Fehler für meine Kampagne an? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Das bedeutet in der Regel, dass das [Rate-Limit für die Zustellgeschwindigkeit](#delivery-speed-rate-limiting) der Kampagne für die Zielgruppengröße zu niedrig eingestellt ist. Der Versand würde daher länger als das zulässige Zeitfenster dauern, und Braze zeigt eine Warnung an. Erhöhen Sie das Rate-Limit für die Zustellgeschwindigkeit, verkleinern Sie die Zielgruppe oder verwenden Sie **Sendevolumen begrenzen**, damit jeder geplante Versand innerhalb des zulässigen Sendefensters abgeschlossen wird. Sie können auch ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) festlegen, um eine Obergrenze über Campaigns hinweg durchzusetzen.

**Sendevolumen begrenzen** steuert, wie viele Nutzer:innen für einen Versand infrage kommen, nicht wie viele Nachrichten Braze pro Minute versendet. Nur ein Rate-Limit für die Zustellgeschwindigkeit legt den Durchsatz pro Minute fest.

Wenn Sie bereits das maximale Rate-Limit für die Zustellgeschwindigkeit erreicht haben, das für Ihr Unternehmen verfügbar ist, wenden Sie sich an Ihre:n CSM or Customer-Success-Manager or Customer-Success-Manager:in, um eine Erhöhung anzufordern.

### Was bedeutet „Gesendet“ im Zusammenhang mit Frequency-Capping? {#what-does-sent-mean-for-frequency-capping}

In Analytics und beim Frequency-Capping bezieht sich *Gesendet* darauf, wann Braze die Nachricht versendet hat (der Versand wird protokolliert), nicht auf die garantierte endgültige Zustellung an das Gerät oder den Posteingang. Frequency-Capping und Versandzähler verwenden diese protokollierten Sende-Events, die von nachgelagerten „Zugestellt“-Metriken abweichen können.

### Warum sehe ich E-Mail-Bounces oder Zurückstellungen? {#why-am-i-seeing-email-bounces-or-deferrals}

E-Mail-Bounce- und Zurückstellungsnachrichten verwenden viele verschiedene Codes und anbieterspezifische Texte. Betrachten Sie einen bestimmten Code nicht als Anzeichen für ein Rate-Limiting-Problem, da die Ursache von Ihrem Sendekontext und dem Feedback des Postfachanbieters abhängt.

Wenn Nachrichten vorübergehend zurückgestellt werden, kann weniger Versand kurzfristig helfen. Verwenden Sie ein [Rate-Limit für die Zustellgeschwindigkeit](#delivery-speed-rate-limiting), **Sendevolumen begrenzen** oder beides.

Für eine langfristige Lösung arbeiten Sie mit einer Zustellbarkeits-Expertin oder einem Zustellbarkeits-Experten zusammen, um Ihre Bounce- und Zurückstellungsdaten zu überprüfen.