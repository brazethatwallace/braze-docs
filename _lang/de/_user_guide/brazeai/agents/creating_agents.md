---
nav_title: Agenten erstellen
article_title: Angepasste Agenten erstellen
description: "Erfahren Sie, wie Sie Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können."
page_order: 1
alias: /creating-agents/
---

# Angepasste Agenten erstellen {#create-custom-agents}

> Erfahren Sie, wie Sie angepasste Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/).

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

- [Berechtigung]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) für den Zugriff auf die **Agentenkonsole** in Ihrem Workspace. Wenden Sie sich an Ihre Braze-Administratoren, falls diese Option nicht angezeigt wird.
- Berechtigung zum Erstellen und Bearbeiten von angepassten KI-Agenten.
- Eine Idee davon, was der Agent erreichen soll. Braze-Agenten können die folgenden Aktionen unterstützen:
   - **Personalisiertes Messaging:** Generieren Sie Betreffzeilen, Überschriften, Produkttexte oder andere Inhalte.
   - **Nutzer:innen-Routing:** Leiten Sie Nutzer:innen in Canvas basierend auf Verhalten, Präferenzen oder angepassten Attributen weiter.
   - **Datenmanagement:** Berechnen Sie Werte, ergänzen Sie Katalogeinträge oder aktualisieren Sie Profilfelder.

## Funktionsweise {#how-it-works}

Wenn Sie einen Agenten erstellen, definieren Sie dessen Zweck und legen Leitplanken für sein Verhalten fest. Nach der Live-Schaltung kann der Agent in Braze eingesetzt werden, um personalisierte Texte zu generieren, Entscheidungen in Realtime zu treffen oder Katalogfelder zu aktualisieren. Während Sie Ihren Agenten erstellen, können Sie ihn als Entwurf speichern, und Sie können einen Agenten jederzeit über das Dashboard pausieren oder aktualisieren.

Die folgenden Anwendungsfälle veranschaulichen einige Möglichkeiten, angepasste Agenten zu nutzen.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Bearbeitung von Kundenfeedback | Leiten Sie das Feedback der Nutzer:innen an einen Agenten weiter, um die Stimmung zu analysieren und einfühlsame Follow-up-Nachrichten zu generieren. Bei besonders wertvollen Nutzer:innen kann der Agent die Antwort eskalieren oder Vergünstigungen hinzufügen. |
| Inhalte lokalisieren | Übersetzen Sie Katalogtexte für globale Campaigns in andere Sprachen oder passen Sie Tonfall und Länge für regionsspezifische Kanäle an. Übersetzen Sie beispielsweise „Classic Clubmaster Sunglasses“ ins Spanische als „Gafas de sol Classic Clubmaster“ oder kürzen Sie Beschreibungen für SMS-Campaigns. |
| Bewertungen oder Feedback zusammenfassen | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, beispielsweise durch die Vergabe von Stimmungsbewertungen wie „Positiv“, „Neutral“ oder „Negativ“ oder durch die Erstellung einer kurzen Textzusammenfassung wie „Die meisten Kund:innen erwähnen die hervorragende Passform, bemerken jedoch den langsamen Versand.“ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Funktionsweise" }

## Einen Agenten erstellen {#create-an-agent}

### 1. Schritt: Agententyp auswählen {#step-1-choose-an-agent-type}

Um einen Agenten zu erstellen, wählen Sie zunächst Ihren Agententyp aus:

1. Gehen Sie zur **Agentenkonsole**.
2. Wählen Sie **Canvas-Schritt-Agenten** oder **Katalog-Agenten** aus.

### 2. Schritt: Erstellungsmethode auswählen {#step-2-choose-how-to-build-an-agent}

Wählen Sie **Agent erstellen** aus und entscheiden Sie sich dann für eine der folgenden Optionen:

a. **Angepasster Agent**, um einen Agenten von Grund auf zu erstellen
b. Eine Option unter **Agent mit Operator erstellen**, um [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) zu verwenden und ein [Starttemplate](#agent-templates-built-with-operator) anzuwenden

Wenn Sie Operator verwenden, überprüfen und genehmigen Sie die Änderungen im Chat, bevor Sie mit dem nächsten Schritt fortfahren.

### 3. Schritt: Details einrichten {#step-3-set-up-details}

Richten Sie anschließend die Details für Ihren Agenten ein:

1. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team den Zweck versteht.
2. (optional) Fügen Sie Tags hinzu, um Ihren Agenten zu filtern.
3. Wählen Sie das [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) aus, das Ihr Agent verwenden soll.
4. Wenn Sie nicht das **Braze Auto**-Modell verwenden, wählen Sie die [Denkstufe]({{site.baseurl}}/user_guide/brazeai/agents/reference/#thinking-levels) des Modells aus. Sie können zwischen Minimal, Niedrig, Mittel oder Hoch wählen. Wir empfehlen, mit **Minimal** zu beginnen, die Antworten Ihres Agenten zu testen und diese bei Bedarf anzupassen.
5. Legen Sie ein tägliches Ausführungslimit fest. Standardmäßig ist dieser Wert auf 250.000 eingestellt, kann jedoch auf 1.000.000 erhöht werden. Wenn Sie das Limit über 1.000.000 hinaus erhöhen möchten, wenden Sie sich an Ihren Customer-Success-Manager, um mehr zu erfahren.

![Agentenkonsole-Oberfläche zum Erstellen eines angepassten Agenten in Braze. Der Bildschirm zeigt Felder zur Eingabe des Agentennamens und der Beschreibung, zur Auswahl eines Modells und zur Festlegung eines täglichen Ausführungslimits.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### 4. Schritt: Anweisungen verfassen {#agent-instructions}

Geben Sie dem Agenten Anweisungen. Wenn Sie ein Operator-Template verwendet haben, überprüfen Sie die vorausgefüllten Anweisungen und bearbeiten Sie diese bei Bedarf.

Nehmen Sie Anweisungen dafür auf, wie der Agent in unerwarteten oder unklaren Szenarien vorgehen soll. Dadurch wird das Risiko minimiert, dass Verwirrung beim Agenten zu Fehlern führt. Anstatt beispielsweise den Agenten nur nach „positiven“ oder „negativen“ Stimmungswerten zu fragen, bitten Sie ihn, „unsicher“ zurückzugeben, wenn er sich nicht entscheiden kann.

Lesen Sie den Abschnitt [Anweisungen verfassen]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) für bewährte Verfahren und [Beispiele]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) für Anregungen, wie Sie Ihren Agenten anweisen können.

{% alert tip %}
Für Canvas-Agenten können Sie Liquid in Ihren Anweisungen verwenden, um auf Nutzerattribute wie Vor- und Nachname oder angepasste Attribute zu referenzieren. Jede Liquid-Variable in den Agentenanweisungen wird automatisch an den Canvas-Schritt übergeben, wenn Nutzer:innen den Schritt betreten.
{% endalert %}

#### Kontext hinzufügen {#add-resources}

Wählen Sie **+ Agentenkontext** aus, um festzulegen, worauf Ihr Agent zugreifen kann. Dies beinhaltet:

- [Katalogfelder]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Gewähren Sie dem Agenten Zugriff auf Ihre Katalogdaten für genauere Antworten.
- [Segmentzugehörigkeit]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Ermöglichen Sie dem Agenten, Antworten basierend auf der Segmentzugehörigkeit der Nutzer:innen zu personalisieren. Sie können bis zu fünf Segmente auswählen.
- [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/): Referenzieren Sie die Richtlinien zur Markenstimme und zum Stil, die der Agent befolgen soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte erstellt, um Nutzer:innen zur Anmeldung für eine Fitnessstudio-Mitgliedschaft zu motivieren, können Sie dieses Feld verwenden, um Ihre vordefinierte, motivierende Richtlinie zu referenzieren.
- [Gesamter Canvas-Kontext]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/): Analysieren Sie alle Canvas-Kontextdaten für Nutzer:innen, wenn dieser Agent aufgerufen wird, einschließlich aller Variablen, die nicht im Abschnitt **Anweisungen** referenziert werden.
- [Nutzer:innen-Interaktionsdaten]({{site.baseurl}}/user_guide/brazeai/agents/reference/#user-history): Stellen Sie dem Agenten die aktuellen Öffnungs-, Klick- und Conversion-Daten der jeweiligen Nutzer:innen aus Campaigns und Canvas bereit.

### 5. Schritt: Ausgabe auswählen {#select-output}

Im Abschnitt **Ausgabe** können Sie die [Ausgabe]({{site.baseurl}}/user_guide/brazeai/agents/reference/#outputs) des Agenten anhand von Basisschemata oder erweiterten Schemata organisieren und definieren. Wenn Sie ein Operator-Template verwendet haben, überprüfen Sie das vorausgefüllte Ausgabeschema und bearbeiten Sie es bei Bedarf.

Um optimale Ergebnisse zu erzielen, stellen Sie sicher, dass die Angaben im Abschnitt **Ausgabe** mit den Agentenanweisungen übereinstimmen, die Sie in [Schritt 4](#agent-instructions) eingegeben haben. Wenn Sie beispielsweise in den Agentenanweisungen angegeben haben, dass Sie ein Objekt mit zwei Strings wünschen, stellen Sie sicher, dass Sie im Abschnitt **Ausgabe** ein Objekt mit zwei Strings angeben. Wenn Ihre Agentenanweisungen nicht mit der festgelegten Ausgabe übereinstimmen, kann der Agent verwirrt werden, eine Zeitüberschreitung verursachen oder unerwünschte Ausgaben generieren.

{% alert tip %}
Wenn Sie ein [erweitertes Ausgabeschema]({{site.baseurl}}/user_guide/brazeai/agents/reference/#advanced-schemas) verwenden, fügen Sie ein String-Feld namens `explanation` hinzu, wenn der Agent zusätzlich zu seinen anderen Ausgaben seine Begründung zurückgeben soll. Weisen Sie den Agenten in Ihren [Anweisungen](#agent-instructions) an, `explanation` zu befüllen, wenn Ihnen das bei der Überprüfung oder Fehlersuche hilft.
{% endalert %}

### 6. Schritt: Agenten testen und erstellen {#step-6-test-and-create-the-agent}

Der **Vorschaubereich** ist eine Instanz des Agenten, die als nebeneinander angeordnetes Panel innerhalb der Konfiguration angezeigt wird. Sie können diesen Bereich verwenden, um den Agenten zu testen, während Sie ihn erstellen oder aktualisieren, und ihn auf ähnliche Weise wie Endnutzer:innen zu erleben. Dieser Schritt hilft Ihnen zu bestätigen, dass er sich wie erwartet verhält, und gibt Ihnen die Möglichkeit, vor der Live-Schaltung Feinabstimmungen vorzunehmen.

1. Geben Sie im Feld **Agent testen** Beispielkundendaten oder Kundenantworten ein – alles, was reale Szenarien widerspiegelt, mit denen Ihr Agent konfrontiert sein wird.
2. Zeigen Sie eine Vorschau der Antwort des Agenten für zufällige Nutzer:innen, bestehende Nutzer:innen oder angepasste Nutzer:innen an.
3. Wählen Sie **Antwort simulieren** aus. Der Agent führt die Konfiguration aus und zeigt seine Antwort an.

{% alert note %}
Testläufe werden auf Ihr tägliches Ausführungslimit angerechnet.
{% endalert %}

![Agentenkonsole mit dem Vorschaubereich zum Testen eines angepassten Agenten. Die Oberfläche zeigt ein Feld für Beispieleingaben mit Beispielkundendaten, einen Button zum Ausführen des Tests und einen Antwortbereich, in dem die Ausgabe des Agenten angezeigt wird.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Überprüfen Sie die Ausgabe mit kritischem Blick. Berücksichtigen Sie die folgenden Fragen:

- Entspricht der Text dem Markenimage?
- Leitet die Entscheidungslogik die Kund:innen wie beabsichtigt weiter?
- Sind die berechneten Werte korrekt?

Wenn etwas nicht stimmt, aktualisieren Sie die Konfiguration des Agenten und testen Sie erneut. Führen Sie einige unterschiedliche Eingaben durch, um zu beobachten, wie sich der Agent an verschiedene Szenarien anpasst – insbesondere an Randfälle wie fehlende Daten oder ungültige Antworten.

{% alert tip %}
Vermeiden Sie es, dem Agenten genau mitzuteilen, was er nicht tun soll. LLMs können diesen Inhalt dennoch generieren, wenn Sie ihn in den Anweisungen erwähnen.
{% endalert %}

### 7. Schritt: Ihren Agenten verwenden {#step-7-use-your-agent}

Ihr Agent ist nun einsatzbereit! Weitere Informationen finden Sie unter [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Mit Operator erstellte Agenten-Templates {#agent-templates-built-with-operator}

Operator kann Anweisungen, Ausgabefelder und Kontext für die folgenden Startvorlagen der Agentenkonsole vorkonfigurieren. Wählen Sie ein Template in Operator aus oder bitten Sie Operator, eines nach Namen anzuwenden.

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

- [Referenz für Agenten]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
- [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/brazeai/agents/faq/)
- [Braze-Webinar über KI in Aktion: 3 neue Anwendungsfälle für 1:1-Personalisierung](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)