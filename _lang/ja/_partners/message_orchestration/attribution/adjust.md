---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "この参考記事では、Brazeとモバイルアトリビューション・分析企業であるAdjustとの提携について概説しています。Adjustは、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメントすることを可能にします。"
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) は、モバイルアトリビューションおよび分析を扱う企業です。広告ソースのアトリビューションと高度な分析を組み合わせ、総合的なビジネスインテリジェンスを提供しています。

_この統合はAdjustによって管理されています。_

## 統合について {#about-the-integration}

BrazeとAdjustの統合により、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメントできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Adjustアカウント | このパートナーシップを活用するには、Adjustアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| Adjust SDK | 必要なBraze SDKに加えて、[Adjust SDK](https://dev.adjust.com/en/sdk)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1: デバイスIDをマッピングする {#step-1-map-device-ids}

#### Android

Androidアプリをお持ちの場合は、一意のBrazeデバイスIDをAdjustに渡す必要があります。このIDは、Adjust SDKの`addGlobalPartnerParameter()`メソッドで設定できます。`Adjust.initSdk.`でSDKを初期化する前に、次のコードスニペットを含める必要があります。

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation because there is no service disruption.
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration.

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective-C %}

iOSアプリがある場合、IDFVはAdjustによって収集され、Brazeに送信されます。このIDは、Brazeで一意のデバイスIDにマッピングされます。

[iOSアップグレードガイド]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/)で説明されているように、IDFAをBrazeで収集している場合も、BrazeはオプトインしたユーザーのIDFA値を保存します。それ以外の場合は、ユーザーをマッピングするためのフォールバック識別子としてIDFVが使用されます。

{% endtab %}
{% tab Swift %}

iOSアプリを使用している場合は、`useUUIDAsDeviceId`フィールドを`false`に設定することで、IDFVを収集することを選択できます。設定されていない場合、iOSのアトリビューションはAdjustからBrazeに正確にマッピングされない可能性が高くなります。詳細については、「[IDFVの収集]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)」を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
AdjustからBrazeにインストール後のイベントを送信する予定がある場合は、次のことが必要になります。<br><br>1) Adjust SDK内でセッションおよびイベントパラメーターとして`external_id`を必ず追加してください。収益イベント転送では、イベントのパラメーターとして`product_id`も設定する必要があります。イベント転送のためのパートナーパラメーターの定義の詳細については、[Adjustのドキュメント](https://github.com/adjust/sdks)を参照してください。<br><br>2) Adjustに入力する新しいAPIキーを生成します。これを行うには、BrazeダッシュボードのAdjustパートナーページにある**Generate API Key**ボタンを選択します。
{% endalert %}

### ステップ2: Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで**統合** > **テクノロジーパートナー**に移動し、**Adjust**を選択します。

ここでは、RESTエンドポイントが見つかり、Brazeデータインポートキーを生成できます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、Adjustのダッシュボードでポストバックを設定する際に次のステップで使用されます。<br><br>![Adjustテクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーとRESTエンドポイントが表示されています。]({% image_buster /assets/img/attribution/adjust.png %}){: style="max-width:90%;"}

### ステップ3: AdjustでBrazeを設定する {#step-3-configure-braze-in-adjust}

1. Adjustのダッシュボードで**App Settings**、**Partner Setup**、**Add Partners**の順に移動します。
2. **Braze (formerly Appboy)**を選択し、データインポートキーとBraze RESTエンドポイントを入力します。
3. **Save & Close**をクリックします。

### ステップ4: 統合を確認する {#step-4-confirm-the-integration}

BrazeがAdjustからアトリビューションデータを受信すると、BrazeのAdjustテクノロジーパートナーページのステータス接続インジケーターが「Not Connected」から「Connected」に変わり、最後にリクエストが成功したタイムスタンプが含まれます。

このステータスは、インストールアトリビューションに関するデータをBrazeが受信した後にのみ変更されます。Brazeはオーガニックインストールを無視し（Adjustのポストバックから除外）、接続が成功したかどうかを判断する際にカウントしません。

## 利用可能なデータフィールド {#available-data-fields}

提案されたとおりに統合を設定すると、次の表に示すように、BrazeによりAdjustのデータがセグメントフィルターにマッピングされます。

| Adjustデータフィールド | Braze セグメントフィルター |
| --- | --- |
| `{network_name}` | Attributed Source |
| `{campaign_name}` | Attributed キャンペーン |
| `{adgroup_name}` | Attributed Adgroup |
| `{creative_name}` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="利用可能なデータフィールド" }

## FacebookとX（旧Twitter）のアトリビューションデータ {#facebook-and-x-formerly-twitter-attribution-data}

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータをBrazeに送信することができません。

## BrazeでのAdjustクリックトラッキングURL（オプション） {#adjust-click-tracking-urls-in-braze-optional}

Brazeのキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールと再エンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきかについて、データドリブン型の意思決定ができるようになります。

Adjustクリックトラッキングリンクの使用を開始するには、[ドキュメント](https://help.adjust.com/tracking/attribution/tracker-urls)を参照してください。BrazeのキャンペーンにAdjustクリックトラッキングリンクを直接挿入できます。Adjustは、[確率的アトリビューション手法](https://www.adjust.com/blog/attribution-compatible-with-ios14/)を使って、リンクをクリックしたユーザーをアトリビュートします。Brazeのキャンペーンからのアトリビューションの精度を高めるために、Adjustトラッキングリンクにデバイス識別子を付加することをお勧めします。これにより、リンクをクリックしたユーザーを決定論的にアトリビュートできます。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeを使用すると、顧客は[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration/#google-advertising-id)にオプトインできます。GAIDはまた、Adjust SDK統合によってネイティブに収集されます。以下のLiquidロジックを利用することで、GAIDをAdjustクリックトラッキングリンクに含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAdjustはSDK統合を通じてIDFVをネイティブに自動収集します。これはデバイスの識別子として使用できます。以下のLiquidロジックを利用することで、AdjustクリックトラッキングリンクにIDFVを含めることができます。

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**この推奨事項は完全に任意です**<br>
現在、IDFVやGAIDなどのデバイス識別子をクリックトラッキングリンクで使用していない場合、または今後使用する予定がない場合でも、Adjustは確率モデリングを介してこれらのクリックをアトリビュートできます。
{% endalert %}