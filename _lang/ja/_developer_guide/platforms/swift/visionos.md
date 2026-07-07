---
nav_title: visionOSサポート
article_title: visionOSサポート
page_order: 7.2
platform:
  - iOS
description: "この記事では、visionOSでサポートされている機能について説明します。"
---

# visionOSサポート {#visionos-support}

> [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)以降、Apple Vision Pro向けのApple空間コンピューティングプラットフォームである[visionOS](https://developer.apple.com/visionos/)でBrazeを活用できます。Brazeを使用したvisionOSサンプルアプリについては、[サンプルアプリ]({{site.baseurl}}/developer_guide/references?tab=swift)を参照してください。

## 完全にサポートされている機能 {#fully-supported-features}

iOSで利用できるほとんどの機能は、visionOSでも利用できます。以下はその例です。

- 分析（セッション、カスタムイベント、購入など）
- アプリ内メッセージング（データモデルとUI）
- Content Cards（データモデルとUI）
- プッシュ通知（アクションボタン付きのユーザー可視通知とサイレント通知）
- フィーチャーフラグ
- ロケーション分析

## 部分的にサポートされている機能 {#partially-supported-features}

一部の機能はvisionOSでは部分的にしかサポートされていませんが、Appleが将来的にこれらに対応する可能性があります。

- リッチプッシュ通知
  - 画像はサポートされています。
  - GIFと動画はプレビューサムネイルが表示されますが、再生することはできません。
  - オーディオ再生はサポートされていません。
- Push Stories
  - Push Storiesページのスクロールと選択はサポートされています。
  - **Next**を使用したPush Storiesページ間のナビゲーションはサポートされていません。

## サポートされていない機能 {#unsupported-features}

- ジオフェンスモニタリングはサポートされていません。Appleは、リージョンモニタリング用のCore Location APIをvisionOSで利用可能にしていません。
- ライブアクティビティはサポートされていません。現在、ActivityKitはiOSとiPadOSでのみ利用可能です。