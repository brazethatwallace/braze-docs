---
nav_title: Markenrichtlinien
article_title: Markenrichtlinien
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Markenrichtlinien erstellen, verwalten und als Kontext für Operator und Agents hinzufügen."
---

# Markenrichtlinien {#brand-guidelines}

> Passen Sie den Stil Ihrer KI-generierten Texte mit personalisierten Markenrichtlinien an die Stimme, den Ton und die Persönlichkeit Ihrer Marke an.

Erstellen und verwalten Sie Markenrichtlinien unter **Content** > **Brand Guidelines**.

## Markenrichtlinien erstellen {#creating-brand-guidelines}

### Schritt 1: Markenrichtlinie erstellen {#step-1-create-a-brand-guideline}

Wählen Sie auf der Seite **Brand Guidelines** die Option **Create new** aus. Wenn diese Markenrichtlinie die Standardrichtlinie für den Workspace sein soll, wählen Sie **Use as default brand guideline** aus. Sie können eine Standardrichtlinie pro Workspace festlegen.

### Schritt 2: Markenpersönlichkeit beschreiben {#step-2-describe-your-brand-personality}

Überlegen Sie bei **Brand personality**, was Ihre Marke einzigartig macht. Fügen Sie Eigenschaften, Werte, Stimme und Archetypen hinzu, die Ihre Marke definieren. Beschränken Sie dieses Feld auf maximal 10.000 Zeichen. Wenn Sie diesen Text mit einem LLM generieren, geben Sie dieses Zeichenlimit in Ihrem Prompt an, damit die Ausgabe in das Feld passt.

Hier sind einige Merkmale, die Sie berücksichtigen sollten:

| Merkmal | Definition | Beispiel |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputation | Wie Ihre Marke am Markt wahrgenommen werden soll. | Wir sind dafür bekannt, die zuverlässigste und kundenorientierteste Marke in unserer Branche zu sein. |
| Persönlichkeitsmerkmale | Menschenähnliche Eigenschaften, die den Charakter Ihrer Marke beschreiben. | Unsere Marke ist freundlich, nahbar und stets gut gelaunt. |
| Werte | Zentrale Werte, die die Handlungen und Entscheidungen Ihrer Marke leiten. | Wir legen Wert auf Nachhaltigkeit, Transparenz und Community. |
| Differenzierung | Einzigartige Qualitäten, die Ihre Marke von der Konkurrenz abheben. | Wir heben uns durch einen personalisierten Kundenservice ab, der die Extrameile geht. |
| Markenstimme | Ton und Stil der Kommunikation, die Ihre Marke verwendet. | Unsere Stimme ist locker und dennoch informativ, klar ohne zu förmlich zu sein. |
| Markenarchetyp | Der Archetyp, der die Persona Ihrer Marke repräsentiert (der Held, der Schöpfer usw.). | Wir verkörpern den Archetyp „Entdecker“ und suchen stets nach neuen Herausforderungen und Abenteuern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Markenpersönlichkeit beschreiben" }

### Schritt 3: Sprache definieren, die vermieden werden soll (optional) {#step-3-define-language-that-should-be-avoided-optional}

Listen Sie unter **Exclusions** Sprache oder Stilmittel auf, die nicht zu Ihrer Marke passen. Beispielsweise möchten Sie vielleicht „Sarkasmus“, „negative Haltungen“ oder „herablassende“ Töne vermeiden. Beschränken Sie dieses Feld auf maximal 300 Zeichen.

![Das Fenster „Create brand guideline“ mit Feldern zur Eingabe von Name, Beschreibung, Persönlichkeit, Ausschlüssen und Tonalität.]({% image_buster /assets/img/guidelines_create.png %})

### Schritt 4: Richtlinien testen {#step-4-test-your-guidelines}

Testen Sie Ihre Richtlinien, um zu sehen, wie sie funktionieren. Erweitern Sie **Test your guidelines**, um Beispieltexte zu generieren und bei Bedarf anzupassen.

### Schritt 5: Richtlinien speichern {#step-5-save-your-guidelines}

Wenn Sie mit Ihren Richtlinien zufrieden sind, wählen Sie **Save brand guideline** aus. Ihre Richtlinien werden in Ihrem Workspace für die zukünftige Verwendung gespeichert.

{% alert important %}
Sie können die Ausgabesprache unabhängig davon ändern, in welcher Sprache Ihr Text verfasst ist. Allerdings garantieren weder Braze noch OpenAI die Qualität der Übersetzung. Testen und überprüfen Sie Übersetzungen immer, bevor Sie sie verwenden.
{% endalert %}

## Brand-Richtlinien verwalten {#managing-brand-guidelines}

Sie können Brand-Richtlinien bearbeiten, indem Sie sie auf der Seite **Brand Guidelines** auswählen. Archivieren Sie eine Brand-Richtlinie, um sie inaktiv und in Nachrichten-Editoren nicht verfügbar zu machen. Um sie wieder aktiv und auswählbar zu machen, können Sie nach archivierten Brand-Richtlinien filtern und die Archivierung aufheben.

## Nutzung von Markenrichtlinien {#using-brand-guidelines}

Wählen Sie im Operator-Chat-Panel <i class="fa-regular fa-plus"></i>&nbsp;**Kontext für Operator hinzufügen** und dann eine oder mehrere Richtlinien unter **Brand guidelines** aus. Operator wendet die ausgewählten Richtlinien auf generierte Texte, Templates und Bilder an. Standardmäßig ist nichts ausgewählt.

![Auswahl von Markenrichtlinien im Operator-Chat-Panel.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

Wenn Sie einen Agenten konfigurieren, wählen Sie unter [Kontext hinzufügen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources) Markenrichtlinien aus, damit der Agent diesem Stil und dieser Tonalität folgt. Die Agent Console wählt automatisch den Workspace-Standard für Sie aus.

{% multi_lang_include brazeai/generative_ai/policy.md %}