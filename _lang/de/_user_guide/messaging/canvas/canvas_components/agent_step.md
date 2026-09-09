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

> Mit dem Agent-Schritt können Sie KI-gestützte Entscheidungsfindung und Inhaltsgenerierung direkt in Ihren Canvas-Workflow integrieren. Allgemeine Informationen finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents).

![Ein Agent-Schritt in einer Canvas-User-Journey.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Voraussetzungen {#prerequisites}

Agent-Schritte verwenden [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables), um relevanten Kontext aufzunehmen und eine Variable auszugeben, die im Canvas genutzt werden kann.

## So funktioniert es {#how-it-works}

Wenn Nutzer:innen einen Agent-Schritt in einem Canvas erreichen, sendet Braze die von Ihnen konfigurierten Eingabedaten (vollständiger Kontext oder ausgewählte Felder) an Ihren gewählten Agenten. Der Agent verarbeitet die Eingabe dann mithilfe seines Modells und seiner Anweisungen und gibt eine Ausgabe zurück. Diese Ausgabe wird in der Ausgabevariablen gespeichert, die Sie im Schritt definiert haben.

Sie können diese Variable dann auf drei wesentliche Arten verwenden:

- **Entscheidungsfindung:** Leiten Sie Nutzer:innen basierend auf der Antwort des Agenten auf verschiedene Canvas-Pfade. Beispielsweise könnte ein Lead-Scoring-Agent eine Lead-Kategorie wie „Sales Ready“, „Marketing Qualified“ oder „Disqualified“ zurückgeben. Sie könnten diese Zuordnung nutzen, um für „Sales Ready“-Leads eine Slack-Benachrichtigung oder automatisierte Nachricht auszulösen, während „Disqualified“-Leads aus der Journey entfernt werden.
- **Personalisierung:** Fügen Sie die Antwort des Agenten direkt in eine Nachricht ein. Beispielsweise könnte ein Agent Kundenfeedback analysieren und eine einfühlsame Follow-up-E-Mail generieren, die auf den Kommentar der Kund:innen eingeht und eine Lösung vorschlägt.
- **Nutzerdaten verarbeiten:** Analysieren und standardisieren Sie Ihre Nutzerdaten und speichern Sie diese im Kundenprofil oder senden Sie sie über einen Webhook. Beispielsweise könnte ein Agent einen Stimmungswert oder eine Produkt-Affinität-Zuordnung zurückgeben. Sie können diese Daten in einem Kundenprofil für die zukünftige Verwendung speichern.

## Erstellen eines Agent-Schritts {#creating-an-agent-step}

### Schritt 1: Schritt hinzufügen {#step-1-add-a-step}

Ziehen Sie die Komponente **Agent** aus der Seitenleiste und legen Sie sie ab, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Agent**.

### Schritt 2: Agent auswählen {#step-2-choose-your-agent}

Wählen Sie den Agent aus, der die Daten in diesem Schritt verarbeiten soll. Hinweise zur Einrichtung finden Sie unter [Benutzerdefinierte Agents erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents).

In der Agent-Liste ist jeder Agent mit seinem [täglichen Aufruf-Limit]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details) gekennzeichnet. Bewegen Sie den Mauszeiger über das Limit, um den heutigen Fortschritt in Richtung dieses Limits zu sehen, einschließlich des genutzten Prozentsatzes und der Anzahl der heute getätigten Aufrufe im Vergleich zum Limit.

![Das Panel „Agent-Schritt konfigurieren“ mit dem Agent-Dropdown und zwei aufgelisteten Agents. Jeder Agent ist mit seinem täglichen Aufruf-Limit gekennzeichnet. Ein Tooltip beim ersten Agent zeigt den genutzten Prozentsatz und die heute getätigten Aufrufe an.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### Schritt 3: Ausgabe des Agents festlegen {#define-the-output-variable}

Agent-Ausgaben werden als „Ausgabevariablen“ bezeichnet und in einer [Kontextvariable]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-filters) für einfachen Zugriff gespeichert. Um die Ausgabevariable zu definieren, geben Sie der Variable einen Namen.

Beachten Sie, dass der Datentyp der Ausgabevariable über die [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents) festgelegt wird. Agent-Ausgaben können als Strings, Zahlen, Booleans oder Objekte gespeichert werden. Dadurch sind sie sowohl für die Personalisierung von Texten als auch für bedingte Logik in Ihrem Canvas flexibel einsetzbar. Hier sind einige gängige Anwendungsfälle für jeden Typ:

| Datentyp | Gängige Anwendungsfälle |
| --- | --- |
| String | Nachrichten-Personalisierung (Betreffzeilen, Text, Antworten) |
| Zahl | Scoring, Schwellenwerte, Weiterleitung in [Zielgruppenpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Boolean | Ja/Nein-Verzweigung in [Decision-Splits]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) |
| Objekt | Nutzen Sie einen oder mehrere der zuvor in diesem Abschnitt genannten Datentypen mit einem einzigen LLM-Aufruf in einer vorhersagbaren Datenstruktur |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Ausgabe des Agents festlegen" }

Sie können eine Ausgabevariable im gesamten Canvas verwenden, indem Sie dieselbe Template-Syntax wie bei einer Kontextvariable nutzen. Verwenden Sie entweder den Segmentfilter **Context Variable** oder binden Sie Agent-Antworten direkt über Liquid ein: {% raw %}`{{context.${response_variable_name}}}`{% endraw %}.

Um eine bestimmte Eigenschaft aus einer Objekt-Ausgabevariable zu verwenden, nutzen Sie die Punktnotation, um über Liquid auf diese Eigenschaft zuzugreifen: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agent-Schritt für den Body-HTML-Writer mit einem Objekt-Datentyp als Ausgabe für die Variable „agent_output“.]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Schritt 4: Optionale Schrittanweisungen hinzufügen {#step-4-add-optional-step-instructions}

Sie können optionale Schrittanweisungen für alles einfügen, was Ihr Agent wissen muss, das spezifisch für diesen Schritt ist und noch nicht in den Hauptanweisungen des Agents abgedeckt wird. Sie können alle Liquid-Template-Werte eingeben, die Sie normalerweise in einem Canvas verwenden würden.

### Schritt 5: Agent testen {#step-5-test-the-agent}

Sie können einen Agent-Schritt auf zwei Arten testen:

**Vorschau im Schritt (Canvas-Builder):** Nachdem Sie den Schritt konfiguriert haben, verwenden Sie die Schrittvorschau, um die Agent-Ausgabe für eine:n zufällige:n Nutzer:in, eine:n bestehende:n Nutzer:in oder eine:n benutzerdefinierte:n Nutzer:in anzuzeigen. Damit wird der Schritt isoliert getestet, ohne den gesamten Canvas-Pfad zu durchlaufen.

**Canvas testen (vollständige Journey):** Wählen Sie **Canvas testen** in der Canvas-Fußzeile, um den Nutzerpfad End-to-End in der Vorschau anzuzeigen. Wenn der Test Ihren Agent-Schritt erreicht, fragt Braze: **Möchten Sie den Agent „{agentName}“ ausführen?**

- Wählen Sie **Ja**, um optional Kontext hinzuzufügen, und wählen Sie dann **Antwort simulieren**, um den Agent für die:den Vorschau-Nutzer:in aufzurufen. Sie können Beispiel-Eingaben in natürlicher Sprache beschreiben (z. B. Warenkorbinhalte oder Nachrichtentext), um das Profil der:des Testnutzer:in und den bereits vorgelagert festgelegten Canvas-Kontext zu ergänzen.
- Wählen Sie **Nein**, um den Live-Aufruf zu überspringen und stattdessen die konfigurierte **Fallback-Ausgabe** des Agents aus der Agent Console zu verwenden.

Aufrufe über **Antwort simulieren** werden auf das tägliche Aufruf-Limit des Agents angerechnet und erscheinen unter **Agent Console** > **Logs**. Für das vollständige Verhalten von „Canvas testen“ siehe [Nutzerpfade in der Vorschau anzeigen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps).

![Vorschau der Agent-Ausgabe als zufällige:r Nutzer:in.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Fehlerbehandlung {#error-handling}

Informationen dazu, wie Braze mit Agent-Fehlern, Rate-Limit-Fehlern und Aufruf-Flusssteuerungen umgeht, finden Sie unter [Fehlerbehandlung und Fallback-Verhalten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior) in „Agents bereitstellen“ und [Fehlerbehandlung]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) in „Braze Agents“.

- Wenn das verbundene Modell einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) vom LLM-Anbieter zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann; Nutzer:innen gehen dann zum nächsten Canvas-Schritt weiter.
- Bei anderen Fehlern (z. B. einem Timeout-Fehler oder einem ungültigen API-Schlüssel) oder wenn ein Agent sein tägliches Aufruf-Limit erreicht, wird die Ausgabevariable auf `null` gesetzt, es sei denn, der Agent hat [Fallback-Werte konfiguriert]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agent Console. Wenn Fallback-Werte konfiguriert sind, rendert Braze den Fallback mit Liquid pro Nutzer:in und speichert das Ergebnis in der Ausgabevariable, auch wenn das tägliche Limit einen Aufruf blockiert.
- Wenn Sie keine Fallback-Werte konfigurieren, verwenden Sie [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) in nachgelagerten Nachrichten-Schritten, um Null-Ausgaben zu behandeln. Beispielsweise können Sie im Modal **Add Personalization** einen Standard-Liquid-Wert eingeben wie {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} oder {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Antworten werden bei identischen Eingaben zwischengespeichert und können bei wiederholten identischen Aufrufen innerhalb weniger Minuten wiederverwendet werden.
    - Antworten, die zwischengespeicherte Werte verwenden, zählen dennoch zu den Gesamt- und täglichen Aufrufen.
- Agent-Schritte können bei der Verarbeitung einer großen Anzahl von Nutzer:innen Zeit in Anspruch nehmen. Braze reiht Aufrufe gemäß den [Aufruf-Flusssteuerungen]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls) in eine Warteschlange ein, sodass Nutzer:innen bei Versendungen mit hohem Volumen möglicherweise ausstehend bleiben. Überprüfen Sie Ihre Logs, um sicherzustellen, dass Aufrufe stattfinden.

## Analytics {#analytics}

In den folgenden Metriken können Sie nachverfolgen, wie Ihre Agent-Schritte performen:

| Metrik | Beschreibung |
| --- | --- |
| _Eingetreten_ | Die Anzahl, wie oft Nutzer:innen den Agent-Schritt betreten haben. |
| _Zum nächsten Schritt weitergegangen_ | Die Anzahl der Nutzer:innen, die nach dem Durchlaufen des Agent-Schritts zum nächsten Schritt im Flow weitergegangen sind. |
| _Canvas verlassen_ | Die Anzahl der Nutzer:innen, die nach dem Durchlaufen des Agent-Schritts den Canvas verlassen haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }

## Best Practices {#best-practices}

### Aufgaben bei komplexen Anwendungsfällen auf mehrere Agents aufteilen {#split-tasks-between-agents-for-complicated-use-cases}

Wenn ein Agent mit der Komplexität der Aufgaben, die Sie ihm stellen, Schwierigkeiten hat, verteilen Sie die Arbeit auf mehr als einen Agent-Schritt. Wenn ein einzelner Prompt Datenbereinigung, Routing-Logik und vollständige Nachrichtenerstellung vermischt, konkurrieren diese Ziele miteinander und die Ausgabequalität kann schwanken.

Das folgende Muster verwendet drei Agents für ein Reisebeispiel: Jemand hat kürzlich in Ihrer App gesucht, aber nicht gebucht, und Sie möchten Retargeting-Texte erstellen, die zum Checkout motivieren.

- Agent 1 fasst den Canvas-Kontext zusammen. Er liest Felder wie Treuestufe, zuletzt gesuchte Stadt und Suchverhalten mit hoher Absicht und gibt eine kurze, strukturierte Zusammenfassung als Ausgabevariable zurück, die spätere Schritte wiederverwenden können.
- Agent 2 gibt einen Routing-Wert zurück, auf dessen Basis Ihr Canvas verzweigen kann. Verwenden Sie eine Zahl, einen Boolean oder ein strukturiertes Objekt, damit die Ausgabe zu Ihrer Verzweigungslogik passt. Ordnen Sie diesen Wert einem [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)- oder [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Schritt zu. Erwägen Sie beispielsweise separate Pfade für Kundenbindungs-basiertes Messaging im Vergleich zu Angebots-basiertem Messaging.
- Agent 3 erstellt generierten Nachrichtentext nur in den Branches, in denen Sie ihn benötigen. Übergeben Sie die Zusammenfassung von Agent 1 (und jeglichen Branch-spezifischen Kontext), damit sich dieser Agent auf Tonalität und Kanalbeschränkungen konzentriert, anstatt im selben Prompt Eingaben zu normalisieren und eine Strategie auszuwählen.

### Den Experimentpfad-Schritt nutzen, um agentische Journeys im kleinen Maßstab zu testen {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

Um die Performance und den Credit-Verbrauch Ihres Agents im Vergleich zu Ihren bestehenden Journeys zu testen, fügen Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt hinzu, sodass nur ein Teil Ihrer Zielgruppe in den Branch gelangt, der Ihren Agent-Schritt enthält.

Sie können beispielsweise damit beginnen, einige Tausend Nutzer:innen pro Tag über einen Pfad mit dem Agent zu senden und den Rest an einen Kontrollpfad oder einen Pfad ohne Agent weiterzuleiten. Sammeln Sie 1–2 Wochen lang Daten und vergleichen Sie KPI (KPIs), Gegenmetriken und den Agent-Credit-Verbrauch zwischen den Pfaden. Auf diese Weise können Sie Vertrauen aufbauen und den Kapitalrendite nachweisen, bevor Sie den Traffic zum Agent-fähigen Branch erhöhen – und dabei den Aufrufverbrauch begrenzen.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wann sollte ich einen Agent-Schritt verwenden? {#when-should-i-use-an-agent-step}

Generell empfehlen wir die Verwendung eines Agent-Schritts, wenn Sie bestimmte kontextuelle Daten in ein LLM einspeisen und es agentisch eine Canvas-Kontextvariable intelligent zuweisen lassen möchten – in einem Umfang, der für Menschen unmöglich wäre.

Angenommen, Sie senden eine personalisierte Nachricht, um einer Nutzerin oder einem Nutzer eine neue Eissorte zu empfehlen, die oder der zuvor Schokolade und Erdbeere bestellt hat. Hier ist der Unterschied zwischen der Verwendung eines Agent-Schritts und KI-Artikelempfehlungen:

- **Agent-Schritt:** Verwendet LLMs, um eine qualitative Entscheidung darüber zu treffen, was die Nutzerin oder der Nutzer basierend auf den Anweisungen und Kontext-Datenpunkten, die dem Agenten gegeben wurden, möchten könnte. In diesem Beispiel könnte ein Agent-Schritt eine neue Sorte empfehlen, basierend auf der Möglichkeit, dass die Nutzerin oder der Nutzer verschiedene Geschmacksrichtungen ausprobieren möchte.
- **KI-Artikelempfehlungen:** Verwendet Modelle für maschinelles Lernen, um die Produkte vorherzusagen, die Nutzer:innen am wahrscheinlichsten wünschen, basierend auf vergangenen Nutzerereignissen wie Käufen. In diesem Beispiel würden KI-Artikelempfehlungen eine Geschmacksrichtung (Vanille) vorschlagen, basierend auf den beiden vorherigen Bestellungen (Schokolade und Erdbeere) und dem Vergleich mit dem Verhalten anderer Nutzer:innen in Ihrem Workspace.

### Wie verwenden Agent-Schritte Eingabedaten? {#how-do-agent-steps-use-input-data}

Ein Agent-Schritt analysiert die Kontextdaten, für deren Verwendung der Agent konfiguriert ist, sowie alle [optionalen Schrittanweisungen](#step-4-add-optional-step-instructions), die Sie dem Schritt hinzufügen.

## Verwandte Artikel {#related-articles}

- [Braze Agents – Übersicht]({{site.baseurl}}/user_guide/brazeai/agents)
- [Angepasste Agents erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Agents bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [Referenz für Agents]({{site.baseurl}}/user_guide/brazeai/agents/reference)