---
nav_title: Modèles de Canvas
article_title: Créer un modèle de Canvas
page_order: 2
alias: "/canvas_templates/"
description: "Créez et gérez des modèles de Canvas réutilisables, ou démarrez avec les modèles Braze préconstruits pour les cas d'utilisation courants."
---

# Créer un modèle de Canvas {#create-a-canvas-template}

> Cet article de référence explique comment créer et gérer des modèles pour Canvas. L'utilisation de modèles peut affiner votre envoi de messages en créant un cadre cohérent, facilement personnalisable pour s'adapter à vos objectifs spécifiques à travers vos Canvas.

{% alert tip %}
Gagnez du temps et simplifiez la création de vos Canvas en utilisant les [modèles Braze Canvas](#available-braze-templates) ! Parcourez notre bibliothèque de modèles préconstruits pour trouver celui qui correspond à votre cas d'utilisation et personnalisez-le pour répondre à vos besoins spécifiques.
{% endalert %}

## Méthode 1 : Créer à partir d'un Canvas existant {#method-1-create-from-an-existing-canvas}

### Étape 1 : Sélectionner votre Canvas existant {#step-1-select-your-existing-canvas}

Dans le tableau de bord de Braze, allez dans **Messaging** > **Canvas** et sélectionnez un Canvas existant que vous souhaitez utiliser comme modèle.

### Étape 2 : Créer votre modèle {#step-2-create-your-template}

Dans l'éditeur Canvas, sélectionnez **Edit Canvas** ou **Edit draft**, selon que votre Canvas est actif ou en brouillon. Développez le menu déroulant **Save as draft** dans le pied de page et sélectionnez **Save as template**.

![]({% image_buster /assets/img/save_canvas_as_template.png %})

### Étape 3 : Enregistrer votre modèle {#step-3-save-your-template}

Ensuite, donnez un nom à votre modèle et ajoutez les étiquettes pertinentes. Puis, sélectionnez **Save**. Votre modèle est maintenant prêt à être utilisé pour créer un Canvas, vous donnant une longueur d'avance avec vos paramètres de base et vos étapes déjà en place.

## Méthode 2 : Créer via l'éditeur de modèles Canvas {#method-2-create-via-canvas-template-editor}

### Étape 1 : Accéder à l'éditeur de modèles Canvas {#step-1-go-to-the-canvas-template-editor}

Dans le tableau de bord de Braze, allez dans **Content** > **Canvas**.

### Étape 2 : Créer un nouveau modèle {#step-2-create-a-new-template}

Sélectionnez **Create template** et commencez à configurer les détails de votre Canvas. Vous pouvez commencer par donner un nom à votre modèle de Canvas.

![Un exemple de modèle de Canvas nommé « Annual sale Canvas template » avec la description « Use for annual spring promotion ».]({% image_buster /assets/img/canvas_template_example.png %})

### Étape 3 : Personnaliser votre modèle {#step-3-customize-your-template}

Ensuite, personnalisez votre modèle en [configurant votre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-2-build-your-canvas). Vous pouvez décider quand les utilisateurs doivent entrer dans le Canvas, déterminer quels utilisateurs peuvent y accéder, ajuster vos paramètres d'envoi et construire le parcours utilisateur pour le modèle.

### Étape 4 : Enregistrer votre modèle {#step-4-save-your-template}

Une fois la personnalisation de votre modèle terminée, sélectionnez le bouton **Save template**. Sur la page **Canvas template**, vous pouvez consulter les détails de votre modèle de Canvas en sélectionnant <i class="fas fa-list"></i> **Template details**.

## Utiliser les modèles de Canvas {#using-canvas-templates}

Il existe deux façons d'utiliser votre modèle lors de la composition d'un Canvas :

- **Depuis Messaging** : Allez dans **Messaging** > **Canvas**. Sélectionnez le bouton **Create Canvas** puis **Use a Canvas Template**.
- **Depuis Content** : Allez dans **Content** > **Canvas** et trouvez le modèle souhaité dans **Canvas templates**. Ensuite, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i> suivi de **Apply template**. Cela vous amènera à un nouveau Canvas avec le modèle appliqué dans le compositeur Canvas.

### Modèles Braze disponibles {#available-braze-templates}

Pour une liste des modèles de Canvas disponibles, consultez [Utiliser les modèles de Canvas Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/). Pour plus de détails sur l'utilisation des modèles Canvas eCommerce, consultez [Comment utiliser les événements recommandés eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

## Gérer les modèles de Canvas {#managing-canvas-templates}

Les modèles de Canvas peuvent être dupliqués et archivés, de manière similaire à un Canvas réel. Pour modifier un modèle de Canvas, sélectionnez le modèle puis **<i class="fas fa-pencil-alt"></i>Edit**.

Au niveau de l'espace de travail, vous pouvez mettre à jour les autorisations des utilisateurs pour autoriser ou limiter l'accès à la création, la modification, la consultation ou l'archivage des modèles de Canvas.

### Autorisations pour les équipes et les espaces de travail {#permissions-for-teams-and-workspaces}

Pour permettre uniquement à certains utilisateurs d'accéder à des modèles de Canvas spécifiques et de les utiliser, [ajoutez une équipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) aux modèles, puis attribuez les autorisations au niveau de l'équipe « Access Campaigns, Canvases, Content Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Center ».

Si vous attribuez l'une des autorisations suivantes au niveau de l'équipe, mais pas au niveau de l'espace de travail, vous ne pouvez effectuer les actions suivantes que pour les éléments assignés à votre équipe :

- Créer et modifier des modèles de Canvas
- Consulter des modèles de Canvas
- Archiver des modèles de Canvas

Si les autorisations sont accordées à la fois au niveau de l'espace de travail et au niveau des équipes, les autorisations au niveau de l'espace de travail seront prioritaires.

## Questions fréquemment posées {#frequently-asked-questions}

### Puis-je enregistrer une étape incomplète dans un modèle de Canvas ? {#can-i-save-an-incomplete-step-in-a-canvas-template}

Oui, vous pouvez enregistrer des étapes incomplètes en tant que modèle de Canvas. Cependant, lorsque le modèle est utilisé, une erreur apparaîtra sur le bouton **Save template** indiquant ce qui est nécessaire pour lancer le Canvas.

### Puis-je enregistrer les paramètres du générateur Canvas en tant que modèle, ou seulement les étapes ? {#can-i-save-my-canvas-builder-settings-as-a-template-or-can-i-only-save-steps}

Oui, vous pouvez enregistrer les paramètres du générateur Canvas dans un modèle de Canvas. Par exemple, si vous prévoyez d'utiliser souvent une combinaison de segments et de filtres, vous pouvez enregistrer ces paramètres d'**audience cible** dans votre modèle de Canvas.