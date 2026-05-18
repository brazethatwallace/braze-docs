---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "このリファレンス記事では、BrazeとKochavaのパートナーシップについて説明します。Kochavaは、アトリビューションおよび分析インサイトを提供して、成長のためのデータ活用を支援するモバイルアトリビューションプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Kochava

> [Kochava](https://www.kochava.com/)は、モバイルのアトリビューションと分析を提供し、成長のためのデータ活用を支援します。Kochava Audience Platformでは、アプリキャンペーンの計画、ターゲティング、アクティベーション、測定、最適化を実施できます。

_この統合はKochavaによって管理されています。_

## 統合について {#about-the-integration}

BrazeとKochavaの統合により、アトリビューションデータをBrazeに送信することで、どのキャンペーンがインストールやアプリ内アクティビティなどを促進しているかをより深く理解し、キャンペーン全体の把握を強化できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Kochavaアカウント | このパートナーシップを活用するには、Kochavaアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| Kochava SDK | 必須のBraze SDKに加えて、[Kochava SDK](https://support.kochava.com/sdk-integration/)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

### ステップ1:ユーザーIDをマップする {#step-1-map-user-ids}

#### Android

[Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDKは、セッション開始時にGUID（Globally Unique Identifier）をBraze IDとして生成します。この識別子をKochavaの`IdentityLink`メソッドに渡すことで、Brazeはデータを正しいユーザープロファイルに照合できます。以下の方法でBraze IDを取得します。

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
2023年2月以前は、Kochavaのアトリビューション統合は、iOSのアトリビューションデータを照合するための主要識別子としてIDFV（Identifier for Vendor）を使用していました。Objective-Cを使用しているBrazeのお客様は、サービスの中断がないため、インストール時にBrazeの`device_id`を取得してKochavaに送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0+を使用しているお客様は、相互識別子としてIDFVを引き続き使用するには、`useUUIDAsDeviceId`フィールドが`false`に設定されていることを確認する必要があります。これにより、統合が中断されることがなくなります。`true`に設定している場合、BrazeがiOSアトリビューションを適切に照合できるように、アプリのインストール時にKochavaにBrazeの`device_id`を渡すために、Swift用のiOSデバイスIDマッピングを実装する必要があります。

Brazeには、同じ値を生成する2つのAPIがあります。1つは完了ハンドラを使用し、もう1つは新しいSwiftコンカレンシーサポートを使用します。次のコードスニペットをKochavaの[iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/)の指示に従って修正する必要があることに注意してください。その他のヘルプについては、Kochavaサポートにお問い合わせください。

##### 完了ハンドラ {#completion-handler}
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Swiftコンカレンシー {#swift-concurrency}
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### ステップ2:Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで、**Partner Integrations** > **Technology Partners**に移動し、**Kochava**を選択します。

ここでは、RESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、Kochavaのダッシュボードでポストバックを設定する次のステップで使用されます。<br><br>![Kochavaテクノロジーページにある「インストールアトリビューションのためのデータインポート」ボックス。このボックスには、データインポートキーとRESTエンドポイントが表示されています。]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### ステップ3:Kochavaからのポストバックを設定する {#step-3-set-up-a-postback-from-kochava}

Kochavaダッシュボードに[ポストバックを追加します](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback)。Brazeのダッシュボードで確認したデータインポートキーとRESTエンドポイントの入力を求められます。

### ステップ4:統合を確認する {#step-4-confirm-the-integration}

BrazeがKochavaからアトリビューションデータを受信すると、BrazeのKochavaテクノロジーパートナーページのステータス接続インジケータが「Not Connected」から「Connected」に変わり、最後にリクエストが成功したタイムスタンプが表示されます。

このステータスは、アトリビューション付きインストールに関するデータをBrazeが受信した後にのみ変更されます。Brazeはオーガニックインストールを無視し（Kochavaのポストバックから除外し）、接続が成功したかどうかを判断する際にカウントしません。

## FacebookとX（旧Twitter）のアトリビューションデータ {#facebook-and-x-formerly-twitter-attribution-data}

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータをBrazeに送信することができません。

## BrazeでのKochavaクリックトラッキングURL（オプション） {#kochava-click-tracking-urls-in-braze-optional}

Brazeのキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールと再エンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきかについて、データドリブン型の意思決定ができるようになります。

Kochavaのクリックトラッキングリンクを使い始めるには、[ドキュメント](https://support.kochava.com/reference-information/attribution-overview/)をご覧ください。BrazeのキャンペーンにKochavaクリックトラッキングリンクを直接挿入できます。Kochavaはその後、[確率的アトリビューション方法論](https://www.kochava.com/getting-prepared-for-ios-14/)を使用して、リンクをクリックしたユーザーをアトリビューションします。Brazeのキャンペーンからのアトリビューションの精度を向上させるために、Kochavaトラッキングリンクにデバイス識別子を追加することをお勧めします。これにより、リンクをクリックしたユーザーを決定論的にアトリビューションできます。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeではお客様が[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAIDはまた、Kochava SDK統合によってネイティブに収集されます。次のLiquidロジックを利用して、KochavaクリックトラッキングリンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとKochavaの両方が、SDK統合を通じてネイティブにIDFVを自動的に収集します。これはデバイス識別子として使用できます。次のLiquidロジックを利用して、KochavaクリックトラッキングリンクにIDFVを含めることができます。

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
現在、クリックトラッキングリンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または将来的に使用する予定がない場合でも、Kochavaは確率モデルを通じてこれらのクリックをアトリビューションすることができます。
{% endalert %}