{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Content Cardsをネイティブに表示する {#unity-content-cards-native-ui}

次の呼び出しを使用して、Content CardsのデフォルトUIを表示できます。

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## UnityでContent Cardsデータを受信する {#receiving-content-card-data-in-unity}

Unityゲームオブジェクトを登録して、受信するContent Cardsの通知を受け取ることができます。Brazeコンフィギュレーションエディタからゲームオブジェクトリスナーを設定することをお勧めします。

ゲームオブジェクトリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()`を使用し、`BrazeUnityMessageType.CONTENT_CARDS_UPDATED`を指定します。

なお、iOSではゲームオブジェクトリスナーでデータの受信を開始するために、`AppboyBinding.RequestContentCardsRefresh()`の呼び出しも必要です。

## Content Cardsの解析 {#parsing-content-cards}

Content Cardsゲームオブジェクトコールバックで受信した`string`メッセージは、あらかじめ用意されている[`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs)モデルオブジェクトに解析すると便利です。

Content Cardsの解析にはJSON解析が必要です。詳細は以下の例を参照してください。

### Content Cardsコールバックの例 {#example-content-cards-callback}

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

## Content Cardsの更新 {#refreshing-content-cards}

BrazeからContent Cardsを更新するには、次のいずれかのメソッドを呼び出します。

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## 分析 {#analytics}

Brazeによって直接表示されないContent Cardsについては、クリックとインプレッションを手動でログに記録する必要があります。

[ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs)の`LogClick()`および`LogImpression()`を使用して、特定のカードのクリックとインプレッションを記録します。