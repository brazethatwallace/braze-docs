## Acerca de las tarjetas de contenido de Flutter {#about-flutter-content-cards}

El SDK de Braze incluye una fuente de tarjetas predeterminada para que empieces a utilizar las Content Cards. Para mostrar la fuente de tarjetas, puedes utilizar el método `braze.launchContentCards()`. La fuente predeterminada de tarjetas incluida en el SDK de Braze gestionará todo el seguimiento de análisis, los descartes y la representación de las Content Cards de un usuario.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Métodos de tarjeta {#card-methods}

Puedes utilizar estos métodos adicionales para crear una fuente de Content Cards personalizada dentro de tu aplicación, usando los siguientes métodos disponibles en la [interfaz pública del complemento](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Método                                         | Descripción                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Solicita las últimas Content Cards al servidor del SDK de Braze.                                           |
| `braze.logContentCardClicked(contentCard)`    | Registra un clic para el objeto de tarjeta de contenido dado.                                                            |
| `braze.logContentCardImpression(contentCard)` | Registra una impresión para el objeto de tarjeta de contenido dado.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Registra un descarte para el objeto de tarjeta de contenido dado.                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de tarjeta" }

## Recepción de datos de Content Cards {#receiving-content-card-data}

Para recibir datos de Content Cards en tu aplicación Flutter, `BrazePlugin` admite el envío de datos de Content Cards mediante [Dart Streams](https://dart.dev/tutorials/language/streams).

El [objeto](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) `BrazeContentCard` admite un subconjunto de campos disponibles en los objetos del modelo nativo, como `description`, `title`, `image`, `url`, `extras`, etc.

### Escuchar datos de Content Cards en la capa Dart {#listen-for-content-card-data-in-the-dart-layer}

Para recibir los datos de Content Cards en la capa Dart, utiliza el código siguiente para crear un `StreamSubscription` y llamar a `braze.subscribeToContentCards()`. Recuerda llamar a `cancel()` en la suscripción al stream cuando ya no la necesites.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

Para ver un ejemplo, consulta [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) en la aplicación de ejemplo del SDK de Braze para Flutter.

### Transmitir datos de Content Cards desde la capa nativa de iOS {#forward-content-card-data-from-the-native-ios-layer}

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Los datos de Content Cards se transmiten automáticamente desde las capas nativas de Android e iOS. No se requiere configuración adicional.

{% endtab %}
{% tab Flutter SDK 17.1.0 y anteriores %}

Si estás utilizando Flutter SDK 17.1.0 o anterior, la transmisión de datos de Content Cards desde la capa nativa de iOS requiere configuración manual. Es probable que tu aplicación contenga una devolución de llamada `contentCards.subscribeToUpdates` que llame a `BrazePlugin.processContentCards(contentCards)`. Para migrar a Flutter SDK 18.0.0, elimina la llamada a `BrazePlugin.processContentCards(_:)`: la transmisión de datos ahora se gestiona automáticamente.

Para ver un ejemplo, consulta [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) en la aplicación de ejemplo del SDK de Braze para Flutter.

{% endtab %}
{% endtabs %}

#### Repetición de la devolución de llamada para Content Cards {#replaying-the-callback-for-content-cards}

Para almacenar las Content Cards desencadenadas antes de que la devolución de llamada esté disponible y reproducirlas una vez establecida, añade la siguiente entrada al mapa `customConfigs` al inicializar `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```
