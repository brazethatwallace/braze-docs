---
nav_title: Cas d'utilisation
article_title: "Cas d'utilisation : favoriser la découverte de contenu après le visionnage"
description: "Cet exemple illustre comment une marque fictive utilise les recommandations produit basées sur l'IA de Braze pour proposer du contenu personnalisé et des suggestions de produits à des moments clés pour les clients."
page_type: tutorial
---

# Cas d'utilisation : favoriser la découverte de contenu après le visionnage {#use-case-drive-content-discovery-after-viewing}

> Cet exemple illustre comment une marque fictive utilise les recommandations produit basées sur l'IA de Braze pour proposer du contenu personnalisé et des suggestions de produits à des moments clés pour les clients. Découvrez comment la logique de recommandation peut améliorer l'engagement, augmenter les conversions et réduire les efforts manuels.

Supposons que Camila occupe le poste de gestionnaire CRM chez MovieCanon, une plateforme de streaming proposant une sélection de films et de séries.

L'objectif de Camila est de maintenir l'intérêt des spectateurs après qu'ils ont terminé de regarder un contenu. Historiquement, les messages « Vous pourriez également aimer » de MovieCanon étaient basés sur une correspondance de genre large et envoyés à des moments arbitraires, souvent plusieurs heures ou jours après une session. L'engagement était faible, et son équipe savait qu'elle pouvait faire mieux.

Grâce aux [recommandations produit basées sur l'IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai), Camila met en place un système qui recommande automatiquement de nouveaux titres en fonction de l'historique de visionnage de chaque spectateur, immédiatement après qu'un utilisateur a terminé un film ou un épisode. C'est une méthode plus intelligente et plus personnalisée pour aider les utilisateurs à découvrir le contenu qu'ils souhaitent réellement regarder ensuite et les fidéliser à la plateforme.

![Message in-app indiquant « À suivre, rien que pour vous. Parce que vous avez regardé "Nomads of the Sun" », avec une image, un titre, une description et un appel à l'action « Regarder maintenant » ou « Passer » pour accéder à la recommandation suivante.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Ce tutoriel explique comment Camila met en place :

- Un message personnalisé déclenché lorsqu'un utilisateur termine de visionner un contenu
- Des recommandations adaptées aux préférences du spectateur, automatiquement extraites du catalogue MovieCanon et intégrées au message

## Étape 1 : Créer une recommandation {#step-1-create-a-churn-prediction-model}

Camila commence par créer une recommandation qui affichera des titres pertinents chaque fois qu'un utilisateur aura terminé de regarder un contenu. Elle souhaite que ce soit dynamique, afin que les utilisateurs reçoivent différentes suggestions en fonction de ce qu'ils ont récemment regardé.

1. Dans le tableau de bord de Braze, Camila accède à **AI Item Recommendations**.
2. Elle crée une nouvelle recommandation et la nomme « Suggestions après visionnage ».
3. Pour le type de recommandation, elle choisit **AI Personalized**, de sorte que chaque utilisateur voit des recommandations adaptées en fonction de ses comportements passés.
4. Elle sélectionne **Do not recommend items users have previously interacted with** afin que les utilisateurs ne reçoivent pas de recommandations pour des contenus qu'ils ont déjà visionnés.
5. Elle sélectionne le catalogue contenant la bibliothèque de contenu actuelle de MovieCanon. Camila n'ajoute pas de sélection au catalogue, car elle souhaite que tous les articles du catalogue puissent être recommandés.
6. Camila associe la recommandation à l'événement personnalisé `Watched Content`, qui suit les visionnages terminés, et définit le **Property Name** sur le titre du contenu.
7. Elle crée la recommandation.

## Étape 2 : Configurer un message in-app {#step-2-set-up-an-in-app-message}

Une fois l'entraînement de la recommandation terminé, Camila crée un flux d'envoi de messages qui atteint l'utilisateur au moment opportun : immédiatement après qu'il a terminé un titre. Le message comprend une liste de trois suggestions personnalisées extraites directement du catalogue.

1. Camila crée une campagne de messages in-app à l'aide de l'éditeur par glisser-déposer.
2. Elle définit le déclencheur sur son événement personnalisé : `Watched Content`.
3. Elle conçoit un message in-app de plusieurs pages avec des images de titre, des noms et un CTA « Regarder maintenant ».

![Fenêtre modale « Ajouter une personnalisation » ouverte dans l'éditeur Braze, avec « Recommandation d'articles » sélectionné comme type de personnalisation.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. Dans le corps du message, Camila utilise la [fenêtre modale Ajouter une personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-pre-formatted-variables) pour ajouter des variables telles que le nom, la description et la vignette du titre recommandé à l'aide de Liquid, qui remplit dynamiquement le contenu à partir du catalogue. Elle crée un modèle avec un attribut personnalisé pour `Last Watched Movie` afin d'informer les utilisateurs que cette recommandation est basée sur leur historique de visionnage.

![Éditeur de messages in-app avec du Liquid brut pour intégrer des champs spécifiques à partir des articles du catalogue issus de la recommandation.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Afficher le Liquid utilisé dans l'image %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. Camila duplique ensuite sa page et incrémente le tableau Liquid {% raw %} (`{{ items[0]}}` vers `{{items[1]}}`) {% endraw %} dans chaque variable pour intégrer l'élément suivant de la liste de recommandations.

## Étape 3 : Mesurer et optimiser {#step-3-measure-and-optimize}

Une fois la campagne en ligne, Camila surveille les taux d'ouverture, les CTR et le comportement de visionnage ultérieur. Elle compare les performances par rapport aux précédentes campagnes de recommandations statiques et constate un engagement plus élevé, ainsi qu'un plus grand nombre de sessions de contenu par utilisateur.

Elle prévoit également de réaliser un test A/B sur :

- Le moment d'envoi (immédiatement ou 10 minutes après le visionnage)
- La disposition du contenu (carrousel ou liste)
- Les variantes de CTA (« Regarder maintenant » ou « Ajouter à la file d'attente »)

En associant l'envoi de messages événementiels aux recommandations produit basées sur l'IA, Camila transforme la découverte de contenu en une expérience automatisée et personnalisée. MovieCanon maintient l'intérêt des utilisateurs sans laisser place au hasard, en leur proposant du contenu pertinent au moment opportun afin d'approfondir les sessions et de réduire l'attrition.