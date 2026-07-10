## Android TV用プッシュ通知について {#about-push-notifications-for-android-tv}

![Android TVプッシュ通知ガイドで使用されるAndroid TVデバイスのイラスト。]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Android TVプッシュ統合はネイティブ機能ではありませんが、Braze Android SDKとFirebase Cloud Messagingを利用してAndroid TV用のプッシュトークンを登録することで実現できます。ただし、通知ペイロードを受信した後にそれを表示するUIを構築する必要があります。

## 前提条件 {#prerequisites}

この機能を使用するには、以下を完了する必要があります。

- [Braze Android SDKを統合する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Braze Android SDKのプッシュ通知を設定する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## プッシュ通知のセットアップ {#setting-up-push-notifications}

Android TVのプッシュ通知を設定するには:

1. アプリでカスタムビューを作成して、通知を表示します。
2. [カスタム通知ファクトリー]({{site.baseurl}}/developer_guide/push_notifications/customization#customization-display)を作成します。これにより、デフォルトのSDK動作がオーバーライドされ、通知を手動で表示できるようになります。`null`を返すことでSDKの処理が防止され、通知を表示するためにカスタムコードが必要になります。これらのステップが完了したら、Android TVへのプッシュ送信を開始できます。<br><br>
3. （オプション）クリック分析を効果的にトラッキングするには、クリック分析トラッキングを設定します。これは、Brazeプッシュ通知の開封および受信インテントをリッスンする[プッシュコールバック]({{site.baseurl}}/developer_guide/push_notifications/customization#push-callback)を作成することで実現できます。

{% alert note %}
これらの通知は**永続的ではなく**、デバイスが表示するときにのみユーザーに表示されます。これは、Android TVの通知センターが過去の通知をサポートしていないためです。
{% endalert %}

## Android TVプッシュ通知のテスト {#testing-android-tv-push-notifications}

プッシュ実装が成功したかどうかをテストするには、通常Androidデバイスで行うようにBrazeダッシュボードから通知を送信します。

- **アプリケーションが閉じている場合**：プッシュメッセージは画面にトースト通知として表示されます。
- **アプリケーションが開いている場合**：独自にホストしているUIでメッセージを表示できます。Android Mobile SDKのアプリ内メッセージのUIスタイルに従うことをお勧めします。

## ベストプラクティス {#best-practices}

Brazeを使用するマーケターの場合、Android TVへのキャンペーンの配信は、Androidモバイルアプリへのプッシュ配信と同じです。これらのデバイスのみをターゲットにするには、セグメンテーションでAndroid TVアプリを選択することをお勧めします。

FCMによって返される配信およびクリックのレスポンスは、モバイルAndroidデバイスと同じ規則に従います。そのため、エラーがあればメッセージアクティビティログに表示されます。