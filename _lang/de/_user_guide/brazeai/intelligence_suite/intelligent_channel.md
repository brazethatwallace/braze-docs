---
nav_title: Kanalfilter
article_title: Intelligenter Kanalfilter
page_order: 1.5
description: "Dieser Artikel behandelt den intelligenten Kanalfilter, einen Filter, der den Teil Ihrer Zielgruppe auswählt, für den der ausgewählte Messaging-Kanal der beste Kanal ist. In diesem Fall bedeutet „am besten“ die höchste Wahrscheinlichkeit für ein Engagement angesichts des Verlaufs der Nutzer:innen."
search_rank: 11
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligenter Kanalfilter {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommost-engaged-channel-stylefloatrightwidth120pxborder0-classnoimgborderintelligent-channel-filter}

> Der Filter `Intelligent Channel` (zuvor `Most Engaged`) wählt den Teil Ihrer Zielgruppe aus, für den der ausgewählte Messaging-Kanal der „beste“ Kanal ist.

## Über den Filter {#about-the-filter}

![Der intelligente Kanalfilter mit einem Dropdown-Menü für die verschiedenen Kanäle, die ausgewählt werden können.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

In diesem Fall bedeutet „am besten“ den Kanal, der angesichts des Verlaufs der Nutzer:innen die höchste Wahrscheinlichkeit für ein Engagement aufweist. Sie können E-Mail, Kurzmitteilungsdienst or SMS, WhatsApp, Web-Push oder Mobile-Push (einschließlich aller verfügbaren mobilen Betriebssysteme oder Geräte) als Kanal auswählen.

Der intelligente Kanal berechnet eine Engagement-Rate für alle Nutzer:innen auf jedem unterstützten Kanal, ordnet diese Kanäle nach Rang und behandelt den am höchsten bewerteten Kanal als den besten Kanal dieser:dieses Nutzer:in.

Um den intelligenten Kanalfilter zu aktivieren, wählen Sie den Filter **Intelligent Channel** auf der Seite **Target Audiences** aus, wenn Sie eine Campaign oder ein Canvas erstellen.

## Wie das Engagement pro Kanal berechnet wird {#how-engagement-is-calculated-by-channel}

Der intelligente Kanal vergleicht Kanäle anhand einer Engagement-Rate: die Anzahl der Nachrichteninteraktionen geteilt durch die Anzahl der empfangenen Nachrichten. Braze wertet bis zu die letzten 100 empfangenen Nachrichten pro Kanal innerhalb der letzten sechs Monate aus.

Jedes Mal, wenn eine Nachricht an eine:n Nutzer:in gesendet wird oder ein:e Nutzer:in mit einer Nachricht interagiert, wird die Engagement-Rate innerhalb von Sekunden neu berechnet. Ein:e Nutzer:in kann nur einmal als mit einer Nachricht interagierend gezählt werden (z. B. wird eine Öffnung und ein Klick auf dieselbe E-Mail als einmaliges Engagement gewertet, nicht zweimal).

### Interaktionsdaten nach Kanal {#interaction-data-by-channel}

Braze erfasst die folgenden Ereignisse bei der Berechnung der Engagement-Raten:

- **E-Mail:** Öffnungen ([maschinelle Öffnungen]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) ausgenommen). E-Mail-Klicks werden nicht berücksichtigt.
- **Mobile-Push:** Direkte Öffnungen. Jede mobile Plattform (z. B. iOS, Android und Kindle) wird separat bewertet. Push-beeinflusste Öffnungen werden nicht berücksichtigt.
- **Web-Push:** Öffnungen
- **Kurzmitteilungsdienst or SMS:** Klicks auf verkürzte Links
- **WhatsApp:** Nachrichtenlesungen oder Klicks auf getrackte Links

Push-beeinflusste Öffnungen, E-Mail-Klicks und Sitzungsaktivitäten werden vom intelligenten Kanal nicht verwendet. Sitzungsaktivitäten werden von [intelligentem Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#about-intelligent-timing) genutzt.

Der intelligente Kanal unterstützt keine Webhooks, LINE, Kakao Talk, In-App Messages oder Content Cards.

{% alert important %}
Um die Engagement-Rate des Kurzmitteilungsdienst or SMS-Kanals zu berechnen, schalten Sie die [Kurzmitteilungsdienst or SMS-Linkverkürzung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) mit erweitertem Tracking und Klick-Tracking ein. Ohne dieses Tracking kann Kurzmitteilungsdienst or SMS als intelligenter Kanal mit einer Engagement-Rate von 0 % ausgewählt werden, da unser [Tie-Break-Verhalten]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel#tie-breaking) greift.
{% endalert %}

## Nicht genügend Daten {#not-enough-data}

Damit Braze feststellen kann, welcher Kanal der „beste“ ist, müssen genügend Daten vorhanden sein. Das bedeutet, dass ein:e Nutzer:in mindestens drei oder mehr Nachrichten auf einem Kanal erhalten haben muss, bevor dieser Kanal bewertet werden kann, und über ausreichende Daten auf mindestens zwei unterstützten Kanälen verfügen muss.

Wenn Nutzer:innen nicht genügend Nachrichten über die Kanäle erhalten haben, fallen sie unter die Option „Nicht genügend Daten“ dieses Filters. So können Sie jeden unterstützten Messaging-Kanal nutzen, um diese Nutzer:innen anzusprechen.

Nehmen wir an, Sie möchten, dass Nutzer:innen, die Push-Nachrichten bevorzugen, eine Push-Nachricht erhalten und Nutzer:innen, die nicht über genügend Daten verfügen, dieselbe Push-Nachricht erhalten. In diesem Fall könnten Sie den intelligenten Kanalfilter auf **Mobile-Push** einstellen und mit **ODER** einen zweiten intelligenten Kanalfilter hinzufügen, der auf **Nicht genügend Daten** eingestellt ist. Mit einer separaten Campaign, bei der der intelligente Kanalfilter auf E-Mail eingestellt ist, können Sie Nutzer:innen ansprechen, die E-Mail bevorzugen.

![Intelligente Kanalfilter für Mobile-Push oder nicht genügend Daten.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Campaigns und Canvas-Schritte, die das [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules) ignorieren, werden vom intelligenten Kanal nicht berücksichtigt und können nicht zu den Datenanforderungen beitragen.
{% endalert %}

## Mobile-Push {#mobile-push}

Mobile-Push umfasst Android, iOS, Kindle und andere Kanäle für mobile Geräte, die auf Braze verfügbar sind. Braze bewertet jede mobile Plattform separat bei der Berechnung der Engagement-Raten.

Wenn Sie den intelligenten Kanalfilter auf **Mobile-Push** einstellen, wird ein:e Nutzer:in zugeordnet, wenn entweder iOS-Push oder Android-Push der am höchsten bewertete Kanal ist. Dies zwingt die:den Nutzer:in nicht dazu, Push-Benachrichtigungen auf einem bestimmten Gerät zu empfangen. Das Ranking wird nur verwendet, um festzustellen, ob Mobile-Push der beste Kanal dieser:dieses Nutzer:in im Vergleich zu E-Mail, Web-Push, Kurzmitteilungsdienst or SMS und WhatsApp ist.

## Filter für die Wahrscheinlichkeit der Nachrichtenöffnung für einzelne Kanäle {#individual-channels}

Anstatt Braze den besten Kanal für eine:n Nutzer:in auswählen zu lassen, können Sie den [Segmentierungsfilter „Wahrscheinlichkeit der Nachrichtenöffnung“]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#message-open-likelihood) verwenden, um Nutzer:innen danach zu filtern, ob sie eine Nachricht auf einem von Ihnen ausgewählten Kanal wahrscheinlich öffnen werden oder nicht. Dieser Filter wird berechnet, indem der Prozentsatz der Interaktionen durch die Gesamtzahl der empfangenen Nachrichten der letzten 100 pro Kanal gesendeten Nachrichten dividiert wird.

Die Wahrscheinlichkeit der Nachrichtenöffnung verwendet dieselben zugrunde liegenden Engagement-Daten wie der intelligente Kanal, ermöglicht es Ihnen jedoch, einen Schwellenwert für einen einzelnen Kanal festzulegen, anstatt den besten Kanal der Nutzer:innen auszuwählen. Dieser Filter ist für E-Mail, Mobile-Push, Kurzmitteilungsdienst or SMS und Web-Push verfügbar.

Bitte beachten Sie, dass ein:e Nutzer:in mindestens drei Nachrichten auf einem bestimmten Kanal erhalten haben muss, bevor eine Wahrscheinlichkeitsbewertung für diesen Kanal vergeben werden kann. Nutzer:innen ohne ausreichende Daten, um eine Wahrscheinlichkeit für einen Kanal zu messen, können mit „ist leer“ ausgewählt werden.

## Best Practices und effektive Nutzungsstrategie {#best-practices-and-effective-use-strategy}

### Tie-Break {#tie-breaking}

Da einige Nutzer:innen nur wenige Nachrichten erhalten, ist es nicht ungewöhnlich, dass die Engagement-Raten für eine:n bestimmte:n Nutzer:in über die verfügbaren Kanäle hinweg gleich sind (z. B. hat ein:e Nutzer:in eine Engagement-Rate von 20 % sowohl für E-Mail als auch für Mobile-Push). In solchen Fällen werden Gleichstände aufgelöst, indem der Kanal mit den zuletzt erfolgten Interaktions-Events bevorzugt (höher bewertet) wird.

Wenn gleichstehende Kanäle beide eine Engagement-Rate von 0 % aufweisen, löst Braze den Gleichstand anhand des Kanals mit der zuletzt empfangenen Nachricht auf.

### Nicht erreichbare Kanäle {#unreachable-channels}

Ein:e Nutzer:in kann über genügend Daten verfügen, damit Braze ein Kanal-Ranking erstellen kann, ist dann aber auf dem am höchsten bewerteten Kanal nicht mehr erreichbar. Beispielsweise könnte ein:e Nutzer:in, deren:dessen historisch bester Kanal E-Mail ist, sich kürzlich von E-Mails abgemeldet haben. Wenn Sie eine Nachricht über diesen Kanal senden, wird sie nicht an diese:n Nutzer:in zugestellt. Nutzer:innen, die auf bestimmten Kanälen nicht erreichbar sind, sollten gesondert angesprochen oder weitergeleitet werden.

### Größe der Zielgruppe {#audience-sizing}

Mit dem intelligenten Kanal können Sie im Voraus gezielt den Teil der Nutzer:innen ansprechen, bei dem die Wahrscheinlichkeit, dass sie sich mit einer Nachricht beschäftigen, wesentlich höher ist als beim Representational State Transfer Ihrer Zielgruppe. Dies entspricht wahrscheinlich nicht der Mehrheit der Nutzer:innen in einer typischen Zielgruppe. Vielmehr können Sie davon ausgehen, dass dieser Filter die 5–20 % Ihrer üblichen Zielgruppe findet, die sich nachweislich auf einem bestimmten Kanal engagiert haben.