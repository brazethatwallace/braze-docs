---
nav_title: Push Max
article_title: Push Max
page_type: reference
description: "Push Maxは、失敗したプッシュ通知を追跡し、ユーザーが受信しやすいタイミングでプッシュを再送信することで、Androidプッシュ通知を強化します。"

permalink: /user_guide/channels/push/platform_specific_resources/android/push_max/
platform: Android
channel:
  - Push

---

# Push Max

> Push Maxについて、また[中国OEMデバイス]({{site.baseurl}}/user_guide/channels/push/best_practices/chinese_push_deliverability)へのAndroidプッシュ通知の配信性を向上させるためにこの機能をどのように活用できるかを説明します。

## Push Maxとは {#what-is-push-max}

Push Maxは、失敗したプッシュ通知を追跡し、ユーザーが受信しやすいタイミングでプッシュを再送信することで、Androidプッシュ通知を強化します。

Xiaomi、OPPO、Vivoなどの中国のオリジナル機器メーカー（OEM）が製造する一部のAndroidデバイスは、バッテリー寿命を延ばすために強力なバッテリー最適化スキームを採用しています。この動作により、バックグラウンドでのアプリ処理が停止されるという意図しない結果が生じ、アプリがフォアグラウンドにない場合、これらのデバイスでのプッシュ通知の配信性が低下する可能性があります。この状況は、アジア太平洋（APAC）市場で最も頻繁に発生します。

## 利用可能条件 {#availability}

- Androidプッシュ通知でのみ利用可能
- アクションベースまたはAPIトリガーメッセージではサポートされていません
- [ユーザーの最後に使用したデバイスにのみ送信する]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#most-recently-used-device)オプションが選択されている場合はサポートされていません

## 前提条件 {#prerequisites}

Push Maxを使用して送信されたプッシュ通知は、少なくとも以下の[最小SDKバージョン]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions)を搭載したデバイスにのみ配信されます。

{% sdk_min_versions android:29.0.1 %}

## Push Maxの使用 {#using-push-max}

{% tabs %}
{% tab キャンペーン %}

キャンペーンでPush Maxを使用するには：

1. プッシュキャンペーンを作成します。
2. プラットフォームとして**Android Push**を選択します。
3. **配信をスケジュール**ステップに移動します。
4. **Send using Push Max**を選択します。

![配信をスケジュールステップのAndroid Push Deliverabilityセクション。「Send using Push Max」オプションが表示されています。]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab キャンバス %}

キャンバスでPush Maxを使用するには：

1. キャンバスにメッセージステップを追加します。
2. プラットフォームとして**Android Push**を選択します。
3. **Delivery Settings**タブに移動します。
4. **Send using Push Max**を選択します。

![Androidプッシュメッセージステップの「Delivery Settings」タブ。「Send using Push Max」オプションが表示されています。]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

以下の2つの機能、インテリジェントタイミングとTime to Liveは、Push Maxと組み合わせて使用することで、Androidプッシュ通知の配信性をさらに向上させることができます。

### インテリジェントタイミング {#intelligent-timing}

Push Maxは、[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)がオンになっている場合に最も効果的に機能します。インテリジェントタイミングは、ユーザーがアプリを使用している可能性が最も高く、プッシュが配信される可能性が最も高い時間を計算してプッシュ通知を送信できます。

### Time to Live（TTL） {#time-to-live-ttl}

Time to Live（TTL）は、Firebase Cloud Messaging（FCM）への失敗したプッシュ通知を追跡し、ユーザーが受信しやすいタイミングで通知を再試行できます。

デフォルトでは、Time to Liveは最大値である28日に設定されています。すべての新しいAndroidプッシュメッセージのデフォルトTTLは、**設定** > **ワークスペース設定** > **プッシュ設定**から短縮できます。また、Androidプッシュ通知を作成する際に**設定**タブでメッセージごとに日数を設定することもできます。

![Time to Liveフィールドが28日に設定されています。]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## 注意事項 {#things-to-know}

### プロモーションコード {#promotion-codes}

Push Maxがオンになっているメッセージでは、Brazeの[プロモーションコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)を使用しないことをお勧めします。

プロモーションコードはユニークであるためです。プロモーションコードを含むプッシュ通知の配信に失敗した場合、Push Maxによってその通知が再送信される際に、新しいプロモーションコードが送信されます。これにより、プロモーションコードが予想よりも早く消費される可能性があります。

### キャンバスのイベントプロパティとエントリプロパティ {#canvas-event-properties-and-entry-properties}

メッセージに[キャンバスのエントリプロパティまたはイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)へのLiquid参照を含めると、Push Maxが期待どおりに動作しない場合があります。これは、Push Maxがメッセージの再送信を試みる際に、エントリプロパティとイベントプロパティが利用できないためです。