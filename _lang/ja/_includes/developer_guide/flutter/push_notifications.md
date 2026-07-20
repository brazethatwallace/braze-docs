{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## プッシュ通知の設定 {#setting-up-push-notifications}

### ステップ1: 初期設定を完了する {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### ステップ1.1: プッシュ登録 {#step-11-register-for-push}

GoogleのFirebase Cloud Messaging（FCM）APIを使用してプッシュに登録します。詳しい手順については、[ネイティブAndroidプッシュ通知統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/)の以下のステップを参照してください。

1. [Firebaseをプロジェクトに追加します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-1-add-firebase-to-your-project)。
2. [Cloud Messagingを依存関係に追加します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-2-add-cloud-messaging-to-your-dependencies)。
3. [サービスアカウントを作成します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-3-create-a-service-account)。
4. [JSON認証情報を生成します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-generate-json-credentials)。
5. [JSON認証情報をBrazeにアップロードします]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-5-upload-your-json-credentials-to-braze)。

#### ステップ1.2: Google Sender IDを取得する {#step-12-get-your-google-sender-id}

まずFirebase Consoleに移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**を選択します。

![「Settings」メニューが開かれたFirebaseプロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**Cloud Messaging**を選択し、**Firebase Cloud Messaging API (V1)**の下にある**Sender ID**をクリップボードにコピーします。

![Firebaseプロジェクトの「Cloud Messaging」ページで「Sender ID」がハイライトされている。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### ステップ1.3: `braze.xml`を更新する {#step-13-update-your-brazexml}

`braze.xml`ファイルに以下を追加します。`FIREBASE_SENDER_ID`を、先ほどコピーした送信者IDに置き換えます。

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### ステップ1.1: APNs証明書をアップロードする {#step-11-upload-apns-certificates}

Appleプッシュ通知サービス（APNs）証明書を生成し、Brazeダッシュボードにアップロードします。詳細な手順については、[APNs証明書のアップロード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-upload-your-apns-certificate)を参照してください。

#### ステップ1.2: アプリにプッシュ通知サポートを追加する {#step-12-add-push-notification-support-to-your-app}

[ネイティブiOS統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)の手順に従います。

{% endtab %}
{% endtabs %}

### ステップ2: プッシュ通知イベントをリッスンする（オプション） {#step-2-listen-for-push-notification-events-optional}

Brazeが検出して処理したプッシュ通知イベントをリッスンするには、`subscribeToPushNotificationEvents()`を呼び出し、実行する引数を渡します。

{% alert note %}
Brazeプッシュ通知イベントは、AndroidとiOSの両方で利用できます。プラットフォームの違いにより、iOSではユーザーが通知を操作した場合にのみBrazeプッシュイベントが検出されます。
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### プッシュ通知イベントフィールド {#push-notification-event-fields}

{% alert note %}
iOSのプラットフォーム制限のため、Braze SDKはアプリがフォアグラウンドにあるときにのみプッシュペイロードを処理できます。リスナーは、ユーザーがプッシュを操作した後、iOSでは`push_opened`イベントタイプに対してのみトリガーされます。
{% endalert %}

プッシュ通知フィールドの完全なリストについては、以下の表を参照してください。

| フィールド名 | タイプ | 説明 |
| ------------------ | --------- | ----------- |
| `payloadType` | 文字列 | 通知ペイロードのタイプを指定します。Braze Flutter SDKから送信される2つの値は、`push_opened`と`push_received`です。iOSでは`push_opened`イベントのみがサポートされています。 |
| `url` | 文字列 | 通知によって開かれたURLを指定します。 |
| `useWebview` | ブール値 | `true`の場合、URLはアプリ内のモーダルウェブビューで開かれます。`false`の場合、URLはデバイスのブラウザーで開かれます。 |
| `title` | 文字列 | 通知のタイトルを表します。 |
| `body` | 文字列 | 通知の本文またはコンテンツテキストを表します。 |
| `summaryText` | 文字列 | 通知の要約テキストを表します。これはiOSでは`subtitle`からマッピングされます。 |
| `badgeCount` | 数値 | 通知のバッジカウントを表します。 |
| `timestamp` | 数値 | ペイロードがアプリケーションによって受信された時刻を表します。 |
| `isSilent` | ブール値 | `true`の場合、ペイロードはサイレントに受信されます。Androidのサイレントプッシュ通知の送信の詳細については、[Androidでのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を参照してください。iOSのサイレントプッシュ通知の送信の詳細については、[iOSでのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)を参照してください。 |
| `isBrazeInternal` | ブール値 | フィーチャーフラグの同期やアンインストール追跡などの内部SDK機能に対して通知ペイロードが送信された場合、これは`true`になります。ペイロードはユーザーに対してサイレントに受信されます。 |
| `imageUrl` | 文字列 | 通知画像に関連するURLを指定します。 |
| `brazeProperties` | オブジェクト | キャンペーンに関連するBrazeプロパティ（キーと値のペア）を表します。 |
| `ios` | オブジェクト | iOS固有のフィールドを表します。 |
| `android` | オブジェクト | Android固有のフィールドを表します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュ通知イベントフィールド" }

### ステップ3: プッシュ通知の表示をテストする {#step-3-test-displaying-push-notifications}

ネイティブレイヤーでプッシュ通知を設定した後、統合をテストするには：

1. Flutterアプリケーションでアクティブユーザーを設定します。これを行うには、`braze.changeUser('your-user-id')`を呼び出してプラグインを初期化します。
2. **キャンペーン**に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、**テスト**タブに移動します。テストユーザーと同じ`user-id`を追加し、**テスト送信**をクリックします。
4. まもなくデバイスに通知が届くはずです。通知が表示されない場合は、通知センターで確認するか、設定を更新する必要がある場合があります。

{% alert tip %}
Xcode 14以降、iOSシミュレーター上でリモートプッシュ通知をテストできるようになりました。
{% endalert %}