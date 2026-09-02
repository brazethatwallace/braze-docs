## Deaktivieren des Daten-Trackings {#disabling-data-tracking}

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab Standardimplementierung %}
Um die Daten-Tracking-Aktivität im Web SDK zu deaktivieren, verwenden Sie die Methode [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Dadurch werden alle Daten synchronisiert, die vor dem Aufruf von `disableSDK()` protokolliert wurden, und alle nachfolgenden Aufrufe des Braze Web SDK für diese Seite und zukünftige Seitenaufrufe werden ignoriert.
{% endtab %}

{% tab Google Tag Manager %}
Verwenden Sie den Tag-Typ **Disable Tracking** oder **Resume Tracking**, um das Web-Tracking zu deaktivieren bzw. wieder zu aktivieren. Diese beiden Optionen rufen [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) und [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) auf.
{% endtab %}
{% endtabs %}

### Best Practices

Um Nutzer:innen die Möglichkeit zu geben, das Tracking zu beenden, empfehlen wir, eine einfache Seite mit zwei Links oder Buttons zu erstellen: einen, der beim Klicken `disableSDK()` aufruft, und einen weiteren, der `enableSDK()` aufruft, damit Nutzer:innen sich wieder anmelden können. Sie können diese Steuerelemente auch verwenden, um das Tracking über andere Daten-Subprozessoren zu starten oder zu stoppen.

{% alert note %}
Das Braze SDK muss nicht initialisiert sein, um `disableSDK()` aufzurufen, sodass Sie das Tracking für vollständig anonyme Nutzer:innen deaktivieren können. Umgekehrt initialisiert `enableSDK()` das Braze SDK nicht, sodass Sie anschließend auch `initialize()` aufrufen müssen, um das Tracking zu aktivieren.
{% endalert %}

## Wiederaufnahme des Trackings von Daten {#resuming-data-tracking}

Um die Datenerfassung wieder aufzunehmen, können Sie die [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)-Methode verwenden.

## Abmelden und Push-Registrierung aufheben {#logout-and-unregister-push}

Das Braze SDK stellt Methoden bereit, um ein Gerät nicht mehr anzusprechen, wenn Nutzer:innen sich von Push-Benachrichtigungen abmelden oder sich ausloggen. Diese Methoden entfernen die Push-Registrierungsdaten der/des aktuellen Nutzer:in auf dem Braze-Server und im SDK, sodass Braze keine zukünftigen Push-Benachrichtigungs-Campaigns mehr an diese:n Nutzer:in sendet.

### Abmelden {#logout}

Wenn sich Nutzer:innen aus einer Anwendung abmelden, rufen Sie die `logout`-Methode des SDK auf, um die Push-Registrierung des Geräts von der/dem aktuellen Nutzer:in zu entfernen und automatisch Bereinigungsaktionen im SDK durchzuführen. Die `logout`-Methode führt Folgendes aus:

- Hebt die Registrierung des Push-Tokens des Geräts bei der/dem aktuellen Nutzer:in auf dem Braze-Server auf.
- Wenn der Aufruf zur Aufhebung der Registrierung erfolgreich ist, löscht das SDK lokal gespeicherte SDK-Daten und deaktiviert das SDK.
- Bei einem Fehler wird der `errorCallback` aufgerufen, damit die Integration entsprechende Maßnahmen ergreifen kann.

Das folgende Beispiel zeigt die Callback-basierte `logout`-Behandlung. Verwenden Sie es, wenn Sie eine sofortige Erfolgs- und Fehlerbehandlung benötigen, und ersetzen Sie das Logging durch Ihren App-Ablauf.

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

#### Tracking und Push nach `logout` wieder aktivieren {#re-enable-tracking-and-push-after-logout}

Rufen Sie nach einem erfolgreichen `logout` [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) auf und Registrieren Sie sich dann erneut für Benachrichtigungen bei Ihrem Betriebssystem oder Push-Anbieter, indem Sie der Anleitung unter [Web-Push-Einrichtung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) folgen.

#### Sofortige Aufrufe zur Aufhebung der Registrierung vermeiden {#avoid-immediate-unregister-calls}

Vermeiden Sie es, `logout` oder `unregisterPush` direkt nach der Registrierung für Push-Benachrichtigungen beim Betriebssystem oder Push-Anbieter aufzurufen. Aufgrund der asynchronen Serververarbeitung kann dies in seltenen Fällen dazu führen, dass das Push-Token erneut der/dem Braze-Nutzer:in hinzugefügt wird.

### Push-Registrierung aufheben {#unregister-push}

Um den Push-Versand an ein Gerät ohne zusätzliche automatische Bereinigung zu stoppen, verwenden Sie die `unregisterPush`-Methode. Diese entfernt das Push-Token des Geräts von der/dem aktuellen Nutzer:in auf dem Braze-Server und löscht das lokal gespeicherte Token.

Das folgende Beispiel zeigt die Callback-basierte `unregisterPush`-Behandlung. Verwenden Sie es, wenn Sie eine sofortige Erfolgs- und Fehlerbehandlung benötigen, und ersetzen Sie das Logging durch Ihren App-Ablauf.

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

#### Push nach `unregisterPush` erneut registrieren {#re-register-push-after-unregisterpush}

Registrieren Sie sich nach dem Aufruf von `unregisterPush` erneut für Benachrichtigungen bei Ihrem Betriebssystem oder Push-Anbieter, indem Sie der Anleitung unter [Web-Push-Einrichtung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) folgen, bevor Sie erneut Braze-Push-Benachrichtigungen senden.

{% alert note %}
In unterstützten Browsern hebt `unregisterPush` bei einer aktiven Push-Subscription auch die Registrierung des von Braze verwalteten Service-Workers auf, nachdem die Abmeldung von der Browser-Push-API erfolgt ist. Wenn Sie `manageServiceWorkerExternally` auf `true` setzen, hebt das SDK die Registrierung des Service-Workers nicht für Sie auf.
{% endalert %}

#### Sofortige Aufrufe zur Aufhebung der Registrierung vermeiden

Vermeiden Sie es, `logout` oder `unregisterPush` direkt nach der Registrierung für Push-Benachrichtigungen beim Betriebssystem oder Push-Anbieter aufzurufen. Aufgrund der asynchronen Serververarbeitung kann dies in seltenen Fällen dazu führen, dass das Push-Token erneut der/dem Braze-Nutzer:in hinzugefügt wird.