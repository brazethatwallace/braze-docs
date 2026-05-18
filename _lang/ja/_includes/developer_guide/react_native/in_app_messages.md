{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## メッセージタイプ {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## データモデル {#data-model}

アプリ内メッセージモデルはReact Native SDKで利用できます。Brazeには、同じデータモデルを共有する4つのアプリ内メッセージタイプ（**スライドアップ**、**モーダル**、**フル**、**HTMLフル**）があります。

### メッセージ {#messages}

アプリ内メッセージモデルは、すべてのアプリ内メッセージのベースを提供します。

| プロパティ | 説明 |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| `inAppMessageJsonString` | メッセージのJSON表現。 |
| `message` | メッセージテキスト。 |
| `header` | メッセージのヘッダー。 |
| `uri` | ボタンクリックアクションに関連付けられたURI。 |
| `imageUrl` | メッセージ画像のURL。 |
| `zippedAssetsUrl` | HTMLコンテンツを表示するために準備されたzip圧縮アセット。 |
| `useWebView` | ボタンクリックアクションがWebビューを使用してリダイレクトするかどうかを示します。 |
| `duration` | メッセージの表示時間。 |
| `clickAction` | ボタンクリックアクションのタイプ。タイプは`URI`および`NONE`です。 |
| `dismissType` | メッセージのクローズタイプ。2つのタイプは`SWIPE`および`AUTO_DISMISS`です。 |
| `messageType` | SDKがサポートするアプリ内メッセージタイプ。4つのタイプは`SLIDEUP`、`MODAL`、`FULL`および`HTML_FULL`です。 |
| `extras` | メッセージのエクストラ辞書。デフォルト値：`[:]`。 |
| `buttons` | アプリ内メッセージのボタン一覧。 |
| `toString()` | 文字列表現としてのメッセージ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messages" }

アプリ内メッセージモデルの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage)のドキュメントを参照してください。

### ボタン {#buttons}

アプリ内メッセージにボタンを追加して、アクションを実行したり、分析をログに記録したりできます。ボタンモデルは、すべてのアプリ内メッセージボタンのベースを提供します。

| プロパティ | 説明 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `text` | ボタンのテキスト。 |
| `uri` | ボタンクリックアクションに関連付けられたURI。 |
| `useWebView` | ボタンクリックアクションがWebビューを使用してリダイレクトするかどうかを示します。 |
| `clickAction` | ユーザーがボタンをクリックしたときに処理されるクリックアクションのタイプ。タイプは`URI`および`NONE`です。 |
| `id` | メッセージのボタンID。 |
| `toString()` | 文字列表現としてのボタン。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buttons" }

ボタンモデルの完全なリファレンスについては、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html)および[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button)のドキュメントを参照してください。