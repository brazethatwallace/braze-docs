{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## カードフィード {#card-feeds}

Braze SDKにはデフォルトのカードフィードが含まれています。デフォルトのカードフィードを表示するには、`launchContentCards()` メソッドを使用します。このメソッドは、ユーザーのContent Cardsの分析トラッキング、非表示、レンダリングをすべて処理します。

## Content Cards

以下の追加メソッドを使用して、アプリ内にカスタムContent Cardsフィードを構築できます。

| 方法 | 説明 |
|---|---|
| `requestContentCardsRefresh()` | Braze SDKサーバーから最新のContent Cardsをリクエストするバックグラウンドリクエストを送信します。 |
| `getContentCardsFromServer(successCallback, errorCallback)` | Braze SDKからContent Cardsを取得します。サーバーから最新のContent Cardsをリクエストし、完了時にカードのリストを返します。 |
| `getContentCardsFromCache(successCallback, errorCallback)` | Braze SDKからContent Cardsを取得します。前回の更新時に更新されたローカルキャッシュから最新のカードリストを返します。 |
| `logContentCardClicked(cardId)` | 指定されたコンテンツカードIDのクリックを記録します。 |
| `logContentCardImpression(cardId)` | 指定されたコンテンツカードIDのインプレッションを記録します。 |
| `logContentCardDismissed(cardId)` | 指定されたコンテンツカードIDの非表示を記録します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cards" }