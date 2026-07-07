---
nav_title: Plantillas de correo electrónico HTML
article_title: Generar plantillas de correo electrónico HTML
permalink: "/template_assistant/"
description: "Este artículo de referencia explica cómo generar plantillas de correo electrónico HTML con Operator, incluyendo cómo funciona y ejemplos de prompts."
page_type: reference
---

# Generar plantillas de correo electrónico HTML {#generate-html-email-templates}

> Genera e itera plantillas de correo electrónico HTML con Operator. Describe la plantilla que necesitas en lenguaje natural, y Operator la crea o modifica utilizando tus directrices de marca y la configuración de estilo global.

{% alert important %}
La generación de plantillas de correo electrónico HTML con Operator se encuentra en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en este acceso anticipado.

Esta funcionalidad solo es compatible con el canal de correo electrónico en el editor HTML, no en otros editores (como arrastrar y soltar o AMP).
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## Cómo acceder {#how-to-access}

{% multi_lang_include brazeai/generative_ai/access_html_template.md %}

## Cómo funciona {#how-it-works}

Operator utiliza tus [directrices de marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) y la [configuración de estilo global]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/) para adaptar el contenido y el estilo del mensaje a tu marca.

Por ejemplo, si tienes configurados los ajustes de estilo global, Operator incorpora los colores y estilos de tu marca. Si tienes directrices de marca definidas en Braze, Operator también hace referencia a ellas para crear textos con el tono y la personalidad de tu marca.

Operator también itera tu plantilla para optimizar su adaptación a dispositivos móviles.

## Ejemplos de prompts {#example-prompts}

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}