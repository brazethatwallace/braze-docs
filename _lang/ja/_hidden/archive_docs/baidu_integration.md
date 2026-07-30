---
nav_title: Baidu の統合
article_title: Android 向け Baidu プッシュ通知の統合
platform: Android
permalink: /baidu_integration/
description: "この記事では、Baidu Android 統合の設定方法について説明します。"
hidden: true
---
# Baidu の統合 {#baidu-integration}
{% alert warning %}
Brazeの Baidu プッシュ統合は、2022年3月24日をもって非推奨となりました。

* **2022年3月24日:** Brazeダッシュボードで新しい Baidu アプリを作成できなくなりました。
* **2022年9月15日:** 新しい Baidu プッシュメッセージを作成できなくなりました。既存のメッセージとデータ収集には影響ありません。
* **2023年1月15日:** Brazeは Baidu アプリからのメッセージ配信およびデータ収集を終了しました。
{% endalert %}

Brazeは、[Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}) を使用して Android デバイスにプッシュ通知を送信できます。Baidu Cloud Push を使用する場合、Baidu アプリストアを介してアプリを配布する必要はありません。

## ステップ1:Baidu のアカウントを作成する {#step-1-create-a-baidu-account}

Baidu アカウントを作成するには、[Baidu ポータル](https://www.baidu.com/)にアクセスし、**登录**（ログイン）をクリックすると、ログインまたは新しいアカウントを作成するためのダイアログが表示されます。

![]({% image_buster /assets/img_archive/baidu_portal.png %})

新しいアカウントを作成するには、ログインダイアログの一番下にある**立即注册**（新しいアカウント）をクリックします。

![]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

アカウント作成ページにユーザー名、電話番号、パスワードを入力します。次に、確認コードの受信ボタンをクリックします。Baidu から認証コードを含む SMS メッセージが届きます。最後に、使用許諾契約に同意し、**注册**（アカウントの作成）をクリックして登録します。これらの設定手順に失敗した場合は、この[ログイン記事](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/)で説明されているように、Baidu Cloud ログイン経由での登録を試してください。

![Baidu サインアップページ]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## ステップ2:Baidu の開発者として登録する {#step-2-register-as-a-baidu-developer}

次に、Baidu の開発者として登録する必要があります。まず、[Baidu 開発者ポータル](http://developer.baidu.com/)にアクセスし、**注册**（新しい開発者アカウントを作成）を選択して登録を開始します。

![]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

登録ページで、アカウントの種類（個人用には「个人」、ビジネス用には「公司」）と開発者の種類を選択します（開発者があらかじめ選択されており、ほとんどの場合正しい設定です）。氏名、略歴、電話番号（カッコ内に国番号を含む）を入力します（例：(1)xxxxxxxxxx）。**发送验证码**（確認コードを送信）をクリックし、次の行に確認コードを入力します。次の2つのフィールド（開発者のWebサイトと開発者のロゴ）は任意です。使用許諾契約に同意し、**提交**（送信）をクリックして送信します。これで Baidu の開発者アカウントが作成されました。

![]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## ステップ3:Baidu にアプリケーションを登録する {#step-3-register-your-application-with-baidu}

Baidu にアプリケーションを登録するには、[Baidu プロジェクトポータル](http://developer.baidu.com/console#app/project)にアクセスし、**创建工程**（プロジェクトの作成）をクリックします。

![]({% image_buster /assets/img_archive/baidu_project.png %})

次のページで、アプリケーション名を入力します。次の2つのチェックボックスは、Baidu の追加サービスを有効にするためのものです。ほとんどの場合、これらは空白のままにしてください。

![]({% image_buster /assets/img_archive/baidu_app_name.png %})

アプリケーションをセットアップすると、APIキーを含むアプリケーションに関する情報を表示するコンソールが表示されます。次に、サイドバーの**云推送**（クラウドプッシュ）に移動します。次のページで、**推送设置**（プッシュを設定する）をクリックします。

![]({% image_buster /assets/img_archive/baidu_app_console.png %})

![]({% image_buster /assets/img_archive/baidu_continue.png %})

次のページで、アプリのパッケージ名（例：`com.braze.sample`）を入力し、メッセージをキャッシュするかどうか、キャッシュする場合はその期間（時間単位）を指定します。これは、Baidu に対して、オフラインユーザーにメッセージの送信を試行し続ける時間を示します。**保存设置**（設定を保存する）をクリックして保存します。

![]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## ステップ4:アプリケーションに Baidu を追加する {#step-4-add-baidu-to-your-application}

[Baidu プッシュSDKポータル](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)にアクセスし、最新の Baidu Cloud Push Android SDKをダウンロードします。

![]({% image_buster /assets/img_archive/baidu_sdk.png %})

SDKの中には、プッシュサービスの jar とプラットフォーム固有のネイティブライブラリがあります。これらをプロジェクトに組み込みます。アプリが現在 Baidu でサポートされている最新のSDKバージョンを対象にしていることを確認してください。このドキュメントは、Baidu Cloud push Android SDKバージョン`4.6.2.38`を対象としています。

以下の必要な Baidu パーミッションをアプリケーションの`AndroidManifest.xml`に追加します。

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

Baidu のライブラリには、受信したプッシュメッセージを処理するブロードキャストレシーバーが含まれています。アプリケーションの`AndroidManifest.xml`内の`<application>`要素内で内部 Baidu レシーバーを宣言します。

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

また、プッシュメッセージや通知の着信をリッスンするブロードキャストレシーバーも作成する必要があります。アプリケーションの`AndroidManifest.xml`の`<application>`要素内でレシーバーを宣言します。このレシーバーは、`com.baidu.android.pushservice.PushMessageReceiver`を拡張し、Baidu プッシュサービスからイベント更新を受け取るメソッドを実装する必要があります。

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

メインアクティビティの`onCreate()`メソッドに次の行を追加します。これにより、アプリケーションが Baidu に登録され、着信プッシュメッセージのリッスンが開始されます。「Your-API-Key」をプロジェクトの Baidu APIキーに置き換えてください。

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

最後に、ユーザーをBrazeに登録する必要があります。このステップで作成した Baidu ブロードキャストレシーバーの`onBind()`メソッドで、`Braze.registerAppboyPushMessages(channelId)`を使用して`channelId`をBrazeに送信します。

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

## ステップ5:プッシュ開封を登録する {#step-5-registering-push-opens}

Baidu は、JSON 形式のプッシュメッセージで追加のキーと値のペアの送信をサポートしています。ブロードキャストレシーバーの`public void onNotificationClicked(Context context, String title, String description, String customContentString)`メソッドは、ユーザーが着信プッシュメッセージをクリックするたびに呼び出されます。パラメーター`customContentString`には、JSON 形式のエクストラが含まれます。Brazeからのすべてのメッセージには、以下の2つのキーと値のペアが含まれます。

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

`onNotificationClicked`が Baidu レシーバーに呼び出されるたびに、レシーバーは`customContentString`を含む [Intent](http://developer.android.com/reference/android/content/Intent.html) をアプリケーションに送信する必要があります。アプリケーションは、`customContentString`を使用してBrazeにクリックを記録します。

次のサンプルコードは、`customContentString`をBrazeに渡し、クリックを記録します。

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

Brazeが使用する予約キー以外に、`customContentString`パラメーターには、ユーザー定義のカスタムのキーと値のペアがすべて含まれています。キーと値のペアを抽出するには、`customContentString`を JSONObject でラップし、エクストラを取得します。

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

## ステップ7:Baidu キーを設定する {#step-7-set-up-baidu-keys}

Brazeダッシュボードに Baidu APIキーと Baidu シークレットキーを入力する必要があります。どちらのキーも Baidu のアプリケーションコンソールから取得できます。

**設定の管理**ページで、Android China アプリを選択し、プッシュ通知セクションに Baidu APIキーと Baidu シークレットキーを入力します。

![]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## その他のリソース {#additional-resources}

- [Baidu ポータル](https://www.baidu.com/)
- [Baidu 開発者ポータル](http://developer.baidu.com/)
- [Baidu プロジェクトポータル](http://developer.baidu.com/console#app/project)
- [Baidu プッシュSDKポータル](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Baidu 統合ドキュメント](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)