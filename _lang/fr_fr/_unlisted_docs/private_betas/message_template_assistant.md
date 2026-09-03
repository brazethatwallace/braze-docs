---
nav_title: Modèles d'e-mail HTML
article_title: Générer des modèles d'e-mail HTML
permalink: "/template_assistant/"
description: "Cet article de référence explique comment générer des modèles d'e-mail HTML à l'aide d'Operator, y compris son fonctionnement et des exemples de prompts."
page_type: reference
---

# Générer des modèles d'e-mail HTML {#generate-html-email-templates}

> Générez et itérez sur des modèles d'e-mail HTML à l'aide d'Operator. Décrivez le modèle dont vous avez besoin en langage naturel, et Operator le crée ou le modifie en utilisant vos directives de marque et vos paramètres de style globaux.

{% alert important %}
La génération de modèles d'e-mail HTML avec Operator est en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.

Cette fonctionnalité n'est prise en charge que pour le canal e-mail dans l'éditeur HTML, pas dans les autres éditeurs (tels que le glisser-déposer ou AMP).
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## Comment y accéder {#how-to-access}

Dans l'éditeur de modèles d'e-mail HTML, le groupe latéral **Générer** contient l'option **Modèle**. Sélectionnez-la pour générer ou itérer sur un modèle d'e-mail HTML conforme à votre marque. Operator applique vos [directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) afin que le résultat corresponde à votre ton et à votre style.

## Fonctionnement {#how-it-works}

Operator utilise vos [directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) et vos [paramètres de style globaux]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) pour adapter le contenu et le style du message à votre marque.

Par exemple, si vous avez configuré des paramètres de style globaux, Operator intègre les couleurs et les styles de votre marque. Si vous avez défini des directives de marque dans Braze, Operator s'en sert également pour créer des textes qui reflètent le ton et la personnalité de votre marque.

Operator optimise aussi votre modèle pour le rendre adapté aux appareils mobiles (responsive).

## Exemples de prompts {#example-prompts}

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}