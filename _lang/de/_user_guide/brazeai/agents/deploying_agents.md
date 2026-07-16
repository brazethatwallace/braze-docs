---
nav_title: Agenten bereitstellen
article_title: Angepasste Agenten bereitstellen
description: "Erfahren Sie, wie Sie angepasste Agenten in Braze einsetzen können, nachdem Sie diese erstellt haben."
alias: /deploying-agents/
page_order: 2
---

# Angepasste Agenten bereitstellen {#deploy-custom-agents}

> Nachdem Sie [einen Agenten erstellt]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) haben, erfahren Sie auf dieser Seite, wo und wie Sie ihn in Braze bereitstellen können. Der Agententyp, den Sie bei der Erstellung wählen – Canvas-Agent oder Katalog-Agent – bestimmt, wo der Agent ausgeführt werden kann. Eine Einführung finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents).

## Typen angepasster Agenten {#types-of-custom-agents}

Angepasste Agenten werden je nach Typ in verschiedenen Bereichen von Braze bereitgestellt. Verwenden Sie die folgende Tabelle, um den richtigen Bereitstellungspfad für Ihren Agenten zu finden.

| Agententyp | Bereitgestellt in | Wird ausgeführt, wenn | Abschnitt |
| --- | --- | --- | --- |
| Canvas-Schritt-Agent | [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) in Canvas | Nutzer:innen den Schritt erreichen | [Canvas-Schritt-Agenten verwenden](#use-canvas-step-agents) |
| Katalog-Agent | Katalogfeld | Eine Katalogzeile erstellt oder aktualisiert wird | [Katalog-Agenten verwenden](#use-catalog-agents) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Typen angepasster Agenten" }

Sie wählen den Agententyp in der **Agentenkonsole** aus, wenn Sie den Agenten erstellen. Informationen zu den Einrichtungsschritten finden Sie unter [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-1-choose-an-agent-type).

## Best Practices {#best-practices}

Konzentrieren Sie sich auf hochwertige Anwendungsfälle, bei denen Agenten die größte Kapitalrendite (ROI) erzielen können, und wählen Sie Zielgruppen aus, die wahrscheinlich reagieren. Eine kleinere Zielgruppe mit hohem Potenzial übertrifft oft eine große Zielgruppe mit geringem Potenzial.

Beginnen Sie bei Canvas-Schritt-Agenten mit Nutzer:innen, die starke Signale aufweisen – wie aktuelle Suchanfragen, hohes Engagement oder umfangreiche Profildaten – bevor Sie auf breitere Segmente ausweiten. Priorisieren Sie bei Katalog-Agenten Zeilen, in denen die benötigten Eingabespalten bereits befüllt sind, damit jeder Aufruf genügend Kontext hat, um nützliche Ausgaben zu erzeugen.

Um die Kapitalrendite in kleinem Maßstab zu testen, bevor Sie einen Agenten breit ausrollen, verwenden Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, sodass nur ein Teil Ihrer Zielgruppe den Branch betritt, der Ihren Agent-Schritt enthält.

## Canvas-Schritt-Agenten verwenden {#use-canvas-step-agents}

Nachdem Sie einen Canvas-Schritt-Agenten erstellt haben, fügen Sie ihn als Agent-Schritt zu einem Canvas hinzu, um Nachrichten zu personalisieren oder Entscheidungen in Echtzeit zu steuern.

### Funktionsweise {#how-it-works}

Wenn Nutzer:innen einen Agent-Schritt in einem Canvas erreichen, sendet Braze die von Ihnen konfigurierten Eingabedaten an Ihren Agenten. Der Agent verarbeitet die Eingabe mithilfe seines Modells und seiner Anweisungen und gibt dann eine Ausgabe zurück, die in der von Ihnen im Schritt definierten Ausgabevariable gespeichert wird. Sie können diese Ausgabe für Entscheidungen, Personalisierung oder nachgelagerte Verarbeitung verwenden.

Agent-Schritte verwenden [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables), um relevanten Kontext aufzunehmen und eine Variable auszugeben, die im Canvas verwendet werden kann. Voraussetzungen und eine vollständige Referenz finden Sie unter [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Einen Agent-Schritt hinzufügen {#add-an-agent-step}

Um einen Agenten zu Ihrem Canvas hinzuzufügen:

1. Ziehen Sie die **Agent**-Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i>-Plus-Button am unteren Rand eines Schritts und wählen Sie **Agent**.
2. Wählen Sie den Agenten aus, der die Daten in diesem Schritt verarbeitet.
3. Definieren Sie den Namen der Ausgabevariable. Der Ausgabedatentyp wird in der [Agentenkonsole]({{site.baseurl}}/user_guide/brazeai/agents) festgelegt.
4. (Optional) Fügen Sie zusätzliche Kontextwerte hinzu, die der Agent bei der Ausführung referenzieren kann. Dies können zusätzliche Liquid-Variablen oder Canvas-Kontext sein, die Sie nicht bereits im Agent-Setup gebunden haben – beispielsweise Werte, die Sie nur zum Sendezeitpunkt aus diesem Schritt übergeben möchten.
5. Testen Sie den Agenten mithilfe der Schrittvorschau oder über [Canvas testen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps), um den vollständigen Nutzerpfad durchzugehen.

Informationen zu Ausgabedatentypen, Liquid-Templating und Screenshots finden Sie unter [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

### Anwendungsfälle {#use-cases}

| Anwendungsfall | Beschreibung |
| --- | --- |
| Lead-Bewertung und -Qualifizierung | Verwenden Sie einen Agent-Schritt, um eingehende Leads auf einer Skala (z. B. 1–10) zu bewerten. Leiten Sie Nutzer:innen mit einer Punktzahl über einem bestimmten Schwellenwert in Nurture-Pfade weiter und disqualifizieren Sie gleichzeitig Leads mit geringer Eignung. |
| Dynamische Nachrichtenpersonalisierung | Lassen Sie einen Agenten Betreffzeilen, Produktempfehlungen oder Nachrichtentexte auf Grundlage von Nutzerattributen oder aktuellen Verhaltensweisen generieren. Die Antwort kann direkt in einen Nachrichten-Schritt eingefügt werden. |
| Bearbeitung von Kundenfeedback | Leiten Sie Kundenkommentare an einen Agenten weiter, um die Stimmung zu analysieren und einfühlsame Follow-up-Nachrichten zu erstellen. Bei besonders wertvollen Nutzer:innen kann der Agent die Antwort eskalieren oder Vergünstigungen hinzufügen. |
| Intelligentes Routing | Verwenden Sie Agent-Ausgaben (boolesch oder numerisch), um Nutzer:innen in verschiedene Canvas-Pfade aufzuteilen. Beispielsweise können Nutzer:innen als „gefährdet“ oder „gesund“ klassifiziert und die Messaging-Frequenz entsprechend angepasst werden. |
| Umfrage- oder Antwortinterpretation | Lassen Sie einen Agenten offene Umfrageantworten oder Freitextfelder analysieren und strukturierte Werte zurückgeben (z. B. Kategorisierung von Absichten oder Bedürfnissen), die nachgelagerte Pfade steuern. |
| Mehrstufiges Reasoning | Konfigurieren Sie einen Agenten, um Kontextfelder zu kombinieren und komplexe Entscheidungen zu treffen, wie beispielsweise die Empfehlung der nächstbesten Aktion (E-Mail, SMS oder persönliche Kontaktaufnahme) auf Grundlage mehrerer Nutzerattribute. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

### Die Agentenausgabe verwenden {#use-the-agent-output}

Nachdem der Agent ausgeführt wurde, verwenden Sie die Ausgabevariable in Ihrem Canvas:

- **Journey-Routing:** Leiten Sie Nutzer:innen basierend auf der Antwort des Agenten in verschiedene Canvas-Pfade. Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) oder [Decision-Splits]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) mit numerischen, booleschen oder strukturierten Ausgaben.
- **Personalisierung:** Fügen Sie die Antwort des Agenten mithilfe von Liquid direkt in einen Nachrichten-Schritt ein.
- **Nutzerdaten verarbeiten:** Analysieren und standardisieren Sie Nutzerdaten und speichern Sie diese dann im Nutzerprofil (z. B. mit einem [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt) oder senden Sie sie über einen Webhook.

Beispiele finden Sie unter [Funktionsweise]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#how-it-works) im Agent-Schritt.

### Fehlerbehandlung und Fallback-Verhalten {#fallback-behavior}

Das Folgende gilt für Canvas-Schritt-Agenten in einem [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step).

- Wenn das verbundene Modell einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) vom LLM-Anbieter zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann; die Nutzer:innen fahren dann mit dem nächsten Canvas-Schritt fort.
- Bei anderen Fehlern (wie einem Timeout oder einem ungültigen API-Schlüssel) wird die Ausgabevariable auf `null` gesetzt, es sei denn, der Agent hat [konfigurierte Fallback-Werte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agentenkonsole.
- Wenn ein Agent sein tägliches Aufruflimit erreicht, wendet Braze ebenfalls konfigurierte Fallback-Werte an, sofern vorhanden; andernfalls wird die Ausgabevariable auf `null` gesetzt.

Wenn Fallback-Werte konfiguriert sind, wendet Braze diese bei nicht wiederholbaren Fehlern und bei Tageslimit-Fehlern an. Braze rendert den Fallback mit Liquid pro Nutzer:in und speichert das Ergebnis in der Ausgabevariable des Agent-Schritts. Ohne Fallback-Werte setzen diese Fehler die Ausgabevariable auf `null`. Wenn Sie es vorziehen, schrittspezifische Standardwerte in Nachrichten-Schritten statt in Agentenkonsolen-Fallbacks zu konfigurieren, können Sie weiterhin [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) nachgelagert verwenden. Lassen Sie dazu die Fallbacks im Abschnitt **Ausgabe** des Agent-Setups leer, damit Liquid-Standardwerte greifen können, wenn der Agent null zurückgibt.

- Antworten werden für identische Eingaben zwischengespeichert und können bei wiederholten identischen Aufrufen innerhalb weniger Minuten wiederverwendet werden. Zwischengespeicherte Antworten zählen weiterhin zu den Gesamt- und Tagesaufrufen.
- Agent-Schritte können bei der Verarbeitung einer großen Anzahl von Nutzer:innen Zeit in Anspruch nehmen. Braze reiht Aufrufe gemäß den [Aufruf-Flusssteuerungen]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls) in eine Warteschlange ein, sodass Nutzer:innen bei Sendungen mit hohem Volumen möglicherweise ausstehend bleiben.

Informationen zum Agent-Schritt-Setup und zu Laufzeitdetails finden Sie unter [Fehlerbehandlung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#error-handling) im Agent-Schritt. Weitere Details finden Sie unter [Fehlerbehandlung]({{site.baseurl}}/user_guide/brazeai/agents#error-handling) in Braze Agents.

## Katalog-Agenten verwenden {#use-catalog-agents}

Nachdem Sie einen Katalog-Agenten erstellt haben, wenden Sie ihn auf ein Katalogfeld an, um automatisch Werte für jede Zeile zu generieren oder zu berechnen. Der Agent wird auch für neue Zeilen ausgeführt, die in Zukunft zum Katalog hinzugefügt werden.

### Funktionsweise

Nach dem Start führt der Agent jede Zeile aus und wertet sie aus, wobei er die ausgewählten Spalten in seinen Kontext einbezieht, um eine Ausgabe zu erzeugen. Agenten werden auf allen neuen Zeilen ausgeführt, die nach der Bereitstellung des Agenten hinzugefügt werden. Wenn Sie **Beim Aktualisieren von Katalogzeilen neu berechnen** ausgewählt haben, werden alle Werte für dieses Feld aktualisiert, wenn sich vorhandene Quellfelder ändern.

Wenn Sie Eingabespalten für einen Katalog-Agenten konfigurieren, aktivieren Sie die produktinterne Steuerung, die markiert, welche ausgewählten Spalten **für die Ausführung erforderlich** sind, bevor der Agent aufgerufen wird (die Bezeichnungen können je nach Workspace leicht variieren). Wenn diese Steuerung aktiviert ist, wählen Sie die Teilmenge der Spalten aus, die Werte enthalten müssen – ausgewählte Spalten sind standardmäßig als erforderlich markiert, aber Sie können Spalten entfernen, die leer bleiben dürfen, ohne den Agenten zu blockieren. Der Agent überspringt eine Zeile nur dann, wenn eine Spalte, die Sie als erforderlich belassen haben, leer ist oder fehlt – beispielsweise ein `gender`-Feld, das noch nicht ausgefüllt wurde. Die Ausführung ohne den erforderlichen Kontext verschwendet Token und kann zu qualitativ minderwertiger Ausgabe führen.

Katalog-Agenten berücksichtigen auch Abhängigkeiten zwischen Spalten. Wenn Spalte D aus den Spalten B und C generiert wird, führt der Agent Spalte D für eine Zeile erst aus, wenn B und C Werte für diese Zeile enthalten.

Sie können die Felder in Ihrem Katalog, die Agenten verwenden, aktualisieren und bearbeiten. Um einen Agenten aus einer Spalte zu entfernen, deaktivieren Sie **KI-Agent anwenden**. Dadurch wird die Spalte wieder in eine reguläre Spalte zurückgesetzt, und die Felder behalten die letzten Werte bei, die der Agent bei seiner letzten Ausführung im Katalog angewendet hat.

Zirkuläre Referenzen in Katalogen werden nicht unterstützt, d. h. das folgende Szenario kann nicht auftreten:

- Agentische Spalte 1 verwendet agentische Spalte 2 als Eingabe
- Agentische Spalte 2 verwendet agentische Spalte 1 als Eingabe

### Einen Agenten zu einem Katalogfeld hinzufügen {#add-an-agent-to-a-catalog-field}

![Ein Agent-Schritt in einem Katalogfeld.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Um einen Agenten zu Ihrem Katalogfeld hinzuzufügen:

1. Fügen Sie in Ihrem Katalog ein neues Feld hinzu.
2. Wählen Sie **KI-Agent anwenden** aus.
3. Weisen Sie diesem Feld einen Agenten zu.
4. Wählen Sie aus, welche Spalten als Eingabe übergeben werden sollen. Wenn keine ausgewählt sind, hat der Agent Zugriff auf alle Spalten im Katalog.
5. (Optional) Aktivieren Sie **Nur ausführen, wenn erforderliche Spalten Werte enthalten**, um Zeilen zu überspringen, in denen eine oder mehrere ausgewählte Eingabespalten leer sind. Wenn diese Option aktiviert ist, wählen Sie aus, welche der Eingabespalten befüllt sein müssen, damit der Agent ausgeführt wird – alle ausgewählten Spalten sind standardmäßig als erforderlich markiert, aber Sie können jede entfernen, die leer bleiben darf, ohne eine Ausführung zu blockieren.
6. Entscheiden Sie, ob der Agent Felder neu berechnen soll, wenn Katalogzeilen aktualisiert werden. Wenn Sie diese Option nicht auswählen, wird der Agent nur einmal pro Zeile ausgeführt.
7. Wählen Sie **Felder hinzufügen** aus, um den Agenten bereitzustellen und die Kostenschätzungen zu überprüfen. Das Modal **Kostenschätzung** zeigt an, wie oft der Agent auf diesem Katalog ausgeführt wird – in etwa entsprechend der Gesamtzahl der Zeilen. Um fortzufahren, wählen Sie **Bestätigen** aus.

### Best Practices für Katalog-Agenten {#catalog-agent-best-practices}

Planen Sie, welche Spalten der Agent benötigt, bevor Sie ihn auf ein Katalogfeld anwenden. Nachdem Sie die Steuerung für erforderliche Eingaben für das Feld aktiviert haben, wählen Sie die Spalten aus, die die Daten enthalten, die Ihr Agent lesen soll, und deaktivieren Sie dann jede Spalte, die leer bleiben darf, ohne eine Ausführung zu blockieren. Der Agent überspringt eine Zeile nur dann, wenn eine Spalte, die Sie als erforderlich markiert belassen haben, leer ist.

Lassen Sie eine Spalte nicht als erforderlich markiert, wenn Sie erwarten, dass sie für einige Zeilen leer bleibt und der Agent trotzdem ausgeführt werden soll – entfernen Sie sie stattdessen aus der erforderlichen Menge. Das Überspringen unvollständiger Zeilen vermeidet unnötigen Token-Verbrauch und hält die Ausgabequalität hoch.

| Szenario | Was passiert |
| --- | --- |
| Vorbefüllte Zeilen mit Platzhaltern | Wenn Sie Katalogzeilen nur mit einer ID und einem Fondsnamen hinzufügen und andere Spalten später ausfüllen, überspringt der Agent diese Zeilen, bis die erforderlichen Eingabespalten Werte enthalten. |
| Agent wird nach vorhandenen Zeilen angewendet | Wenn Sie einen Agenten auf ein Feld eines Katalogs anwenden, der bereits Zeilen enthält, wertet der Agent jede Zeile aus, führt aber nur dort aus, wo die erforderlichen Eingabespalten befüllt sind. |
| Teilweise vollständiger Katalog | Beispielsweise ein Katalog mit 100 Zeilen, in dem `leader` für 2026-Einträge ausgefüllt ist, andere Zeilen aber nur eine ID und einen Fondsnamen mit leeren Feldern enthalten. Der Agent wird auf Zeilen mit einem `leader`-Wert ausgeführt und überspringt Zeilen ohne diesen Wert, wenn `leader` als erforderlich markiert bleibt. |
| Abhängige Spalten | Wenn Spalte 3 von den Spalten 1 und 2 abhängt, schreibt der Agent erst in Spalte 3, wenn die Spalten 1 und 2 Werte für diese Zeile enthalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Best Practices für Katalog-Agenten" }

### Anwendungsfälle

| Anwendungsfall | Beschreibung |
| --- | --- |
| Produktbeschreibungen generieren | Erstellen Sie automatisch kurze Marketingtexte für neue Katalogeinträge, indem Sie beispielsweise aus strukturierten Produktdaten wie Name, Kategorie und Features eine ansprechende Beschreibung generieren. |
| Produktattribute anreichern | Ergänzen Sie fehlende Werte wie Farbfamilie, Stil oder Saison anhand des Produktnamens und der Produktdetails. Wenn ein Produkt beispielsweise den Namen „Laguna Polarized Sunglasses“ trägt, könnte der Agent den Stil als „Sport“ und die Farbfamilie als „Blau“ zuordnen. |
| Abgeleitete Felder berechnen | Verwenden Sie vorhandene Felder, um neue Daten zu generieren, wie beispielsweise einen „Fit-Score“ basierend auf Attributen oder ein „Beliebtheits-Tag“ aus Verkaufs- und Bewertungszahlen. |
| Artikel kategorisieren oder mit Tags versehen | Weisen Sie Tags für die Empfehlungslogik zu, damit Personalisierungsmodelle Produkte effektiver segmentieren können. Beispielsweise können Sie Produkte mit „Outdoor“, „festivaltauglich“ oder „Premium“ taggen. |
| Inhalte lokalisieren | Übersetzen Sie Katalogtexte für globale Campaigns in andere Sprachen oder passen Sie Tonfall und Länge für regionsspezifische Kanäle an. Übersetzen Sie beispielsweise „Classic Clubmaster Sunglasses“ ins Spanische als „Gafas de sol Classic Clubmaster“ oder kürzen Sie Beschreibungen für SMS-Campaigns. |
| Bewertungen oder Feedback zusammenfassen | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, beispielsweise durch die Vergabe von Stimmungsbewertungen wie „Positiv“, „Neutral“ oder „Negativ“ oder durch die Erstellung einer kurzen Textzusammenfassung wie „Die meisten Kund:innen erwähnen die hervorragende Passform, bemerken jedoch den langsamen Versand.“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

### Antwortfelder definieren {#define-response-fields}

Wenn Ihr Agent [Felder]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents?tab=fields#advanced-schemas) als Ausgabeformat verwendet, können Sie das entsprechende Feld des Agenten als **Antwortfeld** auswählen, um es im Katalogfeld zu verwenden.

Angenommen, Sie haben einen Agenten, der Produktbeschreibungen zu einem Katalog hinzufügt und die folgenden Felder zur Strukturierung des Ausgabeformats verwendet:

| Feldname | Wert |
| --- | --- |
| **description** | Text |
| **confidence_score_out_of_ten** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Antwortfelder definieren" }

Sie können ein Feld namens **product_description** zu einem Katalog hinzufügen und **description** als **Antwortfeld** auswählen, um die Spalte mit den Beschreibungen des Agenten zu füllen.

![Ein Feld „product_description“ mit dem angewendeten Agenten „Descriptor“. Die Ausgabe „description“ ist als Antwortfeld ausgewählt.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Sie können die vom Agenten generierte Zelle auch manuell überschreiben, indem Sie **Artikel bearbeiten** auswählen und die vom Agenten generierte Beschreibung mit Ihren Änderungen aktualisieren. Um zur vom Agenten generierten Beschreibung zurückzukehren, wählen Sie das Aktualisierungssymbol in der Zelle aus.

### Fehlerbehandlung {#error-handling}

- Wenn der LLM-Anbieter einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann.
- Bei anderen Fehlern (wie einem Timeout oder einem ungültigen API-Schlüssel) wird der Katalogfeldwert nicht aktualisiert. Katalog-Agenten unterstützen keine Konfiguration von Fallback-Werten in der Agentenkonsole.
- Sie können die Protokolle des Agenten überprüfen, um Details zu fehlgeschlagenen Ausführungen zu erhalten.
- Katalog-Agenten können nur Eingabewerte von bis zu 25 KB pro Zeile verarbeiten.

## Ihren Agenten überwachen {#monitor-your-agent}

Die Überwachung funktioniert unabhängig davon, ob Ihr Agent in Canvas oder in Katalogen ausgeführt wird, auf die gleiche Weise.

Im Abschnitt **Nutzung** Ihres Agenten können Sie einsehen und dorthin navigieren, wo der Agent in Katalogen und Canvases aktiv verwendet wird.

![Der Abschnitt „Nutzung“ des Agenten zeigt zwei aktive Agenten und einen inaktiven Agenten für Canvases an.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Im Abschnitt **Protokolle** Ihres Agenten können Sie die tatsächlichen Agentenaufrufe überwachen, die in Ihren Canvases und Katalogen stattfinden. Sie können nach Informationen wie dem Datumsbereich, dem Ergebnis (Erfolg oder Fehler) oder dem Aufrufstandort filtern. Sie können auch **CSV exportieren** auswählen, um nur die auf der aktuellen Seite angezeigten Protokolle zu exportieren.

{% alert tip %}
Sie können auch Fehler bezüglich des täglichen Aufruflimits im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) überwachen.
{% endalert %}

![Protokolle für einen Agenten „AI Sentiment Score“.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Wählen Sie **Anzeigen** für einen bestimmten Agentenaufruf aus, um die Eingabe, Ausgabe und Nutzer-ID einzusehen.

![Das Detail-Panel für einen Agenten „Random Sports Assignment“, das die Eingabeaufforderung, die Ausgabeantwort und eine zugehörige Nutzer-ID anzeigt.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

Bei Canvas-Schritt-Agenten enthalten die Protokolle einen Abschnitt **Fallback-Ausgabe**, der alle Fallback-Ausgaben anzeigt, die verwendet wurden, wenn der Aufruf fehlgeschlagen ist.

### Currents verwenden {#use-currents}

Sie können auch diese Currents-Ereignisse verwenden, um auf die Kafka-Datensatzschemata zuzugreifen:

- Vom Agenten ausgeführte Ereignisse
- Tool-Aufrufereignisse

Weitere Details finden Sie im [Glossar zu Nachrichten-Engagement-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Verwandte Artikel {#related-articles}

- [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)
- [Referenz für Agenten]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq)