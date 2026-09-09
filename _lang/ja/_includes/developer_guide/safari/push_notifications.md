{% multi_lang_include developer_guide/prerequisites/web.md %} また、Web SDK用の[プッシュ通知を設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)する必要があります。iOSおよびiPadOSユーザーにプッシュ通知を送信できるのは、[Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes)以降を使用している場合に限られます。

## モバイル向け Safari プッシュの設定 {#setting-up-safari-push-for-mobile}

### ステップ1: マニフェストファイルを作成する {#manifest}

[Web アプリケーションマニフェスト](https://developer.mozilla.org/en-US/docs/Web/Manifest)は、ユーザーのホーム画面にインストールされたときにWebサイトがどのように表示されるかを制御するJSONファイルです。

たとえば、[App Switcher](https://support.apple.com/en-us/HT202070)で使用されるバックグラウンドテーマの色やアイコン、ネイティブアプリのようにフルスクリーンで表示するかどうか、アプリを横向きまたは縦向きモードで開くかどうかを設定できます。

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

サポートされているフィールドの完全なリストは、[MDNのWebアプリマニフェストドキュメント](https://developer.mozilla.org/en-US/docs/Web/Manifest)を参照してください。

### ステップ2: マニフェストファイルをリンクする {#manifest-link}

マニフェストファイルがホストされている場所を指す以下の`<link>`タグを、Webサイトの`<head>`要素に追加します。

```html
<link rel="manifest" href="/manifest.json" />
```

### ステップ3: サービスワーカーを追加する {#service-worker}

[Webプッシュ統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker)で説明されているように、Webサイトにはbrazeサービスワーカーライブラリをインポートするサービスワーカーファイルが必要です。

### ステップ4: ホーム画面に追加する {#add-to-homescreen}

一般的なブラウザー（Safari、Chrome、FireFox、Edgeなど）はすべて、最新バージョンでWebプッシュ通知をサポートしています。iOSまたはiPadOSでプッシュ許可をリクエストするには、**共有** > **ホーム画面に追加**を選択して、Webサイトをユーザーのホーム画面に追加する必要があります。[ホーム画面に追加](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc)を使用すると、ユーザーはWebサイトをブックマークし、ホーム画面にアイコンを追加できます。

![Webサイトをブックマークしてホーム画面に保存するオプションを表示しているiPhone]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### ステップ5: ネイティブプッシュプロンプトを表示する {#push-prompt}
アプリがホーム画面に追加された後、ユーザーがアクション（ボタンのクリックなど）を実行したときにプッシュ許可をリクエストできます。これは[`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission)メソッド、または[コード不要のプッシュプライマーアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を使用して行うことができます。

{% alert note %}
プロンプトを承認または拒否した後、再度プロンプトを表示するには、Webサイトを削除してホーム画面に再インストールする必要があります。
{% endalert %}

![通知を「許可」または「許可しない」を尋ねるプッシュプロンプト]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

以下に例を示します。

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

次に、統合を検証するために[テストメッセージ]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages)を自分自身に送信します。統合が完了したら、[ノーコードのプッシュプライマーメッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を使用して、プッシュ通知のオプトイン率を最適化できます。