---
nav_title: Limites de débit
article_title: Limites de débit de l'API Device Messaging
page_order: 3
page_type: reference
description: "Découvrez le fonctionnement des limites de débit et des en-têtes de réponse de l'API Device Messaging."
hidden: true
---

# Limites de débit de l'API Device Messaging {#device-messaging-api-rate-limits}

Braze applique des limites de débit de l'API Device Messaging par espace de travail. Si un espace de travail dépasse une limite, Braze renvoie un code de statut `429 Too Many Requests`.

Les limites de l'API Device Messaging sont distinctes des limites par défaut documentées pour les autres endpoints de la REST API Braze. Ne supposez pas qu'une limite, une fenêtre temporelle, une taille de payload ou un calendrier de réinitialisation documenté pour un autre endpoint s'applique à l'API Device Messaging.

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Device Messaging sont susceptibles d'évoluer. Contactez votre gestionnaire de compte Braze pour demander l'accès.
{% endalert %}

## En-têtes de limitation de débit {#rate-limit-headers}

Lorsque des informations de limitation de débit sont disponibles, une réponse inclut les en-têtes suivants :

| En-tête | Description |
|---|---|
| `X-RateLimit-Limit` | Le nombre maximal de requêtes autorisées dans l'intervalle en cours. |
| `X-RateLimit-Remaining` | Le nombre de requêtes restantes dans la fenêtre de limitation de débit en cours. |
| `X-RateLimit-Reset` | L'heure UTC epoch à laquelle la fenêtre de limitation de débit en cours est réinitialisée. |
| `X-RateLimit-Retry-After` | Le nombre de secondes à attendre avant de réessayer une requête ayant atteint la limite de débit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="En-têtes de limitation de débit de l'API Device Messaging" }

Utilisez ces en-têtes pour réduire ou suspendre les requêtes avant d'atteindre une limite. Ces en-têtes peuvent ne pas être présents dans chaque réponse.

## Gestion des limites de débit {#handling-rate-limits}

Lorsque vous recevez une réponse `429` :

1. Arrêtez ou réduisez les requêtes pour l'espace de travail concerné.
2. Utilisez `X-RateLimit-Retry-After` lorsqu'il est présent pour déterminer le temps d'attente. Sinon, utilisez `X-RateLimit-Reset` lorsqu'il est disponible pour déterminer quand reprendre.
3. Réessayez avec des délais exponentiels et un nombre maximal de tentatives.