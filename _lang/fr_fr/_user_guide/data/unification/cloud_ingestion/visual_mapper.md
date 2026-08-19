---
nav_title: Mappeur visuel
article_title: "Ingestion de données cloud : Mappeur visuel"
description: "Découvrez comment synchroniser une table ou une vue depuis votre entrepôt de données grâce au mappeur visuel de l'ingestion de données cloud, sans écrire de SQL."
page_order: 12
page_type: reference
toc_headers: h2
---

# Ingestion de données cloud : Mappeur visuel {#cloud-data-ingestion-visual-mapper}

> Cette page explique comment utiliser le mappeur visuel pour synchroniser une table ou une vue depuis votre entrepôt de données vers Braze, sans écrire de SQL ni restructurer vos données.

{% alert important %}
Le mappeur visuel est actuellement en version bêta. Il est disponible pour les synchronisations d'attributs utilisateur depuis toutes les sources d'entrepôt de données de l'ingestion de données cloud, et des types de synchronisation supplémentaires seront disponibles tout au long de la bêta. Contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour y accéder.
{% endalert %}

Avec le mappeur visuel, vous pouvez synchroniser une table ou une vue existante depuis votre entrepôt de données sans écrire de SQL ni restructurer vos données. Au lieu de créer une table spécifique à Braze avec les colonnes `EXTERNAL_ID`, `UPDATED_AT` et `payload`, vous mappez les colonnes de votre table existante aux champs Braze directement dans le tableau de bord.

## Prérequis {#prerequisites}

Avant de créer une synchronisation avec le mappeur visuel, vous aurez besoin de :

- Une source d'entrepôt de données d'ingestion de données cloud active. Si vous n'en avez pas encore configuré, consultez [Intégrations d'entrepôt de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- Le nom de la table ou de la vue que vous souhaitez synchroniser, tel qu'il apparaît dans votre entrepôt de données.
- Une colonne dans votre table contenant un identifiant utilisateur pris en charge, et une colonne avec un horodatage que Braze peut utiliser pour la synchronisation incrémentale.

{% alert note %}
Braze exécute uniquement des requêtes en lecture seule sur vos données et ne modifie pas vos tables sous-jacentes. Des objets temporaires peuvent être créés pendant l'exécution des requêtes, mais ils ne sont pas conservés.
{% endalert %}

## Créer une synchronisation avec le mappeur visuel {#creating-a-sync-with-the-visual-mapper}

### Étape 1 : Configurer la synchronisation {#step-1-configure-the-sync}

1. Accédez à **Data Settings** > **Cloud Data Ingestion** > **Syncs**, puis sélectionnez **Create data sync**.
2. Choisissez un nom pour votre synchronisation et sélectionnez une source de données active. Seules les sources actives peuvent être utilisées.
3. Pour **Data destination**, sélectionnez **Braze Data Platform**.
4. Pour **Data Type**, sélectionnez **User Attributes**.
5. Sélectionnez **Next: Data definition**.

### Étape 2 : Mapper votre schéma source {#step-2-map-your-source-schema}

1. À l'étape **Data definition**, sélectionnez **Visual mapper**.
2. Dans le champ **Table**, saisissez le nom de la table ou de la vue tel qu'il apparaît dans votre entrepôt de données.
3. Sélectionnez **Map source schema**. Braze lit le schéma de votre table ou vue et liste chaque colonne avec son type de donnée détecté.

### Étape 3 : Vérifier vos mappages {#step-3-review-your-mappings}

La section **Review mapping** suit deux mappages obligatoires. Votre synchronisation ne peut pas être créée tant que les deux ne sont pas terminés :

- Mappez une colonne à un identifiant utilisateur pris en charge : `external_id`, `braze_id`, `email`, `phone` ou un alias d'utilisateur. Les options d'identifiant apparaissent sous **Identifiers** dans le menu déroulant du champ de destination.
- Mappez une colonne à `updated_at`. Braze utilise cet horodatage pour la synchronisation incrémentale lors des synchronisations récurrentes, où chaque exécution importe les lignes dont la valeur `updated_at` est postérieure à la dernière valeur synchronisée.

Pour chaque colonne restante, vous pouvez :

- **Conserver le mappage par défaut.** Chaque colonne est mappée à un champ Braze du même nom. Si le champ n'existe pas encore dans votre espace de travail, il est marqué **New attribute** et sera créé lors de la première exécution de la synchronisation.
- **Mapper à un champ existant.** Recherchez dans le menu déroulant du champ de destination pour mapper une colonne à un attribut par défaut ou personnalisé existant dans votre espace de travail.
- **Mapper à un nouveau champ.** Saisissez directement dans le menu déroulant du champ de destination pour mapper une colonne à un nouvel attribut personnalisé.
- **Exclure la colonne.** Décochez la case **Import** pour exclure une colonne de la synchronisation.

{% alert tip %}
Avant de créer un nouvel attribut, recherchez un attribut existant dans le menu déroulant de destination. Par exemple, si votre table contient une colonne `fav_color` mais que votre espace de travail suit déjà `favorite_color`, envisagez de mapper `fav_color` à `favorite_color` au lieu de créer un autre attribut.
{% endalert %}

{% alert note %}
Les champs dont le type de donnée ne correspond pas au type détecté de votre colonne affichent un avertissement **Type mismatch**. Vous pouvez tout de même continuer, mais les valeurs incompatibles risquent de ne pas se synchroniser et seront signalées comme erreurs de ligne. Vous pouvez consulter les erreurs de ligne dans les détails d'exécution d'une synchronisation.
{% endalert %}

### Étape 4 : Prévisualiser et valider {#step-4-preview-and-validate}

Sélectionnez **Preview and validate** pour exécuter une vérification en lecture seule sur votre table ou vue. L'aperçu affiche les 10 premières lignes en utilisant les noms de champs mappés, et inclut uniquement les colonnes que vous importez.

### Étape 5 : Finaliser la création de la synchronisation {#step-5-finish-creating-the-sync}

1. À l'étape **Notifications**, saisissez au moins une adresse e-mail de contact pour les notifications d'erreur de synchronisation. Vous pouvez éventuellement activer les alertes **Row Error** (envoyées lorsqu'un pourcentage de lignes échoue à se mettre à jour) et les notifications **Sync success**.
2. À l'étape **Schedule**, activez **Recurring sync** pour exécuter la synchronisation selon une planification, ou laissez l'option désactivée pour une synchronisation unique.
3. Vérifiez l'étape **Summary**. Elle liste votre configuration, les attributs nouveaux par rapport aux existants, et les colonnes exclues de l'import en raison de problèmes de type de donnée ou de vos sélections.
4. Sélectionnez **Create sync**. Vous pouvez également sélectionner **Save as draft** à n'importe quelle étape pour terminer plus tard.

## Gestion des changements de schéma {#handling-schema-changes}

Le mappeur visuel vérifie le schéma de votre table ou vue à chaque exécution de synchronisation et réagit en fonction du type de changement :

| Changement dans votre table source | Comportement de la synchronisation |
|---|---|
| Une nouvelle colonne est ajoutée | La synchronisation continue, mais les nouvelles colonnes ne sont pas synchronisées automatiquement. Pour en inclure une, modifiez la synchronisation et mappez-la. |
| Une colonne mappée est supprimée | L'exécution de la synchronisation échoue et la synchronisation est mise en pause. Le changement de schéma est affiché dans les détails d'exécution de la synchronisation, et vos contacts de notification reçoivent une alerte par e-mail. |
| Une colonne mappée est renommée | Traité comme une colonne supprimée plus une nouvelle colonne. |
| Le type de donnée d'une colonne change | Non détecté comme un changement de schéma. Les valeurs incompatibles sont signalées comme erreurs de ligne dans les journaux de synchronisation. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestion des changements de schéma" }

Pour reprendre une synchronisation mise en pause après la suppression d'une colonne, sélectionnez **Edit sync** et vérifiez vos mappages. La colonne supprimée est signalée et n'apparaît plus dans le mappeur. Enregistrer vos mappages confirme que la synchronisation doit continuer sans cette colonne. Si les données ont été déplacées vers une autre colonne, mappez la nouvelle colonne avant d'enregistrer.

## Questions fréquentes {#frequently-asked-questions}

### Puis-je modifier mes mappages après la création d'une synchronisation ? {#can-i-edit-my-mappings-after-a-sync-is-created}

Oui. Modifiez la synchronisation et sélectionnez **View and edit mapping**. Le schéma actuel de la table source se charge, avec vos mappages précédents enregistrés lors de la création de la synchronisation. Vous pouvez modifier vos mappages à partir de là.

### Puis-je transformer mes données dans le mappeur visuel ? {#can-i-transform-my-data-in-the-visual-mapper}

Non. Le mappeur visuel synchronise les valeurs des colonnes exactement telles qu'elles apparaissent dans votre source. Il ne prend pas en charge les transformations, la logique conditionnelle ni les jointures entre tables. Pour ces cas d'usage, utilisez l'option SQL à l'étape Data definition pour façonner vos données avec une requête. Pour en savoir plus, consultez [Ingestion de données cloud : Éditeur SQL]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor).

### Mes synchronisations CDI existantes sont-elles modifiées ? {#do-my-existing-cdi-syncs-change}

Non. Les synchronisations utilisant le format de table existant avec les colonnes `EXTERNAL_ID`, `UPDATED_AT` et `payload` continuent de fonctionner, et vous pouvez toujours les créer en sélectionnant **Table** à l'étape **Data definition**. Aucune migration n'est nécessaire.

### Comment mon utilisation de Braze est-elle affectée ? {#how-is-my-braze-usage-affected}

Chaque colonne que vous importez est écrite comme une mise à jour d'attribut, et la facturation des points de donnée fonctionne de la même manière que pour les autres synchronisations de données utilisateur CDI. Exclure les colonnes dont vous n'avez pas besoin permet de garder vos synchronisations efficaces. Pour en savoir plus, consultez [Bonnes pratiques pour l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).