{% multi_lang_include developer_guide/prerequisites/web.md %} また、Web SDK用の[プッシュ通知を設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)する必要があります。iOSおよびiPadOSユーザーにプッシュ通知を送信できるのは、[Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes)以降を使用している場合に限られます。

## モバイル向けSafariプッシュの設定 {#setting-up-safari-push-for-mobile}

### ステップ1：マニフェストファイルを作成する {#manifest}

[Webアプリケーションマニフェスト](https://developer.mozilla.org/en-US/docs/Web/Manifest)は、ユーザーのホーム画面にインストールされたときにWebサイトがどのように表示されるかを制御するJSONファイルです。

例えば、[App Switcher](https://support.apple.com/en-us/HT202070)が使用するバックグラウンドのテーマカラーやアイコン、ネイティブアプリのようにフルスクリーンでレンダリングするかどうか、アプリをランドスケープモードで開くかポートレートモードで開くかなどを設定できます。

Webサイトのルートディレクトリに、以下の必須フィールドを含む新しい`manifest.json`ファイルを作成します。

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

サポートされるフィールドの全リストは、[MDNのWebアプリマニフェストドキュメント](https://developer.mozilla.org/en-US/docs/Web/Manifest)で確認できます。

### ステップ2：マニフェストファイルをリンクする {#manifest-link}

Webサイトの`<head>`要素に、マニフェストファイルがホストされている場所を指す次の`<link>`タグを追加します。

```html
<link rel="manifest" href="/manifest.json" />
```

### ステップ3：サービスワーカーを追加する {#service-worker}

[Webプッシュ統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker)で説明されているように、Webサイトにはbrazeのサービスワーカーライブラリをインポートするサービスワーカーファイルが必要です。

### ステップ4：ホーム画面に追加する {#add-to-homescreen}

主要なブラウザ（Safari、Chrome、FireFox、Edgeなど）は、いずれも最新バージョンでWebプッシュ通知をサポートしています。iOSまたはiPadOSでプッシュ通知の権限をリクエストするには、ユーザーが**「共有」**>**「ホーム画面に追加」**を選択して、Webサイトをホーム画面に追加する必要があります。[ホーム画面に追加](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc)機能を使うと、ユーザーがWebサイトをブックマークでき、アイコンがユーザーの貴重なホーム画面スペースに追加されます。

![Webサイトをブックマークしてホーム画面に保存するオプションを表示するiPhone]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### ステップ5：ネイティブのプッシュプロンプトを表示する {#push-prompt}
アプリがホーム画面に追加された後、ユーザーがアクション（ボタンをクリックするなど）を行った際にプッシュ通知の権限をリクエストできるようになります。これを行うには、[`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission)メソッドを使用するか、[コードなしのプッシュプライマーアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)を使用します。

{% alert note %}
プロンプトを承認または拒否した後、再度プロンプトを表示するには、Webサイトをホーム画面から削除して再インストールする必要があります。
{% endalert %}

![通知を「許可」するか「許可しない」かを尋ねるプッシュプロンプト]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

以下はその例です。

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## 次のステップ {#next-steps}

次に、自分自身に[テストメッセージを送信]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)して、統合を検証します。統合が完了したら、[コードなしのプッシュプライマーメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)を使用して、プッシュオプトイン率を最適化できます。