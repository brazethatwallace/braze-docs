---
nav_title: Vue carrousel
article_title: Vue carrousel de Content Cards pour iOS
platform: iOS
page_order: 5
description: "Cet article explique comment déployer un cas d'usage de vue carrousel de Content Cards pour les applications iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Cas d'usage : vue carrousel {#use-case-carousel-view}

![Exemple d'application d'actualités présentant un carrousel de Content Cards dans un article.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Cette section explique comment déployer un flux de carrousel multi-cartes dans lequel un utilisateur peut faire glisser horizontalement pour afficher des cartes en vedette supplémentaires. Pour intégrer une vue carrousel, vous devrez utiliser un déploiement de Content Cards entièrement personnalisé — la phase « exécution » de l'[approche « ramper, marcher, courir »]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

Avec cette approche, vous n'utiliserez pas les vues et la logique par défaut de Braze, mais afficherez les Content Cards de manière totalement personnalisée en utilisant vos propres vues alimentées par les données des modèles Braze.

En termes de niveau d'effort de développement, les différences clés entre le déploiement de base et celui du carrousel comprennent :

- Créer vos propres vues
- Enregistrer l'analyse des Content Cards
- Introduire une logique additionnelle côté client pour déterminer combien de cartes afficher dans le carrousel et lesquelles

## Déploiement {#implementation}

### Étape 1 : Créer un contrôleur de vue personnalisé {#step-1-create-a-custom-view-controller}

Pour créer le carrousel de Content Cards, créez votre propre contrôleur de vue personnalisé (tel que `UICollectionViewController`) et [abonnez-vous aux mises à jour de données]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#getting-the-data). Notez que vous ne pourrez pas étendre ou sous-classer notre `ABKContentCardTableViewController` par défaut, car il ne peut gérer que nos types de Content Cards par défaut.

### Étape 2 : Implémenter l'analytique {#step-2-implement-analytics}

Lors de la création d'un contrôleur de vue entièrement personnalisé, les impressions, les clics et les rejets des Content Cards ne sont pas automatiquement enregistrés. Vous devez implémenter les méthodes d'analytique correspondantes pour vous assurer que les impressions, les événements de rejet et les clics sont correctement enregistrés dans l'analytique du tableau de bord de Braze.

Pour plus d'informations sur les méthodes d'analytique, consultez [Méthodes de carte]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
La même page détaille également les différentes propriétés héritées de notre classe de modèle générique Content Card, que vous pourriez trouver utiles lors du déploiement de votre vue.
{% endalert %}

### Étape 3 : Créer un observateur de Content Card {#step-3-create-a-content-card-observer}

Créez un [observateur de Content Card]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener) qui est responsable de la gestion de l'arrivée des Content Cards, et implémentez une logique conditionnelle pour afficher un nombre spécifique de cartes dans le carrousel à tout moment. Par défaut, les Content Cards sont triées par date de création (les plus récentes en premier), et un utilisateur voit toutes les cartes auxquelles il est éligible.

Cela dit, vous pouvez ordonner et appliquer une logique d'affichage supplémentaire de plusieurs façons. Par exemple, vous pouvez sélectionner les cinq premiers objets Content Card du tableau ou introduire des paires clé-valeur (la propriété `extras` dans le modèle de données) pour construire une logique conditionnelle.

Si vous déployez un carrousel en tant que flux secondaire de Content Cards, consultez [Utiliser plusieurs flux de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds) pour vous assurer de trier les cartes dans le bon flux en fonction des paires clé-valeur.

{% alert important %}
Il est important de s'assurer que vos équipes marketing et de développement se coordonnent sur les paires clé-valeur qui seront utilisées (par exemple, `feed_type = brand_homepage`), car toutes les paires clé-valeur que les marketeurs saisissent dans le tableau de bord de Braze doivent correspondre exactement aux paires clé-valeur que les développeurs intègrent dans la logique de l'application.
{% endalert %}

Pour la documentation développeur spécifique à iOS sur la classe, les méthodes et les attributs des Content Cards, consultez la [référence de la classe iOS `ABKContentCard`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Considérations {#considerations}

- En utilisant des vues entièrement personnalisées, vous ne pourrez pas étendre ou sous-classer les méthodes utilisées dans `ABKContentCardsController`. Vous devrez plutôt intégrer vous-même les méthodes et propriétés du modèle de données.
- La logique et le déploiement de la vue carrousel ne constituent pas un type par défaut de Content Card dans Braze. La logique nécessaire pour réaliser ce cas d'usage doit donc être fournie et maintenue par votre équipe de développement.
- Vous devrez implémenter une logique côté client pour afficher un nombre spécifique de cartes dans le carrousel à tout moment.