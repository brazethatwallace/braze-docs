---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "このリファレンス記事では、BrazeとLinkrunnerの連携について説明します。Linkrunnerはモバイルアトリビューションおよび分析プラットフォームで、アトリビューションデータをインポートしてユーザー獲得キャンペーンをより深く理解できます。"
page_type: partner
search_tag: Partner

---

# Linkrunner

> [Linkrunner](https://linkrunner.io/)は、ユーザー獲得キャンペーンの追跡と分析を支援するモバイルアトリビューションおよび分析プラットフォームです。

_この統合はLinkrunnerによって管理されています。_

## 統合について {#about-the-integration}

BrazeとLinkrunnerの統合により、アトリビューションデータをインポートして、どのキャンペーンがユーザー獲得とエンゲージメントを促進しているかをより深く理解できます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
|---|---|
| Linkrunnerアカウント | この連携を利用するには、Linkrunnerアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合はiOSおよびAndroidアプリをサポートしています。プラットフォームによっては、アプリケーションにコードスニペットが必要になる場合があります。 |
| Linkrunner SDK | [Linkrunner SDK](https://docs.linkrunner.io/introduction)をインストールする必要があります。 |
| Braze SDK | [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/)を統合する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1:ユーザーIDをマッピングする {#step-1-map-user-ids}

Braze SDKの`changeUser`関数を使用している場合は、Linkrunner SDKの`signup`関数の`userData`パラメーターに同じユーザーIDを渡します。

`changeUser`を使用していない場合は、Linkrunner SDKの`signup`関数の`userData`パラメーターに`brazeDeviceId`を渡します。`brazeDeviceId`はBraze SDKから取得します。

{% tabs local %}
{% tab Android (Kotlin) %}
```kotlin
val userData = UserDataRequest(
    id = "123", // Your user ID
    // ...other user fields
    brazeDeviceId = "BRAZE_DEVICE_ID", // Braze device ID from the Braze SDK (Required if you are not using the changeUser function)
)

LinkRunner.getInstance().signup(userData = userData)
```
{% endtab %}

{% tab iOS (Swift) %}
```swift
let userData = UserData(
    id: "123", // Your user ID
    // ...other user fields
    brazeDeviceId: "BRAZE_DEVICE_ID" // Braze Device ID from the Braze SDK (Required if you are not using the changeUser function)
)

try await LinkrunnerSDK.shared.signup(userData: userData)
```
{% endtab %}
{% endtabs %}

### ステップ 2:BrazeでAPIキーを作成する {#step-2-create-api-key-in-braze}

Brazeダッシュボードで、**設定** > **設定およびテスト** > **APIキー** > **APIキー**に移動します。

1. **APIキーを作成**を選択します。
2. **ユーザーデータ**で、以下の権限を選択します。
   - `users.track`
   - `users.export.ids`
3. APIキーを保存します。
4. APIキーとRESTエンドポイントをコピーします。次のステップでこれらをLinkrunnerに貼り付けます。APIキーは秘密情報として扱い、公開しないでください。

### ステップ 3:LinkrunnerのダッシュボードでBrazeを設定する {#step-3-configure-braze-in-linkrunners-dashboard}

1. Linkrunnerで、左側のパネルの**統合**に移動します。
2. **分析**の下で、Brazeの**設定**を選択します。
3. ステップ 2でコピーしたAPIキーとRESTエンドポイントを入力します。

詳細については、[Linkrunnerのドキュメント](https://docs.linkrunner.io/analytics-integrations/braze)を参照してください。

### ステップ 4:ユーザーアトリビューションデータを確認する {#step-4-view-user-attribution-data}

Linkrunnerは`lr_campaign`と`lr_ad_network`をカスタム属性として送信します。このデータは、Brazeダッシュボードのユーザープロファイルの**カスタム属性**セクションで確認できます。

## FacebookおよびX（旧Twitter）のアトリビューションデータ {#facebook-and-x-formerly-twitter-attribution-data}

FacebookおよびX（旧Twitter）のキャンペーンのアトリビューションデータは、パートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータをサードパーティと共有することを許可していないため、パートナーはそのデータをBrazeに送信できません。