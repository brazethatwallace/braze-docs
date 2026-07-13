---
nav_title: Open Loyalty
article_title: Open Loyalty
description: "L'intégration de Braze et d'Open Loyalty vous permet de synchroniser les données de fidélité, telles que le solde de points, les changements de niveaux et les avertissements d'expiration, directement dans Braze en temps réel."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Open Loyalty

> [Open Loyalty](https://www.openloyalty.io/) est une plateforme de programmes de fidélisation basée sur le cloud qui vous permet de créer et de gérer des programmes de fidélisation et de récompenses pour vos clients. L'intégration de Braze et d'Open Loyalty synchronise les données de fidélisation, telles que le solde de points, les changements de niveau et les avertissements d'expiration, directement dans Braze en temps réel. Cela vous permet de déclencher des messages personnalisés (e-mail, notification push, SMS) lorsque le statut de fidélité d'un utilisateur change.

_Cette intégration est maintenue par Open Loyalty._

## À propos de l'intégration {#about-the-integration}

Cette intégration utilise les transformations de données de Braze pour capturer les webhooks d'Open Loyalty et les mapper aux profils utilisateurs de Braze.

* **Mises à jour en temps réel** : envoyez les événements de fidélisation (points gagnés, passage à un niveau supérieur) vers Braze.
* **Personnalisation** : utilisez les attributs de fidélité (solde actuel, nom du prochain palier) dans vos modèles Braze.
* **Bidirectionnel** : mettez à jour les attributs personnalisés des clients d'Open Loyalty en fonction des données d'engagement de Braze.

## Cas d'usage {#use-cases}

Cette intégration couvre les flux de données suivants :

1. **Synchronisation des événements vers Braze (entrant)** : suivez les changements de points, les passages à un niveau supérieur ou les échanges de récompenses en envoyant des données d'Open Loyalty à Braze. La transformation des données convertit ces données en événement utilisateur.
2. **Modification des membres Open Loyalty (sortant)** : mettez automatiquement à jour les données des membres dans Open Loyalty en fonction du comportement des utilisateurs dans Braze, par exemple en ajoutant des étiquettes « VIP » ou en mettant à jour des attributs personnalisés.

## Conditions préalables {#prerequisites}

Avant de commencer, vous devez disposer des éléments suivants :

| Condition | Description |
| :--- | :--- |
| Compte Open Loyalty | Vous devez disposer d'un compte administrateur sur un locataire Open Loyalty pour profiter de ce partenariat. |
| Clé API REST Open Loyalty | Une clé API REST Open Loyalty (pour les intégrations qui envoient des données de Braze à Open Loyalty). <br><br> Créez-la dans **Settings > Admins > API Keys**. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br> Créez cette clé dans le tableau de bord de Braze depuis **Settings** > **API Keys**. |
| Transformation des données Braze | Vous devez avoir accès à l'onglet « Data Settings » dans Braze pour configurer les récepteurs de webhook. |
| Correspondance des ID | L'`external_id` de l'utilisateur dans Braze doit correspondre à son `loyaltyCardNumber` (ou à un autre identifiant par défaut) dans Open Loyalty. |
| ID de locataire | Votre ID de locataire Open Loyalty (requis pour les mises à jour sortantes). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

L'intégration principale synchronise les événements webhook d'Open Loyalty avec Braze à l'aide de la transformation des données.

### Étape 1 : Générer l'URL du webhook dans Braze {#step-1-generate-the-webhook-url-in-braze}

Tout d'abord, créez une transformation de données dans Braze afin de générer une URL unique pour la réception des données.

1.  Dans Braze, ouvrez **Data Settings > Data Transformation**.
2.  Cliquez sur **Create Transformation**.
3.  Complétez les champs suivants :
     * **Transformation name** : donnez un nom descriptif (par exemple, « Open Loyalty Point Update Events »).
     * **Select destination** : choisissez **POST: Track users**.
4.  Cliquez sur **Create Transformation**.
5.  Repérez l'**URL du webhook** dans le panneau de détails et cliquez sur **Copy**.

{% alert important %}
Conservez cette URL en lieu sûr ; vous en aurez besoin pour l'étape suivante.
{% endalert %}

### Étape 2 : Créer l'abonnement au webhook dans Open Loyalty {#step-2-create-the-webhook-subscription-in-open-loyalty}

Indiquez à Open Loyalty d'envoyer des événements spécifiques à l'URL que vous venez de générer.

1.  Connectez-vous à votre panneau d'administration Open Loyalty.
2.  Naviguez vers **General > Webhooks**.
3.  Cliquez sur **Add new webhook** et configurez l'abonnement :
    * **eventName** : sélectionnez l'événement que vous souhaitez suivre (par exemple, `AvailablePointsAmountChanged`, `CustomerLevelChanged` ou `CampaignEffectWasApplied`).
    * **url** : collez l'URL du webhook Braze de l'étape 1.
    * Ajoutez les en-têtes suivants :
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Enregistrez l'abonnement au webhook.

### Étape 3 : Configurer la transformation des données {#step-3-configure-the-data-transformation}

Écrivez la logique JavaScript dans Braze pour mapper le payload Open Loyalty entrant aux propriétés de Braze.

1.  Dans Braze, ouvrez la transformation de données que vous avez créée à l'étape 1.
2.  Déclenchez l'événement dans Open Loyalty (par exemple, modifiez les points d'un membre ou attribuez un niveau) pour générer un exemple de payload dans le volet **Webhook details**.
3.  Dans l'éditeur de **Transformation code**, écrivez un script pour mapper les données entrantes. Utilisez l'exemple suivant comme guide :

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,

      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",

      // timestamp
      "time": new Date().toISOString(),

      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. Cliquez sur **Validate** pour vous assurer que le code fonctionne avec votre échantillon de payload, puis cliquez sur **Activate**.


## Utiliser Open Loyalty avec Braze {#using-open-loyalty-with-braze}

Une fois l'intégration entrante terminée, configurez les **mises à jour sortantes** pour modifier les membres Open Loyalty en fonction du comportement dans Braze.

### Étape 1 : Configurer la Campaign webhook dans Braze {#step-1-configure-braze-webhook-campaign}

Ce processus utilise les webhooks de Braze pour envoyer une requête `PATCH` à l'API Open Loyalty Member (par exemple, pour ajouter une étiquette « VIP »).

1.  Dans Braze, créez une nouvelle **Campaign** webhook (ou utilisez un webhook au sein d'un Canvas).
2.  Cliquez sur **Compose Webhook**.
3.  **URL du webhook** : construisez l'URL en utilisant votre instance Open Loyalty, l'ID du locataire et la variable Liquid de Braze pour l'ID de l'utilisateur.
    * Format :
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Complétez les champs suivants :
    * **Request Method** : `PATCH`
    * **Request Headers** :
      * `Content-Type` : `application/json`
      * `X-AUTH-TOKEN` : `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Request Body** : sélectionnez `Raw text` et collez le payload :

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Étape 2 : Configurer le déclencheur {#step-2-configure-the-trigger}

1.  Accédez à l'onglet **Delivery** ou **Entry Schedule**.
2.  Complétez les champs suivants :
    * **Delivery Method** : Action-Based.
    * **Trigger** : définissez le déclencheur pertinent (par exemple, un utilisateur entre dans un Segment spécifique dans Braze).
    * **Launch** : activez la Campaign.

## Résolution des problèmes {#troubleshooting}

### Vérifier les événements entrants {#verify-inbound-events}
Lorsque la transformation des données est active, les données apparaissent dans Braze sous la forme d'un événement personnalisé. Vérifiez-le en créant une Campaign avec un déclencheur **Perform Custom Event** et en vérifiant si l'événement que vous avez défini (par exemple, `Loyalty Event Triggered`) est disponible.

### Vérifier les webhooks sortants {#verify-outbound-webhooks}
Vérifiez le journal d'activité des messages dans Braze pour vous assurer que le webhook a renvoyé un statut `200 OK`.
* **Erreur 401** : vérifiez votre jeton API Open Loyalty.
* **Erreur 404** : l'ID de l'utilisateur dans Braze n'existe pas dans Open Loyalty.