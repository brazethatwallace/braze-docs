---
nav_title: Mise à jour utilisateur
article_title: Mise à jour utilisateur
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Cet article de référence présente le composant Mise à jour utilisateur et explique comment l'utiliser dans vos Canvas."
tool: Canvas
---

# Mise à jour utilisateur {#user-update}

> Le composant Mise à jour utilisateur vous permet de mettre à jour les attributs, événements et achats d'un utilisateur dans un éditeur JSON, sans avoir besoin d'inclure des informations sensibles comme les clés API.

## Fonctionnement de ce composant {#how-this-component-works}

![Une étape de mise à jour de l'utilisateur nommée « Update loyalty » qui met à jour un attribut « Is Premium Member » à « true ».]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Lorsque vous utilisez ce composant dans votre Canvas, les mises à jour ne sont pas comptabilisées dans la limite de débit de requêtes par minute `/users/track`. Ces mises à jour sont regroupées par lots afin que Braze puisse les traiter plus efficacement qu'un webhook Braze vers Braze. Notez que ce composant n'enregistre pas de [points de donnée]({{site.baseurl}}/user_guide/data/infrastructure/data_points) lorsqu'il est utilisé pour mettre à jour des points de donnée non facturables (comme les groupes d'abonnement).

Une fois que les utilisateurs ont atteint l'étape de mise à jour de l'utilisateur et que le traitement est terminé, ils passent à l'étape suivante. Cela signifie que tout message ultérieur qui dépend de ces mises à jour est à jour lorsque l'étape suivante est exécutée.

## Créer une mise à jour utilisateur {#creating-a-user-update}

Faites glisser et déposez le composant depuis la barre latérale, ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> en bas de la variante ou de l'étape, puis sélectionnez **User Update**.

Trois options vous permettent de mettre à jour les informations existantes du profil utilisateur, d'ajouter de nouvelles informations ou de supprimer des informations du profil utilisateur. Au total, les étapes User Update d'un espace de travail peuvent mettre à jour jusqu'à 200 000 profils utilisateur par minute.

{% alert tip %}
Vous pouvez également tester les modifications apportées par ce composant en recherchant un utilisateur et en lui appliquant la modification. Cela mettra à jour l'utilisateur.
{% endalert %}

## Mise à jour des attributs personnalisés {#updating-custom-attributes}

Pour mettre à jour ou supprimer un attribut personnalisé, sélectionnez un nom d'attribut dans votre liste d'attributs et saisissez la valeur.

![Étape de mise à jour de l'utilisateur qui met à jour les deux attributs « Loyalty Member » et « Loyalty Program » à « true ».]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Suppression d'attributs personnalisés {#removing-custom-attributes}

Pour supprimer un attribut personnalisé, sélectionnez un nom d'attribut à l'aide du menu déroulant. Vous pouvez passer à l'[éditeur JSON avancé](#advanced-json-editor) pour effectuer des modifications supplémentaires.

![Étape de mise à jour de l'utilisateur qui supprime l'attribut « Loyalty Member ».]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Augmenter et diminuer des valeurs {#increasing-and-decreasing-values}

L'étape de mise à jour de l'utilisateur peut augmenter ou diminuer la valeur d'un attribut. Sélectionnez l'attribut, sélectionnez **Increment By** ou **Decrement By**, puis saisissez un nombre.

#### Suivre la progression hebdomadaire {#track-weekly-progress}

En incrémentant un attribut personnalisé qui suit un événement, vous pouvez suivre le nombre de cours qu'un utilisateur a suivis au cours d'une semaine. Grâce à ce composant, le compteur de cours peut être réinitialisé au début de la semaine et recommencer le suivi.

![Étape de mise à jour de l'utilisateur qui incrémente l'attribut « class_count » de un.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Mettre à jour un tableau d'objets {#updating-an-array-of-objects}

Un [tableau d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) est un attribut personnalisé riche en données stocké dans le profil d'un utilisateur. Vous pouvez l'utiliser pour créer un historique des interactions de l'utilisateur avec votre marque et pour créer des Segments basés sur un champ calculé, tel que l'historique d'achats ou la valeur vie client totale.

En utilisant l'option **Advanced JSON Editor**, vous pouvez insérer du JSON pour ajouter ou supprimer des éléments de ce tableau d'objets.

#### Cas d'usage : mettre à jour la liste de souhaits d'un utilisateur {#use-case-updating-a-users-wishlist}

Suivez la liste de souhaits d'un utilisateur afin de pouvoir segmenter ou personnaliser en fonction de ses articles enregistrés.

1. Créez un attribut personnalisé qui est un tableau d'objets, par exemple `wishlist`. Chaque objet peut inclure des champs tels que `product_id`, `product_name` et `added_at`.
2. Dans l'étape de mise à jour de l'utilisateur, sélectionnez **Advanced JSON Editor**. Ensuite, dans la section **Compose**, utilisez l'opération `$add` pour ajouter un élément ou l'opération `$remove` pour supprimer un élément par valeur.

Voici un exemple d'ajout d'un élément à la liste de souhaits :

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

Pour supprimer un élément, utilisez `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` avec la même structure d'objet afin que Braze puisse le trouver et le supprimer.

#### Cas d'usage : calculer le total du panier d'achat {#use-case-calculating-the-shopping-cart-total}

Suivez quand un utilisateur a des articles dans son panier, quand il ajoute ou supprime des articles, et quel est le montant total du panier.

1. Créez un tableau d'objets personnalisé appelé `shopping_cart`. L'exemple suivant montre à quoi cet attribut peut ressembler. Chaque article possède un `product_id` unique qui contient des données supplémentaires dans son propre tableau d'objets imbriqué, y compris `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2. Créez un [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) nommé `add_item_to_cart` qui est enregistré lorsqu'un utilisateur ajoute un article au panier.
3. Créez un Canvas qui cible les utilisateurs effectuant cet événement personnalisé. Désormais, lorsqu'un utilisateur ajoute un article à son panier, ce Canvas est déclenché. Vous pouvez ensuite cibler directement la communication vers cet utilisateur, en proposant des codes de réduction lorsqu'il a atteint un certain montant de dépenses, abandonné son panier pendant un certain temps, ou toute autre action correspondant à votre cas d'usage.

L'attribut `shopping_cart` contient le total de nombreux événements personnalisés : le coût total de tous les articles, le nombre total d'articles dans le panier, si le panier contient un cadeau, et ainsi de suite. Voici à quoi cela peut ressembler :

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Définir une propriété d'entrée Canvas comme attribut {#setting-canvas-entry-property-as-an-attribute}

Vous pouvez utiliser l'étape de mise à jour utilisateur pour conserver une `canvas_entry_property`. Imaginons que vous avez un événement qui se déclenche lorsqu'un article est ajouté au panier. Vous pouvez stocker l'ID de l'article le plus récemment ajouté au panier et l'utiliser pour une campagne de remarketing. Utilisez la fonctionnalité de personnalisation pour récupérer une propriété d'entrée Canvas et la stocker dans un attribut.

![Étape de mise à jour utilisateur qui met à jour l'attribut « most_recent_cart_item » avec un ID d'article.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personnalisation {#personalization}

Pour stocker la propriété de l'événement déclencheur d'un Canvas en tant qu'attribut, utilisez la fenêtre modale de personnalisation pour extraire et stocker la propriété d'entrée Canvas. La mise à jour utilisateur prend également en charge les fonctionnalités de personnalisation suivantes :

* [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
* [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
* [Propriétés d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)
* Logique Liquid (y compris l'[abandon de messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages))
* Mises à jour de plusieurs attributs ou événements par objet

{% alert warning %}
Nous recommandons d'utiliser avec précaution la personnalisation Liquid via le contenu connecté dans les étapes de mise à jour utilisateur, car ce type d'étape est soumis à une limitation du débit de 200 000 requêtes par minute. Cette limitation du débit prévaut sur la limitation du débit du Canvas.
{% endalert %}

## Éditeur JSON avancé {#advanced-json-editor}

Ajoutez un objet JSON d'attribut, d'événement ou d'achat jusqu'à 65 536 caractères dans l'éditeur JSON. L'[abonnement global]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) et l'état du [groupe d'abonnement]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups) d'un utilisateur peuvent également être définis.

![Ajoutez un objet JSON d'attribut, d'événement ou d'achat jusqu'à 65 536 caractères dans l'éditeur JSON. L'abonnement global et l'état du groupe d'abonnement d'un utilisateur peuvent également être définis.]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

L'éditeur JSON vous permet également de prévisualiser et de tester la mise à jour du profil utilisateur avec vos modifications dans l'onglet **Preview and test**. Vous pouvez sélectionner un utilisateur aléatoire ou rechercher un utilisateur spécifique. Ensuite, après avoir envoyé un test à un utilisateur, consultez le profil utilisateur à l'aide du lien généré.

![L'éditeur JSON vous permet également de prévisualiser et de tester la mise à jour du profil utilisateur avec vos modifications dans l'onglet Preview and test. Vous pouvez sélectionner un utilisateur aléatoire ou rechercher un utilisateur spécifique. Ensuite, après avoir envoyé un test à un utilisateur, consultez le profil utilisateur à l'aide du lien généré.]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Considérations {#considerations}

Vous n'avez pas besoin d'inclure de données sensibles telles que votre clé API lors de l'utilisation de l'éditeur JSON, car celles-ci sont automatiquement fournies par la plateforme. Les champs suivants ne doivent pas être inclus dans l'éditeur JSON :
* ID utilisateur externe
* Clé API
* URL du cluster Braze
* Champs relatifs aux imports de jetons push

{% alert important %}
Les propriétés Canvas (telles que les étiquettes Liquid `canvas_id`, `canvas_name` et `canvas_variant_name`) ne sont pas prises en charge dans les étapes de mise à jour de l'utilisateur.
{% endalert %}

{% raw %}
### Journaliser des événements personnalisés {#log-custom-events}

L'éditeur JSON vous permet également de journaliser des événements personnalisés. Notez que cela nécessite un horodatage au format ISO, il est donc nécessaire d'assigner une date et une heure avec Liquid au début. Prenons cet exemple qui journalise un événement avec un horodatage.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

L'exemple suivant associe un événement à une application spécifique en utilisant un événement personnalisé avec des propriétés optionnelles et l'`app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Modifier l'état d'abonnement {#edit-subscription-state}

L'éditeur JSON vous permet également de modifier l'état d'abonnement d'un utilisateur. Par exemple, l'extrait suivant montre l'état d'abonnement d'un utilisateur mis à jour en `opted_in`.

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Mettre à jour les groupes d'abonnement {#update-subscription-groups}

Vous pouvez également mettre à jour les groupes d'abonnement à l'aide de cette étape Canvas. L'exemple suivant montre comment mettre à jour un ou plusieurs groupes d'abonnement.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}