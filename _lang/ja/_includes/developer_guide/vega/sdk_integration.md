## Braze Vega SDKについて {#about-the-braze-vega-sdk}

Braze Vega SDKを使用すると、分析データを収集し、リッチなアプリ内メッセージをユーザーに表示できます。Braze Vega SDKのメソッドの大半は非同期であり、awaitまたはresolveすべきPromiseを返します。

## Braze Vega SDKの統合 {#integrating-the-braze-vega-sdk}

### ステップ 1: Brazeライブラリーをインストールする {#step-1-install-the-braze-library}

お好みのパッケージマネージャーを使って、Braze Vega SDKをインストールします。

{% tabs local %}
{% tab npm %}
プロジェクトでNPMを使用している場合、Braze Vega SDKを依存関係として追加できます。

```bash
npm install @braze/vega-sdk --save
```

インストール後、必要なメソッドをインポートできます：

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
プロジェクトでYarnを使用している場合、Braze Vega SDKを依存関係として追加できます。

```bash
yarn add @braze/vega-sdk
```

インストール後、必要なメソッドをインポートできます：

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### ステップ 2: SDKを初期化する {#step-2-initialize-the-sdk}

プロジェクトにBraze Vega SDKを追加した後、Brazeダッシュボードの**Settings** > **App Settings**にあるAPIキーと[SDKエンドポイントURL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)を使用してライブラリーを初期化します。

{% alert important %}
他のBrazeメソッドを呼び出す前に、`changeUser`のPromiseをawaitまたはresolveする必要があります。そうしないと、イベントや属性が誤ったユーザーに設定される可能性があります。
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");

      // Start a session
      await openSession();

      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };

    initBraze();
  }, []);

  return (
    // Your app components
  );
};
```

{% alert important %}
匿名ユーザーは[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users)にカウントされる可能性があります。そのため、これらのユーザーをMAUカウントから除外するために、条件付きでSDKを読み込むか初期化することを検討してください。
{% endalert %}

## オプション設定 {#optional-configurations}

### ロギング {#logging}

SDKのロギングを有効にすると、デバッグやトラブルシューティングに役立ちます。ロギングを有効にする方法は複数あります。

#### 初期化中にロギングを有効にする {#enable-logging-during-initialization}

デバッグメッセージをコンソールに記録するには、`initialize()`に`enableLogging: true`を渡します：

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
基本ログはすべてのユーザーに表示されるため、本番環境にコードをリリースする前にロギングを無効にすることを検討してください。
{% endalert %}

#### 初期化後にロギングを有効にする {#enable-logging-after-initialization}

初期化後にSDKのロギングを有効または無効にするには、`toggleLogging()`を使用します：

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### カスタムロギング {#custom-logging}

SDKのログ処理をより細かくコントロールするために、`setLogger()`を使用してカスタムロガー関数を指定します：

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 設定オプション {#configuration-options}

SDKの動作をカスタマイズするために、`initialize()`に追加の設定オプションを渡すことができます：

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 1800 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## SDKをアップグレードする {#upgrading-the-sdk}

NPMやYarnからBraze Vega SDKを参照している場合、パッケージの依存関係を更新することで最新バージョンにアップグレードできます：

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 統合のテスト {#testing-your-integration}

SDKの統合が正しく動作していることを確認するには：

1. コンソールにデバッグメッセージを表示するために、`enableLogging: true`を指定してSDKを初期化します
2. 他のSDKメソッドを呼び出す前に、必ず`await changeUser()`を実行します
3. `await openSession()`を呼び出してセッションを開始します
4. Brazeダッシュボードの**Overview**で、セッションデータが記録されていることを確認します
5. カスタムイベントのログ記録をテストし、ダッシュボードに表示されることを確認します