---
nav_title: "POST : Suivre les utilisateurs (en masse) pour les partenaires Braze"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk_partners/
description: "Si vous êtes un partenaire Braze, utilisez cet endpoint pour enregistrer des événements personnalisés et des achats, et mettre à jour les attributs de profil utilisateur en masse."
---

{% api %}
# Suivre les utilisateurs (en masse) pour les partenaires Braze {#track-users-bulk-for-braze-partners}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Si vous êtes un partenaire Braze, utilisez cet endpoint pour enregistrer des événements personnalisés et des achats, et mettre à jour les attributs de profil utilisateur en masse.

{% alert important %}
Cet endpoint est disponible pour les partenaires Braze afin de migrer les cas d'utilisation en masse dans leur intégration Braze. Pour toute question, contactez [isv-support@braze.com](mailto:isv-support@braze.com).
{% endalert %}

## Quand utiliser cet endpoint {#when-to-use-this-endpoint}

Comme pour l'endpoint [POST : Suivre les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), vous pouvez utiliser cet endpoint pour mettre à jour les profils utilisateur. Cependant, cet endpoint est mieux adapté aux mises à jour en masse :

- **Requêtes plus volumineuses :** Cet endpoint permet jusqu'à 1 000 utilisateurs par requête, ce qui signifie que vous devez effectuer moins de requêtes pour répondre à vos besoins de mise à jour en masse.
- **Priorisation :** En cas de pic de trafic, les requêtes provenant de `/users/track` seront prioritaires par rapport aux requêtes provenant de `/users/track/bulk`. L'utilisation des deux endpoints vous offre un meilleur contrôle sur l'ingestion de données.

Envisagez d'utiliser cet endpoint lorsque vous remplissez de nombreux profils utilisateur lors de l'onboarding ou que vous synchronisez de grands volumes de profils utilisateur dans le cadre d'une synchronisation quotidienne.

{% alert note %}
Nous prévoyons de réduire la limite d'objets de `/users/track` de 225 à 5 afin d'encourager l'utilisation de `/users/track/bulk` à la place. Gardez cela à l'esprit pour vous assurer que votre intégration Braze reste compatible avec les futures mises à jour.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l'autorisation `users.track`. Cette autorisation donne accès à `/users/track` et `/users/track/bulk`.

Étant donné que la plupart de nos clients communs utilisent déjà une clé API avec les autorisations `users.track` pour leur intégration partenaire Braze, ils n'auront pas besoin de changer de clé API lorsque vous migrerez votre intégration vers `/users/track/bulk`.

Si vos clients utilisent l'API pour des appels serveur à serveur, ils devront peut-être ajouter l'endpoint à leur liste d'autorisation (par exemple, `rest.iad-01.braze.com`) si vous êtes derrière un pare-feu. Consultez les [endpoints par instance]({{site.baseurl}}/api/basics/#endpoints) pour plus d'informations.

## Limite de débit {#rate-limit}

Pour la plupart des clients, nous appliquons une limite de vitesse de base de 50 requêtes par seconde à cet endpoint.

Cependant, les clients disposant de contrats plus récents peuvent se voir attribuer une limite de débit en rafale (par seconde) et régulière (par heure), liée à leur nombre de MAU contractualisé avec Braze.

Pour améliorer les interactions en temps réel avec notre API, veillez à utiliser nos [en-têtes de réponse recommandés]({{site.baseurl}}/api/api_limits/#monitoring-your-rate-limits).

Chaque requête `/users/sync/bulk` a une limite de payload de 2&nbsp;Mo et peut contenir jusqu'à 1 000 objets d'événements, d'attributs ou d'achats.

Chaque objet (tableaux d'événements, d'attributs et d'achats) peut mettre à jour un utilisateur chacun, ce qui signifie qu'un maximum de 1 000 utilisateurs différents peuvent être mis à jour en une seule requête. Un seul profil utilisateur peut mettre à jour un maximum de 100 objets en une seule requête.

## Corps de la requête {#request-body}


```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Paramètres de la requête {#request-parameters}

{% alert important %}
Pour chaque composant de requête listé dans le tableau suivant, l'un des éléments suivants est requis : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Facultatif | Tableau d'objets d'attributs | Voir [objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Facultatif | Tableau d'objets d'événements | Voir [objet d'événements]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Facultatif | Tableau d'objets d'achats | Voir [objet d'achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemples de requêtes {#example-requests}

### Mise à jour en masse de 1 000 profils utilisateur en une seule requête {#bulk-update-1000-user-profiles-in-one-request}

Vous pouvez mettre à jour jusqu'à 1 000 profils utilisateur en utilisant l'endpoint `/users/track/bulk`. Voici un exemple tronqué où la requête se compose de 1 000 objets d'attributs :

```javascript
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",
            ]
        },

...

        {
            "external_id": "user1000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Voici un exemple où la requête se compose à la fois d'objets d'attributs et d'objets d'événements :

```javascript
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "external_id": "user2",
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
        },
...
        {
            "external_id": "user1000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

## Réponses {#responses}

### Messages réussis {#successful-messages}

Les messages réussis recevront la réponse suivante :

```javascript
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Message réussi avec des erreurs non fatales {#successful-message-with-non-fatal-errors}

Si votre message est réussi mais comporte des erreurs non fatales, comme un objet d'événement invalide dans une longue liste d'événements, vous recevrez la réponse suivante :

```javascript
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### Message avec des erreurs fatales {#message-with-fatal-errors}

Si votre message comporte une erreur fatale, vous recevrez la réponse suivante :

```javascript
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

#### Codes de réponse pour les erreurs fatales {#fatal-error-response-codes}

Pour les codes d'état et les messages d'erreur associés qui seront renvoyés si votre requête rencontre une erreur fatale, consultez [Erreurs fatales et réponses]({{site.baseurl}}/api/errors/#fatal-errors).

Si vous recevez l'erreur `provided external\_id is blacklisted and disallowed`, votre requête peut avoir inclus un `dummy user.` Pour plus d'informations, consultez [Blocage du spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Questions fréquentes {#frequently-asked-questions}

### Dois-je utiliser cet endpoint ou `/users/track` ? {#should-i-use-this-endpoint-or-userstrack}

Nous recommandons d'utiliser les deux.

- Pour les remplissages et synchronisations de profils utilisateur en masse, utilisez l'endpoint `/users/track/bulk`.
- Pour les cas d'utilisation en temps réel, utilisez l'endpoint `/users/track`.

{% alert note %}
Nous prévoyons de réduire la limite d'objets de `/users/track` de 225 à 5 afin d'encourager l'utilisation de `/users/track/bulk` à la place. Gardez cela à l'esprit pour vous assurer que votre intégration Braze reste compatible avec les futures mises à jour.
{% endalert %}

### Quels identifiants puis-je utiliser dans `/users/track/bulk` ? {#what-identifiers-can-i-use-in-userstrackbulk}

L'un des éléments suivants est requis : `external\_id`, `braze\_id`, `user\_alias`, `email` ou `phone`. Consultez notre documentation pour l'[objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/), l'[objet d'événements]({{site.baseurl}}/api/objects_filters/event_object/) ou l'[objet d'achats]({{site.baseurl}}/api/objects_filters/purchase_object/) pour d'autres exemples.

### Puis-je inclure des attributs, des événements et des achats dans une seule requête ? {#can-i-include-attributes-events-and-purchases-in-one-request}

Oui. Vous pouvez construire votre requête avec n'importe quelle quantité d'objets d'attributs, d'événements et d'achats, dans la limite de 1 000 objets par requête.

{% endapi %}