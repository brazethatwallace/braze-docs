---
nav_title: Supprimer des utilisateurs avec CDI
article_title: Supprimer des utilisateurs avec l'Ingestion de données cloud
page_order: 9
page_type: reference
description: "Cette page présente un aperçu du processus de suppression d'utilisateurs avec l'Ingestion de données cloud."

---

# Supprimer des utilisateurs avec l'Ingestion de données cloud {#delete-users-with-cloud-data-ingestion}

> Cette page traite du processus de suppression des utilisateurs avec l'Ingestion de données cloud.

Les synchronisations de suppression d'utilisateurs sont prises en charge pour toutes les sources de données d'Ingestion de données cloud disponibles.

## Configurer l'intégration {#configure-the-integration}

Suivez le processus standard pour [créer une nouvelle intégration dans le tableau de bord de Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) pour l'entrepôt de données auquel vous souhaitez vous connecter. Assurez-vous d'inclure un rôle qui peut accéder à la table de suppression. Sur la page **Create import sync**, définissez le **Data Type** sur **Delete Users** afin que les actions appropriées soient exécutées pendant l'intégration pour supprimer les utilisateurs.

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## Configurer les données sources {#configure-source-data}

Les tables sources pour les suppressions d'utilisateurs doivent inclure un ou plusieurs types d'identifiants d'utilisateurs et un horodatage `UPDATED_AT`. Les colonnes de payload ne sont pas prises en charge pour les données de suppression d'utilisateurs.

### `UPDATED_AT`

Ajoutez un horodatage `UPDATED_AT` à votre table source. Cet horodatage indique l'heure à laquelle cette ligne a été mise à jour ou ajoutée à la table. Braze synchronise les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Les lignes situées exactement à l'horodatage limite peuvent être resynchronisées si de nouvelles lignes partagent ce même horodatage.

### Colonnes d'identification de l'utilisateur {#user-identifier-columns}

Votre table peut contenir une ou plusieurs colonnes d'identifiants utilisateur. Chaque ligne ne doit contenir qu'un seul identifiant : soit `external_id`, soit la combinaison de `alias_name` et `alias_label`, soit `braze_id`. Une table source peut contenir des colonnes pour un, deux ou les trois types d'identifiants.
- `EXTERNAL_ID` : identifie l'utilisateur que vous souhaitez mettre à jour. Cette valeur doit correspondre à la valeur `external_id` utilisée dans Braze.
- `ALIAS_NAME` et `ALIAS_LABEL` : ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais un seul `alias_name` par `alias_label`.
- `BRAZE_ID` : l'identifiant utilisateur Braze. Il est généré par le SDK Braze et les nouveaux utilisateurs ne peuvent pas être créés à l'aide d'un ID Braze via l'Ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias d'utilisateur.

{% alert important %}
N'incluez pas de colonne `payload` dans votre table pour la suppression d'utilisateurs. Pour éviter la suppression accidentelle et permanente d'utilisateurs, la synchronisation échouera si une colonne de payload est fournie dans la table source. Toute autre colonne est autorisée mais sera ignorée par Braze.
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```sql
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216)
);
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar
);
```
{% endtab %}

{% tab BigQuery %}
Créez une table avec les champs suivants :

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User identifier columns" }
{% endtab %}

{% tab Databricks %}
Créez une table avec les champs suivants :

| Nom du champ | Type | Mode |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User identifier columns" }
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
)
GO
```
{% endtab %}

{% endtabs %}

### Fonctionnement {#how-it-works}

Avec l'Ingestion de données cloud de Braze, vous configurez une intégration entre votre instance d'entrepôt de données et votre espace de travail Braze pour synchroniser les données de manière récurrente. Cette synchronisation s'exécute selon la planification que vous définissez, et chaque intégration peut avoir sa propre planification. Les synchronisations peuvent avoir lieu toutes les 15 minutes ou aussi rarement qu'une fois par mois. Si vous avez besoin de synchronisations plus fréquentes que toutes les 15 minutes, contactez votre gestionnaire de la satisfaction client ou envisagez d'utiliser les appels REST API pour l'ingestion de données en temps réel.

Lorsqu'une synchronisation s'exécute, Braze se connecte directement à votre instance d'entrepôt de données, récupère toutes les nouvelles données de la table spécifiée et supprime les profils utilisateur correspondants dans votre tableau de bord de Braze.

{% alert warning %}
La suppression de profils utilisateur est irréversible. Cette action supprime définitivement les utilisateurs, ce qui peut entraîner des écarts dans vos données. Pour en savoir plus, consultez la section [Effets de la suppression de profils utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/#effects-of-deleting-user-profiles).
{% endalert %}

<br><br>