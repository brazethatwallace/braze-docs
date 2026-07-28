---
nav_title: Intégrations d'entrepôts de données
article_title: Intégrations d'entrepôts de données
alias: /partners/databricks/
description: "Cette page explique comment utiliser l'Ingestion de données cloud de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks."
page_order: 3
page_type: reference

---

# Intégrations d'entrepôts de données {#data-warehouse-storage-integrations}

> Cette page explique comment utiliser l'Ingestion de données cloud (CDI) de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks.

## Configuration des intégrations d'entrepôt de données {#setting-up-data-warehouse-integrations}

Les intégrations Cloud Data Ingestion nécessitent une configuration du côté de Braze et dans votre instance d'entrepôt de données. Suivez ces étapes pour configurer l'intégration :

{% tabs %}
{% tab Snowflake %}
1. Dans votre instance Snowflake, configurez les tables ou vues que vous souhaitez synchroniser avec Braze.
2. Créez une nouvelle source Snowflake dans le tableau de bord de Braze.
3. Récupérez la clé publique fournie dans le tableau de bord de Braze et [ajoutez-la à l'utilisateur Snowflake pour l'authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Créez une synchronisation dans le tableau de bord de Braze, testez l'intégration et lancez la synchronisation.

{% alert tip %}
Le [guide de démarrage rapide Snowflake](https://quickstarts.snowflake.com/guide/braze_cdi/index.html) fournit un exemple de code et décrit les étapes nécessaires pour créer un pipeline automatisé utilisant Snowflake Streams et CDI pour synchroniser les données avec Braze.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. Assurez-vous que l'accès de Braze aux tables Redshift que vous souhaitez synchroniser est autorisé. Braze se connecte à Redshift via Internet.
2. Dans votre instance Redshift, configurez les tables ou vues que vous souhaitez synchroniser avec Braze.
3. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.
4. Testez l'intégration et lancez la synchronisation.

{% alert note %}
Le nombre de lignes traitées par synchronisation dépend des performances de votre entrepôt de données, de la latence réseau et du volume de nouvelles données correspondant à la requête de synchronisation. Utilisez l'**historique de synchronisation** de l'intégration dans le tableau de bord pour consulter la durée et le nombre de lignes des exécutions récentes.
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données BigQuery contenant les données que vous souhaitez synchroniser.
2. Dans votre compte BigQuery, configurez les tables ou vues que vous souhaitez synchroniser avec Braze.
3. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.
4. Testez l'intégration et lancez la synchronisation.
{% endtab %}
{% tab Databricks %}
1. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.
2. Dans votre compte Databricks, configurez les tables ou vues que vous souhaitez synchroniser avec Braze.
3. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.
4. Testez l'intégration et lancez la synchronisation.

{% alert important %}
Il peut y avoir un temps de préchauffage de deux à cinq minutes lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui peut entraîner des délais lors de la configuration et du test de la connexion, ainsi qu'au début des synchronisations planifiées. L'utilisation d'une instance SQL serverless minimise le temps de préchauffage et améliore le débit des requêtes, mais peut entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. Créez un principal de service et accordez l'accès aux API Fabric.
2. Configurez un espace de travail partagé et accordez au principal de service l'accès à celui-ci.
3. Dans l'espace de travail Fabric partagé, configurez les tables ou vues que vous souhaitez synchroniser avec Braze.
4. Créez une nouvelle source et une synchronisation dans le tableau de bord de Braze.
5. Testez l'intégration et lancez la synchronisation.
{% endtab %}
{% endtabs %}

### Étape 1 : Configurer les tables ou vues {#step-1-set-up-tables-or-views}

Avant de commencer, consultez [Configuration des tables pour Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup) pour comprendre les exigences des tables sources par rapport aux exigences de formatage de `payload`.

{% alert note %}
Votre table ou vue source peut inclure des colonnes qui ne sont pas répertoriées pour votre entrepôt de données dans les onglets de la section suivante (par exemple, pour l'audit ou le hachage). Braze ne lit que les colonnes décrites dans ces onglets ; les autres colonnes ne sont pas utilisées lors des synchronisations Cloud Data Ingestion.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### Étape 1.1 : Configurer la table {#step-11-set-up-the-table}

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identifiant utilisateur** - Votre table peut contenir une ou plusieurs colonnes d'identifiant utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut avoir des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.
    - `ALIAS_NAME` et `ALIAS_LABEL` - Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des labels différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant utilisateur Braze. Il est généré par le SDK Braze, et de nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un Braze ID via Cloud Data Ingestion. Pour créer de nouveaux utilisateurs, spécifiez un identifiant utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour.
- `payload` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Configurer le rôle et les permissions de la base de données {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

Mettez à jour les noms si nécessaire, mais les permissions doivent correspondre à l'exemple précédent.

#### Étape 1.3 : Configurer l'entrepôt et donner l'accès au rôle Braze {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'entrepôt doit avoir l'option **auto-resume** activée. Si ce n'est pas le cas, accordez à Braze des privilèges `OPERATE` supplémentaires sur l'entrepôt afin que Braze puisse l'activer lorsque la requête s'exécute.
{% endalert %}

#### Étape 1.4 : Configurer l'utilisateur {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Après cette étape, partagez les informations de connexion avec Braze pour recevoir une clé publique à ajouter à l'utilisateur.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur pour plusieurs intégrations, mais la création de l'intégration échoue si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 1.5 : Autoriser les IP Braze dans la politique réseau Snowflake (facultatif) {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Selon la configuration de votre compte Snowflake, vous devrez peut-être autoriser les adresses IP suivantes dans votre politique réseau Snowflake. Pour plus d'informations sur l'activation de cette fonctionnalité, consultez la documentation Snowflake pertinente sur la [modification d'une politique réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### Étape 1.1 : Configurer la table

Optionnellement, configurez une nouvelle base de données et un nouveau schéma pour héberger votre table source.
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Créez une table (ou vue) à utiliser pour votre intégration CDI.
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

Vous pouvez nommer la base de données, le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identifiant utilisateur** - Votre table peut contenir une ou plusieurs colonnes d'identifiant utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut avoir des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.
    - `ALIAS_NAME` et `ALIAS_LABEL` - Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des labels différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant utilisateur Braze. Il est généré par le SDK Braze, et de nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un Braze ID via Cloud Data Ingestion. Pour créer de nouveaux utilisateurs, spécifiez un identifiant utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour.
- `payload` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Créer l'utilisateur et accorder les permissions {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Ce sont les permissions minimales requises pour cet utilisateur. Si vous créez plusieurs intégrations CDI, vous pouvez accorder des permissions au niveau du schéma ou gérer les permissions à l'aide d'un groupe.

#### Étape 1.3 : Autoriser l'accès aux IP Braze {#step-13-allow-access-to-braze-ips}

Si vous disposez d'un pare-feu ou d'autres politiques réseau, vous devez accorder à Braze un accès réseau à votre instance Redshift. Un exemple d'URL d'endpoint Redshift est « example-cluster.ap-northeast-2.redshift.amazonaws.com ».

Quelques points importants à connaître :
- Vous devrez peut-être également modifier vos groupes de sécurité pour permettre à Braze d'accéder à vos données dans Redshift.
- Assurez-vous d'autoriser explicitement le trafic entrant sur les IP du tableau et sur le port utilisé pour interroger votre cluster Redshift (par défaut 5439). Vous devez autoriser explicitement la connectivité TCP Redshift sur ce port même si les règles entrantes sont définies sur « tout autoriser ».
- L'endpoint du cluster Redshift doit être accessible publiquement pour que Braze puisse se connecter à votre cluster.
     - Si vous ne souhaitez pas que votre cluster Redshift soit accessible publiquement, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel SSH afin d'accéder aux données Redshift. Pour plus d'informations, consultez l'[article du centre de connaissances AWS](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine).

Autorisez l'accès depuis les IP suivantes correspondant à la région de votre tableau de bord Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### Étape 1.1 : Configurer la table

Optionnellement, configurez un nouveau projet ou jeu de données pour héberger votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `payload`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 1.1 : Configurer la table" }

Vous pouvez nommer le projet, le jeu de données et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identifiant utilisateur** - Votre table peut contenir une ou plusieurs colonnes d'identifiant utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut avoir des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.
    - `ALIAS_NAME` et `ALIAS_LABEL` - Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des labels différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant utilisateur Braze. Il est généré par le SDK Braze, et de nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un Braze ID via Cloud Data Ingestion. Pour créer de nouveaux utilisateurs, spécifiez un identifiant utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour.
- `payload` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

{% alert important %}
**Partitionnement BigQuery**

CDI prend en charge les partitions pour BigQuery. Si vous partitionnez par une fonction de `UPDATED_AT` (par exemple, à la granularité d'un jour, d'une semaine ou d'une heure, selon la taille de votre jeu de données), BigQuery peut élaguer les données qu'il doit analyser. Cela améliore les performances et l'efficacité pour les très grandes tables.

Ne partitionnez pas par d'autres champs. Testez différentes configurations pour trouver la meilleure pour vos données spécifiques.

Toutes les requêtes CDI filtrent par `UPDATED_AT`, mais ce comportement pourrait changer. Concevez le schéma de votre table de manière à _ne pas_ exiger que les requêtes incluent cette clause.

Pour plus d'informations, consultez la [documentation sur le partitionnement BigQuery](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).
{% endalert %}

#### Étape 1.2 : Créer un compte de service et accorder les permissions {#step-12-create-a-service-account-and-grant-permissions}

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de vos tables. Le compte de service doit disposer des permissions suivantes :

- **BigQuery Connection User :** permet à Braze d'établir des connexions.
- **BigQuery User :** fournit à Braze l'accès pour exécuter des requêtes, lire les métadonnées des jeux de données et lister les tables.
- **BigQuery Data Viewer :** fournit à Braze l'accès pour consulter les jeux de données et leur contenu.
- **BigQuery Job User :** fournit à Braze l'accès pour exécuter des tâches.

Après avoir créé le compte de service et accordé les permissions, générez une clé JSON. Pour plus d'informations, consultez [Créer et supprimer des clés de compte de service](https://cloud.google.com/iam/docs/keys-create-delete). Vous téléchargerez cette clé dans le tableau de bord de Braze lors d'une étape ultérieure.

#### Étape 1.3 : Autoriser l'accès aux IP Braze

Si vous avez des politiques réseau en place, vous devez accorder à Braze un accès réseau à votre instance BigQuery. Autorisez l'accès depuis les IP suivantes correspondant à la région de votre tableau de bord Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### Étape 1.1 : Configurer la table

Optionnellement, configurez un nouveau catalogue ou schéma pour héberger votre table source.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `payload`| STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étape 1.1 : Configurer la table" }

Vous pouvez nommer le schéma et la table comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identifiant utilisateur** - Votre table peut contenir une ou plusieurs colonnes d'identifiant utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut avoir des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.
    - `ALIAS_NAME` et `ALIAS_LABEL` - Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des labels différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant utilisateur Braze. Il est généré par le SDK Braze, et de nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un Braze ID via Cloud Data Ingestion. Pour créer de nouveaux utilisateurs, spécifiez un identifiant utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour.
- `payload` - Il s'agit d'une chaîne ou d'une structure des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.

#### Étape 1.2 : Créer un jeton d'accès {#step-12-create-an-access-token}

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Dans l'onglet Access tokens, sélectionnez **Generate new token**.
3. Saisissez un commentaire qui vous aide à identifier ce jeton, tel que « Braze CDI », et modifiez la durée de vie du jeton en laissant le champ Lifetime (days) vide (sans limite).
4. Sélectionnez **Generate**.
5. Copiez le jeton affiché, puis sélectionnez **Done**.

Conservez le jeton dans un endroit sûr jusqu'à ce que vous deviez le saisir dans le tableau de bord de Braze lors de l'étape de création des identifiants.

#### Étape 1.3 : Autoriser l'accès aux IP Braze

Si vous avez des politiques réseau en place, vous devez accorder à Braze un accès réseau à votre instance Databricks. Autorisez l'accès depuis les IP suivantes correspondant à la région de votre tableau de bord Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 1.1 : Configurer le principal de service et accorder l'accès {#step-11-set-up-the-service-principal-and-grant-access}
Braze se connecte à votre entrepôt Fabric à l'aide d'un principal de service avec l'authentification Entra ID. Créez un nouveau principal de service que Braze utilisera et accordez l'accès aux ressources Fabric selon les besoins. Braze a besoin des informations suivantes pour se connecter :

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure ne permet pas une expiration illimitée des secrets de principal de service. N'oubliez pas d'actualiser les identifiants avant leur expiration pour maintenir le flux de données vers Braze.
{% endalert %}

#### Étape 1.2 : Accorder l'accès aux ressources Fabric {#step-12-grant-access-to-fabric-resources}
Fournissez l'accès pour que Braze puisse se connecter à votre instance Fabric. Dans votre portail d'administration Fabric, accédez à **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Dans **Developer settings**, activez **Service principals can use Fabric APIs** pour que Braze puisse se connecter à l'aide de Microsoft Entra ID.
* Dans **OneLake settings**, activez **Users can access data stored in OneLake with apps external to Fabric** pour que le principal de service puisse accéder aux données depuis une application externe.

#### Étape 1.3 : Configurer un espace de travail partagé et accorder l'accès {#step-13-set-up-a-shared-workspace-and-grant-access}

Toutes les ressources Fabric que vous souhaitez connecter à Braze doivent être placées dans un espace de travail partagé. Si vous n'avez utilisé que l'espace de travail par défaut **My Workspace**, créez un nouvel espace de travail partagé :

1. Dans le menu de navigation, sélectionnez **Workspaces**, puis sélectionnez **+ New workspace**.
2. Saisissez un **Name** pour l'espace de travail, puis sélectionnez **Apply**.

Une fois que vous disposez d'un espace de travail partagé, accordez l'accès au principal de service :

1. Sélectionnez l'espace de travail, puis sélectionnez **Manage Access**.
2. Sélectionnez **+ Add people or groups**.
3. Recherchez et sélectionnez le nom du principal de service que vous avez créé à l'étape 1.1. S'il n'apparaît pas, confirmez que vous avez activé le paramètre **Service principals can use Fabric APIs** à l'étape 1.2.
4. Dans le menu déroulant des rôles, sélectionnez **Contributor**.

Le principal de service peut désormais accéder aux ressources de l'entrepôt Fabric dans cet espace de travail via leurs endpoints SQL, y compris l'entrepôt à utiliser pour Braze.

#### Étape 1.4 : Configurer la table {#step-14-set-up-the-table}
Braze prend en charge les tables et les vues dans les entrepôts Fabric. Si vous devez créer un nouvel entrepôt, créez-le dans l'espace de travail partagé de l'étape 1.3. Accédez à **Create > Data Warehouse > Warehouse** dans la console Fabric.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

Vous pouvez nommer l'entrepôt, le schéma et la table ou vue comme vous le souhaitez, mais les noms de colonnes doivent correspondre à la définition précédente.

- `UPDATED_AT` - L'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être re-synchronisées si de nouvelles lignes partagent ce même horodatage.
- **Colonnes d'identifiant utilisateur** - Votre table peut contenir une ou plusieurs colonnes d'identifiant utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant (soit `external_id`, la combinaison de `alias_name` et `alias_label`, `braze_id`, `email` ou `phone`). Une table source peut avoir des colonnes pour un, deux, trois, quatre ou les cinq types d'identifiants.
    - `EXTERNAL_ID` - Identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.
    - `ALIAS_NAME` et `ALIAS_LABEL` - Ces deux colonnes créent un objet alias d'utilisateur. `alias_name` doit être un identifiant unique, et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec des labels différents, mais un seul `alias_name` par `alias_label`.
    - `BRAZE_ID` - L'identifiant utilisateur Braze. Il est généré par le SDK Braze, et de nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un Braze ID via Cloud Data Ingestion. Pour créer de nouveaux utilisateurs, spécifiez un identifiant utilisateur externe ou un alias d'utilisateur.
    - `EMAIL` - L'adresse e-mail de l'utilisateur. Si plusieurs profils avec la même adresse e-mail existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour. Si vous incluez à la fois l'e-mail et le téléphone, l'e-mail est utilisé comme identifiant principal.
    - `PHONE` - Le numéro de téléphone de l'utilisateur. Si plusieurs profils avec le même numéro de téléphone existent, le profil mis à jour le plus récemment est prioritaire pour les mises à jour.
- `payload` - Il s'agit d'une chaîne JSON des champs que vous souhaitez synchroniser avec l'utilisateur dans Braze.


#### Étape 1.5 : Obtenir la chaîne de connexion de l'entrepôt {#step-15-get-warehouse-connection-string}
Pour récupérer l'endpoint SQL de votre entrepôt, accédez à l'**espace de travail** dans Fabric, survolez le nom de l'entrepôt dans la liste des éléments et sélectionnez **Copy SQL connection string**.

![La page « Console Fabric » dans Microsoft Azure, où les utilisateurs doivent récupérer la chaîne de connexion SQL.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### Étape 1.6 : Autoriser les IP Braze dans le pare-feu (facultatif) {#step-16-allow-braze-ips-in-firewall-optional}

Selon la configuration de votre compte Microsoft Fabric, vous devrez peut-être autoriser les adresses IP suivantes dans votre pare-feu pour permettre le trafic depuis Braze. Pour plus d'informations sur l'activation de cette fonctionnalité, consultez la documentation pertinente sur l'[accès conditionnel Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Étape 2 : Créer une nouvelle source dans le tableau de bord de Braze {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Snowflake**.

#### Étape 2.1 : Ajouter les informations de connexion Snowflake {#step-21-add-snowflake-connection-information}

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Snowflake, puis passez à l'étape suivante.

Avant de continuer, confirmez la valeur que vous saisissez dans **Snowflake Account Locator**.

Pour le champ **Snowflake Account Locator**, saisissez votre [identifiant de compte](https://docs.snowflake.com/en/user-guide/admin-account-identifier) Snowflake. Saisissez uniquement la valeur de l'identifiant de compte, par exemple `myorganization-myaccount`. N'incluez pas `https://`, `.snowflakecomputing.com`, ni aucun chemin.

Pour trouver votre identifiant de compte Snowflake :

1. Dans Snowsight, sélectionnez le menu de votre compte.
2. Sélectionnez **View account details**.
3. Copiez la valeur **Account identifier**.
4. Si vous copiez depuis une URL Snowflake, utilisez uniquement la valeur avant `.snowflakecomputing.com`.

#### Étape 2.2 : Ajouter une clé publique à l'utilisateur Braze {#step-22-add-a-public-key-to-the-braze-user}

Après avoir saisi vos identifiants et votre configuration, cliquez sur **Save credentials** et générez une clé RSA, puis retournez dans Snowflake pour terminer la configuration. Ajoutez la clé publique affichée dans le tableau de bord à l'utilisateur que vous avez créé pour que Braze se connecte à Snowflake.

Pour plus d'informations sur la procédure, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Si vous souhaitez effectuer une rotation des clés à tout moment, Braze peut générer une nouvelle paire de clés et fournir la nouvelle clé publique.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Amazon Redshift**.

#### Étape 2.1 : Ajouter les informations de connexion Redshift et la table source {#step-21-add-redshift-connection-information-and-source-table}

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Redshift. Si vous utilisez un tunnel réseau privé, activez le curseur et saisissez les informations du tunnel. Ensuite, passez à l'étape suivante.

{% alert note %}
Dans le tableau de bord de Braze, le champ **Database name** n'accepte que les lettres (A–Z, a–z), les chiffres (0–9) et les underscores (_), même si Amazon Redshift prend en charge des caractères supplémentaires dans les identifiants de base de données.
{% endalert %}

#### Étape 2.2 : Tester la connexion et se connecter à la source {#step-22-test-connection-and-connect-to-source}

Ensuite, sélectionnez **Test connection**. Une fois le test réussi, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

#### Résolution des problèmes : identifiant de snapshot invalide {#troubleshooting-invalid-snapshot-identifier}

Si Braze renvoie une erreur `Invalid snapshot identifier` lors du **Test connection** ou de la configuration de la synchronisation, Redshift ne peut pas résoudre la référence de snapshot utilisée lorsque votre objet source est interrogé.

Dans Redshift, un snapshot est une sauvegarde ponctuelle d'un cluster. Chaque snapshot possède un identifiant unique utilisé par Redshift pour référencer cet état de sauvegarde. Pour plus d'informations, consultez [Snapshots et sauvegardes Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html).

Cette erreur peut survenir lorsque les métadonnées changent pendant que Braze valide l'objet source, par exemple lors d'opérations de copie, de restauration ou de réplication de snapshots. Pour plus d'informations, consultez [Copier des snapshots vers une autre région AWS](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) et [Restaurer un cluster à partir d'un snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html).

Pour résoudre le problème :

1. Vérifiez les paramètres de la source dans Braze, y compris l'endpoint du cluster, la base de données, le schéma et le nom de l'objet.
2. Exécutez la même requête directement dans Redshift pour confirmer que la table ou la vue est lisible et stable.
3. Réessayez une fois que l'activité de snapshot, de restauration, de redimensionnement ou de réplication est terminée.
4. Si le problème persiste, interrogez une vue matérialisée au lieu d'une table de base qui change fréquemment.

Une vue matérialisée stocke des résultats de requête précalculés que vous pouvez actualiser selon un calendrier, ce qui peut rendre les lectures plus stables pour les synchronisations CDI. Pour plus d'informations, consultez [Vues matérialisées dans Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html).

Exemple :

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

Après avoir créé la vue matérialisée, utilisez le nom de la vue matérialisée comme objet source dans votre synchronisation CDI Braze au lieu de la table de base.
{% endtab %}
{% tab BigQuery %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Google BigQuery**.

#### Étape 2.1 : Ajouter les informations de connexion BigQuery et la table source {#step-21-add-bigquery-connection-information-and-source-table}

Choisissez un nom pour votre source. Ensuite, téléchargez la clé JSON et fournissez un nom pour le compte de service. Puis, saisissez les champs de configuration restants.

#### Étape 2.2 : Tester la connexion et se connecter à la source

Ensuite, sélectionnez **Test connection**. Une fois le test réussi, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% endtab %}
{% tab Databricks %}

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** > **Sources**, sélectionnez **Add data source**, puis sélectionnez **Databricks**.

#### Étape 2.1 : Ajouter les informations de connexion Databricks et la table source {#step-21-add-databricks-connection-information-and-source-table}

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Databricks. Ensuite, passez à l'étape suivante.

#### Étape 2.2 : Tester la connexion et se connecter à la source

Ensuite, sélectionnez **Test connection**. Une fois le test réussi, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une source avec succès avant de pouvoir la créer. Si vous fermez la page de création, votre source n'est pas enregistrée.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Dans le tableau de bord de Braze, accédez à Data Settings > Cloud Data Ingestion > Sources, sélectionnez **Add data source**, puis sélectionnez **Microsoft Fabric**.

#### Étape 2.1 : Configurer une synchronisation Cloud Data Ingestion {#step-21-set-up-a-cloud-data-ingestion-sync}

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Microsoft Fabric.
- **Credentials Name** est un label pour ces identifiants dans Braze ; vous pouvez définir une valeur utile ici.
- Consultez les étapes de la section 1 pour savoir comment récupérer le Tenant ID, le Principal ID, le Client Secret et la Connection String.

#### Étape 2.2 : Tester la connexion et se connecter à la source

Ensuite, sélectionnez **Test connection**. Une fois le test réussi, finalisez les paramètres restants et cliquez sur **Connect to Source**. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une source avec succès avant de pouvoir la créer. Si vous fermez la page de création, votre source n'est pas enregistrée.
{% endalert %}

{% endtab %}

{% endtabs %}

### Étape 3 : Créer une nouvelle synchronisation dans le tableau de bord de Braze {#step-3-create-a-new-sync-in-the-braze-dashboard}
Accédez à **Data Settings** > **Cloud Data Ingestion** > **Syncs**, et sélectionnez **Create data sync**.

{% tabs %}
{% tab Snowflake %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion {#step-31-configure-sync-details-and-test-connection}
Choisissez un nom pour votre synchronisation. Ensuite, sélectionnez une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

Une fois le test réussi, un aperçu des données apparaît. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez quitter la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification {#step-32-add-notification-preferences}
Saisissez la ou les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications concernant les erreurs d'intégration, telles qu'une perte inattendue d'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes de permissions, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent les synchronisations de s'exécuter.

Ces problèmes peuvent inclure les éléments suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions
- (Pour les synchronisations de catalogues uniquement) Le niveau du catalogue est à court d'espace

#### Étape 3.3 : Planification {#step-33-scheduling}
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze planifie la synchronisation récurrente dans le fuseau horaire UTC.

{% endtab %}

{% tab Redshift %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion
Choisissez un nom pour votre synchronisation. Ensuite, sélectionnez une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

Une fois le test réussi, un aperçu des données apparaît. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez quitter la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez la ou les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications concernant les erreurs d'intégration, telles qu'une perte inattendue d'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes de permissions, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent les synchronisations de s'exécuter.

Ces problèmes peuvent inclure les éléments suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions

(Pour les synchronisations de catalogues uniquement) Le niveau du catalogue est à court d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze planifie la synchronisation récurrente dans le fuseau horaire UTC.

{% endtab %}

{% tab BigQuery %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion
Choisissez un nom pour votre synchronisation. Ensuite, sélectionnez une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

Une fois le test réussi, un aperçu des données apparaît. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez quitter la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez la ou les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications concernant les erreurs d'intégration, telles qu'une perte inattendue d'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes de permissions, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent les synchronisations de s'exécuter. Ces problèmes peuvent inclure les éléments suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions

(Pour les synchronisations de catalogues uniquement) Le niveau du catalogue est à court d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze planifie la synchronisation récurrente dans le fuseau horaire UTC.

{% endtab %}

{% tab Databricks %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion
Choisissez un nom pour votre synchronisation. Ensuite, sélectionnez une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

Une fois le test réussi, un aperçu des données apparaît. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez quitter la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez la ou les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications concernant les erreurs d'intégration, telles qu'une perte inattendue d'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes de permissions, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent les synchronisations de s'exécuter.

Ces problèmes peuvent inclure les éléments suivants :
- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions

(Pour les synchronisations de catalogues uniquement) Le niveau du catalogue est à court d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze planifie la synchronisation récurrente dans le fuseau horaire UTC.

{% endtab %}
{% tab Microsoft Fabric %}

#### Étape 3.1 : Configurer les détails de la synchronisation et tester la connexion

Choisissez un nom pour votre synchronisation. Ensuite, sélectionnez une source active et saisissez votre table source pour la synchronisation. Sélectionnez un type de données et cliquez sur **Test Connection**.

Une fois le test réussi, un aperçu des données apparaît. Sélectionnez **Next: Notifications** pour continuer. Si la connexion échoue, un message d'erreur apparaît pour vous aider à résoudre le problème.

{% alert note %}
Vous devez tester une synchronisation avec succès avant de passer aux étapes suivantes. Si vous devez quitter la page de création de la synchronisation, cliquez sur **Save as draft** pour conserver votre travail en cours.
{% endalert %}

#### Étape 3.2 : Ajouter les préférences de notification
Saisissez la ou les adresses e-mail de contact pour les notifications d'erreurs de synchronisation. Braze utilise ces coordonnées pour envoyer des notifications concernant les erreurs d'intégration, telles qu'une perte inattendue d'accès à la table.

Les e-mails de contact ne reçoivent que les notifications d'erreurs globales ou au niveau de la synchronisation, telles que les tables manquantes, les problèmes de permissions, etc. Ils ne reçoivent pas les problèmes au niveau des lignes. Les erreurs globales indiquent des problèmes critiques avec la connexion qui empêchent les synchronisations de s'exécuter.

Ces problèmes peuvent inclure les éléments suivants :

- Problèmes de connectivité
- Manque de ressources
- Problèmes de permissions

(Pour les synchronisations de catalogues uniquement) Le niveau du catalogue est à court d'espace

#### Étape 3.3 : Planification
Enfin, configurez votre synchronisation comme non récurrente ou récurrente.

Les synchronisations non récurrentes peuvent être déclenchées manuellement ou via l'API.

Les synchronisations récurrentes peuvent avoir une fréquence allant de toutes les 15 minutes à une fois par mois. Braze planifie la synchronisation récurrente dans le fuseau horaire UTC.

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez tester une intégration avec succès avant qu'elle puisse passer de l'état Brouillon à l'état Actif. Si vous fermez la page de création, votre intégration est enregistrée et vous pouvez revenir à la page de détails pour apporter des modifications et effectuer des tests.
{% endalert %}

## Configurer des intégrations ou des utilisateurs supplémentaires (facultatif) {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Snowflake.

Si vous réutilisez le même utilisateur et le même rôle pour plusieurs intégrations, vous n'avez pas besoin d'ajouter à nouveau la clé publique.
{% endtab %}
{% tab Redshift %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Snowflake ou Redshift.

Si vous réutilisez le même utilisateur pour plusieurs intégrations, vous ne pouvez pas supprimer cet utilisateur dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.
{% endtab %}
{% tab BigQuery %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte BigQuery.

Si vous réutilisez le même utilisateur pour plusieurs intégrations, vous ne pouvez pas supprimer cet utilisateur dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% tab Databricks %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Databricks.

Si vous réutilisez le même utilisateur pour plusieurs intégrations, vous ne pouvez pas supprimer cet utilisateur dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% tab Microsoft Fabric %}

Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour synchroniser une table différente. Lors de la création de synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Fabric.

Si vous réutilisez le même utilisateur pour plusieurs intégrations, vous ne pouvez pas supprimer cet utilisateur dans le tableau de bord de Braze tant qu'il n'a pas été retiré de toutes les synchronisations actives.

{% endtab %}
{% endtabs %}

## Exécuter la synchronisation {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification de test normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Redshift %}
Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification de test normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab BigQuery %}

Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification de test normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Databricks %}

Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification de test normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}
{% tab Microsoft Fabric %}

Une fois activée, votre synchronisation s'exécute selon la planification configurée lors de la configuration. Si vous souhaitez exécuter la synchronisation en dehors de la planification de test normale ou récupérer les données les plus récentes, sélectionnez **Sync Now**. Cette exécution n'a pas d'impact sur les synchronisations futures régulièrement planifiées.

{% endtab %}

{% endtabs %}