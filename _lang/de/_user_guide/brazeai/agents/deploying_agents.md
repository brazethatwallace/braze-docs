---
nav_title: Agenten bereitstellen
article_title: Angepasste Agenten bereitstellen
description: "Erfahren Sie, wie Sie angepasste Agenten in Braze einsetzen können, nachdem Sie diese erstellt haben."
alias: /deploying-agents/
page_order: 2
---

# Angepasste Agenten bereitstellen {#deploy-custom-agents}

> Erfahren Sie, wie Sie angepasste Agenten in Canvas-Schritten oder Katalogfeldern einsetzen können, nachdem Sie diese erstellt haben. Eine Einführung finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

## Agenten in Canvas {#agents-in-canvas}

Sie können Agenten als Schritte in einer Journey verwenden, um Nachrichten zu personalisieren oder Entscheidungen in Echtzeit zu steuern. Detaillierte Einrichtungsschritte finden Sie unter [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/).

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

## Agenten in Katalogen {#agents-in-catalogs}

Sie können einen Agenten auf Katalogfelder anwenden, sodass er automatisch Werte für jede Zeile generiert oder berechnet. Der Agent wird auch für neue Zeilen ausgeführt, die in Zukunft zum Katalog hinzugefügt werden.

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

### Schritte {#steps}

![Ein Agent-Schritt in einem Katalogfeld.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Um einen Agenten zu Ihrem Katalogfeld hinzuzufügen:

1. Fügen Sie in Ihrem Katalog ein neues Feld hinzu.
2. Wählen Sie **KI-Agent anwenden** aus.
3. Weisen Sie diesem Feld einen Agenten zu.
4. Wählen Sie aus, welche Spalten als Eingabe übergeben werden sollen. Wenn keine ausgewählt sind, hat der Agent Zugriff auf alle Spalten im Katalog.
5. Entscheiden Sie, ob der Agent Felder neu berechnen soll, wenn Katalogzeilen aktualisiert werden. Wenn Sie diese Option nicht auswählen, wird der Agent nur einmal pro Zeile ausgeführt.
6. Wählen Sie **Felder hinzufügen** aus, um den Agenten bereitzustellen und die Kostenschätzungen zu überprüfen. Das Modal **Kostenschätzung** zeigt an, wie oft der Agent auf diesem Katalog ausgeführt wird – in etwa entsprechend der Gesamtzahl der Zeilen. Um fortzufahren, wählen Sie **Bestätigen** aus.

### Wie Katalogagenten ausgeführt werden {#how-catalog-agents-run}

Nach dem Start führt der Agent jede Zeile aus und wertet sie aus, wobei er die ausgewählten Spalten in seinen Kontext einbezieht, um eine Ausgabe zu erzeugen. Agenten werden auf allen neuen Zeilen ausgeführt, die nach der Bereitstellung des Agenten hinzugefügt werden. Wenn Sie **Beim Aktualisieren von Katalogzeilen neu berechnen** ausgewählt haben, werden alle Werte für dieses Feld aktualisiert, wenn sich vorhandene Quellfelder ändern.

Sie können die Felder in Ihrem Katalog, die Agenten verwenden, aktualisieren und bearbeiten. Um einen Agenten aus einer Spalte zu entfernen, deaktivieren Sie **KI-Agent anwenden**. Dadurch wird die Spalte wieder in eine reguläre Spalte zurückgesetzt, und die Felder behalten die letzten Werte bei, die der Agent bei seiner letzten Ausführung im Katalog angewendet hat.

Zirkuläre Referenzen in Katalogen werden nicht unterstützt, d. h. das folgende Szenario kann nicht auftreten:

- Agentische Spalte 1 verwendet agentische Spalte 2 als Eingabe
- Agentische Spalte 2 verwendet agentische Spalte 1 als Eingabe

![Die Option „KI-Agent anwenden“ für ein Katalogfeld auswählen.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Katalogagenten können nur Eingabewerte von bis zu 25 KB pro Zeile verarbeiten.
{% endalert %}

#### Antwortfelder definieren {#define-response-fields}

Wenn Ihr Agent [Felder]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas) als Ausgabeformat verwendet, können Sie das entsprechende Feld des Agenten als **Antwortfeld** auswählen, um es im Katalogfeld zu verwenden.

Angenommen, Sie haben einen Agenten, der Produktbeschreibungen zu einem Katalog hinzufügt und die folgenden Felder zur Strukturierung des Ausgabeformats verwendet:

| Feldname | Wert |
| --- | --- |
| **description** | Text |
| **confidence_score_out_of_ten** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Antwortfelder definieren" }

Sie können ein Feld namens **product_description** zu einem Katalog hinzufügen und **description** als **Antwortfeld** auswählen, um die Spalte mit den Beschreibungen des Agenten zu füllen.

![Ein Feld „product_description“ mit dem angewendeten Agenten „Descriptor“. Die Ausgabe „description“ ist als Antwortfeld ausgewählt.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Sie können die vom Agenten generierte Zelle auch manuell überschreiben, indem Sie **Artikel bearbeiten** auswählen und die vom Agenten generierte Beschreibung mit Ihren Änderungen aktualisieren. Um zur vom Agenten generierten Beschreibung zurückzukehren, wählen Sie das Aktualisierungssymbol in der Zelle aus.

### Fehlerbehandlung in Katalogen {#error-handling-in-catalogs}

- Fehlgeschlagene Katalogaufrufe werden nicht wiederholt, auch nicht bei [Rate-Limit-Fehlern]({{site.baseurl}}/user_guide/brazeai/agents/reference/#rate-limit-errors) des LLM-Anbieters.
- Wenn der API-Aufruf an den Basismodellanbieter einen anderen Fehler zurückgibt, beispielsweise einen ungültigen API-Schlüssel, wird der Feldwert nicht aktualisiert.
- Sie können die Protokolle des Agenten überprüfen, um Details zu fehlgeschlagenen Ausführungen zu erhalten.

## Ihren Agenten überwachen {#monitor-your-agent}

Im Abschnitt **Nutzung** Ihres Agenten können Sie einsehen und dorthin navigieren, wo der Agent in Katalogen und Canvases aktiv verwendet wird.

![Der Abschnitt „Usage“ des Agenten zeigt zwei aktive Agenten und einen inaktiven Agenten für Canvases an.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Im Abschnitt **Protokolle** Ihres Agenten können Sie die tatsächlichen Agentenaufrufe überwachen, die in Ihren Canvases und Katalogen stattfinden. Sie können nach Informationen wie dem Datumsbereich, dem Ergebnis (Erfolg oder Fehler) oder dem Aufrufstandort filtern. Sie können auch **CSV exportieren** auswählen, um nur die auf der aktuellen Seite angezeigten Protokolle zu exportieren.

{% alert tip %}
Sie können auch Fehler bezüglich des täglichen Aufruflimits im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) überwachen.
{% endalert %}

![Protokolle für einen Agenten „AI Sentiment Score“.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Wählen Sie **Anzeigen** für einen bestimmten Agentenaufruf aus, um die Eingabe, Ausgabe und Nutzer-ID einzusehen.

![Das Detail-Panel für einen Agenten „Random Sports Assignment“, das die Eingabeaufforderung, die Ausgabeantwort und eine zugehörige Nutzer-ID anzeigt.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Currents verwenden {#use-currents}

Sie können auch diese Currents-Ereignisse verwenden, um auf die Kafka-Datensatzschemata zuzugreifen:

- Vom Agenten ausgeführte Ereignisse
- Tool-Aufrufereignisse

Weitere Details finden Sie im [Glossar zu Nachrichten-Engagement-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).

## Verwandte Artikel {#related-articles}

- [Referenz für Agenten]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq/)