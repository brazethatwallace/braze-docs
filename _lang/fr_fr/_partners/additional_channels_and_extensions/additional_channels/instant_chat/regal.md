---
nav_title: Regal
article_title: Regal
description: "Cet article de référence décrit le partenariat entre Braze et Regal, une plateforme d'agents Voice AI qui vous aide à orchestrer des parcours clients personnalisés et omnicanaux en utilisant les données Braze et les conversations Regal."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) est une plateforme d'agents Voice AI qui aide les entreprises à offrir de meilleures expériences client grâce à des conversations intelligentes et en temps réel sur l'ensemble des canaux.

_Cette intégration est maintenue par Regal._

En intégrant Regal à Braze, vous pouvez unifier les données comportementales et l'intelligence artificielle conversationnelle pour orchestrer des parcours clients personnalisés et omnicanaux. Braze capture les signaux tout au long du cycle de vie client, que Regal utilise pour alimenter les conversations des agents IA, le routage et les décisions en temps réel.

Utilisez les données Braze pour façonner ce que vos agents IA disent, comment ils répondent et quand interagir. Renvoyez les résultats et les informations des conversations vers Braze pour améliorer le ciblage et le marketing du cycle de vie. Déclenchez des appels et des SMS alimentés par l'IA à des moments clés du parcours client, et effectuez un suivi dans Braze en fonction de ce qui se passe dans chaque conversation.

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Regal | Un compte Regal est requis pour profiter de ce partenariat. |
| Clé API Regal | Une clé API Regal vous permet d'envoyer des événements de Braze à Regal.<br><br>Envoyez un e-mail à [support@regal.io](mailto:support@regal.io) pour obtenir cette clé. |
| Transformation des données Braze | Une [Transformation des données]({{site.baseurl}}/data_transformation) est requise pour recevoir des données de Regal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration : envoi de données de Braze à Regal {#integration-sending-data-from-braze-to-regal}

Utilisez les webhooks de Canvas ou de Campaign Braze pour envoyer les données de profil client et d'événements de Braze à Regal.

### Étape 1 : Créer de nouveaux contacts dans Regal {#step-1-create-new-contacts-in-regal}

Créez un Canvas ou une Campaign qui envoie des webhooks à Regal chaque fois que vous créez un nouveau profil Braze qui doit être disponible pour des appels et des SMS dans Regal.

1. Créez un Canvas ou une Campaign intitulé(e) « Créer un nouveau contact pour Regal » et sélectionnez **Basé sur l'action** comme type d'entrée.

2. Définissez la logique du déclencheur comme **Événement personnalisé**, puis sélectionnez l'événement qui se déclenche lorsqu'un profil avec un numéro de téléphone est créé. Regal recommande également d'ajouter un filtre pour confirmer que le champ téléphone est défini.

3. Dans votre nouveau modèle de webhook, remplissez les champs suivants :
   - **Webhook URL** : <https://events.regalvoice.com/events>
   - **Request Body** : Raw Text

#### En-têtes de requête et méthode {#request-headers-and-method}

Regal nécessite également un en-tête HTTP pour l'autorisation et une méthode HTTP. Les éléments suivants sont inclus dans le modèle en tant que paires clé-valeur dans l'onglet **Settings** :
{% raw %}
- **HTTP Method** : POST
- **Request Headers** :
    - **Authorization** : `{{<REGAL_API_KEY>}}`
    - **Content-Type** : application/json
{% endraw %}

#### Corps de la requête {#request-body}

Le seul identifiant requis est un numéro de téléphone à l'intérieur de `traits.phones`. Utilisez l'objet `traits.phones` pour associer un ou plusieurs numéros de téléphone à un contact. Chaque numéro de téléphone peut stocker son propre libellé, sa désignation principale, ainsi que son statut d'abonnement vocal et SMS. Cette structure est particulièrement utile lorsqu'un contact possède plusieurs numéros de téléphone.

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "custom1": "<custom1>",
    "custom2": "<custom2>"
  },
  "eventSource": "braze"
}
```

L'exemple de payload ci-dessus suppose que les numéros de téléphone listés incluent le statut actuel de consentement vocal et SMS. Si ce n'est pas le cas, vous pouvez omettre `voiceOptIn` et `smsOptIn` lors de la création du contact et configurer un Canvas ou une Campaign séparé(e) pour mettre à jour le consentement sur le numéro de téléphone concerné lorsque l'abonnement est collecté.

### Étape 2 : Mettre à jour les informations d'abonnement {#step-2-update-opt-in-information}

Si l'abonnement et le désabonnement peuvent se produire à différents moments dans votre application, mettez à jour Regal lorsque les utilisateurs changent leur statut d'abonnement.

Regal recommande d'utiliser le schéma `traits.phones` afin de pouvoir gérer l'abonnement et le désabonnement par numéro de téléphone, plutôt qu'au niveau du contact.

Utilisez la configuration Canvas suivante pour envoyer des informations d'abonnement à jour à Regal.

1. Créez un nouveau Canvas ou une nouvelle Campaign intitulé(e) « Envoyer l'abonnement ou le désabonnement à Regal ».

2. Sélectionnez l'une des options de déclencheur suivantes, puis sélectionnez le champ qui représente le statut d'abonnement de l'utilisateur :
    - **Champ de profil utilisateur mis à jour**
    - **Mettre à jour le statut du groupe d'abonnement**
    - **Statut de l'abonnement**

3. Dans votre nouveau modèle de webhook, remplissez les champs suivants :
   - **Webhook URL** : <https://events.regalvoice.com/events>
   - **Request Body** : Raw Text

#### En-têtes de requête et méthode

Regal nécessite également un en-tête HTTP pour l'autorisation et une méthode HTTP. Les éléments suivants sont inclus dans le modèle en tant que paires clé-valeur dans l'onglet **Settings** :
{% raw %}
- **HTTP Method** : POST
- **Request Headers** :
    - **Authorization** : `{{<REGAL_API_KEY>}}`
    - **Content-Type** : application/json
{% endraw %}

#### Corps de la requête

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<phoneNumber>": {
        "voiceOptIn": {
          "subscribed": "<voice_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": "<sms_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    }
  },
  "eventSource": "braze"
}
```

Vous pouvez également inclure des attributs de profil utilisateur supplémentaires dans ce payload pour maintenir d'autres attributs à jour en même temps.

### Étape 3 : Envoyer des événements personnalisés {#step-3-send-custom-events}

Configurez un Canvas ou une Campaign pour chaque événement clé que vous souhaitez envoyer à Regal.

Ces événements font plus que déclencher des actions de communication (par exemple, un SMS de confirmation lorsqu'un prospect termine son inscription). Ils fournissent le contexte en temps réel qui alimente la façon dont les agents IA de Regal parlent, prennent des décisions et routent les conversations tout au long du parcours client. En envoyant les données d'événements et les attributs depuis Braze, vous permettez aux agents IA d'adapter les conversations en fonction du comportement, des préférences et de l'étape du cycle de vie de chaque utilisateur.

Par exemple, les événements et attributs Braze peuvent être utilisés dans Regal pour :

- **Personnaliser le discours de l'agent IA** : référencer le comportement récent ou l'intérêt produit directement dans les conversations.
  - Exemple : si un utilisateur a exploré des options d'assurance vie, l'agent peut référencer `contact.firstName` et `contact.brazeProductInterest` dans la conversation.
- **Piloter une logique de conversation dynamique** : ajuster ce que l'agent priorise en temps réel.
  - Exemple : si `contact.brazeAge` est supérieur à 65, prioriser la couverture Medicare ; sinon, se concentrer sur les plans ACA et le statut d'assurance actuel.
- **Permettre un routage et une escalade intelligents** : router les conversations en fonction de la valeur ou de l'intention.
  - Exemple : si `contact.brazeLeadTier` est « High Value », transférer à un agent senior après qualification ; sinon, continuer avec l'agent IA.
- **Aligner les messages et les offres** : adapter ce que l'agent présente en fonction du contexte de la Campaign.
  - Exemple : si `contact.brazeCampaignName` est « Spring Mortgage Promo », mettre en avant l'offre promotionnelle pendant la conversation.

Créez un nouveau Canvas ou une nouvelle Campaign intitulé(e) « Envoyer l'événement d'intérêt produit à Regal ».

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "brazeProductInterest": "Life Insurance",
    "brazeAge": 68,
    "brazeLeadTier": "High Value",
    "brazeCampaignName": "Spring Insurance Promo"
  },
  "name": "Product Interest Captured",
  "properties": {
    "action": "Viewed Product Comparison",
    "productCategory": "Life Insurance",
    "intentScore": "High",
    "lastPage": "Compare Life Insurance Plans",
    "readyToCommit": true
  },
  "eventSource": "braze"
}
```

#### Attributs de contact à jour {#up-to-date-contact-attributes}

Regal recommande également d'envoyer les attributs clés du profil utilisateur dans les payloads d'événements afin que Regal dispose d'attributs de contact à jour lorsque des événements clés se produisent.

{% alert note %}
Si vous avez des questions sur les événements à envoyer à Regal ou sur la façon de configurer ces Canvas et Campaigns, envoyez un e-mail à [support@regal.io](mailto:support@regal.io).
{% endalert %}

## Intégration : envoi de données de Regal à Braze {#integration-sending-data-from-regal-to-braze}

Utilisez les webhooks de reporting Regal et la Transformation des données Braze pour envoyer les événements de reporting Regal (tels que `SMS.sent` et `call.completed`) à Braze. Une fois ces événements mappés, ils apparaissent sur les profils utilisateur et sont disponibles pour la segmentation, les Canvas et les Campaigns.

### Étape 1 : Créer une Transformation des données dans Braze {#step-1-create-a-data-transformation-in-braze}

Créez une Transformation des données pour chaque webhook Regal que vous prévoyez d'envoyer à Braze.

Pour créer une Transformation des données :
1. Accédez à la page **Transformations** dans votre tableau de bord de Braze.
2. Donnez un nom à votre transformation et cliquez sur **Create transformation**.
3. Dans la liste des transformations, sélectionnez <i class="fa-solid fa-ellipsis-vertical" title="Afficher les actions"></i> **View actions** et sélectionnez **Copy webhook URL**.

### Étape 2 : Activer les webhooks de reporting dans Regal {#step-2-enable-reporting-webhooks-in-regal}

Pour configurer les webhooks de reporting :
1. Accédez à l'application Regal et ouvrez la page **Settings**.

2. Dans la section **Reporting Webhooks**, cliquez sur **Create Webhooks**.

3. Dans le champ de saisie de l'endpoint du webhook, ajoutez l'URL du webhook de Transformation des données Braze pour la transformation associée.

#### Mise à jour d'un endpoint {#updating-an-endpoint}

Lorsque vous modifiez un endpoint, cela peut prendre jusqu'à 5 minutes pour que le cache s'actualise et envoie les événements à votre nouvel endpoint.

#### Nouvelles tentatives {#retries}

Actuellement, Regal ne retente pas ces événements. Si Braze ne répond pas dans les 5 secondes, Regal abandonne l'événement. Regal prévoit d'ajouter les nouvelles tentatives dans une future version.

#### Événements {#events}
Pour la liste complète des événements de reporting, les définitions des propriétés et des exemples de payloads, consultez le [guide des webhooks de reporting](https://developer.regal.io/docs/reporting-webhooks#events) de Regal.

### Étape 3 : Transformer les événements Regal en événements Braze {#step-3-transform-regal-events-into-braze-events}

La fonctionnalité de [Transformation des données]({{site.baseurl}}/data_transformation) de Braze vous permet de mapper les événements Regal entrants dans le format nécessaire pour les ajouter en tant qu'attributs, événements ou achats dans Braze.

1. Nommez votre Transformation des données. Il est recommandé de configurer une Transformation des données par webhook d'événement.

2. Pour tester la connexion, créez un appel sortant depuis le bureau de l'agent Regal vers votre téléphone et soumettez le formulaire de résumé de conversation pour créer un événement `call.completed`.

3. Déterminez quels identifiants vous utiliserez pour mapper vos contacts Regal à vos profils Braze. Les identifiants disponibles dans les événements Regal incluent :
   - `userId` — uniquement défini sur les événements si vous avez déjà envoyé cet identifiant pour un contact
   - `traits.phone`
   - `traits.email` — uniquement défini sur les événements si vous avez déjà envoyé cet identifiant pour un contact

Dans les payloads d'événements de Braze vers Regal, Regal recommande d'utiliser `traits.phones` pour prendre en charge plusieurs numéros de téléphone et le consentement au niveau du numéro. Dans les événements de reporting Regal renvoyés à Braze, `traits.phone` peut toujours apparaître comme identifiant dans les payloads d'événements.

#### Identifiants pris en charge par Braze {#braze-supported-identifiers}
- Braze ne prend pas en charge les numéros de téléphone comme identifiant. Pour l'utiliser comme identifiant, le numéro de téléphone peut être défini comme [alias d'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) dans Braze.
- Lors de l'utilisation de la Transformation des données Braze, l'adresse e-mail peut être utilisée comme identifiant. Si l'adresse e-mail existe en tant que profil dans Braze, le profil existant sera mis à jour. Si l'adresse e-mail n'existe pas encore dans Braze, un profil uniquement e-mail sera créé.

## Cas d'utilisation {#use-cases}

{% tabs %}
{% tab Déclencher un e-mail %}

**Déclencher un e-mail depuis Braze en fonction d'une disposition d'appel dans Regal**

Voici un exemple de payload pour un événement `call.completed` dans Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Alex",
    "agent_fullname": "Alex Lee",
    "agent_id": "xxxx@example.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+15555550200",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+15555550123",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

Voici un exemple de Transformation des données pour mapper cela à un événement personnalisé dans Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Mettre à jour les attributs de profil %}

**Mettre à jour les attributs de profil dans Braze en fonction des événements `contact.attribute.edited` de Regal**

Voici un exemple de payload pour un événement `contact.attribute.edited` dans Regal. Regal envoie cet événement lorsqu'un agent met à jour un attribut sur le profil d'un contact pendant une conversation.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@example.com",
    "contact_phone": "+15555550123",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

Voici un exemple de Transformation des données pour mapper les nouvelles valeurs de propriété personnalisée aux attributs pertinents de vos profils Braze :

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Synchroniser vos expériences %}

**Gardez vos expériences dans Braze et Regal synchronisées en utilisant les événements `contact.experiment.assigned`**

Voici un exemple de payload pour un événement `contact.experiment.assigned` dans Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

Voici un exemple de Transformation des données pour mapper cela à un événement personnalisé dans Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Désabonner un contact %}

**Désabonner un contact dans Braze en fonction des événements `contact.unsubscribed` de Regal**

Voici un exemple de payload pour un événement `contact.unsubscribed` dans Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Voici un exemple de Transformation des données pour désabonner le contact dans Braze.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Déclencher un suivi à partir de l'analyse d'appel %}

**Déclencher des parcours de suivi personnalisés dans Braze en fonction des événements `call.analysis.available` de Regal**

Utilisez l'événement `call.analysis.available` de Regal pour identifier la raison principale pour laquelle un client n'a pas converti et déclencher un parcours de suivi personnalisé dans Braze.

Par exemple :

- Lorsque l'objection principale est le prix, envoyez un e-mail de suivi axé sur la valeur.
- Lorsque l'objection principale est le timing, placez l'utilisateur dans une séquence de nurturing pour une reconsidération ultérieure.
- Lorsque l'objection principale est la confiance, envoyez des témoignages, des évaluations ou des garanties de conformité.
- Lorsque `needs_human_agent` est vrai, notifiez une équipe commerciale ou de support et supprimez les messages automatisés ultérieurs.

Voici un exemple de payload pour un événement `call.analysis.available` dans Regal.

```json
{
  "traits": {
    "phone": "+1XXXXXXXXXX",
    "email": "xxx@example.com"
  },
  "name": "call.analysis.available",
  "brand": "circle-bank",
  "contact_email": "xxx@example.com",
  "contact_phone": "+1XXXXXXXXXX",
  "created_at": "1754079836",
  "entity_type": "event",
  "event_id": "9f5d8dbb2973b0e2359c6fd34111111",
  "event_type": "regal_voice_event",
  "external_id": "41dd1aa2-1111-f011-a2d5-00505611111",
  "original_timestamp": "1754079835",
  "profile_id": "62653af1111111173af128291e92",
  "properties": {
    "agent_email": "xxx@example.com",
    "call_analysis": {
      "purchase_intent": "medium",
      "primary_objection": "price",
      "secondary_objection": "needs_to_compare",
      "product_interest": "Life Insurance",
      "follow_up_required": true,
      "follow_up_email_text": "Thanks for speaking with us today. I know cost is top of mind, so I wanted to send over a simple summary of the life insurance options we discussed and what may fit your budget.",
      "recommended_next_action": "send_value_oriented_follow_up",
      "needs_human_agent": false,
      "customer_sentiment_label": "interested_but_hesitant"
    },
    "contact_phone": "+1XXXXXXXXXX",
    "incoming_sip_headers": {
      "Via": "SIP/2.0/UDP srv1.example.com;branch=z9hG4bK776asdhds",
      "From": "<sip:customer@example.com>;tag=1928301774",
      "Call-ID": "a84b4c76e66710"
    },
    "is_ai_agent": true,
    "outgoing_sip_headers": {
      "Via": "SIP/2.0/TCP srv2.example.com;branch=z9hG4bKgsdh7723",
      "To": "<sip:agent@example.com>",
      "User-Agent": "RegalVoiceAI/1.0"
    },
    "task_id": "WT7f3ea47fa6e6055aa847f0a62111111"
  },
  "originalTimestamp": "1754079835",
  "source": "Regal Voice"
}
```

Utilisez une Transformation des données pour mapper les champs `call_analysis` (tels que `primary_objection` et `needs_human_agent`) à des événements personnalisés ou des attributs de profil Braze. Ensuite, construisez une logique Canvas ou Campaign dans Braze qui se branche en fonction de ces valeurs.

{% endtab %}
{% tab Stocker les liens de transcription d'appel %}

**Mettre à jour les attributs de profil avec les liens de transcription à partir des événements `call.transcript.available`**

Utilisez l'événement `call.transcript.available` pour envoyer un lien vers la transcription complète de l'appel à Braze. Mappez l'URL de la transcription à un attribut de profil utilisateur Braze avec la Transformation des données afin que votre équipe puisse accéder aux conversations et les consulter depuis le profil utilisateur.

Voici un exemple de payload pour un événement `call.transcript.available` dans Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.transcript.available",
  "properties": {
    "agent_email": "xxx@example.com",
    "task_id": "WT953358e8822dd9333fc38dfbac25e1e1",
    "call_summary": "The agent Yuri explained insurance options to Alex and he said he'll need to think about it before moving forward Agent politely ended the call.",
    "contact_name": "Alex Smith",
    "contact_phone": "+15555550123",
    "is_voicemail": false,
    "moments_count": 18,
    "recording_id": "RE0118052841b7299d0630d1dff610c1fb",
    "recording_link": "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Recordings/xxx.mp3",
    "recording_duration": 78.75987,
    "request_timestamp": 1657799128,
    "response_timestamp": 1657799136,
    "sentiments": {
      "contact_sentiment": 70,
      "agent_sentiment": 75,
      "agent_sentiment_reason": "Yuri was polite and attentive, effectively gathering information and providing a resource, which contributed to a positive interaction.",
      "contact_sentiment_reason": "Alex was satisfied with the information provided but may have wanted more assistance regarding insurance options."
    },
    "trackers": [
      {
        "tracker_id": "4be87957-9140-4451-894a-bdbaed1f2460",
        "tracker_name": "Refinance"
      },
      {
        "tracker_id": "eb2577c6-5e23-4c65-9e04-5cc5d49eee7e",
        "tracker_name": "High Intent"
      }
    ],
    "transcript": "[handling agent]: Hi Alex, this is Yuri with BrightCover Insurance. I'll be going over some insurance options with you today. [contact]: Sounds good. [handling agent]: Before we start, I'm going to transfer you to a specialist for a moment. One sec. [transfer agent]: Hi Alex, this is Lee. Just verifying a few details before sending you back to Yuri. [contact]: Okay. [handling agent]: Thanks, Alex. Based on what you shared, here are some plan options... [contact]: I'll need to think about it. [handling agent]: Totally understandable. Feel free to reach out anytime. Have a great day! END OF TRANSCRIPT",
    "transcript_is_truncated": false,
    "transcript_url": "https://app.regalvoice.com/transcripts/WT953358e8822dd9333fc38dfbac25e1e1"
  },
  "originalTimestamp": "1657843308",
  "eventSource": "Regal Voice",
  "eventId": "f49a3cf9cb1336683bd5f19dwe4c61147"
}
```

{% endtab %}
{% endtabs %}