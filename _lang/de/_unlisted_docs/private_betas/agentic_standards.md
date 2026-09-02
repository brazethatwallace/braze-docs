---
nav_title: Agentic Standards
article_title: Agentic Standards
permalink: /campaign_qa_agent/
description: "Dieser Referenzartikel behandelt Agentic Standards, einschließlich der Funktionsweise von Campaign Standards und Best Practices."
hidden: true
---

# Agentic Standards

> Agentic Standards sind Regeln und Regelsätze zur Durchsetzung von Unternehmensrichtlinien und Leitplanken für Campaigns in Braze. Sie werden von Operator während des Erstellungs- und Bearbeitungsprozesses befolgt. Diese Standards können agentisch ausgewertet werden, bevor eine Campaign gestartet wird, und dienen als letzter Schutz zur Validierung gegenüber Markenrichtlinien, organisatorischen Konventionen und technischen Anforderungen vor dem Start.

Agentic Standards reduzieren den manuellen Überwachungsaufwand, sodass jede von Braze gesendete Nachricht korrekt, regelkonform und startbereit ist.

{% alert important %}
Agentic Standards für Agent Console befinden sich derzeit in der Betaphase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie an dieser Beta teilnehmen möchten.
{% endalert %}

## Funktionsweise {#how-it-works}

Wenn Sie einen Campaign Standard erstellen, definieren Sie spezifische Regeln, die in „Regelsätze“ gruppiert sind und die Operator vor dem Start einer Campaign befolgt und auswertet. Sie können aus vorgefertigten Regelsätzen für gängige Marketinganforderungen wählen oder angepasste Regeln erstellen, die auf Ihr Team zugeschnitten sind.

Nach der Konfiguration können Sie den Campaign Standard im Bereich **Evaluation preview** gegen jede bestehende Campaign in Ihrem Workspace testen. Die agentische Auswertung liefert einen detaillierten Bericht mit Kategorien der Ergebnisse.

## Einen Campaign Standard erstellen {#create-a-campaign-standard}

### Schritt 1: Standard-Typ auswählen {#step-1-choose-the-standard-type}

Um Ihren Standard zu erstellen, gehen Sie zu **Agent Console** > **Agentic Standards**. Wählen Sie **Create Agentic Standard** und dann **Campaign Standards** aus dem Dropdown-Menü.

### Schritt 2: Details einrichten {#step-2-set-up-details}

Richten Sie als Nächstes die Details für Ihren Standard ein:

1. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team den Zweck versteht.
2. (Optional) Fügen Sie Tags hinzu, um Ihren Standard zu filtern.
3. Wählen Sie das Auswertungsmodell, das Ihr Standard verwenden soll. Dieses treibt die agentische Auswertung eines Standards an.

![Ein Campaign Standard „Abandoned Cart Campaign Standards“, der die Regeln und Regelsätze für Warenkorb-Abbruch-Campaigns in Braze definiert.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_details.png %}){: style="max-width:80%;"}

### Schritt 3: Campaign-Regeln konfigurieren {#step-3-configure-campaign-rules}

Im Schritt **Campaign Rules** definieren Sie die Regeln, die als Teil dieses Standards durchgesetzt werden sollen. Sie können bis zu 10 Regelsätze pro Standard und bis zu 20 Regeln pro Regelsatz hinzufügen.

Wählen Sie **Add ruleset**, um eine Liste der folgenden Kategorien zu sehen:

- **Campaign setup:** Validiert Namenskonventionen, Tags und Conversion-Tracking.
- **Audience and targeting:** Prüft Segmente, Ausschlüsse und Zielgruppengröße.
- **Content and copy:** Definiert Anforderungen an Textqualität, Zeichenlimits und Nachrichtenvollständigkeit.
- **Links and tracking:** Überprüft URLs, CTAs, Deeplinks und UTM-Parameter.
- **Personalization and dynamic content:** Definiert Prüfungen für Liquid-Logik und Fallback-Werte.
- **Compliance and deliverability:** Definiert Anforderungen an rechtliche Pflichten und Versandschutzmaßnahmen.
- **Custom rules:** Wählen Sie **Create custom ruleset**, um individuelle Anforderungen zu definieren, die nicht eindeutig in eine der vorkonfigurierten Kategorien passen.

Wenn Sie nicht sicher sind, wie Sie eine Regel formulieren sollen, wählen Sie **Generate with Operator**, damit Operator Ihnen hilft, basierend auf Ihren Anforderungen eine spezifische Logik zu entwerfen.

![Vier Regeln, die für die Kategorie „Audience and targeting“ eingerichtet wurden.]({% image_buster /assets/unlisted_docs/img/campaign_qa_agent/campaign_qa_instructions.png %}){: style="max-width:80%;"}

### Schritt 4: Ihren Standard testen {#step-4-test-your-standard}

Bevor Sie Ihren Standard für Campaigns in Braze verwenden, nutzen Sie den Bereich **Evaluation preview**, um eine agentische Auswertung zu simulieren.

1. Wählen Sie eine bestehende Campaign aus dem Dropdown-Menü als Testfall aus.
2. Wählen Sie, ob alle Regelsätze oder ein bestimmter getestet werden sollen.
3. Wählen Sie den Button **Simulate response**.

Überprüfen Sie anschließend die Ergebnisse. Die Auswertung wird gegen die Campaign durchgeführt und zeigt die Ergebnisse in den folgenden Kategorien an:

- **Pass:** Diese Regeln wurden erfolgreich erfüllt. Zum Beispiel kann die Auswertung bestätigen, dass Ihre Namenskonventionen den erwarteten Mustern entsprechen.
- **Warning:** Dies sind nicht kritische Probleme, die möglicherweise Aufmerksamkeit erfordern. Wenn Sie beispielsweise einen E-Mail-Regelsatz gegen eine Webhook-Campaign testen, kann die agentische Auswertung eine Warnung ausgeben, dass Sendernamen nicht zutreffen.
- **Fail:** Dies sind kritische Probleme, die vor dem Start behoben werden sollten. Beispiele sind geplante Daten, die in der Vergangenheit liegen, oder fehlende erforderliche organisatorische Tags.

## Agentic Standards verwenden {#use-agentic-standards}

Nachdem Sie einen Campaign Standard konfiguriert haben, können Sie ihn verwenden, um jede Campaign während des finalen Überprüfungsprozesses auszuwerten. Dies bestätigt, dass Ihre Campaign alle Anforderungen erfüllt, bevor sie an Ihre Nutzer:innen gesendet wird.

### Eine Auswertung durchführen {#run-an-evaluation}

Um eine automatisierte Auswertung durchzuführen, gehen Sie zum Schritt **Review Summary** Ihres Campaign-Erstellungsworkflows.

1. Gehen Sie zum Bereich **Agentic Standards** und wählen Sie Ihren gewünschten Standard aus dem Dropdown-Menü.
2. Wählen Sie **Run evaluation**.

Wenn Sie nach einer ersten Auswertung Änderungen an Ihrer Campaign vornehmen, wählen Sie **Re-run evaluation**, um die Ergebnisse zu aktualisieren.

### Auswertungsergebnisse überprüfen {#review-evaluation-results}

Nach Abschluss der Auswertung zeigt eine Zusammenfassung die Ergebnisse in diesen Kategorien an: **Pass**, **Fail** und **Warning**.

Der Tab **Fail** listet Regeln auf, die nicht erfüllt wurden. Für jede nicht bestandene Prüfung liefert der Standard Folgendes:

- **Rule:** Die spezifischen Kriterien, die geprüft werden, wie z. B. „Spelling & Grammar Check“.
- **Reason:** Eine Erklärung, warum die Prüfung fehlgeschlagen ist. Zum Beispiel könnte die Auswertung feststellen, dass „personalized“ anstelle der australisch-englischen Schreibweise „personalised“ verwendet wurde.

Der Tab **Pass** listet alle Regeln auf, die Ihre Campaign erfolgreich befolgt hat. Dies bestätigt, dass Prüfungen wie **Offensive Language Detection** oder **Naming Convention Validation** bestanden wurden.

Der Tab **Warning** listet nicht kritische Probleme auf, die möglicherweise Aufmerksamkeit erfordern. Wenn Sie beispielsweise einen E-Mail-Regelsatz gegen eine Webhook-Campaign testen, kann die Auswertung des Standards eine Warnung ausgeben, dass Sendernamen nicht zutreffen.

### Probleme beheben oder ignorieren {#resolve-or-ignore-issues}

Für jede identifizierte nicht bestandene Prüfung oder Warnung können Sie vor dem Start entscheiden, wie Sie vorgehen möchten. Wählen Sie **Resolve** neben einem Problem und dann eine der folgenden Optionen:

- **Mark as fixed:** Wählen Sie dies, nachdem Sie Ihre Campaign-Konfiguration oder Ihren Text basierend auf dem Auswertungsvorschlag aktualisiert haben.
- **Ignore this issue:** Wählen Sie dies, um das Problem nur für diesen Durchlauf zu überspringen. Dies ist nützlich für beabsichtigte Abweichungen oder Grenzfälle, bei denen der Auswertungsvorschlag möglicherweise nicht zutrifft.
- **Ask BrazeAI Operator:** Wählen Sie dies, um das Problem mithilfe von Operator zu beheben.

Nachdem alle kritischen Probleme behoben oder ignoriert wurden, können Sie mit dem Start Ihrer Campaign fortfahren.

## Beste Praktiken {#best-practices}

- **Beginnen Sie mit Templates:** Verwenden Sie zuerst die vorgefertigten Regelsätze für Campaign-Setup und Links und Tracking, da diese die häufigsten manuellen Fehler abdecken und der agentischen Auswertung den richtigen Kontext geben.
- **Seien Sie spezifisch:** Wenn Sie angepasste Regeln schreiben, geben Sie klare Beispiele dafür, wie „korrekt“ aussieht. Schreiben Sie zum Beispiel statt „Überprüfe die Namenskonvention“ lieber „Der Campaign-Name beginnt mit dem aktuellen Jahr (z. B. 2026_).“
- **Iterieren Sie häufig:** Wenn sich Ihre Markenrichtlinien oder internen Prozesse ändern, aktualisieren Sie Ihre Campaign-Standard-Regelsätze, um Ihre automatisierten Prüfungen relevant zu halten.