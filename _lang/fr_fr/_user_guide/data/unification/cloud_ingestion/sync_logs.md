---
nav_title: Journaux de synchronisation et observabilité
article_title: Journaux de synchronisation et observabilité
page_order: 8
page_type: reference
description: "Cette page fournit un aperçu des fonctionnalités d'observabilité disponibles dans l'Ingestion de données cloud."
---

# Journaux de synchronisation et observabilité {#sync-logs-and-observability}

> Le tableau de bord **Sync Log** de l'Ingestion de données cloud (CDI) vous permet de surveiller toutes les données traitées par CDI, de vérifier si les données ont été synchronisées avec succès et de diagnostiquer tout problème lié à des données « incorrectes » ou manquantes.

Pour accéder aux journaux de synchronisation, rendez-vous dans **Paramètres des données** > **Ingestion de données cloud** et sélectionnez l'onglet **Sync Log**.

## Comprendre le tableau de bord Sync Log {#understanding-the-sync-log-dashboard}

La page principale du **Sync Log** fournit un aperçu de haut niveau de toutes vos exécutions de synchronisation, y compris un résumé des synchronisations récentes par statut actuel ou final.

* **Running :** tâches de synchronisation actuellement en cours d'exécution.
* **Success :** tâches de synchronisation terminées dont toutes les lignes ont été traitées avec succès.
* **Partial Success :** tâches de synchronisation terminées, mais pour lesquelles une ou plusieurs lignes ont rencontré une erreur.
* **Error :** tâches de synchronisation qui n'ont pas pu aboutir.
* **Limit Exceeded :** tâches de synchronisation dont le traitement a été interrompu en raison du dépassement d'une limite de données.

![Exemple de journaux de synchronisation avec un total de 6 576 réussites.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Les journaux de synchronisation fournissent également les détails suivants pour chaque synchronisation :

* **Nom de la synchronisation :** le nom de la configuration de synchronisation.
* **ID d'exécution :** un identifiant unique pour une exécution spécifique de la synchronisation. Sélectionnez cet ID pour afficher plus de détails. Il peut également être utilisé dans les [endpoints de l'API CDI]({{site.baseurl}}/api/endpoints/cdi/) ou pour référencer une exécution de synchronisation auprès de l'assistance Braze.
* **État :** le statut de l'exécution (réussi, succès partiel, erreur, en cours).
* **Nouvelles lignes lues depuis la source :** le nombre de nouvelles lignes extraites de votre entrepôt de données pour cette exécution.
* **Résultats :** une ventilation du nombre de lignes ayant réussi ou échoué au cours de l'exécution.
* **Dernier `UPDATED_AT` :** l'horodatage de l'enregistrement le plus récent traité lors de cette exécution de synchronisation.
* **Heure de début de l'exécution :** le moment où la tâche de synchronisation a démarré.
* **Durée de l'exécution :** la durée totale nécessaire à l'achèvement de la tâche de synchronisation.

### Conservation des données {#data-retention}

Les données du journal de synchronisation, y compris tous les payloads au niveau des lignes et les détails des erreurs, sont conservées pendant une durée maximale de **30 jours**. Les journaux datant de plus de 30 jours sont automatiquement supprimés.

Les métadonnées d'exécution de synchronisation, telles que le nombre de lignes traitées, sont conservées pendant au moins 12 mois.

### Filtrage des journaux de synchronisation {#filtering-sync-logs}

Vous pouvez filtrer le tableau des journaux de synchronisation pour trouver des exécutions spécifiques. Les filtres disponibles sont les suivants :

* **Date de début de la tâche :** sélectionnez une plage prédéfinie (comme « 30 derniers jours ») ou une plage de dates personnalisée.
* **État :** filtrez par un ou plusieurs statuts de synchronisation (par exemple, affichez uniquement les statuts **Error** et **Partial Success**).
* **Nom de la synchronisation :** recherchez une synchronisation spécifique par son nom.

Pour examiner une synchronisation spécifique, sélectionnez l'**ID d'exécution** correspondant dans le tableau des journaux de synchronisation. Sur la page **Détails de l'exécution**, vous trouverez un journal détaillé, ligne par ligne, de la synchronisation.

### Aperçu de l'exécution {#run-overview}

Cette section résume l'exécution sélectionnée, y compris son heure de début, son heure de fin, sa durée et le nombre total de lignes lues depuis la source. Elle fournit également un décompte du nombre de lignes traitées avec succès et du nombre de lignes ayant généré une erreur.

### Lignes traitées lors de cette exécution {#rows-processed-in-this-run}

Ce tableau offre une visibilité au niveau des lignes sur les données traitées pendant la synchronisation, vous permettant de valider chaque enregistrement individuellement.

* **Recherche :** vous pouvez rechercher un utilisateur spécifique dans les résultats de l'exécution à l'aide de la barre **Search by user ID**.
* **Détails disponibles :**
  * **`UPDATED_AT` :** l'horodatage de la colonne `UPDATED_AT` pour cette ligne spécifique.
  * **ID :** les identifiants utilisateur (tels que `external_id`, `email` ou `alias_name`) utilisés pour associer l'enregistrement à un profil utilisateur Braze.
  * **État :** le statut de traitement individuel pour cette ligne (**Success** ou **Error**).
  * **Payload source :** un lien pour consulter le payload des données.
  * **Motif de l'erreur :** si le statut est **Error**, cette colonne affiche un message expliquant pourquoi la ligne n'a pas pu être synchronisée.

#### Affichage des payloads {#viewing-payloads}

Pour afficher les données exactes envoyées à Braze pour une ligne spécifique, sélectionnez **View payload** dans la colonne **Source** payload. Cela affiche le payload JSON brut qui a été traité pour cet utilisateur.

#### Exportation des journaux de synchronisation {#exporting-sync-logs}

Sélectionnez **Export rows** pour exporter les journaux au niveau des lignes pour une exécution de synchronisation. Choisissez ensuite d'exporter par :

* **Lignes contenant des erreurs :** télécharge un fichier contenant uniquement les lignes ayant un statut **Error**.
* **Toutes les lignes :** télécharge un fichier contenant toutes les lignes traitées lors de l'exécution.

{% multi_lang_include early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Les journaux ne peuvent pas être exportés directement depuis le tableau de bord. Une fois l'exportation générée, vous recevrez un e-mail contenant un lien pour télécharger le fichier d'exportation du journal.

## Notifications {#notifications}

Vous pouvez configurer des notifications par e-mail pour rester informé de l'état de vos synchronisations CDI. Ces paramètres sont configurés lors de la création d'une synchronisation et peuvent être mis à jour à tout moment.

### Notifications d'erreur {#error-notifications}

Au moins une adresse e-mail de contact est requise pour recevoir les notifications relatives aux erreurs au niveau de la synchronisation. Ces alertes sont envoyées lorsqu'une tâche de synchronisation échoue ou ne parvient pas à se terminer, ou si la synchronisation rencontre une erreur nécessitant une intervention de l'utilisateur, telle que des identifiants expirés ou une table source manquante.

Les notifications supplémentaires comprennent :

- **Erreur de ligne :** recevez des alertes lorsqu'un certain pourcentage de lignes ne parvient pas à se mettre à jour lors d'une synchronisation.
- **Seuil d'échec (%) :** indiquez le pourcentage d'échecs de lignes devant déclencher une alerte. Par exemple, en définissant cette valeur sur **1**, une notification sera envoyée si 1 % ou plus des lignes d'une exécution de synchronisation génèrent une erreur.
- **Synchronisation réussie :** recevez une notification lorsqu'une synchronisation se termine avec succès.
- **Alerte même si aucune ligne n'a changé :** recevez une notification même lorsqu'une synchronisation réussie ne traite aucune ligne nouvelle ou mise à jour.