---
nav_title: Synchroniser les données de Decisioning Studio
article_title: "Synchroniser les données de BrazeAI Decisioning Studio"
description: "Découvrez comment synchroniser les tables de votre entrepôt de données vers BrazeAI Decisioning Studio à l'aide de l'ingestion de données cloud."
page_order: 6.5
page_type: reference
toc_headers: h2
---

# Synchroniser les données de BrazeAI Decisioning Studio {#sync-brazeai-decisioning-studio-data}

> Cette page explique comment synchroniser les données de votre entrepôt de données directement vers BrazeAI Decisioning Studio™ à l'aide de l'ingestion de données cloud (CDI).

Grâce à la destination Decisioning Studio de CDI, vous pouvez synchroniser les données de votre entrepôt directement vers BrazeAI Decisioning Studio. Les données issues de ces synchronisations sont mises à disposition de Decisioning Studio pour l'activation, mais vos profils utilisateur et vos espaces de travail Braze restent inchangés.

{% alert important %}
Cette fonctionnalité est en accès anticipé. Contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour y accéder.
{% endalert %}

## Comment ça fonctionne {#how-it-works}

Lorsque vous créez une synchronisation, choisissez Decisioning Studio comme destination et rédigez une requête SQL qui renvoie les données que vous souhaitez synchroniser. CDI exécute cette requête selon la planification que vous définissez et transmet les résultats sous forme de ressource Decisioning Studio. Chaque synchronisation correspond à une seule ressource : vous ne pouvez donc pas associer plusieurs synchronisations à la même ressource.

Contrairement aux synchronisations vers la plateforme de données Braze, les synchronisations Decisioning Studio ne mappent pas vos données à des profils utilisateur, des événements ou des catalogues.

Pour les autres moyens de rendre des données disponibles dans Decisioning Studio, consultez [Connecter vos sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources).

## Prérequis {#prerequisites}

- Accès à Braze et à BrazeAI Decisioning Studio.
- Une source d'entrepôt de données active pour l'ingestion de données cloud. Si vous n'en avez pas encore configuré, consultez [Intégrations d'entrepôts de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- La table ou la vue que vous souhaitez synchroniser.
- Une ou plusieurs colonnes dans cette table à utiliser comme clé primaire, ainsi qu'une colonne d'horodatage que CDI peut utiliser pour la synchronisation incrémentale.

## Créer une synchronisation Decisioning Studio {#create-a-decisioning-studio-sync}

### Étape 1 : Créer la synchronisation et sélectionner la destination {#step-1-create-the-sync-and-select-the-destination}

1. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Syncs**.
2. Sélectionnez **Create data sync**.
3. Saisissez un **Integration Name**, puis sélectionnez votre source sous **Data sources**.
4. Sous **Destination**, définissez **Data destination** sur **BrazeAI Decisioning Studio™**.
5. Sous **Data category**, sélectionnez le type de **Decisioning Studio data** qui correspond le mieux à votre table. Choisissez parmi **Customer profile**, **Message engagement events**, **Conversion events** ou **Other**. Cela étiquette les données pour Decisioning Studio et ne modifie pas la façon dont CDI traite vos lignes.

### Étape 2 : Rédiger votre requête SQL {#step-2-write-your-sql-query}

À l'étape **Data definition**, rédigez une requête SQL qui renvoie les données de la table ou de la vue que vous souhaitez synchroniser. Le résultat de la requête devient le schéma de votre synchronisation.

Vous pouvez utiliser le Source Explorer pour parcourir les tables et vues disponibles, ou le générateur SQL par IA pour vous aider à rédiger votre requête.

Votre requête doit renvoyer une colonne `UPDATED_AT`, car CDI utilise `UPDATED_AT` pour la synchronisation incrémentale et le suivi des modifications. À chaque exécution de synchronisation, CDI ne synchronise que les lignes dont la valeur `UPDATED_AT` est postérieure à la dernière valeur synchronisée. Si la colonne d'horodatage que vous avez identifiée ne s'appelle pas déjà `UPDATED_AT`, vous pouvez lui attribuer un alias dans votre requête :

```sql
SELECT *, LAST_MODIFIED AS UPDATED_AT FROM my_table
```

Pour en savoir plus sur la façon dont `UPDATED_AT` contrôle la synchronisation incrémentale, y compris ce qui se passe lorsque vous la déplacez en arrière, consultez [Comprendre la colonne UPDATED_AT]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#understanding-the-updated_at-column).

{% alert note %}
Seules les requêtes en lecture seule à instruction unique sont prises en charge, y compris les clauses `JOIN`. CDI exécute des requêtes en lecture seule et ne modifie pas vos tables sous-jacentes.
{% endalert %}

### Étape 3 : Prévisualiser et valider votre requête {#step-3-preview-and-validate-your-query}

Sélectionnez **Preview and validate** pour exécuter votre requête. La section **Query preview (first 10 rows)** affiche les 10 premières lignes renvoyées par votre source, ainsi que le type de données détecté pour chaque colonne, afin que vous puissiez confirmer que les données sont correctes avant de continuer.

### Étape 4 : Sélectionner une clé primaire {#step-4-select-a-primary-key}

Chaque synchronisation Decisioning Studio nécessite une clé primaire ou composite, c'est-à-dire une ou plusieurs colonnes qui identifient de manière unique chaque ligne. Une fois la validation réussie, ouvrez le menu déroulant **Primary key** et sélectionnez une colonne comme clé primaire. La sélection de plusieurs colonnes forme une clé composite.

{% alert tip %}
Une bonne clé primaire est unique pour chaque ligne, jamais vide et stable d'une exécution de synchronisation à l'autre. Évitez les valeurs générées au moment de la requête, telles que `UUID()` ou `CURRENT_TIMESTAMP`, car elles peuvent provoquer des lignes en double ou manquantes.
{% endalert %}

### Étape 5 : Configurer les notifications, la planification et créer la synchronisation {#step-5-set-notifications-schedule-and-create-the-sync}

1. À l'étape **Notifications**, saisissez une ou plusieurs adresses **Contact Email(s)** pour recevoir les notifications d'erreurs de synchronisation. Vous pouvez également activer les notifications **Row Error** et **Sync success**.
2. À l'étape **Schedule**, activez **Recurring sync** pour exécuter la synchronisation automatiquement selon une planification. Lorsque **Recurring sync** est désactivé, la synchronisation ne s'exécute que lorsque vous la déclenchez, soit manuellement depuis le tableau de bord, soit via l'endpoint [Déclencher une synchronisation]({{site.baseurl}}/api/endpoints/cdi/post_job_sync).
3. Vérifiez le **Summary**, puis créez la synchronisation.

## Modifier une synchronisation {#editing-a-sync}

Lorsque vous modifiez une synchronisation existante, toute modification de votre requête SQL nécessite une revalidation avant de pouvoir enregistrer. Les clés primaires et composites ne peuvent pas être modifiées et doivent toujours être renvoyées.

Les modifications valides prennent effet lors de la prochaine exécution de synchronisation.

## Gestion des modifications de schéma {#handling-schema-changes}

CDI gère les modifications de schéma source de manière additive. À chaque exécution de synchronisation, CDI compare le schéma de votre source à la ressource Decisioning Studio existante et ajoute les nouvelles colonnes tout en préservant celles déjà présentes.

| Modification dans votre table source | Comportement de la synchronisation |
|---|---|
| Une nouvelle colonne est ajoutée | CDI ajoute la colonne à la ressource Decisioning Studio. Les lignes livrées avant l'existence de la colonne affichent `null` pour celle-ci. |
| Une colonne est supprimée | CDI cesse de mettre à jour cette colonne, mais la colonne et ses données existantes restent dans la ressource. Les autres colonnes continuent d'être synchronisées. |
| Une colonne est renommée | Traité comme une colonne supprimée plus une nouvelle colonne. La colonne d'origine reste dans la ressource et la nouvelle colonne est ajoutée. |
| Le type de données d'une colonne change | CDI convertit les valeurs lorsque c'est possible. Les lignes qu'il ne peut pas convertir sont signalées comme erreurs de ligne dans les détails d'exécution de la synchronisation. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestion des modifications de schéma" }

Lorsque CDI détecte une modification de schéma, celle-ci est affichée dans les détails d'exécution de la synchronisation et sur la page de modification de la synchronisation, et vos contacts de notification reçoivent une alerte par e-mail. Pour modifier les colonnes livrées, mettez à jour votre requête SQL et revalidez.