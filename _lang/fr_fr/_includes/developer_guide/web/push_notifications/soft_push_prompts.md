{% multi_lang_include developer_guide/prerequisites/web.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

Si vous intégrez Braze via le kit embarqué de mParticle sur le Web, consultez l'[étape 3 de l'intégration d'événements Web Braze de mParticle](https://docs.mparticle.com/integrations/braze/event/#web) pour obtenir les instructions d'implémentation des invites de poussée douce.

## À propos des invites de poussée douce {#about-soft-push-prompts}

Il est souvent judicieux pour les sites d'implémenter une invite de poussée « douce » qui « prépare » l'utilisateur et lui explique l'intérêt de recevoir des notifications push avant de demander l'autorisation. Cela est utile car le navigateur limite la fréquence à laquelle vous pouvez solliciter directement l'utilisateur, et si celui-ci refuse l'autorisation, vous ne pourrez plus jamais le lui demander.

Alternativement, si vous souhaitez inclure une gestion personnalisée spéciale, au lieu d'appeler `requestPushPermission()` directement comme décrit dans l'[intégration standard des notifications push Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-2-browser-registration), utilisez nos [messages in-app déclenchés]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
Cela peut être réalisé sans personnalisation du SDK en utilisant notre nouveau [push primer sans code]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).
{% endalert %}

## Configuration des invites de poussée douce {#setting-up-soft-push-prompts}

{% multi_lang_include archive/web-v4-rename.md %}

### Étape 1 : Créer une campagne d'amorçage push {#step-1-create-a-push-primer-campaign}

Tout d'abord, vous devez créer une Campaign de message in-app « Amorçage push » dans le tableau de bord de Braze :

1. Créez un message in-app de type **fenêtre modale** avec le texte et le style souhaités.
2. Ensuite, définissez le comportement au clic sur **Fermer le message**. Ce comportement sera personnalisé ultérieurement.
3. Ajoutez une paire clé-valeur au message où la clé est `msg-id` et la valeur est `push-primer`.
4. Attribuez une action de déclenchement par événement personnalisé (comme « prime-for-push ») au message. Vous pouvez créer l'événement personnalisé manuellement depuis le tableau de bord si nécessaire.

### Étape 2 : Supprimer les appels {#step-2-remove-calls}

Dans votre intégration SDK de Braze, recherchez et supprimez tous les appels à `automaticallyShowInAppMessages()` de votre extrait de code de chargement.

### Étape 3 : Mettre à jour l'intégration {#step-3-update-integration}

Enfin, remplacez l'appel supprimé par l'extrait de code suivant. Appelez `subscribeToInAppMessage()` avant d'appeler `openSession()`. Cela garantit que votre écouteur de message in-app est enregistré à temps pour recevoir le message d'amorçage push.

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

Lorsque vous souhaitez afficher l'invite de poussée douce à l'utilisateur, appelez `braze.logCustomEvent` avec le nom d'événement qui déclenche ce message in-app.