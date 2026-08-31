---
page_order: 1.2
nav_title: 認証
article_title: SDK認証の設定
description: "このリファレンス記事では、SDK認証と、Braze SDKでこの機能を有効にする方法について説明します。"
platform:
  - iOS
  - Android
  - Web

---

# SDK認証の設定 {#set-up-sdk-authentication}

> SDK認証を使用すると、ログインしているユーザーの代わりに行われたSDKリクエストに対して（サーバー側で生成された）暗号証明を提供できます。

## 仕組み {#how-it-works}

アプリでこの機能を有効にすると、無効なまたは欠落しているJSON Web Token（JWT）を含むリクエストを拒否するようBrazeダッシュボードを設定できます。これには以下が含まれます：

- カスタムイベント、属性、購入、セッションデータの送信
- Brazeワークスペースでの新規ユーザーの作成
- 標準ユーザープロファイル属性の更新
- メッセージの受信またはトリガー

これにより、認証されていないログイン済みユーザーがアプリのSDK APIキーを使用して、他のユーザーになりすますなどの悪意あるアクションを実行することを防止できます。

## 認証の設定 {#setting-up-authentication}

### ステップ1：サーバーの設定 {#server-side-integration}

#### ステップ1.1：公開キー/秘密キーのペアを生成する {#generate-keys}

RSA256の公開キー/秘密キーのペアを生成します。公開キーは最終的にBrazeダッシュボードに追加し、秘密キーはサーバーに安全に保存する必要があります。

RS256 JWTアルゴリズムで使用するには、2048ビットのRSAキーを推奨します。

{% alert warning %}
秘密キーは必ず*秘密*にしてください。秘密キーをアプリやWebサイトに公開したりハードコーディングしたりしないでください。秘密キーを知っている人は、あなたのアプリケーションに代わってユーザーになりすましたり、ユーザーを作成したりできます。
{% endalert %}

#### ステップ1.2：現在のユーザーのJSON Webトークンを作成する {#create-jwt}

秘密キーを取得したら、サーバーサイドのアプリケーションはそれを使用して、現在ログインしているユーザーのJWTをアプリまたはWebサイトに返す必要があります。

通常、このロジックは、アプリが現在のユーザープロファイルをリクエストする場所（ログインエンドポイントや、現在のユーザープロファイルを更新する場所など）に配置できます。

JWTを生成する際には、以下のフィールドが必要です：

**JWTヘッダー**

| フィールド | 必須 | 説明 |
| ----- | -------- | ----------------------------------- |
| `alg` | はい | サポートされているアルゴリズムは`RS256`です。 |
| `typ` | はい | タイプは`JWT`と等しくなければなりません。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="現在のユーザーのJSON Webトークンを作成する" }

**JWTペイロード**

| フィールド | 必須 | 説明 |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | はい | 「subject」は、`changeUser`を呼び出す際にBraze SDKに提供するユーザーIDと一致する必要があります |
| `exp` | はい | 「expiration」は、このトークンの有効期限をUnixタイムスタンプ（秒単位）で指定します（例：2030年1月1日の場合は`1893456000`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="現在のユーザーのJSON Webトークンを作成する" }

{% alert tip %}
JSON Webトークンの詳細や、この署名プロセスを簡素化する多くのオープンソースライブラリについては、[https://jwt.io](https://jwt.io)をご覧ください。
{% endalert %}

### ステップ2：SDKの設定 {#sdk-integration}

この機能は、以下の[SDKバージョン]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)以降で利用可能です：

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOSの連携については、このページではBraze Swift SDKの手順を説明しています。レガシーのAppboyKit iOS SDKでの使用例については、[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m)と[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)を参照してください。
{% endalert %}

#### ステップ2.1：Braze SDKで認証を有効にする {#step-21-enable-authentication-in-the-braze-sdk}

この機能を有効にすると、Braze SDKはBrazeサーバーへのネットワークリクエストに、現在のユーザーの最新のJWTを付加します。

{% alert note %}
このオプションだけで初期化しても、Brazeダッシュボードで[認証の適用](#braze-dashboard)を開始するまで、データ収集に影響はありません。
{% endalert %}

{% tabs %}
{% tab Web %}
`initialize`を呼び出す際に、オプションの`enableSdkAuthentication`プロパティを`true`に設定します。
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
SDK認証は、ネイティブSDKの初期化時に有効にする必要があります。ネイティブのiOSおよびAndroidコードに以下の設定を追加してください：

**iOS（AppDelegate.swift）**

```swift
import BrazeKit
import braze_react_native_sdk

let configuration = Braze.Configuration(
  apiKey: "{YOUR-BRAZE-API-KEY}",
  endpoint: "{YOUR-BRAZE-ENDPOINT}"
)
configuration.api.sdkAuthentication = true
let braze = BrazeReactBridge.perform(
  #selector(BrazeReactBridge.initBraze(_:)),
  with: configuration
).takeUnretainedValue() as! Braze
```

**Android（braze.xml）**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以降のステップで示すReact Native JavaScriptメソッドを使用できます。
{% endtab %}
{% tab Java %}
Brazeインスタンスを設定する際に、`setIsSdkAuthenticationEnabled`を`true`に設定します。
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

または、braze.xmlに`<bool name="com_braze_sdk_authentication_enabled">true</bool>`を追加することもできます。
{% endtab %}
{% tab KOTLIN %}
Brazeインスタンスを設定する際に、`setIsSdkAuthenticationEnabled`を`true`に設定します。
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

または、braze.xmlに`<bool name="com_braze_sdk_authentication_enabled">true</bool>`を追加することもできます。
{% endtab %}
{% tab Objective-C %}
SDK認証を有効にするには、Brazeインスタンスを初期化する前に、`BRZConfiguration`オブジェクトの`configuration.api.sdkAuthentication`プロパティを`YES`に設定します：

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
SDK認証を有効にするには、SDKを初期化する際に`Braze.Configuration`オブジェクトの`configuration.api.sdkAuthentication`プロパティを`true`に設定します：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
現在、SDK認証はネイティブのiOSおよびAndroidコードでSDKの初期化時に有効にする必要があります。Flutter SDKでSDK認証を有効にするには、他のタブのiOSおよびAndroidの連携手順に従ってください。SDK認証を有効にした後、残りの機能はDartで統合できます。
{% endtab %}
{% tab Flutter %}
SDK認証は、ネイティブのiOSおよびAndroidコードでSDKの初期化時に有効にする必要があります。ネイティブレイヤーで有効にすると、Flutter SDKメソッドを使用してJWT署名を渡すことができます。

**iOS**

SDK認証を有効にするには、ネイティブiOSコードで`configuration.api.sdkAuthentication`プロパティを`true`に設定します：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android（braze.xml）**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以降のステップで示すFlutter SDKメソッドを使用できます。
{% endtab %}
{% tab Unity %}
SDK認証は、ネイティブSDKの初期化時に有効にする必要があります。ネイティブのiOSおよびAndroidコードに以下の設定を追加してください：

**iOS**

設定ファイルで`SDKAuthenticationEnabled`プロパティを`true`に設定します：

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android（braze.xml）**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以降のステップで示すUnity C#メソッドを使用できます。
{% endtab %}
{% tab Cordova %}
SDK認証は、ネイティブSDKの初期化時に有効にする必要があります。ネイティブのiOSおよびAndroidコードに以下の設定を追加してください：

**iOS**

SDK認証を有効にするには、`config.xml`で`enableSDKAuthentication`プロパティを`true`に設定します：

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android（braze.xml）**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

ネイティブレイヤーでSDK認証を有効にした後、以降のステップで示すCordova JavaScriptメソッドを使用できます。
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
SDK認証は、ネイティブSDKの初期化時に有効にする必要があります。iOSおよびAndroidのSDK認証をそれぞれ設定してください：

**iOS**

SDK認証を有効にするには、SDKを初期化する際に`configuration.Api.SdkAuthentication`プロパティを`true`に設定します：

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android（braze.xml）**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

SDK認証を有効にした後、以降のステップで示す.NET MAUIメソッドを使用できます。
{% endtab %}
{% tab Expo %}
Braze Expoプラグインを使用する場合、アプリ設定で`enableSdkAuthentication`プロパティを`true`に設定します。これにより、手動のネイティブコード変更を必要とせず、ネイティブのiOSおよびAndroidレイヤーでSDK認証が自動的に設定されます。

**app.jsonまたはapp.config.js**

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "enableSdkAuthentication": true
        }
      ]
    ]
  }
}
```

アプリ設定でSDK認証を有効にした後、以降のステップではReact Nativeタブに示すReact Native JavaScriptメソッドを使用できます。

{% alert note %}
完全な実装例については、GitHubの[Braze Expoプラグインサンプルアプリ](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

#### ステップ2.2：現在のユーザーのJWTを設定する {#step-22-set-the-current-users-jwt}

アプリがBrazeの`changeUser`メソッドを呼び出すたびに、[サーバーサイドで生成された](#braze-dashboard)JWTも提供してください。

また、セッション中に現在のユーザーのトークンを更新するように設定することもできます。

{% alert note %}
`changeUser`はユーザーIDが*実際に変更された*場合にのみ呼び出す必要があります。ユーザーIDが変更されていない場合に、認証トークン（JWT）を更新する手段としてこのメソッドを使用しないでください。
{% endalert %}

{% tabs %}
{% tab Web %}
[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)を呼び出す際にJWTを提供します：

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

[`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser)を呼び出す際にJWTを提供します：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)を呼び出す際にJWTを提供します：

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

[`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)を呼び出す際にJWTを提供します：

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

または、セッション中にユーザーのトークンを更新した場合：

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))を呼び出す際にJWTを提供します：

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

または、セッション中にユーザーのトークンを更新した場合：

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

[`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))を呼び出す際にJWTを提供します：

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```

{% alert note %}
`changeUser`は呼び出しスレッドで即座に返されます。ここで提供されたSDK認証署名は、ユーザー切り替え処理が完了した後に付加されます。
{% endalert %}

または、セッション中にユーザーのトークンを更新した場合：

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)を呼び出す際にJWTを提供します：

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
または、セッション中にユーザーのトークンを更新した場合：

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

`changeUser`を呼び出す際にJWTを提供します：

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

`ChangeUser`を呼び出す際にJWTを提供します：

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

`changeUser`を呼び出す際にJWTを提供します：

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

`ChangeUser`を呼び出す際にJWTを提供します：

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

Braze Expoプラグインを使用する場合、同じReact Native SDKメソッドを使用します。`changeUser`を呼び出す際にJWTを提供します：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

または、セッション中にユーザーのトークンを更新した場合：

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### ステップ2.3：無効なトークンのコールバック関数を登録する {#sdk-callback}

この機能が[必須](#enforcement-options)に設定されている場合、以下のシナリオではSDKリクエストがBrazeによって拒否されます：
- Braze APIが受信した時点でJWTの有効期限が切れていた場合
- JWTが空または欠落していた場合
- Brazeダッシュボードにアップロードした公開キーでJWTの検証に失敗した場合

`subscribeToSdkAuthenticationFailures`を使用して、SDKリクエストがこれらの理由で失敗した場合に通知を受け取るよう登録できます。コールバック関数には、関連する[`errorCode`](#error-codes)、エラーの`reason`、リクエストの`userId`（ユーザーは匿名にはなりません）、およびエラーの原因となった認証トークン（JWT）を含むオブジェクトが渡されます。

失敗したリクエストは、アプリが新しい有効なJWTを提供するまで定期的に再試行されます。そのユーザーがまだログインしている場合、このコールバックを使用してサーバーに新しいJWTをリクエストし、Braze SDKに新しい有効なトークンを提供できます。

認証エラーを受信したら、エラー内の`userId`が現在ログインしているユーザーと一致することを確認し、サーバーから新しい署名を取得してBraze SDKに提供してください。これらのエラーを監視サービスやエラー報告サービスに記録することもできます。

{% alert tip %}
これらのコールバックメソッドは、独自の監視やエラーログサービスを追加して、Brazeリクエストが拒否される頻度を追跡するのに最適な場所です。
{% endalert %}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToSdkAuthenticationFailures((error) => {
  console.error("SDK authentication failed:", error);
  console.log("Error code:", error.errorCode);
  console.log("User ID:", error.userId);
  // Note: Do not log error.signature as it contains sensitive authentication credentials

  // Verify the error.userId matches the currently logged-in user
  // Fetch a new token from your server and set it
  fetchNewSignature(error.userId).then((newSignature) => {
    braze.setSdkAuthenticationSignature(newSignature);
  });
});
```
{% endtab %}
{% tab React Native %}
```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);

    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("Invalid SDK Authentication Token.");
  final newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Flutter %}
```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();

braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.");

  String newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Unity %}
**iOS**

ネイティブiOS実装でSDK認証デリゲートを設定します：

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Debug.Log("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    BrazeBinding.SetSdkAuthenticationSignature(newSignature);
  }
}
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.subscribeToSdkAuthenticationFailures((error) => {
  console.log(`SDK Authentication for ${error.user_id} failed with error code ${error.error_code}.`);

  const newSignature = getNewTokenSomehow(error);
  BrazePlugin.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
**iOS**

`Braze`インスタンスにSDK認証デリゲートを設定します：

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public override void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Console.WriteLine("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    Braze.SharedInstance?.SetSDKAuthenticationSignature(newSignature);
  }
}

// Set the delegate during initialization
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
braze.SdkAuthDelegate = new SdkAuthDelegate();
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Expo %}
Braze Expoプラグインを使用する場合、同じReact Native SDKメソッドを使用します：

```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);

    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% endtabs %}

### ステップ3：ダッシュボードで認証を有効にする {#braze-dashboard}

次に、事前に設定したアプリに対して、Brazeダッシュボードで認証を有効にします。

SDK認証設定がBrazeダッシュボードで**必須**に設定されない限り、SDKリクエストは認証なしで通常どおり流れ続けます。

連携に問題が発生した場合（例：アプリがSDKにトークンを正しく渡していない、サーバーが無効なトークンを生成しているなど）、Brazeダッシュボードでこの機能を無効にすると、検証なしでデータが通常どおり流れるようになります。

#### 適用オプション {#enforcement-options}

ダッシュボードの**設定の管理**ページでは、各アプリに3つのSDK認証状態があり、Brazeがリクエストを検証する方法を制御します。

| 設定 | 説明 |
| ------ | ---------- |
| **無効** | BrazeはユーザーのJWTを検証しません。（デフォルト設定） |
| **オプション** | Brazeはログインユーザーのリクエストを検証しますが、無効なリクエストを拒否しません。 |
| **必須** | Brazeはログインユーザーのリクエストを検証し、無効なJWTを拒否します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="適用オプション" }

![無効、オプション、必須の適用オプションが表示されたBraze SDK認証設定。]({% image_buster /assets/img/sdk-auth-settings.png %})

**オプション**設定は、この機能がアプリのSDKトラフィックに与える潜在的な影響を監視するのに便利な方法です。

無効なJWTは**オプション**と**必須**の両方の状態で報告されますが、**必須**状態のみがSDKリクエストを拒否し、アプリにリトライと新しいJWTのリクエストを促します。

## 公開鍵の管理 {#key-management}

### 公開鍵を追加する {#adding-a-public-key}

アプリごとに、プライマリ、セカンダリ、ターシャリの最大3つの公開キーを追加できます。必要に応じて、同じキーを複数のアプリに追加することもできます。公開鍵を追加するには：

1. Brazeダッシュボードに移動し、**設定** > **アプリ設定**を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. **SDK認証**で、**公開キーを追加**を選択します。
4. オプションの説明を入力し、公開キーを貼り付け、**公開キーを追加**を選択します。

### 新しいプライマリキーを割り当てる {#assign-a-new-primary-key}

セカンダリキーまたはターシャリキーを新しいプライマリキーとして割り当てるには：

1. Brazeダッシュボードに移動し、**設定** > **アプリ設定**を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. **SDK認証**でキーを選択し、**管理** > **プライマリキーに設定**を選択します。

### キーを削除する {#deleting-a-key}

プライマリキーを削除するには、まず[新たなプライマリキーを割り当て](#assign-a-new-primary-key)、それからキーを削除します。非プライマリキーを削除するには：

1. Brazeダッシュボードに移動し、**設定** > **アプリ設定**を選択します。
2. 利用可能なアプリのリストからアプリを選びます。
3. **SDK認証**でプライマリキー以外のキーを選択し、**管理** > **公開キーを削除**を選択します。

## 分析 {#analytics}

各アプリには、この機能が**オプション**状態と**必須**状態にある間に収集されたSDK認証エラーの内訳が表示されます。

データはリアルタイムで利用でき、チャート上のポイントにカーソルを合わせると、指定した日付のエラーの内訳を確認できます。

![認証エラーの発生件数を示すグラフ。また、エラーの総数、エラーの種類、調整可能な日付範囲も表示されます。]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## エラーコード {#error-codes}

| エラーコード | エラーの理由 | 説明 | 解決手順 |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | Brazeを使用する場合、有効期限は必須フィールドです。| JWT生成ロジックに`exp`または有効期限フィールドを追加してください。 |
| 20 | `DECODING_ERROR` | 公開鍵が一致しないか、一般的な捕捉不能エラーが発生しました。| JWTをJWTテストツールにコピーして、JWTが無効な形式である理由を診断してください。 |
| 21 | `SUBJECT_MISMATCH` | 期待されるサブジェクトと実際のサブジェクトが一致しません。| `sub`フィールドは、SDKの`changeUser`メソッドに渡されたユーザーIDと同じである必要があります。 |
| 22 | `EXPIRED` | 提供されたトークンの有効期限が切れています。| 有効期限を延長するか、トークンが期限切れになる前に定期的に更新してください。 |
| 23 | `INVALID_PAYLOAD` | トークンのペイロードが無効です。| JWTをJWTテストツールにコピーして、JWTが無効な形式である理由を診断してください。 |
| 24 | `INCORRECT_ALGORITHM` | トークンのアルゴリズムはサポートされていません。| JWTを`RS256`暗号化方式に変更してください。その他のタイプはサポートされていません。 |
| 25 | `PUBLIC_KEY_ERROR` | 公開鍵が適切な形式に変換できませんでした。| JWTをJWTテストツールにコピーして、JWTが無効な形式である理由を診断してください。 |
| 26 | `MISSING_TOKEN` | リクエストにトークンが指定されていません。| `changeUser(id, token)`を呼び出す際にトークンを渡していることを確認し、そのトークンが空白でないことを確認してください。|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | 提供されたトークンに一致する公開鍵がありませんでした。| JWTで使用されている秘密キーは、アプリに設定されている公開キーのいずれとも一致しません。このAPIキーに対応するワークスペース内の正しいアプリに公開キーを追加したことを確認してください。|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | リクエストのペイロード内のユーザーIDがすべて、要求通りに一致しているわけではありません。| これは予期しないエラーであり、不正なペイロードを引き起こす可能性があります。サポートチケットを開いてお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="エラーコード" }

## よくある質問（FAQ） {#faq}

### この機能はすべてのアプリで同時に有効にする必要がありますか？ {#faq-app-by-app}

いいえ、この機能は特定のアプリに対して有効にすることができ、すべてのアプリで一度に使用する必要はありません。

### アプリの古いバージョンを使っているユーザーはどうなりますか？ {#faq-sdk-backward-compatibility}

この機能を適用し始めると、古いバージョンのアプリによるリクエストはBrazeによって拒否され、SDKによって再試行されます。ユーザーがアプリをサポートされたバージョンにアップグレードすると、キューに入れられたリクエストは再び受け入れられるようになります。

可能であれば、他の必須アップグレードと同様に、ユーザーにアップグレードを勧めてください。あるいは、許容できる割合のユーザーがアップグレードしたことを確認するまで、この機能を[オプション](#enforcement-options)にしておくこともできます。

### JWTを生成するときには、どのような有効期限を使用する必要がありますか？ {#faq-expiration}

平均セッション期間、セッションCookie/トークンの有効期限、またはアプリケーションが現在のユーザープロファイルを更新する頻度のうち、高い方の値を使用することをお勧めします。

### ユーザーのセッションの途中でJWTの有効期限が切れた場合はどうなりますか？ {#faq-jwt-expiration}

ユーザーのトークンがセッション中に期限切れになると、SDKは[コールバック関数](#sdk-callback)を呼び出して、Brazeにデータを送信し続けるために新しいJWTが必要であることをアプリに知らせます。

### サーバー側の統合が壊れ、JWTを作成できなくなった場合はどうなりますか？ {#faq-server-downtime}

サーバーがJWTを提供できない場合、または統合に問題がある場合は、Brazeダッシュボードでいつでも機能を無効にできます。

一度無効にすると、保留中の失敗したSDKリクエストは最終的にSDKによって再試行され、Brazeによって受け入れられます。

### なぜこの機能では、共有シークレットではなく公開キー/秘密キーを使うのでしょうか？ {#faq-shared-secrets}

共有シークレットを使う場合、Brazeのダッシュボードページなど、その共有シークレットにアクセスできる人なら誰でも、トークンを生成してエンドユーザーになりすますことができます。

代わりに、公開キーと秘密キーを使用します。これにより、Brazeの従業員でさえ（ましてや御社のユーザーは言うまでもなく）あなたの秘密キーにアクセスできません。

### 拒否されたリクエストはどのように再試行されますか？ {#faq-retry-logic}

認証エラーが原因でリクエストが拒否されると、SDKはユーザーのJWTを更新するために使用されるコールバックを呼び出します。

リクエストはエクスポネンシャルバックオフアプローチを使用して定期的に再試行されます。50回連続で失敗すると、次のセッション開始まで再試行は一時停止されます。各SDKには、手動でデータフラッシュをリクエストするメソッドもあります。

### 匿名ユーザーに対してSDK認証は使えますか？ {#faq-anonymous-users}

いいえ。SDK認証はWebサイトが誰かのIDを主張することで機能するため、識別済みのユーザーにのみ適用されます。匿名ユーザーの場合、主張するIDがありません。

適用は`changeUser`が呼び出された後に開始されます。ユーザーが識別される前（例えば、サインアップ前に匿名で閲覧している間）は、SDKはJWTなしでBrazeにデータを送信できます。`changeUser`が呼び出された後、その識別済みプロファイルに対するリクエストには有効なJWTが必要になります。

つまり、一般的なユーザージャーニーは次のようになります：

1. ユーザーがWebサイトにアクセスするか、アプリを匿名で開きます。BrazeはJWTなしでこのアクティビティを収集します。
2. ユーザーがサインアップまたはログインし、アプリが`external_id`を指定して`changeUser`を呼び出します。
3. Brazeはそのユーザーのアクティビティの収集を続け、その識別済みプロファイルに対するリクエストにはSDK認証が適用されます。

### SDK認証はユーザーエイリアスで機能しますか？ {#faq-aliases}

いいえ。SDK認証には`external_id`が必要です。`braze_id`または`alias_id`のみが利用可能な場合は設定できないため、エイリアスのみのプロファイルではSDK認証を使用できません。

### SDK認証を有効にすると、未認証のアクティビティ収集がブロックされますか？ {#faq-unauthenticated-collection}

いいえ。SDK認証は正当な匿名アクティビティの収集をブロックしません。`changeUser`でプロファイルが識別された後にのみ適用されます。