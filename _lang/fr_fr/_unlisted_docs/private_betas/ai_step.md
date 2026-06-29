---
nav_title: Étape IA
article_title: Étape IA
permalink: /ai_step/
description: "Cet article de référence couvre l'étape IA de Canvas."
tool:
  - Canvas
hidden: true
---

# Étape IA {#ai-step}

> L'étape IA dans Canvas exploite ChatGPT pour automatiser le marketing personnalisé en interprétant les entrées générées par les utilisateurs (comme les retours de sondages), en déterminant la réponse appropriée et en déclenchant des messages, le tout dans Braze. ChatGPT est alimenté par OpenAI, un fournisseur tiers.

{% alert note %}
L'étape IA est actuellement disponible en tant que fonctionnalité bêta. Contactez votre gestionnaire de la satisfaction client si vous souhaitez participer à cette version bêta.
{% endalert %}

## Créer une étape IA {#create-ai-step}

1. Ajoutez une nouvelle étape à votre Canvas et sélectionnez **Étape IA**. <br><br>![Étape IA dans le générateur Canvas][1]{: style="max-width: 30%;"}<br><br>
2. Créez un prompt qui indique à l'IA comment répondre aux différentes actions des utilisateurs. Les réponses peuvent inclure la mise à jour d'un attribut personnalisé ou l'envoi d'un message. Ce prompt peut utiliser Liquid pour attribuer différentes sorties de réponse en fonction de différents attributs ou entrées utilisateur. <br><br>Pour attribuer des sorties qui peuvent ensuite être utilisées pour personnaliser les futurs messages au sein du même Canvas, créez un prompt qui enregistre des variables avec des noms spécifiques (par exemple, « message » et « sentiment score »). <br><br> ![Exemple de prompt IA utilisé dans les paramètres de l'étape IA pour envoyer un message personnalisé basé sur un score de sentiment généré. Cet exemple est décrit dans la section « Réponses de sentiment client ».][2] <br><br>
3. Utilisez l'onglet **Prévisualisation** pour tester ce que l'IA pourrait produire pour des utilisateurs spécifiques.<br><br> ![L'onglet Prévisualisation des paramètres de l'étape IA montrant un message personnalisé généré par l'IA pour trois paramètres : un prénom Cameron, un nom de produit chaussures, et le texte « correct mais mon lacet s'est déjà cassé »][3]

## Référencer la sortie de l'IA avec Liquid {#referencing-ai-output-using-liquid}

Référencez la sortie de l'IA dans les étapes suivantes en insérant la logique Liquid `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`. Vous pouvez définir le `key_name` dans le prompt de l'étape IA.

Par exemple, si vous utilisez les variables « message » et « sentiment score », vous pouvez utiliser `{% raw %}{{ai_step_output.${message}}}{% endraw %}` pour personnaliser un message ultérieur dans ce même Canvas.

Vous pouvez également enregistrer la sortie de n'importe quelle étape IA en tant qu'attribut personnalisé en utilisant l'étape Canvas Mise à jour utilisateur, où vous lisez la sortie de l'étape IA (par exemple, `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). Si la sortie n'est pas stockée en tant qu'attribut personnalisé, elle ne peut pas être utilisée ailleurs que dans les étapes suivantes du même Canvas.

### Utiliser les étapes Contexte {#using-context-steps}

Vous pouvez exploiter les [étapes Contexte de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) pour référencer facilement les sorties plus tard dans votre Canvas.

Voici un exemple d'étape Contexte que vous pourriez configurer après votre étape IA. Dans cet exemple, une étape IA précédente contient les sorties de l'étape IA pour le score de sentiment et le message, et cette étape Contexte crée les variables `sentiment_score` et `message`, qui peuvent être utilisées dans les étapes suivantes.

![Étape Contexte avec les deux variables : « sentiment_score » et « message ».][6]

Vous pourriez également créer une étape Parcours d'audience qui envoie les utilisateurs dans différents parcours en fonction de la valeur de leurs variables de contexte. Dans cet exemple, vous pourriez cibler les utilisateurs différemment en fonction de leur score de sentiment. Vous pouvez aussi utiliser Liquid pour intégrer la variable message dans le corps d'un e-mail en insérant la variable avec {% raw %}`{{context.${message}}}`{% endraw %}.

![Une étape Parcours d'audience avec un groupe d'audience nommé « Groupe 1 » avec le filtre « sentiment_score est supérieur à 80 ».][7]

## Indicateurs de l'étape IA {#ai-step-metrics}

Les étapes IA disposent des indicateurs suivants au niveau de l'étape :

| Indicateur | Description |
| _A avancé à l'étape suivante_ | Nombre d'utilisateurs qui ont avancé vers la ou les étapes suivantes dans le Canvas |
| _A quitté le Canvas_ | Nombre d'utilisateurs qui ont quitté le Canvas si votre étape IA était la dernière étape |
| _Sortie réussie_ | Nombre d'utilisateurs pour lesquels l'étape IA a généré une sortie avec succès |
| _Sortie échouée_ | Nombre d'utilisateurs pour lesquels l'étape IA n'a pas réussi à générer une sortie ; dans ce cas, les utilisateurs avanceront tout de même vers les étapes suivantes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comprendre les sorties de votre étape IA {#understanding-your-ai-step-outputs}

Il existe quelques scénarios dans lesquels Braze écartera la sortie de l'étape IA et enverra le client à l'étape suivante :

- Si la sortie dépasse 1 024 caractères
- Si la sortie n'est pas au format JSON
- Si le prompt ne respecte pas les exigences de [modération](https://platform.openai.com/docs/guides/moderation/overview) d'OpenAI, qui signale le contenu inapproprié généré par les utilisateurs

## Cas d'utilisation de l'étape IA {#ai-step-use-cases}

### Réponses de sentiment client {#customer-sentiment-responses}

Comme démontré par l'exemple dans [Créer une étape IA](#create-ai-step), vous pouvez demander à l'IA d'envoyer des messages de suivi basés sur les scores de sentiment générés à partir des retours clients.

- **Scores de sentiment positifs :** déclencher une notification push qui demande aux utilisateurs de laisser un avis
- **Scores de sentiment moyens :** déclencher un e-mail qui demande aux utilisateurs s'ils souhaitent une aide supplémentaire
- **Scores de sentiment faibles :** déclencher un webhook qui notifie le service d'assistance utilisateur afin qu'un conseiller puisse rédiger un suivi nuancé

#### Exemple de prompt IA {#example-ai-prompt}

Cet exemple a été utilisé dans [Créer une étape IA](#create-ai-step).

Un client a acheté « `{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}` » et a donné le retour produit suivant : « `{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}` ». Créez un score de sentiment sous forme d'entier entre 0 et 100. Puis créez un message personnalisé. Cela devrait retourner deux variables, « message » et « sentiment score ».

### Suivis de sondages {#survey-follow-ups}

Si vous exécutez un sondage in-app ou dans le navigateur avec une section de réponse libre, vous pouvez utiliser les étapes IA pour analyser les réponses libres et effectuer un suivi approprié.

Par exemple, si un détaillant de maquillage a un sondage demandant « Quels produits souhaitez-vous nominer pour les prix beauté de cette année ? », il pourrait utiliser un prompt qui identifie et attribue un attribut pour les types de produits et marques préférés de l'utilisateur, puis personnaliser le contenu futur en fonction de ces données.

#### Exemple de prompt IA

Identifiez la marque préférée de l'utilisateur à partir de sa réponse. Puis créez un message qui remercie les utilisateurs d'avoir rempli le sondage et mentionne comment les experts beauté adorent également leur marque préférée. Cela devrait retourner deux variables, « message » et « marque préférée ».

![L'onglet Prévisualisation des paramètres de l'étape IA montrant un message personnalisé généré par l'IA pour le paramètre de réponse au sondage « J'adore les crèmes pour le visage de Beauty Brand » qui remercie l'utilisateur d'avoir rempli le sondage puis recommande une crème pour le visage.][4]

### Recommandations basées sur le comportement {#behavior-driven-recommendations}

Les clients peuvent demander à l'IA d'analyser les comportements des utilisateurs et d'envoyer des messages de recommandation.

Par exemple, vous pouvez créer un prompt pour analyser les 50 achats les plus récents des utilisateurs et définir leur catégorie la plus fréquemment achetée comme nouvel attribut personnalisé. Ensuite, vous pouvez envoyer des recommandations par e-mail personnalisées pour la catégorie préférée de chaque utilisateur.

#### Exemple de prompt IA

Un client a acheté les produits suivants : « `{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}` ». Identifiez la catégorie de produit la plus achetée par l'utilisateur. Cela devrait retourner une nouvelle variable pour « catégorie la plus achetée ».

![L'onglet Prévisualisation des paramètres de l'étape IA montrant la variable générée par l'IA « livre » pour le paramètre de catégorie la plus achetée.][5]

## Limites de débit {#rate-limits}

Il y a une limite de 10 requêtes par minute (RPM) par société. Cela signifie que pour toute étape IA, jusqu'à 10 utilisateurs peuvent recevoir cette étape au cours d'une minute donnée et tout utilisateur au-delà des 10 avancera automatiquement à l'étape suivante. Lorsque la minute suivante commence, les utilisateurs peuvent à nouveau recevoir l'étape IA, mais les utilisateurs précédents ayant déclenché la limite de débit ne seront pas réessayés.

## Limitations de l'étape IA {#ai-step-limitations}

- Cette fonctionnalité exploite GPT-3.5.
- Cette fonctionnalité utilise la clé API OpenAI de Braze. Vous ne pouvez pas utiliser votre propre clé API OpenAI.
- Il y a une limite de 5 requêtes par minute (RPM) par espace de travail et 10 RPM par société.
- Cette fonctionnalité n'est pas conforme HIPAA et les clients ne doivent pas envoyer d'informations personnellement identifiables (PII) ou d'informations de santé protégées (PHI).

## Comment mes données sont-elles utilisées et envoyées à OpenAI ? {#how-is-my-data-used-and-sent-to-openai}

Afin de générer une sortie IA via les fonctionnalités d'intelligence artificielle de Braze que Braze identifie comme exploitant OpenAI (« Sortie »), Braze enverra votre prompt, tel que le contenu du message, le sentiment de l'utilisateur final, les directives de marque, les données de campagnes passées, ou toute autre entrée, selon le cas (« Entrée ») à [OpenAI](https://openai.com/). Si des données personnelles sont envoyées à OpenAI lorsque vous utilisez l'intégration ChatGPT de Braze avec l'étape IA, OpenAI agira en tant que sous-traitant de Braze, tel que défini dans le DPA entre vous et Braze. Si vous intégrez votre propre modèle de langage (LLM) avec l'étape IA, tout fournisseur de ce LLM sera considéré comme un fournisseur tiers et le traitement de toute donnée personnelle sera soumis aux conditions entre vous et ce fournisseur tiers. Conformément aux [engagements de la plateforme API d'OpenAI](https://openai.com/enterprise-privacy/), les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer les modèles OpenAI et seront supprimées après 30 jours par OpenAI de leurs systèmes. Entre vous et Braze, la Sortie est votre propriété intellectuelle. Braze ne revendiquera aucun droit d'auteur sur cette Sortie. Braze ne fournit aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'IA en général, y compris la Sortie.

[1]: {% image_buster /assets/unlisted_docs/img/ai_step1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/ai_step2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/ai_step3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/ai_step4.png %}
[5]: {% image_buster /assets/unlisted_docs/img/ai_step5.png %}
[6]: {% image_buster /assets/unlisted_docs/img/ai_step6.png %}
[7]: {% image_buster /assets/unlisted_docs/img/ai_step7.png %}