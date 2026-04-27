{% multi_lang_include developer_guide/prerequisites/web.md %}

## Nachrichten triggern {#message-triggers}

## Trigger-Typen {#trigger-types}

In-App-Nachrichten werden automatisch getriggert, wenn das SDK einen der folgenden angepassten Event-Typen protokolliert: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Beachten Sie, dass die Trigger `Specific Purchase` und `Custom Event` auch robuste Filter für Eigenschaften enthalten.

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Events getriggert werden – nur durch angepasste Events, die vom SDK protokolliert werden. Mehr über die Protokollierung erfahren Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Zustellungssemantik {#delivery-semantics}

Alle infrage kommenden In-App-Nachrichten werden zu Beginn der Sitzung an das Gerät der Nutzer:innen zugestellt. Bei der Zustellung ruft das SDK die Assets im Voraus ab, damit sie zum Zeitpunkt des Triggerns verfügbar sind und die Anzeigelatenz minimiert wird. Wenn das triggernde Event mehr als eine infrage kommende In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt.

Weitere Informationen zur Sitzungsstart-Semantik des SDK finden Sie unter [Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/).

### Rate-Limits {#rate-limits}

Standardmäßig begrenzt das SDK getriggerte In-App-Nachrichten auf einmal alle 30 Sekunden.

Setzen Sie diesen Wert bei Produktions-Apps nicht unter 10 Sekunden, damit Nutzer:innen nicht mit aufeinanderfolgenden In-App-Nachrichten überhäuft werden. Für Tests und Beispiel-App-Abläufe sind 5 Sekunden eine gängige Einstellung.

Sie können dieses Intervall zu Testzwecken auf `0` setzen. Ein Intervall von `0` Sekunden erzwingt jedoch nicht, dass mehrere In-App-Nachrichten gleichzeitig erscheinen. Wenn bereits eine andere modale oder Vollbild-In-App-Nachricht sichtbar ist, gibt `braze.showInAppMessage` den Wert `false` zurück und die neue Nachricht wird nicht angezeigt.

Um dies zu überschreiben, fügen Sie die folgende Eigenschaft zu Ihrer Braze-Konfiguration hinzu – bevor die Braze-Instanz initialisiert wird. Sie können jeden nicht-negativen ganzzahligen Wert angeben, der das minimale Zeitintervall in Sekunden darstellt. Zum Beispiel:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Schlüssel-Wert-Paare {#key-value-pairs}

Wenn Sie eine Campaign in Braze erstellen, können Sie Schlüssel-Wert-Paare als `extras` festlegen, die das In-App-Messaging-Objekt verwenden kann, um Daten an Ihre App zu senden. Zum Beispiel:

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

## Automatische Trigger deaktivieren {#disabling-automatic-triggers}

So verhindern Sie, dass In-App-Nachrichten automatisch getriggert werden:

Entfernen Sie den Aufruf von `braze.automaticallyShowInAppMessages()` aus Ihrem Lade-Snippet und erstellen Sie dann eine angepasste Logik, um die Anzeige oder Nichtanzeige von In-App-Nachrichten zu steuern.

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
Wenn Sie `braze.automaticallyShowInAppMessages()` nicht von Ihrer Website entfernen und dann `braze.showInAppMessage` aufrufen, wird die Nachricht möglicherweise mehrfach angezeigt.
{% endalert %}

Der Parameter `inAppMessage` ist eine [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)-Unterklasse oder ein [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html)-Objekt, die jeweils über verschiedene Methoden zum Abonnieren von Lebenszyklus-Events verfügen. Die vollständige Dokumentation finden Sie in den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html).

Es kann jeweils nur eine [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web)- oder [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web)-In-App-Nachricht angezeigt werden. Wenn Sie versuchen, eine zweite modale oder Vollbild-Nachricht anzuzeigen, während bereits eine sichtbar ist, gibt `braze.showInAppMessage` den Wert `false` zurück und die zweite Nachricht wird nicht angezeigt.

## Manuelles Triggern von Nachrichten {#manually-triggering-messages}

### Eine Nachricht in Realtime anzeigen {#displaying-a-message-in-real-time}

In-App-Nachrichten können auch innerhalb Ihrer Website erstellt und lokal in Realtime angezeigt werden. Alle im Dashboard verfügbaren Anpassungsoptionen sind auch lokal verfügbar. Dies ist besonders nützlich, um Nachrichten anzuzeigen, die Sie in Realtime innerhalb der App triggern möchten. Analytics zu diesen lokal erstellten Nachrichten sind jedoch nicht im Braze-Dashboard verfügbar.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Exit-Intent-Nachrichten triggern {#triggering-exit-intent-messages}

Exit-Intent-Nachrichten sind unaufdringliche In-App-Nachrichten, die dazu dienen, Besuchern wichtige Informationen mitzuteilen, bevor sie Ihre Website verlassen.

Um Trigger für diese Nachrichtentypen einzurichten, implementieren Sie eine Exit-Intent-Bibliothek auf Ihrer Website (z. B. die [Open-Source-Bibliothek von ouibounce](https://github.com/carlsednaoui/ouibounce)) und verwenden Sie dann den folgenden Code, um `'exit intent'` als angepasstes Event in Braze zu protokollieren. Ihre zukünftigen In-App-Nachrichten-Campaigns können diesen Nachrichtentyp dann als angepassten Event-Trigger verwenden.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
