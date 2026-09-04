# フィーチャーフラグ {#feature-flags}

> フィーチャーフラグを使用すると、特定のユーザーまたはランダムに選択したユーザーの機能をリモートで有効または無効にすることができます。重要なのは、追加のコードデプロイやアプリストアの更新なしに、本番環境で機能のオンオフを切り替えられることです。これにより、新しい機能を安全かつ確信を持ってロールアウトできます。

{% alert tip %}
独自のフィーチャーフラグを作成する準備ができたら、[フィーチャーフラグの作成]({{site.baseurl}}/developer_guide/feature_flags/create)をご確認ください。
{% endalert %}

## 前提条件 {#prerequisites}

フィーチャーフラグの使用を開始するために必要な最小SDKバージョンは以下のとおりです。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## ユースケース {#use-cases}

### 段階的なロールアウト {#gradual-rollouts}

フィーチャーフラグを使用して、サンプル集団に対して機能を段階的に有効化できます。例えば、VIPユーザーに先行して新機能をソフトローンチできます。この戦略により、全ユーザーに一度に新機能をリリースすることに伴うリスクを軽減し、バグを早期に発見できます。

![ロールアウトトラフィックスライダーが0%から100%に移動するアニメーション画像。]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

例えば、より迅速なカスタマーサービスのために、アプリに新しい「ライブチャットサポート」リンクを追加することを決定したとします。この機能を全顧客に一度にリリースすることもできますが、広範なリリースには以下のようなリスクがあります。

* サポートチームはまだトレーニング中であり、リリース後すぐに顧客がサポートチケットを作成し始める可能性があります。サポートチームにもう少し時間が必要な場合の余裕がありません。
* 新しいサポートケースの実際のボリュームが不明であり、適切な人員配置ができていない可能性があります。
* サポートチームが対応しきれなくなった場合、この機能を素早くオフにする戦略がありません。
* チャットウィジェットにバグが導入される可能性があり、顧客にネガティブな体験をさせたくありません。

Brazeのフィーチャーフラグを使用すれば、機能を段階的にロールアウトし、これらのリスクすべてを軽減できます。

* サポートチームの準備ができたと報告を受けたタイミングで「ライブチャットサポート」機能をオンにします。
* この新機能をまず10%のユーザーにのみ有効化し、適切な人員配置かどうかを判断します。
* バグがあった場合、新しいリリースを急いでリリースする代わりに、機能を素早く無効化できます。

この機能を段階的にロールアウトするために、「Live Chat Widget」という名前の[フィーチャーフラグを作成]({{site.baseurl}}/developer_guide/feature_flags/create)できます。

![Live Chat Widgetという名前のフィーチャーフラグの詳細例。IDはenable_live_chatです。このフィーチャーフラグの説明には、ライブチャットウィジェットがサポートページに表示されると記載されています。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

アプリのコードでは、Brazeのフィーチャーフラグが有効な場合にのみ**Start Live Chat**ボタンを表示します。

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

{% alert note %}
`braze.featureFlags.featureFlags`または`braze.featureFlags.featureFlag(id:)`を読み込むと、SDKが初期化後の操作を完了するまで呼び出しスレッドがブロックされます。メインスレッドやレイテンシが重要なコンテキストでは、代わりに[`getAllFeatureFlags(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/getallfeatureflags(_:))を使用してください。

```swift
// Non-blocking — completion handler always delivers on the main thread.
braze.featureFlags.getAllFeatureFlags { flags in
  let liveChatEnabled = flags.first(where: { $0.id == "enable_live_chat" })?.enabled ?? false
  liveChatView.isHidden = !liveChatEnabled
}
```

Objective-Cの場合:

```objc
[braze.featureFlags getAllFeatureFlagsWithCompletion:^(NSArray<BRZFeatureFlag *> *flags) {
  // Use `flags` here.
}];
```
{% endalert %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### アプリ変数のリモート制御 {#remotely-control-app-variables}

フィーチャーフラグを使用して、本番環境でアプリの機能を変更できます。これはモバイルアプリにとって特に重要で、アプリストアの承認プロセスにより全ユーザーへの変更の迅速な展開が困難です。

例えば、マーケティングチームがアプリのナビゲーションに現在のセールやプロモーションを表示したいとします。通常、エンジニアには変更に1週間のリードタイムとアプリストアレビューに3日間が必要です。しかし、感謝祭、ブラックフライデー、サイバーマンデー、ハヌカ、クリスマス、新年がすべて2か月以内にあるため、これらのタイトなスケジュールに対応できません。

フィーチャーフラグを使用すれば、Brazeにアプリのナビゲーションリンクのコンテンツを制御させ、マーケティングマネージャーが数日ではなく数分で変更を行えるようになります。

この機能をリモート設定するために、`navigation_promo_link`という新しいフィーチャーフラグを作成し、以下の初期プロパティを定義します。

![汎用のセールページを指すリンクとテキストのプロパティを持つフィーチャーフラグ。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

アプリでは、Brazeのgetterメソッドを使用してこのフィーチャーフラグのプロパティを取得し、それらの値に基づいてナビゲーションリンクを構築します。

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

これで、感謝祭の前日にBrazeダッシュボードでプロパティの値を変更するだけで済みます。

![感謝祭セールページを指すリンクとテキストのプロパティを持つフィーチャーフラグ。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

その結果、次にアプリを読み込んだ人には新しい感謝祭のセール情報が表示されます。

### メッセージの連携 {#message-coordination}

フィーチャーフラグを使用して、機能のロールアウトとメッセージングを同期させ、プロダクトチームとマーケティングチームの連携を強化できます。フィーチャーフラグを通じて機能リリースとメッセージングを連携させることで、両チームが戦略を整合し、一貫したユーザー体験を作り出すことができます。

例えば、ユーザー向けに新しいロイヤルティプログラムをローンチするとします。マーケティングチームとプロダクトチームが、プロモーションメッセージのタイミングと機能のロールアウトを完璧に連携させるのは難しい場合があります。しかし、キャンバスでフィーチャーフラグを使用すれば、プロダクトチームは特定のオーディエンスに対して機能を有効化する高度なロジックを適用でき、マーケティングチームは同じユーザーに関連するメッセージングを管理できます。

機能のロールアウトとメッセージングを効果的に連携させるために、`show_loyalty_program`という新しいフィーチャーフラグを作成します。初期の段階的リリースでは、キャンバスにフィーチャーフラグの有効化のタイミングと対象を制御させます。現時点では、ロールアウト率を0%のままにし、ターゲットセグメントは選択しません。

![Loyalty Rewards Programという名前のフィーチャーフラグ。IDはshow_loyalty_programで、説明にはこの新しいロイヤルティプログラムがホーム画面とプロフィールページに表示されると記載されています。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

次に、キャンバスで「High Value Customers」セグメントに対して`show_loyalty_program`フィーチャーフラグを有効にする[フィーチャーフラグステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags)を作成します。

![オーディエンス分割ステップを持つキャンバスの例。高価値顧客セグメントがshow_loyalty_programフィーチャーフラグをオンにしています。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

これで、このセグメントのユーザーは新しいロイヤルティプログラムを目にするようになり、有効化後にはメールと調査が自動的に送信され、チームがフィードバックを収集できるようになります。

### 機能の実験 {#feature-experimentation}

フィーチャーフラグを使用して、新機能に関する仮説を実験し検証できます。トラフィックを2つ以上のグループに分割することで、グループ間でフィーチャーフラグの影響を比較し、結果に基づいて最善のアクションを決定できます。

フィーチャーフラグ実験では、合計最大9つのグループを設定できます。1つのコントロールグループと最大8つのバリアントです。

[A/Bテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)は、変数の複数のバージョンに対するユーザーの反応を比較する強力なツールです。

この例では、eコマースアプリに新しいチェックアウトフローを構築しました。ユーザー体験が向上すると確信していますが、アプリの収益への影響を測定するためにA/Bテストを実施したいと考えています。

まず、`enable_checkout_v2`という新しいフィーチャーフラグを作成します。オーディエンスやロールアウト率は追加しません。代わりに、フィーチャーフラグ実験を使用してトラフィックを分割し、機能を有効化し、結果を測定します。

アプリでは、フィーチャーフラグが有効かどうかを確認し、レスポンスに基づいてチェックアウトフローを切り替えます。

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

A/Bテストは[フィーチャーフラグ実験]({{site.baseurl}}/developer_guide/feature_flags/experiments)で設定します。

これで、50%のユーザーには旧体験が表示され、残りの50%には新体験が表示されます。その後、2つのバリアントを分析して、どちらのチェックアウトフローがより高いコンバージョン率をもたらしたかを判断できます。{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![トラフィックを50%ずつの2つのグループに分割するフィーチャーフラグ実験。]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

勝者を決定したら、このキャンペーンを停止し、フィーチャーフラグのロールアウト率を全ユーザーに対して100%に引き上げます。その間にエンジニアリングチームが次のアプリリリースにハードコーディングします。

### セグメンテーション {#segmentation}

**フィーチャーフラグ**フィルターを使用して、フィーチャーフラグが有効になっているかどうかに基づいてセグメントを作成したり、ユーザーにメッセージをターゲティングしたりできます。例えば、アプリのプレミアムコンテンツを制御するフィーチャーフラグがある場合、フィーチャーフラグが有効になっていないユーザーをフィルタリングするセグメントを作成し、そのセグメントにアカウントをアップグレードしてプレミアムコンテンツを閲覧するよう促すメッセージを送信できます。

1. セグメントまたはメッセージのオーディエンスを開きます。
2. **フィーチャーフラグ**フィルターを追加します。
3. フィーチャーフラグを選択します。
4. フィーチャーフラグが有効になっているユーザーを含めるには比較演算子を**is**に設定し、有効になっていないユーザーを含めるには**is not**に設定します。
![フィーチャーフラグの有効値フィルターを使用したBrazeセグメントビルダー。]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

セグメントのフィルタリングの詳細については、[セグメントの作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)を参照してください。

{% alert note %}
再帰的なセグメントを防ぐため、他のフィーチャーフラグを参照するセグメントを作成することはできません。
{% endalert %}

## プランの制限事項 {#plan-limitations}

これらは、無料プランと有料プランにおけるフィーチャーフラグの制限事項です。

| 機能                                                                                                   | 無料版     | 有料版      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [アクティブなフィーチャーフラグ](#active-feature-flags)                                                                     | ワークスペースあたり10 | ワークスペースあたり110 |
| [アクティブなキャンペーン実験]({{site.baseurl}}/developer_guide/feature_flags/experiments)          | ワークスペースあたり1  | ワークスペースあたり100 |
| [フィーチャーフラグキャンバスステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) | 無制限        | 無制限         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プランの制限事項" }

以下のいずれかに該当する場合、フィーチャーフラグはアクティブとみなされ、制限数にカウントされます。

- ロールアウトが0%を超えている
- アクティブなキャンバスで使用されている
- アクティブな実験で使用されている

同じフィーチャーフラグが複数の条件に一致する場合（例：キャンバスで使用されていて、かつロールアウトが50%の場合）でも、制限に対してアクティブなフィーチャーフラグ1つとしてのみカウントされます。

{% alert note %}
フィーチャーフラグの有料版を購入するには、Brazeアカウントマネージャーに連絡するか、Brazeダッシュボードでアップグレードをリクエストしてください。
{% endalert %}