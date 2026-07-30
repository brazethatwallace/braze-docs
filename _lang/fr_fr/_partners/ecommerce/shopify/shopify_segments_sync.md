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
| Permission utilisateur Shopify | L'utilisateur Shopify qui lance la synchronisation de Segments doit disposer de la permission **Export** pour exporter les données utilisateur. Pour plus d'informations sur les permissions Shopify, consultez la [documentation des permissions de boutique Shopify](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Fonctionnement {#how-it-works}

La synchronisation des segments Shopify fonctionne en deux phases.

1. **Remplissage initial :** Lorsque vous synchronisez un segment pour la première fois, Braze effectue un remplissage de tous les membres actuels et crée une cohorte correspondante dans Braze. Le remplissage s'exécute de manière asynchrone et peut prendre quelques instants.
2. **Synchronisation continue :** Après le remplissage initial, Braze s'abonne également aux webhooks Shopify afin que l'appartenance reste synchronisée en quasi temps réel.

| Sujet du webhook | Effet dans Braze |
| --- | --- |
| `customer.joined_segment` | L'utilisateur est ajouté à la cohorte Braze correspondante. |
| `customer.left_segment` | L'utilisateur est retiré de la cohorte Braze correspondante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sujet du webhook" }

Si une synchronisation échoue, la fenêtre modale de l'extension d'action affiche une bannière d'erreur expliquant ce qui s'est passé et comment procéder. Certaines erreurs proposent une action **Retry sync**. D'autres nécessitent une intervention de l'administrateur ou une modification de la configuration.

## Intégration d'importation de données {#data-import-integration}

### Étape 1 : Sélectionner un segment Shopify à synchroniser {#step-1-select-a-shopify-segment-to-sync}

Dans Shopify, accédez à **Customers** > **Segments**, et sélectionnez le segment que vous souhaitez synchroniser avec Braze. Vous pouvez synchroniser n'importe quel segment créé à l'aide de la segmentation native de Shopify, y compris les segments basés sur l'historique des commandes, les achats de produits, les tags clients, les dépenses totales et les métachamps.

![Panneau des segments avec la liste des segments Shopify.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Étape 2 : Lancer la synchronisation {#step-2-initiate-the-sync}

1. Sur la page de détail du segment dans Shopify, ouvrez le menu déroulant **Use segment** et sélectionnez **Braze Segment Sync**.

![Page de détail du segment avec un menu déroulant « Use segment » contenant une option « Braze Segment Sync ».]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. La fenêtre modale de l'extension d'action Braze s'ouvre, affichant le nom du segment et la taille de l'audience. Sélectionnez **Sync with Braze** pour lancer l'importation.

![Fenêtre modale avec un bouton pour synchroniser avec Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. La fenêtre modale passe à un état de synchronisation et affiche une bannière de progression pendant que Braze importe les membres.

![Fenêtre modale indiquant que la synchronisation est en cours.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. Sélectionnez **Close**. La synchronisation se poursuit en arrière-plan. Fermer la fenêtre modale ne l'interrompt pas.

Pour vérifier si la synchronisation est terminée, fermez et rouvrez la fenêtre modale. Lorsque la synchronisation est terminée, la fenêtre modale s'ouvre avec une bannière de succès.

![Fenêtre modale confirmant que la synchronisation est active.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Étape 3 : Créer un Segment Braze avec le filtre d'appartenance à une cohorte {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Dans Braze, accédez à **Audience** > **Segments**, et créez un nouveau segment. Dans **Add Filter**, sélectionnez le filtre **Cohort Membership** et choisissez votre segment Shopify synchronisé dans le menu déroulant. Après l'enregistrement, vous pouvez référencer ce Segment Braze lors du ciblage des utilisateurs dans une Campaign ou un Canvas.

![Générateur de segments avec le filtre « Shopify Cohorts ».]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Resynchronisation d'un Segment {#re-syncing-a-segment}

Après la synchronisation d'un Segment, vous pouvez actualiser l'appartenance à la cohorte à tout moment depuis la même extension d'action.

1. Dans Shopify, ouvrez le Segment synchronisé et sélectionnez **Use segment** > **Braze Segment Sync**.
2. Dans la boîte de dialogue modale, sélectionnez **Sync now**.
3. Dans la boîte de dialogue de confirmation, sélectionnez **Sync now** pour lancer la resynchronisation.

La resynchronisation est additive : les utilisateurs qui correspondent au Segment Shopify actuel sont ajoutés à la cohorte, mais les utilisateurs qui ne correspondent plus restent dans la cohorte.

## Mises à jour des Segments dans Shopify {#segment-updates-in-shopify}

### Renommer un Segment {#renaming-a-segment}

Lorsque vous renommez un Segment Shopify, Braze met automatiquement à jour le nom d'affichage de la cohorte correspondante. Aucune resynchronisation n'est nécessaire.

### Modifier les critères d'un Segment {#changing-segment-criteria}

Les modifications apportées aux critères d'un Segment Shopify ne se propagent pas automatiquement. Pour récupérer les utilisateurs qui correspondent nouvellement aux critères, resynchronisez le Segment depuis l'extension d'action. Les utilisateurs qui ne correspondent plus restent dans la cohorte, car la resynchronisation ne supprime pas les membres. Pour plus de détails, consultez [Resynchroniser un Segment](#re-syncing-a-segment).

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs synchronisés à partir des segments Shopify sont associés aux profils utilisateur Braze à l'aide de l'alias `shopify_customer_id` défini dans le cadre de l'intégration Braze Shopify. Les utilisateurs sans profil utilisateur Braze correspondant sont ignorés lors de la synchronisation.

Pour plus de détails sur la façon dont l'intégration Shopify identifie et crée des alias pour les utilisateurs, consultez [Fonctionnalités de données Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

Braze associe les utilisateurs synchronisés aux profils utilisateur Braze existants, quelle que soit la manière dont ces profils ont été créés, y compris via le remplissage historique Shopify, votre propre plateforme de données (comme Snowflake ou un autre entrepôt de données), ou des importations directes par API. Si votre cohorte est plus petite que votre segment Shopify, cela signifie que certains membres du segment n'ont pas encore de profil Braze correspondant. Pour améliorer la couverture de correspondance, alimentez les profils utilisateur Braze via la méthode de votre choix avant la synchronisation.

## Limitations

- **Synchronisation unidirectionnelle.** L'appartenance au segment circule uniquement de Shopify vers Braze. Les modifications apportées à l'appartenance à une cohorte directement dans Braze ne sont pas renvoyées vers Shopify.
- **Pas de création de profil.** Seuls les clients Shopify qui possèdent déjà un profil utilisateur Braze sont ajoutés à la cohorte.
- **Impossible d'annuler une synchronisation.** Lorsqu'un segment Shopify est synchronisé, l'opération ne peut pas être annulée.
- **La resynchronisation ajoute uniquement des membres.** Resynchroniser un segment ajoute les utilisateurs nouvellement correspondants à la cohorte, mais ne supprime pas les utilisateurs qui ne font plus partie du segment Shopify.