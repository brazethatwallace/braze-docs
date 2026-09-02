## Désactivation du suivi des données {#disabling-data-tracking}

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab Déploiement standard %}
Pour désactiver le suivi des données sur le SDK Web, utilisez la méthode [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Cela synchronisera toutes les données enregistrées avant l'appel de `disableSDK()`, et tous les appels ultérieurs au SDK Web de Braze pour cette page et les chargements de pages futurs seront ignorés.
{% endtab %}

{% tab Google Tag gestionnaire %}
Utilisez le type d'étiquette **Disable Tracking** ou **Resume Tracking** pour désactiver ou réactiver le suivi Web, respectivement. Ces deux options appellent [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) et [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Bonnes pratiques {#best-practices}

Pour offrir aux utilisateurs la possibilité d'arrêter le suivi, nous recommandons de créer une page simple avec deux liens ou boutons : l'un qui appelle `disableSDK()` lorsqu'il est cliqué, et l'autre qui appelle `enableSDK()` pour permettre aux utilisateurs de se réinscrire. Vous pouvez utiliser ces contrôles pour démarrer ou arrêter le suivi via d'autres sous-traitants de données également.

{% alert note %}
Le SDK Braze n'a pas besoin d'être initialisé pour appeler `disableSDK()`, ce qui vous permet de désactiver le suivi pour les utilisateurs entièrement anonymes. Inversement, `enableSDK()` n'initialise pas le SDK Braze, vous devez donc également appeler `initialize()` ensuite pour activer le suivi.
{% endalert %}

## Reprise du suivi des données {#resuming-data-tracking}

Pour reprendre la collecte de données, veuillez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

## Déconnexion et désinscription des notifications push {#logout-and-unregister-push}

Le SDK Braze fournit des méthodes pour cesser de cibler un appareil lorsqu'un utilisateur se désinscrit des notifications push ou se déconnecte. Ces méthodes suppriment les données d'inscription push de l'utilisateur actuel sur le serveur Braze et dans le SDK, de sorte que Braze n'envoie plus de futures Campaigns de notifications push à cet utilisateur.

### Déconnexion {#logout}

Lorsqu'un utilisateur se déconnecte d'une application, appelez la méthode `logout` du SDK pour supprimer l'inscription push de l'appareil de l'utilisateur actuel et effectuer automatiquement des actions de nettoyage dans le SDK. La méthode `logout` effectue les opérations suivantes :

- Désinscrit le jeton push de l'appareil de l'utilisateur actuel sur le serveur Braze.
- Si l'appel de désinscription réussit, le SDK efface les données SDK stockées localement et désactive le SDK.
- En cas d'échec, invoque le `errorCallback` pour permettre à l'intégrateur de prendre des mesures.

L'exemple suivant montre la gestion de `logout` basée sur des rappels. Utilisez-le lorsque vous avez besoin d'une gestion immédiate des succès et des erreurs, et remplacez la journalisation par le flux de votre application.

```javascript
import { logout } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully logged out');
};

const errorCallback = () => {
  console.log('Failed to log out');
};

logout(successCallback, errorCallback);
```

#### Réactiver le suivi et les notifications push après `logout` {#re-enable-tracking-and-push-after-logout}

Après un `logout` réussi, appelez [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk), puis réinscrivez-vous aux notifications auprès de votre système d'exploitation (OS) ou de votre fournisseur de notifications push en suivant la [configuration des notifications push Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

#### Éviter les appels de désinscription immédiats {#avoid-immediate-unregister-calls}

Évitez d'appeler `logout` ou `unregisterPush` directement après l'inscription aux notifications push auprès de l'OS ou du fournisseur de notifications push. En raison du traitement asynchrone côté serveur, cela peut dans de rares cas réajouter le jeton push à l'utilisateur Braze.

### Désinscription des notifications push {#unregister-push}

Pour cesser d'envoyer des notifications push à un appareil sans nettoyage automatique supplémentaire, utilisez la méthode `unregisterPush`. Celle-ci supprime le jeton push de l'appareil de l'utilisateur actuel sur le serveur Braze et efface le jeton stocké localement.

L'exemple suivant montre la gestion de `unregisterPush` basée sur des rappels. Utilisez-le lorsque vous avez besoin d'une gestion immédiate des succès et des erreurs, et remplacez la journalisation par le flux de votre application.

```javascript
import { unregisterPush } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully unregistered from push');
};

const errorCallback = () => {
  console.log('Failed to unregister from push');
};

unregisterPush(successCallback, errorCallback);
```

#### Réinscrire les notifications push après `unregisterPush` {#re-register-push-after-unregisterpush}

Après avoir appelé `unregisterPush`, réinscrivez-vous aux notifications auprès de votre OS ou de votre fournisseur de notifications push en suivant la [configuration des notifications push Web]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) avant d'envoyer à nouveau des notifications push Braze.

{% alert note %}
Sur les navigateurs pris en charge, lorsqu'un abonnement push actif existe, `unregisterPush` désinscrit également le service de traitement géré par Braze après la désinscription de l'API Push du navigateur. Si vous définissez `manageServiceWorkerExternally` sur `true`, le SDK ne désinscrit pas le service de traitement à votre place.
{% endalert %}

#### Éviter les appels de désinscription immédiats

Évitez d'appeler `logout` ou `unregisterPush` directement après l'inscription aux notifications push auprès de l'OS ou du fournisseur de notifications push. En raison du traitement asynchrone côté serveur, cela peut dans de rares cas réajouter le jeton push à l'utilisateur Braze.