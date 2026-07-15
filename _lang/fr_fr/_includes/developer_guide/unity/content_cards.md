{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Affichage natif des Content Cards {#unity-content-cards-native-ui}

Vous pouvez afficher l'interface utilisateur par défaut pour les Content Cards à l'aide de l'appel suivant :

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Réception des données de Content Cards dans Unity {#receiving-content-card-data-in-unity}

Vous pouvez enregistrer des objets de jeu Unity pour être notifié de l'arrivée de Content Cards. Nous recommandons de définir des écouteurs d'objets de jeu à partir de l'éditeur de configuration Braze.

Si vous devez configurer votre écouteur d'objet de jeu lors de l'exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Notez que vous devrez également appeler `AppboyBinding.RequestContentCardsRefresh()` pour commencer à recevoir des données dans votre écouteur d'objet de jeu sur iOS.

## Analyse des Content Cards {#parsing-content-cards}

Les messages de type `string` entrants reçus dans le rappel de votre objet de jeu Content Cards peuvent être analysés à l'aide de notre objet de modèle [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) pré-fourni pour plus de commodité.

L'analyse des Content Cards nécessite une analyse JSON. Consultez l'exemple suivant pour plus de détails :

### Exemple de rappel de Content Cards {#example-content-cards-callback}

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

## Actualiser les Content Cards {#refreshing-content-cards}

Pour actualiser les Content Cards depuis Braze, appelez l'une des méthodes suivantes :

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Analytique {#analytics}

Les clics et les impressions doivent être enregistrés manuellement pour les Content Cards non affichées directement par Braze.

Utilisez `LogClick()` et `LogImpression()` sur [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) pour enregistrer les clics et les impressions pour des cartes spécifiques.