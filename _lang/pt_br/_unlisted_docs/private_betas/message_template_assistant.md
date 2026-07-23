---
nav_title: Modelos de e-mail HTML
article_title: Gerar modelos de e-mail HTML
permalink: "/template_assistant/"
description: "Este artigo de referência aborda como gerar modelos de e-mail HTML usando o Operator, incluindo como funciona e exemplos de prompts."
page_type: reference
---

# Gerar modelos de e-mail HTML {#generate-html-email-templates}

> Gere e itere modelos de e-mail HTML usando o Operator. Descreva o modelo que você precisa em linguagem natural, e o Operator cria ou modifica usando suas diretrizes da marca e configurações de estilo global.

{% alert important %}
A geração de modelos de e-mail HTML com o Operator está em acesso antecipado. Entre em contato com seu gerente de conta da Braze se tiver interesse em participar desse acesso antecipado.

Essa funcionalidade é compatível apenas com o canal de e-mail no editor de HTML, não em outros editores (como arrastar e soltar ou AMP).
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## Como acessar {#how-to-access}

No editor de modelos de e-mail HTML, o grupo da barra lateral **Generate** contém a opção **Template**. Selecione-a para gerar ou iterar um modelo de e-mail HTML alinhado à sua marca. O Operator aplica suas [diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) para que o resultado corresponda à sua voz e ao seu estilo.

## Como funciona {#how-it-works}

O Operator usa suas [diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) e [configurações de estilo global]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) para adaptar o conteúdo e o estilo da mensagem à sua marca.

Por exemplo, se você tiver configurações de estilo global definidas, o Operator incorpora as cores e os estilos da sua marca. Se você tiver diretrizes da marca definidas na Braze, o Operator também as consulta para criar textos no tom e na personalidade da sua marca.

O Operator também itera seu modelo para responsividade em dispositivos móveis.

## Exemplos de prompts {#example-prompts}

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}