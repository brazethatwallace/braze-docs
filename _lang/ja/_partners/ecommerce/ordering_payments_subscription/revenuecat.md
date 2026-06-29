---
nav_title: RevenueCat
article_title: RevenueCat
description: "RevenueCatとBrazeの統合により、顧客の購入およびサブスクリプションのライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客への働きかけや、請求で問題のある顧客へのリマインダーの送信など、顧客のサブスクリプションライフサイクルステージに対応するキャンペーンを作成できます。"
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) は、iOS、Android、およびWebにおけるサブスクリプションステータスの信頼できる唯一の情報源です。新しいアプリを作成する場合でも、すでに数百万のサブスクライバーがいる場合でも、RevenueCatを使用すれば、サーバーコードなしでクロスプラットフォームのアプリ内購入を構築し、製品とサブスクライバーを管理し、データを分析することができます。

_この統合はRevenueCatによって管理されています。_

## 統合について {#about-the-integration}

RevenueCatとBrazeの統合により、顧客の購入およびサブスクリプションのライフサイクルイベントをプラットフォーム間で自動的に同期できます。これにより、無料トライアル中にオプトアウトした顧客への働きかけや、請求で問題のある顧客へのリマインダーの送信など、顧客のサブスクリプションライフサイクルステージに対応するキャンペーンを作成できます。

## 前提条件 {#prerequisites}

RevenueCatとBrazeを接続するには、少なくともRevenueCatダッシュボードから統合を有効にしておく必要があります。Braze SDKを使用している場合は、RevenueCat SDKとBraze SDKを一緒に使用して、両方のシステムで同じ顧客識別子が使用されるようにすることで、統合を強化できます。

| 要件 | 説明 |
|---|---|
| RevenueCatアカウントとアプリ | このパートナーシップを活用するには、[RevenueCatアカウント](https://app.revenuecat.com/login)が必要です。また、RevenueCatアプリが設定されている必要があります。 |
| RevenueCat SDK | 必要なBraze SDKに加えて[RevenueCat SDK](https://docs.revenuecat.com/docs/configuring-sdk)をインストールして、RevenueCatにユーザーエイリアスを提供することをお勧めします。 |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから入手するか、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)で確認できます。<br><br>RevenueCatでは、正しいBraze RESTエンドポイントにサーバーサイドで送信するためにBrazeインスタンスが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Brazeテスト用REST APIキー（オプション） | テストAPIキーは、テスト購入と本番購入のリクエストを個別のBrazeインスタンスに送信する場合に使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

- 顧客が無料トライアルを開始するときにプレミアム機能を強調するオンボーディングキャンペーンをトリガーする。
- 「Billing Issue」イベントを受信したときに請求情報の更新リマインダーを送信する。
- 顧客が無料トライアルをキャンセルした後にフィードバックアンケートを送信する。

## 統合 {#integration}

### ステップ1: BrazeのユーザーIDを設定する {#step-1-set-braze-user-identity}

Braze SDKでは、RevenueCatアプリのユーザーIDに一致するようにBrazeユーザーIDを設定できます。これにより、BrazeとRevenueCatから送信されるイベントを同じユーザーに同期できます。

RevenueCatと同じアプリユーザーIDでBraze SDKを設定するか、Braze SDKの `.changeUser()` メソッドを使用します。

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name",
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
`````````objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
`````````java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### ユーザーエイリアスオブジェクトをBrazeに送信する（オプション） {#send-user-alias-object-to-braze-optional}

RevenueCatアプリのユーザーIDとは異なる代替の一意のユーザー識別子を送信する場合は、RevenueCatサブスクライバー属性として次のデータでユーザーを更新します。

| キー | 説明 |
|---|---|
| `$brazeAliasName` | [ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)のBraze `alias_name` |
| `$brazeAliasLabel` | [ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)のBraze `alias_label` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Send user alias object to Braze (optional)" }

どちらの属性も、[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)をイベントデータとともに送信するために必要です。これらのプロパティは、他の[RevenueCatサブスクライバー属性](https://docs.revenuecat.com/docs/subscriber-attributes)と同様に手動で設定できます。コードスニペットの例はステップ1に示されています。

### ステップ2: RevenueCatイベントをBrazeに送信する {#step-2-send-revenuecat-events-to-braze}

RevenueCat purchases SDKとBraze SDKを同じユーザーIDを持つように設定したら、RevenueCatダッシュボードで統合を有効にしてイベント名を設定できます。

1. RevenueCatダッシュボードでプロジェクトに移動し、左側のメニューで**Integrations**カードを見つけます。**+ New**を選択します。
2. 次に、利用可能な統合から**Braze**を選択し、BrazeインスタンスとBraze REST APIキーを追加します。
3. RevenueCatが送信するイベント名を入力するか、デフォルトのイベント名を選択します。利用可能なイベントの詳細については、[ステップ3](#configure-event-names)を参照してください。
4. RevenueCatで売上（アプリストアの取り分差し引き後）または収益（総売上高）のどちらを報告するかを選択します。

![Brazeインスタンス、APIキー識別子、およびサンドボックス識別子のフィールドを含むRevenueCatでのBraze設定。]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### ステップ3: イベント名を設定する {#configure-event-names}

RevenueCatが送信するイベント名を入力するか、**Use Default Event Names**を選択してデフォルトのイベント名から選択します。RevenueCatが送信をサポートしているイベントは、以下の表のとおりです。

| イベント | 説明 |
|---|---|
| 初回購入 | 無料トライアルを含まない自動更新サブスクリプション製品の初回購入。 |
| トライアル開始 | 自動更新サブスクリプション製品の無料トライアルの開始。 |
| トライアルコンバージョン | 自動更新サブスクリプション製品が無料トライアルから通常の有料期間に変更された場合。 |
| トライアルキャンセル | 無料トライアル期間中に、ユーザーが自動更新サブスクリプション製品の更新をオフにした場合。 |
| 更新 | 自動更新サブスクリプション製品が更新された場合、またはユーザーがサブスクリプション期限の経過後に自動更新サブスクリプション製品を再購入した場合。 |
| キャンセル | 通常の有料期間中に、ユーザーが自動更新サブスクリプション製品の更新をオフにした場合。 |
| 非サブスクリプション購入 | 自動更新サブスクリプションではない製品の購入。 |
| 有効期限切れ | サブスクリプションの期限が切れた場合。 |
| 課金問題 | ユーザーへの請求時に問題が発生した場合。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Configure event names #configure-event-names" }

収益を含むイベントの場合、RevenueCatはトライアルコンバージョンや更新などのイベントとともに、この金額を自動的にBrazeに記録します。

## この統合を使う {#using-this-integration}

RevenueCatでBrazeの設定が完了したら、イベントがRevenueCatからBrazeに自動的に流れ始めます。お客様による追加の操作は不要です。

## カスタマイズ {#customization}

### テスト用のサンドボックスAPIキーを追加する {#add-a-sandbox-api-key-for-testing}

RevenueCatに1つのBraze REST APIキーのみを指定すると、本番イベントのみが送信されます。サンドボックステストイベントも送信する場合は、[別のBraze REST APIキーを作成]({{site.baseurl}}/api/basics/#app-group-rest-api-keys)し、RevenueCatのBraze設定に追加してください。