---
nav_title: Comment Braze utilise Currents
article_title: Comment Braze utilise Currents
page_order: 6
page_type: tutorial
description: "Cet article « How to » sur Currents vous guidera dans le processus de base pour configurer les intakes appropriés pour les données d'événements, et pour les déplacer vers une base de données et un outil d'aide à la décision (BI)."
tool: Currents

---

# Comment Braze utilise Currents

> Braze utilise Currents en interne avec des [partenaires]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) sélectionnés.

Nous filtrons nos données issues des campagnes d'e-mail et de push dans un outil d'informations commerciales, Looker, mais il faut emprunter un chemin légèrement différent pour y parvenir. Nous utilisons une version inversée de la méthodologie Extraire, Transformer, Charger (ETL) — en changeant l'ordre en Extraire, Charger, Transformer (ELT).

## Étape 1 : Intake et agrégation des données d'événements

Après avoir lancé des campagnes à l'aide de l'un de nos outils d'engagement (comme les campagnes ou Canvas), nous suivons les données d'événements à l'aide de notre propre système ainsi que de certains de nos partenaires en matière d'e-mail. Certaines de ces données sont agrégées et affichées dans le tableau de bord, mais nous voulions creuser plus profond !

## Étape 2 : Envoi des données d'événements à un partenaire de stockage de données

Nous avons configuré Currents pour envoyer les données d'événements Braze à Amazon S3 pour stockage et extraction. Nous savons bien sûr que vous pouvez utiliser [Athena](https://aws.amazon.com/athena/) avec S3 pour lancer des requêtes. C'est une excellente solution à court terme. Mais nous voulions une solution à long terme utilisant une base de données relationnelle et un outil d'aide à la décision/d'analytique. (Nous vous recommandons la même approche.)

S3 offre des options de stockage et de routage flexibles pour déplacer, pivoter et analyser les données. Nous ne transformons pas les données dans S3 car nous maintenons une structure spécifique pour celles-ci.

## Étape 3 : Transformer les données d'événements avec une base de données relationnelle

Depuis S3, nous choisissons un entrepôt de données ([Snowflake Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) ou Snowflake Reader Accounts, dans notre cas). Nous y transformons les données, puis les envoyons vers Looker, où nous avons configuré des blocs qui structurent et organisent nos données.

Snowflake n'est pas la seule option d'entrepôt de données. D'autres options incluent [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE), et bien d'autres !

### Snowflake Reader Accounts

Les Snowflake Reader Accounts offrent aux utilisateurs l'accès aux mêmes données et fonctionnalités que le [Partage de données Snowflake]({{site.baseurl}}/partners/snowflake/), sans nécessiter de compte Snowflake ni de relation client avec Snowflake. Avec les Reader Accounts, Braze crée et partage vos données dans un compte et vous fournit des identifiants pour vous connecter et accéder à vos données. Ainsi, l'ensemble du partage de données et de la facturation d'utilisation est entièrement géré par Braze.

Pour en savoir plus, contactez votre gestionnaire de la satisfaction client.

#### Ressources supplémentaires
Pour des ressources utiles de suivi de l'utilisation, consultez les articles de Snowflake sur les [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html) et la [consultation de l'utilisation des crédits d'entrepôt](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## Étape 4 : Utiliser un outil d'aide à la décision (BI) pour manipuler vos données

Enfin, nous utilisons un outil BI pour analyser nos données, les transformer en graphiques et autres outils visuels, et bien plus encore grâce à [Looker et les blocs Looker](https://www.marketplace.looker.com/) afin de ne pas avoir à effectuer d'ETL ou d'ELT à chaque fois que les données transitent depuis Currents.

Envie de faire de même ? Consultez la documentation suivante pour obtenir plus d'informations et découvrir comment les utiliser pour créer votre base de données !

- [Bloc Comportement utilisateur](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloc Engagement des messages](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)