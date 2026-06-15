## .NET MAUI SDKの統合 {#integrating-the-net-maui-sdk}

Braze .NET MAUI（旧称Xamarin）SDKを統合すると、基本的な分析機能に加え、ユーザーとのエンゲージメントに活用できる機能的なアプリ内メッセージが利用可能になります。

### 前提条件 {#prerequisites}

.NET MAUI Braze SDKを統合する前に、以下の要件を満たしていることを確認してください。

- `version 3.0.0` 以降、このSDKでは.NET 6以降を使用する必要があり、Xamarinフレームワークを使用するプロジェクトのサポートは削除されています。
- `version 4.0.0` 以降、このSDKはXamarin & Xamarin.Formsのサポートを終了し、.NET MAUIのサポートを追加しました。Xamarinのサポート終了に関する[Microsoftのポリシー](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)を参照してください。

### ステップ1: .NET MAUIバインディングを入手する {#step-1-get-the-net-maui-binding}

{% tabs %}
{% tab android %}
.NET MAUIバインディングとは、.NET MAUIアプリでネイティブライブラリーを利用する方法です。バインディングの実装は、ライブラリーに対してC#インターフェイスを構築し、アプリケーションでそのインターフェイスを使用することから構成されます。[.NET MAUIのドキュメント](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/)を参照してください。Braze SDKバインディングを含めるには、NuGetを使用する方法と、ソースからコンパイルする方法の2つがあります。

{% subtabs local %}
{% subtab NuGet %}
最も簡単な統合方法は、[NuGet.org](https://www.nuget.org/)中央リポジトリーからBraze SDKを取得することです。Visual Studioサイドバーで`Packages`フォルダを右クリックし、`Add Packages...`をクリックします。「Braze」を検索し、[`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/)パッケージをプロジェクトにインストールします。

Brazeの位置情報サービスとジオフェンスを使用するには、[`BrazePlatform.BrazeAndroidLocationBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidLocationBinding/)パッケージもインストールしてください。
{% endsubtab %}

{% subtab Source %}
2番目の統合方法は、[バインディングソース](https://github.com/braze-inc/braze-xamarin-sdk)を含めることです。[`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding)にバインディングのソースコードがあります。.NET MAUIアプリケーションで`BrazeAndroidBinding.csproj`へのプロジェクト参照を追加すると、バインディングがプロジェクトと共にビルドされ、Braze Android SDKを利用できるようになります。

Brazeの位置情報サービスとジオフェンスを使用するには、[`appboy-component/src/androidnet6/BrazeAndroidLocationBinding`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidLocationBinding)にある`BrazeAndroidLocationBinding.csproj`へのプロジェクト参照も追加してください。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
.NET MAUI SDKバージョン4.0.0以降のiOSバインディングは[Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/)を使用しています。それ以前のバージョンでは[従来のAppboyKit SDK](https://github.com/Appboy/Appboy-ios-sdk)を使用しています。
{% endalert %}

.NET MAUIバインディングとは、.NET MAUIアプリでネイティブライブラリーを利用する方法です。バインディングの実装は、ライブラリーに対してC#インターフェイスを構築し、アプリケーションでそのインターフェイスを使用することから構成されます。Braze SDKバインディングを含めるには、NuGetを使用する方法と、ソースからコンパイルする方法の2つがあります。

{% subtabs local %}
{% subtab NuGet %}
最も簡単な統合方法は、[NuGet.org](https://www.nuget.org/)中央リポジトリーからBraze SDKを取得することです。Visual Studioサイドバーで`Packages`フォルダを右クリックし、`Add Packages...`をクリックします。「Braze」を検索し、最新の.NET MAUI iOS NuGetパッケージである[Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)、[Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)、および[Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)をプロジェクトにインストールします。

.NET MAUIへの移行を容易にするために、互換性ライブラリーパッケージ[Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)および[Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)も提供しています。
{% endsubtab %}

{% subtab Source %}
2番目の統合方法は、[バインディングソース](https://github.com/braze-inc/braze-xamarin-sdk)を含めることです。[`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding)にバインディングのソースコードがあります。.NET MAUIアプリケーションで`BrazeiOSBinding.csproj`へのプロジェクト参照を追加すると、バインディングがプロジェクトと共にビルドされ、Braze iOS SDKを利用できるようになります。プロジェクトの「Reference」フォルダに`BrazeiOSBinding.csproj`が表示されていることを確認してください。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ2: Brazeインスタンスを設定する {#step-2-configure-your-braze-instance}

{% tabs %}
{% tab android %}
#### ステップ2.1: Braze.xmlでBraze SDKを設定する {#step-21-configure-the-braze-sdk-in-brazexml}

ライブラリーが統合されたので、プロジェクトの`Resources/values`フォルダに`Braze.xml`ファイルを作成する必要があります。ファイルの内容は、次のコードスニペットのようになります。

{% alert note %}
`YOUR_API_KEY`を、Brazeダッシュボードの**Settings** > **API Keys**にあるAPIキーに必ず置き換えてください。
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
バインディングソースを手動で含める場合は、コードから`<item>NUGET</item>`を削除してください。

{% alert tip %}
`Braze.xml`の例については、[Android MAUIサンプルアプリ](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml)を参照してください。
{% endalert %}

#### ステップ2.2: Androidマニフェストに必要な権限を追加する {#step-22-add-required-permissions-to-android-manifest}

APIキーを追加したので、次の権限を`AndroidManifest.xml`ファイルに追加する必要があります。

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
`AndroidManifest.xml`の例については、[Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml)サンプルアプリケーションを参照してください。

#### ステップ2.3: ユーザーセッションのトラッキングとアプリ内メッセージの登録 {#step-23-track-user-sessions-and-registering-for-in-app-messages}

ユーザーセッショントラッキングを有効にし、アプリ内メッセージ用にアプリを登録するには、アプリの`Application`クラスの`OnCreate()`ライフサイクルメソッドに次の呼び出しを追加します。

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Brazeインスタンスを設定する際に、次のスニペットを追加してインスタンスを設定します。

{% alert note %}
`YOUR_API_KEY`を、Brazeダッシュボードの**Settings** > **API Keys**にあるAPIキーに必ず置き換えてください。
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs)サンプルアプリケーションの`App.xaml.cs`ファイルを参照してください。
{% endtab %}
{% endtabs %}

### ステップ3: 統合をテストする {#step-3-test-the-integration}

{% tabs %}
{% tab android %}
これで、アプリケーションを起動して、セッションがBrazeダッシュボードに（デバイス情報やその他の分析と共に）記録されていることを確認できます。基本的なSDK統合のベストプラクティスの詳細については、[Android統合の手順]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を参照してください。
{% endtab %}

{% tab ios %}
これで、アプリケーションを起動して、セッションがBrazeダッシュボードに記録されていることを確認できます。基本的なSDK統合のベストプラクティスの詳細については、[iOS統合の手順]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift)を参照してください。

{% alert important %}
現在公開中のiOS SDK向け.NET MAUIバインディングは、iOS Facebook SDK（ソーシャルデータの連携）には接続せず、またBrazeへのIDFA送信機能も含まれていません。
{% endalert %}
{% endtab %}
{% endtabs %}