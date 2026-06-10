---
nav_title: Assistant de modèle de message
article_title: Assistant de modèle de message
permalink: "/template_assistant/"
description: "Cet article de référence explique comment utiliser l'assistant de modèle de message pour générer des modèles pour vos e-mails."
page_type: reference
---

# Assistant de modèle de message {#message-template-assistant}

> L'assistant de modèle de message vous aide à itérer sur un modèle d'e-mail HTML existant en utilisant l'intelligence artificielle générative pour créer des modèles adaptés à vos besoins spécifiques. Cette fonctionnalité peut vous aider à optimiser votre contenu pour un cas d'utilisation, une audience ou une conversion spécifique, et à réduire le temps et les efforts nécessaires à la composition de vos e-mails.

{% alert important %}
L'assistant de modèle de message est en accès anticipé. Contactez votre gestionnaire de la satisfaction client si vous souhaitez participer à cet accès anticipé. <br><br>Cette fonctionnalité n'est actuellement prise en charge que pour le canal e-mail et uniquement dans l'éditeur HTML, pas dans les autres éditeurs (tels que le glisser-déposer ou AMP).
{% endalert %}

## Comment ça fonctionne {#how-it-works}

L'assistant de modèle de message utilise vos [directives de marque](https://www.braze.com/docs/user_guide/administrative/app_settings/brand_guidelines) et vos [paramètres de style globaux](https://www.braze.com/docs/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) pour adapter le contenu et le style du message à votre marque.

Par exemple, si vous avez configuré des paramètres de style globaux, l'assistant de modèle de message intégrera les couleurs et les styles de votre marque. Si vous avez défini des directives de marque dans Braze, l'assistant peut également s'y référer pour créer du contenu dans le ton et la personnalité de votre marque.

L'assistant de modèle de message peut se souvenir de l'historique de votre conversation uniquement lorsque vous êtes encore dans la même fenêtre de chat. Cela signifie qu'il peut faire référence à des prompts précédents pour en générer de nouveaux. L'assistant essaiera également d'adapter votre modèle pour qu'il soit responsive sur mobile.

Par exemple, si vous passez d'un prompt spécifiquement lié à une marque de fitness à une marque générique dans vos prompts suivants, l'assistant de modèle de message peut indiquer dans le modèle qu'il s'agit de cette même marque de fitness. Pour démarrer une nouvelle conversation, sélectionnez **Effacer l'historique** dans la fenêtre de chat et ouvrez à nouveau l'assistant de modèle de message.

## Créer un modèle {#creating-a-template}

1. Dans le tableau de bord, allez dans **Modèles** > **Modèles d'e-mail**.
2. Sélectionnez un modèle d'e-mail existant.
3. Dans la section **Créer avec l'IA** de l'éditeur HTML, sélectionnez **Modèle**.
4. À partir de là, vous pouvez saisir différents prompts ou poser des questions sur votre contenu.
5. L'assistant de modèle de message fournira une réponse et déterminera les modifications nécessaires à votre modèle.
6. Sélectionnez **Générer** pour appliquer les suggestions.

{% alert important %}
Nous vous recommandons vivement de tester le résultat généré pour vous assurer qu'il correspond à votre message.
{% endalert %}

![Un exemple de prompt pour créer un modèle avec plusieurs sections à utiliser pour plusieurs e-mails. L'assistant de modèle de message explique les modifications apportées au modèle actuel.]({% image_buster /assets/unlisted_docs/img/ai_message_template_assistant1.png %}){: style="width:70%;"}

### Exemples de prompts {#example-prompts}

Voici quelques exemples de prompts pour vous aider à démarrer :

- Ajouter un sondage de satisfaction en bas de l'e-mail
- Changer la police en {% raw %}`{{font name}}` et la taille de police du paragraphe en taille `{{number}}`{% endraw %}
- Arrondir les coins de toutes les images
- Ajouter une autre section avec une image et un appel à l'action

{% alert note %}
Selon votre prompt et la réponse, l'assistant de modèle de message peut ajouter des images de substitution lors de la génération du nouveau modèle.
{% endalert %}