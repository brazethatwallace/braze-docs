## 前提条件 {#prerequisites}

このチュートリアルを始める前に、Braze SDKが最低バージョン要件を満たしていることを確認してください：

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Web SDKのバナーを表示する {#displaying-banners-for-the-web-sdk}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!step
lines-index.js=5

### 1. デバッグを有効にする（オプション） {#1-enable-debugging-optional}

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-index.js=8-23

### 2. バナーの更新をサブスクライブする {#2-subscribe-to-banner-updates}

`subscribeToBannersUpdates()` を使用して、バナーが更新されるたびに実行されるハンドラーを登録します。ハンドラー内で`braze.getBanner("global_banner")`を呼び出して、最新のプレースメントを取得します。

!!step
lines-index.js=15-22

### 3. バナーを挿入し、コントロールグループを処理する {#3-insert-the-banner-and-handle-control-groups}

バナーが返されたら、`braze.insertBanner(banner, container)`を使用してバナーを挿入します。レイアウトを整えるために、コントロールグループに含まれるバナーは非表示にするか折りたたんでください（例えば、`isControl`が`true`の場合）。

!!step
lines-index.js=25

### 4. バナーを更新する {#4-refresh-your-banners}

SDKを初期化した後、`requestBannersRefresh(["global_banner", ...])`を呼び出して、各セッションの開始時にバナーが更新されるようにします。

この関数はいつでも呼び出して、後からバナーのプレースメントを更新することもできます。

!!step
lines-main.html=3

### 5. バナー用のコンテナを追加する {#5-add-a-container-for-your-banner}

HTMLに新しい`<div>`要素を追加し、`global-banner-container`のようなバナーに関連する短い`id`を付けます。Brazeはこの`<div>`を使用して、バナーをページに挿入します。

{% endscrolly %}