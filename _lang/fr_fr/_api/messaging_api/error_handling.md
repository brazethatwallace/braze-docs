---
nav_title: Gestion des erreurs et nouvelles tentatives
article_title: Gestion des erreurs et nouvelles tentatives de l'API Messaging
page_order: 2
page_type: reference
description: "Découvrez comment gérer les réponses, les erreurs et les nouvelles tentatives de l'API Messaging."
hidden: true
---

# Gestion des erreurs et nouvelles tentatives de l'API Messaging {#messaging-api-error-handling-and-retries}

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Messaging sont susceptibles d'être modifiées.
{% endalert %}

Les corps de réponse et la sémantique de succès de l'API Messaging varient selon l'endpoint. Utilisez le schéma de réponse et le tableau des codes de statut de chaque endpoint comme référence faisant autorité.

## Réponses de succès {#success-responses}

Les endpoints Banner utilisent des réponses de succès différentes :

- `POST /v1/device-messaging/banners/sync` renvoie un code de statut `200` avec un objet `banners`.
- `POST /v1/device-messaging/banners/track` renvoie un code de statut `202` avec `events_processed` et `message`. Si Braze ignore certains événements individuels, la réponse inclut également un tableau `errors`.

Une réponse `202` de l'endpoint de suivi signifie que Braze a accepté au moins un événement valide. Consultez le tableau `errors` pour identifier les événements ignorés.

## Réponses d'erreur {#error-responses}

Les champs de réponse d'erreur varient également :

- Les erreurs de récupération de Banner utilisent un champ `error`.
- Les erreurs de suivi de Banner utilisent un champ `message` et peuvent inclure un tableau indexé `errors`.

N'analysez pas le texte des messages d'erreur pour déterminer le comportement de l'application. Utilisez plutôt le code de statut HTTP et les champs spécifiques à l'endpoint.

## Recommandations pour les nouvelles tentatives {#retry-guidance}

Utilisez les recommandations suivantes pour décider si une nouvelle tentative est appropriée :

| Code de statut | Recommandation |
|---|---|
| `400` | Corrigez la requête avant de réessayer. Pour le suivi de Banner, corrigez les événements ignorés avant de les renvoyer. |
| `401` ou `403` | Vérifiez la clé API REST côté client et ses permissions avant de réessayer. |
| `404` | Confirmez que l'API Messaging est activée pour l'espace de travail et que l'URL de l'endpoint est correcte. |
| `429` | Réduisez le débit des requêtes et réessayez avec des délais exponentiels. Utilisez les en-têtes de réponse de limitation de débit lorsqu'ils sont disponibles. |
| `5XX` | Réessayez avec des délais exponentiels et un nombre maximal de tentatives. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recommandations pour les nouvelles tentatives de l'API Messaging" }

Pour connaître le corps de réponse exact et les codes de statut pris en charge, consultez l'endpoint concerné :

- [Récupérer les Banners pour un utilisateur]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners)
- [Suivre les événements d'analyse de Banner]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)