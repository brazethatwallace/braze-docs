---
nav_title: Google tag manager
article_title: Google Tag Manager with the Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Learn how to initialize the Braze SDK using methods like runtime initialization, delayed initialization, or Google Tag Manager."

---
## Google Tag Manager for Webについて {#google-tag-manager}

Google Tag Manager（GTM）を使えば、プロダクションコードのリリースやエンジニアリングリソースを必要とせずに、Webサイトのタグをリモートで追加、削除、編集できます。BrazeはWeb SDK用に以下のテンプレートを提供しています。

| タグの種類 | ユースケース |
|--------|--------|
| 初期化タグ | このタグにより、サイトのコードを変更することなく、[Web Braze SDKを統合する]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web)ことができます。|
| アクションタグ | このタグで[Content Cardsの作成]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager)、[ユーザー属性の設定]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web)、[データ収集の管理]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web)ができます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Google Tag Manager for Webについて" }

## Brazeアクションタグのタグシーケンス {#tag-sequencing-for-braze-action-tags}

Braze初期化タグは、Braze SDKメソッド（`braze.getUser()`、`braze.logCustomEvent()`、`braze.logPurchase()`など）を呼び出すすべてのタグよりも先に発火する必要があります。SDKが初期化される前にこれらのメソッドが発火すると、`Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')` のようなエラーが発生する可能性があります。

Google Tag Managerでタグシーケンスを設定するには：

1. Braze SDKメソッドを呼び出すタグ（Custom HTMLタグやBrazeアクションタグなど）を開きます。
2. **Advanced Settings** > **Tag Sequencing**に移動します。
3. **A tag that fires before [this tag] is fired**を選択します。
4. **Braze Initialization**タグを選択します。

これにより、他のタグがBrazeメソッドを呼び出す前に、SDKが完全に読み込まれます。

詳細については、[カスタムイベントのタグシーケンスの検証]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing)を参照してください。

## トラブルシューティング

### Web SDKのセッションが誤ったユーザーに紐付けられる

GTMがBrazeの初期化タグやイベントタグを、アプリがサインイン済みユーザーを特定する前に発火させると、セッションやイベントが誤ったプロファイルに紐付けられる場合があります。Web SDKを初期化し、サインイン済みユーザーの`external_id`を指定して`changeUser()`を呼び出し、その後イベントのロギングや属性の設定を行うタグの前に`openSession()`を呼び出してください。GTMのタグシーケンスや同意トリガーを使用して、認証フローが完了した後にのみBrazeタグが実行されるようにしてください。

### ShopifyまたはスクリプトタグでインストールしたWeb SDKのコンソールログ

Shopifyアプリの埋め込みはコンソールログをオフにしてWeb SDKを読み込みます。GTM初期化タグまたは`initialize()`オプションでログを設定してください。Brazeダッシュボードには、これらのローダーに対するログ制御は含まれていません。

ブラウザコンソールにBrazeのログが表示される場合は、本番環境に公開する前にGTM初期化タグまたはカスタムHTMLから`enableLogging: true`を削除してください。初期化後は、`toggleLogging()`または`?brazeLogging=true` URLパラメーターを使用してください。Web SDKの全オプションについては、[詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)を参照してください。

Brazeが初期化されない場合やイベントが期待どおりに表示されない場合は、GTMコンテナが公開済みであること、トリガーとタグの発火順序がSDKの[ライフサイクルと初期化戦略]({{site.baseurl}}/developer_guide/sdk_integration)と合致していること、テストデバイスがBrazeエンドポイントをブロックしていないことを確認してください。

初期化の失敗については、Brazeタグまたはカスタムタグプロバイダーが期待される`actionType`とパラメーターを受信していることを確認してください（このページのAndroid、Swift、Webタブを参照）。GTMから発火されたイベントを検証する際の詳細ログについては、それらのタブからリンクされているプラットフォーム統合ガイドの説明に従って、各プラットフォームのSDKデバッグログを有効にしてください。