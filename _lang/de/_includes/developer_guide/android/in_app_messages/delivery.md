{% multi_lang_include developer_guide/prerequisites/android.md %}

## Nachrichten triggern {#message-triggers}

### Trigger-Typen {#trigger-types}

In-App-Nachrichten werden automatisch getriggert, wenn das SDK einen der folgenden angepassten Event-Typen protokolliert: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Beachten Sie, dass die Trigger `Specific Purchase` und `Custom Event` auch robuste Filter für Eigenschaften enthalten.

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Events getriggert werden – nur durch angepasste Events, die vom SDK protokolliert werden. Mehr über die Protokollierung erfahren Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Zustellungssemantik {#delivery-semantics}

Alle infrage kommenden In-App-Nachrichten werden zu Beginn der Sitzung an das Gerät der Nutzer:innen zugestellt. Bei der Zustellung ruft das SDK die Assets im Voraus ab, damit sie zum Zeitpunkt des Triggerns verfügbar sind und die Anzeigelatenz minimiert wird. Wenn das triggernde Event mehr als eine infrage kommende In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt.

Weitere Informationen über die Semantik des SDK für den Sitzungsstart finden Sie unter [Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android).

### Rate-Limits {#rate-limit}

Standardmäßig begrenzt das SDK die Rate für getriggerte In-App-Nachrichten auf einmal alle 30 Sekunden, um ein hochwertiges Nutzererlebnis zu unterstützen.

Setzen Sie diesen Wert bei Produktions-Apps nicht unter 10 Sekunden, damit Nutzer:innen nicht mit aufeinanderfolgenden In-App-Nachrichten überhäuft werden. Für Tests und Beispiel-App-Flows sind 5 Sekunden eine gängige Einstellung.

Sie können dieses Intervall zu Testzwecken auf `0` setzen. Ein Intervall von `0` Sekunden erzwingt jedoch nicht, dass mehrere In-App-Nachrichten gleichzeitig erscheinen. Wenn eine Nachricht noch sichtbar ist, wird die nächste Nachricht erst angezeigt, nachdem die aktuelle Nachricht geschlossen wurde.

Um diesen Wert zu überschreiben, setzen Sie `com_braze_trigger_action_minimum_time_interval_seconds` in Ihrer `braze.xml` wie folgt:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Schlüssel-Wert-Paare {#key-value-pairs}

Wenn Sie eine Campaign in Braze erstellen, können Sie Schlüssel-Wert-Paare als `extras` festlegen, die das In-App-Messaging-Objekt verwenden kann, um Daten an Ihre App zu senden. Zum Beispiel:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
Weitere Informationen finden Sie in der [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}

## Automatische Trigger deaktivieren {#disabling-automatic-triggers}

So verhindern Sie, dass In-App-Nachrichten automatisch getriggert werden:

1. Stellen Sie sicher, dass Sie die automatische Initialisierung der Integration verwenden, die ab Version `2.2.0` standardmäßig aktiviert ist.
2. Setzen Sie die Standardoperation für In-App-Nachrichten auf `DISCARD`, indem Sie die folgende Zeile in Ihre Datei `braze.xml` einfügen.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Nachrichten manuell triggern {#manually-triggering-messages}

Standardmäßig werden In-App-Nachrichten automatisch getriggert, wenn das SDK ein angepasstes Event protokolliert. Sie können eine Nachricht jedoch auch manuell mit den folgenden Methoden triggern.

### Ein serverseitiges Event verwenden {#using-a-server-side-event}

Um eine In-App-Nachricht über ein vom Server gesendetes Event zu triggern, senden Sie eine stille Push-Benachrichtigung an das Gerät, die einen angepassten Push-Callback zur Protokollierung eines SDK-basierten Events ermöglicht. Dieses Event triggert dann die für Nutzer:innen sichtbare In-App-Nachricht.

#### 1. Schritt: Erstellen Sie einen Push-Callback, um den stillen Push zu empfangen {#step-1-create-a-push-callback-to-receive-the-silent-push}

Registrieren Sie [Ihren angepassten Push-Callback]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback), um auf eine bestimmte stille Push-Benachrichtigung zu warten.

Im folgenden Beispiel werden zwei Events für die zuzustellende In-App-Nachricht protokolliert – eines vom Server und eines von Ihrem angepassten Push-Callback. Um sicherzustellen, dass dasselbe Event nicht dupliziert wird, sollte das von Ihrem Push-Callback protokollierte Event einer generischen Namenskonvention folgen, z. B. „In-App-Nachricht Trigger-Event“, und nicht denselben Namen tragen wie das vom Server gesendete Event. Andernfalls können die Segmentierung und die Nutzerdaten dadurch beeinträchtigt werden, dass für eine einzelne Nutzeraktion doppelte Events protokolliert werden.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

#### 2. Schritt: Erstellen Sie eine Push-Campaign {#step-2-create-a-push-campaign}

Erstellen Sie eine [stille Push-Campaign]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android), die über das vom Server gesendete Event getriggert wird.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

Die Push-Campaign muss Schlüssel-Wert-Paare als Extras enthalten, die angeben, dass diese Push-Campaign gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird verwendet, um die In-App-Nachricht zu triggern.

![Zwei Sätze von Schlüssel-Wert-Paaren: IS_SERVER_EVENT auf „true“ gesetzt und CAMPAIGN_NAME auf „example campaign name“ gesetzt.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Der zuvor gezeigte Push-Callback-Code erkennt die Schlüssel-Wert-Paare und protokolliert das entsprechende angepasste SDK-Event.

Wenn Sie Ihrem „In-App-Nachricht Trigger“-Event Event-Eigenschaften hinzufügen möchten, können Sie diese in den Schlüssel-Wert-Paaren des Push-Payloads übergeben. In diesem Beispiel wurde der Campaign-Name der nachfolgenden In-App-Nachricht eingefügt. Ihr angepasster Push-Callback kann dann bei der Protokollierung des angepassten Events den Wert als Parameter der Event-Eigenschaft übergeben.

#### 3. Schritt: In-App-Nachricht-Campaign erstellen {#step-3-create-an-in-app-message-campaign}

Erstellen Sie Ihre für Nutzer:innen sichtbare In-App-Nachricht-Campaign im Braze-Dashboard. Diese Campaign sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event getriggert werden, das in Ihrem angepassten Push-Callback protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft als Teil des ursprünglichen stillen Push gesendet wurde.

![Eine Campaign mit aktionsbasierter Zustellung, bei der eine In-App-Nachricht getriggert wird, wenn „campaign_name“ gleich „IAM campaign name example“ ist.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Wenn ein vom Server gesendetes Event protokolliert wird, während sich die App nicht im Vordergrund befindet, wird das Event protokolliert, aber die In-App-Nachricht wird nicht angezeigt. Wenn Sie möchten, dass das Event verzögert wird, bis die Anwendung im Vordergrund ist, muss in Ihrem angepassten Push-Empfänger eine Prüfung eingebaut werden, um das Event zu verwerfen oder zu verzögern, bis die App in den Vordergrund getreten ist.

### Anzeige einer vordefinierten Nachricht {#displaying-a-pre-defined-message}

Um eine vordefinierte In-App-Nachricht manuell anzuzeigen, verwenden Sie die folgende Methode:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

### Anzeige einer Nachricht in Realtime {#displaying-a-message-in-real-time}

Sie können auch lokale In-App-Nachrichten in Realtime erstellen und anzeigen, wobei dieselben Anpassungsoptionen wie im Dashboard zur Verfügung stehen. Gehen Sie dazu wie folgt vor:

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
Zeigen Sie keine In-App-Nachrichten an, wenn die Softtastatur auf dem Bildschirm angezeigt wird, da das Rendering unter diesen Umständen undefiniert ist.
{% endalert %}