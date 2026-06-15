---
nav_title: LiveRamp
article_title: LiveRamp
description: "Apprenez à connecter LiveRamp, Snowflake et Braze afin de créer des campagnes marketing pertinentes et hautement personnalisées."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Connecter LiveRamp, Snowflake et Braze {#connect-liveramp-snowflake-and-braze}

> Apprenez à connecter LiveRamp, Snowflake et Braze afin de créer des campagnes marketing pertinentes et hautement personnalisées en réduisant le temps nécessaire pour obtenir des informations, en éliminant les silos de données et en optimisant l'engagement client. Cette intégration améliore le marketing axé sur les données en fournissant des informations exploitables basées sur les personnes et en consolidant les points de contact avec les consommateurs pour une meilleure segmentation de l'audience et des campagnes opportunes. Elle s'appuie également sur des benchmarks fournis par Snowflake pour vous aider à affiner vos stratégies marketing par rapport aux normes du secteur.

{% alert important %}
Le [partage de données sécurisé](https://docs.snowflake.com/en/user-guide/data-sharing-intro) de Snowflake ne transfère pas de données entre LiveRamp, Snowflake et Braze. Les données sont uniquement partagées via les services et le magasin de métadonnées de Snowflake, ce qui signifie qu'aucune donnée n'est copiée et qu'aucun frais de stockage supplémentaire n'est facturé. L'accès aux données partagées est contrôlé et régi à l'aide des contrôles d'accès de votre compte Snowflake.
{% endalert %}

## Cas d'utilisation {#use-cases}

- **Minimisation des données :** L'application d'activation de LiveRamp utilise la fonctionnalité de partage de données sécurisé de Snowflake pour lire efficacement les tables directement depuis votre instance. Aucune donnée n'est transférée depuis Snowflake jusqu'au point de distribution au partenaire en aval.
- **Activation sécurisée des données first party :** En utilisant l'application Identity Resolution mentionnée ci-dessus, l'application d'activation de LiveRamp utilisera uniquement les tables basées sur RampID dans votre instance Snowflake, et les informations personnelles n'auront donc jamais à quitter votre environnement.
- **Accélérer la mise en production :** En résolvant les données en RampID directement dans votre environnement, la distribution vers une destination finale peut s'effectuer en quelques heures, contre plusieurs jours avec l'approche plus traditionnelle basée sur les fichiers de LiveRamp. Cela augmente considérablement la capacité à optimiser les performances des campagnes au moment opportun.
- **Économies opérationnelles :** De même, grâce à la fonctionnalité de partage de données sécurisé de Snowflake, les clients économisent du temps et de l'argent par rapport à la coordination du transfert des fichiers vers LiveRamp ou vers n'importe quelle destination finale.

## Conditions préalables {#prerequisites}

| Prérequis | Description |
|-----------|-------------|
| Compte Snowflake | Vous avez besoin d'un compte Snowflake avec des autorisations de niveau administrateur. |
| Compte LiveRamp | Contactez votre équipe LiveRamp ou [snowflake@liveramp.com](mailto:snowflake@liveramp.com) pour discuter des applications LiveRamp requises dans Snowflake. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Configuration de l'intégration {#setting-up-the-integration}

### Étape 1 : Demander un partage de données à Braze {#step-1-request-a-data-share-from-braze}

Tout d'abord, contactez votre gestionnaire de compte Braze ou votre gestionnaire de la satisfaction client pour acheter un connecteur de partage de données Snowflake pour votre compte Braze. Lorsque vous demandez un partage de données, Braze fournira le partage depuis le ou les espaces de travail pour lesquels l'achat a été effectué. Une fois le partage configuré, toutes les données sont immédiatement accessibles depuis votre instance Snowflake sous la forme d'un partage de données entrant. Une fois que le partage est visible dans votre instance, créez une base de données à partir du partage afin de pouvoir voir et interroger les tables.

Pour une procédure pas à pas complète, consultez le [guide d'intégration de Snowflake avec Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Étape 2 : Configurer l'application LiveRamp dans Snowflake {#step-2-set-up-the-liveramp-app-in-snowflake}

Les fonctionnalités de traduction et de résolution d'identité sont disponibles dans Snowflake via l'application native LiveRamp Identity Resolution and Translation, qui crée un partage sur votre compte, ouvrant une vue pour interroger l'ensemble de données de référence depuis votre propre environnement Snowflake.

Pour configurer l'application native, suivez ces étapes dans la documentation LiveRamp : [Set Up the LiveRamp Native App in Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Lorsque vous avez terminé, passez à l'étape suivante.

### Étape 3 : Créer une table de données {#step-3-create-a-data-table}

{% alert warning %}
Avant de préparer des tables basées sur des informations personnelles, assurez-vous de bien comprendre le [filtre de confidentialité de LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) qui est exécuté pendant les tâches pour garantir que les colonnes d'attributs (non-identifiants) de vos tables d'entrée ne contiennent pas de valeurs trop uniques. Cela est essentiel pour préserver la confidentialité des consommateurs et éviter toute réidentification.
{% endalert %}

Ensuite, créez une table de données au [format requis](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) qui sera appelée par le biais de l'application native LiveRamp. Reportez-vous aux catégories suivantes pour déterminer lesquels de vos identifiants peuvent faire l'objet d'une résolution :

| Type d'identifiant | Description |
|-----------------|--------------|
| PII complet | Les informations personnelles identifiables (PII) incluent le nom, l'adresse postale, l'e-mail et le numéro de téléphone de l'utilisateur. **Remarque :** tous les identifiants ne sont pas requis pour chaque enregistrement. |
| E-mail uniquement | Les adresses e-mail de l'utilisateur, telles que `alex-lee@email.com`. |
| Appareil | Cela inclut les cookies tiers, les identifiants publicitaires mobiles (MAID), les identifiants de télévision connectée (CTV ID) et les RampID (résolus en RampID de foyer). |
| CID | Il s'agit d'identifiants provenant d'un partenaire de plateforme ou d'une synchronisation d'identité avec LiveRamp, tels que votre identifiant client interne. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 3 : Créer une table de données" }

#### Identifiants Braze {#braze-identifiers}

Les journaux d'événements de Braze contiennent des identifiants que vous pouvez utiliser dans l'application native LiveRamp. Pour obtenir la liste complète des identifiants disponibles pour chaque type d'événement, téléchargez les [schémas et identifiants d'événements Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).

| Type d'identifiant | Description |
|-----------------|--------------|
| `AD_ID` | Les identifiants publicitaires, tels que `ios_idfa`, `google_ad_id` et `roku_ad_id`, capturés dans le cadre de types d'événements particuliers, peuvent être utilisés conjointement avec les services de résolution des appareils de LiveRamp. Par défaut, les identifiants publicitaires ne sont pas collectés&#8212;toutefois, vous pouvez activer le suivi en suivant la [documentation de Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS` | Adresse e-mail pouvant être utilisée conjointement avec les services de résolution par e-mail uniquement de LiveRamp. |
| `TO_PHONE_NUMBER` | Numéro de téléphone pouvant être utilisé conjointement avec les services de résolution PII de LiveRamp. |
| `EXTERNAL_USER_ID` | L'ID externe associé à un utilisateur, pouvant être utilisé conjointement avec les services de résolution des appareils (CID) de LiveRamp. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Identifiants Braze" }

{% alert important %}
L'utilisation de tout identifiant personnalisé spécifique à un client ou à une marque dans l'application de LiveRamp nécessite une [synchronisation d'identité avec LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Étape 4 : Définir vos variables {#step-4-set-your-variables}

Ensuite, définissez vos variables pour la tâche dans la feuille de travail des étapes d'exécution fournie dans l'application. Cela inclut des détails tels que la base de données cible, les tables associées (données d'entrée, indicateurs, journalisation) et la définition du nom de la table de sortie. Pour une procédure pas à pas complète, consultez [LiveRamp : Specify the Variables](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### Étape 5 : Créer la table de métadonnées pour la résolution des PII {#step-5-create-the-metadata-table-for-pii-resolution}

Maintenant que vos variables sont définies, créez la table de métadonnées pour la résolution des PII. Celle-ci fournira des détails sur le type de tâche spécifique à exécuter en fonction de la catégorie d'identifiants impliquée. Pour une procédure pas à pas complète, consultez [LiveRamp : Create the Metadata Table](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Étape 6 : Effectuer l'opération de résolution d'identité {#step-6-perform-the-identity-resolution-operation}

Enfin, effectuez l'opération de résolution d'identité. Pour une procédure pas à pas complète, consultez [LiveRamp : Perform the Identity Resolution Operation](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab exemple d'entrée %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab exemple de sortie %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Prochaines étapes {#next-steps}

Vos données étant désormais pseudonymisées selon votre encodage dédié de RampID, vous avez la possibilité de partager les tables basées sur RampID avec l'application Managed Activation de LiveRamp pour une distribution simplifiée vers vos principaux partenaires de plateformes publicitaires. L'application d'activation comprend une interface conviviale pour les utilisateurs professionnels permettant une segmentation supplémentaire et la sélection/configuration des partenaires de destination en aval. Pour plus de détails sur l'application, contactez votre équipe de compte LiveRamp ou [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Résolution des problèmes {#troubleshooting}

{% alert note %}
Si vous avez des problèmes ou des questions plus spécifiques, contactez [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Régions Snowflake {#snowflake-regions}

Actuellement, cette application n'est disponible que pour les régions américaines suivantes :

  - aws-us-east-1 : POA18931
  - aws-us-west-2 : FAA28932
  - azure-east-us-2 : BL60425

### Confidentialité et valeurs des colonnes {#privacy-column-values}

Le processus évalue la combinaison de toutes les valeurs de colonne par ligne pour détecter les valeurs uniques. Si une combinaison particulière de valeurs de colonne apparaît 3 fois ou moins, les lignes contenant ces valeurs ne pourront pas être mises en correspondance et ne seront pas renvoyées dans la table de sortie. De même, pour garantir la confidentialité, le service LiveRamp évalue le caractère unique des combinaisons de valeurs de colonnes, garantissant ainsi que si plus de 5 % des lignes du fichier deviennent non appariables en raison de combinaisons rares, la tâche échouera.

### Données historiques {#historical-data}

Les données historiques dans Snowflake remontent à avril 2019, mais il peut y avoir de légères différences dans les données antérieures à août 2019 en raison de changements de produit.

### Vitesse, performance et coût {#speed-performance-cost}

La rapidité et le coût des requêtes dépendent de la taille de l'entrepôt utilisé. Tenez compte de vos besoins en matière d'accès aux données lors de la sélection de la taille de l'entrepôt.

### Benchmarks Braze {#braze-benchmarks}

Les benchmarks vous permettent de comparer vos indicateurs aux normes du secteur, disponibles directement dans le Snowflake Data Exchange.

### Changements disruptifs et non disruptifs {#breaking-vs-non-breaking-changes}

Soyez attentif aux changements qui peuvent affecter votre intégration. Les changements disruptifs seront précédés d'une annonce et d'une période de migration.