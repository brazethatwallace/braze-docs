{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Native Anzeige von Content Cards {#unity-content-cards-native-ui}

Mit dem folgenden Aufruf können Sie die Standard-UI für Content Cards anzeigen:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Empfangen von Content-Card-Daten in Unity {#receiving-content-card-data-in-unity}

Sie können Unity-Spielobjekte Registrierung, um über eingehende Content Cards benachrichtigt zu werden. Wir empfehlen, Spielobjekt-Listener über den Braze-Konfigurationseditor einzustellen.

Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.CONTENT_CARDS_UPDATED` an.

Beachten Sie, dass zusätzlich ein Aufruf an `AppboyBinding.RequestContentCardsRefresh()` erforderlich ist, um unter iOS Daten in Ihrem Spielobjekt-Listener zu empfangen.

## Parsen von Content Cards {#parsing-content-cards}

Eingehende Nachrichten des Typs `string`, die im Spielobjekt-Callback Ihrer Content Cards empfangen werden, können in unser vorgefertigtes Modellobjekt [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) geparst werden.

Das Parsen von Content Cards erfordert JSON-Parsing. Weitere Details finden Sie im folgenden Beispiel:

### Beispiel für einen Content-Card-Callback {#example-content-cards-callback}

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

## Aktualisieren von Content Cards {#refreshing-content-cards}

Um Content Cards von Braze zu aktualisieren, rufen Sie eine der folgenden Methoden auf:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Analytics

Klicks und Impressionen müssen für Content Cards, die nicht direkt von Braze angezeigt werden, manuell protokolliert werden.

Verwenden Sie `LogClick()` und `LogImpression()` auf [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs), um Klicks und Impressionen für bestimmte Karten zu protokollieren.