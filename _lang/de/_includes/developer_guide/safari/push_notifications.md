{% multi_lang_include developer_guide/prerequisites/web.md %} Außerdem müssen Sie [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) für das Web-SDK einrichten. Beachten Sie, dass Sie Push-Benachrichtigungen nur an iOS- und iPadOS-Nutzer:innen senden können, die [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) oder höher verwenden.

## Safari-Push für Mobilgeräte einrichten {#setting-up-safari-push-for-mobile}

### Schritt 1: Eine Manifest-Datei erstellen {#manifest}

Ein [Web Application Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest) ist eine JSON-Datei, die steuert, wie Ihre Website dargestellt wird, wenn sie auf dem Startbildschirm eines Nutzers bzw. einer Nutzerin installiert wird.

Sie können beispielsweise die Hintergrund-Designfarbe und das Symbol festlegen, das der [App Switcher](https://support.apple.com/en-us/HT202070) verwendet, ob die App im Vollbildmodus angezeigt wird, um einer nativen App zu ähneln, oder ob die App im Quer- oder Hochformat geöffnet werden soll.

Erstellen Sie eine neue `manifest.json`-Datei im Stammverzeichnis Ihrer Website mit den folgenden Pflichtfeldern.

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

Die vollständige Liste der unterstützten Felder finden Sie in der [MDN-Dokumentation zum Web App Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Schritt 2: Die Manifest-Datei verknüpfen {#manifest-link}

Fügen Sie das folgende `<link>`-Tag zum `<head>`-Element Ihrer Website hinzu, das auf den Speicherort Ihrer Manifest-Datei verweist.

```html
<link rel="manifest" href="/manifest.json" />
```

### Schritt 3: Einen Service Worker hinzufügen {#service-worker}

Ihre Website muss über eine Service-Worker-Datei verfügen, die die Braze-Service-Worker-Bibliothek importiert, wie in unserem [Leitfaden zur Web-Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker) beschrieben.

### Schritt 4: Zum Startbildschirm hinzufügen {#add-to-homescreen}

Gängige Browser (wie Safari, Chrome, FireFox und Edge) unterstützen Web-Push-Benachrichtigungen in ihren neueren Versionen. Um eine Push-Berechtigung unter iOS oder iPadOS anzufordern, muss Ihre Website zum Startbildschirm der Nutzer:innen hinzugefügt werden, indem Sie **Teilen** > **Zum Home-Bildschirm** auswählen. [Zum Home-Bildschirm](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) ermöglicht es Nutzer:innen, Ihre Website als Lesezeichen zu speichern und Ihr Symbol auf dem Startbildschirm hinzuzufügen.

![Ein iPhone mit Optionen zum Setzen eines Lesezeichens für eine Website und zum Speichern auf dem Startbildschirm]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Schritt 5: Die native Push-Eingabeaufforderung anzeigen {#push-prompt}
Nachdem die App zu Ihrem Startbildschirm hinzugefügt wurde, können Sie eine Push-Berechtigung anfordern, wenn Nutzer:innen eine Aktion ausführen (z. B. auf einen Button klicken). Dies kann mit der [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission)-Methode oder mit einer [codefreien Push-Primer-In-App-Nachricht]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) erfolgen.

{% alert note %}
Nachdem Sie die Eingabeaufforderung akzeptiert oder abgelehnt haben, müssen Sie die Website von Ihrem Startbildschirm löschen und erneut installieren, um die Eingabeaufforderung wieder anzeigen zu können.
{% endalert %}

![Eine Push-Eingabeaufforderung mit den Optionen „Erlauben“ oder „Nicht erlauben“ für Benachrichtigungen]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Zum Beispiel:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## Nächste Schritte {#next-steps}

Senden Sie sich als Nächstes eine [Testnachricht]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages), um die Integration zu validieren. Nachdem Ihre Integration abgeschlossen ist, können Sie unsere [No-Code-Push-Primer-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) verwenden, um Ihre Push-Opt-in-Raten zu optimieren.