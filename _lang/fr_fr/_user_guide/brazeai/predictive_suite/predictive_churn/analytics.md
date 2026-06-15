---
nav_title: Analyse de l'attrition
article_title: Analyses prédictives de l'attrition
description: "Cet article de référence présente les différents composants de la page Analyses prédictives de l'attrition et explique comment ils peuvent être utilisés pour prendre des décisions fondées sur des informations."
page_order: 1.5

---

# Analyses prédictives de l'attrition {#predictive-churn-analytics}

> Une fois que votre prédiction a été créée et entraînée, vous avez accès à la page **Analyses prédictives**. Cette page vous aide à décider quels utilisateurs vous devez cibler en fonction de leur _score de risque d'attrition_ ou de leur catégorie.

## À propos des analyses prédictives de l'attrition {#about-predictive-churn-analytics}

Dès que la prédiction est terminée et que cette page est remplie, vous pouvez passer à l'utilisation des [filtres]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) dans les segments ou les campagnes pour commencer à utiliser les résultats du modèle. Mais si vous voulez de l'aide pour décider qui cibler et pourquoi, cette page peut le faire en fonction de l'exactitude historique du modèle et de vos propres objectifs métier.

Tels sont les composants de l'analyse prédictive de l'attrition :

- [Score et catégorie d'attrition](#churn_score)
- [Qualité de prédiction](#prediction_quality)
- [Précision estimée](#estimated_results)
- [Tableau de corrélation de l'attrition](#correlation_table)

La répartition des scores pour l'ensemble de l'audience de prédiction est affichée en haut de la page dans un graphique que vous pouvez consulter par catégorie ou par score. Les utilisateurs dans les compartiments situés plus à droite ont des scores plus élevés et sont plus susceptibles de se désabonner. Les utilisateurs dans les compartiments situés plus à gauche sont moins susceptibles de se désabonner. Le curseur situé sous le graphique vous permet de sélectionner un groupe d'utilisateurs et d'estimer les résultats du ciblage des utilisateurs se situant dans la fourchette sélectionnée du _score de risque d'attrition_ ou de la catégorie.

Au fur et à mesure que vous déplacez le curseur, la barre située dans la moitié gauche du panneau inférieur vous informe du nombre d'utilisateurs ciblés sur l'ensemble de l'audience de prédiction.

![]({% image_buster /assets/img/churn/churnTargeting.gif %})

## Score et catégorie d'attrition {#churn_score}

Les utilisateurs de l'audience de prédiction se verront attribuer un _score de risque d'attrition_ compris entre 0 et 100. Plus le score est élevé, plus la probabilité d'attrition est grande.
- Les utilisateurs dont le score est compris entre 0 et 50 seront classés dans la catégorie _Risque faible_.
- Les utilisateurs dont le score est compris entre 50 et 75, et entre 75 et 100, seront classés respectivement dans les catégories _Risque moyen_ et _Risque fort_.

Les scores et les catégories correspondantes seront mis à jour conformément à la planification que vous avez choisie sur la page de création du modèle. Le nombre d'utilisateurs avec des scores d'attrition dans chacun des 20 compartiments de taille égale s'affiche dans le graphique en haut de la page. Cela peut vous aider à déterminer ce à quoi ressemble le risque d'attrition sur la population selon cette prédiction.

## Qualité de prédiction {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Précision estimée {#estimated_results}

Dans la moitié droite du panneau situé sous le graphique, nous présentons des estimations de la précision attendue du ciblage de cette partie de l'audience de prédiction. Sur la base des données relatives aux utilisateurs de l'audience de prédiction dans le passé et de la précision apparente du modèle pour distinguer les utilisateurs qui se désabonnent de ceux qui ne se désabonnent pas sur ces données passées, ces barres de progression permettent d'estimer, pour un futur message potentiel utilisant l'audience mise en évidence par le curseur :

![]({% image_buster /assets/img/churn/churnEstimatedResults.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

- Combien d'utilisateurs sélectionnés sont susceptibles de se désabonner
- Combien d'utilisateurs sélectionnés sont susceptibles de **ne pas** se désabonner

À l'aide de ces informations, nous vous encourageons à décider du nombre de désabonnés que vous souhaitez capturer et du coût des faux positifs pour votre entreprise. Si vous envoyez une promotion de valeur, vous voudrez peut-être garder un minimum de non-désabonnés dans votre ciblage tout en capturant le maximum de vrais désabonnés proposés par le modèle. Ou, si vous êtes moins sensible aux faux positifs et aux utilisateurs recevant des messages supplémentaires, vous pouvez envoyer un message à une audience plus importante afin de capturer plus de désabonnés attendus et ignorer les erreurs probables.

### Utilisateurs susceptibles de se désabonner {#users-expected-to-churn}

Il s'agit d'une estimation du nombre de désabonnés réels qui seront correctement ciblés. Bien entendu, nous ne connaissons pas parfaitement l'avenir, et nous ne savons donc pas précisément quels utilisateurs de l'audience de prédiction se désabonneront à l'avenir. Mais la prédiction est une déduction fiable. Sur la base des performances passées, cette barre de progression indique le nombre total de désabonnés « réels » ou « vrais » attendus au sein de l'audience de prédiction (sur la base des taux d'attrition précédents) qui seront ciblés avec la sélection de ciblage actuelle. Nous estimons que ce nombre d'utilisateurs se désabonnera si vous ne les ciblez pas avec un message supplémentaire ou inhabituel.

### Utilisateurs susceptibles de ne pas se désabonner {#users-expected-not-to-churn}

Il s'agit d'une estimation du nombre d'utilisateurs qui ne se seraient pas désabonnés et qui seront incorrectement ciblés. Tous les modèles de machine learning font des erreurs. Il se peut que certains utilisateurs de votre sélection aient un _score de risque d'attrition_ élevé, mais qu'ils ne se désabonnent pas pour autant. Ils ne se désabonneront pas même si vous ne prenez aucune mesure. Ils seront de toute façon ciblés, il s'agit donc d'une erreur ou d'un « faux positif ». La largeur totale de cette deuxième barre de progression représente le nombre attendu d'utilisateurs qui ne se désabonneront pas, et la partie remplie représente ceux qui seront incorrectement ciblés en utilisant la position actuelle du curseur.

## Tableau de corrélation de l'attrition {#correlation_table}

Cette analyse affiche tous les attributs ou comportements des utilisateurs qui sont en corrélation avec l'attrition des utilisateurs dans l'audience de prédiction historique. Les tableaux sont divisés en une partie gauche et une partie droite correspondant respectivement à « plus » et « moins » susceptibles de se désabonner. Pour chaque ligne, le rapport indiquant si les utilisateurs ayant le comportement ou l'attribut dans la colonne de gauche sont plus ou moins susceptibles de se désabonner s'affiche dans la colonne de droite. Ce chiffre est le rapport entre la probabilité d'attrition des utilisateurs ayant ce comportement ou cet attribut et la probabilité d'attrition de l'ensemble de l'audience de prédiction.

Ce tableau est uniquement mis à jour lorsque la prédiction est réentraînée et non lorsque les _scores de risque d'attrition_ des utilisateurs sont actualisés.

{% alert note %}
Les données de corrélation pour les aperçus de prédictions seront partiellement masquées. Un achat est requis pour révéler ces informations. Contactez votre gestionnaire de compte pour plus d'informations.
{% endalert %}