---
nav_title: Analyse
article_title: "Analyse des recommandations d'articles"
description: "Découvrez les analyses des recommandations d'articles et comment les consulter dans Braze."
page_order: 1.3
---

# Analyse des recommandations d'articles {#item-recommendation-analytics}

> Découvrez les analyses des recommandations d'articles et comment les consulter dans Braze.

## Consulter les analyses {#viewing-analytics}

Vous pouvez consulter les analyses de votre recommandation pour voir quels articles ont été recommandés aux utilisateurs et quelle a été la précision du modèle de recommandation.

1. Allez dans **Analytics** > **Item Recommendation**.
2. Sélectionnez votre recommandation dans la liste.

## Indicateurs disponibles {#available-metrics}

### Audience {#audience}

Il s'agit d'indicateurs liés à l'audience de votre recommandation, qui comprennent la précision, la couverture et le type de recommandation.

![Indicateurs d'audience des recommandations affichant la précision, la couverture et les types de recommandations répartis entre les articles personnalisés et les articles les plus populaires.]({% image_buster /assets/img/item_recs_analytics_1.png %})

Pour plus d'informations, reportez-vous au tableau suivant :

| Indicateur | Description |
| ------------------- | ---------- |
| **Précision** | Le pourcentage de fois où le modèle a correctement deviné le prochain article acheté par un utilisateur. La précision dépend fortement de la taille et de la composition de votre catalogue spécifique, et doit être utilisée comme guide pour comprendre à quelle fréquence le modèle est correct.<br><br>Lors de tests antérieurs, nous avons constaté que les modèles fonctionnaient bien avec des valeurs de précision allant de 6 à 20 %. Cet indicateur est mis à jour lors du prochain réentraînement du modèle. |
| **Couverture** | Le pourcentage d'articles disponibles dans le catalogue qui sont recommandés à au moins un utilisateur. Vous pouvez vous attendre à une couverture d'articles plus élevée avec des recommandations d'articles personnalisées par rapport aux articles les plus populaires. |
| **Type de recommandation** | Le pourcentage d'utilisateurs qui recevront des recommandations personnalisées ou les plus récentes par rapport à la solution de repli des articles les plus populaires. La solution de repli est envoyée aux utilisateurs qui ne disposent pas de suffisamment de données pour générer une recommandation personnalisée ou la plus récente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Audience" }

### Articles {#items}

Ce tableau comprend des indicateurs sur les articles personnalisés, les plus récents et les plus populaires de votre catalogue.

![Tableaux côte à côte répertoriant les articles attribués aux utilisateurs, séparés par recommandations personnalisées et recommandations les plus populaires.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Pour plus d'informations, reportez-vous au tableau suivant :

| Indicateur | Description |
| ------------------- | ---------- |
| **Articles personnalisés**<br><br>**Articles les plus récents** | Cette colonne répertorie chaque article du catalogue par ordre décroissant de fréquence de recommandation aux utilisateurs. Elle indique également le nombre d'utilisateurs auxquels le modèle a attribué chaque article.<br><br>Les articles **personnalisés** ou les **plus récents** seront affichés en fonction du [type de recommandation]({{site.baseurl}}/user_guide/brazeai/item_recommendations). |
| **Articles les plus populaires** | Cette colonne présente chaque article du catalogue par ordre décroissant de popularité. La popularité fait ici référence aux articles du catalogue avec lesquels les utilisateurs interagissent le plus souvent dans l'ensemble de l'espace de travail. Les articles les plus populaires sont utilisés comme solution de repli lorsque les recommandations personnalisées ou les plus récentes ne peuvent pas être calculées pour un utilisateur individuel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Articles" }

### Aperçu {#overview}

Il s'agit d'un aperçu de la configuration de recommandation que vous avez choisie, qui comprend la date de la dernière mise à jour de la recommandation.

![Tableau d'aperçu des recommandations affichant le type, le catalogue, le type d'événement, le nom de l'événement personnalisé, le nom de la propriété et la date de la dernière mise à jour.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }