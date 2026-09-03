---
nav_title: Synchronisation des segments Shopify
article_title: Synchronisation des segments Shopify
alias: /shopify_segments_sync/
page_order: 8
description: "Cet article de référence explique comment synchroniser les segments Shopify dans Braze en tant que cohortes pour une gestion et un ciblage d'audience unifiés."
---

# Synchronisation des segments Shopify {#shopify-segments-sync}

> La synchronisation des segments Shopify étend votre boutique Shopify dans Braze, offrant à votre équipe marketing un accès direct à des données utilisateur plus riches qui résident dans Shopify, y compris des signaux qui ne sont pas capturés par l'intégration standard Braze Shopify. En synchronisant les segments Shopify en tant que cohortes, vous alignez les définitions d'audience sur les deux plateformes et offrez des expériences utilisateur cohérentes et coordonnées, que vous les cibliez dans Shopify ou que vous les contactiez via une Campaign Braze.

{% alert important %}
La synchronisation des segments Shopify est actuellement en version bêta. Pour demander l'accès, contactez votre gestionnaire du succès des clients.
{% endalert %}

## Prérequis {#prerequisites}

| Condition | Description |
| --- | --- |
| Intégration Braze Shopify | L'application Braze Shopify doit être installée sur votre boutique Shopify et connectée à un espace de travail Braze. Pour les instructions de configuration, consultez [Configuration de l'intégration standard Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou [Configuration de l'intégration personnalisée Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). |
| Permission utilisateur Shopify | L'utilisateur Shopify qui lance la synchronisation de Segment doit disposer de la permission **Export** pour exporter les données utilisateur. Pour plus d'informations sur les permissions Shopify, consultez la [documentation sur les permissions de boutique Shopify](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Comment ça fonctionne {#how-it-works}

La synchronisation des Segments Shopify fonctionne en deux phases.

1. **Remplissage initial :** Lorsque vous synchronisez un Segment pour la première fois, Braze effectue un remplissage de tous les membres actuels et crée une cohorte correspondante dans Braze. Le remplissage s'exécute de manière asynchrone et peut prendre quelques instants.
2. **Synchronisation continue :** Après le remplissage initial, Braze s'abonne également aux webhooks Shopify afin que l'appartenance reste synchronisée en quasi temps réel.

| Sujet du webhook | Effet dans Braze |
| --- | --- |
| `customer.joined_segment` | L'utilisateur est ajouté à la cohorte Braze correspondante. |
| `customer.left_segment` | L'utilisateur est retiré de la cohorte Braze correspondante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sujet du webhook" }

Si une synchronisation échoue, la fenêtre modale de l'extension d'action affiche une bannière d'erreur expliquant ce qui s'est passé et comment procéder. Certaines erreurs proposent une action **Réessayer la synchronisation**. D'autres nécessitent une intervention d'un administrateur ou une modification de la configuration.

## Intégration d'importation de données {#data-import-integration}

### Étape 1 : Sélectionner un segment Shopify à synchroniser {#step-1-select-a-shopify-segment-to-sync}

Dans Shopify, accédez à **Customers** > **Segments**, puis sélectionnez le segment que vous souhaitez synchroniser avec Braze. Vous pouvez synchroniser n'importe quel segment créé à l'aide de la segmentation native de Shopify, y compris les segments basés sur l'historique des commandes, les achats de produits, les tags clients, les dépenses cumulées et les métachamps.

![Panneau de segments avec la liste des segments Shopify.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Étape 2 : Lancer la synchronisation {#step-2-initiate-the-sync}

1. Sur la page de détail du segment dans Shopify, ouvrez le menu déroulant **Use segment** et sélectionnez **Braze Segment Sync**.

![Page de détail du segment avec un menu déroulant « Use segment » contenant une option « Braze Segment Sync ».]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. La fenêtre modale de l'extension d'action Braze s'ouvre, affichant le nom du segment et la taille de l'audience. Sélectionnez **Sync with Braze** pour lancer l'importation.

![Fenêtre modale avec un bouton pour synchroniser avec Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. La fenêtre modale passe à un état de synchronisation et affiche une bannière de progression pendant que Braze importe les membres.

![Fenêtre modale montrant la synchronisation en cours.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. Sélectionnez **Close**. La synchronisation continue en arrière-plan. Fermer la fenêtre modale ne l'arrête pas.

Pour vérifier si la synchronisation est terminée, fermez puis rouvrez la fenêtre modale. Lorsque la synchronisation est terminée, la fenêtre modale s'ouvre avec une bannière de succès.

![Fenêtre modale confirmant que la synchronisation est active.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Étape 3 : Créer un Segment Braze avec le filtre Cohort Membership {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Dans Braze, accédez à **Audience** > **Segments**, puis créez un nouveau segment. Dans **Add Filter**, sélectionnez le filtre **Cohort Membership** et choisissez votre segment Shopify synchronisé dans le menu déroulant. Après l'enregistrement, vous pouvez référencer ce Segment Braze lors du ciblage des utilisateurs dans une Campaign ou un Canvas.

![Générateur de segments avec le filtre « Shopify Cohorts ».]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Resynchronisation d'un segment {#re-syncing-a-segment}

Après la synchronisation d'un segment, vous pouvez actualiser l'appartenance à la cohorte à tout moment depuis la même extension d'action.

1. Dans Shopify, ouvrez le segment synchronisé et sélectionnez **Use segment** > **Braze Segment Sync**.
2. Dans la fenêtre modale, sélectionnez **Sync now**.
3. Dans la boîte de dialogue de confirmation, sélectionnez **Sync now** pour lancer la resynchronisation.

La resynchronisation est additive : les utilisateurs qui correspondent au Segment Shopify actuel sont ajoutés à la cohorte, mais les utilisateurs qui n'y correspondent plus restent dans la cohorte.

## Gestion des segments synchronisés dans Braze {#managing-synced-segments-in-braze}

Vous pouvez gérer chaque segment synchronisé depuis le tableau de bord de Braze. Accédez à **Intégrations partenaires** > **Partenaires technologiques**, sélectionnez votre intégration Shopify, puis ouvrez l'onglet **Gérer les utilisateurs**.

### Statut de synchronisation {#sync-status}

Chaque segment synchronisé dispose d'un statut de synchronisation.

| Statut | Description |
| --- | --- |
| **En cours de synchronisation** | Braze importe les membres du segment. |
| **En file d'attente** | Le segment attend un créneau de synchronisation disponible. |
| **Actif** | Le segment est synchronisé et les mises à jour d'appartenance se font en quasi temps réel. |
| **En pause** | Les mises à jour d'appartenance pour ce segment sont en pause. |
| **Erreur** | La dernière tentative de synchronisation a échoué. Sélectionnez **Réessayer la synchronisation** pour réessayer. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statuts de synchronisation" }

### Synchroniser des segments en masse {#syncing-segments-in-bulk}

Pour synchroniser des segments supplémentaires, modifiez l'intégration, accédez à l'étape **Gérer les utilisateurs**, puis sélectionnez **Modifier les segments** dans la section **Synchroniser les segments**. Dans la fenêtre modale de sélection :

- Sélectionnez autant de segments que souhaité. 25 segments sont synchronisés à la fois ; les autres sont automatiquement mis en file d'attente.
- Les segments déjà en cours de synchronisation sont verrouillés. Pour supprimer un segment, supprimez-le dans Shopify.

Enregistrez vos modifications pour lancer les synchronisations.

### Mettre en pause un segment individuel {#pausing-a-single-segment}

Pour mettre en pause la synchronisation d'un segment, sélectionnez **Mettre en pause la synchronisation** sur sa ligne dans le tableau des segments, puis confirmez. Lorsque la synchronisation d'un segment est en pause :

- La cohorte et ses membres restent dans Braze et peuvent toujours être ciblés. Les Campaigns et Canvas qui utilisent la cohorte continuent d'envoyer des messages aux membres actuels de la cohorte.
- Les mises à jour d'appartenance s'arrêtent.
- Renommer le segment dans Shopify met toujours à jour le nom d'affichage de la cohorte.
- Supprimer le segment dans Shopify met toujours fin au suivi.
- Les requêtes **Synchroniser maintenant** depuis l'extension d'action Shopify sont rejetées.

Pour reprendre, sélectionnez **Reprendre la synchronisation** sur la ligne. Braze reprend les mises à jour d'appartenance et exécute une synchronisation de rattrapage. Les utilisateurs qui ont quitté le segment Shopify pendant la pause restent dans la cohorte Braze.

### Mettre en pause la synchronisation de tous les segments {#pausing-all-segment-syncing}

Pour mettre en pause la synchronisation de tous les segments en même temps, modifiez l'intégration, sélectionnez **Mettre en pause la synchronisation** dans la section **Synchroniser les segments** de l'étape **Gérer les utilisateurs**, puis enregistrez vos paramètres. Pendant que la synchronisation de tous les segments est en pause :

- Le tableau des segments affiche uniquement les noms des segments, avec un statut **En pause** à côté de l'en-tête.
- Les actions au niveau des lignes sont indisponibles jusqu'à la reprise.
- Braze ne met pas à jour les noms des cohortes lors des renommages dans Shopify. Les noms des cohortes sont actualisés à la reprise.
- Les requêtes **Synchroniser maintenant** depuis l'extension d'action sont rejetées. L'extension continue d'afficher le dernier statut connu de chaque segment, et sélectionner **Synchroniser maintenant** ne déclenche pas de synchronisation.

Pour reprendre, sélectionnez **Reprendre la synchronisation** dans la même section et enregistrez. Braze resynchronise automatiquement tous les segments précédemment sélectionnés avec une synchronisation de rattrapage. Vous n'avez pas besoin de les resélectionner. Les segments que vous avez mis en pause individuellement restent en pause jusqu'à ce que vous les repreniez depuis leur ligne dans le tableau des segments.

## Mises à jour des Segments dans Shopify {#segment-updates-in-shopify}

### Renommer un Segment {#renaming-a-segment}

Lorsque vous renommez un Segment Shopify, Braze met automatiquement à jour le nom d'affichage de la cohorte correspondante. Aucune resynchronisation n'est nécessaire. Braze met également à jour le nom de la cohorte lorsque la synchronisation d'un Segment est individuellement mise en pause. Lorsque toute la synchronisation des Segments est en pause, Braze met à jour les noms de cohortes à la reprise.

### Modifier les critères d'un Segment {#changing-segment-criteria}

Braze ne met pas automatiquement à jour l'appartenance à la cohorte lorsque vous modifiez les critères d'un Segment Shopify. Pour inclure les utilisateurs qui correspondent nouvellement aux critères, resynchronisez le Segment depuis l'extension d'action. Les utilisateurs qui ne correspondent plus restent dans la cohorte, car la resynchronisation ne supprime pas les membres. Pour plus de détails, consultez [Resynchroniser un Segment](#re-syncing-a-segment).

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs synchronisés à partir des segments Shopify sont mis en correspondance avec les profils utilisateur Braze à l'aide de l'alias `shopify_customer_id` défini dans le cadre de l'intégration Braze Shopify. Les utilisateurs sans profil utilisateur Braze correspondant sont ignorés lors de la synchronisation.

Pour plus de détails sur la manière dont l'intégration Shopify identifie et attribue des alias aux utilisateurs, consultez [Fonctionnalités de données Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

Braze met en correspondance les utilisateurs synchronisés avec les profils utilisateur Braze existants, quelle que soit la manière dont ces profils ont été créés, y compris via le remplissage historique Shopify, votre propre plateforme de données (telle que Snowflake ou un autre entrepôt de données), ou des importations directes via l'API. Si votre cohorte est plus petite que votre segment Shopify, cela signifie que certains membres du segment n'ont pas encore de profil Braze correspondant. Pour améliorer la couverture de correspondance, renseignez les profils utilisateur Braze via la méthode de votre choix avant la synchronisation.

## Limitations

- **Synchronisation unidirectionnelle.** L'appartenance au segment circule uniquement de Shopify vers Braze. Les modifications apportées à l'appartenance à une cohorte directement dans Braze ne sont pas renvoyées vers Shopify.
- **Pas de création de profil.** Seuls les clients Shopify qui possèdent déjà un profil utilisateur Braze sont ajoutés à la cohorte.
- **Aucun moyen d'arrêter la synchronisation depuis Braze.** Pour arrêter la synchronisation d'un segment, supprimez-le dans Shopify. La cohorte et ses membres restent dans Braze et cessent d'être mis à jour.
- **La resynchronisation ajoute uniquement des membres.** Resynchroniser un segment ajoute les utilisateurs nouvellement correspondants à la cohorte, mais ne supprime pas les utilisateurs qui ne font plus partie du segment Shopify.