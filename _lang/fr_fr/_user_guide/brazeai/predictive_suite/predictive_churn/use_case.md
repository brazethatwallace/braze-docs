---
nav_title: Cas d'utilisation
article_title: "Cas d'utilisation : réduire l'attrition grâce à un contenu opportun"
description: "Cet exemple illustre comment une marque fictive utilise Predictive Churn pour réduire de manière proactive le taux d'abandon des utilisateurs."
page_type: tutorial
---

# Cas d'utilisation : réduire l'attrition grâce à un réengagement opportun par le contenu {#use-case-reduce-churn-with-timely-content-re-engagement}

> Cet exemple illustre comment une marque fictive utilise Predictive Churn pour réduire de manière proactive le taux d'abandon des utilisateurs. Au lieu d'attendre que l'attrition se produise, identifiez les utilisateurs à risque et envoyez-leur des messages personnalisés tant qu'ils sont encore actifs.

Supposons que Camila occupe le poste de gestionnaire CRM chez MovieCanon, une plateforme de streaming proposant des films indépendants, des documentaires et des séries internationales.

L'équipe de Camila a remarqué une tendance préoccupante : les utilisateurs s'inscrivent, regardent un ou deux films en streaming, puis disparaissent. Par le passé, ils ont tenté d'envoyer un e-mail générique « Vous nous manquez » une semaine plus tard, mais avec un taux de conversion de seulement 3 %, c'était trop peu et trop tard. La plupart des utilisateurs ne se réengagent pas, et l'attrition devient inévitable.

Camila souhaite changer cela. Au lieu de réagir à l'attrition après coup, elle utilise Predictive Churn pour identifier les utilisateurs susceptibles de devenir inactifs dans les 14 jours à venir, ce qui permet à son équipe de les réengager tant qu'ils sont encore actifs.

Ce tutoriel explique comment Camila :

- Élabore un modèle de prédiction d'attrition basé sur le comportement des utilisateurs
- Segmente les utilisateurs en fonction du niveau de risque
- Crée une campagne de réengagement adaptée aux personnes les plus à risque
- Évalue l'impact à l'aide des analyses de campagne

## Étape 1 : Créer un modèle de prédiction d'attrition {#step-1-create-a-churn-prediction-model}

Camila commence par modéliser le résultat qu'elle souhaite éviter : que les utilisateurs deviennent inactifs. Pour MovieCanon, l'attrition correspond au fait de ne pas démarrer de streaming dans les 14 jours. C'est donc ce comportement qu'elle souhaite prédire.

1. Dans le tableau de bord de Braze, Camila se rend dans **Analytics** > **Predictive Churn**.
2. Elle crée une nouvelle prédiction d'attrition et la nomme « Risque d'attrition dans deux semaines ».
3. Pour définir l'attrition, elle sélectionne `do not` et l'événement personnalisé `stream_started`, qui indique un engagement actif.
4. Elle définit la fenêtre de prédiction sur 14 jours, ce qui signifie que le modèle identifiera les utilisateurs susceptibles de passer 14 jours sans démarrer un nouveau streaming.

![Définition de l'attrition montrant qu'un utilisateur est considéré comme désabonné s'il n'a pas effectué l'événement personnalisé « stream_started » au cours des 14 derniers jours.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5. Elle sélectionne une audience de prédiction qui comprend tous les utilisateurs ayant déclenché des événements pertinents au cours des 30 derniers jours, fournissant ainsi au modèle suffisamment de comportements récents pour apprendre.
6. Elle définit la planification de mise à jour des prédictions sur une base hebdomadaire afin que les scores restent à jour.
7. Elle sélectionne **Create prediction**.

Le modèle commence alors l'apprentissage, en analysant des comportements tels que les sessions récentes, la fréquence de consultation et les interactions avec le contenu afin de mettre en évidence les schémas permettant de prédire les abandons. Une heure plus tard, Camila reçoit un e-mail l'informant que sa prédiction a terminé son apprentissage. Elle l'ouvre dans Braze et vérifie le score de [qualité de la prédiction]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics#prediction_quality). Il est étiqueté « Bon », ce qui signifie que les prédictions du modèle sont susceptibles d'être précises et fiables. Confiante dans les performances du modèle, elle poursuit.

## Étape 2 : Segmenter les utilisateurs en fonction du risque d'attrition {#step-2-segment-users-by-churn-risk}

Une fois le modèle entraîné, Braze attribue à chaque utilisateur éligible un [score de risque d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics#churn_score) compris entre 0 et 100.

Pour déterminer un seuil de départ pour le ciblage, Camila utilise le curseur d'audience de prédiction afin de prévisualiser le nombre d'utilisateurs qui se situent dans chaque fourchette de score et la précision de la prédiction à ce niveau. Elle équilibre la couverture et la précision en fonction des vrais positifs attendus. Sur cette base, elle décide de cibler les scores de risque supérieurs à 70.

1. Camila accède à la section Segments dans Braze.
2. Elle crée un [segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) à l'aide du [filtre de score de risque d'attrition]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#churn-risk-score) et sélectionne la prédiction d'attrition qu'elle a créée :
   - **Susceptible de se désabonner :** score supérieur à 70

![Filtrage de segment pour les utilisateurs dont le score de risque d'attrition est supérieur à 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Étape 3 : Cibler les utilisateurs à risque avec du contenu récurrent de réengagement {#step-3-target-at-risk-users-with-recurring-re-engagement-content}

Une fois sa prédiction et son segment prêts, Camila met en place une campagne récurrente qui cible automatiquement les utilisateurs présentant un risque chaque semaine.

1. Camila crée une campagne récurrente et active le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), de sorte que chaque message soit envoyé au moment où chaque utilisateur est le plus susceptible d'interagir, plutôt que de se baser sur un jour et une heure fixes.
2. Elle cible le segment « Susceptible de se désabonner » qu'elle vient de créer.
3. Elle définit l'événement de conversion de la campagne sur l'événement personnalisé `stream_started`, afin de suivre le nombre d'utilisateurs qui reviennent effectivement pour consulter du contenu.
4. Camila privilégie l'e-mail comme canal principal, car il lui permet de mettre en avant plusieurs contenus personnalisés dans un format visuellement riche, sans trop de contraintes. L'e-mail comprend :
   - Une liste de favoris personnalisée alimentée par les [recommandations produit basées sur l'IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations), sélectionnées de manière dynamique à partir du catalogue de MovieCanon.
   - Un appel à l'action qui redirige directement vers l'application.

Cela garantit que chaque semaine, MovieCanon n'atteint que les utilisateurs qui ont besoin d'un petit coup de pouce, sans excès de messages ni conjectures.

### Exemple d'e-mail {#example-email}

- **Ligne d'objet :** Ne laissez pas ces titres en suspens
- **En-tête :** Votre prochaine pépite vous attend
- **Corps :** Vous n'avez pas appuyé sur lecture depuis un moment ? Pas d'inquiétude, nous avons sélectionné quelques suggestions spécialement pour vous. Des thrillers à suspense aux documentaires primés, il y a forcément quelque chose qui vous plaira.
- **CTA :** Voir plus de suggestions

## Étape 4 : Mesurer les performances {#step-4-measure-performance}

Après quelques semaines, Camila examine les [analyses de sa campagne]({{site.baseurl}}/user_guide/channels/email/reporting) afin d'évaluer l'efficacité de sa stratégie.

Elle constate :

- *Taux d'ouverture :* 31 %
- *Taux de clics :* 15 %
- *Taux de conversion* (streaming démarré dans les 48 heures) : 11 %

Par rapport à l'ancienne campagne « Vous nous manquez » (dont les taux de conversion avoisinaient les 3 %), ce nouveau flux réduit l'attrition dans le groupe cible de 28 %. Elle examine attentivement le [rapport d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports) afin d'identifier les points de désengagement des utilisateurs. Bien que les taux d'ouverture et de clics soient élevés, elle constate un léger décalage entre les clics et les conversions, ce qui l'incite à envisager de tester le texte des CTA ou d'expérimenter différentes mises en page.

Afin de comprendre l'impact à long terme, Camila suit également le nombre d'utilisateurs entrant dans le segment « Susceptible de se désabonner » chaque semaine. Cela lui permet d'évaluer la santé globale du cycle de vie et d'élaborer une stratégie de fidélisation à un niveau plus large. Enfin, elle consulte à nouveau la page [Analyses prédictives]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/analytics) de sa prédiction d'attrition pour comparer les désabonnés prévus et réels, ce qui constitue une vérification utile pour s'assurer que le modèle fonctionne comme prévu.

Sur la base de ces informations, Camila prévoit de réaliser des tests A/B sur les lignes d'objet, de tester différentes fenêtres temporelles et d'expérimenter différents formats de contenu, tels que des recommandations de type carrousel dans un message in-app.

Grâce à Predictive Churn, au timing intelligent et à la personnalisation basée sur l'intelligence artificielle, l'équipe de Camila ne se contente pas de réagir à l'attrition : elle la devance. Et sa campagne se déroule discrètement en arrière-plan, touchant les bonnes personnes, au bon moment, avec un contenu qui les intéresse réellement.