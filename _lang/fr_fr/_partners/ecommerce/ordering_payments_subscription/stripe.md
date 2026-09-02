---
nav_title: Stripe
article_title: Stripe
description: "Cet article présente le partenariat entre Braze et Stripe."
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Stripe

> [Stripe](https://www.stripe.com/) est une plateforme d'infrastructure financière complète qui permet aux entreprises d'accepter les paiements, de gérer les opérations de chiffre d'affaires et de faciliter le commerce mondial grâce à une suite d'API et de services intégrés.

En intégrant Braze et Stripe, vous pouvez :

- Mettre à jour les profils utilisateurs dans Braze avec les données de paiement et de facturation en temps réel provenant de Stripe.
- Déclencher des messages dans Braze en fonction des événements Stripe, tels que le démarrage d'un essai, l'activation d'un abonnement, l'annulation d'un abonnement, et plus encore.
- Personnaliser les messages de Braze en fonction de l'historique de paiement ou du statut de facturation d'un utilisateur reçu à l'aide des webhooks Stripe.

## Prérequis {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Stripe | Un compte Stripe avec accès aux webhooks est requis pour tirer parti de ce partenariat. |
| Transformation de données Braze | Une [URL de transformation de données]({{site.baseurl}}/user_guide/data/unification/data_transformation) est nécessaire pour recevoir les données de Stripe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

### Étape 1 : Configurer la transformation de données Braze pour accepter les webhooks Stripe {#step-1}

{% multi_lang_include data_activation/create_transformation.md %}

### Étape 2 : Configurer les webhooks Stripe {#step-2-set-up-stripe-webhooks}

Suivez les étapes de la [documentation sur les webhooks de Stripe](https://docs.stripe.com/development/dashboard/webhooks) pour configurer un webhook.

Ajoutez l'URL du webhook de votre transformation de données comme **URL de destination** et sélectionnez les types d'événements que vous souhaitez envoyer à Braze. Consultez la [documentation de Stripe](https://docs.stripe.com/api/events/types) pour obtenir la liste complète des types d'événements.

![Un exemple de configuration de webhook Stripe.]({% image_buster /assets/img/stripe/stripe_webhook_configuration.png %}){: style="max-width:80%;"}

Envoyez ensuite un événement de test à votre transformation de données.

### Étape 3 : Écrire le code de transformation pour accepter les événements Stripe choisis {#step-3-write-transformation-code-to-accept-your-chosen-stripe-events}

Vous allez ensuite transformer le payload du webhook envoyé par Stripe en un objet JavaScript renvoyé en valeur de retour.

1. Actualisez votre transformation de données et vérifiez que le payload de test Stripe est visible dans la section **Webhook details**.
2. Mettez à jour le code de votre transformation de données pour prendre en charge les événements Stripe choisis.
3. Sélectionnez **Validate** pour obtenir un aperçu de la sortie de votre code et vérifier qu'il s'agit d'une requête `/users/track` valide.
4. Enregistrez et activez votre transformation de données.

![Un exemple de détails de webhook et de code de transformation.]({% image_buster /assets/img/stripe/stripe_data_transformation.png %})

#### Format du corps de la requête {#request-body-format}

Cette valeur de retour doit respecter le format du corps de requête de l'endpoint `/users/track` :

- Le code de transformation est accepté dans le langage de programmation JavaScript. Tout flux de contrôle JavaScript standard, comme la logique if/else, est pris en charge.
- Le code de transformation accède au corps de la requête du webhook via la variable payload. Cette variable est un objet rempli en analysant le JSON du corps de la requête.
- Toutes les fonctionnalités prises en charge par notre endpoint `/users/track` sont compatibles, notamment :
    - Les objets d'attributs utilisateur, les objets d'événements et les objets d'achat
    - Les attributs imbriqués et les propriétés d'événement personnalisé imbriquées
    - Les mises à jour de groupes d'abonnement
    - L'adresse e-mail comme identifiant

### Étape 4 : Publier votre webhook Stripe {#step-4-publish-your-stripe-webhook}

Après avoir écrit votre transformation de données, sélectionnez **Validate** pour vous assurer que le code de votre transformation de données est correctement formaté et fonctionnera comme prévu. Enregistrez ensuite et activez votre transformation de données. Une fois activée, les données d'événements personnalisés seront enregistrées dans le profil d'un utilisateur lorsqu'il complète l'événement.

![Un événement personnalisé Stripe « Charge Succeeded » dans un profil utilisateur Braze.]({% image_buster /assets/img/stripe/stripe_braze_profile_event.png %}){: style="max-width:80%;"}

## Exemple de payload de webhook Stripe {#example}

```json
{
 "headers": {
   "Version": "HTTP/1.1",
   "X-Datadog-Trace-Id": "9124157397962821303",
   "X-Datadog-Parent-Id": "9124157397962821303",
   "X-Datadog-Sampling-Priority": "2",
   "Host": "xxx",
   "X-Request-Id": "xxx",
   "X-Real-Ip": "165.159.72.690",
   "X-Forwarded-For": "161.123.56.890",
   "X-Forwarded-Host": "xxx",
   "X-Forwarded-Port": "443",
   "X-Forwarded-Proto": "https",
   "X-Forwarded-Scheme": "https",
   "X-Scheme": "https",
   "X-Original-Forwarded-For": "12.345.678.123",
   "Cf-Ray": "9470a06172f8816e-IAD",
   "Cache-Control": "no-cache",
   "User-Agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)",
   "Accept-Encoding": "gzip",
   "Cf-Connecting-Ip": "12.123.456.789",
   "Cf-Visitor": "{\"scheme\":\"https\"}",
   "X-Worker-Executions": "1",
   "Cf-Worker": "xxx",
   "X-Fastly-Geoloc-Countrycode": "US",
   "Stripe-Signature": "t=xxx,v1=xxxx,v0=xxxx",
   "Cf-Ew-Via": "15",
   "Cdn-Loop": "cloudflare; loops=1; subreqs=1",
   "Accept": "*/*; q=0.5, application/xml"
 },
 "payload": {
   "id": "evt_3RTqw0RMEOaIvYpU1k2TFajH",
   "object": "event",
   "api_version": "2025-04-30.basil",
   "created": 1748465448,
   "data": {
     "object": {
       "id": "ch_3RTqw0RMEOaIvYpU1M9ZYtjP",
       "object": "charge",
       "amount": 100,
       "amount_captured": 100,
       "amount_refunded": 0,
       "application": null,
       "application_fee": null,
       "application_fee_amount": null,
       "balance_transaction": null,
       "billing_details": {
         "address": {
           "city": null,
           "country": null,
           "line1": null,
           "line2": null,
           "postal_code": null,
           "state": null
         },
         "email": null,
         "name": null,
         "phone": null,
         "tax_id": null
       },
       "calculated_statement_descriptor": "Stripe",
       "captured": true,
       "created": 1748465448,
       "currency": "usd",
       "customer": "cus_SOeDf39aosGb97",
       "description": "(created by Stripe CLI)",
       "destination": null,
       "dispute": null,
       "disputed": false,
       "failure_balance_transaction": null,
       "failure_code": null,
       "failure_message": null,
       "fraud_details": {},
       "livemode": false,
       "metadata": {},
       "on_behalf_of": null,
       "order": null,
       "outcome": {
         "advice_code": null,
         "network_advice_code": null,
         "network_decline_code": null,
         "network_status": "approved_by_network",
         "reason": null,
         "risk_level": "normal",
         "risk_score": 9,
         "seller_message": "Payment complete.",
         "type": "authorized"
       },
       "paid": true,
       "payment_intent": "pi_3RTqw0RMEOaIvYpU1pQl3Lmp",
       "payment_method": "pm_1RTqw0RMEOaIvYpU5VE8HFlp",
       "payment_method_details": {
         "card": {
           "amount_authorized": 100,
           "authorization_code": null,
           "brand": "visa",
           "checks": {
             "address_line1_check": null,
             "address_postal_code_check": null,
             "cvc_check": "pass"
           },
           "country": "US",
           "exp_month": 5,
           "exp_year": 2026,
           "extended_authorization": {
             "status": "disabled"
           },
           "fingerprint": "HAKdyqJ9xh2YhbzT",
           "funding": "credit",
           "incremental_authorization": {
             "status": "unavailable"
           },
           "installments": null,
           "last4": "4242",
           "mandate": null,
           "multicapture": {
             "status": "unavailable"
           },
           "network": "visa",
           "network_token": {
             "used": false
           },
           "network_transaction_id": "726575100121113",
           "overcapture": {
             "maximum_amount_capturable": 100,
             "status": "unavailable"
           },
           "regulated_status": "unregulated",
           "three_d_secure": null,
           "wallet": null
         },
         "type": "card"
       },
       "radar_options": {},
       "receipt_email": null,
       "receipt_number": null,
       "receipt_url": "https://pay.stripe.com/receipts/payment/xxx",
       "refunded": false,
       "review": null,
       "shipping": null,
       "source": null,
       "source_transfer": null,
       "statement_descriptor": null,
       "statement_descriptor_suffix": null,
       "status": "succeeded",
       "transfer_data": null,
       "transfer_group": null
     }
   },
   "livemode": false,
   "pending_webhooks": 3,
   "request": {
     "id": "req_jqtL1Q6CPaNx8x",
     "idempotency_key": "f0f9aee4-a889-4fcc-bc2e-fa41fa426f05"
   },
   "type": "charge.succeeded"
 }
}
```

## Cas d'usage de Data Transformation {#data-transformation-use-cases}

Les modèles suivants sont des exemples construits à partir de notre [exemple de payload de webhook Stripe](#example). Ces modèles peuvent être utilisés comme point de départ. Vous pouvez partir de zéro ou supprimer des composants spécifiques selon vos besoins.

Dans cet exemple de modèle, nous enregistrons un événement personnalisé sur le profil Braze. Le type d'événement sera envoyé comme nom de l'événement personnalisé, et l'objet de données sera transmis en tant que propriétés d'événement.

### Cas d'usage : le client comme identifiant {#use-case-customer-as-an-identifier}

Dans cet exemple de modèle, nous utilisons le champ customer comme identifiant.

{% tabs local %}
{% tab Entrée %}

```javascript

/* This template is based on the source platform's documentation here: https://stripe.com/docs/webhooks


/* Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Stripe's charge succeeded event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.data.object.created;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();


/* defines a variable 'brazecall' that will hold the request payload for the /users/track request
let brazecall;


/* if the type is charge.succeeded and customer field is not null, build the /users/track request to log an event to the user profile
if (payload.type == "charge.succeeded" && payload.data.object.customer) {
 brazecall = {
   "events": [
     {
       "external_id": payload.data.object.customer,
       "name": "Charge Succeeded",
       "time": isoString,
       "properties": {
         "amount": payload.data.object.amount,
         "paid": payload.data.object.paid,
         "status": payload.data.object.status
       }
     }
   ]
 };
}
/* After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Sortie %}

```json
{
  "events": [
    {
      "external_id": "an_account@example.com",
      "name": "Charge Succeeded",
      "time": "2025-05-28T18:21:39.527Z",
      "properties": {
        "amount": 100,
    "paid":true,
    "Status":"succeeded"
    }
   }
  ]
}
```

{% endtab %}
{% endtabs %}

## Surveillance et résolution des problèmes {#monitoring-and-troubleshooting}

Consultez [Surveiller votre transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-5-monitor-your-transformation) pour en savoir plus sur la surveillance et la résolution des problèmes liés à votre transformation.