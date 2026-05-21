---
nav_title: 非推奨
article_title: 非推奨
page_order: 9
page_type: reference
description: "このページには、非推奨の記事への参照と、非推奨の機能およびサポート対象外の機能のリストが含まれています。"
---

# 非推奨 {#deprecations}

テクノロジーは、Brazeの内外を問わず常に進化しています。当社は、それに追いつくために最善を尽くしています。ここでは、Brazeの起源とその技術、そして現在に至るまでの「かつての時代」にどのように人々を支えてきたかを知ることができます。

存在しなくなった統合や機能の用語を検索してここにたどり着いたかもしれません。これは、テクノロジー業界における当社の進歩と動向について、皆様に常に最新情報を提供することを目的としています。以下のリンクから、非推奨の機能とサポート対象外の機能のリストを確認し、非推奨の記事を読むことができます。

## 非推奨記事 {#deprecated-articles}

- [Android用カスタムプッシュブロードキャストレシーバー]({{site.baseurl}}/releases/deprecations/custom_broadcast_receiver/)
- [Eclipse SDKのセットアップ]({{site.baseurl}}/releases/deprecations/eclipse_setup_deprecated/)
- [TLS 1.0および1.1の非推奨]({{site.baseurl}}/releases/deprecations/tls_deprecation/)
- [Twilio Webhookの統合]({{site.baseurl}}/releases/deprecations/twilio/)
- [Apptimizeのパートナーシップ]({{site.baseurl}}/releases/deprecations/apptimize/)
- [Grouparooのパートナーシップ]({{site.baseurl}}/releases/deprecations/grouparoo/)
- [Shopify `checkout.liquid` の非推奨]({{site.baseurl}}/releases/deprecations/shopify_checkout/)

## 非推奨ログ {#deprecations-log}

### Shopify `checkout.liquid`

**サポートの撤回**: 2024年8月（第1フェーズ）、2025年8月（第2フェーズ）

Shopify `checkout.liquid` のサポートは、2024年8月に非推奨が開始され、2025年8月に終了します。Shopifyは、より安全で、パフォーマンスが高く、カスタマイズ可能な[Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions)に移行する予定です。

### Android用カスタムプッシュブロードキャストレシーバー {#custom-push-broadcast-receiver-for-android}

**サポートの撤回**: 2022年10月

プッシュ通知にカスタム`BroadcastReceiver`を使用することは非推奨となりました。代わりに[` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events)を使用してください。

### Grouparooのパートナーシップ {#grouparoo-partnership}

**サポートの撤回**: 2022年4月

Grouparooのサポートは、2022年4月に終了しました。

### Braze Windows SDK

**2022年3月24日**: Braze Windows SDKは非推奨となり、Brazeダッシュボードで新しいWindowsアプリを作成することはできません。<br>
**2022年9月15日**: Windowsアプリに新しいメッセージを送ることはできません。既存のメッセージやデータ収集に影響はありません。<br>
**2024年1月11日**: Brazeは、Windowsアプリからのメッセージ配信やデータ収集を行いません。

### Baiduプッシュ統合 {#baidu-push-integration}

**2022年3月24日**: BrazeのBaiduプッシュ統合は非推奨となり、Brazeダッシュボードで新しいBaiduアプリを作成することはできません。<br>
**2022年9月15日**: 新しいBaiduプッシュメッセージは作成できません。既存のメッセージやデータ収集に影響はありません。<br>
**2024年1月11日**: Brazeは今後、Baiduアプリからのメッセージ配信やデータ収集を行いません。

### appboyBridgeグローバル変数 {#appboybridge-global-variable}

**サポートの撤回**: 2021年5月<br>
**置換**: `brazeBridge`

グローバル変数`appboyBridge`は非推奨となり、`brazeBridge`に置き換えられました。`appboyBridge`は既存のお客様も引き続き使用できますが、`appboyBridge`を使用している場合は`brazeBridge`に移行することをお勧めします。

### Amazon Momentsパートナーシップ {#amazon-moments-partnership}

**サポートの撤回**: 2020年6月

Amazon Momentsのサポートは2020年6月をもって終了しました。Amazon MomentsはAmazon Advertisingに統合され、APIおよび当社との統合は廃止されました。

### Factualパートナーシップ {#factual-partnership}

**サポートの撤回**: 2020年6月

Factualのサポートは、2020年6月に終了しました。Factualは最近Foursquareに買収され、Brazeプラットフォームとの統合はなくなりました。

### Twilio Webhookの統合 {#twilio-webhook-integration}

**サポートの撤回**: 2020年1月

[Twilio Webhook統合]({{site.baseurl}}/partners/twilio/)のサポートは2020年1月31日をもって終了しました。BrazeでSMSサービスに引き続きアクセスしたい場合は、[SMSのドキュメント]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)を参照してください。

### Apptimizeのパートナーシップ {#apptimize-partnership}

**サポートの撤回**: 2019年8月

現在[BrazeでApptimize]({{site.baseurl}}/releases/deprecations/apptimize/)を使用している場合、サービスの中断は発生しません。Apptimizeのカスタム属性をBrazeのユーザープロファイルに設定することもできます。ただし、パートナーとの正式なエスカレーションサポートは提供されません。

### オリジナルのアプリ内メッセージ {#original-in-app-messages}

**サポートの撤回**: 2019年2月<br>
**置換**: [アプリ内メッセージング]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

Brazeは、最新のUXとUIのベストプラクティスに準拠するため、アプリ内メッセージのルック＆フィールを改善し、オリジナルのアプリ内メッセージのサポートを終了しました。

Brazeは、以下のSDKリリースでアプリ内メッセージの新しい形式に移行しました。
- iOS: `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

これらのリリース以前は、Brazeは「オリジナルのアプリ内メッセージ」をサポートしていました。これまでは、新しいリリース前にアプリ内キャンペーンを実行したすべてのお客様に対して、オリジナルのアプリ内メッセージのサポートが提供されていました。すべてのキャンペーン統計はこの変更の影響を受けず、オリジナルのアプリ内メッセージを送信した方は、**キャンペーン**ページの**キャンペーンを作成**ボタンから他のメッセージを送信することができました。

### フィードバックウィジェット {#feedback-widget}

**サポートの撤回**: 2019年7月1日

Braze SDKは、アプリに追加できるフィードバックウィジェットを提供し、ユーザーが`submitfeedback`メソッドを使ってフィードバックを残し、それをDesk.comまたはZendeskに渡し、ダッシュボードで管理できるようにしていました。

### Google Cloud Messaging (GCM)

**サポートの撤回**: Brazeのサポート終了: 2018年7月、Googleによるサポートの終了: 2019年5月29日<br>
**置換**: [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

Googleは、2019年5月29日をもって[GCMのサポートを終了](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html)しました。Brazeは2018年7月にAndroid SDKからGCMのサポートを終了しましたが、これは[Android SDKの変更ログ](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)に記載されています。これは、既存のGCMトークンが引き続き機能し、既存のユーザーにメッセージを送ることができることを意味します。ただし、新規ユーザーにメッセージを送ることはできません。

まだ[Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)に移行していないお客様は、この変更の影響を受ける可能性があります。

FCMに移行していない場合、GCMプッシュトークンの登録はすべて失敗します。アプリが現在GCMをサポートしている場合は、[GCMからFirebase Cloud Messaging (FCM)への移行](https://developers.google.com/cloud-messaging/android/android-migrate-fcm)について開発チームと連携する必要があります。

### Eclipse

**サポートの撤回**: 2014～2015年<br>
**置換**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

GoogleがEclipse Android Developer Tools (ADT) プラグインの[サポートを終了](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)したため、BrazeはEclipse IDEのサポートを中止しました。

移行前にEclipseの統合に関するサポートが必要な場合は、[サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。

### Raw Event Stream (RES) {#the-raw-event-stream-res}

**サポートの撤回**: 2018年7月<br>
**置換**: [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)

Raw Event Streamは[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)の前身であり、Brazeデータの将来に備えて廃止されました。

### アイドル時のディレイ - GCM機能 {#delay-while-idle-gcm-feature}

**サポートの撤回**: 2016年11月

Delay While Idleパラメータは、以前は[GCMプッシュオプション](https://developers.google.com/cloud-messaging/http-server-ref)の一部でした。Googleは2016年11月15日にこのオプションのサポートを撤回しました。以前は、**true**に設定した場合、デバイスがアクティブになるまでメッセージを送信しないことを示していました。

### カスタムエンドポイント {#custom-endpoints}

**サポートの撤回**: 2019年12月

カスタムエンドポイントの廃止。カスタムエンドポイントをお持ちの場合は引き続き使用できますが、Brazeはもう新たに提供しません。