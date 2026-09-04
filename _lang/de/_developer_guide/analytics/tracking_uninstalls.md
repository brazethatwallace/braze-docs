---
nav_title: Uninstall-Tracking
article_title: Deinstallationen über das Braze SDK verfolgen
page_order: 3.5
description: "Erfahren Sie, wie Sie das Uninstall-Tracking über das Braze SDK einrichten."

---

# Uninstall-Tracking {#track-uninstalls}

> Erfahren Sie, wie Sie das Uninstall-Tracking über das Braze SDK einrichten. Allgemeine Informationen finden Sie unter [Benutzerhandbuch: Uninstall-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

{% sdktabs %}
{% sdktab android %}
## Einrichten des Uninstall-Trackings {#setting-up-uninstall-tracking}

### Schritt 1: FCM einrichten {#step-1-set-up-fcm}

Das Android Braze SDK verwendet Firebase Cloud Messaging (FCM), um stille Push-Benachrichtigungen zu versenden, die zum Sammeln von Analytics für das Uninstall-Tracking verwendet werden. Falls noch nicht geschehen, [richten Sie die]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#android_setting-up-push-notifications) Firebase Cloud Messaging API für Push-Benachrichtigungen ein oder [migrieren Sie zu dieser]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

### Schritt 2: Manuelles Uninstall-Tracking erkennen (optional) {#step-2-manually-detect-uninstall-tracking-optional}

Standardmäßig erkennt und ignoriert das Android Braze SDK automatisch stille Push-Benachrichtigungen im Zusammenhang mit dem Uninstall-Tracking. Sie können das Tracking jedoch auch manuell mit der [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) Methode erkennen.

{% alert important %}
Da stille Benachrichtigungen für das Uninstall-Tracking nicht an Push-Callbacks von Braze weitergeleitet werden, können Sie diese Methode nur verwenden, bevor Sie eine Push-Benachrichtigung an Braze übergeben.
{% endalert %}

### Schritt 3: Automatische Server-Pings entfernen {#step-3-remove-automatic-server-pings}

Eine stille Push-Benachrichtigung weckt Ihre App auf und instanziiert die `Application`-Komponente, wenn die App noch nicht läuft. Wenn Sie also eine angepasste [`Application`](https://developer.android.com/reference/android/app/Application)-Unterklasse haben, entfernen Sie jegliche Logik, die während der [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate())-Lifecycle-Methode automatisch Ihre Server anpingt.

### Schritt 4: Uninstall-Tracking aktivieren {#step-4-enable-uninstall-tracking}

Aktivieren Sie abschließend das Uninstall-Tracking in Braze. Eine vollständige Anleitung finden Sie unter [Uninstall-Tracking aktivieren]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
Das Uninstall-Tracking kann ungenau sein. Die Metriken, die Sie in Braze sehen, können verzögert oder ungenau sein.
{% endalert %}

{% endsdktab %}

{% sdktab swift %}
## Einrichten des Uninstall-Trackings

### Schritt 1: Push im Hintergrund aktivieren {#step-1-enable-background-push}

Gehen Sie in Ihrem Xcode-Projekt zu **Capabilities** und stellen Sie sicher, dass die **Background Modes** aktiviert sind. Weitere Informationen finden Sie unter [Stille Push-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Schritt 2: Interne Push-Benachrichtigungen ignorieren {#step-2-ignore-internal-push-notifications}

Das Swift Braze SDK verwendet Push-Benachrichtigungen im Hintergrund, um Analytics zum Uninstall-Tracking zu sammeln. Stellen Sie sicher, dass Ihre App [interne Push-Benachrichtigungen ignoriert]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications), damit sie keine unerwünschten Aktionen durchführt, wenn diese gesendet werden.

### Schritt 3: Senden Sie einen Push zu Testzwecken (optional) {#step-3-send-a-test-push-optional}

Senden Sie sich als Nächstes eine Test-Push-Benachrichtigung vom Braze-Dashboard aus (keine Sorge&#8212;Ihr Kundenprofil wird dadurch nicht aktualisiert).

1. Gehen Sie zu **Messaging** > **Campaigns** und erstellen Sie eine Push-Benachrichtigungs-Campaign über die entsprechende Plattform.
2. Gehen Sie zu **Einstellungen** > **App-Einstellungen** und fügen Sie den Schlüssel `appboy_uninstall_tracking` mit dem entsprechenden Wert `true` hinzu, und markieren Sie dann **Add Content-Available Flag**.
3. Verwenden Sie die **Vorschau**-Seite, um sich selbst eine Test-Push-Benachrichtigung für das Uninstall-Tracking zu senden.
4. Überprüfen Sie, dass Ihre App keine unerwünschten automatischen Aktionen durchführt, wenn sie eine Push-Benachrichtigung empfängt.

{% alert note %}
Zusammen mit der Test-Push-Benachrichtigung wird eine Badge-Nummer gesendet&#8212;eine echte Uninstall-Tracking-Push-Benachrichtigung sendet jedoch keine Badge-Nummern.
{% endalert %}

### Schritt 4: Uninstall-Tracking aktivieren

Aktivieren Sie abschließend das Uninstall-Tracking in Braze. Eine vollständige Anleitung finden Sie unter [Uninstall-Tracking aktivieren]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking#turning-on-uninstall-tracking).

{% alert important %}
Das Uninstall-Tracking kann ungenau sein. Die Metriken, die Sie in Braze sehen, können verzögert oder ungenau sein.
{% endalert %}

{% endsdktab %}
{% endsdktabs %}