---
nav_title: Connecteur Currents personnalisé
alias: /currents_connector/
hidden: true
---

# Connecteur Currents personnalisé {#custom-currents-connector}

> Découvrez comment intégrer un connecteur Currents personnalisé afin d'obtenir des données d'événements de Braze en temps réel, ce qui permet de réaliser des analyses plus personnalisées, de créer des rapports et de mettre en place des automatisations.

## Conditions préalables {#prerequisites}

Pour intégrer un connecteur Currents personnalisé dans Braze, vous devrez fournir une URL d'endpoint et un [jeton d'authentification facultatif](#authentication).

En outre, si vous avez plusieurs groupes d'applications dans Braze, vous devrez configurer un connecteur Currents personnalisé pour chaque groupe. Cependant, vous pouvez faire pointer tous les groupes d'applications vers le même endpoint, ou vers un endpoint avec un paramètre `GET` supplémentaire, tel que `your_app_group_key="Brand A"`.

## Prévenir la perte de données {#preventing-data-loss}

### Surveillance des erreurs {#error-monitoring}

Pour éviter les pertes de données et les interruptions de service, il est essentiel que vous surveilliez vos endpoints en permanence et que vous vous efforciez de remédier aux erreurs matérielles ou aux temps d'arrêt dans les 24 heures.

Pour la plupart des types d'erreurs (erreurs de serveur, erreurs de connexion réseau, etc.), Braze continue à mettre en file d'attente et à réessayer les transmissions d'événements pendant 24 heures. Passé ce délai, les événements non transmis seront abandonnés. Les connecteurs dont le taux d'erreur ou la disponibilité sont constamment médiocres seront automatiquement suspendus.

### Résilience aux changements {#change-resilience}

De temps à autre, nous apportons des modifications non radicales aux schémas de Braze Currents. Les modifications non radicales sont de nouvelles colonnes nullables ou de nouveaux types d'événements.

Nous donnons généralement un préavis de deux semaines pour ces changements, mais cela n'est pas toujours possible. Il est essentiel que vous conceviez votre intégration de manière à gérer les champs ou les types d'événements non reconnus, faute de quoi vous risquez de perdre des données.

{% alert tip %}
Pour la liste complète des schémas d'événements Currents, consultez [Événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).
{% endalert %}

## Mise en lots et sérialisation {#batching-and-serialization}

Le format de données cible est JSON sur HTTPS. Par défaut, les événements sont regroupés par lots de 100 en fonction des critères suivants :

- **Nombre d'événements en file d'attente** : par exemple, si la taille du lot est configurée pour 200 événements et qu'il y a 200 événements dans la file d'attente.
- **Durée d'un événement** : en règle générale, les événements ne sont pas mis en file d'attente s'ils durent plus de 15 minutes. Chaque type d'événement dispose d'une file d'attente distincte, de sorte que la latence peut varier d'un type d'événement à l'autre.

Les événements sont ensuite envoyés à l'endpoint sous la forme d'un tableau JSON de tous les événements au format suivant :

```json
{"events": [event1, event2, event3, etc...]}
```

Il y aura un objet JSON de premier niveau avec la clé `"events"` qui correspond à un tableau d'objets JSON supplémentaires, chacun représentant un seul événement.

## Exemples de payloads {#payload-examples}

Les exemples suivants montrent des payloads pour des événements individuels, ce qui signifie que les payloads appartiendraient à un tableau d'objets JSON plus large, où chaque objet JSON représenterait un seul événement dans le lot.

En outre, leur structure diffère légèrement de la structure plate que l'on trouve dans les [événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). En particulier, ils contiennent deux sous-objets :

| Nom | Description |
|----|-----------|
| `"user"` | Contient des propriétés utilisateur telles que `user_id`, `external_user_id`, `device_id` et `timezone`. |
| `"properties"` | Contient les attributs d'un événement, tels que le `app/campaign/canvas/platform` auquel il s'applique. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Payload examples" }

Si un endpoint en aval reçoit un payload avec zéro événement ou un corps de requête vide, le résultat doit être considéré comme un no-op, ce qui signifie qu'aucun effet en aval ne doit résulter de cet appel. Cependant, vous devez toujours vérifier l'en-tête `Authorization` (comme vous le feriez pour un appel API normal) et fournir une réponse HTTP appropriée en cas d'[informations d'identification non valides](#authentication), telle que `401` ou `403`. Cela permet à Braze de savoir que les informations d'identification du connecteur sont valides.

### Événements associés à une campagne {#campaign-associated-events}

Voici quelques exemples de payloads pour différents événements, tels qu'ils apparaîtraient s'ils étaient associés à une campagne :

#### Clic sur un message in-app {#in-app-message-click}

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Envoi de notification push {#push-notification-send}

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### Ouverture d'e-mail {#email-open}

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### Réception SMS {#sms-delivery}

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Événements associés à un Canvas {#canvas-associated-events}

Voici quelques exemples de payloads pour différents événements, tels qu'ils apparaîtraient s'ils étaient associés à un Canvas :

#### Clic sur un message in-app

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Envoi de notification push

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### Ouverture d'e-mail

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### Réception SMS

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Autres événements {#other-events}

Voici quelques exemples de payloads pour divers autres événements qui ne sont associés ni à des campagnes ni à des Canvas :

#### Événement personnalisé {#custom-event}

```json
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Événement d'achat {#purchase-event}

```json
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Début de session {#session-start}

```json
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Authentification {#authentication}

Les jetons d'authentification dans votre payload sont facultatifs. Ils peuvent être transmis via un en-tête HTTP `Authorization` en utilisant le schéma d'autorisation `Bearer`, comme spécifié dans la [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Bien que facultatif, si un jeton d'authentification est transmis, Braze le validera toujours en premier&#8212;même si aucun événement ne figure dans le payload.

Conformément à la RFC 6750, les jetons doivent être des valeurs encodées en Base64 comportant au moins un caractère. N'oubliez pas que la RFC 6750 autorise les jetons à contenir les caractères suivants en plus des caractères Base64 normaux : `-`, `.`, `_` et `~`. Vous pouvez choisir d'inclure ou non ces caractères dans votre jeton&#8212;cependant, celui-ci doit être au format Base64.

De plus, si l'en-tête `Authorization` est présent, il sera construit selon le format suivant :

```plaintext
"Authorization: Bearer " + <token>
```

Par exemple, si votre jeton d'authentification est `0p3n5354m3==`, votre en-tête `Authorization` devrait ressembler à ce qui suit :

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
À l'avenir, nous pourrons utiliser les en-têtes `Authorization` pour mettre en œuvre un schéma d'autorisation personnalisé, basé sur des paires clé-valeur, propre à Braze. Cela respecterait la spécification [RFC 7235](https://tools.ietf.org/html/rfc7235), qui est la manière dont certaines entreprises implémentent leurs schémas d'authentification, comme Amazon Web Services (AWS).
{% endalert %}

## Versionnage {#versioning}

Toutes les requêtes provenant de l'intégration de notre connecteur HTTP seront envoyées avec un en-tête personnalisé désignant la version de la requête Currents effectuée :

```plaintext
Braze-Currents-Version: 1
```

La version sera toujours `1`, car nous ne prévoyons pas d'incrémenter ce nombre très souvent, voire jamais.

Tout comme les [schémas de stockage de nos entrepôts de données]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), chaque champ d'un événement individuel est garanti comme étant rétrocompatible avec les versions précédentes du payload de l'événement, conformément à la définition de la rétrocompatibilité d'[Apache Avro](https://avro.apache.org/) :

1. Il est garanti que les champs d'événements spécifiques auront toujours le même type de données au fil du temps.
2. Tous les nouveaux champs ajoutés au payload au fil du temps doivent être considérés comme facultatifs par toutes les parties.
3. Les champs requis ne seront jamais supprimés.

## Gestion des erreurs et mécanisme de nouvelle tentative {#error-handling-and-retry-mechanism}

En cas d'erreur, Braze met la requête en file d'attente et la relance en fonction du code de retour HTTP reçu. Les tentatives se poursuivent pendant au moins deux jours, tant que des données sont stockées dans la mémoire tampon du système. Si les données restent bloquées pendant plus de 24 heures, nos ingénieurs d'astreinte seront automatiquement alertés. Pour l'instant, notre stratégie de repli consiste à réessayer périodiquement.

Si votre intégration Currents commence à renvoyer des erreurs `4XX`, Braze vous enverra automatiquement un e-mail de notification et prolongera automatiquement la période de conservation à un minimum de sept jours.

Tout code d'erreur HTTP non répertorié ci-dessous sera traité comme une erreur HTTP `5XX`.

{% alert warning %}
Si le mécanisme de relance de Braze ne parvient pas à livrer un événement pendant plus de 24 heures, il y aura perte de données.
{% endalert %}

Les codes d'état HTTP suivants seront reconnus par notre client de connecteur :

<table aria-label="Error handling and retry mechanism">
  <caption>Gestion des erreurs et mécanisme de nouvelle tentative</caption>
  <thead>
    <tr>
      <th>Code d'état</th>
      <th>Réponse</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Réussi</td>
      <td>Les données relatives à l'événement ne seront pas renvoyées.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Erreur côté serveur</td>
      <td>Les données des événements seront renvoyées selon un schéma de délais exponentiels avec variation aléatoire. Si les données ne sont pas envoyées avec succès dans les 24 heures, elles seront supprimées.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Erreur côté client</td>
      <td>Le connecteur a envoyé au moins un événement malformé. Les données relatives à l'événement seront divisées en lots de taille 1 et renvoyées. Tous les événements de ces lots de taille 1 qui reçoivent une autre réponse <code>400</code> seront définitivement abandonnés. Vous devez signaler les occurrences répétées.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Non autorisé</td>
      <td>Le connecteur a été configuré avec des informations d'identification non valides. Les données relatives à l'événement seront renvoyées après un délai de 2 à 5 minutes. Si le problème n'est pas résolu dans les 48 heures, les données de l'événement seront supprimées.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Interdit</td>
      <td>Le connecteur a été configuré avec des informations d'identification non valides. Les données relatives à l'événement seront renvoyées après un délai de 2 à 5 minutes. Si le problème n'est pas résolu dans les 48 heures, les données de l'événement seront supprimées.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Introuvable</td>
      <td>Le connecteur a été configuré avec des informations d'identification non valides. Les données relatives à l'événement seront renvoyées après un délai de 2 à 5 minutes. Si le problème n'est pas résolu dans les 48 heures, les données de l'événement seront supprimées.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Payload trop volumineux</td>
      <td>Les données relatives à l'événement seront divisées en lots plus petits et renvoyées.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Trop de requêtes</td>
      <td>Indique une limite de débit. Les données des événements seront renvoyées selon un schéma de délais exponentiels avec variation aléatoire. Si elles ne sont pas envoyées avec succès dans les 24 heures, elles seront abandonnées.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Error handling and retry mechanism" }