{% multi_lang_include developer_guide/prerequisites/web.md %}

## Déclencheurs de messages {#message-triggers}

## Types de déclencheurs {#trigger-types}

Les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` et `Push Click`. Notez que les déclencheurs `Specific Purchase` et `Custom Event` contiennent également des filtres de propriétés robustes.

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API — uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, consultez la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Sémantique de distribution {#delivery-semantics}

Tous les messages in-app éligibles sont envoyés sur l'appareil de l'utilisateur au début de sa session. À la réception, le SDK précharge les ressources afin qu'elles soient disponibles au moment du déclenchement, ce qui minimise la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera distribué.

Pour plus d'informations sur la sémantique de démarrage de session du SDK, consultez la section [Cycle de vie de la session]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/).

### Limites de débit {#rate-limits}

Par défaut, le SDK limite le déclenchement des messages in-app à une fois toutes les 30 secondes.

Pour les applications en production, ne définissez pas cette valeur en dessous de 10 secondes, afin d'éviter que les utilisateurs ne soient submergés par des messages in-app successifs. Pour les tests et les flux d'applications de démonstration, 5 secondes est un réglage courant.

Vous pouvez définir cet intervalle à `0` pour les tests. Cependant, un intervalle de `0` seconde ne force pas l'affichage simultané de plusieurs messages in-app. Si un autre message in-app de type fenêtre modale ou plein écran est déjà visible, `braze.showInAppMessage` renvoie `false` et le nouveau message ne s'affichera pas.

Pour modifier ce comportement, ajoutez la propriété suivante à votre configuration Braze — avant l'initialisation de l'instance Braze. Vous pouvez la définir sur n'importe quel entier non négatif, qui représente l'intervalle de temps minimum en secondes. Par exemple :

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Paires clé-valeur {#key-value-pairs}

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur en tant qu'`extras`, que l'objet de message in-app peut utiliser pour envoyer des données à votre application. Par exemple :

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## Désactivation des déclencheurs automatiques {#disabling-automatic-triggers}

Pour empêcher les messages in-app de se déclencher automatiquement :

Supprimez l'appel à `braze.automaticallyShowInAppMessages()` dans votre extrait de code de chargement, puis créez une logique personnalisée pour gérer l'affichage ou non des messages in-app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Si vous ne supprimez pas `braze.automaticallyShowInAppMessages()` de votre site web et que vous appelez ensuite `braze.showInAppMessage`, le message risque de s'afficher plusieurs fois.
{% endalert %}

Le paramètre `inAppMessage` sera une sous-classe de [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) ou un objet [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html), chacun disposant de différentes méthodes d'abonnement aux événements de cycle de vie. Consultez les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) pour la documentation complète.

Un seul message in-app [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) ou [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) peut être affiché à un instant donné. Si vous tentez d'afficher un deuxième message de type fenêtre modale ou plein écran alors qu'un autre est déjà visible, `braze.showInAppMessage` renverra false et le deuxième message ne s'affichera pas.

## Déclenchement manuel des messages {#manually-triggering-messages}

### Affichage d'un message en temps réel {#displaying-a-message-in-real-time}

Les messages in-app peuvent également être créés au sein de votre site et affichés localement en temps réel. Toutes les options de personnalisation disponibles sur le tableau de bord sont également disponibles localement. C'est particulièrement utile pour afficher des messages que vous souhaitez déclencher dans l'application en temps réel. Cependant, les données analytiques de ces messages créés localement ne seront pas disponibles dans le tableau de bord de Braze.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Déclenchement de messages d'intention de sortie {#triggering-exit-intent-messages}

Les messages d'intention de sortie sont des messages in-app non intrusifs utilisés pour communiquer des informations importantes aux visiteurs avant qu'ils ne quittent votre site.

Pour configurer des déclencheurs pour ces types de messages, implémentez une bibliothèque d'intention de sortie sur votre site web (telle que [la bibliothèque open source ouibounce](https://github.com/carlsednaoui/ouibounce)), puis utilisez le code suivant pour enregistrer `'exit intent'` en tant qu'événement personnalisé dans Braze. Vos futures campagnes de messages in-app pourront alors utiliser ce type de message comme déclencheur d'événement personnalisé.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
