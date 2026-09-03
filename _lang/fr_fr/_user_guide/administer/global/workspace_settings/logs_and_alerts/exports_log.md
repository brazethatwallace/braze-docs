---
nav_title: Journal des exportations
article_title: Journal des exportations
page_order: 2
page_type: reference
description: "Cette page présente le journal des exportations, qui vous permet de visualiser l'état des travaux d'exportation et d'annuler les exportations en cours."
---

# Journal des exportations {#exports-log}

> Utilisez la page **Journal des exportations** pour consulter l'état des travaux d'exportation et annuler les exportations en cours directement depuis la plateforme Braze. Le journal des exportations prend en charge les exportations de Segments et de [listes de suppression]({{site.baseurl}}/user_guide/audience/suppression_lists) initiées depuis le tableau de bord ou l'[API d'exportation d'utilisateurs]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment).

Vous pouvez accéder au journal des exportations en allant dans **Paramètres** > **Configuration et test** > **Journal des exportations**.

## Ce que le journal des exportations affiche {#what-the-exports-log-shows}

Le journal des exportations répertorie les tâches d'exportation pour l'espace de travail actuel. Chaque ligne représente une tentative d'exportation et inclut le nom du Segment ou de la liste de suppression, la source de l'exportation, le statut et les horodatages.

| Colonne | Description |
|---------|-------------|
| ID d'exportation | Identifiant unique de la tâche d'exportation. Sélectionnez cet ID pour ouvrir les détails de l'exportation ou partager le journal. |
| Nom du Segment | Nom du Segment ou de la liste de suppression exporté(e). |
| Type de Segment | Indique si l'exportation concerne un **Segment** ou une **liste de suppression**. |
| Source | Lieu de déclenchement de l'exportation : **Dashboard** (exportation CSV depuis l'interface) ou **API** (API d'exportation des utilisateurs). |
| Statut | État actuel de la tâche d'exportation. Voir [Statuts d'exportation](#export-statuses). |
| Démarré à | Date et heure de début de la tâche d'exportation. |
| Terminé à | Date et heure à laquelle la tâche d'exportation s'est terminée, a échoué ou a été annulée. Vide tant que la tâche est en cours. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Colonnes du journal des exportations" }

## Statuts d'exportation {#export-statuses}

| Statut | Description |
|--------|-------------|
| In Progress | La tâche d'exportation est en cours d'exécution. |
| Complete | L'exportation s'est terminée avec succès. |
| Failed | L'exportation ne s'est pas terminée. |
| Cancelled | L'exportation a été annulée avant la fin. |
| Cancelling | Une demande d'annulation est en cours. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuts d'exportation" }

Vous ne pouvez annuler que les exportations ayant le statut **In Progress**. Si une exportation n'est plus en cours d'exécution, l'action d'annulation n'est pas disponible.

## Détails de l'exportation {#export-details}

Sélectionnez un **Export ID** pour afficher des informations supplémentaires sur cette tâche, notamment :

| Champ | Description |
|-------|-------------|
| Destination | L'emplacement où les fichiers exportés sont livrés (par exemple, un chemin de stockage cloud le cas échéant). |
| Fields Exported | Les champs du profil utilisateur inclus dans l'exportation. |
| Self Hosted | Indique si l'exportation utilise une livraison hébergée par le client. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs des détails de l'exportation" }

Depuis la page de détails de l'exportation, vous pouvez annuler une exportation en cours ou partager un lien vers l'entrée du journal.

## Workflows d'exportation associés {#related-export-workflows}

| Type d'exportation | Comment démarrer | Documentation |
|-------------|--------------|---------------|
| Exportation CSV de Segment | **Audience** > **Segments** > sélectionnez un segment > **User Data** > **CSV Export** | [Exporter les données de segment au format CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv) |
| Exportation de liste de suppression | **Audience** > **Suppression Lists** | [Listes de suppression]({{site.baseurl}}/user_guide/audience/suppression_lists) |
| Exportation de segment par API | `POST /users/export/segment` | [POST : Exporter le profil utilisateur par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Workflows d'exportation associés" }

## Annuler une exportation en attente {#cancelling-a-pending-export}

Vous pouvez annuler les exportations en attente directement depuis la page **Journal des exportations** en sélectionnant le menu <i class="fas fa-ellipsis-vertical"></i> puis **Annuler l'exportation**, ou en sélectionnant l'**ID d'exportation** puis **Annuler l'exportation** sur la page de l'exportation.

## Partager un journal d'exportation spécifique {#sharing-a-specific-export-log}

Partagez un journal d'exportation en sélectionnant l'**Export ID**, puis en sélectionnant **Share Log**.