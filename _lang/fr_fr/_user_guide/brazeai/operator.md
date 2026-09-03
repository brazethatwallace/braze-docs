---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Découvrez comment accéder à BrazeAI Operator<sup>TM</sup> et l'utiliser. Cet assistant alimenté par l'intelligence artificielle est intégré au tableau de bord de Braze. Retrouvez ses fonctionnalités et les bonnes pratiques associées."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> est un assistant alimenté par l'intelligence artificielle, intégré au tableau de bord. Operator vous aide à créer — en rédigeant des Campaigns, des Canvas, des Segments et du contenu — et vous aide à avancer, que ce soit pour répondre à vos questions, résoudre des problèmes ou générer des idées.

## Accéder à Operator {#access-operator}

Ouvrez Operator depuis n'importe quelle page du tableau de bord de Braze.

1. Sélectionnez **BrazeAI Operator<sup>TM</sup>** à côté de votre profil utilisateur.
2. Le panneau de conversation Operator s'ouvre dans un panneau latéral.

![Le panneau de conversation Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Agrandissez le panneau pour faciliter la lecture, ou réduisez-le pour garder Operator disponible pendant que vous travaillez.
{% endalert %}

## Utiliser Operator {#use-operator}

Décrivez ce que vous souhaitez accomplir en langage naturel. Des prompts clairs et précis produisent des réponses plus utiles. Vos prompts peuvent aller d'une simple question à une demande de création complète :

- **Poser une question :** Pourquoi mon Liquid ne s'affiche-t-il pas ?
- **Créer quelque chose :** Crée un Segment d'utilisateurs ayant abandonné leur panier au cours des 7 derniers jours.

Operator peut fournir des instructions étape par étape, des liens vers la documentation Braze, des explications en langage clair, ainsi que des ébauches de Campaigns, de Canvas, de Segments et de contenu que vous pouvez examiner et insérer directement dans votre travail. Pour en savoir plus sur la façon dont Operator propose et applique les modifications, consultez [Agir avec Operator](#take-action-with-operator).

Operator utilise [GPT-5.6 Terra](https://developers.openai.com/api/docs/models/gpt-5.6-terra), adapté aux tâches complexes et multi-étapes. Pour découvrir l'ensemble des possibilités offertes par Operator, consultez [Ce que vous pouvez faire avec Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Pour des exemples prêts à l'emploi, consultez la [bibliothèque de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

Regardez cette vidéo pour découvrir un exemple de ce qu'Operator peut faire.

{% multi_lang_include video.html id="lnv9t8hn11" source="wistia" %}

## Bonnes pratiques {#best-practices}

Considérez Operator comme une conversation, pas comme un moteur de recherche. Des prompts courts et naturels fonctionnent le mieux.

- **Soyez précis :** au lieu de « Parlez-moi de Canvas », essayez « Comment utiliser les parcours d'action dans Canvas ? ».
- **Posez des questions de suivi :** si la première réponse ne correspond pas à votre besoin, demandez des précisions ou des détails supplémentaires. Operator se souvient des messages précédents dans la conversation jusqu'à ce que vous effaciez votre historique de conversation.
- **Tirez parti du contexte lié à la page :** Operator comprend votre emplacement dans Braze. Ouvrez Operator en consultant la page pertinente pour obtenir les résultats les plus précis.

## Personnaliser votre expérience {#customize-your-experience}

### Appliquer des directives de marque {#apply-brand-guidelines}

Ajoutez des directives de marque comme contexte pour qu'Operator puisse correspondre à la voix, au ton et à la personnalité de votre marque lorsqu'il suggère du texte ou explique des fonctionnalités.

1. Sélectionnez <i class="fa-regular fa-plus"></i>&nbsp;**Ajouter du contexte pour Operator** dans le panneau de conversation.
2. Sous **Directives de marque**, sélectionnez une ou plusieurs directives.

Operator applique uniquement les directives que vous sélectionnez. Rien n'est sélectionné par défaut, y compris la valeur par défaut de l'espace de travail.

Lorsque vous ouvrez Operator depuis **Générer avec Operator** ou **Affiner avec Operator** dans la console d'agent, Operator attache la directive déjà présente sur l'agent comme contexte. Vous pouvez ajouter ou supprimer des directives depuis le même menu.

Pour configurer des directives de marque, accédez à **Contenu** > **Directives de marque**. Pour en savoir plus, consultez [Directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines).

![Sélection de directives de marque dans le panneau de conversation d'Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Tirer parti du contexte lié à la page {#leverage-page-aware-context}

Operator comprend automatiquement votre emplacement dans Braze et adapte ses réponses en fonction de ce contexte. Par exemple, lorsque vous ouvrez Operator pendant la création d'un Canvas, il peut suggérer des étapes pertinentes ou fournir des conseils sur les fonctionnalités de Canvas sans que vous ayez à expliquer où vous en êtes dans votre flux de travail.

Cette connaissance du contexte signifie que vous pouvez utiliser des prompts courts et naturels pour interagir avec Operator, comme « Mets à jour les paramètres de mon éditeur pour correspondre à mes directives de marque. » Lorsque votre demande nécessite une autre partie du tableau de bord, Operator peut [vous y diriger]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) directement.


Pour des idées de prompts prêtes à l'emploi, consultez la [bibliothèque de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library).

## Travailler avec les réponses d'Operator {#work-with-operator-responses}

### Commencer avec les prompts suggérés {#get-started-with-suggested-prompts}

Lorsque vous ouvrez une conversation avec Operator, des prompts suggérés apparaissent en fonction des tâches courantes et de votre page actuelle. Sélectionnez-en un pour commencer rapidement, ou saisissez votre propre question personnalisée.

### Comprendre le raisonnement d'Operator {#understand-how-operator-thinks}

Operator affiche ses étapes de raisonnement dans des sections réductibles intitulées **Reasoned**. Sélectionnez le menu déroulant pour développer ces sections et voir comment Operator a déterminé une réponse. Cela est utile lorsque vous souhaitez comprendre la logique derrière une suggestion ou vérifier l'approche utilisée.

![Le menu déroulant « Reasoned » réduit dans une réponse d'Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Agir avec Operator {#take-action-with-operator}

Operator peut proposer et exécuter des modifications directement dans le tableau de bord de Braze, comme remplir des champs de formulaire, mettre à jour des paramètres, générer du contenu ou vous rediriger vers une autre page pour traiter votre demande. Chaque modification proposée est présentée sous forme de carte d'action que vous pouvez examiner et approuver avant qu'elle ne prenne effet. Pour en savoir plus sur ce fonctionnement, consultez [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions).

### Copier les réponses vers d'autres outils {#copy-responses-to-other-tools}

Les réponses d'Operator sont formatées en Markdown. Lorsque vous avez reçu une réponse, sélectionnez **Copy** dans la barre d'outils qui apparaît pour copier la réponse complète dans votre presse-papiers. La plupart des outils affichent le Markdown nativement ou l'acceptent avec des ajustements mineurs. Sélectionnez un onglet correspondant à votre destination :

{% tabs %}
{% tab Google Docs %}

D'abord, accédez à **Tools** > **Preferences** et sélectionnez **Automatically detect Markdown**. Ensuite, pour coller du Markdown, accédez à **Edit** > **Paste from Markdown**. Vous pouvez également faire un clic droit et sélectionner **Paste from Markdown**.

{% endtab %}
{% tab Microsoft Word et Outlook %}

Word et Outlook n'affichent pas le Markdown nativement. Collez la réponse dans un visualiseur Markdown en ligne, puis copiez le résultat rendu et collez-le dans Word ou Outlook avec **Conserver la mise en forme source**. Vous pouvez également coller en texte brut et formater manuellement.

{% endtab %}
{% tab Confluence et Notion %}

Collez directement. Les deux plateformes affichent le Markdown automatiquement.

{% endtab %}
{% tab Slack %}

Collez directement. Slack affiche le gras, le code en ligne, les blocs de code, les citations et les listes à puces, mais il n'affiche pas les titres Markdown ni la syntaxe des liens.

{% endtab %}
{% tab Autres outils %}

Si vous souhaitez travailler dans un fichier ou utiliser des outils de conversion, vous pouvez également :

- Ouvrir un éditeur de texte comme [VS Code](https://code.visualstudio.com/) et créer un nouveau fichier texte, puis coller le Markdown et prévisualiser pour vérifier le formatage avant de le convertir ou de le coller ailleurs.
- Utiliser [Pandoc](https://pandoc.org/) pour convertir le Markdown en document Word, HTML ou PDF lorsque vous avez besoin d'une structure prévisible dans Word ou Outlook sans passer par un collage depuis un navigateur.

{% endtab %}
{% endtabs %}

## Gérer votre session {#manage-your-session}

### Arrêter une réponse {#stop-a-response}

Pendant qu'Operator génère une réponse, le bouton **Envoyer** devient un bouton **Stop**. Sélectionnez **Stop** pour mettre fin à la réponse prématurément si vous devez reformuler votre question ou si la réponse va dans la mauvaise direction.

### Effacer votre historique {#clear-your-history}

Pour repartir de zéro ou supprimer des informations sensibles de la conversation, sélectionnez **Clear chat history**. Cela supprime tout le contenu actuel et réinitialise le contexte de la conversation.

### Donner votre avis {#provide-feedback}

En bas de chaque réponse, utilisez les boutons pouce en haut ou pouce en bas pour donner un retour rapide. Vos retours contribuent à améliorer les réponses d'Operator au fil du temps.

## Confidentialité et sécurité des données {#data-privacy-and-security}

BrazeAI Operator<sup>TM</sup> s'intègre à OpenAI, qui agit en tant que sous-traitant de Braze soumis à l'accord de traitement des données (DPA) entre vous et Braze. Les données envoyées à OpenAI via Braze ne sont pas utilisées pour entraîner ou améliorer les modèles d'OpenAI. Pour en savoir plus sur la conformité HIPAA, la conservation des données, le traitement des données d'identification et la gouvernance, consultez [Confidentialité et sécurité des données]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security).

## Étapes suivantes {#next-steps}

- [Ce que vous pouvez faire avec Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) : Parcourez les fonctionnalités d'Operator dans le tableau de bord
- [Bibliothèque de prompts]({{site.baseurl}}/user_guide/brazeai/operator/prompt_library) : Parcourez des exemples de prompts organisés par page du tableau de bord
- [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions) : Découvrez comment examiner et approuver les modifications proposées par Operator
- [Soumettre des tickets d'assistance]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets) : Soumettez des tickets d'assistance directement depuis Operator
- [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting) : Consultez les problèmes courants et leurs solutions
- [Confidentialité et sécurité des données]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security) : Consultez les informations sur la conformité HIPAA, la conservation des données et la minimisation des données d'identification