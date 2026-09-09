---
nav_title: Personnaliser les messages
article_title: "Personnaliser les messages in-app"
page_order: 0.1
description: "Découvrez comment configurer les messages in-app pour le SDK de Braze."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personnaliser les messages in-app {#customize-in-app-messages}

> Découvrez comment personnaliser les messages in-app pour le SDK de Braze. Pour découvrir des techniques de mise en forme avancées, consultez notre tutoriel sur [la personnalisation de la mise en forme des messages à l'aide de paires clé-valeur]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling).

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
## Personnaliser le comportement d'affichage {#customizing-the-display-behavior}

Vous pouvez modifier le comportement d'affichage des messages in-app au moment de l'exécution via les méthodes suivantes :

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Définir un listener personnalisé {#setting-a-custom-listener}

Si vous avez besoin de plus de contrôle sur la façon dont un utilisateur interagit avec les messages in-app, utilisez un `BrazeInAppMessageListener` et assignez-le à `Appboy.AppboyBinding.inAppMessageListener`. Pour les délégués que vous ne souhaitez pas utiliser, vous pouvez simplement les laisser à `null`.

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