---
nav_title: Vue carrousel
article_title: Vue carrousel de Content Cards pour iOS
platform: iOS
page_order: 5
description: "Cet article explique comment implémenter un cas d'utilisation de vue carrousel de Content Cards pour les applications iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Cas d'utilisation : vue carrousel {#use-case-carousel-view}

![Exemple d'application d'actualités présentant un carrousel de Content Cards dans un article.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Cette section explique comment implémenter un flux de carrousel multi-cartes dans lequel un utilisateur peut faire glisser horizontalement pour afficher des cartes en vedette supplémentaires. Pour intégrer une vue carrousel, vous devrez utiliser une implémentation de Content Cards entièrement personnalisée — la phase « exécution » de l'[approche « ramper, marcher, courir »]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize#customization-approaches).

Avec cette approche, vous n'utiliserez pas les vues et la logique par défaut de Braze, mais afficherez les Content Cards de manière totalement personnalisée en utilisant vos propres vues alimentées par les données des modèles Braze.

En termes de niveau d'effort de développement, les différences clés entre l'implémentation de base et celle du carrousel comprennent :

- Créer vos propres vues
- Enregistrer les analyses des Content Cards
- Introduire une logique additionnelle côté client pour déterminer combien de cartes afficher dans le carrousel et lesquelles

## Implémentation {#implementation}

### Étape 1 : Créer un contrôleur de vue personnalisé {#step-1-create-a-custom-view-controller}

Pour créer le carrousel de Content Cards, créez votre propre contrôleur de vue personnalisé (tel que `UICollectionViewController`) et [abonnez-vous aux mises à jour des données]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#getting-the-data). Notez que vous ne pourrez ni étendre ni sous-classer notre `ABKContentCardTableViewController` par défaut, car il est uniquement capable de gérer nos types de Content Cards par défaut.

### Étape 2 : Implémenter les analyses {#step-2-implement-analytics}

Lors de la création d'un contrôleur de vue entièrement personnalisé, les impressions, les clics et les rejets de Content Cards ne sont pas automatiquement enregistrés. Vous devez implémenter les méthodes d'analyse correspondantes pour vous assurer que les impressions, les événements de rejet et les clics sont correctement enregistrés dans les analyses du tableau de bord de Braze.

Pour plus d'informations sur les méthodes d'analyse, reportez-vous aux [méthodes de carte]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#card-methods).

{% alert note %}
La même page détaille également les différentes propriétés héritées de notre classe de modèle de Content Card générique, que vous pouvez trouver utiles pendant l'implémentation de votre vue.
{% endalert %}

### Étape 3 : Créer un observateur de Content Cards {#step-3-create-a-content-card-observer}

Créez un [observateur de Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener) chargé de gérer l'arrivée des Content Cards et implémentez une logique conditionnelle pour afficher un nombre spécifique de cartes dans le carrousel à tout moment. Par défaut, les Content Cards sont triées par date de création (la plus récente en premier) et un utilisateur voit toutes les cartes auxquelles il est éligible.

Cela dit, vous pouvez ordonner et appliquer une logique d'affichage supplémentaire de différentes manières. Par exemple, vous pouvez sélectionner les cinq premiers objets de Content Cards du tableau ou introduire des paires clé-valeur (la propriété `extras` dans le modèle de données) pour concevoir une logique conditionnelle.

Si vous implémentez un carrousel comme flux secondaire de Content Cards, reportez-vous à la section [Utilisation de plusieurs flux de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds) pour vous assurer que vous triez les cartes dans le flux approprié en fonction des paires clé-valeur.

{% alert important %}
Il est important de veiller à ce que vos équipes marketing et de développement se coordonnent sur les paires clé-valeur qui seront utilisées (par exemple, `feed_type = brand_homepage`), car toutes les paires clé-valeur saisies par les marketeurs dans le tableau de bord de Braze doivent correspondre exactement aux paires clé-valeur que les développeurs intègrent dans la logique de l'application.
{% endalert %}

Pour obtenir la documentation pour développeurs spécifique à iOS sur la classe, les méthodes et les attributs des Content Cards, reportez-vous à la [référence de la classe `ABKContentCard`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html) pour iOS.

## Considérations {#considerations}

- En utilisant des vues entièrement personnalisées, vous ne pourrez pas étendre ou sous-classer les méthodes utilisées dans `ABKContentCardsController`. Vous devrez à la place intégrer les méthodes et les propriétés du modèle de données vous-même.
- La logique et l'implémentation de la vue carrousel ne sont pas un type par défaut de Content Card dans Braze. Par conséquent, la logique nécessaire au cas d'utilisation doit être fournie et prise en charge par votre équipe de développement.
- Vous devrez implémenter la logique côté client pour afficher un nombre spécifique de cartes dans le carrousel à tout moment.