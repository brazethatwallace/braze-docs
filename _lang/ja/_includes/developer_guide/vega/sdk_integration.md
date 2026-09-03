## Braze Vega SDKについて {#about-the-braze-vega-sdk}

Braze Vega SDKを使用すると、分析データを収集し、リッチなアプリ内メッセージをユーザーに表示できます。Braze Vega SDKのほとんどのメソッドは非同期であり、awaitまたはresolveする必要があるPromiseを返します。

## Braze Vega SDKの統合 {#integrating-the-braze-vega-sdk}

### ステップ1：Brazeライブラリをインストールする {#step-1-install-the-braze-library}

お好みのパッケージマネージャーを使用してBraze Vega SDKをインストールします。

{% tabs local %}
{% tab npm %}
プロジェクトでNPMを使用している場合、Braze Vega SDKを依存関係として追加できます。

```bash
npm install @braze/vega-sdk --save
```

インストール後、必要なメソッドをインポートできます。

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
プロジェクトでYarnを使用している場合、Braze Vega SDKを依存関係として追加できます。

```bash
yarn add @braze/vega-sdk
```

インストール後、必要なメソッドをインポートできます。

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### ステップ2：SDKを初期化する {#step-2-initialize-the-sdk}

Braze Vega SDKをプロジェクトに追加した後、Brazeダッシュボードの**設定** > **アプリ設定**にあるAPIキーと[SDKエンドポイントURL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)を使用してライブラリを初期化します。

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
匿名ユーザーは[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users)にカウントされる場合があります。そのため、MAUカウントからこれらのユーザーを除外するために、SDKの読み込みまたは初期化を条件付きで行うことを検討してください。
{% endalert %}

## オプションの設定 {#optional-configurations}

### ログ {#logging}

デバッグやトラブルシューティングに役立つSDKログを有効にできます。ログを有効にするには複数の方法があります。

#### 初期化時にログを有効にする {#enable-logging-during-initialization}

`initialize()` に `enableLogging: true` を渡すと、デバッグメッセージがコンソールに出力されます：

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
基本的なログはすべてのユーザーに表示されるため、コードを本番環境にリリースする前にログを無効にすることを検討してください。
{% endalert %}

#### 初期化後にログを有効にする {#enable-logging-after-initialization}

`toggleLogging()` を使用して、初期化後にSDKログを有効または無効にできます：

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### カスタムログ {#custom-logging}

`setLogger()` を使用してカスタムロガー関数を提供することで、SDKログの処理方法をより細かくコントロールできます：

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 設定オプション {#configuration-options}

`initialize()` に追加の設定オプションを渡すことで、SDKの動作をカスタマイズできます：

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 1800 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## SDKのアップグレード {#upgrading-the-sdk}

NPMまたはYarnからBraze Vega SDKを参照している場合、パッケージの依存関係を更新することで最新バージョンにアップグレードできます。

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 統合のテスト {#testing-your-integration}

SDK統合が正しく動作しているかどうかを確認するには：

1. `enableLogging: true` を設定してSDKを初期化し、コンソールにデバッグメッセージが表示されることを確認します
2. 他のSDKメソッドを呼び出す前に、必ず `await changeUser()` を実行します
3. `await openSession()` を呼び出してセッションを開始します
4. Brazeダッシュボードの**概要**でセッションデータが記録されていることを確認します
5. カスタムイベントのログを記録し、ダッシュボードに表示されることを確認します