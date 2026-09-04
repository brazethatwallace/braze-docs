---
nav_title: Journaux de synchronisation et observabilité
article_title: Journaux de synchronisation et observabilité
page_order: 8
page_type: reference
description: "Cette page fournit un aperçu des fonctionnalités d'observabilité disponibles dans l'ingestion de données cloud."
---

# Journaux de synchronisation et observabilité {#sync-logs-and-observability}

> Le tableau de bord **Sync Log** de l'ingestion de données cloud (CDI) vous permet de surveiller toutes les données traitées par CDI, de vérifier si les données ont été synchronisées avec succès et de diagnostiquer tout problème lié à des données « incorrectes » ou manquantes.

Pour accéder aux journaux de synchronisation, rendez-vous dans **Paramètres des données** > **Ingestion de données cloud** et sélectionnez l'onglet **Sync Log**.

<!-- support-analyzer-phase2:cdi_updated_at_row_sync -->
{% alert note %}
Si le nombre de lignes de l'entrepôt de données ne correspond pas aux **Rows Synced** ou si vous voyez des exécutions en **Partial Success**, ouvrez le **Run ID** dans le Sync Log et examinez les valeurs **Error reason** au niveau des lignes. CDI sélectionne les lignes à l'aide de `UPDATED_AT` — les lignes dont les horodatages ont déjà été traités, dont la valeur `UPDATED_AT` n'a pas changé après modification, ou qui ont été écrites pendant une synchronisation active peuvent être ignorées. Pour les cas courants, consultez [Pourquoi « Rows Synced » ne correspond-il pas au nombre dans mon entrepôt de données ?]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs#why-doesnt-rows-synced-match-the-number-in-my-warehouse) et la [FAQ sur l'ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/faqs).
{% endalert %}

## Comprendre le tableau de bord du journal de synchronisation {#understanding-the-sync-log-dashboard}

La page principale du **journal de synchronisation** fournit un aperçu de haut niveau de toutes vos exécutions de synchronisation, y compris un résumé des synchronisations récentes selon leur statut actuel ou final.

* **Running :** Tâches de synchronisation actuellement en cours.
* **Success :** Tâches de synchronisation terminées dont toutes les lignes ont été traitées avec succès.
* **Partial Success :** Tâches de synchronisation terminées, mais dont une ou plusieurs lignes ont rencontré une erreur.
* **Error :** Tâches de synchronisation qui n'ont pas pu aboutir.
* **Limit Exceeded :** Tâches de synchronisation qui ont cessé le traitement car une limite de données a été dépassée.

![Un exemple de journaux de synchronisation avec 6 576 succès au total.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Les journaux de synchronisation fournissent également les détails suivants pour chaque synchronisation :

* **Sync name :** Le nom de la configuration de synchronisation.
* **Run ID :** Un identifiant unique pour une exécution spécifique de la synchronisation. Sélectionnez cet ID pour afficher plus de détails ou pour référencer une exécution de synchronisation auprès du support Braze.
* **Status :** Le statut de l'exécution (success, partial success, error, running).
* **New rows read from source :** Le nombre de nouvelles lignes extraites de votre entrepôt de données pour cette exécution.
* **Results :** Une ventilation du nombre de lignes ayant réussi ou échoué au cours de l'exécution.
* **Last "UPDATED_AT" :** L'horodatage de l'enregistrement le plus récent traité lors de cette exécution de synchronisation.
* **Run start time :** Le moment où la tâche de synchronisation a démarré.
* **Run duration :** La durée totale de la tâche de synchronisation.

### Conservation des données {#data-retention}

Les données du journal de synchronisation, y compris tous les payloads au niveau des lignes et les détails des erreurs, sont conservées pendant **30 jours** maximum. Les journaux de plus de 30 jours sont automatiquement purgés.

Les métadonnées d'exécution de synchronisation, telles que le nombre de lignes traitées, sont conservées pendant au moins 12 mois.

### Filtrer les journaux de synchronisation {#filtering-sync-logs}

Vous pouvez filtrer le tableau des journaux de synchronisation pour trouver des exécutions spécifiques. Les filtres disponibles incluent :

* **Job start date :** Sélectionnez une plage prédéfinie (comme « 30 derniers jours ») ou une plage de dates personnalisée.
* **Status :** Filtrez par un ou plusieurs statuts de synchronisation (par exemple, afficher uniquement les statuts **Error** et **Partial success**).
* **Sync name :** Recherchez une synchronisation spécifique par son nom.

Pour examiner une synchronisation spécifique, sélectionnez le **Run ID** correspondant dans le tableau des journaux de synchronisation. Sur la page **Run details**, vous trouverez un journal granulaire, ligne par ligne, de la synchronisation.

### Aperçu de l'exécution {#run-overview}

Cette section résume l'exécution sélectionnée, y compris son heure de début, son heure de fin, sa durée et le nombre total de lignes lues depuis la source. Elle fournit également un décompte du nombre de lignes ayant réussi et du nombre de lignes ayant généré une erreur.

### Lignes traitées lors de cette exécution {#rows-processed-in-this-run}

Ce tableau offre une visibilité au niveau des lignes sur les données traitées pendant la synchronisation, vous permettant de valider les enregistrements individuels.

* **Search :** Vous pouvez rechercher un utilisateur spécifique dans les résultats de l'exécution à l'aide de la barre **Search by user ID**.
* **Détails disponibles :**
  * **UPDATED_AT :** L'horodatage de la colonne `UPDATED_AT` pour cette ligne spécifique.
  * **ID :** Les identifiants utilisateur (tels que `external_id`, `email` ou `alias_name`) utilisés pour associer l'enregistrement à un profil utilisateur Braze.
  * **Status :** Le statut de traitement individuel pour cette ligne (**Success** ou **Error**).
  * **Source payload :** Un lien pour afficher le payload des données.
  * **Error reason :** Si le statut est **Error**, cette colonne fournit un message expliquant pourquoi la ligne n'a pas pu être synchronisée.

#### Afficher les payloads {#viewing-payloads}

Pour voir les données exactes envoyées à Braze pour une ligne spécifique, sélectionnez **View payload** dans la colonne **Source** payload. Cela affiche le payload JSON brut qui a été traité pour cet utilisateur.

#### Exporter les journaux de synchronisation {#exporting-sync-logs}

Sélectionnez **Export rows** pour exporter les journaux au niveau des lignes pour une exécution de synchronisation. Ensuite, choisissez d'exporter par :

* **Rows with errors :** Télécharge un fichier contenant uniquement les lignes ayant un statut **Error**.
* **All rows :** Télécharge un fichier contenant toutes les lignes traitées lors de l'exécution.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Les journaux ne peuvent pas être exportés directement depuis le tableau de bord. Une fois l'exportation générée, vous recevrez un e-mail contenant un lien pour télécharger le fichier d'exportation du journal.

## Notifications {#notifications}

Vous pouvez configurer des notifications par e-mail pour rester informé de l'état de vos synchronisations CDI. Ces paramètres sont configurés lors de la création d'une synchronisation et peuvent être mis à jour à tout moment.

### Notifications d'erreur {#error-notifications}

Au moins une adresse e-mail de contact est requise pour recevoir les notifications relatives aux erreurs au niveau de la synchronisation. Ces alertes sont envoyées lorsqu'une tâche de synchronisation complète échoue ou ne se termine pas, ou si la synchronisation rencontre une erreur nécessitant une intervention de l'utilisateur, comme des identifiants expirés ou une table source manquante.

Les notifications supplémentaires incluent :

- **Erreur de ligne :** Recevez des alertes lorsqu'un certain pourcentage de lignes échoue à se mettre à jour au cours d'une synchronisation.
- **Seuil d'échec (%) :** Spécifiez le pourcentage d'échecs de lignes devant déclencher une alerte. Par exemple, définir cette valeur à **1** enverrait une notification si 1 % ou plus des lignes d'une exécution de synchronisation aboutissent à une erreur.
- **Succès de la synchronisation :** Recevez une notification lorsqu'une synchronisation se termine avec succès.
- **Alerter même si aucune ligne ne change :** Recevez une notification même lorsqu'une exécution de synchronisation réussie ne traite aucune ligne nouvelle ou mise à jour.