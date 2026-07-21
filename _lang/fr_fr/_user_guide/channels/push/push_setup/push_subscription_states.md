---
nav_title: "États d'abonnement push"
article_title: "États d'abonnement push"
page_order: 2
page_type: reference
description: "Cet article de référence couvre les concepts d'activation push et d'états d'abonnement push dans Braze, y compris les différences fondamentales de comportement entre iOS, Android et le Web."
channel:
  - push

---

# Activation push et abonnement push {#push-enablement-and-push-subscription}

> Cet article de référence couvre les concepts d'activation push et d'états d'abonnement push dans Braze, y compris les différences fondamentales de comportement entre iOS, Android et le Web.

{% multi_lang_include push/subscription_states.md %}

## Où apparaissent l'enregistrement et le statut push {#where-push-registration-and-status-appear}

Vous pouvez consulter l'état d'abonnement push, l'enregistrement et l'activation à trois endroits principaux dans Braze :

1. **[Profils utilisateurs](#user-profiles-and-push-changelog)** dans l'onglet **Engagement**
2. **[Segmentation](#segmentation-and-push-filters)** dans le générateur de segments
3. **[Analyse de Campaign et Canvas](#campaign-and-canvas-analytics)** sur la page d'analyse de chaque message

### Profils utilisateurs et journal des modifications push {#user-profiles-and-push-changelog}

Sur le profil d'un utilisateur ([**Rechercher des utilisateurs**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) > sélectionnez l'utilisateur > onglet **Engagement**), **Contact Settings** liste l'état d'abonnement push, **Push Registered For** (les applications et plateformes que Braze peut utiliser pour envoyer des notifications push au premier plan à ce profil), et le **Push Changelog** pour les transferts de jetons, les erreurs et les mises à jour d'enregistrement. Pour savoir comment lire **Push Registered For** et l'autorisation au premier plan par rapport à l'arrière-plan, consultez [Vérifier le statut d'enregistrement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status).

Sur iOS et Android, lorsqu'un appareil passe de l'autorisation push au premier plan à l'arrière-plan uniquement (par exemple, après que l'utilisateur a désactivé les notifications dans les paramètres système et que le SDK signale le changement), le journal des modifications push peut inclure une entrée telle que « Push token was updated from foreground push enabled to foreground push disabled ».

Après avoir attendu de nouvelles données SDK (par exemple, juste après une session de test), sélectionnez **Refresh** sur le profil utilisateur si les valeurs semblent obsolètes. Il peut y avoir un court délai entre le moment où le SDK envoie les données et celui où le profil reflète le dernier enregistrement push.

Pour les utilisateurs que vous ajoutez à un [groupe interne]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), sélectionnez **Record User Events for group members** dans les **Internal Group Settings** de ce groupe afin que les requêtes SDK apparaissent dans le journal. Ouvrez ensuite le [Journal des événements utilisateurs]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) dans **Paramètres** > **Event User Log**, trouvez les requêtes SDK de l'utilisateur et développez le payload brut. Vous pouvez inspecter des champs tels que `remote_notification_enabled` pour vérifier si l'appareil signale les notifications distantes comme activées ou désactivées.

### Segmentation et filtres push {#segmentation-and-push-filters}

Dans le générateur de segments, utilisez des filtres tels que **`Foreground Push Enabled`**, **`Foreground Push Enabled for App`**, **`Background or Foreground Push Enabled`**, et les filtres d'abonnement push pour cibler ou auditer les utilisateurs par préférence et autorisation au niveau de l'appareil. Sur iOS, la façon dont ces filtres s'appliquent à un utilisateur donné dépend du fait qu'il ait complété l'invite de l'OS, modifié ses paramètres, ou qu'il utilise l'[autorisation provisoire](#provisional-push) ; consultez [Actions utilisateur iOS et statut push](#ios-user-actions-push-status) et [Autres scénarios spécifiques aux plateformes](#foreground-push-enabled).

### Analyse de Campaign et Canvas {#campaign-and-canvas-analytics}

Sur la page d'analyse d'une **Campaign** ou d'un **Canvas** push, des indicateurs tels que *Envoyés*, *Rebonds* et *Ouvertures* reflètent la distribution et l'engagement pour cet envoi. Pour rapprocher ces chiffres des profils individuels, exportez les destinataires depuis **Campaign Details** ou **Canvas Details** en utilisant **User Data** (CSV). Pour les étapes et les autorisations, consultez [Exporter les données de Campaign]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data) et [Exporter les données Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data). Si les chiffres entre l'analyse et un export ne correspondent pas, consultez [Analyse de Campaign et Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting#campaign-and-canvas-analytics) dans la résolution des problèmes d'export.

## Actions utilisateur iOS et statut push {#ios-user-actions-push-status}

Le tableau suivant montre comment différentes actions utilisateur affectent l'activation push iOS, l'enregistrement push au premier plan ou en arrière-plan, et le statut d'abonnement push dans Braze. Lorsqu'un utilisateur installe votre application et démarre sa première session, son état est généralement celui indiqué dans la première ligne. Chaque action ultérieure peut mettre à jour certaines de ces valeurs mais pas d'autres.

| Action utilisateur | `Foreground Push Enabled` | `Foreground Push Enabled for App` | Type d'enregistrement push | Statut d'abonnement push |
| --- | --- | --- | --- | --- |
| L'utilisateur installe l'application et enregistre une session | `false`* | Non mis à jour | Arrière-plan | `Subscribed` |
| L'utilisateur reçoit l'invite push native iOS et sélectionne **Allow** | `true` | `true` | Premier plan | `Opted-In`** |
| L'utilisateur reçoit l'invite push native iOS et sélectionne **Don't Allow** | `false` | Non mis à jour | Arrière-plan | Non mis à jour |
| L'utilisateur active les notifications push depuis les paramètres de l'appareil et enregistre une session | `true` | `true` | Premier plan | `Opted-In`** |
| L'utilisateur désactive les notifications push depuis les paramètres de l'appareil et enregistre une session | `false` | `false` | Arrière-plan | Non mis à jour |
| L'utilisateur supprime l'application | Non mis à jour | Mis à jour lorsque le jeton push est retiré | Mis à jour lorsque le jeton push est retiré | Non mis à jour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Actions utilisateur iOS et statut push" }

<sup>* Si l'application n'utilise pas le push provisoire, `Foreground Push Enabled` est `false` jusqu'à ce que l'utilisateur autorise les notifications push. Si l'application utilise le push provisoire, `Foreground Push Enabled` est `true` au début de la première session. Pour plus d'informations, consultez [Autorisation provisoire et push silencieux](#provisional-push).</sup>

<sup>** À partir de la [version 7.5.0 du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), la propriété de configuration `optInWhenPushAuthorized` contrôle si l'état d'abonnement push est automatiquement défini sur `Opted-In` lorsque l'autorisation push est accordée. Pour plus d'informations, consultez [Jetons push](#push-tokens).</sup>

## Autorisation push {#push-permission}

Toutes les plateformes compatibles push — iOS, Web et Android — nécessitent un abonnement explicite via une invite système au niveau de l'OS, avec quelques légères différences décrites dans la section suivante.

Étant donné que la décision d'un utilisateur est définitive et que vous ne pouvez pas redemander après un refus, utiliser des messages in-app de type [push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) est une stratégie importante pour augmenter vos taux d'abonnement.

**Invites natives d'autorisation push de l'OS**

| Plateforme | Capture d'écran | Description |
|--|--|--|
| iOS | ![Une invite push native iOS demandant « My App would like to send you notifications » avec deux boutons, « Don't Allow » et « Allow » en bas du message.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Cela ne s'applique pas lors de la demande d'autorisation de [push provisoire](#provisional-push). |
| Android | ![Un message push Android demandant « Allow Kitchenerie to send you notifications? » avec deux boutons, « Allow » et « Don't allow » en bas du message.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Cette autorisation push a été introduite avec Android 13. Avant Android 13, aucune autorisation n'était requise pour envoyer des notifications push. |
| Web | ![Une invite push native du navigateur web demandant « Braze.com wants to show notification » avec deux boutons, « Block » et « Allow » en bas du message.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Autorisation push" }

### Android

Avant Android 13, aucune autorisation n'était nécessaire pour envoyer des notifications push. Sur Android 12 et versions antérieures, tous les utilisateurs sont considérés comme `Subscribed` dès leur première session lorsque Braze demande automatiquement un jeton push. À ce stade, l'utilisateur est **activé pour le push** avec un jeton push valide pour cet appareil et un état d'abonnement par défaut de `Subscribed`.

À partir d'[Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13), l'autorisation push doit être demandée et accordée par l'utilisateur. Votre application peut demander manuellement l'autorisation à l'utilisateur au moment opportun, mais dans le cas contraire, les utilisateurs seront automatiquement invités lorsque votre application crée un [canal de notification](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

![Une notification dans le centre de notifications du système avec un message en bas demandant « Keep receiving notifications from the Yachtr app? » avec deux boutons en dessous pour « Keep » ou « Turn Off »]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Votre application peut demander un push provisoire ou un push autorisé.

Le push autorisé nécessite une autorisation explicite de l'utilisateur avant d'envoyer toute notification, tandis que le [push provisoire](https://www.braze.com/resources/articles/mastering-provisional-push) vous permet d'envoyer des notifications __silencieusement__, directement dans le centre de notifications sans aucun son ni alerte.

#### Autorisation provisoire et push silencieux {#provisional-push}

Avant iOS 12 (sorti en 2018), tous les utilisateurs devaient explicitement s'abonner pour recevoir des notifications push.

Avec iOS 12, Apple a introduit l'[autorisation provisoire](https://www.braze.com/resources/articles/mastering-provisional-push), permettant aux marques d'envoyer des notifications push silencieuses dans le centre de notifications de leurs utilisateurs avant qu'ils ne s'abonnent explicitement, vous donnant ainsi la possibilité de démontrer la valeur de vos messages en amont. Consultez [autorisation provisoire]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push) pour en savoir plus.

### Web {#web}

Pour le Web, vous devez demander l'abonnement explicite de l'utilisateur via la boîte de dialogue d'autorisation native du navigateur.

Contrairement à iOS et Android, qui permettent à votre application d'afficher l'invite d'autorisation à tout moment, certains navigateurs modernes n'afficheront l'invite que si elle est déclenchée par un « geste utilisateur » (clic de souris ou frappe au clavier). Si votre site tente de demander l'autorisation de notification push au chargement de la page, elle sera probablement ignorée ou masquée par le navigateur.

Par conséquent, vous ne devriez demander l'autorisation que lorsqu'un utilisateur clique quelque part sur votre site web et non de manière aléatoire au chargement d'une page.

## Jetons push {#push-tokens}

Les [jetons push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) sont un identifiant anonyme unique généré par l'appareil d'un utilisateur et envoyé à Braze pour identifier où envoyer la notification de chaque destinataire.

Il existe deux façons de classifier un [jeton push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) qui sont essentielles pour comprendre comment une notification push peut être envoyée à vos utilisateurs.

1. **Push au premier plan** offre la possibilité d'envoyer des notifications push visibles classiques au premier plan de l'appareil d'un utilisateur.
2. **Push en arrière-plan** est disponible indépendamment du fait qu'un appareil particulier ait accepté de recevoir des notifications push de cette marque. Le push en arrière-plan permet aux marques d'envoyer des notifications push silencieuses — des notifications qui ne sont intentionnellement pas affichées — aux appareils pour prendre en charge des fonctionnalités clés comme le [suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Lorsqu'un profil utilisateur possède un jeton push de premier plan valide associé à une application, Braze considère l'utilisateur comme « enregistré pour le push » pour l'application donnée. Braze fournit alors un filtre de segmentation spécifique, `Foreground Push Enabled for App,` pour aider à identifier ces utilisateurs.

{% alert note %}
Le filtre `Foreground Push Enabled for App` ne prend en compte que la présence d'un jeton push de premier plan et d'arrière-plan valide pour l'application donnée. Cependant, le filtre plus générique [`Foreground Push Enabled`](#foreground-push-enabled) segmente les utilisateurs qui ont explicitement activé les notifications push pour n'importe quelle application de votre espace de travail. Ce décompte inclut uniquement le push au premier plan et n'inclut pas les utilisateurs qui se sont désabonnés. Vous pouvez en savoir plus sur ces filtres et d'autres dans [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
{% endalert %}

### Plusieurs utilisateurs sur un même appareil {#multiple-users-on-one-device}

Les jetons push sont spécifiques à la fois à un appareil et à une application, il n'est donc pas possible d'utiliser les jetons push pour distinguer plusieurs utilisateurs utilisant le même appareil.

Par exemple, supposons que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre application sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecter au sien, le jeton push sera réattribué au profil de Kim. Le jeton push restera alors attribué au profil de Kim sur cet appareil jusqu'à ce qu'elle se déconnecte et que Charlie se reconnecte.

Une application ou un site web ne peut avoir qu'un seul abonnement push par appareil. Ainsi, lorsqu'un utilisateur se déconnecte d'un appareil ou d'un site web et qu'un nouvel utilisateur se connecte, le jeton push est réattribué au nouvel utilisateur. Cela se reflète sur le profil de l'utilisateur, dans la section **Contact Settings** de l'onglet **Engagement** :

![Journal des modifications du jeton push dans l'onglet Engagement du profil d'un utilisateur, qui indique quand le jeton push a été transféré à un autre utilisateur et quel était le jeton.]({% image_buster /assets/img/push_token_changelog.png %})

Comme il n'existe aucun moyen pour les fournisseurs push (APNs/FCM) de distinguer plusieurs utilisateurs sur un même appareil, nous transmettons le jeton push au dernier utilisateur connecté pour déterminer quel utilisateur cibler sur l'appareil pour le push.

### Plusieurs appareils et un seul utilisateur {#multiple-devices-and-one-user}

L'état d'abonnement push est basé sur l'utilisateur et n'est pas spécifique à une application individuelle. L'état de l'abonnement push correspond à la dernière valeur définie. Ainsi, si un utilisateur a accepté les notifications push, son état d'abonnement push est `Opted-In` sur tous les appareils éligibles. Si un utilisateur se désabonne ultérieurement explicitement des notifications push via votre application ou d'autres méthodes fournies par votre marque, son état d'abonnement push est mis à jour en `Unsubscribed` et aucun appareil enregistré pour le push ne peut recevoir de notifications push.

## Filtre Foreground Push Enabled {#foreground-push-enabled}

`Foreground Push Enabled` est un filtre de segmentation dans Braze qui permet aux marketeurs d'identifier facilement les utilisateurs qui autorisent Braze à envoyer des notifications push et les utilisateurs qui n'ont pas exprimé de préférence pour ne pas recevoir de notifications push.

Le filtre `Foreground Push Enabled` prend en compte les éléments suivants :
- La capacité de Braze à envoyer une notification push (jeton push de premier plan)
- La préférence globale de l'utilisateur pour recevoir des notifications push sur l'un de ses appareils (état d'abonnement push)

![Une capture d'écran du tableau de bord montrant qu'un utilisateur est « Push Registered for Marketing (iOS) »]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Un utilisateur est considéré comme « activé pour le push » ou « enregistré pour le push » s'il possède un jeton push de premier plan actif pour une application dans votre espace de travail, ce qui signifie que le statut d'activation push est spécifique à l'application.

{% alert note %}
Pour savoir comment vérifier l'état d'enregistrement push, consultez [Statut d'enregistrement push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status).
{% endalert %}

## Trouver les informations d'enregistrement push et le journal des modifications {#finding-push-registration-and-changelog-information}

Dans le tableau de bord, vous pouvez trouver des informations sur l'enregistrement push et les journaux de modifications push dans :

- **Segmentation** – Filtrez les utilisateurs par états d'abonnement, état d'activation, et état d'activation au premier plan et en arrière-plan.
- **Analyse de Campaign** – Consultez les statistiques push et les retours pour une Campaign ou un Canvas individuel.
- **Profil utilisateur (onglet Engagement)** – Consultez les **Contact Settings** et le journal des modifications push pour un utilisateur spécifique.

Lors de l'examen de l'état d'activation push, **Push Registered for** indique les plateformes vers lesquelles Braze peut envoyer des notifications push au premier plan pour cet utilisateur. Sur iOS et Android, si un utilisateur est passé de l'activation push au premier plan à l'activation push en arrière-plan (`remote_notification_enabled`), cela sera documenté dans le journal des modifications push comme « Push token was updated from foreground push enabled to foreground push disabled. »

Si l'utilisateur est ajouté en tant qu'utilisateur test, dans **Console de développement** > **User Event Log**, le profil utilisateur affichera une requête SDK avec `remote_notification_enabled` défini sur `true` ou `false`. Vous devrez peut-être actualiser le profil utilisateur pour voir les mises à jour, car il y a un court délai avant que les mises à jour du SDK n'atteignent le profil utilisateur.

**Filtres de segmentation pour l'état push iOS :**

- **Push au premier plan et en arrière-plan iOS désactivé :** L'utilisateur n'a pas encore reçu d'invite push.
- **Arrière-plan iOS activé :** L'utilisateur a reçu l'invite push et a refusé, ou a accepté puis a désactivé les notifications push dans les paramètres de son appareil (reflété après que l'utilisateur a enregistré une session).
- **Premier plan iOS activé :** L'utilisateur a reçu l'invite push et est éligible pour recevoir des notifications push au premier plan.

L'analyse de Campaign reflétera les statistiques push conformément aux détails présentés plus haut dans cette section. Vous pouvez également télécharger les profils utilisateurs qui sont entrés dans la Campaign ou le Canvas pour croiser les profils utilisateurs.

## Autres scénarios spécifiques aux plateformes {#other-platform-specific-scenarios}

{% tabs %}
{% tab Web %}

Lorsqu'un utilisateur accepte l'invite native d'autorisation push, son statut d'abonnement sera changé en `opted in`.

Pour gérer les abonnements, vous pouvez utiliser la méthode utilisateur [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) pour créer une page de paramètres de préférences sur votre site, après quoi vous pouvez filtrer les utilisateurs par statut de désabonnement dans le tableau de bord.

Si un utilisateur désactive les notifications dans son navigateur, la prochaine notification push envoyée à cet utilisateur rebondira, et Braze mettra à jour le jeton push de l'utilisateur en conséquence. Cela est utilisé pour gérer l'éligibilité aux filtres d'activation push (`Background or Foreground Push Enabled`, `Foreground Push Enabled` et `Foreground Push Enabled for App`). Le statut d'abonnement défini sur le profil de l'utilisateur est un paramètre au niveau de l'utilisateur et ne change pas lorsqu'un push rebondit.

### Erreurs de jeton push Web 410 {#410-web-push-token-errors} {#410-web-push-token-errors}

Si vous recevez une erreur `410: Gone`, cela peut se produire lorsqu'un utilisateur désactive les notifications push web depuis le navigateur dans les paramètres de son OS, ou s'il se connecte en tant qu'utilisateur différent sur le même appareil, ou si l'utilisateur n'a pas visité le site web depuis un certain temps.

Si vous recevez une erreur `410: Endpoint Not Valid`, cela peut signifier que le jeton push web (essentiellement l'URL) a expiré. Cela peut se produire si l'utilisateur ne visite plus jamais le site ou si le navigateur invalide le jeton. Cela peut également se produire périodiquement (souvent tous les quelques mois), selon le navigateur. Lorsque l'utilisateur visite à nouveau le site, si son navigateur est toujours configuré sur « Allow », Braze collectera automatiquement un nouveau jeton pour l'appareil. Cela suppose que l'[option d'initialisation `disablePushTokenMaintenance`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions) n'est pas utilisée lors de l'initialisation du SDK.

{% alert note %}
Les plateformes web ne permettent pas le push en arrière-plan ou silencieux.
{% endalert %}
{% endtab %}
{% tab Android %}

Si un utilisateur activé pour le push au premier plan désactive le push dans les paramètres de son OS, alors au début de la session suivante :
- Braze le marque comme désactivé pour le push au premier plan et ne tente plus de lui envoyer de messages push.
- Le filtre `Foreground Push Enabled for App (Android)` et le filtre de segmentation `Foreground Push Enabled` (en supposant qu'aucune autre application sur le profil de l'utilisateur ne possède un jeton push de premier plan valide) retourneront `false`.

Dans ce scénario, puisqu'un jeton push en arrière-plan existera toujours, vous pouvez continuer à envoyer des notifications push en arrière-plan (silencieuses) avec le filtre de segmentation `Background or Foreground Push Enabled = true`.

Pour Android, Braze considérera un utilisateur comme désactivé pour le push si :

- Un utilisateur désinstalle l'application de son appareil.
- Un message push échoue à la distribution en raison d'un rebond. Cela est souvent causé par une désinstallation, mais peut également être dû à des mises à jour de l'application, une nouvelle version du jeton push ou un changement de format.
- L'enregistrement push échoue auprès de Firebase Cloud Messaging (parfois causé par une mauvaise connexion réseau ou un échec de connexion à FCM ou de la part de FCM pour retourner un jeton valide).
- L'utilisateur bloque les notifications push pour l'application dans les paramètres de son appareil et enregistre ensuite une session.

{% alert note %}
Vous ne pouvez intercepter une notification push Android que lorsque l'application est au premier plan ou en arrière-plan (mais toujours en cours d'exécution). Vous ne pouvez pas intercepter les notifications lorsque l'application est terminée ou complètement arrêtée.
{% endalert %}

{% endtab %}
{% tab iOS %}

Que l'utilisateur accepte ou non l'invite d'abonnement au push au premier plan, vous pourrez toujours envoyer un push en arrière-plan si vous avez activé les notifications distantes dans Xcode et que votre application appelle [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Si votre application est provisoirement autorisée ou si l'utilisateur a accepté le push, il reçoit un jeton push de premier plan, vous permettant de lui envoyer tous les types de push. Dans Braze, nous considérons qu'un utilisateur sur iOS qui est activé pour le push au premier plan est activé pour le push, soit explicitement (au niveau de l'application) soit provisoirement (au niveau de l'appareil).

Si un utilisateur refuse de recevoir des notifications push au niveau de l'OS, son état d'abonnement push sera `Subscribed`, et son profil n'indiquera pas qu'un jeton push de premier plan a été enregistré.

Dans le scénario où un utilisateur, qui avait initialement accepté au niveau de l'OS, désactive les notifications push dans les paramètres de son OS, au début de la session suivante, les événements suivants se produiront :
- Braze le marque comme désactivé pour le push au premier plan et ne tente plus d'envoyer de messages push.
- Le filtre `Foreground Push Enabled for App (iOS)` et le filtre de segmentation `Foreground Push Enabled` (en supposant qu'aucune autre application sur le profil de l'utilisateur ne possède un jeton push de premier plan valide) retourneront `false`.

Dans ce scénario, puisqu'un jeton push en arrière-plan existera toujours, vous pouvez continuer à envoyer des notifications push en arrière-plan (silencieuses) avec le filtre de segmentation `Background or Foreground Push Enabled = true`.

{% alert note %}
iOS ne permet pas aux applications d'intercepter une notification push avant son affichage. Cela signifie que les applications (et Braze) n'ont aucun contrôle sur la possibilité d'afficher ou de masquer la notification. Un utilisateur peut désactiver les notifications push pour une application dans les paramètres de l'appareil, mais cela est contrôlé par le système d'exploitation.
{% endalert %}

{% endtab %}
{% endtabs %}

## Bonnes pratiques {#best-practices}

Consultez notre article dédié sur les [bonnes pratiques push]({{site.baseurl}}/user_guide/channels/push/best_practices) pour des conseils détaillés sur la façon d'optimiser votre utilisation du push avec Braze.