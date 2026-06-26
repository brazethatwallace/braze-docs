---
nav_title: "POST : Créer et mettre à jour des utilisateurs (en masse)"
article_title: "POST : Créer et mettre à jour des utilisateurs (en masse)"
search_tag: Endpoint
page_order: 4.25
layout: api_page
page_type: reference
alias:
  - /unlisted_docs/track_users_bulk_partners/
  - /api/endpoints/user_data/post_user_track_bulk_partners/
description: "Cet article décrit en détail l'endpoint de suivi des utilisateurs en masse."
---
{% api %}
# Créer et mettre à jour des utilisateurs (en masse) {#create-and-update-users-bulk}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

Utilisez cet endpoint pour enregistrer des événements personnalisés et des achats, et mettre à jour les attributs de profils utilisateur en masse.

{% alert important %}
Cet endpoint est actuellement en **bêta limitée**. Bien que nous n'ajoutions pas de nouveaux clients à la bêta pour le moment, faites savoir à votre gestionnaire de compte Braze si vous pensez que cette fonctionnalité pourrait être utile pour votre intégration Braze.
{% endalert %}

## Quand utiliser cet endpoint {#when-to-use-this-endpoint}

Comme l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez utiliser cet endpoint pour mettre à jour les profils utilisateur. Cet endpoint est mieux adapté aux mises à jour en masse :

- **Requêtes plus volumineuses :** Envoyez jusqu'à 1 000 utilisateurs par requête, ce qui vous permet de faire moins de requêtes pour les remplissages et synchronisations importants.
- **Priorisation :** En cas de pic de trafic, les requêtes vers `/users/track` sont prioritaires par rapport aux requêtes vers `/users/track/bulk`.

Utilisez cet endpoint lorsque vous remplissez de nombreux profils utilisateur lors de l'onboarding, ou que vous synchronisez de grands volumes de profils dans le cadre d'une synchronisation quotidienne.

{% alert note %}
Les limites de l'objet de requête de l'endpoint `/users/track` varient en fonction du modèle de tarification et de la configuration. Utilisez `/users/track/bulk` pour l'ingestion en masse.
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous devez disposer d'une [clé API]({{site.baseurl}}/api/api_key/) avec la permission `users.track.bulk`.

Si vous effectuez des appels serveur à serveur derrière un pare-feu, vous devrez peut-être ajouter votre endpoint REST Braze à votre liste d'autorisation (par exemple, `rest.iad-01.braze.com`). Pour plus d'informations, consultez [Endpoints API]({{site.baseurl}}/api/basics/#api-definitions).

## Limite de débit {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/bulk" %}

Pour la plupart des clients, cet endpoint a une limite de vitesse de base de 50 requêtes par seconde.

Les clients disposant de contrats plus récents peuvent avoir des limites en rafale (par seconde) et régulières (par heure) basées sur le nombre d'utilisateurs actifs par mois contractualisé.

Chaque requête `/users/track/bulk` a une limite de payload de 2 Mo et peut inclure jusqu'à 1 000 objets au total entre les attributs, les événements et les achats, en fonction de la politique de limite de débit en masse de votre compte.

Chaque objet peut mettre à jour un utilisateur, de sorte qu'une seule requête peut mettre à jour jusqu'à la limite d'objets de requête de votre compte pour différents utilisateurs. De plus, chaque requête peut contenir un maximum de 100 objets par profil utilisateur entre les attributs, les événements et les achats.

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object)
}
```

### Paramètres de la requête {#request-parameters}

{% alert important %}
Pour chaque objet de requête, vous devez inclure l'un des éléments suivants : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Paramètre | Requis | Type de données | Description |
| --- | --- | --- | --- |
| `attributes` | Facultatif | Tableau d'objets d'attributs | Voir [objet d'attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Facultatif | Tableau d'objets d'événements | Voir [objet d'événements]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Facultatif | Tableau d'objets d'achats | Voir [objet d'achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de la requête" }

## Exemples de requêtes {#example-requests}

### Mettre à jour des profils utilisateur en masse dans une seule requête {#bulk-update-user-profiles-in-one-request}

Mettez à jour jusqu'à la limite d'objets de requête de votre compte de profils utilisateur en une seule requête.

```
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
        "asparagus"
      ]
    }
  ]
}'
```

### Envoyer des attributs et des événements dans une seule requête {#send-attributes-and-events-in-one-request}

Incluez des attributs et des événements dans la même requête, jusqu'à la limite totale d'objets de votre compte.

```
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
    }
  ]
}'
```

## Réponses {#responses}

### Message de réussite {#successful-message}

Les messages de réussite renvoient la réponse suivante :

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}
```

### Message de réussite avec des erreurs non fatales {#successful-message-with-non-fatal-errors}

Si votre requête aboutit mais comporte des erreurs non fatales (par exemple, un objet d'événement invalide dans un lot volumineux), vous recevez la réponse suivante :

```json
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

Si votre requête comporte une erreur fatale, vous recevez la réponse suivante :

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

### Codes de réponse pour les erreurs fatales {#fatal-error-response-codes}

Pour les codes d'état et les messages d'erreur associés que Braze renvoie lorsque votre requête comporte une erreur fatale, consultez [Erreurs fatales et réponses]({{site.baseurl}}/api/errors/#fatal-errors).

Si vous recevez l'erreur « provided external_id is blacklisted and disallowed », votre requête peut inclure un « utilisateur fictif ». Pour plus d'informations, consultez [Blocage du spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Questions fréquemment posées {#frequently-asked-questions}

### Dois-je utiliser cet endpoint ou `/users/track` ? {#should-i-use-this-endpoint-or-userstrack}

Utilisez les deux endpoints en fonction de votre cas d'utilisation :

- Pour les remplissages et synchronisations volumineux, utilisez `/users/track/bulk`.
- Pour les cas d'utilisation en temps réel, utilisez `/users/track`.

### Quels identifiants puis-je utiliser dans `/users/track/bulk` ? {#what-identifiers-can-i-use-in-userstrackbulk}

Pour chaque objet de requête, incluez l'un des éléments suivants : `external_id`, `braze_id`, `user_alias`, `email` ou `phone`.

### Puis-je inclure des attributs, des événements et des achats dans une seule requête ? {#can-i-include-attributes-events-and-purchases-in-one-request}

Oui. Incluez n'importe quelle combinaison d'attributs, d'événements et d'achats, jusqu'à la limite combinée d'objets de requête de votre compte.

{% endapi %}