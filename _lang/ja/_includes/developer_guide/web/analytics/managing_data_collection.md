## データトラッキングを無効にする {#disabling-data-tracking}

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab 標準実装 %}
Web SDKのデータトラッキングアクティビティを無効にするには、メソッド[`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)を使用します。これにより、`disableSDK()`が呼び出される前にログされたデータが同期され、このページおよび今後のページ読み込みにおけるBraze Web SDKへの後続のすべての呼び出しが無視されます。
{% endtab %}

{% tab Google Tag Manager %}
Webトラッキングを無効にしたり再度有効にしたりするには、それぞれ**Disable Tracking**または**Resume Tracking**タグタイプを使用します。これらの2つのオプションは、[`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)と[`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)を呼び出します。
{% endtab %}
{% endtabs %}

### ベストプラクティス {#best-practices}

ユーザーにトラッキングを停止するオプションを提供するには、2つのリンクまたはボタンを含むシンプルなページを構築することをお勧めします。1つはクリック時に`disableSDK()`を呼び出し、もう1つは`enableSDK()`を呼び出してユーザーが再度オプトインできるようにします。これらのコントロールを使用して、他のデータサブプロセッサーを介したトラッキングの開始や停止も行えます。

{% alert note %}
Braze SDKは`disableSDK()`を呼び出すために初期化する必要がないため、完全に匿名のユーザーに対してもトラッキングを無効にできます。逆に、`enableSDK()`はBraze SDKを初期化しないため、トラッキングを有効にするにはその後に`initialize()`も呼び出す必要があります。
{% endalert %}

## データトラッキングを再開する {#resuming-data-tracking}

データ収集を再開するには、[`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) メソッドを使用します。

## ログアウトとプッシュ登録解除 {#logout-and-unregister-push}

Braze SDKは、ユーザーがプッシュ通知の登録を解除したりログアウトしたりする際に、デバイスへのターゲティングを停止するためのメソッドを提供しています。これらのメソッドは、BrazeサーバーおよびSDKから現在のユーザーのプッシュ登録データを削除するため、Brazeはそのユーザーに今後のプッシュ通知キャンペーンを送信しなくなります。

### ログアウト {#logout}

ユーザーがアプリケーションからログアウトする際に、SDKの`logout`メソッドを呼び出して、現在のユーザーからデバイスのプッシュ登録を削除し、SDK上のクリーンアップアクションを自動的に実行します。`logout`メソッドは以下を実行します。

- Brazeサーバー上の現在のユーザーからデバイスのプッシュトークンの登録を解除します。
- 登録解除の呼び出しが成功した場合、SDKはローカルに保存されたSDKデータを消去し、SDKを無効化します。
- 失敗した場合、`errorCallback`を呼び出して、インテグレーターがアクションを実行できるようにします。

以下の例は、コールバックベースの`logout`処理を示しています。即時の成功およびエラー処理が必要な場合に使用し、ログ出力をアプリのフローに置き換えてください。

```javascript
import { logout } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully logged out');
};

const errorCallback = () => {
  console.log('Failed to log out');
};

logout(successCallback, errorCallback);
```

#### `logout`後にトラッキングとプッシュを再有効化する {#re-enable-tracking-and-push-after-logout}

`logout`が成功した後、[`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)を呼び出し、次に[Webプッシュの設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)に従って、オペレーティングシステム（OS）またはプッシュプロバイダーで通知を再登録します。

#### 即時の登録解除呼び出しを避ける {#avoid-immediate-unregister-calls}

OSまたはプッシュプロバイダーでプッシュ通知を登録した直後に`logout`または`unregisterPush`を呼び出すことは避けてください。非同期のサーバー処理により、まれにプッシュトークンがBrazeユーザーに再追加される可能性があります。

### プッシュ登録解除 {#unregister-push}

追加の自動クリーンアップなしにデバイスへのプッシュ送信を停止するには、`unregisterPush`メソッドを使用します。これにより、Brazeサーバー上の現在のユーザーからデバイスのプッシュトークンが削除され、ローカルに保存されたトークンがクリアされます。

以下の例は、コールバックベースの`unregisterPush`処理を示しています。即時の成功およびエラー処理が必要な場合に使用し、ログ出力をアプリのフローに置き換えてください。

```javascript
import { unregisterPush } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully unregistered from push');
};

const errorCallback = () => {
  console.log('Failed to unregister from push');
};

unregisterPush(successCallback, errorCallback);
```

#### `unregisterPush`後にプッシュを再登録する {#re-register-push-after-unregisterpush}

`unregisterPush`を呼び出した後、Brazeプッシュ通知を再度送信する前に、[Webプッシュの設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)に従って、OSまたはプッシュプロバイダーで通知を再登録してください。

{% alert note %}
サポートされているブラウザーでは、アクティブなプッシュサブスクリプションが存在する場合、`unregisterPush`はブラウザーのPush APIからのサブスクリプション解除後に、Brazeが管理するサービスワーカーの登録も解除します。`manageServiceWorkerExternally`を`true`に設定した場合、SDKはサービスワーカーの登録を解除しません。
{% endalert %}

#### 即時の登録解除呼び出しを避ける

OSまたはプッシュプロバイダーでプッシュ通知を登録した直後に`logout`または`unregisterPush`を呼び出すことは避けてください。非同期のサーバー処理により、まれにプッシュトークンがBrazeユーザーに再追加される可能性があります。