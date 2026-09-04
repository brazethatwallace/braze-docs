---
nav_title: Clés API et identifiants
article_title: Clés API et identifiants
page_order: 0
page_type: reference
description: "Cet article présente la page Clés API et identifiants, qui affiche les identifiants API de votre espace de travail."
---

# Clés API {#api-keys}

> La page **Clés API et identifiants** est votre hub centralisé pour gérer toutes vos clés REST API en un seul endroit. Vous pouvez y accéder à l'ensemble des clés API et des identifiants d'application de chaque espace de travail.

La page **Clés API et identifiants** se trouve sous **Paramètres**.

## Clés API

Cette section fournit les clés REST API de votre espace de travail, les identifiants uniques qui vous permettent d'accéder aux données d'un espace de travail. Une clé REST API est requise pour chaque requête envoyée à l'API Braze. Pour en savoir plus sur la création et l'utilisation des clés API, consultez notre [aperçu des clés REST API]({{site.baseurl}}/api/basics).

### Liste d'autorisation d'adresses IP pour l'API {#api-ip-allowlisting}

Pour renforcer la sécurité, vous pouvez spécifier une liste d'adresses IP et de sous-réseaux autorisés à effectuer des requêtes REST API pour une clé REST API donnée. C'est ce qu'on appelle la liste d'autorisation (allowlisting ou whitelisting). Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les dans la section **Whitelist IPs** lors de la création d'une nouvelle clé REST API :

![Section de liste d'autorisation d'adresses IP lors de la création d'une nouvelle clé API]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si vous n'en spécifiez aucune, les requêtes pourront être envoyées depuis n'importe quelle adresse IP.

{% alert tip %}
Vous créez un webhook Braze-vers-Braze avec une liste d'autorisation ? Consultez notre liste d'[adresses IP à autoriser]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting).
{% endalert %}

### Alertes d'utilisation de l'API {#api-usage-alerts}

Configurez des alertes d'utilisation de l'API pour surveiller l'activité clé de l'API et détecter les problèmes rapidement. Ces alertes vous aident à repérer des schémas de trafic inhabituels avant qu'ils n'impactent votre expérience.

Vous pouvez suivre deux types d'activité API :

- **Endpoints REST API :** Actions telles que l'envoi de messages, la création de Campaigns ou l'exportation de données.
- **Requêtes API du SDK :** Événements provenant de votre expérience client, comme le déclenchement de messages in-app ou la synchronisation de profils utilisateur. *Cette fonctionnalité est disponible si vous avez acheté les Utilisateurs actifs mensuels (CY 24–25).*

Une fois que vous avez choisi ce que vous souhaitez suivre, vous pouvez définir les conditions d'alerte. Par exemple, être notifié si les réponses d'erreur augmentent de 20 % en une heure. Vous recevrez une notification par e-mail, webhook, ou les deux, selon vos paramètres. Pour commencer, consultez [Alertes d'utilisation de l'API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts).

## Identifiants d'application {#app-identifiers}

Cette section comprend une liste d'identifiants utilisés pour référencer des applications spécifiques dans les requêtes envoyées à l'API Braze. Pour en savoir plus sur les identifiants d'application, consultez [Clé API d'identifiant d'application]({{site.baseurl}}/api/identifier_types).

## Autres identifiants {#other-identifiers}

Pour intégrer notre API, vous pouvez rechercher les identifiants liés à n'importe quels Segments, Campaigns, Content Cards et plus encore, auxquels vous souhaitez accéder depuis l'API externe de Braze. Tous les messages doivent suivre l'encodage [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Après avoir sélectionné l'un d'entre eux, l'identifiant s'affichera sous le menu déroulant.

Pour en savoir plus, consultez [Types d'identifiants API]({{site.baseurl}}/api/identifier_types).