---
nav_title: Cas d'utilisation eCommerce
article_title: Cas d'utilisation eCommerce
alias: /ecommerce_use_cases/
page_order: 4
description: "Cet article de référence présente plusieurs modèles Braze préconfigurés, conçus spécifiquement pour les marketeurs eCommerce, afin de faciliter la mise en œuvre de stratégies essentielles."
toc_headers: h2
---

# Comment utiliser les événements recommandés eCommerce {#how-to-use-ecommerce-recommended-events}

> Cette page explique comment et où utiliser les événements recommandés eCommerce sur l'ensemble de la plateforme, y compris comment utiliser les modèles de Canvas eCommerce de Braze.

{% alert note %}
Si vous utilisez le nouveau connecteur Shopify, les événements recommandés eCommerce sont automatiquement disponibles via l'intégration.
{% endalert %}

## Utiliser un modèle de Canvas {#using-a-canvas-template}

Pour utiliser un modèle de Canvas :
1. Accédez à **Messaging** > **Canvas**.
2. Sélectionnez **Create Canvas** > **Use a Canvas Template**.
3. Parcourez l'onglet **Braze templates** pour trouver le modèle souhaité. Vous pouvez prévisualiser un modèle en sélectionnant son nom.
4. Sélectionnez **Apply Template** pour le modèle que vous souhaitez utiliser.<br><br>![Page « Modèles de Canvas » ouverte sur l'onglet « Modèles Braze » affichant une liste de modèles récemment utilisés et de modèles Braze sélectionnables.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Modèles de Canvas eCommerce {#ecommerce-canvas-templates}

Braze propose quatre modèles de Canvas eCommerce.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personnalisation des messages {#message-personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) est un langage de modélisation puissant utilisé par Braze qui vous permet de créer du contenu dynamique et personnalisé pour vos clients. Grâce aux étiquettes Liquid, vous pouvez personnaliser les messages en fonction des données client, des informations produit et d'autres variables, améliorant ainsi l'expérience d'achat et stimulant l'engagement.

### Fonctionnalités clés de Liquid {#key-features-of-liquid}

- **Contenu dynamique :** Insérez des informations spécifiques au client, telles que les noms, les détails de commande et les préférences, dans vos messages.
- **Logique conditionnelle :** Utilisez des instructions if/else pour afficher différents contenus en fonction de conditions spécifiques (comme la localisation du client et l'historique d'achat).
- **Boucles :** Parcourez des collections de produits ou de données client pour afficher des listes ou des grilles d'articles.

### Premiers pas avec Liquid {#getting-started-with-liquid}

Pour commencer à personnaliser vos messages à l'aide des étiquettes Liquid, vous pouvez consulter les ressources suivantes :

- Référence des [données Shopify]({{site.baseurl}}/shopify_features/#shopify-data) avec des étiquettes Liquid prédéfinies
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)

## Segmentation {#segmentation}

Utilisez les segments Braze pour créer des segments de clients ciblés en fonction d'attributs et de comportements spécifiques, et diffusez des messages et des campagnes personnalisés. Grâce à cette fonctionnalité puissante, vous pouvez engager efficacement vos clients en atteignant la bonne audience avec le bon message au bon moment.

Pour en savoir plus sur la prise en main des segments, consultez [À propos des segments Braze]({{site.baseurl}}/user_guide/audience/segments/#about-braze-segments).

### Événements recommandés {#recommended-events}

Les événements eCommerce reposent sur les [événements recommandés]({{site.baseurl}}/recommended_events/).
Comme les événements recommandés sont des événements personnalisés plus structurés, vous pouvez rechercher les noms d'événements recommandés eCommerce en sélectionnant n'importe quel [filtre d'événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#segmentation-filters).

### Filtres eCommerce {#ecommerce-filters}

Segmentez vos utilisateurs avec des filtres eCommerce, comme **Ecommerce Source** et **Total Revenue**, en accédant à la section **eCommerce** dans l'outil de segmentation.

Pour consulter la liste des filtres eCommerce et leurs définitions, reportez-vous à [Filtres de segments]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) et sélectionnez la catégorie de recherche « eCommerce ».

![Menu déroulant des filtres de segments avec les filtres « Ecommerce ».]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propriétés de l'événement imbriqué {#nested-event-properties}

Pour segmenter par propriétés de l'événement imbriqué, vous pouvez utiliser les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#why-use-segment-extensions). Par exemple, vous pouvez utiliser les extensions de segments pour identifier les utilisateurs ayant acheté le produit « SKU-123 » au cours des 90 derniers jours.

## Analyse {#analytics}

### Rapport d'événements personnalisés {#custom-events-report}

Vous pouvez suivre le volume des événements recommandés eCommerce dans le [Rapport d'événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#analytics). Filtrez par **Perform Custom Event**, puis spécifiez le [nom de l'événement recommandé eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) pour visualiser ses performances au fil du temps.

![Graphique des événements personnalisés affichant les résultats pour six événements sélectionnés.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Tableaux de bord {#dashboards}

#### Tableau de bord des conversions {#conversions-dashboard}

Après avoir lancé une campagne ou un Canvas utilisant l'événement de conversion « Places Order », vous pouvez créer un [rapport de conversion]({{site.baseurl}}/user_guide/analytics/dashboards/conversions/#setting-up-your-report) correspondant pour suivre les performances.

![Tableau des détails de conversion avec les campagnes et Canvas, ainsi que les statistiques de conversion associées.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### Tableau de bord du chiffre d'affaires eCommerce {#ecommerce-revenue-dashboard}

Pour obtenir des informations sur le chiffre d'affaires attribué à la dernière campagne ou au dernier Canvas avec lequel un utilisateur a interagi avant de passer une commande, utilisez le [tableau de bord du chiffre d'affaires eCommerce]({{site.baseurl}}/ecommerce_revenue_dashboard/) et sélectionnez une fenêtre de conversion.

### Rapport sur les revenus {#revenue-report}

Pour analyser les données de ces nouveaux événements, accédez au [Générateur de tableaux de bord]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/) et consultez le [tableau de bord **eCommerce Revenue - Last Touch Attribution**]({{site.baseurl}}/ecommerce_revenue_dashboard/).