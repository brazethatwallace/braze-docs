---
nav_title: Campaign-QA-Agent
article_title: Campaign-QA-Agent
permalink: /campaign_qa_agent/
description: "Dieser Referenzartikel behandelt Campaign-QA-Agents, einschließlich ihrer Funktionsweise und Best Practices."
hidden: true
---

# Campaign-QA-Agent

> Campaign-QA-Agents sind KI-gestützte Helfer, die automatisierte Prüfungen Ihrer Campaign-Konfiguration durchführen. Diese Agents fungieren als letzte Sicherheitsinstanz und validieren Ihr Setup anhand von Markenrichtlinien, organisatorischen Konventionen und technischen Anforderungen, bevor Sie starten.

Durch den Einsatz von Campaign-QA-Agents können Sie den manuellen Prüfaufwand reduzieren und sicherstellen, dass jede über die Braze-Plattform gesendete Nachricht korrekt, konform und startbereit ist.

{% alert important %}
Campaign-QA-Agents für die Agentenkonsole befinden sich derzeit in der Betaphase. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an dieser Beta teilnehmen möchten.
{% endalert %}

## Funktionsweise {#how-it-works}

Wenn Sie einen Campaign-QA-Agent erstellen, definieren Sie spezifische Regeln, die in „Regelsets“ gruppiert sind und die der Agent zur Bewertung einer Campaign verwendet. Sie können aus vorgefertigten Regelsets für gängige Marketing-Anforderungen wählen oder benutzerdefinierte Regeln erstellen, die auf Ihr Team zugeschnitten sind.

Nach der Konfiguration können Sie den Agent im Vorschaubereich gegen jede bestehende Campaign in Ihrem Workspace testen. Der Agent erstellt einen detaillierten Bericht und kategorisiert seine Ergebnisse in „Bestanden“, „Warnung“ oder „Fehlgeschlagen“.

## Einen Campaign-QA-Agent erstellen {#create-a-campaign-qa-agent}

### 1. Schritt: Agent-Typ auswählen {#step-1-choose-the-agent-type}

Um Ihren Agent zu erstellen, gehen Sie zu **Agentenkonsole** > **Agentenmanagement**. Wählen Sie **Agent erstellen** und wählen Sie **Campaign QA** aus dem Dropdown-Menü.

### 2. Schritt: Details einrichten {#step-2-set-up-details}

Richten Sie als Nächstes die Details für Ihren Agent ein:

1. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team den Zweck versteht.
2. (Optional) Fügen Sie Tags hinzu, um Ihren Agent zu filtern.
3. Wählen Sie das Modell, das Ihr Agent verwenden soll. Dieses steuert die Logik des Agents.

![Ein Campaign-QA-Agent „Campaign QA for copy“, der die Qualität der Campaign-Nachricht prüft und das Braze-Auto-Modell verwendet.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### 3. Schritt: Anweisungen und Regeln konfigurieren {#step-3-configure-instructions-and-rules}

Definieren Sie im Tab **Anweisungen** die Regeln, die der Agent prüft. Sie können bis zu 10 Regelsets pro Agent und bis zu 20 Regeln pro Regelset hinzufügen.

1. Wählen Sie **Regelset hinzufügen**, um eine Liste der folgenden Kategorien anzuzeigen:

- **Campaign-Setup:** Validiert Namenskonventionen, Tags und Conversion-Tracking.
- **Zielgruppe und Targeting:** Prüft Segmente, Ausschlüsse und Zielgruppengröße.
- **Inhalt und Text:** Bewertet Textqualität, Zeichenlimits und Nachrichtenvollständigkeit.
- **Links und Tracking:** Überprüft URLs, CTAs, Deeplinks und UTM-Parameter.
- **Personalisierung und dynamischer Content:** Prüft Liquid-Logik und Fallback-Werte.
- **Compliance und Zustellbarkeit:** Stellt sicher, dass rechtliche Anforderungen und Versandschutzmaßnahmen eingehalten werden.
- **Mit Operator generieren:** Wenn Sie sich nicht sicher sind, wie Sie eine Regel formulieren sollen, wählen Sie „Mit Operator generieren“, damit unser KI-Assistent Ihnen hilft, spezifische Logik basierend auf Ihren Anforderungen zu entwerfen.
- **Benutzerdefinierte Regeln:** Wählen Sie „Benutzerdefiniertes Regelset erstellen“, um individuelle Prüfungen zu definieren, die nicht eindeutig in eine der vorkonfigurierten Kategorien passen.

![Sechs Regeln, die für die Kategorie „Inhalt und Text“ eingerichtet sind.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### 4. Schritt: Ihren Agent testen {#step-4-test-your-agent}

Bevor Sie Ihren Agent bereitstellen, verwenden Sie den **Vorschau**-Bereich, um eine Antwort zu simulieren und zu bestätigen, dass die Logik wie erwartet funktioniert.

1. Wählen Sie eine bestehende Campaign aus dem Dropdown-Menü als Testfall aus.
2. Wählen Sie, ob alle Regelsets oder ein bestimmtes getestet werden sollen.
3. Wählen Sie den Button **Antwort simulieren**.

Überprüfen Sie anschließend die Ergebnisse. Der Agent bewertet die Campaign und zeigt die Ergebnisse in den folgenden Kategorien an:

- **Bestanden:** Diese Regeln wurden erfolgreich erfüllt. Beispielsweise könnte der Agent bestätigen, dass Ihre Namenskonventionen den erwarteten Mustern entsprechen.
- **Warnung:** Dies sind nicht-kritische Probleme, die möglicherweise Aufmerksamkeit erfordern. Wenn Sie beispielsweise ein E-Mail-Regelset gegen eine Webhook-Campaign testen, kann der Agent eine Warnung ausgeben, dass Absendernamen nicht zutreffen.
- **Fehlgeschlagen:** Dies sind kritische Probleme, die vor dem Start behoben werden sollten. Beispiele sind geplante Daten, die in der Vergangenheit liegen, oder fehlende erforderliche organisatorische Tags.

## Campaign-QA-Agents verwenden {#use-campaign-qa-agents}

Nachdem Sie einen Campaign-QA-Agent konfiguriert haben, können Sie ihn verwenden, um jede Campaign während des abschließenden Überprüfungsprozesses zu auditieren. Dies stellt sicher, dass Ihre Campaign alle Anforderungen erfüllt, bevor sie an Ihre Nutzer:innen gesendet wird.

### Ein Audit durchführen {#run-an-audit}

Um eine automatisierte Prüfung durchzuführen, gehen Sie zum Schritt **Zusammenfassung überprüfen** in Ihrem Campaign-Erstellungsworkflow.

1. Gehen Sie zum Abschnitt **QA-Agent** und wählen Sie den gewünschten Agent aus dem Dropdown-Menü.
3. Wählen Sie **QA-Agent ausführen**.

Wenn Sie nach einer ersten Prüfung Änderungen an Ihrer Campaign vornehmen, können Sie **QA-Agent erneut ausführen** wählen, um die Ergebnisse zu aktualisieren.

### Audit-Ergebnisse überprüfen {#review-audit-results}

Nach Abschluss der Bewertung liefert der Agent eine Zusammenfassung seiner Ergebnisse, kategorisiert in diese Tabs: **Bestanden**, **Fehlgeschlagen** und **Warnung**.

Der Tab **Fehlgeschlagen** listet Regeln auf, die nicht erfüllt wurden. Für jeden Fehler liefert der Agent:

- **Regel:** Die spezifischen Kriterien, die geprüft werden, wie z. B. „Rechtschreibung und Grammatik prüfen“.
- **Begründung:** Eine detaillierte Erklärung, warum die Prüfung fehlgeschlagen ist. Beispielsweise könnte der Agent feststellen, dass „personalized“ anstelle der australisch-englischen Schreibweise „personalised“ verwendet wurde.
- **Direkte Korrekturen:** Spezifische Text- oder Konfigurationsänderungen, die der Agent zur Behebung des Problems vorschlägt.

Der Tab **Bestanden** listet alle Regeln auf, die Ihre Campaign erfolgreich eingehalten hat. Dies bestätigt, dass Prüfungen wie **Erkennung anstößiger Sprache** oder **Validierung der Namenskonvention** bestanden wurden.

Der Tab **Warnung** listet nicht-kritische Probleme auf, die möglicherweise Aufmerksamkeit erfordern. Wenn Sie beispielsweise ein E-Mail-Regelset gegen eine Webhook-Campaign testen, kann der Agent eine Warnung ausgeben, dass Absendernamen nicht zutreffen.

### Probleme beheben oder ignorieren {#resolve-or-ignore-issues}

Für jeden identifizierten Fehler oder jede Warnung können Sie vor dem Start entscheiden, wie Sie vorgehen möchten. Wählen Sie **Beheben** neben einem Problem und wählen Sie dann aus den folgenden Optionen:

- **Ich habe das Problem behoben:** Wählen Sie dies, nachdem Sie Ihre Campaign-Konfiguration oder Ihren Text basierend auf dem Feedback des Agents aktualisiert haben.
- **Dieses Problem ignorieren:** Wählen Sie dies, um eine Ausnahme von der Regel zu machen. Dies ist nützlich für beabsichtigte Abweichungen oder Grenzfälle, in denen der Vorschlag des Agents möglicherweise nicht zutrifft.

Nachdem alle kritischen Probleme behoben oder ignoriert wurden, können Sie mit dem Start Ihrer Campaign fortfahren.

## Best Practices

- **Mit Templates beginnen:** Verwenden Sie zuerst die vorgefertigten Regelsets für Campaign-Setup und Links und Tracking, da diese die häufigsten manuellen Fehler abdecken und sicherstellen, dass der Agent den richtigen Kontext für die Prüfung hat.
- **Seien Sie spezifisch:** Geben Sie beim Schreiben benutzerdefinierter Regeln klare Beispiele dafür, wie „korrekt“ aussieht. Anstatt beispielsweise „Namenskonvention prüfen“ zu schreiben, versuchen Sie „Stellen Sie sicher, dass der Campaign-Name mit dem aktuellen Jahr beginnt (z. B. 2026_).“
- **Regelmäßig iterieren:** Wenn sich Ihre Markenrichtlinien oder internen Prozesse ändern, aktualisieren Sie die Regelsets Ihres Campaign-QA-Agents, um Ihre automatisierten Prüfungen relevant zu halten.