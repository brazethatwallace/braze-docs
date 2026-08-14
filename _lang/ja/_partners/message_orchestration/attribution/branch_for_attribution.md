---
nav_title: Branch（アトリビューション）
article_title: Branch（アトリビューション）
alias: /partners/branch_for_attribution/
description: "この参考記事では、あらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援するモバイルリンクプラットフォームであるBrazeとBranchのパートナーシップについて概説しています。"
page_type: partner
search_tag: Partner
---

# Branch（アトリビューション） {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/)はモバイルリンクプラットフォームで、すべてのユーザータッチポイントの包括的なビューを提供することにより、あらゆるデバイス、チャネル、プラットフォームでの獲得、エンゲージメント、測定を支援します。

_この統合はBranchによって管理されています。_

## 統合について {#about-the-integration}

BrazeとBranchの統合により、堅牢なアトリビューションと[ディープリンク]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking)を通じて、ユーザーがいつ、どこで獲得されたかを正確に把握し、ユーザーのジャーニーをパーソナライズできるようになります。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Branchアカウント | このパートナーシップを活用するには、Branchアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| Branch SDK | 必要なBraze SDKに加えて、[Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:デバイスIDをマップする {#step-1-map-device-ids}

#### Android

Androidアプリを使用している場合は、BrazeのユニークなデバイスIDをBranchに渡す必要があります。このIDは、Branch SDKの`setRequestMetadataKey()`メソッドで設定できます。`initSession`を呼び出す前に、次のコードスニペットを含める必要があります。また、Branch SDKでリクエストメタデータを設定する前に、Braze SDKを初期化する必要があります。

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId);
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
2023年2月以前は、Branchアトリビューション統合ではiOSアトリビューションデータのマッチングにおいて、IDFV（Identifier for Vendor）を主要な識別子として使用していました。Objective-Cを使用するBrazeの顧客は、Brazeの`device_id`を取得してインストール時にBranchに送信する必要はありません。サービスの中断が発生しないためです。
{% endalert%}

Swift SDK v5.7.0以降を使用しているお客様で、相互識別子としてIDFVを引き続き使用する場合は、`useUUIDAsDeviceId`フィールドが`false`に設定されていることを確認する必要があります。これにより、統合が中断されることがなくなります。

`true`に設定している場合、BrazeがiOSアトリビューションを適切に照合できるように、アプリのインストール時にBranchにBrazeの`device_id`を渡すために、Swift用のiOSデバイスIDマッピングを実装する必要があります。

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init
}
```

{% endtab %}
{% endtabs %}

### ステップ2:Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Branch**を選択します。

ここでは、RESTエンドポイントが見つかり、Brazeデータインポートキーを生成できます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。Branchのダッシュボードでポストバックを設定する際に、次のステップでデータインポートキーとRESTエンドポイントを使用します。<br><br>![Branchテクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーとRESTエンドポイントが表示されています。]({% image_buster /assets/img/attribution/branch.png %}){: style="max-width:90%;"}

### ステップ3:データフィードを設定する {#step-3-set-up-data-feeds}

1. Branchの**Exports**セクションで、**Data Feeds**を選択します。
2. **Data Feeds Manager**ページで、ページ上部の**Data Integrations**タブを選択します。
3. 利用可能なデータパートナーのリストからBrazeを選択します。
4. Brazeエクスポートページで、Brazeダッシュボードで見つけたデータインポートキーとRESTエンドポイントを入力し、**Enable**を選択します。

### ステップ4:統合を確認する {#step-4-confirm-the-integration}

BrazeがBranchからアトリビューションデータを受信すると、BrazeのBranchテクノロジーパートナーページのステータス接続インジケーターが「Not Connected」から「Connected」に変わり、最後に成功したリクエストのタイムスタンプが含まれます。

このステータスは、Brazeがアトリビュートされたインストールに関するデータを受信した後にのみ変更されます。Brazeはオーガニックインストールを無視し（Branchのポストバックから除外）、接続が成功したかどうかを判断する際にそれらをカウントしません。

## フィールドマッピング {#field-mapping}

Branchのアトリビューションフィールドは、以下のようにBrazeにマッピングされます。

| Branchフィールド | Brazeフィールド |
| --- | --- |
| キャンペーン | `campaign` |
| Channel | `source` |
| Ad Set Name | `adgroup` |
| Ad Name | `ad` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Branchフィールドマッピング" }

## FacebookとX（旧Twitter）のアトリビューションデータ {#facebook-and-x-formerly-twitter-attribution-data}

FacebookおよびX（旧Twitter）のキャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできません。

## BrazeでのBranchクリックトラッキングURL（オプション） {#branch-click-tracking-urls-in-braze-optional}

Brazeのキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきかについて、データドリブン型の意思決定ができるようになります。

Branchのクリックトラッキングリンクを使い始めるには、Branchの[ドキュメント](https://help.branch.io/using-branch/docs/ad-links)を参照してください。BrazeのキャンペーンにBranchのクリックトラッキングリンクを直接挿入できます。その後Branchは、リンクをクリックしたユーザーをアトリビュートするために、[確率的アトリビューション手法](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings)を使用します。Brazeのキャンペーンからのアトリビューションの精度を向上させるために、Branchトラッキングリンクにデバイス識別子を付加することをお勧めします。これにより、リンクをクリックしたユーザーを決定論的にアトリビュートできます。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeではお客様が[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id)にオプトインできます。GAIDはまた、Branch SDKの統合によってネイティブに収集されます。以下のLiquidロジックを利用して、BranchのクリックトラッキングリンクにGAIDを組み込むことができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとBranchの両方がSDKの統合を通じてネイティブにIDFVを自動的に収集します。これはデバイス識別子として使用できます。以下のLiquidロジックを利用して、BranchのクリックトラッキングリンクにIDFVを組み込むことができます。

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**この推奨事項の適用は完全に任意です。**<br>
現在、クリックトラッキングリンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Branchは確率的モデリングによってこれらのクリックをアトリビュートすることができます。
{% endalert %}