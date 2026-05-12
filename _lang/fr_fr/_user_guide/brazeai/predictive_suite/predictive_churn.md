---
nav_title: Predictive Churn
article_title: Prédiction du taux d'attrition
description: "Cette page présente Predictive Churn, un outil de la Predictive Suite de Braze qui vous permet de définir ce que signifie l'attrition pour votre entreprise, ainsi que les utilisateurs que vous souhaitez retenir."
page_order: 8
alias: /predictive_churn/
search_rank: 2
---

# Prédiction du taux d'attrition {#predictive-churn}

> Avec Predictive Churn, un outil de la Predictive Suite de Braze, vous pouvez définir ce que signifie l'attrition pour votre entreprise et identifier les utilisateurs que vous souhaitez fidéliser. Lorsque vous créez une prédiction, Braze entraîne un modèle de machine learning à l'aide d'[arbres de décision boostés par gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour reconnaître les utilisateurs à risque en analysant les schémas de comportement passé — aussi bien ceux des utilisateurs ayant abandonné que ceux qui sont restés.

{% alert tip %}
Pour plus d'informations, consultez [Définition de l'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn) et [Audience de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-3-filter-your-prediction-audience).
{% endalert %}

## À propos de Predictive Churn {#about-predictive-churn}

Une fois le modèle de prédiction créé, les utilisateurs de l'audience de prédiction se verront attribuer un [score de risque d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/#churn_score) compris entre 0 et 100, indiquant leur probabilité d'abandonner selon votre définition. Plus le score est élevé, plus il est probable que l'utilisateur se désabonne.

La mise à jour des scores de risque de l'audience de prédiction peut se faire à la [fréquence de votre choix]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-4-choose-the-update-frequency-for-churn-prediction). De cette manière, vous pouvez contacter les utilisateurs qui risquent de se désabonner avant qu'ils ne le fassent réellement et empêcher cela de se produire. En utilisant jusqu'à trois prédictions actives, vous pouvez exploiter Predictive Churn pour adapter des modèles individuels afin de prévenir l'attrition dans des segments spécifiques de vos utilisateurs que vous considérez comme les plus précieux.

![Un aperçu de l'attrition, comprenant une audience de prédiction passée entraînée à partir de données historiques. Cela contribue à prédire le risque d'attrition futur en mesurant l'audience prédite actuelle avec un score de risque d'attrition.]({% image_buster /assets/img/churn/churn_overview.png %})

## Accéder à Predictive Churn {#accessing-predictive-churn}

{% multi_lang_include brazeai/predictions_page_access.md %}

Avant d'acheter cette fonctionnalité, elle est disponible en mode prévisualisation. Ce mode vous permet de consulter une démonstration de prédiction d'attrition avec des données synthétiques et de créer un modèle de prédiction d'attrition basé sur vos données utilisateur à un instant donné. Cette prévisualisation ne vous permettra pas de cibler des utilisateurs pour l'envoi de messages en fonction du risque d'attrition et ne se mettra pas à jour régulièrement après sa création.

Grâce à la prévisualisation, vous pouvez également modifier et reconstruire votre prédiction, ou l'archiver et en créer d'autres pour tester la [qualité de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics/) attendue de différentes [définitions]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/creating_a_churn_prediction/#step-2-define-churn).