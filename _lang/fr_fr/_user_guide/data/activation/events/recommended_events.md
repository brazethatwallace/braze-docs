---
nav_title: Événements recommandés
article_title: Événements recommandés
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Cet article de référence décrit les événements recommandés, qui sont des recommandations fournies par Braze pour les événements eCommerce."
---

# Événements recommandés

> Les événements recommandés correspondent aux cas d'utilisation eCommerce les plus courants. En les utilisant, vous pouvez accéder à des modèles de Canvas prédéfinis, des tableaux de bord de reporting alignés sur le cycle de vie client, et bien plus encore.

Par exemple, vous pouvez avoir un événement personnalisé nommé « cart_updated » ou « update_to_cart » pour capturer le moment où un utilisateur a ajouté, supprimé ou mis à jour les produits dans son panier. Pour les événements recommandés, Braze fournit le modèle d'événement, qui inclut un nom défini et les propriétés pertinentes pour cet événement.

{% alert important %}
Les événements recommandés sont actuellement en accès anticipé. Contactez votre gestionnaire de la satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous utilisez le nouveau [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), ces événements recommandés seront automatiquement disponibles via l'intégration.
{% endalert %}

## Comment ça fonctionne

Braze applique une validation spéciale à tous les événements recommandés, et certains d'entre eux disposent d'actions de post-traitement spéciales. Pour certains événements recommandés par secteur, Braze peut prendre en charge un traitement spécial, comme de nouveaux déclencheurs basés sur l'action pour les campagnes et les Canvas.

Les événements recommandés fonctionnent de manière similaire aux [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/). Vous pouvez exporter les événements recommandés depuis Currents, les ajouter à une liste de blocage et les utiliser dans vos rapports. Vous pouvez également envoyer des données à Braze pour suivre ces événements à l'aide du [SDK Braze]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) ou de l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Événements recommandés eCommerce

Les [événements recommandés eCommerce]({{site.baseurl}}/ecommerce_events/) sont basés sur les événements recommandés. Ils permettent de suivre les actions effectuées par vos clients, comme la consultation d'un produit, la mise à jour de leur panier ou le début du processus de paiement.

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### Modèles de Canvas eCommerce

Consultez nos [cas d'utilisation eCommerce]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/) dédiés pour découvrir comment tirer parti des modèles prédéfinis de Canvas Braze et mettre en œuvre des stratégies essentielles.

## Questions fréquentes

### Les événements recommandés sont-ils identiques aux événements personnalisés ?

Non. Braze définit des schémas de données structurés pour les événements recommandés. Cela inclut des propriétés d'événement requises et facultatives qui font l'objet d'un processus de validation dans Braze. Les [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) sont des actions spécifiques effectuées par vos utilisateurs, ou des mises à jour les concernant, dans votre application ou sur votre site web, que vous souhaitez suivre. Vous pouvez personnaliser le nom de l'événement et ce qu'il suit.

### Puis-je personnaliser le nom des événements recommandés ?

Non. Les événements recommandés ont des noms et des propriétés standardisés. Cette standardisation contribue à assurer la cohérence de vos données.

### Puis-je toujours utiliser les événements d'achat pour enregistrer des achats ?

Avec le lancement des événements recommandés eCommerce, Braze prévoit de retirer progressivement l'ancien événement d'achat à l'avenir. Si vous utilisez actuellement l'événement d'achat, vous recevrez un préavis concernant les plans de dépréciation. En attendant, vous pouvez continuer à utiliser les événements d'achat jusqu'à la date officielle de dépréciation.