---
nav_title: Agenten bereitstellen
article_title: Angepasste Agenten bereitstellen
description: "Erfahren Sie, wie Sie angepasste Agenten in Braze einsetzen können, nachdem Sie diese erstellt haben."
alias: /deploying-agents/
page_order: 2
---

# Angepasste Agenten bereitstellen {#deploy-custom-agents}

> Nachdem Sie [einen Agenten erstellt]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) haben, erfahren Sie auf dieser Seite, wo und wie Sie ihn in Braze bereitstellen können. Der Agententyp, den Sie bei der Erstellung wählen – Canvas-Agent oder Katalog-Agent – bestimmt, wo der Agent ausgeführt werden kann. Eine Einführung finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents).

## Typen benutzerdefinierter Agents {#types-of-custom-agents}

Benutzerdefinierte Agents werden je nach Typ in verschiedenen Bereichen von Braze bereitgestellt. Verwenden Sie die folgende Tabelle, um den richtigen Bereitstellungspfad für Ihren Agent zu finden.

| Agent-Typ | Bereitgestellt in | Wird ausgeführt, wenn | Abschnitt |
| --- | --- | --- | --- |
| Canvas-Schritt-Agent | [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) in Canvas | Ein:e Nutzer:in den Schritt betritt | [Canvas-Schritt-Agents verwenden](#use-canvas-step-agents) |
| Katalog-Agent | Katalogfeld | Eine Katalogreihe erstellt oder aktualisiert wird | [Katalog-Agents verwenden](#use-catalog-agents) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Typen benutzerdefinierter Agents" }

Sie wählen den Agent-Typ in der **Agent Console** aus, wenn Sie den Agent erstellen. Die Einrichtungsschritte finden Sie unter [Benutzerdefinierte Agents erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-1-choose-an-agent-type).

## Best Practices {#best-practices}

Konzentrieren Sie sich auf hochwertige Anwendungsfälle, bei denen Agents die größte Kapitalrendite (Kapitalrendite) erzielen können, und wählen Sie Zielgruppen aus, die wahrscheinlich reagieren werden. Eine kleinere Zielgruppe mit hoher Opportunity übertrifft oft eine große Zielgruppe mit geringer Opportunity.

Beginnen Sie bei Canvas-Schritt-Agents mit Nutzer:innen, die starke Signale aufweisen – wie kürzliche Suchanfragen, hohes Engagement oder umfangreiche Profildaten – bevor Sie auf breitere Segmente ausweiten. Priorisieren Sie bei Catalog-Agents Zeilen, in denen die benötigten Eingabespalten bereits befüllt sind, damit jeder Aufruf genügend Kontext hat, um nützliche Ergebnisse zu liefern.

Um die Kapitalrendite in kleinem Maßstab zu testen, bevor Sie einen Agent breit ausrollen, verwenden Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, sodass nur ein Teil Ihrer Zielgruppe den Branch betritt, der Ihren Agent-Schritt enthält.

### Nach einem erfolgreichen Test skalieren {#scale-after-a-successful-test}

Nachdem ein Test in kleinem Maßstab (zum Beispiel ein [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Branch) akzeptable Qualität und Kapitalrendite gezeigt hat, planen Sie den Rollout des Agents auf Ihre gesamte Zielgruppe (nicht nur die Testgruppe), damit alle berechtigten Nutzer:innen davon profitieren.

Bevor Sie skalieren, beachten Sie Folgendes:

- Erhöhen Sie das tägliche Aufruf-Limit des Agents in der Agent Console, damit er das volle Zielgruppenvolumen bewältigen kann. Der Standardwert beträgt 250.000; Sie können ihn auf bis zu 1.000.000 erhöhen (oder mit Ihrem CSM auf einen höheren Wert). Siehe [Tägliche Aufruf- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Überprüfen Sie die Schätzung des **Daily action credit cost limit** und bestätigen Sie, dass Ihr Workspace über genügend Credits für Sends im vollen Umfang verfügt.
- Entfernen oder rekonfigurieren Sie das Experiment, sodass die gesamte Zielgruppe den Agent-Schritt betritt (oder stufen Sie die Gewinnervariante zum Hauptpfad hoch).

Die Skalierung auf die gesamte Zielgruppe erhöht den Credit-Verbrauch proportional. Überwachen Sie die Nutzung nach dem Launch unter **Einstellungen** > **Abrechnung** > **Credits-Nutzung** > **Agent Console**.

## Canvas-Schritt-Agents verwenden {#use-canvas-step-agents}

Nachdem Sie einen Canvas-Schritt-Agent erstellt haben, fügen Sie ihn als Agent-Schritt zu einem Canvas hinzu, um Nachrichten zu personalisieren oder Entscheidungen in Echtzeit zu steuern.

### Funktionsweise {#how-it-works}

Wenn Nutzer:innen einen Agent-Schritt in einem Canvas erreichen, sendet Braze die von Ihnen konfigurierten Eingabedaten an Ihren Agent. Der Agent verarbeitet die Eingabe mithilfe seines Modells und seiner Anweisungen und gibt dann eine Ausgabe zurück, die in der von Ihnen im Schritt definierten Ausgabevariable gespeichert wird. Sie können diese Ausgabe für Entscheidungen, Personalisierung oder nachgelagerte Verarbeitung verwenden.

Agent-Schritte verwenden [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables), um relevanten Kontext aufzunehmen und eine Variable auszugeben, die im Canvas verwendet werden kann. Voraussetzungen und eine vollständige Referenz finden Sie unter [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Einen Agent-Schritt hinzufügen {#add-an-agent-step}

So fügen Sie einen Agent zu Ihrem Canvas hinzu:

1. Ziehen Sie die Komponente **Agent** aus der Seitenleiste per Drag-and-Drop, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Agent**.
2. Wählen Sie den Agent aus, der die Daten in diesem Schritt verarbeitet.
3. Definieren Sie den Namen der Ausgabevariable. Der Ausgabedatentyp wird in der [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents) festgelegt.
4. (Optional) Fügen Sie zusätzliche Kontextwerte hinzu, auf die der Agent bei der Ausführung zugreifen kann. Dies können zusätzliche Liquid-Variablen oder Canvas-Kontext sein, die Sie nicht bereits im Agent-Setup gebunden haben – zum Beispiel Werte, die Sie nur zum Sendezeitpunkt aus diesem Schritt übergeben möchten.
5. Testen Sie den Agent mithilfe der Vorschau im Schritt oder über [Canvas testen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps), um den vollständigen Nutzerpfad durchzugehen.

Informationen zu Ausgabedatentypen, Liquid-Templating und Screenshots finden Sie unter [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Anwendungsfälle {#use-cases}

| Anwendungsfall | Beschreibung |
| --- | --- |
| Lead-Scoring und -Qualifizierung | Verwenden Sie einen Agent-Schritt, um eingehende Leads auf einer Skala zu bewerten (zum Beispiel 1–10). Leiten Sie Nutzer:innen mit einem Score über einem Schwellenwert in Nurture-Pfade, während Leads mit geringer Eignung disqualifiziert werden. |
| Dynamische Nachrichtenpersonalisierung | Lassen Sie einen Agent Betreffzeilen, Produktempfehlungen oder Nachrichtentexte basierend auf Nutzerattributen oder kürzlichem Verhalten generieren. Die Antwort kann direkt in einen Nachrichtenschritt eingefügt werden. |
| Kundenfeedback-Verarbeitung | Übergeben Sie Kundenkommentare an einen Agent, um die Stimmung zu analysieren und empathische Follow-up-Nachrichten zu generieren. Bei hochwertigen Nutzer:innen kann der Agent die Antwort eskalieren oder Vergünstigungen einschließen. |
| Intelligentes Routing | Verwenden Sie Agent-Ausgaben (boolesch oder numerisch), um Nutzer:innen in verschiedene Canvas-Pfade aufzuteilen. Klassifizieren Sie beispielsweise Nutzer:innen als „gefährdet“ oder „gesund“ und passen Sie die Messaging-Kadenz entsprechend an. |
| Umfrage- oder Antwortinterpretation | Lassen Sie einen Agent offene Umfrageantworten oder Freitextfelder analysieren und strukturierte Werte zurückgeben (zum Beispiel Kategorisierung von Absicht oder Bedarf), die nachgelagerte Pfade steuern. |
| Mehrstufiges Reasoning | Konfigurieren Sie einen Agent, um Kontextfelder zu kombinieren und komplexe Entscheidungen zu treffen, wie zum Beispiel die Empfehlung der nächstbesten Aktion (E-Mail, SMS oder menschliche Kontaktaufnahme) basierend auf mehreren Nutzerattributen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

### Die Agent-Ausgabe verwenden {#use-the-agent-output}

Nachdem der Agent ausgeführt wurde, verwenden Sie die Ausgabevariable in Ihrem Canvas:

- **Journey-Routing:** Leiten Sie Nutzer:innen basierend auf der Antwort des Agents in verschiedene Canvas-Pfade. Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) oder [Decision-Splits]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) mit numerischen, booleschen oder strukturierten Ausgaben.
- **Personalisierung:** Fügen Sie die Antwort des Agents mithilfe von Liquid direkt in einen Nachrichtenschritt ein.
- **Nutzerdaten verarbeiten:** Analysieren und standardisieren Sie Nutzerdaten und speichern Sie diese dann im Kundenprofil (zum Beispiel mit einem [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt) oder senden Sie sie über einen Webhook.

Beispiele finden Sie unter [Funktionsweise]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#how-it-works) im Agent-Schritt.

### Fehlerbehandlung und Fallback-Verhalten {#fallback-behavior}

Folgendes gilt für Canvas-Schritt-Agents in einem [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

- Wenn das verbundene Modell einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) vom LLM-Anbieter zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann; Nutzer:innen fahren dann mit dem nächsten Canvas-Schritt fort.
- Bei anderen Fehlern (wie einem Timeout oder einem ungültigen API-Schlüssel) wird die Ausgabevariable auf `null` gesetzt, es sei denn, der Agent hat [konfigurierte Fallback-Werte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agent Console.
- Wenn ein Agent sein tägliches Aufruf-Limit erreicht, wendet Braze ebenfalls konfigurierte Fallback-Werte an, sofern vorhanden; andernfalls wird die Ausgabevariable auf `null` gesetzt.

Wenn Fallback-Werte konfiguriert sind, wendet Braze diese bei nicht wiederholbaren Fehlern und bei Tageslimit-Fehlern an. Braze rendert den Fallback mit Liquid pro Nutzer:in und speichert das Ergebnis in der Ausgabevariable des Agent-Schritts. Ohne Fallback-Werte setzen diese Fehler die Ausgabevariable auf `null`. Wenn Sie es vorziehen, schrittspezifische Standardwerte in Nachrichtenschritten statt in Agent-Console-Fallbacks zu konfigurieren, können Sie weiterhin [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) nachgelagert verwenden. Lassen Sie dazu die Fallbacks im Abschnitt **Output** des Agent-Setups leer, damit Liquid-Standardwerte greifen können, wenn der Agent null zurückgibt.

Rate-Limit-Fehler, Modell-Nichtverfügbarkeit und Tageslimit-Fehler verbrauchen keine Braze-Credits. Timeouts verbrauchen Credits. Siehe [Wann Credits verbraucht werden]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

- Antworten werden für identische Eingaben zwischengespeichert und können bei wiederholten identischen Aufrufen innerhalb weniger Minuten wiederverwendet werden. Zwischengespeicherte Antworten zählen weiterhin zu den Gesamt- und Tagesaufrufen.
- Agent-Schritte können bei der Verarbeitung einer großen Anzahl von Nutzer:innen Zeit in Anspruch nehmen. Braze reiht Aufrufe gemäß den [Aufruf-Flusssteuerungen]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls) in eine Warteschlange ein, sodass Nutzer:innen bei Sendungen mit hohem Volumen möglicherweise ausstehend bleiben.

Informationen zum Agent-Schritt-Setup und Laufzeitdetails finden Sie unter [Fehlerbehandlung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#error-handling) im Agent-Schritt. Weitere Details finden Sie unter [Fehlerbehandlung]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) in Braze Agents.

## Catalog Agents verwenden {#use-catalog-agents}

Nachdem Sie einen Catalog Agent erstellt haben, wenden Sie ihn auf ein Katalogfeld an, um automatisch Werte für jede Zeile zu generieren oder zu berechnen. Der Agent wird auch für neue Zeilen ausgeführt, die dem Katalog in Zukunft hinzugefügt werden.

### Funktionsweise

Nach dem Start wird der Agent ausgeführt und wertet jede Zeile aus, wobei er die ausgewählten Spalten als Kontext heranzieht, um eine Ausgabe zu erzeugen. Agents werden für alle neuen Zeilen ausgeführt, die nach der Bereitstellung des Agents hinzugefügt werden. Wenn Sie **Recalculate when catalog rows update** ausgewählt haben, werden alle Werte für dieses Feld aktualisiert, wenn sich vorhandene Quellfelder ändern.

Wenn Sie Eingabespalten für einen Catalog Agent konfigurieren, aktivieren Sie die produktinterne Steuerung, die kennzeichnet, welche ausgewählten Spalten erforderlich sein müssen, bevor der Agent aufgerufen wird (die Bezeichnungen können je nach Workspace leicht variieren). Wenn diese Steuerung aktiviert ist, wählen Sie die Teilmenge der Spalten aus, die Werte enthalten müssen – ausgewählte Spalten sind standardmäßig als erforderlich markiert, aber Sie können Spalten entfernen, die leer bleiben dürfen, ohne den Agent zu blockieren. Der Agent überspringt eine Zeile nur dann, wenn eine Spalte, die Sie als erforderlich belassen haben, leer ist oder fehlt – zum Beispiel ein `gender`-Feld, das noch nicht ausgefüllt wurde. Eine Ausführung ohne den erforderlichen Kontext verschwendet Token und kann zu minderwertiger Ausgabe führen.

Catalog Agents berücksichtigen auch Abhängigkeiten zwischen Spalten. Wenn Spalte D aus den Spalten B und C generiert wird, führt der Agent Spalte D für eine Zeile erst aus, wenn B und C Werte für diese Zeile enthalten.

Sie können die Felder in Ihrem Katalog, die Agents verwenden, aktualisieren und bearbeiten. Um einen Agent aus einer Spalte zu entfernen, deaktivieren Sie **Apply KI agent**. Dadurch wird die Spalte wieder zu einer nicht-agentischen Spalte, und die Felder behalten die letzten Werte bei, die der Agent bei seiner letzten Ausführung auf den Katalog angewendet hat.

Zirkuläre Referenzen in Katalogen werden nicht unterstützt, d. h. das folgende Szenario kann nicht auftreten:

- Agentische Spalte 1 verwendet agentische Spalte 2 als Eingabe
- Agentische Spalte 2 verwendet agentische Spalte 1 als Eingabe

### Einen Agent zu einem Katalogfeld hinzufügen {#add-an-agent-to-a-catalog-field}

![Ein Agent-Schritt in einem Katalogfeld.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

So fügen Sie einen Agent zu Ihrem Katalogfeld hinzu:

1. Fügen Sie in Ihrem Katalog ein neues Feld hinzu.
2. Wählen Sie **Apply KI agent** aus.
3. Weisen Sie diesem Feld einen Agent zu.
4. Wählen Sie aus, welche Spalten als Eingabe übergeben werden sollen. Wenn keine ausgewählt sind, hat der Agent Zugriff auf alle Spalten im Katalog.
5. (Optional) Aktivieren Sie **Only run when required columns have values**, um Zeilen zu überspringen, in denen eine oder mehrere ausgewählte Eingabespalten leer sind. Wenn diese Option aktiviert ist, wählen Sie aus, welche der Eingabespalten ausgefüllt sein müssen, damit der Agent ausgeführt wird – alle ausgewählten Spalten sind standardmäßig als erforderlich markiert, aber Sie können alle entfernen, die leer bleiben dürfen, ohne eine Ausführung zu blockieren.
6. Entscheiden Sie, ob der Agent Felder neu berechnen soll, wenn Katalogzeilen aktualisiert werden. Wenn Sie diese Option nicht auswählen, wird der Agent nur einmal pro Zeile ausgeführt.
7. Wählen Sie **Add fields** aus, um den Agent bereitzustellen und Kostenschätzungen zu überprüfen. Das Modal **Cost estimation** zeigt an, wie oft der Agent auf diesem Katalog ausgeführt wird, was ungefähr der Gesamtzahl der Zeilen entspricht. Um fortzufahren, wählen Sie **Confirm** aus.

### Best Practices für Catalog Agents {#catalog-agent-best-practices}

Planen Sie, welche Spalten der Agent benötigt, bevor Sie ihn auf ein Katalogfeld anwenden. Nachdem Sie die Steuerung für erforderliche Eingaben für das Feld aktiviert haben, wählen Sie die Spalten aus, die die Daten enthalten, die Ihr Agent lesen soll, und deaktivieren Sie dann alle Spalten, die leer bleiben dürfen, ohne eine Ausführung zu blockieren. Der Agent überspringt eine Zeile nur dann, wenn eine Spalte, die Sie als erforderlich markiert belassen haben, leer ist.

Lassen Sie eine Spalte nicht als erforderlich markiert, wenn Sie erwarten, dass sie für einige Zeilen leer bleibt und der Agent trotzdem ausgeführt werden soll – entfernen Sie sie stattdessen aus der erforderlichen Menge. Das Überspringen unvollständiger Zeilen vermeidet unnötigen Token-Verbrauch und hält die Ausgabequalität hoch.

| Szenario | Was passiert |
| --- | --- |
| Vorbefüllte Zeilen mit Platzhaltern | Wenn Sie Katalogzeilen nur mit einer ID und einem Fondsnamen hinzufügen und andere Spalten später ausfüllen, überspringt der Agent diese Zeilen, bis die erforderlichen Eingabespalten Werte enthalten. |
| Agent wird nach vorhandenen Zeilen angewendet | Wenn Sie einen Agent auf ein Feld in einem Katalog anwenden, der bereits Zeilen enthält, wertet der Agent jede Zeile aus, führt aber nur dort aus, wo die erforderlichen Eingabespalten ausgefüllt sind. |
| Teilweise vollständiger Katalog | Zum Beispiel ein Katalog mit 100 Zeilen, in dem `leader` für 2026-Einträge ausgefüllt ist, aber andere Zeilen nur eine ID und einen Fondsnamen mit leeren Feldern enthalten. Der Agent wird für Zeilen mit einem `leader`-Wert ausgeführt und überspringt Zeilen ohne diesen Wert, wenn `leader` als erforderlich markiert bleibt. |
| Abhängige Spalten | Wenn Spalte 3 von den Spalten 1 und 2 abhängt, schreibt der Agent erst in Spalte 3, wenn die Spalten 1 und 2 Werte für diese Zeile enthalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best Practices für Catalog Agents" }

### Anwendungsfälle

| Anwendungsfall | Beschreibung |
| --- | --- |
| Produktbeschreibungen generieren | Erstellen Sie automatisch kurze Marketingtexte für neue Katalogeinträge, zum Beispiel durch Generierung einer ansprechenden Beschreibung aus strukturierten Produktdaten wie Name, Kategorie und Features. |
| Produktattribute anreichern | Füllen Sie fehlende Werte wie Farbfamilie, Stil oder Saison basierend auf einem Produktnamen und Details aus. Wenn ein Produktname beispielsweise „Laguna Polarized Sunglasses“ lautet, könnte der Agent den Stil als „Sport“ und die Farbfamilie als „Blau“ zuweisen. |
| Abgeleitete Felder berechnen | Verwenden Sie vorhandene Felder, um neue Daten zu generieren, wie z. B. einen „Fit-Score“ basierend auf Attributen oder ein „Beliebtheitstag“ aus Verkaufs- und Bewertungszahlen. |
| Artikel kategorisieren oder taggen | Weisen Sie Tags für Empfehlungslogik zu, damit Personalisierungsmodelle Produkte effektiver segmentieren können. Taggen Sie Produkte beispielsweise als „Outdoor“, „Festival-tauglich“ oder „Premium“. |
| Inhalte lokalisieren | Übersetzen Sie Katalogtexte in eine andere Sprache für globale Campaigns, oder passen Sie Ton und Länge für regionsspezifische Kanäle an. Übersetzen Sie beispielsweise „Classic Clubmaster Sunglasses“ ins Spanische als „Gafas de sol Classic Clubmaster“ oder kürzen Sie Beschreibungen für SMS-Campaigns. |
| Bewertungen oder Feedback zusammenfassen | Fassen Sie Stimmung oder Feedback in einem neuen Feld zusammen, z. B. durch Zuweisung von Stimmungswerten wie Positiv, Neutral oder Negativ, oder erstellen Sie eine kurze Textzusammenfassung wie „Die meisten Kund:innen erwähnen eine tolle Passform, bemerken aber langsamen Versand.“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

### Antwortfelder definieren {#define-response-fields}

Wenn Ihr Agent [Felder]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents?tab=fields#advanced-schemas) als Ausgabeformat verwendet, können Sie das entsprechende Feld des Agents für **Response Field** auswählen, um es im Katalogfeld zu verwenden.

Angenommen, Sie haben einen Agent, der Produktbeschreibungen zu einem Katalog hinzufügt, mit den folgenden Feldern zur Strukturierung des Ausgabeformats:

| Feldname | Wert |
| --- | --- |
| **description** | Text |
| **confidence_score_out_of_ten** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Antwortfelder definieren" }

Sie können ein Feld namens **product_description** zu einem Katalog hinzufügen und **description** als **Response Field** auswählen, um die Spalte mit den Beschreibungen des Agents zu befüllen.

![Ein Feld „product_description“ mit dem angewendeten Agent „Descriptor“. Die Ausgabe „description“ ist als Antwortfeld ausgewählt.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Sie können die vom Agent generierte Zelle auch manuell überschreiben, indem Sie **Edit Item** auswählen und die vom Agent generierte Beschreibung mit Ihren Änderungen aktualisieren. Um zur vom Agent generierten Beschreibung zurückzukehren, wählen Sie das Aktualisierungssymbol in der Zelle aus.

### Fehlerbehandlung {#error-handling}

- Wenn der LLM-Anbieter einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann.
- Bei anderen Fehlern (wie einem Timeout oder einem ungültigen API-Schlüssel) wird der Katalogfeldwert nicht aktualisiert. Catalog Agents unterstützen keine Konfiguration von Fallback-Werten in der Agent Console.
- Sie können die Protokolle des Agents überprüfen, um Details zu fehlgeschlagenen Ausführungen zu erhalten.
- Catalog Agents sind auf die Verarbeitung von Eingabewerten bis zu 25 KB pro Zeile beschränkt.

## Ihren Agenten überwachen {#monitor-your-agent}

Die Überwachung funktioniert unabhängig davon, ob Ihr Agent in Canvas oder in Katalogen ausgeführt wird, auf die gleiche Weise.

Im Abschnitt **Nutzung** Ihres Agenten können Sie nachschlagen und dorthin navigieren, wo der Agent aktiv in Katalogen und Canvases verwendet wird.

![Abschnitt „Nutzung“ des Agenten, der zwei aktive und einen inaktiven Agenten für Canvases zeigt.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Im Abschnitt **Protokolle** Ihres Agenten können Sie die tatsächlichen Agentenaufrufe überwachen, die in Ihren Canvases und Katalogen stattfinden. Sie können nach Informationen wie dem Datumsbereich, dem Ergebnis (Erfolg oder Fehler) oder dem Aufrufstandort filtern. Sie können auch **CSV exportieren** auswählen, um nur die auf der aktuellen Seite angezeigten Protokolle zu exportieren.

{% alert tip %}
Sie können Fehler beim täglichen Aufruflimit auch im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) überwachen.
{% endalert %}

![Protokolle für einen Agenten „AI Sentiment Score“.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Wählen Sie **Anzeigen** für einen bestimmten Agentenaufruf aus, um die Eingabe, die Ausgabe und die Nutzer-ID zu sehen.

![Das Detailpanel für einen Agenten „Random Sports Assignment“, das den Eingabeprompt, die Ausgabeantwort und eine zugehörige Nutzer-ID zeigt.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

Bei Canvas-Schritt-Agenten enthalten die Protokolle einen Abschnitt **Fallback-Ausgabe**, der jede Fallback-Ausgabe anzeigt, die verwendet wurde, wenn der Aufruf fehlgeschlagen ist.

### Currents verwenden {#use-currents}

Sie können auch diese Currents-Ereignisse nutzen, um auf die Kafka-Datensatzschemata zuzugreifen:

- Ereignisse zu ausgeführten Agenten
- Ereignisse zu Tool-Aufrufen

Weitere Informationen finden Sie im [Glossar der Nachrichteninteraktionsereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Verwandte Artikel {#related-articles}

- [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)
- [Referenz für Agents]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq)