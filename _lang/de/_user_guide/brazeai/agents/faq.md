---
nav_title: FAQ
article_title: Agents – FAQ
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Braze Agents."
page_order: 10
---

# Agents – Häufig gestellte Fragen {#agents-frequently-asked-questions}

> Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Braze Agents.

## Allgemein {#general}

### Was ist der Unterschied zwischen Canvas-Agents und Katalog-Agents? {#what-is-the-difference-between-canvas-agents-and-catalog-agents}

Beim Erstellen eines Agents legen Sie fest, ob Sie einen Canvas-Agent oder einen Katalog-Agent erstellen möchten. Dies bestimmt, welche Arten von Anweisungen und Optionen der Agent unterstützen kann. Canvas-Agents verarbeiten Nutzer:innen in Realtime innerhalb von Journeys, während Katalog-Agents Katalogdaten anreichern, indem sie Spalten mit verarbeiteten Informationen hinzufügen oder aktualisieren.

### Welche Vorteile bietet das Auto-Modell im Vergleich zum Bring-your-own-Modell (BYO)? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Vorteile des Braze Auto-Modells:

- Es sind keine API-Schlüssel, kein Abrufen von Zugangsdaten und kein Integrations-Setup erforderlich.
- Jeder Aufruf wird automatisch an das effektivste Modell für die jeweilige Aufgabe weitergeleitet.

### Wo kann ich meine aktuelle Agent-Nutzung einsehen? {#where-can-i-find-my-current-agent-usage}

Gehen Sie zu **Einstellungen** > **Abrechnung** > **Credit-Nutzung**, um Details zu Ihrer Agent-Nutzung und den Credit-Kosten einzusehen.

### Kann ich bedingte Liquid-Anweisungen in Agent-Anweisungen verwenden? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Nein. Der Versuch, Liquid-Blöcke wie {% raw %}`{% if %}`{% endraw %}-Anweisungen zu schreiben, kann zu einem Validierungsfehler führen. Agents können verschiedene Szenarien stattdessen über natürlichsprachliche Beschreibungen im Prompt abdecken.

### Können Agents auf Nutzerdaten zugreifen, die über die spezifischen Liquid-Attribute oder -Werte hinausgehen, die ich ihnen übergebe? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-values-that-i-pass-to-them}

Nein. Agents erhalten nur die spezifischen Datenpunkte, die ihnen über Liquid übergeben werden, sowie [Ressourcen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#add-resources), die dem Agent-Kontext hinzugefügt wurden. Agents können nicht in Nutzerprofilen nach Attributen suchen, für deren Abfrage sie vom Marketer nicht konfiguriert wurden.

## Fehlerbehebung {#troubleshooting}

### Warum hat mein Agent meine Anweisungen oder Regeln nicht befolgt? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Verwenden Sie [Operator]({{site.baseurl}}/user_guide/brazeai/operator/), um herauszufinden, warum Ihr Agent Ihre Anweisungen nicht befolgt. Operator kann Schritt-für-Schritt-Anleitungen und detaillierte Erklärungen liefern.

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

## Compliance {#compliance}

### Ist die Agentenkonsole DSGVO-/CCPA-konform? {#is-agent-console-gdprccpa-compliant}

Ja. Wenn Kund:innen das Braze Auto-Modell (basierend auf Gemini) verwenden, agiert Google als Braze-Unterauftragsverarbeiter, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen den Kund:innen und Braze.

### Ist die Agentenkonsole HIPAA-konform? {#is-agent-console-hipaa-compliant}

Ja. Bei Verwendung des Braze Auto-Modells haben wir eine spezifische HIPAA-Vereinbarung, den Business Associate Addendum (BAA), mit Google für Gemini abgeschlossen, das unser Auto-Modell betreibt.

Unser BAA gilt nur für Kund:innen, die das Braze Auto-Modell verwenden. Wenn Kund:innen ihren eigenen LLM-Schlüssel verwenden, sendet Braze keine geschützten Gesundheitsinformationen (PHI), die dem US-Gesetz zum Schutz medizinischer Daten (HIPAA) unterliegen, in ihrem Namen an ein LLM – die Kund:innen senden diese direkt. In diesem Fall gilt der BAA zwischen Braze und Google nicht. Die Datenverarbeitung über den eigenen LLM-Schlüssel unterliegt dem Vertrag der Kund:innen und etwaigen BAAs, die sie direkt mit ihrem LLM-Anbieter abgeschlossen haben.