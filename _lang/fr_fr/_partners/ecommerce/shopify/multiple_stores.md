---
nav_title: Connecter plusieurs boutiques
article_title: Prise en charge de plusieurs boutiques Shopify
alias: /shopify_connecting_multiple_stores/
page_order: 6
description: "Cet article de référence explique comment connecter et configurer plusieurs boutiques Shopify à un seul espace de travail."
---

# Connecter plusieurs boutiques Shopify {#connect-multiple-shopify-stores}

> Connectez plusieurs domaines de boutiques Shopify à un espace de travail unique pour avoir une vue globale de vos clients sur tous les marchés. Créez et lancez des programmes d'automatisation et des parcours dans un espace de travail unique sans dupliquer les efforts dans les boutiques régionales.

{% alert important %}
Cette fonctionnalité ne prend pas en charge Shopify Markets ou Markets Pro. {% multi_lang_include product_feedback_cta.md context="gap" feature="Shopify Markets or Markets Pro support" %}
{% endalert %}

## Conditions requises {#requirements}

| Condition | Description |
| ----------- | ----------- |
| Configurer une boutique Shopify | Assurez-vous d'avoir déjà [configuré au moins une boutique Shopify avec Braze]({{site.baseurl}}/shopify_overview). |
| Domaines de vitrine Shopify uniques pour chaque région | La prise en charge de plusieurs boutiques est destinée à être utilisée avec des domaines de boutique Shopify uniques pour différentes vitrines régionales. <br><br>Si vous souhaitez connecter plusieurs sous-marques à Braze, nous vous recommandons de créer des espaces de travail distincts pour chaque sous-marque. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions requises" }

## Connexion d'une boutique supplémentaire {#connecting-an-additional-store}
Après avoir installé l'application Braze sur votre boutique Shopify et installé votre première boutique, sélectionnez **+ Connect New Store**.

![Le bouton « + Connect New Store » sur la page d'intégration de Shopify.]({% image_buster /assets/img/shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Pour votre boutique régionale Shopify supplémentaire, sélectionnez **Begin setup**.

![La section « Integration settings » avec un bouton « Begin setup ».]({% image_buster /assets/img/shopify/multiple_stores.png %}){: style="max-width:80%;"}

Comme pour votre première intégration de boutique Shopify, vous pouvez choisir entre une configuration standard ou personnalisée.

![La section « Enable the Braze SDKs » avec des options pour implémenter le SDK Web de Braze avec la configuration standard ou personnalisée.]({% image_buster /assets/img/shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Choisissez l'option qui correspond le mieux à vos besoins :

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

Pour afficher l'intégration de chaque boutique et configurer les paramètres avancés, sélectionnez une boutique dans le menu déroulant.

![« Integration settings » avec un menu déroulant pour sélectionner une boutique Shopify.]({% image_buster /assets/img/shopify/store_dropdown_menu.png %})

## Synchronisation des utilisateurs entre les boutiques {#syncing-users-across-stores}

### Alias Shopify {#shopify-alias}

Lorsque vous connectez plusieurs boutiques, les utilisateurs Shopify synchronisés qui se sont connectés ou ont passé une commande recevront un nouvel alias au format : {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### ID externe Braze {#braze-external-id}

Vous pouvez choisir parmi les options suivantes pour votre ID externe Braze :

| Option | Description |
|------|-----------|
| ID client Shopify | Si vous utilisez l'ID client de Shopify comme ID externe de Braze, chaque boutique générera un ID client unique pour chaque utilisateur. Cela signifie que si un utilisateur interagit avec plusieurs boutiques, il aura des profils distincts dans Braze. |
| E-mail, e-mail haché ou ID externe personnalisé | Si vous utilisez les types e-mail, e-mail haché ou ID externe personnalisé, les utilisateurs qui interagissent avec plusieurs boutiques verront leurs profils fusionnés en un seul profil consolidé lorsqu'ils se connecteront ou passeront une commande. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ID externe Braze" }

### Champs fusionnés {#merged-fields}

Lorsqu'un profil utilisateur est synchronisé, les champs suivants sont fusionnés. Pour plus de détails sur le comportement de fusion, reportez-vous à la section [Comportement de fusion]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

- Informations sur l'appareil
- Nombre total de sessions (combiné des deux profils)
- Données d'événements personnalisés et d'achats
- Propriétés d'événement personnalisées pour la segmentation (par exemple, « X fois en Y jours » où X ≤ 50 et Y ≤ 30)
- Nombre d'événements (combiné des deux profils)
- Dates du premier et du dernier événement (Braze sélectionne les dates les plus anciennes et les plus récentes)
- Données d'interaction de Campaign (champs de date les plus récents)
- Résumés des flux de travail (champs de date les plus récents)
- Historique des messages et de l'engagement
- Groupes d'abonnement

### Recueillir les abonnés (facultatif) {#collecting-subscribers-optional}

Vous pouvez choisir de collecter les abonnés directement via Braze (dans les paramètres de votre connecteur Shopify) ou via des alternatives API et SDK qui synchronisent les données depuis Shopify.

{% tabs local %}
{% tab Connecteur Shopify %}
Dans l'étape **Gérer les utilisateurs** des paramètres de votre connecteur Shopify, vous pouvez utiliser Braze pour collecter les abonnements par e-mail et SMS et les organiser dans un groupe d'abonnement dédié :

1. Créez un groupe d'abonnement unique pour chaque boutique que vous connectez. Cela vous permet de conserver des données précises sur la provenance des abonnés.
2. Activez la collecte d'abonnés par e-mail et par SMS.
{% endtab %}

{% tab API ou SDK de Braze %}
Vous pouvez également synchroniser les informations d'abonnement au marketing par e-mail et par SMS directement depuis Shopify à l'aide de l'API ou des SDK de Braze.

| Option | Ressources |
|------|---------|
| API | - Les [endpoints des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) pour remplacer directement ce qui est pris en charge par l'intégration<br>- L'[endpoint `Users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#set-subscription-groups) pour définir les données du groupe d'abonnement ou l'[état d'abonnement global à l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-states)<br>- Le [centre de préférences de Braze]({{site.baseurl}}/user_guide/channels/email/subscriptions) pour des options de collecte d'abonnement marketing plus personnalisées |
| SDK | - [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recueillir les abonnés (facultatif)" }
{% endtab %}
{% endtabs %}

## Données Shopify {#shopify-data}

### Attributs synchronisés {#synced-attributes}

Lorsque vous connectez plus d'une boutique, les attributs suivants sont synchronisés avec l'état le plus récent du profil Shopify :
- Prénom
- Nom
- E-mail
- Genre
- Date de naissance
- Pays
- Ville
- Dernière application utilisée
- Langue
- Fuseau horaire
- Étiquettes Shopify
- Nombre de commandes Shopify
- Total dépensé Shopify

### Événements pris en charge {#supported-events}

#### Événements recommandés pour le commerce électronique {#ecommerce-recommended-events}

Lorsque vous connectez plusieurs boutiques, les événements recommandés eCommerce entrants incluent une propriété d'événement source. Cette propriété identifie l'URL de la vitrine d'où provient l'événement, ce qui vous permet d'utiliser cette information pour la segmentation ou le déclenchement de cas d'usage spécifiques.

![Un Canvas basé sur une action avec un déclencheur pour faire entrer les utilisateurs qui effectuent l'événement personnalisé `ecommerce.order_placed`.]({% image_buster /assets/img/shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Les événements recommandés eCommerce pris en charge dans le cadre de l'intégration Shopify sont les suivants :

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Événements personnalisés Shopify {#shopify-custom-events}

Les événements personnalisés Shopify entrants comprennent une propriété d'événement appelée `shopify_storefront`. Cette propriété indique l'URL de la vitrine d'où provient l'événement, ce qui vous permet de l'exploiter pour la segmentation ou le déclenchement de cas d'usage.

![Un Canvas basé sur une action avec un déclencheur pour faire entrer les utilisateurs qui effectuent l'événement personnalisé `shopify_paid_order`.]({% image_buster /assets/img/shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Les événements personnalisés Shopify pris en charge sont les suivants :

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Pour un aperçu complet de tous les payloads d'événements, reportez-vous aux [fonctionnalités des données Shopify]({{site.baseurl}}/shopify_data_features).

### Synchronisation des produits Shopify {#shopify-product-sync}

Lorsque vous connectez et configurez chaque boutique Shopify dans Braze, vous pouvez éventuellement activer la synchronisation des produits Shopify dans le cadre de l'intégration.

Si vous activez la synchronisation des produits pour chaque boutique, Braze inclut le nom de votre boutique Shopify dans le nom du catalogue. Cela permet de distinguer les produits des différentes boutiques.

![Catalogues Shopify avec le nom de leur boutique Shopify dans leur nom.]({% image_buster /assets/img/shopify/catalog_store_name.png %})