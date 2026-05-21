---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Découvrez comment accéder à BrazeAI Operator<sup>TM</sup> et l'utiliser. Cet assistant alimenté par l'intelligence artificielle est intégré au tableau de bord de Braze. Retrouvez ses fonctionnalités et les bonnes pratiques associées."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> est un assistant alimenté par l'intelligence artificielle, intégré au tableau de bord. Operator vous aide à avancer dans vos tâches : répondre à vos questions, vous guider dans la configuration, résoudre des problèmes et générer des idées.

## Accéder à Operator {#access-operator}

Ouvrez Operator depuis n'importe quelle page du tableau de bord de Braze.

1. Sélectionnez **BrazeAI Operator<sup>TM</sup>** à côté de votre profil utilisateur.

![L'icône BrazeAI Operator à côté d'un profil utilisateur.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Le panneau de discussion d'Operator s'ouvre sur le côté droit de l'écran.

![Le panneau de discussion d'Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Agrandissez le panneau pour faciliter la lecture, ou réduisez-le pour garder Operator accessible pendant que vous travaillez.
{% endalert %}

Regardez cette vidéo pour découvrir un exemple de ce qu'Operator peut faire.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Utiliser Operator {#use-operator}

Décrivez ce que vous souhaitez accomplir en langage naturel. Vos requêtes peuvent aller de simples questions à des demandes complexes :

- **Simple :** Pourquoi mon Liquid ne s'affiche-t-il pas correctement ?
- **Complexe :** Comment puis-je faire en sorte que la balise `abort_message` de mon message inclue l'attribut utilisateur qui a provoqué l'interruption ?

Operator peut fournir des instructions étape par étape, des liens vers la documentation Braze et des explications en langage clair. Des questions claires et précises permettent d'obtenir des réponses plus utiles. Operator utilise [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), qui offre un raisonnement solide et convient aux tâches complexes en plusieurs étapes.

## Bonnes pratiques {#best-practices}

Considérez Operator comme une conversation, et non comme un moteur de recherche. Les requêtes courtes et naturelles sont les plus efficaces.

- **Soyez précis :** Au lieu de « Parlez-moi de Canvas », essayez plutôt « Comment utiliser les Parcours d'actions dans Canvas ? ».
- **Posez des questions complémentaires :** Si la première réponse ne correspond pas à votre besoin, demandez des précisions ou des informations supplémentaires.
- **Exploitez le contexte de page :** Operator identifie la page sur laquelle vous vous trouvez dans Braze. Ouvrez Operator en consultant la page concernée pour obtenir les résultats les plus pertinents.

## Personnaliser votre expérience {#customize-your-experience}

### Appliquer les directives de marque {#apply-brand-guidelines}

Ajoutez les directives de marque comme contexte à vos requêtes Operator afin que les réponses correspondent au ton, au style et à la personnalité de votre marque. Operator utilise les directives de marque configurées dans votre espace de travail, ce qui contribue à garantir la cohérence de l'envoi de messages lorsqu'il suggère des textes ou explique des fonctionnalités.

Pour configurer les directives de marque, rendez-vous dans **Paramètres** > **Directives de marque**. Pour en savoir plus, consultez [Directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/).

![Sélection des directives de marque dans le panneau de discussion d'Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Tirer parti du contexte de page {#leverage-page-aware-context}

Operator identifie automatiquement votre emplacement dans Braze et adapte ses réponses en fonction de ce contexte. Par exemple, lorsque vous ouvrez Operator pendant la création d'un Canvas, il peut vous suggérer des étapes pertinentes ou vous fournir des conseils sur les fonctionnalités de Canvas sans que vous ayez à expliquer où vous en êtes dans votre flux de travail.

Cette prise en compte du contexte vous permet de poser des questions plus courtes et plus naturelles, comme « Comment ajouter un délai ? » au lieu de « Comment ajouter une étape de délai dans un flux de travail Canvas ? ».

## Exploiter les réponses d'Operator {#work-with-operator-responses}

### Commencer avec les suggestions proposées {#get-started-with-suggested-prompts}

Lorsque vous ouvrez une conversation avec Operator, des suggestions s'affichent en fonction des tâches courantes et de la page sur laquelle vous vous trouvez. Sélectionnez-en une pour démarrer rapidement, ou saisissez votre propre question.

### Comprendre le raisonnement d'Operator {#understand-how-operator-thinks}

Operator affiche ses étapes de raisonnement dans des sections repliables intitulées **Reasoned**. Sélectionnez le menu déroulant pour développer ces sections et découvrir comment Operator a déterminé sa réponse. C'est utile lorsque vous souhaitez comprendre la logique derrière une suggestion ou vérifier l'approche adoptée.

![Le menu déroulant « Reasoned » replié dans une réponse d'Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Passer à l'action avec Operator {#take-action-with-operator}

Operator peut proposer et exécuter des modifications directement dans le tableau de bord de Braze, comme remplir des champs de formulaire, mettre à jour des paramètres ou générer du contenu. Chaque modification proposée est présentée sous forme de carte d'action que vous pouvez examiner et approuver avant qu'elle ne prenne effet. Pour en savoir plus, consultez [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

### Copier les réponses vers d'autres outils {#copy-responses-to-other-tools}

Les réponses d'Operator sont formatées en Markdown. Lorsque vous avez reçu une réponse, sélectionnez **Copy** dans la barre d'outils qui apparaît pour copier l'intégralité de la réponse dans votre presse-papiers. La plupart des outils affichent le Markdown nativement ou l'acceptent avec des ajustements mineurs. Sélectionnez un onglet correspondant à votre destination :

{% tabs %}
{% tab Google Docs %}

Commencez par aller dans **Tools** > **Preferences** et sélectionnez **Automatically detect Markdown**. Ensuite, pour coller du Markdown, allez dans **Edit** > **Paste from Markdown**. Vous pouvez également faire un clic droit et sélectionner **Paste from Markdown**.

{% endtab %}
{% tab Microsoft Word et Outlook %}

Word et Outlook n'affichent pas le Markdown nativement. Collez la réponse dans un outil de prévisualisation Markdown en ligne, puis copiez le résultat rendu et collez-le dans Word ou Outlook avec **Keep Source Formatting**. Vous pouvez également coller en texte brut et mettre en forme manuellement.

{% endtab %}
{% tab Confluence et Notion %}

Collez directement. Les deux plateformes affichent le Markdown automatiquement.

{% endtab %}
{% tab Slack %}

Collez directement. Slack affiche le gras, le code en ligne, les blocs de code, les citations et les listes à puces, mais il n'affiche pas les titres Markdown ni la syntaxe des liens.

{% endtab %}
{% tab Autres outils %}

Si vous souhaitez travailler dans un fichier ou utiliser des outils de conversion, vous pouvez également :

- Ouvrir un éditeur de texte comme [VS Code](https://code.visualstudio.com/) et créer un nouveau fichier texte, puis coller le Markdown et prévisualiser pour vérifier la mise en forme avant de le convertir ou de le coller ailleurs.
- Utiliser [Pandoc](https://pandoc.org/) pour convertir le Markdown en document Word, HTML ou PDF lorsque vous avez besoin d'une structure prévisible dans Word ou Outlook sans passer par un navigateur.

{% endtab %}
{% endtabs %}

## Gérer votre session {#manage-your-session}

### Interrompre une réponse {#stop-a-response}

Pendant qu'Operator génère une réponse, le bouton **Send** devient un bouton **Stop**. Sélectionnez **Stop** pour mettre fin à la réponse si vous devez reformuler votre question ou si la réponse ne va pas dans la bonne direction.

### Effacer votre historique {#clear-your-history}

Pour repartir de zéro ou supprimer des informations sensibles de la conversation, sélectionnez **Clear chat history**. Cela supprime tout le contenu actuel et réinitialise le contexte de la conversation.

### Donner votre avis {#provide-feedback}

Au bas de chaque réponse, utilisez les boutons « pouce vers le haut » ou « pouce vers le bas » pour fournir un retour rapide. Vos retours contribuent à améliorer les réponses d'Operator au fil du temps.

## Confidentialité et sécurité des données {#data-privacy-and-security}

### Fournisseurs de modèles en tant que sous-traitants ou fournisseurs tiers {#model-providers-as-sub-processors-or-third-party-providers}

Lorsque vous utilisez une intégration avec un fournisseur LLM fourni par Braze via les services Braze (« LLM fourni par Braze »), les fournisseurs dudit LLM fourni par Braze agissent en tant que sous-traitants de Braze, sous réserve des conditions de l'Addendum relatif au traitement des données (DPA) conclu entre vous et Braze. BrazeAI Operator<sup>TM</sup> s'intègre avec OpenAI.

### Utilisation des données avec OpenAI {#how-data-is-used-with-openai}

Afin de générer des résultats d'intelligence artificielle grâce aux fonctionnalités BrazeAI qui exploitent OpenAI (« Résultats »), Braze transmettra certaines informations (« Données d'entrée ») à OpenAI. Les données d'entrée comprennent vos requêtes, le contenu affiché dans le tableau de bord et les données de l'espace de travail pertinentes pour vos demandes. Conformément aux [engagements de la plateforme API d'OpenAI](https://openai.com/enterprise-privacy/), les données transmises à l'API d'OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer les modèles d'OpenAI. Entre vous et Braze, les Résultats constituent votre propriété intellectuelle. Braze ne fera valoir aucun droit d'auteur sur ces Résultats. Braze n'offre aucune garantie de quelque nature que ce soit concernant tout contenu généré par l'intelligence artificielle, y compris les Résultats.

## Étapes suivantes {#next-steps}

- [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) : Découvrez comment examiner et approuver les modifications proposées par Operator.
- [Créer des tickets d'assistance]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/) : Créez des tickets d'assistance directement depuis Operator.
- [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) : Consultez les problèmes courants et leurs solutions.