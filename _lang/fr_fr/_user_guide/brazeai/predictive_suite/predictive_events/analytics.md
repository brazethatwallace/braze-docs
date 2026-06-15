---
nav_title: Analyse des événements
article_title: Analyses prédictives des événements
description: "Cet article de référence présente les différents composants de la page Analyses prédictives des événements et explique comment ils peuvent être utilisés pour prendre des décisions fondées sur des informations."
page_order: 1.3

---

# Analyses prédictives des événements {#predictive-event-analytics}

> Une fois que votre prédiction a été créée et entraînée, vous avez accès à la page **Analyses prédictives**. Cette page vous aide à décider quels utilisateurs vous devez cibler en fonction de leur score de probabilité ou de leur catégorie.

## À propos des analyses prédictives des événements {#about-predictive-event-analytics}

Dès que la prédiction est terminée et que cette page est remplie, vous pouvez commencer à utiliser les [filtres]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) dans les segments ou les Campaigns pour exploiter les résultats du modèle. Si vous souhaitez de l'aide pour décider qui cibler et pourquoi, cette page peut vous guider en fonction de l'exactitude historique du modèle et de vos propres objectifs métier.

Tels sont les éléments constitutifs des analyses prédictives des événements :

- [Score de probabilité](#purchase_score)
- [Qualité de prédiction](#prediction_quality)
- [Précision estimée](#estimated_results)
- [Tableau de corrélation des événements](#correlation_table)

La distribution des scores de probabilité pour l'ensemble de l'audience de prédiction est affichée en haut de la page. Les utilisateurs des compartiments situés plus à droite ont des scores plus élevés et sont plus susceptibles de réaliser l'événement. Les utilisateurs des compartiments situés plus à gauche sont moins susceptibles de réaliser l'événement. Le curseur situé sous le graphique vous permet de sélectionner une section d'utilisateurs et d'estimer quels seraient les résultats du ciblage de ces utilisateurs.

Lorsque vous déplacez les curseurs sur différentes positions, la barre située dans la moitié gauche du panneau vous indique combien d'utilisateurs, sur l'ensemble de l'audience de prédiction, seraient ciblés en utilisant la partie de la population que vous avez sélectionnée.

![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"}

## Score de probabilité {#purchase_score}

Les utilisateurs de l'audience de prédiction se verront attribuer un score de probabilité compris entre 0 et 100. Plus le score est élevé, plus la probabilité de réaliser l'événement est grande.

Voici comment un utilisateur est classé en fonction de son score de probabilité :

- **Faible :** entre 0 et 50
- **Moyen :** entre 50 et 75
- **Élevé :** entre 75 et 100

Les scores et les catégories correspondantes seront mis à jour selon la planification que vous avez choisie dans la page de **création des prédictions**. Le nombre d'utilisateurs ayant des scores de probabilité dans chacun des 20 compartiments de taille égale ou dans chacune des catégories de probabilité est affiché dans le graphique en haut de la page.

### Accès aux scores de probabilité au niveau utilisateur {#accessing-user-level-likelihood-scores}

Pour consulter le score de probabilité d'un utilisateur individuel, recherchez cet utilisateur dans le tableau de bord et rendez-vous dans **Engagement** > **Predictions** afin de visualiser son score. Pour accéder aux scores et aux catégories de plusieurs utilisateurs à la fois, créez un [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) à l'aide des filtres [Score de probabilité d'événement]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#event-likelihood-score) ou [Catégorie de probabilité d'événement]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#event-likelihood-category), puis exportez les utilisateurs de ce segment. Lors de l'exportation, vous pouvez inclure les scores de probabilité dans les données exportées.

{% alert note %}
Bien que les événements prédictifs et [la prédiction du taux d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/) attribuent tous deux des scores aux utilisateurs, il existe des différences importantes :<br><br>

- **Événements prédictifs** (prédictions d'achat) : prennent en compte tous les utilisateurs de l'audience de prédiction, qu'ils aient déjà effectué l'événement cible ou non. Par exemple, une prédiction d'achat peut identifier les utilisateurs susceptibles d'effectuer leur premier achat.
- **Prédiction du taux d'attrition** : ne prend en compte que les utilisateurs ayant déjà effectué l'événement personnalisé. Les prédictions d'attrition identifient les utilisateurs qui ont déjà effectué une action et qui sont susceptibles de cesser de le faire. Un utilisateur qui ne s'est jamais connecté ne peut être considéré comme « désabonné » s'il ne se connecte pas.

Lors de l'exportation des scores de risque d'attrition à partir d'un segment, ces scores reflètent le modèle de prédiction d'attrition, qui diffère des modèles de prédiction des achats ou d'autres événements.
{% endalert %}

## Précision estimée {#estimated_results}

Dans la moitié droite du panneau situé sous le graphique, nous présentons des estimations de la précision attendue du ciblage de la partie de l'audience de prédiction que vous avez sélectionnée, de deux manières : combien d'utilisateurs sélectionnés sont censés réaliser l'événement, et combien sont censés ne pas le faire.

![L'audience sélectionnée et la précision estimée affichées dans le tableau de bord de Braze.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Susceptibles de réaliser l'événement {#expected-to-perform}

Vous pouvez utiliser la précision estimée pour vérifier combien d'utilisateurs sélectionnés sont censés effectuer l'événement.

La prédiction n'est pas parfaitement exacte — et aucune prédiction ne l'est jamais — ce qui signifie que Braze ne sera pas en mesure d'identifier chaque futur utilisateur susceptible de réaliser l'événement. Les scores de probabilité sont comme un ensemble de prédictions informées et fiables. La barre de progression indique combien de « vrais positifs » attendus dans l'audience de prédiction seront ciblés avec l'audience sélectionnée. Notez que nous nous attendons à ce que ce nombre d'utilisateurs réalise l'événement même si vous ne leur envoyez pas de message.

### Non susceptibles de réaliser l'événement {#not-expected-to-perform}

Vous pouvez utiliser la précision estimée pour vérifier combien d'utilisateurs sélectionnés sont susceptibles de ne pas réaliser l'événement.

Tous les modèles de machine learning font des erreurs. Il se peut que certains utilisateurs de votre sélection aient un score de probabilité élevé, mais qu'ils ne réalisent finalement pas l'événement. Si vous n'agissiez pas, ils ne réaliseraient pas l'événement. Ils seront de toute façon ciblés, il s'agit donc d'une erreur ou d'un « faux positif ». La largeur totale de cette deuxième barre de progression représente le nombre attendu d'utilisateurs qui n'effectueront pas l'événement, et la partie remplie représente ceux qui seront incorrectement ciblés avec la position actuelle du curseur.

À l'aide de ces informations, nous vous encourageons à décider du nombre de vrais positifs que vous souhaitez capturer, du nombre de faux positifs dont vous pouvez accepter le ciblage et du coût des erreurs pour votre entreprise. Si vous envoyez une promotion intéressante, vous pouvez cibler uniquement les non-acheteurs (faux positifs) en privilégiant le côté gauche du graphique. Vous pouvez également encourager les acheteurs réguliers (les vrais positifs) à acheter de nouveau en sélectionnant une section d'utilisateurs qui privilégie le côté droit du graphique.

## Qualité de prédiction {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Tableau de corrélation des événements {#correlation_table}

Cette analyse affiche les attributs ou les comportements des utilisateurs qui sont corrélés avec les événements dans l'audience de prédiction. Les attributs évalués sont l'âge, le pays, le sexe et la langue. Les comportements analysés comprennent les sessions, les achats, le montant total des dépenses, les événements personnalisés, ainsi que les Campaigns et les étapes Canvas reçues au cours des 30 derniers jours.

Les tableaux sont divisés en deux parties, gauche et droite, respectivement pour les utilisateurs les plus et les moins susceptibles de réaliser l'événement. Pour chaque ligne, le ratio par lequel les utilisateurs ayant le comportement ou l'attribut dans la colonne de gauche sont plus ou moins susceptibles de réaliser l'événement est affiché dans la colonne de droite. Ce nombre est le rapport entre les scores de probabilité des utilisateurs ayant ce comportement ou cet attribut et la probabilité de réaliser l'événement sur l'ensemble de l'audience de prédiction.

Ce tableau n'est mis à jour que lorsque la prédiction se réentraîne, et non lorsque les scores de probabilité des utilisateurs sont mis à jour.

{% alert note %}
Les données de corrélation pour les aperçus de prédictions seront partiellement masquées. Un achat est requis pour révéler ces informations. Contactez votre gestionnaire de compte pour plus d'informations.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

### Impossible de créer une prédiction {#unable-to-create-a-prediction}

Si vous ne parvenez pas à créer une prédiction pour un événement personnalisé, cela peut être dû à un échantillon de taille insuffisante. Braze estime le nombre d'utilisateurs ayant effectué l'événement. Si un nombre insuffisant d'utilisateurs a effectué l'événement, l'échantillon peut ne pas fournir suffisamment de données pour entraîner le modèle. Dans ce cas, le système peut extrapoler à zéro utilisateur, empêchant ainsi la création de la prédiction.

Pour créer une prédiction avec succès, assurez-vous qu'un nombre suffisant d'utilisateurs dans votre audience de prédiction ont effectué votre événement personnalisé cible. Le seuil exact varie, mais les événements très peu utilisés par votre base d'utilisateurs peuvent ne pas fournir suffisamment de données pour un entraînement fiable du modèle.