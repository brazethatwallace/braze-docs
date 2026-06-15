---
nav_title: KI-Schritt
article_title: KI-Schritt
permalink: /ai_step/
description: "Dieser Referenzartikel behandelt den Canvas-KI-Schritt."
tool:
  - Canvas
hidden: true
---

# KI-Schritt {#ai-step}

> Der KI-Schritt innerhalb von Canvas nutzt ChatGPT, um personalisiertes Marketing zu automatisieren, indem er nutzergenerierte Eingaben (wie Umfrage-Feedback) interpretiert, die passende Antwort bestimmt und Nachrichten triggert – alles innerhalb von Braze. ChatGPT wird von OpenAI betrieben, einem Drittanbieter.

{% alert note %}
Der KI-Schritt ist derzeit als Beta-Feature verfügbar. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie an der Teilnahme an diesem Beta-Test interessiert sind.
{% endalert %}

## Einen KI-Schritt erstellen {#create-ai-step}

1. Fügen Sie einen neuen Schritt zu Ihrem Canvas hinzu und wählen Sie den **KI-Schritt** aus. <br><br>![KI-Schritt im Canvas-Builder][1]{: style="max-width: 30%;"}<br><br>
2. Erstellen Sie einen Prompt, der der KI mitteilt, wie sie auf verschiedene Nutzeraktionen reagieren soll. Antworten können das Aktualisieren eines angepassten Attributs oder das Senden einer Nachricht umfassen. Dieser Prompt kann Liquid verwenden, um verschiedene Antwortausgaben basierend auf unterschiedlichen Nutzerattributen oder Eingaben zuzuweisen. <br><br>Um Ausgaben zuzuweisen, die dann zur Personalisierung zukünftiger Nachrichten innerhalb desselben Canvas verwendet werden können, erstellen Sie einen Prompt, der Variablen mit bestimmten Namen speichert (zum Beispiel „message“ und „sentiment score“). <br><br> ![Beispiel-KI-Prompt, der in den KI-Schritt-Einstellungen verwendet wird, um eine personalisierte Nachricht basierend auf einem generierten Sentiment-Score zu senden. Dieses Beispiel wird im Abschnitt „Kundenstimmungs-Antworten“ beschrieben.][2] <br><br>
3. Verwenden Sie den Tab **Vorschau**, um zu testen, was die KI für bestimmte Nutzer:innen ausgeben könnte.<br><br> ![Der Tab „Vorschau“ der KI-Schritt-Einstellungen, der eine KI-generierte personalisierte Nachricht für drei Parameter zeigt: einen Vornamen „Cameron“, einen Produktnamen „shoes“ und den Text „decent but my shoe lace already broke“][3]

## KI-Ausgabe mit Liquid referenzieren {#referencing-ai-output-using-liquid}

Referenzieren Sie die KI-Ausgabe in späteren Schritten, indem Sie die Liquid-Logik `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}` einfügen. Sie können den `key_name` innerhalb des Prompts im KI-Schritt festlegen.

Wenn Sie beispielsweise die Variablen „message“ und „sentiment score“ verwenden, können Sie `{% raw %}{{ai_step_output.${message}}}{% endraw %}` nutzen, um eine nachfolgende Nachricht in demselben Canvas zu personalisieren.

Sie können die Ausgabe jedes KI-Schritts auch als angepasstes Attribut protokollieren, indem Sie den Canvas-Schritt „Nutzeraktualisierung“ verwenden, in dem Sie die KI-Schritt-Ausgabe auslesen (zum Beispiel `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). Wenn die Ausgabe nicht als angepasstes Attribut gespeichert wird, kann sie an keiner anderen Stelle außer in nachfolgenden Schritten desselben Canvas verwendet werden.

### Kontext-Schritte verwenden {#using-context-steps}

Sie können [Canvas-Kontext-Schritte](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) nutzen, um Ausgaben später in Ihrem Canvas einfach zu referenzieren.

Das Folgende ist ein Beispiel für einen Kontext-Schritt, den Sie nach Ihrem KI-Schritt einrichten könnten. In diesem Beispiel enthält ein vorheriger KI-Schritt die KI-Schritt-Ausgaben für Sentiment-Score und Nachricht, und dieser Kontext-Schritt erstellt die Variablen `sentiment_score` und `message`, die in nachfolgenden Schritten verwendet werden können.

![Kontext-Schritt mit den zwei Variablen: „sentiment_score“ und „message“.][6]

Sie könnten auch einen Zielgruppenpfade-Schritt erstellen, der Nutzer:innen basierend auf dem Wert ihrer Kontextvariablen auf verschiedene Pfade leitet. In diesem Beispiel könnten Sie Nutzer:innen je nach ihrem Sentiment-Score unterschiedlich ansprechen. Sie können auch Liquid verwenden, um die Nachrichtenvariable in den Text einer E-Mail einzufügen, indem Sie die Variable mit {% raw %}`{{context.${message}}}`{% endraw %} einfügen.

![Ein Zielgruppenpfade-Schritt mit einer Zielgruppe namens „Group 1“ mit dem Filter „sentiment_score ist mehr als 80“.][7]

## KI-Schritt-Metriken {#ai-step-metrics}

KI-Schritte haben die folgenden Metriken auf Schrittebene:

| Metrik | Beschreibung |
| _Zum nächsten Schritt weitergegangen_ | Anzahl der Nutzer:innen, die zu den folgenden Schritten im Canvas weitergegangen sind |
| _Canvas verlassen_ | Anzahl der Nutzer:innen, die das Canvas verlassen haben, wenn Ihr KI-Schritt der letzte Schritt war |
| _Ausgabe erfolgreich_ | Anzahl der Nutzer:innen, für die der KI-Schritt erfolgreich eine Ausgabe generiert hat |
| _Ausgabe fehlgeschlagen_ | Anzahl der Nutzer:innen, für die der KI-Schritt keine Ausgabe generieren konnte – in diesem Fall gehen die Nutzer:innen trotzdem zu nachfolgenden Schritten weiter |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### KI-Schritt-Ausgaben verstehen {#understanding-your-ai-step-outputs}

Es gibt einige Szenarien, in denen Braze die Ausgabe des KI-Schritts verwirft und die Kund:innen zum nächsten Schritt weiterleitet:

- Wenn die Ausgabe 1.024 Zeichen überschreitet
- Wenn die Ausgabe nicht im JSON-Format vorliegt
- Wenn der Prompt die [Moderations](https://platform.openai.com/docs/guides/moderation/overview)-Anforderungen von OpenAI nicht erfüllt, die unangemessene nutzergenerierte Inhalte kennzeichnen

## Anwendungsfälle für den KI-Schritt {#ai-step-use-cases}

### Kundenstimmungs-Antworten {#customer-sentiment-responses}

Wie im Beispiel unter [Einen KI-Schritt erstellen](#create-ai-step) gezeigt, können Sie die KI bitten, Follow-up-Nachrichten basierend auf Sentiment-Scores zu senden, die aus Kundenfeedback generiert wurden.

- **Positive Sentiment-Scores:** Triggern Sie eine Push-Benachrichtigung, die Nutzer:innen bittet, eine Bewertung abzugeben
- **Mittlere Sentiment-Scores:** Triggern Sie eine E-Mail, die Nutzer:innen fragt, ob sie zusätzliche Hilfe wünschen
- **Niedrige Sentiment-Scores:** Triggern Sie einen Webhook, der den Nutzer-Helpdesk benachrichtigt, damit eine Support-Vertretung eine differenzierte Nachfassnachricht verfassen kann

#### Beispiel-KI-Prompt {#example-ai-prompt}

Dieses Beispiel wurde unter [Einen KI-Schritt erstellen](#create-ai-step) verwendet.

Ein:e Kund:in hat „`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`“ gekauft und folgendes Produktfeedback gegeben: „`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`“. Erstelle einen Sentiment-Score als Ganzzahl zwischen 0 und 100. Erstelle dann eine personalisierte Nachricht. Dies sollte zwei Variablen zurückgeben: „message“ und „sentiment score.“

### Umfrage-Follow-ups {#survey-follow-ups}

Wenn Sie eine In-App- oder In-Browser-Umfrage mit einem Freitext-Abschnitt durchführen, können Sie KI-Schritte verwenden, um freie Antworten zu analysieren und entsprechend nachzufassen.

Wenn beispielsweise ein Kosmetikhändler eine Umfrage mit der Frage „Welche Produkte möchten Sie für die diesjährigen Beauty Awards nominieren?“ durchführt, könnte er einen Prompt verwenden, der die bevorzugten Produkttypen und Marken der Nutzer:innen identifiziert und als Attribut zuweist, um dann zukünftige Inhalte basierend auf diesen Daten zu personalisieren.

#### Beispiel-KI-Prompt

Identifiziere die Lieblingsmarke der Nutzer:innen anhand ihrer Antwort. Erstelle dann eine Nachricht, die den Nutzer:innen für das Ausfüllen der Umfrage dankt und erwähnt, wie Beauty-Expert:innen ihre Lieblingsmarke ebenfalls lieben. Dies sollte zwei Variablen zurückgeben: „message“ und „favorite brand.“

![Tab „Vorschau“ der KI-Schritt-Einstellungen, der eine KI-generierte personalisierte Nachricht für den Umfrageantwort-Parameter „I love Beauty Brand face creams“ zeigt, die den Nutzer:innen für das Ausfüllen der Umfrage dankt und dann eine Gesichtscreme empfiehlt.][4]

### Verhaltensbasierte Empfehlungen {#behavior-driven-recommendations}

Kund:innen können die KI bitten, Nutzerverhalten zu analysieren und Empfehlungsnachrichten zu senden.

Sie können beispielsweise einen Prompt erstellen, der die 50 letzten Käufe der Nutzer:innen analysiert und deren am häufigsten gekaufte Kategorie als neues angepasstes Attribut festlegt. Anschließend können Sie personalisierte E-Mail-Empfehlungen für die Lieblingskategorie jeder Nutzerin und jedes Nutzers senden.

#### Beispiel-KI-Prompt

Ein:e Kund:in hat die folgenden Produkte gekauft: „`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`“. Identifiziere die am häufigsten gekaufte Produktkategorie der Nutzer:innen. Dies sollte eine neue Variable für „most purchased category“ zurückgeben.

![Tab „Vorschau“ der KI-Schritt-Einstellungen, der die KI-generierte Variable „book“ für den Parameter der am häufigsten gekauften Kategorie zeigt.][5]

## Rate-Limits

Es gibt ein Limit von 10 Anfragen pro Minute (RPM) pro Unternehmen. Das bedeutet, dass für jeden KI-Schritt bis zu 10 Nutzer:innen diesen Schritt innerhalb einer bestimmten Minute erhalten können und alle Nutzer:innen über die 10 hinaus automatisch zum nächsten Schritt weitergeleitet werden. Wenn die nächste Minute beginnt, können Nutzer:innen den KI-Schritt erneut erhalten, aber vorherige Nutzer:innen, die das Rate-Limit ausgelöst haben, werden nicht erneut verarbeitet.

## Einschränkungen des KI-Schritts {#ai-step-limitations}

- Dieses Feature nutzt GPT-3.5.
- Dieses Feature verwendet den Braze-OpenAI-API-Schlüssel. Sie können nicht Ihren eigenen OpenAI-API-Schlüssel verwenden.
- Es gibt ein Limit von 5 Anfragen pro Minute (RPM) pro Workspace und 10 RPM pro Unternehmen.
- Dieses Feature ist nicht HIPAA-konform, und Kund:innen sollten keine personenbezogenen Daten (PII) oder geschützten Gesundheitsinformationen (PHI) senden.

## Wie werden meine Daten verwendet und an OpenAI gesendet? {#how-is-my-data-used-and-sent-to-openai}

Um KI-Ausgaben über Braze-KI-Features zu generieren, die Braze als OpenAI-gestützt identifiziert („Ausgabe“), sendet Braze Ihren Prompt, wie z. B. Nachrichteninhalte, Endnutzerstimmung, Markenrichtlinien, vergangene Campaign-Daten oder andere Eingaben, soweit zutreffend („Eingabe“), an [OpenAI](https://openai.com/). Wenn personenbezogene Daten an OpenAI gesendet werden, wenn Sie die ChatGPT-Integration von Braze mit dem KI-Schritt verwenden, handelt OpenAI als Unterauftragsverarbeiter von Braze, wie im DPA zwischen Ihnen und Braze festgelegt. Wenn Sie Ihr eigenes Large Language Model (LLM) mit dem KI-Schritt integrieren, wird jeder Anbieter eines solchen LLM als Drittanbieter betrachtet, und die Verarbeitung personenbezogener Daten unterliegt den Bedingungen zwischen Ihnen und diesem Drittanbieter. Gemäß den [API-Plattform-Verpflichtungen von OpenAI](https://openai.com/enterprise-privacy/) werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet und werden nach 30 Tagen von OpenAI aus deren Systemen gelöscht. Zwischen Ihnen und Braze ist die Ausgabe Ihr geistiges Eigentum. Braze wird keine Urheberrechtsansprüche an solchen Ausgaben geltend machen. Braze gibt keinerlei Garantie in Bezug auf KI-generierte Inhalte im Allgemeinen, einschließlich der Ausgabe.

[1]: {% image_buster /assets/unlisted_docs/img/ai_step1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/ai_step2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/ai_step3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/ai_step4.png %}
[5]: {% image_buster /assets/unlisted_docs/img/ai_step5.png %}
[6]: {% image_buster /assets/unlisted_docs/img/ai_step6.png %}
[7]: {% image_buster /assets/unlisted_docs/img/ai_step7.png %}