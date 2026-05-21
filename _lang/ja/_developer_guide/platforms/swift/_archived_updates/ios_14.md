---
nav_title: iOS 14アップグレードガイド
article_title: iOS 14 SDKアップグレードガイド
page_order: 7
platform: iOS
description: "この参考記事では、iOS 14 SDKのアップデートについて、ジオフェンス、ロケーションターゲティング、IDFAなどの変更点を紹介しています。"
hidden: true
noindex: true
---

# iOS 14 SDKアップグレードガイド {#ios-14-sdk-upgrade-guide}

> このガイドでは、iOS 14で導入されたBraze関連の変更と、Braze iOS SDK統合に必要なアップグレード手順について説明します。iOS 14の新しいアップデートの完全なリストについては、Appleの[iOS 14ページ](https://www.apple.com/ios/ios-14/)を参照してください。

{% alert tip %}
iOS 14.5以降、**IDFA**の収集と[特定のデータ共有](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)には、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)フレームワークの許可プロンプトが必要になります（[詳細はこちら](#idfa)）。
{% endalert %}

#### iOS 14の破壊的変更のまとめ {#summary-of-ios-14-breaking-changes}

- iOS 14 / Xcode 12を対象とするアプリは、[公式iOS 14リリース](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0)を使用する必要があります。
- 新しい_おおよその位置情報_パーミッションを選択したユーザーに対して、ジオフェンスは[iOSでサポートされなくなりました](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization)。
- 「Last Known Location」ターゲティング機能を使用するには、_おおよその位置情報_パーミッションとの互換性のため、Braze iOS SDK v3.26.1以降へのアップグレードが必要です。Xcode 12を使用している場合は、v3.27.0以降にアップグレードする必要があります。
- iOS 14.5以降、IDFAの収集と[特定のデータ共有](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track)には、新しい[AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency)フレームワークの許可プロンプトが必要になります。
- キャンペーンターゲティングや分析のために「Ad Tracking Enabled」フィールドを使用する場合は、Xcode 12にアップグレードし、新しいAppTrackingTransparencyフレームワークを使用してユーザーのオプトインステータスを報告する必要があります。

## アップグレードの概要 {#upgrade-summary}

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

| アプリの使用状況 | アップグレードの推奨 | 説明 |
|------|--------|---|
| Xcode 12 | **iOS SDK v3.27以降にアップグレードしてください** | Xcode 12を使用しているお客様は、互換性を確保するためにv3.27.0以降を使用する必要があります。iOS 14の互換性に関連する問題や質問がある場合は、新しい[GitHub issue](https://github.com/Appboy/appboy-ios-sdk/issues)を開いてください。|
| 最新の位置情報 | **iOS SDK v3.26.1以降にアップグレードしてください** | 最新の位置情報ターゲティング機能を使用しており、まだXcode 11を使用している場合は、新しい_おおよその位置情報_機能をサポートするiOS SDK v3.26.1以降にアップグレードする必要があります。古いSDKでは、ユーザーがiOS 14にアップグレード_し_、おおよその位置情報を選択した場合、位置情報を確実に収集できません。<br><br>アプリがiOS 14をターゲットにしていなくても、ユーザーがiOS 14にアップグレードし、新しい位置情報精度オプションを使い始める可能性があります。iOS SDK v3.26.1以降にアップグレードしていないアプリでは、iOS 14デバイスでユーザーが_おおよその位置情報_を提供した場合、位置情報属性を確実に収集できません。|
| IDFA広告トラッキングID | **Xcode 12とiOS SDK v3.27へのアップグレードが必要な場合があります** | 2021年のある時点で、AppleはIDFAの収集に許可プロンプトを要求し始める予定です。その時点で、IDFAの収集を続行するには、アプリをXcode 12にアップグレードし、新しい`AppTrackingTransparency`フレームワークを使用する必要があります。IDFAをBraze SDKに渡す場合は、その時点でv3.27.0以降にもアップグレードする必要があります。<br><br>新しいiOS 14のAPIを使用していないアプリは、2021年にAppleがこの変更を実施し始めた後、IDFAを収集できなくなり、代わりに空白のID（`00000000-0000-0000-0000-000000000000`）を収集することになります。アプリに適用されるかどうかの詳細については、[IDFAの詳細](#idfa)を参照してください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Upgrade summary" }


## iOS 14の動作変更 {#ios-14-behavior-changes}

### おおよその位置情報の許可 {#approximate-location-permission}

![正確な位置情報]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### 概要 {#overview}

位置情報の許可をリクエストする際、ユーザーは_正確な位置情報_（以前の動作）を提供するか、新しい_おおよその位置情報_を提供するかを選択できるようになりました。おおよその位置情報では、正確な座標ではなく、ユーザーがいるより広い半径が返されます。

#### ジオフェンス {#geofences}

新しい_おおよその位置情報_パーミッションを選択したユーザーに対して、ジオフェンスは[iOSでサポートされなくなりました](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization)。Braze SDK統合にアップデートは必要ありませんが、ジオフェンスに依存するキャンペーンについては、[ロケーションベースのマーケティング戦略](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/)を調整する必要があるかもしれません。

#### ロケーションターゲティング {#location-tracking}

_おおよその位置情報_が付与されたときにユーザーの_最新の既知の位置情報_を引き続き収集するには、アプリをBraze iOS SDK v3.26.1以降にアップグレードする必要があります。ただし、位置情報の精度は低くなることに留意してください。当社のテストでは、最大で12,000メートル（7マイル以上）に達しました。Brazeダッシュボードの_最新の既知の位置情報_ターゲティングオプションを使用する際は、新しい_おおよその位置情報_を考慮して、位置の半径を必ず大きくしてください（少なくとも半径1マイル/1.6kmを推奨します）。

Braze iOS SDKをv3.26.1以降にアップグレードしていないアプリでは、iOS 14デバイスで_おおよその位置情報_が付与された場合、位置情報トラッキングを使用できなくなります。

すでに位置情報アクセスを許可しているユーザーは、アップグレード後も引き続き_正確な位置情報_を提供します。

Xcode 12を使用している場合は、v3.27.0以降にアップグレードする必要があります。

おおよその位置情報の詳細については、Appleの[What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/) WWDCビデオを参照してください。

### IDFAとアプリトラッキングの透明性 {#idfa}

#### 概要

IDFA（Identifier for Advertisers）は、広告およびアトリビューションパートナーとのクロスデバイストラッキングのためにAppleが提供する識別子であり、個人のApple IDに紐付けられています。

iOS 14.5からは、IDFAに対する明示的なユーザーの同意を収集するために、新しい許可プロンプト（新しい`AppTrackingTransparency`フレームワークによって起動される）を表示する必要があります。「他社が所有するアプリやWebサイトでユーザーを追跡する」ためのこの許可プロンプトは、位置情報をリクエストするようにユーザーにプロンプトを出すのと同様にリクエストされます。

ユーザーがプロンプトを受け入れない場合、またはXcode 12の`AppTrackingTransparency`フレームワークにアップグレードしない場合、空白のIDFA値（`00000000-0000-0000-0000-000000000000`）が返され、アプリは再度ユーザーにプロンプトを出すことができなくなります。

{% alert important %}
これらのIDFAアップデートは、エンドユーザーがデバイスをiOS 14.5にアップグレードした後に有効になります。IDFAの収集を計画している場合は、Xcode 12でアプリが新しい`AppTransparencyFramework`を使用していることを確認してください。
{% endalert %}

#### Braze IDFAコレクションの変更点 {#changes-to-braze-idfa-collection}
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Brazeは、アプリがユーザーのIDFA値をBraze SDKに提供することを引き続き許可します。

2. オプションの自動IDFAコレクションで条件付きコンパイルを行う`ABK_ENABLE_IDFA_COLLECTION`コンパイルマクロは、iOS 14では機能しなくなり、3.27.0で削除されました。

3. キャンペーンターゲティングや分析のために「Ad Tracking Enabled」フィールドを使用する場合は、Xcode 12にアップグレードし、新しいAppTrackingTransparencyフレームワークを使用して、ユーザーのオプトインステータスを報告する必要があります。この変更の理由は、iOS 14では古い[`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled)フィールドが常にNoを返すためです。

4. アプリがBrazeのexternal IDとしてIDFAまたはIDFVを使用していた場合、これらの識別子からUUIDに移行することを強く推奨します。external IDの移行に関する詳細については、[external ID移行APIエンドポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)を参照してください。

Appleの[プライバシーに関する更新](https://developer.apple.com/app-store/user-privacy-and-data-use/)と新しい[アプリトラッキングの透明性フレームワーク](https://developer.apple.com/documentation/apptrackingtransparency)について詳しくはこちらをご覧ください。

### プッシュ認証 {#push-provisional-auth}

{% alert important %}
iOS 14には、暫定プッシュ承認に関する変更は含まれていません。iOS 14の以前のベータ版で、Appleは変更を導入しましたが、その後以前の動作に戻されています。
{% endalert %}

## iOS 14の新機能 {#ios-14-new-features}

### アプリのプライバシーとデータ収集の概要 {#app-privacy}

2020年12月8日以降、App Storeへのすべての提出には、[Appleの新しいApp Privacy基準](https://developer.apple.com/app-store/app-privacy-details/)を遵守するための追加のステップが必要となります。

#### Apple Developer Portalアンケート {#apple-developer-portal-questionnaire}

_Apple Developer Portal_で：
* アプリまたはサードパーティパートナーがデータを収集する方法を説明するアンケートに記入するよう求められます。
  * このアンケートは、App Storeに掲載されている最新のリリースを常に反映したものであることが求められます。
  * アンケートは、新しいアプリの提出がなくても更新される可能性があります。
* アプリのプライバシーポリシーURLへのリンクを貼り付ける必要があります。

アンケートに記入する際には、法務チームに相談し、以下の分野でのBrazeの使用が開示要件にどのように影響するかを検討してください。

#### Brazeのデフォルトのデータ収集 {#braze-default-data-collection}
**識別子** - 匿名のデバイス識別子は、Braze SDKによって常に収集されます。これは現在、デバイスのIDFV（ベンダーの識別子）に設定されています。

**利用データ** - Brazeのセッションデータ、および製品のインタラクションを測定するために使用するイベントまたは属性収集が含まれます。

#### オプションのデータ収集 {#optional-data-collection}
Brazeの使用を通じて任意に収集される可能性のあるデータ：

**位置情報** - Braze SDKは、オプションで、おおよその位置情報と正確な位置情報の両方を収集できます。これらの機能はデフォルトでは無効になっています。

**連絡先情報** - これには、ユーザーのIDに関連するイベントや属性を含めることができます。

**購入** - これには、ユーザーの代わりに記録されたイベントや購入が含まれる可能性があります。

{% alert important %}
これは網羅的なリストではないことに注意してください。Brazeでユーザーに関するその他の情報を手動で収集する場合に、その情報がApp Privacy Questionnaireの他のカテゴリに該当する場合は、それらも開示する必要があります。
{% endalert %}

この機能の詳細については、[Appleのプライバシーとデータ利用](https://developer.apple.com/app-store/user-privacy-and-data-use/)を参照してください。