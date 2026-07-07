---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: "/partners/amazon_personalize_overview/"
description: "Cet article de référence décrit une architecture de référence et une intégration entre Braze et Amazon Personalize. Cet article de référence vous aidera à comprendre les cas d'utilisation proposés par Amazon Personalize, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer à Braze."
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> [Amazon Personalize](https://aws.amazon.com/personalize/), c'est comme si vous aviez votre propre système de recommandation par machine learning d'Amazon, disponible en permanence. S'appuyant sur plus de 20 ans d'expérience en matière de recommandations, Amazon Personalize vous permet d'améliorer l'engagement client en proposant des recommandations personnalisées de produits et de contenus en temps réel, ainsi que des promotions marketing ciblées.

_Cette intégration est gérée par Amazon Personalize._

## À propos de l'intégration {#about-the-integration}

À l'aide du machine learning et d'un algorithme que vous aidez à définir, Amazon Personalize peut vous aider à entraîner un modèle qui génère des recommandations de haute qualité pour vos sites web et applications. Ces modèles vous permettent de créer des listes de recommandations en fonction des comportements antérieurs des utilisateurs, de trier les éléments par pertinence et de recommander d'autres éléments en fonction de leur similitude. Les listes obtenues à partir de l'API Amazon Personalize peuvent ensuite être utilisées dans le contenu connecté de Braze pour lancer des campagnes de recommandation Braze personnalisées. Grâce à l'intégration avec Amazon Personalize, les clients ont la liberté de contrôler les paramètres utilisés pour entraîner les modèles et de définir des objectifs commerciaux facultatifs qui optimisent les résultats de l'algorithme.

Cet article de référence vous aidera à comprendre les cas d'utilisation proposés par Amazon Personalize, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer à Braze.

## Conditions préalables {#prerequisites}

| Condition | Description |
| --- | --- |
| Compte Amazon Web Service | Un compte AWS est nécessaire pour bénéficier de ce partenariat. Une fois que vous avez un compte AWS, vous pouvez accéder à Amazon Personalize via la console Amazon Personalize, l'interface de ligne de commande AWS (AWS CLI) ou les SDK AWS. |
| Cas d'utilisation définis | Avant de créer un modèle, vous devez déterminer votre cas d'utilisation pour cette intégration. Consultez la liste suivante pour les cas d'utilisation courants. |
| Ensembles de données | Les modèles de recommandation Amazon Personalize nécessitent trois types différents d'ensembles de données : interactions, utilisateurs et éléments. Consultez les informations suivantes pour connaître les exigences de chaque ensemble de données. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{% tabs %}
{% tab Use Cases %}

**Cas d'utilisation**

Avant de créer un modèle, vous devez déterminer votre cas d'utilisation pour cette intégration. Parmi les cas d'utilisation courants, citons :
- Recommander des articles aux utilisateurs en fonction de leurs interactions précédentes, afin de créer une expérience véritablement personnalisée pour vos utilisateurs.
- Fournir une liste d'articles ou de résultats de recherche adaptés à chaque utilisateur, en augmentant l'engagement en présentant les éléments en fonction de leur pertinence pour l'utilisateur.
- Trouver des recommandations pour des articles similaires, afin d'aider les utilisateurs à découvrir de nouvelles choses.

Dans le guide suivant, nous nous concentrerons sur la recette de recommandations personnalisées pour les utilisateurs.

{% endtab %}
{% tab Datasets %}

**Ensembles de données**

Pour commencer à utiliser les modèles de recommandation Amazon Personalize, vous avez besoin de trois types d'ensembles de données :

- Interactions
  - Stocke l'historique des interactions entre les utilisateurs et les éléments
  - Requiert les valeurs `USER_ID`, `ITEM_ID`, `EVENT_TYPE` et `TIMESTAMP` et accepte éventuellement les métadonnées relatives à l'événement
- Utilisateurs
  - Stocke les métadonnées relatives aux utilisateurs
  - Nécessite une valeur `USER_ID` et au moins un champ de métadonnées (chaîne de caractères ou numérique) tel que le sexe, l'âge ou l'adhésion au programme de fidélité
- Éléments
  - Stocke les métadonnées relatives aux éléments
  - Nécessite un `ITEM_ID` et au moins un champ de métadonnées (textuel, catégoriel ou numérique) qui décrit l'élément

Pour une recette de recommandations aux utilisateurs, vous devez fournir un ensemble de données d'interactions contenant au moins 1 000 points de données d'interaction provenant d'au moins 25 utilisateurs uniques ayant chacun au moins deux interactions. Ces ensembles de données peuvent être chargés en masse à l'aide de fichiers CSV stockés dans S3 ou de manière incrémentielle via l'API.

{% endtab %}
{% endtabs %}

## Création de modèles {#creating-models}

### Étape 1 : Entraînement {#step-1-training}

Une fois les ensembles de données importés, vous pouvez créer une solution. Une solution utilise l'une des [recettes](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (algorithmes) d'Amazon Personalize pour entraîner un modèle. Dans notre cas, nous utiliserons la recette `USER_PERSONALIZATION`. L'entraînement de la solution crée une version de la solution (modèle entraîné) que vous pouvez évaluer en fonction des indicateurs de performance du modèle.

Amazon Personalize vous permet d'ajuster les hyperparamètres utilisés par le modèle pour l'entraînement. Par exemple :
- Le paramètre « Percentile de longueur de l'historique utilisateur » de la console Amazon Personalize vous permet d'ajuster le percentile de l'historique utilisateur à inclure dans l'entraînement :<br><br>![Paramètre de profil utilisateur minimal et maximal]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile` : exclut un pourcentage d'utilisateurs dont l'historique est très court, ce qui peut être utile pour éliminer les articles les plus populaires et créer des recommandations basées sur des modèles sous-jacents plus approfondis.
  - `max_user_history_length_percentile` : ajuste le pourcentage d'utilisateurs à prendre en compte lors de l'entraînement avec un historique très long.

Le nombre de dimensions cachées permet de détecter des modèles plus complexes pour des ensembles de données complexes, tandis que la technique de rétropropagation dans le temps (BPTT) ajuste les récompenses pour un événement précoce après qu'une chaîne d'événements s'est produite et a donné lieu à une action de grande valeur.

En outre, Amazon Personalize permet de régler automatiquement les hyperparamètres en exécutant simultanément plusieurs versions de la solution avec différentes valeurs. Pour utiliser le réglage, activez l'option **Perform HPO** lors de la création d'une solution.

### Étape 2 : Évaluer et comparer {#step-2-evaluate-and-compare}

Une fois l'entraînement d'une solution terminé, vous êtes prêt à l'évaluer et à comparer les différentes versions. Chaque version de la solution affiche des indicateurs calculés. Parmi les indicateurs disponibles, citons :

- **Gain cumulé actualisé normalisé :** compare l'ordre recommandé des articles à la liste réelle des articles et attribue à chaque article un poids correspondant à sa position dans la liste
- **Precision @k :** la quantité d'articles correctement recommandés divisée par la quantité de tous les articles recommandés, où `k` est le nombre d'articles
- **Rang réciproque moyen :** se concentre sur la première recommandation la mieux classée et calcule le nombre d'éléments recommandés consultés avant l'apparition de la première recommandation correspondante
- **Couverture :** proportion d'éléments uniques recommandés par rapport au nombre total d'éléments uniques dans l'ensemble de données

## Obtenir des recommandations {#getting-recommendations}

Une fois que vous avez créé une version de solution qui vous convient, il est temps de mettre les recommandations en œuvre. Vous pouvez accéder aux recommandations de deux manières :

1. Campagne en temps réel<br>Une campagne est une version de solution déployée avec un débit de transactions minimal défini. Une transaction est un appel d'API unique pour obtenir une sortie de recommandation, et elle est définie en TPS (transactions par seconde), avec une valeur minimale de un. La campagne ajustera les ressources en cas d'augmentation de la charge, mais celles-ci ne tomberont pas en dessous de votre valeur minimale. Vous pouvez consulter les recommandations dans la console, dans l'interface de ligne de commande AWS ou via les SDK AWS dans votre code.<br><br>
2. Tâche par lots<br>Une tâche par lots exporte les recommandations vers un compartiment S3. La tâche prend en entrée un fichier JSON contenant la liste des ID d'utilisateur pour lesquels vous souhaitez exporter les recommandations. Ensuite, après avoir spécifié les autorisations appropriées et la destination de sortie, vous êtes prêt à exécuter la tâche. Le temps d'exécution dépend de la taille de vos ensembles de données et de la longueur de la liste des recommandations.

### Filtres {#filters}

Les filtres vous permettent d'ajuster la sortie des recommandations en excluant des éléments en fonction de leur ID, de leur type d'événement ou de leurs métadonnées. Vous pouvez également filtrer les utilisateurs en fonction de leurs métadonnées, telles que leur âge ou leur statut de membre du programme de fidélité. Les filtres peuvent s'avérer utiles pour empêcher de recommander des éléments avec lesquels l'utilisateur a déjà interagi.

## Intégrer les résultats avec Braze {#integrating-results-with-braze}

Avec le modèle créé et la campagne de recommandations, vous êtes prêt à lancer une campagne Braze pour vos utilisateurs à l'aide de Content Cards et du contenu connecté.
Avant de lancer une campagne Braze, vous devez créer un service capable de diffuser ces recommandations via une API. Vous pouvez suivre l'[étape 3 de l'article de l'atelier]({{site.baseurl}}/partners/amazon_personalize_workshop/#step-3-send-personalized-emails-from-braze) pour déployer le service à l'aide des services AWS. Vous pouvez également déployer votre propre service backend indépendant qui fournit les recommandations.

### Cas d'utilisation de la campagne de Content Cards {#content-card-campaign-use-case}

Lançons une campagne de Content Cards avec le premier élément recommandé de la liste.<br><br>
Dans les exemples suivants, nous allons interroger
l'endpoint `GET http://<service-endpoint.com>/recommendations?user_id=user123` avec un paramètre `user_id` qui renverra une liste d'articles recommandés :

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Dans le tableau de bord de Braze, créez une nouvelle [campagne de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/). Dans le champ de texte du message, créez un bloc Liquid de contenu connecté pour interroger l'API et enregistrer la réponse dans la variable `recommendations` :

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Vous pouvez ensuite référencer le premier élément du tableau obtenu et afficher le contenu à l'utilisateur :

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

En incluant le titre, l'image et le lien vers l'URL, voici à quoi ressemblerait la Content Card complète :

![Image d'une campagne avec du contenu connecté ajouté au corps du message et au champ « Ajouter une image ». Cette image montre également la logique de contenu connecté ajoutée au champ « Rediriger vers l'URL Web », reliant les utilisateurs à une URL de recommandation.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})