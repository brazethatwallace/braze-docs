## Fehlerbehebung {#troubleshooting}

### Tippen auf eine Push-Benachrichtigung öffnet die App nicht {#tapping-push-notification-doesnt-open-the-app}

Unter Android wird über das native Flag `com_braze_handle_push_deep_links_automatically` gesteuert, ob das Tippen auf eine Push-Benachrichtigung Ihre App automatisch in den Vordergrund bringt und den Deeplink öffnet. Standardmäßig ist dieses Flag auf `false` gesetzt.

Mit dem Standardwert `false`:

- Das native SDK or Software-Development-Kit sendet weiterhin einen `BRAZE_PUSH_CLICKED`-Broadcast, und Ihr Dart-`push_opened`-Listener wird wie erwartet ausgelöst.
- Das native SDK or Software-Development-Kit ruft `startActivity()` nicht auf, sodass Ihre App nicht in den Vordergrund gebracht wird und der Deeplink nicht automatisch geöffnet wird.

Wenn diese beiden Verhaltensweisen dem entsprechen, was Sie beobachten, ist die Flag-Einstellung wahrscheinlich die Ursache.
Um dies zu bestätigen, prüfen Sie Ihre Geräteprotokolle auf einen `BrazePushReceiver`-Eintrag, der `com.braze.action.BRAZE_PUSH_CLICKED` verarbeitet, gefolgt von einem `push_opened`-Ereignis in Ihren Flutter-Protokollen, ohne einen entsprechenden App-Start.

Um dies zu beheben, setzen Sie `com_braze_handle_push_deep_links_automatically` in Ihrer `braze.xml` auf `true`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Weitere Informationen finden Sie unter [Deeplinks hinzufügen (Android)]({{site.baseurl}}/developer_guide/push_notifications#flutter_step-4-add-deep-links-android) im Flutter-Leitfaden für Push-Benachrichtigungen.

### Weitere Probleme bei der Push-Zustellung und -Registrierung {#other-push-delivery-and-registration-issues}

Da das Braze Flutter SDK or Software-Development-Kit für Android auf dem nativen Braze Android SDK or Software-Development-Kit aufbaut, gelten die meisten anderen Probleme bei der Push-Zustellung, -Registrierung und -Protokollierung (wie z. B. Sender-ID-Abweichungen, fehlende Google Play Services oder ein nicht registrierter `BrazeFirebaseMessagingService`) auch für Flutter-Apps. Weitere Informationen finden Sie im [nativen Android-Leitfaden zur Fehlerbehebung]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android).