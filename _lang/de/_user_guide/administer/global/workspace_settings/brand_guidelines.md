---
nav_title: Markenrichtlinien
article_title: Markenrichtlinien
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Markenrichtlinien erstellen, verwalten und verwenden, die Operator beim Generieren von Texten, Templates und Bildern anwendet."
---

# Markenrichtlinien {#brand-guidelines}

> Passen Sie den Stil Ihrer KI-generierten Texte mit personalisierten Markenrichtlinien an die Stimme, den Ton und die Persönlichkeit Ihrer Marke an.

Erstellen und verwalten Sie Markenrichtlinien unter **Content** > **Brand Guidelines**.

## Markenrichtlinien erstellen {#creating-brand-guidelines}

### Schritt 1: Markenrichtlinie erstellen {#step-1-create-a-brand-guideline}

Wählen Sie auf der Seite **Brand Guidelines** die Option **Create new** aus. Wenn diese Markenrichtlinie als Standard für den Workspace verwendet werden soll, wählen Sie **Use as default brand guideline** aus. Sie können einen Standard pro Workspace festlegen.

### Schritt 2: Markenpersönlichkeit beschreiben {#step-2-describe-your-brand-personality}

Überlegen Sie unter **Brand personality**, was Ihre Marke einzigartig macht. Fügen Sie Eigenschaften, Werte, Stimme und Archetypen hinzu, die Ihre Marke definieren. Beschränken Sie dieses Feld auf maximal 10.000 Zeichen. Wenn Sie diesen Text mit einem LLM generieren, geben Sie dieses Zeichenlimit in Ihrem Prompt an, damit die Ausgabe in das Feld passt.

Hier sind einige Merkmale, die Sie berücksichtigen sollten:

| Merkmal | Definition | Beispiel |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputation | Wie Ihre Marke auf dem Markt wahrgenommen werden soll. | Wir sind dafür bekannt, die zuverlässigste und kund:innenorientierteste Marke in unserer Branche zu sein. |
| Persönlichkeitsmerkmale | Menschenähnliche Eigenschaften, die den Charakter Ihrer Marke beschreiben. | Unsere Marke ist freundlich, zugänglich und stets optimistisch. |
| Werte | Zentrale Werte, die die Handlungen und Entscheidungen Ihrer Marke leiten. | Wir schätzen Nachhaltigkeit, Transparenz und Community. |
| Differenzierung | Einzigartige Qualitäten, die Ihre Marke von der Konkurrenz abheben. | Wir heben uns durch personalisierten Kundenservice ab, der weit über das Übliche hinausgeht. |
| Markenstimme | Der Ton und Stil der Kommunikation, den Ihre Marke verwendet. | Unsere Stimme ist ungezwungen und dennoch informativ – klar, ohne zu formell zu sein. |
| Markenarchetyp | Der Archetyp, der die Persona Ihrer Marke repräsentiert (der Held, der Schöpfer usw.). | Wir verkörpern den Archetyp des „Entdeckers“, immer auf der Suche nach neuen Herausforderungen und Abenteuern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2: Markenpersönlichkeit beschreiben" }

### Schritt 3: Zu vermeidende Sprache definieren (optional) {#step-3-define-language-that-should-be-avoided-optional}

Listen Sie unter **Exclusions** Ausdrucksweisen oder Stile auf, die nicht zu Ihrer Marke passen. Beispielsweise möchten Sie möglicherweise „Sarkasmus“, „negative Einstellungen“ oder „herablassende“ Töne vermeiden. Beschränken Sie dieses Feld auf maximal 300 Zeichen.

![Das Fenster „Create brand guideline“ mit Feldern zur Eingabe von Name, Beschreibung, Persönlichkeit, Ausschlüssen und Tonalität.]({% image_buster /assets/img/guidelines_create.png %})

### Schritt 4: Richtlinien testen {#step-4-test-your-guidelines}

Testen Sie Ihre Richtlinien, um zu sehen, wie sie sich bewähren. Erweitern Sie **Test your guidelines**, um Beispieltexte zu generieren, und passen Sie sie bei Bedarf an.

### Schritt 5: Richtlinien speichern {#step-5-save-your-guidelines}

Wenn Sie mit Ihren Richtlinien zufrieden sind, wählen Sie **Save brand guideline** aus. Ihre Richtlinien werden in Ihrem Workspace zur zukünftigen Verwendung gespeichert.

{% alert important %}
Sie können die Ausgabesprache unabhängig davon ändern, in welcher Sprache Ihr Text verfasst ist. Weder Braze noch OpenAI garantieren jedoch die Qualität der Übersetzung. Testen und überprüfen Sie Übersetzungen immer, bevor Sie sie verwenden.
{% endalert %}

## Verwalten von Markenrichtlinien {#managing-brand-guidelines}

Sie können Markenrichtlinien bearbeiten, indem Sie sie auf der Seite **Brand Guidelines** auswählen. Archivieren Sie eine Markenrichtlinie, um sie inaktiv zu machen und in Nachrichten-Editoren nicht mehr verfügbar zu haben. Um sie wieder aktiv und auswählbar zu machen, können Sie nach archivierten Markenrichtlinien filtern und die Archivierung dann aufheben.

## Markenrichtlinien verwenden {#using-brand-guidelines}

Öffnen Sie beim Verfassen einer Nachricht den Operator, um [Text zu generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy), und wählen Sie Ihre Markenrichtlinie im Dropdown-Menü **Markenrichtlinie anwenden** aus. Wenn Sie eine bestimmte Markenrichtlinie als Standard festlegen, wählt Braze diese automatisch im Dropdown-Menü aus. Sie können jedoch eine andere Richtlinie auswählen.

![Operator mit „Important Alerts!!“ als ausgewählter Markenrichtlinie.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}