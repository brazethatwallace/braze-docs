---
nav_title: Aperçu
article_title: Aperçu de l'API Messaging
page_order: 0
page_type: reference
description: "Découvrez l'API Messaging de Braze et ses fonctionnalités en accès anticipé."
hidden: true
---

# Aperçu de l'API Messaging {#messaging-api-overview}

L'API Messaging de Braze est un ensemble d'endpoints REST permettant d'intégrer les fonctionnalités de communication de Braze sans SDK Braze. Vous pouvez appeler ces endpoints depuis des applications clientes ou serveur.

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Messaging sont susceptibles d'évoluer. Contactez votre gestionnaire de compte Braze pour demander l'accès.
{% endalert %}

## Fonctionnalités prises en charge {#supported-capabilities}

Pendant l'accès anticipé, vous pouvez utiliser l'API Messaging pour :

- [Récupérer les bannières éligibles]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners) pour un ID utilisateur externe et un ensemble de placements
- [Signaler les événements d'impression et de clic des bannières]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)

L'API Messaging renvoie des propriétés de bannière structurées afin que vous puissiez créer une interface personnalisée. Elle ne renvoie pas de HTML rendu.

## Prérequis d'intégration {#integration-requirements}

Pour intégrer l'API Messaging, vous avez besoin des éléments suivants :

- Un espace de travail avec l'API Messaging activée
- Une clé API REST côté client pour cet espace de travail
- L'endpoint REST pour cet espace de travail
- L'ID utilisateur externe de l'utilisateur
- L'identifiant API de l'application

Pour plus d'informations sur les identifiants, consultez [Authentification et sécurité]({{site.baseurl}}/api/messaging_api/authentication).

## Recommandations pour l'API Messaging et la REST API {#messaging-api-and-rest-api-guidance}

L'API Messaging utilise les mêmes endpoints REST régionaux que la REST API de Braze, mais elle dispose d'un contrat d'authentification et de réponse distinct. Les recommandations générales de la REST API concernant les clés privées côté serveur, les corps de réponse, les erreurs et les limites de débit ne s'appliquent pas, sauf si un article de l'API Messaging y fait explicitement référence.

Utilisez la documentation des endpoints de l'API Messaging comme source de référence pour les champs de requête, les corps de réponse, les codes de statut et les limites.