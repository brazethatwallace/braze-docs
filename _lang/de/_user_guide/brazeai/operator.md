---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Erfahren Sie, wie Sie auf BrazeAI Operator<sup>TM</sup> zugreifen und diesen nutzen können, einen in das Braze-Dashboard integrierten KI-gestützten Assistenten, einschließlich seiner Features und Best Practices."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> ist ein KI-gestützter Assistent, der in das Dashboard integriert ist. Operator unterstützt Sie beim Erstellen – beim Entwerfen von Campaigns, Canvases, Segmenten und Inhalten – und hilft Ihnen, wenn Sie nicht weiterkommen, indem er Fragen beantwortet, bei der Fehlerbehebung unterstützt und gemeinsam mit Ihnen Ideen entwickelt.

## Auf Operator zugreifen {#access-operator}

Öffnen Sie Operator von jeder Seite im Braze-Dashboard aus.

1. Wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Nutzerprofil aus.
2. Das Operator-Chat-Panel öffnet sich in einem Seitenpanel.

![Das Operator-Chat-Panel.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximieren Sie das Panel für leichteres Lesen, oder minimieren Sie es, um Operator beim Arbeiten verfügbar zu halten.
{% endalert %}

## Operator verwenden {#use-operator}

Beschreiben Sie in natürlicher Sprache, was Sie erreichen möchten. Klare und spezifische Prompts führen zu hilfreicheren Antworten. Prompts können von einer einzelnen Frage bis hin zu einer vollständigen Build-Anfrage reichen:

- **Eine Frage stellen:** Warum wird mein Liquid nicht gerendert?
- **Etwas erstellen:** Erstelle ein Segment von Nutzer:innen, die in den letzten 7 Tagen ihren Warenkorb abgebrochen haben.

Operator kann Schritt-für-Schritt-Anleitungen, Links zur Braze-Dokumentation, verständliche Erklärungen sowie Entwürfe von Campaigns, Canvases, Segmenten und Inhalten bereitstellen, die Sie überprüfen und direkt in Ihre Arbeit einfügen können. Wie Operator Änderungen vorschlägt und anwendet, erfahren Sie unter [Mit Operator Aktionen ausführen](#take-action-with-operator).

Operator verwendet [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), das für komplexe, mehrstufige Aufgaben geeignet ist. Die vollständige Übersicht darüber, was Operator Ihnen beim Erstellen helfen kann, finden Sie unter [Was Sie mit Operator tun können]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Fertige Beispiele finden Sie in der [Prompt-Bibliothek]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

Sehen Sie sich dieses Video an, um ein Beispiel dafür zu sehen, was Operator leisten kann.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Best Practices {#best-practices}

Behandeln Sie Operator wie ein Gespräch, nicht wie eine Suchmaschine. Kurze, natürliche Prompts funktionieren am besten.

- **Seien Sie konkret:** Statt „Erzähl mir etwas über Canvas“ versuchen Sie „Wie verwende ich Aktionspfade in Canvas?“.
- **Stellen Sie Folgefragen:** Wenn die erste Antwort nicht Ihrem Bedarf entspricht, bitten Sie um Klarstellung oder zusätzliche Details. Operator merkt sich frühere Nachrichten im Gespräch, bis Sie Ihren Chatverlauf löschen.
- **Nutzen Sie den seitenabhängigen Kontext:** Operator versteht, wo Sie sich in Braze befinden. Öffnen Sie Operator, während Sie die relevante Seite ansehen, um die genauesten Ergebnisse zu erhalten.

## Erlebnis anpassen {#customize-your-experience}

### Markenrichtlinien anwenden {#apply-brand-guidelines}

Fügen Sie Markenrichtlinien als Kontext zu Operator-Anfragen hinzu, damit die Antworten zur Stimme, zum Ton und zur Persönlichkeit Ihrer Marke passen. Operator verwendet die in Ihrem Workspace konfigurierten Markenrichtlinien, was eine konsistente Kommunikation sicherstellt, wenn es Texte vorschlägt oder Features erklärt.

Um Markenrichtlinien einzurichten, gehen Sie zu **Inhalt** > **Markenrichtlinien**. Weitere Informationen finden Sie unter [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines).

![Auswahl von Markenrichtlinien im Operator-Chat-Panel.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Seitenabhängigen Kontext nutzen {#leverage-page-aware-context}

Operator erkennt automatisch, wo Sie sich in Braze befinden, und passt die Antworten entsprechend an. Wenn Sie Operator beispielsweise beim Erstellen eines Canvas öffnen, kann es relevante Schritte vorschlagen oder Hinweise zu Canvas-Features geben, ohne dass Sie erklären müssen, an welcher Stelle Ihres Workflows Sie sich befinden.

Dank dieses Kontextbewusstseins können Sie kurze, natürliche Prompts verwenden, um mit Operator zu interagieren, wie z. B. „Aktualisiere meine Editor-Einstellungen, damit sie meinen Markenrichtlinien entsprechen.“ Wenn Ihre Anfrage einen anderen Bereich des Dashboards erfordert, kann Operator Sie [direkt dorthin navigieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard).


Fertige Prompt-Ideen finden Sie in der [Prompt-Bibliothek]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Mit Operator-Antworten arbeiten {#work-with-operator-responses}

### Mit vorgeschlagenen Prompts starten {#get-started-with-suggested-prompts}

Wenn Sie ein Gespräch mit Operator öffnen, erscheinen vorgeschlagene Prompts basierend auf häufigen Aufgaben und Ihrer aktuellen Seite. Wählen Sie einen aus, um schnell loszulegen, oder geben Sie Ihre eigene Frage ein.

### Verstehen, wie Operator denkt {#understand-how-operator-thinks}

Operator zeigt seine Überlegungsschritte in einklappbaren Abschnitten mit der Bezeichnung **Reasoned** an. Wählen Sie das Dropdown aus, um diese Abschnitte aufzuklappen und zu sehen, wie Operator eine Antwort ermittelt hat. Das ist hilfreich, wenn Sie die Logik hinter einem Vorschlag nachvollziehen oder den Ansatz überprüfen möchten.

![Das eingeklappte „Reasoned“-Dropdown in einer Operator-Antwort.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Mit Operator Aktionen ausführen {#take-action-with-operator}

Operator kann Änderungen direkt im Braze-Dashboard vorschlagen und ausführen, z. B. Formularfelder ausfüllen, Einstellungen aktualisieren, Inhalte generieren oder Sie zu einer anderen Seite navigieren, um Ihre Anfrage abzuschließen. Jede vorgeschlagene Änderung wird als Aktionskarte dargestellt, die Sie überprüfen und genehmigen können, bevor sie wirksam wird. Weitere Informationen zur Funktionsweise finden Sie unter [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions).

### Antworten in andere Tools kopieren {#copy-responses-to-other-tools}

Operator-Antworten sind in Markdown formatiert. Wenn Sie eine Antwort erhalten haben, wählen Sie **Copy** in der angezeigten Symbolleiste, um die vollständige Antwort in Ihre Zwischenablage zu kopieren. Die meisten Tools rendern Markdown nativ oder akzeptieren es mit geringfügigen Anpassungen. Wählen Sie einen Tab für Ihr Ziel aus:

{% tabs %}
{% tab Google Docs %}

Gehen Sie zunächst zu **Tools** > **Preferences** und wählen Sie **Automatically detect Markdown** aus. Um Markdown einzufügen, gehen Sie dann zu **Edit** > **Paste from Markdown**. Sie können auch mit der rechten Maustaste klicken und **Paste from Markdown** auswählen.

{% endtab %}
{% tab Microsoft Word und Outlook %}

Word und Outlook rendern Markdown nicht nativ. Fügen Sie die Antwort in einen webbasierten Markdown-Previewer ein, kopieren Sie dann die gerenderte Ausgabe und fügen Sie sie in Word oder Outlook mit **Quellformatierung beibehalten** ein. Alternativ können Sie als reinen Text einfügen und manuell formatieren.

{% endtab %}
{% tab Confluence und Notion %}

Direkt einfügen. Beide Plattformen rendern Markdown automatisch.

{% endtab %}
{% tab Slack %}

Direkt einfügen. Slack rendert Fettschrift, Inline-Code, Code-Blöcke, Zitate und Aufzählungslisten, aber keine Markdown-Überschriften oder Link-Syntax.

{% endtab %}
{% tab Andere Tools %}

Wenn Sie in einer Datei arbeiten oder Konvertierungstools verwenden möchten, können Sie auch:

- Einen Texteditor wie [VS Code](https://code.visualstudio.com/) öffnen und eine neue Textdatei erstellen, dann das Markdown einfügen und die Vorschau nutzen, um die Formatierung zu prüfen, bevor Sie es konvertieren oder anderswo einfügen.
- [Pandoc](https://pandoc.org/) verwenden, um Markdown in ein Word-Dokument, HTML oder PDF zu konvertieren, wenn Sie eine vorhersagbare Struktur in Word oder Outlook benötigen, ohne aus einem Browser einzufügen.

{% endtab %}
{% endtabs %}

## Sitzung verwalten {#manage-your-session}

### Antwort stoppen {#stop-a-response}

Während Operator eine Antwort generiert, wird der **Senden**-Button zu einem **Stopp**-Button. Wählen Sie **Stopp**, um die Antwort vorzeitig zu beenden, wenn Sie Ihre Frage umformulieren möchten oder die Antwort in die falsche Richtung geht.

### Verlauf löschen {#clear-your-history}

Um neu zu beginnen oder sensible Informationen aus dem Gespräch zu entfernen, wählen Sie **Chatverlauf löschen**. Dadurch werden alle aktuellen Inhalte entfernt und der Gesprächskontext zurückgesetzt.

### Feedback geben {#provide-feedback}

Am Ende jeder Antwort können Sie über die Daumen-hoch- oder Daumen-runter-Buttons schnelles Feedback geben. Ihr Feedback hilft dabei, die Antworten von Operator im Laufe der Zeit zu verbessern.

## Datenschutz und Sicherheit {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup> ist mit OpenAI integriert, das als Unterauftragsverarbeiter von Braze dem Datenverarbeitungsvertrag (DPA) zwischen Ihnen und Braze unterliegt. Daten, die über Braze an OpenAI gesendet werden, werden nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet. Einzelheiten zu HIPAA-Konformität, Datenaufbewahrung, PII-Handhabung und Governance finden Sie unter [Datenschutz und Sicherheit]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Nächste Schritte {#next-steps}

- [Was Sie mit Operator tun können]({{site.baseurl}}/user_guide/brazeai/operator/capabilities): Durchsuchen Sie die Funktionen von Operator im gesamten Dashboard
- [Prompt-Bibliothek]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library): Durchsuchen Sie Beispiel-Prompts, organisiert nach Dashboard-Seite
- [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions): Erfahren Sie, wie Sie vorgeschlagene Änderungen von Operator überprüfen und genehmigen
- [Support-Tickets erstellen]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets): Erstellen Sie Support-Tickets direkt aus Operator
- [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting): Referenz für häufige Probleme und Lösungen
- [Datenschutz und Sicherheit]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security): Informieren Sie sich über HIPAA-Konformität, Datenaufbewahrung und PII-Minimierung