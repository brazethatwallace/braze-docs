---
nav_title: In-App-Nachrichten-Zustellung
article_title: In-App-Nachrichten-Zustellung für iOS
platform: iOS
page_order: 3
description: "Dieser Referenzartikel behandelt die Zustellung von iOS-In-App-Nachrichten und listet verschiedene Trigger-Typen, Zustellungssemantiken und Schritte zur Event-Auslösung auf."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Zustellung von In-App-Nachrichten {#in-app-message-delivery}

## Trigger-Typen {#trigger-types}

Mit unserem Produkt für In-App-Nachrichten können Sie die Anzeige von In-App-Nachrichten infolge verschiedener Event-Typen auslösen: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Darüber hinaus enthalten die Trigger `Specific Purchase` und `Custom Event` robuste Eigenschaftsfilter.

{% alert note %}
Getriggerte In-App-Nachrichten funktionieren nur mit angepassten Events, die über das Braze SDK protokolliert werden. In-App-Nachrichten können nicht über die API oder durch API-Events (wie Kauf-Events) getriggert werden. Wenn Sie mit iOS arbeiten, lesen Sie unseren Artikel zum [Tracking angepasster Events]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift), um mehr zu erfahren.
{% endalert %}

## Zustellungssemantik {#delivery-semantics}

Alle In-App-Nachrichten, für die Nutzer:innen berechtigt sind, werden zu Beginn der Sitzung an das Gerät gesendet. Wenn durch ein Event zwei In-App-Nachrichten ausgelöst werden, wird die In-App-Nachricht mit der höheren Priorität angezeigt. Weitere Informationen zur Sitzungsstart-Semantik des SDK finden Sie unter [Lebenszyklus einer Sitzung]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions#session-lifecycle). Bei der Zustellung ruft das SDK die Assets per Prefetching ab, damit sie zum Trigger-Zeitpunkt sofort verfügbar sind und die Anzeigelatenz minimiert wird.

Wenn ein Trigger-Event mit mehr als einer in Frage kommenden In-App-Nachricht verknüpft ist, wird nur die In-App-Nachricht mit der höchsten Priorität zugestellt.

Bei In-App-Nachrichten, die sofort nach der Zustellung angezeigt werden (Sitzungsstart, Push-Klick), kann es zu einer gewissen Latenz kommen, da die Assets nicht per Prefetching abgerufen werden.

## Mindestzeitintervall zwischen Triggern {#minimum-time-interval-between-triggers}

Standardmäßig begrenzen wir In-App-Nachrichten auf einmal alle 30 Sekunden, um ein hochwertiges Nutzungserlebnis zu gewährleisten.

Sie können diesen Wert über `ABKMinimumTriggerTimeIntervalKey` im Parameter `appboyOptions` überschreiben, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Setzen Sie `ABKMinimumTriggerTimeIntervalKey` auf den ganzzahligen Wert, den Sie als Mindestzeit in Sekunden zwischen In-App-Nachrichten verwenden möchten:

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

## Wenn kein passender Trigger gefunden wird {#failing-to-find-a-matching-trigger}

Wenn Braze keinen passenden Trigger für ein bestimmtes Event findet, wird die Methode [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) von [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html) aufgerufen. Implementieren Sie diese Methode in Ihrer Klasse, die das Delegate-Protokoll übernimmt, um dieses Szenario zu behandeln.

## Lokale Zustellung von In-App-Nachrichten {#local-in-app-message-delivery}

### Der In-App-Nachrichten-Stack {#the-in-app-message-stack}

#### Anzeigen von In-App-Nachrichten {#showing-in-app-messages}

Wenn Nutzer:innen zum Empfang einer In-App-Nachricht berechtigt sind, wird dem `ABKInAppMessageController` die neueste In-App-Nachricht aus dem In-App-Nachrichten-Stack angeboten. Der Stack hält nur gespeicherte In-App-Nachrichten im Arbeitsspeicher und wird zwischen App-Starts aus dem angehaltenen Modus geleert.

{% alert important %}
Zeigen Sie keine In-App-Nachrichten an, wenn die Tastatur auf dem Bildschirm angezeigt wird, da die Darstellung in diesem Fall undefiniert ist.
{% endalert %}

#### Hinzufügen von In-App-Nachrichten zum Stack {#adding-in-app-messages-to-the-stack}

Nutzer:innen sind in den folgenden Situationen zum Empfang einer In-App-Nachricht berechtigt:

- Ein Trigger-Event für eine In-App-Nachricht wird ausgelöst
- Sitzungsstart-Event
- Die App wird über eine Push-Benachrichtigung geöffnet

Getriggerte In-App-Nachrichten werden auf den Stack gelegt, wenn ihr Trigger-Event ausgelöst wird. Wenn sich mehrere In-App-Nachrichten im Stack befinden und darauf warten, angezeigt zu werden, zeigt Braze die zuletzt empfangene In-App-Nachricht zuerst an (Last-in-first-out-Prinzip).

#### Rückgabe von In-App-Nachrichten an den Stack {#returning-in-app-messages-to-the-stack}

Eine getriggerte In-App-Nachricht kann in den folgenden Situationen an den Stack zurückgegeben werden:

- Die In-App-Nachricht wird ausgelöst, wenn sich die App im Hintergrund befindet.
- Eine andere In-App-Nachricht ist derzeit sichtbar.
- Die veraltete [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` wurde nicht implementiert und die Tastatur wird derzeit angezeigt.
- Die [Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` oder die veraltete [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` hat `ABKDisplayInAppMessageLater` zurückgegeben.

#### Verwerfen von In-App-Nachrichten {#discarding-in-app-messages}

Eine getriggerte In-App-Nachricht wird in den folgenden Situationen verworfen:

- Die [Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` oder die veraltete [UI-Delegate-Methode]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) `beforeInAppMessageDisplayed:withKeyboardIsUp:` hat `ABKDiscardInAppMessage` zurückgegeben.
- Das Asset (Bild oder ZIP-Datei) der In-App-Nachricht konnte nicht heruntergeladen werden.
- Die In-App-Nachricht ist zur Anzeige bereit, hat aber die Timeout-Dauer überschritten.
- Die Geräteausrichtung stimmt nicht mit der Ausrichtung der getriggerten In-App-Nachricht überein.
- Die In-App-Nachricht ist eine Vollbild-In-App-Nachricht, enthält aber kein Bild.
- Die In-App-Nachricht ist eine modale In-App-Nachricht, die nur ein Bild enthält, aber kein Bild vorhanden ist.

#### Manuelles Einreihen von In-App-Nachrichten in die Anzeigewarteschlange {#manually-queue-in-app-message-display}

Wenn Sie eine In-App-Nachricht zu anderen Zeitpunkten in Ihrer App anzeigen möchten, können Sie die oberste In-App-Nachricht auf dem Stack manuell anzeigen, indem Sie die folgende Methode aufrufen:

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

### Erstellung und Anzeige von In-App-Nachrichten in Realtime {#real-time-in-app-message-creation-and-display}

In-App-Nachrichten können auch lokal in der App erstellt und über Braze angezeigt werden. Dies ist besonders nützlich für die Anzeige von Nachrichten, die Sie in Realtime in der App auslösen möchten. Braze unterstützt keine Analytics für lokal erstellte In-App-Nachrichten.

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