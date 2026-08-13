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
Das von Braze bereitgestellte **Auto**-Modell ist für Modelle optimiert, deren Denkfähigkeiten ausreichen, um Aufgaben wie Katalogsuche und Segment-Zugehörigkeit durchzuführen. Bei der Verwendung anderer Modelle empfehlen wir, durch Tests zu bestätigen, dass Ihr Modell für Ihren Anwendungsfall gut funktioniert. Möglicherweise müssen Sie Ihre [Anweisungen](#writing-instructions) anpassen, um Modellen mit unterschiedlichen Geschwindigkeiten und Fähigkeiten verschiedene Detailstufen oder schrittweises Denken zu ermöglichen.
{% endalert %}

### Option 1: Ein von Braze bereitgestelltes Modell verwenden {#option-1-use-a-braze-powered-model}

Dies ist die einfachste Option, ohne zusätzliche Einrichtung. Braze bietet direkten Zugang zu Large Language Models (LLMs). Um diese Option zu nutzen, wählen Sie **Auto**, das Gemini-Modelle verwendet.

{% alert important %}
Wenn Sie **Braze Auto** nicht als Option im **Modell**-Dropdown beim Erstellen eines Agenten sehen, wenden Sie sich an Ihren Customer-Success-Manager, um zu erfahren, wie Sie für die Nutzung des Braze-Auto-Modells berechtigt werden können.
{% endalert %}

### Option 2: Eigenen API-Schlüssel mitbringen {#option-2-bring-your-own-api-key}

Mit dieser Option können Sie Ihr Braze-Konto mit Anbietern wie OpenAI, Anthropic oder Google Gemini verbinden. Wenn Sie Ihren eigenen API-Schlüssel von einem LLM-Anbieter mitbringen, werden Token-Kosten direkt über Ihren Anbieter abgerechnet, nicht über Braze.

Wir empfehlen, regelmäßig die neuesten Modelle zu testen, da ältere Modelle nach einigen Monaten eingestellt oder als veraltet markiert werden können. Stellen Sie sicher, dass Sie über ausreichend Guthaben bei Ihrem Anbieter verfügen, um Ihre Agenten im großen Maßstab auszuführen. Sie können sich auch für Agent-Console-Benachrichtigungen in den [Benachrichtigungseinstellungen]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences) anmelden, um benachrichtigt zu werden, wenn Braze erkennt, dass ein Modell nicht mehr verfügbar ist oder Abrechnungsprobleme mit Ihrem LLM-Anbieter auftreten.

So richten Sie dies ein:

1. Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie Ihren Anbieter.
2. Geben Sie Ihren API-Schlüssel vom Anbieter ein.
3. Wählen Sie **Speichern**.

Anschließend können Sie zu Ihrem Agenten zurückkehren und Ihr Modell auswählen.

Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Braze-Unterauftragsverarbeiter, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie Ihren eigenen API-Schlüssel mitbringen, gilt der Anbieter Ihres LLM-Abonnements als Drittanbieter gemäß dem Vertrag zwischen Ihnen und Braze.

#### Denkstufen {#thinking-levels}

Einige LLM-Anbieter ermöglichen es Ihnen, die Denkstufe eines ausgewählten Modells anzupassen. Denkstufen definieren den Umfang des Denkprozesses, den das Modell vor der Antwort durchläuft – von schnellen, direkten Antworten bis hin zu längeren Argumentationsketten. Dies beeinflusst die Antwortqualität, Latenz und Token-Nutzung.

| Stufe | Wann verwenden |
|-------|----------------|
| **Minimal** | Einfache, klar definierte Aufgaben (wie Katalogsuche, einfache Klassifizierung). Schnellste Antworten und niedrigste Kosten. |
| **Niedrig** | Aufgaben, die von etwas mehr Überlegung profitieren, aber keine tiefgehende Analyse erfordern. |
| **Mittel** | Mehrstufige oder nuancierte Aufgaben (wie die Analyse mehrerer Eingaben, um eine Aktion zu empfehlen). |
| **Hoch** | Komplexe Argumentation, Grenzfälle oder wenn das Modell Schritte durcharbeiten soll, bevor es antwortet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Denkstufen" }

Wir empfehlen, mit **Minimal** zu beginnen und die Antworten Ihres Agenten zu testen. Anschließend können Sie die Denkstufe auf **Niedrig** oder **Mittel** anpassen, wenn der Agent Schwierigkeiten hat, genaue Antworten zu liefern. In seltenen Fällen kann eine **hohe** Denkstufe erforderlich sein, obwohl diese Stufe zu hohen Token-Kosten und längeren Antwortzeiten oder einem höheren Risiko von [Timeout-Fehlern]({{site.baseurl}}/user_guide/brazeai/agents/faq#what-might-cause-a-custom-agent-to-frequently-time-out) führen kann. Wenn Ihr Agent Schwierigkeiten hat, mehrstufige Argumentation mit angemessenen Antwortzeiten in Einklang zu bringen, erwägen Sie, Ihren Anwendungsfall in mehr als einen Agenten aufzuteilen, die in einem Canvas oder Katalog zusammenarbeiten können.

Braze verwendet für ausgehende LLM-Aufrufe dieselben IP-Bereiche wie für Connected-Content. Die Bereiche sind in der [Connected-Content-IP-Zulassungsliste]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting) aufgeführt. Wenn Ihr Anbieter IP-Zulassungslisten unterstützt, können Sie den Schlüssel auf diese Bereiche beschränken, sodass nur Braze ihn verwenden kann.

{% alert important %}
Wenn Sie ein von Braze bereitgestelltes LLM verwenden, agieren die Anbieter eines solchen Modells als Braze-Unterauftragsverarbeiter, vorbehaltlich der Bedingungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. Wenn Sie Ihren eigenen API-Schlüssel mitbringen, gilt der Anbieter Ihres LLM-Abonnements als Drittanbieter gemäß dem Vertrag zwischen Ihnen und Braze.
{% endalert %}

#### Bestimmen, welches Modell verwendet werden soll {#determine-which-model-to-use}

Jeder LLM-Anbieter hat eine leicht unterschiedliche Mischung aus Modellfähigkeiten, Kosten und Denkstufen. Hier sind einige allgemeine Richtlinien und Best Practices:

- Für Kosteneffizienz priorisieren Sie das Testen von Modellen mit niedrigeren Token-Kosten gegenüber teureren Modellen. Wechseln Sie nur dann zu teureren Modellen, wenn günstigere Modelle mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente oder ungenaue Ergebnisse liefern.
- Für Geschwindigkeit und Performance-Effizienz priorisieren Sie das Testen niedrigerer Denkstufen gegenüber höheren Denkstufen. Wechseln Sie nur dann zu höheren Denkstufen, wenn niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente oder ungenaue Ergebnisse liefern.
- Wenn günstigere Modelle oder niedrigere Denkstufen mit dem Anwendungsfall Schwierigkeiten haben oder inkonsistente oder ungenaue Ergebnisse liefern, erwägen Sie den Wechsel zu teureren Modellen oder höheren Denkstufen.
- Achten Sie beim Testen darauf, Zuverlässigkeit und Genauigkeit mit Token-Nutzung und Aufruf-Dauer in Einklang zu bringen.
- Jeder Anwendungsfall kann ein anderes optimales Modell und eine andere optimale Denkstufe haben. Wir empfehlen gründliches Testen, um konsistente Qualität ohne Timeouts sicherzustellen.

### Steuerung des Aufruf-Flusses {#invocation-flow-controls}

Die folgenden Steuerungen des Aufruf-Flusses gelten pro Workspace:

- **Von Braze bereitgestelltes Modell:** 5.000 Aufrufe pro Minute
- **Eigener API-Schlüssel:** 5.000 Aufrufe pro Minute

Wenn viele Nutzer:innen gleichzeitig einen Agenten-Schritt betreten, reiht Braze Aufrufe gemäß diesen Limits in eine Warteschlange ein, sodass die Verarbeitung bei Sendungen mit hohem Volumen länger dauern kann.

### Tägliche Aufruf- und Credit-Limits {#daily-invocation-and-credit-limits}

Jeder Agent hat ein tägliches Aufruf-Limit (Standard 250.000; Maximum 1.000.000, sofern Ihr Vertrag nichts Höheres erlaubt). Jeder Aufruf (einschließlich Agent-Console-Vorschauen und Test-Canvas-Durchläufe, die **Antwort simulieren** verwenden) wird auf dieses Limit angerechnet.

In der Agent Console schätzt das **Tägliche Aktions-Credit-Kostenlimit** die maximalen Credits, die ein Agent pro Tag verbrauchen kann. Braze multipliziert das Pro-Aufruf-Credit-Verhältnis Ihres Workspace für das ausgewählte Modell mit dem täglichen Aufruf-Limit.

### Wann Credits verbraucht werden {#when-credits-are-consumed}

Braze berechnet Credits nur für Aufrufe, die die Verarbeitung abschließen. Credits werden nicht verbraucht, wenn ein Aufruf fehlschlägt aufgrund von:

- Einem [Rate-Limit-Fehler](#rate-limit-errors) des LLM-Anbieters (einschließlich Wiederholungsversuche, die letztendlich fehlschlagen)
- Nichtverfügbarkeit des ausgewählten Modells
- Erreichen des täglichen Aufruf-Limits durch den Agenten

Credits werden verbraucht, wenn ein Aufruf ein Timeout erreicht, auch wenn der Agent kein verwertbares Ergebnis zurückgibt.

### Credit-Nutzung überwachen {#monitor-credit-usage}

Gehen Sie zu **Einstellungen** > **Abrechnung** > **Credit-Nutzung** > **Agent Console**, um den Credit-Verbrauch, die Aufrufzahlen und die Credit-Verhältnisse pro Agent einzusehen.

Credit-Verhältnisse stammen aus Ihrem Vertrag und erscheinen im [Credit-Nutzung]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)-Dashboard (Tab **Credit-Verhältnisse** und Tab **Agent Console**). Die Schätzung wird aktualisiert, wenn Sie das Modell oder das Aufruf-Limit ändern.

Um Ausgaben zu steuern, senken Sie das tägliche Aufruf-Limit. Bei [Bring-your-own (BYO)](#option-2-bring-your-own-api-key)-Modellen können Sie auch ein günstigeres Modell wählen oder die [Denkstufe](#thinking-levels) reduzieren, um die Token-Kosten beim Anbieter zu senken. Braze Auto unterstützt keine Anpassung der Denkstufe.

### Rate-Limit-Fehler {#rate-limit-errors}

Wenn der LLM-Anbieter während eines Canvas-Schritt-Agenten- oder Katalog-Agenten-Aufrufs einen Rate-Limit-Fehler zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff, bis der Aufruf erfolgreich ist oder Braze feststellt, dass er nicht abgeschlossen werden kann.

Wenn die Wiederholungsversuche für Canvas oder Katalog erschöpft sind, zeigt das **Logs**-Detailpanel **Error** und die Anbieternachricht (wie `Rate limit exceeded`) unter **Output** an. Wiederholungsversuche sind in den Logs sichtbar, einschließlich des allerersten Aufrufs unabhängig von seinem letztendlichen Erfolg oder Misserfolg. Wenn es für eine:n bestimmte:n Nutzer:in vier Wiederholungsversuche braucht, um schließlich einen Erfolg zu erzielen, können Sie die Nutzer-ID suchen und alle fünf (Original plus vier Wiederholungsversuche) in den **Logs** sehen, wobei das Original und die ersten drei Wiederholungsversuche **Error** mit `Rate limit exceeded` anzeigen.

Rate-Limit-Fehler verbrauchen keine Braze-Credits, einschließlich fehlgeschlagener Wiederholungsversuche, die in den **Logs** angezeigt werden.

![Agent-Console-Log-Details, die einen Rate-Limit-Exceeded-Fehler im Output-Feld zeigen.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## Anweisungen schreiben {#writing-instructions}

Anweisungen sind die Regeln oder Richtlinien, die Sie dem Agenten geben (System-Prompt). Sie definieren, wie sich der Agent bei jeder Ausführung verhalten soll. Systemanweisungen können bis zu 25 KB umfassen.

Wenn Sie Ihren Agenten mit [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) unter Verwendung eines [Starttemplate]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) erstellt haben, überprüfen Sie die vorausgefüllten Anweisungen und bearbeiten Sie diese nach Bedarf.

Hier sind einige allgemeine Best Practices für den Einstieg in das Prompting:

1. Beginnen Sie mit dem Ziel vor Augen. Formulieren Sie zuerst das Ziel.
2. Geben Sie dem Modell eine Rolle oder Persona („Du bist ein …“).
3. Setzen Sie klaren Kontext und Einschränkungen (Zielgruppe, Länge, Tonalität, Format).
4. Fordern Sie Struktur an („Gib JSON/Aufzählung/Tabelle zurück …“).
5. Zeigen statt erzählen. Fügen Sie einige hochwertige Beispiele hinzu.
6. Unterteilen Sie komplexe Aufgaben in geordnete Schritte („Schritt 1 … Schritt 2 …“).
7. Fördern Sie das Nachdenken („Denke die Schritte intern durch und gib dann eine prägnante Endantwort“ oder „erkläre kurz deine Entscheidung“).
8. Testen, prüfen und iterieren. Kleine Anpassungen können zu großen Qualitätsverbesserungen führen.
9. Behandeln Sie Randfälle, fügen Sie Leitplanken hinzu und ergänzen Sie Ablehnungsanweisungen.
10. Messen und dokumentieren Sie, was intern funktioniert, zur Wiederverwendung und Skalierung.

### Beispiele {#examples}

Für Startkonfigurationen in der Agent Console siehe [Agenten-Templates, erstellt mit Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

Für vollständige Anweisungsbeispiele, die Sie kopieren oder anpassen können, siehe die [Anwendungsfall-Bibliothek für Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/examples).

| Beispiel | Kategorie | Agententyp | Beschreibung |
| --- | --- | --- | --- |
| [Personalisierte Nachrichten basierend auf dem Kontext der Nutzer:innen schreiben]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | Inhaltserstellung | Canvas-Schritt-Agent | Generiert koordinierte E-Mail-Betreffzeile/Preheader und Push-Titel/Text für Nutzer:innen, die gesucht, aber nicht gebucht haben. |
| [Nutzerfeedback analysieren, um nächste Schritte zu bestimmen]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | Datenstandardisierung | Canvas-Schritt-Agent | Klassifiziert Stimmung und Thema einer Umfrage nach der Reise und empfiehlt dann einen CRM-Folgeschritt. |
| [Nutzer:innen anhand vorhandener Attribute in Interessens-Buckets kategorisieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | Affinitäts-Agent | Canvas-Schritt-Agent | Klassifiziert Nutzer:innen anhand von Attributen und Signalen mit hoher Absicht in Interessens-Buckets und empfiehlt dann das beste nächste Erlebnis oder den besten Artikel. |
| [Nutzer:innen basierend auf aktuellem Verhalten zum relevantesten Canvas-Pfad weiterleiten]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | Affinitäts-Agent | Canvas-Schritt-Agent | Leitet die Motivation aus dem aktuellen Verhalten ab und gibt den besten Routenschlüssel für den nächsten Canvas-Schritt der Nutzer:innen zurück. |
| [Nutzer:innen anhand von Realtime-Aktionen mit hoher Absicht Interessenskategorien zuweisen]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | Affinitäts-Agent | Canvas-Schritt-Agent | Weist Interessenskategorien basierend auf Aktionen mit hoher Absicht zu und empfiehlt das beste nächste Erlebnis oder den besten Artikel. |
| [Eingehende Nachrichten auf Opt-out-Absicht klassifizieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | Klassifizierung und Routing | Canvas-Schritt-Agent | Gibt einen strikten booleschen Wert zurück, der angibt, ob eine Nachricht eine Opt-out-Anfrage ist. |
| [Eingehende Nachrichten in strukturierte Daten für die Automatisierung standardisieren]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | Datenstandardisierung | Canvas-Schritt-Agent | Normalisiert eingehende SMS oder Chat-Nachrichten in strukturierte Absichten, Entitäten und Compliance-Flags für nachgelagerte Automatisierung. |
| [Konversionsstarke Beschreibungen schreiben, die den Markenrichtlinien entsprechen]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | Inhaltserstellung | Catalog Agent | Generiert kurze, markenkonforme Beschreibungen für jede Catalog-Zeile. |
| [Übersetzungen basierend auf der regionalen Sprache bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | Catalog-Anreicherung | Catalog Agent | Lokalisiert UI- und Marketing-Strings pro Gebietsschema und Zeichenlimit. |
| [Catalog-Artikel mit Beschreibungen, Kategorien und Tags anreichern]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | Catalog-Anreicherung | Catalog Agent | Generiert erweiterte Beschreibungen, Kategorien und Tags aus vorhandenen Catalog-Artikeldaten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Zusammenfassung der Beispiele" }

### Liquid verwenden {#using-liquid}

Die Einbindung von [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) in die Anweisungen Ihres Agenten kann eine zusätzliche Ebene der Personalisierung in seiner Antwort hinzufügen. Sie können die genaue Liquid-Variable angeben, die der Agent erhält, und sie in den Kontext Ihres Prompts einbinden. Anstatt beispielsweise explizit „Vorname“ zu schreiben, können Sie das Liquid-Snippet {% raw %}`{{${first_name}}}`{% endraw %} verwenden:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

Im Bereich **Logs** der **Agent Console** können Sie die Details zu Eingabe und Ausgabe des Agenten überprüfen, um zu verstehen, welcher Wert aus dem Liquid gerendert wird.

### Welche Daten Agenten erhalten {#what-data-agents-receive}

Der Agentenkontext ist kein offenes Konversationsgedächtnis. Anders als ein Chat-Assistent sieht ein Agent nur die Daten, die Sie ihm zum Aufrufzeitpunkt explizit übergeben – er durchsucht keine Nutzerprofile, leitet fehlende Felder ab und teilt Ihnen auch nicht mit, wenn erforderliche Informationen fehlen.

Gestalten Sie jeden Agenten als eine bewusste Eingabe-zu-Ausgabe-Pipeline. Verbinden Sie jeden Datenpunkt, den der Agent benötigt, über eine oder mehrere der folgenden Methoden:

1. **Liquid in Anweisungen:** Verwenden Sie Nutzerattribute ({% raw %}`{{${first_name}}}`{% endraw %}) und [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) ({% raw %}`{{context.${variable_name}}}`{% endraw %}) direkt im Agenten-Prompt als Template.
2. **+ Agent context:** Wählen Sie Catalogs, Segmentzugehörigkeit, Markenrichtlinien, **All Canvas Context** oder Nutzerinteraktionsdaten in der Agent Console aus.
3. [Context-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): Setzen oder aktualisieren Sie `context.*`-Variablen im Canvas vor der Ausführung eines Agenten-Schritts.
4. **Zusätzlicher Kontext im Agenten-Schritt:** Übergeben Sie alle zusätzlichen Liquid-Template-Werte, die nicht bereits über die anderen Methoden angegeben wurden, zum Sendezeitpunkt über die Schrittkonfiguration an den Agenten.

Stellen Sie sicher, dass Sie diese Kontextvariablen entweder als Liquid-Template in den Agentenanweisungen verwenden oder **Add All Canvas Context** auswählen. Wenn ein Wert nicht über einen dieser Kanäle übergeben wird, erhält der Agent ihn nicht. Listen Sie erforderliche Eingaben in Ihren Anweisungen oder in den [Voraussetzungen für Anwendungsfälle]({{site.baseurl}}/user_guide/brazeai/agents/use_cases) auf und überprüfen Sie die Eingaben unter **Agent Console** > **Logs** nach dem Testen.

![Die Details für einen Agenten, der Liquid in seinen Anweisungen verwendet.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

Für Catalog Agents verwenden Sie **Fields** im Bereich **Output** anstelle eines JSON-Schemas; Sie können dennoch Anweisungen schreiben, die das Modell nach einer Schlüssel-Wert-Ausgabe fragen, die diesen Feldnamen entspricht.

Weitere Details zu Best Practices für das Prompting finden Sie in den Leitfäden der folgenden Modellanbieter:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Ausgaben {#outputs}

Wenn Sie Ihren Agenten mit [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) unter Verwendung eines [Startvorlagen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) erstellt haben, überprüfen Sie das vorausgefüllte Ausgabeschema und bearbeiten Sie es nach Bedarf.

### Einfache Schemas {#basic-schemas}

Einfache Schemas sind eine einfache Ausgabe, die ein Agent zurückgibt. Dies kann ein String, eine Zahl, ein Boolean, ein String-Array oder ein Zahlen-Array sein.

Wenn Sie beispielsweise Stimmungswerte von Nutzer:innen aus einer einfachen Feedback-Umfrage erfassen möchten, um festzustellen, wie zufrieden Ihre Kund:innen nach dem Erhalt eines Produkts sind, können Sie **Number** als einfaches Schema auswählen, um das Ausgabeformat zu strukturieren.

{% alert important %}
Arrays sind nur für Canvas-Schritt-Agenten verfügbar, nicht für Katalog-Agenten.
{% endalert %}

![Agent-Konsole mit „Number“ als ausgewähltem einfachen Schema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### Erweiterte Schemas {#advanced-schemas}

Erweiterte Schema-Optionen umfassen die manuelle Strukturierung von Feldern oder die Verwendung von JSON.

- **Fields:** Eine No-Code-Methode, um eine konsistente Agentenausgabe zu erzwingen.
- **JSON:** Ein Code-Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können. Nur für Canvas-Schritt-Agenten verfügbar, nicht für Katalog-Agenten.

Wir empfehlen die Verwendung erweiterter Schemas, wenn der Agent eine Datenstruktur mit mehreren Werten in strukturierter Form zurückgeben soll, anstatt einer einzelnen Ausgabe. Dadurch kann die Ausgabe besser als konsistente Kontextvariable formatiert werden.

### Fallback-Ausgabe {#fallback-output}

Fallback-Werte sind nur für Canvas-Schritt-Agenten verfügbar. Im Abschnitt **Output** der Agent-Konsole für einen Canvas-Schritt-Agenten können Sie Werte definieren, die Braze verwendet, wenn ein Aufruf fehlschlägt.

Bei **JSON**-Schemas liest Braze das Schema und generiert ein Eingabefeld für jede Eigenschaft, sodass Sie einen Fallback-Wert pro Schlüssel festlegen können. Bei **Fields**-Schemas geben Sie einen Fallback-Wert für jedes Feld ein. Bei einfachen Schemas geben Sie einen einzelnen Fallback-Wert ein. Canvas-Schritt-Agenten unterstützen Liquid in Fallback-Werten.

Informationen zu den Einrichtungsschritten finden Sie unter [Fallback-Werte konfigurieren]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values). Informationen zum Laufzeitverhalten in Canvas finden Sie unter [Fehlerbehandlung und Fallback-Verhalten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

Beispielsweise können Sie ein Ausgabeformat innerhalb eines Agenten verwenden, der eine Beispielreiseroute für Nutzer:innen basierend auf einem eingereichten Formular erstellen soll. Das Ausgabeformat ermöglicht es Ihnen festzulegen, dass jede Agentenantwort mit Werten für `tripStartDate`, `tripEndDate` und `destination` zurückkommen soll. Jeder dieser Werte kann aus Kontextvariablen extrahiert und in einem Nachrichtenschritt zur Personalisierung mit Liquid platziert werden.

{% tabs %}
{% tab Fields %}

Wenn Sie Antworten auf eine einfache Feedback-Umfrage formatieren möchten, um festzustellen, wie wahrscheinlich es ist, dass Befragte die neueste Eissorte Ihres Restaurants weiterempfehlen, können Sie die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erweiterte Schemas" }

![Agent-Konsole mit drei Ausgabefeldern für Wahrscheinlichkeitsbewertung, Erklärung und Konfidenzbewertung.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON-Schema %}

Wenn Sie Nutzerfeedback für das letzte Restauranterlebnis in Ihrer Restaurantkette erfassen möchten, können Sie **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Stimmungsvariable und eine Begründungsvariable enthält.

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

Wählen Sie bestimmte Kataloge aus, auf die ein Agent verweisen soll, und geben Sie Ihrem Agenten den Kontext, den er benötigt, um Ihre Produkte und andere nicht nutzerbezogene Daten zu verstehen, wenn dies relevant ist. Agenten verwenden Tools, um nur die relevanten Artikel zu finden und diese an das LLM zu senden, um den Token-Verbrauch zu minimieren. Für einen besseren Katalogazugriff erstellen Sie eine [Wissensquelle]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) und fügen Sie diese als Agentenkontext hinzu, anstatt den Katalog direkt anzuhängen.

![Der Katalog „restaurants“ und die Spalte „Loyalty_Program“ sind für die Agentensuche ausgewählt.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

Wenn Sie einen Catalog Agent in einem Katalogfeld bereitstellen, aktivieren Sie die Pflichtfeld-Steuerung und wählen Sie aus, welche ausgewählten Spalten ausgefüllt sein müssen, bevor der Agent ausgeführt wird. Der Agent überspringt eine Zeile nur dann, wenn eine dieser Pflichtspalten leer ist oder fehlt – zum Beispiel ein `gender`-Feld, das noch nicht ausgefüllt wurde. Ausgewählte Spalten sind standardmäßig als Pflichtfelder markiert, aber Sie können Spalten entfernen, die leer sein dürfen, ohne die Ausführung zu blockieren. Dies verhindert verschwendete Token bei unvollständigen Daten.

Catalog Agents berücksichtigen auch die Spaltenreihenfolge, wenn Eingabefelder voneinander abhängen. Wenn Spalte D aus den Spalten B und C generiert werden soll, führt der Agent Spalte D erst aus, wenn B und C Werte für diese Zeile enthalten.

Informationen zu Bereitstellungsszenarien und Beispielen finden Sie unter [Catalog Agents verwenden]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) und [Best Practices für Catalog Agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices).

## Segment-Mitgliedschaftskontext {#segment-membership-context}

Sie können bis zu fünf Segmente auswählen, gegen die der Agent die Segment-Mitgliedschaft jedes Nutzers bzw. jeder Nutzerin abgleichen kann, wenn der Agent in einem Canvas verwendet wird. Angenommen, Ihr Agent hat die Segment-Mitgliedschaft für ein Segment „Loyalty Users“ ausgewählt und wird in einem Canvas verwendet. Wenn Nutzer:innen einen Agent-Schritt betreten, kann der Agent für jede:n Nutzer:in prüfen, ob er oder sie Mitglied der in der Agent-Konsole angegebenen Segmente ist, und die Mitgliedschaft (oder Nicht-Mitgliedschaft) jedes Nutzers bzw. jeder Nutzerin als Kontext für das LLM verwenden.

![Das Segment „Loyalty Users“ ist für den Segment-Mitgliedschaftszugriff des Agents ausgewählt.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Markenrichtlinien {#brand-guidelines}

Sie können [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) auswählen, an die sich Ihr Agent in seinen Antworten halten soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte generiert, die Nutzer:innen dazu ermutigen, sich für eine Fitnessstudio-Mitgliedschaft anzumelden, können Sie dieses Feld verwenden, um auf Ihre vordefinierte, motivierende Markenrichtlinie zu verweisen.

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
2. Wählen Sie **Duplizieren** aus.

## Agenten archivieren {#archive-agents}

Wenn Sie mehr angepasste Agenten erstellen, können Sie die Seite **Agent Management** organisieren, indem Sie Agenten archivieren, die nicht aktiv verwendet werden. So archivieren Sie einen Agenten:

1. Bewegen Sie den Mauszeiger über die Zeile des Agenten und wählen Sie das Menü <i class="fas fa-ellipsis-vertical"></i> aus.
2. Wählen Sie **Archivieren** aus.