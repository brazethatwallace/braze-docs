---
nav_title: Anwendungsfall
article_title: "Anwendungsfall: Churn durch zeitnahe Inhalte verringern"
description: "Dieses Beispiel veranschaulicht, wie eine fiktive Marke Predictive Churn einsetzt, um proaktiv die Abwanderung von Nutzer:innen zu reduzieren."
page_type: tutorial
---

# Anwendungsfall: Churn durch zeitnahe erneute Interaktion mit Inhalten verringern {#use-case-reduce-churn-with-timely-content-re-engagement}

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke Predictive Churn einsetzt, um proaktiv die Abwanderung von Nutzer:innen zu reduzieren. Anstatt abzuwarten, bis es zu Abwanderungen kommt, sollten Sie vorhersagen, welche Nutzer:innen gefährdet sind, und ihnen maßgeschneiderte Nachrichten zukommen lassen, solange sie noch aktiv sind.

Nehmen wir an, Camila ist CRM-Manager:in bei MovieCanon, einer Streaming-Plattform für Independent-Filme, Dokumentationen und internationale Serien.

Das Team von Camila hat einen besorgniserregenden Trend festgestellt: Nutzer:innen führen eine Registrierung durch, streamen ein oder zwei Filme und verschwinden dann. In der Vergangenheit wurde versucht, eine Woche später eine allgemeine E-Mail mit dem Inhalt „Wir vermissen Sie“ zu versenden – jedoch mit einer Konversionsrate von nur 3 % war dies unzureichend und kam zu spät. Die meisten Nutzer:innen interagieren nicht erneut, und die Abwanderung wird unvermeidlich.

Camila möchte dies ändern. Anstatt auf Churn zu reagieren, nachdem er bereits eingetreten ist, nutzt sie Predictive Churn, um Nutzer:innen zu identifizieren, die innerhalb der nächsten 14 Tage wahrscheinlich inaktiv werden – so hat ihr Team die Möglichkeit zu einer erneuten Interaktion mit diesen Personen, solange sie noch aktiv sind.

Dieses Tutorial führt Sie durch die Vorgehensweise von Camila:

- Erstellen eines Modells zur Churn-Prognose auf Grundlage des Nutzerverhaltens
- Segmentieren von Nutzer:innen nach Risikostufe
- Entwickeln einer Campaign zur erneuten Interaktion, die auf die am stärksten gefährdeten Personen zugeschnitten ist
- Bewerten der Auswirkungen mithilfe von Campaign-Analytics

## 1. Schritt: Erstellen Sie ein Modell zur Churn-Prognose {#step-1-create-a-churn-prediction-model}

Camila beginnt damit, das Ergebnis zu modellieren, das sie vermeiden möchte: dass Nutzer:innen inaktiv werden. Für MovieCanon bedeutet Churn, dass innerhalb von 14 Tagen kein Stream gestartet wird – dies ist das Verhalten, das sie vorhersagen möchte.

1. Im Braze-Dashboard navigiert Camila zu **Analytics** > **Predictive Churn**.
2. Sie erstellt eine neue Churn-Prognose und benennt sie „Churn-Risiko in zwei Wochen“.
3. Um die Abwanderung zu definieren, wählt sie `do not` und das angepasste Event `stream_started`, das aktives Engagement anzeigt.
4. Sie legt das Prognosefenster auf 14 Tage fest – das bedeutet, dass das Modell Nutzer:innen identifiziert, die wahrscheinlich 14 Tage lang keinen neuen Stream starten werden.

![Churn-Definition, wobei Churn als Nutzer:in definiert ist, die in den letzten 14 Tagen das angepasste Event „stream_started“ nicht durchgeführt hat.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5. Sie wählt eine Prognosegruppe aus, die alle Nutzer:innen umfasst, die in den letzten 30 Tagen relevante Events ausgelöst haben – sodass das Modell über ausreichend aktuelle Verhaltensdaten verfügt, um daraus zu lernen.
6. Sie stellt den Zeitplan für die Prognose-Updates auf wöchentlich ein, damit die Ergebnisse aktuell bleiben.
7. Sie wählt **Create prediction** aus.

Das Modell beginnt dann mit dem Training und analysiert Verhaltensweisen wie kürzlich durchgeführte Sitzungen, die Häufigkeit der Aufrufe und Interaktionen mit Inhalten, um Muster zu erkennen, die einen Abbruch vorhersagen. Eine Stunde später erhält Camila eine E-Mail, dass ihre Prognose fertig trainiert ist. Sie öffnet sie in Braze und überprüft den [Qualitätswert der Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality). Er ist mit „Gut“ gekennzeichnet, was bedeutet, dass die Prognosen des Modells wahrscheinlich genau und zuverlässig sind. Überzeugt von der Performance des Modells, setzt sie ihre Arbeit fort.

## 2. Schritt: Segmentieren Sie Nutzer:innen nach Churn-Risiko {#step-2-segment-users-by-churn-risk}

Nach Abschluss des Trainings weist Braze jeder in Frage kommenden Nutzer:in einen [Churn-Risiko-Score]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/#churn_score) zwischen 0 und 100 zu.

Um einen Startschwellenwert für das Targeting zu ermitteln, nutzt Camila den Schieberegler für die Prognose der Zielgruppe, um eine Vorschau anzuzeigen, wie viele Nutzer:innen in jeden Punktebereich fallen und wie genau die Prognose auf dieser Ebene ist. Sie wägt Abdeckung und Präzision auf der Grundlage der erwarteten echten Positiven ab. Auf dieser Grundlage beschließt sie, Risikowerte über 70 zu berücksichtigen.

1. Camila navigiert zu Segments in Braze.
2. Sie erstellt ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) mithilfe des [Filters „Churn Risk Score“]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#churn-risk-score) und wählt die von ihr erstellte Churn-Prognose aus:
   - **Wahrscheinliche Abwanderung:** Score über 70

![Segmentfilterung für Nutzer:innen mit einem Churn-Risiko-Score von über 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## 3. Schritt: Erreichen Sie gefährdete Nutzer:innen mit wiederkehrenden Inhalten zur erneuten Interaktion {#step-3-target-at-risk-users-with-recurring-re-engagement-content}

Nachdem ihre Prognose und ihr Segment fertig sind, richtet Camila eine wiederkehrende Campaign ein, die jede Woche automatisch Nutzer:innen erreicht, die einem Risiko ausgesetzt sind.

1. Camila erstellt eine wiederkehrende Campaign und aktiviert [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/), sodass jede Nachricht zu dem Zeitpunkt zugestellt wird, zu dem die Wahrscheinlichkeit des Engagements durch die jeweilige Nutzer:in am höchsten ist, anstatt sich auf einen festen Tag und eine feste Uhrzeit zu verlassen.
2. Sie richtet sich an das Segment „Wahrscheinliche Abwanderung“, das sie gerade erstellt hat.
3. Sie legt das Konversions-Event der Campaign als angepasstes Event `stream_started` fest, um zu verfolgen, wie viele Nutzer:innen tatsächlich zurückkehren, um Inhalte anzusehen.
4. Camila wählt E-Mail als ihren primären Kanal – dieser bietet ihr die Möglichkeit, mehrere personalisierte Inhalte in einem visuell ansprechenden Format ohne allzu großen Druck hervorzuheben. Die E-Mail enthält:
   - Eine personalisierte Watchlist, die auf [KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/) basiert und dynamisch aus dem Katalog von MovieCanon ausgewählt wird
   - Einen Aufruf zum Handeln, der die Nutzer:innen direkt in die App führt.

Dadurch wird sichergestellt, dass MovieCanon jede Woche nur die Nutzer:innen erreicht, die eine Erinnerung benötigen – ohne übermäßiges Messaging und ohne Spekulationen.

### Beispiel-E-Mail {#example-email}

- **Betreffzeile:** Lassen Sie diese Titel nicht ungesehen
- **Überschrift:** Ihr nächstes großartiges Filmerlebnis wartet auf Sie
- **Text:** Haben Sie schon länger nicht mehr auf „Play“ geklickt? Keine Sorge – wir haben einige Empfehlungen speziell für Sie zusammengestellt. Von spannungsgeladenen Thrillern bis hin zu preisgekrönten Dokumentarfilmen – hier ist für jeden Geschmack etwas dabei.
- **CTA:** Weitere Empfehlungen anzeigen

## 4. Schritt: Performance messen {#step-4-measure-performance}

Nach einigen Wochen überprüft Camila ihre [Campaign-Analytics]({{site.baseurl}}/user_guide/channels/email/reporting/), um die Performance der Strategie zu bewerten.

Sie sieht:

- *Öffnungsrate:* 31 %
- *Klickrate:* 15 %
- *Konversionsrate* (Stream innerhalb von 48 Stunden gestartet): 11 %

Im Vergleich zur früheren „Wir vermissen Sie“-Campaign (bei der die Konversionsraten bei etwa 3 % lagen) verringert dieser neue Ablauf den Churn in der Zielgruppe um 28 %. Sie analysiert den [Funnel-Bericht]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/), um festzustellen, an welcher Stelle die Nutzer:innen abspringen. Obwohl die Öffnungs- und Klickraten gut sind, stellt sie eine leichte Diskrepanz zwischen Klick und Conversion fest – was sie dazu veranlasst, den CTA-Text zu testen oder mit dem Layout zu experimentieren.

Um die langfristigen Auswirkungen zu verstehen, verfolgt Camila auch die Anzahl der Nutzer:innen, die Woche für Woche in das Segment „Wahrscheinliche Abwanderung“ gelangen. Dies unterstützt sie dabei, den allgemeinen Zustand des Lebenszyklus zu beurteilen und die Strategie zur Bindung auf einer breiteren Ebene zu gestalten. Abschließend kehrt sie zur Seite [Prognose-Analytics]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/) zurück, um ihre Churn-Prognose zu überprüfen und die prognostizierten Abgewanderten mit den tatsächlichen Abgewanderten zu vergleichen – eine nützliche Überprüfung, um sicherzustellen, dass das Modell wie erwartet funktioniert.

Auf Grundlage dieser Insights plant Camila, Betreffzeilen einem A/B-Test zu unterziehen, verschiedene Zeitfenster zu testen und mit Inhaltsformaten wie Empfehlungen im Karussellstil in einer In-App-Nachricht zu experimentieren.

Dank Predictive Churn, intelligentem Timing und KI-gestützter Personalisierung reagiert Camilas Team nicht nur auf Churn – sie sind ihm einen Schritt voraus. Und ihre Campaign läuft diskret im Hintergrund und erreicht die richtigen Personen zur richtigen Zeit mit Inhalten, die für sie tatsächlich von Interesse sind.