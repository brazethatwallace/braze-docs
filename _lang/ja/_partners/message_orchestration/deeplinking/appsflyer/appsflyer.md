---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "このリファレンス記事では、アプリの分析と最適化を支援するモバイルマーケティング分析およびアトリビューションプラットフォームであるBrazeとAppsFlyerのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [AppsFlyer](https://www.appsflyer.com/)は、モバイルマーケティング分析およびアトリビューションプラットフォームで、マーケティング分析、モバイルアトリビューション、ディープリンクを通じてアプリの分析と最適化を支援します。

BrazeとAppsFlyerの統合により、AppsFlyerのモバイルインストールアトリビューションデータを活用して、より全体的なCampaignsを最適化し構築する方法をより深く理解できます。

また、[AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/)統合により、AppsFlyerのオーディエンス（コホート）を直接Brazeに渡すことができ、適切なタイミングで適切なユーザーをターゲットにした強力なカスタマーエンゲージメントCampaignsを作成できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| AppsFlyerアカウント | このパートナーシップを活用するには、AppsFlyerアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| AppsFlyer SDK | 必要なBraze SDKに加えて、[AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started)をインストールする必要があります。 |
| メールドメインのセットアップ完了 | Brazeオンボーディング時にメールを設定するには、[IPとドメインの設定ステップ]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/)を完了している必要があります。 |
| SSL証明書 | [SSL証明書]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate)を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1: デバイスIDをマッピングする {#step-1-map-device-id}

{% tabs local %}
{% tab Android %}
Androidアプリの場合、AppsFlyerに固有のBrazeデバイスIDを渡す必要があります。

以下のコード行が、Braze SDKの起動後、AppsFlyer SDKの初期化コードの前の正しい位置に挿入されていることを確認してください。詳細については、AppsFlyerの[Android SDK統合ガイド](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)を参照してください。

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
2023年2月以前のAppsFlyerアトリビューション統合では、iOSアトリビューションデータを照合するための主要識別子としてIDFV（Identifier for Vendor）を使用していました。Objective-Cを使用しているBraze顧客は、サービスの中断がないため、インストール時にBrazeの`device_id`を取得してAppsFlyerに送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0+を使用している場合、相互識別子としてIDFVを引き続き使用するには、統合の中断を避けるために`useUUIDAsDeviceId`フィールドが`false`に設定されていることを確認する必要があります。

`true`に設定している場合、BrazeがiOSアトリビューションを適切に照合できるように、アプリのインストール時にAppsFlyerにBrazeの`device_id`を渡すために、Swift用のiOSデバイスIDマッピングを実装する必要があります。

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab unity %}
UnityでデバイスIDをマッピングするには、以下を使用します。

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### ステップ2: Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで、**Partner Integrations** > **Technology Partners**に移動し、**AppsFlyer**を選択します。

ここで、RESTエンドポイントを確認し、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、AppsFlyerのダッシュボードでポストバックを設定する際に次のステップで使用されます。<br><br>![AppsFlyerテクノロジーページで利用可能な「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーとRESTエンドポイントが表示されています。]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### ステップ3: AppsFlyerのダッシュボードでBrazeを設定する {#step-3-configure-braze-in-appsflyers-dashboard}

1. AppsFlyerで、左側のバーの**Integrated Partners**ページに移動します。次に**Braze**を検索し、Brazeのロゴを選択すると設定ウィンドウが開きます。
2. **Integration**タブで**Activate Partner**をオンにします。
3. Brazeダッシュボードで確認したデータインポートキーとRESTエンドポイントを入力します。
4. **Advanced Privacy**をオフに切り替え、設定を保存します。

{% alert important %}
AppsFlyerのIntegrationタブでBraze RESTエンドポイントを入力する際は、`https://`プロトコルや`/attribution/appsflyer`パスを含めず、ドメインのみ（例：`rest.fra-02.braze.eu`）を入力してください。AppsFlyerが自動的にプロトコルを付加し、パスを追加します。いずれかを入力に含めると、ポストバックが失敗します。
{% endalert %}

これらの手順に関する追加情報は、[AppsFlyerのドキュメント](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration)に掲載されています。

### ステップ4: 統合を確認する {#step-4-confirm-the-integration}

BrazeのAppsFlyerテクノロジーパートナーページでは、ステップ2でデータインポートAPIキーを生成するまで、接続インジケーターに**Not Connected**と表示されます。キーを生成すると、インジケーターが**Connected**に変わり、タイムスタンプが表示されます。このタイムスタンプは、AppsFlyerが最後にポストバックを送信した時点ではなく、Brazeで統合が最初にセットアップされた時点（データインポートキーが作成された時点）を反映しています。

インストールアトリビューションデータがAppsFlyerから流入していることを確認するには、ステップ5を使用して、非オーガニックインストールデータがBrazeのセグメントフィルターに表示されることを検証してください。BrazeはAppsFlyerのポストバックからのオーガニックインストールを無視し、アトリビューション付きインストールデータとして保存しません。

### ステップ5: ユーザーアトリビューションデータを確認する {#step-5-viewing-user-attribution-data}

#### 利用可能なデータフィールド {#available-data-fields}

統合が成功した場合、Brazeはすべての非オーガニックインストールデータをセグメントフィルターにマッピングします。

| AppsFlyerデータフィールド | Braze Segmentフィルター |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Available data fields" }

Brazeダッシュボードでは、インストールアトリビューションフィルターを使用して、アトリビューションデータでユーザー群をセグメンテーションできます。

![4つのフィルターが利用可能です。1つ目は「Install Attribution Sourceがnetwork_val_0」。2つ目は「Install Attribution Sourceがcampaign_val_0」。3つ目は「Install Attribution Sourceがadgroup_val_0」。4つ目は「Install Attribution Sourceがcreative_val_0」。リストされたフィルターの横に、これらのアトリビューションソースがどのようにユーザープロファイルに追加されるかを確認できます。ユーザー情報ページの「Install Attribution」ボックスで、Install Sourceはnetwork_val_0、campaignはcampaign_val_0などと表示されます。]({% image_buster /assets/img/braze_attribution.png %})

さらに、特定のユーザーのアトリビューションデータは、Brazeダッシュボードの各ユーザーのプロファイルで利用可能です。

{% alert note %}
FacebookおよびX（旧Twitter）Campaignsのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできません。
{% endalert %}

## ディープリンクのためにAppsFlyerとBrazeを統合する {#integrate-appsflyer-with-braze-for-deep-linking}

ディープリンク&#8212;アプリやWebサイト内の特定のページや場所にユーザーを誘導するリンク&#8212;は、カスタマイズされたユーザー体験を作り出すために使用されます。

広く使われている一方で、ユーザーデータの収集に使われるもう一つの重要な機能であるクリックトラッキング&#8212;でメールによるディープリンクを使用する場合、問題が発生する可能性があります。これらの問題は、メールサービスプロバイダー（ESP）がディープリンクをクリック記録ドメインでラッピングし、元のリンクを壊してしまうことに起因します。そのため、ディープリンクをサポートするには追加の設定が必要です。

AppsFlyerはこのような問題を回避する[サービス](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer)を提供しており、ESPサーバーとお客様のドメイン名の間にAppsFlyerを仲介として介在させることができます。プロキシとしての役割により、ディープリンクを容易にするアソシエーションファイル（AASA/アセットリンク）の提供が可能になります。

## ステップ1 - クリック追跡ドメインを作成する {#step-1-create-a-click-tracking-domain}

[Brazeのメール設定ガイダンス]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate)の初期要素に従って、メール送信ドメインとクリック追跡ドメインを作成します。サポートについては、Brazeダッシュボードからチケットを発行し、Brazeメールチームと新しいCTDのセットアップを開始できます。

![右上の「Support」ボタンの下にある「Get Help」ボタンを示すBraze UI]({% image_buster /assets/img/attribution/appsflyer/1.png %})

既存のCTDを使用している場合でも、新しいCTDの作成は必須です。これにより、現在のライブメールCampaignsのトラフィックに影響を与えることはありません。

{% alert important%}
AppsFlyerがSSL証明書を作成します。この段階では、メールのリンクはセキュリティで保護されていない可能性が高く、URLプレフィックスがHTTPSではなくHTTPであることを意味します。これは後のステップで解決されます。
{%endalert%}

## ステップ2 - AppsFlyerでOneLinkテンプレートを作成する {#step-2-create-a-onelink-template-in-appsflyer}
[OneLinkテンプレート](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures)を作成し、「When app is installed」でユニバーサルリンク/アプリリンクを設定します。このテンプレートは、後でメールCampaigns用のOneLinkリンクを作成する際に使用します。

{% alert note%} ユニバーサルリンク/アプリリンクを有効にする既存のOneLinkテンプレートがすでに設定されている場合は、それを使用できます。
{%endalert%}

## ステップ3 - AppsFlyerでBraze統合を設定する {#step-3-set-up-your-braze-integration-in-appsflyer}
いよいよAppsFlyerでBraze統合を設定します。このステップと次のステップ（「アプリの設定」）は同時に設定できます。
AppsFlyerでBraze統合を設定するには：

### 1. AppsFlyerのサイドメニューから、Engage > ESP integrationを選択します。 {#1-in-appsflyer-from-the-side-menu-select-engage-esp-integration}
![AppsFlyerのUIに、左側のメニューにある「ESP Integration」ボタンが表示されています。]({% image_buster /assets/img/attribution/appsflyer/2.png %})


### 2. Brazeを選択します。 {#2-select-braze}
![Brazeを含むESP統合のリストを表示するAppsFlyerのUI。]({% image_buster /assets/img/attribution/appsflyer/3.png %})


### 3. メールCampaignsに使用するOneLinkテンプレートを選択し、「Next」をクリックします。 {#3-select-the-onelink-template-you-want-to-use-for-email-campaigns-then-click-next}
![AppsFlyerのUIに、ユーザーがテンプレートを選択できるドロップダウンが表示されています。]({% image_buster /assets/img/attribution/appsflyer/4.png %})


### 4. ステップ1で作成した新しいCTDで提供されたクリック追跡ドメインと「Braze endpoint」の値を入力し、「Validate connection」をクリックします。 {#4-enter-your-click-tracking-domain-and-braze-endpoint-value-which-was-provided-with-the-new-ctd-created-in-step-1-then-click-validate-connection}

これにより、クリック追跡ドメインが入力したエンドポイントを指していることが検証されます。

![AppsFlyerのUIで、顧客がクリック追跡ドメインと関連する詳細を追加する場所がハイライトされています。]({% image_buster /assets/img/attribution/appsflyer/5.png %})

「Braze Endpoint」とは、このガイドのステップ1でBrazeから提供された詳細、特に新しいCTDのことです。

次に、**Validate connection**をクリックし、クリック追跡ドメインが入力したエンドポイントを指していることを検証します。
完了したら、**Next**をクリックします。

### 5. リンクトラフィックをAppsFlyerにルーティングする {#5-route-link-traffic-to-appsflyer}

#### a. AppsFlyerでカスタマイズされたプレハブの説明書をコピーし、ITまたはドメイン管理者に送信します。 {#a-copy-and-send-the-customized-pre-fabricated-instructions-in-appsflyer-to-your-it-or-domain-administrator}

管理者は、AppsFlyerが提供する新しいドメインでDNS CNAMEレコードを更新することにより、メールCampaignsのトラフィックをESPサーバーからAppsFlyerサーバーにリルートする必要があります。

その結果、リンクがクリックされるたびに、クリックはAppsFlyerにリダイレクトされ、AppsFlyerからESPエンドポイントにリダイレクトされます。

![クリックデータがドメインからAppsFlyerを経由してESPエンドポイントへどのように渡されるかを示す図]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. 説明書をコピーして送信したら、「Done」をクリックします。 {#b-after-copying-and-sending-the-instructions-click-done}
Braze統合が作成されました。

{%alert important%}
Braze統合のステータスは保留中で、CNAMEレコードがマッピングされた後にのみ機能し始めます。新しい統合が機能してアクティブになるまでには、マッピング後最大24時間かかることがあります。
{%endalert%}

## ステップ4: アプリを設定する（開発者タスク） {#step-4-configure-your-app-developer-task}
AppsFlyerは、ユニバーサルリンクをサポートするためにWebチームまたはアプリチームが従うべき正しいアプリ設定に関する[ガイダンスを提供](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task)しています。

## ステップ5: BrazeでSSLクリックトラッキングが有効になっていることを確認する {#step-5-confirm-ssl-click-tracking-is-enabled-with-braze}

この段階で、AppsFlyerでCTDの詳細を共有し検証した後、OneLinkの送信ドメインにSSL証明書があるかどうかを確認するため、テスト送信を実行することを推奨します。これは[メール設定](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate)ガイドに沿ったものです。

OneLinkを使ってディープリンクを送信することで、品質保証やトラブルシューティングを行うことができます。OneLinkの使い方の詳細については、[AppsFlyerのドキュメント](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)を参照してください。

CTDリンクがHTTPと識別された場合、Brazeのメールオペレーションチームに連絡し、SSLクリックトラッキングを有効にしてください。これにより、すべてのHTTPリンクが自動的にHTTPSに変換されます。
カスタマーサクセスマネージャーに連絡する際、またはステップ1と同様にBrazeダッシュボードで再度チケットを発行する際に、以下のメッセージ文例を使用できます：

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS.
```

### BrazeでのAppsFlyerクリックトラッキングURL（オプション） {#appsflyer-click-tracking-urls-in-braze-optional}

プッシュやメールなどのBraze Campaignsで、AppsFlyerの[OneLinkアトリビューションリンク](https://support.AppsFlyer.com/hc/en-us/articles/360001294118)を使用できます。これにより、インストールやリエンゲージメントのアトリビューションデータをBraze CampaignsからAppsFlyerに送り返すことができます。その結果、マーケティング活動をより効果的に測定し、データドリブン型の意思決定を行うことができます。

AppsFlyerでOneLinkトラッキングURLを作成し、Braze Campaignsに直接挿入するだけです。その後、AppsFlyerは[確率的アトリビューション手法](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)を使用して、リンクをクリックしたユーザーをアトリビューションします。Braze Campaignsからのアトリビューションの精度を高めるために、AppsFlyerのトラッキングリンクにデバイス識別子を付加することを推奨します。これにより、リンクをクリックしたユーザーを決定論的にアトリビューションします。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeは顧客が[Google Advertising ID収集（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできるようにしています。AppsFlyer SDK統合もGAIDを収集します。以下のLiquidロジックを使用することで、AppsFlyerのクリック追跡リンクにGAIDを含めることができます：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAppsFlyerの両方が、SDK統合を通じてIDFVをネイティブに自動収集します。IDFVをデバイス識別子として使用できます。以下のLiquidロジックを使用することで、AppsFlyerのクリック追跡リンクにIDFVを含めることができます：

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}