---
nav_title: Best Practices
article_title: Best Practices für Kampagnen
page_order: 0
description: "Dieser Artikel enthält Best Practices für die Erstellung und Anpassung Ihrer Kampagnen."
tool: Campaign

---

# Best Practices für Kampagnen

## Die vier T's von Braze

Braze empfiehlt, nur Kundendaten zu senden, die Sie tatsächlich auf der Braze-Plattform nutzen möchten. Orientieren Sie sich an der Philosophie der „Vier T's von Braze", um sicherzustellen, dass Sie nur Daten senden, die Sie für folgende Zwecke verwenden:

- **Target** – Ihre Zielgruppen durch die Erstellung von [Zielgruppen-Segmenten]({{site.baseurl}}/user_guide/audience/segments/) ansprechen.
- **Trigger** – Ihre Nachrichten mit [aktionsbasierter]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#action-based-delivery) oder [API-getriggerter]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) Zustellung triggern.
- **Template** – Ihre Nachrichten mit [bedingter Liquid-Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) gestalten und personalisieren.
- **Track** – Die Wirksamkeit Ihrer Kampagnen mit [Conversion-Tracking]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/) verfolgen.

So können Sie die Daten optimieren, die Sie an Braze senden, und Ihre Fähigkeit verbessern, Ihre Nutzer:innen zu erreichen – und gleichzeitig vermeiden, Datenpunkte zu tracken, die Ihr Team langfristig möglicherweise nicht als hilfreich erachtet.

## Nutzer-Targeting

Wenn Sie Ihre Kampagnen im Laufe der Zeit ausbauen, können Lücken in Ihrer Zielgruppe auftreten. An diesem entscheidenden Punkt können Sie Ihre [passiven Nutzer:innen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/capturing_lapsing_users/) mit einer spezialisierten Kampagne mithilfe von Segmentierung ansprechen.

### Identifizieren Sie Ihre Zielgruppe

Nutzen Sie Segmente und Filter zu Ihrem Vorteil, indem Sie Ihre Zielgruppe definieren. Überlegen Sie, wen Ihre Kampagne und Nachrichten ansprechen sollen. Mit diesen wichtigen Informationen können Sie [Multichannel-Kampagnen]({{site.baseurl}}/user_guide/messaging/campaigns/faq#how-do-you-create-a-multichannel-campaign) erstellen, die Ihnen die Flexibilität bieten, Ihre Nachrichten in verschiedenen Kanälen zu gestalten, um den Präferenzen für Benachrichtigungen Ihrer Zielgruppe zu entsprechen.

Es ist außerdem wichtig, Ihre [aktiven Nutzer:innen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns/) zu verstehen, um Ihren treuen Nutzer:innen Ihre Wertschätzung zu zeigen.

## Multichannel-Kampagnen

### Feature-Awareness

Wenn Ihr Ziel darin besteht, Ihre Nutzer:innen auf ein neues Feature oder eine neue App-Version aufmerksam zu machen, verwenden Sie eine Multichannel-Strategie mit Fokus auf In-App-Kanäle. [In-App-Nachrichten]({{site.baseurl}}/in-app_messages/) und [Content-Cards]({{site.baseurl}}/user_guide/channels/content_cards/) sind in der Regel weniger störend, wenn Nutzer:innen nicht sofort aktualisieren möchten.

Stellen Sie sicher, dass Sie [Deeplinks]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) zum entsprechenden App Store einfügen.

Es kann schwierig sein, Nutzer:innen davon zu überzeugen, ihre App zu aktualisieren oder die Art und Weise zu ändern, wie sie Ihre App nutzen. Informieren Sie sie daher über alle Vorteile der neuen Version oder der neuen Features und darüber, wie sich ihr Erlebnis mit Ihrer App dadurch verbessert.

### Sendezeitpunkt

Timing ist entscheidend! Wenn Ihr Ziel darin besteht, Nutzer:innen zu einem App-Update zu bewegen, warten Sie, bis sie eine positive Erfahrung innerhalb der App gemacht haben, bevor Sie sie darum bitten. Um Ihre Zielgruppe bei der Stange zu halten, vermeiden Sie wiederholtes Messaging, das aufdringlich wirken könnte.

Im Laufe der Zeit können Ihre Nutzer:innen bestimmte Features vergessen oder neue Features nicht bemerken. Wenn neue Features hinzugefügt werden, informieren Sie Ihre Nutzer:innen mit [In-App-Nachrichten]({{site.baseurl}}/in-app_messages/). Wenn Nutzer:innen wichtige Features innerhalb der App nicht nutzen, kann es sinnvoll sein, sie daran zu erinnern, wenn sie die App aktiv verwenden und das neue Feature nützlich wäre. Unser Artikel zum [Daten-Opt-in]({{site.baseurl}}/user_guide/channels/content_cards/) enthält weitere Informationen dazu, wie Sie sicherstellen, dass Ihre Anfrage den Workflow-Erwartungen der Nutzer:innen entspricht.

## Hohe Bewertungen

Fünf-Sterne-Bewertungen im App Store stehen auf der Wunschliste jedes Mobile-Marketers. Positive Bewertungen zu erhalten, ist jedoch keine leichte Aufgabe, da es zusätzlichen Aufwand von Ihren Nutzer:innen erfordert. Durch den cleveren Einsatz unserer Funktionalitäten können wir Ihnen helfen, Ihr Customer-Engagement zu steigern.

### Power-User ansprechen

Power-User können Fürsprecher für Ihre App sein. Oft interagieren sie regelmäßig mit Ihrer App und können wertvolles Feedback zur Verbesserung geben. Obwohl sie sich von App zu App unterscheiden, haben Power-User in der Regel folgende Eigenschaften:

- Viele Sessions protokolliert
- Die App kürzlich genutzt
- Geld ausgegeben und Käufe getätigt

Um höhere Bewertungen zu erzielen, bitten Sie Ihre Power-User, Ihre App im App Store zu bewerten, da sie eher Positives zu berichten haben. Sie könnten beispielsweise ein Segment namens „Power-User" mit folgenden Filtern erstellen:
- Hat diese Apps in den letzten 14 Tagen mehr als 10 Mal genutzt
- Hat mehr als 50 Dollar ausgegeben

![Ein Beispiel für ein Segment, das Power-User einer App anspricht.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Der Besuch des App Stores kostet Ihre Nutzer:innen Zeit. Um die Wahrscheinlichkeit zu maximieren, dass sie den zusätzlichen Aufwand auf sich nehmen, bitten Sie um eine Bewertung, nachdem sie gerade eine positive Erfahrung mit Ihrer App gemacht haben. Fragen Sie sie beispielsweise, nachdem sie ein Spiellevel geschafft oder einen Kauf mit einem Rabattcode getätigt haben. Unser Artikel zum [Daten-Opt-in]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) enthält weitere Informationen dazu, wie Sie sicherstellen, dass Ihre Anfrage den Workflow-Erwartungen der Nutzer:innen entspricht.

## Zeitplanung Ihrer Kampagnen

Beachten Sie beim Bearbeiten von Kampagnen-Zeitplänen oder Zielgruppen die folgenden Best Practices:

- **Einmalig geplante Kampagnen:** Sie können die Kampagne bis zum geplanten Sendezeitpunkt bearbeiten.
- **Wiederkehrend geplante Kampagnen:** Sie können die Kampagne bis zum geplanten Sendezeitpunkt bearbeiten.
- **Kampagnen mit lokaler Sendezeit:** Nehmen Sie keine Änderungen 24 Stunden vor dem geplanten Sendezeitpunkt vor.
- **Kampagnen mit optimaler Sendezeit:** Nehmen Sie keine Änderungen 24 Stunden vor Mitternacht des Tages vor, an dem die Kampagne gesendet werden soll.

{% alert note %}
Wenn Sie eine laufende Kampagne bearbeiten und die Zustellung auf **Lokale Sendezeit** ändern, wird ein neuer Batch von Nachrichten in die Warteschlange gestellt. Das bedeutet, dass Ihre Nutzer:innen die Nachricht zweimal erhalten, da die Nachricht doppelt in die Warteschlange eingereiht wird. Um dies zu verhindern, stoppen Sie zuerst die ursprüngliche Kampagne und starten Sie dann ein Duplikat, nachdem Sie den Zeitplan aktualisiert haben.
{% endalert %}