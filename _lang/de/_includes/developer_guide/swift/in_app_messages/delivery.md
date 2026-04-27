{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Nachrichten triggern {#message-triggers}

### Trigger-Typen {#trigger-types}

In-App-Nachrichten werden automatisch getriggert, wenn das SDK einen der folgenden angepassten Event-Typen protokolliert: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Beachten Sie, dass die Trigger `Specific Purchase` und `Custom Event` auch robuste Filter für Eigenschaften enthalten.

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Events getriggert werden – nur durch angepasste Events, die vom SDK protokolliert werden. Mehr über die Protokollierung erfahren Sie unter [Angepasste Events protokollieren]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Zustellungssemantik {#delivery-semantics}

Alle infrage kommenden In-App-Nachrichten werden zu Beginn der Sitzung an das Gerät der Nutzer:innen zugestellt. Bei der Zustellung ruft das SDK die Assets im Voraus ab, damit sie zum Zeitpunkt des Triggerns verfügbar sind und die Anzeigelatenz minimiert wird. Wenn das triggernde Event mehr als eine infrage kommende In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt.

Weitere Informationen über die Semantik des SDK für den Sitzungsstart finden Sie unter [Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift).

### Standard-Rate-Limit {#default-rate-limit}

Standardmäßig begrenzt das SDK getriggerte In-App-Nachrichten auf einmal alle 30 Sekunden.

Setzen Sie diesen Wert bei Produktions-Apps nicht unter 10 Sekunden, damit Nutzer:innen nicht mit aufeinanderfolgenden In-App-Nachrichten überhäuft werden. Für Tests und Beispiel-App-Flows ist ein Wert von 5 Sekunden eine gängige Einstellung.

Sie können dieses Intervall zu Testzwecken auf `0` setzen. Ein Intervall von `0` Sekunden erzwingt jedoch nicht, dass mehrere In-App-Nachrichten gleichzeitig erscheinen. Wenn eine Nachricht sichtbar ist, wartet eine weitere getriggerte Nachricht im In-App-Nachrichten-Stack, bis eine Nachricht angezeigt werden kann.

Um dies zu überschreiben, aktualisieren Sie die Eigenschaft `triggerMinimumTimeInterval` in Ihrer Braze-Konfiguration, bevor die Braze-Instanz initialisiert wird. Sie kann auf jede nicht-negative Ganzzahl gesetzt werden und stellt das minimale Zeitintervall in Sekunden dar. Zum Beispiel:

{% tabs %}
{% tab swift %}

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
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Schlüssel-Wert-Paare {#key-value-pairs}

Wenn Sie eine Campaign in Braze erstellen, können Sie Schlüssel-Wert-Paare als `extras` festlegen, die das In-App-Messaging-Objekt verwenden kann, um Daten an Ihre App zu senden. Zum Beispiel:

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Eine vollständige Implementierung finden Sie in den Beispielen für die Anpassung von In-App-Nachrichten in unserer [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Deaktivieren von automatischen Triggern {#disabling-automatic-triggers}

So verhindern Sie, dass In-App-Nachrichten automatisch getriggert werden:

1. Implementieren Sie den Delegaten `BrazeInAppMessageUIDelegate` wie in unserem [iOS-Artikel hier](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui) beschrieben.
2. Aktualisieren Sie die Delegate-Methode `inAppMessage(_:displayChoiceForMessage:)`, um `.discard` zurückzugeben.

## Manuelles Triggern von Nachrichten {#manually-triggering-messages}

### Ein serverseitiges Event verwenden {#using-a-server-side-event}

Um In-App-Nachrichten über serverseitige Events zu triggern, senden Sie eine stille Push-Benachrichtigung an das Gerät, damit das Gerät ein SDK-basiertes Event protokollieren kann. Dieses SDK-Event kann anschließend die für Nutzer:innen sichtbare In-App-Nachricht triggern.

#### 1. Schritt: Stille Push-Benachrichtigungen und Schlüssel-Wert-Paare verarbeiten {#step-1-handle-silent-push-and-key-value-pairs}

Implementieren Sie die folgende Funktion und rufen Sie sie in der [Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) auf:

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Beim Empfang der stillen Push-Benachrichtigung wird ein vom SDK aufgezeichnetes Event des Typs „In-App-Nachrichten-Trigger“ im Nutzerprofil protokolliert.

{% alert important %}
Da eine Push-Nachricht verwendet wird, um ein vom SDK protokolliertes angepasstes Event aufzuzeichnen, muss Braze ein Push-Token für jede:n Nutzer:in speichern, um diese Lösung zu ermöglichen. Für iOS-Nutzer:innen speichert Braze ein Token erst ab dem Zeitpunkt, an dem ein:e Nutzer:in den Push-Prompt des Betriebssystems erhalten hat. Davor ist die Person nicht per Push erreichbar und die obige Lösung nicht möglich.
{% endalert %}

#### 2. Schritt: Eine stille Push-Campaign erstellen {#step-2-create-a-silent-push-campaign}

Erstellen Sie eine [Campaign mit einer stillen Push-Benachrichtigung]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift), die über das vom Server gesendete Event ausgelöst wird.

![Eine aktionsbasierte Zustellung einer In-App-Nachrichten-Campaign, die an Nutzer:innen zugestellt wird, deren Nutzerprofile das angepasste Event „server_event“ enthalten.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

Die Push-Campaign muss zusätzliche Schlüssel-Wert-Paare (Extras) enthalten, die angeben, dass diese Push-Campaign gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird verwendet, um die In-App-Nachricht zu triggern.

![Eine aktionsbasierte Zustellung einer In-App-Nachrichten-Campaign mit zwei Schlüssel-Wert-Paaren. „CAMPAIGN_NAME“ ist auf „Beispiel für den Namen der In-App-Nachricht“ und „IS_SERVER_EVENT“ auf „true“ gesetzt.]({% image_buster /assets/img_archive/iOSServerPush.png %})

Der Code in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` prüft auf den Schlüssel `IS_SERVER_EVENT` und protokolliert ein angepasstes SDK-Event, wenn dieser vorhanden ist.

Sie können entweder den Event-Namen oder die Event-Eigenschaften ändern, indem Sie den gewünschten Wert in den zusätzlichen Schlüssel-Wert-Paaren (Extras) der Push-Nutzlast senden. Bei der Protokollierung des angepassten Events können diese Extras entweder als Parameter des Event-Namens oder als Event-Eigenschaft verwendet werden.

#### 3. Schritt: In-App-Nachrichten-Campaign erstellen {#step-3-create-an-in-app-message-campaign}

Erstellen Sie im Braze-Dashboard eine für Ihre Nutzer:innen sichtbare In-App-Nachrichten-Campaign. Diese Campaign sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event getriggert werden, das in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft im Rahmen des ursprünglichen stillen Push gesendet wurde.

![Eine aktionsbasierte Zustellung einer In-App-Nachrichten-Campaign, die an Nutzer:innen zugestellt wird, die das angepasste Event „In-App message trigger“ ausführen, wobei „campaign_name“ gleich „IAM Campaign Name Example“ ist.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Beachten Sie, dass diese In-App-Nachrichten nur getriggert werden, wenn sich die Anwendung beim Empfang der stillen Push-Benachrichtigung im Vordergrund befindet.
{% endalert %}

### Anzeige einer vordefinierten Nachricht {#displaying-a-pre-defined}

Um eine vordefinierte In-App-Nachricht manuell anzuzeigen, verwenden Sie die folgende Methode:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Anzeige einer Nachricht in Realtime {#displaying-a-message-in-real-time}

Sie können lokale In-App-Nachrichten auch in Realtime anzeigen, indem Sie die Methode [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) manuell auf Ihrem `inAppMessagePresenter` aufrufen. Zum Beispiel:

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

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

{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie Ihre eigene In-App-Nachricht erstellen, verzichten Sie auf jegliches Analytics-Tracking und müssen die Protokollierung von Klicks und Impressionen manuell über Ihr `message.context` vornehmen.
{% endalert %}

## Der In-App-Nachrichten-Stack {#the-in-app-message-stack}

### Hinzufügen von In-App-Nachrichten zum Stack {#adding-in-app-messages-to-the-stack}

Nutzer:innen sind in den folgenden Situationen zum Empfang von In-App-Nachrichten berechtigt:

- Ein Trigger-Event für eine In-App-Nachricht wird ausgelöst
- Eine Sitzung wird gestartet
- Die App wird über eine Push-Benachrichtigung geöffnet

Wenn das Trigger-Event einer In-App-Nachricht ausgelöst wird, wird die Nachricht auf einem „Stack“ platziert. Wenn sich mehrere In-App-Nachrichten im Stack befinden und darauf warten, angezeigt zu werden, zeigt Braze die zuletzt empfangene In-App-Nachricht zuerst an (Last-in-first-out-Prinzip).

Wenn ein:e Nutzer:in zum Empfang einer In-App-Nachricht berechtigt ist, fordert `BrazeInAppMessagePresenter` die neueste In-App-Nachricht aus dem In-App-Nachrichten-Stack an. Der Stack hält nur gespeicherte In-App-Nachrichten im Arbeitsspeicher und wird zwischen App-Starts aus dem angehaltenen Modus geleert.

### Rückgabe von In-App-Nachrichten an den Stack {#returning-in-app-messages-to-the-stack}

Eine getriggerte In-App-Nachricht kann in den folgenden Situationen an den Stack zurückgegeben werden:

- Die In-App-Nachricht wird getriggert, wenn sich die App im Hintergrund befindet.
- Eine andere In-App-Nachricht ist derzeit sichtbar.
- Die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` hat `.reenqueue` zurückgegeben.

Die getriggerte In-App-Nachricht wird oben auf dem Stack platziert, damit sie später angezeigt werden kann, wenn ein:e Nutzer:in zum Empfang einer In-App-Nachricht berechtigt ist.

### Verwerfen von In-App-Nachrichten {#discarding-in-app-messages}

Eine getriggerte In-App-Nachricht wird in den folgenden Situationen verworfen:

- Die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` hat `.discard` zurückgegeben.
- Das Asset (Bild oder ZIP-Datei) der In-App-Nachricht konnte nicht heruntergeladen werden.
- Die In-App-Nachricht ist zur Anzeige bereit, hat aber das Timeout überschritten.
- Die Ausrichtung des Geräts stimmt nicht mit der Ausrichtung der getriggerten In-App-Nachricht überein.

Die In-App-Nachricht wird aus dem Stack entfernt. Nach dem Verwerfen kann die In-App-Nachricht zu einem späteren Zeitpunkt durch eine weitere Instanz des Trigger-Events erneut ausgelöst werden.