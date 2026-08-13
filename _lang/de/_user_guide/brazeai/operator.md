---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Erfahren Sie, wie Sie auf BrazeAI Operator<sup>TM</sup> zugreifen und diesen nutzen können, einen in das Braze-Dashboard integrierten KI-gestützten Assistenten, einschließlich seiner Features und Best Practices."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> ist ein KI-gestützter Assistent, der in das Dashboard integriert ist. Operator unterstützt Sie beim Erstellen – beim Entwerfen von Campaigns, Segmenten und Inhalten – und hilft Ihnen, wenn Sie nicht weiterkommen, indem er Fragen beantwortet, bei der Fehlerbehebung unterstützt und gemeinsam mit Ihnen Ideen entwickelt.

## Auf Operator zugreifen {#access-operator}

Öffnen Sie Operator von jeder Seite im Braze-Dashboard aus.

1. Wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Nutzerprofil aus.
2. Das Operator-Chat-Panel öffnet sich in einem Seitenpanel.

![Das Chat-Panel von Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximieren Sie das Panel, um es für eine bessere Lesbarkeit zu vergrößern, oder minimieren Sie es, um Operator während der Arbeit verfügbar zu halten.
{% endalert %}

## Operator verwenden {#use-operator}

Beschreiben Sie in natürlicher Sprache, was Sie erreichen möchten. Klare und spezifische Prompts führen zu hilfreicheren Antworten. Prompts können von einer einzelnen Frage bis hin zu einer vollständigen Erstellungsanfrage reichen:

- **Eine Frage stellen:** Warum wird mein Liquid nicht gerendert?
- **Etwas erstellen:** Erstelle ein Segment von Nutzer:innen, die in den letzten 7 Tagen ihren Warenkorb abgebrochen haben.

Operator kann Schritt-für-Schritt-Anleitungen, Links zur Braze-Dokumentation, Erklärungen in einfacher Sprache sowie Entwürfe von Campaigns, Segmenten und Inhalten bereitstellen, die Sie überprüfen und direkt in Ihre Arbeit einfügen können. Informationen dazu, wie Operator Änderungen vorschlägt und anwendet, finden Sie unter [Aktionen mit Operator ausführen](#take-action-with-operator).

Operator verwendet [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), das sich für komplexe, mehrstufige Aufgaben eignet. Den vollständigen Umfang dessen, was Operator Ihnen beim Erstellen helfen kann, finden Sie unter [Was Sie mit Operator tun können]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Sofort einsetzbare Beispiele finden Sie in der [Prompt-Bibliothek]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

Sehen Sie sich dieses Video an, um ein Beispiel dafür zu erhalten, was Operator leisten kann.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Best Practices {#best-practices}

Behandeln Sie Operator wie eine Konversation, nicht wie eine Suchmaschine. Kurze, natürliche Prompts funktionieren am besten.

- **Seien Sie konkret:** Anstelle von „Erzählen Sie mir etwas über Canvas“ versuchen Sie es mit „Wie verwende ich Aktionspfade in Canvas?“.
- **Stellen Sie Folgefragen:** Sollte die erste Antwort Ihre Frage nicht vollständig beantworten, bitten Sie um eine Klarstellung oder um weitere Details. Operator merkt sich frühere Nachrichten in der Konversation, bis Sie Ihren Chatverlauf löschen.
- **Nutzen Sie den seitenbezogenen Kontext:** Operator erkennt Ihren Standort in Braze. Öffnen Sie Operator, während Sie die entsprechende Seite anzeigen, um die genauesten Ergebnisse zu erhalten.

## Passen Sie Ihr Erlebnis an {#customize-your-experience}

### Markenrichtlinien anwenden {#apply-brand-guidelines}

Fügen Sie Markenrichtlinien als Kontext zu Operator-Abfragen hinzu, damit die Antworten dem Stil, Tonfall und der Persönlichkeit Ihrer Marke entsprechen. Operator nutzt die in Ihrem Workspace konfigurierten Markenrichtlinien, was dazu beiträgt, ein einheitliches Messaging zu gewährleisten, wenn er Texte vorschlägt oder Features erläutert.

Um Markenrichtlinien festzulegen, navigieren Sie zu **Inhalt** > **Markenrichtlinien**. Weitere Informationen finden Sie unter [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines).

![Auswahl der Markenrichtlinien im Chat-Panel von Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Seitenbezogenen Kontext nutzen {#leverage-page-aware-context}

Operator erkennt automatisch Ihren Standort in Braze und passt die Antworten entsprechend an. Wenn Sie beispielsweise Operator während der Erstellung eines Canvas öffnen, kann er Ihnen relevante Schritte vorschlagen oder Anleitungen zu Canvas-Features geben, ohne dass Sie erklären müssen, an welcher Stelle Ihres Arbeitsablaufs Sie sich befinden.

Dank dieser Kontextbezogenheit können Sie kürzere, natürlichere Fragen stellen, wie beispielsweise „Wie füge ich eine Verzögerung hinzu?“ anstelle von „Wie füge ich einen Verzögerungsschritt in einen Canvas-Workflow ein?“. Sofort einsetzbare Prompts, geordnet nach Dashboard-Seite, finden Sie in der [Prompt-Bibliothek]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Arbeiten mit Operator-Antworten {#work-with-operator-responses}

### Starten Sie mit den vorgeschlagenen Prompts {#get-started-with-suggested-prompts}

Wenn Sie eine Konversation mit Operator öffnen, werden Ihnen auf Basis häufiger Aufgaben und Ihrer aktuellen Seite vorgeschlagene Prompts angezeigt. Wählen Sie einen aus, um schnell loszulegen, oder geben Sie Ihre eigene Frage ein.

### Verstehen Sie, wie Operator denkt {#understand-how-operator-thinks}

Operator zeigt seine Argumentationsschritte in ausblendbaren Abschnitten mit der Bezeichnung **Reasoned** an. Wählen Sie das Dropdown aus, um diese Abschnitte zu erweitern und nachzuvollziehen, wie Operator zu einer Antwort gelangt ist. Dies ist hilfreich, wenn Sie die Logik hinter einem Vorschlag verstehen oder den Ansatz überprüfen möchten.

![Das ausgeblendete Dropdown „Reasoned“ in einer Antwort von Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Aktionen mit Operator ausführen {#take-action-with-operator}

Operator kann direkt im Braze-Dashboard Änderungen vorschlagen und ausführen, beispielsweise Formularfelder ausfüllen, Einstellungen aktualisieren oder Inhalte generieren. Jede vorgeschlagene Änderung wird Ihnen als Aktionskarte zur Überprüfung und Genehmigung vorgelegt, bevor sie wirksam wird. Weitere Informationen zur Funktionsweise finden Sie unter [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions).

### Antworten in andere Tools kopieren {#copy-responses-to-other-tools}

Operator-Antworten sind in Markdown formatiert. Wenn Sie eine Antwort erhalten haben, wählen Sie **Copy** in der angezeigten Symbolleiste aus, um die vollständige Antwort in Ihre Zwischenablage zu kopieren. Die meisten Tools rendern Markdown nativ oder akzeptieren es mit geringfügigen Anpassungen. Wählen Sie einen Tab für Ihr Ziel aus:

{% tabs %}
{% tab Google Docs %}

Navigieren Sie zunächst zu **Tools** > **Preferences** und wählen Sie **Automatically detect Markdown** aus. Um Markdown einzufügen, navigieren Sie dann zu **Edit** > **Paste from Markdown**. Sie können auch rechtsklicken und **Paste from Markdown** auswählen.

{% endtab %}
{% tab Microsoft Word und Outlook %}

Word und Outlook rendern Markdown nicht nativ. Fügen Sie die Antwort in einen webbasierten Markdown-Previewer ein, kopieren Sie dann die gerenderte Ausgabe und fügen Sie sie mit **Keep Source Formatting** in Word oder Outlook ein. Alternativ können Sie den Text als reinen Text einfügen und manuell formatieren.

{% endtab %}
{% tab Confluence und Notion %}

Fügen Sie den Text direkt ein. Beide Plattformen rendern Markdown automatisch.

{% endtab %}
{% tab Slack %}

Fügen Sie den Text direkt ein. Slack rendert Fettschrift, Inline-Code, Code-Blöcke, Blockzitate und Aufzählungslisten, rendert jedoch keine Markdown-Überschriften oder Link-Syntax.

{% endtab %}
{% tab Andere Tools %}

Wenn Sie in einer Datei arbeiten oder Konvertierungstools verwenden möchten, können Sie auch:

- Einen Texteditor wie [VS Code](https://code.visualstudio.com/) öffnen und eine neue Textdatei erstellen, dann den Markdown-Text einfügen und die Vorschau nutzen, um die Formatierung zu überprüfen, bevor Sie ihn konvertieren oder anderswo einfügen.
- [Pandoc](https://pandoc.org/) verwenden, um Markdown in ein Word-Dokument, HTML oder PDF zu konvertieren, wenn Sie eine vorhersehbare Struktur in Word oder Outlook benötigen, ohne aus einem Browser einfügen zu müssen.

{% endtab %}
{% endtabs %}

## Ihre Sitzung verwalten {#manage-your-session}

### Eine Antwort stoppen {#stop-a-response}

Während Operator eine Antwort generiert, wird der Button **Send** zu einem Button **Stop**. Wählen Sie **Stop** aus, um die Antwort vorzeitig zu beenden, falls Sie Ihre Frage umformulieren müssen oder die Antwort in eine unerwünschte Richtung geht.

### Verlauf löschen {#clear-your-history}

Um neu zu starten oder sensible Informationen aus der Unterhaltung zu entfernen, wählen Sie **Clear chat history** aus. Dadurch werden alle aktuellen Inhalte gelöscht und der Konversationskontext zurückgesetzt.

### Feedback geben {#provide-feedback}

Verwenden Sie am Ende jeder Antwort die Daumen-hoch- oder Daumen-runter-Buttons, um schnelles Feedback zu geben. Ihr Feedback trägt dazu bei, die Antworten von Operator im Laufe der Zeit zu verbessern.

## Datenschutz und Sicherheit {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup> verfügt über eine Integration mit OpenAI, das als Unterauftragsverarbeiter von Braze fungiert und dem Datenverarbeitungszusatz (DPA) zwischen Ihnen und Braze unterliegt. Daten, die über Braze an OpenAI gesendet werden, werden nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet. Einzelheiten zur HIPAA-Konformität, Datenaufbewahrung, PII-Handhabung und Governance finden Sie unter [Datenschutz und Sicherheit]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Nächste Schritte {#next-steps}

- [Was Sie mit Operator tun können]({{site.baseurl}}/user_guide/brazeai/operator/capabilities): Entdecken Sie die Funktionen von Operator im gesamten Dashboard
- [Prompt-Bibliothek]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): Durchsuchen Sie Beispiel-Prompts, geordnet nach Dashboard-Seite
- [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Erfahren Sie, wie Sie die von Operator vorgeschlagenen Änderungen überprüfen und genehmigen können
- [Support-Tickets einreichen]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): Reichen Sie Support-Tickets direkt über Operator ein
- [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Häufige Probleme und Lösungen
- [Datenschutz und Sicherheit]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): Informationen zu HIPAA-Konformität, Datenaufbewahrung und PII-Minimierung