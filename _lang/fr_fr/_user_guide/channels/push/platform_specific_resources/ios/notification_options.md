---
nav_title: "Options de notification"
article_title: Options de notification iOS
page_order: 2
page_layout: reference
description: "Cet article de référence couvre les options de notification iOS telles que les alertes critiques, les notifications silencieuses, les notifications push provisoires, et plus encore."

platform: iOS
channel:
  - push
---

# Options de notification {#notification-options}

> Avec la sortie d'iOS 12 d'Apple, Braze prend en charge plusieurs de ses fonctionnalités, notamment les [groupes de notifications](#notification-groups), les [notifications silencieuses/autorisation provisoire](#provisional-push-authentication--quiet-notifications) et les [alertes critiques](#critical-alerts).

## Groupes de notifications {#notification-groups}

Si vous souhaitez catégoriser vos messages et les regrouper dans le tiroir de notifications de votre utilisateur, vous pouvez utiliser la fonctionnalité Groupes de notifications d'iOS via Braze.

Créez votre Campaign push iOS, puis accédez à l'onglet **Paramètres** et ouvrez le menu déroulant **Groupe de notification**.

![L'onglet « Paramètres » avec un menu déroulant « Groupe de notification » dont la valeur sélectionnée est « Coupons ».]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

Sélectionnez vos groupes de notifications dans le menu déroulant. Si les paramètres de votre groupe de notification dysfonctionnent ou si vous sélectionnez **None** dans le menu déroulant, le message sera automatiquement envoyé normalement à tous les utilisateurs définis dans l'espace de travail.

Si vous n'avez aucun groupe de notification répertorié ici, vous pouvez en ajouter un à l'aide de l'iOS Thread ID. Vous aurez besoin d'un iOS Thread ID pour chaque groupe de notification que vous souhaitez ajouter. Ensuite, ajoutez-le à vos groupes de notifications en cliquant sur **Manage Notification Groups** dans le menu déroulant et en remplissant les champs requis dans la fenêtre **Manage iOS Push Notification Groups** qui apparaît.

![Fenêtre de gestion des groupes de notifications push iOS.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

Créez votre Campaign push iOS, puis regardez en haut du compositeur. Vous y trouverez un menu déroulant intitulé **Notification Groups**.

### Arguments de résumé {#summary-arguments}

En plus de regrouper les notifications par Thread IDs, Apple vous permet de modifier les résumés qui apparaissent lorsque les notifications sont regroupées. Les utilisateurs de Braze peuvent spécifier la catégorie du résumé, le nombre du résumé et l'argument du résumé lors de la composition d'une Campaign push à l'aide de notre outil.

{% alert tip %}
Notez que la manière dont les notifications avec le même Thread ID sont regroupées dans le tiroir de notifications est contrôlée par le système d'exploitation. iOS peut choisir d'afficher les notifications avec le même Thread ID séparément ou en groupes selon ce qu'il considère comme optimal.
{% endalert %}

Cochez la case **Alert Options** dans le **Push Composer**.

Ensuite, sélectionnez `summary-arg` et `summary-arg-count` comme clés et saisissez ces valeurs dans la colonne correspondante. Si vous ne définissez pas de valeur pour `summary-arg`, elle sera par défaut à 1.

### Catégories de résumé {#summary-categories}

Les catégories de résumé vous permettent de personnaliser l'ensemble du résumé qui apparaît lorsque les notifications sont regroupées. Vous pouvez créer et appliquer plusieurs catégories.

Pour utiliser une catégorie dans votre message, travaillez avec vos développeurs pour l'implémenter en utilisant l'exemple suivant :

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
Cela ne nécessitera pas de mise à jour du SDK.
{% endalert %}

{% alert tip %}
Notez que `%u` et `%@` sont des chaînes de formatage pour le nombre du résumé et l'argument du résumé, respectivement. Lorsque le résumé est affiché, ces marques substitutives seront remplacées par les valeurs de `summary-count` et `summary-arg`.
{% endalert %}

Une fois que cela est configuré dans votre application, utilisez la catégorie de résumé en cochant la case **Notification Buttons** et en sélectionnant **Enter Pre-registered iOS Category**.

Ensuite, saisissez l'identifiant de la catégorie de résumé que vous avez défini dans votre application.

### Authentification push provisoire et notifications silencieuses {#provisional-push}

Apple permet aux marques d'envoyer des notifications push silencieuses vers les centres de notifications de leurs utilisateurs avant qu'ils ne s'abonnent officiellement et explicitement, vous donnant ainsi la possibilité de démontrer la valeur de vos messages de manière anticipée. Tout ce que vous avez à faire est de [configurer les notifications push provisoires](#set-up-provisional-push-notifications) dans votre application, puis tout utilisateur disposant d'un jeton push provisoire recevra vos messages.

Contrairement à un jeton push iOS traditionnel, un jeton push provisoire agit comme un « laissez-passer d'essai » qui permet aux marques de contacter de nouveaux utilisateurs avant qu'ils n'aient vu et cliqué sur l'invite native d'abonnement push d'Apple. Avec cette fonctionnalité, votre notification push sera livrée directement dans le tiroir de notifications de votre nouvel utilisateur avec l'option de « Conserver » ou « Désactiver » les futures notifications. Au lieu de vivre un parcours d'« abonnement », les utilisateurs vivront quelque chose qui s'apparente davantage à un parcours de « désabonnement ».

{% alert tip %}
L'autorisation provisoire a le potentiel d'augmenter considérablement votre taux d'abonnement, mais uniquement si les utilisateurs trouvent de la valeur dans vos messages. Assurez-vous d'utiliser nos fonctionnalités de [segmentation des utilisateurs]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), de [ciblage géographique]({{site.baseurl}}/user_guide/audience/locations_and_geofences) et de [personnalisation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) pour vous assurer que les utilisateurs appropriés reçoivent ces notifications « d'essai » au bon moment. Ensuite, vous pouvez encourager les utilisateurs à s'abonner pleinement à vos notifications push, sachant qu'elles ajoutent de la valeur à leur expérience avec votre application.
{% endalert %}

Quelle que soit l'option choisie par l'utilisateur, le jeton approprié ou le [statut d'abonnement]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states) sera ajouté à ses [Paramètres de contact]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#engagement-tab) sous l'onglet **Engagement** de son profil utilisateur.

![Paramètres de contact avec un statut d'abonnement push.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

Vous pourrez cibler vos utilisateurs selon qu'ils sont provisoirement autorisés ou non à l'aide de nos [filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

![Panneau de détails du Segment avec l'exemple de filtre de segmentation « Provisionally Authorized on iOS Stopwatch (iOS) is true » pour cibler les utilisateurs.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
Si les utilisateurs choisissent de « désactiver » les notifications push provisoires de votre part, ils ne verront plus aucun message push provisoire de votre part. Soyez attentif au contenu des messages et à la cadence d'envoi avec cette fonctionnalité !
{% endalert %}

{% alert important %}
Si vous utilisez des invites push supplémentaires ou des [primers push in-app](https://www.braze.com/resources/glossary/priming-for-push/) (un message in-app qui encourage les utilisateurs à s'abonner aux notifications push), contactez votre conseiller Braze pour obtenir des conseils supplémentaires.
{% endalert %}

#### Configurer les notifications push provisoires {#set-up-provisional-push-notifications}

Braze vous permet de vous inscrire à l'authentification provisoire en mettant à jour votre code dans l'extrait d'enregistrement de jeton au sein de votre déploiement du SDK iOS de Braze en utilisant les extraits de code suivants comme exemple (envoyez-les à vos développeurs ou assurez-vous qu'ils [implémentent l'authentification push provisoire durant le processus d'intégration]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)).

{% alert warning %}
Le déploiement de l'authentification push provisoire ne prend en charge qu'iOS 12+ et générera une erreur si la cible de déploiement est antérieure. Vous pouvez en apprendre davantage à ce sujet [dans notre documentation de déploiement plus détaillée ici]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift).
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### Niveau d'interruption (iOS 15+) {#interruption-level}

Avec le nouveau mode Concentration d'iOS 15, les utilisateurs ont davantage de contrôle sur le moment où les notifications des applications peuvent les « interrompre » avec un son ou une vibration.

![Page des paramètres de notification iOS montrant les notifications activées pour la réception immédiate et les notifications urgentes activées.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

Les applications peuvent désormais spécifier le niveau d'interruption qu'une notification doit inclure, en fonction de son urgence.

Pour modifier le niveau d'interruption d'une notification push iOS, sélectionnez l'onglet **Paramètres** et choisissez le niveau souhaité dans le menu déroulant **Interruption Level**.

![Menu déroulant de sélection du niveau d'interruption.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

Cette fonctionnalité n'a pas d'exigence minimale en termes de version de SDK, mais ne s'applique qu'aux appareils exécutant iOS 15+.

Gardez à l'esprit que les utilisateurs sont en fin de compte ceux qui contrôlent leur mode Concentration, et même si une notification urgente est livrée, ils peuvent spécifier quelles applications ne sont pas autorisées à passer outre leur mode Concentration.

Consultez le tableau suivant pour les niveaux d'interruption et leurs descriptions.

| Niveau d'interruption | Description | Quand l'utiliser | Passe outre le mode Concentration |
|--|--|--|--|
| [Passive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive) | Envoie une notification sans son, vibration ni activation de l'écran. | Notifications qui ne nécessitent pas d'attention immédiate. | Non |
| [Active](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (par défaut) | Produira un son, une vibration et activera l'écran uniquement si l'utilisateur n'est pas en mode Concentration. | Notifications nécessitant une attention immédiate, sauf si l'utilisateur a activé le mode Concentration. | Non |
| [Time Sensitive](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive) | Produira un son, une vibration et activera l'écran même en mode Concentration. Cela nécessite que la **capacité Time Sensitive Notifications** soit ajoutée à votre application dans Xcode. | Notifications urgentes qui doivent alerter les utilisateurs quel que soit leur mode Concentration, comme une notification de covoiturage ou de livraison. | Oui |
| [Critical](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical) | Produira un son, une vibration et activera l'écran même si le commutateur **Ne pas déranger** du téléphone est activé. Cela [nécessite une approbation explicite d'Apple](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/). | Urgences telles que les alertes météorologiques graves ou les alertes de sécurité. | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Niveau d'interruption (iOS 15+)" }

### Score de pertinence (iOS 15+) {#relevance-score}

![Un résumé de notifications pour iOS intitulé « Your Evening Summary » avec trois notifications.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15 introduit également une nouvelle façon pour les utilisateurs de planifier optionnellement un regroupement digest de plusieurs notifications à des moments désignés tout au long de la journée. Cela permet d'éviter les interruptions constantes tout au long de la journée pour les notifications qui ne nécessitent pas d'attention immédiate.

Les applications peuvent spécifier quelles notifications push sont les plus pertinentes en définissant un **score de pertinence**. Apple utilisera ce score pour déterminer quelles notifications doivent être mises en avant dans le résumé de notifications planifié tandis que les autres seront disponibles lorsque les utilisateurs cliqueront sur le résumé.

Toutes les notifications resteront accessibles dans le centre de notifications de l'utilisateur.

Pour définir le score de pertinence d'une notification iOS, saisissez une valeur entre `0.0` et `1.0` dans l'onglet **Paramètres**. Par exemple, le message le plus important doit être envoyé avec `1.0`, tandis qu'un message d'importance moyenne peut être envoyé avec `0.5`.

![Score de pertinence de « 0.5 ».]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

Cette fonctionnalité n'a pas d'exigence minimale en termes de version de SDK, mais ne s'applique qu'aux appareils exécutant iOS 15+.

Pour plus d'informations sur les longueurs maximales de messages pour les différents types de messages, consultez les ressources suivantes :

- [Spécifications des images et du texte]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)
- [Directives relatives au nombre de caractères iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications#character-count)