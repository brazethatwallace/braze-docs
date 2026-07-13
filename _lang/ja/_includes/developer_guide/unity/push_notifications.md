{% multi_lang_include developer_guide/prerequisites/unity.md %}

## プッシュ通知の設定 {#setting-up-push-notification}

### ステップ1:プラットフォームを設定する {#step-1-set-up-the-platform}

{% tabs %}
{% tab Android %}
#### ステップ1.1:Firebaseを有効にする {#step-11-enable-firebase}

開始するには、[Firebase Unityの設定ドキュメント](https://firebase.google.com/docs/unity/setup)に従ってください。

{% alert note %}
Firebase Unity SDKを統合すると、`AndroidManifest.xml`がオーバーライドされる場合があります。その場合は、必ず元に戻してください。
{% endalert %}

#### ステップ1.2:Firebaseの認証情報を設定する {#step-12-set-your-firebase-credentials}

FirebaseサーバーキーとSender IDをBrazeダッシュボードに入力する必要があります。これを行うには、[Firebase Developers Console](https://console.firebase.google.com/)にログインし、Firebaseプロジェクトを選択します。次に、**Settings**の下にある**Cloud Messaging**を選択し、サーバーキーとSender IDをコピーします。<br>![FirebaseコンソールのCloud Messaging設定。サーバーキーとSender IDが表示されています。]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Brazeの**設定の管理**にある**アプリ設定**ページでAndroidアプリを選択します。次に、**Firebase Cloud Messaging Server Key**フィールドにFirebaseサーバーキーを入力し、**Firebase Cloud Messaging Sender** IDフィールドにFirebase Sender IDを入力します。

![BrazeのAndroidアプリ設定。Firebase Cloud MessagingサーバーキーとSender IDのフィールドが表示されています。]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### ステップ1.1:統合方法を確認する {#step-11-verify-integration-method}

Brazeは、iOSプッシュ統合を自動化するためのUnityネイティブソリューションを提供します。代わりに手動で統合の設定と管理を行いたい場合は、[Swift:プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を参照してください。

それ以外の場合は、次のステップに進みます。

{% alert note %}
自動プッシュ通知ソリューションは、iOS 12の暫定認証機能を利用しており、ネイティブのプッシュプロンプトポップアップでは使用できません。
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### ステップ1.1:ADMを有効にする {#step-11-enable-adm}

1. まだアカウントを作成していない場合は、[Amazon Apps & Games Developer Portal](https://developer.amazon.com/public)でアカウントを作成します。
2. [OAuth認証情報（クライアントIDとクライアントシークレット）とADM APIキー](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)を取得します。
3. Unity Braze設定ウィンドウで**Automatic ADM Registration Enabled**を有効にします。
  - または、`res/values/braze.xml`ファイルに次の行を追加して、ADM登録を有効にすることもできます。

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### ステップ2:プッシュ通知を構成する {#step-2-configure-push-notifications}

{% tabs %}
{% tab Android %}
#### ステップ2.1:プッシュ設定を行う {#unity_step-21-configure-push-settings}

Braze SDKは、Firebase Cloud Messagingサーバーへのプッシュ登録を自動的に処理して、デバイスがプッシュ通知を受信できるようにすることができます。Unityで**Automate Unity Android Integration**を有効にし、以下の**プッシュ通知**設定を行います。

| 設定 | 説明 |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatic Firebase Cloud Messaging Registration Enabled | デバイスのFCMプッシュトークンを自動的に取得して送信するようにBraze SDKに指示します。 |
| Firebase Cloud Messaging Sender ID | Firebaseコンソールの送信者ID。 |
| Handle Push Deeplinks Automatically | プッシュ通知がクリックされたときに、ディープリンクを開くかアプリを開くかをSDKで処理するかどうか。 |
| Small Notification Icon Drawable | プッシュ通知が届いたときに表示される小さなアイコンのAndroid Drawableリソース参照。`@drawable/`プレフィックスを含む完全な参照を入力します（例:`@drawable/hourglass_icon`）。自動統合はこの値をそのまま`braze.xml`に書き込みます。空のままにすると、通知はアプリケーションアイコンを小さなアイコンとして使用します。 |
| Large Notification Icon Drawable | 通知用のオプションの大きなアイコン。小さなアイコンと同じ`@drawable/`形式を使用します（例:`@drawable/my_large_icon`）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2.1: Configure push settings" }

{% alert note %}
**Small Notification Icon Drawable**と**Large Notification Icon Drawable**は、**Braze > Braze Configuration**の**Push Configuration**の下に表示されます。両方の値は入力したとおりに`braze.xml`に書き込まれます。`@drawable/`プレフィックスは自分で含めてください。Braze Unity統合では自動的に追加されません（例:`<drawable name="com_braze_push_small_notification_icon">@drawable/hourglass_icon</drawable>`）。
{% endalert %}
{% endtab %}

{% tab Swift %}
#### ステップ2.1:APNsトークンをアップロードする {#step-21-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### ステップ2.2:自動プッシュを有効にする {#step-22-enable-automatic-push}

Unityエディターで**Braze** > **Braze Configuration**の順に移動して、Braze構成設定を開きます。

**Integrate Push With Braze**をチェックして、プッシュ通知用にユーザーを自動的に登録し、プッシュトークンをBrazeに渡し、プッシュ開封の分析を追跡し、デフォルトのプッシュ通知処理を利用します。

#### ステップ2.3:バックグラウンドプッシュを有効にする（オプション） {#step-23-enable-background-push-optional}

プッシュ通知で`background mode`を有効にする場合は、**Enable Background Push**をチェックします。これにより、プッシュ通知が到着したときにシステムがアプリケーションを`suspended`状態から復帰させ、アプリケーションがプッシュ通知に応答してコンテンツをダウンロードできるようになります。アンインストール追跡機能を使用するには、このオプションをチェックする必要があります。

![Unityエディターに Brazeの設定オプションが表示されています。このエディターでは、「Automate Unity iOS integration」、「Integrate push with braze」、および「Enable background push」が有効になっています。]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### ステップ2.4:自動登録を無効にする（オプション） {#step-24-disable-automatic-registration-optional}

まだプッシュ通知をオプトインしていないユーザーは、アプリケーションを開くと自動的にプッシュの許可が付与されます。この機能を無効にし、手動でユーザーをプッシュ登録するには、**Disable Automatic Push Registration**をチェックします。

- iOS 12以降で**Disable Provisional Authorization**がチェックされていない場合、ユーザーはサイレントプッシュを受信することを暫定的に（サイレントに）許可されます。チェックした場合、ユーザーにネイティブのプッシュプロンプトが表示されます。
- 実行時にプロンプトが表示されるタイミングを正確に設定する必要がある場合は、Braze構成エディターから自動登録を無効にし、代わりに`AppboyBinding.PromptUserForPushPermissions()`を使用します。

![Unityエディターに Brazeの設定オプションが表示されています。このエディターでは、「Automate Unity iOS integration」、「Integrate push with braze」、および「Disable automatic push registration」が有効になっています。]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### ステップ2.1:`AndroidManifest.xml`を更新する {#unity_step-21-update-androidmanifestxml}

アプリに`AndroidManifest.xml`がない場合は、以下をテンプレートとして使用できます。それ以外の場合、すでに`AndroidManifest.xml`がある場合は、以下の不足しているセクションが既存の`AndroidManifest.xml`に追加されていることを確認してください。

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:label="@string/app_name"
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### ステップ2.2:ADM APIキーを保存する {#step-22-store-your-adm-api-key}

まず、[アプリ用のADM APIキーを生成](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)し、そのキーを`api_key.txt`という名前のファイルに保存して、プロジェクトの[`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html)ディレクトリに追加します。

{% alert important %}
`api_key.txt`に末尾の改行などの空白文字が含まれている場合、Amazonはキーを認識しません。
{% endalert %}

次に、`mainTemplate.gradle`ファイルに以下を追加します。

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### ステップ2.3:ADM Jarを追加する {#step-23-add-adm-jar}

必要なADM Jarファイルは、[Unity JARドキュメント](https://docs.unity3d.com/Manual/AndroidJARPlugins.html)に従ってプロジェクト内の任意の場所に配置できます。

#### ステップ2.4:クライアントシークレットとクライアントIDをBrazeダッシュボードに追加する {#step-24-add-client-secret-and-client-id-to-your-braze-dashboard}

最後に、[ステップ1](#unity_step-1-enable-adm)で取得したクライアントシークレットとクライアントIDをBrazeダッシュボードの**設定の管理**ページに追加する必要があります。

![Braze Fire OSアプリ設定ページ。ADMクライアントIDとクライアントシークレットのフィールドが表示されています。]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### ステップ3:プッシュリスナーを設定する {#step-3-set-push-listeners}

{% tabs %}
{% tab Android %}
#### ステップ3.1:プッシュ受信リスナーを有効にする {#step-31-enable-push-received-listener}

プッシュ受信リスナーは、ユーザーがプッシュ通知を受信したときに起動されます。Unityにプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、**Set Push Received Listener**の下でプッシュ受信リスナーのコールバックメソッドを指定します。

#### ステップ3.2:プッシュ開封リスナーを有効にする {#step-32-enable-push-opened-listener}

プッシュ開封リスナーは、ユーザーがプッシュ通知をクリックしてアプリを起動したときに起動されます。Unityにプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、**Set Push Opened Listener**の下でプッシュ開封リスナーのコールバックメソッドを指定します。

#### ステップ3.3:プッシュ削除リスナーを有効にする {#step-33-enable-push-deleted-listener}

プッシュ削除リスナーは、ユーザーがプッシュ通知をスワイプして削除したり、無視したりしたときに起動されます。Unityにプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、**Set Push Deleted Listener**の下でプッシュ削除リスナーのコールバックメソッドを指定します。

#### プッシュリスナーの例 {#push-listener-example}

次の例では、コールバックメソッド名`PushNotificationReceivedCallback`、`PushNotificationOpenedCallback`、および`PushNotificationDeletedCallback`をそれぞれ使用して、`BrazeCallback`ゲームオブジェクトを実装します。

![この実装例の図は、前のセクションで述べたBrazeの構成オプションと、C#のコードスニペットを示しています。]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Swift %}
#### ステップ3.1:プッシュ受信リスナーを有効にする

プッシュ受信リスナーは、ユーザーがアプリケーションをアクティブに使用しているとき（アプリがフォアグラウンドになっているときなど）にプッシュ通知を受信すると起動されます。Braze構成エディターでプッシュ受信リスナーを設定します。ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()`を使用し、`BrazeUnityMessageType.PUSH_RECEIVED`を指定します。

![Unityエディターに Brazeの設定オプションが表示されています。このエディターでは、「Set Push Received Listener」オプションが展開され、「Game Object Name」(AppBoyCallback) と「Callback Method Name」(PushNotificationReceivedCallback) が指定されています。]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### ステップ3.2:プッシュ開封リスナーを有効にする

プッシュ開封リスナーは、ユーザーがプッシュ通知をクリックしてアプリを起動したときに起動されます。Unityにプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、**Set Push Opened Listener**オプションの下でプッシュ開封リスナーのコールバックメソッドを指定します。

![Unityエディターに Brazeの設定オプションが表示されています。このエディターでは、「Set Push Opened Listener」オプションが展開され、「Game Object Name」(AppBoyCallback) と「Callback Method Name」(PushNotificationOpenedCallback) が指定されています。]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()`を使用し、`BrazeUnityMessageType.PUSH_OPENED`を指定します。

#### プッシュリスナーの例

次の例では、コールバックメソッド名`PushNotificationReceivedCallback`および`PushNotificationOpenedCallback`をそれぞれ使用して、`AppboyCallback`ゲームオブジェクトを実装します。

![この実装例の図は、前のセクションで述べたBrazeの構成オプションと、C#のコードスニペットを示しています。]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Amazon Device Messaging %}
[前のステップ](#unity_step-21-update-androidmanifestxml)で`AndroidManifest.xml`を更新した際に、以下の行を追加したことでプッシュリスナーが自動的に設定されています。そのため、追加の設定は必要ありません。

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
ADMプッシュリスナーについて詳しくは、[Amazon: Amazon Device Messagingを統合する](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

## オプション構成 {#optional-configurations}

{% tabs %}
{% tab Android %}
### アプリ内リソースへのディープリンク {#deep-linking-to-in-app-resources}

Brazeはデフォルトで標準的なディープリンク（WebサイトのURL、AndroidのURIなど）を処理できますが、カスタムディープリンクを作成するには、追加のマニフェスト設定が必要です。

設定ガイダンスについては、[アプリ内リソースへのディープリンク](https://developer.android.com/training/app-links/deep-linking)を参照してください。

#### Brazeプッシュ通知アイコンの追加 {#adding-braze-push-notification-icons}

{% alert important %}
通知アイコンの画像を`Assets/Plugins/Android/res`に追加しないでください。Unityは[このパスでのAndroidリソースの提供を非推奨](https://support.unity.com/hc/en-us/articles/115005875443-Providing-Android-resources-in-Assets-Plugins-Android-res-is-deprecated)としており、ビルド警告やバリデーションエラーが発生する可能性があります。アイコンのDrawableは[Android Archive（AAR）プラグイン](https://docs.unity3d.com/Manual/AndroidAARPlugins.html)またはAndroidライブラリプロジェクトにパッケージ化して、他のDrawableと同様にビルドされたアプリのリソースにマージされるようにしてください。
{% endalert %}

プロジェクトにプッシュアイコンを追加するには、`res/drawable*`（または密度別フォルダー）の下にアイコン画像ファイルを含むAARプラグインまたはAndroidライブラリを作成し、**Braze > Braze Configuration**で完全な`@drawable/`リソース名を使用して各アイコンを参照します（[ステップ2.1:プッシュ設定を行う](#unity_step-21-configure-push-settings)を参照）。Unityのパッケージングとインポートの手順については、[Android Library Projects and Android Archive plug-ins](https://docs.unity3d.com/Manual/AndroidAARPlugins.html)を参照してください。

小さなアイコンのアートワークルール（アルファのみ、色なし）については、[Androidプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)のステップ2:小さなアイコンをデザインガイドラインに準拠させるを参照してください。
{% endtab %}

{% tab Swift %}
#### プッシュトークンコールバック {#push-token-callback}

OSからBrazeデバイストークンのコピーを受け取るには、`AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`を使用してデリゲートを設定します。
{% endtab %}

{% tab Amazon Device Messaging %}
現時点では、ADMのオプション構成はありません。
{% endtab %}
{% endtabs %}