---
nav_title: septembre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2020."
---

# Septembre {#september}

## Rapports d'entonnoir {#funnel-reporting}

Le rapport d'entonnoir offre un rapport visuel qui vous permet d'analyser les parcours de vos clients après avoir reçu une [campagne]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) ou un [Canvas]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/).

## Guide de mise à niveau iOS 14 {#ios-14-upgrade-guide}

Conformément aux modifications annoncées dans la nouvelle version iOS 14 d'Apple, certains changements et éléments d'action liés à Braze sont requis pour les intégrations du SDK iOS de Braze. Pour plus d'informations, consultez ce [guide de mise à niveau]({{site.baseurl}}/ios_14/).

## Modifications apportées à IDFA et IDFV pour iOS 14 {#changes-to-idfa-and-idfv-for-ios-14}

Dans iOS 14, les utilisateurs doivent décider s'ils souhaitent s'abonner au suivi publicitaire et laisser les applications et les réseaux publicitaires lire leur IDFA lorsqu'ils visitent une application. Par conséquent, la stratégie de Braze consiste à utiliser plutôt l'« identifiant pour les fournisseurs » (tel que l'IDFV) afin que vous puissiez continuer à suivre les utilisateurs sur différents appareils. Pour plus d'informations, consultez le [guide de mise à niveau d'iOS 14]({{site.baseurl}}/ios_14/).

## Validation de l'e-mail {#email-validation}

Ce nouveau processus de validation de syntaxe d'e-mail est une mise à niveau du processus existant de Braze. Il permet de vérifier que les adresses e-mail mises à jour ou importées dans Braze sont correctes. Pour plus d'informations, consultez [ces lignes directrices et notes]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/).

## Événement utilisateur de numéro de compartiment aléatoire dans Currents {#random-bucket-user-event-in-currents}

Le numéro de compartiment aléatoire (tel que RBN) est généré chaque fois qu'un nouvel utilisateur est créé dans son espace de travail. Au cours de cet événement, chaque nouvel utilisateur reçoit un numéro de compartiment aléatoire que vous pouvez ensuite utiliser pour créer des segments d'utilisateurs aléatoires distribués uniformément. Utilisez cette option pour regrouper une série de valeurs de numéro de compartiment aléatoire et comparer les performances à travers vos campagnes et variantes de campagne. Pour savoir si cet événement est disponible pour vous, consultez le [glossaire des événements de comportement des clients]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) de Currents.

## Composants Canvas — Prochainement ! {#canvas-components-coming-soon}

Braze a ajouté quatre nouveaux composants Canvas pour améliorer la flexibilité et la fonctionnalité de vos Canvas. Ces nouveaux composants comprennent : [Étape d'arbre décisionnel]({{site.baseurl}}/decision_split/), [Étape de délai]({{site.baseurl}}/delay_step/), [Étapes d'envoi de messages]({{site.baseurl}}/message_step/) et [Synchronisation de l'audience vers Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Étapes d'arbre décisionnel, de délai et d'envoi de messages dans Canvas**<br>Les arbres décisionnels peuvent être utilisés pour créer des branches Canvas selon qu'un utilisateur corresponde ou non à une requête définie. Les étapes de délai vous permettent d'ajouter un délai distinct à votre Canvas sans avoir besoin d'un message correspondant. Les étapes de message vous permettent d'ajouter un message indépendant où vous le souhaitez dans votre flux Canvas.
- **Synchronisation de l'audience vers Facebook**<br>Grâce à la synchronisation de l'audience Braze vers Facebook, les marques peuvent choisir d'ajouter les données de leurs propres utilisateurs à partir de leur intégration Braze aux audiences personnalisées Facebook Custom Audiences afin de diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore. Tous les critères que vous utilisez habituellement pour déclencher un message (push, e-mail, SMS, webhook, etc.) dans un Canvas Braze en fonction de vos données utilisateur peuvent désormais être utilisés pour déclencher une publicité destinée à cet utilisateur dans Facebook via Custom Audiences.

## Événements de réception de SMS entrants {#sms-inbound-received-events}

Un nouvel événement d'engagement de messagerie a été ajouté à Currents. Cet événement se produit lorsque l'un de vos utilisateurs envoie un SMS à un numéro de téléphone dans l'un de vos groupes d'abonnement SMS Braze. Pour plus d'informations, consultez le [glossaire Currents des événements d'envoi de messages et d'engagement]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).