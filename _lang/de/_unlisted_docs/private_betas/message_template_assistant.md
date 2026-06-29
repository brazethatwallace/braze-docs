---
nav_title: HTML-E-Mail-Templates
article_title: HTML-E-Mail-Templates generieren
permalink: "/template_assistant/"
description: "Dieser Referenzartikel beschreibt, wie Sie HTML-E-Mail-Templates mit Operator generieren, einschließlich der Funktionsweise und Beispiel-Prompts."
page_type: reference
---

# HTML-E-Mail-Templates generieren {#generate-html-email-templates}

> Generieren und iterieren Sie HTML-E-Mail-Templates mit Operator. Beschreiben Sie das gewünschte Template in natürlicher Sprache, und Operator erstellt oder modifiziert es anhand Ihrer Markenrichtlinien und globalen Stileinstellungen.

{% alert important %}
Die Generierung von HTML-E-Mail-Templates mit Operator befindet sich im Early Access. Kontaktieren Sie Ihren Account Manager, wenn Sie an diesem Early Access teilnehmen möchten.

Diese Funktionalität wird nur für den E-Mail-Kanal im HTML-Editor unterstützt, nicht in anderen Editoren (wie Drag-and-Drop oder AMP).
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## Zugriff {#how-to-access}

{% multi_lang_include brazeai/generative_ai/access_html_template.md %}

## Funktionsweise {#how-it-works}

Operator verwendet Ihre [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) und [globalen Stileinstellungen]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/), um den Nachrichteninhalt und -stil an Ihre Marke anzupassen.

Wenn Sie beispielsweise globale Stileinstellungen eingerichtet haben, bezieht Operator die Farben und Stile Ihrer Marke ein. Wenn Sie Markenrichtlinien in Braze definiert haben, referenziert Operator diese ebenfalls, um Texte im Ton und in der Persönlichkeit Ihrer Marke zu erstellen.

Operator optimiert Ihr Template außerdem für mobile Responsivität.

## Beispiel-Prompts {#example-prompts}

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}