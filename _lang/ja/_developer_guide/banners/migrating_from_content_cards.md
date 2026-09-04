---
nav_title: "Content Cardsから移行する"
article_title: "Content Cardsからバナーへ移行する"
description: "Content Cardsからバナーへの移行方法について、サポートされている全SDKのコード例、制限事項、利点を含めて説明します。"
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Content Cardsからバナーへ移行する {#migrate-from-content-cards-to-banners}

> このガイドは、バナー形式のメッセージングユースケースにおいて、Content Cardsからバナーへの移行を支援するものです。バナーは、アプリケーション内の特定の配置に表示される、インラインで持続的なアプリ内メッセージおよびWebメッセージに最適です。

## なぜBannersに移行するのか？ {#why-migrate-to-banners}

- エンジニアリングチームがカスタムContent Cardsを構築または保守している場合、Bannersに移行することでその継続的な投資を削減できます。Bannersを使えばマーケターがUIを直接コントロールできるため、開発者は他の作業に集中できます。
- 新しいホームページメッセージ、オンボーディングフロー、または永続的なお知らせを立ち上げる場合は、Content Cardsで構築するのではなく、Bannersから始めましょう。リアルタイムのパーソナライゼーション、30日間の有効期限なし、サイズ制限なし、ネイティブの優先順位付けを初日から活用できます。
- 30日間の有効期限の制約を回避したり、複雑な再適格性ロジックを管理したり、古いパーソナライゼーションに不満を感じている場合、Bannersはこれらの問題をネイティブに解決します。

Bannersは、バナースタイルのメッセージングにおいてContent Cardsよりもいくつかの利点を提供します。

### 制作の加速 {#accelerated-production}

- **継続的なエンジニアリングサポートの削減**: マーケターはドラッグ＆ドロップエディターとカスタムHTMLを使用してカスタムメッセージを作成でき、カスタマイズに開発者の支援を必要としません
- **柔軟なカスタマイズオプション**: エディターで直接デザインしたり、HTMLを使用したり、カスタムプロパティで既存のデータモデルを活用したりできます

### より良いUX {#better-ux}

- **ダイナミックなコンテンツ更新**: BannersはリフレッシュのたびにLiquidロジックと適格性を更新し、ユーザーが常に最も関連性の高いコンテンツを見られるようにします
- **ネイティブの配置サポート**: メッセージはフィードではなく特定のコンテキストに表示されるため、より適切な文脈的関連性を提供します
- **ネイティブの優先順位付け**: カスタムロジックなしで表示順序をコントロールでき、メッセージの階層管理が容易になります

### 永続性 {#persistence}

- **有効期限の制限なし**: Bannersキャンペーンには、Content Cardsのような30日間の有効期限がないため、メッセージを真に永続的に表示できます

## 移行のタイミング {#when-to-migrate}

以下のような用途でContent Cardsを使用している場合は、バナーへの移行を検討してください。

- ホームページのヒーロー、商品ページのプロモーション、チェックアウトオファー
- 永続的なナビゲーションのお知らせやサイドバーメッセージ
- 30日以上継続して配信される常時オンのメッセージ
- リアルタイムのパーソナライゼーションと適格性判定が必要なメッセージ

## Content Cardsを引き続き使用すべき場合 {#when-to-keep-content-cards}

以下のような要件がある場合は、Content Cardsを引き続き使用してください。

- **フィード体験：**複数のスクロール可能なメッセージやカードベースの「受信トレイ」を含むユースケース。
- **特定の機能：**プロモーションコードを必要とするメッセージ。バナーはこれらをネイティブにサポートしていません。バナーは早期アクセスで[Connected Content]({{site.baseurl}}/developer_guide/banners#connected-content)をサポートしています。
- **トリガー配信：**APIトリガーまたはアクションベースの配信を厳密に必要とするユースケース。バナーはAPIトリガーやアクションベースの配信をサポートしていませんが、リアルタイムの適格性評価により、ユーザーは更新のたびにセグメントメンバーシップに基づいて即座に適格または不適格になります。

## 移行ガイド {#migration-guide}

### 前提条件 {#prerequisites}

移行する前に、Braze SDKが最小バージョン要件を満たしていることを確認してください。

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

却下と再適格性には、以下の最小SDKバージョンが必要です。

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### 更新を購読する {#subscribe-to-updates}

#### Content Cardsのアプローチ {#content-cards-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### バナーのアプローチ {#banners-approach}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("sample_placement_id").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### コンテンツを表示する {#display-content}

{% alert note %}
Content Cardsはカスタム UI ロジックで手動レンダリングできますが、バナーはSDKの標準メソッドでのみレンダリングできます。
{% endalert %}

#### Content Cardsのアプローチ

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getCachedContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### バナーのアプローチ

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### 分析を記録する（カスタム実装） {#log-analytics-custom-implementations}

{% alert note %}
Content Cardsとバナーはどちらも、デフォルトの UI コンポーネントを使用する場合は分析を自動的にトラッキングします。以下の例は、独自の UI を構築するカスタム実装向けです。
{% endalert %}

#### Content Cardsのアプローチ

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
  card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
  card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
  Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
  braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### バナーのアプローチ

{% tabs %}
{% tab Web %}

{% alert important %}
`insertBanner()` を使用する場合、分析は自動的にトラッキングされます。`insertBanner()` を使用する場合は、手動ロギングを使用しないでください。
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
BannerView を使用する場合、分析は自動的にトラッキングされます。BannerView を使用する場合は、手動ロギングを使用しないでください。
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
BannerUIView を使用する場合、分析は自動的にトラッキングされます。デフォルトの BannerUIView を使用する場合は、手動ロギングを使用しないでください。
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
BrazeBannerView を使用する場合、分析は自動的にトラッキングされます。手動ロギングは不要です。
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
BrazeBannerView を使用する場合、分析は自動的にトラッキングされます。手動ロギングは不要です。
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### プロパティを取得する {#getting-properties}

#### Content Cardsのアプローチ

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### バナーのアプローチ

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### コントロールグループを処理する {#handling-control-groups}

#### Content Cardsのアプローチ

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### バナーのアプローチ

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementId='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## 制限事項 {#limitations}

Content Cardsからバナーに移行する際は、以下の制限事項に注意してください。

### トリガーメッセージの移行 {#migrating-triggered-messages}

バナーはスケジュール配信キャンペーンのみをサポートしています。以前APIトリガーまたはアクションベースだったメッセージを移行するには、セグメントベースのターゲティングに変換してください。

- **例：** APIで「プロフィール完成」カードをトリガーする代わりに、過去7日間にサインアップしたがプロフィールを完成していないユーザーのセグメントを作成します。
- **リアルタイム適格性：** ユーザーは、リフレッシュのたびにセグメントメンバーシップに基づいて即座にバナーの対象になったり対象外になったりします。

### 機能の違い {#feature-differences}

| 機能 | Content Cards | バナー |
|---------|--------------|---------|
| **コンテンツ構造** |
| フィード内の複数カード | ✅ サポート | ✅ カルーセルのような実装を実現するために複数のプレースメントを作成できます。プレースメントごとに返されるバナーは1つのみです。 |
| 複数プレースメント | N/A | ✅ 複数プレースメントをサポート |
| カードタイプ（クラシック、キャプション付き、画像のみ） | ✅ 複数の定義済みタイプ | ✅ 単一のHTMLベースのバナー（より柔軟） |
| **コンテンツ管理** |
| ドラッグ＆ドロップエディター | ❌ カスタマイズには開発者が必要 | ✅ マーケターが開発なしで作成・更新可能 |
| カスタムHTML/CSS | ❌ カード構造に限定 | ✅ 完全なHTML/CSSサポート |
| カスタマイズ用のキーと値のペア | ✅ 高度なカスタマイズに必要 | ✅ 高度なカスタマイズ用の「プロパティ」と呼ばれる厳密に型付けされたキーと値のペア |
| メッセージエクストラ | ✅ サポート | ❌ 現在サポートされていません |
| **永続性と有効期限** |
| カードの有効期限 | ✅ サポート（30日間の制限） | ✅ サポート（有効期限の制限なし） |
| 真の永続性 | ❌ 最大30日間 | ✅ 無制限の永続性 |
| **表示とターゲティング** |
| フィードUI | ✅ デフォルトフィードが利用可能 | ❌ プレースメントベースのみ |
| コンテキスト固有のプレースメント | ❌ フィードベース | ✅ ネイティブプレースメントサポート |
| 優先順位付け | ❌ カスタムロジックが必要 | ✅ ネイティブの優先順位付け |
| **ユーザーインタラクション** |
| 手動での非表示 | ✅ サポート | ✅ サポート |
| 非表示後の再適格性 | ❌ カスタムフィルターまたはキャンペーンロジックが必要 | ✅ デフォルトの待機期間 |
| ピン留めカード | ✅ サポート | N/A |
| **分析** |
| 自動分析（デフォルトUI） | ✅ サポート | ✅ サポート |
| 優先度ソート | ❌ サポートされていません | ✅ サポート |
| **コンテンツの更新** |
| Liquidテンプレートのリフレッシュ | ❌ 送信/起動時にカードごとに1回 | ✅ リフレッシュのたびに更新 |
| 適格性のリフレッシュ | ❌ 送信/起動時にカードごとに1回 | ✅ セッションごとに更新 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="機能の違い" }

### プロダクトの制限事項 {#product-limitations}

- プレースメントごとに最大25件のアクティブメッセージ。
- リフレッシュリクエストごとに最大10件のプレースメントID。これを超えるリクエストは切り捨てられます。

### SDKの制限事項 {#sdk-limitations}

- バナーは現在、.NET MAUI（Xamarin）、Cordova、Unity、Vega、またはTVプラットフォームではサポートされていません。
- 前提条件に記載されている最小SDKバージョンを使用していることを確認してください。

## 関連記事 {#related-articles}

- [バナープレースメント]({{site.baseurl}}/developer_guide/banners/placements)
- [チュートリアル: プレースメントIDによるバナーの表示]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [バナー分析]({{site.baseurl}}/developer_guide/banners/analytics)
- [バナーFAQ]({{site.baseurl}}/developer_guide/banners/faq)