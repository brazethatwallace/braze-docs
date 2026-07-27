---
nav_title: FAQ
article_title: Agents – FAQ
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Braze Agents."
page_order: 10
toc_headers: h2
---

# Agents – Häufig gestellte Fragen {#agents-frequently-asked-questions}

> Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Braze Agents.

## Allgemein {#general}

### Was ist der Unterschied zwischen Canvas-Schritt-Agents und Katalog-Agents? {#what-is-the-difference-between-canvas-step-agents-and-catalog-agents}

Beim Erstellen eines Agents legen Sie fest, ob Sie einen Canvas-Schritt-Agent oder einen Katalog-Agent erstellen möchten. Dies bestimmt, welche Arten von Anweisungen und Optionen der Agent unterstützen kann. Canvas-Schritt-Agents verarbeiten Nutzer:innen in Realtime innerhalb von Journeys, während Katalog-Agents Katalogdaten anreichern, indem sie Spalten mit verarbeiteten Informationen hinzufügen oder aktualisieren.

### Welche Vorteile bietet das Auto-Modell im Vergleich zum Bring-your-own-Modell (BYO)? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Vorteile des Braze Auto-Modells:

- Es sind keine API-Schlüssel, kein Abrufen von Zugangsdaten und kein Integrations-Setup erforderlich.
- Jeder Aufruf wird automatisch an das effektivste Modell für die jeweilige Aufgabe weitergeleitet.

### Wo kann ich meine aktuelle Agent-Nutzung einsehen? {#where-can-i-find-my-current-agent-usage}

Gehen Sie zu **Einstellungen** > **Abrechnung** > **Credit-Nutzung** > **Agentenkonsole**, um den Credit-Verbrauch, die Anzahl der Aufrufe und die Credit-Verhältnisse pro Agent einzusehen. Weitere Informationen finden Sie unter [Tägliche Aufruf- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).

### Kann ich bedingte Liquid-Anweisungen in Agent-Anweisungen verwenden? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Nein. Der Versuch, Liquid-Blöcke wie {% raw %}`{% if %}`{% endraw %}-Anweisungen zu schreiben, kann zu einem Validierungsfehler führen. Agents können verschiedene Szenarien stattdessen über natürlichsprachliche Beschreibungen im Prompt abdecken.

### Können Agents auf Nutzerdaten zugreifen, die über die spezifischen Liquid-Attribute oder den Canvas-Kontext hinausgehen, die ich ihnen übergebe? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

Nein. Agents erhalten nur die spezifischen Datenpunkte, die über Liquid in den Anweisungen übergeben werden, über die Auswahl unter [+ Agent-Kontext]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources), über vorgelagerte [Kontext-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) in Canvas oder über zusätzlichen Kontext im Agent-Schritt. Agents können nicht in Nutzerprofilen nach Attributen suchen, für deren Empfang sie nicht konfiguriert wurden.

Agents können Sie auch nicht warnen, wenn erforderliche Daten fehlen – sie arbeiten mit dem, was im Prompt vorhanden ist. Behandeln Sie die Agent-Einrichtung als bewusstes Input-zu-Output-Design: Übergeben Sie jedes Feld, das der Agent benötigt, und überprüfen Sie die Eingaben unter **Agentenkonsole** > **Logs**. Weitere Hinweise finden Sie unter [Welche Daten Agents erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Fehlerbehebung {#troubleshooting}

### Warum hat mein Agent meine Anweisungen oder Regeln nicht befolgt? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Verwenden Sie [Operator]({{site.baseurl}}/user_guide/brazeai/operator), um herauszufinden, warum Ihr Agent Ihre Anweisungen nicht befolgt. Operator kann Schritt-für-Schritt-Anleitungen und detaillierte Erklärungen liefern.

### Warum hat mein Katalog-Agent einige Zeilen übersprungen? {#why-did-my-catalog-agent-skip-some-rows}

Katalog-Agents überspringen eine Zeile, wenn eine Spalte, die Sie als **zum Ausführen erforderlich** markiert haben, leer ist oder fehlt – beispielsweise ein `gender`-Feld, das noch nicht ausgefüllt wurde. Nachdem Sie Eingabespalten ausgewählt haben, aktivieren Sie die Pflichtfeld-Kontrolle für das Katalogfeld und legen fest, welche Spalten Werte enthalten müssen, bevor der Agent ausgeführt wird. Ausgewählte Spalten sind standardmäßig als erforderlich markiert, aber Sie können Spalten entfernen, die leer sein dürfen, ohne den Aufruf zu blockieren. So werden keine Token für unvollständige Daten verschwendet.

Der Agent berücksichtigt auch Spaltenabhängigkeiten. Wenn eine Ausgabespalte von anderen Spalten abhängt (z. B. Spalte D Werte in den Spalten B und C erfordert), wird der Agent für diese Zeile erst ausgeführt, wenn die vorgelagerten Spalten befüllt sind.

Weitere Informationen finden Sie unter [Best Practices für Katalog-Agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### Mein Agent hat Schwierigkeiten mit einer komplexen Aufgabe. Wie kann ich seine Performance verbessern? {#subagent-approach}

Wenn der Agent mit den gestellten Aufgaben Schwierigkeiten hat, ziehen Sie einen Sub-Agent-Ansatz in Betracht. Sie könnten beispielsweise drei Agents für folgende Aufgaben einsetzen:

- Agent 1 standardisiert und transformiert eingehende unstrukturierte Canvas-Kontextdaten.
- Agent 2 referenziert einen Katalog mit Artikeldetails und identifiziert, welche Artikel relevant sein könnten.
- Agent 3 referenziert einen anderen Katalog, der verschiedene mögliche Beschreibungen für jeden Artikel enthält, und wählt die für die/den Nutzer:in relevanteste Artikelbeschreibung für eine E-Mail aus.

### Was kann dazu führen, dass ein angepasster Agent häufig ein Timeout hat? {#what-might-cause-a-custom-agent-to-frequently-time-out}

Ein angepasster Agent kann ein Timeout haben, wenn:

- Die Agent-Anweisungen unvollständig oder widersprüchlich sind
- Die Agent-Anweisungen nicht alle Szenarien abdecken oder keine Fallback-Bedingung enthalten (z. B. „Wenn alle Eingaben leer sind, gib ‚Konnte nicht personalisieren' aus“)
- Die Agent-Anweisungen ein anderes Ausgabeformat verlangen als das im Tab **Ausgabe** festgelegte (z. B. wenn die Agent-Anweisungen einen String verlangen, aber im Tab **Ausgabe** die Ausgabe als Zahl definiert ist)
- Die Aufgabe des Agents zu komplex ist und von einem [Sub-Agent-Ansatz](#subagent-approach) profitieren würde

Konfigurieren Sie für Canvas-Schritt-Agents [Fallback-Werte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agentenkonsole, damit Nutzer:innen auch dann eine Ausgabe erhalten, wenn ein Aufruf fehlschlägt.

### Warum hat mein Agent im Test funktioniert, erhält aber nach dem Start in einem Canvas keine nutzerspezifischen Daten? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

Wenn Ihr Agent beim Testen korrekt funktioniert, aber in einem Live-Canvas keine nutzerspezifischen Daten erhält, versuchen Sie folgende Schritte zur Fehlerbehebung:

- Stellen Sie sicher, dass die nutzerspezifischen Daten, die der Agent erhalten soll, als Liquid-Variablen in den Agent-Anweisungen eingetragen sind.
- Wenn Sie wichtige Daten im Canvas-Kontext haben, verwenden Sie die Option **Gesamten Canvas-Kontext hinzufügen** in der Agent-Konfiguration, damit der Agent den vollständigen Canvas-Kontext erhält.
- Stellen Sie sicher, dass alle Daten, auf die der Agent zugreifen soll, als Canvas-Kontext gespeichert sind. Verwenden Sie einen Kontext-Schritt vor dem Agent-Schritt, um diese Daten zu speichern.

## Compliance {#compliance}

### Ist die Agentenkonsole DSGVO-/CCPA-konform? {#is-agent-console-gdprccpa-compliant}

Ja. Wenn Kund:innen das Braze Auto-Modell (basierend auf Gemini) verwenden, agiert Google als Braze-Unterauftragsverarbeiter, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen den Kund:innen und Braze.

### Ist die Agentenkonsole HIPAA-konform? {#is-agent-console-hipaa-compliant}

Ja. Bei Verwendung des Braze Auto-Modells haben wir eine spezifische HIPAA-Vereinbarung, den Business Associate Addendum (BAA), mit Google für Gemini abgeschlossen, das unser Auto-Modell betreibt.

Unser BAA gilt nur für Kund:innen, die das Braze Auto-Modell verwenden. Wenn Kund:innen ihren eigenen LLM-Schlüssel verwenden, sendet Braze keine geschützten Gesundheitsinformationen (PHI), die dem US-Gesetz zum Schutz medizinischer Daten (HIPAA) unterliegen, in ihrem Namen an ein LLM – die Kund:innen senden diese direkt. In diesem Fall gilt der BAA zwischen Braze und Google nicht. Die Datenverarbeitung über den eigenen LLM-Schlüssel unterliegt dem Vertrag der Kund:innen und etwaigen BAAs, die sie direkt mit ihrem LLM-Anbieter abgeschlossen haben.