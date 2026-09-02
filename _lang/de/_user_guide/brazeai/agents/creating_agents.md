---
nav_title: Agenten erstellen
article_title: Angepasste Agenten erstellen
description: "Erfahren Sie, wie Sie Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können."
page_order: 1
alias: /creating-agents/
---

# Angepasste Agenten erstellen {#create-custom-agents}

> Erfahren Sie, wie Sie angepasste Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents).

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

- [Berechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions) für den Zugriff auf die **Agent Console** in Ihrem Workspace. Wenden Sie sich an Ihre Braze-Admins, wenn Sie diese Option nicht sehen.
- Berechtigung zum Erstellen und Bearbeiten angepasster KI-Agents.
- Eine Idee, was der Agent erreichen soll. Braze Agents können die folgenden Aktionen unterstützen:
   - **Personalisiertes Messaging:** Betreffzeilen, Überschriften, In-Product-Texte oder andere Inhalte generieren.
   - **Nutzer:innen-Routing:** Nutzer:innen in Canvas basierend auf Verhalten, Präferenzen oder angepassten Attributen weiterleiten.
   - **Datenmanagement:** Werte berechnen, Katalogeinträge anreichern oder Profilfelder aktualisieren.

## So funktioniert es {#how-it-works}

Wenn Sie einen Agenten erstellen, definieren Sie seinen Zweck und legen Leitplanken für sein Verhalten fest. Sobald er aktiv ist, kann der Agent in Braze eingesetzt werden, um personalisierte Texte zu generieren, Realtime-Entscheidungen zu treffen oder Katalogfelder zu aktualisieren. Während Sie Ihren Agenten erstellen, können Sie ihn als Entwurf speichern und jederzeit über das Dashboard pausieren oder aktualisieren. Jedes Speichern erstellt eine neue Version, die Sie im Tab [Versionsverlauf]({{site.baseurl}}/user_guide/brazeai/agents/reference#version-history) überprüfen können.

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten, angepasste Agenten zu nutzen.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Kundenfeedback bearbeiten | Leiten Sie Nutzerfeedback an einen Agenten weiter, um die Stimmung zu analysieren und empathische Folgenachrichten zu generieren. Bei besonders wertvollen Nutzer:innen kann der Agent die Antwort eskalieren oder Vergünstigungen einbinden. |
| Inhalte lokalisieren | Übersetzen Sie Katalogtexte in eine andere Sprache für globale Campaigns oder passen Sie Tonalität und Länge für regionsspezifische Kanäle an. Übersetzen Sie zum Beispiel „Classic Clubmaster Sunglasses“ ins Spanische als „Gafas de sol Classic Clubmaster“ oder kürzen Sie Beschreibungen für SMS-Campaigns. |
| Bewertungen oder Feedback zusammenfassen | Fassen Sie Stimmungen oder Feedback in einem neuen Feld zusammen, z. B. durch die Vergabe von Stimmungswerten wie „Positiv“, „Neutral“ oder „Negativ“, oder erstellen Sie eine kurze Textzusammenfassung wie „Die meisten Kund:innen loben die gute Passform, bemängeln aber den langsamen Versand.“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="So funktioniert es" }

## Einen Agenten erstellen {#create-an-agent}

### Schritt 1: Agententyp auswählen {#step-1-choose-an-agent-type}

Um einen Agenten zu erstellen, wählen Sie zunächst Ihren Agententyp:

1. Gehen Sie zur **Agent Console**.
2. Wählen Sie **Canvas-Schritt Agents** oder **Catalog Agents**.

### Schritt 2: Erstellungsmethode auswählen {#step-2-choose-how-to-build-an-agent}

Wählen Sie **Create agent** und dann eine der folgenden Optionen:

- **Custom agent**, um einen Agenten von Grund auf zu erstellen
- Eine Option unter **Create an agent with Operator**, um [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) zu verwenden und ein [Starttemplate](#agent-templates-built-with-operator) anzuwenden

Wenn Sie Operator verwenden, überprüfen und genehmigen Sie die Änderungen im Chat, bevor Sie mit dem nächsten Schritt fortfahren.

### Schritt 3: Details einrichten {#step-3-set-up-details}

Richten Sie als Nächstes die Details für Ihren Agenten ein:

1. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team den Zweck des Agenten versteht.
2. (optional) Fügen Sie Tags hinzu, um Ihren Agenten zu filtern.
3. Wählen Sie das [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference#models), das Ihr Agent verwenden soll.
4. Wenn Sie nicht das Modell **Braze Auto** verwenden, wählen Sie die [Denkstufe]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) des Modells. Sie können zwischen Minimal, Niedrig, Mittel oder Hoch wählen. Wir empfehlen, mit **Minimal** zu beginnen und die Antworten Ihres Agenten zu testen und diese Einstellung bei Bedarf anzupassen.
5. Legen Sie ein tägliches Aufruf-Limit fest. Standardmäßig ist dieser Wert auf 250.000 eingestellt, kann aber auf 1.000.000 erhöht werden. Wenn Sie das Limit über 1.000.000 hinaus erhöhen möchten, wenden Sie sich an Ihren CSM, um mehr zu erfahren. Setzen Sie das Limit nach dem Testen hoch genug für Ihre geplante Zielgruppengröße. Ein zu niedriges Limit verursacht Tageslimit-Fehler (die keine Credits verbrauchen, aber Fallback-Werte anwenden oder die Ausgabe auf `null` belassen).

Das Feld **Daily action credit cost limit** gibt die maximale Anzahl an Credits an, die dieser Agent pro Tag verbrauchen kann. Braze berechnet diesen Wert aus dem Pro-Aufruf-Credit-Verhältnis Ihres Workspace für das ausgewählte Modell (aus Ihrem Vertrag, angezeigt auf der Seite [Credit Ratios]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)), multipliziert mit dem täglichen Aufruf-Limit. Die Schätzung wird aktualisiert, wenn Sie das Modell oder das Aufruf-Limit ändern.

Um die Kosten zu steuern, senken Sie das tägliche Aufruf-Limit. Bei [Bring-your-own (BYO)]({{site.baseurl}}/user_guide/brazeai/agents/reference#option-2-bring-your-own-api-key)-Modellen können Sie auch zu einem kostengünstigeren Modell wechseln oder die [Denkstufe]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) reduzieren. **Braze Auto** unterstützt keine Anpassung der Denkstufe. Verfolgen Sie die tatsächliche Nutzung unter **Einstellungen** > **Abrechnung** > **Credits-Nutzung** > **Agent Console**.

![Agent-Console-Oberfläche zum Erstellen eines benutzerdefinierten Agenten in Braze. Der Bildschirm zeigt Felder zur Eingabe des Agentennamens und der Beschreibung, zur Auswahl eines Modells und zur Festlegung eines täglichen Aufruf-Limits.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Schritt 4: Anweisungen schreiben {#agent-instructions}

Geben Sie dem Agenten Anweisungen. Wenn Sie ein Operator-Template verwendet haben, überprüfen Sie die vorausgefüllten Anweisungen und bearbeiten Sie diese bei Bedarf.

Fügen Sie Anweisungen hinzu, was der Agent in unerwarteten oder mehrdeutigen Szenarien tun soll. Dies minimiert das Risiko, dass Verwirrung des Agenten zu Fehlern führt. Bitten Sie den Agenten beispielsweise nicht nur um „positive“ oder „negative“ Stimmungswerte, sondern lassen Sie ihn „unsicher“ zurückgeben, wenn er sich nicht entscheiden kann.

Lesen Sie die [Anweisungen schreiben]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) für Best Practices und [Beispiele]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples) als Inspiration für die Formulierung Ihrer Agenten-Prompts.

#### Kontext hinzufügen {#add-resources}

{% alert important %}
Agenten erhalten nur Daten, die Sie explizit übergeben – sie durchsuchen keine Nutzerprofile und warnen Sie nicht, wenn erforderliche Daten fehlen. Verwenden Sie Liquid in Ihren Anweisungen, wählen Sie **+ Agent context**, fügen Sie vorgelagerte [Context-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) in Canvas hinzu oder übergeben Sie zusätzlichen Kontext im Agent-Schritt. Eine vollständige Liste der Datenquellen und Designhinweise finden Sie unter [Welche Daten Agenten erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).
{% endalert %}

Wählen Sie **+ Agent context**, um auszuwählen, worauf Ihr Agent zugreifen kann. Dazu gehören:

- [Katalogfelder]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields): Geben Sie dem Agenten Zugriff auf Ihre Katalogdaten für genauere Antworten.
- [Wissensquellen]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources): Geben Sie dem Agenten Zugriff auf Katalogdaten über eine Wissensquelle für genaueres Abrufen als beim direkten Anhängen eines Katalogs.
- [Segment-Zugehörigkeit]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context): Lassen Sie den Agenten Antworten basierend darauf personalisieren, zu welchen Segmenten eine Nutzer:in gehört. Sie können bis zu fünf Segmente auswählen.
- [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines): Referenzieren Sie die Markenstimme und Stilrichtlinien, denen der Agent folgen soll. Wenn Ihr Agent beispielsweise SMS-Texte generieren soll, die Nutzer:innen dazu ermutigen, sich für eine Fitnessstudio-Mitgliedschaft anzumelden, können Sie dieses Feld verwenden, um auf Ihre vordefinierten, motivierenden Richtlinien zu verweisen.
- [Gesamter Canvas-Kontext]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables): Analysieren Sie alle Canvas-Kontextdaten für eine Nutzer:in, wenn dieser Agent aufgerufen wird, einschließlich aller Variablen, die nicht im Abschnitt **Instructions** referenziert werden.
- [Nutzerinteraktionsdaten]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history): Stellen Sie dem Agenten die aktuellen Campaign- und Canvas-Öffnungen, Klicks und Konversionsdaten jeder Nutzer:in zur Verfügung.

{% alert tip %}
Für Canvas-Agenten können Sie Liquid in Ihren Anweisungen verwenden, um auf Nutzerattribute wie Vor- und Nachname oder angepasste Attribute zu verweisen. Jede Liquid-Variable in den Agentenanweisungen wird automatisch an den Agent-Schritt übergeben, wenn eine Nutzer:in den Schritt betritt. Unter [Welche Daten Agenten erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive) erfahren Sie, wie Sie Canvas-Kontext und Profildaten gezielt übergeben.
{% endalert %}

### Schritt 5: Ausgabe auswählen {#select-output}

Im Abschnitt **Output** können Sie die [Ausgabe]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs) des Agenten mit einfachen oder erweiterten Schemas organisieren und definieren. Wenn Sie ein Operator-Template verwendet haben, überprüfen Sie das vorausgefüllte Ausgabeschema und bearbeiten Sie es bei Bedarf.

Für beste Ergebnisse stellen Sie sicher, dass das, was Sie im Abschnitt **Output** angeben, mit den Agentenanweisungen übereinstimmt, die Sie in [Schritt 4](#agent-instructions) eingegeben haben. Wenn Sie beispielsweise in den Agentenanweisungen angegeben haben, dass Sie ein Objekt mit zwei Strings möchten, stellen Sie sicher, dass Sie im Abschnitt **Output** ein Objekt mit zwei Strings angeben. Wenn Ihre Agentenanweisungen nicht mit der angegebenen Ausgabe übereinstimmen, kann der Agent verwirrt werden, eine Zeitüberschreitung erleiden oder unerwünschte Ausgaben generieren.

{% alert tip %}
Wenn Sie ein [erweitertes Ausgabeschema]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas) verwenden, fügen Sie ein String-Feld namens `explanation` hinzu, wenn der Agent zusätzlich zu seinen anderen Ausgaben seine Begründung zurückgeben soll. Weisen Sie den Agenten in Ihren [Anweisungen](#agent-instructions) an, `explanation` zu befüllen, wenn Ihnen das bei der Überprüfung oder Fehlersuche hilft.
{% endalert %}

#### Fallback-Werte konfigurieren {#configure-fallback-values}

Fallback-Werte sind nur für Canvas-Step-Agenten verfügbar. Im Abschnitt **Output** eines Canvas-Step-Agenten können Sie Werte definieren, die Braze verwendet, wenn ein Agentenaufruf fehlschlägt – beispielsweise wenn das LLM eine Zeitüberschreitung hat oder einen ungültigen API-Schlüssel-Fehler zurückgibt. Fallback-Werte funktionieren wie Personalisierungsstandards. Sie könnten eine statische Betreffzeile oder eine kurze Nachricht festlegen, die Nutzer:innen dennoch nützliche Ausgaben liefert, wenn der Agent nicht ausgeführt werden kann.

Catalog-Agenten unterstützen keine Konfiguration von Fallback-Werten in der Agent Console.

![Agent-Console-Ausgabekonfiguration mit dem Fallback-Ausgabefeld für ein Number-Schema.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Für Canvas-Agenten unterstützen Fallback-Werte [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)-Templating, sodass Sie Nutzerattribute oder Kontextvariablen im Fallback-Text referenzieren können.

Die Fallback-Felder passen sich dem Ausgabeformat Ihres Canvas-Step-Agenten an:

| Ausgabeformat | Fallback-Konfiguration |
| --- | --- |
| String, Number oder Boolean | Geben Sie einen einzelnen Fallback-Wert ein (Liquid wird unterstützt). |
| Felder (erweitertes Schema) | Geben Sie einen Fallback-Wert für jedes in der Agentenausgabe definierte Feld ein. |
| JSON-Schema (erweitertes Schema) | Braze liest Ihr JSON-Schema und generiert ein Eingabefeld für jede Eigenschaft, sodass Sie einen Fallback-Wert pro Schlüssel definieren können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fallback-Werte konfigurieren" }

Wenn ein Canvas-Step-Agent mit Fallback-Werten in einem [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) ausgeführt wird, rendert Braze den Fallback pro Nutzer:in und speichert ihn in der Ausgabevariable anstelle von `null`. Wenn Sie keine Fallback-Werte konfigurieren, bleibt die Canvas-Ausgabe bei fehlgeschlagenen Aufrufen ungesetzt (`null`).

Informationen zum Laufzeitverhalten finden Sie unter [Fehlerbehandlung und Fallback-Verhalten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

### Schritt 6: Den Agenten testen {#step-6-test-the-agent}

Der Bereich **Preview** ist eine Instanz des Agenten, die als nebeneinander liegendes Panel innerhalb der Konfigurationsoberfläche angezeigt wird. Sie können diesen Bereich nutzen, um den Agenten zu testen, während Sie ihn erstellen oder aktualisieren, und ihn auf ähnliche Weise wie Endnutzer:innen zu erleben. Dieser Schritt hilft Ihnen zu bestätigen, dass er sich wie erwartet verhält, und gibt Ihnen die Möglichkeit, vor der Aktivierung Feinabstimmungen vorzunehmen.

1. Geben Sie im Feld **Test your agent** Beispiel-Kundendaten oder Kundenantworten ein – alles, was reale Szenarien widerspiegelt, die Ihr Agent bearbeiten wird.
2. Zeigen Sie die Antwort des Agenten für eine zufällige Nutzer:in, eine bestehende Nutzer:in oder eine benutzerdefinierte Nutzer:in in der Vorschau an.
3. Wählen Sie **Simulate response**. Der Agent wird basierend auf Ihrer Konfiguration ausgeführt und zeigt seine Antwort an.

{% alert note %}
Testläufe werden auf Ihr tägliches Aufruf-Limit angerechnet.
{% endalert %}

![Agent Console mit dem Vorschaubereich zum Testen eines benutzerdefinierten Agenten. Die Oberfläche zeigt ein Feld für Beispieleingaben mit Beispiel-Kundendaten, einen Button zum Ausführen des Tests und einen Antwortbereich, in dem die Agentenausgabe erscheint.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Überprüfen Sie die Ausgabe mit kritischem Blick. Berücksichtigen Sie die folgenden Fragen:

- Fühlt sich der Text markenkonform an?
- Leitet die Entscheidungslogik Kund:innen wie beabsichtigt weiter?
- Sind die berechneten Werte korrekt?

Wenn etwas nicht stimmt, aktualisieren Sie die Konfiguration des Agenten und testen Sie erneut. Führen Sie verschiedene Eingaben durch, um zu sehen, wie sich der Agent über verschiedene Szenarien hinweg anpasst, insbesondere bei Grenzfällen wie fehlenden Daten oder ungültigen Antworten.

{% alert tip %}
Vermeiden Sie es, dem Agenten genau zu sagen, was er *nicht* tun soll. LLMs können diesen Inhalt trotzdem generieren, wenn Sie ihn in den Anweisungen erwähnen.
{% endalert %}

### Schritt 7: Ihren Agenten verwenden {#step-7-use-your-agent}

Ihr Agent ist jetzt einsatzbereit! Weitere Details finden Sie unter [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Mit Operator erstellte Agenten-Templates {#agent-templates-built-with-operator}

Operator kann Anweisungen, Ausgabefelder und Kontext für die folgenden Startvorlagen der Agent Console vorkonfigurieren. Wählen Sie ein Template in Operator aus oder bitten Sie Operator, eines nach Namen anzuwenden.

### Canvas-Schritt-Agenten-Templates {#canvas-step-agent-templates}

| Template | Beschreibung | Beispielausgabe |
| --- | --- | --- |
| Personalisierter Texter | Generiert kanalspezifische Nachrichtentexte aus Nutzerattributen, Canvas-Kontext und Markenrichtlinien | E-Mail-Betreffzeile und Preheader; Push-Titel und -Text |
| Feedback-Analyst | Analysiert offene Umfrage- oder Support-Feedbacks und wandelt sie in strukturierte Felder für Canvas-Verzweigungen um | Stimmung, Thema, empfohlene nächste Aktion |
| Journey-Router | Leitet Nutzer:innen basierend auf Profil- und Journey-Kontext zum relevantesten Canvas-Pfad weiter | Pfadname oder boolescher Wert für Decision-Split-Schritte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvas-Schritt-Agenten-Templates" }

### Katalog-Agenten-Templates {#catalog-agent-templates}

| Template | Beschreibung | Beispielausgabe |
| --- | --- | --- |
| Beschreibungstexter | Erstellt kurze Marketingbeschreibungen aus vorhandenen Katalogspalten | Produkt- oder Zielbeschreibung |
| Artikelkategorisierer | Weist Kategorien oder Tags aus Zeilendaten zu | Kategorielabels für Filterung und Empfehlungen |
| Lokalisierungsübersetzer | Übersetzt Katalog-Strings in Zielsprachen innerhalb von Zeichenlimits | Lokalisierter Text pro Sprache |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Katalog-Agenten-Templates" }

## Verwandte Ressourcen {#related-resources}

- [Referenz für Agents]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq)
- [Braze-Webinar über KI in Aktion: 3 neue Anwendungsfälle für 1:1-Personalisierung](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)