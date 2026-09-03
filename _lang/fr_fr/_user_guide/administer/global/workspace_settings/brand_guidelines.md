---
nav_title: Directives de marque
article_title: Directives de marque
page_order: 1
page_type: reference
description: "Cet article de référence explique comment créer, gérer et ajouter des directives de marque en tant que contexte pour Operator et les agents."
---

# Directives de marque {#brand-guidelines}

> Adaptez le style de vos textes générés par l'IA à la voix, au ton et à la personnalité de votre marque grâce à des directives de marque personnalisées.

Créez et gérez vos directives de marque depuis **Contenu** > **Directives de marque**.

## Créer des directives de marque {#creating-brand-guidelines}

### Étape 1 : Créer une directive de marque {#step-1-create-a-brand-guideline}

Sur la page **Directives de marque**, sélectionnez **Créer nouveau**. Si vous souhaitez que cette directive de marque soit la valeur par défaut de l'espace de travail, sélectionnez **Utiliser comme directive de marque par défaut**. Vous pouvez avoir une seule valeur par défaut par espace de travail.

### Étape 2 : Décrire la personnalité de votre marque {#step-2-describe-your-brand-personality}

Pour **Personnalité de la marque**, réfléchissez à ce qui rend votre marque unique. Incluez les traits, les valeurs, la voix et les archétypes qui définissent votre marque. Limitez ce champ à 10 000 caractères ou moins. Si vous générez ce texte avec un LLM, incluez cette limite de caractères dans votre prompt afin que le résultat tienne dans le champ.

Voici quelques caractéristiques à prendre en compte :

| Caractéristique | Définition | Exemple |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Réputation | Comment vous souhaitez que votre marque soit perçue sur le marché. | Nous sommes reconnus comme la marque la plus fiable et la plus centrée sur le client dans notre secteur. |
| Traits de personnalité | Caractéristiques humaines qui décrivent le caractère de votre marque. | Notre marque est amicale, accessible et toujours positive. |
| Valeurs | Les valeurs fondamentales qui guident les actions et les décisions de votre marque. | Nous valorisons la durabilité, la transparence et la communauté. |
| Différenciation | Les qualités uniques qui distinguent votre marque de la concurrence. | Nous nous démarquons en offrant un service client personnalisé qui va au-delà des attentes. |
| Voix de la marque | Le ton et le style de communication utilisés par votre marque. | Notre voix est décontractée mais informative, assurant la clarté sans être trop formelle. |
| Archétype de marque | L'archétype qui représente le personnage de votre marque (le Héros, le Créateur, etc.). | Nous incarnons l'archétype de l'« Explorateur », toujours en quête de nouveaux défis et aventures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Décrire la personnalité de votre marque" }

### Étape 3 : Définir le langage à éviter (facultatif) {#step-3-define-language-that-should-be-avoided-optional}

Pour **Exclusions**, listez tout langage ou style qui ne correspond pas à votre marque. Par exemple, vous pourriez vouloir éviter le « sarcasme », les « attitudes négatives » ou les tons « condescendants ». Limitez ce champ à 300 caractères ou moins.

![La fenêtre « Créer une directive de marque » avec des champs pour saisir le nom, la description, la personnalité, les exclusions et le ton.]({% image_buster /assets/img/guidelines_create.png %})

### Étape 4 : Tester vos directives {#step-4-test-your-guidelines}

Testez vos directives pour voir comment elles fonctionnent. Développez **Tester vos directives** pour générer un exemple de texte et ajustez si nécessaire.

### Étape 5 : Enregistrer vos directives {#step-5-save-your-guidelines}

Lorsque vous êtes satisfait de vos directives, sélectionnez **Enregistrer la directive de marque**. Vos directives sont enregistrées dans votre espace de travail pour une utilisation future.

{% alert important %}
Vous pouvez modifier la langue de sortie quel que soit la langue de votre texte, mais ni Braze ni OpenAI ne garantissent la qualité de la traduction. Testez et vérifiez toujours les traductions avant de les utiliser.
{% endalert %}

## Gestion des directives de marque {#managing-brand-guidelines}

Vous pouvez modifier les directives de marque en les sélectionnant sur la page **Brand Guidelines**. Archivez une directive de marque pour la rendre inactive et indisponible dans les composeurs de messages. Pour la rendre à nouveau active et sélectionnable, vous pouvez filtrer les directives de marque archivées, puis la désarchiver.

## Utiliser les directives de marque {#using-brand-guidelines}

Dans le panneau de chat de l'Operator, sélectionnez <i class="fa-regular fa-plus"></i>&nbsp;**Ajouter du contexte pour Operator**, puis choisissez une ou plusieurs directives sous **Brand guidelines**. Operator applique les directives sélectionnées aux textes, modèles et images générés. Par défaut, rien n'est sélectionné.

![Sélection des directives de marque dans le panneau de chat de l'Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

Lorsque vous configurez un agent, sélectionnez les directives de marque sous [Ajouter du contexte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources) pour que l'agent suive cette voix et ce style. Agent Console sélectionne la valeur par défaut du workspace pour vous.

{% multi_lang_include brazeai/generative_ai/policy.md %}