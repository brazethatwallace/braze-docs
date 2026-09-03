---
nav_title: Baidu の統合
article_title: Android 向け Baidu プッシュ通知の統合
platform: Android
permalink: /baidu_integration/
description: "この記事では、Baidu Android 統合の設定方法について説明します。"
hidden: true
excerpt_separator: ""
---
# Baidu の統合 {#baidu-integration}
{% alert warning %}
Brazeの Baidu プッシュ統合は、2022年3月24日をもって非推奨となりました。

* **2022年3月24日:** Brazeダッシュボードで新しい Baidu アプリを作成できなくなりました。
* **2022年9月15日:** 新しい Baidu プッシュメッセージを作成できなくなりました。既存のメッセージとデータ収集には影響ありません。
* **2023年1月15日:** Brazeは Baidu アプリからのメッセージ配信およびデータ収集を終了しました。
{% endalert %}

Brazeは、[Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}) を使用して Android デバイスにプッシュ通知を送信できます。Baidu Cloud Push を使用する場合、Baidu アプリストアを介してアプリを配布する必要はありません。

## ステップ1：Baiduアカウントを作成する {#step-1-create-a-baidu-account}

Baiduアカウントを作成するには、[Baiduポータル](https://www.baidu.com/)にアクセスし、**登录**（ログイン）をクリックして、ログインまたは新規アカウント作成が可能なダイアログを表示します。

![Baiduポータルページ]({% image_buster /assets/img_archive/baidu_portal.png %})

新規アカウントを作成するには、ログインダイアログの下部にある**立即注册**（新規アカウント）をクリックします。

![Baiduログインダイアログ]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

アカウント作成ページにユーザー名、電話番号、パスワードを入力します。次に、認証コード受信ボタンをクリックします。Baiduから認証コードを含むSMSメッセージが届きます。最後に、ライセンス契約に同意し、**注册**（アカウント作成）をクリックして登録を完了します。これらの設定ステップが失敗した場合は、この[ログインに関する記事](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/)に記載されているBaidu Cloudログインを使用して登録をお試しください。

![Baidu登録ページ]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## ステップ2:Baidu開発者として登録する {#step-2-register-as-a-baidu-developer}

次に、Baidu開発者として登録する必要があります。まず、[Baidu開発者ポータル](http://developer.baidu.com/)にアクセスし、**注册**（新しい開発者アカウントを作成）を選択して登録を開始します。

![Baidu開発者ポータルページ]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

登録ページで、アカウントタイプ（个人は個人用、公司はビジネス用）と開発者タイプ（ほとんどの場合、developerがあらかじめ選択されており、そのままで問題ありません）を選択します。名前、自己紹介、国コードを括弧で囲んだ電話番号を入力します（例：(1)xxxxxxxxxx）。**发送验证码**（認証コードを送信）をクリックし、次の行に認証コードを入力します。次の2つのフィールド（開発者Webサイトと開発者ロゴ）は任意です。ライセンス契約に同意し、**提交**（送信）をクリックして送信します。これでBaidu開発者アカウントが作成されました。

![Baidu開発者登録ページ]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## ステップ3:Baiduにアプリケーションを登録する {#step-3-register-your-application-with-baidu}

Baiduにアプリケーションを登録するには、[Baiduプロジェクトポータル](http://developer.baidu.com/console#app/project)にアクセスし、**创建工程**（プロジェクトを作成）をクリックします。

![Baiduプロジェクトポータルページ]({% image_buster /assets/img_archive/baidu_project.png %})

次のページで、アプリケーション名を入力します。以下の2つのチェックボックスは、追加のBaiduサービスを有効にするためのものです。ほとんどの場合、これらは空白のままにしてください。

![Baiduアプリケーション名の入力ページ]({% image_buster /assets/img_archive/baidu_app_name.png %})

アプリケーションの設定が完了すると、APIキーを含むアプリの情報が表示されるコンソールに移動します。次に、サイドバーの**云推送**（クラウドプッシュ）に移動します。次のページで、**推送设置**（プッシュの設定）をクリックします。

![APIキーを含むBaiduアプリコンソール]({% image_buster /assets/img_archive/baidu_app_console.png %})

![Baiduクラウドプッシュのページ]({% image_buster /assets/img_archive/baidu_continue.png %})

次のページで、アプリのパッケージ名（例：`com.braze.sample`）を入力し、メッセージをキャッシュするかどうか、キャッシュする場合はその期間（時間単位）を指定します。これは、オフラインユーザーへのメッセージ送信をBaiduがどのくらいの期間試行し続けるかを示します。**保存设置**（設定を保存）をクリックして保存します。

![Baiduクラウドプッシュの設定ページ]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## ステップ4:アプリケーションにBaiduを追加する {#step-4-add-baidu-to-your-application}

[BaiduプッシュSDKポータル](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)にアクセスし、最新のBaidu Cloud Push Android SDKをダウンロードします。

![Baidu SDKのダウンロードページ]({% image_buster /assets/img_archive/baidu_sdk.png %})

SDK内には、プッシュサービスのjarファイルとプラットフォーム固有のネイティブライブラリがあります。これらをプロジェクトに統合してください。アプリがBaiduで現在サポートされている最新のSDKバージョンをターゲットにしていることを確認してください。このドキュメントはBaidu Cloud Push Android SDKバージョン`4.6.2.38`に対応しています。

アプリケーションの`AndroidManifest.xml`に、以下の必要なBaiduパーミッションを追加します。

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

Baiduのライブラリには、受信プッシュメッセージを処理するブロードキャストレシーバーが含まれています。アプリケーションの`AndroidManifest.xml`の`<application>`要素内に、Baiduの内部レシーバーを宣言します。

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

また、受信プッシュメッセージと通知をリッスンするブロードキャストレシーバーを作成する必要があります。アプリケーションの`AndroidManifest.xml`の`<application>`要素内にレシーバーを宣言します。このレシーバーは`com.baidu.android.pushservice.PushMessageReceiver`を拡張し、Baiduプッシュサービスからのイベント更新を受信するメソッドを実装する必要があります。

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

メインアクティビティの`onCreate()`メソッドに以下の行を追加します。これにより、アプリケーションがBaiduに登録され、受信プッシュメッセージのリッスンが開始されます。「Your-API-Key」をプロジェクトのBaidu APIキーに置き換えてください。

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

最後に、ユーザーをBrazeに登録する必要があります。このステップで作成したBaiduブロードキャストレシーバーの`onBind()`メソッドで、`Braze.registerAppboyPushMessages(channelId)`を使用して`channelId`をBrazeに送信します。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## ステップ5: プッシュ開封の登録 {#step-5-registering-push-opens}

Baiduは、プッシュメッセージとともにJSON形式で追加のキーと値のペアを送信することをサポートしています。ブロードキャストレシーバーの`public void onNotificationClicked(Context context, String title, String description, String customContentString)`メソッドは、ユーザーが受信したプッシュメッセージをクリックするたびに呼び出されます。パラメーター`customContentString`には、JSON形式のエクストラが含まれています。Brazeからのすべてのメッセージには、次の2つのキーと値のペアが含まれます。

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Baiduレシーバーで`onNotificationClicked`が呼び出されるたびに、レシーバーは`customContentString`を含む[Intent](http://developer.android.com/reference/android/content/Intent.html)をアプリケーションに送信する必要があります。アプリケーションは`customContentString`を使用して、Brazeにクリックを記録します。

次のサンプルコードは、`customContentString`をBrazeに渡してクリックを記録します。

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## ステップ6:エクストラ {#step-6-extras}

Brazeが使用する予約キーとは別に、パラメーター`customContentString`にはユーザー定義のカスタムキーと値のペアもすべて含まれます。キーと値のペアを抽出するには、`customContentString`をJSONObjectでラップし、エクストラを取得します。

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## ステップ7：Baiduキーの設定 {#step-7-set-up-baidu-keys}

BrazeダッシュボードにBaidu APIキーとBaiduシークレットキーを入力する必要があります。両方のキーはBaiduアプリケーションコンソールから取得できます。

**設定の管理**ページで、Android Chinaアプリを選択し、プッシュ通知セクションにBaidu APIキーとBaiduシークレットキーを入力します。

![APIキー]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## その他のリソース {#additional-resources}

- [Baidu ポータル](https://www.baidu.com/)
- [Baidu 開発者ポータル](http://developer.baidu.com/)
- [Baidu プロジェクトポータル](http://developer.baidu.com/console#app/project)
- [Baidu プッシュ SDK ポータル](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Baidu 統合ドキュメント](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)