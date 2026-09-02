---
nav_title: Personalizar mensajes
article_title: "Personalizar mensajes dentro de la aplicación"
page_order: 0.1
description: "Aprende a configurar mensajes dentro de la aplicación para el SDK or kit de desarrollo de software de Braze."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalizar mensajes dentro de la aplicación {#customize-in-app-messages}

> Aprende a personalizar los mensajes dentro de la aplicación para el SDK or kit de desarrollo de software de Braze. Para conocer técnicas de estilo avanzadas, consulta nuestro tutorial sobre cómo [personalizar el estilo de los mensajes mediante pares clave-valor]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling).

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

{% sdktab React Native %}
{% multi_lang_include developer_guide/react_native/analytics/logging_iam_data.md %}
{% endsdktab %}

{% sdktab unity %}
## Personalizar el comportamiento de visualización {#customizing-the-display-behavior}

Puedes cambiar el comportamiento de visualización de los mensajes dentro de la aplicación en tiempo de ejecución mediante lo siguiente:

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Configurar un listener personalizado {#setting-a-custom-listener}

Si necesitas más control sobre cómo interactúa un usuario con los mensajes dentro de la aplicación, utiliza un `BrazeInAppMessageListener` y asígnalo a `Appboy.AppboyBinding.inAppMessageListener`. Para cualquier delegado que no quieras utilizar, simplemente puedes dejarlo como `null`.

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