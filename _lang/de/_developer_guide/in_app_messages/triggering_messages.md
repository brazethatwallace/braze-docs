---
nav_title: Nachrichten Trigger or triggern or triggern
article_title: "In-App-Nachrichten Trigger or triggern or triggern"
page_order: 0.2
description: "Erfahren Sie, wie Sie In-App-Nachrichten über das Braze SDK or Software-Development-Kit Trigger or triggern or triggern können, einschließlich der Verkettung von Nachrichten in einer Sitzung und dem Außerkraftsetzen des Standard-Rate-Limits."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# In-App-Nachrichten Trigger or triggern or triggern {#trigger-in-app-messages}

> Erfahren Sie, wie Sie In-App-Nachrichten über das Braze SDK or Software-Development-Kit Trigger or triggern or triggern können.

## Nachrichten-Trigger or triggern und Zustellung {#message-triggers-and-delivery}

In-App-Nachrichten werden getriggert, wenn das SDK or Software-Development-Kit einen der folgenden angepassten Event-Typen protokolliert: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase` und `Custom Event` (die letzten beiden enthalten umfangreiche Eigenschafts-Filter).

Zu Beginn der Sitzung eines Nutzers bzw. einer Nutzerin liefert Braze alle berechtigten In-App-Nachrichten an das Gerät und ruft gleichzeitig Assets vorab ab, um die Anzeigelatenz zu minimieren. Wenn das Trigger or triggern-Event mehr als eine berechtigte In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt. Weitere Informationen finden Sie unter [Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/analytics/tracking_sessions).

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Events getriggert werden – nur durch angepasste Events, die vom SDK or Software-Development-Kit protokolliert werden. Weitere Informationen zur Protokollierung finden Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events).
{% endalert %}

## Typen von In-App-Nachrichten {#types-of-in-app-messages}

Braze sendet die folgenden Typen von In-App-Nachrichten beim Sitzungsstart an die Geräte der Nutzer:innen: `inapp` und `templated_iam`. Als Dashboard-Nutzer:in sehen Sie die verschiedenen Typen nicht, aber Braze behandelt sie je nach Konfiguration und Inhalt unterschiedlich.

### `inapp` (Standard) {#inapp-standard}

Eine `inapp`-In-App-Nachricht (oder „[Standard]({{site.baseurl}}/user_guide/channels/in_app_messages)“-In-App-Nachricht) ist bereits mit den notwendigen Informationen vorausgefüllt, wie z. B. angepasste Attribute, die Braze bereits kennt. Wenn die In-App-Nachricht auf das Gerät heruntergeladen wird, bewirkt das Trigger or triggern-Event in der Regel, dass das SDK or Software-Development-Kit die `inapp`-In-App-Nachricht anzeigt – auch wenn das Gerät offline oder im Flugmodus ist.

### `templated_iam` (templated) {#templated_iam-templated}

Eine `templated_iam`-In-App-Nachricht (oder „templated“-In-App-Nachricht) ist noch nicht mit den notwendigen Informationen vorausgefüllt. Braze muss eine weitere Anfrage stellen, um die Informationen abzurufen, bevor die Nachricht angezeigt werden kann.

In-App-Nachrichten werden als templated In-App-Nachrichten zugestellt, wenn **Campaign-Berechtigung vor der Anzeige erneut prüfen** ausgewählt ist oder wenn einer der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- Kurzmitteilungsdienst or SMS-Variablen wie {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Das bedeutet, dass das Gerät beim Sitzungsstart den Trigger or triggern dieser In-App-Nachricht erhält, nicht die gesamte Nachricht. Wenn die Nutzer:innen die In-App-Nachricht Trigger or triggern or triggern, stellt ihr Gerät eine Netzwerkanfrage, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Internetzugang hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Liquid-Logik zu lange für die Auflösung benötigt.
{% endalert %}

## Schlüssel-Wert-Paare {#key-value-pairs}

Wenn Sie eine Campaign in Braze erstellen, können Sie Schlüssel-Wert-Paare als `extras` festlegen, die das In-App-Nachricht-Objekt verwenden kann, um Daten an Ihre App zu senden.

{% tabs %}
{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Weitere Informationen finden Sie in der [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
Das folgende Beispiel verwendet angepasste Logik, um die Darstellung einer In-App-Nachricht basierend auf ihren Schlüssel-Wert-Paaren in `extras` festzulegen. Ein vollständiges Anpassungsbeispiel finden Sie in [unserer Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Automatische Trigger or triggern deaktivieren {#disabling-automatic-triggers}

Standardmäßig werden In-App-Nachrichten automatisch getriggert. So deaktivieren Sie dies:

{% tabs %}

{% tab web %}
Entfernen Sie den Aufruf von `braze.automaticallyShowInAppMessages()` aus Ihrem Lade-Snippet und erstellen Sie anschließend eine eigene Logik, um die Anzeige einer In-App-Nachricht zu steuern.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Wenn Sie `braze.showInAppMessage` aufrufen, ohne `braze.automaticallyShowInAppMessages()` zu entfernen, werden Nachrichten möglicherweise doppelt angezeigt.
{% endalert %}

Für eine erweiterte Steuerung des Nachrichtenzeitpunkts, einschließlich dem Verzögern und Wiederherstellen von getriggerten Nachrichten, lesen Sie unser [Tutorial: Getriggerte Nachrichten verzögern und wiederherstellen]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab android %}
1. Implementieren Sie den [`IInAppMessageManagerListener`]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener), um einen angepassten Listener festzulegen.
2. Update or aktualisieren or aktualisieren Sie Ihre [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html)-Methode, sodass sie [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html) zurückgibt.

Für eine erweiterte Steuerung des Nachrichtenzeitpunkts, einschließlich späterer Anzeige und erneutem Einreihen in die Warteschlange, lesen Sie unsere Seite [Nachrichten anpassen]({{site.baseurl}}/developer_guide/in_app_messages/customization?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener).
{% endtab %}

{% tab swift %}
1. Implementieren Sie den `BrazeInAppMessageUIDelegate`-Delegate in Ihrer App. Eine vollständige Anleitung finden Sie unter [Tutorial: In-App Message UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Update or aktualisieren or aktualisieren Sie Ihre `inAppMessage(_:displayChoiceForMessage:)`-Delegate-Methode, sodass sie `.discard` zurückgibt.

Für eine erweiterte Steuerung des Nachrichtenzeitpunkts, einschließlich dem Verzögern und Wiederherstellen von getriggerten Nachrichten, lesen Sie unser [Tutorial: Getriggerte Nachrichten verzögern und wiederherstellen]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).
{% endtab %}

{% tab flutter %}
1. Stellen Sie sicher, dass Sie den automatischen Integrations-Initializer verwenden, der in Version `2.2.0` und höher standardmäßig aktiviert ist.
2. Setzen Sie die Standard-In-App-Nachrichtenoperation auf `DISCARD`, indem Sie die folgende Zeile zu Ihrer `braze.xml`-Datei hinzufügen.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
Deaktivieren Sie für Android die Option **Automatically Display In-App Messages** im Braze-Konfigurationseditor. Alternativ können Sie `com_braze_inapp_show_inapp_messages_automatically` in der Datei `braze.xml` Ihres Unity-Projekts auf `false` setzen.

Die anfängliche Anzeigeoperation für In-App-Nachrichten kann in der Braze-Konfiguration über „In App Message Manager:in Initial Display Operation“ festgelegt werden.
{% endsubtab %}

{% subtab iOS %}
Legen Sie für iOS die Spielobjekt-Listener im Braze-Konfigurationseditor fest und stellen Sie sicher, dass **Braze Displays In-App Messages** nicht ausgewählt ist.

Die anfängliche Anzeigeoperation für In-App-Nachrichten kann in der Braze-Konfiguration über „In App Message Manager:in Initial Display Operation“ festgelegt werden.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Verkettung von zwei In-App-Nachrichten in einer Sitzung {#chaining-two-in-app-messages-in-one-session}

Sie können eine In-App-Nachricht beim Sitzungsstart Trigger or triggern or triggern und dann eine zweite In-App-Nachricht auslösen, nachdem ein Button in der ersten Nachricht gedrückt wurde. Loggen Sie dazu ein angepasstes Event für den Button-Klick, das die zweite Nachricht triggert. Der Trigger or triggern für die zweite Nachricht muss bereits auf dem Gerät vorhanden sein (die Nutzer:innen müssen bereits für die zweite Nachricht berechtigt sein) und auf der Geräteseite ausgelöst werden (das Braze SDK or Software-Development-Kit erkennt keine Änderungen an angepassten Attributen, die auf den Braze-Servern vorgenommen werden). Die standardmäßige 30-Sekunden-Abklingzeit zwischen In-App-Nachricht-Trigger or triggern or triggern muss angepasst werden, um mehrere In-App-Nachrichten in schneller Folge anzuzeigen. Informationen zur plattformspezifischen Konfiguration finden Sie unter [Überschreiben des Standard-Rate-Limits](#overriding-the-default-rate-limit).

## Überschreiben des Standard-Rate-Limits {#overriding-the-default-rate-limit}

Standardmäßig begrenzt das SDK or Software-Development-Kit getriggerte In-App-Nachrichten auf einmal alle 30 Sekunden. Um dies zu überschreiben, fügen Sie die folgende Eigenschaft zu Ihrer Konfigurationsdatei hinzu, bevor die Braze-Instanz initialisiert wird. Dieser Wert wird als neues Rate-Limit in Sekunden verwendet.

Setzen Sie diesen Wert bei Produktions-Apps nicht unter 10 Sekunden, damit Nutzer:innen nicht mit aufeinanderfolgenden In-App-Nachrichten überhäuft werden. Für Tests und Beispiel-App-Abläufe sind 5 Sekunden eine gängige Einstellung.

Sie können dieses Intervall zu Testzwecken auf `0` setzen. Ein Intervall von `0` Sekunden erzwingt jedoch nicht, dass mehrere In-App-Nachrichten gleichzeitig angezeigt werden. Wenn bereits eine In-App-Nachricht sichtbar ist, wird eine weitere getriggerte Nachricht erst angezeigt, wenn die aktuelle Nachricht geschlossen wird.

{% tabs %}
{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Manuelles Trigger or triggern or triggern von Nachrichten {#manually-triggering-messages}

Standardmäßig werden In-App-Nachrichten automatisch getriggert, wenn das SDK or Software-Development-Kit ein angepasstes Event protokolliert. Darüber hinaus können Sie Nachrichten jedoch auch manuell Trigger or triggern or triggern, indem Sie die folgenden Methoden verwenden.

### Verwenden eines serverseitigen Events {#using-a-server-side-event}

{% tabs %}
{% tab web %}
Derzeit unterstützt das Braze Web SDK or Software-Development-Kit das manuelle Trigger or triggern or triggern von Nachrichten über serverseitige Events nicht.
{% endtab %}

{% tab android %}
Um eine In-App-Nachricht über ein vom Server gesendetes Event zu Trigger or triggern or triggern, senden Sie eine stille Push-Benachrichtigung an das Gerät. So kann ein angepasster Push-Callback ein SDK or Software-Development-Kit-basiertes Event protokollieren. Dieses Event triggert dann die für Nutzer:innen sichtbare In-App-Nachricht.

#### Schritt 1: Einen Push-Callback erstellen, um die stille Push-Benachrichtigung zu empfangen {#step-1-create-a-push-callback-to-receive-the-silent-push}

Registrierung or registrieren Sie Ihren angepassten Push-Callback, um auf eine bestimmte stille Push-Benachrichtigung zu lauschen. Weitere Informationen finden Sie unter [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications#android_setting-up-push-notifications).

Zwei Events werden protokolliert, damit die In-App-Nachricht zugestellt wird: eines vom Server und eines aus Ihrem angepassten Push-Callback heraus. Um sicherzustellen, dass dasselbe Event nicht dupliziert wird, sollte das aus Ihrem Push-Callback heraus protokollierte Event einer generischen Namenskonvention folgen, z. B. „In-App-Nachricht-Trigger or triggern-Event“, und nicht denselben Namen wie das vom Server gesendete Event haben. Andernfalls können Segmentierung und Nutzerdaten durch doppelt protokollierte Events für eine einzelne Nutzeraktion beeinträchtigt werden.

{% subtabs %}
{% subtab JAVA %}

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

{% endsubtab %}
{% subtab KOTLIN %}

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

{% endsubtab %}
{% endsubtabs %}

#### Schritt 2: Eine Push-Campaign erstellen {#step-2-create-a-push-campaign}

Erstellen Sie eine [stille Push-Campaign]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android), die über das vom Server gesendete Event getriggert wird.

![Zustellungsschritt einer stillen Push-Campaign, konfiguriert für aktionsbasierte Zustellung mit einem angepassten Event-Trigger or triggern „server_event“.]({% image_buster /assets/img_archive/serverSentPush.png %})

Die Push-Campaign muss Schlüssel-Wert-Paar-Extras enthalten, die angeben, dass diese Push-Campaign gesendet wird, um ein angepasstes SDK or Software-Development-Kit-Event zu protokollieren. Dieses Event wird verwendet, um die In-App-Nachricht zu Trigger or triggern or triggern.

![Zwei Schlüssel-Wert-Paare: IS_SERVER_EVENT auf „true“ gesetzt und CAMPAIGN_NAME auf „example campaign name“ gesetzt.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Der oben gezeigte Push-Callback-Beispielcode erkennt die Schlüssel-Wert-Paare und protokolliert das entsprechende angepasste SDK or Software-Development-Kit-Event.

Wenn Sie Event-Eigenschaften an Ihr „In-App-Nachricht-Trigger or triggern“-Event anhängen möchten, können Sie diese in den Schlüssel-Wert-Paaren des Push-Payloads übergeben. In diesem Beispiel wurde der Campaign-Name der nachfolgenden In-App-Nachricht einbezogen. Ihr angepasster Push-Callback kann den Wert dann als Parameter der Event-Eigenschaft übergeben, wenn das angepasste Event protokolliert wird.

#### Schritt 3: Eine In-App-Nachricht-Campaign erstellen {#step-3-create-an-in-app-message-campaign}

Erstellen Sie Ihre für Nutzer:innen sichtbare In-App-Nachricht-Campaign im Braze-Dashboard. Diese Campaign sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event getriggert werden, das aus Ihrem angepassten Push-Callback heraus protokolliert wurde.

Im folgenden Beispiel wurde die spezifische In-App-Nachricht, die getriggert werden soll, konfiguriert, indem die Event-Eigenschaft als Teil der initialen stillen Push-Benachrichtigung gesendet wurde.

![Eine aktionsbasierte Zustellungs-Campaign, bei der eine In-App-Nachricht getriggert wird, wenn „campaign_name“ gleich „IAM campaign name example“ ist.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Wenn ein vom Server gesendetes Event protokolliert wird, während die App nicht im Vordergrund ist, wird das Event protokolliert, aber die In-App-Nachricht wird nicht angezeigt. Wenn Sie möchten, dass das Event verzögert wird, bis die Anwendung im Vordergrund ist, muss in Ihrem angepassten Push-Receiver eine Prüfung enthalten sein, um das Event zu verwerfen oder zu verzögern, bis die App in den Vordergrund gelangt ist.
{% endtab %}

{% tab swift %}
#### Schritt 1: Stille Push-Benachrichtigungen und Schlüssel-Wert-Paare verarbeiten {#step-1-handle-silent-push-and-key-value-pairs}

Implementieren Sie die folgende Funktion und rufen Sie sie innerhalb der [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`-Methode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:)) auf:

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

Wenn die stille Push-Benachrichtigung empfangen wird, wird ein SDK or Software-Development-Kit-erfasstes Event „In-App-Nachricht-Trigger or triggern“ gegen das Kundenprofil or Nutzerprofil protokolliert.

{% alert important %}
Da eine Push-Nachricht verwendet wird, um ein SDK or Software-Development-Kit-protokolliertes angepasstes Event aufzuzeichnen, muss Braze für jede:n Nutzer:in ein Push-Token / Textbaustein speichern, um diese Lösung zu ermöglichen. Für iOS-Nutzer:innen speichert Braze ein Token / Textbaustein erst ab dem Zeitpunkt, an dem Nutzer:innen die Push-Eingabeaufforderung des Betriebssystems erhalten haben. Vorher sind Nutzer:innen nicht per Push erreichbar, und die oben beschriebene Lösung ist nicht möglich.
{% endalert %}

#### Schritt 2: Eine stille Push-Campaign erstellen {#step-2-create-a-silent-push-campaign}

Erstellen Sie eine [stille Push-Campaign]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift), die über das vom Server gesendete Event getriggert wird.

![Eine aktionsbasierte Zustellungs-In-App-Nachricht-Campaign, die an Nutzer:innen zugestellt wird, deren Nutzerprofile das angepasste Event „server_event“ aufweisen.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

Die Push-Campaign muss Schlüssel-Wert-Paar-Extras enthalten, die angeben, dass diese Push-Campaign gesendet wird, um ein angepasstes SDK or Software-Development-Kit-Event zu protokollieren. Dieses Event wird verwendet, um die In-App-Nachricht zu Trigger or triggern or triggern.

![Eine aktionsbasierte Zustellungs-In-App-Nachricht-Campaign mit zwei Schlüssel-Wert-Paaren. „CAMPAIGN_NAME“ auf „In-app message name example“ gesetzt und „IS_SERVER_EVENT“ auf „true“ gesetzt.]({% image_buster /assets/img_archive/iOSServerPush.png %})

Der Code innerhalb der `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`-Methode prüft den Schlüssel `IS_SERVER_EVENT` und protokolliert ein angepasstes SDK or Software-Development-Kit-Event, falls dieser vorhanden ist.

Sie können entweder den Event-Namen oder die Event-Eigenschaften ändern, indem Sie den gewünschten Wert innerhalb der Schlüssel-Wert-Paar-Extras des Push-Payloads senden. Beim Protokollieren des angepassten Events können diese Extras als Parameter des Event-Namens oder als Event-Eigenschaft verwendet werden.

#### Schritt 3: Eine In-App-Nachricht-Campaign erstellen

Erstellen Sie Ihre für Nutzer:innen sichtbare In-App-Nachricht-Campaign im Braze-Dashboard. Diese Campaign sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event getriggert werden, das innerhalb der `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`-Methode protokolliert wurde.

Im folgenden Beispiel wurde die spezifische In-App-Nachricht, die getriggert werden soll, konfiguriert, indem die Event-Eigenschaft als Teil der initialen stillen Push-Benachrichtigung gesendet wurde.

![Eine aktionsbasierte Zustellungs-In-App-Nachricht-Campaign, die an Nutzer:innen zugestellt wird, die das angepasste Event „In-app message Trigger or triggern“ ausführen, wobei „campaign_name“ gleich „IAM Campaign Name Example“ ist.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Beachten Sie, dass diese In-App-Nachrichten nur getriggert werden, wenn die stille Push-Benachrichtigung empfangen wird, während die Anwendung im Vordergrund ist.
{% endalert %}
{% endtab %}
{% endtabs %}

### Anzeigen einer vordefinierten Nachricht {#displaying-a-pre-defined-message}

Um eine vordefinierte In-App-Nachricht manuell anzuzeigen, verwenden Sie die folgende Methode:

{% tabs %}
{% tab web %}
Verwenden Sie für das Web SDK or Software-Development-Kit `braze.showInAppMessage(inAppMessage)`, um eine beliebige In-App-Nachricht anzuzeigen. Einzelheiten und ein Beispiel finden Sie unter [Anzeigen einer Nachricht in Realtime](#displaying-a-message-in-real-time).
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### Anzeigen einer Nachricht in Realtime {#displaying-a-message-in-real-time}

Sie können auch lokale In-App-Nachrichten in Realtime erstellen und anzeigen, wobei dieselben Anpassungsoptionen wie im Dashboard verfügbar sind. Gehen Sie dazu wie folgt vor:

{% tabs %}
{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Zeigen Sie keine In-App-Nachrichten an, wenn die Bildschirmtastatur eingeblendet ist, da das Rendering in diesem Fall nicht definiert ist.
{% endalert %}
{% endtab %}

{% tab swift %}
Rufen Sie manuell die [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))-Methode auf Ihrem `inAppMessagePresenter` auf. Beispiel:

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Wenn Sie Ihre eigene In-App-Nachricht erstellen, verzichten Sie auf jegliches Analytics-Tracking und müssen das Klick- und Impression-Logging manuell über Ihren `message.context` verwalten.
{% endalert %}
{% endtab %}

{% tab unity %}
Um die nächste Nachricht im Stack anzuzeigen, verwenden Sie die Methode `DisplayNextInAppMessage()`. Nachrichten werden in diesem Stack gespeichert, wenn `DISPLAY_LATER` oder `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` als Anzeigeaktion für die In-App-Nachricht gewählt wird.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Ursachen für Verzögerungen bei In-App-Nachrichten {#causes-of-in-app-message-delays}

Wenn Sie eine In-App-Nachrichten-Campaign einige Sekunden nach Sitzungsbeginn erhalten, kann die Verzögerung folgende Ursachen haben:

- Eine Verzögerung beim Campaign-Trigger or triggern
- Anpassungen
- Das Trigger or triggern-Event wurde später als erwartet aufgezeichnet (z. B. bei einem `templated_iam`)

## Exit-Intent-Nachrichten für Web {#exit-intent-messages-for-web}

Exit-Intent-Nachrichten sind nicht-störende In-App-Nachrichten, die verwendet werden, um Besucher:innen wichtige Informationen mitzuteilen, bevor sie Ihre Website verlassen.

Um Trigger or triggern für diese Nachrichtentypen im Web-SDK or Software-Development-Kit einzurichten, implementieren Sie eine Exit-Intent-Bibliothek in Ihrer Website (z. B. die [Open-Source-Bibliothek von ouibounce](https://github.com/carlsednaoui/ouibounce)) und verwenden Sie dann den folgenden Code, um `'exit intent'` als angepasstes Event in Braze zu protokollieren. Ihre zukünftigen In-App-Nachricht-Campaigns können diesen Nachrichtentyp dann als Trigger or triggern für ein angepasstes Event verwenden.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
