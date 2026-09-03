---
nav_title: Nachrichten anpassen
article_title: "In-App-Nachrichten anpassen"
page_order: 0.1
description: "Erfahren Sie, wie Sie In-App-Nachrichten für das Braze SDK einrichten können."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# In-App-Nachrichten anpassen {#customize-in-app-messages}

> Erfahren Sie, wie Sie In-App-Nachrichten für das Braze SDK anpassen können. Für fortgeschrittene Styling-Techniken empfehlen wir Ihnen unser Tutorial zur [Anpassung des Nachrichtenstylings mithilfe von Schlüssel-Wert-Paaren]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling).

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/customization.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/customization.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/customization.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/analytics/logging_iam_data.md %}
{% endsdktab %}

{% sdktab unity %}
## Anpassen des Anzeigeverhaltens {#customizing-the-display-behavior}

Sie können das Anzeigeverhalten von In-App-Nachrichten zur Laufzeit wie folgt ändern:

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Einen angepassten Listener einrichten {#setting-a-custom-listener}

Wenn Sie mehr Kontrolle darüber benötigen, wie Nutzer:innen mit In-App-Nachrichten interagieren, verwenden Sie einen `BrazeInAppMessageListener` und weisen Sie ihn `Appboy.AppboyBinding.inAppMessageListener` zu. Für Delegates, die Sie nicht verwenden möchten, können Sie diese einfach auf `null` setzen.

```csharp
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
  BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed,
  OnInAppMessageButtonClicked = OnInAppMessageButtonClicked,
  OnInAppMessageClicked       = OnInAppMessageClicked,
  OnInAppMessageHTMLClicked   = OnInAppMessageHTMLClicked,
  OnInAppMessageDismissed     = OnInAppMessageDismissed,
};
Appboy.AppboyBinding.inAppMessageListener = listener;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Executed before an in-app message is displayed.
}

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
  // Executed whenever an in-app message button is clicked.
}

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is clicked.
}

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
  // Executed whenever an HTML in-app message is clicked.
}

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is dismissed without a click.
}
```

{% endsdktab %}
{% endsdktabs %}