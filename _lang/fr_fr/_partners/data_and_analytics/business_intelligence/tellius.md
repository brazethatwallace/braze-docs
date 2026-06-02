---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "Cet article de référence présente le partenariat entre Braze et Tellius, une plateforme d'analyse augmentée et d'intelligence décisionnelle, vous permettant d'exploiter les données, sans faire appel à des ingénieurs BI, pour créer des tableaux de bord et générer des informations afin de prendre de meilleures décisions marketing."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/), une plateforme d'analyse augmentée et d'intelligence décisionnelle, vous permet d'interroger vos données à l'aide d'une recherche en langage naturel et d'approfondir le « pourquoi » grâce à des informations guidées par l'intelligence artificielle.

L'intégration de Braze et Tellius permet aux utilisateurs d'exploiter les données, sans faire appel à des ingénieurs BI, pour créer des tableaux de bord et générer des informations permettant de prendre de meilleures décisions marketing. Cette intégration nécessite que les données de Braze soient stockées dans Snowflake, où Tellius peut se connecter directement et transmettre des requêtes grâce à une intégration en production.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Tellius | Un compte Tellius est nécessaire pour profiter de ce partenariat. Vous pouvez vous familiariser avec Tellius dans le cadre d'un [essai gratuit](https://www.tellius.com/free-trial/)|
| Programme de partage de données Snowflake | Pour les clients existants de Snowflake, contactez votre conseiller Braze au sujet du programme de partage de données Snowflake afin d'intégrer vos données Braze dans votre instance Snowflake.|
| Compte de lecteur Snowflake | Si vous n'êtes pas client de Snowflake, contactez votre conseiller Braze pour obtenir un compte de lecteur Snowflake afin de pouvoir accéder à vos données Braze.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

### Étape 1 : Obtenir l'accès à Braze par l'intermédiaire de Snowflake {#step-1-obtain-access-to-braze-through-snowflake}

Braze stocke des données client granulaires dans Snowflake. Vous pouvez exploiter vos données Braze pour générer des informations grâce au programme de partage de données Snowflake de Braze ou en obtenant un compte de lecteur Snowflake.

Suivez les instructions de l'[intégration Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) pour la mise en place.

### Étape 2 : Connecter Tellius aux données de Braze dans Snowflake {#step-2-connect-tellius-to-braze-data-in-snowflake}

Connectez Tellius aux données de Braze dans Snowflake par l'une des méthodes suivantes :

- Accès direct : pour charger des données dans Tellius, suivez les instructions fournies dans l'article [Charger des ensembles de données](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- Accès OAuth : pour un accès OAuth à Snowflake, suivez les étapes décrites dans la section [Authentification OAuth](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Étape 3 : Créer une Business View dans Tellius à partir des données chargées {#step-3-create-business-view-in-tellius-from-loaded-data}

Pour commencer à utiliser la recherche en langage naturel et les informations automatisées, créez une [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) et sélectionnez des ensembles de données depuis votre connexion Snowflake.

### Étape 4 : Tirer le meilleur parti de vos données grâce à Tellius {#step-4-get-the-most-value-out-of-your-data-using-tellius}

Dans Tellius, une interface guidée vous permet de découvrir les fonctionnalités de la plateforme. Pour toute question ou explication complémentaire, consultez la [base de connaissances](https://help.tellius.com/) complète.