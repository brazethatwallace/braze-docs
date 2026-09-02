---
nav_title: Angepasstes Triggern
article_title: Anpassen der Auslösung von In-App-Nachrichten für iOS
platform: iOS
page_order: 7
description: "Dieser Referenzartikel behandelt das angepasste Triggern von In-App-Nachrichten für Ihre iOS-Anwendung."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasstes Triggern von In-App-Nachrichten {#custom-in-app-message-triggering}

Standardmäßig werden In-App-Nachrichten durch Event-Typen ausgelöst, die vom SDK protokolliert werden. Sie können In-App-Nachrichten jedoch auch durch vom Server gesendete Events auslösen.

Um dieses Feature zu aktivieren, senden Sie eine stille Push-Benachrichtigung an das Gerät. Sie ermöglicht es dem Gerät, ein SDK-basiertes Event zu protokollieren. Dieses SDK-Event würde dann die für Nutzer:innen sichtbare In-App-Nachricht auslösen.

## 1. Schritt: Stille Push-Benachrichtigungen und Schlüssel-Wert-Paare verarbeiten {#step-1-handle-silent-push-and-key-value-pairs}

Fügen Sie den folgenden Code in die Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` ein:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Beim Empfang einer stillen Push-Benachrichtigung wird ein vom SDK aufgezeichnetes Event des Typs „In-App-Nachrichten-Trigger“ im Kundenprofil protokolliert. Beachten Sie, dass diese In-App-Nachrichten nur ausgelöst werden, wenn sich die Anwendung beim Empfang der stillen Push-Benachrichtigung im Vordergrund befindet.

## 2. Schritt: Eine Push-Kampagne erstellen {#step-2-create-a-push-campaign}

Erstellen Sie eine Kampagne mit einem stillen Push, die über das vom Server gesendete Event ausgelöst wird. Einzelheiten zur Erstellung einer stillen Push-Kampagne finden Sie unter [Stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

![Eine aktionsbasierte Zustellung einer In-App-Nachrichten-Kampagne, die an Nutzer:innen zugestellt wird, die das angepasste Event „server_event“ ausführen.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

Die Push-Kampagne muss zusätzliche Schlüssel-Wert-Paare (Extras) enthalten, die angeben, dass diese Push-Kampagne gesendet wird, um ein angepasstes SDK-Event zu protokollieren. Dieses Event wird zum Triggern der In-App-Nachricht verwendet:

![Eine aktionsbasierte Zustellung einer In-App-Nachrichten-Kampagne mit zwei Schlüssel-Wert-Paaren. „CAMPAIGN_NAME“ ist auf „Beispiel für den Namen der In-App-Nachricht“ gesetzt und „IS_SERVER_EVENT“ ist auf „true“ gesetzt.]({% image_buster /assets/img_archive/iOSServerPush.png %})

Der Code in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` prüft auf den Schlüssel `IS_SERVER_EVENT` und protokolliert ein angepasstes SDK-Event, wenn dieser vorhanden ist.

Sie können entweder den Event-Namen oder die Event-Eigenschaften ändern, indem Sie den gewünschten Wert in den zusätzlichen Schlüssel-Wert-Paaren (Extras) der Push-Nutzlast senden. Bei der Protokollierung des angepassten Events können diese Extras entweder als Parameter des Event-Namens oder als Event-Eigenschaft verwendet werden.

## 3. Schritt: Eine In-App-Nachrichten-Kampagne erstellen {#step-3-create-an-in-app-message-campaign}

Erstellen Sie Ihre für Nutzer:innen sichtbare In-App-Nachrichten-Kampagne über das Braze-Dashboard. Diese Kampagne sollte eine aktionsbasierte Zustellung haben und durch das angepasste Event ausgelöst werden, das in der Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` protokolliert wird.

Im folgenden Beispiel wurde die zu triggernde In-App-Nachricht konfiguriert, indem die Event-Eigenschaft im Rahmen des ursprünglichen stillen Push gesendet wurde.

![Eine aktionsbasierte Zustellung einer In-App-Nachrichten-Kampagne, die an Nutzer:innen zugestellt wird, die das angepasste Event „In-App-Nachrichten-Trigger“ ausführen, wobei „campaign_name“ gleich „Beispiel für den Namen der In-App-Nachricht“ ist.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

Da eine Push-Nachricht verwendet wird, um ein vom SDK protokolliertes angepasstes Event aufzuzeichnen, muss Braze ein Push-Token / Textbaustein für jede:n Nutzer:in speichern, um diese Lösung zu ermöglichen. Sowohl für iOS als auch für Android speichert Braze ein Token / Textbaustein erst ab dem Zeitpunkt, an dem Nutzer:innen die Push-Aufforderung des Betriebssystems erhalten haben. Davor sind Nutzer:innen nicht per Push erreichbar und die obige Lösung ist nicht möglich.