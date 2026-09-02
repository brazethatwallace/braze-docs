---
nav_title: Baidu-Integration
article_title: Baidu Push-Benachrichtigung Integration für Android
platform: Android
permalink: /baidu_integration/
description: "Dieser Artikel zeigt Ihnen, wie Sie eine Baidu Android Integration einrichten."
hidden: true
excerpt_separator: ""
---
# Baidu-Integration
{% alert warning %}
Die Braze Baidu Push-Integration ist seit dem 24. März 2022 veraltet.

* **24. März 2022:** Es können keine neuen Baidu-Apps mehr im Braze-Dashboard erstellt werden.
* **15. September 2022:** Es können keine neuen Baidu Push-Nachrichten mehr erstellt werden. Bestehende Nachrichten und die Datenerfassung sind davon nicht betroffen.
* **15. Januar 2023:** Braze stellt keine Nachrichten mehr zu und erfasst keine Daten mehr von Baidu-Apps.
{% endalert %}

Braze kann Push-Benachrichtigungen an Android-Geräte über [Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}) senden. Beachten Sie, dass Sie Ihre Apps bei Verwendung von Baidu Cloud Push nicht über den Baidu App Store vertreiben müssen.

## Schritt 1: Ein Baidu-Konto erstellen {#step-1-create-a-baidu-account}

Um ein Baidu-Konto zu erstellen, besuchen Sie das [Baidu-Portal](https://www.baidu.com/) und klicken Sie auf **登录** (Anmelden), um ein Dialogfeld aufzurufen, in dem Sie sich anmelden oder ein neues Konto erstellen können.

![Baidu-Portal-Startseite]({% image_buster /assets/img_archive/baidu_portal.png %})

Um ein neues Konto zu erstellen, klicken Sie unten im Anmeldedialog auf **立即注册** (Neues Konto).

![Baidu-Anmeldedialog]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

Geben Sie Ihren Nutzernamen, Ihre Telefonnummer und Ihr Passwort auf der Kontoerstellungsseite ein. Klicken Sie anschließend auf den Button zum Empfangen des Verifizierungscodes. Sie erhalten nun eine Kurzmitteilungsdienst or SMS von Baidu mit einem Verifizierungscode. Akzeptieren Sie abschließend die Lizenzvereinbarung und klicken Sie auf **注册** (Konto erstellen), um sich zu Registrierung or registrieren. Falls diese Einrichtungsschritte fehlschlagen, versuchen Sie, sich über die Baidu-Cloud-Anmeldung zu Registrierung or registrieren, wie in diesem [Anmeldeartikel](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/) beschrieben.

![Baidu-Registrierungsseite]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## Schritt 2: Als Baidu-Entwickler:in Registrierung or registrieren {#step-2-register-as-a-baidu-developer}

Als Nächstes müssen Sie sich als Baidu-Entwickler:in Registrierung or registrieren. Besuchen Sie zunächst das [Baidu-Entwicklerportal](http://developer.baidu.com/) und wählen Sie **注册** (neues Entwicklerkonto erstellen), um die Registrierung zu starten.

![Baidu-Entwicklerportal]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

Wählen Sie auf der Registrierungsseite Ihren Kontotyp (个人 für Privatperson, 公司 für Unternehmen) und den Entwicklertyp (Entwickler:in ist vorausgewählt und in den meisten Fällen korrekt). Geben Sie Ihren Namen, eine Kurzbiografie und Ihre Telefonnummer mit Ländervorwahl in Klammern ein (zum Beispiel (1)xxxxxxxxxx). Klicken Sie auf **发送验证码** (Bestätigungscode senden) und geben Sie den Bestätigungscode in der folgenden Zeile ein. Die nächsten beiden Felder – Entwickler-Website und Entwickler-Logo – sind optional. Akzeptieren Sie die Lizenzvereinbarung und klicken Sie auf **提交** (Absenden), um die Registrierung abzuschließen. Sie verfügen nun über ein Baidu-Entwicklerkonto.

![Baidu-Entwicklerregistrierungsseite]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## Schritt 3: Ihre Anwendung bei Baidu Registrierung or registrieren {#step-3-register-your-application-with-baidu}

Um Ihre Anwendung bei Baidu zu Registrierung or registrieren, besuchen Sie das [Baidu-Projektportal](http://developer.baidu.com/console#app/project) und klicken Sie auf **创建工程** (Projekt erstellen).

![Baidu-Projektportal]({% image_buster /assets/img_archive/baidu_project.png %})

Geben Sie auf der folgenden Seite den Namen Ihrer Anwendung ein. Die beiden folgenden Kontrollkästchen dienen zur Aktivierung zusätzlicher Baidu-Dienste. In den meisten Fällen sollten diese leer gelassen werden.

![Eingabefeld für den App-Namen bei Baidu]({% image_buster /assets/img_archive/baidu_app_name.png %})

Nach dem Einrichten Ihrer Anwendung gelangen Sie zu einer Konsole, die Informationen über Ihre App anzeigt, einschließlich des API-Schlüssels. Navigieren Sie als Nächstes in der Seitenleiste zu **云推送** (Cloud-Push). Klicken Sie auf der folgenden Seite auf **推送设置** (Push einrichten).

![Baidu-App-Konsole mit Informationen zur App]({% image_buster /assets/img_archive/baidu_app_console.png %})

![Baidu-Seitenleiste mit Cloud-Push-Option]({% image_buster /assets/img_archive/baidu_continue.png %})

Geben Sie auf der folgenden Seite den Paketnamen Ihrer App ein (zum Beispiel `com.braze.sample`) und legen Sie fest, ob Nachrichten zwischengespeichert werden sollen und, falls ja, wie lange (in Stunden). Dies gibt Baidu an, wie lange weiterhin versucht werden soll, Nachrichten an Offline-Nutzer:innen zu senden. Klicken Sie auf **保存设置** (Einstellungen speichern), um zu speichern.

![Baidu-Cloud-Push-Konfigurationsseite]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## Schritt 4: Baidu zu Ihrer Anwendung hinzufügen {#step-4-add-baidu-to-your-application}

Besuchen Sie das [Baidu Push-SDK or Software-Development-Kit-Portal](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk) und laden Sie das neueste Baidu Cloud Push Android SDK or Software-Development-Kit herunter.

![Baidu-SDK or Software-Development-Kit-Downloadseite]({% image_buster /assets/img_archive/baidu_sdk.png %})

Im SDK or Software-Development-Kit finden Sie die Push-Service-JAR-Datei und plattformspezifische native Bibliotheken. Integrieren Sie diese in Ihr Projekt. Stellen Sie sicher, dass Ihre App auf die höchste SDK or Software-Development-Kit-Version abzielt, die derzeit von Baidu unterstützt wird. Diese Dokumentation ist aktuell für die Baidu Cloud Push Android SDK or Software-Development-Kit-Version `4.6.2.38`.

Fügen Sie die folgenden erforderlichen Baidu-Berechtigungen zur `AndroidManifest.xml` Ihrer Anwendung hinzu.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

Die Baidu-Bibliothek enthält Broadcast-Receiver, die eingehende Push-Nachrichten verarbeiten. Deklarieren Sie die internen Baidu-Receiver in der `AndroidManifest.xml` Ihrer Anwendung innerhalb des `<application>`-Elements.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

Sie müssen außerdem einen Broadcast-Receiver erstellen, der auf eingehende Push-Nachrichten und Benachrichtigungen lauscht. Deklarieren Sie Ihren Receiver in der `AndroidManifest.xml` Ihrer Anwendung innerhalb des `<application>`-Elements. Dieser Receiver muss `com.baidu.android.pushservice.PushMessageReceiver` erweitern und Methoden implementieren, die Ereignis-Updates vom Baidu-Push-Dienst empfangen.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

Fügen Sie in der `onCreate()`-Methode Ihrer Hauptaktivität die folgende Zeile hinzu, die Ihre Anwendung bei Baidu registriert und beginnt, auf eingehende Push-Nachrichten zu lauschen. Stellen Sie sicher, dass Sie „Your-API-Key“ durch den Baidu-API-Schlüssel Ihres Projekts ersetzen.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Abschließend müssen Sie Ihre Nutzer:innen bei Braze Registrierung or registrieren. Senden Sie in der `onBind()`-Methode des Baidu-Broadcast-Receivers, den Sie in diesem Schritt erstellt haben, die `channelId` an Braze mit `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Schritt 5: Push-Öffnungen Registrierung or registrieren {#step-5-registering-push-opens}

Baidu unterstützt das Senden zusätzlicher Schlüssel-Wert-Paare mit Push-Nachrichten im JSON-Format. Die Methode `public void onNotificationClicked(Context context, String title, String description, String customContentString)` Ihres Broadcast-Receivers wird aufgerufen, wenn Nutzer:innen auf eine eingehende Push-Nachricht klicken. Der Parameter `customContentString` enthält die Extras im JSON-Format. Alle Nachrichten von Braze enthalten die folgenden zwei Schlüssel-Wert-Paare:

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Immer wenn `onNotificationClicked` von Ihrem Baidu-Receiver aufgerufen wird, sollte Ihr Receiver einen [Intent](http://developer.android.com/reference/android/content/Intent.html) an Ihre Anwendung senden, der `customContentString` enthält. Ihre Anwendung protokolliert den Klick bei Braze mithilfe des `customContentString`.

Der folgende Beispielcode übergibt `customContentString` an Braze und protokolliert einen Klick:

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Schritt 6: Extras {#step-6-extras}

Neben den von Braze reservierten Schlüsseln enthält der Parameter `customContentString` auch alle benutzerdefinierten angepassten Schlüssel-Wert-Paare. Um Ihre Schlüssel-Wert-Paare zu extrahieren, verpacken Sie `customContentString` in ein JSONObject und rufen Sie Ihre Extras ab:

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Schritt 7: Baidu-Schlüssel einrichten {#step-7-set-up-baidu-keys}

Sie müssen Ihren Baidu-API-Schlüssel und Ihren geheimen Baidu-Schlüssel im Braze-Dashboard eingeben. Beide Schlüssel sind über die Baidu-Anwendungskonsole verfügbar.

Wählen Sie auf der Seite **Einstellungen verwalten** Ihre Android-China-App aus und geben Sie Ihren Baidu-API-Schlüssel und Ihren geheimen Baidu-Schlüssel im Bereich für Push-Benachrichtigungen ein.

![Baidu-API-Schlüssel-Konfiguration im Braze-Dashboard]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## Zusätzliche Ressourcen {#additional-resources}

- [Baidu-Portal](https://www.baidu.com/)
- [Baidu-Entwicklerportal](http://developer.baidu.com/)
- [Baidu-Projektportal](http://developer.baidu.com/console#app/project)
- [Baidu-Push-SDK or Software-Development-Kit-Portal](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Baidu-Integrationsdokumentation](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)