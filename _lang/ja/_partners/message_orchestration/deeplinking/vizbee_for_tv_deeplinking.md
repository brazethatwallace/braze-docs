---
nav_title: Vizbee
article_title: Vizbee (TV ディープリンク)
alias: /partners/vizbee/
page_type: partner
description: "このリファレンス記事では、BrazeとVizbeeのパートナーシップと、これを利用してTVディープリンクをサポートする方法について説明します。"
search_tag: Partner

---
# Vizbee {#vizbee}

> [Vizbee](https://vizbee.tv/)は、ご家庭のすべてのスマートフォンとスマートテレビを1つのシームレスなデバイスとして連携させ、優れたユーザーエクスペリエンスを実現します。Vizbeeは、通知、ディープリンク、メールなどの既存のモバイルアプリマーケティングチャネルを使用して、すべてのコネクテッドTV（CTV）デバイス（Roku、FireTV、Samsung TV、LG TVなど）でシームレスに視聴者を獲得し、エンゲージメントを高めることができます。

_この統合はVizbeeによって維持されています。_

## 統合について {#about-the-integration}

BrazeとVizbeeの統合により、モバイルデバイスとCTVデバイスの両方でストリーミングアプリの視聴者を獲得・維持するためのマーケティングキャンペーンを、1つのコンソールでスケジュールできます。この統合により、次のことが可能になります。
- ターゲットユーザーへのモバイル通知をスケジュールできます。タップすると、モバイルアプリでの視聴や、近くにあるストリーミングデバイスやテレビでのシームレスな再生が可能になります。
- ターゲットユーザーへのメールマーケティングキャンペーンをスケジュールできます。タップすると、RokuやFireTVなどのCTVデバイスへのCTVアプリの自動インストールやサインインが可能になります。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Vizbeeアカウント | このパートナーシップを利用するには、[Vizbee](https://vizbee.tv/)アカウントが必要です。Vizbeeでアプリを登録し、Vizbee IDを割り当てる必要があります。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリをサポートしています。プラットフォームによっては、アプリケーションにコードスニペットが必要になる場合があります。 |
| Vizbee SDK | 必要なBraze SDKに加えて、Vizbee SDKをインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

Vizbeeの[SDK統合ガイド](https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity)に従って、VizbeeとBrazeの統合を開始してください。ここでは、モバイルからテレビへのディープリンク、テレビアプリのインストール、視聴アトリビューションに関するガイダンスを確認できます。

### インストールおよびアトリビューションレポートの表示 {#vizbee-tv-app-installs-viewership-attribution}

VizbeeとBrazeを使用すると、モバイルとCTVデバイスにまたがるキャンペーンの総合的なパフォーマンスを表示することもできます。Vizbee SDKはカスタムイベントをBraze SDKに送信します。カスタムイベントは、Brazeダッシュボードのキャンペーンレポートで確認できます。