---
nav_title: Utiliser les modèles Braze
article_title: Utiliser les modèles de Canvas Braze
alias: "/canvas_templates/templates/"
page_order: 2
description: "Cet article de référence explique comment créer des Canvas à partir des modèles disponibles."
page_type: reference
---

# Utiliser les modèles de Canvas Braze {#use-braze-canvas-templates}

> Braze propose une sélection de modèles de Canvas que vous pouvez consulter et utiliser comme bonnes pratiques pour des cas d'utilisation courants. Bien que ces modèles ne puissent pas être modifiés, vous pouvez les consulter dans **Contenu** > **Canvas** > **Modèles Braze** ou les utiliser dans vos Canvas.

![Modèles Braze dans la section des modèles de Canvas avec treize modèles disponibles.]({% image_buster /assets/img/braze_canvas_templates.png %})

Sélectionnez l'un des modèles disponibles suivants pour le consulter ou l'utiliser comme Canvas.

## Modèles de Canvas standard {#standard-canvas-templates}

{% tabs %}
{% tab Abandoned Intent %}

### Intention abandonnée {#abandoned-intent}

Interagissez avec les utilisateurs en temps réel pour les encourager à finaliser leurs achats.

Tenez compte des éléments suivants lors de l'utilisation de ce modèle :

- La planification d'entrée est déclenchée par API. Utilisez l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) pour faire entrer les utilisateurs lorsqu'ils abandonnent un panier, ou passez à une planification basée sur une action avec un déclencheur tel que **Effectuer un événement personnalisé** ou **Effectuer un événement de mise à jour du panier** si cela correspond à votre configuration.
- La conversion par défaut suit **Effectuer un achat quelconque (Legacy)**. Adaptez les événements de conversion et les étapes Parcours d'actions **A effectué un achat ?** à des produits spécifiques si nécessaire.
- Les utilisateurs sortent du Canvas lorsqu'ils effectuent un achat dans les étapes Parcours d'actions **A effectué un achat ?**. Ce modèle suppose que vous disposez d'un parcours post-achat distinct.
- Le Canvas inclut un e-mail pour le **rappel détaillé**, une étape de délai, une répartition par canal intelligent pour l'e-mail et le SMS, des messages par canal avec des Content Cards (e-mail, SMS et message in-app), ainsi qu'une étape Audience Sync. Configurez le **reciblage publicitaire** avec vos partenaires et audiences.

Pour un guide pas à pas, consultez [Panier abandonné]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/abandoned_cart/).

{% endtab %}
{% tab Back In Stock %}

### Retour en stock {#back-in-stock}

Stimulez les achats en informant vos utilisateurs lorsqu'un article est de nouveau en stock grâce à des messages personnalisés. Tenez compte des éléments suivants lors de l'utilisation de ce modèle :

- Dans **Planification d'entrée**, sélectionnez un catalogue à utiliser. Cela vous permet d'accéder à des données, telles que les produits, les remises et les promotions, pour mieux cibler vos utilisateurs.
- Dans **Audience cible**, ajoutez un segment pour cibler les utilisateurs ayant manifesté un intérêt pour un article donné.
- Dans les étapes Message tout au long du Canvas, mettez à jour le Liquid pour référencer votre catalogue.

{% endtab %}
{% tab Feature Adoption %}

### Adoption de fonctionnalité {#feature-adoption}

Envoyez des messages personnalisés au bon moment pour mettre en avant les avantages et les conseils d'utilisation. Tenez compte des éléments suivants lors de l'utilisation de ce modèle :

- Excluez les utilisateurs qui ont déjà adopté la fonctionnalité. Par exemple, dans **Audience cible**, ajoutez un filtre pour un événement personnalisé tel que « Fonctionnalité activée » qui s'est déjà produit.
- Pour utiliser l'étape chemin d'expérience, définissez un événement de conversion. Cet événement doit être celui qui signale l'adoption de la fonctionnalité.
- Configurez l'étape Parcours d'actions dans le modèle avec des événements personnalisés pour « Fonctionnalité activée » et « Visite guidée effectuée ».
- Configurez les attributs personnalisés dans l'étape Message nommée « Enquête de satisfaction » pour capturer le sentiment des retours.

{% endtab %}
{% tab Lapsed User %}

### Utilisateur inactif {#lapsed-user}

Ramenez les utilisateurs vers votre application grâce à des incitations basées sur leurs interactions passées. Tenez compte des éléments suivants lors de l'utilisation de ce modèle :

- Dans **Bases**, sélectionnez une application spécifique pour le suivi des conversions.
- Dans l'éditeur de Canvas, ajoutez des applications spécifiques pour les étapes Parcours d'actions.
- Configurez l'étape Audience Sync avec les partenaires et les audiences correspondant à votre cas d'utilisation.

{% endtab %}
{% tab Onboarding %}

### Onboarding {#onboarding}

Créez des parcours d'onboarding qui favorisent une adoption initiale solide et encouragent des relations durables avec vos utilisateurs. Tenez compte des éléments suivants lors de l'utilisation de ce modèle :

- Dans l'étape Parcours d'audience nommée « Répartition de l'audience », envisagez de personnaliser les actions clés pour les utilisateurs engagés. Dans le modèle, le filtre de segment est « A cliqué sur l'e-mail pour l'étape E-mail de bienvenue ».

{% endtab %}
{% tab Post-Purchase Feedback %}

### Retour post-achat {#post-purchase-feedback}

Orchestrez des expériences personnalisées qui vous permettent de répondre aux retours et de construire une relation avec vos utilisateurs. Tenez compte des éléments suivants lors de l'utilisation de ce modèle :

- Dans la première étape de l'éditeur de Canvas :
    - Spécifiez les attributs personnalisés dans le message in-app pour indiquer le sentiment du retour en fonction de l'option d'enquête sélectionnée.
    - Spécifiez les attributs sur les liens pour chaque appel à l'action afin de capturer l'option sélectionnée. Ces attributs sont référencés dans le parcours d'audience suivant.
- Personnalisez le Parcours d'audience avec les attributs de la première étape de ce modèle.
- Configurez l'étape Audience Sync nommée « Reciblage publicitaire ».

{% endtab %}
{% endtabs %}

## Modèles de Canvas eCommerce {#ecommerce-canvas-templates}

Les modèles de Canvas eCommerce sont spécialement conçus pour les marketeurs eCommerce, facilitant la mise en œuvre de stratégies essentielles.

{% multi_lang_include canvas/ecommerce_templates.md %}