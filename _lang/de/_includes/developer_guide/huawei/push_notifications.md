{% multi_lang_include developer_guide/prerequisites/android.md %}

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

Neuere von [Huawei](https://huaweimobileservices.com/) hergestellte Telefone sind mit Huawei Mobile Services (HMS) ausgestattet – einem Dienst, der Push anstelle von Googles Firebase Cloud Messaging (FCM) zustellt.

### Schritt 1: Registrieren Sie sich für ein Huawei-Entwicklerkonto {#step-1-register-for-a-huawei-developer-account}

Bevor Sie beginnen, müssen Sie sich registrieren und ein [Huawei-Entwicklerkonto](https://developer.huawei.com/consumer/en/console) einrichten. Gehen Sie in Ihrem Huawei-Konto zu **Meine Projekte > Projekteinstellungen > App-Informationen** und notieren Sie sich die `App ID` und das `App secret`.

![Seite „App-Informationen“ in der Huawei-Entwicklerkonsole mit App-ID und App-Secret.]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### Schritt 2: Erstellen Sie eine neue Huawei-App im Braze-Dashboard {#step-2-create-a-new-huawei-app-in-the-braze-dashboard}

Gehen Sie im Braze-Dashboard zu **App-Einstellungen**, die unter der Navigation **Einstellungen** aufgeführt sind.

Klicken Sie auf **+ App hinzufügen**, geben Sie einen Namen an (z. B. My Huawei App) und wählen Sie `Android` als Plattform.

![Braze-Dialog „App hinzufügen“ zum Erstellen einer Android-Huawei-App.]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Sobald Ihre neue Braze-App erstellt wurde, suchen Sie die Einstellungen für Push-Benachrichtigungen und wählen Sie `Huawei` als Push-Anbieter aus. Geben Sie als Nächstes Ihr `Huawei Client Secret` und Ihre `Huawei App ID` an.

![Braze-Einstellungen für den Huawei-Push-Anbieter mit den Feldern „Huawei App ID“ und „Client Secret“.]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### Schritt 3: Integrieren Sie das Huawei-Messaging-SDK in Ihre App {#step-3-integrate-the-huawei-messaging-sdk-into-your-app}

Huawei hat ein [Android-Integrations-Codelab](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) bereitgestellt, das die Integration des Huawei-Messaging-Dienstes in Ihre Anwendung beschreibt. Folgen Sie diesen Schritten, um loszulegen.

Nachdem Sie das Codelab abgeschlossen haben, müssen Sie einen angepassten [Huawei Message Service](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) erstellen, um Push-Token zu erhalten und Nachrichten an das Braze SDK weiterzuleiten.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

Nachdem Sie Ihren angepassten Push-Dienst hinzugefügt haben, fügen Sie Folgendes zu Ihrer `AndroidManifest.xml` hinzu:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Schritt 4: Vordergrundbenachrichtigungen verarbeiten {#step-4-handle-foreground-notifications}

Wenn eine Push-Benachrichtigung eingeht, während sich Ihre App im Vordergrund befindet, zeigt Huawei sie standardmäßig automatisch an. Damit Braze die Push-Benachrichtigungsdaten verarbeiten kann (für Analytics-Tracking, Deeplink-Verarbeitung und angepasste Verarbeitung), leiten Sie die eingehenden Push-Daten innerhalb Ihrer `HmsMessageService.onMessageReceived`-Methode an Braze weiter.

Wenn Sie `BrazeHuaweiPushHandler.handleHmsRemoteMessageData` aufrufen, ermittelt Braze, ob es sich bei der Nutzlast um eine Braze-Push-Benachrichtigung handelt. Ist dies der Fall, wird die Benachrichtigung erstellt und angezeigt. Weitere Informationen finden Sie unter [Vordergrundbenachrichtigungen verarbeiten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) in der Dokumentation zu Android-Push-Benachrichtigungen.

Ein vollständiges Beispiel finden Sie in der [Huawei-Handler-Referenz](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-huawei-push-handler/index.html) in der Braze Android SDK-Dokumentation.

### Schritt 5: Push-Benachrichtigungen testen (optional) {#step-5-test-your-push-notifications-optional}

Zu diesem Zeitpunkt haben Sie im Braze-Dashboard eine neue Huawei-Android-App erstellt, diese mit Ihren Huawei-Entwickler-Zugangsdaten konfiguriert und die SDKs von Braze und Huawei in Ihre App integriert.

Als Nächstes können Sie die Integration testen, indem Sie eine neue Push-Campaign in Braze ausprobieren.

#### Schritt 5.1: Erstellen Sie eine neue Push-Benachrichtigungs-Campaign {#step-51-create-a-new-push-notification-campaign}

Erstellen Sie auf der Seite **Campaigns** eine neue Campaign und wählen Sie **Push-Benachrichtigung** als Nachrichtentyp.

Nachdem Sie Ihre Campaign benannt haben, wählen Sie **Android Push** als Push-Plattform.

![Der Campaign-Erstellungs-Composer zeigt die verfügbaren Push-Plattformen an.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

Verfassen Sie als Nächstes Ihre Push-Campaign mit einem Titel und einer Nachricht.

#### Schritt 5.2: Senden Sie einen Test-Push {#step-52-send-a-test-push}

Geben Sie im Tab **Test** Ihre Nutzer:innen-ID ein, die Sie in Ihrer App mit der [`changeUser(USER_ID_STRING)`-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#assigning-a-user-id) festgelegt haben, und klicken Sie auf **Test senden**, um einen Test-Push zu senden.

![Der Tab „Test“ im Campaign-Erstellungs-Composer zeigt, dass Sie eine Testnachricht an sich selbst senden können, indem Sie Ihre Nutzer:innen-ID angeben und in das Feld „Einzelne Nutzer:innen hinzufügen“ eingeben.]({% image_buster /assets/img/huawei/huawei-test-send.png %})

Zu diesem Zeitpunkt sollten Sie eine Test-Push-Benachrichtigung von Braze auf Ihrem Huawei-Gerät (HMS) erhalten.

#### Schritt 5.3: Huawei-Segmentierung einrichten (optional) {#step-53-set-up-huawei-segmentation-optional}

Da Ihre Huawei-App im Braze-Dashboard auf der Android-Push-Plattform aufbaut, haben Sie die Flexibilität, Push an alle Android-Nutzer:innen zu senden (Firebase Cloud Messaging und Huawei Mobile Services), oder Sie können die Zielgruppe Ihrer Campaign auf bestimmte Apps segmentieren.

Um Push nur an Huawei-Apps zu senden, [erstellen Sie ein neues Segment]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) und wählen Sie Ihre Huawei-App im Abschnitt **Apps** aus.

![Braze-Segment-App-Filter mit ausgewählter Huawei-App für Push-Targeting.]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Wenn Sie denselben Push an alle Android-Push-Anbieter senden möchten, können Sie natürlich auf die Angabe der App verzichten, sodass der Push an alle im aktuellen Workspace konfigurierten Android-Apps gesendet wird.