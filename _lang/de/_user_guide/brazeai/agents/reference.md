---
nav_title: Referenz
article_title: Referenz für Agenten
description: "Wichtige Informationen zu Braze-Agenten."
page_order: 3
---

# Referenz für Agenten {#reference-for-agents}

> Wenn Sie angepasste Agenten erstellen, lesen Sie diesen Artikel für weitere Informationen zu wichtigen Einstellungen wie Anweisungen und Ausgabeschemata. Eine schrittweise Einrichtungsanleitung finden Sie unter [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Eine Einführung finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) und [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Modelle {#models}

Wenn Sie einen Agenten einrichten, können Sie das Modell auswählen, das er zur Generierung von Antworten verwendet. Sie haben zwei Möglichkeiten: ein von Braze bereitgestelltes Modell verwenden oder Ihren eigenen API-Schlüssel einbinden.

{% alert important %}
Das von Braze bereitgestellte **Auto**-Modell ist für Modelle optimiert, deren Denkfähigkeiten ausreichen, um Aufgaben wie Katalogsuche und Segmentzugehörigkeit auszuführen. Bei der Verwendung anderer Modelle empfehlen wir, Tests durchzuführen, um sicherzustellen, dass Ihr Modell für Ihren Anwendungsfall geeignet ist. Möglicherweise müssen Sie Ihre [Anweisungen](#writing-instructions) anpassen, um unterschiedliche Detailstufen oder schrittweises Denken für Modelle mit unterschiedlichen Geschwindigkeiten und Fähigkeiten bereitzustellen.
{% endalert %}

### Option 1: Ein von Braze bereitgestelltes Modell verwenden {#option-1-use-a-braze-powered-model}

Dies ist die einfachste Option, die keine zusätzliche Einrichtung erfordert. Braze ermöglicht den direkten Zugriff auf große Sprachmodelle (LLMs). Um diese Option zu verwenden, wählen Sie **Auto** aus – dabei werden Gemini-Modelle verwendet.

{% alert important %}
Sollten Sie beim Erstellen eines Agenten die Option **Braze Auto** nicht in der Dropdown-Liste **Model** sehen, wenden Sie sich an Ihren Customer-Success-Manager, um zu erfahren, wie Sie die Berechtigung zur Nutzung des Braze Auto-Modells erhalten.
{% endalert %}

### Option 2: Eigenen API-Schlüssel einbinden {#option-2-bring-your-own-api-key}

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter verwenden, werden die Token-Kosten direkt über Ihren Anbieter und nicht über Braze abgerechnet.

Wir empfehlen, regelmäßig die neuesten Modelle zu testen, da ältere Modelle nach einigen Monaten möglicherweise eingestellt oder als veraltet markiert werden. Stellen Sie sicher, dass Sie über ausreichend Guthaben bei Ihrem Anbieter verfügen, um Ihre Agenten im großen Maßstab auszuführen. Sie können sich auch für Benachrichtigungen der Agentenkonsole unter [Präferenzen für Benachrichtigungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) anmelden, um benachrichtigt zu werden, wenn Braze erkennt, dass ein Modell nicht mehr verfügbar ist oder Abrechnungsprobleme mit Ihrem LLM-Anbieter auftreten.

So richten Sie dies ein:

1. Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie Ihren Anbieter.
2. Geben Sie Ihren API-Schlüssel vom Anbieter ein.
3. Wählen Sie **Speichern**.

Anschließend können Sie zu Ihrem Agenten zurückkehren und Ihr Modell auswählen.

Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bestimmungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie sich dafür entscheiden, Ihren eigenen API-Schlüssel einzubinden, gilt der Anbieter Ihres LLM-Abos gemäß dem Vertrag zwischen Ihnen und Braze als Drittanbieter.

#### Denkstufen {#thinking-levels}

Einige LLM-Anbieter ermöglichen es Ihnen, die Denkstufe eines ausgewählten Modells anzupassen. Denkstufen definieren den Umfang der Überlegungen, die das Modell vor der Antwort durchführt – von schnellen, direkten Antworten bis hin zu längeren Argumentationsketten. Dies beeinflusst die Antwortqualität, Latenz und den Token-Verbrauch.

| Stufe | Wann verwenden |
|-------|-------------|
| **Minimal** | Einfache, klar definierte Aufgaben (z. B. Katalogsuche, einfache Klassifizierung). Schnellste Antworten und niedrigste Kosten. |
| **Niedrig** | Aufgaben, die von etwas mehr Überlegung profitieren, aber keine tiefgehende Analyse erfordern. |
| **Mittel** | Mehrstufige oder nuancierte Aufgaben (z. B. Analyse mehrerer Eingaben, um eine Aktion zu empfehlen). |
| **Hoch** | Komplexe Argumentation, Sonderfälle oder wenn das Modell Schritte durchdenken soll, bevor es antwortet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Denkstufen" }

Wir empfehlen, mit **Minimal** zu beginnen und die Antworten Ihres Agenten zu testen. Anschließend können Sie die Denkstufe auf **Niedrig** oder **Mittel** anpassen, wenn der Agent Schwierigkeiten hat, genaue Antworten zu liefern. In seltenen Fällen kann eine **hohe** Denkstufe erforderlich sein, wobei diese Stufe zu hohen Token-Kosten und längeren Antwortzeiten oder einem höheren Risiko von Timeout-Fehlern führen kann. Wenn Ihr Agent Schwierigkeiten hat, mehrstufiges Denken mit angemessenen Antwortzeiten in Einklang zu bringen, sollten Sie Ihren Anwendungsfall in mehrere Agenten aufteilen, die in einem Canvas oder Katalog zusammenarbeiten können.

Braze verwendet für ausgehende LLM-Aufrufe dieselben IP-Bereiche wie für Connected-Content. Die Bereiche sind in der [Connected-Content-IP-Zulassungsliste]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting) aufgeführt. Wenn Ihr Anbieter IP-Zulassungslisten unterstützt, können Sie den Schlüssel auf diese Bereiche beschränken, sodass nur Braze ihn verwenden kann.

{% alert important %}
Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bestimmungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie sich dafür entscheiden, Ihren eigenen API-Schlüssel einzubinden, gilt der Anbieter Ihres LLM-Abos gemäß dem Vertrag zwischen Ihnen und Braze als Drittanbieter.
{% endalert %}

#### Das richtige Modell bestimmen {#determine-which-model-to-use}

Jeder LLM-Anbieter bietet eine leicht unterschiedliche Mischung aus Modellfähigkeiten, Kosten und Denkstufen. Hier sind einige allgemeine Richtlinien und Best Practices:

- Für Kosteneffizienz sollten Sie zuerst Modelle mit niedrigeren Token-Kosten testen, bevor Sie zu teureren Modellen wechseln. Passen Sie nur dann auf teurere Modelle an, wenn günstigere Modelle mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente bzw. ungenaue Ergebnisse liefern.
- Für Geschwindigkeit und Performance-Effizienz sollten Sie zuerst niedrigere Denkstufen testen, bevor Sie höhere Denkstufen verwenden. Passen Sie nur dann auf höhere Denkstufen an, wenn niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente bzw. ungenaue Ergebnisse liefern.
- Wenn günstigere Modelle oder niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente bzw. ungenaue Ergebnisse liefern, sollten Sie auf teurere Modelle oder höhere Denkstufen umsteigen.
- Achten Sie beim Testen darauf, Zuverlässigkeit und Genauigkeit mit Token-Verbrauch und Aufrufdauer in Einklang zu bringen.
- Jeder Anwendungsfall kann ein anderes optimales Modell und eine andere optimale Denkstufe haben. Wir empfehlen gründliches Testen, um konsistente Qualität ohne Timeouts sicherzustellen.

### Aufruf-Rate-Limits {#invocation-flow-controls}

Die folgenden Aufruf-Rate-Limits gelten pro Workspace:

- **Von Braze bereitgestelltes Modell:** 5.000 Aufrufe pro Minute
- **Eigener API-Schlüssel:** 5.000 Aufrufe pro Minute

Wenn viele Nutzer:innen gleichzeitig einen Agenten-Schritt aufrufen, reiht Braze die Aufrufe gemäß diesen Limits in eine Warteschlange ein, sodass die Verarbeitung bei Sendungen mit hohem Volumen länger dauern kann.

### Tägliche Aufruf- und Credit-Limits {#daily-invocation-and-credit-limits}

Jeder Agent hat ein tägliches Aufruflimit (Standard 250.000; Maximum 1.000.000, sofern Ihr Vertrag nichts anderes vorsieht). Jeder Aufruf – einschließlich Vorschauen in der Agentenkonsole und Test-Canvas-Durchläufe mit **Antwort simulieren** – wird auf dieses Limit angerechnet.

In der Agentenkonsole schätzt das **Tägliche Aktions-Credit-Kostenlimit** die maximalen Credits, die ein Agent pro Tag verbrauchen kann. Braze multipliziert das **Credit-Verhältnis** pro Aufruf Ihres Workspace für das ausgewählte Modell mit dem täglichen Aufruflimit.

### Credit-Verbrauch überwachen {#monitor-credit-usage}

Gehen Sie zu **Einstellungen** > **Abrechnung** > **Credit-Verbrauch** > **Agent Console**, um den Credit-Verbrauch, die Aufrufzahlen und die Credit-Verhältnisse pro Agent einzusehen.

Credit-Verhältnisse ergeben sich aus Ihrem Vertrag und werden im Dashboard [Credit-Verbrauch]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) angezeigt (Tab **Credit Ratios** und Tab **Agent Console**). Die Schätzung wird aktualisiert, wenn Sie das Modell oder das Aufruflimit ändern.

Um die Ausgaben zu steuern, senken Sie das tägliche Aufruflimit. Bei [Bring-your-own (BYO)](#option-2-bring-your-own-api-key)-Modellen können Sie auch ein günstigeres Modell wählen oder die [Denkstufe](#thinking-levels) reduzieren, um die Token-Kosten beim Anbieter zu senken. **Braze Auto** unterstützt keine Anpassung der Denkstufe.

### Rate-Limit-Fehler {#rate-limit-errors}

Wenn der LLM-Anbieter während eines Canvas-Schritt-Agenten- oder Katalog-Agenten-Aufrufs einen Rate-Limit-Fehler zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann.

Wenn alle Canvas- oder Katalog-Wiederholungsversuche erschöpft sind, zeigt das Detailpanel **Logs** den Status **Error** und die Anbieternachricht (z. B. `Rate limit exceeded`) unter **Output** an. Wiederholungsversuche sind in den Logs sichtbar, einschließlich des allerersten Aufrufs unabhängig von seinem endgültigen Erfolg oder Misserfolg. Wenn es bei einer bestimmten Nutzerin bzw. einem bestimmten Nutzer vier Wiederholungsversuche braucht, um schließlich einen Erfolg zu erzielen, können Sie die Nutzer-ID suchen und alle fünf Einträge (Original plus vier Wiederholungen) in den **Logs** sehen. Das Original und die ersten drei Wiederholungen zeigen dabei **Error** mit `Rate limit exceeded` an.

![Agentenkonsole-Logdetails mit einem „Rate limit exceeded“-Fehler im Ausgabefeld.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Anweisungen verfassen {#writing-instructions}

Anweisungen sind die Regeln oder Richtlinien, die Sie dem Agenten geben (System-Prompt). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Systemanweisungen können bis zu 25 KB groß sein.

Wenn Sie Ihren Agenten mit [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) unter Verwendung eines [Start-Templates]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) erstellt haben, überprüfen Sie die vorausgefüllten Anweisungen und bearbeiten Sie diese nach Bedarf.

Hier sind einige allgemeine Best Practices für den Einstieg in das Prompting:

1. Beginnen Sie mit dem Ziel vor Augen. Formulieren Sie zuerst das Ziel.
2. Weisen Sie dem Modell eine Rolle oder Persona zu („Sie sind ein ...“).
3. Legen Sie einen klaren Kontext und klare Vorgaben fest (Zielgruppe, Länge, Tonfall, Format).
4. Fordern Sie Struktur an („Geben Sie JSON/Aufzählungsliste/Tabelle zurück ...“).
5. Zeigen statt erklären. Fügen Sie einige hochwertige Beispiele bei.
6. Teilen Sie komplexe Aufgaben in geordnete Schritte auf („Schritt 1 ... Schritt 2 ...“).
7. Fördern Sie das logische Denken („Überlegen Sie die einzelnen Schritte im Kopf und geben Sie dann eine prägnante endgültige Antwort“ oder „Erläutern Sie kurz Ihre Entscheidung“).
8. Testen, überprüfen und iterieren. Kleine Optimierungen können zu erheblichen Qualitätssteigerungen führen.
9. Behandeln Sie Sonderfälle, fügen Sie Sicherheitsvorkehrungen hinzu und ergänzen Sie Ablehnungsanweisungen.
10. Messen und dokumentieren Sie, was intern für die Wiederverwendung und Skalierung funktioniert.

### Beispiele {#examples}

Für Startkonfigurationen in der Agentenkonsole siehe [Agenten-Templates, erstellt mit Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Für vollständige Anweisungsbeispiele, die Sie kopieren oder anpassen können, besuchen Sie die [Anwendungsfallbibliothek für Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Beispiel | Kategorie | Agententyp | Beschreibung |
| --- | --- | --- | --- |
| [Personalisierte Nachrichten basierend auf dem Kontext von Nutzer:innen verfassen]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Inhaltserstellung | Canvas-Schritt-Agent | Generiert koordinierte E-Mail-Betreffzeile/Preheader und Push-Titel/Text für Nutzer:innen, die gesucht, aber nicht gebucht haben. |
| [Nutzerfeedback analysieren, um nächste Schritte zu bestimmen]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Datenstandardisierung | Canvas-Schritt-Agent | Klassifiziert die Stimmung und das Thema einer Umfrage nach der Reise und empfiehlt dann einen CRM-Folgeschritt. |
| [Nutzer:innen anhand vorhandener Attribute in Interessen-Buckets kategorisieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Affinitäts-Agent | Canvas-Schritt-Agent | Klassifiziert Nutzer:innen anhand von Attributen und High-Intent-Signalen in Interessen-Buckets und empfiehlt dann das beste nächste Erlebnis oder den besten nächsten Artikel. |
| [Nutzer:innen basierend auf aktuellem Verhalten zum relevantesten Canvas-Pfad weiterleiten]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Affinitäts-Agent | Canvas-Schritt-Agent | Leitet die Motivation aus dem aktuellen Verhalten ab und gibt den besten Routenschlüssel für den nächsten Canvas-Schritt zurück. |
| [Nutzer:innen basierend auf Echtzeit-High-Intent-Aktionen Interessenkategorien zuweisen]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Affinitäts-Agent | Canvas-Schritt-Agent | Weist Interessenkategorien basierend auf High-Intent-Aktionen zu und empfiehlt das beste nächste Erlebnis oder den besten nächsten Artikel. |
| [Eingehende Nachrichten auf Opt-out-Absicht klassifizieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Klassifizierung und Routing | Canvas-Schritt-Agent | Gibt einen strikten booleschen Wert zurück, der angibt, ob eine Nachricht eine Opt-out-Anfrage ist. |
| [Eingehende Nachrichten in strukturierte Daten für die Automatisierung standardisieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Datenstandardisierung | Canvas-Schritt-Agent | Normalisiert eingehende SMS oder Chat-Nachrichten in strukturierte Absichten, Entitäten und Compliance-Flags für nachgelagerte Automatisierung. |
| [Konversionsstarke Beschreibungen erstellen, die den Markenrichtlinien entsprechen]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Inhaltserstellung | Katalog-Agent | Generiert kurze, markengerechte Beschreibungen für jede Katalogzeile. |
| [Übersetzungen basierend auf der regionalen Sprache bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Kataloganreicherung | Katalog-Agent | Lokalisiert UI- und Marketing-Strings pro Gebietsschema und Zeichenlimit. |
| [Katalogeinträge mit Beschreibungen, Kategorien und Tags anreichern]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Kataloganreicherung | Katalog-Agent | Generiert erweiterte Beschreibungen, Kategorien und Tags aus vorhandenen Katalogdaten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Zusammenfassung der Beispiele" }

### Liquid verwenden {#using-liquid}

Die Einbindung von [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) in die Anweisungen Ihres Agenten kann dessen Antworten eine zusätzliche Ebene der Personalisierung verleihen. Sie können die genaue Liquid-Variable angeben, die der Agent erhält, und diese in den Kontext Ihres Prompts einfügen. Anstatt beispielsweise explizit „Vorname“ zu schreiben, können Sie das Liquid-Snippet {% raw %}`{{${first_name}}}`{% endraw %} verwenden:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Im Abschnitt **Logs** der **Agent Console** können Sie die Details zu den Ein- und Ausgabedaten des Agenten überprüfen, um zu verstehen, welcher Wert aus Liquid gerendert wird.

### Welche Daten Agenten erhalten {#what-data-agents-receive}

Der Agentenkontext ist kein offenes Konversationsgedächtnis. Anders als ein Chat-Assistent sieht ein Agent nur die Daten, die Sie ihm zum Zeitpunkt des Aufrufs explizit übergeben – er durchsucht keine Nutzerprofile, leitet fehlende Felder ab und teilt Ihnen auch nicht mit, wenn erforderliche Informationen fehlen.

Gestalten Sie jeden Agenten als eine bewusste Eingabe-zu-Ausgabe-Pipeline. Verbinden Sie jeden Datenpunkt, den der Agent benötigt, über eine oder mehrere der folgenden Methoden:

1. **Liquid in Anweisungen:** Verwenden Sie Nutzerattribute ({% raw %}`{{${first_name}}}`{% endraw %}) und [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) direkt im Agenten-Prompt als Template.
2. **+ Agentenkontext:** Wählen Sie Kataloge, Segmentzugehörigkeit, Markenrichtlinien, **Gesamter Canvas-Kontext** oder Nutzerinteraktionsdaten in der Agentenkonsole aus.
3. [Kontextschritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): Setzen oder aktualisieren Sie `context.*`-Variablen im Canvas vor der Ausführung eines Agenten-Schritts.
4. **Zusätzlicher Kontext im Agenten-Schritt:** Übergeben Sie alle zusätzlichen Liquid-Template-Werte, die nicht bereits über die anderen Methoden angegeben wurden, zum Sendezeitpunkt über die Schrittkonfiguration an den Agenten.

Stellen Sie sicher, dass Sie diese Kontextvariablen entweder als Liquid-Template in den Agentenanweisungen verwenden oder **Gesamten Canvas-Kontext hinzufügen** auswählen. Wenn ein Wert nicht über einen dieser Kanäle übergeben wird, erhält der Agent ihn nicht. Listen Sie die erforderlichen Eingaben in Ihren Anweisungen oder in den [Voraussetzungen für Anwendungsfälle]({{site.baseurl}}/user_guide/brazeai/agents/use_cases) auf und überprüfen Sie die Eingaben unter **Agent Console** > **Logs** nach dem Testen.

![Die Details für einen Agenten, der Liquid in seinen Anweisungen verwendet.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Für Katalog-Agenten verwenden Sie **Felder** im Abschnitt **Ausgabe** anstelle von JSON Schema. Sie können dennoch Anweisungen verfassen, die das Modell auffordern, eine Schlüssel-Wert-Ausgabe zu liefern, die diesen Feldnamen entspricht.

Weitere Informationen zu Best Practices für Prompting finden Sie in den Leitfäden der folgenden Modellanbieter:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Ausgaben {#outputs}

Wenn Sie Ihren Agenten mit [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) unter Verwendung eines [Start-Templates]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) erstellt haben, überprüfen Sie das vorausgefüllte Ausgabeschema und bearbeiten Sie es nach Bedarf.

### Einfache Schemata {#basic-schemas}

Einfache Schemata sind eine einfache Ausgabe, die ein Agent zurückgibt. Dies kann ein String, eine Zahl, ein boolescher Wert, ein String-Array oder ein Zahlen-Array sein.

Wenn Sie beispielsweise Stimmungswerte von Nutzer:innen aus einer einfachen Feedback-Umfrage erfassen möchten, um die Zufriedenheit Ihrer Kund:innen nach Erhalt eines Produkts zu ermitteln, können Sie **Number** als einfaches Schema auswählen, um das Ausgabeformat zu strukturieren.

{% alert important %}
Arrays sind nur für Canvas-Schritt-Agenten verfügbar, nicht für Katalog-Agenten.
{% endalert %}

![Agentenkonsole mit „Number“ als einfachem Schema ausgewählt.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Erweiterte Schemata {#advanced-schemas}

Erweiterte Schema-Optionen umfassen die manuelle Strukturierung von Feldern oder die Verwendung von JSON.

- **Felder:** Eine No-Code-Methode, um eine konsistente Agentenausgabe zu erzwingen.
- **JSON:** Ein Code-Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können. Nur für Canvas-Schritt-Agenten verfügbar, nicht für Katalog-Agenten.

Wir empfehlen die Verwendung erweiterter Schemata, wenn der Agent eine Datenstruktur mit mehreren strukturiert definierten Werten zurückgeben soll, anstatt einer einzelnen Ausgabe. Dadurch kann die Ausgabe besser als konsistente Kontextvariable formatiert werden.

### Fallback-Ausgabe {#fallback-output}

Fallback-Werte sind nur für Canvas-Schritt-Agenten verfügbar. Im Abschnitt **Ausgabe** der Agentenkonsole für einen Canvas-Schritt-Agenten können Sie Werte definieren, die Braze verwendet, wenn ein Aufruf fehlschlägt.

Für **JSON**-Schemata liest Braze das Schema und generiert ein Eingabefeld für jede Eigenschaft, sodass Sie einen Fallback-Wert pro Schlüssel festlegen können. Für **Felder**-Schemata geben Sie einen Fallback-Wert für jedes Feld ein. Für einfache Schemata geben Sie einen einzelnen Fallback-Wert ein. Canvas-Schritt-Agenten unterstützen Liquid in Fallback-Werten.

Informationen zu den Einrichtungsschritten finden Sie unter [Fallback-Werte konfigurieren]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Informationen zum Laufzeitverhalten in Canvas finden Sie unter [Fehlerbehandlung und Fallback-Verhalten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Beispielsweise können Sie ein Ausgabeformat innerhalb eines Agenten verwenden, der eine Beispiel-Reiseroute für Nutzer:innen basierend auf einem eingereichten Formular erstellen soll. Das Ausgabeformat ermöglicht es Ihnen festzulegen, dass jede Agentenantwort Werte für `tripStartDate`, `tripEndDate` und `destination` enthalten soll. Jeder dieser Werte kann aus Kontextvariablen extrahiert und in einem Nachrichtenschritt zur Personalisierung mit Liquid eingefügt werden.

{% tabs %}
{% tab Felder %}

Wenn Sie Antworten auf eine einfache Feedback-Umfrage formatieren möchten, um zu ermitteln, wie wahrscheinlich es ist, dass Befragte die neueste Eissorte Ihres Restaurants weiterempfehlen, können Sie die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erweiterte Schemata" }

![Agentenkonsole mit drei Ausgabefeldern für Wahrscheinlichkeitswert, Erklärung und Konfidenzwert.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON Schema %}

Wenn Sie Nutzerfeedback zur letzten Restauranterfahrung in Ihrer Restaurantkette erfassen möchten, können Sie **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Stimmungsvariable und eine Begründungsvariable enthält.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## Kataloge und Felder {#catalogs-and-fields}

Wählen Sie bestimmte Kataloge aus, die ein Agent referenzieren soll, und geben Sie Ihrem Agenten den Kontext, den er benötigt, um Ihre Produkte und andere nicht-nutzerbezogene Daten zu verstehen. Agenten verwenden Tools, um nur die relevanten Einträge zu finden und diese an das LLM zu senden, um den Token-Verbrauch zu minimieren. Für eine bessere Katalogabfrage erstellen Sie eine [Wissensquelle]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) und fügen Sie diese als Agentenkontext hinzu, anstatt den Katalog direkt anzuhängen.

![Der Katalog „restaurants“ und die Spalte „Loyalty_Program“, die für die Suche durch den Agenten ausgewählt wurden.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Wenn Sie einen Katalog-Agenten in einem Katalogfeld bereitstellen, aktivieren Sie die Pflichtfeld-Steuerung und wählen Sie aus, welche ausgewählten Spalten für die Ausführung erforderlich sind, bevor der Agent aufgerufen wird. Der Agent überspringt eine Zeile nur dann, wenn eine dieser Pflichtspalten leer ist oder fehlt – beispielsweise ein `gender`-Feld, das noch nicht ausgefüllt wurde. Ausgewählte Spalten sind standardmäßig als Pflichtfelder markiert, aber Sie können Spalten entfernen, die leer sein dürfen, ohne die Ausführung zu blockieren. Dies verhindert verschwendete Token bei unvollständigen Daten.

Katalog-Agenten berücksichtigen auch die Spaltenreihenfolge, wenn Eingabefelder voneinander abhängen. Wenn Spalte D aus den Spalten B und C generiert werden soll, führt der Agent Spalte D erst aus, wenn B und C Werte für diese Zeile enthalten.

Informationen zu Bereitstellungsszenarien und Beispielen finden Sie unter [Katalog-Agenten verwenden]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) und [Best Practices für Katalog-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Segmentzugehörigkeitskontext {#segment-membership-context}

Sie können bis zu fünf Segmente auswählen, anhand derer der Agent die Segmentzugehörigkeit jedes Nutzers bzw. jeder Nutzerin abgleichen kann, wenn der Agent in einem Canvas verwendet wird. Angenommen, Ihr Agent hat die Segmentzugehörigkeit für ein Segment „Treue-Nutzer:innen“ ausgewählt und wird in einem Canvas eingesetzt. Wenn Nutzer:innen einen Agenten-Schritt aufrufen, kann der Agent prüfen, ob jede Nutzerin bzw. jeder Nutzer Mitglied der in der Agentenkonsole angegebenen Segmente ist, und die Zugehörigkeit (oder Nicht-Zugehörigkeit) als Kontext für das LLM verwenden.

![Das Segment „Loyalty Users“, das für den Zugang zur Agenten-Mitgliedschaft ausgewählt wurde.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Markenrichtlinien {#brand-guidelines}

Sie können [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) auswählen, an die sich Ihr Agent bei seinen Antworten halten soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte erstellt, um Nutzer:innen zur Anmeldung für eine Fitnessstudio-Mitgliedschaft zu motivieren, können Sie dieses Feld verwenden, um Ihre vordefinierte, motivierende Richtlinie zu referenzieren.

## Nutzerspezifischer Interaktionsverlauf {#user-history}

Die Interaktionsdaten von Nutzer:innen umfassen ihre letzten Campaign- und Canvas-Öffnungen, Klicks und Conversion-Daten. Sie können diesen Kontext beispielsweise einbeziehen, damit ein Agent ihn bei der Auswertung in einem Canvas referenzieren kann. Der nutzerspezifische Interaktionsverlauf kann auch dazu beitragen, einen Agenten zu beeinflussen, dessen Aufgabe es ist, personalisierte Nachrichtentexte zu verfassen.

## Versionsverlauf {#version-history}

Die Agentenkonsole zeichnet jedes Mal eine neue Version auf, wenn Sie Änderungen am Agenten speichern. Der Tab **Versionsverlauf** listet jede gespeicherte Version und die Änderungen zwischen den Speichervorgängen auf.

1. Öffnen Sie den Agenten in der Agentenkonsole.
2. Wählen Sie den Tab **Versionsverlauf**.
3. Wählen Sie eine Version aus, um deren Konfiguration zu überprüfen.

Um zu sehen, was sich in einer Version geändert hat, wählen Sie **Anzeigen**. Braze zeigt einen Inline-Diff im Code-Stil an, der Ergänzungen und Löschungen hervorhebt. Gelöschte Inhalte werden mit roter Durchstreichung dargestellt.

Wenn Sie Anweisungen aus einer früheren Version wiederherstellen möchten, öffnen Sie **Anzeigen** für diese Version, kopieren Sie den Anweisungstext und fügen Sie ihn in Ihr aktuelles Feld **Anweisungen** ein.

{% alert tip %}
In der Inline-Diff-Ansicht drücken Sie <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) oder <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows), um alle Anweisungen ohne die rote Löschungsmarkierung auszuwählen, sodass Sie den sauberen Text kopieren und wiederherstellen können.
{% endalert %}

## Agenten duplizieren {#duplicate-agents}

Duplizieren Sie einen Agenten, um Verbesserungen oder Iterationen Seite an Seite mit dem Original zu testen. Verwenden Sie den [Versionsverlauf](#version-history), um frühere Konfigurationen zu überprüfen oder wiederherzustellen. So duplizieren Sie einen Agenten:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das <i class="fas fa-ellipsis-vertical"></i>-Menü aus.
2. Wählen Sie **Duplizieren**.

## Agenten archivieren {#archive-agents}

Wenn Sie weitere angepasste Agenten erstellen, können Sie die Seite **Agentenmanagement** organisieren, indem Sie Agenten archivieren, die nicht aktiv verwendet werden. So archivieren Sie einen Agenten:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das <i class="fas fa-ellipsis-vertical"></i>-Menü aus.
2. Wählen Sie **Archivieren**.