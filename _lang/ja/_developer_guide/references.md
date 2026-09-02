---
nav_title: リファレンスとサンプルアプリ
article_title: Braze SDK リファレンス、リポジトリ、サンプルアプリ
page_order: 5.5
description: "各 Braze SDKに属するリファレンスドキュメント、GitHubリポジトリ、サンプルアプリの一覧です。"
toc_headers: h2
---

# リファレンス、リポジトリ、サンプルアプリ {#references-repositories-and-sample-apps}

> これは、各 Braze SDKに属するリファレンスドキュメント、GitHubリポジトリ、サンプルアプリの一覧です。SDKのリファレンスドキュメントには、使用可能なクラス、型、関数、変数の詳細が記載されています。GitHubリポジトリは、SDKの関数や属性の宣言、コードの変更、バージョン管理に関するインサイトを提供します。各リポジトリには、Brazeの機能をテストしたり、独自のアプリケーションと併せて実装するために使用できる、完全にビルド可能なサンプルアプリケーションも含まれています。

ドキュメント内のミラーリングされたリポジトリREADMEコンテンツについては、[リポジトリガイド]({{site.baseurl}}/developer_guide/sdk_repository_guides)を参照してください。

## リソース一覧 {#list-of-resources}

{% alert note %}
現在、一部のSDKには専用のリファレンスドキュメントがありません。現在対応を進めています。
{% endalert %}

| プラットフォーム          | リファレンス                                                                                                                                    | リポジトリ                                                                 | サンプルアプリ                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [リファレンスドキュメント](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [GitHub リポジトリ](https://github.com/braze-inc/braze-android-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| Swift SDK         | [リファレンスドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [GitHub リポジトリ](https://github.com/braze-inc/braze-swift-sdk)            | [サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| Web SDK           | [リファレンスドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [GitHub リポジトリ](https://github.com/braze-inc/braze-web-sdk)              | [サンプルアプリ](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Javascript SDK           | [リファレンスドキュメント](https://braze-inc.github.io/braze-javascript-sdk/)                                                               | [GitHub リポジトリ](https://github.com/braze-inc/braze-javascript-sdk/tree/main)              | N/A              |
| Cordova SDK       | [宣言ファイル](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [GitHub リポジトリ](https://github.com/braze-inc/braze-cordova-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [リファレンスドキュメント](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [GitHub リポジトリ](https://github.com/braze-inc/braze-flutter-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [リファレンスドキュメント](https://braze-inc.github.io/braze-react-native-sdk/)                                                                   | [GitHub リポジトリ](https://github.com/braze-inc/braze-react-native-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Vega SDK          | [リファレンスドキュメント](https://braze-inc.github.io/braze-vega-sdk/)                                                                           | [GitHub リポジトリ](https://github.com/braze-inc/braze-vega-sdk)         | N/A                                                                                       |
| Roku SDK          | N/A                                                                                                                                                         | [GitHub リポジトリ](https://github.com/braze-inc/braze-roku-sdk)            | [サンプルアプリ](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [宣言ファイル](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [GitHub リポジトリ](https://github.com/braze-inc/braze-unity-sdk)          | [サンプルアプリ](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| .NET MAUI SDK（旧 Xamarin）      | N/A                                                                                                                                                         | [GitHub リポジトリ](https://github.com/braze-inc/braze-xamarin-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リソース一覧" }

## サンプルアプリのビルド {#building-a-sample-app}

{% tabs %}
{% tab android %}
### 「Droidboy」のビルド {#building-droidboy}

[Android SDK GitHub リポジトリ](https://github.com/braze-inc/braze-android-sdk)内のテストアプリケーションは Droidboy と呼ばれます。以下の手順に従って、プロジェクトと並行して完全に機能するコピーをビルドしてください。

1. 新しい[ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces)を作成し、Braze API 識別子キーをメモします。<br><br>
2. FCM 送信者 ID と Braze API 識別子キーを `/droidboy/res/values/braze.xml` 内の適切な場所（それぞれ `com_braze_push_fcm_sender_id` および `com_braze_api_key` という名前の文字列タグの間）にコピーします。<br><br>
3. FCM サーバーキーとサーバー ID を、ワークスペース設定の**設定の管理**にコピーします。<br><br>
4. Droidboy APK をアセンブルするには、SDK ディレクトリ内で `./gradlew assemble` を実行します。Windows では `gradlew.bat` を使用してください。<br><br>
5. テストデバイスに Droidboy APK を自動的にインストールするには、SDK ディレクトリ内で `./gradlew installDebug` を実行します。

### 「Hello Braze」のビルド {#building-hello-braze}

Hello Braze テストアプリケーションは、Braze SDKの最小限のユースケースを示し、さらに Gradle プロジェクトに Braze SDKを簡単に統合する方法を示します。

1. **設定の管理**ページから API 識別子キーを `res/values` フォルダ内の `braze.xml` ファイルにコピーします。
![「Hello Braze」のビルドに関するスクリーンショット]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. サンプルアプリをデバイスまたはエミュレーターにインストールするには、SDK ディレクトリ内で以下のコマンドを実行します。
```
./gradlew installDebug
```
`ANDROID_HOME` 変数が正しく設定されていない場合、または有効な `sdk.dir` フォルダを含む `local.properties` フォルダがない場合、このプラグインはベース SDKも自動的にインストールします。詳細については、[プラグインリポジトリ](https://github.com/JakeWharton/sdk-manager-plugin)を参照してください。

Android SDK ビルドシステムの詳細については、[GitHub リポジトリの README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md) を参照してください。
{% endtab %}

{% tab swift %}
### Swift テストアプリのビルド {#building-swift-test-apps}

以下の手順に従って、テストアプリケーションをビルドおよび実行してください。

1. 新しい[ワークスペース]({{site.baseurl}}/user_guide/get_started/workspaces)を作成し、アプリ識別子 API キーとエンドポイントをメモします。
2. 統合方法（Swift Package Manager、CocoaPods、手動）に基づいて、適切な `xcodeproj` ファイルを選択して開きます。
3. API キーとエンドポイントを `Credentials` ファイルの適切なフィールドに入力します。
{% endtab %}
{% endtabs %}

{% alert note %}
SDK統合の QA を実施する際は、[SDK デバッガー]({{site.baseurl}}/developer_guide/sdk_integration/debugging)を使用して、アプリの詳細ログを有効にすることなく問題をトラブルシューティングしてください。
{% endalert %}