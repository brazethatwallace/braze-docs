---
nav_title: Analyse
article_title: "Analyse des recommandations d'articles"
description: "Découvrez les analyses des recommandations d'articles et comment les consulter dans Braze."
page_order: 1.3
---

# Analyse des recommandations d'articles {#item-recommendation-analytics}

> Découvrez les analyses des recommandations d'articles et comment les consulter dans Braze.

## Consulter les analyses {#view-analytics}

Vous pouvez consulter les analyses de votre recommandation pour voir quels articles ont été recommandés aux utilisateurs et dans quelle mesure le modèle de recommandation était précis.

1. Allez dans **Analytics** > **Item Recommendation**.
2. Sélectionnez votre recommandation dans la liste.

## Indicateurs disponibles {#available-metrics}

### Audience {#audience}

Ces indicateurs décrivent l'audience de votre recommandation. Selon le type de recommandation et les données d'analyse disponibles, la section **Audience** peut inclure les indicateurs **Précision** et **Couverture**.

Pour les recommandations **AI Personalized**, la carte **Type de recommandation** affiche le taux de personnalisation estimé, les utilisateurs ayant effectué l'événement configuré et la population totale. Pour les recommandations **Most Recent**, elle affiche la proportion d'utilisateurs recevant des recommandations **Most Recent** par rapport au repli **Most Popular**. Les recommandations **Most Popular** et **Trending** n'affichent pas de répartition par type de recommandation au niveau utilisateur.

![Indicateurs d'audience de recommandation montrant la précision, la couverture et les types de recommandation répartis entre les articles personnalisés et les plus populaires.]({% image_buster /assets/img/item_recs_analytics_1.png %}){: style="max-width:80%;"}

Consultez le tableau suivant pour plus d'informations :

| Indicateur              | Description |
| ------------------- | ---------- |
| **Précision**           | Le pourcentage de fois où le modèle a correctement deviné le prochain article qu'un utilisateur achèterait. La précision dépend fortement de la taille et de la composition spécifiques de votre catalogue, et doit être utilisée comme guide pour comprendre à quelle fréquence le modèle est correct.<br><br>Lors de tests précédents, les modèles ont obtenu de bons résultats avec des chiffres de précision allant de 6 à 20 %. Cet indicateur est mis à jour lors du prochain réentraînement du modèle.  |
| **Couverture**            | Le pourcentage d'articles disponibles dans le catalogue qui sont recommandés à au moins un utilisateur. Vous pouvez vous attendre à une couverture d'articles plus élevée avec les recommandations d'articles personnalisées qu'avec les plus populaires. |
| **Taux de personnalisation** | Pour les recommandations **AI Personalized**, le pourcentage estimé d'utilisateurs disposant de recommandations personnalisées stockées sur leur profil, calculé par rapport au nombre total d'utilisateurs ayant effectué l'événement configuré au cours des 24 derniers mois. Les utilisateurs ayant effectué l'événement mais ne disposant pas de suffisamment de données pour générer une recommandation personnalisée reçoivent les articles les plus populaires en repli lorsqu'ils sont contactés. |
| **Type de recommandation** | Pour les recommandations **Most Recent**, le pourcentage d'utilisateurs qui reçoivent des recommandations **Most Recent** par rapport au repli **Most Popular**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Audience" }

### Articles {#items}

Ce tableau inclut des indicateurs sur vos articles personnalisés, les plus récents et les plus populaires de votre catalogue.

![Tableaux côte à côte listant les articles attribués aux utilisateurs, séparés entre recommandations personnalisées et recommandations les plus populaires.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Consultez le tableau suivant pour plus d'informations :

| Indicateur              | Description |
| ------------------- | ---------- |
| **Articles personnalisés**<br><br>**Articles les plus récents** | Cette colonne liste chaque article du catalogue par ordre décroissant de fréquence de recommandation aux utilisateurs. Elle indique également combien d'utilisateurs se sont vu attribuer chaque article par le modèle.<br><br>Les articles **personnalisés** ou **les plus récents** sont listés selon le [type de recommandation]({{site.baseurl}}/user_guide/brazeai/item_recommendations). |
| **Articles les plus populaires** | Cette colonne liste chaque article du catalogue par ordre décroissant de popularité. La popularité fait ici référence aux articles du catalogue avec lesquels les utilisateurs interagissent le plus souvent dans l'ensemble de l'espace de travail. Les articles les plus populaires sont utilisés en repli lorsque les recommandations personnalisées ou les plus récentes ne peuvent pas être calculées pour un utilisateur individuel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Articles" }

### Aperçu {#overview}

Il s'agit d'un aperçu de la configuration de recommandation que vous avez choisie, incluant la date de dernière mise à jour de la recommandation.

![Tableau d'aperçu de la recommandation affichant le type, le catalogue, le type d'événement, le nom de l'événement personnalisé, le nom de la propriété et la date de dernière mise à jour.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }