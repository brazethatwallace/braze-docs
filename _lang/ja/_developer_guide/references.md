---
nav_title: リファレンスとサンプルアプリ
article_title: Braze SDK リファレンス、リポジトリ、サンプルアプリ
page_order: 5.5
description: "各 Braze SDKに属するリファレンスドキュメント、GitHubリポジトリ、サンプルアプリの一覧です。"
toc_headers: h2
---

# リファレンス、リポジトリ、サンプルアプリ {#references-repositories-and-sample-apps}

> これは、各 Braze SDKに属するリファレンスドキュメント、GitHubリポジトリ、サンプルアプリの一覧です。SDKのリファレンスドキュメントには、使用可能なクラス、型、関数、変数の詳細が記載されています。GitHubリポジトリは、SDKの関数や属性の宣言、コードの変更、バージョン管理に関するインサイトを提供します。各リポジトリには、Brazeの機能をテストしたり、独自のアプリケーションと併せて実装するために使用できる、完全にビルド可能なサンプルアプリケーションも含まれています。

ドキュメント内のミラーリングされたリポジトリREADMEコンテンツについては、[リポジトリガイド]({{site.baseurl}}/developer_guide/sdk_repository_guides/)を参照してください。

## リソース一覧 {#list-of-resources}

{% alert note %}
現在、一部のSDKには専用のリファレンスドキュメントがありませんが、積極的に作成に取り組んでいます。
{% endalert %}

| プラットフォーム | リファレンス | リポジトリ | サンプルアプリ |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK | [リファレンスドキュメント](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html) | [GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-android-sdk/tree/master/samples) |
| Swift SDK | [リファレンスドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze) | [GitHubリポジトリ](https://github.com/braze-inc/braze-swift-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples) |
| Web SDK | [リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) | [GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds) |
| Javascript SDK | [リファレンスドキュメント](https://braze-inc.github.io/braze-javascript-sdk/) | [GitHubリポジトリ](https://github.com/braze-inc/braze-javascript-sdk/tree/main) | N/A |
| Cordova SDK | [宣言ファイル](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js) | [GitHubリポジトリ](https://github.com/braze-inc/braze-cordova-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project) |
| Flutter SDK | [リファレンスドキュメント](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/) | [GitHubリポジトリ](https://github.com/braze-inc/braze-flutter-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example) |
| React Native SDK | [リファレンスドキュメント](https://braze-inc.github.io/braze-react-native-sdk/) | [GitHubリポジトリ](https://github.com/braze-inc/braze-react-native-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Vega SDK | [リファレンスドキュメント](https://braze-inc.github.io/braze-vega-sdk/) | [GitHubリポジトリ](https://github.com/braze-inc/braze-vega-sdk) | N/A |
| Roku SDK | N/A | [GitHubリポジトリ](https://github.com/braze-inc/braze-roku-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv) |
| Unity SDK | [宣言ファイル](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs) | [GitHubリポジトリ](https://github.com/braze-inc/braze-unity-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples) |
| .NET MAUI SDK（旧称 Xamarin） | N/A | [GitHubリポジトリ](https://github.com/braze-inc/braze-xamarin-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リソース一覧" }

## サンプルアプリのビルド {#building-a-sample-app}

{% tabs %}
{% tab android %}
### 「Droidboy」のビルド {#building-droidboy}

[Android SDK GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk)内のテストアプリケーションはDroidboyと呼ばれます。以下の手順に従って、プロジェクトとともに完全に機能するDroidboyのコピーをビルドしてください。

1. 新しい[ワークスペース]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration)を作成し、Braze API識別子キーを書き留めます。<br><br>
2. FCM送信者IDとBraze API識別子キーを `/droidboy/res/values/braze.xml` 内の適切な場所（それぞれ `com_braze_push_fcm_sender_id` と `com_braze_api_key` という文字列のタグの間）にコピーします。<br><br>
3. FCMサーバーキーとサーバーIDを**設定の管理**のワークスペース設定にコピーします。<br><br>
4. Droidboy APKをアセンブルするには、SDKディレクトリ内で `./gradlew assemble` を実行します。Windowsでは `gradlew.bat` を使用してください。<br><br>
5. Droidboy APKをテストデバイスに自動的にインストールするには、SDKディレクトリ内で `./gradlew installDebug` を実行します。

### 「Hello Braze」のビルド {#building-hello-braze}

Hello Brazeテストアプリケーションは、Braze SDKの最小限のユースケースを示すとともに、Braze SDKをGradleプロジェクトに簡単に統合する方法も示します。

1. **設定の管理**ページのAPI識別子キーを `res/values` フォルダーの `braze.xml` ファイルにコピーします。
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. サンプルアプリをデバイスまたはエミュレーターにインストールするには、SDKディレクトリ内で次のコマンドを実行します。
```
./gradlew installDebug
```
`ANDROID_HOME` 変数が適切に設定されていない場合、または有効な `sdk.dir` フォルダーを含む `local.properties` フォルダーがない場合、このプラグインはベースSDKもインストールします。詳細については、[プラグインリポジトリ](https://github.com/JakeWharton/sdk-manager-plugin)を参照してください。

Android SDKビルドシステムの詳細については、[GitHubリポジトリのREADME](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md)を参照してください。
{% endtab %}

{% tab swift %}
### Swiftテストアプリのビルド {#building-swift-test-apps}

以下の手順に従って、テストアプリケーションをビルドして実行してください。

1. 新しい[ワークスペース]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps)を作成し、アプリ識別子APIキーとエンドポイントを書き留めます。
2. 統合方法（Swift Package Manager、CocoaPods、手動）に基づいて、適切な `xcodeproj` ファイルを選択して開きます。
3. `Credentials` ファイルの適切なフィールドにAPIキーとエンドポイントを入力します。
{% endtab %}
{% endtabs %}

{% alert note %}
SDKインテグレーションのQAを行う際は、[SDKデバッガー]({{site.baseurl}}/developer_guide/sdk_integration/debugging/)を使用すれば、アプリの冗長ロギングをオンにすることなく問題のトラブルシューティングを行うことができます。
{% endalert %}