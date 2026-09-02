---
nav_title: In-App-Nachrichten-Zustellung
article_title: In-App-Nachrichten-Zustellung für iOS
platform: iOS
page_order: 3
description: "Dieser Referenzartikel behandelt die Zustellung von iOS-In-App-Nachrichten und listet verschiedene Trigger or triggern-Typen, Zustellungssemantiken und Schritte zur Event-Auslösung auf."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Zustellung von In-App-Nachrichten {#in-app-message-delivery}

## Trigger or triggern-Typen {#trigger-types}

Unser In-App-Nachricht-Produkt ermöglicht es Ihnen, die Anzeige von In-App-Nachrichten als Ergebnis verschiedener Event-Typen zu Trigger or triggern or triggern: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Darüber hinaus enthalten die Trigger or triggern `Specific Purchase` und `Custom Event` umfangreiche Eigenschaftsfilter.

{% alert note %}
Getriggerte In-App-Nachrichten funktionieren nur mit angepassten Events, die über das Braze SDK or Software-Development-Kit protokolliert werden. In-App-Nachrichten können nicht über die API oder durch API-Events (wie z. B. Kauf-Events) getriggert werden. Wenn Sie mit iOS arbeiten, besuchen Sie unseren Artikel zum [Tracking angepasster Events]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift), um mehr zu erfahren.
{% endalert %}

## Zustellungs-Semantik {#delivery-semantics}

Alle In-App-Nachrichten, für die ein:e Nutzer:in qualifiziert ist, werden beim Sitzungsstart an das Gerät der/des Nutzer:in zugestellt. Falls zwei In-App-Nachrichten durch ein Event getriggert werden, wird die In-App-Nachricht mit der höheren Priorität angezeigt. Weitere Informationen zur Sitzungsstart-Semantik des SDK or Software-Development-Kit finden Sie unter [Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/analytics/tracking_sessions#session-lifecycle). Bei der Zustellung ruft das SDK or Software-Development-Kit Assets vorab ab, damit sie zum Trigger or triggern-Zeitpunkt sofort verfügbar sind, um die Anzeigelatenz zu minimieren.

Wenn ein Trigger or triggern-Event mehr als eine qualifizierte In-App-Nachricht hat, wird nur die In-App-Nachricht mit der höchsten Priorität zugestellt.

Bei In-App-Nachrichten, die sofort bei der Zustellung angezeigt werden (Sitzungsstart, Push-Klick), kann es zu einer gewissen Latenz kommen, da Assets nicht vorab abgerufen wurden.

## Minimales Zeitintervall zwischen Trigger or triggern or triggern {#minimum-time-interval-between-triggers}

Standardmäßig werden In-App-Nachrichten auf einmal alle 30 Sekunden begrenzt, um ein hochwertiges Nutzungserlebnis zu ermöglichen.

Sie können diesen Wert über den `ABKMinimumTriggerTimeIntervalKey` innerhalb des `appboyOptions`-Parameters überschreiben, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Setzen Sie den `ABKMinimumTriggerTimeIntervalKey` auf den ganzzahligen Wert, den Sie als minimale Zeit in Sekunden zwischen In-App-Nachrichten verwenden möchten:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Kein passender Trigger or triggern gefunden {#failing-to-find-a-matching-trigger}

Wenn Braze keinen passenden Trigger or triggern für ein bestimmtes Event findet, wird die Methode [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) des [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html) aufgerufen. Implementieren Sie diese Methode in Ihrer Klasse, die das Delegate-Protokoll übernimmt, um dieses Szenario zu behandeln.

## Lokale Zustellung von In-App-Nachrichten {#local-in-app-message-delivery}

### Der In-App-Nachrichten-Stack {#the-in-app-message-stack}

#### In-App-Nachrichten anzeigen {#showing-in-app-messages}

Wenn Nutzer:innen berechtigt sind, eine In-App-Nachricht zu erhalten, wird dem `ABKInAppMessageController` die neueste In-App-Nachricht vom In-App-Nachrichten-Stack angeboten. Der Stack speichert In-App-Nachrichten nur im Arbeitsspeicher und wird zwischen App-Starts aus dem Ruhezustand geleert.

{% alert important %}
Zeigen Sie keine In-App-Nachrichten an, während die Tastatur auf dem Bildschirm angezeigt wird, da das Rendering in diesem Fall nicht definiert ist.
{% endalert %}

#### In-App-Nachrichten zum Stack hinzufügen {#adding-in-app-messages-to-the-stack}

Nutzer:innen sind in den folgenden Situationen berechtigt, eine In-App-Nachricht zu erhalten:

- Ein Trigger or triggern-Event für In-App-Nachrichten wird ausgelöst
- Sitzungsstart-Event
- Die App wird über eine Push-Benachrichtigung geöffnet

Getriggerte In-App-Nachrichten werden auf den Stack gelegt, wenn ihr Trigger or triggern-Event ausgelöst wird. Wenn sich mehrere In-App-Nachrichten im Stack befinden und darauf warten, angezeigt zu werden, zeigt Braze die zuletzt empfangene In-App-Nachricht zuerst an (Last-in, First-out).

#### In-App-Nachrichten zum Stack zurückgeben {#returning-in-app-messages-to-the-stack}

Eine getriggerte In-App-Nachricht kann in den folgenden Situationen zum Stack zurückgegeben werden:

- Die In-App-Nachricht wird getriggert, während die App im Hintergrund ist.
- Eine andere In-App-Nachricht wird gerade angezeigt.
- Die veraltete `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) wurde nicht implementiert und die Tastatur wird gerade angezeigt.
- Die `beforeInAppMessageDisplayed:` [Delegate-Methode]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) oder die veraltete `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) hat `ABKDisplayInAppMessageLater` zurückgegeben.

#### In-App-Nachrichten verwerfen {#discarding-in-app-messages}

Eine getriggerte In-App-Nachricht wird in den folgenden Situationen verworfen:

- Die `beforeInAppMessageDisplayed:` [Delegate-Methode]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) oder die veraltete `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) hat `ABKDiscardInAppMessage` zurückgegeben.
- Das Asset (Bild oder ZIP-Datei) der In-App-Nachricht konnte nicht heruntergeladen werden.
- Die In-App-Nachricht ist bereit zur Anzeige, hat aber die Timeout-Dauer überschritten.
- Die Geräteausrichtung stimmt nicht mit der Ausrichtung der getriggerten In-App-Nachricht überein.
- Die In-App-Nachricht ist eine Vollbild-In-App-Nachricht, enthält aber kein Bild.
- Die In-App-Nachricht ist eine reine Bild-Modal-In-App-Nachricht, enthält aber kein Bild.

#### Anzeige von In-App-Nachrichten manuell in die Warteschlange stellen {#manually-queue-in-app-message-display}

Wenn Sie eine In-App-Nachricht zu einem anderen Zeitpunkt in Ihrer App anzeigen möchten, können Sie die oberste In-App-Nachricht im Stack manuell anzeigen, indem Sie die folgende Methode aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Realtime-Erstellung und -Anzeige von In-App-Nachrichten {#real-time-in-app-message-creation-and-display}

In-App-Nachrichten können auch lokal innerhalb der App erstellt und über Braze angezeigt werden. Dies ist besonders nützlich, um Nachrichten anzuzeigen, die Sie in Realtime innerhalb der App Trigger or triggern or triggern möchten. Braze unterstützt keine Analytics für lokal erstellte In-App-Nachrichten.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}