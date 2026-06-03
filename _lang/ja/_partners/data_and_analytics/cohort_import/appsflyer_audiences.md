---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "このリファレンス記事では、BrazeとAppsFlyer Audiencesのパートナーシップについて説明します。AppsFlyer Audiencesは、オーディエンスセグメントを効率的に作成してパートナーネットワークに接続できるAppsFlyerプラットフォームの機能です。"
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> この記事では、[AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/) 統合を使用してAppsFlyerからBrazeにユーザーコホートをインポートする方法について説明します。AppsFlyerとその他の機能（モバイルアトリビューションなど）の統合の詳細については、メインの[AppsFlyerの記事]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer/)を参照してください。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| AppsFlyerアカウント | このパートナーシップを活用するには、AppsFlyerアカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOSアプリとAndroidアプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| AppsFlyer SDK | 必要なBraze SDKに加えて、[AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## データインポート統合 {#data-import-integration}

### ステップ1: AppsFlyer SDKの設定 {#step-1-configure-the-appsflyer-sdk}

この統合を使用するには、AppsFlyer SDKの`setPartnerData()`関数を使用して、ユーザーのBraze external IDをAppsFlyerに渡す必要があります。

#### Android
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
`````````objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### ステップ2: Brazeデータインポートキーを取得する {#step-2-get-the-braze-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**AppsFlyer**を選択します。

ここでRESTエンドポイントを見つけ、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、AppsFlyerのダッシュボードでポストバックを設定する次のステップで使用されます。<br><br>![AppsFlyerテクノロジーページの「コホートインポートを使用したデータインポート」ボックス。このボックスには、データインポートキーとRESTエンドポイントが表示されています。]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### ステップ3: AppsFlyer AudiencesでのBraze接続の設定 {#step-3-configure-a-braze-connection-in-appsflyer-audiences}

1. [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections)で、**Connections**タブに移動し、**Add partner connection**をクリックします。
2. パートナーとしてBrazeを選択し、接続に名前を付けます。
3. データインポートキーとBraze RESTエンドポイントを入力します。
4. 接続を保存します。保存した接続は、新しいオーディエンスまたは既存のオーディエンスにリンクできます。

![AppsFlyer Audiencesプラットフォームのパートナー接続設定ページ。画像下部で「Braze external ID」ボックスがオンになっています。]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### ステップ4: BrazeでのAppsFlyer Audiencesコホートの使用 {#step-4-using-appsflyer-audiences-cohorts-in-braze}

AppsFlyerオーディエンスがBrazeにアップロードされると、**AppsFlyer Cohorts**フィルターを選択して、Brazeでセグメントを定義する際のフィルターとして使用できます。

![ユーザー属性フィルター「AppsFlyer Cohorts」が選択されています。]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートではBrazeに新しいユーザーは作成されません。
{% endalert %}

## ユーザーマッチング {#user-matching}

識別されたユーザーは、`external_id`または`alias`のどちらかによって照合できます。匿名ユーザーは、`device_id`によって照合できます。元々匿名ユーザーとして作成された識別済みユーザーは、`device_id`では識別できず、`external_id`または`alias`で識別する必要があります。