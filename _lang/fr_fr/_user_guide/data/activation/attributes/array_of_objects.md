---
nav_title: Tableau d'objets
article_title: Tableau d'objets
alias: "/array_of_objects/"
page_order: 2
page_type: reference
description: "Cet article de référence couvre l'utilisation d'un tableau d'objets comme type de données pour les attributs personnalisés, y compris les limitations et les exemples d'utilisation."
---

# Tableau d'objets {#array-of-objects}

> Cette page explique comment utiliser un tableau d'objets pour regrouper des attributs connexes. Vous pouvez, par exemple, avoir un groupe d'objets « animaux de compagnie », un groupe d'objets « chansons » et un groupe d'objets « compte » pour le même utilisateur. Ces tableaux d'objets peuvent être utilisés pour personnaliser votre envoi de messages avec Liquid, ou segmenter votre audience si un élément d'un objet correspond aux critères.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Restrictions {#considerations}

- Les tableaux d'objets sont destinés aux attributs personnalisés envoyés par l'API. Les téléchargements de fichiers CSV ne sont pas pris en charge, car les virgules dans le fichier CSV sont interprétées comme des séparateurs de colonnes, et les virgules dans les valeurs provoquent des erreurs d'analyse.
- Les tableaux d'objets n'ont pas de limite quant au nombre d'éléments, mais leur taille maximale est de 100&nbsp;Ko. Si une mise à jour (comme `$add` ou `$update`) fait dépasser cette limite au tableau, Braze rejette la mise à jour et l'attribut reste inchangé. La requête API renvoie tout de même une réponse de succès. Pour maintenir le tableau sous la limite afin de pouvoir ajouter de nouveaux éléments, utilisez `$remove` pour supprimer des éléments du tableau au préalable.
- Tous les partenaires de Braze ne prennent pas en charge les tableaux d'objets. Consultez la [documentation du partenaire]({{site.baseurl}}/partners/home/) pour savoir si l'intégration prend en charge cette fonctionnalité.

La mise à jour ou la suppression d'éléments d'un tableau nécessite l'identification de l'élément par sa clé et sa valeur ; pensez donc à inclure un identifiant unique pour chaque élément du tableau. L'unicité est limitée au tableau et s'avère utile si vous souhaitez mettre à jour ou supprimer des objets spécifiques de votre tableau. Cela n'est pas imposé par Braze.

{% alert important %}
Lorsqu'un attribut personnalisé imbriqué dans votre requête contient des valeurs invalides (comme des formats de date/heure incorrects ou des valeurs `null`), Braze rejette toutes les mises à jour d'attributs personnalisés imbriqués de la requête. Cela s'applique à toutes les structures imbriquées au sein de cet attribut spécifique. Vérifiez que toutes les valeurs des attributs personnalisés imbriqués sont valides avant l'envoi. Pour en savoir plus, consultez [Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#how-does-userstrack-handle-invalid-nested-custom-attributes).
{% endalert %}

{% alert tip %}
Pour en savoir plus sur l'utilisation des tableaux d'objets pour les objets d'attributs utilisateur, consultez [Objet attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens).
{% endalert %}

## Exemple d'API {#api-example}

Utilisez ces exemples lorsque vous envoyez des requêtes `/users/track` qui créent ou mettent à jour des attributs personnalisés imbriqués stockés sous forme de tableaux d'objets. Le payload utilise les opérateurs `$add`, `$remove` et `$update` pour modifier des objets spécifiques sans reconstruire l'intégralité du tableau à chaque requête.

{% tabs local %}
{% tab Créer %}

Voici un exemple `/users/track` avec un tableau `pets`. Pour capturer les propriétés des animaux de compagnie, envoyez une requête API qui liste `pets` comme un tableau d'objets. Notez que chaque objet s'est vu attribuer un `id` unique qui pourra être référencé ultérieurement lors des mises à jour.

Utilisez ce format lorsque vous souhaitez créer l'attribut pour la première fois ou remplacer l'intégralité du tableau par un nouvel ensemble de base d'objets.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Ajouter %}

Ajoutez un autre élément au tableau à l'aide de l'opérateur `$add`. L'exemple suivant montre l'ajout de trois objets animaux supplémentaires au tableau `pets` de l'utilisateur.

Utilisez `$add` lorsque vous devez ajouter un ou plusieurs nouveaux objets tout en conservant les objets existants inchangés.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Mettre à jour %}

Mettez à jour les valeurs d'objets spécifiques dans un tableau à l'aide du paramètre `_merge_objects` et de l'opérateur `$update`. Comme pour les mises à jour d'objets simples d'[attributs personnalisés imbriqués]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body), cela effectue une fusion en profondeur.

Notez que `$update` ne peut pas être utilisé pour supprimer une propriété imbriquée d'un objet à l'intérieur d'un tableau. Pour cela, vous devez supprimer l'élément entier du tableau, puis ajouter l'objet sans cette clé spécifique (en combinant `$remove` et `$add`).

Utilisez `$update` lorsque l'objet existe déjà et que vous souhaitez modifier un ou plusieurs champs en faisant correspondre `$identifier_key` et `$identifier_value`.

L'exemple suivant montre la mise à jour de la propriété `breed` en `goldfish` pour l'objet dont l'`id` est `4`. Cet exemple met également à jour l'objet dont l'`id` est `5` avec un nouveau `name` `Annette`. Comme le paramètre `_merge_objects` est défini sur `true`, tous les autres champs de ces deux objets restent inchangés.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
Vous devez définir `_merge_objects` sur true, sinon vos objets seront écrasés. `_merge_objects` est défini sur false par défaut.
{% endalert %}

{% endtab %}
{% tab Supprimer %}

Supprimez des objets d'un tableau à l'aide de l'opérateur `$remove` combiné à une clé correspondante (`$identifier_key`) et une valeur (`$identifier_value`).

Utilisez `$remove` lorsque vous souhaitez supprimer tous les objets correspondant à une paire identifiant connue, comme `id = 2` ou `type = dog`.

L'exemple suivant montre la suppression de tout objet du tableau `pets` dont l'`id` a la valeur `1`, dont l'`id` a la valeur `2`, et dont le `type` a la valeur `dog`. S'il existe plusieurs objets avec la valeur `dog` pour `type`, tous les objets correspondants seront supprimés.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Ordre de traitement {#processing-order}

Lorsqu'une seule requête `/users/track` inclut des opérations `$add`, `$remove` et `$update` pour le même attribut de tableau, Braze les traite dans cet ordre :

1. `$add`
2. `$remove`
3. `$update`

Cet ordre s'applique au sein d'un même objet de mise à jour d'attribut dans une requête et détermine l'état final du tableau une fois toutes les opérations évaluées.

Comme `$add` s'exécute avant `$remove`, vous ne pouvez pas utiliser un `$remove` suivi d'un `$add` comme mécanisme d'upsert au sein d'une même requête. Le `$add` est traité en premier, puis le `$remove` supprime l'élément. Pour effectuer un upsert, envoyez le `$remove` dans une requête séparée avant le `$add`.

### Horodatages {#timestamps}

Lorsque vous incluez des champs comme des horodatages dans un tableau d'objets, utilisez le format `$time` au lieu de chaînes de caractères simples ou d'entiers d'époque Unix.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
Pour en savoir plus, consultez [Attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/).
{% endalert %}

## Exemple SDK {#sdk-example}

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Créer %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Ajouter %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Mettre à jour %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Supprimer %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Créer %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Gus"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Ajouter %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Doug"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Larry"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Mary"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Mettre à jour %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Supprimer %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Les attributs personnalisés imbriqués ne sont pas pris en charge par AppboyKit.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Créer %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Ajouter %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Mettre à jour %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Supprimer %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Modèles Liquid {#liquid-templating}

Vous pouvez utiliser ce tableau `pets` pour personnaliser un message. L'exemple de modèle Liquid suivant montre comment référencer les propriétés de l'objet d'attribut personnalisé enregistrées à partir de la requête API précédente et les utiliser dans vos messages.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %}

{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %}
```
{% endraw %}

Dans ce scénario, vous pouvez utiliser Liquid pour parcourir le tableau `pets` et afficher une phrase pour chaque animal. [Assignez une variable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#assigning-variables) à l'attribut personnalisé `pets` et utilisez la notation par points pour accéder aux propriétés d'un objet. Spécifiez le nom de l'objet, suivi d'un point `.`, suivi du nom de la propriété.

## Segmentation {#segmentation}

Lors de la segmentation des utilisateurs en fonction de tableaux d'objets, un utilisateur sera éligible au segment si un objet quelconque du tableau correspond aux critères.

Créez un nouveau segment et sélectionnez **Attribut personnalisé imbriqué** comme filtre. Recherchez et sélectionnez ensuite le nom de votre tableau d'objets.

![Filtrer par tableau d'objets.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Utilisez la notation par points pour spécifier quel champ du tableau d'objets vous souhaitez utiliser. Commencez le champ de texte par une paire de crochets vides `[]` pour indiquer à Braze que vous recherchez à l'intérieur d'un tableau d'objets. Ajoutez ensuite un point `.`, suivi du nom du champ que vous souhaitez utiliser.

Par exemple, si vous souhaitez filtrer un tableau d'objets `top_3_movies` en fonction du champ `type`, saisissez `[].type` et choisissez les films à filtrer, comme `Fantasy Movie`.


### Niveaux d'imbrication {#levels-of-nesting}

Vous pouvez créer un segment avec un seul niveau d'imbrication de tableau (un tableau à l'intérieur d'un autre tableau). Par exemple, avec les attributs suivants, vous pouvez créer un segment pour `pets[].name` contient `Gus`, mais vous ne pouvez pas créer un segment pour `pets[].nicknames[]` contient `Gugu`.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Points de donnée {#data-points}

Les points de donnée sont comptabilisés différemment selon que vous créez, mettez à jour ou supprimez une propriété.

{% tabs local %}
{% tab Créer %}

La création d'un nouveau tableau consomme un point de donnée pour chaque attribut d'un objet. Cet exemple coûte huit points de donnée : chaque objet animal possède quatre attributs et il y a deux objets.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Mettre à jour %}

La mise à jour d'un tableau existant consomme un point de donnée pour chaque propriété ajoutée. Cet exemple coûte deux points de donnée, car il ne met à jour qu'une seule propriété dans chacun des deux objets.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Supprimer %}

La suppression d'un objet d'un tableau consomme un point de donnée pour chaque critère de suppression envoyé. Cet exemple coûte trois points de donnée, même si vous supprimez potentiellement plusieurs chiens avec cette instruction.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}