---
nav_title: Distribution en temps réel des messages in-app
article_title: Distribution en temps réel des messages in-app
permalink: "/real_time_in_app_messages/"
description: "Cette page présente l'accès anticipé à la distribution en temps réel des messages in-app, qui envoie les messages in-app à un appareil dès qu'un utilisateur devient éligible, sans attendre le début de la session suivante."
page_type: reference
hidden: true
noindex: true
---

# Distribution en temps réel des messages in-app {#real-time-in-app-message-delivery}

> Avec la distribution en temps réel, Braze envoie un message in-app à l'appareil dès que l'utilisateur devient éligible. Les utilisateurs n'ont plus besoin de démarrer une nouvelle session pour recevoir un message in-app pour lequel ils sont devenus éligibles en cours de session.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Real-time in-app message delivery' type='early_access' %}

## Fonctionnement {#how-it-works}

Sans la distribution en temps réel, le SDK demande les messages in-app éligibles au démarrage de la session et les met en cache sur l'appareil. Un utilisateur qui devient éligible en cours de session ne reçoit le message qu'au début de la session suivante. Pour plus d'informations sur ce comportement, consultez [Déclencher des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages).

Avec la distribution en temps réel, Braze envoie le message à l'appareil via une connexion en direct or en ligne/en production/instantané que le SDK maintient pendant la session. Braze envoie un message dans deux cas :

- Un utilisateur devient éligible pour une campagne de message in-app.
- Un utilisateur atteint une étape de message in-app dans un Canvas.

La distribution en temps réel modifie le moment où un message atteint l'appareil. Le comportement d'affichage reste identique : le message attend son événement déclencheur avant d'apparaître.

### Ce que cela signifie pour vos campagnes {#what-this-means-for-your-campaigns}

| Scénario | Sans distribution en temps réel | Avec distribution en temps réel |
| --- | --- | --- |
| Un utilisateur devient éligible pour une campagne de message in-app en cours de session | Le message arrive au début de la session suivante | Le message arrive pendant la session en cours |
| Un utilisateur atteint une étape de message in-app dans un Canvas en cours de session | Le message arrive au début de la session suivante | Le message arrive pendant la session en cours |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comparaison de la distribution en temps réel des messages in-app" }

## Versions SDK requises {#sdk-requirements}

La distribution en temps réel nécessite les versions SDK minimales suivantes :

{% sdk_min_versions swift:18.0.0 android:43.1.1 %}

Les appareils continuent de recevoir les messages in-app au démarrage de la session, quelle que soit la version du SDK.

## Limitations actuelles {#current-limitations}

- **Le SDK Web n'est pas encore pris en charge :** la distribution en temps réel est disponible pour les SDK Swift et Android pendant l'accès anticipé.
- **Les modifications d'une campagne en cours s'appliquent au début de la session suivante :** si vous modifiez un message in-app qu'un appareil a déjà reçu, cet appareil conserve la version qu'il possède jusqu'au début de la session suivante de l'utilisateur.

## Participer à l'accès anticipé {#participate-in-early-access}

1. Contactez votre gestionnaire de compte Braze pour que votre espace de travail soit ajouté à l'accès anticipé.
2. Mettez à jour votre application vers la version SDK minimale pour votre plateforme.
3. Publiez l'application mise à jour auprès de vos utilisateurs.

La distribution en temps réel ne nécessite aucune configuration du tableau de bord, aucune modification de campagne ni aucune modification du code SDK. Une fois votre espace de travail ajouté à l'accès anticipé, la distribution en temps réel s'applique à vos campagnes de messages in-app et à vos Canvas existants.

## Partagez vos retours {#share-feedback}

Braze développe activement cette fonctionnalité, et vos retours influencent ce qui sera livré en disponibilité générale. Envoyez à votre gestionnaire de compte vos observations sur les délais de distribution, tout comportement différent de celui attendu, et les scénarios que vous aimeriez voir couverts par la distribution en temps réel.