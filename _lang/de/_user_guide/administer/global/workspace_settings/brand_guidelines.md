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

### 1. Schritt: Markenrichtlinie erstellen {#step-1-create-a-brand-guideline}

Wählen Sie auf der Seite **Brand Guidelines** die Option **Create new** aus. Wenn Sie möchten, dass diese Markenrichtlinie der Standard für den Workspace ist, markieren Sie **Use as default brand guideline**. Sie können einen Standard pro Workspace haben.

### 2. Schritt: Beschreiben Sie Ihre Markenpersönlichkeit {#step-2-describe-your-brand-personality}

Überlegen Sie bei der **Brand personality**, was Ihre Marke einzigartig macht. Fügen Sie Merkmale, Werte, Sprachstil und alle Archetypen hinzu, die Ihre Marke definieren. Hier sind einige Merkmale, die Sie beachten sollten:

| **Merkmal** | **Definition** | **Beispiel** |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputation | Wie Ihre Marke auf dem Markt wahrgenommen werden soll. | Wir sind dafür bekannt, die zuverlässigste und kundenorientierteste Marke in unserer Branche zu sein. |
| Persönlichkeitsmerkmale | Menschenähnliche Eigenschaften, die den Charakter Ihrer Marke beschreiben. | Unsere Marke ist freundlich, zugänglich und stets positiv. |
| Werte | Zentrale Werte, die die Handlungen und Entscheidungen Ihrer Marke leiten. | Wir schätzen Nachhaltigkeit, Transparenz und Gemeinschaft. |
| Differenzierung | Einzigartige Qualitäten, die Ihre Marke von der Konkurrenz abheben. | Wir heben uns durch personalisierten Kundenservice ab, der über das Erwartete hinausgeht. |
| Markenstimme | Der Ton und Stil der Kommunikation, den Ihre Marke verwendet. | Unsere Stimme ist locker und dennoch informativ – klar, ohne zu förmlich zu sein. |
| Markenarchetyp | Der Archetyp, der die Persona Ihrer Marke repräsentiert (Der Held, Der Schöpfer usw.). | Wir verkörpern den Archetyp des „Entdeckers“, der stets neue Herausforderungen und Abenteuer sucht. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2. Schritt: Beschreiben Sie Ihre Markenpersönlichkeit" }

### 3. Schritt: Sprache definieren, die vermieden werden soll (optional) {#step-3-define-language-that-should-be-avoided-optional}

Listen Sie unter **Exclusions** alle Formulierungen oder Stile auf, die nicht zu Ihrer Marke passen. Beispielsweise möchten Sie vielleicht „Sarkasmus“, „negative Einstellungen“ oder „herablassende“ Töne vermeiden.

![Das Fenster „Markenrichtlinie erstellen“ mit Feldern für Name, Beschreibung, Persönlichkeit, Ausschlüsse und Ton.]({% image_buster /assets/img/guidelines_create.png %})

### 4. Schritt: Ihre Richtlinien testen {#step-4-test-your-guidelines}

Testen Sie Ihre Richtlinien, um zu sehen, wie sie funktionieren. Erweitern Sie **Test your guidelines**, um Beispieltexte zu generieren, und passen Sie diese bei Bedarf an.

### 5. Schritt: Ihre Richtlinien speichern {#step-5-save-your-guidelines}

Wenn Sie mit Ihren Richtlinien zufrieden sind, wählen Sie **Save brand guideline**. Ihre Richtlinien werden in Ihrem Workspace für die zukünftige Verwendung gespeichert.

{% alert important %}
Sie können die Ausgabesprache unabhängig von der Sprache Ihres Textes ändern, aber weder Braze noch OpenAI garantieren die Qualität der Übersetzung. Testen und überprüfen Sie Übersetzungen immer, bevor Sie sie verwenden.
{% endalert %}

## Markenrichtlinien verwalten {#managing-brand-guidelines}

Sie können Markenrichtlinien bearbeiten, indem Sie sie auf der Seite **Brand Guidelines** auswählen. Archivieren Sie eine Markenrichtlinie, um sie zu deaktivieren und in Nachrichten-Editoren nicht mehr verfügbar zu machen. Um sie wieder aktiv und auswählbar zu machen, können Sie nach archivierten Markenrichtlinien filtern und sie dann dearchivieren.

![Die Seite „Markenrichtlinien“ mit Filter für archivierte Markenrichtlinien.]({% image_buster /assets/img/unarchive_brand_guideline.png %})

## Markenrichtlinien verwenden {#using-brand-guidelines}

Öffnen Sie beim Verfassen einer Nachricht Operator, um [Texte zu generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy), und wählen Sie Ihre Markenrichtlinie im Dropdown-Menü **Apply brand guideline** aus. Wenn Sie eine bestimmte Markenrichtlinie als Standard festlegen, wählt Braze sie automatisch im Dropdown-Menü aus, aber Sie können eine andere Richtlinie wählen.

![Operator mit „Important Alerts!!“ als ausgewählter Markenrichtlinie.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}