---
nav_title: Synchronisation et suppression des données du catalogue
article_title: Synchronisation et suppression des données du catalogue
page_order: 6
page_type: reference
description: "Cette page donne un aperçu de la manière de synchroniser les données du catalogue."

---

# Synchronisation et suppression des données du catalogue {#sync-and-delete-catalog-data}

> Cette page explique comment synchroniser les données du catalogue.

## Étape 1 : Créer un nouveau catalogue {#step-1-create-a-new-catalog}

Avant de créer une nouvelle intégration d'ingestion de données cloud (CDI) pour les [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs), vous devez créer un nouveau catalogue ou identifier un catalogue existant que vous souhaitez utiliser pour l'intégration. Il existe plusieurs façons de créer un nouveau catalogue, et chacune d'entre elles fonctionne pour l'intégration CDI :
- Charger un [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- Créer un catalogue dans le [tableau de bord de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/create) ou lors de la configuration CDI.
- Créer un catalogue à l'aide de l'[endpoint Créer un catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)

Toute modification apportée au schéma du catalogue (par exemple, l'ajout de nouveaux champs ou la modification du type de champ) doit être effectuée via le tableau de bord du catalogue avant que les données mises à jour ne soient synchronisées par CDI. Nous vous recommandons d'effectuer ces mises à jour lorsque la synchronisation est en pause ou n'est pas planifiée, afin d'éviter les conflits entre les données de votre entrepôt de données et le schéma dans Braze.

## Étape 2 : Intégrer l'ingestion de données cloud avec les données de catalogue {#step-2-integrate-cloud-data-ingestion-with-catalog-data}
La configuration d'une synchronisation de catalogue suit de près le processus des [intégrations CDI de données utilisateur]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).

{% tabs %}
{% tab Snowflake %}

1. Configurez une table source dans Snowflake. Vous pouvez utiliser les noms de l'exemple suivant ou choisir vos propres noms de base de données, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée à la place d'une table.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         payload VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Configurez un rôle, un entrepôt et un utilisateur, puis accordez les autorisations appropriées. Si vous disposez déjà d'identifiants provenant d'une synchronisation existante, vous pouvez les réutiliser, mais assurez-vous d'étendre l'accès à la table source du catalogue.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Si votre compte Snowflake dispose de politiques réseau, ajoutez les adresses IP de Braze à la liste d'autorisation afin que le service CDI puisse se connecter. Pour obtenir la liste des adresses IP, consultez la section [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
4. Dans le tableau de bord de Braze, accédez à **Partenaires technologiques** > **Snowflake** et créez une nouvelle synchronisation.
5. Saisissez les détails de connexion (ou réutilisez des identifiants existants) et la table source.
6. Passez à l'étape 2 du flux de configuration, sélectionnez le type de synchronisation « Catalogs » et saisissez le nom de l'intégration ainsi que la planification. Notez que le nom de l'intégration doit **correspondre exactement** au nom du catalogue que vous avez précédemment créé.
7. Choisissez une fréquence de synchronisation et passez à l'étape suivante.
8. Ajoutez la clé publique affichée sur le tableau de bord à l'utilisateur que vous avez créé pour que Braze puisse se connecter à Snowflake. Pour effectuer cette étape, vous aurez besoin d'une personne disposant d'un accès `SECURITYADMIN` ou supérieur dans Snowflake.
9. Sélectionnez **Test Connection** pour vérifier que tout fonctionne comme prévu.
10. Enregistrez la synchronisation et utilisez les données de catalogue synchronisées pour tous vos cas d'usage de personnalisation.
{% endtab %}
{% tab Redshift %}

1. Configurez une table source dans Redshift. Vous pouvez utiliser les noms de l'exemple suivant ou choisir vos propres noms de base de données, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée à la place d'une table.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Configurez un utilisateur et accordez les autorisations appropriées. Si vous disposez déjà d'identifiants provenant d'une synchronisation existante, vous pouvez les réutiliser, mais assurez-vous d'étendre l'accès à la table source du catalogue.
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Si vous disposez d'un pare-feu ou d'autres politiques réseau, vous devez accorder à Braze un accès réseau à votre instance Redshift. Autorisez l'accès depuis les adresses IP suivantes correspondant à la région de votre tableau de bord Braze. Pour obtenir la liste des adresses IP, consultez la section [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Facultatif : configurez un nouveau projet ou un jeu de données pour héberger votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| NOM DU CHAMP | TYPE | MODE |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| payload | JSON | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | OPTIONAL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Intégrer l'ingestion de données cloud avec les données de catalogue" }

{:start="2"}

2. Configurez un utilisateur et accordez les autorisations appropriées. Si vous disposez déjà d'identifiants provenant d'une synchronisation existante, vous pouvez les réutiliser&#8212;mais assurez-vous d'étendre l'accès à la table source du catalogue.
Le compte de service doit disposer des autorisations décrites dans la section suivante :
- BigQuery Connection User : cela permettra à Braze d'établir des connexions.
- BigQuery User : cela fournira à Braze l'accès pour exécuter des requêtes, lire les métadonnées des jeux de données et lister les tables.
- BigQuery Data Viewer : cela fournira à Braze l'accès pour consulter les jeux de données et leur contenu.
- BigQuery Job User : cela fournira à Braze l'accès pour exécuter des tâches.<br><br>Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Consultez la section [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) pour plus d'informations. Vous l'importerez ultérieurement dans le tableau de bord de Braze.

{:start="3"}
3. Si vous avez des politiques réseau en place, vous devez accorder à Braze un accès réseau à votre instance BigQuery. Pour obtenir la liste des adresses IP, consultez la section [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Configurez une table source dans Databricks. Vous pouvez utiliser les noms de l'exemple suivant ou choisir vos propres noms de catalogue, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée à la place d'une table.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| NOM DU CHAMP | TYPE | MODE |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| payload | STRING, STRUCT, or MAP | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Intégrer l'ingestion de données cloud avec les données de catalogue" }

{:start="2"}

2. Créez un jeton d'accès personnel dans votre espace de travail Databricks.

- a. Sélectionnez votre nom d'utilisateur Databricks, puis sélectionnez **User Settings** dans le menu déroulant.
- b. Dans l'onglet **Access tokens**, sélectionnez **Generate new token**.
- c. Saisissez un commentaire pour identifier ce jeton, par exemple « Braze CDI ».
- d. Modifiez la durée de vie du jeton pour qu'il n'ait pas de limite en laissant le champ **Lifetime (days)** vide. Sélectionnez **Generate**.
- e. Copiez le jeton affiché, puis sélectionnez **Done**.
- f. Conservez le jeton dans un endroit sûr jusqu'à ce que vous deviez le saisir lors de l'étape de création des identifiants dans le tableau de bord de Braze.

{:start="3"}
3. Si vous avez des politiques réseau en place, vous devez accorder à Braze un accès réseau à votre instance Databricks. Pour obtenir la liste des adresses IP, consultez la page [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. Configurez un principal de service et accordez les autorisations appropriées. Si vous disposez déjà d'identifiants provenant d'une synchronisation existante, vous pouvez les réutiliser&#8212;assurez-vous simplement d'étendre l'accès à la table source du catalogue. Pour en savoir plus sur la création d'un nouveau principal de service et de ses identifiants, consultez la page [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{:start="3"}
3. Si vous avez des politiques réseau en place, vous devez accorder à Braze un accès réseau à votre instance Microsoft Fabric. Pour obtenir la liste des adresses IP, consultez la page [Ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Créez des fichiers source dans S3 au format JSON ou CSV. Chaque fichier doit contenir les champs suivants :

| Champ | Obligatoire ? | Description |
| --- | --- | --- |
| `ID` | Oui | L'ID de l'élément de catalogue à créer ou à mettre à jour. |
| `payload` | Oui | Une chaîne JSON des champs à synchroniser avec l'élément de catalogue dans Braze. |
| `DELETED` | Facultatif | Lorsque défini sur `true`, l'élément de catalogue correspondant est supprimé du catalogue. |
| `UPDATED_AT` | *Non pris en charge* | Le stockage de fichiers ne prend pas en charge les colonnes `UPDATED_AT`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 2 : Intégrer l'ingestion de données cloud avec les données de catalogue" }

{% alert note %}
Les noms de fichiers doivent respecter les règles AWS et être uniques. Ajoutez des horodatages pour garantir l'unicité.
{% endalert %}

La configuration complète de S3 nécessite un compartiment S3, une file d'attente Amazon SQS et un rôle et une politique AWS IAM. Braze ne traite que les fichiers téléchargés après la création de la synchronisation ; re-téléchargez les fichiers existants que vous souhaitez ingérer.

Pour le flux de configuration S3 complet, consultez la section [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations), en particulier :

- [Configuration de l'ingestion de données cloud dans AWS]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-aws)
- [Configuration de l'ingestion de données cloud dans Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)
- [Résolution des problèmes]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#troubleshooting)

Pour les problèmes courants de notification et d'autorisation côté AWS, consultez [Granting permissions to publish event notification messages to a destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html).

Les exemples suivants montrent des formats JSON et CSV valides pour synchroniser les données de catalogue depuis le stockage de fichiers.

{% subtabs %}
{% subtab JSON Catalogs %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
{% endalert %}
{% endsubtab %}
{% subtab CSV Catalogs with Delete %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% subtab CSV Catalogs without Delete %}
```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"
```
{% endsubtab %}
{% endsubtabs %}

Pour des exemples de fichiers supplémentaires, consultez la section [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).

{% endtab %}
{% endtabs %}

## Fonctionnement de l'intégration {#how-the-integration-works}

{% alert note %}
Les vues de synchronisation de cette section s'appliquent uniquement aux intégrations d'entrepôts de données. Pour le stockage de fichiers S3, Braze traite les nouveaux fichiers au fur et à mesure qu'ils sont téléchargés dans votre compartiment. Consultez [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations) pour plus de détails.
{% endalert %}

Chaque fois que la synchronisation s'exécute, Braze récupère toutes les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage. Nous vous recommandons de créer une vue dans votre entrepôt de données à partir de vos données de catalogue afin de configurer une table source qui sera entièrement actualisée à chaque exécution de la synchronisation. Avec les vues, vous n'aurez pas besoin de réécrire la requête à chaque fois.

Par exemple, si vous disposez d'une table de données produit (`product_catalog_1`) avec `product_id` et trois attributs supplémentaires, vous pouvez synchroniser la vue suivante :

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Les données récupérées par l'intégration seront utilisées pour créer ou mettre à jour des éléments dans le catalogue cible en fonction de l'`id` fourni.
- Si DELETED est défini sur `true`, l'élément de catalogue correspondant sera supprimé.
- La synchronisation ne consommera pas de points de données, mais toutes les données synchronisées seront comptabilisées dans votre utilisation totale du catalogue ; cette utilisation est mesurée en fonction du volume total de données stockées, vous n'avez donc pas à vous soucier de ne synchroniser que les données modifiées.