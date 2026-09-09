---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Cet article décrit le partenariat entre Braze et Snowflake, couvrant à la fois le partage de données (de Braze vers Snowflake) et l'ingestion de données cloud."
page_type: partner
search_tag: Partner
---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) est un entrepôt de données SQL cloud spécialement conçu, fourni en tant que SaaS (Software-as-a-Service). Snowflake offre un entrepôt de données plus rapide, plus simple d'utilisation et bien plus flexible que les solutions traditionnelles. Grâce à son architecture unique et brevetée, Snowflake vous permet de centraliser facilement toutes vos données, d'effectuer des analyses rapides et d'en tirer des informations exploitables pour l'ensemble de vos utilisateurs.

Braze propose deux intégrations avec Snowflake. Ensemble, elles constituent un pipeline de données bidirectionnel complet entre vos environnements Braze et Snowflake.

## Choisir une intégration {#choosing-an-integration}

### Partage de données (de Braze vers Snowflake) {#data-sharing-braze-to-snowflake}

Le [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing) de Snowflake vous donne un accès sécurisé et en temps réel aux données d'engagement et de Campaign de Braze directement dans votre instance Snowflake. Aucune donnée n'est copiée ni transférée entre les comptes : tout le partage s'effectue via la couche de services et le magasin de métadonnées propres à Snowflake.

**Utilisez le partage de données lorsque vous souhaitez :**
- Interroger les données d'événements et de Campaign de Braze à l'aide de Snowflake SQL
- Créer des rapports complexes et effectuer une modélisation d'attribution
- Joindre les données de Braze à d'autres données de votre entrepôt de données Snowflake
- Comparer vos données d'engagement entre canaux, secteurs d'activité et plateformes d'appareils

Pour les instructions de configuration, consultez [Partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing).

### Ingestion de données cloud (de Snowflake vers Braze) {#cloud-data-ingestion-snowflake-to-braze}

L'[ingestion de données cloud (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) vous permet de synchroniser les données de votre instance Snowflake directement dans Braze. Cela vous permet de maintenir à jour les attributs utilisateurs, les événements et les achats dans Braze avec votre entrepôt de données source de vérité.

**Utilisez l'ingestion de données cloud lorsque vous souhaitez :**
- Synchroniser les attributs utilisateurs de Snowflake vers les profils utilisateurs de Braze
- Envoyer des données d'événements ou d'achats de Snowflake vers Braze
- Maintenir Braze synchronisé avec les transformations de données effectuées dans votre entrepôt de données
- Éviter de créer et de maintenir des pipelines ETL personnalisés de Snowflake vers Braze

Pour en savoir plus sur le partage de données de Snowflake, consultez [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Prérequis {#prerequisites}

Avant de pouvoir utiliser cette fonctionnalité, vous devrez remplir les conditions suivantes :

| Condition | Description |
| ----------- | ----------- |
| Accès à Braze | Pour accéder à cette fonctionnalité dans Braze, vous devrez contacter votre gestionnaire de compte Braze ou votre gestionnaire de la satisfaction client. |
| Autorisations de l'espace de travail Braze | [Afficher les intégrations Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) pour consulter le partage de données. [Modifier les intégrations Currents]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) pour créer, mettre à jour ou supprimer un partage de données. |
| Compte Snowflake | Un compte Snowflake avec des autorisations `admin`. Pour les clients non-HIPAA, Snowflake Standard ou Enterprise Edition est pris en charge. Pour le partage de données conforme à la norme HIPAA, l'édition Business Critical est requise. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Configuration du Secure Data Sharing {#setting-up-secure-data-sharing}

Pour Snowflake, le partage de données s'effectue entre un [fournisseur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) et un [consommateur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Dans ce contexte, votre compte Braze est le fournisseur de données, car il crée et envoie le partage de données&#8212;tandis que votre compte Snowflake est le consommateur de données, car il utilise le partage de données pour créer une base de données. Pour plus de détails, consultez [Snowflake : Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Étape 1 : Envoyer le partage de données depuis Braze {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Étape 2 : Créer la base de données dans Snowflake {#step-2-create-the-database-in-snowflake}

1. Après quelques minutes, vous devriez recevoir le partage de données entrant dans votre compte Snowflake.
2. À l'aide du partage de données entrant, créez une base de données pour visualiser et interroger les tables. Par exemple :
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Accordez les privilèges nécessaires pour interroger la nouvelle base de données.

{% alert warning %}
Si vous supprimez et recréez un partage dans le tableau de bord de Braze, vous devez supprimer la base de données précédemment créée et la recréer en utilisant `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` pour interroger le partage entrant.
Si vous avez plusieurs espaces de travail partageant des données vers le même compte Snowflake, consultez la [FAQ sur le partage des données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) pour obtenir des conseils sur la gestion des configurations multi-espaces de travail.
{% endalert %}

## Utilisation et visualisation {#usage-and-visualization}

Une fois le partage de données provisionné, vous devrez créer une base de données à partir du partage de données entrant, ce qui rendra toutes les tables partagées visibles dans votre instance Snowflake et interrogeables comme n'importe quelle autre donnée stockée dans votre instance. Cependant, gardez à l'esprit que les données partagées sont en lecture seule et ne peuvent être qu'interrogées, mais ni modifiées ni supprimées de quelque façon que ce soit.

À l'instar de Currents, vous pouvez utiliser le Secure Data Sharing de Snowflake pour :

{% multi_lang_include partners/data_sharing_use_cases.md %}

Pour une liste complète des tables et colonnes disponibles, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Le partage de données Snowflake inclut toutes les tables de cette référence, ainsi que des tables supplémentaires exclusives à Snowflake pour les instantanés, les journaux de modifications de Campaign et Canvas, les événements de la console d'agent et les événements de nouvelle tentative de message.

Vous pouvez également [télécharger les schémas de tables bruts](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) sous forme de fichier texte.

### Schéma d'identifiant utilisateur {#user-id-schema}

Notez les différences suivantes entre les conventions de nommage Braze et Snowflake pour les identifiants utilisateur.

| Schéma Braze | Schéma Snowflake | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | L'identifiant unique automatiquement attribué par Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | L'identifiant unique du profil d'un utilisateur, défini par le client. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schéma d'identifiant utilisateur" }

## Informations importantes et limitations {#important-information-and-limitations}

### Modifications avec et sans rupture {#breaking-versus-non-breaking-changes}

#### Modifications sans rupture {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Étant donné que l'ajout de nouvelles colonnes est considéré comme une modification sans rupture, Braze recommande fortement de lister explicitement les colonnes qui vous intéressent dans chaque requête au lieu d'utiliser des requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes, puis interroger ces vues au lieu des tables directement.
{% endalert %}

#### Modifications avec rupture {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Régions Snowflake {#snowflake-regions}

Braze héberge actuellement toutes les données au niveau utilisateur dans les régions Snowflake AWS US East-1, EU-Central (Francfort), AP-Northeast-1 (Tokyo), AP-Southeast-2 (Sydney) et AP-Southeast-3 (Jakarta). Pour les utilisateurs en dehors de ces régions, Braze peut fournir un partage de données aux clients communs qui hébergent leur infrastructure Snowflake dans n'importe quelle région AWS, Azure ou GCP.

### Conservation des données {#data-retention}

#### Politique de conservation {#retention-policy}

Toute donnée datant de plus de deux ans sera archivée et transférée vers un stockage longue durée. Dans le cadre du processus d'archivage, tous les événements sont anonymisés et tous les champs sensibles contenant des données d'identification personnelle (PII) sont supprimés (cela inclut les champs optionnellement PII comme `properties`). Les données archivées contiennent toujours le champ `user_id`, ce qui permet des analyses par utilisateur sur l'ensemble des données d'événements.

Vous pourrez interroger les deux années les plus récentes de données pour chaque événement dans la vue `USERS_*_SHARED` correspondante. De plus, chaque événement disposera d'une vue `USERS_*_SHARED_ALL` qui peut être interrogée pour renvoyer à la fois des données anonymisées et non anonymisées.

#### Données historiques {#historical-data}

L'archive des données d'événements historiques dans Snowflake remonte à avril 2019. Au cours des premiers mois où Braze stockait des données dans Snowflake, des modifications produit ont été effectuées qui ont pu entraîner un aspect légèrement différent de certaines données ou la présence de valeurs nulles (car nous ne transmettions pas de données dans chaque champ disponible à cette époque). Il est préférable de considérer que tout résultat incluant des données antérieures à août 2019 peut différer légèrement des attentes.

### Conformité au Règlement général sur la protection des données (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Interrogation des données partagées : `TIME` et performances des requêtes {#querying-shared-data-time-and-query-performance}

Les données d'événements dans les vues de partage de données (par exemple, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) sont **regroupées (clustered) sur le champ `TIME`**. Lorsque vous filtrez par **date de survenue de l'événement**, utilisez **`TIME`** comme filtre de préférence. Les requêtes qui restreignent les lignes en utilisant **`TIME`** sont généralement **plus performantes** que les requêtes filtrant sur **`SF_CREATED_AT`**, car le regroupement (clustering) est aligné sur le temps de l'événement.

| Champ | Signification |
| ----- | ------------- |
| `TIME` | Horodatage Unix indiquant le moment où l'événement s'est produit. À privilégier pour filtrer par date de survenue. |
| `SF_CREATED_AT` | Horodatage indiquant le moment où la ligne a été chargée dans Snowflake (temps d'ingestion). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Interrogation des données partagées : TIME et performances des requêtes" }

### Vitesse, performances et coût des requêtes {#speed-performance-cost-of-queries}

La vitesse, les performances et le coût de toute requête exécutée sur les données sont déterminés par la taille de l'entrepôt que vous utilisez pour interroger les données. Dans certains cas, en fonction du volume de données auquel vous accédez pour vos analyses, vous pourriez constater qu'il est nécessaire d'utiliser un entrepôt de plus grande taille pour que la requête aboutisse. Snowflake met à disposition d'excellentes ressources sur la manière de déterminer la taille la plus adaptée, notamment [Overview of warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) et [Warehouse considerations](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Pour un ensemble d'exemples de requêtes à consulter lors de la configuration de Snowflake, consultez nos exemples de [requêtes types]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) et de [configuration du pipeline d'événements ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).

Pour les instructions de configuration, consultez [Ingestion de données cloud : intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).