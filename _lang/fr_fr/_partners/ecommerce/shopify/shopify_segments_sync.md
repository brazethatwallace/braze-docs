---
nav_title: Synchronisation des segments Shopify
article_title: Synchronisation des segments Shopify
alias: /shopify_segments_sync/
page_order: 8
description: "Cet article de référence explique comment synchroniser les segments Shopify dans Braze en tant que cohortes pour une gestion et un ciblage d'audience unifiés."
---

# Synchronisation des segments Shopify {#shopify-segments-sync}

> La synchronisation des segments Shopify étend votre boutique Shopify dans Braze, offrant à votre équipe marketing un accès direct à des données utilisateur plus riches qui résident dans Shopify, y compris des signaux qui ne sont pas capturés par l'intégration standard Braze Shopify. En synchronisant les segments Shopify en tant que cohortes, vous alignez les définitions d'audience sur les deux plateformes et offrez des expériences utilisateur cohérentes et coordonnées, qu'un utilisateur soit ciblé dans Shopify ou engagé via une campagne Braze.

{% alert important %}
La synchronisation des segments Shopify est actuellement en version bêta. Pour demander l'accès, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Conditions préalables {#prerequisites}

| Exigence | Description |
| --- | --- |
| Intégration Braze Shopify | L'application Braze Shopify doit être installée sur votre boutique Shopify et connectée à un espace de travail Braze. Pour les instructions de configuration, consultez [Configuration de l'intégration standard Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) ou [Configuration de l'intégration personnalisée Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Comment ça fonctionne {#how-it-works}

La synchronisation des segments Shopify fonctionne en deux phases.

1. Lorsque vous synchronisez un segment pour la première fois, Braze effectue un remplissage rétroactif de tous les membres actuels et crée une cohorte correspondante dans Braze. Le remplissage rétroactif s'exécute de manière asynchrone et peut prendre quelques instants.
2. Lors de la synchronisation initiale, Braze effectue le remplissage rétroactif des membres actuels et s'abonne aux webhooks Shopify afin que l'appartenance reste synchronisée en quasi temps réel.

| Sujet du webhook | Effet dans Braze |
| --- | --- |
| `customer.joined_segment` | L'utilisateur est ajouté à la cohorte Braze correspondante. |
| `customer.left_segment` | L'utilisateur est retiré de la cohorte Braze correspondante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook topic" }

Si une synchronisation échoue, la fenêtre modale de l'extension d'action affiche une bannière d'erreur avec une action recommandée. Sélectionnez **Sync with Braze** pour réessayer.

## Intégration d'import de données {#data-import-integration}

### Étape 1 : Sélectionner un segment Shopify à synchroniser {#step-1-select-a-shopify-segment-to-sync}

Dans Shopify, accédez à **Customers** > **Segments**, puis sélectionnez le segment que vous souhaitez synchroniser avec Braze. Vous pouvez synchroniser n'importe quel segment créé à l'aide de la segmentation native de Shopify, y compris les segments basés sur l'historique des commandes, les achats de produits, les étiquettes client, les dépenses à vie et les métachamps.

![Panneau des segments avec la liste des segments Shopify.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Étape 2 : Lancer la synchronisation {#step-2-initiate-the-sync}

1. Sur la page de détail du segment dans Shopify, ouvrez le menu déroulant **Use segment** et sélectionnez **Braze Segment Sync**.

![Page de détail du segment avec un menu déroulant « Use segment » contenant une option « Braze Segment Sync ».]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Dans la fenêtre modale de l'extension d'action Braze qui s'ouvre, le nom du segment et la taille de l'audience sont affichés. Sélectionnez **Sync with Braze** pour lancer l'import.

![Fenêtre modale avec un bouton pour synchroniser avec Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. Sélectionnez **Done**.

![Fenêtre modale confirmant que la synchronisation est active.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Étape 3 : Créer un segment Braze avec le filtre Cohort Membership {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Dans Braze, accédez à **Audience** > **Segments**, puis créez un nouveau segment. Dans **Add Filter**, sélectionnez le filtre **Cohort Membership** et choisissez votre segment Shopify synchronisé dans le menu déroulant. Après l'enregistrement, vous pouvez référencer ce segment Braze lors du ciblage des utilisateurs dans une campagne ou un Canvas.

![Générateur de segments avec le filtre « Shopify Cohorts ».]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Correspondance des utilisateurs {#user-matching}

Les utilisateurs synchronisés à partir des segments Shopify sont associés aux profils utilisateur Braze à l'aide de l'alias `shopify_customer_id` défini dans le cadre de l'intégration Braze Shopify. Les utilisateurs sans profil utilisateur Braze correspondant sont ignorés lors de la synchronisation.

Pour plus de détails sur la façon dont l'intégration Shopify identifie et attribue des alias aux utilisateurs, consultez [Fonctionnalités de données Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

## Limitations

- **Synchronisation unidirectionnelle.** L'appartenance au segment circule uniquement de Shopify vers Braze. Les modifications apportées à l'appartenance à une cohorte directement dans Braze ne sont pas renvoyées vers Shopify.
- **Pas de création de profil.** Seuls les clients Shopify qui possèdent déjà un profil utilisateur Braze sont ajoutés à la cohorte.
- **Impossible d'annuler une synchronisation.** Lorsqu'un segment Shopify est synchronisé, l'opération ne peut pas être annulée.