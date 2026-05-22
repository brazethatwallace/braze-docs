---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "このリファレンス記事では、BrazeとSingularのパートナーシップについて説明します。Singularは、有料インストールアトリビューションデータをインポートできる統合マーケティング分析プラットフォームです。"
page_type: partner
search_tag: Partner

---

# Singular

> [Singular](https://www.singular.net/)は、アトリビューション、コスト集計、マーケティング分析、クリエイティブレポート、ワークフローオートメーションを提供する統合マーケティング分析プラットフォームです。

_この統合はSingularによって管理されています。_

## 統合について {#about-the-integration}

BrazeとSingularの統合により、有料インストールのアトリビューションデータをインポートして、ライフサイクルキャンペーン内でインテリジェントにセグメントすることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Singularアカウント | このパートナーシップを活用するには、Singularアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| Singular SDK | 必要なBraze SDKに加えて、[Singular SDK](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1:ユーザーIDをマップする {#step-1-map-user-ids}

#### Android

Androidアプリをお持ちの場合は、SingularにBrazeのユニークなユーザーIDを渡す以下のコードスニペットを含める必要があります。

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
2023年2月以前は、Singularのアトリビューション統合は、iOSアトリビューションデータを照合するための主要識別子としてIDFV（Identifier for Vendor）を使用していました。OBJECTIVE-Cを使用しているBrazeのお客様は、サービスの中断がないため、インストール時にBrazeの`device_id`を取得してSingularに送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0+を使用しているお客様は、相互識別子としてIDFVを引き続き使用するには、`useUUIDAsDeviceId`フィールドが`false`に設定されていることを確認する必要があります。これにより、統合が中断されることがなくなります。

`true`に設定している場合、BrazeがiOSアトリビューションを適切に照合できるように、アプリのインストール時にSingularにBrazeの`device_id`を渡すために、Swift用のiOSデバイスIDマッピングを実装する必要があります。

{% tabs local %}
{% tab Objective-C %}

`````````objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

`````````swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### ステップ2:Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Singular**を選択します。

ここでは、RESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。

統合を完了するには、データインポートキーとRESTエンドポイントをSingularアカウントマネージャーに提供する必要があります。<br><br>![Singularテクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーとRESTエンドポイントが表示されています。]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### ステップ3:統合を確認する {#step-3-confirm-the-integration}

BrazeがSingularからアトリビューションデータを受信すると、BrazeのSingularテクノロジーパートナーページのステータス接続インジケーターが「Not Connected」から「Connected」に変わり、最後にリクエストが成功したタイムスタンプが表示されます。

このステータスは、アトリビュートされたインストールに関するデータをBrazeが受信した後にのみ変更されます。Brazeはオーガニックインストールを無視し（Singularのポストバックから除外し）、接続が成功したかどうかを判断する際にカウントしません。

## FacebookとX（旧Twitter）のアトリビューションデータ {#facebook-and-x-formerly-twitter-attribution-data}

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできません。

## BrazeでのSingularクリックトラッキングURL（オプション） {#singular-click-tracking-urls-in-braze-optional}

Brazeのキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきかについて、データドリブン型の意思決定ができるようになります。

Singularクリックトラッキングリンクを使い始めるには、[ドキュメント](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true)を参照してください。SingularのクリックトラッキングリンクをBrazeのキャンペーンに直接挿入することができます。その後、Singularは[確率的アトリビューション手法](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true)を用いて、リンクをクリックしたユーザーをアトリビュートします。Brazeのキャンペーンからのアトリビューションの精度を高めるために、Singularトラッキングリンクにデバイス識別子を付加することをお勧めします。これにより、リンクをクリックしたユーザーを決定論的にアトリビュートできます。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeではお客様が[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAIDはまた、Singular SDKの統合によってネイティブに収集されます。以下のLiquidロジックを利用することで、SingularクリックトラッキングリンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとSingularの両方が、SDKの統合を通じてネイティブにIDFVを自動的に収集します。これはデバイス識別子として使用できます。以下のLiquidロジックを利用することで、SingularクリックトラッキングリンクにIDFVを含めることができます。

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
**この推奨事項の適用は完全に任意です。**<br>
現在、クリックトラッキングリンクにIDFVやGAIDのようなデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Singularは確率的モデリングによってこれらのクリックをアトリビュートすることができます。
{% endalert %}