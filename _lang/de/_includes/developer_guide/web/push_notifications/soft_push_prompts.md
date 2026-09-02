{% multi_lang_include developer_guide/prerequisites/web.md %} Außerdem müssen Sie [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

Wenn Sie Braze über das eingebettete Kit von mParticle im Internet integrieren, lesen Sie [Schritt 3 in der Braze-Web-Event-Integration von mParticle](https://docs.mparticle.com/integrations/braze/event/#web) für Anweisungen zur Implementierung von Soft-Push-Aufforderungen.

## Über sanfte Push-Aufforderungen {#about-soft-push-prompts}

Oft ist es für Websites sinnvoll, eine „sanfte“ Push-Aufforderung zu implementieren, bei der Sie Nutzer:innen vorbereiten und Ihre Argumente für den Versand von Push-Benachrichtigungen darlegen, bevor die Push-Berechtigung angefragt wird. Dies ist nützlich, da der Browser einschränkt, wie oft Nutzer:innen direkt aufgefordert werden können, und wenn Nutzer:innen die Berechtigung ablehnen, können Sie sie nie wieder danach fragen.

Alternativ können Sie, wenn Sie eine spezielle angepasste Verarbeitung einbinden möchten, anstatt `requestPushPermission()` direkt aufzurufen, wie in der standardmäßigen [Web-Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-2-browser-registration) beschrieben, unsere [getriggerten In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) verwenden.

{% alert tip %}
Dies kann ohne SDK or Software-Development-Kit-Anpassung mit unserem neuen [Push-Primer ohne Code]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) umgesetzt werden.
{% endalert %}

## Sanfte Push-Aufforderungen einrichten {#setting-up-soft-push-prompts}

{% multi_lang_include archive/web-v4-rename.md %}

### Schritt 1: Eine Push-Primer-Campaign erstellen {#step-1-create-a-push-primer-campaign}

Zunächst müssen Sie eine In-App-Messaging-Campaign „Prime for Push“ im Braze-Dashboard erstellen:

1. Erstellen Sie eine **modale** In-App-Nachricht mit dem gewünschten Text und Styling.
2. Setzen Sie dann das Klickverhalten auf **Nachricht schließen**. Dieses Verhalten wird später angepasst.
3. Fügen Sie der Nachricht ein Schlüssel-Wert-Paar hinzu, wobei der Schlüssel `msg-id` und der Wert `push-primer` ist.
4. Weisen Sie der Nachricht eine angepasste Event-Trigger or triggern-Aktion zu (z. B. „prime-for-push“). Sie können das angepasste Event bei Bedarf manuell über das Dashboard erstellen.

### Schritt 2: Aufrufe entfernen {#step-2-remove-calls}

Suchen und entfernen Sie in Ihrer Braze-SDK or Software-Development-Kit-Integration alle Aufrufe von `automaticallyShowInAppMessages()` aus Ihrem Lade-Snippet.

### Schritt 3: Integration Update or aktualisieren or aktualisieren {#step-3-update-integration}

Ersetzen Sie abschließend den entfernten Aufruf durch das folgende Snippet. Rufen Sie `subscribeToInAppMessage()` auf, bevor Sie `openSession()` aufrufen. So wird sichergestellt, dass Ihr In-App-Nachrichten-Listener rechtzeitig registriert ist, um die Push-Primer-Nachricht zu empfangen.

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

Wenn Sie die sanfte Push-Aufforderung anzeigen möchten, rufen Sie `braze.logCustomEvent` auf – mit dem Event-Namen, der diese In-App-Nachricht triggert.