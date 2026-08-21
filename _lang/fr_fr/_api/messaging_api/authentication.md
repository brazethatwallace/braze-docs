---
nav_title: Authentification et sécurité
article_title: Authentification et sécurité de l'API Messaging
page_order: 1
page_type: reference
description: "Découvrez comment authentifier les requêtes de l'API Messaging de manière sécurisée."
hidden: true
---

# Authentification et sécurité de l'API Messaging {#messaging-api-authentication-and-security}

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Messaging sont susceptibles d'être modifiées.
{% endalert %}

L'API Messaging utilise des clés API REST côté client. Ces clés sont distinctes des clés API REST privées utilisées pour les requêtes côté serveur de la REST API de Braze.

## Clés API REST côté client {#client-side-rest-api-keys}

Les clés API REST côté client sont limitées à un seul espace de travail et restreintes aux permissions de l'API Messaging. Vous pouvez intégrer ces clés dans les applications clientes.

{% alert important %}
Utilisez uniquement une clé API REST côté client dans une application cliente. N'exposez jamais une clé API REST privée côté serveur dans du code côté client.
{% endalert %}

Pour créer une clé API REST côté client :

1. Accédez à **Paramètres** > **API et identifiants** > **Clés API** dans le tableau de bord de Braze.
2. Sélectionnez **Créer une clé API**.
3. Pour **Type de clé**, sélectionnez **Client**.
4. Attribuez la permission `banners.sync` pour récupérer les Banners, la permission `banners.track` pour signaler les événements Banner, ou les deux.

## Authentification des requêtes {#authenticating-requests}

Envoyez la clé API REST côté client en tant que jeton bearer dans l'en-tête `Authorization` :

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

Utilisez HTTPS et l'[endpoint REST]({{site.baseurl}}/api/basics#endpoints) correspondant à votre instance Braze.

## Identité de l'utilisateur {#user-identity}

Une clé API REST côté client authentifie l'application appelante et l'espace de travail, pas l'utilisateur. Le champ `external_user_id` dans une requête identifie l'utilisateur associé au contenu et aux événements Banner.

Appliquez les contrôles d'autorisation de votre application avant d'effectuer des requêtes à l'API Messaging.

## Erreurs d'authentification {#authentication-errors}

Les échecs d'authentification et de permissions peuvent varier selon l'endpoint. Consultez le tableau des codes de statut de chaque endpoint et la [gestion des erreurs de l'API Messaging]({{site.baseurl}}/api/messaging_api/error_handling).