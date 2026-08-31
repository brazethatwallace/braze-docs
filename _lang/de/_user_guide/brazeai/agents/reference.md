---
nav_title: Referenz
article_title: Referenz für Agenten
description: "Wichtige Informationen zu Braze-Agenten."
page_order: 3
---

# Referenz für Agenten {#reference-for-agents}

> Wenn Sie angepasste Agenten erstellen, lesen Sie diesen Artikel für weitere Informationen zu wichtigen Einstellungen wie Anweisungen und Ausgabeschemata. Eine schrittweise Einrichtungsanleitung finden Sie unter [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents). Eine Einführung finden Sie unter [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) und [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq).

## Modelle {#models}

Wenn Sie einen Agenten einrichten, können Sie das Modell auswählen, das er zur Generierung von Antworten verwendet. Sie haben zwei Optionen: ein von Braze bereitgestelltes Modell verwenden oder Ihren eigenen API-Schlüssel mitbringen.

{% alert important %}
Das von Braze bereitgestellte **Auto**-Modell ist für Modelle optimiert, deren Denkfähigkeiten ausreichen, um Aufgaben wie die Katalogsuche und die Segment-Zugehörigkeit auszuführen. Bei der Verwendung anderer Modelle empfehlen wir, durch Tests zu bestätigen, dass Ihr Modell für Ihren Anwendungsfall gut funktioniert. Möglicherweise müssen Sie Ihre [Anweisungen](#writing-instructions) anpassen, um Modellen mit unterschiedlichen Geschwindigkeiten und Fähigkeiten unterschiedliche Detailstufen oder schrittweises Denken zu geben.
{% endalert %}

### Option 1: Ein von Braze bereitgestelltes Modell verwenden {#option-1-use-a-braze-powered-model}

Dies ist die einfachste Option, ohne zusätzliche Einrichtung. Braze bietet direkten Zugriff auf Large Language Models (LLMs). Um diese Option zu nutzen, wählen Sie **Auto**, was Gemini-Modelle verwendet.

{% alert important %}
Wenn Sie **Braze Auto** nicht als Option im **Modell**-Dropdown beim Erstellen eines Agenten sehen, wenden Sie sich an Ihren Customer-Success-Manager, um zu erfahren, wie Sie berechtigt werden können, das Braze-Auto-Modell zu nutzen.
{% endalert %}

### Option 2: Eigenen API-Schlüssel mitbringen {#option-2-bring-your-own-api-key}

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter mitbringen, werden Token-Kosten direkt über Ihren Anbieter abgerechnet, nicht über Braze.

Wir empfehlen, regelmäßig die neuesten Modelle zu testen, da ältere Modelle nach einigen Monaten eingestellt oder als veraltet markiert werden können. Stellen Sie sicher, dass Sie über ausreichende Guthaben bei Ihrem Anbieter verfügen, um Ihre Agenten im großen Maßstab auszuführen. Sie können sich auch für Agent-Console-Benachrichtigungen in den [Benachrichtigungseinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) anmelden, um benachrichtigt zu werden, wenn Braze erkennt, dass ein Modell nicht mehr verfügbar ist oder Abrechnungsprobleme mit Ihrem LLM-Anbieter auftreten.

So richten Sie dies ein:

1. Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie Ihren Anbieter.
2. Geben Sie Ihren API-Schlüssel vom Anbieter ein.
3. Wählen Sie **Speichern**.

Anschließend können Sie zu Ihrem Agenten zurückkehren und Ihr Modell auswählen.

Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Braze-Unterauftragsverarbeiter, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie sich entscheiden, Ihren eigenen API-Schlüssel mitzubringen, gilt der Anbieter Ihres LLM-Abonnements als Drittanbieter gemäß dem Vertrag zwischen Ihnen und Braze.

#### Denkstufen {#thinking-levels}

Einige LLM-Anbieter ermöglichen es Ihnen möglicherweise, die Denkstufe eines ausgewählten Modells anzupassen. Denkstufen definieren den Umfang des Denkens, den das Modell vor der Beantwortung verwendet – von schnellen, direkten Antworten bis hin zu längeren Argumentationsketten. Dies beeinflusst die Antwortqualität, Latenz und Token-Nutzung.

| Stufe | Wann verwenden |
|-------|----------------|
| **Minimal** | Einfache, klar definierte Aufgaben (wie Katalogsuche, einfache Klassifizierung). Schnellste Antworten und niedrigste Kosten. |
| **Niedrig** | Aufgaben, die von etwas mehr Argumentation profitieren, aber keine tiefe Analyse benötigen. |
| **Mittel** | Mehrstufige oder nuancierte Aufgaben (wie die Analyse mehrerer Eingaben, um eine Aktion zu empfehlen). |
| **Hoch** | Komplexe Argumentation, Grenzfälle oder wenn das Modell Schritte durcharbeiten soll, bevor es antwortet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Denkstufen" }

Wir empfehlen, mit **Minimal** zu beginnen und die Antworten Ihres Agenten zu testen. Anschließend können Sie die Denkstufe auf **Niedrig** oder **Mittel** anpassen, wenn Sie feststellen, dass der Agent Schwierigkeiten hat, genaue Antworten zu liefern. In seltenen Fällen kann eine **Hohe** Denkstufe erforderlich sein, obwohl die Verwendung dieser Stufe zu hohen Token-Kosten und längeren Antwortzeiten oder einem höheren Risiko von [Timeout-Fehlern]({{site.baseurl}}/user_guide/brazeai/agents/faq#what-might-cause-a-custom-agent-to-frequently-time-out) führen kann. Wenn Ihr Agent Schwierigkeiten hat, mehrstufige Argumentation mit angemessenen Antwortzeiten in Einklang zu bringen, sollten Sie erwägen, Ihren Anwendungsfall in mehr als einen Agenten aufzuteilen, die in einem Canvas oder Katalog zusammenarbeiten können.

Braze verwendet für ausgehende LLM-Aufrufe dieselben IP-Bereiche wie für Connected-Content. Die Bereiche sind in der [Connected-Content-IP-Allowlist]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting) aufgeführt. Wenn Ihr Anbieter IP-Allowlisting unterstützt, können Sie den Schlüssel auf diese Bereiche beschränken, sodass nur Braze ihn verwenden kann.

{% alert important %}
Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Braze-Unterauftragsverarbeiter, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie sich entscheiden, Ihren eigenen API-Schlüssel mitzubringen, gilt der Anbieter Ihres LLM-Abonnements als Drittanbieter gemäß dem Vertrag zwischen Ihnen und Braze.
{% endalert %}

#### Bestimmen, welches Modell zu verwenden ist {#determine-which-model-to-use}

Jeder LLM-Anbieter hat eine leicht unterschiedliche Mischung aus Modellfähigkeiten, Kosten und Denkstufen. Hier sind einige allgemeine Richtlinien und Best Practices:

- Priorisieren Sie für die Kosteneffizienz das Testen von Modellen mit niedrigeren Token-Kosten gegenüber Modellen mit höheren Kosten. Wechseln Sie nur dann zu teureren Modellen, wenn günstigere Modelle mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente oder ungenaue Ergebnisse liefern.
- Priorisieren Sie für Geschwindigkeit und Performance das Testen niedrigerer Denkstufen gegenüber höheren. Wechseln Sie nur dann zu höheren Denkstufen, wenn niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente oder ungenaue Ergebnisse liefern.
- Wenn günstigere Modelle oder niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente oder ungenaue Ergebnisse liefern, erwägen Sie den Wechsel zu teureren Modellen oder höheren Denkstufen.
- Stellen Sie beim Testen sicher, dass Sie die Zuverlässigkeit und Genauigkeit mit der Token-Nutzung und der Aufruf-Dauer in Einklang bringen.
- Jeder Anwendungsfall kann ein anderes optimales Modell und eine andere optimale Denkstufe haben. Wir empfehlen gründliches Testen, um eine konsistente Qualität ohne Timeouts sicherzustellen.

### Aufruf-Flow-Steuerungen {#invocation-flow-controls}

Die folgenden Aufruf-Flow-Steuerungen gelten pro Workspace:

- **Von Braze bereitgestelltes Modell:** 5.000 Aufrufe pro Minute
- **Eigener API-Schlüssel:** 5.000 Aufrufe pro Minute

Wenn viele Nutzer:innen gleichzeitig einen Agenten-Schritt betreten, stellt Braze die Aufrufe gemäß diesen Limits in eine Warteschlange, sodass die Verarbeitung bei Sends mit hohem Volumen länger dauern kann.

### Tägliche Aufruf- und Credit-Limits {#daily-invocation-and-credit-limits}

Jeder Agent hat ein tägliches Aufruf-Limit (Standard 250.000; Maximum 1.000.000, sofern Ihr Vertrag nicht höhere Werte erlaubt). Jeder Aufruf (einschließlich Agent-Console-Vorschauen und Test-Canvas-Durchläufe, die **Antwort simulieren** verwenden) zählt zu diesem Limit.

In der Agent Console schätzt das **Tägliche Aktions-Credit-Kostenlimit** die maximalen Credits, die ein Agent pro Tag verbrauchen kann. Braze multipliziert das pro-Aufruf-Credit-Verhältnis Ihres Workspace für das ausgewählte Modell mit dem täglichen Aufruf-Limit.

### Wann Credits verbraucht werden {#when-credits-are-consumed}

Braze berechnet Credits nur für Aufrufe, die die Verarbeitung abschließen. Credits werden nicht verbraucht, wenn ein Aufruf aufgrund folgender Ursachen fehlschlägt:

- Ein [Rate-Limit-Fehler](#rate-limit-errors) vom LLM-Anbieter (einschließlich Wiederholungsversuche, die letztlich fehlschlagen)
- Das ausgewählte Modell ist nicht verfügbar
- Der Agent hat sein tägliches Aufruf-Limit erreicht

Credits werden verbraucht, wenn ein Aufruf ein Timeout hat, auch wenn der Agent keine verwendbare Ausgabe zurückgibt.

### Credit-Nutzung überwachen {#monitor-credit-usage}

Gehen Sie zu **Einstellungen** > **Abrechnung** > **Credit-Nutzung** > **Agent Console**, um den Credit-Verbrauch, die Aufrufzahlen und die Credit-Verhältnisse pro Agent einzusehen.

Credit-Verhältnisse ergeben sich aus Ihrem Vertrag und erscheinen im [Credit-Nutzung]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)-Dashboard (Tab **Credit-Verhältnisse** und Tab **Agent Console**). Die Schätzung wird aktualisiert, wenn Sie das Modell oder das Aufruf-Limit ändern.

Um die Ausgaben zu steuern, senken Sie das tägliche Aufruf-Limit. Für Modelle mit [eigenem API-Schlüssel (BYO)](#option-2-bring-your-own-api-key) können Sie auch ein günstigeres Modell wählen oder die [Denkstufe](#thinking-levels) reduzieren, um die Token-Kosten beim Anbieter zu senken. Braze Auto unterstützt keine Anpassung der Denkstufe.

### Rate-Limit-Fehler {#rate-limit-errors}

Wenn der LLM-Anbieter während eines Canvas-Schritt-Agenten- oder Katalog-Agenten-Aufrufs einen Rate-Limit-Fehler zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann.

Wenn die Canvas- oder Katalog-Wiederholungsversuche erschöpft sind, zeigt das **Logs**-Detailpanel **Error** und die Anbieternachricht (wie `Rate limit exceeded`) unter **Output**. Wiederholungsversuche sind in den Logs sichtbar, einschließlich des allerersten Aufrufs unabhängig von seinem endgültigen Erfolg oder Misserfolg. Wenn es für eine bestimmte Nutzer:in vier Wiederholungsversuche bis zum Erfolg dauert, können Sie die Nutzer-ID suchen und alle fünf (Original plus vier Wiederholungen) in den **Logs** sehen, wobei das Original und die ersten drei Wiederholungen **Error** mit `Rate limit exceeded` anzeigen.

Rate-Limit-Fehler verbrauchen keine Braze-Credits, einschließlich fehlgeschlagener Wiederholungsversuche, die in den **Logs** angezeigt werden.

![Agent-Console-Log-Details, die einen Rate-Limit-Exceeded-Fehler im Output-Feld zeigen.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Anleitung schreiben {#writing-instructions}

Anleitungen sind die Regeln oder Richtlinien, die Sie dem Agent (Systemprompt) mitgeben. Sie definieren, wie sich der Agent bei jeder Ausführung verhalten soll. Systemanleitungen können bis zu 25 KB umfassen.

Wenn Sie Ihren Agent mit [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) über ein [Start-Template]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) erstellt haben, überprüfen Sie die vorausgefüllten Anleitungen und bearbeiten Sie diese nach Bedarf.

Hier sind einige allgemeine Best Practices für den Einstieg in das Prompting:

1. Beginnen Sie mit dem Ziel vor Augen. Nennen Sie zuerst das Ziel.
2. Geben Sie dem Modell eine Rolle oder Persona („Du bist ein/eine …“).
3. Setzen Sie klaren Kontext und Einschränkungen (Zielgruppe, Länge, Ton, Format).
4. Fordern Sie Struktur an („Gib JSON / eine Aufzählung / eine Tabelle zurück …“).
5. Zeigen, nicht erzählen. Fügen Sie einige hochwertige Beispiele ein.
6. Unterteilen Sie komplexe Aufgaben in geordnete Schritte („Schritt 1 … Schritt 2 …“).
7. Ermutigen Sie zum Durchdenken („Denke die Schritte intern durch und gib dann eine knappe Antwort“ oder „Erkläre kurz deine Entscheidung“).
8. Testen, prüfen und iterieren. Kleine Anpassungen können zu großen Qualitätsgewinnen führen.
9. Behandeln Sie Grenzfälle, fügen Sie Leitplanken hinzu und fügen Sie Ablehnungsanweisungen hinzu.
10. Messen und dokumentieren Sie, was intern funktioniert, zur Wiederverwendung und Skalierung.

### Beispiele {#examples}

Für Startkonfigurationen in der Agent Console siehe [Agent-Templates erstellt mit Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Für vollständige Anleitungsbeispiele, die Sie kopieren oder anpassen können, siehe die [Anwendungsfall-Bibliothek für Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Beispiel | Kategorie | Agent-Typ | Was er tut |
| --- | --- | --- | --- |
| [Personalisiertes Messaging basierend auf dem Kontext der Nutzer:innen verfassen]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Inhaltserstellung | Canvas Step Agent | Generiert koordinierte E-Mail-Betreff-/Preheader- und Push-Titel-/Textinhalte für Nutzer:innen, die gesucht, aber nicht gebucht haben. |
| [Nutzer:innen-Feedback analysieren, um nächste Schritte zu bestimmen]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Datenstandardisierung | Canvas Step Agent | Klassifiziert die Stimmung und das Thema einer Nachreise-Umfrage und empfiehlt dann einen CRM-Folgeschritt. |
| [Nutzer:innen anhand bestehender Attribute in Interessen-Buckets einordnen]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Affinitäts-Agent | Canvas Step Agent | Ordnet Nutzer:innen anhand von Attributen und Signalen mit hoher Kaufabsicht in Interessen-Buckets ein und empfiehlt dann das beste nächste Erlebnis oder den besten nächsten Artikel. |
| [Nutzer:innen basierend auf aktuellem Verhalten zum relevantesten Canvas-Pfad weiterleiten]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Affinitäts-Agent | Canvas Step Agent | Leitet die Motivation aus dem aktuellen Verhalten ab und gibt den besten Routenschlüssel für den nächsten Canvas-Schritt der Nutzer:innen zurück. |
| [Nutzer:innen anhand von Realtime-Aktionen mit hoher Kaufabsicht Interessenkategorien zuweisen]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Affinitäts-Agent | Canvas Step Agent | Weist Interessenkategorien anhand von Aktionen mit hoher Kaufabsicht zu und empfiehlt das beste nächste Erlebnis oder den besten nächsten Artikel. |
| [Eingehende Nachrichten auf Opt-out-Absicht klassifizieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Klassifizierung und Routing | Canvas Step Agent | Gibt einen strikten Boolean zurück, der angibt, ob eine Nachricht eine Opt-out-Anfrage ist. |
| [Eingehende Nachrichten in strukturierte Daten für die Automatisierung standardisieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Datenstandardisierung | Canvas Step Agent | Normalisiert eingehende SMS oder Chat-Nachrichten in strukturierte Absicht, Entitäten und Compliance-Flags für nachgelagerte Automatisierung. |
| [Hochkonvertierende Beschreibungen verfassen, die den Markenrichtlinien entsprechen]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Inhaltserstellung | Catalog Agent | Generiert kurze, markengerechte Beschreibungen für jede Zeile im Katalog. |
| [Übersetzungen basierend auf der regionalen Sprache bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Kataloganreicherung | Catalog Agent | Lokalisiert UI- und Marketing-Strings nach Locale und Zeichenlimit. |
| [Katalogartikel mit Beschreibungen, Kategorien und Tags anreichern]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Kataloganreicherung | Catalog Agent | Generiert erweiterte Beschreibungen, Kategorien und Tags aus vorhandenen Katalogartikeldaten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Zusammenfassung der Beispiele" }

### Liquid verwenden {#using-liquid}

Das Einfügen von [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) in die Anleitungen Ihres Agents kann eine zusätzliche Personalisierungsebene in der Antwort schaffen. Sie können die genaue Liquid-Variable angeben, die der Agent erhält, und sie im Kontext Ihres Prompts verwenden. Anstatt beispielsweise explizit „Vorname“ zu schreiben, können Sie das Liquid-Snippet {% raw %}`{{${first_name}}}`{% endraw %} verwenden:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Im Bereich **Logs** der **Agent Console** können Sie die Details zu den Eingaben und Ausgaben des Agents überprüfen, um zu verstehen, welcher Wert aus dem Liquid gerendert wird.

### Welche Daten Agents erhalten {#what-data-agents-receive}

Der Agent-Kontext ist kein offenes Konversationsgedächtnis. Anders als ein Chat-Assistent sieht ein Agent nur die Daten, die Sie zum Aufrufzeitpunkt explizit übergeben – er durchsucht keine Nutzer:innenprofile, leitet fehlende Felder nicht ab und meldet auch nicht, wenn erforderliche Informationen fehlen.

Gestalten Sie jeden Agent als eine bewusste Eingabe-zu-Ausgabe-Pipeline. Verbinden Sie jeden Datenpunkt, den der Agent benötigt, über eine oder mehrere der folgenden Methoden:

1. **Liquid in Anleitungen:** Nutzer:innenattribute ({% raw %}`{{${first_name}}}`{% endraw %}) und [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) direkt im Agent-Prompt als Template verwenden.
2. **+ Agent-Kontext:** Kataloge, Segment-Mitgliedschaft, Markenrichtlinien, **All Canvas Context** oder Nutzer:innen-Interaktionsdaten in der Agent Console auswählen.
3. [Kontext-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): `context.*`-Variablen im Canvas vor der Ausführung eines Agent-Schritts setzen oder aktualisieren.
4. **Zusätzlicher Kontext im Agent-Schritt:** Alle zusätzlichen Liquid-Template-Werte, die nicht bereits über die anderen Methoden angegeben sind, zum Sendezeitpunkt aus der Schrittkonfiguration an den Agent übergeben.

Stellen Sie sicher, dass Sie diese Kontextvariablen entweder als Liquid-Template in den Agent-Anleitungen verwenden oder **Add All Canvas Context** auswählen. Wenn ein Wert nicht über einen dieser Kanäle übergeben wird, erhält der Agent ihn nicht. Listen Sie erforderliche Eingaben in Ihren Anleitungen oder in den [Voraussetzungen für Anwendungsfälle]({{site.baseurl}}/user_guide/brazeai/agents/examples) auf und überprüfen Sie die Eingaben unter **Agent Console** > **Logs** nach dem Testen.

![Die Details für einen Agent, der Liquid in seinen Anleitungen verwendet.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Für Catalog Agents verwenden Sie **Fields** im Abschnitt **Output** anstelle von JSON-Schema; Sie können dennoch Anleitungen schreiben, die das Modell auffordern, Schlüssel-Wert-Ausgaben zu liefern, die diesen Feldnamen entsprechen.

Weitere Informationen zu Best Practices für das Prompting finden Sie in den Leitfäden der folgenden Modellanbieter:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Ausgaben {#outputs}

Wenn Sie Ihren Agenten mit [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) unter Verwendung eines [Start-Templates]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) erstellt haben, überprüfen Sie das vorausgefüllte Ausgabeschema und bearbeiten Sie es bei Bedarf.

### Einfache Schemas {#basic-schemas}

Einfache Schemas sind eine simple Ausgabe, die ein Agent zurückgibt. Dies kann ein String, eine Zahl, ein boolescher Wert, ein String-Array oder ein Zahlenarray sein.

Wenn Sie beispielsweise Stimmungswerte von Nutzer:innen aus einer einfachen Feedback-Umfrage erfassen möchten, um herauszufinden, wie zufrieden Ihre Kund:innen nach dem Erhalt eines Produkts sind, können Sie **Number** als einfaches Schema auswählen, um das Ausgabeformat zu strukturieren.

{% alert important %}
Arrays sind nur für Canvas-Schritt-Agenten verfügbar, nicht für Katalog-Agenten.
{% endalert %}

![Agent-Konsole mit „Number“ als ausgewähltem einfachen Schema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Erweiterte Schemas {#advanced-schemas}

Erweiterte Schema-Optionen umfassen die manuelle Strukturierung von Feldern oder die Verwendung von JSON.

- **Fields:** Eine No-Code-Methode, um eine konsistente Agentenausgabe zu erzwingen.
- **JSON:** Ein codebasierter Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können. Nur für Canvas-Schritt-Agenten verfügbar, nicht für Katalog-Agenten.

Wir empfehlen die Verwendung erweiterter Schemas, wenn der Agent eine Datenstruktur mit mehreren in strukturierter Weise definierten Werten zurückgeben soll, anstatt einer einzelnen Ausgabe. Dies ermöglicht eine bessere Formatierung der Ausgabe als konsistente Kontextvariable.

### Fallback-Ausgabe {#fallback-output}

Fallback-Werte sind nur für Canvas-Schritt-Agenten verfügbar. Im Abschnitt **Output** der Agent-Konsole für einen Canvas-Schritt-Agenten können Sie Werte definieren, die Braze verwendet, wenn ein Aufruf fehlschlägt.

Bei **JSON**-Schemas liest Braze das Schema und generiert ein Eingabefeld für jede Eigenschaft, sodass Sie einen Fallback-Wert pro Schlüssel festlegen können. Bei **Fields**-Schemas geben Sie einen Fallback-Wert für jedes Feld ein. Bei einfachen Schemas geben Sie einen einzelnen Fallback-Wert ein. Canvas-Schritt-Agenten unterstützen Liquid in Fallback-Werten.

Für die Einrichtungsschritte siehe [Fallback-Werte konfigurieren]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Für das Laufzeitverhalten in Canvas siehe [Fehlerbehandlung und Fallback-Verhalten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Sie können beispielsweise ein Ausgabeformat innerhalb eines Agenten verwenden, der eine Beispiel-Reiseroute für Nutzer:innen basierend auf einem eingereichten Formular erstellen soll. Das Ausgabeformat ermöglicht es Ihnen, festzulegen, dass jede Agentenantwort Werte für `tripStartDate`, `tripEndDate` und `destination` enthalten soll. Jeder dieser Werte kann aus Kontextvariablen extrahiert und mithilfe von Liquid in einem Nachrichtenschritt zur Personalisierung verwendet werden.

{% tabs %}
{% tab Fields %}

Wenn Sie Antworten auf eine einfache Feedback-Umfrage formatieren möchten, um herauszufinden, wie wahrscheinlich es ist, dass die Befragten die neueste Eissorte Ihres Restaurants weiterempfehlen, können Sie die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erweiterte Schemas" }

![Agent-Konsole mit drei Ausgabefeldern für Wahrscheinlichkeitsbewertung, Erklärung und Konfidenzwert.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON-Schema %}

Wenn Sie Nutzerfeedback zur letzten Essenserfahrung in Ihrer Restaurantkette erfassen möchten, können Sie **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Stimmungsvariable und eine Begründungsvariable enthält.

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

Wählen Sie bestimmte Kataloge aus, auf die ein Agent verweisen kann, und geben Sie Ihrem Agenten den Kontext, den er benötigt, um Ihre Produkte und andere nicht nutzerbezogene Daten zu verstehen, wenn dies relevant ist. Agenten verwenden Tools, um nur die relevanten Artikel zu finden, und senden diese an das LLM, um den Token-Verbrauch zu minimieren. Für einen besseren Katalogarbruf erstellen Sie eine [Wissensquelle]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) und fügen Sie diese als Agentenkontext hinzu, anstatt den Katalog direkt anzuhängen.

![Der Katalog „restaurants“ und die Spalte „Loyalty_Program“ sind für die Suche durch den Agenten ausgewählt.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Wenn Sie einen Catalog Agent in einem Katalogfeld bereitstellen, aktivieren Sie die Pflichtfeld-Kontrolle und wählen Sie aus, welche der ausgewählten Spalten ausgefüllt sein müssen, bevor der Agent ausgeführt wird. Der Agent überspringt eine Zeile nur, wenn eine dieser Pflichtspalten leer ist oder fehlt – zum Beispiel ein `gender`-Feld, das noch nicht ausgefüllt wurde. Ausgewählte Spalten sind standardmäßig als Pflichtfelder markiert, aber Sie können Spalten entfernen, die leer sein dürfen, ohne die Ausführung zu blockieren. Dies verhindert unnötigen Token-Verbrauch bei unvollständigen Daten.

Catalog Agents respektieren auch die Spaltenreihenfolge, wenn Eingabefelder voneinander abhängen. Wenn Spalte D aus den Spalten B und C generiert werden soll, führt der Agent die Verarbeitung von Spalte D erst aus, wenn B und C Werte für diese Zeile enthalten.

Für Bereitstellungsszenarien und Beispiele siehe [Catalog Agents verwenden]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) und [Best Practices für Catalog Agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Segment-Mitgliedschaftskontext {#segment-membership-context}

Sie können bis zu fünf Segmente auswählen, anhand derer der Agent die Segment-Mitgliedschaft jedes/jeder Nutzers/Nutzerin abgleichen kann, wenn der Agent in einem Canvas verwendet wird. Angenommen, Ihr Agent hat die Segment-Mitgliedschaft für ein Segment „Loyalty Users“ ausgewählt und wird in einem Canvas verwendet. Wenn Nutzer:innen einen Agent-Schritt betreten, kann der Agent prüfen, ob jede:r Nutzer:in Mitglied in jedem Segment ist, das Sie in der Agent-Konsole angegeben haben, und die Mitgliedschaft (oder Nicht-Mitgliedschaft) jedes/jeder Nutzers/Nutzerin als Kontext für das LLM verwenden.

![Das Segment „Loyalty Users“ für den Zugriff auf die Agent-Mitgliedschaft ausgewählt.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Markenrichtlinien {#brand-guidelines}

Sie können [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) auswählen, an die sich Ihr Agent in seinen Antworten halten soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte generiert, um Nutzer:innen zu ermutigen, sich für eine Fitnessstudio-Mitgliedschaft anzumelden, können Sie dieses Feld verwenden, um auf Ihre vordefinierte, ausdrucksstarke und motivierende Richtlinie zu verweisen.

## Nutzerspezifischer Interaktionsverlauf {#user-history}

Die Interaktionsdaten von Nutzer:innen umfassen ihre letzten Campaign- und Canvas-Öffnungen, Klicks und Conversion-Daten. Sie können diesen Kontext beispielsweise einbeziehen, damit ein Agent ihn bei der Auswertung in einem Canvas referenzieren kann. Der nutzerspezifische Interaktionsverlauf kann auch dazu beitragen, einen Agenten zu beeinflussen, dessen Aufgabe es ist, personalisierte Nachrichtentexte zu verfassen.

## Versionsverlauf {#version-history}

Die Agentenkonsole zeichnet jedes Mal eine neue Version auf, wenn Sie Änderungen am Agenten speichern. Der Tab **Versionsverlauf** listet jede gespeicherte Version und die Änderungen zwischen den Speichervorgängen auf.

1. Öffnen Sie den Agenten in der Agentenkonsole.
2. Wählen Sie den Tab **Versionsverlauf**.
3. Wählen Sie eine Version aus, um deren Konfiguration zu überprüfen.

Um zu sehen, was sich in einer Version geändert hat, wählen Sie **Anzeigen**. Braze zeigt einen Inline-Diff im Code-Stil an, der Ergänzungen und Löschungen hervorhebt. Gelöschte Inhalte werden mit roter Durchstreichung dargestellt.

![Versionsverlauf der Agentenkonsole mit geöffnetem Panel „Unterschiede zur vorherigen Version“, das Inline-Ergänzungen in Grün und Löschungen in Rot für Agentenanweisungen zeigt.]({% image_buster /assets/img/ai_agent/instruction_differences.png %}){: style="max-width:75%;"}

Wenn Sie Anweisungen aus einer früheren Version wiederherstellen möchten, öffnen Sie **Anzeigen** für diese Version, kopieren Sie den Anweisungstext und fügen Sie ihn in Ihr aktuelles Feld **Anweisungen** ein.

{% alert tip %}
In der Inline-Diff-Ansicht drücken Sie <kbd>⌘</kbd> + <kbd>A</kbd> (macOS) oder <kbd>Ctrl</kbd> + <kbd>A</kbd> (Windows), um alle Anweisungen ohne die rote Löschungsmarkierung auszuwählen, sodass Sie den sauberen Text kopieren und wiederherstellen können.
{% endalert %}

## Agenten duplizieren {#duplicate-agents}

Duplizieren Sie einen Agenten, um Verbesserungen oder Iterationen Seite an Seite mit dem Original zu testen. Verwenden Sie den [Versionsverlauf](#version-history), um frühere Konfigurationen zu überprüfen oder wiederherzustellen. So duplizieren Sie einen Agenten:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> aus.
2. Wählen Sie **Duplizieren**.

## Agenten archivieren {#archive-agents}

Wenn Sie mehr angepasste Agenten erstellen, können Sie die Seite **Agent Management** organisieren, indem Sie Agenten archivieren, die nicht aktiv genutzt werden. So archivieren Sie einen Agenten:

1. Fahren Sie mit dem Mauszeiger über die Zeile des Agenten und wählen Sie das Menü <i class="fas fa-ellipsis-vertical" aria-label="Mehr Optionen"></i> aus.
2. Wählen Sie **Archivieren** aus.