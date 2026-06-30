---
nav_title: iOS 17 アップグレードガイド
article_title: iOS 17 アップグレードガイド
page_order: 7
platform:
  - iOS
description: "この記事では、SDKをシームレスにアップグレードするために役立つ、iOS 17リリースに関するインサイトを紹介します。"
hidden: true
noindex: true
---

# iOS 17 アップグレードガイド {#ios-17-upgrade-guide}

> BrazeがこれからのiOSリリースに向けてどのように準備しているか気になりますか？この記事では、iOS 17リリースに関するインサイトをまとめ、あなたとユーザーにシームレスな体験を提供するお手伝いをします。

## iOS 17とXcode 15の互換性 {#ios-17-and-xcode-15-compatibility}

Braze Swift SDKとObjective-C SDKはどちらもXcode 14およびXcode 15と下位互換性があり、iOS 17デバイスと互換性があります。

## iOS 17の変更点 {#changes-in-ios-17}

### リンクトラッキングとUTMパラメータの削除 {#link-tracking-and-utm-parameter-stripping}

iOS 17の重要な変更点の1つは、SafariでUTMパラメータをブロックすることです。UTMパラメータはURLに追加されるコードの一部であり、メール、SMS、その他のメッセージングチャネルの効果を測定するためにマーケティングキャンペーンで頻繁に使用されます。

この変更はBrazeメールのクリックトラッキングおよびSMSリンク短縮送信には影響しません。

### App Tracking Transparency {#app-tracking-transparency}

Appleは、ユーザーが他社のアプリやWebサイト上のアクティビティへのアプリのアクセスをコントロールできるようにする[Ad Tracking Transparency (ATT)](https://support.apple.com/en-us/HT212025)の範囲を拡大することを発表しました。iOS 17のリリースには、プライバシーマニフェストとコード署名という2つの重要なATT機能が含まれています。

#### プライバシーマニフェスト {#privacy-manifests}

Appleでは、アプリとサードパーティのSDKがデータを収集する理由と、そのデータ収集方法を説明するプライバシーマニフェストファイルが必要になりました。iOS 17.2から、Appleはエンドユーザーが ATTプロンプトを受け入れるまで、アプリ内のすべての宣言されたトラッキングエンドポイントをブロックします。

Brazeは、宣言されたトラッキングデータを自動的に専用の`-tracking`エンドポイントにリルートする新しい柔軟なAPIとともに、独自のプライバシーマニフェストをリリースしました。詳細については、[Brazeプライバシーマニフェスト]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest)を参照してください。

#### コード署名 {#code-signing}

コード署名により、サードパーティのSDKをアプリケーションで使用する開発者は、Xcodeで以前のバージョンと同じ開発者が署名したことを検証できます。

### Braze SDKとプライバシー {#braze-sdk-and-privacy}

Appleはまた、2023年後半に「プライバシーに影響を与える」と見なされるサードパーティSDKのリストを公開することも発表しました。これらのSDKは、Appleによってユーザーのプライバシーに特に大きな影響を与えると予想されています。

従来のトラッキングSDKが複数のWebサイトやアプリケーションにわたってユーザーを監視するように設計されているのに対し、Braze SDKはファーストパーティデータのメッセージングとユーザー体験に焦点を当てています。

Braze SDKがこのリストに含まれるとは予想していませんが、この状況を注意深く監視し、必要なアップデートをリリースする予定です。