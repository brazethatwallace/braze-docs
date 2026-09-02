{% multi_lang_include developer_guide/prerequisites/web.md %}

## Angepasste Stile {#custom-styles}

Die UI-Elemente von Braze sind standardmäßig so gestaltet, dass sie ein neutrales In-App-Nachricht-Erlebnis bieten und die Konsistenz mit anderen mobilen Plattformen von Braze gewährleisten. Die Standardstile von Braze sind in CSS im Braze SDK definiert.

### Einstellen eines Standard-Stils {#setting-a-default-style}

Indem Sie ausgewählte Stile in Ihrer Anwendung außer Kraft setzen, können Sie unsere standardmäßigen In-App-Nachrichtentypen mit Ihren eigenen Hintergrundbildern, Schriftfamilien, Stilen, Größen, Animationen und vielem mehr anpassen.

Im Folgenden finden Sie ein Beispiel für eine Überschreibung, die bewirkt, dass die Kopfzeilen einer In-App-Nachricht kursiv dargestellt werden:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

In den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) finden Sie weitere Informationen.

### Anpassen des Z-Index {#customizing-the-z-index}

In-App-Nachrichten werden standardmäßig über `z-index: 9001` angezeigt. Dies lässt sich mit der [Initialisierungsoption](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex ` konfigurieren, falls Ihre Website Elemente mit höheren Werten stilisiert.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Dieses Feature ist nur für Web Braze SDK v3.3.0 und höher verfügbar.
{% endalert %}

## Anpassen von Nachrichtenabweisungen {#customizing-message-dismissals}

Standardmäßig wird eine In-App-Nachricht durch Drücken der Escape-Taste oder durch einen Klick auf den ausgegrauten Hintergrund der Seite verworfen, wenn sie angezeigt wird. Konfigurieren Sie die [Initialisierungsoption](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` auf `true`, um dieses Verhalten zu verhindern und einen expliziten Klick auf einen Button zu verlangen, um Nachrichten zu schließen.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Anpassen des Anzeigezeitpunkts {#customizing-display-timing}

Um das standardmäßige Anzeigeverhalten zu überschreiben, entfernen Sie Aufrufe von `braze.automaticallyShowInAppMessages()` und verarbeiten Sie Nachrichten in `braze.subscribeToInAppMessage()`. Registrierung Sie Ihren Callback vor `braze.openSession()`, damit Sie Nachrichten beim Sitzungsstart abfangen und entscheiden können, ob Sie jede Nachricht anzeigen oder zurückstellen möchten.

Standardmäßig zeigt Braze In-App-Nachrichten an, wenn sie getriggert werden und zur Anzeige berechtigt sind. Wenn Sie ein anderes Verhalten für Ihr App-Erlebnis benötigen, verwenden Sie einen angepassten Callback, um Nachrichten basierend auf Ihrer eigenen Logik zurückzustellen oder anzuzeigen.

Das folgende Beispiel zeigt, wie Sie getriggerte In-App-Nachrichten abonnieren, ausgewählte Nachrichten zurückstellen und zurückgestellte Nachrichten später anzeigen können:

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

Weitere Informationen zur Anpassung der Zustellung finden Sie unter:

- [Web `deferInAppMessage`-Referenz](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)
- [Web `subscribeToInAppMessage`-Referenz](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)

## Öffnen von Links in einem neuen Tab {#opening-links-in-a-new-tab}

Um festzulegen, dass Ihre In-App-Nachricht-Links in einem neuen Tab geöffnet werden, setzen Sie die Option `openInAppMessagesInNewTab` auf `true`, um zu erzwingen, dass alle Links von In-App-Nachrichten-Klicks in einem neuen Tab oder Fenster geöffnet werden.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
