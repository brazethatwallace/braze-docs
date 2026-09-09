{% multi_lang_include developer_guide/prerequisites/web.md %} [プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)も必要です。

mParticleの組み込みキットを使用してWebでBrazeを統合している場合は、ソフトプッシュプロンプトの実装手順について[mParticleのBraze Webイベント統合のステップ3](https://docs.mparticle.com/integrations/braze/event/#web)を参照してください。

## ソフトプッシュプロンプトについて {#about-soft-push-prompts}

サイトでは、プッシュ許可をリクエストする前に、ユーザーに「事前説明」を行い、プッシュ通知を送信する理由を伝える「ソフト」プッシュプロンプトを実装することが推奨されます。これが有用な理由は、ブラウザーがユーザーに直接プロンプトを表示できる頻度を制限しているためです。また、ユーザーが許可を拒否した場合、再度リクエストすることはできません。

また、標準の[Webプッシュ統合]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-2-browser-registration)で説明されているように`requestPushPermission()`を直接呼び出す代わりに、特別なカスタム処理を含めたい場合は、[トリガーされたアプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)を使用してください。

{% alert tip %}
これは、新しい[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を使用することで、SDKのカスタマイズなしで実現できます。
{% endalert %}

## ソフトプッシュプロンプトの設定 {#setting-up-soft-push-prompts}

{% multi_lang_include archive/web-v4-rename.md %}

### ステップ1:プッシュプライマーキャンペーンを作成する {#step-1-create-a-push-primer-campaign}

まず、Brazeダッシュボードで「Prime for Push」アプリ内メッセージングキャンペーンを作成する必要があります。

1. 希望するテキストとスタイルで**モーダル**アプリ内メッセージを作成します。
2. 次に、クリック時の動作を**メッセージを閉じる**に設定します。この動作は後でカスタマイズします。
3. メッセージにキーと値のペアを追加します。キーは`msg-id`、値は`push-primer`です。
4. メッセージにカスタムイベントトリガーアクション（「prime-for-push」など）を割り当てます。必要に応じて、ダッシュボードからカスタムイベントを手動で作成できます。

### ステップ2:呼び出しを削除する {#step-2-remove-calls}

Braze SDKの統合で、読み込みスニペット内の`automaticallyShowInAppMessages()`への呼び出しをすべて見つけて削除します。

### ステップ3:統合を更新する {#step-3-update-integration}

最後に、削除した呼び出しを以下のスニペットに置き換えます。`openSession()`を呼び出す前に`subscribeToInAppMessage()`を呼び出してください。これにより、アプリ内メッセージリスナーがプッシュプライマーメッセージを受信するために適切なタイミングで登録されます。

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

ユーザーにソフトプッシュプロンプトを表示したい場合は、`braze.logCustomEvent`を呼び出します。このアプリ内メッセージをトリガーするイベント名を指定してください。