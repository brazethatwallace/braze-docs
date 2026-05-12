---
nav_title: Cas d'utilisation
article_title: "Cas d'utilisation : prévoir les mises à niveau d'abonnement"
description: "Cet exemple illustre comment une marque fictive utilise Braze Predictive Events pour définir les résultats qui comptent pour son activité, comme la mise à niveau vers un abonnement pro, et créer des stratégies ciblées qui améliorent les résultats."
page_type: tutorial
---

# Cas d'utilisation : prévoyez les mises à niveau d'abonnement grâce à un ciblage plus intelligent {#use-case-predict-subscription-upgrades-with-smarter-targeting}

> Cet exemple illustre comment une marque fictive utilise Braze Predictive Events pour définir les résultats qui comptent pour son activité, comme la mise à niveau vers un abonnement pro, et créer des stratégies ciblées qui améliorent les résultats.

Supposons que Jordan soit stratège en cycle de vie chez Steppington, une application de santé et de remise en forme proposant des formules gratuites et payantes. L'équipe de Jordan a pour objectif d'augmenter le nombre de mises à niveau vers le forfait Pro sans inonder l'ensemble de ses utilisateurs gratuits de messages promotionnels. Actuellement, ils envoient une promotion « Essayez la version Pro à 50 % de réduction » à tous les utilisateurs de la version gratuite après sept jours. Bien que cela génère certaines conversions (environ 5 % sur 7 jours), cela entraîne également une portée excessive, notamment en accordant des remises à des utilisateurs qui auraient probablement effectué la mise à niveau de toute façon.

Afin d'améliorer le ciblage et de réduire la lassitude liée à l'envoi de messages, Jordan utilise Predictive Events pour modéliser la probabilité qu'un utilisateur passe à la version Pro dans les 7 prochains jours. Il définit un événement personnalisé : `upgraded_to_pro`, puis l'utilise pour entraîner un modèle de prédiction et répartir les utilisateurs en groupes intelligents et orientés vers l'action.

Ce tutoriel explique comment Jordan a créé :

- Un modèle prédictif pour `upgraded_to_pro` dans les 7 prochains jours
- Des segments qui contribuent à augmenter les conversions tout en réduisant le nombre total de messages envoyés

## Étape 1 : créer un modèle prédictif pour les mises à niveau {#step-1-create-a-predictive-model-for-upgrades}

Jordan commence par définir le résultat le plus important pour sa stratégie de mise à niveau : un utilisateur passant de la version gratuite à la version Pro. Plutôt que de s'appuyer sur des déclencheurs génériques tels que « le temps écoulé depuis l'inscription », il souhaite prévoir quels utilisateurs sont réellement susceptibles de se convertir. De cette manière, son équipe peut agir sur la base de signaux réels, et non pas seulement d'hypothèses.

1. Dans le tableau de bord de Braze, Jordan accède à **Analytics** > **Predictive Events**.
2. Il [crée une nouvelle prédiction d'événement]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/) et la nomme « Passer à la version Pro en 7 jours ».
3. Comme événement cible, il sélectionne son événement personnalisé : `upgraded_to_pro`.
4. Jordan définit la fenêtre de prédiction sur 7 jours, établit une planification de mise à jour et crée la prédiction.

![Paramètres de prédiction indiquant la définition, la fenêtre, l'audience et la planification de mise à jour de la prédiction.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Étape 2 : segmenter les utilisateurs en fonction de la probabilité de mise à niveau {#step-2-segment-users-based-on-upgrade-probability}

Une fois l'entraînement terminé, Braze attribue un [score de probabilité d'événement]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/analytics/#purchase_score) (0-100) à chaque utilisateur éligible. Jordan utilise ce score pour créer des segments exploitables : l'un pour les utilisateurs ayant une forte intention de conversion qui n'ont peut-être pas besoin de remise, et l'autre pour les utilisateurs qui ne se convertiront probablement pas sans aide.

1. Jordan accède à la section Segments dans Braze.
2. Il crée deux [segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) à l'aide du [filtre Event Likelihood Score]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#event-likelihood-score) et sélectionne la prédiction qu'il a créée. Les deux segments sont les suivants :
  - **Susceptible de passer à la version supérieure :** score supérieur à 70
  - **A besoin d'un coup de pouce pour passer à la version supérieure :** score supérieur à 40 et inférieur à 70

{% alert tip %}
Les filtres prédictifs peuvent être combinés avec n'importe quel autre attribut ou comportement utilisateur. Jordan prévoit d'affiner davantage ces segments en fonction des intérêts des utilisateurs, par exemple en accordant la priorité aux utilisateurs qui utilisent fréquemment les fonctionnalités de suivi de la condition physique. Cela lui permet de cibler plus précisément quatre sous-groupes, afin d'adapter le contenu et l'envoi de messages aux besoins de chaque utilisateur.
{% endalert %}

![Générateur de segments avec deux filtres pour le score de probabilité d'événement.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Étape 3 : personnaliser l'envoi de messages en fonction du niveau d'intention {#step-3-personalize-messaging-by-intent-level}

Maintenant que Jordan dispose de signaux clairs indiquant une intention de mise à niveau et de sous-groupes affinés en fonction du comportement des utilisateurs, il élabore une stratégie d'envoi de messages qui s'adapte aux besoins de chaque utilisateur. Fini les envois standardisés.

Il choisit l'e-mail comme canal principal pour cette Campaign. Pourquoi ? Parce que Jordan souhaite expliquer la valeur ajoutée de Pro aux utilisateurs ayant une forte intention et convaincre les utilisateurs plus hésitants, ce qui nécessite de l'espace, des visuels et un appel à l'action percutant. L'e-mail lui offre la flexibilité nécessaire pour y parvenir sans exercer de pression sur les utilisateurs, et lui permet de suivre les performances grâce au comportement des clics.

Jordan [crée un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) qui divise l'expérience en fonction des segments qu'il vient de créer. Il ajoute une étape Parcours d'audience pour cibler :

- Les utilisateurs ayant une forte intention, axés sur le fitness
- Les utilisateurs ayant une forte intention, autres profils
- Les utilisateurs ayant une faible intention, axés sur le fitness
- Les utilisateurs ayant une faible intention, autres profils

![Parcours d'audience Canvas avec quatre parcours pour chaque type d'intention.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Il définit également l'événement de conversion du Canvas sur l'événement personnalisé `upgraded_to_pro`, de sorte que Braze suit automatiquement les conversions de mise à niveau à mesure que les utilisateurs progressent dans le flux.

### Exemples de messages par parcours {#example-messages-per-path}

{% tabs %}
{% tab Forte intention, fitness %}

Ces utilisateurs sont déjà actifs et très impliqués dans les fonctionnalités de suivi de la condition physique. Ils sont susceptibles de passer à la version supérieure sans incitations supplémentaires. Le message met donc l'accent sur la découverte d'informations plus approfondies et d'outils avancés qui s'appuient sur leurs habitudes existantes.

- **Ligne d'objet :** Allez plus loin dans vos objectifs de remise en forme
- **En-tête :** Vos progrès méritent la version Pro
- **Corps :** Vous avez déjà construit une routine solide. Avec Pro, vous pouvez aller plus loin : suivez vos progrès pour chaque groupe musculaire, fixez-vous des objectifs de performance hebdomadaires et accédez à des analyses avancées adaptées à votre façon de bouger.
- **CTA :** Commencez votre essai gratuit de la version Pro

{% endtab %}
{% tab Forte intention, autre %}
Ces utilisateurs manifestent un engagement fort, par exemple en consultant les fonctionnalités Pro ou en utilisant fréquemment l'application, mais ne se concentrent pas spécifiquement sur le suivi de leur condition physique. Le message met en avant les avantages plus généraux de Pro, tels que le coaching et la personnalisation, afin de les inciter à franchir le pas.

- **Ligne d'objet :** Vous y êtes presque — Pro est prêt quand vous l'êtes
- **En-tête :** Découvrez de nouvelles façons de bouger
- **Corps :** Vous avez exploré ce que Pro a à offrir. C'est le moment d'accéder à des programmes personnalisés, à des contenus de coaching individuel et à des programmes guidés conçus pour répondre à vos objectifs uniques, qu'il s'agisse de force, d'équilibre ou de régularité.
- **CTA :** Commencez votre essai gratuit de la version Pro

{% endtab %}
{% tab Faible intention, fitness %}
Ces utilisateurs s'intéressent aux fonctionnalités de fitness, mais n'ont pas encore entrepris de démarches pour passer à la version supérieure. Le message met l'accent sur leurs intérêts en matière de fitness tout en réduisant les frictions grâce à une offre à durée limitée, les aidant à considérer Pro comme un moyen peu risqué d'améliorer leur routine.

- **Ligne d'objet :** Prêt à vous entraîner plus intelligemment ? Essayez Pro à 50 % de réduction
- **En-tête :** Votre mise à niveau d'entraînement vous attend
- **Corps :** Pro vous fournit tout ce dont vous avez besoin pour démarrer efficacement : des programmes d'entraînement faciles à suivre, des conseils d'experts et un suivi réel de vos progrès. Essayez-le dès maintenant avec 50 % de réduction et résiliez à tout moment.
- **CTA :** Bénéficiez de 50 % de réduction sur Pro

{% endtab %}
{% tab Faible intention, autre %}

Ces utilisateurs présentent un engagement global minimal. Il est peu probable qu'ils passent à la version supérieure sans une incitation convaincante. Le message adopte donc une approche simple, axée sur les avantages, avec une remise et un ton modéré pour les inviter à explorer l'offre sans pression.

- **Ligne d'objet :** 50 % de réduction sur Pro — uniquement ce week-end
- **En-tête :** Prêt quand vous l'êtes
- **Corps :** Créez votre premier programme de remise en forme personnalisé, suivez vos progrès et accédez à des entraînements exclusifs, le tout à moitié prix. Essayez Pro à moindre coût et résiliez à tout moment.
- **CTA :** Bénéficiez de 50 % de réduction sur Pro

{% endtab %}
{% endtabs %}

## Étape 4 : mesurer les résultats et optimiser votre stratégie {#step-4-measure-results-and-optimize-your-strategy}

Une fois la Campaign terminée, Jordan examine les performances dans [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) afin de comprendre l'efficacité des parcours personnalisés et de déterminer si la combinaison de l'intention prédictive et des signaux comportementaux a amélioré les taux de mise à niveau.

Performances des e-mails par parcours :

- **Forte intention, fitness**
   - *Taux d'ouverture :* 34 %
   - *Taux de clics :* 20 %
   - *Taux de conversion :* 13 %
   - Aucune remise utilisée
- **Forte intention, autre**
   - *Taux d'ouverture :* 30 %
   - *Taux de clics :* 17 %
   - *Taux de conversion :* 11 %
   - Aucune remise utilisée
- **Faible intention, fitness**
   - *Taux d'ouverture :* 27 %
   - *Taux de clics :* 12 %
   - *Taux de conversion :* 8 %
   - Offre de réduction de 50 % incluse
- **Faible intention, autre**
   - *Taux d'ouverture :* 23 %
   - *Taux de clics :* 9 %
   - *Taux de conversion :* 6 %
   - Offre de réduction de 50 % incluse

Par rapport à la Campaign précédente de l'équipe, qui était uniforme (une remise générale après 7 jours n'avait généré que 5 % de conversions et un excès d'envoi de messages), l'approche ciblée montre une amélioration significative dans tous les groupes, avec une efficacité accrue et moins de remises inutiles.

Le [rapport d'entonnoir]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) montre également une nette réduction du taux d'abandon à chaque étape clé, en particulier chez les utilisateurs ayant une faible intention qui ont reçu des messages personnalisés. De plus en plus d'utilisateurs ouvrent, cliquent et effectuent des mises à niveau, ce qui démontre la valeur du ciblage basé sur l'intention.

Jordan utilise ces informations pour :

- Explorer des tests A/B sur les lignes d'objet et la formulation des CTA
- Réévaluer le seuil de remise pour les utilisateurs ayant une intention modérée
- Continuer à affiner les segments en fonction de comportements supplémentaires tels que les consultations de contenu ou l'utilisation des fonctionnalités de l'application

Grâce à Predictive Events et à la segmentation par couches, son équipe dispose désormais d'une stratégie évolutive qui adapte les messages en fonction de l'intention et du comportement des utilisateurs, favorisant les mises à niveau tout en préservant la confiance envers la marque.