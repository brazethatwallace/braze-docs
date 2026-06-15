---
nav_title: "POST : Créer et mettre à jour des utilisateurs (synchrone)"
article_title: "POST : Créer et mettre à jour des utilisateurs (synchrone)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "Cet article présente en détail l'endpoint synchrone de suivi utilisateur de Braze."

---
{% api %}
# Créer et mettre à jour des utilisateurs (synchrone) {#create-and-update-users-synchronous}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> Utilisez cet endpoint pour enregistrer des événements personnalisés et des achats, et pour mettre à jour les attributs de profil utilisateur de manière synchrone. Cet endpoint fonctionne de la même manière que l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), qui met à jour les profils utilisateurs de manière asynchrone.

{% alert important %}
Cet endpoint est actuellement en **version bêta limitée**. Bien que nous n'ajoutions pas de nouveaux clients à la version bêta pour le moment, veuillez informer votre gestionnaire de compte Braze si vous pensez que cette fonctionnalité pourrait être utile pour votre intégration Braze.
{% endalert %}

## Appels d'API synchrones et asynchrones {#synchronous-and-asynchronous-api-calls}

Dans le cadre d'un appel asynchrone, l'API renvoie le code d'état `201`, indiquant que votre requête a été reçue, comprise et acceptée avec succès. Toutefois, cela ne signifie pas que votre requête a été entièrement exécutée.

Dans le cadre d'un appel synchrone, l'API renvoie un code d'état `201`, indiquant que votre requête a été reçue, comprise, acceptée et traitée avec succès. La réponse à l'appel affiche certains champs du profil utilisateur résultant de l'opération.

La limite de débit de cet endpoint est inférieure à celle de l'endpoint `/users/track` (voir [Limite de débit](#rate-limit) ci-dessous). Chaque requête `/users/track/sync` ne peut contenir qu'un seul objet d'événement, un seul objet d'attribut **ou** un seul objet d'achat. Cet endpoint doit être réservé aux mises à jour du profil utilisateur pour lesquelles un appel synchrone est nécessaire. Pour une implémentation saine, nous vous recommandons d'utiliser `/users/track/sync` et `/users/track` ensemble.

Par exemple, si vous envoyez des requêtes consécutives pour le même utilisateur sur une courte période, des conditions de concurrence sont possibles avec l'endpoint asynchrone `/users/track`, mais avec l'endpoint `/users/track/sync`, vous pouvez envoyer ces requêtes en séquence, chacune après avoir reçu une réponse `2XX`.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l'autorisation `users.track.sync`.

Les clients utilisant l'API pour les appels de serveur à serveur devront peut-être ajouter `rest.iad-01.braze.com` à leur liste d'autorisations s'ils sont derrière un pare-feu.

## Limite de débit {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/sync" %}

Nous appliquons une limite de débit de base de 500 requêtes par minute à cet endpoint pour tous les clients. Chaque requête `/users/track/sync` peut contenir jusqu'à un objet d'événement, un objet d'attribut ou un objet d'achat. Chaque objet (tableaux d'événements, d'attributs et d'achats) peut mettre à jour un utilisateur chacun.

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Paramètres de requête {#request-parameters}

{% alert important %}
Pour chaque composant de requête répertorié dans le tableau suivant, vous devez inclure l'un des éléments suivants : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Facultatif | Un objet d'attributs | Voir [objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) |
| `events` | Facultatif | Un objet d'événement | Voir [objet événements]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Facultatif | Un objet d'achat | Voir [objet achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Réponses {#responses}

Lorsque vous utilisez les [paramètres de requête](#request-parameters) de cet endpoint, vous devriez recevoir l'une des réponses suivantes : un message de réussite ou un message contenant des erreurs fatales.

### Message de réussite {#successful-message}

Les messages de réussite renvoient la réponse suivante, qui comprend des informations sur les données du profil utilisateur mises à jour par Braze.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
```

### Message avec erreurs fatales {#message-with-fatal-errors}

Si votre message comporte une erreur fatale, vous recevrez la réponse suivante :

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

## Exemples de requêtes et de réponses {#example-requests-and-responses}

### Mise à jour d'un attribut personnalisé par ID externe {#update-a-custom-attribute-by-external-id}

#### Requête {#request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Réponse {#response}

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### Mise à jour d'un événement personnalisé par e-mail {#update-a-custom-event-by-email}

#### Requête

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
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
}'
```

#### Réponse

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### Mise à jour d'un événement d'achat par alias d'utilisateur {#update-a-purchase-event-by-user-alias}

#### Requête

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Réponse

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## Foire aux questions {#frequently-asked-questions}

### Dois-je utiliser l'endpoint asynchrone ou synchrone ? {#should-i-use-the-asynchronous-or-synchronous-endpoint}

Pour la plupart des mises à jour de profil, l'endpoint `/users/track` est le plus adapté en raison de sa limite de débit plus élevée et de sa flexibilité qui vous permet de regrouper les requêtes. Cependant, l'endpoint `/users/track/sync` est utile si vous rencontrez des conditions de concurrence dues à des requêtes rapides et consécutives pour le même utilisateur.

### Le temps de réponse diffère-t-il de celui de l'endpoint `/users/track` ? {#does-the-response-time-differ-from-the-userstrack-endpoint}

Avec un appel synchrone, l'API attend que Braze termine la requête avant de renvoyer une réponse. Par conséquent, les requêtes synchrones prennent en moyenne plus de temps que les requêtes asynchrones vers `/users/track`. Pour la majorité des requêtes, vous pouvez vous attendre à une réponse en quelques secondes.

### Puis-je envoyer plusieurs requêtes en même temps ? {#can-i-send-multiple-requests-at-the-same-time}

Oui, à condition que les requêtes concernent des utilisateurs différents, ou que chaque requête mette à jour des attributs, des événements ou des achats différents pour un même utilisateur.

Si vous envoyez plusieurs requêtes pour un utilisateur, pour le même attribut, le même événement ou le même achat, Braze recommande d'attendre une réponse positive entre chaque requête afin d'éviter les conditions de concurrence.

### Pourquoi la valeur de la réponse ne correspond-elle pas à celle de ma requête initiale ? {#why-doesnt-the-response-value-match-the-one-in-my-original-request}

Bien que votre requête soit terminée, il est possible que la valeur de votre attribut personnalisé n'ait pas été mise à jour. Cela peut se produire lorsque la mise à jour de votre attribut personnalisé dépasse le nombre maximum de caractères, dépasse les limites du tableau, ou si l'utilisateur n'existe pas dans Braze et que vous avez défini `_update_existing_only = true`.

Dans ces cas, considérez la réponse comme une indication que, même si votre requête a bien été traitée, la mise à jour souhaitée n'a pas été effectuée. Procédez à la résolution des problèmes en vous référant aux raisons mentionnées ci-dessus.

{% endapi %}