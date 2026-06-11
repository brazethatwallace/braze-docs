## Unity Braze SDKについて {#about-the-unity-braze-sdk}

型、関数、変数などの完全なリストについては、[Unity宣言ファイル](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)を参照してください。また、すでにUnityをiOS用に手動で統合している場合は、代わりに[自動統合に切り替える](#unity_automated-integration)ことができます。

## Unity SDKを統合する {#integrating-the-unity-sdk}

### 前提条件 {#prerequisites}

開始する前に、お使いの環境が[最新のBraze Unity SDKバージョン](https://github.com/braze-inc/braze-unity-sdk/releases)でサポートされていることを確認してください。

### ステップ1:Braze Unityパッケージを選択する {#step-1-choose-your-braze-unity-package}

{% tabs %}
{% tab Android %}
Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html)は、AndroidプラットフォームとiOSプラットフォーム向けのネイティブバインディングをC#インターフェイスとともにバンドルします。

[Braze Unityリリースページ](https://github.com/Appboy/appboy-unity-sdk/releases)でいくつかのBraze Unityパッケージをダウンロードできます。

- `Appboy.unitypackage`
    - このパッケージは、Braze AndroidおよびiOS SDKと、iOS SDKの[SDWebImage](https://github.com/SDWebImage/SDWebImage)依存関係をバンドルします。これは、Brazeアプリ内メッセージおよびiOS上のContent Cards機能を適切に機能させるために必要です。SDWebImageフレームワークは、GIFを含む画像のダウンロードと表示に使用されます。Brazeの完全な機能を使用する場合は、このパッケージをダウンロードしてインポートしてください。
- `Appboy-nodeps.unitypackage`
    - このパッケージは`Appboy.unitypackage`に似ていますが、[SDWebImage](https://github.com/SDWebImage/SDWebImage)フレームワークが含まれていない点が異なります。このパッケージは、iOSアプリにSDWebImageフレームワークを含めたくない場合に便利です。

{% alert note %}
Unity 2.6.0以降、バンドルされたBraze Android SDKアーティファクトには[AndroidX](https://developer.android.com/jetpack/androidx)依存関係が必要です。以前に`jetified` unitypackageを使用していた場合は、対応する`unitypackage`に安全に移行できます。

Androidビルドが「This project uses AndroidX dependencies, but the 'android.useAndroidX' property is not enabled」で失敗する場合は、UnityのPublishing Settingsで[Custom Gradle Properties Template](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing)を有効にしてください。次に`Assets/Plugins/Android/gradleTemplate.properties`を開き、`android.useAndroidX=true`を設定します。動作するテンプレートについては、[Braze Unityサンプルアプリ](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)とその[`gradleTemplate.properties`](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/gradleTemplate.properties)ファイルを参照してください。
{% endalert %}
{% endtab %}

{% tab Swift %}
Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html)は、AndroidプラットフォームとiOSプラットフォーム向けのネイティブバインディングをC#インターフェイスとともにバンドルします。

Braze Unityパッケージは、次の2種類の統合オプションを使用して、[Braze Unityリリースページ](https://github.com/Appboy/appboy-unity-sdk/releases)でダウンロードできます。

1. `Appboy.unitypackage`のみ
  - このパッケージは、Braze AndroidとiOS SDKを追加の依存関係なしでバンドルします。この統合方法では、Brazeアプリ内メッセージおよびiOS上のContent Cards機能が適切に機能しません。カスタムコードなしでBrazeの完全な機能を使用する場合は、代わりに以下のオプションを使用してください。
  - この統合オプションを使用する場合は、「Braze Configuration」の下にあるUnity UIで`Import SDWebImage dependency`の横にあるボックスに*チェックマークが入っていない*ことを確認してください。
2. `SDWebImage`を含む`Appboy.unitypackage`
  - この統合オプションは、Braze AndroidおよびiOS SDKと、iOS SDKの[SDWebImage](https://github.com/SDWebImage/SDWebImage)依存関係をバンドルします。これは、Brazeアプリ内メッセージおよびiOS上のContent Cards機能を適切に機能させるために必要です。`SDWebImage`フレームワークは、GIFを含む画像のダウンロードと表示に使用されます。Brazeの完全な機能を使用する場合は、このパッケージをダウンロードしてインポートしてください。
  - `SDWebImage`を自動的にインポートするには、「Braze Configuration」の下にあるUnity UIで`Import SDWebImage dependency`の横にあるボックスに*チェックマークが入っている*ことを確認してください。

{% alert note %}
iOSプロジェクトに[SDWebImage](https://github.com/SDWebImage/SDWebImage)依存関係が必要かどうかを確認するには、[iOSアプリ内メッセージドキュメント]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ2:パッケージをインポートする {#step-2-import-the-package}

{% tabs %}
{% tab Android %}
Unityエディターで、**Assets > Import Package > Custom Package**の順に移動して、Unityプロジェクトにパッケージをインポートします。次に、**Import**をクリックします。

または、カスタムUnityパッケージのインポートに関して詳しくは、[Unityアセットパッケージのインポート](https://docs.unity3d.com/Manual/AssetPackages.html)の説明を参照してください。

{% alert note %}
iOSまたはAndroidプラグインのみをインポートする場合は、Braze `.unitypackage`をインポートするときに`Plugins/Android`または`Plugins/iOS`サブディレクトリの選択を解除してください。
{% endalert %}
{% endtab %}

{% tab Swift %}
Unityエディターで、**Assets > Import Package > Custom Package**の順に移動して、Unityプロジェクトにパッケージをインポートします。次に、**Import**をクリックします。

または、カスタムUnityパッケージのインポートに関して詳しくは、[Unityアセットパッケージのインポート](https://docs.unity3d.com/Manual/AssetPackages.html)の説明を参照してください。

{% alert note %}
iOSまたはAndroidプラグインのみをインポートする場合は、Braze `.unitypackage`をインポートするときに`Plugins/Android`または`Plugins/iOS`サブディレクトリの選択を解除してください。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ3:SDKを設定する {#step-3-configure-the-sdk}

{% tabs %}
{% tab Android %}
#### ステップ3.1:`AndroidManifest.xml`を設定する {#step-31-configure-androidmanifestxml}

Braze SDKが機能するように[`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)を設定します。アプリに`AndroidManifest.xml`がない場合は、以下をテンプレートとして使用できます。すでに`AndroidManifest.xml`がある場合は、以下の不足しているセクションが既存の`AndroidManifest.xml`に追加されていることを確認してください。

1. `Assets/Plugins/Android/`ディレクトリに移動し、`AndroidManifest.xml`ファイルを開きます。これは[Unityエディターのデフォルトの場所](https://docs.unity3d.com/Manual/android-manifest.html)です。
2. `AndroidManifest.xml`に、以下のテンプレートにある必要な権限とアクティビティを追加します。
3. 完了後、`AndroidManifest.xml`には`"android.intent.category.LAUNCHER"`が存在するアクティビティが1つだけ含まれているはずです。

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:theme="@style/UnityThemeSelector"
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

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

{% alert important %}
`AndroidManifest.xml`ファイルに登録されているすべてのActivityクラスは、Braze Android SDKと完全に統合されている必要があります。そうでなければ分析が収集されません。独自のActivityクラスを追加する場合は、必ず[Braze Unityプレーヤーを拡張](#unity_extend-unity-player)して、これを防いでください。
{% endalert %}

#### ステップ3.2:`AndroidManifest.xml`をパッケージ名で更新する {#step-32-update-androidmanifestxml-with-your-package-name}

パッケージ名を確認するには、**File > Build Settings > Player Settings > Android Tab**を選択します。

![]({% image_buster /assets/img_archive/UnityPackageName.png %})

`AndroidManifest.xml`では、`REPLACE_WITH_YOUR_PACKAGE_NAME`のすべてのインスタンスを前のステップの`Package Name`に置き換える必要があります。

#### ステップ3.3:gradleの依存関係を追加する {#step-33-add-gradle-dependencies}

Unityプロジェクトにgradleの依存関係を追加するには、まず公開設定で[「Custom Main Gradle Template」](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing)を有効にします。これにより、プロジェクトで使用するテンプレートgradleファイルが作成されます。gradleファイルは、依存関係の設定やその他のビルド時のプロジェクト設定を処理します。詳細については、Braze Unityサンプルアプリの[mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle)を参照してください。

次の依存関係が必要です。

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

これらの依存関係は、[External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver)を使用して設定することもできます。

#### ステップ3.4:Unity Android統合を自動化する {#step-34-automate-the-unity-android-integration}

Brazeは、Unity Android統合を自動化するためのネイティブUnityソリューションを提供しています。

1. Unityエディターで**Braze > Braze Configuration**の順に移動して、Braze設定を開きます。
2. **Automate Unity Android Integration**ボックスにチェックマークを入れます。
3. **Braze API Key**フィールドに、Brazeダッシュボードの**設定の管理**にあるアプリケーションのAPIキーを入力します。

{% alert note %}
手動で作成した`braze.xml`ファイルでは、プロジェクトのビルド中に設定値が競合する可能性があるため、この自動統合は使用しないでください。手動の`braze.xml`が必要な場合は、自動統合を無効にしてください。
{% endalert %}
{% endtab %}

{% tab Swift %}
#### ステップ3.1:APIキーを設定する {#step-31-set-your-api-key}

Brazeは、Unity iOS統合を自動化するためのネイティブUnityソリューションを提供しています。このソリューションは、Unityの[`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html)を使用してビルドされたXcodeプロジェクトを変更し、`IMPL_APP_CONTROLLER_SUBCLASS`マクロを使用して`UnityAppController`をサブクラス化します。

1. Unityエディターで**Braze > Braze Configuration**の順に移動して、Braze設定を開きます。
2. **Automate Unity iOS Integration**ボックスにチェックマークを入れます。
3. **Braze API Key**フィールドに、**設定の管理**にあるアプリケーションのAPIキーを入力します。

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

アプリですでに別の`UnityAppController`サブクラスを使用している場合は、サブクラスの実装を`AppboyAppDelegate.mm`とマージする必要があります。
{% endtab %}
{% endtabs %}

## Unityパッケージをカスタマイズする {#customizing-the-unity-package}

### ステップ1:リポジトリを複製する {#step-1-clone-the-repository}

ターミナルで、[Braze Unity SDK GitHubリポジトリ](https://github.com/braze-inc/braze-unity-sdk)を複製し、そのフォルダーに移動します。

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### ステップ2:リポジトリからパッケージをエクスポートする {#step-2-export-package-from-repository}

まずUnityを起動し、バックグラウンドで実行しておきます。次に、リポジトリのルートで以下のコマンドを実行して、パッケージを`braze-unity-sdk/unity-package/`にエクスポートします。

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}
{% endtabs %}

{% alert tip %}
これらのコマンドを実行した後に問題が発生した場合は、[Unity: Command Line Arguments](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html)を参照してください。
{% endalert %}

### ステップ3:Unityにパッケージをインポートする {#step-3-import-package-into-unity}

1. Unityで、**Assets** > **Import Package** > **Custom Package**の順に移動して、目的のパッケージをUnityプロジェクトにインポートします。
2. インポートしたくないファイルがあれば、ここで選択を解除します。
3. `Assets/Editor/Build.cs`にあるエクスポートされたUnityパッケージをカスタマイズします。

## 自動統合に切り替える（Swiftのみ） {#automated-integration}

Braze Unity SDKで提供される自動化されたiOS統合を利用するには、手動から自動統合に移行するための以下のステップに従ってください。

1. Xcodeプロジェクトの`UnityAppController`サブクラスから、Braze関連のコードをすべて削除します。
2. UnityまたはXcodeプロジェクトからBraze iOSライブラリーを削除します（`Appboy_iOS_SDK.framework`や`SDWebImage.framework`など）。
3. Braze Unityパッケージをプロジェクトに再度インポートします。完全なウォークスルーは、[ステップ2:パッケージをインポートする](#unity_step-2-import-the-package)を参照してください。
4. APIキーを再度設定します。完全なウォークスルーは、[ステップ3.1:APIキーを設定する](#unity_step-31-set-your-api-key)を参照してください。

## オプション設定 {#optional-configurations}

### 詳細ログ {#verbose-logging}

Unityエディターで詳細ログを有効にするには、以下の手順を実行します。

1. **Braze** > **Braze Configuration**の順に移動して、Braze設定を開きます。
2. **Show Braze Android Settings**ドロップダウンをクリックします。
3. **SDK Log Level**フィールドに値「0」を入力します。

### Prime 31の互換性 {#prime-31-compatibility}

Prime31プラグインでBraze Unityプラグインを使用するには、Prime31互換のActivityクラスを使用するようにプロジェクトの`AndroidManifest.xml`を編集します。以下のすべての参照を
`com.braze.unity.BrazeUnityPlayerActivity`から`com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`に変更してください。

### Amazon Device Messaging (ADM)

Brazeは、Unityアプリへの[ADMプッシュ](https://developer.amazon.com/public/apis/engage/device-messaging)の統合をサポートしています。ADMプッシュを統合する場合は、ADM APIキーを含む`api_key.txt`というファイルを作成し、`Plugins/Android/assets/`フォルダーに配置してください。ADMとBrazeの統合の詳細については、[ADMプッシュ統合の説明]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity)を参照してください。

### Braze Unityプレーヤーの拡張（Androidのみ） {#extend-unity-player}

提供されている`AndroidManifest.xml`ファイルの例では、1つのActivityクラス[`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt)が登録されています。このクラスはBraze SDKと統合され、セッション処理、アプリ内メッセージ登録、プッシュ通知分析ログなどの機能で`UnityPlayerActivity`を拡張します。`UnityPlayerActivity`クラスの拡張の詳細については、[Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html)を参照してください。

ライブラリーやプラグインプロジェクトで独自のカスタム`UnityPlayerActivity`を作成する場合は、カスタム機能をBrazeと統合するために`BrazeUnityPlayerActivity`を拡張する必要があります。`BrazeUnityPlayerActivity`の拡張作業を始める前に、UnityプロジェクトにBrazeを統合するための手順に従ってください。

1. [Braze Android SDK統合の説明]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)に従って、Braze Android SDKをライブラリーまたはプラグインプロジェクトに依存関係として追加します。
2. Unity固有の機能を含むUnity `.aar`を、Unity用に構築しているAndroidライブラリープロジェクトに統合します。`appboy-unity.aar`は、[公開リポジトリ](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android)から入手できます。Unityライブラリーが正常に統合されたら、`BrazeUnityPlayerActivity`を拡張するように`UnityPlayerActivity`を変更します。
3. ライブラリーまたはプラグインプロジェクトをエクスポートし、通常どおり`/<your-project>/Assets/Plugins/Android`にドロップします。ライブラリーやプラグインにBrazeのソースコードを含めないでください。それらはすでに`/<your-project>/Assets/Plugins/Android`に存在しています。
4. `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml`を編集し、`BrazeUnityPlayerActivity`のサブクラスをメインアクティビティとして指定します。

これでUnity IDEから、Brazeと完全に統合され、カスタム`UnityPlayerActivity`機能を含む`.apk`をパッケージできるようになります。

## トラブルシューティング {#troubleshooting}

### エラー:「File could not be read」 {#error-file-could-not-be-read}

以下のようなエラーは無視して問題ありません。AppleのソフトウェアはCgBIと呼ばれる独自のPNG拡張を使用していますが、Unityはこれを認識しません。これらのエラーは、iOSのビルドやBrazeバンドル内の関連画像の適切な表示には影響しません。

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
