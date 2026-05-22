---
nav_title: Treasure Data
article_title: Importation de cohortes Treasure Data
description: "Cet article de référence décrit la fonctionnalité d'importation de cohortes de Treasure Data."
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# Importation de cohortes Treasure Data {#treasure-data-cohort-import}

> Cet article décrit comment importer des cohortes d'utilisateurs de Treasure Data vers Braze afin de pouvoir envoyer des campagnes ciblées basées sur des données qui peuvent n'exister que dans votre entrepôt.

{% alert important %}
Cette fonctionnalité est actuellement en version bêta. Pour plus d'informations, contactez vos conseillers Treasure Data et Braze.
{% endalert %}

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Treasure Data | Un compte [Treasure Data](https://www.treasuredata.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'importation des données Braze | Cette clé peut être récupérée dans le tableau de bord de Braze depuis **Intégrations partenaires** > **Partenaires technologiques**, puis en sélectionnant **Treasure Data**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Adresse IP statique de Treasure Data | L'adresse IP statique de Treasure Data est le point d'accès et la source du lien de cette intégration. Pour déterminer l'adresse IP statique, contactez votre conseiller en satisfaction client Treasure Data ou l'assistance technique de Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration de l'importation de données {#data-import-integration}

### Étape 1 : Obtenir votre clé d'importation des données Braze {#step-1-get-your-braze-data-import-key}

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Treasure Data**. Vous y trouverez votre endpoint REST et pourrez générer votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.

### Étape 2 : Créer une connexion de données {#step-2-create-a-data-connection}

Avant de créer votre connexion de données dans Treasure Data, vous devez vous authentifier. Commencez par sélectionner **Integrations Hub**, puis **Catalog**.

![Catalogue du centre d'intégrations Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %})

Recherchez l'intégration Braze dans le **Catalog**, puis survolez l'icône et sélectionnez **Create Authentication**. Saisissez vos identifiants, nommez votre authentification, puis sélectionnez **Done**.

![Catalogue du centre d'intégrations Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %})

### Étape 3 : Définir l'audience de votre cohorte {#step-3-define-your-cohort-audience}

Synchronisez vos cohortes avec Braze par le biais d'une activation dans l'**Audience Studio** ou en exécutant une requête dans le **Data Workbench**.

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze sont ajoutés ou supprimés d'une cohorte. L'importation de cohortes ne crée pas de nouveaux utilisateurs dans Braze.
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### Étape 3.1 : Définir votre requête {#step-31-define-your-query}

{% alert note %}
Les colonnes de la requête doivent être spécifiées avec les noms de colonnes et le type de données exacts. Les colonnes de la requête doivent inclure au moins l'une des colonnes suivantes : `user_ids`, `device_ids` ou la colonne d'alias Braze correspondant à la configuration dans l'interface. Seuls les profils utilisateurs existant dans Braze seront ajoutés à une cohorte. L'importation de cohortes ne crée pas de nouveaux profils utilisateurs.
{% endalert %}

1. Naviguez vers **Data Workbench** > **Queries**.
2. Sélectionnez **New Query**.
3. Exécutez la requête pour valider l'ensemble des résultats.

![Catalogue du centre d'intégrations Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Cas d'utilisation : synchronisation des cohortes par identifiant {#use-case-syncing-cohorts-by-identifier}

{% subtabs local %}
{% subtab Syncing External IDs %}
Voici un exemple de tableau dans Treasure Data :

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
Le nom de la colonne doit être `user_ids`, sinon la synchronisation échouera.
{% endalert %}

Pour synchroniser les cohortes à l'aide de l'ID externe, exécutez la requête suivante :

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Après l'exécution de la requête, ces alias d'utilisateurs seront ajoutés à la cohorte dans Braze :

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Voici un exemple de tableau dans Treasure Data :

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

Pour synchroniser les cohortes à l'aide de l'alias d'utilisateur, exécutez la requête suivante :

```sql
SELECT
  email
FROM
  example_cohort_table
```

Après l'exécution de la requête, ces alias d'utilisateurs seront ajoutés à la cohorte dans Braze :

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Voici un exemple de tableau dans Treasure Data :

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
Le nom de la colonne doit être `device_ids`, sinon la synchronisation échouera.
{% endalert %}

Pour synchroniser les cohortes à l'aide de l'ID d'appareil, exécutez la requête suivante :

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Après l'exécution de la requête, ces ID d'appareils seront ajoutés à la cohorte dans Braze :

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Étape 3.2 : Spécifier la cible d'exportation des résultats {#step-32-specify-the-result-export-target}

Une fois la requête créée, sélectionnez **Export Results**. Vous pouvez sélectionner une authentification existante, telle que celle créée lors des étapes précédentes, ou créer une nouvelle authentification à utiliser pour la sortie.

![Catalogue du centre d'intégrations Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %})


| Mappage de l'exportation des résultats |	Description	|
| ----------- | ----------- |
| ID de la cohorte	| Il s'agit de l'identifiant backend de la cohorte qui sera envoyé à Braze. 	|
| Nom de la cohorte (facultatif)	| C'est le nom qui apparaîtra dans le filtre de cohorte de l'outil de segmentation de Braze. Si ce paramètre n'est pas défini, la valeur `Cohort ID` sera utilisée comme `Cohort Name`.	|
| Opération	| Détermine si la requête doit ajouter ou supprimer des profils de la cohorte dans Braze.	|
| Alias (facultatif) | Lorsqu'il est défini, le nom de la colonne correspondante dans votre requête sera envoyé en tant que `alias_label`, et les valeurs de chaque ligne de la colonne seront envoyées en tant que `alias_name`.	|
| Nombre de threads | Nombre d'appels API simultanés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Specify the result export target" }

Suivez [les étapes de Treasure Data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) pour configurer votre exportation en fonction de votre cas d'utilisation.

#### Étape 3.3 : Exécuter la requête {#step-33-execute-the-query}

Enregistrez la requête en lui donnant un nom et exécutez-la, ou exécutez simplement la requête. Une fois la requête terminée avec succès, le résultat est automatiquement exporté vers Braze.

{% endtab %}
{% tab Audience Studio %}
#### Étape 3.1 : Créer une activation {#step-31-create-an-activation}

Créez un nouveau segment ou choisissez un segment existant à synchroniser avec Braze en tant que cohorte. Dans le segment, sélectionnez **Create Activation**.

#### Étape 3.2 : Renseigner les détails de votre activation {#step-32-fill-out-your-activation-details}

![Détails de l'activation Treasure Data Integrations]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %})

| Paramètre des détails de l'activation |	Description	|
| ----------- | ----------- |
| Nom de l'activation	| Le nom de votre activation.	|
| Description de l'activation | Une brève description de l'activation.	|
| Authentification	| Choisissez l'authentification de la cohorte Braze créée à l'étape 2.	|
| ID de la cohorte	| Il s'agit de l'identifiant backend de la cohorte qui sera envoyé à Braze. 	|
| Nom de la cohorte (facultatif)	| C'est le nom qui apparaîtra dans le filtre de cohorte de l'outil de segmentation de Braze. Si ce paramètre n'est pas défini, la valeur `Cohort ID` sera utilisée comme `Cohort Name`.	|
| Opération	| Détermine si la requête doit ajouter ou supprimer des profils de la cohorte dans Braze.	|
| Alias (facultatif) | Lorsqu'il est défini, le nom de la colonne correspondante dans votre requête sera envoyé en tant que `alias_label`, et les valeurs de chaque ligne de la colonne seront envoyées en tant que `alias_name`.	|
| Nombre de threads | Nombre d'appels API simultanés. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Fill out your activation details" }

#### Étape 3.3 : Configurer le mappage des sorties {#step-33-set-up-output-mapping}

![Mappage des sorties de l'activation Treasure Data Integrations]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %})

| Mappage des sorties de l'activation |	Description	|
| ----------- | ----------- |
| Colonnes d'attributs	| Déterminez les colonnes de votre base de données de segments qui seront mappées en tant qu'identifiants lors de la synchronisation des profils vers une cohorte Braze.	|
| Générateur de chaînes de caractères | Le générateur de chaînes de caractères n'est pas nécessaire pour l'intégration Braze.	|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.3: Set up output mapping" }

{% alert important %}
 - Si vous utilisez `device_id` comme identifiant, le **nom de la colonne de sortie** doit être `device_ids`.
 - Lorsque vous utilisez des alias comme identifiant, le **nom de la colonne de sortie** doit être le nom de la colonne correspondante dans votre requête, qui sera envoyé en tant que `alias_label`, et les valeurs de chaque ligne de la colonne seront envoyées en tant que `alias_name`.
 - Si vous utilisez `external_id` comme identifiant, le **nom de la colonne de sortie** doit être `user_ids`.
{% endalert %}

Tous les noms de colonnes non pertinents ou mal nommés seront ignorés. Vous pouvez choisir d'utiliser plus d'un identifiant dans vos synchronisations.

#### Étape 3.4 : Définir votre planification d'activation {#step-34-define-your-activation-schedule}

Définissez la planification de synchronisation souhaitée et enregistrez votre activation.

![Planification de l'activation Treasure Data Integrations]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### Étape 4 : Créer un segment Braze à partir de l'exportation Treasure Data {#step-4-create-a-braze-segment-from-the-treasure-data-export}

Dans Braze, naviguez vers **Segments**, créez un nouveau segment et sélectionnez **Treasure Data Cohorts** comme filtre. Vous pouvez alors choisir la cohorte Treasure Data que vous souhaitez inclure. Une fois votre segment de cohorte Treasure Data créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

![Catalogue du centre d'intégrations Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %})

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs identifiés peuvent être associés par leur `external_id` ou leur `alias`. Les utilisateurs anonymes peuvent être associés par leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id` et doivent être identifiés par leur `external_id` ou leur `alias`.