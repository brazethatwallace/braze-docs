---
nav_title: iOS 18 へのアップグレード
article_title: iOS 18 へのアップグレード
page_order: 7.1
platform:
  - iOS
description: "この記事では、SDKをシームレスにアップグレードするのに役立つ、iOS 18リリースに関するインサイトを紹介します。"
---

# iOS 18 へのアップグレード {#upgrading-to-ios-18}

> Brazeが次のiOSリリースに向けてどのように準備しているか気になりますか？この記事では、iOS 18のリリースに関するインサイトをまとめており、あなたとユーザーのシームレスなエクスペリエンス作りに役立ちます。

Appleの[WWDC](https://developer.apple.com/wwdc24/)は、2024年6月9日〜11日に開催されました。発表の詳細については、[ブログ記事](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18)をご覧ください。また、BrazeでiOS 18を活用する方法については、以下をお読みください。

## iOS 18の変更点 {#changes-in-ios-18}

### Apple Watchでのライブアクティビティ {#live-activities-on-apple-watch}

[ライブアクティビティ]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)は、watchOS 11でサポートされます。追加の設定は必要ありません。ただし、Appleではウォッチインターフェイスをカスタマイズするオプションが用意されています。

### Apple Vision Pro

Vision Proは現在、中国、日本、シンガポール、オーストラリア、カナダ、フランス、ドイツ、英国で販売されています。[BrazeがvisionOSをどのようにサポートしているか](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support)については、弊社のブログをご覧ください。

### MacOSでのiPhone通知 {#iphone-notifications-on-macos}

Appleの新しい[iPhoneミラーリング](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/)機能により、ユーザーはMacOSデバイスでiPhoneの通知を受け取ることができます。Push Storyの画像やGIFなど、一部のメディアタイプはMacOS通知としてレンダリングできないため、サポートされていない点にご注意ください。

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence)は、iOS 18.1以降を実行しているデバイスで利用できるようになりました。

Brazeユーザーとして知っておくべき最も重要な新機能は[通知サマリー](https://support.apple.com/en-us/108781)です。これは、デバイス上の処理を使用して、1つのアプリから送信される関連するプッシュ通知を自動的にグループ化し、テキストサマリーを生成します。エンドユーザーはサマリーをタップして展開し、最初に送信されたときの各プッシュ通知を表示できます。

これらのサマリーの生成方法の性質上、特定の動作や生成されるテキストを制御することはできません。ただし、プッシュクリックのトラッキングなどの分析機能やレポート機能には影響しません。

![プッシュ通知プレビューサマリーのサンプルスクリーンショット。]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})