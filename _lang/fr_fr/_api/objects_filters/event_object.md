---
nav_title: "Objet événement"
article_title: Objet événement de l'API
page_order: 6
page_type: reference
description: "Cet article de référence explique l'objet événement, ce qu'il est et en quoi il est essentiel dans les stratégies de Campaign basées sur les événements."

---

# Objet événement {#event-object}

> Cet article explique les différents composants d'un objet événement, comment vous pouvez l'utiliser et des exemples dont vous pouvez vous inspirer.

## Qu'est-ce qu'un objet événement ? {#what-is-an-event-object}

Un objet événement est un objet transmis via l'API lorsqu'un événement spécifique se produit. Les objets événement sont contenus dans un tableau d'événements. Chaque objet événement du tableau représente une occurrence unique d'un événement personnalisé par un utilisateur particulier à la valeur temporelle désignée. L'objet événement possède de nombreux champs différents qui vous permettent de personnaliser en définissant et en utilisant des propriétés d'événement dans les messages, la collecte de données et la personnalisation.

Pour les étapes de configuration des événements personnalisés pour une plateforme spécifique, consultez le guide d'intégration de plateforme dans le [guide du développeur]({{site.baseurl}}/developer_guide/home). Consultez l'article correspondant en fonction de votre plateforme :

- [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### Corps de l'objet {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

{% alert note %}
Les événements avec des horodatages dans le futur utilisent par défaut l'heure actuelle. Cela garantit que les événements personnalisés sont enregistrés avec un horodatage précis.
{% endalert %}

- [ID utilisateur externe]({{site.baseurl}}/api/basics#user-ids)
- [Identifiant d'application]({{site.baseurl}}/api/identifier_types)
- [Code temporel ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Certaines paires d'identifiants ne peuvent pas être utilisées ensemble dans une même requête. Lorsque `email` et `phone` sont tous deux fournis, `email` a la priorité sur `phone`. Pour plus de détails, consultez [Résolution des identifiants]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).
{% endalert %}

#### Mettre à jour uniquement les profils existants {#update-existing-profiles-only}

Pour mettre à jour uniquement les profils utilisateur existants dans Braze, vous devez transmettre la clé `_update_existing_only` avec la valeur `true` dans le corps de votre requête. Si cette valeur est omise, Braze créera un nouveau profil utilisateur si l'`external_id` n'existe pas déjà.

{% alert note %}
Si vous créez un profil utilisateur alias uniquement via l'endpoint `/users/track`, `_update_existing_only` doit être défini sur `false`. Si cette valeur est omise, le profil alias uniquement ne sera pas créé.
{% endalert %}

## Objet de propriétés d'événement {#event-properties-object}

Les événements personnalisés et les achats peuvent avoir des propriétés d'événement. Les valeurs de « properties » doivent être un objet dont les clés sont les noms des propriétés et les valeurs sont les valeurs des propriétés. Les noms de propriétés doivent être des chaînes de caractères non vides de 255 caractères ou moins, sans signe dollar ($) en début de chaîne.

Les valeurs de propriétés peuvent être de l'un des types de données suivants :

| Type de données | Description |
| --- | --- |
| Nombres | Sous forme d'[entiers](https://en.wikipedia.org/wiki/Integer) ou de [floats](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booléens | `true` ou `false` |
| Dates et heures | Doivent être formatées en tant que chaînes de caractères au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) ou dans l'un des formats suivants : <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Non pris en charge dans les tableaux. <br><br>Notez que « T » est un indicateur de temps, pas une marque substitutive, et ne doit pas être modifié ni supprimé. <br><br> Les attributs de temps sans fuseau horaire seront définis par défaut à minuit UTC (et seront formatés sur le tableau de bord comme l'équivalent de minuit UTC dans le fuseau horaire de l'entreprise). <br><br> Les événements avec des horodatages dans le futur seront définis par défaut à l'heure actuelle.  |
| Chaînes de caractères | 255 caractères ou moins. |
| Tableaux | Les tableaux ne peuvent pas contenir de dates et heures. |
| Objets | Les objets seront ingérés en tant que chaînes de caractères. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Objet de propriétés d'événement" }

Les objets de propriétés d'événement contenant des valeurs de type tableau ou objet peuvent avoir un payload de propriétés d'événement allant jusqu'à 100&nbsp;Ko.

### Clés réservées {#reserved-keys}

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisé :

- `time`
- `event_name`

{% alert important %}
L'utilisation de clés réservées comme noms de propriétés d'événement personnalisé entraînera des erreurs d'API lors de l'envoi de requêtes vers l'endpoint `/users/track`.
{% endalert %}

### Persistance des propriétés d'événement {#event-property-persistence}

Les propriétés d'événement sont conçues pour le filtrage et la personnalisation Liquid dans les messages déclenchés par leurs événements parents. Par défaut, elles ne sont pas conservées sur le profil utilisateur Braze. Pour utiliser les valeurs de propriétés d'événement dans la segmentation, consultez la section [événements personnalisés]({{site.baseurl}}/user_guide/data/activation/events/custom_events), qui détaille les différentes approches pour stocker les valeurs de propriétés d'événement à long terme.

#### Exemple de requête d'événement {#event-example-request}

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [Wiki sur le code temporel ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)

## Objets d'événement {#event-objects}

En utilisant l'exemple fourni, nous pouvons voir qu'une personne a récemment regardé une bande-annonce, puis a loué un film. Bien que nous ne puissions pas accéder à une Campaign et segmenter les utilisateurs en fonction de ces propriétés, nous pouvons les utiliser de manière stratégique sous la forme d'un reçu, pour envoyer un message personnalisé via un canal en utilisant Liquid. Par exemple : « Bonjour **Alex**, merci d'avoir loué **The Sad Egg** de **Alex Smith**, voici quelques films recommandés en fonction de votre location... »