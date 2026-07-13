---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "このリファレンス記事では、BrazeとAirbridgeのパートナーシップについて説明します。Airbridgeは、デバイス、ID、プラットフォームにわたり真のマーケティング効果を測定するためのピープルベースドアトリビューションとインクリメンタル測定を提供します。"
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/)は、モバイルアトリビューション、インクリメンタル計測、マーケティングミックスモデリングによる成長源を発見するための統合モバイル計測プラットフォームです。

_この統合はAirbridgeによって管理されています。_

## 統合について {#about-the-integration}

BrazeとAirbridgeの統合により、Airbridgeからオーガニック以外のすべてのインストールアトリビューションデータをBrazeに渡して、パーソナライズされたマーケティングキャンペーンを構築できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Airbridgeアカウント | このパートナーシップを活用するには、Airbridgeアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリがサポートされています。プラットフォームによっては、アプリケーションにコードスニペットが必要になる場合があります。 |
| Airbridge SDK | 必要なBraze SDKに加えて、Airbridge [Android](https://help.airbridge.io/en/developers/android-sdk)または[iOS](https://help.airbridge.io/en/developers/ios-sdk) SDKをインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1：デバイスIDをマッピングする {#step-1-map-device-id}

サーバー間統合を有効にするには、アプリに次のコードスニペットを組み込みます。

#### Android

Androidアプリをお持ちの場合は、一意のBrazeデバイスIDをAirbridgeに渡す必要があります。

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

iOSアプリの場合、useUUIDAsDeviceIdフィールドをfalseに設定することで、IDFVを収集できます。設定されていない場合、iOSのアトリビューションはAirbridgeからBrazeに正確にマッピングされない可能性が高くなります。詳細については、「IDFVの収集」を参照してください。

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### ステップ2：Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで**パートナー連携** > **テクノロジーパートナー**に移動し、**Airbridge**を選択します。

ここでは、RESTエンドポイントの確認とBrazeデータインポートキーの生成ができます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、次のステップでAirbridgeのダッシュボードでポストバックを設定する際に使用されます。

![データインポートキーとRESTエンドポイントのフィールドが表示されたBraze Airbridgeパートナーページ。]({% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %})

### ステップ3：AirbridgeのダッシュボードでBrazeを設定する {#step-3-configure-braze-in-airbridges-dashboard}

1. Airbridgeで、左サイドバーの**Integrations** > **Third-party Integrations**に移動し、**Braze**を選択します。
2. Brazeダッシュボードで確認したデータインポートキーとRESTエンドポイントを入力します。
3. イベントタイプ（Install EventまたはInstall & Deeplink Open Event）を選択し、保存します。

{% alert note %}
ディープリンクオープンイベントにつながったキャンペーンのアトリビューションデータは、デバイスレベルで更新されます。例えば、2人のユーザーが1つのデバイスを使用し、1人のユーザーがディープリンクオープンイベントを実行した場合、このイベントのアトリビューションデータはもう1人のユーザーのデータにも反映されます。
{% endalert %}

詳細な手順については、[Airbridge](https://help.airbridge.io/en/guides/braze)を参照してください。

### ステップ4：統合を確認する {#step-4-confirm-the-integration}

BrazeがAirbridgeからアトリビューションデータを受信すると、BrazeのAirbridgeテクノロジーパートナーページのステータス接続インジケーターが「Not Connected」から「Connected」に変わり、最後に成功したリクエストのタイムスタンプが表示されます。

このステータスは、Brazeがアトリビュートされたインストールに関するデータを受信した後にのみ変更されます。Brazeはオーガニックインストールを無視し（Airbridgeのポストバックから除外）、接続が成功したかどうかを判断する際にそれらをカウントしません。

## 利用可能なデータフィールド {#available-data-fields}

Airbridgeは、次のデータフィールドチャートにリストされている4種類のアトリビューションデータをBrazeに送信できます。このデータはAirbridgeダッシュボードで確認でき、ユーザーのインストールアトリビューションおよびフィルタリングに使用されます。

提案されたとおりに統合を設定すると、Brazeはインストールデータをセグメントフィルターにマッピングします。

| Airbridgeのデータフィールド | Brazeセグメントフィルター | 説明 |
| -------------------- | ---------------------| ---- |
| `Channel` | インストールアトリビューションソース | インストールまたはディープリンクオープンが紐づけられるチャネル |
| `キャンペーン` | インストールアトリビューションキャンペーン | インストールまたはディープリンクオープンが紐づけられるキャンペーン |
| `Ad Group` | インストールアトリビューション広告グループ | インストールまたはディープリンクオープンが紐づけられる広告グループ |
| `Ad Creative` | インストールアトリビューション広告 | インストールまたはディープリンクオープンが紐づけられる広告クリエイティブ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="利用可能なデータフィールド" }

ユーザー群は、Brazeダッシュボードでインストールアトリビューションフィルターを使用して、アトリビューションデータによってセグメント化できます。

![利用可能なAirbridgeインストールアトリビューションフィールドが表示されたBrazeセグメントフィルター。]({% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %})

## Meta Businessアトリビューションデータ {#meta-business-attribution-data}

Meta Businessキャンペーンのアトリビューションデータは、当社のパートナーを通じて入手することはできません。このメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータをBrazeに送信できません。

## BrazeでのAirbridgeクリックトラッキングURL（オプション） {#airbridge-click-tracking-urls-in-braze-optional}

Brazeキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールと再エンゲージメントを促進しているかを確認できます。この結果を用いてマーケティングパフォーマンスを測定し、より強力なROIのためにどこにリソースを投入するかを決定できます。

Airbridgeのクリックトラッキングリンクの使用を開始するには、[Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link)にアクセスしてください。セットアップが完了したら、AirbridgeのクリックトラッキングリンクをBrazeキャンペーンに直接挿入できます。その後、Airbridgeは[確率的アトリビューション手法](https://help.airbridge.io/en/guides/identity-matching)を使用して、リンクをクリックしたユーザーをアトリビュートします。Brazeキャンペーンからのアトリビューションの精度を高めるために、Airbridgeトラッキングリンクにデバイス識別子を付加することをお勧めします。これにより、リンクをクリックしたユーザーを決定論的にアトリビュートできます。

{% tabs %}
{% tab Android %}
Androidの場合、Brazeでは[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id)にオプトインできます。GAIDはまた、Airbridge SDK統合によってネイティブに収集されます。以下のLiquidロジックを利用することで、AirbridgeのクリックトラッキングリンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAirbridgeの両方が、SDK統合を通じてネイティブにIDFVを自動的に収集します。これはデバイス識別子として使用できます。以下のLiquidロジックを利用することで、AirbridgeのクリックトラッキングリンクにIDFVを含めることができます。

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**この推奨事項の適用は完全に任意です。**<br>
現在、クリックトラッキングリンクでIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Airbridgeは確率的モデリングによってこれらのクリックをアトリビュートできます。
{% endalert %}