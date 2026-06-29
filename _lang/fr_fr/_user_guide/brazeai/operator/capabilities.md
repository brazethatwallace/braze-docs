---
nav_title: Fonctionnalités
article_title: Ce que vous pouvez faire avec Operator
page_order: 6
page_type: reference
toc_headers: h2
description: "Cet article de référence couvre les tâches d'intelligence artificielle disponibles via BrazeAI Operator™, notamment la rédaction, le Liquid, la génération d'images, le code de transformation des données et la vérification de contenu."
---

# Ce que vous pouvez faire avec Operator {#operator-capabilities}

> Les fonctionnalités d'intelligence artificielle auparavant disponibles en tant qu'assistants autonomes sont désormais accessibles via [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/). Comme Operator est intégré au tableau de bord et comprend votre espace de travail (vos directives de marque, attributs, contenu connecté et la page sur laquelle vous travaillez), les résultats sont plus contextuels que ce que les assistants précédents pouvaient produire.

Au lieu d'ouvrir un outil différent pour chaque tâche, décrivez ce que vous souhaitez en langage naturel et Operator s'en charge dans le contexte. Vous pouvez également animer la conversation en demandant un ton différent, une version plus courte ou une traduction, sans repartir de zéro. Operator peut aussi proposer et exécuter des modifications directement via des [cartes d'action]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) que vous vérifiez avant leur application.

## Conditions préalables {#prerequisites}

Operator dispose des mêmes autorisations que vous, de sorte que certaines actions nécessitent l'autorisation correspondante pour cette surface. Par exemple, la génération d'une image nécessite l'autorisation *Modifier les ressources de la bibliothèque multimédia*. Si vous ne voyez pas de point d'entrée, vérifiez vos autorisations auprès de votre administrateur. Pour en savoir plus, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions).

## Ce qui est disponible via Operator {#whats-available-through-operator}

Tous les points d'entrée existants restent en place, vos flux de travail ne sont donc pas affectés. Ces expériences sont désormais alimentées par Operator. Le tableau suivant fait correspondre chaque ancien assistant autonome à son emplacement actuel.

| Ancien assistant | Ce qu'il faisait | Où le trouver maintenant |
| --- | --- | --- |
| AI Copywriter | Générait du texte marketing à partir d'un nom ou d'une description de produit | Une nouvelle icône **Ask Operator** dans les éditeurs SMS, push, e-mail HTML et Canvas |
| AI Liquid Assistant | Générait du Liquid pour la personnalisation | Une nouvelle icône **Ask Operator** dans les éditeurs SMS, push, e-mail HTML et Canvas |
| AI Image Generator | Générait des images à partir d'une description textuelle pour la bibliothèque multimédia | Un nouveau bouton **Générer avec Operator** dans la bibliothèque multimédia |
| Data Transformations AI Copilot | Générait du code de transformation | Le bouton **Insérer le code** sur la page Transformation des données |
| Vérification de contenu | Vérifiait le contenu pour l'orthographe, la grammaire, le ton, le langage offensant et le code résiduel | Le bouton **Vérifier avec Operator** dans l'onglet **Test** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ce qui est disponible via Operator" }

## Appliquer les directives de marque {#apply-brand-guidelines}

Operator utilise les directives de marque configurées dans votre espace de travail afin que le texte, les modèles et les images générés correspondent à la voix, au ton et au style de votre marque. Pour configurer les directives de marque, accédez à **Contenu** > **Directives de marque**. Pour en savoir plus, consultez [Directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/). Pour plus de détails sur l'application des directives de marque avec Operator, consultez [Appliquer les directives de marque]({{site.baseurl}}/user_guide/brazeai/operator/#apply-brand-guidelines).

## Générer du texte {#generate-copy}

Vous pouvez utiliser Operator pour réfléchir ou générer du texte depuis n'importe où, mais vous obtiendrez la meilleure expérience en l'utilisant directement dans l'éditeur de messages, où il peut travailler à vos côtés sur le message que vous construisez. Décrivez votre produit ou votre campagne, et Operator renvoie un texte que vous pouvez vérifier et insérer.

Operator améliore le rédacteur autonome de plusieurs façons :

- Il applique automatiquement vos [directives de marque](#apply-brand-guidelines) lorsqu'elles sont configurées.
- Il utilise le [contexte de la page]({{site.baseurl}}/user_guide/brazeai/operator/#leverage-page-aware-context), vous n'avez donc pas besoin de re-décrire le canal ou le message sur lequel vous travaillez. Grâce à cette connaissance de la page, vous pouvez également l'utiliser pour modifier ou affiner un message existant au lieu d'en générer un de zéro.
- Il peut consulter vos [attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) et événements, ce qui vous permet de lui demander de personnaliser les recommandations de texte avec du vrai Liquid.
- Vous pouvez animer la conversation et itérer. Par exemple, demandez un ton différent, une version plus courte ou une traduction.

### Tons {#generate-copy-tones}

Le ton du texte généré est déterminé par votre prompt. Décrivez le style souhaité — par exemple, formel, décontracté, urgent ou accrocheur — et Operator ajuste sa production en conséquence. Vous pouvez également affiner le ton dans des prompts de suivi, par exemple en demandant une version plus détendue ou plus soignée. Lorsque les [directives de marque](#apply-brand-guidelines) sont configurées, Operator les applique automatiquement pour que le texte reste cohérent avec la voix de votre marque.

### Exemples de prompts {#generate-copy-example-prompts}

{% include copy_block.html content="Write a short, eye-catching push notification announcing our summer sale." %}

{% include copy_block.html content="Rewrite this subject line in a more casual tone." %}

{% include copy_block.html content="Translate this copy into Spanish." %}

## Générer du Liquid {#generate-liquid}

Dans n'importe quel éditeur de messages, ouvrez Operator pour générer et affiner du Liquid pour la personnalisation. Operator comprend la [syntaxe Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/), vos attributs standard et [personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), ainsi que le [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), et il peut expliquer ce que fait le code.

### Où générer du Liquid {#generate-liquid-supported-channels}

Comme pour la rédaction, vous pouvez demander à Operator de générer du Liquid depuis n'importe où, et cela fonctionne sur tous les canaux et éditeurs de messages. Vous obtiendrez les meilleurs résultats depuis un éditeur de messages, où Operator dispose du contexte complet du message que vous construisez.

### Fonctionnalités Liquid {#generate-liquid-attributes}

Operator est très performant avec Liquid. Il peut générer une logique Liquid complexe basée sur les données de votre espace de travail — y compris la consultation des données de [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/) pour trouver des exemples de valeurs — et il peut vérifier et expliquer le Liquid existant dans vos campagnes.

### Bonnes pratiques {#generate-liquid-best-practices}

#### Utilisez le langage naturel {#generate-liquid-use-natural-language}

Operator est entraîné pour comprendre le langage naturel. Discutez avec lui comme vous le feriez avec un collègue lorsque vous demandez de l'aide. Cela aide Operator à comprendre vos besoins et à fournir une assistance précise.

#### Donnez du contexte {#generate-liquid-give-context}

Fournir du contexte aide Operator à comprendre la vue d'ensemble de votre projet. Il est utile d'inclure des informations telles que :

- Le nom et le secteur d'activité de votre entreprise
- La campagne sur laquelle vous travaillez, comme le Black Friday ou les soldes de fin d'année
- Votre objectif, comme augmenter votre taux de clics
- Les attributs personnalisés spécifiques que vous souhaitez inclure dans votre message

Inclure du contexte dans votre prompt aide Operator à adapter ses réponses pour mieux répondre à vos besoins. Vous pouvez également inclure des détails de votre campagne, de votre brief de message ou de votre document de brainstorming pour mettre Operator au courant.

#### Soyez précis {#generate-liquid-be-specific}

Operator peut poser des questions de suivi, mais fournir des détails dès le départ peut conduire à des résultats plus précis plus rapidement. Pensez à inclure des détails tels que :

- Toute préférence ou exigence connue pour le message
- Des instructions sur la façon de gérer certaines situations, comme l'absence de réponse du destinataire du message ou les options de message de secours
- Des valeurs exactes ou similaires pour les attributs personnalisés que vous souhaitez utiliser, ce qui aide Operator à générer et tester une logique plus précise
- Lorsque vous demandez du Liquid utilisant du contenu connecté, la documentation de l'endpoint API, un exemple de réponse API, ou les deux

#### Faites preuve de créativité {#generate-liquid-get-creative}

Essayez différents prompts pour voir comment Operator peut améliorer vos messages. Expérimentez avec différents prompts et idées, car la créativité peut conduire à des résultats plus engageants.

### Exemples de prompts {#generate-liquid-example-prompts}

{% tabs local %}
{% tab À propos de Liquid %}

{% include copy_block.html content="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" %}

{% include copy_block.html content="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" %}

{% include copy_block.html content="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" %}

{% include copy_block.html content="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" %}

{% endtab %}
{% tab Personnalisation %}

{% include copy_block.html content="Add a countdown to this message that shows the time until the user's flight." %}

{% include copy_block.html content="Personalize this message with the user's first name, with a fallback if it's missing." %}

{% include copy_block.html content="Improve this Liquid so it's easier to read." %}

{% include copy_block.html content="Create a message that shows different content based on my customer's loyalty status. If we don't know about their loyalty status, send a fallback message." %}

{% include copy_block.html content="Write a dynamic message that includes a user's favorite product and their last purchase date. If there's no last purchase, abort the message." %}

{% include copy_block.html content="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." %}

{% include copy_block.html content="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." %}

{% include copy_block.html content="Write Liquid to personalize a message based on a customer's country. I want to fill in the message with the country's name. If we don't have either of them, suggest they click on a link to update their profile." %}

{% include copy_block.html content="How can I personalize a welcome message with a user's first name and write different copy based on the user's gender?" %}

{% include copy_block.html content="Write Liquid to display different messages based on a custom attribute, \"CUSTOM_ATTRIBUTE_NAME\" and its value. There are six different options I could send. If there's no value for the custom attribute, I want to send a placeholder message." %}

{% endtab %}
{% endtabs %}

## Générer des images {#generate-images}

Operator génère des images à l'aide de [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), un système d'intelligence artificielle d'OpenAI, fournisseur tiers de Braze. Cela vous permet de créer des images réalistes et des illustrations à partir d'une description en langage naturel.

Dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/), sélectionnez **Générer avec Operator** dans le panneau **Charger des ressources**. Décrivez l'image souhaitée, et Operator la génère et l'enregistre directement dans votre bibliothèque multimédia.

### Conseils pour les prompts {#generate-images-prompt-tips}

- Décrivez le sujet, le style, l'ambiance et les couleurs de manière précise. Plus vous incluez de détails, meilleur sera le résultat.
- Saisie de texte uniquement ; le chargement d'une image de référence n'est pas pris en charge.
- Lorsque vous appliquez les [directives de marque](#apply-brand-guidelines) comme contexte dans votre prompt Operator, celui-ci les applique directement à l'image générée, de sorte que le résultat reflète le style visuel de votre marque.
- Les générations d'images sont comptabilisées dans votre limite d'utilisation quotidienne d'Operator. Pour en savoir plus, consultez [Limitations]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/#limitations).

### Exemples de prompts {#generate-images-example-prompts}

{% include copy_block.html content="Generate a bright, summery banner image of a beach scene for an email header." %}

{% include copy_block.html content="Create a minimalist product background in our brand colors." %}

## Générer du code de transformation des données {#generate-data-transformation-code}

Dans l'éditeur de [Transformation des données]({{site.baseurl}}/user_guide/data/unification/data_transformation/), sélectionnez **Insérer le code** pour générer du code de transformation qui convertit un payload webhook entrant en requêtes API Braze valides.

Pour des instructions étape par étape sur la création d'une transformation, consultez [Créer une transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation/).

### Exemples de prompts {#generate-data-transformation-example-prompts}

{% include copy_block.html content="Write transformation code that maps this survey webhook to a custom event on the user's profile." %}

{% include copy_block.html content="Update this transformation to identify users by email address instead of external ID." %}

## Vérifier la qualité du contenu {#review-content-quality}

Dans l'onglet **Test** pour les SMS, les notifications push Android, les notifications push iOS et les messages in-app traditionnels, sélectionnez **Vérifier avec Operator** pour vérifier votre contenu avant l'envoi. Par défaut, Operator vérifie votre campagne pour les erreurs d'orthographe et de grammaire, le ton inapproprié ou hors marque, le langage offensant, ainsi que tout code résiduel, contenu de test ou Liquid non rendu, et recommande comment corriger ce qu'il trouve. Vous pouvez également demander à Operator d'adapter la façon dont il vérifie votre contenu directement dans votre prompt.

### Ce que vous pouvez demander à Operator de vérifier {#review-content-quality-supported-features}

Au-delà de sa vérification par défaut, vous pouvez orienter Operator vers des contrôles spécifiques. Pensez à lui demander de vérifier l'un des éléments suivants :

| Vérification | Ce qu'il faut demander |
| --- | --- |
| Orthographe et grammaire | Demandez à Operator de relire l'orthographe et la grammaire et de suggérer des corrections qui améliorent la précision de votre contenu. |
| Ton | Demandez à Operator d'évaluer si le ton correspond au style de communication souhaité et de signaler tout ce qui pourrait être mal interprété. |
| Langage offensant | Demandez à Operator de rechercher un langage potentiellement offensant ou inapproprié afin que vous puissiez le réviser et garder vos messages respectueux. |
| Contenu accidentel | Demandez à Operator de détecter le code résiduel, le balisage ou les messages de test ajoutés involontairement, y compris le Liquid qui ne s'est pas rendu pour un utilisateur test. |
| Autres langues | Demandez à Operator de vérifier du contenu rédigé dans une autre langue. La prise en charge du contenu non anglophone peut varier, vérifiez donc les résultats attentivement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ce que vous pouvez demander à Operator de vérifier" }

### Bonnes pratiques {#review-content-quality-best-practices}

Tenez compte des éléments suivants pour tirer le meilleur parti de la vérification de contenu :

- **Relisez votre message :** bien que la vérification de contenu puisse aider à identifier les erreurs, il est toujours essentiel de relire votre contenu manuellement. Appuyez-vous sur les suggestions générées par l'intelligence artificielle comme guide utile, mais utilisez votre jugement pour garantir la précision.
- **Comprenez l'analyse du ton :** les résultats de l'analyse du ton sont subjectifs et basés sur la compréhension du modèle d'intelligence artificielle. Bien qu'ils puissent fournir des informations utiles, tenez compte de votre ton souhaité et du contexte de la conversation pour effectuer les ajustements appropriés.
- **Vérifiez le langage offensant signalé :** la détection du langage offensant est conçue pour être robuste, mais elle peut occasionnellement signaler des faux positifs. Examinez attentivement les sections signalées et apportez les modifications nécessaires.

### Exemples de prompts {#review-content-quality-example-prompts}

{% include copy_block.html content="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." %}

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Confidentialité et sécurité des données {#data-privacy-and-security}

Operator s'intègre à OpenAI pour générer des résultats. Pour en savoir plus sur les informations que Braze envoie à OpenAI, la façon dont ces données sont utilisées et vos droits de propriété intellectuelle, consultez [Comment les données sont utilisées avec OpenAI]({{site.baseurl}}/user_guide/brazeai/operator/#how-data-is-used-with-openai).

## Étapes suivantes {#next-steps}

- [Premiers pas avec Operator]({{site.baseurl}}/user_guide/brazeai/operator/) : accédez à Operator et utilisez-le
- [Vérifier les actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) : vérifiez et approuvez les modifications proposées par Operator
- [Résolution des problèmes]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) : consultez les problèmes courants et leurs solutions