---
nav_title: Directives de marque
article_title: Directives de marque générées par l'intelligence artificielle
page_order: 2.2
description: "Cet article de référence traite des directives de marque pour l'assistant de rédaction de l'intelligence artificielle. Cette fonctionnalité vous permet d'adapter le style des textes générés par l'assistant de rédaction de l'intelligence artificielle à la voix et au style de votre marque."
---

# Générer des directives de marque avec BrazeAI {#generate-brand-guidelines-with-brazeai}

> Adaptez le style de vos textes générés par l'intelligence artificielle à la voix et à la personnalité de votre marque grâce à des directives de marque personnalisées.

## Élaborer des directives de marque {#steps}

Suivez ces étapes pour créer des directives de marque dans l'assistant de rédaction de l'intelligence artificielle. Vous pouvez également créer des directives de marque sur la page de paramétrage des [Directives de marque]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/).

### Étape 1 : Créer une directive de marque {#step-1-create-a-brand-guideline}

1. Dans votre compositeur de messages, recherchez et sélectionnez <i class="fa-solid fa-wand-magic-sparkles" title="Assistant de rédaction IA"></i> **Assistant de rédaction IA** pour [ouvrir l'assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/#access).
2. Sélectionnez **Appliquer une directive de marque**, puis **Créer une directive de marque**.

![Menu déroulant « Appliquer les directives de marque » ouvert avec le bouton « Créer une directive de marque » en surbrillance.]({% image_buster /assets/img/ai_copywriter/create_brand_guideline_button.png %}){:style="max-width:75%"}

{: start="3"}

3. Saisissez un nom pour cette directive. Il s'agira de l'étiquette qui apparaît dans la sélection précédente.
4. Pour la rubrique **Quand utiliserez-vous ces directives de marque ?**, ajoutez des détails afin d'aider vos collègues (et vous à l'avenir) à comprendre le contexte d'utilisation de cette directive.
5. Si vous souhaitez qu'il s'agisse de la directive de marque par défaut pour l'espace de travail actuel, cochez la case **Utiliser comme directive de marque par défaut**.

![Vue de la création des directives de marque.]({% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} "Brand Guidelines")

### Étape 2 : Décrire la personnalité de votre marque {#step-2-describe-your-brand-personality}

Pour la **personnalité de la marque**, réfléchissez à ce qui rend votre marque unique. Incluez les caractéristiques, les valeurs, la voix et tous les archétypes qui définissent votre marque. Voici quelques caractéristiques à prendre en compte :

| **Caractéristique** | **Définition** | **Exemple** |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Réputation | Comment vous souhaitez que votre marque soit perçue sur le marché. | Nous sommes connus comme la marque la plus fiable et la plus orientée client de notre secteur. |
| Traits de personnalité | Caractéristiques humaines qui décrivent le caractère de votre marque. | Notre marque est conviviale, accessible et toujours optimiste. |
| Valeurs | Les valeurs fondamentales qui orientent les actions et les décisions de votre marque. | Nous accordons de l'importance à la durabilité, à la transparence et à la communauté. |
| Différenciation | Les qualités uniques qui distinguent votre marque de ses concurrents. | Nous nous distinguons en offrant un service client personnalisé qui va au-delà des attentes. |
| Voix de la marque | Le ton et le style de communication de votre marque. | Notre voix est décontractée mais informative, claire sans être trop formelle. |
| Archétype de la marque | L'archétype qui représente le persona de votre marque (le héros, le créateur, etc.). | Nous incarnons l'archétype de l'explorateur, toujours à la recherche de nouveaux défis et de nouvelles aventures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Décrire la personnalité de votre marque" }

### Étape 3 : Définir le langage à éviter (facultatif) {#step-3-define-language-that-should-be-avoided-optional}

Pour les **exclusions**, énumérez tout langage ou style qui ne correspond pas à votre marque. Par exemple, vous pourriez vouloir éviter le « sarcasme », les « attitudes négatives » ou le ton « condescendant ».

### Étape 4 : Tester vos directives {#step-4-test-your-guidelines}

Testez vos directives pour en évaluer le résultat. Développez la section **Tester vos directives** pour générer des exemples de textes et les ajuster si nécessaire.

![Test des directives de marque à l'aide d'une promotion sur les soldes de printemps pour des lignes d'objet d'e-mails.]({% image_buster /assets/img/ai_copywriter/test_brand_guidelines.png %})

### Étape 5 : Enregistrer vos directives {#step-5-save-your-guidelines}

Lorsque vous êtes satisfait de vos directives, sélectionnez **Enregistrer la directive de marque**. Vos nouvelles directives seront enregistrées dans votre espace de travail pour une utilisation ultérieure.

{% alert important %}
Vous pouvez changer la langue du texte généré, quelle que soit la langue de votre texte d'origine, mais ni Braze ni OpenAI ne garantissent la qualité de la traduction. Testez et vérifiez toujours les traductions avant de les utiliser.
{% endalert %}

## Modifier les directives existantes {#editing-existing-guidelines}

Pour modifier vos directives de marque existantes :

1. Ouvrez l'assistant de rédaction de l'intelligence artificielle.
2. Appliquez les directives de marque que vous souhaitez modifier. Un bouton apparaît à côté du champ.
3. Sélectionnez **Modifier la directive**.

{% multi_lang_include brazeai/generative_ai/policy.md %}