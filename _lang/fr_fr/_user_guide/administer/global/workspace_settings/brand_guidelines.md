---
nav_title: Directives de marque
article_title: Directives de marque
page_order: 1
page_type: reference
description: "Cet article de référence explique comment créer, gérer et utiliser des directives de marque qu'Operator applique lors de la génération de textes, de modèles et d'images."
---

# Directives de marque {#brand-guidelines}

> Adaptez le style de vos textes générés par l'intelligence artificielle à la voix, au ton et à la personnalité de votre marque grâce à des directives de marque personnalisées.

Créez et gérez vos directives de marque depuis **Contenu** > **Directives de marque**.

## Créer des directives de marque {#creating-brand-guidelines}

### Étape 1 : Créer une directive de marque {#step-1-create-a-brand-guideline}

Sur la page **Brand Guidelines**, sélectionnez **Create new**. Si vous souhaitez que cette directive de marque soit celle par défaut pour l'espace de travail, sélectionnez **Use as default brand guideline**. Vous ne pouvez avoir qu'une seule directive par défaut par espace de travail.

### Étape 2 : Décrire la personnalité de votre marque {#step-2-describe-your-brand-personality}

Pour **Brand personality**, réfléchissez à ce qui rend votre marque unique. Incluez les traits, les valeurs, la voix et les archétypes qui définissent votre marque. Limitez ce champ à 10 000 caractères ou moins. Si vous générez ce texte avec un LLM, incluez cette limite de caractères dans votre prompt afin que le résultat tienne dans le champ.

Voici quelques caractéristiques à prendre en compte :

| Caractéristique | Définition | Exemple |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Réputation | La manière dont vous souhaitez que votre marque soit perçue sur le marché. | Nous sommes reconnus comme la marque la plus fiable et la plus centrée sur le client de notre secteur. |
| Traits de personnalité | Les caractéristiques humaines qui décrivent le caractère de votre marque. | Notre marque est conviviale, accessible et toujours positive. |
| Valeurs | Les valeurs fondamentales qui guident les actions et les décisions de votre marque. | Nous valorisons la durabilité, la transparence et la communauté. |
| Différenciation | Les qualités uniques qui distinguent votre marque de ses concurrents. | Nous nous démarquons en offrant un service client personnalisé qui va au-delà des attentes. |
| Voix de marque | Le ton et le style de communication utilisés par votre marque. | Notre voix est décontractée mais informative, garantissant la clarté sans être trop formelle. |
| Archétype de marque | L'archétype qui représente le persona de votre marque (le Héros, le Créateur, etc.). | Nous incarnons l'archétype de l'« Explorateur », toujours en quête de nouveaux défis et aventures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Décrire la personnalité de votre marque" }

### Étape 3 : Définir le langage à éviter (facultatif) {#step-3-define-language-that-should-be-avoided-optional}

Pour **Exclusions**, listez tout langage ou style qui ne correspond pas à votre marque. Par exemple, vous pourriez vouloir éviter le « sarcasme », les « attitudes négatives » ou les tons « condescendants ». Limitez ce champ à 300 caractères ou moins.

![La fenêtre « Create brand guideline » avec des champs pour saisir le nom, la description, la personnalité, les exclusions et le ton.]({% image_buster /assets/img/guidelines_create.png %})

### Étape 4 : Tester vos directives {#step-4-test-your-guidelines}

Testez vos directives pour voir comment elles fonctionnent. Développez **Test your guidelines** pour générer un exemple de texte et ajustez si nécessaire.

### Étape 5 : Enregistrer vos directives {#step-5-save-your-guidelines}

Lorsque vous êtes satisfait de vos directives, sélectionnez **Save brand guideline**. Vos directives sont enregistrées dans votre espace de travail pour une utilisation future.

{% alert important %}
Vous pouvez modifier la langue de sortie indépendamment de la langue de votre texte, mais ni Braze ni OpenAI ne garantissent la qualité de la traduction. Testez et vérifiez toujours les traductions avant de les utiliser.
{% endalert %}

## Gestion des directives de marque {#managing-brand-guidelines}

Vous pouvez modifier les directives de marque en les sélectionnant sur la page **Brand Guidelines**. Archivez une directive de marque pour la rendre inactive et indisponible dans les éditeurs de messages. Pour la rendre à nouveau active et sélectionnable, vous pouvez filtrer les directives de marque archivées, puis la désarchiver.

## Utiliser les directives de marque {#using-brand-guidelines}

Lorsque vous composez un message, ouvrez Operator pour [générer du texte]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) et sélectionnez votre directive de marque dans le menu déroulant **Apply brand guideline**. Si vous désignez une directive de marque spécifique comme directive par défaut, Braze la sélectionne automatiquement dans le menu déroulant, mais vous pouvez en choisir une autre.

![Operator avec « Important Alerts!! » sélectionné comme directive de marque.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}