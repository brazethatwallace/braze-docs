{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Mostrar Content Cards de forma nativa {#unity-content-cards-native-ui}

Puedes mostrar la interfaz predeterminada para Content Cards utilizando la siguiente llamada:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Recibir datos de Content Cards en Unity {#receiving-content-card-data-in-unity}

Puedes registrar objetos del juego de Unity para que se les notifique la llegada de Content Cards. Recomendamos configurar los oyentes del objeto del juego desde el editor de configuración de Braze.

Si necesitas configurar el oyente de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Ten en cuenta que, además, tendrás que hacer una llamada a `AppboyBinding.RequestContentCardsRefresh()` para empezar a recibir datos en el oyente de tu objeto del juego en iOS.

## Análisis sintáctico de Content Cards {#parsing-content-cards}

Los mensajes entrantes de `string` recibidos en la devolución de llamada de tu objeto del juego de Content Cards pueden analizarse en nuestro objeto de modelo [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) presuministrado para mayor comodidad.

El análisis de Content Cards requiere análisis JSON; consulta el siguiente ejemplo para obtener más detalles:

### Ejemplo de devolución de llamada de Content Cards {#example-content-cards-callback}

```csharp
void ExampleCallback(string message) {
  try {
    JSONClass json = (JSONClass)JSON.Parse(message);

    // Content Card data is contained in the `mContentCards` field of the top level object.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String.Format("Parsed content cards array with {0} cards", jsonArray.Count));

      // Iterate over the card array to parse individual cards.
      for (int i = 0; i < jsonArray.Count; i++) {
        JSONClass cardJson = jsonArray[i].AsObject;
        try {
          ContentCard card = new ContentCard(cardJson);
          Debug.Log(String.Format("Created card object for card: {0}", card));

          // Example of logging Content Card analytics on the ContentCard object
          card.LogImpression();
          card.LogClick();
        } catch {
          Debug.Log(String.Format("Unable to create and log analytics for card {0}", cardJson));
        }
      }
    }
  } catch {
    throw new ArgumentException("Could not parse content card JSON message.");
  }
}
```

## Actualizar Content Cards {#refreshing-content-cards}

Para actualizar Content Cards desde Braze, llama a cualquiera de los siguientes métodos:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Análisis {#analytics}

Los clics y las impresiones deben registrarse manualmente para las Content Cards que no se muestran directamente a través de Braze.

Utiliza `LogClick()` y `LogImpression()` en [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) para registrar los clics y las impresiones de tarjetas concretas.