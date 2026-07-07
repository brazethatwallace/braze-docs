---
nav_title: プッシュ設定
article_title: プッシュ設定
page_order: 5
page_type: reference
description: "この記事では、Brazeダッシュボードのプッシュ設定の概要について説明します。"
channel: push

---

# プッシュ設定 {#push-settings}

> **プッシュ設定**ページでは、プッシュTTL（Time to Live）やAndroid キャンペーンのデフォルトの FCM 優先度など、プッシュ通知の主要な設定を行うことができます。これらの設定により、プッシュ通知の配信と効果が最適化され、ユーザーの体験が向上します。

## プッシュTTLとは {#what-is-push-ttl}

プッシュTTL（Time to Live）は、キャンペーンの送信時にオフラインのデバイスに対してBrazeがプッシュ通知を配信しようとする時間を制御します。TTLの有効期限が切れた後にデバイスが再接続された場合、メッセージは配信されません。この設定では、ユーザーのデバイスがすでに受信している通知は削除されません。プッシュプロバイダーが通知を配信しようとする時間のみが制御されます。

## デフォルトのプッシュTTL値の設定 {#setting-default-push-ttl-values}

デフォルトでは、BrazeはプッシュTTLを各プッシュメッセージングサービスの最大値に設定します。

| プッシュメッセージングサービス | 最大TTL |
| --- | --- |
| Web（FCMまたはWebプッシュサービス経由） | 28日 |
| Firebase Cloud Messaging (FCM) | 28日 |
| Kindle (ADM) | 31日 |
| Huawei (HMS) | 15日 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Setting default Push TTL values" }

これらの設定は、特定のメッセージに別のTTLが設定されていない限り、すべてのプッシュキャンペーンにグローバルに適用されます。メッセージのTTLを調整するには、[詳細なキャンペーン設定]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#ttl)を参照してください。

別のデフォルトのプッシュTTLを設定するには:

1. **設定** > **設定の管理** > **プッシュ設定**に移動します。
2. Androidプラットフォームごとに、デフォルトの有効期限値を定義します。より正確な制御を行うには、時間や秒などのより小さな増分を設定できます。
3. **Save**を選択して変更を適用します。

![Firebase、Web、Kindle、HuaweiデバイスのプッシュTTL設定。]({% image_buster /assets/img/push_ttl.png %})

## Android キャンペーンのデフォルトのFCM優先度 {#default-fcm-priority-for-android-campaigns}

すべてのAndroidプッシュキャンペーンのデフォルトのFirebase Cloud Messaging（FCM）優先度を設定できます。この優先度によって、プッシュ通知がユーザーのデバイスにどのように配信されるかが決まります。

FCMの優先度オプションは次のとおりです。

| 優先度 | 説明 | ユースケース |
| --- | --- | --- |
| 通常 | バッテリー使用量に合わせて最適化された標準の配信優先度 | 即時の対応を必要としないコンテンツ |
| 高 | メッセージは即座に送信されます | 迅速な配信が必要な時間的制約のある通知 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Default FCM Priority for Android キャンペーン" }

デフォルトのFCM優先度を設定するには:

1. **設定** > **設定の管理** > **プッシュ設定**に移動します。
2. FCM優先度セクションで、デフォルト設定として「通常」または「高」を選択します。
3. **Save**を選択して変更を適用します。

![Androidの配信優先度設定。]({% image_buster /assets/img/push_fcm_priority_settings.png %})

この設定は、特定のキャンペーンの作成時に別の優先度が選択されていない限り、すべての新しいAndroidプッシュキャンペーンにグローバルに適用されます。

{% alert note %}
FCMが、アプリがユーザーに表示される通知やユーザーエンゲージメントにつながらない高優先度メッセージを頻繁に送信していることを検出した場合、それらのメッセージは自動的に通常の優先度に降格される場合があります。
{% endalert %}

FCMの優先度レベルと優先度の降格の詳細については、[詳細なキャンペーン設定]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/#fcm-priority)を参照してください。