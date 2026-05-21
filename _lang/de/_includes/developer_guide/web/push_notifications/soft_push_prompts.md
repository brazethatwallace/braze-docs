{% multi_lang_include developer_guide/prerequisites/web.md %} Außerdem müssen Sie [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

Wenn Sie Braze über das eingebettete Kit von mParticle im Internet integrieren, lesen Sie [Schritt 3 in der Braze-Web-Event-Integration von mParticle](https://docs.mparticle.com/integrations/braze/event/#web) für Anweisungen zur Implementierung von Soft-Push-Aufforderungen.

## Über sanfte Push-Aufforderungen {#about-soft-push-prompts}

Es ist oft eine gute Idee, eine „sanfte“ Push-Aufforderung zu implementieren, mit der Sie die Nutzer:innen „vorbereiten“ und Ihre Argumente für das Senden von Push-Benachrichtigungen darlegen, bevor Sie die Push-Berechtigung anfordern. Dies ist nützlich, da der Browser die Häufigkeit drosselt, mit der Sie Nutzer:innen direkt auffordern können, und wenn Nutzer:innen die Erlaubnis verweigern, können Sie sie nie wieder fragen.

Wenn Sie alternativ eine spezielle angepasste Verarbeitung einbinden möchten, verwenden Sie anstelle des direkten Aufrufs von `requestPushPermission()`, wie in der Standard-[Web-Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) beschrieben, unsere [getriggerten In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
Dies kann ohne SDK-Anpassung mit unserem neuen [No Code Push Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) geschehen.
{% endalert %}

## Einrichtung von Soft-Push-Aufforderungen {#setting-up-soft-push-prompts}

{% multi_lang_include archive/web-v4-rename.md %}

### 1. Schritt: Push-Primer-Kampagne erstellen {#step-1-create-a-push-primer-campaign}

Zunächst müssen Sie im Braze-Dashboard eine „Prime for Push“-In-App-Messaging-Kampagne erstellen:

1. Erstellen Sie eine **modale** In-App-Nachricht mit dem gewünschten Text und Design.
2. Legen Sie anschließend das Verhalten beim Klick auf **Nachricht schließen** fest. Dieses Verhalten wird zu einem späteren Zeitpunkt angepasst.
3. Fügen Sie der Nachricht ein Schlüssel-Wert-Paar hinzu, wobei der Schlüssel `msg-id` und der Wert `push-primer` lautet.
4. Weisen Sie der Nachricht eine angepasste Event-triggernde Aktion zu (z. B. „prime-for-push“). Bei Bedarf können Sie das angepasste Event manuell über das Dashboard erstellen.

### 2. Schritt: Aufrufe entfernen {#step-2-remove-calls}

Suchen Sie in Ihrer Braze-SDK-Integration nach Aufrufen von `automaticallyShowInAppMessages()` und entfernen Sie diese aus Ihrem Lade-Snippet.

### 3. Schritt: Integration aktualisieren {#step-3-update-integration}

Ersetzen Sie abschließend den entfernten Aufruf durch das folgende Snippet. Rufen Sie `subscribeToInAppMessage()` auf, bevor Sie `openSession()` aufrufen. Dadurch wird sichergestellt, dass Ihr In-App-Nachrichten-Listener rechtzeitig registriert wird, um die Push-Primer-Nachricht zu empfangen.

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

Wenn Sie den Nutzer:innen die Soft-Push-Aufforderung anzeigen möchten, rufen Sie `braze.logCustomEvent` auf – mit dem Event-Namen, der diese In-App-Nachricht triggert.