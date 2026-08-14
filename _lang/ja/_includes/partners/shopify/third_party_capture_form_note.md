{% alert note %}
[Shopifyの概要]({{site.baseurl}}/shopify_overview)で述べたように、サードパーティのキャプチャフォームを使用する場合、開発者がBraze SDKコードを統合する必要があります。これにより、フォーム送信からメールアドレスとグローバルメール購読ステータスをキャプチャできるようになります。具体的には、以下のメソッドを`theme.liquid`ファイルに実装してテストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): ユーザープロファイルにメールアドレスを設定します
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): グローバルメール購読ステータスを更新します
{% endalert %}