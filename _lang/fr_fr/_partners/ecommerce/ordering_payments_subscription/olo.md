---
nav_title: Olo
article_title: Olo
description: "Cet article présente le partenariat entre Braze et Olo, une plateforme SaaS ouverte de premier plan pour les restaurants qui permet de renforcer l'accueil à chaque point de contact."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/) est une plateforme SaaS ouverte de premier plan pour les restaurants qui permet de renforcer l'accueil à chaque point de contact.

En intégrant Olo et Braze, vous pouvez :

- Mettre à jour les profils utilisateurs dans Braze pour qu'ils restent cohérents avec les profils utilisateurs d'Olo
- Envoyer les messages les plus pertinents depuis Braze en fonction des événements Olo

## Conditions préalables {#prerequisites}

| Condition | Description |
| ----------- | ----------- |
| Compte Olo | Un compte Olo avec accès aux webhooks est nécessaire pour profiter de ce partenariat. Configurez les abonnements aux webhooks via l'[outil webhooks en libre-service](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dans le tableau de bord d'Olo. |
| Transformation des données Braze | Une [URL de Transformation des données]({{site.baseurl}}/data_transformation) est nécessaire pour recevoir des données d'Olo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

Un webhook est un moyen pour Olo d'envoyer des informations événementielles à Braze sur les utilisateurs et leurs actions, y compris des événements tels que la commande passée, l'inscription d'un invité, la commande récupérée et bien d'autres. Le webhook Olo transmet l'événement à Braze généralement dans les secondes qui suivent l'exécution de l'action.

## Clause de non-responsabilité {#disclaimer}

Dans Olo, vous êtes limité à un webhook par environnement pour chaque marque approuvée, tous envoyés à la même **URL de destination**. Des marques différentes peuvent avoir des URL différentes, mais les événements d'une même marque doivent partager une même URL. Dans Braze, cela signifie que vous ne pouvez créer qu'une seule transformation à utiliser avec Olo.

Pour gérer plusieurs événements Olo au sein de cette transformation unique, recherchez l'en-tête `X-Olo-Event-Type` dans chaque webhook. Cet en-tête vous permet de traiter de manière conditionnelle différents événements Olo.

## Intégration {#integration}

### Étape 1 : Configurer la Transformation des données Braze pour accepter l'événement test d'Olo {#step-1}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

### Étape 2 : Configurer les webhooks d'Olo {#step-2-set-up-olo-webhooks}

Utilisez l'[outil webhooks en libre-service](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dans le tableau de bord d'Olo pour configurer les webhooks à envoyer à votre Transformation des données.

1. Choisissez les événements à envoyer à Braze.
2. Configurez l'**URL de destination**. Il s'agit de l'URL de Transformation des données créée à l'[étape 1](#step-1).

{% alert note %}
`OAuth` et le secret partagé de l'en-tête `X-Olo-Signature` ne sont pas nécessaires pour la transformation.
{% endalert %}

{:start="3"}
3. Vérifiez que le webhook est configuré correctement en envoyant un [événement test](https://developer.olo.com/docs/load/webhooks#operation/test) à votre Transformation des données. Seuls les utilisateurs du tableau de bord d'Olo disposant de l'[autorisation Developer Tools](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) peuvent envoyer des événements test.

Olo exige une réponse positive du webhook de l'événement test avant que vous puissiez terminer le processus de configuration du webhook d'Olo.

### Étape 3 : Écrire le code de transformation pour accepter les événements Olo choisis {#step-3-write-transformation-code-to-accept-your-chosen-olo-events}

Au cours de cette étape, vous transformerez le payload du webhook envoyé depuis la plateforme source en une valeur de retour sous forme d'objet JavaScript.

1. Envoyez une requête à votre URL de Transformation des données avec un exemple de payload d'un événement Olo que vous souhaitez prendre en charge. Consultez le [format du corps de la requête](#request-body-format) pour obtenir de l'aide sur le formatage de votre requête.
2. Actualisez votre Transformation des données et assurez-vous que vous pouvez voir l'exemple de payload dans les **Détails du webhook**.
3. Mettez à jour votre code de Transformation des données pour prendre en charge les événements Olo choisis.
4. Cliquez sur **Valider** pour obtenir un aperçu de la sortie de votre code et vérifier s'il s'agit d'une requête `/users/track` acceptable.
5. Enregistrez et activez votre Transformation des données.

#### Format du corps de la requête {#request-body-format}

Cette valeur de retour doit respecter le format du corps de la requête `/users/track` de Braze :

- Le code de transformation est accepté dans le langage de programmation JavaScript. Tout flux de contrôle JavaScript standard, tel que la logique if/else, est pris en charge.
- Le code de transformation accède au corps de la requête du webhook via la variable payload. Cette variable est un objet rempli en analysant le JSON du corps de la requête.
- Toutes les fonctionnalités prises en charge par notre endpoint `/users/track` sont prises en charge, y compris :
    - Objets d'attributs utilisateur, objets d'événements et objets d'achat
    - Attributs et propriétés d'événements personnalisés imbriqués
    - Mises à jour des groupes d'abonnement
    - L'adresse e-mail comme identifiant

## Exemples de Transformations de données pour les webhooks Olo {#example-data-transformations-for-olo-webhooks}

Cette section contient des exemples de modèles qui peuvent servir de point de départ. N'hésitez pas à repartir de zéro ou à supprimer des composants spécifiques si vous le souhaitez.

Dans chaque modèle, le code définit une variable `brazecall` pour créer une requête `/users/track`.

Une fois la requête `/users/track` affectée à `brazecall`, vous devez renvoyer explicitement `brazecall` pour créer une sortie.

### Transformation d'un événement unique {#single-event-transformation}

Si vous ne souhaitez prendre en charge qu'un seul événement Olo, vous n'aurez pas besoin d'utiliser l'en-tête `X-Olo-Event-Type` pour créer conditionnellement le payload de la requête `/users/track`. Par exemple, enregistrer un événement d'achat ou un événement personnalisé dans le profil utilisateur lorsqu'un webhook Olo Order Placed est envoyé à Braze.

### Enregistrement de chaque produit en tant qu'achat {#logging-each-product-as-a-purchase}

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Enregistrement d'un événement personnalisé {#logging-a-custom-event}

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = {
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Transformation multi-événements {#multi-event-transformation}

Olo envoie le type d'événement dans l'en-tête `X-Olo-Event-Type` de chaque webhook. Pour prendre en charge plusieurs événements webhook Olo au sein d'une même transformation, utilisez une logique conditionnelle pour transformer le payload du webhook en fonction de la valeur de ce type d'en-tête.

Dans l'exemple de transformation ci-dessous, le script JavaScript crée un payload particulier pour les événements `UserSignedUp` et `OrderPlaced`. En outre, une condition `else` gère un payload pour tous les événements Olo envoyés à Braze sans l'en-tête X-Olo-Event-Type `UserSignedUp` ou `OrderPlaced`.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Étape 4 : Publier votre webhook Olo {#step-4-publish-your-olo-webhook}

Après avoir activé votre Transformation des données dans Braze, utilisez l'[outil webhooks en libre-service](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dans le tableau de bord d'Olo pour publier votre webhook. Une fois le webhook publié, la Transformation des données commencera à recevoir les messages d'événements des webhooks Olo.

## Ce qu'il faut savoir {#things-to-know}

### Nouvelles tentatives {#retries}

Olo retentera les appels de webhook aboutissant à un code d'état de réponse HTTP `429 - Too Many Requests` ou dans la plage `5xx` (par exemple, en raison d'un délai d'attente de la passerelle ou d'une erreur du serveur), jusqu'à 50 fois sur une période de 24 heures avant d'abandonner la requête.

### Réception au moins une fois {#at-least-once-delivery}

Si un appel webhook aboutit à un code d'état de réponse HTTP `429 - Too Many Requests` ou dans la plage `5xx` (par exemple, en raison d'un dépassement de délai de la passerelle ou d'une erreur du serveur), Olo réessayera le message jusqu'à 50 fois sur une période de 24 heures avant d'abandonner.

Les webhooks peuvent donc être reçus plusieurs fois par un même destinataire. Il appartient au destinataire d'ignorer les doublons en vérifiant l'en-tête `X-Olo-Message-Id`.