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

## Informationen zum Rate-Limiting {#about-rate-limiting}

Braze ermöglicht es Ihnen, den Marketingdruck zu kontrollieren, indem Sie Ihre Campaigns durch Rate-Limiting begrenzen und den Umfang des ausgehenden Traffics von Ihrer Plattform regulieren. Sie können zwei verschiedene Arten von Rate-Limiting für Ihre Campaigns implementieren:

1. [Nutzerzentriertes Rate-Limiting:](#user-centric-rate-limiting) Konzentriert sich darauf, die beste Nutzererfahrung zu bieten.
2. [Rate-Limiting für die Zustellgeschwindigkeit:](#delivery-speed-rate-limiting) Berücksichtigt die Ressourcen Ihrer Server.

Braze unterstützt kein Rate-Limit pro Sekunde. Braze versucht, die Nachrichtensendungen gleichmäßig über die Minute zu verteilen, kann dies jedoch nicht garantieren. Wenn Sie beispielsweise eine Campaign mit einem Rate-Limit von 5.000 Nachrichten pro Minute haben, versuchen wir, die 5.000 Anfragen gleichmäßig über die Minute zu verteilen (etwa 84 Nachrichten pro Sekunde), es kann jedoch gewisse Schwankungen bei der Rate pro Sekunde geben.

### Nutzerzentriertes Rate-Limiting {#user-centric-rate-limiting}

Je mehr Segments Sie erstellen, desto häufiger werden sich die Mitgliedschaften dieser Segments überschneiden. Wenn Sie Campaigns an diese Segments senden, möchten Sie sicherstellen, dass Sie Ihre Nutzer:innen nicht zu häufig ansprechen. Wenn Nutzer:innen innerhalb kurzer Zeit zu viele Nachrichten erhalten, fühlen sie sich überflutet und deaktivieren entweder Push-Benachrichtigungen oder deinstallieren Ihre App.

#### Relevante Segment-Filter {#relevant-segment-filters}

Braze bietet die folgenden Filter, mit denen Sie die Rate begrenzen können, mit der Ihre Nutzer:innen Nachrichten erhalten:

- Last Engaged With Message
- Last Received Any Message
- Last Received Push
- Last Received Email
- Last Received SMS

#### Filter implementieren {#implementing-filters}

Nehmen wir an, wir haben ein Segment namens „Retargeting Filter Showcase“ mit einem Filter „App zuletzt vor mehr als 7 Tagen verwendet“ erstellt, um Nutzer:innen gezielt anzusprechen. Dies wäre ein Standard-Segment zur erneuten Interaktion.

Wenn Sie andere, zielgerichtetere Segments haben, die kürzlich Benachrichtigungen erhalten haben, möchten Sie möglicherweise nicht, dass Ihre Nutzer:innen zusätzlich von generischeren Campaigns für dieses Segment angesprochen werden. Indem Sie den Filter „Last Received Push“ zu diesem Segment hinzufügen, stellen Sie sicher, dass Nutzer:innen, die in den letzten 24 Stunden eine andere Benachrichtigung erhalten haben, für die nächsten 24 Stunden aus diesem Segment herausfallen. Wenn sie 24 Stunden später die anderen Kriterien des Segments weiterhin erfüllen und keine weiteren Benachrichtigungen erhalten haben, fallen sie wieder in das Segment zurück.

![Ein Segment namens „Retargeting Filter Showcase“ mit der Filtergruppe „App zuletzt vor mehr als 7 Tagen verwendet“.]({% image_buster /assets/img_archive/rate_limit_daily.png %}){: style="max-width:80%;"}

Wenn Sie diesen Filter zu allen Segments hinzufügen, die von Campaigns angesprochen werden, erhalten Ihre Nutzer:innen maximal einen Push alle 24 Stunden. Sie können dann Ihre Nachrichten priorisieren, indem Sie sicherstellen, dass Ihre wichtigsten Nachrichten vor weniger wichtigen Nachrichten zugestellt werden.

#### Ein maximales Nutzerlimit festlegen {#setting-a-maximum-user-cap}

Im Schritt **Target Audiences** Ihres Campaign-Composers können Sie auch die Gesamtzahl der Nutzer:innen begrenzen, die Ihre Nachricht erhalten. Dies dient als Kontrolle, die unabhängig von Ihren Campaign-Filtern ist.

![Zielgruppenübersicht mit einem aktivierten Kontrollkästchen zur Begrenzung der Anzahl der Personen, die die Campaign erhalten.]({% image_buster /assets/img_archive/total_limit.png %}){: style="max-width:50%;"}

Durch die Auswahl des maximalen Nutzerlimits können Sie das Nachrichtenvolumen auf Kanalbasis oder global über alle Nachrichtentypen hinweg begrenzen. Braze sendet keine Nachrichten an Nutzer:innen, die Kontrollgruppen zugewiesen sind, daher werden diese nicht auf das Limit angerechnet.

{% alert note %}
Das maximale Nutzerlimit begrenzt die Anzahl der versendeten Nutzer:innen, nicht die Anzahl der erfolgreich zugestellten Nachrichten. Da abgebrochene Nachrichten auf dieses Limit angerechnet werden, kann die tatsächliche Anzahl gesendeter Nachrichten unter dem konfigurierten Limit liegen. Wenn Sie beispielsweise ein Limit von 10.000 festlegen und 2.000 Nachrichten aufgrund von Liquid-Logik oder anderen Bedingungen abgebrochen werden, werden nur 8.000 Nachrichten gesendet.
{% endalert %}

##### Maximales Nutzerlimit für Multichannel-Campaigns {#maximum-user-cap-for-multichannel-campaigns}

Für Multichannel-Campaigns wählt Braze zunächst eine Zielgruppe bis zu Ihrem konfigurierten maximalen Nutzerlimit aus. Anschließend bewertet Braze jede:n Nutzer:in in dieser begrenzten Zielgruppe für jeden Kanal in der Campaign.

Dadurch bleibt die Größe der begrenzten Zielgruppe gleich, aber die Sendungen pro Kanal können je nach Kanalberechtigung variieren. Wenn Sie beispielsweise ein maximales Nutzerlimit von 500.000 festlegen und ein:e Nutzer:in nur für Push und Content Cards berechtigt ist, erhält diese:r Nutzer:in diese Kanäle, aber keine E-Mail.

Wenn Sie diese Kanäle in separate Campaigns aufteilen, die jeweils dasselbe Segment ansprechen und jeweils ein eigenes maximales Nutzerlimit haben, bewertet und begrenzt jede Campaign Nutzer:innen unabhängig. Braze garantiert nicht, dass jede Campaign exakt dieselbe Teilmenge von Nutzer:innen auswählt.

Wenn Sie Folge-Campaigns benötigen, die sich an Nutzer:innen richten, denen eine frühere Campaign gesendet wurde, erstellen Sie ein Segment mit dem Filter **Received Campaign** und verwenden Sie dieses Segment dann für die Folge-Campaigns.

##### Maximales Nutzerlimit mit Optimierungen {#maximum-user-cap-with-optimizations}

Bei einer einmalig gesendeten Campaign mit **Optimierung durch BrazeAI<sup>TM</sup>** besteht die Campaign aus zwei Sendungen: dem anfänglichen Experiment und der optimierten Sendung.

Um in diesem Szenario ein maximales Nutzerlimit einzurichten, wählen Sie **Sendevolumen begrenzen**, dann **Lebensdauer der Campaign** und geben Sie einen Wert für **Maximale Sendungen** ein. Ihr Zielgruppenlimit wird nach den im **A/B-Tests**-Panel angezeigten Prozentsätzen aufgeteilt.

Wenn Sie **Bei jeder geplanten Campaign** auswählen, werden diese beiden Phasen separat auf die festgelegte Anzahl begrenzt. Dies ist in der Regel nicht wünschenswert.

#### Ein maximales Impressionen-Limit für Campaigns festlegen {#setting-a-maximum-impression-cap-on-campaigns}

Für In-App-Nachrichten können Sie den Marketingdruck steuern, indem Sie eine maximale Anzahl von Impressionen festlegen, die Ihrer Nutzerbasis angezeigt werden, wonach Braze keine weiteren Nachrichten mehr an Ihre Nutzer:innen sendet. Es ist jedoch wichtig zu beachten, dass dieses Limit nicht exakt ist.

In-App-Nachrichtenregeln werden beim Sitzungsstart an eine App gesendet, was bedeutet, dass Braze eine Nachricht an die:den Nutzer:in senden kann, bevor das Limit erreicht ist, aber bis die:der Nutzer:in die Nachricht auslöst, wurde das Limit bereits erreicht. In dieser Situation zeigt das Gerät die Nachricht dennoch an.

Nehmen wir beispielsweise an, Sie haben ein Spiel mit einer In-App-Nachricht, die ausgelöst wird, wenn Nutzer:innen ein Level abschließen, und Sie das Limit auf 100 Impressionen begrenzen. Es gab bisher 99 Impressionen. Alice und Bob öffnen beide das Spiel, und Braze teilt ihren Geräten mit, dass sie berechtigt sind, die Nachricht zu erhalten, wenn sie ein Level abschließen. Alice schließt zuerst ein Level ab und erhält die Nachricht. Bob schließt als Nächstes das Level ab, aber da sein Gerät seit Sitzungsbeginn nicht mit den Braze-Servern kommuniziert hat, ist sein Gerät nicht über das erreichte Limit informiert, und er erhält die Nachricht ebenfalls. Sobald jedoch ein Impressionen-Limit erreicht wurde, sendet das System diese Nachricht beim nächsten Abruf der Liste der berechtigten In-App-Nachrichten durch ein beliebiges Gerät nicht mehr und entfernt die Nachricht von diesem Gerät.

### Rate-Limiting und A/B-Tests {#rate-limiting-and-ab-testing}

Wenn Sie Rate-Limiting mit einem A/B-Test verwenden, wird das Rate-Limit nicht in gleicher Weise auf die Kontrollgruppe wie auf die Testgruppe angewendet, was eine potenzielle Quelle für zeitliche Verzerrungen darstellt. Um diese Verzerrung zu vermeiden, verwenden Sie geeignete Konversionsfenster.

### Rate-Limiting für die Zustellgeschwindigkeit {#delivery-speed-rate-limiting}

Wenn Sie erwarten, dass große Campaigns einen Anstieg der Nutzeraktivität verursachen und Ihre Server überlasten, können Sie ein Rate-Limit pro Minute für den Nachrichtenversand festlegen, was bedeutet, dass Braze nicht mehr als Ihre rate-limitierte Einstellung innerhalb einer Minute sendet.

Beim Targeting von Nutzer:innen während der Campaign-Erstellung können Sie zu **Target Audiences** (für Campaigns) oder **Send Settings** (für Canvas) navigieren, um ein Rate-Limit auszuwählen (in verschiedenen Stufen von mindestens 10 bis maximal 500.000 Nachrichten pro Minute).

Beachten Sie, dass nicht rate-limitierte Campaigns diese Zustellungslimits überschreiten können. Seien Sie sich jedoch bewusst, dass Nachrichten abgebrochen werden, wenn sie aufgrund eines niedrigen Rate-Limits 72 Stunden oder länger verzögert werden. Wenn das Rate-Limit zu niedrig ist, erhält die:der Ersteller:in der Campaign Warnungen im Dashboard und per E-Mail.

{% alert tip %}
Legen Sie ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) fest, um ein Rate-Limit über einen gesamten Workspace hinweg durchzusetzen.
{% endalert %}

#### Beispiel {#example}

Wenn Sie 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute versenden möchten, wird die Zustellung über acht Minuten verteilt. Ihre Campaign liefert in jeder der ersten sieben Minuten nicht mehr als 10.000 Nachrichten und 5.000 in der letzten Minute.

#### Anzahl der Sendungen {#number-of-sends}

Beachten Sie, dass rate-limitierte Nachrichten möglicherweise nicht gleichmäßig über den Verlauf jeder Minute verteilt werden. Am Beispiel eines Rate-Limits von 10.000 pro Minute bedeutet dies, dass Braze sicherstellt, dass nicht mehr als 10.000 Nachrichten pro Minute gesendet werden. Dies kann bedeuten, dass ein höherer Prozentsatz der 10.000 Nachrichten in der ersten Hälfte der Minute gesendet wird als in der zweiten Hälfte.

Das Rate-Limit wird zu Beginn des Nachrichtensendeversuchs angewendet. Wenn es Schwankungen bei der Dauer bis zum Abschluss des Versands gibt, kann die Anzahl der abgeschlossenen Sendungen das Rate-Limit für einige Minuten leicht überschreiten. Im Zeitverlauf gleicht sich die Anzahl der Sendungen pro Minute auf nicht mehr als das Rate-Limit aus.

{% alert important %}
Seien Sie vorsichtig, zeitkritische Nachrichten mit dieser Form des Rate-Limitings in Bezug auf die Gesamtzahl der Nutzer:innen in einem Segment zu verzögern. Wenn das Segment beispielsweise 30 Millionen Nutzer:innen enthält, wir aber das Rate-Limit auf 10.000 pro Minute festlegen, wird ein großer Teil Ihrer Nutzerbasis die Nachricht erst am folgenden Tag erhalten.
{% endalert %}

#### Multichannel-Campaigns und Canvases {#multichannel-campaigns-and-canvases}

Beim Festlegen eines Rate-Limits für die Zustellgeschwindigkeit einer Multichannel-Campaign oder eines Canvas können Sie wählen, ob Sie ein gemeinsames Rate-Limit oder ein kanalbasiertes Limit festlegen.

Wenn eine Multichannel-Campaign oder ein Canvas ein gemeinsames Rate-Limit verwendet, bedeutet dies, dass die Gesamtzahl der pro Minute gesendeten Nachrichten der Campaign oder des Canvas das Rate-Limit nicht überschreitet. Wenn Ihr Canvas beispielsweise ein Rate-Limit von 500.000 pro Minute hat und E-Mail- sowie SMS-Nachrichtenschritte enthält, sendet Braze insgesamt 500.000 Nachrichten pro Minute über E-Mail und SMS hinweg.

![Die Option zur Begrenzung der Rate, mit der die Campaign sendet, ausgewählt mit 500.000 Nachrichten pro Minute.]({% image_buster /assets/img_archive/multichannel_campaigns_rate_limit.png %}){: style="max-width:50%;"}

Wenn eine Multichannel-Campaign oder ein Canvas kanalbasiertes Rate-Limiting verwendet, wird das Rate-Limit auf jeden Ihrer ausgewählten Kanäle angewendet. Sie können beispielsweise Ihre Campaign oder Ihren Canvas so einstellen, dass maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die Campaign oder den Canvas hinweg gesendet werden.

![Separate Rate-Limits für zwei Kanäle, Webhook und SMS/MMS/RCS, mit jeweils 5.000 und 2.500 Nachrichten pro Minute.]({% image_buster /assets/img_archive/channel_rate_limits.png %}){: style="max-width:70%;"}

##### Push-Benachrichtigungen {#push-notifications}

Für Campaigns oder Canvases mit Push-Plattformen (wie Android, iOS, Web-Push oder Kindle) können Sie **Push-Benachrichtigungen** auswählen, um ein Rate-Limit durchzusetzen, das zwischen allen Push-Plattformen in Ihrer Campaign oder Ihrem Canvas geteilt wird.

![Das Kanal-Dropdown mit Optionen für Push-Plattformen und Push-Benachrichtigungen.]({% image_buster /assets/img_archive/push_notifications_rate_limit.png %}){: style="max-width:30%;"}

Wenn Sie ein Limit für Push-Benachrichtigungen auswählen, können Sie keine individuellen Push-Kanal-Rate-Limits festlegen. Ebenso können Sie keine gemeinsamen Push-Benachrichtigungslimits festlegen, wenn Sie Limits für einzelne Push-Kanäle auswählen.

{% alert important %}
**Aktualisierungen der Rate-Limiting-Oberfläche**<br>
Braze hat die Rate-Limiting-Oberfläche aktualisiert, um mehr Transparenz und Kontrolle darüber zu bieten, wie Rate-Limits auf Multichannel-Campaigns und Canvases angewendet werden.<br><br>

- **Bestehende Campaigns und Canvases:** Alle bestehenden Campaigns und Canvases wurden auf diese Oberfläche migriert. Ihr Zustellverhalten bleibt gleich. Das Dashboard zeigt an, ob die Campaign eine gemeinsame oder kanalbasierte Logik verwendet.<br>
- **Neue Campaigns und Canvases:** Für alle neuen Campaigns und Canvases gibt es einen manuellen Schalter zur Auswahl Ihrer bevorzugten Rate-Limit-Logik. Stellen Sie sicher, dass Sie das Rate-Limiting-Verhalten auswählen, das mit Ihrem beabsichtigten Verhalten übereinstimmt, wenn Sie ein Campaign- oder Canvas-Rate-Limit festlegen oder aktualisieren.
{% endalert %}

##### Überlegungen zum Rate-Limiting {#rate-limiting-considerations}

Einige Hinweise, die Sie bei der Konfiguration von Rate-Limits beachten sollten, und welches Verhalten Sie erwarten können:

- SMS-Sendungen unterliegen einem Rate-Limit von 50.000 pro Abo-Gruppe. Einige SMS-Anbieter können weitere Limits durchsetzen.
- Die folgenden Nachrichten werden weder durch das Rate-Limit gedrosselt noch darauf angerechnet:
    - Testsendungen
    - Seed-Gruppen
    - Content Cards, die so konfiguriert sind, dass sie „bei erster Impression“ erstellt werden (Dies wird durch die Rate der App-Impressionen gesteuert. Weitere Informationen zu den Unterschieden zwischen den Card-Creation-Optionen finden Sie unter [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation#differences).)
- Rate-Limits für die Zustellgeschwindigkeit werden für Folgendes nicht unterstützt:
    - SMS-Autoantworten
    - SLA-gestützte Nachrichten (wie [Transaktions-E-Mails]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email))
    - In-App-Nachrichten
    - Feature-Flags
    - Banner

#### Rate-Limiting und Connected-Content-Wiederholungsversuche {#rate-limiting-and-connected-content-retries}

Wenn der [Connected-Content-Wiederholungsversuch]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries) aktiviert ist, wiederholt Braze fehlgeschlagene Aufrufe unter Einhaltung des Rate-Limits, das Sie für jede erneute Sendung festgelegt haben. Betrachten wir das Szenario des Versendens von 75.000 Nachrichten mit einem Rate-Limit von 10.000 pro Minute. Stellen Sie sich vor, dass in der ersten Minute der Aufruf fehlschlägt oder langsam ist und nur 4.000 Nachrichten gesendet werden.

Anstatt zu versuchen, die Verzögerung auszugleichen und die verbleibenden 6.000 Nachrichten in der zweiten Minute zu senden oder sie zu den bereits für den Versand geplanten 10.000 hinzuzufügen, verschiebt Braze diese 6.000 Nachrichten an das „Ende der Warteschlange“ und fügt bei Bedarf eine Minute zur Gesamtzeit hinzu, die für den Versand Ihrer Nachricht benötigt wird.

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Rate-Limiting und Connected-Content-Wiederholungsversuche" }

Connected-Content-Anfragen werden nicht unabhängig rate-limitiert und folgen dem Webhook-Rate-Limit. Das bedeutet, wenn es einen Connected-Content-Aufruf an einen eindeutigen Endpunkt pro Webhook gibt, würden Sie 5.000 Webhooks und auch 5.000 Connected-Content-Aufrufe pro Minute erwarten. Beachten Sie, dass Caching dies beeinflussen und die Anzahl der Connected-Content-Aufrufe reduzieren kann. Zusätzlich können Wiederholungsversuche die Connected-Content-Aufrufe erhöhen. Wir empfehlen daher, zu überprüfen, ob der Connected-Content-Endpunkt gewisse Schwankungen bewältigen kann.

{% alert note %}
**Rate-Limits sind Geschwindigkeitsbegrenzungen und definieren keine exakte Sendegeschwindigkeit.** Im Allgemeinen werden Nachrichten innerhalb einer gegebenen Minute gleichmäßig verteilt, und in der überwiegenden Mehrheit der Fälle werden sie am oder sehr nahe am konfigurierten Limit gesendet. Dies ist nicht immer der Fall – beispielsweise wenn Nachrichten sehr groß sind (wie E-Mails mit vielen Content Blocks, Connected-Content-Tags oder Katalog-Artikel-Tags) oder wenn es viele Liquid-Abbrüche gibt (abgebrochene Nachrichten belegen weiterhin einen Slot und können die effektive Senderate reduzieren).<br><br>
In der Praxis kann die nachhaltige Senderate (abgeschlossene Nachrichten pro Minute) aufgrund von Wiederholungsversuchen, Netzwerkvariabilität, Latenz nachgelagerter Endpunkte und pro-Minuten-Glättung niedriger als das konfigurierte Rate-Limit sein. Wenn Sie dauerhaft einen deutlich niedrigeren Durchsatz als erwartet feststellen, überprüfen Sie Connected-Content-Antwortzeiten, Fehlerraten (wie `429`) und das Wiederholungsverhalten.
{% endalert %}

## Frequency-Capping im Detail {#about-frequency-capping}

Wenn Ihre Nutzerbasis weiter wächst und Ihr Messaging sich auf Lifecycle-, getriggerte, transaktionale und Konversions-Campaigns ausweitet, ist es wichtig zu verhindern, dass Ihre Benachrichtigungen als „spammy“ oder störend wahrgenommen werden. Durch eine bessere Kontrolle über das Erlebnis Ihrer Nutzer:innen ermöglicht Ihnen Frequency-Capping, die gewünschten Campaigns zu erstellen, ohne Ihre Zielgruppe zu überfordern.

### Rate-Limiting und Frequency-Capping gemeinsam verwenden {#use-rate-limiting-and-frequency-capping-together}

Wenn Sie sowohl Rate-Limiting als auch Frequency-Capping für eine Campaign aktivieren, wendet Braze diese in folgender Reihenfolge an:

1. **Rate-Limit** wird zuerst angewendet, um den anfänglichen Pool von Nutzer:innen auszuwählen, die Nachrichten erhalten können.
2. **Frequency-Capping** wird als Zweites angewendet, um Nutzer:innen aus diesem Pool zu filtern.
3. **Nachrichten werden gesendet** an die verbleibenden Nutzer:innen.

{% alert important %}
Wenn viele Nutzer:innen in Ihrem rate-limitierten Pool durch Frequency-Capping eingeschränkt werden, senden Sie möglicherweise weniger Nachrichten als Ihr Rate-Limit-Wert vorsieht. Braze füllt keine zusätzlichen Nutzer:innen aus dem Rate-Limit nach, sobald das Frequency-Capping Nutzer:innen aus dem Sendepool entfernt hat.
{% endalert %}

#### Beispiel

Bei einem Rate-Limit von 500 Nutzer:innen und aktiviertem Frequency-Capping: Wenn 200 dieser 500 rate-limitierten Nutzer:innen durch Frequency-Capping eingeschränkt werden, werden nur 300 Nachrichten gesendet – nicht 500.

#### Empfehlungen {#recommendations}

Wenn Sie bei gleichzeitiger Verwendung beider Features eine bestimmte Anzahl von Nutzer:innen erreichen möchten, ziehen Sie folgende Ansätze in Betracht:

- **Erhöhen Sie Ihr Rate-Limit:** Um Nutzer:innen zu berücksichtigen, die durch Frequency-Capping eingeschränkt werden. Wenn Sie beispielsweise 500 Nutzer:innen erreichen möchten, aber erwarten, dass einige durch Frequency-Capping eingeschränkt werden, setzen Sie Ihr Rate-Limit höher an (z. B. 1.000 Nutzer:innen).
- **Verwenden Sie nur Rate-Limiting:** Wenn Ihr Ziel darin besteht, das Nachrichtenvolumen pro Campaign zu steuern.
- **Wenden Sie sich an Ihren Customer-Success-Manager:** Für Unterstützung bei der Entwicklung einer robusten Messaging-Strategie, die sowohl geschäftliche Anforderungen als auch technische Aspekte in Einklang bringt.

### Feature-Übersicht {#freq-cap-feat-over}

Frequency-Capping wird auf der Sendeebene von Campaigns oder Canvas-Komponenten angewendet und kann für jeden Workspace unter **Einstellungen** > **Frequency-Capping-Regeln** eingerichtet werden.

Standardmäßig ist Frequency-Capping aktiviert, wenn neue Campaigns erstellt werden. Von hier aus können Sie Folgendes festlegen:

- Den Messaging-Kanal, den Sie begrenzen möchten: Push, E-Mail, SMS, Webhook, WhatsApp, LINE oder jeden dieser Kanäle.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente über einen Kanal innerhalb eines bestimmten Zeitraums erhalten soll.
- Wie oft jede:r Nutzer:in eine Campaign oder Canvas-Komponente mit einem bestimmten [Tag](#frequency-capping-by-tag) innerhalb eines bestimmten Zeitraums erhalten soll.

Dieser Zeitraum kann in Minuten, Tagen oder Wochen (sieben Tage) gemessen werden, mit einer maximalen Dauer von 30 Tagen.

Jede Zeile von Frequency-Capping-Regeln ist mit dem `AND`-Operator verbunden, und Sie können bis zu 10 Regeln pro Workspace hinzufügen. Sie können mehrere Begrenzungen für dieselben Nachrichtentypen einrichten. Beispielsweise können Sie Nutzer:innen auf maximal einen Push pro Tag und maximal drei Pushes pro Woche begrenzen. Beachten Sie, dass abgebrochene Nachrichten nicht auf das Frequency-Capping angerechnet werden.

![Frequency-Capping-Bereich mit Listen von Campaigns und Canvases, auf die Regeln angewendet werden und nicht angewendet werden.]({% image_buster /assets/img_archive/rate_limiting_overview_2.png %}){: style="max-width:90%;"}

#### Verhalten, wenn Nutzer:innen durch Frequency-Capping eingeschränkt sind oder eine Nachricht in einem Canvas-Schritt abgebrochen wird {#behavior-when-users-are-frequency-capped-or-a-message-is-aborted-on-a-canvas-step}

Globales Frequency-Capping allein lässt Nutzer:innen nicht aus einem Canvas aussteigen. Bei [Nachrichtenschritten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) kommen Nutzer:innen weiterhin voran, wenn eine Nachricht aufgrund des globalen Frequency-Cappings nicht gesendet wird, gemäß den Regeln dazu, [wie Nutzer:innen vorankommen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Dasselbe gilt, wenn eine Nachricht abgebrochen wird (z. B. durch eine Liquid-Abbruchbedingung): Die:der Nutzer:in durchläuft das Canvas weiter, als ob die Nachricht gesendet worden wäre.

Dies ist getrennt von den **Zustellungsvalidierungen** eines Nachrichtenschritts. Wenn ein:e Nutzer:in Ihre Zustellungsvalidierungskriterien zum Sendezeitpunkt nicht erfüllt, kann sie bzw. er das Canvas an diesem Schritt verlassen.

### Zustellungsregeln {#delivery-rules}

Es kann Campaigns geben, z. B. transaktionale Nachrichten, die Nutzer:innen immer erreichen sollen – auch wenn sie bereits ihr Frequency-Capping erreicht haben. Beispielsweise kann eine Liefer-App eine E-Mail oder einen Push senden wollen, wenn ein Artikel zugestellt wird, unabhängig davon, wie viele Campaigns die:der Nutzer:in bereits erhalten hat.

Wenn Sie möchten, dass eine bestimmte Campaign die Frequency-Capping-Regeln überschreibt, können Sie dies im Braze-Dashboard beim Planen der Zustellung dieser Campaign einrichten, indem Sie **Frequency-Capping** auf **AUS** umschalten.

Danach werden Sie gefragt, ob diese Campaign trotzdem auf Ihr Frequency-Capping angerechnet werden soll. Nachrichten, die auf das Frequency-Capping angerechnet werden, fließen in die Berechnungen des intelligenten Kanal-Filters ein.

Beim Senden von [API-Campaigns]({{site.baseurl}}/developer_guide/rest_api/messaging#messaging), die oft transaktional sind, haben Sie die Möglichkeit anzugeben, dass eine Campaign die Frequency-Capping-Regeln ignorieren soll, indem Sie `override_frequency_capping` in der API-Anfrage auf `true` setzen.

Standardmäßig werden neue Campaigns und Canvases, die das Frequency-Capping nicht einhalten, auch nicht darauf angerechnet. Dies ist für jede Campaign und jedes Canvas konfigurierbar.

{% alert note %}
Dieses Verhalten ändert das Standardverhalten, wenn Sie Frequency-Capping für eine Campaign oder ein Canvas deaktivieren. Die Änderungen sind abwärtskompatibel und wirken sich nicht auf Nachrichten aus, die derzeit aktiv sind.
{% endalert %}

![Bereich „Zustellungskontrollen“ mit aktiviertem Frequency-Capping.]({% image_buster /assets/img_archive/frequencycappingupdate.png %}){: style="max-width:90%;"}

#### Wie Sendungen auf Begrenzungen angerechnet werden {#how-sends-count-toward-caps}

Frequency-Capping wird pro Versand angewendet: Jedes Mal, wenn Braze eine Campaign oder Canvas-Komponente an eine:n Nutzer:in sendet, wird dies auf Ihre Begrenzungen angerechnet – nicht jede Nachrichtenvariante oder Plattform innerhalb dieses Versands. Wenn Nutzer:innen beispielsweise auf fünf Push-Campaigns pro Woche begrenzt sind, erhalten sie nach dem fünften Versand keine weiteren Push-Campaigns, bis die Begrenzung zurückgesetzt wird.

##### Multichannel-Sendungen {#multichannel-sends}

Wenn ein einzelner Versand mehrere Kanäle nutzt, wird dieser Versand höchstens einmal pro geltender Frequency-Capping-Regel gezählt. Wenn Sie beispielsweise eine Multichannel-Kampagne erstellen, die E-Mail, iOS-Push und Android-Push in einer Zustellung sendet, und Ihr Workspace Regeln für Push und E-Mail sowie eine Regel hat, die für alle Kanäle gilt, wird diese Zustellung einmal auf die Push-Regel, einmal auf die E-Mail-Regel und einmal auf die Alle-Kanäle-Regel angerechnet – sie wird nicht einmal pro Push-Plattform oder pro Nachricht innerhalb des Versands gezählt. Wenn Nutzer:innen auf einen Push und eine E-Mail-Campaign pro Tag begrenzt sind und diese Multichannel-Kampagne erhalten, sind sie für den Rest des Tages nicht für weitere Push- oder E-Mail-Campaigns berechtigt, es sei denn, eine Campaign ignoriert die Frequency-Capping-Regeln.

In-App-Nachrichten und Content Cards werden nicht als Begrenzungen für Campaigns oder Canvas-Komponenten irgendeines Typs gezählt oder darauf angerechnet.

##### Push-Benachrichtigungen mit mehreren Geräten {#push-notifications-with-multiple-devices}

Bei Push-Campaigns wird das Frequency-Capping auf Campaign- oder Canvas-Komponentenebene gezählt, nicht pro einzelnem Gerät. Wenn ein Nutzerprofil mehrere für Push registrierte Geräte hat (z. B. ein iPhone und ein iPad), zählt eine Begrenzung auf Campaign-Ebene dies als einen Versand, unabhängig davon, wie viele Geräte die Benachrichtigung erhalten. Dies ähnelt der Art und Weise, wie eine wiederkehrende Campaign mit täglicher Kadenz als ein Versand pro Tag gezählt wird, auch wenn sie im Laufe der Woche mehrmals wiederkehrt.

{% alert important %}
Globales Frequency-Capping basiert auf der Zeitzone der Nutzer:innen und wird nach Kalendertagen berechnet, nicht nach 24-Stunden-Zeiträumen. Wenn Sie beispielsweise eine Frequency-Capping-Regel einrichten, die nicht mehr als eine Campaign pro Tag vorsieht, kann ein:e Nutzer:in um 23 Uhr in der jeweiligen Ortszeit eine Nachricht erhalten und wäre eine Stunde später bereits für eine weitere Nachricht berechtigt.
{% endalert %}

#### Anwendungsfälle {#use-cases}

{% tabs %}
{% tab Anwendungsfall 1 %}

Nehmen wir an, Sie legen eine Frequency-Capping-Regel fest, die besagt, dass Ihre Nutzer:innen pro Woche maximal drei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte von allen Campaigns oder Canvas-Schritten erhalten sollen.

Wenn Ihre:Ihr Nutzer:in in dieser Woche drei Push-Benachrichtigungen, zwei In-App-Nachrichten und eine Content-Card erhalten soll, werden alle diese Nachrichten zugestellt.

{% endtab %}
{% tab Anwendungsfall 2 %}

Dieses Szenario verwendet eine Frequency-Capping-Regel, nach der Nutzer:innen pro Woche nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Schritte von allen Campaigns oder Canvas-Schritten erhalten sollen.

**Wenn folgendes Szenario eintritt:**

- Ein:e Nutzer:in triggert dieselbe Campaign `Campaign ABC` dreimal im Laufe einer Woche.
- Diese:r Nutzer:in triggert `Campaign ABC` einmal am Montag, einmal am Mittwoch und einmal am Donnerstag.

![Frequency-Capping-Bereich mit der Regel, nicht mehr als 2 Push-Benachrichtigungs-Campaigns/Canvas-Schritte von allen Campaigns/Canvas-Schritten pro Woche an eine:n Nutzer:in zu senden.]({% image_buster /assets/img/standard_rules_fnfn.png %})

**Dann ist das erwartete Verhalten:**

- Diese:r Nutzer:in erhält die Campaign-Sendungen, die am Montag und Mittwoch getriggert wurden.
- Diese:r Nutzer:in erhält die dritte Campaign-Sendung am Donnerstag nicht, da die:der Nutzer:in in dieser Woche bereits zwei Push-Campaign-Sendungen erhalten hat.

{% endtab %}
{% endtabs %}

### Frequency-Capping nach Tag {#frequency-capping-by-tag}

[Frequency-Capping-Regeln](#delivery-rules) können auf Workspaces angewendet werden, indem bestimmte Tags verwendet werden, die Sie Ihren Campaigns und Canvases zugewiesen haben. So können Sie Ihr Frequency-Capping im Wesentlichen auf benutzerdefinierten Gruppen basieren.

Beim Frequency-Capping nach Tag können Regeln für Haupt- und verschachtelte Tags festgelegt werden, sodass Braze alle Tags berücksichtigt. Wenn Sie beispielsweise das Haupt-Tag A als Frequency-Capping-Kriterium ausgewählt haben, beziehen wir auch Informationen zu allen verschachtelten Tags (z. B. Tags B und C) in die Berechnung der Begrenzung ein.

Sie können auch reguläres Frequency-Capping mit Frequency-Capping nach Tags kombinieren. Betrachten Sie die folgenden Regeln:

1. Nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten. <br>**UND**
2. Nicht mehr als zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit zwei Regeln, die die Anzahl der Push-Benachrichtigungs-Campaigns/Canvases begrenzen, die pro Woche an eine:n Nutzer:in gesendet werden können.]({% image_buster /assets/img/tag_rule_fnfn.png %} "rules")

Infolgedessen erhalten Ihre Nutzer:innen pro Woche maximal drei Campaign-Sendungen über alle Campaigns und Canvas-Schritte hinweg und maximal zwei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten mit dem Tag `promotional`.

{% alert important %}
Canvases werden auf Canvas-Ebene getaggt, nicht auf Komponentenebene. Jede Canvas-Komponente übernimmt daher alle Tags auf Canvas-Ebene.
{% endalert %}

#### Konfligierende Regeln {#conflicting-rules}

Wenn Regeln in Konflikt stehen, wird die restriktivste geltende Frequency-Capping-Regel auf Ihre Nutzer:innen angewendet. Nehmen wir beispielsweise an, Sie haben folgende Regeln:

1. Nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente pro Woche von allen Campaigns und Canvas-Komponenten. <br>**UND**
2. Nicht mehr als drei Push-Benachrichtigungs-Campaigns oder Canvas-Komponenten pro Woche mit dem Tag `promotional`.

![Frequency-Capping-Bereich mit konfligierenden Regeln zur Begrenzung der Anzahl von Push-Benachrichtigungs-Campaigns/Canvas-Schritten, die pro Woche an eine:n Nutzer:in gesendet werden.]({% image_buster /assets/img/global_rules.png %} "global rules")

In diesem Beispiel erhält Ihre:Ihr Nutzer:in nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente mit dem Tag „promotional“ in einer bestimmten Woche, da Sie festgelegt haben, dass Nutzer:innen nicht mehr als eine Push-Benachrichtigungs-Campaign oder Canvas-Komponente von allen Campaigns und Canvas-Komponenten erhalten sollen. Mit anderen Worten: Die restriktivste geltende Frequency-Regel ist die Regel, die auf die jeweilige:n Nutzer:in angewendet wird.

#### Tag-Zählung {#tag-count}

Frequency-Capping-Regeln nach Tag werden zum Zeitpunkt des Nachrichtenversands berechnet. Das bedeutet, dass Frequency-Capping nach Tag nur Tags zählt, die sich derzeit auf den Campaigns oder Canvases befinden, die ein:e Nutzer:in in der Vergangenheit erhalten hat. Es zählt nicht die Tags, die sich zu dem Zeitpunkt auf den Campaigns oder Canvases befanden, als sie gesendet wurden, aber seitdem entfernt wurden. Es zählt jedoch, wenn ein Tag nachträglich zu einer Nachricht hinzugefügt wird, die ein:e Nutzer:in in der Vergangenheit erhalten hat, aber bevor die neueste getaggte Nachricht gesendet wird.

##### Anwendungsfall {#use-case}

Betrachten Sie die folgenden Campaigns und die Frequency-Capping-Regel nach Tag:

**Campaigns**:

- **Campaign A** ist eine Push-Campaign mit dem Tag `promotional`. Sie ist für den Versand am Montag um 9 Uhr geplant.
- **Campaign B** ist eine Push-Campaign mit dem Tag `promotional`. Sie ist für den Versand am Mittwoch um 9 Uhr geplant.

**Frequency-Capping-Regel nach Tag:**

- Ihre:Ihr Nutzer:in soll pro Woche nicht mehr als eine Push-Benachrichtigungs-Campaign mit dem Tag `promotional` erhalten.<br><br>

| Aktion | Ergebnis |
|---|---|
| Das Tag `promotional` wird von **Campaign A** entfernt, nachdem Ihre:Ihr Nutzer:in die Nachricht erhalten hat, aber bevor **Campaign B gesendet wurde.** | Ihre:Ihr Nutzer:in erhält **Campaign B**. |
| Das Tag `promotional` wird versehentlich von **Campaign A** entfernt, nachdem Ihre:Ihr Nutzer:in die Nachricht erhalten hat. <br> Das Tag wird am Dienstag wieder zu **Campaign A** hinzugefügt, bevor **Campaign B** gesendet wird. | Ihre:Ihr Nutzer:in erhält **Campaign B** nicht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfall" }

#### Versand in großem Umfang {#sending-at-large-scales}

Frequency-Capping-Regeln nach Tag werden bei großen Volumina möglicherweise nicht korrekt angewendet, z. B. bei 100 Nachrichten pro Kanal von Campaigns oder Canvas-Komponenten.

Wenn Ihre Frequency-Capping-Regel nach Tag beispielsweise lautet:

> Nicht mehr als zwei E-Mail-Campaigns oder Canvas-Komponenten mit dem Tag `Promotional` pro Woche an eine:n Nutzer:in.

Und Sie den Nutzer:innen im Laufe einer Woche mehr als 100 E-Mails von Campaigns und Canvas-Schritten mit aktiviertem Frequency-Capping senden, können mehr als zwei E-Mails an die:den Nutzer:in gesendet werden.

Da 100 Nachrichten pro Kanal mehr sind, als die meisten Marken an ihre Nutzer:innen senden, ist es unwahrscheinlich, dass Sie von dieser Einschränkung betroffen sind. Um diese Einschränkung zu vermeiden, können Sie eine Begrenzung für die maximale Anzahl von E-Mails festlegen, die Ihre Nutzer:innen im Laufe einer Woche erhalten sollen.

Beispielsweise könnten Sie folgende Regel einrichten:

> Nicht mehr als drei E-Mail-Campaigns oder Canvas-Komponenten pro Woche von allen Campaigns und Canvas-Schritten.

Diese Regel stellt sicher, dass keine:r Nutzer:in mehr als 100 E-Mails pro Woche erhält, da Nutzer:innen höchstens drei E-Mails pro Woche von Campaigns oder Canvas-Komponenten mit aktiviertem Frequency-Capping erhalten.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wenn ich eine Sendedrosselung in einem aktiven Canvas ändere, wirkt sich das auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#if-i-change-a-send-throttle-on-an-active-canvas-does-it-affect-users-already-in-the-canvas}

Ja. Wenn Sie ein Canvas-Rate-Limit erhöhen oder verringern, gilt das aktualisierte Limit für neue Nachrichten innerhalb von ca. 30 Sekunden nach der Änderung aufgrund von Caching.

### Bewirkt Frequency-Capping, dass Nutzer:innen einen Canvas verlassen? {#does-frequency-capping-cause-users-to-exit-a-canvas}

Nein. Wenn ein:e Canvas-Nutzer:in aufgrund globaler Frequency-Capping-Einstellungen begrenzt ist, wird die:der Nutzer:in sofort zum nächsten Canvas-Schritt weitergeleitet. Die:der Nutzer:in verlässt den Canvas aufgrund des Frequency-Cappings **nicht**.

### Wie kann ich Nutzer:innen identifizieren, bei denen in einem Canvas Frequency-Capping angewendet wurde? {#how-can-i-identify-users-who-were-frequency-capped-in-a-canvas}

Nutzer:innen, bei denen Frequency-Capping greift, erzeugen für diesen Schritt kein Sendeereignis. Um diese Nutzer:innen zu identifizieren, können Sie [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) verwenden, um Ereignisse zu verfolgen, bei denen Nachrichten durch Frequency-Capping begrenzt wurden. Alternativ können Sie eine [Segmenterweiterung]({{site.baseurl}}/user_guide/audience/segments/segment_extension) erstellen, um Nutzer:innen zu analysieren, die den Canvas betreten, aber die erwartete Nachricht nicht erhalten haben.

### Warum zeigt das Dashboard einen Rate-Limit-Fehler für meine Campaign an? {#why-does-the-dashboard-show-a-rate-limit-error-for-my-campaign}

Das bedeutet in der Regel, dass das [Rate-Limit für die Zustellgeschwindigkeit](#delivery-speed-rate-limiting) der Campaign für die Zielgruppengröße zu niedrig eingestellt ist. In diesem Fall würde der Versand länger dauern als das zulässige Zeitfenster, und Braze gibt eine Warnung aus. Erhöhen Sie das Rate-Limit für die Zustellgeschwindigkeit, verkleinern Sie die Zielgruppe oder verwenden Sie **Sendevolumen begrenzen**, damit jeder geplante Versanddurchlauf innerhalb des zulässigen Sendefensters abgeschlossen wird. Sie können auch ein [Workspace-Messaging-Rate-Limit]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) festlegen, um eine Obergrenze über Campaigns hinweg durchzusetzen.

**Sendevolumen begrenzen** steuert, wie viele Nutzer:innen für einen Versand berechtigt sind – nicht, wie viele Nachrichten Braze pro Minute sendet. Nur ein Rate-Limit für die Zustellgeschwindigkeit legt den Durchsatz pro Minute fest.

Wenn Sie bereits das maximale Rate-Limit für die Zustellgeschwindigkeit erreicht haben, das für Ihr Unternehmen verfügbar ist, wenden Sie sich an Ihre:n Customer-Success-Manager, um eine Erhöhung anzufordern.

### Was bedeutet „Gesendet“ beim Frequency-Capping? {#what-does-sent-mean-for-frequency-capping}

In Analytics und beim Frequency-Capping bezieht sich *Gesendet* auf den Zeitpunkt, an dem Braze die Nachricht versendet (der Versand wird erfasst) – nicht auf die garantierte endgültige Zustellung an das Gerät oder den Posteingang. Frequency-Capping und Sendezähler verwenden diese erfassten Sendeereignisse, die von nachgelagerten „Zugestellt“-Metriken abweichen können.

### Warum sehe ich E-Mail-Bounces oder -Zurückstellungen? {#why-am-i-seeing-email-bounces-or-deferrals}

E-Mail-Bounce- und Zurückstellungsnachrichten verwenden viele verschiedene Codes und anbieterspezifische Texte. Betrachten Sie einen bestimmten Code nicht als Zeichen für ein Rate-Limiting-Problem, da die Ursache von Ihrem Sendekontext und dem Feedback des Postfachanbieters abhängt.

Wenn Nachrichten vorübergehend zurückgestellt werden, kann ein geringeres Sendevolumen kurzfristig helfen. Verwenden Sie ein [Rate-Limit für die Zustellgeschwindigkeit](#delivery-speed-rate-limiting), **Sendevolumen begrenzen** oder beides.

Arbeiten Sie für eine langfristige Lösung mit einem Zustellbarkeitsexperten zusammen, um Ihre Bounce- und Zurückstellungsdaten zu überprüfen.