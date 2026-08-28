---
nav_title: Sitzungen verfolgen
article_title: Sitzungen verfolgen
page_order: 3.3
description: "Erfahren Sie, wie Sie Sitzungen über das Braze SDK tracken können."
---

# Sitzungen verfolgen {#track-sessions}

> Erfahren Sie, wie Sie Sitzungen über das Braze SDK tracken können.

{% alert note %}
Für Wrapper-SDKs, die nicht aufgeführt sind, verwenden Sie stattdessen die entsprechende native Android- oder Swift-Methode.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Definition von Inaktivität {#defining-inactivity}

Das Verständnis, wie Inaktivität definiert und gemessen wird, ist entscheidend für die effektive Verwaltung von Sitzungslebenszyklen im Web SDK. Inaktivität bezieht sich auf einen Zeitraum, in dem das Braze Web SDK keine getrackten Events von Nutzer:innen erkennt.

### Wie Inaktivität gemessen wird {#how-inactivity-is-measured}

Das Web SDK trackt Inaktivität basierend auf [SDK-getrackten Events]({{site.baseurl}}/user_guide/data/activation/events/events_overview). Das SDK führt einen internen Timer, der bei jedem gesendeten getrackten Event zurückgesetzt wird. Wenn innerhalb des konfigurierten Timeout-Zeitraums keine SDK-getrackten Events auftreten, gilt die Sitzung als inaktiv und wird beendet.

Weitere Informationen zur Implementierung des Sitzungslebenszyklus im Web SDK finden Sie im Quellcode zur Sitzungsverwaltung im [Braze Web SDK GitHub Repository](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**Was standardmäßig als Aktivität zählt:**
- Öffnen oder Aktualisieren der Web-App
- Interaktion mit Braze-gesteuerten UI-Elementen (wie [In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages) oder [Content Cards]({{site.baseurl}}/developer_guide/content_cards))
- Aufrufen von SDK-Methoden, die getrackte Events senden (wie [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events) oder [Aktualisierungen von Nutzerattributen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes))

**Was standardmäßig nicht als Aktivität zählt:**
- Wechsel zu einem anderen Browser-Tab
- Minimieren des Browserfensters
- Browser-Fokus- oder Blur-Events
- Scrollen oder Mausbewegungen auf der Seite

{% alert note %}
Das Web SDK trackt nicht automatisch Änderungen der Browser-Sichtbarkeit, Tab-Wechsel oder Nutzer:innen-Fokus. Sie können diese Browser-Interaktionen jedoch tracken, indem Sie benutzerdefinierte Event-Listener mithilfe der [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) des Browsers implementieren und [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web) an Braze senden. Ein Beispiel für die Implementierung finden Sie unter [Tracking benutzerdefinierter Inaktivität](#tracking-custom-inactivity).
{% endalert %}

### Konfiguration des Sitzungs-Timeouts {#session-timeout-configuration}

Standardmäßig betrachtet das Web SDK eine Sitzung nach 30 Minuten ohne getrackte Events als inaktiv. Sie können diesen Schwellenwert bei der Initialisierung des SDK mithilfe des Parameters `sessionTimeoutInSeconds` anpassen. Details zur Konfiguration dieses Parameters, einschließlich Code-Beispielen, finden Sie unter [Ändern des Standard-Sitzungs-Timeouts](#changing-the-default-session-timeout).

### Beispiel: Inaktivitätsszenarien verstehen {#example-understanding-inactivity-scenarios}

Betrachten Sie das folgende Szenario:

1. Eine Nutzerin oder ein Nutzer öffnet Ihre Website, und das SDK startet eine Sitzung durch den Aufruf von [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. Die Person wechselt zu einem anderen Browser-Tab, um 30 Minuten lang eine andere Website zu besuchen.
3. Während dieser Zeit treten keine SDK-getrackten Events auf Ihrer Website auf.
4. Nach 30 Minuten Inaktivität wird die Sitzung automatisch beendet.
5. Wenn die Person zu Ihrem Website-Tab zurückkehrt und ein SDK-Event auslöst (z. B. eine Seite anzeigt oder mit Inhalten interagiert), beginnt eine neue Sitzung.

### Tracking benutzerdefinierter Inaktivität {#tracking-custom-inactivity}

Wenn Sie Inaktivität basierend auf Browser-Sichtbarkeit oder Tab-Wechsel tracken möchten, implementieren Sie benutzerdefinierte Event-Listener in Ihrem JavaScript-Code. Verwenden Sie Browser-Events wie `visibilitychange`, um zu erkennen, wann Nutzer:innen Ihre Seite verlassen, und senden Sie manuell [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events) an Braze oder rufen Sie bei Bedarf [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) auf.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

Weitere Informationen zum Protokollieren angepasster Events finden Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events). Details zum Sitzungslebenszyklus und zur Timeout-Konfiguration finden Sie unter [Ändern des Standard-Sitzungs-Timeouts](#change-session-timeout).

## Updates für Sitzungen abonnieren {#subscribing-to-session-updates}

### Schritt 1: Updates abonnieren {#step-1-subscribe-to-updates}

Um Sitzungs-Updates zu abonnieren, verwenden Sie die Methode `subscribeToSessionUpdates()`.

{% tabs %}
{% tab web %}
Das Abonnieren von Sitzungs-Updates wird derzeit vom Web Braze SDK nicht unterstützt.
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
Wenn Sie einen Callback für das Sitzungsende registrieren, wird dieser ausgelöst, wenn die App in den Vordergrund zurückkehrt. Die Sitzungsdauer wird vom Zeitpunkt des Öffnens oder In-den-Vordergrund-Bringens der App bis zum Schließen oder In-den-Hintergrund-Wechseln gemessen.

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

Um einen asynchronen Stream zu abonnieren, können Sie stattdessen [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) verwenden.

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
Das React Native SDK stellt keine Methode zum direkten Abonnieren von Sitzungs-Updates bereit. Der Sitzungslebenszyklus wird vom zugrunde liegenden nativen SDK verwaltet. Um Updates zu abonnieren, verwenden Sie daher den nativen Plattformansatz im Tab **Android** oder **Swift**.
{% endtab %}
{% endtabs %}

### Schritt 2: Sitzungs-Tracking testen (optional) {#step-2-test-session-tracking-optional}

Um das Sitzungs-Tracking zu testen, starten Sie eine Sitzung auf Ihrem Gerät und öffnen Sie dann das Braze-Dashboard und suchen Sie nach der entsprechenden Nutzer:in. Wählen Sie in ihrem Nutzerprofil **Sessions Overview** aus. Wenn die Metriken wie erwartet aktualisiert werden, funktioniert das Sitzungs-Tracking korrekt.

![Der Abschnitt „Sitzungsübersicht“ eines Nutzerprofils mit der Anzahl der Sitzungen, dem Datum der letzten Nutzung und dem Datum der ersten Nutzung.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
App-spezifische Details werden nur für Nutzer:innen angezeigt, die mehr als eine App verwendet haben.
{% endalert %}

## Ändern des Standard-Sitzungs-Timeouts {#change-session-timeout}

Sie können die Zeitspanne ändern, die vergeht, bevor eine Sitzung automatisch beendet wird.

{% tabs %}
{% tab web %}
Standardmäßig ist das Sitzungs-Timeout auf `30` Minuten eingestellt. Um dies zu ändern, übergeben Sie die Option `sessionTimeoutInSeconds` an Ihre [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)-Funktion. Der Wert kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
Standardmäßig ist das Sitzungs-Timeout auf `10` Sekunden eingestellt. Um dies zu ändern, öffnen Sie Ihre Datei `braze.xml` und fügen Sie den Parameter `com_braze_session_timeout` hinzu. Der Wert kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Standardmäßig ist das Sitzungs-Timeout auf `10` Sekunden eingestellt. Um dies zu ändern, setzen Sie `sessionTimeout` in dem `configuration`-Objekt, das an [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) übergeben wird. Der Wert kann auf eine beliebige ganze Zahl größer oder gleich `1` gesetzt werden.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}
Das React Native SDK stützt sich auf die nativen SDKs, um Sitzungen zu verwalten. Um das Standard-Sitzungs-Timeout zu ändern, konfigurieren Sie es in der nativen Ebene:

- **Android:** Setzen Sie `com_braze_session_timeout` in Ihrer `braze.xml`-Datei. Für weitere Informationen wählen Sie den Tab **Android**.
- **iOS:** Setzen Sie `sessionTimeout` in Ihrem `Braze.Configuration`-Objekt. Für weitere Informationen wählen Sie den Tab **Swift**.
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie ein Sitzungs-Timeout festlegen, werden alle Sitzungssemantiken automatisch auf das festgelegte Timeout erweitert.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### Nutzerprofil zeigt 0 Sitzungen {#user-profile-has-0-sessions}

Ein Nutzerprofil kann 0 Sitzungen aufweisen, wenn die Nutzer:innen außerhalb des SDK erstellt wurden:

- **Erstellt über die REST API:** Wenn Nutzer:innen über den Endpunkt [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) mit einer `app_id` in der Anfrage erstellt werden, erscheint das Profil zwar mit dieser App verknüpft, enthält aber keine Sitzungsdaten, da das SDK für diese Nutzer:innen nie initialisiert wurde.
- **Erstellt per CSV-Import:** Wenn Nutzer:innen über [CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) importiert werden, ohne Werte für die Felder „Erste Sitzung“ oder „Letzte Sitzung“ anzugeben, existiert das Profil mit 0 Sitzungen.

### Einige Nutzer:innen protokollieren keine Sitzungen {#some-users-are-not-logging-sessions}

Da Sitzungen erst nach der Initialisierung des SDK erfasst werden, protokollieren Nutzer:innen, die keine SDK-Initialisierung auslösen, keine Sitzungen. Dies geschieht typischerweise, wenn Ihre App bedingte Logik vor der Initialisierung des SDK verwendet – beispielsweise eine verzögerte Initialisierung hinter einem Anmeldeablauf, einer Einwilligungsabfrage oder einem Feature-Flag. Hinweise zur Implementierung finden Sie unter [Verzögerte Initialisierung]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#step-2-set-up-delayed-initialization-optional). In diesen Fällen startet keine Sitzung für Nutzer:innen, die die Bedingung nicht erfüllen.

Wenn einige Nutzer:innen Sitzungen protokollieren und andere nicht, überprüfen Sie Folgendes:

- **Prüfen Sie Ihre Initialisierungslogik.** Stellen Sie sicher, dass das SDK für alle Nutzer:innen und App-Einstiegspunkte initialisiert wird, nicht nur für einige.
- **Achten Sie auf aktuelle App-Änderungen.** Neue bedingte Logik rund um die SDK-Initialisierung kann einen plötzlichen Rückgang der Sitzungszahlen verursachen.
- **Vergleichen Sie betroffene und nicht betroffene Nutzer:innen.** Identifizieren Sie Unterschiede bei App-Version, Gerätetyp oder Nutzerablauf, die erklären könnten, warum die Initialisierung bei bestimmten Nutzer:innen übersprungen wird.

Wenn das Problem nach Überprüfung Ihrer Implementierung weiterhin besteht, reproduzieren Sie das Problem und sammeln Sie die folgenden Informationen, bevor Sie den Support kontaktieren:

- Schritte zur Reproduktion des Problems
- Die betroffene App-Version
- [Ausführliche SDK-Logs]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), die während des Auftretens des Problems aufgezeichnet wurden (oder nach Plattform: [Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_enabling-logs), [Swift]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift#swift_setting-the-log-level), [Web]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web#web_logging))
- Das Code-Snippet für die SDK-Initialisierung
- Eine Zusammenfassung der bedingten Logik, die vor der Initialisierung angewendet wird