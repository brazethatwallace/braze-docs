---
nav_title: Éditeur SQL
article_title: "Ingestion de données cloud : éditeur SQL"
description: "Découvrez comment créer et valider des synchronisations d'ingestion de données cloud avec des requêtes SQL."
page_order: 11
page_type: reference
toc_headers: h2
---

# Ingestion de données cloud : éditeur SQL {#cloud-data-ingestion-sql-editor}

> Cette page explique comment utiliser l'éditeur SQL de l'ingestion de données cloud (CDI) de Braze pour créer et valider des synchronisations avec des requêtes SQL.

L'éditeur SQL de l'ingestion de données cloud vous permet de créer des synchronisations en écrivant des requêtes SQL directement sur votre entrepôt de données. Cela supprime la nécessité de créer ou de maintenir une table CDI dédiée, ce qui était auparavant requis dans l'[étape 1.1 des intégrations d'entrepôt de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

Utilisez l'éditeur SQL lorsque vous souhaitez :

- Synchroniser des données sans modifier les tables en amont
- Travailler avec des données brutes dans votre entrepôt
- Éviter de construire une colonne `PAYLOAD`
- Gérer des cas d'utilisation de données plus complexes avec SQL

{% alert important %}
L'éditeur SQL de l'ingestion de données cloud est en bêta. Contactez votre gestionnaire de la satisfaction client ou votre gestionnaire de compte pour y accéder.
{% endalert %}

## Conditions préalables et limitations {#prerequisites-and-limitations}

L'éditeur SQL présente les limitations suivantes :

- Disponible uniquement pour les sources d'entrepôt de données : Snowflake, Redshift, BigQuery, Databricks et Fabric.
- Seules les requêtes en lecture seule à instruction unique sont prises en charge.

{% alert note %}
Braze exécute uniquement des requêtes en lecture seule sur vos données et ne modifie pas vos tables sous-jacentes. Des objets temporaires peuvent être créés pendant l'exécution des requêtes, mais ne sont pas conservés.
{% endalert %}

## Créer une nouvelle synchronisation avec l'éditeur SQL {#create-a-new-sql-editor-sync}

Suivez ces étapes pour créer d'abord une source, puis une synchronisation avec l'éditeur SQL. Si vous avez déjà configuré une source pour CDI, vous pouvez passer à l'étape 3.

{% alert note %}
Notez que ces étapes utilisent une source Snowflake comme exemple. Le processus de configuration pour les autres sources d'entrepôt de données est similaire et peut être consulté dans l'[étape 2 : Créer une nouvelle source dans le tableau de bord de Braze](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations#step-2-create-a-new-source-in-the-braze-dashboard) de la documentation [Configuration des intégrations d'entrepôt de données](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations).
{% endalert %}

### Étape 1 : Configurer votre rôle, vos autorisations, votre entrepôt et votre utilisateur Snowflake {#step-1-set-up-your-snowflake-role-permissions-warehouse-and-user}

Avant de créer votre source Snowflake dans CDI, assurez-vous que l'utilisateur Snowflake utilisé par Braze a accès aux données que vous souhaitez interroger et à un entrepôt pour exécuter les requêtes.

#### Étape 1.1 : (Facultatif) Créer une base de données et un schéma {#step-11-optional-create-a-database-and-schema}

Si nécessaire, créez une base de données et un schéma dédiés pour vos données CDI :

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### Étape 1.2 : Configurer le rôle et les autorisations de base de données {#step-12-set-up-role-and-database-permissions}

Accordez l'accès aux tables que vous souhaitez synchroniser :

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

Vous pouvez également accorder l'accès à plusieurs tables ou à des tables futures, selon votre cas d'utilisation. Par exemple, pour accorder l'accès à toutes les futures tables d'un schéma :

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### Étape 1.3 : Configurer l'entrepôt et accorder l'accès au rôle Braze {#step-13-set-up-the-warehouse-and-grant-access-to-the-braze-role}

Créez un entrepôt pour que Braze puisse exécuter des requêtes :

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
L'entrepôt doit avoir la reprise automatique activée. Si ce n'est pas le cas, accordez à Braze des privilèges `OPERATE` supplémentaires sur l'entrepôt afin que Braze puisse l'activer lors de l'exécution de la requête.
{% endalert %}

#### Étape 1.4 : Créer un utilisateur Snowflake {#step-14-create-a-snowflake-user}

Créez un utilisateur pour Braze et attribuez-lui le rôle :

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Vous utiliserez cet utilisateur lorsque vous configurerez votre source Snowflake dans Braze.

### Étape 2 : Créer une nouvelle source dans le tableau de bord de Braze {#step-2-create-a-new-source-in-the-braze-dashboard}

Dans cette étape, créez votre source Snowflake dans Braze et validez la connexion.

#### Étape 2.1 : Ajouter une source Snowflake {#step-21-add-a-snowflake-source}

1. Dans le tableau de bord de Braze, accédez à **Paramètres des données** > **Ingestion de données cloud** > **Sources**.
2. Sélectionnez **Add data source**.
3. Sélectionnez **Snowflake**.

#### Étape 2.2 : Saisir les détails de connexion {#step-22-enter-connection-details}

Choisissez un nom pour votre source et saisissez vos identifiants et votre configuration Snowflake.

{% alert note %}
Pour le champ **Snowflake Account Locator**, saisissez votre [identifiant de compte](https://docs.snowflake.com/en/user-guide/admin-account-identifier) Snowflake, qui suit généralement un format tel que `xy12345.us-east-1.aws`. Ce n'est pas la même chose qu'un nom de base de données ou un nom d'entrepôt.
{% endalert %}

#### Étape 2.3 : Terminer la configuration de la clé RSA {#step-23-complete-rsa-key-setup}

Après avoir saisi vos identifiants et votre configuration, sélectionnez **Save credentials** et générez une clé RSA. Retournez ensuite dans Snowflake pour terminer la configuration. Ajoutez la clé publique affichée dans le tableau de bord à l'utilisateur que vous avez créé pour que Braze puisse se connecter à Snowflake.

Pour plus d'informations, consultez la documentation sur l'[authentification par paire de clés Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth). Si vous souhaitez effectuer une rotation des clés à tout moment, Braze peut générer une nouvelle paire de clés et fournir la nouvelle clé publique.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

De retour dans Braze, sélectionnez **Test connection** pour vérifier l'accès à la source, puis créez la source.

### Étape 3 : Créer une nouvelle synchronisation et écrire votre requête SQL {#step-3-create-a-new-sync-and-write-your-sql-query}

1. Accédez à **Paramètres des données** > **Ingestion de données cloud** > **Syncs**.
2. Sélectionnez **Create data sync**.
3. Choisissez n'importe quelle synchronisation sous **Data Type**.
4. Référencez la source de l'étape 2.
5. Sélectionnez **SQL** et écrivez une requête SQL qui renvoie les données utilisateur de votre entrepôt. Votre requête SQL définit les données qui se synchronisent vers Braze. Le résultat de la requête devient le schéma de votre synchronisation.

Vous pouvez utiliser l'explorateur de sources pour parcourir les tables et vues disponibles à synchroniser, ou le générateur SQL par intelligence artificielle pour obtenir l'aide de Braze Operator sur votre requête SQL.

{% alert note %}
Seules les requêtes en lecture seule sont prises en charge, y compris les clauses `JOIN`. Pour plus de détails, consultez [Contraintes SQL](#sql-constraints).
{% endalert %}

### Étape 4 : Prévisualiser et valider votre requête {#step-4-preview-and-validate-your-query}

Sélectionnez **Preview and validate** pour exécuter votre requête.

La prévisualisation :

- Affiche les résultats sous forme de tableau
- Montre jusqu'à 100 lignes
- Montre jusqu'à 250 colonnes

Pour que la validation réussisse, votre requête SQL doit renvoyer différentes colonnes requises :

| Type de données de synchronisation | Colonnes requises |
|---|---|
| Attributs | - Un identifiant utilisateur, l'un des suivants : `external_id`, `braze_id`, `alias_name` et `alias_label`, e-mail ou numéro de téléphone.<br>- `UPDATED_AT`.<br>- Au moins une colonne supplémentaire (attribut) à synchroniser. |
| Supprimer des utilisateurs | - Un identifiant utilisateur, l'un des suivants : `external_id`, `braze_id`, `alias_name` et `alias_label`, e-mail ou numéro de téléphone.<br>- `UPDATED_AT`. |
| Déclencheurs Canvas | - Un identifiant utilisateur, l'un des suivants : `external_id`, `braze_id`, `alias_name` et `alias_label`, e-mail ou numéro de téléphone.<br>- `UPDATED_AT`. |
| Événements personnalisés | - Un identifiant utilisateur, l'un des suivants : `external_id`, `braze_id`, `alias_name` et `alias_label`, e-mail ou numéro de téléphone.<br>- `UPDATED_AT`.<br>- `NAME` pour représenter le nom de l'événement.<br>- `TIME` pour représenter l'heure de l'événement. Si indisponible, CDI utilise `UPDATED_AT` comme substitut. |
| Événements d'achat | - Un identifiant utilisateur, l'un des suivants : `external_id`, `braze_id`, `alias_name` et `alias_label`, e-mail ou numéro de téléphone.<br>- `UPDATED_AT`.<br>- `PRODUCT_ID`.<br>- `CURRENCY`.<br>- `PRICE`.<br>- `TIME` pour représenter l'heure de l'événement d'achat. Si indisponible, CDI utilise `UPDATED_AT` comme substitut. |
| Catalogue | - `ID` pour représenter l'identifiant de l'élément du catalogue.<br>- `UPDATED_AT`.<br>- Au moins une colonne supplémentaire (champ de catalogue) à synchroniser. |
| Comptes | - `ID` pour représenter l'identifiant du compte.<br>- `NAME` pour représenter le nom du compte.<br>- `UPDATED_AT`.<br>- Au moins une colonne supplémentaire (champ de compte) à synchroniser. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 4 : Prévisualiser et valider votre requête" }

Les colonnes supplémentaires en dehors des colonnes requises sont synchronisées respectivement en tant qu'attributs, propriétés de contexte Canvas, propriétés d'événement, champs de catalogue et champs de compte. Consultez [Comportement de validation](#validation-behavior) et [Résolution des problèmes](#troubleshooting) pour des conseils utiles sur les erreurs de prévisualisation et de validation et comment les corriger.

### Étape 5 : Vérifier le mappage des attributs et créer la synchronisation {#step-5-review-attribute-mapping-and-create-sync}

Lorsque la validation réussit, continuez vers **Next: Notifications** et créez votre synchronisation.

{% alert important %}
Une configuration SQL incorrecte peut entraîner des résultats non souhaités, y compris une surconsommation de points de données et des risques opérationnels plus larges. Vous êtes responsable de vous assurer que la logique de votre requête est correcte et devez prévisualiser attentivement tous les résultats avant d'activer une synchronisation.
{% endalert %}

## Contraintes SQL {#sql-constraints}

### Utiliser uniquement des requêtes `SELECT` {#use-select-queries-only}

Seules les requêtes en lecture seule sont prises en charge.

Vous pouvez utiliser :

- `SELECT`
- `WITH` (CTE)
- `JOIN`

Vous ne pouvez pas utiliser :

- `INSERT`, `UPDATE` ou `DELETE`
- `CREATE` ou `DROP`
- Plusieurs instructions séparées par `;`

### Utiliser une seule instruction {#use-a-single-statement}

Votre requête doit être une seule instruction exécutable.

## Comportement de validation {#validation-behavior}

L'éditeur SQL valide votre requête avant de vous permettre de continuer.

### Erreurs SQL {#sql-errors}

Si votre requête contient des erreurs de syntaxe :

- La validation échoue
- Aucune prévisualisation n'apparaît
- Votre entrepôt renvoie un message d'erreur

### Erreurs de compilation {#compilation-errors}

Si votre requête fait référence à des tables, colonnes ou objets invalides ou non autorisés :

- La validation échoue
- Aucune prévisualisation n'apparaît
- Votre entrepôt renvoie un message d'erreur

### Erreurs de connexion {#connection-errors}

Si Braze ne peut pas se connecter à votre entrepôt :

- La validation échoue
- Aucune prévisualisation n'apparaît
- Un message d'erreur de connexion apparaît

### Expiration de la requête {#query-timeout}

Si votre requête s'exécute trop longtemps :

- Braze met fin à la requête
- La validation échoue
- Une erreur d'expiration apparaît

### Erreurs de schéma de table {#table-schema-errors}

Si votre requête compile, la validation peut tout de même échouer si :

- Aucune colonne d'identifiant n'est trouvée
- `UPDATED_AT` est absente
- D'autres colonnes requises sont manquantes

Dans ce cas, la prévisualisation apparaît tout de même pour vous aider à atteindre une validation réussie. Consultez l'[étape 4 de la section précédente](#step-4-preview-and-validate-your-query) pour plus de détails sur les colonnes requises pour chaque type de données de synchronisation.

### Résultats à zéro ligne {#zero-row-results}

Si votre requête renvoie zéro ligne :

- La validation **réussit**
- Vous pouvez tout de même créer la synchronisation
- Aucun utilisateur n'est mis à jour tant que des lignes ne sont pas renvoyées

## Prise en charge de `PAYLOAD` (hérité) {#payload-support-legacy}

L'éditeur SQL prend en charge les [tables CDI héritées]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-1-set-up-tables-or-views) où une colonne `PAYLOAD` est présente.

Si votre requête inclut :

- Un identifiant valide
- `UPDATED_AT`
- Une colonne `PAYLOAD`
- Des colonnes supplémentaires

Alors :

- Braze synchronise uniquement la colonne `PAYLOAD`
- Braze ignore les colonnes supplémentaires

## Modifier une synchronisation SQL {#edit-a-sql-sync}

Lors de la modification d'une synchronisation existante :

- Toute modification SQL nécessite une revalidation
- Vous ne pouvez pas enregistrer des modifications invalides
- Les modifications valides prennent effet après l'enregistrement

Si une exécution de synchronisation est déjà en cours, vos modifications prennent effet lors de la prochaine exécution.

## Résolution des problèmes {#troubleshooting}

Cette section présente les erreurs courantes et des conseils pour les résoudre.

### Aucune prévisualisation disponible {#no-preview-available}

Lorsque vous voyez « No preview available », l'un des types d'erreur sous-jacents suivants peut en être la cause.

| Type d'erreur | Étapes de résolution |
|---|---|
| « No preview available » | Lisez la bannière d'erreur pour obtenir des indices. |
| « Unable to connect to the source » | Vérifiez le nom d'utilisateur configuré, le localisateur de compte et la configuration de l'authentification par paire de clés RSA.<br>Vérifiez que l'entrepôt est en cours d'exécution.<br>Confirmez l'accès réseau. |
| « SQL syntax error » | Vérifiez votre syntaxe SQL. |
| « Object does not exist or not authorized » | Assurez-vous que le rôle dispose d'un accès `SELECT` à la table.<br>Confirmez les autorisations de base de données et de schéma.<br>Vérifiez les fautes de frappe dans le nom de la table. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aucune prévisualisation disponible" }

### Colonne d'identité requise {#identity-column-required}

Assurez-vous que votre requête inclut un identifiant valide, tel que `external_id`.

### La colonne `UPDATED_AT` est manquante {#updated_at-column-is-missing}

Ajoutez une colonne d'horodatage pour la synchronisation incrémentielle.

### Ajoutez plus de colonnes… Il n'y a aucun attribut/champ de catalogue/champ de compte à synchroniser {#add-more-columns-there-are-no-attributescatalog-fieldsaccount-fields-to-sync}

Ajoutez au moins une colonne supplémentaire en plus de l'identifiant et de `UPDATED_AT`.

### L'exécution de la requête a expiré {#query-execution-timed-out}

Optimisez votre requête ou utilisez un entrepôt plus grand.