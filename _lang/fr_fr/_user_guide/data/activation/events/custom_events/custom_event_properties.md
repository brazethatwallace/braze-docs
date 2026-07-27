---
nav_title: Propriétés d'événement personnalisé
article_title: Propriétés d'événement personnalisé
page_order: 0
page_type: reference
description: "Cet article décrit les propriétés d'événement personnalisé, leur format attendu, comment les utiliser et le stockage des propriétés d'événement personnalisé."
---

# Propriétés d'événement personnalisé {#custom-event-properties}

> Cet article décrit les propriétés d'événement personnalisé, leur format attendu, comment les utiliser pour l'envoi de messages et la segmentation, ainsi que le stockage des propriétés d'événement personnalisé.

Les propriétés d'événement personnalisé sont des métadonnées ou des attributs d'événement personnalisé qui décrivent une occurrence spécifique d'un événement. Ces propriétés peuvent être utilisées pour affiner les conditions de déclenchement, augmenter la personnalisation des messages, suivre les conversions et générer des analyses plus sophistiquées via l'exportation de données brutes.

Les propriétés d'événement personnalisé ne sont pas stockées sur le profil Braze et ne consomment donc pas de points de donnée (voir [Points de donnée](#data-points) pour les exceptions).

{% alert important %}
Chaque événement personnalisé ou achat peut comporter jusqu'à 256 propriétés d'événement personnalisé distinctes. Si un événement personnalisé ou un achat est enregistré avec plus de 256 propriétés, seules les 256 premières seront capturées et disponibles.
{% endalert %}

## Format attendu {#expected-format}

Les valeurs des propriétés doivent être un objet : les clés sont les noms des propriétés (chaînes de caractères non vides, 255 caractères maximum, sans `$` en début), et les valeurs sont les valeurs des propriétés. Pour les types de données pris en charge, les exigences de format et les limites de payload, consultez [Types de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#event-property-data-types).

Vous pouvez modifier le type de données de votre propriété d'événement personnalisé, mais soyez conscient des impacts du [changement de type de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) après la collecte des données.

### Clés réservées {#reserved-keys}

Vous ne pouvez pas utiliser de clés réservées comme noms de propriétés d'événement. L'utilisation d'une clé réservée dans l'objet `properties` renvoie l'erreur « Invalid 'properties' field ».

| Propriété | Clé réservée |
| --- | --- |
| Événements personnalisés | `time` et `event_name` |
| Événements d'achat | `time`, `product_id`, `quantity`, `event_name`, `price`, `currency` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clés réservées" }

## Utiliser les propriétés d'événement personnalisé {#using-custom-event-properties}

Les propriétés d'événement personnalisé peuvent être utilisées pour qualifier les déclencheurs de Campaign, suivre les conversions et personnaliser les messages.

### Déclencher des messages {#trigger-messages}

Utilisez les propriétés d'événement personnalisé pour affiner davantage votre audience pour une Campaign ou un Canvas particulier. Par exemple, si vous avez une application d'e-commerce et souhaitez envoyer un message à un utilisateur lorsqu'il abandonne son panier, vous pouvez ajouter une propriété d'événement personnalisé `price` pour améliorer votre audience cible et permettre une personnalisation accrue de la Campaign.

![Filtres de propriétés d'événement personnalisé pour un panier abandonné. Deux filtres sont combinés avec un opérateur AND pour envoyer cette Campaign aux utilisateurs qui ont abandonné leur panier avec un prix compris entre 100 et 200 dollars]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

Les propriétés d'événement personnalisé imbriquées sont également prises en charge dans la [livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Filtres de propriétés d'événement personnalisé pour un panier abandonné. Un filtre est sélectionné si un article du panier a un prix supérieur à 100 dollars.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### Personnaliser les messages {#personalize-messages}

Vous pouvez également utiliser les propriétés d'événement personnalisé pour la personnalisation au sein du modèle de message. Toute Campaign utilisant la [livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) avec un événement déclencheur peut utiliser les propriétés d'événement personnalisé de cet événement pour la personnalisation des messages.

#### Considérations relatives aux filtres {#considerations-with-filters}

- **Appels API :** Lorsque vous effectuez des appels API et utilisez le filtre « est vide », une propriété d'événement personnalisé est considérée comme « vide » si elle est exclue de l'appel. Par exemple, si vous incluez `"event_property": ""`, vos utilisateurs sont considérés comme « non vides ».
- **Entiers :** Lorsque vous filtrez sur une propriété d'événement personnalisé de type nombre et que le nombre est très grand, n'utilisez pas le filtre « exactement ». Si un nombre est trop grand, il peut être arrondi à une certaine longueur, et votre filtre ne fonctionnera pas comme prévu.

#### Coercition de type pour les comparaisons {#type-coercion-for-comparisons}

Lorsque vous utilisez des propriétés d'événement dans des instructions conditionnelles Liquid, vous pouvez rencontrer l'erreur `Liquid error: comparison of String with 0 failed` si vous comparez une propriété d'événement de type entier en utilisant des opérateurs tels que supérieur à, inférieur à ou égal à. Cela se produit parce que Liquid traite la propriété comme une chaîne de caractères par défaut.

Pour corriger cela, utilisez le filtre `plus: 0` pour convertir la propriété en nombre avant la comparaison :

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent >= 100 %}
  Great job completing the level quickly!
{% endif %}
```
{% endraw %}

Par exemple, si vous avez une application de jeu et souhaitez envoyer un message aux utilisateurs qui ont terminé un niveau, vous pourriez personnaliser davantage votre message avec une propriété indiquant le temps qu'il a fallu aux utilisateurs pour terminer ce niveau.

Le message suivant est personnalisé pour trois Segments différents en utilisant la [logique conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic). La propriété d'événement personnalisé appelée `time_spent` peut être incluse dans le message en appelant ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif time_spent < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Si l'utilisateur n'a pas de connexion Internet, les messages in-app déclenchés avec des propriétés d'événement personnalisé modélisées (par exemple, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) échouent et ne s'affichent pas.
{% endalert %}

Pour une liste complète des étiquettes Liquid qui entraînent la distribution des messages in-app en tant que messages in-app modélisés, consultez la [Foire aux questions]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

#### Canvas {#canvas}

Dans Canvas, `context` et `event_properties` servent des objectifs différents :

- **`context`** : Propriétés de l'événement ou de l'appel API qui a déclenché l'entrée dans le Canvas. Utilisez `context` dans n'importe quelle étape Message, y compris la première.
- **`event_properties`** : Propriétés d'un événement personnalisé ou d'un achat qui se produit pendant le parcours. Utilisez-les uniquement dans la première étape Message après une étape [Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) — pas sur le chemin « Tous les autres », et pas dans les étapes Message suivantes.

{% alert important %}
Dans la première étape Message d'un Canvas, utilisez `context` au lieu de `event_properties`, ou ajoutez une étape Parcours d'action avant l'étape Message. Exception : pour les messages in-app, vous pouvez utiliser `event_properties` dans la première étape Message lorsque cet événement est le déclencheur d'entrée du Canvas.
{% endalert %}

Pour plus d'informations, consultez [Contexte et propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) et [Propriétés d'entrée Canvas et propriétés d'événement](#canvas-entry-properties-and-event-properties).

### Segmentation {#segmentation}

Utilisez la segmentation par propriétés d'événement pour cibler les utilisateurs en fonction des événements personnalisés effectués et des propriétés associées à ces événements. Cela augmente vos options de filtrage lors de la segmentation par achat et événements personnalisés.

Les propriétés d'événement pour les événements personnalisés sont mises à jour en temps réel pour tout Segment qui les utilise. Vous pouvez gérer les propriétés en accédant à **Paramètres des données** > **Événements personnalisés** et en sélectionnant **Gérer les propriétés** pour l'événement personnalisé associé. Les propriétés d'événement personnalisé utilisées dans certains filtres de Segment ont un historique de consultation maximal de 30 jours.

#### Ajouter des propriétés d'événement pour la segmentation {#adding-event-properties-for-segmentation}

Vous avez besoin de l'[autorisation utilisateur]({{site.baseurl}}/user_guide/data/infrastructure/data_points#viewing-data-point-usage) « Edit Custom Event Property Segmentation » pour créer des Segments basés sur la récence et la fréquence des propriétés d'événement.

Par défaut, vous pouvez avoir 20 propriétés d'événement segmentables par espace de travail. Contactez votre gestionnaire de compte Braze pour augmenter cette limite.

Pour ajouter des propriétés d'événement pour la segmentation, procédez comme suit :

1. Accédez à votre événement personnalisé et sélectionnez **Gérer les propriétés**.
2. Sélectionnez le bouton **Activer la segmentation** pour ajouter la propriété d'événement à la segmentation. Vous pouvez accéder à des options de filtrage supplémentaires lors de la segmentation.

Les filtres de segmentation par propriétés d'événement incluent :

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Un groupe de filtres avec « Panier abandonné » avec la propriété « nombre d'articles » et la valeur 2 plus d'une fois au cours des 30 derniers jours calendaires.]({% image_buster /assets/img/nested_object3.png %})

Les données ne sont enregistrées pour une propriété d'événement donnée qu'après son activation, et les propriétés d'événement ne sont disponibles qu'à partir de cette date.

#### Points de donnée {#data-points}

En ce qui concerne l'utilisation de l'abonnement, les propriétés d'événement personnalisé activées pour la segmentation avec les filtres suivants sont toutes comptées comme des points de donnée distincts en plus du point de donnée comptabilisé par l'événement personnalisé lui-même :

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriétés d'entrée Canvas et propriétés d'événement {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Objets imbriqués {#nested-objects}

Vous pouvez utiliser des objets imbriqués (des objets à l'intérieur d'un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour modéliser des informations personnalisées dans les messages, déclencher des envois de messages et segmenter les utilisateurs.

Pour en savoir plus, consultez notre page dédiée sur les [objets imbriqués]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

## Stockage des propriétés d'événement personnalisé {#custom-event-property-storage}

Les propriétés d'événement personnalisé sont conçues pour vous aider à affiner la précision du ciblage et à rendre vos messages encore plus personnalisés. Les propriétés d'événement personnalisé peuvent être stockées dans Braze à court et à long terme.

Vous pouvez segmenter en fonction des valeurs des propriétés d'événement de deux manières :

1. **Dans les 30 jours :** Vous pouvez utiliser la segmentation par propriétés d'événement basée sur la fréquence et la récence de valeurs spécifiques de propriétés d'événement au sein des Segments Braze. Cette option a un impact sur l'utilisation des données.<br><br>
2. **Dans et au-delà de 30 jours :** Pour couvrir la segmentation par propriétés d'événement à court et à long terme, vous pouvez utiliser les [extensions de segments]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Cette fonctionnalité segmente les utilisateurs en fonction des événements personnalisés et des propriétés d'événement suivis au cours des deux dernières années. Cette option n'a pas d'impact sur l'utilisation des données.

Contactez votre gestionnaire du succès des clients Braze pour obtenir des recommandations sur la meilleure approche en fonction de vos besoins spécifiques.