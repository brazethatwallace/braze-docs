---
nav_title: Markenrichtlinien
article_title: KI-generierte Markenrichtlinien
page_order: 2.2
description: "Dieser Referenzartikel behandelt die Markenrichtlinien für den KI-Texterstellungsassistenten, ein Feature, mit dem Sie den Stil der vom KI-Texterstellungsassistenten generierten Texte an die Stimme und den Stil Ihrer Marke anpassen können."
---

# Markenrichtlinien mit BrazeAI generieren

> Passen Sie den Stil Ihrer KI-generierten Texte mit personalisierten Markenrichtlinien an die Stimme und Persönlichkeit Ihrer Marke an.

## Markenrichtlinien generieren {#steps}

Folgen Sie diesen Schritten, um Markenrichtlinien im KI-Texterstellungsassistenten zu erstellen. Sie können Markenrichtlinien auch auf der Einstellungsseite für [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) erstellen.

### Schritt 1: Markenrichtlinie erstellen

1. Suchen und wählen Sie in Ihrem Nachrichten-Editor <i class="fa-solid fa-wand-magic-sparkles" title="KI-Texter"></i>, um [den KI-Texterstellungsassistenten zu öffnen]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/#access).
2. Wählen Sie **Markenrichtlinie anwenden** und dann **Markenrichtlinie erstellen**.

![Dropdown-Menü für „Markenrichtlinien anwenden“ erweitert mit dem Button „Markenrichtlinie erstellen“ im Fokus.]({% image_buster /assets/img/ai_copywriter/create_brand_guideline_button.png %}){:style="max-width:75%"}

{: start="3"}

3. Geben Sie einen Namen für diese Richtlinie ein. Dieser wird als Bezeichnung in der vorherigen Auswahl angezeigt.
4. Fügen Sie bei **Wann werden Sie diese Markenrichtlinien verwenden?** Details hinzu, um Ihren Kolleg:innen (und Ihrem zukünftigen Ich) den Kontext für die Verwendung dieser Richtlinie zu erläutern.
5. Wenn Sie möchten, dass dies die Standard-Markenrichtlinie für den aktuellen Workspace ist, markieren Sie **Als Standard-Markenrichtlinie verwenden**.

![Ansicht zur Erstellung von Markenrichtlinien.]({% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} "Brand Guidelines")

### Schritt 2: Beschreiben Sie Ihre Markenpersönlichkeit

Überlegen Sie bei der **Markenpersönlichkeit**, was Ihre Marke einzigartig macht. Fügen Sie Merkmale, Werte, Sprachstil und alle Archetypen hinzu, die Ihre Marke definieren. Hier sind einige Merkmale, die Sie beachten sollten:

| **Charakteristik**       | **Definition**                                                                       | **Beispiel**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputation               | Wie Ihre Marke auf dem Markt wahrgenommen werden soll.                               | Wir sind dafür bekannt, die zuverlässigste und kundenorientierteste Marke in unserer Branche zu sein. |
| Persönlichkeitsmerkmale       | Menschenähnliche Eigenschaften, die den Charakter Ihrer Marke beschreiben.                     | Unsere Marke ist freundlich, sympathisch und immer optimistisch.          |
| Werte                   | Zentrale Werte, die das Handeln und die Entscheidungen Ihrer Marke leiten.                           | Wir legen Wert auf Nachhaltigkeit, Transparenz und Gemeinschaft.            |
| Differenzierung          | Einzigartige Eigenschaften, die Ihre Marke von der Konkurrenz abheben.                         | Wir zeichnen uns durch einen personalisierten Kundenservice aus, der weit über das übliche Maß hinausgeht. |
| Sprachstil der Marke              | Der Ton und der Stil der Kommunikation, die Ihre Marke verwendet.                                 | Unser Ton ist leger und doch informativ und sorgt für Klarheit, ohne zu förmlich zu sein. |
| Archetyp der Marke          | Der Archetyp, der die Persona Ihrer Marke repräsentiert (Der Held, Der Schöpfer usw.).    | Wir verkörpern den Archetyp des „Entdeckers“, der immer auf der Suche nach neuen Herausforderungen und Abenteuern ist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 3: Sprache definieren, die vermieden werden sollte (optional)

Listen Sie unter **Ausschlüsse** alle Formulierungen oder Stile auf, die nicht zu Ihrer Marke passen. Zum Beispiel möchten Sie vielleicht „Sarkasmus“, „negative Haltungen“ oder einen „herablassenden“ Ton vermeiden.

### Schritt 4: Richtlinien testen

Testen Sie Ihre Richtlinien, um zu sehen, wie sie funktionieren. Erweitern Sie **Richtlinien testen**, um Beispieltexte zu generieren und bei Bedarf anzupassen.

![Testen der Markenrichtlinien mit einer Aktion zum Frühjahrsverkauf für E-Mail-Betreffzeilen.]({% image_buster /assets/img/ai_copywriter/test_brand_guidelines.png %})

### Schritt 5: Richtlinien speichern

Wenn Sie mit Ihren Richtlinien zufrieden sind, wählen Sie **Markenrichtlinie speichern**. Ihre neuen Richtlinien werden in Ihrem Workspace zur späteren Verwendung gespeichert.

{% alert important %}
Sie können die Ausgabesprache unabhängig von der Sprache Ihres Textes ändern, aber weder Braze noch OpenAI garantieren die Qualität der Übersetzung. Testen und überprüfen Sie Übersetzungen immer, bevor Sie sie verwenden.
{% endalert %}

## Bestehende Richtlinien bearbeiten

So bearbeiten Sie Ihre bestehenden Markenrichtlinien:

1. Öffnen Sie den KI-Texterstellungsassistenten.
2. Wenden Sie die Markenrichtlinien an, die Sie ändern möchten. In der Nähe des Feldes wird ein Button angezeigt.
3. Wählen Sie **Richtlinie bearbeiten**.

{% multi_lang_include brazeai/generative_ai/policy.md %}