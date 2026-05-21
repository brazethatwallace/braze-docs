---
nav_title: Segmentation basée sur les comptes
article_title: Configurer la segmentation basée sur les comptes
page_order: 2
page_type: reference
description: "Découvrez comment utiliser les différentes fonctionnalités de Braze pour alimenter vos cas d'utilisation de segmentation basée sur les comptes B2B."
---

# Configurer la segmentation basée sur les comptes {#set-up-account-based-segmentation}

> Cette page explique comment utiliser diverses fonctionnalités de Braze pour répondre à vos cas d'utilisation de segmentation basée sur les comptes B2B.

Vous pouvez effectuer une segmentation B2B basée sur les comptes de deux manières, selon la façon dont vous avez configuré votre [modèle de données B2B]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/b2b_data_models/) :

- En utilisant des [catalogues pour vos objets métier](#option-1-when-using-catalogs-for-your-business-objects)
- En utilisant des [sources connectées pour vos objets métier](#option-2-when-using-connected-sources-for-your-business-objects)

## Mise en place de la segmentation B2B basée sur les comptes {#setting-up-b2b-account-based-segmentation}

### Option 1 : Utiliser des catalogues pour vos objets métier {#option-1-when-using-catalogs-for-your-business-objects}

#### Segmentation avec les modèles SQL de base {#basic-sql-template-segmentation}

Pour vous aider à démarrer, nous avons créé des modèles SQL de base pour une segmentation simple basée sur les comptes.

Supposons que vous souhaitiez segmenter les utilisateurs qui sont des employés d'un compte d'entreprise cible.

1. Allez dans **Audience** > **Segment Extensions** > **Create New Extension** > **Start with a template** et sélectionnez le modèle **Catalog segment for events**. <br><br> ![Fenêtre modale « Sélectionner un modèle » avec des options de segmentation de catalogue pour les événements ou les achats.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>L'éditeur SQL se remplit automatiquement avec un modèle qui associe les données d'événements utilisateur aux données du catalogue afin de segmenter les utilisateurs qui interagissent avec certains articles du catalogue. <br><br>![Un éditeur SQL pour une nouvelle extension avec un onglet « Variables » ouvert.]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. Utilisez l'onglet **Variables** pour renseigner les champs nécessaires à votre modèle avant de générer votre segment.<br><br>Pour que Braze identifie les utilisateurs en fonction de leur engagement avec les articles du catalogue, vous devez :
- Sélectionner un catalogue contenant un champ de catalogue
- Sélectionner un événement personnalisé contenant une propriété d'événement
- Faire correspondre les valeurs du champ de catalogue et de la propriété d'événement

##### Recommandations sur les variables pour les cas d'utilisation B2B {#variables-guidelines-for-b2b-use-cases}

Sélectionnez les variables suivantes pour un cas d'utilisation de segmentation B2B basée sur les comptes :

| Variable | Propriété |
| --- | --- |
| Catalogue | Catalogue des comptes |
| Champ du catalogue | ID |
| Événement personnalisé | account_linked |
| Propriété de l'événement personnalisé | account_id |
| (Sous Filtrer les résultats SQL) Champ du catalogue | Classification |
| (Sous Filtrer les résultats SQL) Valeur | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Segmentation SQL avancée {#sophisticated-sql-segmentation}

Pour une segmentation plus sophistiquée ou complexe, consultez les [Extensions de segments SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/). Pour vous aider à démarrer, voici quelques modèles SQL qui vous permettront de prendre une longueur d'avance avec la segmentation basée sur les comptes B2B :

1. Créez un segment comparant deux filtres dans un même catalogue (par exemple, les utilisateurs qui travaillent dans le secteur de la restauration pour un compte de niveau entreprise). Vous devez inclure l'ID du catalogue et l'ID de l'article.

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
;
```

{: start="2"}
2. Créez un segment comparant deux filtres dans deux catalogues distincts (par exemple, les utilisateurs associés à des comptes cibles de type entreprise qui ont une opportunité ouverte au « Stage 3 »).

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### Option 2 : Utiliser des sources connectées pour vos objets métier {#option-2-when-using-connected-sources-for-your-business-objects}

Pour les bases de l'utilisation des sources connectées dans la segmentation, consultez les [Extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments/). Inspirez-vous des modèles décrits dans la section [Utiliser des catalogues](#option-1-when-using-catalogs-for-your-business-objects) pour le formatage des tables sources, car vous pouvez les structurer comme vous le souhaitez.

## Utiliser votre extension basée sur les comptes dans un segment {#using-your-account-based-extension-in-a-segment}

Une fois votre segmentation au niveau du compte créée en suivant les étapes ci-dessus, vous pouvez directement intégrer ces Extensions de segments dans vos critères de ciblage. Vous pouvez aussi facilement ajouter des critères démographiques supplémentaires pour les utilisateurs, tels que le rôle, l'engagement dans des campagnes précédentes, etc. Pour en savoir plus, consultez [Utiliser votre extension dans un segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#step-6-use-your-extension-in-a-segment).