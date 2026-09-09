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
- Eine Idee davon, was der Agent erreichen soll. Braze Agents können die folgenden Aktionen unterstützen:
   - **Personalisiertes Messaging:** Betreffzeilen, Überschriften, In-Product-Texte oder andere Inhalte generieren.
   - **Nutzer:innen-Routing:** Nutzer:innen in Canvas basierend auf Verhalten, Präferenzen oder angepassten Attributen weiterleiten.
   - **Datenverwaltung:** Werte berechnen, Katalogeinträge anreichern oder Profilfelder aktualisieren.

## So funktioniert es {#how-it-works}

Wenn Sie einen Agenten erstellen, definieren Sie seinen Zweck und legen Guardrails fest, die sein Verhalten steuern. Sobald er aktiv ist, kann der Agent in Braze eingesetzt werden, um personalisierte Texte zu generieren, Realtime-Entscheidungen zu treffen oder Katalogfelder zu aktualisieren. Während Sie Ihren Agenten erstellen, können Sie ihn als Entwurf speichern und jederzeit über das Dashboard aktualisieren. Jedes Speichern erstellt eine neue Version, die Sie im Tab [Versionsverlauf]({{site.baseurl}}/user_guide/brazeai/agents/reference#version-history) einsehen können.

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten, angepasste Agenten zu nutzen.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Kundenfeedback verarbeiten | Übergeben Sie Nutzerfeedback an einen Agenten, um die Stimmung zu analysieren und empathische Folgenachrichten zu generieren. Bei besonders wertvollen Nutzer:innen kann der Agent die Antwort eskalieren oder Vergünstigungen hinzufügen. |
| Inhalte lokalisieren | Übersetzen Sie Katalogtexte in eine andere Sprache für globale Campaigns, oder passen Sie Ton und Länge für regionsspezifische Kanäle an. Übersetzen Sie beispielsweise „Classic Clubmaster Sunglasses“ ins Spanische als „Gafas de sol Classic Clubmaster“ oder kürzen Sie Beschreibungen für SMS-Campaigns. |
| Bewertungen oder Feedback zusammenfassen | Fassen Sie Stimmungen oder Feedback in einem neuen Feld zusammen, z. B. durch Zuweisen von Stimmungswerten wie „Positiv“, „Neutral“ oder „Negativ“, oder erstellen Sie eine kurze Textzusammenfassung wie „Die meisten Kund:innen loben die gute Passform, weisen aber auf langsamen Versand hin.“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="So funktioniert es" }

## Einen Agenten erstellen {#create-an-agent}

### Schritt 1: Agententyp auswählen {#step-1-choose-an-agent-type}

Um einen Agenten zu erstellen, wählen Sie zunächst Ihren Agententyp:

1. Gehen Sie zur **Agent Console**.
2. Wählen Sie **Canvas Step Agents** oder **Catalog Agents**.

### Schritt 2: Erstellungsmethode auswählen {#step-2-choose-how-to-build-an-agent}

Wählen Sie **Create agent** und dann eine der folgenden Optionen:

- **Custom agent**, um einen Agenten von Grund auf zu erstellen
- Eine Option unter **Create an agent with Operator**, um [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) zu verwenden und ein [Starttemplate](#agent-templates-built-with-operator) anzuwenden

Wenn Sie Operator verwenden, überprüfen und genehmigen Sie dessen Änderungen im Chat, bevor Sie mit dem nächsten Schritt fortfahren.

### Schritt 3: Details einrichten {#step-3-set-up-details}

Richten Sie als Nächstes die Details für Ihren Agenten ein:

1. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team den Zweck versteht.
2. (optional) Fügen Sie Tags hinzu, um Ihren Agenten zu filtern.
3. Wählen Sie das [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) aus, das Ihr Agent verwenden soll.
4. Wenn Sie nicht das **Braze Auto**-Modell verwenden, wählen Sie die [Denkstufe]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) des Modells. Sie können zwischen minimal, niedrig, mittel oder hoch wählen. Wir empfehlen, mit **Minimal** zu beginnen und die Antworten Ihres Agenten zu testen und diese bei Bedarf anzupassen.
5. Legen Sie ein tägliches Aufruf-Limit fest. Standardmäßig ist dieser Wert auf 250.000 eingestellt, kann aber auf 1.000.000 erhöht werden. Wenn Sie das Limit über 1.000.000 hinaus erhöhen möchten, wenden Sie sich an Ihren Customer-Success-Manager, um mehr zu erfahren. Setzen Sie das Limit nach dem Testen hoch genug für Ihre geplante Zielgruppengröße. Ein zu niedriges Limit verursacht Fehler durch das tägliche Limit (die keine Credits verbrauchen, aber Fallback-Werte anwenden oder die Ausgabe `null` belassen).

Das Feld **Daily action credit cost limit** gibt die maximale Anzahl an Credits an, die dieser Agent pro Tag verbrauchen kann. Braze berechnet diesen Wert anhand des Credit-Verhältnisses pro Aufruf Ihres Workspace für das ausgewählte Modell (aus Ihrem Vertrag, angezeigt auf der Seite [Credit Ratios]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage)), multipliziert mit dem täglichen Aufruf-Limit. Die Schätzung wird aktualisiert, wenn Sie das Modell oder das Aufruf-Limit ändern.

Um Kosten zu steuern, senken Sie das tägliche Aufruf-Limit. Bei [Bring-your-own-Modellen (BYO)]({{site.baseurl}}/user_guide/brazeai/agents/reference#option-2-bring-your-own-api-key) können Sie auch auf ein kostengünstigeres Modell wechseln oder die [Denkstufe]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels) reduzieren. **Braze Auto** unterstützt keine Anpassung der Denkstufe. Verfolgen Sie die tatsächliche Nutzung unter **Settings** > **Billing** > **Credits Usage** > **Agent Console**.

![Agent-Console-Oberfläche zum Erstellen eines benutzerdefinierten Agenten in Braze. Der Bildschirm zeigt Felder zur Eingabe von Agentenname und Beschreibung, zur Auswahl eines Modells und zum Festlegen eines täglichen Aufruf-Limits.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Schritt 4: Anweisungen schreiben {#agent-instructions}

Geben Sie dem Agenten Anweisungen. Wenn Sie ein Operator-Template verwendet haben, überprüfen Sie die vorausgefüllten Anweisungen und bearbeiten Sie sie bei Bedarf.

Fügen Sie Anweisungen für unerwartete oder mehrdeutige Szenarien hinzu. Dies minimiert das Risiko, dass Verwirrung des Agenten zu Fehlern führt. Bitten Sie den Agenten beispielsweise statt nur um „positive“ oder „negative“ Stimmungswerte darum, „unsicher“ zurückzugeben, wenn er sich nicht entscheiden kann.

Lesen Sie die [Anweisungen schreiben]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) für Best Practices und die [Beispiele]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples) für Inspiration, wie Sie Ihren Agenten prompten.

#### Kontext hinzufügen {#add-resources}

{% alert important %}
Agenten erhalten nur Daten, die Sie explizit übergeben – sie durchsuchen keine Nutzerprofile und warnen Sie nicht, wenn erforderliche Daten fehlen. Verwenden Sie Liquid in Ihren Anweisungen, wählen Sie **+ Agent context**, fügen Sie vorgelagerte [Context-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) in Canvas hinzu oder übergeben Sie zusätzlichen Kontext im Agent-Schritt. Eine vollständige Liste der Datenquellen und Designanleitungen finden Sie unter [Welche Daten Agenten erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).
{% endalert %}

Wählen Sie **+ Agent context**, um auszuwählen, worauf Ihr Agent zugreifen kann. Dazu gehören:

- [Catalog-Felder]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields): Geben Sie dem Agenten Zugriff auf Ihre Catalog-Daten für genauere Antworten.
- [Wissensquellen]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources): Geben Sie dem Agenten über eine Wissensquelle Zugriff auf Catalog-Daten für eine genauere Abfrage als das direkte Anhängen eines Catalogs.
- [Segment-Mitgliedschaft]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context): Lassen Sie den Agenten Antworten basierend darauf personalisieren, zu welchen Segmenten Nutzer:innen gehören. Sie können bis zu fünf Segmente auswählen.
- [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines): Referenzieren Sie die Markenstimme und Stilrichtlinien, denen der Agent folgen soll. Wenn Ihr Agent beispielsweise SMS-Texte generieren soll, um Nutzer:innen zur Anmeldung für eine Fitnessstudio-Mitgliedschaft zu motivieren, können Sie dieses Feld verwenden, um auf Ihre vordefinierten, kraftvollen und motivierenden Richtlinien zu verweisen.
- [Gesamter Canvas-Kontext]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables): Analysieren Sie alle Canvas-Kontextdaten für Nutzer:innen, wenn dieser Agent aufgerufen wird, einschließlich aller Variablen, die nicht im Abschnitt **Instructions** referenziert werden.
- [Nutzerinteraktionsdaten]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history): Stellen Sie dem Agenten die aktuellen Campaign- und Canvas-Öffnungen, Klicks und Konversionsdaten jeder/jedes Nutzerin/Nutzers bereit.

{% alert tip %}
Für Canvas-Agenten können Sie Liquid in Ihren Anweisungen verwenden, um Nutzerattribute wie Vor- und Nachname oder angepasste Attribute zu referenzieren. Jede Liquid-Variable in den Agenten-Anweisungen wird automatisch an den Agent-Schritt übergeben, wenn Nutzer:innen den Schritt betreten. Unter [Welche Daten Agenten erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive) erfahren Sie, wie Sie Canvas-Kontext- und Profildaten gezielt übergeben.
{% endalert %}

### Schritt 5: Ausgabe auswählen {#select-output}

Im Abschnitt **Output** können Sie die [Ausgabe]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs) des Agenten mit einfachen oder erweiterten Schemas organisieren und definieren. Wenn Sie ein Operator-Template verwendet haben, überprüfen Sie das vorausgefüllte Ausgabeschema und bearbeiten Sie es bei Bedarf.

Für beste Ergebnisse stellen Sie sicher, dass die Angaben im Abschnitt **Output** mit den Agenten-Anweisungen übereinstimmen, die Sie in [Schritt 4](#agent-instructions) eingegeben haben. Wenn Sie beispielsweise in den Agenten-Anweisungen angegeben haben, dass Sie ein Objekt mit zwei Strings möchten, stellen Sie sicher, dass Sie im Abschnitt **Output** ein Objekt mit zwei Strings angeben. Wenn Ihre Agenten-Anweisungen nicht mit Ihrer angegebenen Ausgabe übereinstimmen, kann der Agent verwirrt werden, ein Timeout verursachen oder unerwünschte Ausgaben erzeugen.

{% alert tip %}
Wenn Sie ein [erweitertes Ausgabeschema]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas) verwenden, fügen Sie ein String-Feld mit dem Namen `explanation` hinzu, wenn der Agent seine Begründung zusätzlich zu seinen anderen Ausgaben zurückgeben soll. Weisen Sie den Agenten in Ihren [Anweisungen](#agent-instructions) an, `explanation` zu befüllen, wenn dies beim Überprüfen oder Debuggen von Antworten hilft.
{% endalert %}

#### Fallback-Werte konfigurieren {#configure-fallback-values}

Fallback-Werte sind nur für Canvas-Step-Agenten verfügbar. Im Abschnitt **Output** eines Canvas-Step-Agenten können Sie Werte definieren, die Braze verwendet, wenn ein Agentenaufruf fehlschlägt – beispielsweise wenn das LLM ein Timeout verursacht oder einen ungültigen API-Schlüssel-Fehler zurückgibt. Fallback-Werte funktionieren wie Personalisierungsstandards. Sie könnten eine statische Betreffzeile oder eine kurze Nachricht festlegen, die Nutzer:innen dennoch nützliche Ausgaben liefert, wenn der Agent nicht ausgeführt werden kann.

Catalog-Agenten unterstützen die Konfiguration von Fallback-Werten in der Agent Console nicht.

![Agent-Console-Ausgabekonfiguration mit dem Feld für Fallback-Ausgabe bei einem Number-Schema.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Für Canvas-Agenten unterstützen Fallback-Werte [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)-Templating, sodass Sie Nutzerattribute oder Kontextvariablen im Fallback-Text referenzieren können.

Die Fallback-Felder passen sich dem Ausgabeformat Ihres Canvas-Step-Agenten an:

| Ausgabeformat | Fallback-Konfiguration |
| --- | --- |
| String, Number oder Boolean | Geben Sie einen einzelnen Fallback-Wert ein (Liquid wird unterstützt). |
| Felder (erweitertes Schema) | Geben Sie einen Fallback-Wert für jedes in der Agenten-Ausgabe definierte Feld ein. |
| JSON-Schema (erweitertes Schema) | Braze liest Ihr JSON-Schema und generiert für jede Eigenschaft ein Eingabefeld, damit Sie einen Fallback-Wert pro Schlüssel definieren können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fallback-Werte konfigurieren" }

Wenn ein Canvas-Step-Agent mit Fallback-Werten in einem [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) ausgeführt wird, rendert Braze den Fallback pro Nutzer:in und speichert ihn in der Ausgabevariablen anstelle von `null`. Wenn Sie keine Fallback-Werte konfigurieren, bleibt die Canvas-Ausgabe bei fehlgeschlagenen Aufrufen ungesetzt (`null`).

Zum Laufzeitverhalten siehe [Fehlerbehandlung und Fallback-Verhalten]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior).

### Schritt 6: Den Agenten testen {#step-6-test-the-agent}

Der Bereich **Preview** ist eine Instanz des Agenten, die als Side-by-Side-Panel innerhalb der Konfigurationsansicht erscheint. Sie können diesen Bereich nutzen, um den Agenten während der Erstellung oder Aktualisierung zu testen und ihn auf ähnliche Weise wie Endnutzer:innen zu erleben. Dieser Schritt hilft Ihnen zu bestätigen, dass er sich wie erwartet verhält, und gibt Ihnen die Möglichkeit, vor dem Go-Live Feinabstimmungen vorzunehmen.

1. Geben Sie im Feld **Test your agent** Beispiel-Kundendaten oder Kundenantworten ein – alles, was reale Szenarien widerspiegelt, die Ihr Agent bewältigen wird.
2. Zeigen Sie die Antwort des Agenten für zufällige, bestehende oder benutzerdefinierte Nutzer:innen in der Vorschau an.
3. Wählen Sie **Simulate response**. Der Agent wird basierend auf Ihrer Konfiguration ausgeführt und zeigt seine Antwort an.

{% alert note %}
Testläufe werden auf Ihr tägliches Aufruf-Limit angerechnet.
{% endalert %}

![Agent Console mit dem Preview-Bereich zum Testen eines benutzerdefinierten Agenten. Die Oberfläche zeigt ein Feld für Beispieleingaben mit Beispiel-Kundendaten, einen Button zum Ausführen des Tests und einen Antwortbereich, in dem die Agentenausgabe erscheint.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Überprüfen Sie die Ausgabe mit kritischem Blick. Berücksichtigen Sie die folgenden Fragen:

- Fühlt sich der Text markenkonform an?
- Leitet die Entscheidungslogik Kund:innen wie beabsichtigt weiter?
- Sind die berechneten Werte korrekt?

Wenn etwas nicht stimmt, aktualisieren Sie die Konfiguration des Agenten und testen Sie erneut. Führen Sie verschiedene Eingaben durch, um zu sehen, wie sich der Agent über Szenarien hinweg anpasst, insbesondere bei Grenzfällen wie fehlenden Daten oder ungültigen Antworten.

{% alert tip %}
Vermeiden Sie es, dem Agenten genau zu sagen, was er nicht tun soll. LLMs können diese Inhalte trotzdem generieren, wenn Sie sie in den Anweisungen erwähnen.
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