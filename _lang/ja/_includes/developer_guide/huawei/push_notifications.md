{% multi_lang_include developer_guide/prerequisites/android.md %}

## プッシュ通知の設定 {#setting-up-push-notifications}

[Huawei](https://huaweimobileservices.com/) 製の新しいスマートフォンには、GoogleのFirebase Cloud Messaging (FCM) の代わりにプッシュ配信に使用されるサービス、Huawei Mobile Services (HMS) が搭載されています。

### ステップ1:Huawei開発者アカウントに登録する {#step-1-register-for-a-huawei-developer-account}

始める前に、[Huawei開発者アカウント](https://developer.huawei.com/consumer/en/console)への登録と設定が必要です。Huaweiアカウントで、**[My Projects] > [Project Settings] > [App Information]** に移動し、`App ID` と `App secret` を書き留めます。

![App IDとApp secretが表示されているHuawei開発者コンソールのアプリ情報ページ。]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### ステップ2:Brazeダッシュボードで新しいHuaweiアプリを作成する {#step-2-create-a-new-huawei-app-in-the-braze-dashboard}

Brazeダッシュボードで、**設定**ナビゲーションの下にある**アプリ設定**に移動します。

**+ アプリを追加**をクリックし、名前（My Huawei Appなど）を入力し、プラットフォームとして `Android` を選択します。

![Android Huaweiアプリを作成するBrazeのアプリ追加ダイアログ。]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

新しいBrazeアプリを作成したら、プッシュ通知設定を見つけて、プッシュプロバイダーとして `Huawei` を選択します。次に、`Huawei Client Secret` と `Huawei App ID` を指定します。

![Huawei App IDとClient Secretフィールドが表示されているBrazeのHuaweiプッシュプロバイダー設定。]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### ステップ3:HuaweiメッセージングSDKをアプリに統合する {#step-3-integrate-the-huawei-messaging-sdk-into-your-app}

Huaweiは、Huawei Messaging Serviceをアプリケーションに統合する[Android統合codelab](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html)を提供しています。以下の手順に従って開始してください。

codelabが完了したら、カスタムの[Huawei Message Service](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls)を作成してプッシュトークンを取得し、メッセージをBraze SDKに転送する必要があります。

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

カスタムプッシュサービスを追加した後、`AndroidManifest.xml` に以下を追加します。

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### ステップ4:フォアグラウンド通知を処理する {#step-4-handle-foreground-notifications}

デフォルトでは、アプリがフォアグラウンドにあるときにプッシュ通知が届くと、Huaweiは自動的にそれを表示します。Brazeにプッシュ通知のペイロードを処理させる場合（分析トラッキング、ディープリンク処理、カスタム処理のため）、`HmsMessageService.onMessageReceived` メソッド内で受信したプッシュデータをBrazeにルーティングします。

`BrazeHuaweiPushHandler.handleHmsRemoteMessageData` を呼び出すと、BrazeはペイロードがBrazeプッシュ通知かどうかを判断し、該当する場合は通知を作成して表示します。詳細については、Androidプッシュ通知のドキュメントにある[フォアグラウンド通知の処理]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications)を参照してください。

完全な例については、Braze Android SDKドキュメントの[Huaweiハンドラーリファレンス](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-huawei-push-handler/index.html)を参照してください。

### ステップ5:プッシュ通知をテストする（任意） {#step-5-test-your-push-notifications-optional}

ここまでで、Brazeダッシュボードに新しいHuawei Androidアプリを作成し、Huawei開発者の認証情報を使用して設定し、BrazeおよびHuawei SDKをアプリに統合しました。

次に、Brazeで新しいプッシュキャンペーンをテストすることで、統合をテストできます。

#### ステップ5.1:新しいプッシュ通知キャンペーンを作成する {#step-51-create-a-new-push-notification-campaign}

**キャンペーン**ページで、新しいキャンペーンを作成し、メッセージタイプとして**プッシュ通知**を選択します。

キャンペーンに名前を付けたら、プッシュプラットフォームとして**Androidプッシュ**を選択します。

![利用可能なプッシュプラットフォームを表示するキャンペーン作成コンポーザー。]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

次に、タイトルとメッセージを入力してプッシュキャンペーンを作成します。

#### ステップ5.2:テストプッシュを送信する {#step-52-send-a-test-push}

**テスト**タブで、[`changeUser(USER_ID_STRING)` メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#assigning-a-user-id)を使ってアプリに設定したユーザーIDを入力し、**テスト送信**をクリックしてテストプッシュを送信します。

![キャンペーン作成コンポーザーのテストタブ。ユーザーIDを入力し、「個人ユーザーを追加」フィールドに入力することで、自分自身にテストメッセージを送信できます。]({% image_buster /assets/img/huawei/huawei-test-send.png %})

この時点で、BrazeからHuawei (HMS) デバイスにテストプッシュ通知が届くはずです。

#### ステップ5.3:Huaweiセグメンテーションを設定する（任意） {#step-53-set-up-huawei-segmentation-optional}

Brazeダッシュボードの Huaweiアプリは Androidプッシュプラットフォーム上に構築されているため、すべてのAndroidユーザー（Firebase Cloud MessagingおよびHuawei Mobile Services）にプッシュを送信するか、キャンペーンオーディエンスを特定のアプリにセグメント化するかを柔軟に選択できます。

Huaweiアプリのみにプッシュを送信するには、[新しいセグメントを作成]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform)して、**アプリ**セクション内でHuaweiアプリを選択します。

![プッシュターゲティング用にHuaweiアプリを選択するBrazeセグメントのアプリフィルター。]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

もちろん、すべてのAndroidプッシュプロバイダーに同じプッシュを送信する場合は、アプリを指定しないことを選択することで、現在のワークスペース内で設定されているすべてのAndroidアプリに送信できます。