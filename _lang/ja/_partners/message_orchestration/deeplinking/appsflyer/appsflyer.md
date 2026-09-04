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

BrazeとAppsFlyerの統合により、AppsFlyerのモバイルインストールアトリビューションデータを活用して、より全体的なキャンペーンを最適化し構築する方法をより深く理解できます。

また、[AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences)統合により、AppsFlyerのオーディエンス（コホート）を直接Brazeに渡すことができ、適切なタイミングで適切なユーザーをターゲットにした強力なカスタマーエンゲージメントキャンペーンを作成できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| AppsFlyer アカウント | このパートナーシップを利用するには、AppsFlyer アカウントが必要です。 |
| iOS または Android アプリ | この連携は iOS および Android アプリをサポートしています。プラットフォームによっては、アプリケーションにコードスニペットが必要になる場合があります。これらの要件の詳細は、連携プロセスのステップ1に記載されています。 |
| AppsFlyer SDK | 必須の Braze SDKに加えて、[AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started) をインストールする必要があります。 |
| メールドメイン設定の完了 | Braze オンボーディング中のメール設定で、[IP とドメインの設定ステップ]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains)が完了している必要があります。 |
| SSL 証明書 | [SSL 証明書]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate)が設定されている必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ 1: デバイスIDをマッピングする {#step-1-map-device-id}

{% tabs local %}
{% tab Android %}
Androidアプリがある場合は、一意のBrazeデバイスIDをAppsFlyerに渡す必要があります。

以下のコード行が正しい場所（Braze SDKの起動後、AppsFlyer SDKの初期化コードの前）に挿入されていることを確認してください。詳細については、AppsFlyerの[Android SDK連携ガイド](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)を参照してください。

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
2023年2月以前は、AppsFlyerアトリビューション連携において、iOSアトリビューションデータの照合にIdentifier for Vendor（IDFV）をプライマリ識別子として使用していました。Objective-Cを使用しているBrazeのお客様は、Brazeの`device_id`を取得してインストール時にAppsFlyerに送信する必要はありません。サービスの中断は発生しないためです。
{% endalert%}

Swift SDK v5.7.0以降を使用している場合、相互識別子としてIDFVを引き続き使用するには、`useUUIDAsDeviceId`フィールドが`false`に設定されていることを確認して、連携の中断を防ぐ必要があります。

`true`に設定されている場合、Brazeが適切にiOSアトリビューションを照合できるよう、アプリのインストール時にBrazeの`device_id`をAppsFlyerに渡すためのSwift用iOSデバイスIDマッピングを実装する必要があります。

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

### ステップ 2: Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー** に移動し、**AppsFlyer** を選択します。

ここで、RESTエンドポイントを確認し、Brazeデータインポートキーを生成できます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーとRESTエンドポイントは、次のステップでAppsFlyerのダッシュボードにポストバックを設定する際に使用されます。<br><br>![AppsFlyerテクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスにはデータインポートキーとRESTエンドポイントが含まれています。]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### ステップ 3: AppsFlyerのダッシュボードでBrazeを設定する {#step-3-configure-braze-in-appsflyers-dashboard}

1. AppsFlyerで、ナビゲーションメニューから **Integrated Partners** ページに移動します。次に、**Braze**を検索し、Brazeのロゴを選択して設定ウィンドウを開きます。
2. **Integration** タブで、**Activate Partner** をオンにします。
3. Brazeダッシュボードで確認したデータインポートキーとRESTエンドポイントを入力します。
4. **Advanced Privacy** をオフに切り替え、設定を保存します。

{% alert important %}
AppsFlyerの [Integration] タブにBraze RESTエンドポイントを入力する際は、`https://`プロトコルや`/attribution/appsflyer`パスを含めず、ドメインのみ（例: `rest.fra-02.braze.eu`）を入力してください。AppsFlyerが自動的にプロトコルを付加し、パスを追加します。いずれかを入力に含めると、ポストバックの失敗が発生します。
{% endalert %}

これらの手順の追加情報は、[AppsFlyerのドキュメント](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration)で確認できます。

### ステップ 4: 連携を確認する {#step-4-confirm-the-integration}

BrazeのAppsFlyerテクノロジーパートナーページでは、ステップ 2でデータインポートAPIキーを生成するまで、接続インジケーターに **Not Connected** と表示されます。キーを生成すると、インジケーターが **Connected** に変わり、タイムスタンプが表示されます。このタイムスタンプは、AppsFlyerが最後にポストバックを送信した時点ではなく、Brazeで連携が最初に設定された時点（データインポートキーが作成された時点）を示します。

インストールアトリビューションデータがAppsFlyerから流入していることを確認するには、ステップ 5を使用して、非オーガニックインストールデータがBrazeのセグメントフィルターに表示されるかどうかを確認してください。BrazeはAppsFlyerのポストバックからのオーガニックインストールを無視し、アトリビューション済みインストールデータとして保存しません。

### ステップ 5: ユーザーアトリビューションデータを表示する {#step-5-viewing-user-attribution-data}

#### 利用可能なデータフィールド {#available-data-fields}

連携が成功している場合、Brazeはすべての非オーガニックインストールデータをセグメントフィルターにマッピングします。

| AppsFlyerデータフィールド | Brazeセグメントフィルター |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed キャンペーン |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="利用可能なデータフィールド" }

Brazeダッシュボードで、インストールアトリビューションフィルターを使用して、アトリビューションデータに基づいてユーザーベースをセグメント化できます。

![4つの利用可能なフィルター。1つ目は「Install Attribution Source is network_val_0」。2つ目は「Install Attribution Source is campaign_val_0」。3つ目は「Install Attribution Source is adgroup_val_0」。4つ目は「Install Attribution Source is creative_val_0」。フィルターの横には、これらのアトリビューションソースがユーザープロファイルにどのように追加されるかが表示されています。ユーザー情報ページの「Install Attribution」ボックスでは、Install Sourceがnetwork_val_0、campaignがcampaign_val_0などと表示されています。]({% image_buster /assets/img/braze_attribution.png %})

さらに、特定のユーザーのアトリビューションデータは、Brazeダッシュボードの各ユーザープロファイルで確認できます。

{% alert note %}
FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータをサードパーティと共有することを許可していないため、パートナーはBrazeにそのデータを送信できません。
{% endalert %}

## AppsFlyerとBrazeを統合してディープリンクを設定する {#integrate-appsflyer-with-braze-for-deep-linking}

ディープリンク&#8212;ユーザーをアプリやWebサイト内の特定のページや場所に誘導するリンク&#8212;は、カスタマイズされたユーザー体験を作成するために使用されます。

ディープリンクは広く活用されていますが、ユーザーデータの収集に使用されるもう1つの重要な機能であるクリックトラッキング付きのメールディープリンクを使用すると、問題が発生する場合があります。これらの問題は、メールサービスプロバイダー (ESP) がディープリンクをクリック記録ドメインでラップし、元のリンクを壊してしまうことが原因です。そのため、ディープリンクをサポートするには追加の設定が必要です。

AppsFlyerはこれらの問題を回避する[サービス](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer)を提供しており、AppsFlyerがESPサーバーとお客様のドメイン名の間の仲介役として機能できるようにします。プロキシとしての役割により、アソシエーションファイル（AASA/アセットリンク）の提供が可能になり、ディープリンクが容易になります。

## ステップ1 - クリックトラッキングドメインを作成する {#step-1-create-a-click-tracking-domain}

[Brazeのメール設定ガイダンス]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate)の初期要素に従って、メール送信ドメインとクリックトラッキングドメインを作成します。サポートが必要な場合は、Brazeダッシュボードからチケットを起票して、Brazeメールチームに新しいCTDの設定を依頼できます。

![Brazeの上部ナビゲーションバーにある「サポート」ボタンの下に表示されている「ヘルプを見る」ボタンを示すUI。]({% image_buster /assets/img/attribution/appsflyer/1.png %})

既存のクリックトラッキングドメインを使用している場合でも、新しいCTDの作成は必須です。これにより、現在配信中のメールキャンペーンのトラフィックに影響が出ないようにします。

{% alert important%}
AppsFlyerがSSL証明書を作成します。この段階では、メールリンクはセキュアでない可能性が高く、URLのプレフィックスがHTTPSではなくHTTPになっています。これは後のステップで解決されます。
{%endalert%}

## ステップ2 - AppsFlyerでOneLinkテンプレートを作成する {#step-2-create-a-onelink-template-in-appsflyer}
[OneLinkテンプレート](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures)を作成し、「When app is installed」でユニバーサルリンク/アプリリンクを設定します。このテンプレートは、後でメールキャンペーン用のOneLinkリンクを作成する際に使用します。

{% alert note%} ユニバーサルリンク/アプリリンクが有効になっている既存のOneLinkテンプレートがある場合は、それを使用できます。
{%endalert%}

## ステップ3 - AppsFlyerでBraze連携を設定する {#step-3-set-up-your-braze-integration-in-appsflyer}
次に、AppsFlyerでBraze連携を設定します。このステップと次のステップ（「アプリの設定」）は同時に設定できます。
AppsFlyerでBraze連携を設定するには：

### 1. AppsFlyerのサイドメニューから、Engage > ESP integrationを選択します。 {#1-in-appsflyer-from-the-side-menu-select-engage-esp-integration}
![AppsFlyerのUIで、ナビゲーションメニューに表示されている「ESP Integration」ボタン。]({% image_buster /assets/img/attribution/appsflyer/2.png %})


### 2. Brazeを選択します。 {#2-select-braze}
![AppsFlyerのUIで、Brazeを含むESP連携の一覧が表示されている画面。]({% image_buster /assets/img/attribution/appsflyer/3.png %})


### 3. メールキャンペーンに使用するOneLinkテンプレートを選択し、Nextをクリックします。 {#3-select-the-onelink-template-you-want-to-use-for-email-campaigns-then-click-next}
![AppsFlyerのUIで、テンプレートを選択するドロップダウンが表示されている画面。]({% image_buster /assets/img/attribution/appsflyer/4.png %})


### 4. クリックトラッキングドメインと「Braze endpoint」の値を入力し、Validate connectionをクリックします。この値はステップ1で作成した新しいCTDで提供されたものです。 {#4-enter-your-click-tracking-domain-and-braze-endpoint-value-which-was-provided-with-the-new-ctd-created-in-step-1-then-click-validate-connection}

これにより、クリックトラッキングドメインが入力したエンドポイントを指していることが検証されます。

![AppsFlyerのUIで、クリックトラッキングドメインと関連する詳細情報の入力場所がハイライトされている画面。]({% image_buster /assets/img/attribution/appsflyer/5.png %})

「Braze Endpoint」とは、このガイドのステップ1でBrazeから提供された詳細情報、具体的には新しいCTDのことです。

次に、**Validate connection**をクリックします。これにより、クリックトラッキングドメインが入力したエンドポイントを指していることが検証されます。
完了したら、**Next**をクリックします。

### 5. リンクトラフィックをAppsFlyerにルーティングする： {#5-route-link-traffic-to-appsflyer}

#### a. AppsFlyerでカスタマイズされた既成の手順をコピーし、ITまたはドメイン管理者に送信します。 {#a-copy-and-send-the-customized-pre-fabricated-instructions-in-appsflyer-to-your-it-or-domain-administrator}

管理者は、DNS CNAMEレコードをAppsFlyerが提供した新しいドメインに更新することで、メールキャンペーンのトラフィックをESPサーバーからAppsFlyerサーバーにリルートする必要があります。

これにより、リンクがクリックされるたびに、クリックはAppsFlyerにリダイレクトされ、AppsFlyerがさらにESPエンドポイントにリダイレクトします。

![クリックデータがドメインからAppsFlyer、そしてESPエンドポイントへと渡される仕組みを示す図。]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. 手順をコピーして送信したら、Doneをクリックします。 {#b-after-copying-and-sending-the-instructions-click-done}
Braze連携が作成されました。

{%alert important%}
Braze連携のステータスは保留中であり、CNAMEレコードがマッピングされた後にのみ動作を開始します。新しい連携がマッピング後に動作を開始してアクティブになるまで、最大24時間かかる場合があります。
{%endalert%}

## ステップ4：アプリを設定する（開発者タスク） {#step-4-configure-your-app-developer-task}

AppsFlyerは、ユニバーサルリンクをサポートするためにWebまたはアプリチームが実施すべき、正しいアプリ設定に関する[ガイダンスを提供しています](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task)。

## ステップ5：BrazeでSSLクリックトラッキングが有効であることを確認する {#step-5-confirm-ssl-click-tracking-is-enabled-with-braze}

この段階で、AppsFlyerのCTD情報を共有・検証した後、Onelinkの送信ドメインにSSL証明書があるかどうかを確認するためにテスト送信を行うことをお勧めします。これは[メール設定]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate)ガイドに沿っています。

OneLinkを使用してディープリンクを送信することで、品質保証とトラブルシューティングを行うことができます。OneLinkの使用方法の詳細については、[AppsFlyerドキュメント](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)を参照してください。

CTDリンクがHTTPとして識別される場合は、BrazeのEmail Opsチームに連絡してSSLクリックトラッキングを有効にしてください。これにより、すべてのHTTPリンクが自動的にHTTPSに変換されます。
カスタマーサクセスマネージャーに連絡する際、またはステップ1のようにBrazeダッシュボードでチケットを起票する際に、以下のサンプルメッセージテキストを使用できます。

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS.
```

### BrazeでのAppsFlyerクリックトラッキングURL（オプション） {#appsflyer-click-tracking-urls-in-braze-optional}

AppsFlyerの[OneLinkアトリビューションリンク](https://support.AppsFlyer.com/hc/en-us/articles/360001294118)を、プッシュ、メールなどのBrazeキャンペーン全体で使用できます。これにより、BrazeキャンペーンからのインストールまたはリエンゲージメントのアトリビューションデータをAppsFlyerに送り返すことができます。その結果、マーケティング活動をより効果的に測定し、データドリブン型の意思決定を行うことができます。

AppsFlyerでOneLinkトラッキングURLを作成し、Brazeキャンペーンに直接挿入するだけです。その後、AppsFlyerは[確率的アトリビューション手法](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)を使用して、リンクをクリックしたユーザーをアトリビューションします。Brazeキャンペーンからのアトリビューションの精度を向上させるため、AppsFlyerのトラッキングリンクにデバイス識別子を付加することをお勧めします。これにより、リンクをクリックしたユーザーを確定的にアトリビューションします。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeではお客様が[Google広告ID収集（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id)にオプトインできます。AppsFlyer SDK連携でもGAIDを収集します。以下のLiquidロジックを使用して、AppsFlyerのクリックトラッキングリンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAppsFlyerの両方がSDK連携を通じてIDFVをネイティブに自動収集します。IDFVをデバイス識別子として使用できます。以下のLiquidロジックを使用して、AppsFlyerのクリックトラッキングリンクにIDFVを含めることができます。

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}