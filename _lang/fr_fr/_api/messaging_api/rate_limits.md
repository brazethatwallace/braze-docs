---
nav_title: Limites de débit
article_title: Limites de débit de l'API Messaging
page_order: 3
page_type: reference
description: "Découvrez le fonctionnement des limites de débit et des en-têtes de réponse de l'API Messaging."
hidden: true
---

# Limites de débit de l'API Messaging {#messaging-api-rate-limits}

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Messaging sont susceptibles d'être modifiées.
{% endalert %}

Braze applique des limites de débit de l'API Messaging par espace de travail. Si un espace de travail dépasse une limite, Braze renvoie un code de statut `429 Too Many Requests`.

Les limites de l'API Messaging sont distinctes des limites par défaut documentées pour les autres endpoints de la REST API Braze. Ne supposez pas qu'une limite, une fenêtre temporelle, une taille de payload ou un calendrier de réinitialisation documenté pour un autre endpoint s'applique à l'API Messaging.

## En-têtes de limite de débit {#rate-limit-headers}

Lorsque des informations sur la limite de débit sont disponibles, la réponse inclut les en-têtes suivants :

| En-tête | Description |
|---|---|
| `X-RateLimit-Limit` | Le nombre maximum de requêtes autorisées dans l'intervalle en cours. |
| `X-RateLimit-Remaining` | Le nombre de requêtes restantes dans la fenêtre de limite de débit en cours. |
| `X-RateLimit-Reset` | L'heure UTC epoch à laquelle la fenêtre de limite de débit en cours est réinitialisée. |
| `X-RateLimit-Retry-After` | Le nombre de secondes à attendre avant de relancer une requête limitée par le débit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="En-têtes de limite de débit de l'API Messaging" }

Utilisez ces en-têtes pour réduire ou suspendre les requêtes avant d'atteindre une limite. Les en-têtes peuvent ne pas être présents dans chaque réponse.

## Gestion des limites de débit {#handling-rate-limits}

Lorsque vous recevez une réponse `429` :

1. Arrêtez ou réduisez les requêtes pour l'espace de travail concerné.
2. Utilisez `X-RateLimit-Retry-After` lorsqu'il est présent pour déterminer combien de temps attendre. Sinon, utilisez `X-RateLimit-Reset` lorsqu'il est disponible pour déterminer quand reprendre.
3. Relancez avec des délais exponentiels et un nombre maximum de tentatives.