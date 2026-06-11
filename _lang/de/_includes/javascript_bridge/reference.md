Angepasste HTML-In-App-Nachrichten und Banner unterstützen eine JavaScript-„Bridge“ als Schnittstelle zum Braze SDK, sodass Sie angepasste Braze-Aktionen triggern können, wenn Nutzer:innen auf Elemente mit Links klicken oder anderweitig mit Ihren Inhalten interagieren. Diese Methoden existieren mit der globalen Variable `brazeBridge` oder `appboyBridge`.

{% alert important %}
Braze empfiehlt Ihnen, die globale Variable `brazeBridge` zu verwenden. Die globale Variable `appboyBridge` ist veraltet, wird aber für bestehende Nutzer:innen weiterhin funktionieren. Wenn Sie `appboyBridge` verwenden, empfehlen wir Ihnen eine Migration auf `brazeBridge`. <br><br> `appboyBridge` wurde in den folgenden SDK-Versionen als veraltet markiert:<br><br>
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Um beispielsweise ein angepasstes Attribut und ein angepasstes Event zu protokollieren und anschließend die Nachricht zu schließen, können Sie das folgende JavaScript in Ihrem angepassten HTML verwenden:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### JavaScript-Bridge-Methoden {#bridge}

Die folgenden JavaScript-Methoden werden in angepasstem HTML für In-App-Nachrichten und Banner unterstützt:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% multi_lang_include archive/appboyBridge.md %}

### Tracking von Button-Klicks {#button-click-tracking}

Verwenden Sie die Methode `brazeBridge.logClick(button_id)` zum Tracking von Klicks in Ihrem angepassten HTML.

{% alert note %}
**Banner:** Es wird nur `brazeBridge.logClick()` (ohne Argumente) unterstützt. Button-IDs und angepasstes Button-Tracking werden ausschließlich für In-App-Nachrichten unterstützt.
{% endalert %}

Bei In-App-Nachrichten können Sie „Button 1“, „Button 2“ und „Body Clicks“ programmgesteuert mit `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` bzw. `brazeBridge.logClick()` tracken.

| Klicks | Methode | Unterstützt |
| ---------- | ---------------------------- | --------- |
| Body-Klick | `brazeBridge.logClick()` | In-App-Nachrichten und Banner |
| Button 1 | `brazeBridge.logClick('0')` | Nur In-App-Nachrichten |
| Button 2 | `brazeBridge.logClick('1')` | Nur In-App-Nachrichten |
| Angepasstes Button-Tracking | `brazeBridge.logClick('your custom name here')` | Nur In-App-Nachrichten |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Button-Klick-Tracking" }

Bei In-App-Nachrichten können Sie mehrere Button-Klick-Events pro Impression tracken. Um beispielsweise eine Nachricht zu schließen und einen Klick auf Button 2 zu protokollieren:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

Sie können auch neue angepasste Button-Namen tracken – bis zu 100 eindeutige Namen pro Campaign. Zum Beispiel: `brazeBridge.logClick('blue button')` oder `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Bei der Verwendung von JavaScript-Methoden innerhalb eines `onclick`-Attributs sollten Sie String-Werte in einfache Anführungszeichen setzen, um Konflikte mit dem HTML-Attribut in doppelten Anführungszeichen zu vermeiden.
{% endalert %}

#### Einschränkungen (nur In-App-Nachrichten) {#limitations-in-app-messages-only}

- Sie können bis zu 100 eindeutige Button-IDs pro Campaign haben.
- Button-IDs können jeweils bis zu 255 Zeichen lang sein.
- Button-IDs dürfen nur Buchstaben, Zahlen, Leerzeichen, Bindestriche und Unterstriche enthalten.