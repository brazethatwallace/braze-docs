---
nav_title: 9月
page_order: 3
noindex: true
page_type: update
description: "この記事には2021年9月のリリースノートが含まれています。"
---

# 2021年9月 {#september-2021}

## iOS 15

### Apple Mailのプライバシー保護 {#apple-mail-privacy-protection}

Appleのメールプライバシー保護 (MPP) は、9月中旬にリリースされたiOS 15、iPadOS 15、macOS Monterey、watchOS 8のApple Mailアプリのユーザーに提供されるプライバシーアップデートです。MPPにオプトインしたユーザーの場合、メールはプロキシサーバーを使用してプリロードされ、画像がキャッシュされ、[開封トラッキング]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#open-tracking-pixel)などの指標のトラッキングピクセルを活用する機能が制限されます。MPPおよびメール到達率の指標に関する問題、またこれらの指標に基づいてトリガーされる既存のキャンペーンやキャンバスに関する問題については、[ドキュメント]({{site.baseurl}}/user_guide/channels/email/best_practices/apple_mail/mpp)を参照してください。

### プッシュ機能 {#push-features}

iOS 15では新しい通知機能が導入され、ユーザーが1日を通して集中力を保ち、頻繁な中断を避けられるようになりました。[中断レベルや関連性スコア]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options)など、これらの新機能のサポートを提供できることをうれしく思います。

## 連絡先カード {#contact-cards}

連絡先カードは、アドレス帳や連絡先帳に簡単にインポートできる、ビジネス情報や連絡先情報を送信するための標準化されたファイル形式です。SMSおよびMMSメッセージ用の連絡先カードをアップロードして作成できるようになりました。組み込みの連絡先カードジェネレーターでの連絡先カードの作成方法について詳しくは、[ドキュメント]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create/contact_card)をご覧ください。

## デフォルトのContent Cardsカスタマイズ {#default-content-cards-customization}

`ABKContentCardsTableViewController`を拡張してすべてのUI要素とContent Cardsの動作をカスタマイズすることで、独自のContent Cardsインターフェイスを作成できます。Content Cardsフィードのカスタマイズ方法の詳細については、[ドキュメント]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)をご覧ください。

## APIレート制限 {#api-rate-limits}

[レート制限]({{site.baseurl}}/api/api_limits)は、2021年9月16日以降にオンボーディングされたすべての顧客に適用されます。

## AndroidおよびFireOS開発者ガイドの更新 {#updates-to-android-and-fireos-developer-guides}

AndroidとFireOSの開発者ガイドが1つの場所に統合されました。専用のFireOS記事は、この[新しいAndroidセクション]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)で利用できます。

## ファネルレポートとリテンションレポートの更新 {#updates-to-funnel-and-retention-reports}

[ファネルレポート]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports)と[リテンションレポート]({{site.baseurl}}/user_guide/analytics/reports/retention_reports)がSMSキャンペーンで利用可能になりました。