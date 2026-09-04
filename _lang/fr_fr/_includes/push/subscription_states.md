## Statuts d'abonnement aux notifications push {#push-sub-states}

Un « état d'abonnement push » dans Braze identifie la préférence globale d'un **utilisateur** quant à son souhait de recevoir des notifications push. Étant donné que le statut d'abonnement est basé sur l'utilisateur, il n'est pas spécifique à une application donnée. Les états d'abonnement deviennent des indicateurs utiles lorsque vous décidez quels utilisateurs cibler avec les notifications push.

{% alert note %}
L'état d'abonnement aux notifications push d'un utilisateur s'applique à l'ensemble de son profil utilisateur, ce qui inclut tous les appareils de celui-ci.
{% endalert %}

Les options d'état d'abonnement suivantes sont disponibles : `Subscribed`, `Opted-In` et `Unsubscribed`.

Par défaut, pour que vos utilisateurs puissent recevoir vos messages via des notifications push, leur statut d'abonnement aux notifications push doit être `Subscribed` ou `Opted-In`, et les notifications push en avant-plan doivent être activées. Vous pouvez remplacer cette configuration si nécessaire lors de la rédaction d'un message.

| État d'abonnement | Description |
|---|---|
| `Subscribed` | État d'abonnement aux notifications push par défaut lorsqu'un profil utilisateur est créé dans Braze. |
| `Opted-In` | Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Braze modifie automatiquement le statut d'abonnement d'un utilisateur à `Opted-In` si l'utilisateur accepte une invite push au niveau du système d'exploitation.<br><br>Ceci ne s'applique pas aux utilisateurs d'Android 12 ou antérieur. |
| `Unsubscribed` | Un utilisateur s'est explicitement désabonné des notifications push par le biais de votre application ou d'autres méthodes fournies par votre marque. Par défaut, les Campaigns push de Braze ciblent uniquement les utilisateurs qui sont `Subscribed` ou `Opted-in` pour les notifications push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement aux notifications push" }

{% alert important %}
Braze ne change pas automatiquement le statut d'abonnement aux notifications push d'un utilisateur vers `Unsubscribed`. Veuillez noter que si l'état d'abonnement push d'un utilisateur est `Unsubscribed`, alors le filtre `Foreground Push Enabled` de l'utilisateur dans la segmentation est `false`.
{% endalert %}

### Enregistrement push et utilisateurs pouvant être atteints {#push-registration-and-reachable-users}

L'état d'abonnement push reflète la préférence d'un utilisateur, mais le fait qu'il soit compté comme **pouvant être atteint** pour les notifications push dans le tableau de bord dépend également de l'[enregistrement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle), c'est-à-dire de la présence d'un jeton de notification push en avant-plan valide sur son profil. Pour savoir comment Braze calcule les comptages au niveau des canaux, consultez [Mesurer la taille d'un Segment]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

- **Campaigns push et Canvas :** Les utilisateurs qui ne sont pas enregistrés pour les notifications push ne sont pas inclus dans les **Utilisateurs pouvant être atteints** pour les notifications push Android ou iOS dans les statistiques d'audience, même si leur état d'abonnement push est `Subscribed` ou `Opted-In`.
- **Autres canaux :** Ces mêmes utilisateurs peuvent toujours être comptés comme pouvant être atteints pour d'autres canaux auxquels ils sont éligibles (par exemple, les e-mails ou les messages in-app).
- **Segments :** L'appartenance à un Segment suit vos filtres. Les utilisateurs sans enregistrement push restent dans le Segment à moins qu'un filtre ne les exclue (par exemple, **Foreground Push Enabled**). Le nombre total de membres d'un Segment peut être supérieur à la somme des utilisateurs affichés dans les lignes **Utilisateurs pouvant être atteints** spécifiques aux notifications push.

Un profil utilisateur peut afficher un état d'abonnement push `Subscribed` alors qu'aucun jeton de notification push n'est attribué. Ces utilisateurs ne sont toujours pas comptabilisés dans les **Utilisateurs pouvant être atteints** pour les notifications push Android ou iOS tant que Braze n'a pas enregistré un jeton valide.

Pour les définitions des filtres, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Mise à jour des états d'abonnement aux notifications push {#update-push-subscription-state}

Voici les différentes méthodes pour mettre à jour l'état d'abonnement push d'un utilisateur :

#### Abonnement automatique (par défaut) {#automatic-opt-in-default}

Par défaut, Braze définit l'état d'abonnement push d'un utilisateur sur `Opted-In` lorsqu'il autorise pour la première fois les notifications push pour votre application. Braze procède également de la sorte lorsqu'un utilisateur réactive les autorisations push dans les paramètres de son système après les avoir précédemment désactivées.

{% tabs local %}
{% tab android %}
Pour désactiver ce comportement par défaut, ajoutez la propriété suivante au fichier `braze.xml` de votre projet Android Studio :

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
Sur iOS, une nouvelle installation affiche généralement l'état d'abonnement push **`Subscribed`** jusqu'à ce que l'utilisateur autorise les notifications. Après que l'utilisateur a sélectionné **Autoriser** dans l'invite du système d'exploitation, Braze définit l'état sur **`Opted-In`** lorsque l'abonnement automatique est activé. Si l'utilisateur sélectionne **Ne pas autoriser** et active ensuite les notifications push dans les réglages iOS, l'état est mis à jour après que l'utilisateur a enregistré une session, et non au moment où il modifie les réglages.

À partir de la [version 7.5.0 du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), vous pouvez désactiver ou personnaliser davantage ce comportement en ajoutant la configuration `optInWhenPushAuthorized` au fichier `AppDelegate.swift` de votre projet Xcode :

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Intégration SDK {#sdk-integration}

Vous pouvez mettre à jour l'état d'abonnement d'un utilisateur avec le SDK de Braze à l'aide de la méthode `setPushNotificationSubscriptionType` sur le [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) ou [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Par exemple, vous pouvez utiliser cette méthode pour créer une page de paramètres dans votre application où les utilisateurs peuvent activer ou désactiver manuellement les notifications push.

#### REST API

Vous pouvez mettre à jour l'état d'abonnement d'un utilisateur avec la REST API de Braze en utilisant l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) pour mettre à jour l'attribut [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object).

### Différences entre l'activation push et l'état d'abonnement push {#differences-between-push-enablement-and-push-subscription-status}

L'activation push indique si un utilisateur a accordé l'autorisation au niveau du système d'exploitation ou du navigateur de recevoir des notifications sur un appareil spécifique. L'état d'abonnement push est un paramètre au niveau de Braze qui représente la préférence globale d'un utilisateur pour la réception de notifications push sur l'ensemble de son profil.

Lorsque l'abonnement automatique est activé (comportement par défaut), Braze met à jour l'état d'abonnement push d'un utilisateur à `Opted-In` lorsqu'il autorise les notifications push pour votre application ou réactive les autorisations dans les paramètres de son système (par exemple, sur iOS, Android 13+ et les navigateurs web pris en charge). Dans le cas contraire, l'état d'abonnement push de l'utilisateur reste `Subscribed` jusqu'à ce que vous le modifiiez explicitement à l'aide d'une méthode SDK ou d'un appel à la REST API.

Braze ne change pas automatiquement l'état d'abonnement push d'un utilisateur à `Unsubscribed` lorsqu'il désactive les notifications au niveau du système d'exploitation, du navigateur ou de l'application. Pour mettre à jour l'état d'abonnement push d'un utilisateur, vous devez le modifier dans Braze. Par exemple, si un utilisateur désactive les notifications push depuis un centre de préférences in-app, mettez à jour l'état d'abonnement push à `Unsubscribed` dans Braze. Braze ne met pas à jour les profils utilisateurs en fonction de votre centre de préférences. Pour aligner les états d'abonnement avec les préférences in-app d'un utilisateur, appelez les méthodes appropriées à l'aide du SDK (iOS ou Android) ou de la REST API. Pour en savoir plus, consultez [Mise à jour des états d'abonnement aux notifications push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state).

### Jetons de notification push importés (iOS) {#imported-push-tokens-ios}

Lorsque vous [importez des jetons de notification push iOS]({{site.baseurl}}/api/objects_filters/user_attributes_object#push-token-import) avec `push_token_import`, l'état d'abonnement push de l'utilisateur est généralement **`Subscribed`** jusqu'à ce qu'il enregistre une session dans votre application intégrée à Braze. Après la première session, Braze peut mettre à jour l'état à **`Opted-In`** si l'[abonnement automatique](#automatic-opt-in-default) s'applique (par exemple, lorsque l'utilisateur autorise les notifications push sur iOS et que `optInWhenPushAuthorized` est activé).

Vérifiez les **paramètres de contact** sur le profil de l'utilisateur après l'importation, puis à nouveau après la première session in-app de l'utilisateur, pour confirmer l'état attendu.

### Vérification de l'état d'abonnement aux notifications push {#checking-push-subscription-state}

![Profil utilisateur de John Doe dont l'état d'abonnement push est défini sur Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez vérifier l'état d'abonnement push d'un utilisateur avec Braze de l'une des manières suivantes :

* **Profil utilisateur :** Vous pouvez accéder aux profils utilisateurs individuels via le tableau de bord de Braze sur la page **[Recherche d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)**. Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID utilisateur externe), vous pouvez sélectionner l'onglet **Engagement** pour afficher et ajuster manuellement l'état d'abonnement d'un utilisateur.
* **Exportation via la REST API :** Vous pouvez exporter des profils utilisateurs individuels au format JSON à l'aide des endpoints d'exportation [Utilisateurs par Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) ou [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). Braze renvoie un objet de jetons de notification push contenant les informations d'activation push par appareil.