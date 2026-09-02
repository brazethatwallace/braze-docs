---
nav_title: "Partage de données"
article_title: Partage de données Snowflake
page_order: 0
description: "Cet article de référence présente l'intégration Snowflake Secure Data Sharing, qui vous permet d'accéder aux données d'engagement et de Campaign de Braze directement dans votre instance Snowflake."
page_type: partner
search_tag: Partner

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Partage de données Snowflake {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsnowflake-secure-data-sharing-via-braze-stylefloatrightwidth120pxborder0-classnoimgbordersnowflake-data-sharing}

> Le [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) de Snowflake permet à Braze de vous donner un accès sécurisé aux données de notre portail Snowflake, sans vous soucier des frictions de workflow, des ralentissements, des points de défaillance et des coûts inutiles liés aux relations classiques avec les fournisseurs de données. Le partage de données peut être configuré via l'intégration suivante ou via les [comptes Snowflake Reader]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts).

Le partage de données Snowflake fait partie de la distribution de données Braze. Pour un aperçu complet des options de distribution de données, consultez [Distribution de données]({{site.baseurl}}/user_guide/data/distribution).

{% alert tip %}
**Vous souhaitez accéder à des données de niveau Snowflake sans avoir besoin d'un compte Snowflake ?**<br>Consultez les [comptes Snowflake Reader]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts). Avec les comptes Reader, Braze crée un compte dans lequel vos données sont partagées et vous fournit des identifiants pour vous connecter et accéder à vos données. Ainsi, l'ensemble du partage de données et de la facturation d'utilisation est entièrement géré par Braze.
{% endalert %}

## Droits d'accès à la distribution des données {#data-distribution-entitlements}

Votre droit d'accès à la distribution des données détermine les types d'événements disponibles dans votre partage de données. Braze organise les événements dans les catégories suivantes :

| Droit d'accès | Catégorie d'événement | Description | Référence du glossaire des événements |
|------------|----------------|-------------|--------------------------|
| **Engagement Events** | Événements d'engagement lié aux messages | Événements liés aux envois, livraisons, ouvertures, clics, rebonds et autres interactions avec les canaux de communication | [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **Customer Behavior Events** | Événements d'engagement lié aux messages et événements de comportement client | Comprend tous les événements d'engagement lié aux messages, ainsi que les événements liés aux achats, aux événements personnalisés, aux sessions, à l'attribution et aux actions des utilisateurs dans l'application | [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Événements de comportement client et utilisateur]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **User Profiles and Attributes** | Événements d'engagement lié aux messages, événements de comportement client et événements de profil utilisateur | Comprend les événements d'engagement lié aux messages et les événements de comportement client, ainsi que les événements liés aux modifications des profils et attributs utilisateur | [Événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [Événements de comportement client et utilisateur]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [Événements de profil utilisateur]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Droits d'accès à la distribution des données" }

Pour toute question concernant les événements inclus dans votre droit d'accès, contactez votre gestionnaire de compte Braze ou votre gestionnaire du succès des clients.

## À propos du partage sécurisé de données {#about-secure-data-sharing}

Avec le partage de données, aucune donnée n'est réellement copiée ou transférée entre les comptes. Tout le partage s'effectue via la couche de services et le magasin de métadonnées uniques de Snowflake. C'est un concept important, car les données partagées n'occupent aucun espace de stockage dans votre compte et ne contribuent donc pas à vos frais mensuels de stockage de données. Les **seuls** frais concernent les ressources de calcul (tels que les entrepôts virtuels) utilisées pour interroger les données partagées.

De plus, grâce aux fonctionnalités intégrées de rôles et de permissions de Snowflake, l'accès aux données partagées depuis Braze peut être contrôlé et régi à l'aide des contrôles d'accès déjà en place pour votre compte Snowflake et les données qu'il contient. L'accès peut être restreint et surveillé de la même manière que vos propres données.

- **Réduisez le délai d'obtention d'informations**<br>Dites adieu aux processus ETL qui prennent des semaines à mettre en place. Les architectures uniques de Braze et Snowflake rendent toutes les données d'engagement client et de Campaign immédiatement accessibles et interrogeables dès leur arrivée dans le lac de données. Aucune donnée n'est copiée ou déplacée, ce qui vous permet d'offrir des expériences client basées uniquement sur les informations les plus pertinentes et les plus récentes.
- **Éliminez les silos de données**<br>Créez une vue globale de vos clients à travers les canaux et les plateformes. Le partage de données facilite plus que jamais la jonction de vos données d'engagement client Braze avec toutes vos autres données Snowflake, pour des informations plus riches à partir d'une source unique et fiable.
- **Évaluez votre engagement par rapport aux références du secteur**<br>Optimisez vos stratégies d'engagement client avec Braze Benchmarks. Cet outil interactif, alimenté par Braze et Snowflake, vous permet de comparer les données d'engagement de votre marque à des références de référence par canal, secteur et plateforme d'appareil.

Pour en savoir plus sur le partage de données de Snowflake, consultez [Introduction au partage sécurisé de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Accès à Braze | Contactez votre gestionnaire de compte Braze ou votre CSM or gestionnaire de la satisfaction client or gestionnaire du succès des clients pour configurer le partage de données. |
| Compte Snowflake | Un compte Snowflake avec les permissions `admin`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Configuration du partage sécurisé des données {#setting-up-secure-data-sharing}

Pour Snowflake, le partage de données s'effectue entre un [fournisseur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) et un [consommateur de données](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Dans ce contexte, votre compte Braze est le fournisseur de données car il crée et envoie le partage de données&#8212;tandis que votre compte Snowflake est le consommateur de données car il utilise le partage de données pour créer une base de données. Pour plus de détails, consultez [Snowflake : Consommer des données partagées](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Étape 1 : Envoyer le partage de données depuis Braze {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### Étape 2 : Créer la base de données dans Snowflake {#step-2-create-the-database-in-snowflake}

1. Après quelques minutes, vous devriez recevoir le partage de données entrant dans votre compte Snowflake.
2. En utilisant le partage de données entrant, créez une base de données pour visualiser et interroger les tables. Par exemple :
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. Accordez les privilèges nécessaires pour interroger la nouvelle base de données.

{% alert warning %}
Si vous supprimez et recréez un partage dans le tableau de bord de Braze, vous devez supprimer la base de données précédemment créée et la recréer en utilisant `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` pour interroger le partage entrant.
Si vous avez plusieurs espaces de travail partageant des données vers le même compte Snowflake, consultez la [FAQ sur le partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs) pour obtenir des conseils sur la gestion des configurations multi-espaces de travail.
{% endalert %}

## Utilisation et visualisation {#usage-and-visualization}

Une fois le partage de données provisionné, créez une base de données à partir du partage de données entrant, afin que toutes les tables partagées apparaissent dans votre instance Snowflake et puissent être interrogées comme n'importe quelles autres données stockées dans votre instance. Cependant, gardez à l'esprit que les données partagées sont en lecture seule et ne peuvent être qu'interrogées, sans possibilité de modification ou de suppression.

Comme avec Currents, vous pouvez utiliser votre partage sécurisé de données Snowflake pour :

{% multi_lang_include partners/data_sharing_use_cases.md %}

[Télécharger les schémas de tables brutes.](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

{% alert note %}
Le téléchargement du schéma brut n'inclut pas les vues d'attributs de profil utilisateur. Pour les schémas complets et les conseils d'utilisation de `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`, `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` et des vues d'attributs utilisateur associées, consultez [Attributs de profil utilisateur]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

### Schéma des identifiants utilisateur {#user-id-schema}

Notez les différences suivantes entre les conventions de nommage de Braze et de Snowflake pour les identifiants utilisateur.

| Schéma Braze | Schéma Snowflake | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | L'identifiant unique attribué automatiquement par Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | L'identifiant unique du profil d'un utilisateur, défini par le client. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schéma des identifiants utilisateur" }

## Informations importantes et limitations {#important-information-and-limitations}

### Modifications avec rupture et sans rupture {#breaking-versus-non-breaking-changes}

#### Modifications sans rupture {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
Étant donné que les nouvelles colonnes sont considérées comme des modifications sans rupture, Braze recommande fortement de lister explicitement les colonnes qui vous intéressent dans chaque requête au lieu d'utiliser des requêtes `SELECT *`. Vous pouvez également créer des vues qui nomment explicitement les colonnes, puis interroger ces vues au lieu des tables directement.
{% endalert %}

#### Modifications avec rupture {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Régions Snowflake {#snowflake-regions}

Braze héberge actuellement toutes les données au niveau utilisateur dans les régions AWS Snowflake suivantes :

 - US East-1
 - EU-Central (Francfort)
 - AP-Northeast-1 (Tokyo)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)

Pour les utilisateurs en dehors de ces régions, Braze peut fournir un partage de données aux clients communs qui hébergent leur infrastructure Snowflake dans n'importe quelle région AWS, Azure ou GCP.

### Conservation des données {#data-retention}

#### Politique de conservation {#retention-policy}

Toute donnée datant de plus de deux ans sera archivée et déplacée vers un stockage à long terme. Dans le cadre du processus d'archivage, tous les événements sont anonymisés et tous les champs sensibles contenant des données d'identification (PII) sont supprimés (cela inclut les champs optionnellement PII comme `properties`). Les données archivées contiennent toujours le champ `user_id`, ce qui permet d'effectuer des analyses par utilisateur sur l'ensemble des données d'événements.

Vous pourrez interroger les deux années de données les plus récentes pour chaque événement dans la vue `USERS_*_SHARED` correspondante. De plus, chaque événement disposera d'une vue `USERS_*_SHARED_ALL` qui peut être interrogée pour renvoyer à la fois des données anonymisées et non anonymisées.

#### Données historiques {#historical-data}

L'archive des données d'événements historiques dans Snowflake remonte à avril 2019. Au cours des premiers mois où Braze stockait des données dans Snowflake, des modifications produit ont été apportées qui ont pu entraîner des différences mineures dans certaines données ou la présence de valeurs nulles (car nous ne transmettions pas encore de données dans tous les champs disponibles à cette époque). Il est préférable de considérer que tout résultat incluant des données antérieures à août 2019 peut présenter de légères différences par rapport aux attentes.

### Conformité au Règlement général sur la protection des données (RGPD) {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### Vitesse, performance et coût des requêtes {#speed-performance-cost-of-queries}

La vitesse, la performance et le coût de toute requête exécutée sur les données sont déterminés par la taille de l'entrepôt que vous utilisez pour interroger les données. Dans certains cas, selon le volume de données auxquelles vous accédez à des fins d'analyse, vous pourriez constater qu'il est nécessaire d'utiliser un entrepôt de plus grande taille pour que la requête aboutisse. Snowflake met à disposition d'excellentes ressources sur la manière de déterminer la taille la plus adaptée, notamment [Aperçu des entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) et [Considérations relatives aux entrepôts](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

{% alert tip %}
Pour consulter un ensemble d'exemples de requêtes lors de la configuration de Snowflake, découvrez nos exemples de [requêtes types]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) et de [configuration de pipeline d'événements ETL]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup).
{% endalert %}