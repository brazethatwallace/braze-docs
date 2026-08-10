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

Beim Erstellen eines Agents legen Sie fest, ob Sie einen Canvas-Schritt-Agent oder einen Katalog-Agent erstellen möchten. Dies bestimmt die Arten von Anweisungen und Optionen, die der Agent unterstützen kann. Canvas-Schritt-Agents verarbeiten Nutzer:innen in Echtzeit innerhalb von Journeys, während Katalog-Agents Katalogdaten anreichern, indem sie Spalten mit verarbeiteten Informationen hinzufügen oder aktualisieren.

### Welche Vorteile bietet das Auto-Modell gegenüber einem eigenen (BYO) Modell? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Vorteile des Braze Auto-Modells:

- Es sind keine API-Schlüssel oder Integrationseinrichtungen erforderlich
- Automatisches Routing jedes Aufrufs an das effektivste Modell für die jeweilige Aufgabe

### Wo kann ich meine aktuelle Agent-Nutzung einsehen? {#where-can-i-find-my-current-agent-usage}

Gehen Sie zu **Einstellungen** > **Abrechnung** > **Credits-Nutzung** > **Agent Console**, um den Credit-Verbrauch, die Anzahl der Aufrufe und die Credit-Verhältnisse pro Agent einzusehen. Weitere Details finden Sie unter [Tägliche Aufruf- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).

### Kann ich bedingte Liquid-Anweisungen in Agent-Instruktionen verwenden? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

Nein, der Versuch, Liquid-Blöcke wie {% raw %}`{% if %}{% endraw %}`-Anweisungen zu schreiben, kann zu einem Validierungsfehler führen. Agents können verschiedene Szenarien stattdessen durch natürlichsprachliche Beschreibungen im Prompt abdecken.

### Können Agents auf Nutzerdaten zugreifen, die über die spezifischen Liquid-Attribute oder den Canvas-Kontext hinausgehen, die ich ihnen übergebe? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

Nein. Agents erhalten nur die spezifischen Nutzerdatenpunkte, die über Liquid in den Instruktionen, die Auswahl unter [+ Agent-Kontext]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources), vorgelagerte [Kontext-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) in Canvas oder zusätzlichen Kontext im Agent-Schritt übergeben werden. Agents können keine Nutzerprofile nach Attributen durchsuchen, für deren Empfang Sie sie nicht konfiguriert haben.

Agents können Sie auch nicht warnen, wenn erforderliche Daten fehlen – sie arbeiten mit dem, was im Prompt vorhanden ist. Behandeln Sie die Agent-Einrichtung als bewusstes Input-zu-Output-Design: Übergeben Sie jedes Feld, das der Agent benötigt, und überprüfen Sie die Eingaben unter **Agent Console** > **Logs**. Weitere Hinweise finden Sie unter [Welche Daten Agents erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

## Fehlerbehebung {#troubleshooting}

### Warum hat mein Agent meine Anweisungen oder Regeln nicht befolgt? {#why-did-my-agent-not-follow-my-instructions-or-rules}

Verwenden Sie [Operator]({{site.baseurl}}/user_guide/brazeai/operator), um herauszufinden, warum Ihr Agent Ihre Anweisungen nicht befolgt. Operator kann schrittweise Anleitungen und detaillierte Erklärungen liefern.

### Warum hat mein Catalog-Agent einige Zeilen übersprungen? {#why-did-my-catalog-agent-skip-some-rows}

Catalog-Agents überspringen eine Zeile, wenn eine Spalte, die Sie als **für die Ausführung erforderlich** markiert haben, leer ist oder fehlt – zum Beispiel ein `gender`-Feld, das nicht ausgefüllt wurde. Nachdem Sie Eingabespalten ausgewählt haben, aktivieren Sie die Pflichtfeld-Steuerung für das Katalogfeld und wählen Sie aus, welche Spalten Werte enthalten müssen, bevor der Agent ausgeführt wird. Ausgewählte Spalten sind standardmäßig als erforderlich markiert, aber Sie können Spalten entfernen, die leer sein dürfen, ohne die Ausführung zu blockieren. So werden keine Token für unvollständige Daten verschwendet.

Der Agent berücksichtigt auch Spaltenabhängigkeiten. Wenn eine Ausgabespalte von anderen Spalten abhängt (zum Beispiel erfordert Spalte D Werte in den Spalten B und C), wird der Agent erst ausgeführt, wenn diese vorgelagerten Spalten für die jeweilige Zeile befüllt sind.

Weitere Details finden Sie unter [Best Practices für Catalog-Agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

### Verbrauchen fehlgeschlagene Agent-Aufrufe Credits? {#do-failed-agent-invocations-consume-credits}

Das hängt von der Art des Fehlers ab:

| Fehler | Verbraucht Credits? |
| --- | --- |
| Rate-Limit-Fehler | Nein |
| Modell nicht verfügbar | Nein |
| Tägliches Aufruflimit erreicht | Nein |
| Timeout | Ja |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verbrauchen fehlgeschlagene Agent-Aufrufe Credits?" }

Weitere Informationen finden Sie unter [Wann Credits verbraucht werden]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

### Mein Agent hat Schwierigkeiten mit einer komplexen Aufgabe. Wie kann ich seine Performance verbessern? {#subagent-approach}

Wenn Sie feststellen, dass der Agent mit den gestellten Aufgaben Schwierigkeiten hat, ziehen Sie einen Sub-Agent-Ansatz in Betracht. Sie könnten beispielsweise drei Agents verwenden, um Folgendes zu tun:

- Agent 1 standardisiert und transformiert eingehende unstrukturierte Canvas-Kontextdaten.
- Agent 2 referenziert einen Katalog mit Artikeldetails und identifiziert, welche Artikel relevant sein könnten.
- Agent 3 referenziert einen anderen Katalog, der verschiedene mögliche Beschreibungen für jeden Artikel enthält, und identifiziert die für die Nutzer:innen relevanteste Artikelbeschreibung zur Verwendung in einer E-Mail.

### Was kann dazu führen, dass ein angepasster Agent häufig ein Timeout hat? {#what-might-cause-a-custom-agent-to-frequently-time-out}

Ein angepasster Agent kann ein Timeout haben, wenn:

- Die Agent-Anweisungen unvollständig oder widersprüchlich sind
- Die Agent-Anweisungen nicht alle Szenarien abdecken oder keine Fallback-Bedingung enthalten (wie „Wenn alle Eingaben leer sind, gib ‚Konnte nicht personalisieren' aus“)
- Die Agent-Anweisungen den Agent auffordern, ein anderes Ausgabeformat als das im Tab **Output** angegebene zu verwenden (zum Beispiel, wenn die Agent-Anweisungen einen String verlangen, aber im Tab **Output** die Ausgabe als Zahl definiert ist)
- Die Aufgabe des Agents zu komplex ist und von einem [Sub-Agent-Ansatz](#subagent-approach) profitieren würde

#### So reduzieren Sie Timeouts {#how-to-reduce-timeouts}

Wenn Ihr Agent häufig Timeouts hat, versuchen Sie Folgendes, bevor Sie Ihren Account Manager wegen eines höheren Timeout-Limits kontaktieren:

- **Wählen Sie ein einfacheres oder kostengünstigeres Modell:** Schnellere Modelle werden in der Regel innerhalb des Standard-Timeout-Fensters fertig. Siehe [Bestimmen, welches Modell verwendet werden soll]({{site.baseurl}}/user_guide/brazeai/agents/reference#determine-which-model-to-use).
- **Senken Sie das Thinking-Level (nur BYO-Modelle):** Beginnen Sie mit **Minimal** und erhöhen Sie nur, wenn die Ausgabequalität leidet. Siehe [Thinking-Levels]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels).
- **Vereinfachen Sie den Prompt:** Entfernen Sie redundante Anweisungen, kürzen Sie Beispiele und schränken Sie das Ausgabeschema ein. Verwenden Sie [Operator]({{site.baseurl}}/user_guide/brazeai/operator), um Ihre Anweisungen zu überprüfen und zu optimieren.
- **Teilen Sie komplexe Workflows in mehrere Agents auf:** Wenn der Anwendungsfall mehrere Teilschritte umfasst (zum Beispiel Absicht klassifizieren, dann Text generieren), verwenden Sie separate Agents nacheinander in Canvas oder im Katalog, anstatt einen einzelnen Agent für alles einzusetzen. Siehe [Sub-Agent-Ansatz](#subagent-approach).

{% alert note %}
Timeouts verbrauchen Braze-Credits, auch wenn der Agent keine verwertbare Ausgabe liefert. Siehe [Wann Credits verbraucht werden]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).
{% endalert %}

Konfigurieren Sie für Canvas-Schritt-Agents [Fallback-Werte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agent Console, damit Nutzer:innen auch dann eine Ausgabe erhalten, wenn ein Aufruf fehlschlägt.

### Warum hat mein Agent beim Testen gut funktioniert, erhält aber keine nutzerspezifischen Daten, wenn ich ihn in einem Canvas starte? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

Wenn Ihr Agent beim Testen korrekt funktioniert, aber in einem Live-Canvas keine nutzerspezifischen Daten erhält, versuchen Sie diese Schritte zur Fehlerbehebung:

- Stellen Sie sicher, dass die nutzerspezifischen Daten, die der Agent erhalten soll, als Liquid-Variablen in den Agent-Anweisungen eingetragen sind.
- Wenn Sie wichtige Daten im Canvas-Kontext haben, verwenden Sie die Option **Add all Canvas context** in der Agent-Konfiguration, um sicherzustellen, dass der Agent den gesamten Canvas-Kontext erhält.
- Stellen Sie sicher, dass alle Canvas-Kontextdaten, auf die der Agent zugreifen soll, als Canvas-Kontext gespeichert sind. Verwenden Sie einen Kontextschritt vor dem Agent-Schritt, um diese Daten zu speichern.

## Compliance {#compliance}

### Ist Agent Console DSGVO-/CCPA-konform? {#is-agent-console-gdprccpa-compliant}

Ja. Wenn Kund:innen das Braze-Auto-Modell (basierend auf Gemini) verwenden, agiert Google als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen den Kund:innen und Braze.

### Ist Agent Console HIPAA-konform? {#is-agent-console-hipaa-compliant}

Ja. Bei Verwendung des Braze-Auto-Modells haben wir eine spezifische HIPAA-Vereinbarung, den Business Associate Addendum (BAA), mit Google abgeschlossen, der Gemini abdeckt, das unser Auto-Modell antreibt.

Unser BAA gilt nur für Kund:innen, die das Braze-Auto-Modell verwenden. Wenn Kund:innen ihren eigenen LLM-Schlüssel verwenden, sendet Braze keine geschützten Gesundheitsinformationen (PHI), die dem US-Gesetz zum Schutz medizinischer Daten (HIPAA) unterliegen, in ihrem Auftrag an ein LLM; die Kund:innen senden diese direkt. In diesem Fall gilt der BAA zwischen Braze und Google nicht. Die Datenverarbeitung über ihren eigenen LLM-Schlüssel unterliegt dem Vertrag der Kund:innen und einem etwaigen BAA, das sie direkt mit ihrem LLM-Anbieter abgeschlossen haben.