---
nav_title: Intégration multi-domaine
article_title: Intégration multi-domaine pour le SDK Web de Braze
platform: Web
page_order: 23
page_type: reference
description: "Découvrez comment déployer le SDK Web de Braze sur plusieurs domaines, y compris la stratégie de clé API, la configuration push et le comportement des sessions."
---

# Intégration multi-domaine {#multi-domain-integration}

> Découvrez comment intégrer le SDK Web de Braze sur plusieurs domaines web.

Lorsque votre déploiement s'étend sur plusieurs domaines, les limites d'origine du navigateur affectent la manière dont le SDK Web de Braze stocke et lit l'état utilisateur.

## Choisir une stratégie d'application et de clé API {#choose-an-app-and-api-key-strategy}

Vous pouvez utiliser une seule clé API du SDK Web sur plusieurs domaines, mais dans la plupart des cas, l'utilisation de clés API distinctes associées à des applications séparées dans le même workspace vous offre un meilleur contrôle.

| Stratégie | Recommandée quand | Compromis |
|---|---|---|
| **Applications séparées (recommandé)** | Vous souhaitez un ciblage, un reporting et un contrôle de Campaign indépendants par domaine | Nécessite la gestion de deux intégrations d'applications |
| **Application unique** | Vous traitez les deux domaines comme une seule propriété sur le plan opérationnel | Les déclencheurs de session et le reporting par domaine sont plus difficiles à séparer |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Options de stratégie d'application et de clé API" }

Avec des applications séparées dans un même workspace, vous pouvez utiliser des filtres d'application pour une segmentation et un ciblage de messages plus précis par domaine.

## Configurer les notifications push sur un seul domaine {#configure-push-notifications-on-one-domain}

Pour des domaines racine distincts, l'enregistrement des notifications push Web est isolé par domaine.

- Choisissez un domaine comme domaine de notification push.
- N'enregistrez pas les notifications push sur les deux domaines racine pour le même parcours utilisateur, car cela peut créer des comportements conflictuels d'invite et d'abonnement.

## Identifier les utilisateurs de manière cohérente entre les domaines {#identify-users-consistently-across-domains}

Par défaut, chaque domaine racine stocke son propre état SDK. Pour associer l'activité au même profil utilisateur Braze entre les domaines :

- Appelez [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) avec le même `external_id` sur chaque domaine après la connexion.
- Conservez les deux applications dans le même workspace si vous utilisez des clés API séparées.

Pour des conseils généraux sur les ID utilisateur, consultez [Définir les ID utilisateur via le SDK de Braze]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## Planifier le comportement des événements et des déclencheurs par domaine {#plan-event-and-trigger-behavior-by-domain}

La manière dont vous modélisez les événements et les déclencheurs dépend de votre stratégie d'application :

- **Application unique sur plusieurs domaines :** Enregistrez des événements personnalisés spécifiques au domaine afin de pouvoir distinguer le comportement par site dans la segmentation et le déclenchement.
- **Applications séparées :** Privilégiez les filtres d'application pour le ciblage et l'analyse spécifiques au domaine.

## Comprendre le comportement des sessions entre les domaines {#understand-session-behavior-across-domains}

Par défaut, le délai d'expiration de session du SDK Web est de 30 minutes d'inactivité. Pour des domaines racine distincts utilisant une seule application/clé API :

- Chaque domaine démarre et termine les sessions de manière indépendante.
- Un utilisateur naviguant entre les deux domaines peut créer des sessions qui se chevauchent.
- Les déclencheurs de début de session peuvent se déclencher sur les deux domaines.

Pour plus de détails sur le cycle de vie des sessions, consultez [Suivre les sessions via le SDK de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).