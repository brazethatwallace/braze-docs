---
nav_title: FAQ
article_title: FAQ sur la synchronisation des produits Shopify
page_order: 0
page_type: FAQ
description: "Cette page fournit des réponses aux questions fréquemment posées sur la synchronisation des produits Shopify avec les catalogues Braze."
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cette page fournit des réponses à certaines questions fréquemment posées sur la [synchronisation des produits Shopify]({{site.baseurl}}/shopify_catalogs/).

## Comportement du catalogue et de la synchronisation {#catalog-and-sync-behavior}

### Puis-je modifier mon catalogue Shopify directement dans Braze ? {#can-i-edit-my-shopify-catalog-directly-in-braze}

Non. Le catalogue Shopify est en lecture seule dans Braze. Toute modification manuelle peut être écrasée lors de la prochaine synchronisation. Effectuez toutes les mises à jour de produits directement dans Shopify.

### Comment supprimer mon catalogue Shopify ? {#how-do-i-delete-my-shopify-catalog}

Pour supprimer votre catalogue Shopify, désactivez la synchronisation depuis la page partenaire Shopify. Ne supprimez pas le catalogue directement depuis la page **Catalogs**. La désactivation supprime l'intégralité de votre catalogue, y compris toutes les étiquettes, collections et données de métachamps synchronisées. Avant de désactiver, mettez à jour ou suspendez toutes les campagnes ou Canvas qui font référence à ce catalogue, car ils pourraient envoyer des messages avec des détails de produit manquants.

### Que se passe-t-il si je supprime un produit ou un champ de produit précédemment synchronisé dans Shopify ? {#what-happens-if-i-delete-a-previously-synced-product-or-product-field-in-shopify}

Braze supprime automatiquement le produit ou le champ de votre catalogue Shopify lorsqu'il détecte la suppression. Cependant, toutes les campagnes, Canvas ou segments qui font référence au produit ou au champ supprimé cesseront de fonctionner. Avant de supprimer des produits ou des champs dans Shopify, vérifiez qu'ils ne sont pas activement utilisés dans Braze.

### Comment modifier l'ID de mon catalogue (identifiant de produit) ? {#how-do-i-change-my-catalog-id-product-identifier}

Pour modifier l'ID de votre catalogue, désactivez d'abord la synchronisation et confirmez qu'aucun message actif ne fait référence aux données de ce catalogue. Ensuite, relancez la synchronisation initiale et sélectionnez l'identifiant souhaité.

### La modification de mes étiquettes, collections ou métachamps synchronisés affectera-t-elle les campagnes actives ? {#will-changing-my-synced-tags-collections-or-metafields-affect-active-campaigns}

Oui. La modification de vos sélections synchronisées peut affecter les campagnes, Canvas ou [sélections de catalogue]({{site.baseurl}}/catalog_selections/) actifs qui y font référence. Vérifiez que votre contenu actif est mis à jour avant d'effectuer des modifications.

### Combien de temps dure la synchronisation initiale ? {#how-long-does-the-initial-sync-take}

La durée de la synchronisation dépend du nombre de produits et de variantes dans votre boutique. La synchronisation initiale récupère les produits par lots, il peut donc falloir un certain temps avant que toutes les étiquettes de produits, les métachamps et les associations de collections apparaissent. Surveillez l'état de votre synchronisation sur la page partenaire Shopify.

## Configuration et limites {#configuration-and-limits}

### Combien d'étiquettes, de collections ou de métachamps puis-je synchroniser ? {#how-many-tags-collections-or-metafields-can-i-sync}

Vous pouvez synchroniser jusqu'à 20 de chaque par configuration :

- Jusqu'à 20 étiquettes de produits
- Jusqu'à 20 collections
- Jusqu'à 20 métachamps de produits

### Que se passe-t-il si un produit appartient à plus de 250 collections ? {#what-if-a-product-belongs-to-more-than-250-collections}

Shopify permet aux produits d'appartenir à plus de 250 collections, mais Braze ne peut récupérer que les 250 premières associations de collections par produit. Si un produit appartient à une collection sélectionnée qui se situe au-delà des 250 premières récupérées, cette association ne sera pas reflétée dans votre catalogue Shopify. Si vous constatez des associations de collections manquantes, contactez votre gestionnaire de la satisfaction client.

### Pourquoi ne vois-je pas toutes mes collections dans la boîte de dialogue modale de configuration ? {#why-dont-i-see-all-my-collections-in-the-configuration-modal}

La boîte de dialogue modale de configuration affiche jusqu'à 5 000 des collections les plus récemment mises à jour. Si votre boutique dépasse cette limite, les collections plus anciennes peuvent ne pas apparaître. Les collections précédemment sélectionnées qui se situent au-delà des 5 000 premières seront toujours affichées dans votre sélection.

### Puis-je filtrer à la fois par étiquettes et par collections dans une seule sélection de catalogue ? {#can-i-filter-by-both-tags-and-collections-in-a-single-catalog-selection}

Non. Les sélections de catalogue ne prennent en charge qu'un seul champ de type tableau par filtre de sélection. Vous ne pouvez pas combiner étiquettes et collections dans la même sélection. Si vous devez cibler des utilisateurs en fonction de critères d'étiquettes et de collections, utilisez plutôt les [Extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) avec des requêtes SQL.

### Quelles sont les limites des sélections de catalogue ? {#what-are-the-catalog-selection-limits}

Les sélections de catalogue sont soumises aux mêmes limites que les sélections de catalogue standard. Pour plus de détails sur les limites d'éléments, les contraintes de filtres et les plafonds de stockage par niveau, consultez [Sélections de catalogue]({{site.baseurl}}/catalog_selections/).

## Métachamps et résolution des problèmes {#metafields-and-troubleshooting}

### Pourquoi certains de mes types de métachamps n'apparaissent-ils pas ? {#why-are-some-of-my-metafield-types-not-showing-up}

Seuls les types de métachamps pris en charge apparaissent dans la boîte de dialogue modale de configuration. Les types suivants ne sont actuellement pas pris en charge : `dimension`, `json`, `link`, `money`, `rating`, `rich_text_field`, `volume` et `weight`. Pour les types pris en charge et la liste complète, consultez [Métachamps de produits Shopify]({{site.baseurl}}/shopify_catalogs/#shopify-product-metafields) sur la page de synchronisation des produits Shopify.

### J'ai reçu une erreur « Duplicate Metafield Column Name ». Que dois-je faire ? {#i-got-a-duplicate-metafield-column-name-error-what-do-i-do}

Deux ou plusieurs de vos métachamps sélectionnés créeraient le même nom de colonne dans le catalogue. Désélectionnez l'un des métachamps en conflit, ou renommez la clé du métachamp dans Shopify afin que chacun corresponde à un nom de colonne unique. Ensuite, enregistrez à nouveau votre configuration.

### Pourquoi mes étiquettes mettent-elles plus de temps que prévu à se charger ? {#why-are-my-tags-taking-longer-than-expected-to-load}

Les étiquettes sont récupérées directement depuis Shopify lorsque vous ouvrez la boîte de dialogue modale de configuration. Si votre boutique comporte un grand nombre de produits ou d'étiquettes, le chargement peut prendre plus de temps. Il s'agit d'un comportement attendu qui n'affecte pas les performances de synchronisation. Si le chargement expire systématiquement, essayez de réduire le nombre total d'étiquettes dans votre boutique Shopify ou contactez l'assistance.

## Stockage {#storage}

### La synchronisation de données de produits supplémentaires affectera-t-elle mon stockage de catalogue ? {#will-syncing-additional-product-data-affect-my-catalog-storage}

Oui. La synchronisation des étiquettes, des métachamps et des collections augmente l'utilisation de votre stockage de catalogue. Le niveau gratuit de catalogue dispose d'une limite de stockage de 100 Mo. Si votre synchronisation dépasse votre limite, Braze arrête la synchronisation et les mises à jour de produits ne seront plus reflétées. Contactez votre gestionnaire de compte pour mettre à niveau votre niveau si nécessaire.