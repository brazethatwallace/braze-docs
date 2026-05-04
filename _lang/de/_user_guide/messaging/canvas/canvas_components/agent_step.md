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

# Agent-Schritt

> Mit dem Agent-Schritt können Sie KI-gestützte Entscheidungsfindung und Inhaltsgenerierung direkt in Ihren Canvas-Workflow integrieren. Allgemeine Informationen finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

![Ein Agent-Schritt in einer Canvas-User-Journey.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Voraussetzungen

Agent-Schritte verwenden [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/), um relevanten Kontext aufzunehmen und eine Variable auszugeben, die im Canvas genutzt werden kann.

## So funktioniert es

Wenn ein:e Nutzer:in einen Agent-Schritt in einem Canvas erreicht, sendet Braze die von Ihnen konfigurierten Eingabedaten (vollständiger Kontext oder ausgewählte Felder) an den gewählten Agent. Der Agent verarbeitet dann die Eingabe mithilfe seines Modells und seiner Anweisungen und gibt eine Ausgabe zurück. Diese Ausgabe wird in der Ausgabevariable gespeichert, die Sie im Schritt definiert haben.

Sie können diese Variable auf drei Hauptarten verwenden:

- **Entscheidungsfindung:** Leiten Sie Nutzer:innen basierend auf der Antwort des Agents auf verschiedene Canvas-Pfade. Beispielsweise könnte ein Lead-Scoring-Agent eine Zahl zwischen 1 und 10 zurückgeben. Sie können diesen Score verwenden, um zu entscheiden, ob Sie eine:n Nutzer:in weiter ansprechen oder aus der Journey entfernen.
- **Personalisierung:** Fügen Sie die Antwort des Agents direkt in eine Nachricht ein. Beispielsweise könnte ein Agent Kundenfeedback analysieren und eine empathische Follow-up-E-Mail generieren, die auf den Kommentar der Kund:innen eingeht und eine Lösung vorschlägt.
- **Nutzerdaten verarbeiten:** Analysieren und standardisieren Sie Ihre Nutzerdaten und speichern Sie diese im Nutzerprofil oder senden Sie sie über einen Webhook. Beispielsweise könnte ein Agent einen Sentiment-Score oder eine Produkt-Affinität-Zuordnung zurückgeben. Sie können diese Daten in einem Nutzerprofil für die zukünftige Verwendung speichern.

## Einen Agent-Schritt erstellen

### 1. Schritt: Schritt hinzufügen

Ziehen Sie die **Agent**-Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Agent**.

### 2. Schritt: Agent auswählen

Wählen Sie den Agent aus, der die Daten in diesem Schritt verarbeiten soll. Wählen Sie einen vorhandenen Agent. Eine Anleitung zur Einrichtung finden Sie unter [Benutzerdefinierte Agents erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### 3. Schritt: Ausgabe des Agents festlegen {#define-the-output-variable}

Agent-Ausgaben werden als „Ausgabevariablen" bezeichnet und in einer [Kontextvariable]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-types) für einfachen Zugriff gespeichert. Um die Ausgabevariable zu definieren, geben Sie der Variable einen Namen.

Beachten Sie, dass der Datentyp der Ausgabevariable in der [Agentenkonsole]({{site.baseurl}}/user_guide/brazeai/agents) festgelegt wird. Agent-Ausgaben können als Strings, Zahlen, Boolesche Werte oder Objekte gespeichert werden. Das macht sie flexibel sowohl für Text-Personalisierung als auch für bedingte Logik in Ihrem Canvas. Hier sind einige gängige Verwendungszwecke für jeden Typ:

| Datentyp | Gängige Verwendungszwecke |
| --- | --- |
| String | Nachrichten-Personalisierung (Betreffzeilen, Texte, Antworten) |
| Zahl | Scoring, Schwellenwerte, Routing in [Zielgruppenpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) |
| Boolescher Wert | Ja/Nein-Verzweigung in [Decision-Splits]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) |
| Objekt | Nutzen Sie einen oder mehrere der oben genannten Datentypen mit einem einzigen LLM-Aufruf in einer vorhersagbaren Datenstruktur |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie können eine Ausgabevariable im gesamten Canvas verwenden, indem Sie dieselbe Template-Syntax wie bei einer Kontextvariable nutzen. Verwenden Sie entweder den Segment-Filter **Context Variable** oder templaten Sie Agent-Antworten direkt mit Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Um eine bestimmte Eigenschaft aus einer Objekt-Ausgabevariable zu verwenden, nutzen Sie die Punkt-Notation, um mit Liquid auf diese Eigenschaft zuzugreifen: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agent-Schritt für Body HTML Writer mit einem Objekt-Datentyp als Ausgabe für die Variable „agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### 4. Schritt: Zusätzlichen Kontext hinzufügen (optional)

Sie können entscheiden, ob Sie zusätzliche Kontextwerte einbeziehen möchten, auf die der Agent-Schritt bei der Ausführung zugreifen kann. Sie können beliebige Liquid-Template-Werte eingeben, die Sie normalerweise in einem Canvas verwenden würden.

{% alert note %}
Beachten Sie, dass der Agent bereits automatisch den Kontext erhält, der im Abschnitt **Instructions** konfiguriert ist. Liquid-Variablen, die dort bereits konfiguriert wurden, müssen hier nicht erneut eingegeben werden.
{% endalert %}

![Die Option, einem Agent-Schritt zusätzlichen Kontext mit Liquid hinzuzufügen.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### 5. Schritt: Agent testen

Nachdem Sie Ihren Agent-Schritt eingerichtet haben, können Sie die Ausgabe dieses Schritts testen und in der Vorschau anzeigen.

![Vorschau der Agent-Ausgabe als zufällige:r Nutzer:in.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Fehlerbehandlung

- Wenn das verbundene Modell einen Rate-Limit-Fehler zurückgibt, versucht Braze es bis zu fünf Mal mit exponentiellem Backoff erneut.
- Wenn der Agent aus einem anderen Grund fehlschlägt (z. B. ein Timeout-Fehler oder ein ungültiger API-Schlüssel), wird die Ausgabevariable auf `null` gesetzt.
    - Wenn ein Agent sein tägliches Aufruf-Limit erreicht, wird die Ausgabevariable auf `null` gesetzt.
- Verwenden Sie [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values/), um sich gegen Fehler abzusichern. Beispielsweise können Sie im Modal **Add Personalization** einen Standard-Liquid-Wert eingeben wie {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} oder {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}.
- Antworten werden bei identischen Eingaben zwischengespeichert und können bei wiederholten identischen Aufrufen innerhalb weniger Minuten wiederverwendet werden.
    - Antworten, die zwischengespeicherte Werte verwenden, zählen dennoch zu den Gesamt- und täglichen Aufrufen.
- Agent-Schritte können bei der Verarbeitung einer großen Anzahl von Nutzer:innen Zeit in Anspruch nehmen. Wenn Sie Nutzer:innen sehen, die in diesem Schritt noch ausstehend sind, überprüfen Sie Ihre Logs, um sicherzustellen, dass Aufrufe stattfinden.

## Analytics

Verwenden Sie die folgenden Metriken, um die Leistung Ihrer Agent-Schritte zu verfolgen:

| Metrik | Beschreibung |
| --- | --- |
| _Eingetreten_ | Die Anzahl der Male, die Nutzer:innen den Agent-Schritt betreten haben. |
| _Zum nächsten Schritt weitergegangen_ | Die Anzahl der Nutzer:innen, die nach dem Durchlaufen des Agent-Schritts zum nächsten Schritt im Flow weitergegangen sind. |
| _Canvas verlassen_ | Die Anzahl der Nutzer:innen, die den Canvas nach dem Durchlaufen des Agent-Schritts verlassen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Wann sollte ich einen Agent-Schritt verwenden?

Generell empfehlen wir die Verwendung eines Agent-Schritts, wenn Sie bestimmte kontextuelle Daten in ein LLM einspeisen und es agentisch eine Canvas-Kontextvariable intelligent in einem Umfang zuweisen lassen möchten, der für Menschen unmöglich wäre.

Angenommen, Sie senden eine personalisierte Nachricht, um einem:einer Nutzer:in, der/die zuvor Schokolade und Erdbeere bestellt hat, eine neue Eissorte zu empfehlen. Hier ist der Unterschied zwischen der Verwendung eines Agent-Schritts und KI-Artikelempfehlungen:

- **Agent-Schritt:** Verwendet LLMs, um eine qualitative Entscheidung darüber zu treffen, was der/die Nutzer:in basierend auf den Anweisungen und Kontext-Datenpunkten, die dem Agent gegeben wurden, möchten könnte. In diesem Beispiel könnte ein Agent-Schritt eine neue Sorte empfehlen, basierend auf der Möglichkeit, dass der/die Nutzer:in verschiedene Sorten ausprobieren möchte.
- **KI-Artikelempfehlungen:** Verwendet Modelle des maschinellen Lernens, um die Produkte vorherzusagen, die ein:e Nutzer:in am wahrscheinlichsten möchte, basierend auf vergangenen Nutzer-Events wie Käufen. In diesem Beispiel würden KI-Artikelempfehlungen eine Sorte (Vanille) vorschlagen, basierend auf den beiden vorherigen Bestellungen des/der Nutzer:in (Schokolade und Erdbeere) und wie diese im Vergleich zum Verhalten anderer Nutzer:innen in Ihrem Workspace stehen.

### Wie verwenden Agent-Schritte Eingabedaten?

Ein Agent-Schritt analysiert die Kontextdaten, für deren Verwendung der Agent konfiguriert ist, sowie jeden zusätzlichen Kontext, der [dem Agent bereitgestellt wird](#step-4-add-any-additional-context-optional).

## Verwandte Artikel

- [Braze Agents – Übersicht]({{site.baseurl}}/user_guide/brazeai/agents/)
- [Benutzerdefinierte Agents erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Agents bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)
- [Referenz für Agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)