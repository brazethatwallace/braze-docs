---
nav_title: アクセシビリティ
article_title: アクセシビリティ
platform: Web
page_order: 22
page_type: reference
description: "この記事では、Brazeがアクセシビリティをどのようにサポートしているかについて説明します。"

---

# アクセシビリティ {#accessibility}

> この記事では、Brazeが統合環境内でアクセシビリティをどのようにサポートしているかについて概説します。

Braze Web SDKは、[Webコンテンツアクセシビリティガイドライン（WCAG 2.1）](https://www.w3.org/TR/WCAG21/)が提供する標準をサポートしています。アクセシビリティ基準を維持するため、すべての新規ビルドにおいてContent Cardsとアプリ内メッセージに対して[100/100のLighthouseスコア](https://developer.chrome.com/docs/lighthouse/accessibility/scoring)を維持しています。

## 前提条件 {#prerequisites}

WCAG 2.1を満たす最小のSDKバージョンはv3.4.0に近いです。ただし、画像タグの重大な修正のため、少なくともv6.0.0へのアップグレードを推奨します。

### 主なアクセシビリティの修正 {#notable-accessibility-fixes}

| バージョン | タイプ | 主な変更点 |
|---------|------|-------------|
| **6.0.0** | **メジャー** | 画像の`<img>`タグ化、`imageAltText`または`language`フィールド、一般的なUIアクセシビリティの改善 |
| **3.5.0** | マイナー | スクロール可能なテキストのアクセシビリティ改善 |
| **3.4.0** | 修正 | Content Cardsの`article`ロール修正 |
| **3.2.0** | マイナー | ボタンの最小タッチターゲット45×45px |
| **3.1.2** | マイナー | 画像のデフォルト代替テキスト |
| **2.4.1** | **メジャー** | セマンティックHTML（`h1`または`button`）、ARIA属性、キーボードナビゲーション、フォーカス管理 |
| **2.0.5** | マイナー | フォーカス管理、キーボードナビゲーション、ラベル |
{: .reset-td-br-1, .reset-td-br-2 aria-label="主なアクセシビリティの修正" }

## サポートされているアクセシビリティ機能 {#supported-accessibility-features}

Content Cardsとアプリ内メッセージでは、以下の機能をサポートしています。

- ARIAロールとラベル
- キーボードナビゲーションのサポート
- フォーカス管理
- スクリーンリーダーによる読み上げ
- 画像の代替テキスト対応

## SDK統合のためのアクセシビリティガイドライン {#accessibility-guidelines-for-sdk-integrations}

アクセシビリティに関する一般的なガイドラインについては、[Brazeでアクセシブルなメッセージを作成する]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility)を参照してください。このガイドでは、Braze Web SDKをWebアプリケーションに統合する際のアクセシビリティを最大限に高めるためのヒントとベストプラクティスを提供します。

### Content Cards

#### 最大高さの設定 {#setting-a-maximum-height}

Content Cardsが縦方向のスペースを過剰に占めるのを防ぎ、アクセシビリティを向上させるために、フィードコンテナに最大高さを設定できます。以下はその例です。

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### ビューポートに関する考慮事項 {#viewport-considerations}

インラインで表示されるContent Cardsについては、以下の例のようにビューポートの制約を考慮してください。

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### アプリ内メッセージ {#in-app-messages}

{% alert warning %}
スライドアップ型のアプリ内メッセージに重要な情報を配置しないでください。スクリーンリーダーではアクセスできません。
{% endalert %}

### モバイルに関する考慮事項 {#mobile-considerations}

#### レスポンシブデザイン {#responsive-design}

SDKにはレスポンシブブレークポイントが含まれています。カスタマイズがさまざまな画面サイズで正しく機能することを確認してください。以下はその例です。

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }

  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### アクセシビリティのテスト {#testing-accessibility}

#### 手動テストチェックリスト {#manual-test-checklist}

以下のタスクを実施して、アクセシビリティを手動でテストしてください。

- Content Cardsとアプリ内メッセージをキーボードのみ（Tab、Enter、Space）で操作する
- スクリーンリーダー（NVDA、JAWS、VoiceOver）でテストする
- すべての画像に代替テキストがあることを確認する
- 色のコントラスト比を確認する（WebAIM Contrast Checkerなどのツールを使用する）
- タッチ操作が可能なモバイルデバイスでテストする
- フォーカスインジケーターが表示されていることを確認する
- モーダルメッセージのフォーカストラッピングをテストする
- すべてのインタラクティブな要素がキーボードで到達可能であることを確認する

### よくあるアクセシビリティの問題 {#common-accessibility-issues}

よくあるアクセシビリティの問題を避けるために、以下を実施してください。

1. **フォーカススタイルを維持する：** SDKのフォーカスインジケーターはキーボードユーザーにとって不可欠です。
2. **`display: none`は非インタラクティブ要素にのみ使用する：** インタラクティブな要素を非表示にするには、`visibility: hidden`または`opacity: 0`を使用してください。
3. **ARIA属性をオーバーライドしない：** SDKは適切なARIAロールとラベルを設定します。
4. **`tabindex`属性を使用する：** これらはキーボードナビゲーションの順序を制御します。
5. **`overflow: hidden`を設定する場合はスクロールを提供する：** スクロール可能なコンテンツがアクセス可能であることを確認してください。
6. **組み込みのキーボードハンドラに干渉しない：** 既存のキーボードナビゲーションが正しく機能することを確認してください。