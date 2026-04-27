---
nav_title: Synchronisation des produits Shopify
article_title: Synchronisation des produits Shopify
alias: /shopify_catalogs/
page_order: 5
description: "Cet article de référence explique comment importer vos produits Shopify dans les catalogues Braze."
---

# Synchronisation des produits Shopify {#shopify-product-sync}

> Vous pouvez synchroniser tous les produits de votre boutique Shopify avec un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/) Braze pour une personnalisation plus poussée des messages.

Les catalogues Shopify se mettent à jour en quasi-temps réel à mesure que vous apportez des modifications aux produits de votre boutique Shopify. Vous pouvez enrichir votre panier abandonné, votre confirmation de commande et bien plus encore avec les détails et informations produit les plus à jour.

{% alert warning %}
Braze synchronise jusqu'à 250 variantes de chaque produit Shopify dans votre catalogue. Les variantes au-delà de cette limite ne sont pas synchronisées. Si vous avez besoin de plus de 250 variantes par produit, contactez votre gestionnaire de la satisfaction client Braze.
{% endalert %}

## Configuration de la synchronisation des produits Shopify {#setting-up}

Si vous avez déjà installé votre boutique Shopify, vous pouvez toujours synchroniser vos produits en suivant les instructions ci-dessous.

### Étape 1 : Activer la synchronisation {#step-1-turn-on-the-sync}

Vous pouvez synchroniser vos produits avec un catalogue Braze via le flux d'installation Shopify ou sur la page partenaire Shopify.

![Étape 3 du processus de configuration avec « Shopify Variant ID » comme « identifiant de produit du catalogue ».]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Les produits synchronisés avec un catalogue Braze contribueront à votre [limite de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers).

### Étape 2 : Sélectionner votre identifiant de produit {#step-2-select-your-product-identifier}

Sélectionnez l'identifiant de produit à utiliser comme ID de catalogue :
- Shopify Variant ID
- SKU

Les valeurs d'ID et d'en-tête pour l'identifiant de produit que vous choisissez ne peuvent inclure que des lettres, des chiffres, des tirets et des underscores. Si l'identifiant de produit ne respecte pas ce format, Braze le filtrera de votre synchronisation de catalogue.

Il s'agira de l'identifiant principal que vous utiliserez pour référencer les informations du catalogue Braze.

{% alert note %}
Si vous sélectionnez SKU comme ID de votre catalogue, assurez-vous que tous vos produits et variantes dans votre boutique ont un SKU défini et qu'il est unique.
- Si un article n'a pas de SKU, Braze ne peut pas synchroniser ce produit dans le catalogue.
- Si plusieurs produits possèdent le même SKU, cela peut entraîner un comportement inattendu ou l'écrasement involontaire des informations du produit par le SKU en double.
{% endalert %}

### Étape 3 : Synchronisation en cours {#step-3-sync-in-progress}

Vous recevrez une notification sur le tableau de bord, et votre statut s'affichera comme « En cours » pour indiquer que la synchronisation initiale commence. Le temps nécessaire pour terminer la synchronisation dépendra du nombre de produits et de variantes que Braze devra synchroniser depuis Shopify. Pendant ce temps, vous pouvez quitter cette page et attendre une notification sur le tableau de bord ou un e-mail pour vous informer lorsque l'opération est terminée.

Notez que si votre synchronisation initiale dépasse votre [limite de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers), Braze arrêtera de synchroniser d'autres produits. Si vous dépassez la limite après une synchronisation réussie en raison de nouveaux produits ajoutés au fil du temps, la synchronisation ne sera plus active. Dans les deux cas, les mises à jour de produits depuis Shopify ne seront plus reflétées dans Braze. Contactez votre gestionnaire de compte pour envisager de passer à un niveau supérieur.

### Étape 4 : Synchronisation terminée {#step-4-sync-completed}

Vous recevrez une notification sur le tableau de bord et un e-mail une fois la synchronisation réussie. La page partenaire Shopify mettra également à jour l'état sous les catalogues Shopify en « Synchronisation ». Vous pouvez consulter vos produits en cliquant sur le nom du catalogue dans la page partenaire Shopify.

Reportez-vous aux [cas d'utilisation supplémentaires des catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/use/) pour en savoir plus sur la façon de tirer parti des données de catalogue pour personnaliser vos messages.

#### Données de catalogue Shopify prises en charge {#supported-shopify-catalog-data}

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Toute modification du catalogue Shopify peut interférer involontairement avec les synchronisations de produits en temps réel. N'apportez aucune modification au catalogue Shopify, car elles pourraient être écrasées par Shopify. Effectuez plutôt les mises à jour nécessaires des produits dans votre instance Shopify.<br><br>Pour supprimer votre catalogue Shopify, accédez à la page Shopify et désactivez la synchronisation. Ne supprimez pas directement le catalogue Shopify sur la page des catalogues.
{% endalert %}

## Cas d'utilisation de retour en stock et de baisse de prix {#back-in-stock-and-price-drop-use-cases}

Pour configurer les notifications de retour en stock, suivez les étapes [ici]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/).

Pour configurer les notifications de baisse de prix, suivez les étapes [ici]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/).

Notez qu'avec l'intégration Shopify, vous devrez créer un événement personnalisé qui capture le statut d'abonnement d'un utilisateur dans votre catalogue pour chaque cas d'utilisation. L'événement personnalisé nécessitera une propriété d'événement qui correspond soit au [SKU, soit au Shopify Variant ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/#step-2-select-your-product-identifier) que vous avez sélectionné dans le cadre de la synchronisation de vos produits Shopify.

## Changement de l'ID du catalogue {#changing-catalog-id}

Pour changer l'identifiant de produit de votre catalogue Shopify, vous devez désactiver la synchronisation. Confirmez d'abord que vous avez cessé d'envoyer tout message utilisant ces données de catalogue Shopify. Relancez la synchronisation initiale du catalogue Shopify et sélectionnez l'identifiant de produit souhaité en suivant les étapes de [synchronisation des produits](#setting-up).

## Désactivation de la synchronisation des produits {#deactivate}

La désactivation de la fonctionnalité de synchronisation des produits Shopify supprimera l'intégralité de votre catalogue et de vos produits. Cela peut également avoir un impact sur les messages qui utilisent activement les données produit de ce catalogue. Confirmez que vous avez mis à jour ou mis en pause ces campagnes ou Canvas avant la désactivation, car cela pourrait entraîner l'envoi de messages sans détails sur les produits. Ne supprimez pas directement le catalogue Shopify sur la page des catalogues.

## Résolution des problèmes {#troubleshooting}
Si la synchronisation de vos produits Shopify rencontre une erreur, cela pourrait être dû aux erreurs suivantes. Suivez les instructions pour corriger le problème et résoudre la synchronisation :

| Erreur | Raison | Solution |
| --- | --- | --- |
| Erreur du serveur | Cela se produit lorsqu'il y a une erreur de serveur du côté de Shopify au moment de la synchronisation de vos produits. | [Désactivez la synchronisation](#deactivate) et resynchronisez l'ensemble de votre inventaire de produits. |
| SKU en double | Cela se produit si vous utilisez un SKU comme ID d'article de catalogue et que plusieurs produits partagent le même SKU. Comme l'ID de l'article du catalogue doit être unique, tous vos produits doivent avoir des SKU uniques. | Vérifiez votre liste complète de produits et de variantes dans Shopify pour vous assurer qu'il n'y a pas de SKU en double. S'il y en a, mettez-les à jour pour qu'ils soient uniques dans votre compte de boutique Shopify. Une fois la correction effectuée, [désactivez la synchronisation](#deactivate) et resynchronisez l'ensemble de votre inventaire de produits. |
| Limite du catalogue dépassée | Cela se produit lorsque vous dépassez votre limite de catalogue. Braze ne pourra pas terminer la synchronisation ou la maintenir active en raison de l'absence d'espace de stockage disponible. | Il existe deux solutions à ce problème :<br><br>1. Contactez votre gestionnaire de compte pour passer à un niveau supérieur afin d'augmenter votre limite de catalogue.<br><br>2. Libérez de l'espace de stockage en supprimant l'un des éléments suivants :<br>- Des articles de catalogue d'autres catalogues<br>- D'autres catalogues<br>- Des sélections créées<br><br> Après avoir utilisé l'une ou l'autre des solutions, la synchronisation doit être désactivée puis relancée. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }