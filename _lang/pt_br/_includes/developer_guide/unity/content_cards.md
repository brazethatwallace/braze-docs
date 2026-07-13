{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Exibição nativa de Content Cards {#unity-content-cards-native-ui}

Você pode exibir a interface padrão para os Content Cards usando a seguinte chamada:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Recebimento de dados de Content Cards no Unity {#receiving-content-card-data-in-unity}

Você pode registrar objetos de jogo Unity para serem notificados sobre Content Cards recebidos. Recomendamos configurar os ouvintes de objetos de jogo no editor de configuração da Braze.

Se você precisar configurar o ouvinte do objeto de jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Note que, além disso, será necessário fazer uma chamada para `AppboyBinding.RequestContentCardsRefresh()` para começar a receber dados no ouvinte do objeto de jogo no iOS.

## Parsing de Content Cards {#parsing-content-cards}

As mensagens `string` recebidas no retorno de chamada do objeto de jogo de Content Cards podem ser convertidas no objeto modelo [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) por conveniência.

O parsing de Content Cards requer parsing de JSON. Consulte o exemplo a seguir para mais detalhes:

### Exemplo de retorno de chamada de Content Cards {#example-content-cards-callback}

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

## Atualizando Content Cards {#refreshing-content-cards}

Para atualizar os Content Cards da Braze, use um dos métodos a seguir:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Análise de dados {#analytics}

Os cliques e as impressões devem ser registrados manualmente para Content Cards não exibidos diretamente pela Braze.

Use `LogClick()` e `LogImpression()` no [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) para registrar cliques e impressões de cartões específicos.