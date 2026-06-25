---
nav_title: Agent
article_title: Agent-Schritt
alias: /agent_step/
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie den Agent-Schritt in Canvas verwenden, um Inhalte zu generieren oder intelligente Entscheidungen in Echtzeit zu treffen."
tool: Canvas
toc_headers: h2
---

# Agent-Schritt {#agent-step}

> Mit dem Agent-Schritt können Sie KI-gestützte Entscheidungsfindung und Inhaltsgenerierung direkt in Ihren Canvas-Workflow integrieren. Allgemeine Informationen finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

![Ein Agent-Schritt in einer Canvas-User-Journey.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Voraussetzungen {#prerequisites}

Agent-Schritte verwenden [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/), um relevanten Kontext aufzunehmen und eine Variable auszugeben, die im Canvas genutzt werden kann.

## So funktioniert es {#how-it-works}

Wenn Nutzer:innen einen Agent-Schritt in einem Canvas erreichen, sendet Braze die von Ihnen konfigurierten Eingabedaten (vollständiger Kontext oder ausgewählte Felder) an den gewählten Agent. Der Agent verarbeitet dann die Eingabe mithilfe seines Modells und seiner Anweisungen und gibt eine Ausgabe zurück. Diese Ausgabe wird in der Ausgabevariable gespeichert, die Sie im Schritt definiert haben.

Sie können diese Variable auf drei Hauptarten verwenden:

- **Entscheidungsfindung:** Leiten Sie Nutzer:innen basierend auf der Antwort des Agents auf verschiedene Canvas-Pfade. Beispielsweise könnte ein Lead-Scoring-Agent eine Lead-Kategorie wie „Sales Ready“, „Marketing Qualified“ oder „Disqualified“ zurückgeben. Sie könnten diese Zuordnung verwenden, um einen Slack-Alert oder eine automatisierte Nachricht für „Sales Ready“-Leads auszulösen, während „Disqualified“-Leads aus der Journey entfernt werden.
- **Personalisierung:** Fügen Sie die Antwort des Agents direkt in eine Nachricht ein. Beispielsweise könnte ein Agent Kundenfeedback analysieren und eine empathische Follow-up-E-Mail generieren, die auf den Kommentar der Kund:innen eingeht und eine Lösung vorschlägt.
- **Nutzerdaten verarbeiten:** Analysieren und standardisieren Sie Ihre Nutzerdaten und speichern Sie diese im Nutzerprofil oder senden Sie sie über einen Webhook. Beispielsweise könnte ein Agent einen Sentiment-Score oder eine Produkt-Affinität-Zuordnung zurückgeben. Sie können diese Daten in einem Nutzerprofil für die zukünftige Verwendung speichern.

## Einen Agent-Schritt erstellen {#creating-an-agent-step}

### 1. Schritt: Schritt hinzufügen {#step-1-add-a-step}

Ziehen Sie die **Agent**-Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Agent**.

### 2. Schritt: Agent auswählen {#step-2-choose-your-agent}

Wählen Sie den Agent aus, der die Daten in diesem Schritt verarbeiten soll. Eine Anleitung zur Einrichtung finden Sie unter [Benutzerdefinierte Agents erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

In der Agent-Liste ist jeder Agent mit seinem [täglichen Aufruf-Limit]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#step-3-set-up-details) gekennzeichnet. Bewegen Sie den Mauszeiger über das Limit, um den heutigen Fortschritt in Richtung dieses Limits zu sehen, einschließlich des genutzten Prozentsatzes und der Anzahl der heute genutzten Aufrufe im Vergleich zum Limit.

![Das Panel „Agent-Schritt konfigurieren“ mit dem Agent-Dropdown, in dem zwei Agents aufgelistet sind. Jeder Agent ist mit seinem täglichen Aufruf-Limit gekennzeichnet. Ein Tooltip beim ersten Agent zeigt den genutzten Prozentsatz und die heute genutzten Aufrufe.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### 3. Schritt: Ausgabe des Agents festlegen {#define-the-output-variable}

Agent-Ausgaben werden als „Ausgabevariablen“ bezeichnet und in einer [Kontextvariable]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#context-variable-types) für einfachen Zugriff gespeichert. Um die Ausgabevariable zu definieren, geben Sie der Variable einen Namen.

Beachten Sie, dass der Datentyp der Ausgabevariable in der [Agentenkonsole]({{site.baseurl}}/user_guide/brazeai/agents/) festgelegt wird. Agent-Ausgaben können als Strings, Zahlen, Boolesche Werte oder Objekte gespeichert werden. Das macht sie flexibel sowohl für Text-Personalisierung als auch für bedingte Logik in Ihrem Canvas. Hier sind einige gängige Verwendungszwecke für jeden Typ:

| Datentyp | Gängige Verwendungszwecke |
| --- | --- |
| String | Nachrichten-Personalisierung (Betreffzeilen, Texte, Antworten) |
| Zahl | Scoring, Schwellenwerte, Routing in [Zielgruppenpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) |
| Boolescher Wert | Ja/Nein-Verzweigung in [Decision-Splits]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) |
| Objekt | Nutzen Sie einen oder mehrere der oben genannten Datentypen mit einem einzigen LLM-Aufruf in einer vorhersagbaren Datenstruktur |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3. Schritt: Ausgabe des Agents festlegen" }

Sie können eine Ausgabevariable im gesamten Canvas verwenden, indem Sie dieselbe Template-Syntax wie bei einer Kontextvariable nutzen. Verwenden Sie entweder den Segment-Filter **Context Variable** oder templaten Sie Agent-Antworten direkt mit Liquid: {% raw %}`{{context.${response_variable_name}}}`{% endraw %}.

Um eine bestimmte Eigenschaft aus einer Objekt-Ausgabevariable zu verwenden, nutzen Sie die Punkt-Notation, um mit Liquid auf diese Eigenschaft zuzugreifen: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agent-Schritt für Body HTML Writer mit einem Objekt-Datentyp als Ausgabe für die Variable „agent_output“.]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### 4. Schritt: Zusätzlichen Kontext hinzufügen (optional) {#step-4-add-any-additional-context-optional}

Sie können entscheiden, ob Sie zusätzliche Kontextwerte einbeziehen möchten, auf die der Agent-Schritt bei der Ausführung zugreifen kann. Sie können beliebige Liquid-Template-Werte eingeben, die Sie normalerweise in einem Canvas verwenden würden.

{% alert note %}
Beachten Sie, dass der Agent bereits automatisch den Kontext erhält, der im Abschnitt **Instructions** konfiguriert ist. Liquid-Variablen, die dort bereits konfiguriert wurden, müssen hier nicht erneut eingegeben werden.
{% endalert %}

![Die Option, einem Agent-Schritt zusätzlichen Kontext mit Liquid hinzuzufügen.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### 5. Schritt: Agent testen {#step-5-test-the-agent}

Nachdem Sie Ihren Agent-Schritt eingerichtet haben, können Sie die Ausgabe dieses Schritts testen und in der Vorschau anzeigen.

![Vorschau der Agent-Ausgabe als zufällige:r Nutzer:in.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Fehlerbehandlung {#error-handling}

Informationen dazu, wie Braze mit Agent-Fehlern, Rate-Limit-Fehlern und Aufruf-Flusssteuerungen umgeht, finden Sie unter [Fehlerbehandlung und Fallback-Verhalten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#fallback-behavior) in „Agents bereitstellen“ und [Fehlerbehandlung]({{site.baseurl}}/user_guide/brazeai/agents/#error-handling) in „Braze Agents“.

- Wenn das verbundene Modell einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors) vom LLM-Anbieter zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann; Nutzer:innen gehen dann zum nächsten Canvas-Schritt weiter.
- Bei anderen Fehlern (z. B. einem Timeout-Fehler oder einem ungültigen API-Schlüssel) oder wenn ein Agent sein tägliches Aufruf-Limit erreicht, wird die Ausgabevariable auf `null` gesetzt, es sei denn, der Agent hat [Fallback-Werte konfiguriert]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#configure-fallback-values) in der Agentenkonsole. Wenn Fallback-Werte konfiguriert sind, rendert Braze den Fallback mit Liquid pro Nutzer:in und speichert das Ergebnis in der Ausgabevariable, auch wenn das tägliche Limit einen Aufruf blockiert.
- Wenn Sie keine Fallback-Werte konfigurieren, verwenden Sie [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/) in nachgelagerten Nachrichten-Schritten, um Null-Ausgaben zu behandeln. Beispielsweise können Sie im Modal **Add Personalization** einen Standard-Liquid-Wert eingeben wie {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} oder {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Antworten werden bei identischen Eingaben zwischengespeichert und können bei wiederholten identischen Aufrufen innerhalb weniger Minuten wiederverwendet werden.
    - Antworten, die zwischengespeicherte Werte verwenden, zählen dennoch zu den Gesamt- und täglichen Aufrufen.
- Agent-Schritte können bei der Verarbeitung einer großen Anzahl von Nutzer:innen Zeit in Anspruch nehmen. Braze reiht Aufrufe gemäß den [Aufruf-Flusssteuerungen]({{site.baseurl}}/user_guide/brazeai/agents/reference/#invocation-flow-controls) in eine Warteschlange ein, sodass Nutzer:innen bei Versendungen mit hohem Volumen möglicherweise ausstehend bleiben. Überprüfen Sie Ihre Logs, um sicherzustellen, dass Aufrufe stattfinden.

## Analytics {#analytics}

Verwenden Sie die folgenden Metriken, um die Performance Ihrer Agent-Schritte zu verfolgen:

| Metrik | Beschreibung |
| --- | --- |
| _Eingetreten_ | Die Anzahl der Male, die Nutzer:innen den Agent-Schritt betreten haben. |
| _Zum nächsten Schritt weitergegangen_ | Die Anzahl der Nutzer:innen, die nach dem Durchlaufen des Agent-Schritts zum nächsten Schritt im Flow weitergegangen sind. |
| _Canvas verlassen_ | Die Anzahl der Nutzer:innen, die den Canvas nach dem Durchlaufen des Agent-Schritts verlassen haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }

## Best Practices {#best-practices}

### Aufgaben bei komplexen Anwendungsfällen auf mehrere Agents aufteilen {#split-tasks-between-agents-for-complicated-use-cases}

Wenn Sie feststellen, dass ein Agent mit der Komplexität der Aufgaben, die Sie ihm stellen, Schwierigkeiten hat, verteilen Sie die Arbeit auf mehr als einen Agent-Schritt. Wenn ein Prompt Datenbereinigung, Routing-Logik und vollständiges Verfassen von Nachrichten vermischt, konkurrieren diese Ziele miteinander und die Ausgabequalität kann variieren.

Das folgende Muster verwendet drei Agents für ein Reisebeispiel: Jemand hat kürzlich in Ihrer App gesucht, aber nicht gebucht, und Sie möchten Retargeting-Texte, die zum Checkout anregen.

- Agent 1 fasst den Canvas-Kontext zusammen. Er liest Felder wie Treuestufe, zuletzt gesuchte Stadt und Suchverhalten mit hoher Kaufabsicht und gibt eine kurze strukturierte Zusammenfassung als Ausgabevariable zurück, die spätere Schritte wiederverwenden können.
- Agent 2 gibt einen Routing-Wert zurück, auf dem Ihr Canvas verzweigen kann. Verwenden Sie eine Zahl, einen Booleschen Wert oder ein strukturiertes Objekt, damit die Ausgabe zu Ihrer Verzweigungslogik passt. Ordnen Sie diesen Wert einem [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/)- oder [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)-Schritt zu. Erwägen Sie beispielsweise separate Pfade für Treue-basiertes Messaging im Vergleich zu Angebots-basiertem Messaging.
- Agent 3 verfasst generierten Nachrichtentext nur in Branches, in denen Sie dies wünschen. Übergeben Sie die Zusammenfassung von Agent 1 (und jeden Branch-spezifischen Kontext), damit sich dieser Agent auf Tonalität und Kanallimits konzentriert, anstatt im selben Prompt Eingaben zu normalisieren und eine Strategie zu wählen.

### Den Experimentpfad-Schritt verwenden, um agentische Journeys im kleinen Maßstab zu testen {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Um die Performance und den Credit-Verbrauch Ihres Agents im Vergleich zu Ihren bestehenden Journeys zu testen, fügen Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/)-Schritt hinzu, sodass nur ein Teil Ihrer Zielgruppe den Branch betritt, der Ihren Agent-Schritt enthält.

Senden Sie beispielsweise zunächst einige Tausend Nutzer:innen pro Tag auf einen Pfad mit dem Agent und den Rest auf einen Kontrollpfad oder einen Pfad ohne Agent. Sammeln Sie 1–2 Wochen lang Daten und vergleichen Sie Leistungskennzahlen (KPIs), Gegenmetriken und den Agent-Credit-Verbrauch zwischen den Pfaden. So können Sie Vertrauen aufbauen und den ROI nachweisen, bevor Sie den Traffic zum Agent-aktivierten Branch erhöhen, und gleichzeitig den Aufrufverbrauch begrenzen.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wann sollte ich einen Agent-Schritt verwenden? {#when-should-i-use-an-agent-step}

Generell empfehlen wir die Verwendung eines Agent-Schritts, wenn Sie bestimmte kontextuelle Daten in ein LLM einspeisen und es agentisch eine Canvas-Kontextvariable intelligent in einem Umfang zuweisen lassen möchten, der für Menschen unmöglich wäre.

Angenommen, Sie senden eine personalisierte Nachricht, um Nutzer:innen, die zuvor Schokolade und Erdbeere bestellt haben, eine neue Eissorte zu empfehlen. Hier ist der Unterschied zwischen der Verwendung eines Agent-Schritts und KI-Artikelempfehlungen:

- **Agent-Schritt:** Verwendet LLMs, um eine qualitative Entscheidung darüber zu treffen, was die Nutzer:innen basierend auf den Anweisungen und Kontext-Datenpunkten, die dem Agent gegeben wurden, möchten könnten. In diesem Beispiel könnte ein Agent-Schritt eine neue Sorte empfehlen, basierend auf der Möglichkeit, dass die Nutzer:innen verschiedene Sorten ausprobieren möchten.
- **KI-Artikelempfehlungen:** Verwendet Modelle des maschinellen Lernens, um die Produkte vorherzusagen, die Nutzer:innen am wahrscheinlichsten möchten, basierend auf vergangenen Nutzer-Events wie Käufen. In diesem Beispiel würden KI-Artikelempfehlungen eine Sorte (Vanille) vorschlagen, basierend auf den beiden vorherigen Bestellungen der Nutzer:innen (Schokolade und Erdbeere) und wie diese im Vergleich zum Verhalten anderer Nutzer:innen in Ihrem Workspace stehen.

### Wie verwenden Agent-Schritte Eingabedaten? {#how-do-agent-steps-use-input-data}

Ein Agent-Schritt analysiert die Kontextdaten, für deren Verwendung der Agent konfiguriert ist, sowie jeden zusätzlichen Kontext, der [dem Agent bereitgestellt wird](#step-4-add-any-additional-context-optional).

## Verwandte Artikel {#related-articles}

- [Braze Agents – Übersicht]({{site.baseurl}}/user_guide/brazeai/agents/)
- [Benutzerdefinierte Agents erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Agents bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
- [Referenz für Agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)