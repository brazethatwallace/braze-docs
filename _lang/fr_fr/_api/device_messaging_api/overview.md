---
nav_title: Aperçu
article_title: Aperçu de l'API Device Messaging
page_order: 0
page_type: reference
description: "Découvrez l'API Device Messaging de Braze et ses fonctionnalités en accès anticipé."
hidden: true
---

# Aperçu de l'API Device Messaging {#device-messaging-api-overview}

L'API Device Messaging de Braze est un ensemble d'endpoints REST permettant d'intégrer les fonctionnalités de communication de Braze sans SDK Braze. Vous pouvez appeler ces endpoints depuis des applications clientes ou serveur.

{% alert important %}
Cette page est en version bêta. Les fonctionnalités et la documentation de l'API Device Messaging sont susceptibles d'évoluer. Contactez votre gestionnaire de compte Braze pour demander l'accès.
{% endalert %}

## Fonctionnalités prises en charge {#supported-capabilities}

Pendant l'accès anticipé, vous pouvez utiliser l'API Device Messaging pour :

- [Récupérer les bannières éligibles]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) pour un ID utilisateur externe et un ensemble de placements
- [Signaler les événements d'impression et de clic des bannières]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_track_banner_events)

L'API Device Messaging renvoie les propriétés structurées des bannières afin que vous puissiez créer une interface personnalisée. Elle ne renvoie pas de HTML rendu.

## Prérequis d'intégration {#integration-requirements}

Pour intégrer l'API Device Messaging, vous avez besoin des éléments suivants :

- Un espace de travail avec l'API Device Messaging activée
- Une clé REST API côté client pour cet espace de travail
- L'endpoint REST pour cet espace de travail
- L'ID utilisateur externe de l'utilisateur
- L'identifiant API de l'application

Pour plus d'informations sur les identifiants, consultez [Authentification et sécurité]({{site.baseurl}}/api/device_messaging_api/authentication).

## API Device Messaging et recommandations pour la REST API {#device-messaging-api-and-rest-api-guidance}

L'API Device Messaging utilise les mêmes endpoints REST régionaux que la REST API de Braze, mais elle dispose d'un contrat d'authentification et de réponse distinct. Les recommandations générales relatives à la REST API concernant les clés privées côté serveur, les corps de réponse, les erreurs et les limites de débit ne s'appliquent pas, sauf si un article de l'API Device Messaging y fait explicitement référence.

Utilisez la documentation des endpoints de l'API Device Messaging comme source de référence pour les champs de requête, les corps de réponse, les codes de statut et les limites.