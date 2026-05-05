{% multi_lang_include developer_guide/prerequisites/web.md %}

## Styles personnalisés {#custom-styles}

Les éléments de l'IU de Braze sont dotés d'un aspect et d'une convivialité par défaut qui créent une expérience de message in-app neutre et visent à assurer la cohérence avec les autres plateformes mobiles Braze. Les styles par défaut de Braze sont définis en CSS dans le SDK de Braze.

### Définition d'un style par défaut {#setting-a-default-style}

En écrasant des styles sélectionnés dans votre application, vous pouvez personnaliser nos types de messages in-app standard avec vos propres images de fond, familles de polices, styles, tailles, animations, et bien plus encore.

Par exemple, ce qui suit est un exemple de remplacement qui entraînera la mise en italique des en-têtes d'un message in-app :

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consultez les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) pour plus d'informations.

### Personnaliser le z-index {#customizing-the-z-index}

Par défaut, les messages in-app sont affichés en utilisant `z-index: 9001`. Ceci est configurable en utilisant l'[option d'initialisation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex ` dans le cas où votre site web stylise des éléments avec des valeurs plus élevées.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Cette fonctionnalité n'est disponible que pour le SDK Web de Braze v3.3.0 et les versions ultérieures.
{% endalert %}

## Personnaliser la fermeture des messages {#customizing-message-dismissals}

Par défaut, lorsqu'un message in-app est affiché, le fait d'appuyer sur la touche Échap ou de cliquer sur l'arrière-plan grisé de la page fermera le message. Configurez l'[option d'initialisation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` sur `true` pour empêcher ce comportement et exiger un clic explicite sur un bouton pour fermer les messages.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Personnaliser le moment d'affichage {#customizing-display-timing}

Pour remplacer le comportement d'affichage par défaut, supprimez les appels à `braze.automaticallyShowInAppMessages()` et gérez les messages dans `braze.subscribeToInAppMessage()`. Enregistrez votre rappel avant `braze.openSession()`, afin de pouvoir intercepter les messages de début de session et décider d'afficher ou de différer chaque message.

Par défaut, Braze affiche les messages in-app lorsqu'ils sont déclenchés et éligibles à l'affichage. Si vous avez besoin d'un comportement différent pour votre expérience sur l'application, utilisez un rappel personnalisé pour différer ou afficher les messages selon votre propre logique.

L'exemple suivant montre comment s'abonner aux messages in-app déclenchés, différer certains messages et afficher les messages différés ultérieurement :

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT"
});

braze.subscribeToInAppMessage(function (message) {
    // Control-group messages should always be "shown" to log analytics.
    if (message.isControl || message instanceof braze.ControlMessage) {
        braze.showInAppMessage(message);
        return;
    }

    const shouldDefer = true; // Replace with your own display logic

    if (shouldDefer) {
        braze.deferInAppMessage(message);
        return;
    }

    braze.showInAppMessage(message);
});

braze.openSession();

// Later, when your app is ready to display a deferred message:
const deferredMessage = braze.getDeferredInAppMessage();
if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
}
```

Pour des conseils connexes sur la personnalisation de la réception, consultez :

- [Référence Web `deferInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)
- [Référence Web `subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)

## Ouverture des liens dans un nouvel onglet {#opening-links-in-a-new-tab}

Pour configurer les liens de vos messages in-app afin qu'ils s'ouvrent dans un nouvel onglet, définissez l'option `openInAppMessagesInNewTab` sur `true` pour forcer tous les liens issus des clics sur les messages in-app à s'ouvrir dans un nouvel onglet ou une nouvelle fenêtre.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
