---
nav_title: Authentification et sécurité
article_title: Authentification et sécurité de l'API Device Messaging
page_order: 1
page_type: reference
description: "Découvrez comment authentifier les requêtes de l'API Device Messaging de manière sécurisée."
hidden: true
---

# Authentification et sécurité de l'API Device Messaging {#device-messaging-api-authentication-and-security}

L'API Device Messaging utilise des clés API REST côté client. Ces clés sont distinctes des clés API REST privées utilisées pour les requêtes côté serveur de la REST API de Braze.

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Device Messaging sont susceptibles d'évoluer. Contactez votre gestionnaire de compte Braze pour demander l'accès.
{% endalert %}

## Clés REST API côté client {#client-side-rest-api-keys}

Les clés REST API côté client sont limitées à un seul espace de travail et restreintes aux autorisations de l'API Device Messaging. Vous pouvez intégrer ces clés dans les applications côté client.

{% alert important %}
N'utilisez qu'une clé REST API côté client dans une application cliente. N'exposez jamais une clé REST API privée côté serveur dans le code côté client.
{% endalert %}

Pour créer une clé REST API côté client :

1. Dans le tableau de bord de Braze, accédez à **Paramètres** > **API et identifiants** > **Clés API**.
2. Sélectionnez **Créer une clé API**.
3. Pour **Type de clé**, sélectionnez **Client**.
4. Attribuez la permission `banners.sync` pour récupérer les bannières, la permission `banners.track` pour signaler les événements de bannière, ou les deux.

## Authentification des requêtes {#authenticating-requests}

Envoyez la clé REST API côté client en tant que jeton porteur dans l'en-tête `Authorization` :

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

Utilisez HTTPS et l'[endpoint REST]({{site.baseurl}}/api/basics#endpoints) correspondant à votre instance Braze.

## Identité de l'utilisateur {#user-identity}

Une clé API REST côté client authentifie l'application appelante et l'espace de travail, et non l'utilisateur. L'`external_user_id` dans une requête identifie l'utilisateur associé au contenu et aux événements du Banner.

Appliquez les contrôles d'autorisation de votre application avant d'effectuer des requêtes à l'API Device Messaging.

## Erreurs d'authentification {#authentication-errors}

Les échecs d'authentification et de permissions peuvent varier selon l'endpoint. Consultez le tableau des codes de statut de chaque endpoint et la [gestion des erreurs de l'API Device Messaging]({{site.baseurl}}/api/device_messaging_api/error_handling).