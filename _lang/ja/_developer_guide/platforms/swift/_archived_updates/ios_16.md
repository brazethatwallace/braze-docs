---
nav_title: iOS 16 アップグレードガイド
article_title: iOS 16 アップグレードガイド
page_order: 7
platform:
  - iOS
description: "この参考記事では、iOS 16、アップグレード方法、SDKの更新などについて説明します。"
hidden: true
noindex: true
---

# iOS 16 SDKアップグレードガイド {#ios-16-sdk-upgrade-guide}

> このガイドでは、iOS 16 (2022) で導入された関連する変更と、Braze iOS SDKインテグレーションへの影響について説明します。完全な移行ガイドについては、[iOS 16 リリースノート](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes)を参照してください。

## iOS 16での変更点 {#changes-in-ios-16}

### Safari Webプッシュ {#safari-web-push}

Appleは、Webプッシュ機能に対する2つの変更を発表しました。

#### デスクトップWebプッシュ (MacOS) {#macos-push}

以前、Appleは独自のSafariプッシュAPIを使用してmacOS (デスクトップ) でのプッシュ通知をサポートしていました。

macOS Ventura (2022年10月24日リリース) 以降、[SafariにはSafariプッシュに加えてWeb Push APIのサポートが追加されました](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos)。これは、他の一般的なブラウザで使用されている既存のクロスブラウザAPI標準です。

すでにBraze経由でSafari用Webプッシュを送信している場合は、変更する必要はありません。

#### モバイルWebプッシュ (iOSおよびiPadOS) {#ios-push}

以前は、iPhoneおよびiPadのSafariはプッシュ通知の受信をサポートしていませんでした。

2023年に、AppleはSafariを介したiPhoneおよびiPadデバイスでのWebプッシュのサポートを追加する予定です。

Brazeは、追加の変更やアップグレードを必要とせずに、この新しいiOSおよびiPadOSのWebプッシュをサポートします。

## iOS 16への準備 {#next-steps}

Braze iOS SDKをiOS 16用にアップグレードする必要はありませんが、他に2つの注目すべき更新があります。

1. Brazeは[新しいSwift SDK](https://github.com/braze-inc/braze-swift-sdk)をリリースしました。これにより、パフォーマンスの向上、新機能、および多くの改善がもたらされます。
2. Braze Swift SDKは、新しい[「ノーコード」プッシュプライマー機能]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)をサポートしています。