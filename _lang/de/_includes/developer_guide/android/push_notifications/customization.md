{% multi_lang_include developer_guide/prerequisites/android.md %} Außerdem müssen Sie [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Verwendung eines Callbacks für Push-Ereignisse {#push-callback}

Braze stellt einen [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html)-Callback bereit, der ausgelöst wird, wenn Push-Benachrichtigungen empfangen, geöffnet oder verworfen werden. Es wird empfohlen, diesen Callback in Ihrem `Application.onCreate()` zu platzieren, um keine Ereignisse zu verpassen, die auftreten, während Ihre Anwendung nicht läuft.

{% alert note %}
Wenn Sie bisher einen angepassten Broadcast-Empfänger für diese Funktion in Ihrer Anwendung verwendet haben, können Sie ihn zugunsten dieser Integrationsoption bedenkenlos entfernen.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Bei Aktions-Buttons für Benachrichtigungen werden die `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`-Intents ausgelöst, wenn Buttons mit den Aktionen `opens app` oder `deep link` angeklickt werden. Die Handhabung von Deeplinks und Extras bleibt unverändert. Buttons mit `close`-Aktionen lösen keine `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED`-Intents aus und schließen die Benachrichtigung automatisch.
{% endalert %}

{% alert important %}
Erstellen Sie Ihren Listener für Push-Benachrichtigungen in `Application.onCreate`, um sicherzustellen, dass er getriggert wird, wenn Endnutzer:innen auf eine Benachrichtigung tippen, während sich Ihre App in einem beendeten Zustand befindet.
{% endalert %}

## Anpassen der Benachrichtigungsanzeige {#customization-display}

### Schritt 1: Angepasste Benachrichtigungs-Factory erstellen {#step-1-create-your-custom-notification-factory}

In manchen Szenarien möchten Sie Push-Benachrichtigungen auf eine Weise anpassen, die auf dem Server umständlich oder nicht verfügbar wäre. Um Ihnen die vollständige Kontrolle über die Benachrichtigungsanzeige zu geben, haben wir die Möglichkeit hinzugefügt, Ihre eigene [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) zu definieren, um Benachrichtigungsobjekte für die Anzeige durch Braze zu erstellen.

Wenn eine angepasste `IBrazeNotificationFactory` eingestellt ist, ruft Braze beim Push-Empfang die Methode `createNotification()` Ihrer Factory auf, bevor die Benachrichtigung den Nutzer:innen angezeigt wird. Braze übergibt ein `Bundle` mit Push-Daten von Braze und ein weiteres `Bundle` mit angepassten Schlüssel-Wert-Paaren, die entweder über das Dashboard oder die Messaging-APIs gesendet werden:

Braze übermittelt ein [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) mit Daten aus der Braze-Push-Benachrichtigung.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Sie können von Ihrer angepassten `createNotification()`-Methode `null` zurückgeben, um die Benachrichtigung vollständig zu unterdrücken, mit `BrazeNotificationFactory.getInstance().createNotification()` unser Standard-`notification`-Objekt für diese Daten abrufen und es vor der Anzeige modifizieren oder ein vollständig separates `notification`-Objekt für die Anzeige generieren.

{% alert note %}
Die Dokumentation zu den Push-Datenschlüsseln von Braze finden Sie im [Android SDK or Software-Development-Kit](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Schritt 2: Angepasste Benachrichtigungs-Factory einstellen {#step-2-set-your-custom-notification-factory}

Um Braze anzuweisen, Ihre angepasste Benachrichtigungs-Factory zu verwenden, nutzen Sie die Methode `setCustomBrazeNotificationFactory`, um Ihre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) einzustellen:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

Der empfohlene Ort, um Ihre angepasste `IBrazeNotificationFactory` einzustellen, ist die Lifecycle-Methode `Application.onCreate()` (nicht Activity). Dadurch kann die Benachrichtigungs-Factory korrekt eingerichtet werden, wenn Ihr App-Prozess aktiv ist.

{% alert important %}
Das Erstellen einer eigenen Benachrichtigung von Grund auf ist ein fortgeschrittener Anwendungsfall und sollte nur nach gründlichen Tests und einem umfassenden Verständnis der Push-Funktionalität von Braze durchgeführt werden. Sie müssen zum Beispiel sicherstellen, dass Ihre Benachrichtigung Push-Öffnungen korrekt protokolliert.
{% endalert %}

Um Ihre angepasste [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) zu deaktivieren und zur Standard-Braze-Behandlung für Push zurückzukehren, übergeben Sie `null` an den Setter der angepassten Benachrichtigungs-Factory:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Mehrfarbigen Text rendern {#rendering-multicolor-text}

In der Braze SDK or Software-Development-Kit-Version 3.1.1 kann HTML an ein Gerät gesendet werden, um mehrfarbigen Text in Push-Benachrichtigungen darzustellen.

![Eine Android-Push-Nachricht mit dem Text „Multicolor Push test message“, in der die Buchstaben unterschiedliche Farben aufweisen, kursiv geschrieben sind und einen farbigen Hintergrund haben.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Dieses Beispiel wird mit dem folgenden HTML-Code gerendert:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Bitte beachten Sie, dass Android die HTML-Elemente und -Tags einschränkt, die in Ihren Push-Benachrichtigungen zulässig sind. Zum Beispiel ist `marquee` nicht zulässig.

{% alert important %}
Die Darstellung von mehrfarbigem Text ist gerätespezifisch und wird möglicherweise je nach Android-Gerät oder -Version nicht angezeigt.
{% endalert %}

Um mehrfarbigen Text in einer Push-Benachrichtigung darzustellen, können Sie Ihre `braze.xml` oder `BrazeConfig` Update or aktualisieren or aktualisieren:

{% tabs local %}
{% tab braze.xml %}
Fügen Sie Folgendes in Ihrer `braze.xml` hinzu:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Fügen Sie Folgendes in Ihrer [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration#runtime-configuration) hinzu:

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Unterstützte HTML-Tags {#supported-html-tags}

Derzeit listet Google die unterstützten HTML-Tags für Android nicht direkt in seiner Dokumentation auf&#8212;diese Informationen sind nur in der [`Html.java`-Datei des Git-Repositorys](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java) zu finden. Bitte beachten Sie dies, wenn Sie sich auf die folgende Tabelle beziehen, da diese Informationen aus dieser Datei stammen und sich die unterstützten HTML-Tags ändern können.

<table aria-label="Unterstützte HTML-Tags">
  <thead>
    <tr>
      <th>Kategorie</th>
      <th>HTML-Tag</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Grundlegende Textformatierung</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Fettgedruckter Text</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Kursiver Text</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Unterstrichener Text</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Durchgestrichener Text</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Hochgestellter Text</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Tiefgestellter Text</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Monospace-Text</td>
    </tr>
    <tr>
      <td rowspan="3">Größe/Schriftart</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Relative Textgrößenänderungen</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Legt die Vordergrundfarbe fest</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (mit Inline-CSS)</td>
      <td>Inline-Stile (z. B. Farbe, Hintergrund)</td>
    </tr>
    <tr>
      <td rowspan="4">Absatz und Block</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Abschnitte auf Blockebene</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Zeilenumbruch</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Zitierter Block</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Ungeordnete Liste mit Aufzählungszeichen</td>
    </tr>
    <tr>
      <td>Überschriften</td>
      <td><code>&lt;h1&gt;</code> – <code>&lt;h6&gt;</code></td>
      <td>Überschriften (verschiedene Größen)</td>
    </tr>
    <tr>
      <td rowspan="2">Links und Bilder</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Klickbarer Link</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Inline-Bild</td>
    </tr>
    <tr>
      <td>Sonstiges Inline</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Synonyme für kursiv oder fett</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte HTML-Tags" }

## Inline-Bilder rendern {#rendering-inline-images}

### Funktionsweise {#how-it-works}

Mit Inline-Bild-Push können Sie ein größeres Bild in Ihrer Android-Push-Benachrichtigung präsentieren. Bei diesem Design müssen Nutzer:innen die Push-Benachrichtigung nicht mehr manuell erweitern, um das Bild zu vergrößern. Im Gegensatz zu normalen Android-Push-Benachrichtigungen haben Inline-Bild-Push-Bilder ein Seitenverhältnis von 3:2.

![Vorschau einer Android-Push-Benachrichtigung mit Inline-Bild-Darstellung.]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Kompatibilität {#compatibility}

Sie können Inline-Bilder an jedes Gerät senden. Geräte und SDKs, die nicht die Mindestversionen erfüllen, zeigen stattdessen ein Standardbild an. Damit Inline-Bilder korrekt angezeigt werden, sind sowohl das Android Braze SDK or Software-Development-Kit v10.0.0+ als auch ein Gerät mit Android M+ erforderlich. Das SDK or Software-Development-Kit muss ebenfalls aktiviert sein, damit das Bild gerendert werden kann.

{% alert note %}
Geräte mit Android 12 werden aufgrund von Änderungen bei den angepassten Push-Benachrichtigungsstilen anders dargestellt.
{% endalert %}

### Versenden eines Inline-Bild-Pushs {#sending-an-inline-image-push}

Wenn Sie eine Android-Push-Nachricht erstellen, ist diese Funktion im Dropdown-Menü **Notification Type** verfügbar.

![Der Push-Campaign-Editor zeigt die Position des Dropdown-Menüs „Notification Type“ oberhalb der Standard-Push-Vorschau.]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Einstellungen {#settings}

Für Android-Push-Benachrichtigungen, die über das Braze-Dashboard versendet werden, stehen zahlreiche erweiterte Einstellungen zur Verfügung. Dieser Artikel beschreibt diese Features und wie Sie sie erfolgreich nutzen können.

![Panel für erweiterte Einstellungen im Braze Android Push Composer.]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### Benachrichtigungs-ID {#notification-id}

Eine **Benachrichtigungs-ID** ist ein eindeutiger Bezeichner für eine von Ihnen gewählte Nachrichtenkategorie, der dem Messaging-Dienst mitteilt, dass er nur die jüngste Nachricht mit dieser ID berücksichtigen soll. Wenn Sie eine Benachrichtigungs-ID festlegen, können Sie nur die aktuellste und relevanteste Nachricht versenden, anstatt einen Stapel veralteter, irrelevanter Nachrichten.

#### Verhindern, dass identische Benachrichtigungen sich gegenseitig überschreiben {#preventing-duplicate-notifications-from-overwriting}

Standardmäßig generiert Android bei Push-Benachrichtigungen mit identischem Titel und Textkörper dieselbe Benachrichtigungs-ID für beide Nachrichten, indem Titel und Text zusammen gehasht werden. Dadurch überschreibt die zweite Benachrichtigung die erste, sodass nur eine einzige Benachrichtigung in der Benachrichtigungsleiste erscheint.

Um zu verhindern, dass identische Benachrichtigungen sich gegenseitig überschreiben, können Sie in Ihren Android-Push-Benachrichtigungseinstellungen eindeutige Benachrichtigungs-ID-Werte angeben. Hier sind einige Optionen:

- **Liquid-Templating mit Zeitstempel verwenden:** Generieren Sie einen eindeutigen Wert basierend auf der aktuellen Uhrzeit.

{% raw %}
```liquid
{% assign random_number = 'now' | date: '%s' | plus: 1000000 %}
{{random_number}}
```
{% endraw %}

- **Serverseitige Generierung:** Für wirklich zufällige Werte generieren Sie die Benachrichtigungs-ID auf Ihrem Server und übergeben sie über Liquid. Dadurch wird sichergestellt, dass jede Benachrichtigung einen eindeutigen Bezeichner hat, sodass mehrere Benachrichtigungen gleichzeitig angezeigt werden können.

### Priorität der Firebase-Nachrichtenzustellung {#fcm-priority}

Mit dem Feld [Firebase Messaging Delivery Priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority#setting-priority-for-messages) können Sie festlegen, ob ein Push mit „normaler“ oder „hoher“ Priorität an Firebase Cloud Messaging gesendet wird.

### Lebensdauer (TTL) {#ttl}

Im Feld **TTL** (TTL) können Sie eine angepasste Zeitspanne für die Speicherung von Nachrichten beim Push-Messaging-Dienst festlegen. Die Standardwerte für die Lebensdauer betragen vier Wochen für FCM und 31 Tage für ADM.

### Zusammenfassungstext {#summary-text}

Mit dem Zusammenfassungstext können Sie zusätzlichen Text in der erweiterten Benachrichtigungsansicht einstellen. Er dient auch als Bildunterschrift für Benachrichtigungen mit Bildern.

![Eine Android-Nachricht mit dem Titel „This is the title for the notification.“ und dem Zusammenfassungstext „This is the summary text for the notification.“]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Der Zusammenfassungstext wird in der erweiterten Ansicht unter dem Text der Nachricht angezeigt.

![Eine Android-Nachricht mit dem Titel „This is the title for the notification.“ und dem Zusammenfassungstext „This is the summary text for the notification.“]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Bei Push-Benachrichtigungen, die Bilder enthalten, wird der Nachrichtentext in der eingeklappten Ansicht angezeigt, während der Zusammenfassungstext als Bildunterschrift angezeigt wird, wenn die Benachrichtigung erweitert wird.

### Angepasste URIs {#custom-uri}

Mit der Funktion **Custom URI** können Sie eine Web-URL oder eine Android-Ressource angeben, zu der navigiert werden soll, wenn die Benachrichtigung angeklickt wird. Wenn keine angepasste URI angegeben ist, gelangen Nutzer:innen durch Klicken auf die Benachrichtigung zu Ihrer App. Sie können die angepasste URI verwenden, um Deeplinks in Ihrer App zu setzen und Nutzer:innen zu Ressourcen außerhalb Ihrer App zu leiten. Dies kann über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) oder unser Dashboard unter **Advanced Settings** im Push Composer wie abgebildet festgelegt werden:

![Die erweiterten Einstellungen für Deeplinking im Braze Push Composer.]({% image_buster /assets/img_archive/deep_link.png %})

### Benachrichtigungs-Anzeigepriorität {#notification-priority}

{% alert important %}
Die Einstellung für die Benachrichtigungs-Anzeigepriorität wird auf Geräten mit Android O oder neuer nicht mehr verwendet. Bei neueren Geräten legen Sie die Priorität über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) fest.
{% endalert %}

Die Prioritätsstufe einer Push-Benachrichtigung wirkt sich darauf aus, wie Ihre Benachrichtigung im Vergleich zu anderen Benachrichtigungen in der Benachrichtigungsleiste angezeigt wird. Dies kann sich auch auf die Geschwindigkeit und die Art der Zustellung auswirken, da normale Nachrichten und Nachrichten mit geringerer Priorität mit etwas höherer Latenz oder in Stapeln gesendet werden, um den Akku zu schonen, während Nachrichten mit hoher Priorität immer sofort gesendet werden.

In Android O wurde die Benachrichtigungspriorität eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrer Entwickler:in zusammenarbeiten, um die Priorität für einen Kanal während seiner Konfiguration festzulegen, und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungstöne senden. Bei Geräten, auf denen Android-Versionen vor O laufen, ist es möglich, über das Braze-Dashboard und die Messaging-API eine Prioritätsstufe für Android-Benachrichtigungen festzulegen.

Um Ihre gesamte Nutzerbasis mit einer bestimmten Priorität zu benachrichtigen, empfehlen wir Ihnen, die Priorität indirekt über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels#importance) festzulegen (für O+-Geräte) *und* die individuelle Priorität über das Dashboard zu senden (für &#60;O-Geräte).

Die Prioritätsstufen, die Sie bei Push-Benachrichtigungen für Android oder Fire OS einstellen können, sind:

| Priorität | Beschreibung/Verwendungszweck | `priority`-Wert (für API-Nachrichten) |
|----------|--------------------------|-------------------------------------|
| Max.      | Dringende oder zeitkritische Nachrichten | `2` |
| Hoch     | Wichtige Mitteilungen, wie z. B. eine neue Nachricht von einer Freund:in | `1` |
| Standard  | Die meisten Benachrichtigungen – verwenden Sie diese Option, wenn Ihre Nachricht nicht ausdrücklich unter eine der anderen Prioritätsarten fällt | `0` |
| Niedrig      | Informationen, die Sie Ihren Nutzer:innen mitteilen möchten, die aber keine sofortige Aktion erfordern | `-1` |
| Min.      | Kontextuelle oder Hintergrundinformationen | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Benachrichtigungs-Anzeigepriorität" }

Weitere Informationen finden Sie in der Google-Dokumentation zu [Android-Benachrichtigungen](http://developer.android.com/design/patterns/notifications.html).

### Töne {#sounds}

In Android O wurden die Benachrichtigungstöne eine Eigenschaft der Benachrichtigungskanäle. Sie müssen mit Ihrer Entwickler:in zusammenarbeiten, um den Ton für einen Kanal während seiner Konfiguration zu definieren, und dann das Dashboard verwenden, um den richtigen Kanal auszuwählen, wenn Sie Ihre Benachrichtigungen senden.

Für Geräte mit Android-Versionen vor O können Sie mit Braze den Ton einer einzelnen Push-Nachricht über den Dashboard Composer einstellen. Hierzu können Sie eine lokale Tonressource auf dem Gerät angeben (z. B. `android.resource://com.mycompany.myapp/raw/mysound`). Wenn Sie in diesem Feld „default“ angeben, wird der standardmäßige Benachrichtigungston auf dem Gerät abgespielt. Dies kann über die [Messaging-API]({{site.baseurl}}/api/endpoints/messaging) oder das Dashboard unter **Advanced Settings** im Push Composer festgelegt werden.

![Die erweiterten Toneinstellungen im Braze Push Composer.]({% image_buster /assets/img_archive/sound_android.png %})

Geben Sie die vollständige URI der Tonressource (z. B. `android.resource://com.mycompany.myapp/raw/mysound`) in die Eingabeaufforderung des Dashboards ein.

Um Ihre gesamte Nutzerbasis mit einem bestimmten Ton zu benachrichtigen, empfehlen wir Ihnen, den Ton indirekt über die [Konfiguration des Benachrichtigungskanals](https://developer.android.com/training/notify-user/channels) festzulegen (für O+-Geräte) *und* den individuellen Ton über das Dashboard zu senden (für &#60;O-Geräte).