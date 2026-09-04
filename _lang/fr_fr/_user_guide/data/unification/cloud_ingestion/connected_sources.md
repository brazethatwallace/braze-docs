---
nav_title: Sources connectées
article_title: Sources connectées
description: "Cette page explique comment utiliser l'ingestion de données cloud de Braze pour synchroniser des données pertinentes avec votre intégration Snowflake, Redshift, BigQuery et Databricks."
page_order: 2
page_type: reference

---

# Sources connectées {#connected-sources}

> Les sources connectées constituent une alternative en zéro copie à la synchronisation directe des données avec la fonctionnalité d'ingestion de données cloud (CDI) de Braze. Une source connectée interroge directement votre entrepôt de données pour créer de nouveaux segments sans copier les données sous-jacentes dans Braze.

Après avoir ajouté une source connectée à votre espace de travail Braze, vous pouvez créer un segment CDI dans les extensions de segments. Les extensions de segments CDI vous permettent d'écrire du code SQL qui interroge directement votre entrepôt de données (en utilisant les données rendues disponibles via votre source connectée CDI) et de créer et gérer un groupe d'utilisateurs pouvant être ciblés dans Braze.

Pour plus d'informations sur la création d'un segment avec cette source, consultez les [extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert warning %}
Étant donné que les sources connectées s'exécutent directement sur votre entrepôt de données, vous supporterez tous les coûts liés à l'exécution de ces requêtes dans votre entrepôt de données. Les sources connectées n'enregistrent pas de points de données et les extensions de segments CDI ne consomment pas de crédits de segments SQL.
{% endalert %}

## Intégration des sources connectées {#integrating-connected-sources}

### Étape 1 : Connecter vos ressources {#step-1-connect-your-resources}

Les sources connectées de Cloud Data Ingestion nécessitent une configuration dans Braze et dans votre instance. Suivez ces étapes pour mettre en place l'intégration&#8722;certaines étapes seront effectuées dans votre entrepôt de données et d'autres dans votre tableau de bord de Braze.

{% tabs %}
{% tab Snowflake %}
**Dans votre entrepôt de données**
1. Créez un rôle et accordez les permissions pour interroger et créer des tables dans un schéma.
2. Configurez votre entrepôt et donnez accès à ce rôle.
3. Créez un utilisateur pour ce rôle.
4. Selon votre configuration, vous devrez peut-être autoriser les adresses IP de Braze dans votre politique réseau Snowflake.

**Dans le tableau de bord de Braze**

{: start="5"}
5. Créez une nouvelle source connectée dans le tableau de bord de Braze.
6. Configurez les détails de synchronisation pour la source connectée.
7. Récupérez la clé publique fournie dans le tableau de bord de Braze.

**Dans votre entrepôt de données**

{: start="8"}
8. Ajoutez la clé publique du tableau de bord de Braze à l'[utilisateur Snowflake pour l'authentification](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Une fois terminé, vous pouvez utiliser la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% tab Redshift %}
1. Configurez les données sources et les ressources nécessaires dans votre environnement Redshift.
2. Créez une nouvelle source connectée dans le tableau de bord de Braze.
3. Testez l'intégration.
4. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% tab BigQuery %}
1. Configurez les données sources et les ressources nécessaires dans votre environnement BigQuery.
2. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données BigQuery contenant les données que vous souhaitez synchroniser.
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% tab Databricks %}
1. Configurez les données sources et les ressources nécessaires dans votre environnement Databricks.
2. Créez un compte de service et autorisez l'accès au(x) projet(s) et jeu(x) de données Databricks contenant les données que vous souhaitez synchroniser.
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.

{% alert important %}
Il peut y avoir un temps de préchauffage de deux à cinq minutes lorsque Braze se connecte aux instances SQL Classic et Pro, ce qui entraînera des délais lors de la configuration et du test de la connexion, ainsi que lors de la création et de l'actualisation des extensions de segments CDI. L'utilisation d'une instance SQL serverless réduira le temps de préchauffage et améliorera le débit des requêtes, mais pourra entraîner des coûts d'intégration légèrement plus élevés.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Créez un principal de service et autorisez l'accès à l'espace de travail Fabric qui sera utilisé pour votre intégration.
2. Dans votre espace de travail Fabric, configurez les données sources et accordez les permissions à votre principal de service.
3. Créez une nouvelle source connectée dans le tableau de bord de Braze.
4. Testez l'intégration.
5. Utilisez la source connectée pour créer une ou plusieurs extensions de segments CDI.
{% endtab %}

{% endtabs %}

### Étape 2 : Configurer votre entrepôt de données {#step-2-set-up-your-data-warehouse}

Configurez les données sources et les ressources nécessaires dans votre environnement d'entrepôt de données. La source connectée peut référencer une ou plusieurs tables, assurez-vous donc que votre utilisateur Braze dispose des permissions d'accès à toutes les tables souhaitées dans la source connectée.

{% tabs %}
{% tab Snowflake %}
#### Étape 2.1 : Créer un rôle et accorder les permissions {#step-21-create-a-role-and-grant-permissions}

Créez un rôle à utiliser pour votre source connectée. Ce rôle sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI et pour interroger les tables sources afin de créer de nouveaux segments. Une fois la source connectée créée, Braze découvrira les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma source.

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès seront disponibles pour les requêtes dans l'extension de segments CDI.

La permission `create table` est requise pour que Braze puisse créer une table avec les résultats de votre requête d'extension de segments CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, et la table ne persistera que pendant la mise à jour du segment par Braze.

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Étape 2.2 : Configurer l'entrepôt et donner accès au rôle Braze {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'entrepôt doit avoir l'option **auto-resume** activée. Si ce n'est pas le cas, vous devrez accorder à Braze des privilèges `OPERATE` supplémentaires sur l'entrepôt pour que Braze puisse l'activer au moment d'exécuter la requête.
{% endalert %}

#### Étape 2.3 : Configurer l'utilisateur {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Vous partagerez les informations de connexion avec Braze et recevrez une clé publique à ajouter à l'utilisateur lors d'une étape ultérieure.

{% alert note %}
Lorsque vous connectez différents espaces de travail au même compte Snowflake, vous devez créer un utilisateur unique pour chaque espace de travail Braze dans lequel vous créez une intégration. Au sein d'un espace de travail, vous pouvez réutiliser le même utilisateur pour plusieurs intégrations, mais la création de l'intégration échouera si un utilisateur du même compte Snowflake est dupliqué entre les espaces de travail.
{% endalert %}

#### Étape 2.4 : Autoriser les adresses IP de Braze dans votre politique réseau Snowflake (facultatif) {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Selon la configuration de votre compte Snowflake, vous devrez peut-être autoriser les adresses IP suivantes dans votre politique réseau Snowflake. Pour plus d'informations, consultez la documentation Snowflake pertinente sur la [modification d'une politique réseau](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Étape 2.1 : Créer un utilisateur et accorder les permissions {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Créez un utilisateur à utiliser pour votre source connectée. Cet utilisateur sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI et pour interroger les tables sources afin de créer de nouveaux segments. Une fois la source connectée créée, Braze découvrira les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma source. Si vous créez plusieurs intégrations CDI, vous pouvez accorder les permissions à un schéma ou gérer les permissions à l'aide d'un groupe.

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès seront disponibles pour les requêtes dans l'extension de segments CDI. Assurez-vous d'accorder l'accès à toute nouvelle table à l'utilisateur lors de sa création, ou de définir des permissions par défaut pour l'utilisateur.

La permission `create table` est requise pour que Braze puisse créer une table avec les résultats de votre requête d'extension de segments CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, qui ne persistera que pendant la mise à jour du segment par Braze.


#### Étape 2.2 : Autoriser l'accès aux adresses IP de Braze {#step-22-allow-access-to-braze-ips}

Si vous disposez d'un pare-feu ou d'autres politiques réseau, vous devez donner à Braze un accès réseau à votre instance Redshift. Autorisez l'accès depuis les adresses IP suivantes correspondant à la région de votre tableau de bord de Braze.

Vous devrez peut-être également modifier vos groupes de sécurité pour autoriser l'accès de Braze à vos données dans Redshift. Assurez-vous d'autoriser explicitement le trafic entrant sur les adresses IP de la section suivante et sur le port utilisé pour interroger votre cluster Redshift (par défaut 5439). Vous devez autoriser explicitement la connectivité TCP Redshift sur ce port même si les règles entrantes sont définies sur « tout autoriser ». De plus, il est important que l'endpoint du cluster Redshift soit accessible publiquement pour que Braze puisse se connecter à votre cluster.

Si vous ne souhaitez pas que votre cluster Redshift soit accessible publiquement, vous pouvez configurer un VPC et une instance EC2 pour utiliser un tunnel SSH afin d'accéder aux données Redshift. Pour plus d'informations, consultez [AWS : Comment accéder à un cluster Amazon Redshift privé depuis ma machine locale ?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Étape 2.1 : Créer un compte de service et accorder les permissions {#step-21-create-a-service-account-and-grant-permissions}

Créez un compte de service dans GCP que Braze utilisera pour se connecter et lire les données de vos tables. Le compte de service doit disposer des permissions suivantes :

- **BigQuery Connection User :** permet à Braze d'établir des connexions.
- **BigQuery User :** fournit à Braze l'accès pour exécuter des requêtes, lire les métadonnées des jeux de données et lister les tables.
- **BigQuery Data Viewer :** fournit à Braze l'accès pour visualiser les jeux de données et leur contenu.
- **BigQuery Job User :** fournit à Braze l'accès pour exécuter des tâches.
- **bigquery.tables.create :** fournit à Braze l'accès pour créer des tables temporaires lors de l'actualisation des segments.

Créez un compte de service à utiliser pour votre source connectée. Cet utilisateur sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI et pour interroger les tables sources afin de créer de nouveaux segments. Une fois la source connectée créée, Braze découvrira les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma source.

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un jeu de données ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès seront disponibles pour les requêtes dans l'extension de segments CDI.

La permission `create table` est requise pour que Braze puisse créer une table avec les résultats de votre requête d'extension de segments CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, et la table ne persistera que pendant la mise à jour du segment par Braze.

Après avoir créé le compte de service et accordé les permissions, générez une clé JSON. Pour plus d'informations, consultez [Google Cloud : Créer et supprimer des clés de compte de service](https://cloud.google.com/iam/docs/keys-create-delete). Vous la téléchargerez ultérieurement dans le tableau de bord de Braze.

#### Étape 2.2 : Autoriser l'accès aux adresses IP de Braze

Si vous avez des politiques réseau en place, vous devez donner à Braze un accès réseau à votre instance BigQuery. Autorisez l'accès depuis les adresses IP suivantes correspondant à la région de votre tableau de bord de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Étape 2.1 : Créer un jeton d'accès {#step-21-create-an-access-token}

Pour que Braze puisse accéder à Databricks, un jeton d'accès personnel doit être créé.

1. Dans votre espace de travail Databricks, sélectionnez votre nom d'utilisateur Databricks dans la barre supérieure, puis sélectionnez **User Settings** dans le menu déroulant.
2. Assurez-vous que le compte de service dispose des privilèges `CREATE TABLE` sur le schéma utilisé pour la source connectée.
3. Dans l'onglet **Access tokens**, sélectionnez **Generate new token**.
4. Saisissez un commentaire pour identifier ce jeton, par exemple « Braze CDI », et définissez la durée de vie du jeton sur illimitée en laissant le champ Lifetime (days) vide.
5. Sélectionnez **Generate**.
6. Copiez le jeton affiché, puis sélectionnez **Done**.

Ce jeton sera utilisé pour générer la liste des tables disponibles dans vos extensions de segments CDI et pour interroger les tables sources afin de créer de nouveaux segments. Une fois la source connectée créée, Braze découvrira les noms et la description de toutes les tables disponibles pour l'utilisateur dans le schéma source.

Vous pouvez choisir d'accorder l'accès à toutes les tables d'un schéma ou d'accorder des privilèges uniquement à des tables spécifiques. Les tables auxquelles le rôle Braze a accès seront disponibles pour les requêtes dans l'extension de segments CDI.

La permission `create table` est requise pour que Braze puisse créer une table avec les résultats de votre requête d'extension de segments CDI avant de mettre à jour le segment dans Braze. Braze créera une table temporaire par segment, qui ne persistera que pendant la mise à jour du segment par Braze.

Conservez le jeton en lieu sûr jusqu'à ce que vous deviez le saisir dans le tableau de bord de Braze lors de l'étape de création des identifiants.

#### Étape 2.2 : Autoriser l'accès aux adresses IP de Braze

Si vous avez des politiques réseau en place, vous devez donner à Braze un accès réseau à votre instance Databricks. Autorisez l'accès depuis les adresses IP suivantes correspondant à la région de votre tableau de bord de Braze.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Étape 2.1 : Accorder l'accès aux ressources Fabric {#step-21-grant-access-to-fabric-resources}
Braze se connectera à votre entrepôt Fabric à l'aide d'un principal de service avec l'authentification Entra ID. Vous allez créer un nouveau principal de service que Braze utilisera et accorder l'accès aux ressources Fabric selon les besoins. Braze aura besoin des informations suivantes pour se connecter :

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure ne permet pas une expiration illimitée des secrets de principal de service. N'oubliez pas d'actualiser les identifiants avant leur expiration afin de maintenir le flux de données vers Braze.
{% endalert %}

#### Étape 2.2 : Accorder l'accès aux ressources Fabric {#step-22-grant-access-to-fabric-resources}
Vous allez fournir l'accès pour que Braze puisse se connecter à votre instance Fabric. Dans votre portail d'administration Fabric, accédez à **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* Dans **Developer settings**, activez « Service principals can use Fabric APIs » pour que Braze puisse se connecter à l'aide de Microsoft Entra ID.
* Dans **OneLake settings**, activez « Users can access data stored in OneLake with apps external to Fabric » pour que le principal de service puisse accéder aux données depuis une application externe.

#### Étape 2.3 : Obtenir la chaîne de connexion de l'entrepôt {#step-23-get-warehouse-connection-string}

Vous aurez besoin de l'endpoint SQL de votre entrepôt pour que Braze puisse se connecter. Pour récupérer l'endpoint SQL, accédez à l'**espace de travail** dans Fabric, et dans la liste des éléments, survolez le nom de l'entrepôt et sélectionnez **Copy SQL connection string**.
Conservez cette valeur pour la configuration des identifiants à l'étape 3.

#### Étape 2.4 : Autoriser les adresses IP de Braze dans le pare-feu (facultatif) {#step-24-allow-braze-ips-in-firewall-optional}

Selon la configuration de votre compte Microsoft Fabric, vous devrez peut-être autoriser les adresses IP suivantes dans votre pare-feu pour permettre le trafic depuis Braze. Pour plus d'informations sur l'activation de cette fonctionnalité, consultez la documentation pertinente sur l'[accès conditionnel Entra](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Étape 3 : Créer une source connectée dans le tableau de bord de Braze {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### Étape 3.1 : Ajouter les informations de connexion Snowflake et la table source {#step-31-add-snowflake-connection-information-and-source-table}

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, sélectionnez **Add data source**, puis sélectionnez **Snowflake**.

Dans **Setup source**, saisissez les informations suivantes :
- **Credentials :** **Account Locator**, **Username** et **Role**
- **Configuration :** **Warehouse**, **Database** et **Schema**

Si vous créez de nouveaux identifiants Snowflake, sélectionnez **Save credentials and generate RSA key** avant de tester la connexion.

#### Étape 3.2 : Configurer les détails de synchronisation {#step-32-configure-sync-details}

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segments CDI.

Configurez un temps d'exécution maximum pour cette source. Braze interrompra automatiquement toute requête dépassant le temps d'exécution maximum. Le temps d'exécution maximum autorisé est de 60 minutes ; un temps d'exécution inférieur réduira les coûts encourus sur votre compte Snowflake. Ce paramètre s'applique aux requêtes exécutées via cette source, y compris les synchronisations et les extensions de segments CDI qui l'utilisent.

{% alert note %}
Si les requêtes expirent régulièrement et que vous avez défini un temps d'exécution maximum de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus grand à l'utilisateur Braze.
{% endalert %}

#### Étape 3.3 : Noter la clé publique {#step-33-note-the-public-key}

Dans l'étape **Test connection**, notez la clé publique RSA. Vous en aurez besoin pour finaliser l'intégration dans Snowflake.

{% endtab %}
{% tab Redshift %}
#### Étape 3.1 : Ajouter les informations de connexion Redshift et la table source {#step-31-add-redshift-connection-information-and-source-table}

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, sélectionnez **Add data source**, puis sélectionnez **Amazon Redshift**.

Dans **Setup source**, saisissez les informations suivantes :
- **Credentials :** **Redshift Host URL**, **Username**, **Password** et **Port**
- **Configuration :** **Database** et **Schema**

Si nécessaire, activez **Connect with SSH Tunnel** et saisissez **Tunnel Host**, **Tunnel Port** et **Tunnel Username**.

#### Étape 3.2 : Configurer les détails de synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segments CDI.

Configurez un temps d'exécution maximum pour cette source. Braze interrompra automatiquement toute requête dépassant le temps d'exécution maximum. Le temps d'exécution maximum autorisé est de 60 minutes ; un temps d'exécution inférieur réduira les coûts encourus sur votre compte Redshift.
Ce paramètre s'applique aux requêtes exécutées via cette source, y compris les synchronisations et les extensions de segments CDI qui l'utilisent.

{% alert note %}
Si les requêtes expirent régulièrement et que vous avez défini un temps d'exécution maximum de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus grand à l'utilisateur Braze.
{% endalert %}

#### Étape 3.3 : Noter la clé publique (facultatif) {#step-33-note-the-public-key-optional}

Si vos identifiants ont l'option **Connect with SSH Tunnel** sélectionnée, notez la clé publique RSA dans l'étape **Test connection**. Vous en aurez besoin pour finaliser l'intégration dans Redshift.

{% endtab %}
{% tab BigQuery %}
#### Étape 3.1 : Ajouter les informations de connexion BigQuery et la table source {#step-31-add-bigquery-connection-information-and-source-table}

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, sélectionnez **Add data source**, puis sélectionnez **Google BigQuery**.

Dans **Setup source**, saisissez les informations suivantes :
- **Credentials :** **Credential name** et téléchargez votre **JSON key**
- **Configuration :** **Project** et **Dataset**

#### Étape 3.2 : Configurer les détails de synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segments CDI.

Configurez un temps d'exécution maximum pour cette source. Braze interrompra automatiquement toute requête dépassant le temps d'exécution maximum. Le temps d'exécution maximum autorisé est de 60 minutes ; un temps d'exécution inférieur réduira les coûts encourus sur votre compte BigQuery. Ce paramètre s'applique aux requêtes exécutées via cette source, y compris les synchronisations et les extensions de segments CDI qui l'utilisent.

{% alert note %}
Si les requêtes expirent régulièrement et que vous avez défini un temps d'exécution maximum de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus grand à l'utilisateur Braze.
{% endalert %}

#### Étape 3.3 : Tester la connexion {#step-33-test-the-connection}

Sélectionnez **Test Connection** pour vérifier que la liste des tables visibles par l'utilisateur correspond à vos attentes, puis sélectionnez **Done**. Votre source connectée est maintenant créée et prête à être utilisée dans les extensions de segments CDI.

{% endtab %}
{% tab Databricks %}
#### Étape 3.1 : Ajouter les informations de connexion Databricks et la table source {#step-31-add-databricks-connection-information-and-source-table}

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, sélectionnez **Add data source**, puis sélectionnez **Databricks**.

Dans **Setup source**, saisissez les informations suivantes :
- **Credentials :** **Credential Name**, **Hostname**, **HTTP Path** et **Access Token**
- **Configuration :** **Catalog** et **Schema**

#### Étape 3.2 : Configurer les détails de synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segments CDI.

Configurez un temps d'exécution maximum pour cette source. Braze interrompra automatiquement toute requête dépassant le temps d'exécution maximum. Le temps d'exécution maximum autorisé est de 60 minutes ; un temps d'exécution inférieur réduira les coûts encourus sur votre compte Databricks. Ce paramètre s'applique aux requêtes exécutées via cette source, y compris les synchronisations et les extensions de segments CDI qui l'utilisent.

{% alert note %}
Si les requêtes expirent régulièrement et que vous avez défini un temps d'exécution maximum de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de dédier un entrepôt plus grand à l'utilisateur Braze.
{% endalert %}

#### Étape 3.3 : Tester la connexion

Sélectionnez **Test Connection** pour vérifier que la liste des tables visibles par l'utilisateur correspond à vos attentes, puis sélectionnez **Done**. Votre source connectée est maintenant créée et prête à être utilisée dans les extensions de segments CDI.

{% endtab %}
{% tab Microsoft Fabric %}
#### Étape 3.1 : Ajouter les informations de connexion Microsoft Fabric et la table source {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Créez une source connectée dans le tableau de bord de Braze. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, sélectionnez **Add data source**, puis sélectionnez **Microsoft Fabric**.

Dans **Setup source**, saisissez les informations suivantes :
- **Credentials :** **Credentials Name**, **Tenant ID**, **Principal ID**, **Client Secret** et **Connection String**
- **Configuration :** **Database** et **Schema**

Si **Connect with SSH Tunnel** est disponible dans votre espace de travail et nécessaire pour votre configuration, saisissez également **Tunnel Host**, **Tunnel Port** et **Tunnel Username**.

#### Étape 3.2 : Configurer les détails de synchronisation

Choisissez un nom pour la source connectée. Ce nom sera utilisé dans la liste des sources disponibles lorsque vous créerez une nouvelle extension de segments CDI.

Configurez un temps d'exécution maximum pour cette source. Braze interrompra automatiquement toute requête dépassant le temps d'exécution maximum. Le temps d'exécution maximum autorisé est de 60 minutes ; un temps d'exécution inférieur réduira les coûts encourus sur votre compte Microsoft Fabric. Ce paramètre s'applique aux requêtes exécutées via cette source, y compris les synchronisations et les extensions de segments CDI qui l'utilisent.

{% alert note %}
Si les requêtes expirent régulièrement et que vous avez défini un temps d'exécution maximum de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou de mettre à l'échelle la capacité Fabric.
{% endalert %}

#### Étape 3.3 : Tester la connexion

Sélectionnez **Test Connection** pour vérifier que la liste des tables visibles par l'utilisateur correspond à vos attentes, puis sélectionnez **Done**. Votre source connectée est maintenant créée et prête à être utilisée dans les extensions de segments CDI.

{% endtab %}
{% endtabs %}

### Étape 4 : Finaliser la configuration de l'entrepôt de données {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
Ajoutez la clé publique que vous avez notée lors de la dernière étape à votre utilisateur dans Snowflake. Cela permettra à Braze de se connecter à Snowflake. Pour plus de détails sur la procédure, consultez la [documentation Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

Si vous souhaitez effectuer une rotation des clés à tout moment, vous pouvez créer une nouvelle clé publique en accédant à **Data Access Management** dans **Cloud Data Ingestion** et en sélectionnant **Generate New Key** pour le compte concerné.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Après avoir ajouté la clé à l'utilisateur dans Snowflake, sélectionnez **Test Connection** dans Braze, puis sélectionnez **Done**. Votre source connectée est maintenant créée et prête à être utilisée dans les extensions de segments CDI.
{% endtab %}

{% tab Redshift %}
Si vous vous connectez via un tunnel SSH, ajoutez la clé publique que vous avez notée lors de la dernière étape à l'utilisateur du tunnel SSH.

Après avoir ajouté la clé à l'utilisateur, sélectionnez **Test Connection** dans Braze, puis sélectionnez **Done**. Votre source connectée est maintenant créée et prête à être utilisée dans les extensions de segments CDI.

{% endtab %}
{% tab BigQuery %}
Cela ne s'applique pas à BigQuery.

{% endtab %}
{% tab Databricks %}
Cela ne s'applique pas à Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Cela ne s'applique pas à Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Vous devez tester une source avec succès avant qu'elle puisse passer de l'état « brouillon » à l'état « actif ». Si vous devez quitter la page de création, votre intégration sera enregistrée et vous pourrez revenir à la page de détails pour apporter des modifications et effectuer des tests.
{% endalert %}

## Configuration d'intégrations ou d'utilisateurs supplémentaires (facultatif) {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Vous pouvez configurer plusieurs intégrations avec Braze, mais chaque intégration doit être configurée pour se connecter à un schéma différent. Lors de la création de connexions supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Snowflake.

Si vous réutilisez le même utilisateur et le même rôle pour plusieurs intégrations, vous n'aurez pas besoin d'ajouter à nouveau la clé publique.
{% endtab %}

{% tab Redshift %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour se connecter à un schéma différent. Lors de la création de sources supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Redshift.
{% endtab %}

{% tab BigQuery %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour se connecter à un jeu de données différent. Lors de la création de sources supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte BigQuery.
{% endtab %}

{% tab Databricks %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour se connecter à un schéma différent. Lors de la création de sources supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Databricks.
{% endtab %}

{% tab Microsoft Fabric %}
Vous pouvez configurer plusieurs sources avec Braze, mais chaque source doit être configurée pour se connecter à un schéma différent. Lors de la création de sources supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Azure.
{% endtab %}
{% endtabs %}

## Utilisation de la source connectée {#using-the-connected-source}

Une fois la source créée, vous pouvez l'utiliser pour créer une ou plusieurs extensions de segments CDI. Pour plus d'informations sur la création d'un segment avec cette source, consultez la [documentation sur les extensions de segments CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).

{% alert note %}
Si les requêtes expirent régulièrement et que vous avez défini un temps d'exécution maximum de 60 minutes, essayez d'optimiser le temps d'exécution de vos requêtes ou d'allouer davantage de ressources de calcul (comme un entrepôt de données plus grand) à l'utilisateur Braze.
{% endalert %}