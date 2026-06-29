## Android SDKの統合 {#integrating-the-android-sdk}

### ステップ1: Gradleのビルド設定を更新する {#step-1-update-your-gradle-build-configuration}

プロジェクトのリポジトリ設定（例：`settings.gradle`、`settings.gradle.kts`、または最上位の`build.gradle`）で、リポジトリ一覧に[`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html)を追加します。この構文はGroovyとKotlin DSLの両方で同じです。

```groovy
repositories {
  mavenCentral()
}
```

次に、依存関係にBrazeを追加します。以下の例では、`SDK_VERSION`を現在のAndroid Braze SDKのバージョンに置き換えてください。全バージョンのリストについては、[変更ログ]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android)を参照してください。

{% alert note %}
- Kotlin DSL（`build.gradle.kts`）では、`implementation("...")`構文を使用します。
- Groovy（`build.gradle`）では、`implementation '...'`構文を使用します。
- [バージョンカタログ](https://developer.android.com/build/migrate-to-catalogs)の場合は、`gradle/libs.versions.toml`ファイルにエントリを追加し、生成されたアクセサを使用して参照します。
{% endalert %}

{% tabs local %}
{% tab base only %}
Braze UIコンポーネントを使用する予定がない場合は、依存関係に以下を追加します。

{% subtabs local %}
{% subtab Groovy %}
`````````groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
`````````kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
`gradle/libs.versions.toml`ファイルに以下を追加します：

`````````toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

次に、`build.gradle`または`build.gradle.kts`ファイルに以下の依存関係を追加します。この構文はGroovyとKotlin DSLの両方で同じです。

`````````groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Braze UIコンポーネントを使用する予定がある場合は、依存関係に以下を追加します。

{% subtabs local %}
{% subtab Groovy %}
`````````groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
`````````kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
`gradle/libs.versions.toml`ファイルに以下を追加します：

`````````toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

次に、`build.gradle`または`build.gradle.kts`ファイルに以下の依存関係を追加します。この構文はGroovyとKotlin DSLの両方で同じです。

`````````groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ2: `braze.xml`を設定する {#step-2-configure-your-brazexml}

{% alert note %}
2019年12月をもって、カスタムエンドポイントは提供されなくなりました。既存のカスタムエンドポイントがある場合は、引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a> を参照してください。
{% endalert %}

プロジェクトの`res/values`フォルダ内に`braze.xml`ファイルを作成します。特定のデータクラスターを使用している場合、または既存のカスタムエンドポイントがある場合は、`braze.xml`ファイルでもエンドポイントを指定する必要があります。

ファイルの内容は、次のコードスニペットのようになります。`YOUR_APP_IDENTIFIER_API_KEY`をBrazeダッシュボードの**設定の管理**ページにある識別子に置き換えてください。[dashboard.braze.com](https://dashboard.braze.com)にログインして、[クラスターアドレス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)を確認してください。

`````````xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### ステップ3: `AndroidManifest.xml`に権限を追加する {#step-3-add-permissions-to-androidmanifestxml}

次に、`AndroidManifest.xml`に以下の権限を追加します：

`````````xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android Mのリリースにより、Androidはインストール時の権限モデルからランタイム権限モデルに切り替わりました。ただし、これらの権限はどちらも通常の権限であり、アプリのマニフェストにリストされている場合は自動的に付与されます。詳細については、Androidの[権限に関するドキュメント](https://developer.android.com/training/permissions/index.html)を参照してください。
{% endalert %}

### ステップ4: 遅延初期化を有効にする（オプション） {#step-4-enable-delayed-initialization-optional}

遅延初期化を使用するには、以下の最低限のBraze SDKバージョンが必要です：

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
遅延初期化が有効な間は、すべてのネットワーク接続がキャンセルされ、SDKがBrazeサーバーにデータを送信できなくなります。
{% endalert %}

#### ステップ4.1: `braze.xml`を更新する {#step-41-update-your-brazexml}

遅延初期化はデフォルトで無効になっています。有効にするには、次のいずれかのオプションを使用します：

{% tabs %}
{% tab Braze XML file %}
プロジェクトの`braze.xml`ファイルで、`com_braze_enable_delayed_initialization`を`true`に設定します。

`````````xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
実行時に遅延初期化を有効にするには、以下のメソッドを使用します。

{% subtabs %}
{% subtab JAVA %}

`````````java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

`````````kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
遅延初期化が有効な場合、プッシュ通知にディープリンクアクションが含まれていても、そのディープリンクは解決されません。
{% endalert %}

#### ステップ4.2: プッシュ分析を設定する（オプション） {#step-42-configure-push-analytics-optional}

遅延初期化が有効な場合、プッシュ分析はデフォルトでキューに格納されます。ただし、プッシュ分析を[明示的にキューに入れる](#explicitly-queue-push-analytics)か、[破棄する](#drop-push-analytics)かを選択することもできます。

##### 明示的にキューに入れる {#explicitly-queue-push-analytics}

プッシュ分析を明示的にキューに入れるには、次のいずれかのオプションを選択します：

{% tabs %}
{% tab Braze XML file %}
`braze.xml`ファイルで、`com_braze_delayed_initialization_analytics_behavior`を`QUEUE`に設定します：

`````````xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
[`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)メソッドに`QUEUE`を追加します：

{% subtabs %}
{% subtab JAVA %}

`````````java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

`````````kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### 破棄する {#drop-push-analytics}

プッシュ分析を破棄するには、次のいずれかのオプションを選択します：

{% tabs %}
{% tab Braze XML file %}
`braze.xml`ファイルで、`com_braze_delayed_initialization_analytics_behavior`を`DROP`に設定します：

`````````xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
[`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)メソッドに`DROP`を追加します：

{% subtabs %}
{% subtab JAVA %}

`````````java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

`````````kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### ステップ4.3: SDKを手動で初期化する {#step-43-manually-initialize-the-sdk}

選択した遅延期間の後、[`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html)メソッドを使用してSDKを手動で初期化します。

{% tabs local %}
{% tab JAVA %}

`````````java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### ステップ5: ユーザーセッショントラッキングを有効にする {#step-5-enable-user-session-tracking}

ユーザーセッショントラッキングを有効にすると、`openSession()`、`closeSession()`、[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)、および`InAppMessageManager`の登録呼び出しが自動的に処理されます。

アクティビティのライフサイクルコールバックを登録するには、`Application`クラスの`onCreate()`メソッドに以下のコードを追加します。

{% tabs local %}
{% tab JAVA %}

`````````java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

利用可能なパラメータの一覧については、[`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)を参照してください。

{% endtab %}
{% endtabs %}

## セッショントラッキングのテスト {#testing-session-tracking}

{% alert tip %}
SDKの問題を診断するには、[SDKデバッガー]({{site.baseurl}}/developer_guide/debugging/)も利用できます。
{% endalert %}

テスト中に問題が発生した場合は、[詳細ログ](#android_enabling-logs)を有効にし、logcatを使用してアクティビティ内で欠落している`openSession`および`closeSession`呼び出しを検出してください。

1. Brazeで**Overview**に移動し、アプリを選択します。次に**Display Data For**ドロップダウンから**Today**を選択します。
    ![Brazeの「Overview」ページで、「Display Data For」フィールドが「Today」に設定されている状態。]({% image_buster /assets/img_archive/android_sessions.png %})
2. アプリを開き、Brazeダッシュボードを更新します。指標が1増加したことを確認してください。
3. アプリ内を操作し、Brazeに記録されたセッションが1つだけであることを確認します。
4. アプリをバックグラウンドに少なくとも10秒間送ってから、フォアグラウンドに戻します。新しいセッションが記録されたことを確認してください。

## オプション設定 {#optional-configurations}

### ランタイム設定 {#runtime-configuration}

Brazeのオプションを`braze.xml`ファイルではなくコード内で設定するには、[ランタイム設定](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)を使用します。両方の場所に値が存在する場合、ランタイムの値が使用されます。必要な設定をすべてランタイムで指定したら、`braze.xml`ファイルを削除できます。

次の例では、[ビルダーオブジェクト](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)が作成され、[`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)に渡されます。利用可能なランタイムオプションの一部のみが表示されていることに注意してください&#8212;完全なリストについては[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)を参照してください。

{% tabs %}
{% tab JAVA %}

`````````java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
別の例をお探しですか？[Hello Brazeサンプルアプリ](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java)をご覧ください。
{% endalert %}

### Google広告ID {#google-advertising-id}

[Google広告ID（GAID）](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en)は、Google Playサービスが提供する、広告向けのオプションのユーザー固有の匿名で一意かつリセット可能なIDです。GAIDにより、ユーザーは自分の識別子をリセットし、Google Playアプリ内の興味・関心に基づく広告をオプトアウトできます。また、開発者はアプリの収益化を継続するためのシンプルな標準システムを利用できます。

Google広告IDはBraze SDKによって自動的に収集されないため、[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html)メソッドを使用して手動で設定する必要があります。

{% tabs local %}
{% tab JAVA %}

`````````java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Googleでは、広告IDを非UIスレッドで収集する必要があります。
{% endalert %}


### 位置情報の追跡 {#location-tracking}

Brazeの位置情報収集を有効にするには、`braze.xml`ファイルで`com_braze_enable_location_collection`を`true`に設定します：

`````````xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDKバージョン3.6.0以降、Brazeの位置情報収集はデフォルトで無効になっています。
{% endalert %}

### ロギング {#logging}

デフォルトでは、Braze Android SDKのログレベルは`INFO`に設定されています。[これらのログを抑制](#android_suppressing-logs)したり、`VERBOSE`、`DEBUG`、`WARN`などの[別のログレベルを設定](#android_enabling-logs)したりすることができます。

#### ログを有効にする {#enabling-logs}

アプリの問題をトラブルシューティングしたり、Brazeサポートの対応時間を短縮したりするために、SDKの詳細ログを有効にできます。Brazeサポートに詳細ログを送信する場合は、アプリケーションを起動したらすぐにログを開始し、問題が発生してからしばらく後にログを終了するようにしてください。集中管理された概要については、[詳細ログ]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/)を参照してください。ログ出力の解釈方法については、[詳細ログの読み方]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs/)を参照してください。

詳細ログは開発環境のみを対象としているため、アプリをリリースする前に無効にする必要があります。

{% alert important %}
`Application.onCreate()`で他の呼び出しを行う前に詳細ログを有効にして、ログが可能な限り完全になるようにしてください。
{% endalert %}

{% tabs local %}
{% tab Application %}
アプリで直接ログを有効にするには、他のメソッドの前に、以下をアプリケーションの`onCreate()`メソッドに追加します。

{% subtabs local %}
{% subtab JAVA %}
`````````java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
`````````kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

`MIN_LOG_LEVEL`を、最小ログレベルとして設定するログレベルの**定数**に置き換えます。設定した`MIN_LOG_LEVEL`以上（`>=`）のレベルのログはすべて、Androidのデフォルトの[`Log`](https://developer.android.com/reference/android/util/Log)メソッドに転送されます。設定した`MIN_LOG_LEVEL`未満（`<`）のすべてのログは破棄されます。

| 定数 | 値 | 説明 |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | デバッグや開発のために最も詳細なメッセージをログに記録します。            |
| `DEBUG`     | 3              | デバッグや開発のために説明的なメッセージをログに記録します。                  |
| `INFO`      | 4              | 一般的なハイライトのための情報メッセージを記録します。                       |
| `WARN`      | 5              | 潜在的に有害な状況を特定するための警告メッセージをログに記録します。     |
| `ERROR`     | 6              | アプリケーションの失敗や深刻な問題を示すエラーメッセージを記録します。 |
| `ASSERT`    | 7              | 開発中に条件が偽の場合にアサーションメッセージをログに記録します。     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Enabling logs" }

たとえば、以下のコードはログレベル`2`、`3`、`4`、`5`、`6`、`7`を`Log`メソッドに転送します。

{% subtabs local %}
{% subtab JAVA %}
`````````java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
`````````kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
`braze.xml`でログを有効にするには、ファイルに以下を追加します：

`````````xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

`MIN_LOG_LEVEL`を、最小ログレベルとして設定するログレベルの**値**に置き換えます。設定した`MIN_LOG_LEVEL`以上（`>=`）のレベルのログはすべて、Androidのデフォルトの[`Log`](https://developer.android.com/reference/android/util/Log)メソッドに転送されます。設定した`MIN_LOG_LEVEL`未満（`<`）のすべてのログは破棄されます。

| 定数 | 値 | 説明 |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | デバッグや開発のために最も詳細なメッセージをログに記録します。            |
| `DEBUG`     | 3              | デバッグや開発のために説明的なメッセージをログに記録します。                  |
| `INFO`      | 4              | 一般的なハイライトのための情報メッセージを記録します。                       |
| `WARN`      | 5              | 潜在的に有害な状況を特定するための警告メッセージをログに記録します。     |
| `ERROR`     | 6              | アプリケーションの失敗や深刻な問題を示すエラーメッセージを記録します。 |
| `ASSERT`    | 7              | 開発中に条件が偽の場合にアサーションメッセージをログに記録します。     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Enabling logs" }

たとえば、以下のコードはログレベル`2`、`3`、`4`、`5`、`6`、`7`を`Log`メソッドに転送します。

`````````xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### 詳細ログを検証する {#verifying-verbose-logs}

ログが`VERBOSE`に設定されていることを確認するには、ログのどこかに`V/Braze`が出現するかどうかを確認します。出現していれば、詳細ログは正常に有効になっています。以下に例を示します：

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### ログを抑制する {#suppressing-logs}

Braze Android SDKのすべてのログを抑制するには、アプリケーションの`onCreate()`メソッドで、他のメソッドの_前に_ログレベルを`BrazeLogger.SUPPRESS`に設定します。

{% tabs local %}
{% tab JAVA %}
`````````java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
`````````kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### 複数のAPIキー {#multiple-api-keys}

複数のAPIキーの最も一般的なユースケースは、デバッグおよびリリースビルドバリアントのAPIキーを分離することです。

ビルド内の複数のAPIキーを簡単に切り替えられるように、関連する[ビルドバリアント](https://developer.android.com/studio/build/build-variants.html)ごとに個別の`braze.xml`ファイルを作成することをお勧めします。ビルドバリアントは、ビルドタイプと製品フレーバーの組み合わせです。デフォルトでは、新しいAndroidプロジェクトは[`debug`と`release`のビルドタイプ](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType)で構成され、製品フレーバーは設定されていません。

関連する各ビルドバリアントについて、`src/<build variant name>/res/values/`ディレクトリ内に新しい`braze.xml`を作成します。ビルドバリアントがコンパイルされると、新しいAPIキーが使用されます。

`````````xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
コード内でAPIキーを設定する方法については、[ランタイム設定]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)を参照してください。
{% endalert %}

### アプリ内メッセージの排他的TalkBack {#exclusive-in-app-message-talkback}

[Androidアクセシビリティガイドライン](https://developer.android.com/guide/topics/ui/accessibility)に準拠し、Braze Android SDKはデフォルトでAndroid TalkBackを提供します。アプリ内メッセージの内容のみを読み上げさせ、アプリタイトルバーやナビゲーションなどの他の画面要素を含めないようにするには、TalkBackの排他モードを有効にできます。

アプリ内メッセージの排他モードを有効にするには：

{% tabs local %}
{% tab Braze XML %}
`````````xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
`````````kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
`````````java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8とProGuard {#r8-and-proguard}

[コード圧縮](https://developer.android.com/build/shrink-code)設定は、Braze統合に自動的に含まれます。

Brazeコードを難読化するクライアントアプリでは、Brazeがスタックトレースを解釈するためのリリースマッピングファイルを保存する必要があります。すべてのBrazeコードを引き続き保持する場合は、ProGuardファイルに以下を追加します：

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
