---
nav_title: Anwendungsfall
article_title: "Anwendungsfall: Prognose für Abonnement-Upgrades"
description: "Dieses Beispiel veranschaulicht, wie eine fiktive Marke Braze Predictive Events einsetzt, um die für ihr Geschäft relevanten Ergebnisse zu definieren – wie beispielsweise das Upgraden auf eine Pro-Mitgliedschaft – und gezielte Strategien zu entwickeln, die die Ergebnisse verbessern."
page_type: tutorial
---

# Anwendungsfall: Abonnement-Upgrades mit intelligenterem Targeting prognostizieren {#use-case-predict-subscription-upgrades-with-smarter-targeting}

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke Braze Predictive Events einsetzt, um die für ihr Geschäft relevanten Ergebnisse zu definieren – wie beispielsweise das Upgraden auf eine Pro-Mitgliedschaft – und gezielte Strategien zu entwickeln, die die Ergebnisse verbessern.

Nehmen wir an, Jordan ist Lifecycle-Strateg:in bei Steppington, einer Gesundheits- und Fitness-App mit kostenlosen und kostenpflichtigen Angeboten. Das Team von Jordan hat sich zum Ziel gesetzt, die Anzahl der Pro-Upgrades zu erhöhen, ohne die gesamte kostenlose Nutzerbasis mit Rabattnachrichten zu überfluten. Derzeit versenden sie nach sieben Tagen eine Werbeaktion mit dem Titel „Pro mit 50 % Rabatt testen“ an alle Nutzer:innen der kostenlosen Version. Das führt zwar zu einigen Conversions (etwa 5 % über 7 Tage), jedoch auch zu übermäßiger Ansprache – einschließlich der Rabattierung von Nutzer:innen, die wahrscheinlich ohnehin upgradet hätten.

Um das Targeting zu verbessern und die Messaging-Ermüdung zu reduzieren, verwendet Jordan Predictive Events, um die Wahrscheinlichkeit zu modellieren, dass Nutzer:innen innerhalb der nächsten 7 Tage auf Pro upgraden. Er definiert ein angepasstes Event: `upgraded_to_pro` und nutzt dieses anschließend, um ein Prognosemodell zu trainieren und die Nutzer:innen in intelligente, handlungsorientierte Gruppen zu segmentieren.

Dieses Tutorial führt Sie durch den Prozess, den Jordan durchlaufen hat:

- Ein Prognosemodell für `upgraded_to_pro` innerhalb von 7 Tagen
- Segmente, die dazu beitragen, die Conversions zu erhöhen und gleichzeitig weniger Nachrichten insgesamt zu versenden

## Schritt 1: Ein Prognosemodell für Upgrades erstellen {#step-1-create-a-predictive-model-for-upgrades}

Jordan beginnt damit, das für seine Upgrade-Strategie wichtigste Ergebnis zu definieren: Nutzer:innen, die von der kostenlosen Version zur Pro-Version wechseln. Anstatt sich auf allgemeine Auslöser wie „Zeit seit der Anmeldung“ zu verlassen, möchte er prognostizieren, welche Nutzer:innen tatsächlich wahrscheinlich konvertieren werden. Auf diese Weise kann sein Team auf echte Signale reagieren und nicht nur auf Annahmen.

1. Im Braze-Dashboard navigiert Jordan zu **Analytics** > **Predictive Events**.
2. Er [erstellt eine neue Event-Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction) und benennt sie „Upgrade auf Pro in 7 Tagen“.
3. Als Ziel-Event wählt er sein angepasstes Event aus: `upgraded_to_pro`.
4. Jordan legt das Prognosefenster auf 7 Tage fest, erstellt einen Update-Zeitplan und erstellt die Prognose.

![Prognoseeinstellungen mit der Definition, dem Fenster, der Zielgruppe und dem Update-Zeitplan für die Prognose.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Schritt 2: Nutzer:innen anhand der Upgrade-Wahrscheinlichkeit segmentieren {#step-2-segment-users-based-on-upgrade-probability}

Nach Abschluss des Trainings weist Braze jeder berechtigten Nutzer:in einen [Event Likelihood Score]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics#purchase_score) (0–100) zu. Jordan nutzt diesen Score, um umsetzbare Segmente zu erstellen – eines für Nutzer:innen mit hoher Kaufabsicht, die möglicherweise keinen Rabatt benötigen, und ein weiteres für Nutzer:innen, die ohne Unterstützung wahrscheinlich nicht konvertieren werden.

1. Jordan navigiert zu Segments in Braze.
2. Er erstellt zwei [Segmente]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mithilfe des [Filters „Event Likelihood Score“]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#event-likelihood-score) und wählt die von ihm erstellte Prognose aus. Die beiden Segmente sind:
  - **Wahrscheinliches Upgrade:** Score mehr als 70
  - **Braucht Anstoß zum Upgrade:** Score mehr als 40 und weniger als 70

{% alert tip %}
Prädiktive Filter können mit beliebigen anderen Attributen oder Verhaltensweisen von Nutzer:innen kombiniert werden. Jordan plant, diese Segmente auf Grundlage der Nutzerinteressen weiter zu verfeinern – beispielsweise durch die Priorisierung von Nutzer:innen, die häufig Fitness-Tracking-Features verwenden. Dadurch erhält er vier Untergruppen, die er gezielter ansprechen kann, sodass Inhalte und Messaging auf die Bedürfnisse jeder Nutzer:in abgestimmt werden können.
{% endalert %}

![Segment-Builder mit zwei Filtern für den Event Likelihood Score.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Schritt 3: Messaging nach Absichtsstufe personalisieren {#step-3-personalize-messaging-by-intent-level}

Da Jordan nun eindeutige Signale für die Upgrade-Absicht hat und die Untergruppen auf der Grundlage des Nutzerverhaltens verfeinert hat, entwickelt er eine Messaging-Strategie, die sich an die Bedürfnisse jeder Nutzer:in anpasst. Keine pauschalen Nachrichten mehr.

Er wählt E-Mail als primären Kanal für diese Campaign. Warum? Weil Jordan den Wert von Pro für Nutzer:innen mit hoher Kaufabsicht erläutern und überzeugende Argumente für eher zögerliche Nutzer:innen liefern möchte – für beides sind Platz, visuelle Elemente und ein aussagekräftiger CTA erforderlich. E-Mails bieten ihm die Flexibilität, dies effektiv zu tun, ohne die Nutzer:innen unter Druck zu setzen, und ermöglichen es ihm, die Performance anhand des Klickverhaltens zu verfolgen.

Jordan [erstellt ein Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas), das die Erfahrung auf der Grundlage der von ihm erstellten Segmente aufteilt. Er fügt einen Zielgruppenpfade-Schritt hinzu, um folgende Gruppen anzusprechen:

- Hohe Absicht, Fitness-fokussierte Nutzer:innen
- Hohe Absicht, andere Nutzer:innen
- Geringe Absicht, Fitness-fokussierte Nutzer:innen
- Geringe Absicht, andere Nutzer:innen

![Canvas-Zielgruppenpfad mit vier Pfaden für jeden Absichtstyp.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Er legt außerdem das Canvas-Konversions-Event als angepasstes Event `upgraded_to_pro` fest, sodass Braze die Upgrade-Conversions automatisch verfolgt, während die Nutzer:innen den Ablauf durchlaufen.

### Beispielnachrichten pro Pfad {#example-messages-per-path}

{% tabs %}
{% tab High intent, fitness %}

Diese Nutzer:innen sind bereits aktiv und nutzen die Fitness-Tracking-Features intensiv. Es ist wahrscheinlich, dass sie ohne zusätzliche Anreize upgraden werden. Daher konzentriert sich die Nachricht darauf, tiefere Insights und fortschrittliche Tools zu erschließen, die auf ihren bestehenden Gewohnheiten aufbauen.

- **Betreffzeile:** Erreichen Sie mehr mit Ihren Fitnesszielen
- **Überschrift:** Ihr Fortschritt verdient Pro
- **Text:** Sie haben bereits eine solide Routine aufgebaut. Mit Pro können Sie noch tiefer gehen – verfolgen Sie Ihre Fortschritte über verschiedene Muskelgruppen hinweg, legen Sie wöchentliche Performance-Ziele fest und erschließen Sie sich erweiterte Analytics, die auf Ihre Bewegungsabläufe zugeschnitten sind.
- **CTA:** Starten Sie Ihre kostenlose Pro-Testversion

{% endtab %}
{% tab High intent, other %}
Diese Nutzer:innen zeigen deutliche Anzeichen für ein starkes Engagement – beispielsweise durch das Durchsuchen der Pro-Features oder häufige App-Aktivitäten –, konzentrieren sich jedoch nicht speziell auf das Fitness-Tracking. Die Nachricht hebt die umfassenderen Vorteile von Pro hervor, wie Coaching und Personalisierung, um sie zum Upgrade zu bewegen.

- **Betreffzeile:** Sie sind fast am Ziel – Pro ist bereit, wenn Sie es sind
- **Überschrift:** Entdecken Sie weitere Möglichkeiten, sich zu bewegen
- **Text:** Sie haben sich mit den Funktionen von Pro vertraut gemacht. Dies ist Ihre Gelegenheit, auf angepasste Pläne, 1:1-Coaching-Inhalte und geführte Programme zuzugreifen, die auf Ihre individuellen Ziele zugeschnitten sind – sei es Kraft, Gleichgewicht oder Beständigkeit.
- **CTA:** Starten Sie Ihre kostenlose Pro-Testversion

{% endtab %}
{% tab Low intent, fitness %}
Diese Nutzer:innen beschäftigen sich gelegentlich mit Fitness-Features, haben jedoch noch keine Schritte in Richtung Upgrade unternommen. Die Nachricht spricht ihr Interesse an Fitness an und reduziert gleichzeitig die Hemmschwelle durch ein zeitlich begrenztes Angebot – so wird Pro zu einer risikoarmen Möglichkeit, ihre Routine zu verbessern.

- **Betreffzeile:** Bereit, intelligenter zu trainieren? Testen Sie Pro mit 50 % Rabatt
- **Überschrift:** Ihr Workout-Upgrade wartet auf Sie
- **Text:** Pro bietet Ihnen alles, was Sie für einen erfolgreichen Start benötigen – leicht verständliche Trainingspläne, Expertentipps und zuverlässiges Fortschritts-Tracking. Testen Sie es jetzt mit 50 % Rabatt und kündigen Sie jederzeit.
- **CTA:** 50 % Rabatt auf Pro sichern

{% endtab %}
{% tab Low intent, other %}

Diese Nutzer:innen zeigen insgesamt nur ein geringes Engagement. Ohne einen überzeugenden Anreiz ist es unwahrscheinlich, dass sie upgraden. Daher verfolgt die Nachricht einen einfachen, vorteilsorientierten Ansatz mit einem Rabatt und einer freundlichen Sprache, um ohne Druck zum Ausprobieren einzuladen.

- **Betreffzeile:** 50 % Rabatt auf Pro – nur an diesem Wochenende
- **Überschrift:** Bereit, wenn Sie es sind
- **Text:** Erstellen Sie Ihren ersten personalisierten Fitnessplan, verfolgen Sie Ihre Fortschritte und greifen Sie auf exklusive Workouts zu – und das alles zum halben Preis. Testen Sie Pro zu einem reduzierten Preis und kündigen Sie jederzeit.
- **CTA:** 50 % Rabatt auf Pro sichern

{% endtab %}
{% endtabs %}

## Schritt 4: Ergebnisse messen und Strategie optimieren {#step-4-measure-results-and-optimize-your-strategy}

Nach Abschluss der Campaign überprüft Jordan die Performance in [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics), um zu ermitteln, wie erfolgreich die personalisierten Pfade waren – und ob die Kombination aus prädiktiver Absicht und Verhaltenssignalen die Upgrade-Raten verbessert hat.

E-Mail-Performance nach Pfad:

- **Hohe Absicht, Fitness**
   - *Öffnungsrate:* 34 %
   - *Klickrate:* 20 %
   - *Konversionsrate:* 13 %
   - Kein Rabatt verwendet
- **Hohe Absicht, Sonstiges**
   - *Öffnungsrate:* 30 %
   - *Klickrate:* 17 %
   - *Konversionsrate:* 11 %
   - Kein Rabatt verwendet
- **Geringe Absicht, Fitness**
   - *Öffnungsrate:* 27 %
   - *Klickrate:* 12 %
   - *Konversionsrate:* 8 %
   - 50 % Rabatt enthalten
- **Geringe Absicht, Sonstiges**
   - *Öffnungsrate:* 23 %
   - *Klickrate:* 9 %
   - *Konversionsrate:* 6 %
   - 50 % Rabatt enthalten

Im Vergleich zur vorherigen einheitlichen Campaign des Teams (bei der ein pauschaler Rabatt nach 7 Tagen zu nur 5 % Conversions und übermäßigem Messaging führte) zeigt der zielgerichtete Ansatz eine deutliche Steigerung in allen Gruppen, mit verbesserter Effizienz und weniger unnötigen Rabatten.

Der [Funnel-Bericht]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) zeigt auch einen deutlichen Rückgang der Abbrüche in wichtigen Schritten, insbesondere bei Nutzer:innen mit geringer Kaufabsicht, die personalisiertes Messaging erhalten haben. Immer mehr Nutzer:innen öffnen, klicken und upgraden – ein Beweis für den Wert des absichtsbasierten Targetings.

Jordan nutzt diese Insights, um:

- A/B-Tests zu Betreffzeilen und CTA-Formulierungen durchzuführen
- Die Rabattschwelle für Nutzer:innen mit mittlerer Kaufabsicht neu zu bewerten
- Die Segmente auf der Grundlage zusätzlicher Verhaltensweisen wie Inhaltsaufrufe oder Nutzung von App-Features weiter zu verfeinern

Dank Predictive Events und mehrstufiger Segmentierung verfügt sein Team nun über eine skalierbare Strategie, die das Messaging an die Absichten und das Verhalten der Nutzer:innen anpasst – und so mehr Upgrades generiert, während das Vertrauen in die Marke gewahrt bleibt.