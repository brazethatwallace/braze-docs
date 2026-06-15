---
nav_title: "Delta Sharing"
article_title: Databricks Delta Sharing
page_order: 0
description: "Cet article de référence couvre Databricks Delta Sharing avec Braze (bêta fermée), qui vous permet d'accéder aux données d'engagement et de campagne Braze dans votre compte Databricks."
page_type: partner
search_tag: Partner
permalink: /delta_sharing/
hidden: true
---

# Databricks Delta Sharing

> Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) vous permet de partager en toute sécurité des données d'engagement et de campagne Braze en temps réel dans votre environnement Databricks. Cet article décrit le fonctionnement du partage depuis Braze en tant que fournisseur de données vers votre compte Databricks en tant que destinataire, et comment interroger les tables partagées.

{% alert important %}
Databricks Delta Sharing avec Braze est en **bêta fermée**. La disponibilité, les régions prises en charge et le comportement du produit peuvent changer. Contactez votre gestionnaire de la satisfaction client Braze pour participer ou pour confirmer si cette fonctionnalité est activée pour votre espace de travail.
{% endalert %}

Databricks Delta Sharing fait partie de la distribution de données Braze. Pour un aperçu complet des options de distribution de données, consultez [Distribution de données]({{site.baseurl}}/user_guide/data/distribution/).

## Configurer Delta Sharing {#set-up-delta-sharing}

Pour Databricks, le partage de données s'effectue entre un fournisseur de données et un destinataire de données. Votre compte Braze est le **fournisseur de données** car il crée et envoie le partage, et votre compte Databricks est le **destinataire de données** car il consomme le partage pour créer un catalogue que vous pouvez interroger. Pour plus de détails, consultez la documentation Databricks sur la [lecture de données partagées via Databricks-to-Databricks Delta Sharing (pour les destinataires)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html).

### Étape 1 : Configurer le partage depuis Braze {#step-1-configure-sharing-from-braze}

1. Dans Braze, accédez à **Intégrations partenaires** > **Partage de données** > **Databricks Delta Sharing**.
2. Saisissez votre identifiant de partage Databricks.
3. Lorsque vous avez terminé, sélectionnez **Create Datashare**. Braze envoie le partage à votre compte Databricks.

### Étape 2 : Créer un catalogue dans Databricks {#step-2-create-a-catalog-in-databricks}

1. Après quelques minutes, vous devriez recevoir le partage entrant dans votre compte Databricks.
2. En utilisant le partage entrant, créez un catalogue pour visualiser et interroger les tables. Par exemple :
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. Accordez les privilèges nécessaires pour que les bons utilisateurs et groupes puissent interroger le nouveau catalogue.

{% alert warning %}
Les données partagées sont en lecture seule dans votre espace de travail Databricks. Vous pouvez les interroger comme d'autres données, mais vous ne pouvez pas modifier ni supprimer des lignes dans les tables partagées via le partage.
{% endalert %}

## Utilisation et visualisation {#usage-and-visualization}

Une fois le partage de données provisionné, créez un catalogue à partir du partage entrant afin que les tables partagées apparaissent dans votre espace de travail Databricks et soient interrogeables comme les autres données que vous y stockez. Les données partagées restent en lecture seule.

De manière similaire à Currents, vous pouvez utiliser Databricks Delta Sharing pour :

- Créer des rapports complexes
- Effectuer une modélisation d'attribution
- Sécuriser le partage au sein de votre propre entreprise
- Mapper des données brutes d'événements ou d'utilisateurs vers un CRM (comme Salesforce)
- Et bien plus encore

Pour une liste complète des tables et colonnes disponibles dans Databricks, [téléchargez les schémas de tables brutes Databricks]({% image_buster /assets/download_file/databricks-data-sharing-raw-table-schemas.txt %}) sous forme de fichier texte. Ce fichier reflète le schéma Databricks Delta Sharing (par exemple, `DB_CREATED_AT` pour l'heure d'ingestion). Il n'est pas interchangeable avec les [schémas de tables brutes Snowflake]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}) ou la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/), qui décrivent la nomenclature et les champs Snowflake.

{% alert note %}
Pendant la bêta fermée, toutes les tables listées dans le fichier de schéma Databricks peuvent ne pas être disponibles dans votre partage. Les noms et types de colonnes peuvent également différer de Snowflake Data Sharing (par exemple, `DB_CREATED_AT` au lieu de `SF_CREATED_AT`). Contactez votre gestionnaire de la satisfaction client Braze si vous avez besoin de la liste actuelle des tables pour votre espace de travail.
{% endalert %}

### Schéma des identifiants utilisateur {#user-id-schema}

Notez les différences suivantes entre les conventions de nommage de Braze et de Databricks pour les identifiants utilisateur.

| Schéma Braze | Schéma Databricks | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | L'identifiant unique que Braze attribue automatiquement. |
| `external_id` | `EXTERNAL_USER_ID` | L'identifiant unique du profil d'un utilisateur que vous définissez dans Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User ID schema" }

## Informations importantes et limitations {#important-information-and-limitations}

### Disponibilité de la bêta fermée {#closed-beta-availability}

Pendant la bêta fermée, votre partage peut ne pas inclure toutes les tables du fichier de [schémas de tables brutes Databricks]({% image_buster /assets/download_file/databricks-data-sharing-raw-table-schemas.txt %}). Les données partagées peuvent également différer de Snowflake Data Sharing au niveau des noms et types de colonnes. Par exemple, les partages Databricks utilisent `DB_CREATED_AT` pour l'heure d'ingestion, tandis que les partages Snowflake utilisent `SF_CREATED_AT`.

### Modifications avec et sans rupture {#breaking-versus-non-breaking-changes}

#### Modifications sans rupture {#non-breaking-changes}

Les modifications sans rupture peuvent survenir à tout moment et fournissent généralement des fonctionnalités supplémentaires. Exemples de modifications sans rupture :

- Ajout d'une nouvelle table ou vue
- Ajout d'une colonne à une table ou vue existante

{% alert important %}
Étant donné que les nouvelles colonnes sont considérées comme des modifications sans rupture, Braze recommande fortement de lister explicitement les colonnes d'intérêt dans chaque requête au lieu d'utiliser des requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes et interroger ces vues au lieu d'interroger directement les tables partagées.
{% endalert %}

#### Modifications avec rupture {#breaking-changes}

Lorsque cela est possible, les modifications avec rupture sont précédées d'une annonce et d'une période de migration. Exemples de modifications avec rupture :

- Suppression d'une table ou vue
- Suppression d'une colonne d'une table ou vue existante
- Modification du type ou de la possibilité de valeur nulle d'une colonne existante

### Régions Databricks {#databricks-regions}

Pendant la bêta fermée, les fournisseurs cloud et les régions pris en charge peuvent varier selon l'espace de travail et le déploiement. Contactez votre gestionnaire de la satisfaction client Braze pour connaître les options applicables à votre compte.

### Politique de rétention {#retention-policy}

Pendant la bêta fermée, le remplissage historique au-delà de la fenêtre de rétention standard peut être limité.

Vous pouvez interroger les deux années les plus récentes de données pour chaque événement dans la vue `USERS_*_SHARED` correspondante.

### Conformité au Règlement général sur la protection des données (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Interrogation des données partagées : `TIME` et performances des requêtes {#querying-shared-data-time-and-query-performance}

Les données d'événements dans les vues de partage de données (par exemple, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) sont regroupées sur le champ `TIME`. Lorsque vous filtrez par date d'occurrence de l'événement, utilisez `TIME` comme filtre privilégié. Les requêtes qui restreignent les lignes en utilisant `TIME` sont généralement plus performantes que celles qui filtrent sur `DB_CREATED_AT`, car le regroupement est aligné sur l'heure de l'événement.

| Champ | Signification |
| ----- | ------- |
| `TIME` | Horodatage Unix auquel l'événement s'est produit. Privilégiez ce champ pour filtrer par heure d'occurrence. |
| `DB_CREATED_AT` | Horodatage du chargement de la ligne dans Databricks (heure d'ingestion). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Querying shared data: TIME and query performance" }

### Vitesse, performances et coût des requêtes {#speed-performance-and-cost-of-queries}

La vitesse, les performances et le coût de toute requête que vous exécutez sur les données dépendent de la taille de l'entrepôt SQL que vous utilisez. Selon le volume de données auquel vous accédez, vous pourriez avoir besoin d'un entrepôt plus grand pour que la requête aboutisse. Pour plus d'informations, consultez la documentation Databricks sur la [création et la configuration d'un entrepôt SQL](https://docs.databricks.com/en/compute/sql-warehouse/create.html) (y compris la taille du cluster et la mise à l'échelle).