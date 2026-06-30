---
nav_title: "Types de message"
article_title: Types de notifications push
page_order: 3
page_type: reference
description: "Cet article de référence répertorie les différents types de notifications push que vous pouvez envoyer avec Braze."
channel: push
---

# Types de notifications push {#push-message-types}

> Il existe de nombreux types de notifications push que vous pouvez utiliser pour interagir avec vos clients. Vous pouvez configurer la plupart de ces paramètres dans vos campagnes push, mais certains nécessitent des configurations backend comme indiqué dans les descriptions.

## Notification push standard {#standard-push}

La notification push classique par excellence. Elle apparaît sur l'appareil de l'utilisateur avec un son de notification et un message qui glisse ou s'affiche dans une barre ou une pile de notifications.

**Prise en charge :** Web, Android, iOS

Pour en savoir plus, consultez [Créer une notification push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).

## Notification push Web {#web-push}

Ces notifications push apparaissent dans les applications Web ou les navigateurs. Elles nécessitent l'autorisation de l'utilisateur. Les notifications push Web ne fonctionnent pas si l'utilisateur utilise un navigateur en mode privé.

**Prise en charge :** Web

Pour en savoir plus, consultez [Notifications push Web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web).

## Campagnes d'amorce push {#push-primer-campaigns}

Campagnes de messages in-app utilisées pour obtenir un signal explicite d'abonnement ou de désabonnement push de la part des utilisateurs. Grâce à l'amorce, vous pouvez éviter d'envoyer des notifications aux utilisateurs susceptibles de désactiver les notifications push via les paramètres de leur appareil. Pour iOS, les campagnes push sont pertinentes car les notifications push au premier plan (telles que les notifications qui réveillent l'appareil) ne sont pas activées tant que l'utilisateur n'a pas explicitement accepté l'invite push native d'iOS.

**Prise en charge :** Web, Android, iOS

Pour en savoir plus, consultez [Messages in-app d'amorce push]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Push Stories

Les Push Stories sont des messages immersifs qui guident l'utilisateur à travers un parcours visuel sous forme de carrousel. Elles sont disponibles uniquement sur les appareils mobiles.

**Prise en charge :** iOS, Android

Pour en savoir plus, consultez [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories).

## Notifications push avec boutons d'action {#push-with-action-buttons}

Les notifications push avec boutons d'action sont des messages qui vous permettent de proposer des options à vos utilisateurs et d'offrir plusieurs appels à l'action.

**Prise en charge :** Web, Android, iOS

Pour en savoir plus, consultez [Boutons d'action push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons).

## Notifications push riches {#rich-push-notifications}

Les notifications push riches sont des notifications avec des images immersives et du contenu créatif qui peuvent s'étendre au-delà d'une simple icône et d'un texte d'appel à l'action.

**Prise en charge :** iOS, Android

Pour en savoir plus, consultez [Créer des notifications riches pour iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications) ou [Créer des notifications riches pour Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications).

## Notifications push provisoires pour iOS {#provisional-push-notifications-for-ios}

Introduite par Apple dans iOS 12, l'autorisation provisoire s'effectue automatiquement lors de l'installation des applications iOS, permettant aux marques d'envoyer des notifications silencieuses sans afficher d'invite push aux utilisateurs. Lorsque la notification push silencieuse est envoyée et consultée dans le centre de notifications de l'appareil, les utilisateurs ont la possibilité d'autoriser ou de désactiver les notifications push.

**Prise en charge :** iOS

Pour en savoir plus, consultez [Options de notification iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push).

## Notifications push HTML {#html-push-notifications}

Les notifications push HTML sont des messages push codés en dur en HTML qui n'utilisent pas les modèles push prédéfinis fournis par Braze. La possibilité de créer des notifications push HTML offre à votre entreprise une liberté créative totale et une image de marque cohérente pour l'apparence de ces messages push.

**Prise en charge :** Android

## ID de notification et ID de canal {#notification-ids-and-channel-ids}

Les ID de notification et les ID de canal vous permettent de remplacer ou de mettre à jour des notifications push déjà reçues, mais pas encore ouvertes, par l'utilisateur.

**Prise en charge :** iOS, Android

Pour en savoir plus, consultez [Canaux de notification]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels) et [Paramètres avancés des campagnes push]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings).

## Notifications push en arrière-plan ou silencieuses {#background-push-notifications}

Notifications push qui ne s'affichent pas sur l'appareil. Elles sont généralement utilisées pour envoyer des paquets d'informations à l'application pour des processus en arrière-plan et le suivi des désinstallations. Un jeton de notification push compatible avec l'arrière-plan est requis pour envoyer une notification push en arrière-plan ou silencieuse.

**Prise en charge :** Web, Android, iOS

Pour en savoir plus, consultez [Notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent).

## Notifications push pour appareils connectés {#wearable-push-notifications}

Ces notifications push permettent aux marques d'envoyer des messages directement aux appareils connectés comme l'Apple Watch.

**Prise en charge :** iOS