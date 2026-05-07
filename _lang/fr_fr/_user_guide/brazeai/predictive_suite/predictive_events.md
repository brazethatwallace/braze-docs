---
nav_title: Predictive Events
article_title: Predictive Events
description: "Cet article traite de Predictive Events (anciennement Predictive Purchases), un outil de la Predictive Suite de Braze qui permet aux marketeurs d'identifier les utilisateurs et de leur envoyer des messages en fonction de leur probabilité de réaliser un événement."
page_order: 9
alias: /predictive_purchases/
search_rank: 1
---

# Predictive Events {#predictive-events}

> Predictive Events est un outil performant de la Predictive Suite de Braze qui permet d'identifier et d'envoyer des messages aux utilisateurs en fonction de leur probabilité de réaliser un événement. Lorsque vous créez une prédiction d'événement, Braze entraîne un modèle de machine learning à l'aide d'[arbres de décision boostés par le gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l'activité passée et prédire l'activité future.

## À propos de Predictive Events {#about-predictive-events}

Une fois la prédiction créée, les utilisateurs se voient attribuer un [score de vraisemblance]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#purchase_score) compris entre 0 et 100, indiquant la probabilité qu'ils réalisent l'événement sélectionné. Plus le score est élevé, plus l'utilisateur est susceptible de réaliser cet événement. Les utilisateurs sont également classés par catégories de probabilité faible, moyenne et élevée.

La véritable valeur de Predictive Events réside dans l'utilisation des résultats de prédiction pour créer un segment ou une Campaign. Les marketeurs peuvent créer des Campaigns ciblées directement sur la page **Prediction** pour obtenir des résultats immédiats en termes de chiffre d'affaires, ou enregistrer un segment pour une future Campaign ou un Canvas. Vous ne savez pas qui cibler en premier ? Consultez nos [considérations stratégiques]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) pour l'envoi de messages aux utilisateurs en fonction de leur score de probabilité.

![Graphique intitulé « Comment fonctionne Predictive Events », montrant les données utilisateur alimentant le modèle de machine learning. Le libellé indique : « Entraînez le modèle avec des données historiques, comparez le comportement des utilisateurs ayant réalisé l'événement au cours d'une certaine période avec ceux qui ne l'ont pas fait. » Il montre également les résultats du machine learning, où les utilisateurs sont classés du moins susceptible au plus susceptible de réaliser l'événement. Le libellé indique : « Prédire la probabilité d'événements futurs, attribuer un score de probabilité aux utilisateurs pour un ciblage précis et pratique. »]({% image_buster /assets/img/how_predictive_events_works.png %})

## Accéder à Predictive Events {#accessing-predictive-events}

{% multi_lang_include brazeai/predictions_page_access.md %}

Avant l'achat de cette fonctionnalité, elle est disponible en mode prévisualisation. Cela vous permet de consulter une prédiction de démonstration avec des données synthétiques et de créer un modèle de prédiction en prévisualisation à la fois. Cette prédiction sera créée à partir de vos données utilisateur réelles, mais elle ne vous permettra pas de cibler les utilisateurs pour l'envoi de messages en fonction de leur score de probabilité. Elle ne sera pas non plus mise à jour régulièrement après sa création.

Avec la prévisualisation, vous pouvez également modifier et reconstruire cette prédiction, ou l'archiver et en créer d'autres pour tester la [qualité de prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#prediction_quality) attendue de [différentes audiences]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) et vous familiariser avec les analyses.