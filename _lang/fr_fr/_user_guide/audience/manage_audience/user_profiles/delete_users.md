---
nav_title: Supprimer des utilisateurs
article_title: Supprimer des utilisateurs
page_order: 6
toc_headers: h2
description: "Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement via le tableau de bord de Braze."
alias: /delete_users/
---

# Supprimer des utilisateurs {#delete-users}

> Découvrez comment supprimer un utilisateur individuel ou un segment d'utilisateurs directement via le tableau de bord de Braze.

{% alert important %}
La suppression d'utilisateurs est actuellement en accès anticipé. Contactez votre gestionnaire de la satisfaction client si vous souhaitez participer.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour supprimer des utilisateurs, vous devez être administrateur ou disposer de l'autorisation **Delete Users**. Pour consulter les enregistrements de suppression d'utilisateurs, vous devez être administrateur ou disposer de l'autorisation **View User Deletion Records**. Les autorisations suivantes contrôlent la suppression d'utilisateurs et les enregistrements de suppression :

| Autorisation | Description |
|------------|-------------|
| Delete Users | Supprimer définitivement des utilisateurs individuellement ou en masse. |
| View User Deletion Records | Consulter les enregistrements de suppression d'utilisateurs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## À propos de la suppression d'utilisateurs {#about-user-deletion}

La suppression d'utilisateurs vous permet de gérer votre base de données en supprimant les profils qui ne sont plus nécessaires, qui ont été créés par erreur ou qui doivent être supprimés pour des raisons de conformité (comme le RGPD ou le CCPA).

| Considération | Détails |
|---------------|---------|
| Taille maximale | Vous pouvez supprimer jusqu'à 100 millions de profils utilisateurs lors de la suppression d'un segment. |
| Période d'attente | Toutes les suppressions de segments nécessitent une période d'attente de 7 jours plus le temps nécessaire au traitement des suppressions. |
| Limites de tâches | Un seul segment peut être supprimé à la fois, ce qui inclut la période d'attente de 7 jours. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="À propos de la suppression d'utilisateurs" }

## Supprimer des utilisateurs {#deleting-users}

Vous pouvez supprimer un [utilisateur individuel](#delete-individual) ou un [segment d'utilisateurs](#delete-segment) via le tableau de bord de Braze :

### Supprimer un utilisateur individuel {#delete-individual}

Pour supprimer un utilisateur individuel de Braze, accédez à **Audience** > **Search Users**, puis recherchez et sélectionnez un utilisateur. Si vous supprimez un profil utilisateur en double, vérifiez que vous avez sélectionné le bon.

![La page « Search Users » dans Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Les suppressions d'utilisateurs individuels sont permanentes : les profils ne peuvent pas être récupérés après leur suppression.
{% endalert %}

Sur la page de profil de l'utilisateur, sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Show options** > **Delete User**. La suppression complète de l'utilisateur dans Braze peut prendre quelques minutes.

![Un utilisateur dans Braze avec le menu à points de suspension verticaux ouvert, affichant l'option de suppression de l'utilisateur.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Supprimer un segment {#delete-segment}

Si ce n'est pas déjà fait, [créez un segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) contenant les profils utilisateurs que vous souhaitez supprimer. Assurez-vous d'inclure tous les profils utilisateurs si vous supprimez des utilisateurs en double.

Dans Braze, accédez à **Audience** > **Manage Audience**, puis sélectionnez l'onglet **Delete Users**.

![L'onglet « Delete Users » dans la section « Manage Audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Sélectionnez **Delete users**, choisissez le segment que vous souhaitez supprimer, puis sélectionnez **Next**.

![Une fenêtre contextuelle avec un segment choisi pour la suppression.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Tapez **DELETE** pour confirmer votre demande, puis sélectionnez **Delete users**.

![La page de confirmation avec « DELETE » saisi dans le champ de confirmation.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Les utilisateurs de ce segment ne seront pas supprimés immédiatement. Ils seront marqués comme en attente de suppression pendant les 7 prochains jours. Après cette période, ils seront supprimés et nous vous enverrons un e-mail pour vous en informer.

{% alert tip %}
Pour garantir que ces utilisateurs exacts soient supprimés indépendamment des modifications du segment, un filtre de segment appelé **Pending Deletion** est automatiquement créé. Vous pouvez [utiliser ce filtre]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters) pour vérifier l'état des suppressions en attente.
{% endalert %}

## Confirmer les suppressions de segments {#confirming-segment-deletions}

Braze envoie un e-mail de confirmation avec le nombre de profils en attente de suppression.

Pour poursuivre la suppression, connectez-vous à Braze et confirmez la demande de suppression.

Si vous ne confirmez pas dans le délai indiqué dans l'e-mail, la demande de suppression expire et n'est pas exécutée.

## Annuler les suppressions de segments {#cancel}

Vous disposez de 7 jours pour annuler les suppressions de segments en attente. Pour annuler, accédez à **Audience** > **Manage Audience**, puis sélectionnez l'onglet **Delete Users**.

![L'onglet « Delete Users » dans la section « Manage Audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

À côté d'une suppression de segment en attente, sélectionnez <i class="fa-solid fa-eye"></i> **View details** pour ouvrir les détails de l'enregistrement de suppression.

![Une suppression de segment en attente dans l'onglet « Delete Users ».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Dans les détails de l'enregistrement de suppression, sélectionnez **Cancel deletion**.

![La fenêtre « Deletion Record Details » dans l'onglet « Delete Users ».]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Lorsqu'une suppression en masse d'utilisateurs est en cours, vous pouvez l'annuler à tout moment. Cependant, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être restaurés.
{% endalert %}

## Vérifier l'état de la suppression {#status}

Vous pouvez vérifier l'état d'une suppression à l'aide des [filtres de segment](#segment-filters), de la page [Manage Audience](#manage-audience) ou des [rapports d'événements de sécurité](#security-event-report).

### Filtres de segment {#segment-filters}

Lorsque vous demandez la suppression d'un segment d'utilisateurs, un [filtre de segment]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters) appelé **Pending Deletion** est automatiquement créé. Vous pouvez l'utiliser pour :

- Voir l'ensemble exact d'utilisateurs liés à une date d'exécution de suppression spécifique.
- Exclure ces utilisateurs des campagnes afin qu'ils ne reçoivent pas de messages avant leur suppression.
- Exporter la liste si vous en avez besoin à des fins de conformité ou d'archivage.

### Manage Audience {#manage-audience}

{% alert note %}
Pour obtenir la liste des utilisateurs exacts qui seront supprimés, utilisez plutôt le [filtre de segment Pending Deletion](#segment-filters).
{% endalert %}

Accédez à **Audience** > **Manage Audience**, puis sélectionnez l'onglet **Delete Users**.

![L'onglet « Delete Users » dans la section « Manage Audience » du tableau de bord de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Sur cette page, vous trouverez les informations générales suivantes pour toutes les suppressions en cours et en attente :

| Champ | Description |
|-------|-------------|
| Date de la demande | La date à laquelle la demande a été initialement effectuée. Utilisez-la avec le filtre **Pending Deletion** pour obtenir la liste des profils en attente de suppression. |
| Demandeur | L'utilisateur qui a initié la demande de suppression. |
| Nom du segment | Le nom du segment utilisé pour sélectionner les utilisateurs en attente de suppression. |
| État | Indique si la demande de suppression est en attente, en cours ou terminée. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Manage Audience" }

Pour plus de détails sur une demande spécifique, sélectionnez <i class="fa-solid fa-eye"></i> **View details** pour afficher les détails de l'enregistrement de suppression. Vous pouvez également [annuler les suppressions de segments en attente](#cancel) depuis cet écran.

![Une suppression de segment en attente dans l'onglet « Delete Users ».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Rapport d'événements de sécurité {#security-event-report}

Vous pouvez également vérifier l'état des suppressions précédentes en téléchargeant un rapport d'événements de sécurité. Pour plus d'informations, consultez [Paramètres de sécurité]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report).

## Questions fréquentes {#faq}

### Puis-je supprimer des segments de plus de 100 millions d'utilisateurs ? {#can-i-delete-segments-with-more-than-100-million-users}

Non. Vous ne pouvez pas supprimer des segments de plus de 100 millions d'utilisateurs. Si vous avez besoin d'aide pour supprimer un segment de cette taille, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/).

### Il semble que je ne puisse pas supprimer 100 millions d'utilisateurs et que je sois limité à 10 millions. Est-ce un bug ? {#it-looks-like-i-am-not-able-to-delete-100-million-users-and-am-limited-to-deleting-only-10-million-is-this-a-bug}

Non, ce n'est pas un bug. Certains clients sont limités dans le nombre d'utilisateurs qu'ils peuvent supprimer pendant le programme d'accès anticipé (EA).

Au fur et à mesure de l'avancement du programme EA, cette capacité est conçue pour augmenter jusqu'à ce que tous les clients puissent supprimer jusqu'à 100 millions d'utilisateurs.

Si vous souhaitez augmenter cette capacité, contactez votre gestionnaire de compte Braze. Les demandes sont accordées à la discrétion de l'équipe produit.

### La fusion automatique d'utilisateurs affecte-t-elle la suppression d'utilisateurs ? {#does-automated-user-merging-affect-user-deletion}

Si une fusion planifiée inclut des profils utilisateurs en attente de suppression, Braze ignore ces profils et ne les fusionne pas. Pour fusionner ces profils, vous devez d'abord les retirer de la suppression.

### Qu'advient-il des données envoyées aux utilisateurs en attente de suppression ? {#what-happens-to-data-sent-to-users-pending-deletion}

Les données envoyées depuis des systèmes externes ou des SDK sont toujours acceptées, mais les utilisateurs seront supprimés comme prévu, indépendamment de l'activité.

### Les Canvas et les Campaigns se déclenchent-ils pour les utilisateurs en attente de suppression ? {#do-canvases-and-campaigns-trigger-for-users-pending-deletion}

Oui. Cependant, vous pouvez ajouter un filtre d'inclusion de segment pour exclure tous les utilisateurs avec le [filtre de segment](#segment-filters) **Pending Deletion**.

### Puis-je récupérer des profils utilisateurs supprimés ? {#can-i-recover-deleted-user-profiles}

La suppression d'utilisateurs individuels est permanente.

Vous pouvez [annuler les suppressions de segments](#cancel) dans les 7 premiers jours. Cependant, les utilisateurs déjà supprimés avant l'annulation ne peuvent pas être restaurés.

### Puis-je supprimer des utilisateurs via l'API au lieu du tableau de bord ? {#can-i-delete-users-with-the-api-instead-of-the-dashboard}

Oui. Pour des lots plus petits, vous pouvez utiliser l'[endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/), qui accepte jusqu'à 50 identifiants par requête et est soumis à la [limite de débit]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/#rate-limit) de cet endpoint. La suppression par segment via le tableau de bord est mieux adaptée aux très grandes audiences, mais inclut la [période d'attente de 7 jours](#about-user-deletion).