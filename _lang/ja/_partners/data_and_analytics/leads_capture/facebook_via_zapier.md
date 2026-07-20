---
nav_title: Zapier経由のFacebookリード獲得広告
article_title: Zapier経由のFacebookリード獲得広告
description: "このリファレンス記事では、Zapierを介したBrazeとFacebookリード獲得広告の統合について説明します。FacebookからBrazeへのリードデータの転送を自動化し、リアルタイムのエンゲージメントとパーソナライズされたフォローアップアクションを実現します。"
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Zapier経由のFacebookリード獲得広告統合 {#facebook-lead-ads-via-zapier-integration}

> <a href="https://zapier.com/" target="_blank">Zapier</a> を介したFacebookリード獲得広告統合により、FacebookからBrazeにリードをインポートし、リードがキャプチャされたときにカスタムイベントを追跡できます。

Facebookリード獲得広告は、企業がFacebook上で直接リード情報を収集できる広告フォーマットです。この広告は、リード生成プロセスを簡単かつシームレスにするように設計されています。Zapier統合とBrazeを活用することで、FacebookからBrazeへのリードデータの転送を自動化でき、リアルタイムのエンゲージメントとパーソナライズされたフォローアップアクションが可能になります。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Zapierアカウント | このパートナーシップを活用するには、Zapierアカウントが必要です。この統合には<a href="https://zapier.com/app/pricing/" target="_blank">プレミアムZapierアプリ</a> を使用する必要があるため、ご利用のZapierプランでプレミアムアプリにアクセスできることを確認してください。 |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebookリードアクセス</a> | Brazeで使用する予定の各広告アカウントには、Facebookリードアクセスが必要です。 |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | この統合の一環として、Facebook Business Managerを使用します。Facebook Business Managerは、ブランドのFacebookアセット（広告アカウント、ページ、アプリなど）を管理するための一元的なツールです。 |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook広告アカウント</a> | ブランドのビジネスマネージャーに紐づいた有効なFacebook広告アカウントが必要です。<br><br>Brazeで使用する予定の各広告アカウントに対する「Manage ad accounts」権限を持っており、広告アカウントの利用規約に同意していることを確認してください。 |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Facebookページ</a> | ブランドのビジネスマネージャーに紐づいた有効なFacebookページが必要です。<br><br>Brazeで使用する予定の各Facebookページに対する「Manage Pages」権限があることを確認してください。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics#api-definitions)を確認してください。APIエンドポイントは、BrazeインスタンスのダッシュボードURLと一致します。<br><br>たとえば、ダッシュボードURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキーがあることを確認してください。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1：インスタントフォームでリード獲得広告キャンペーンを作成する {#step-1-create-a-lead-ads-campaign-with-an-instant-form}

Facebook広告マネージャから、<a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebookリードキャンペーンとリード獲得広告フォーム</a> を作成します。

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)へのリクエスト時に、メールアドレスまたは電話番号を使用してユーザープロファイルを更新または作成できます。このため、リード広告フォームに**メール**または**電話番号**の**連絡先フィールド**を含めてください。名または姓を収集する場合は、フルネームではなくフォームで別々に収集します。

### ステップ2：FacebookアカウントをZapierに接続する {#step-2-connect-your-facebook-account-to-zapier}

#### ステップ2a：Zapierで接続方法を選択する {#step-2a-select-your-connection-method-in-zapier}

Zapierで**Apps**に移動して利用可能なFacebookアプリを検索します。**Facebook Lead Ads**または**Facebook Lead Ads (for Business admins)**のいずれかを選択します。

FacebookアカウントをZapierに接続するこの2つの方法の詳細については、以下を参照してください。

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![Zapierアプリ検索でFacebook Lead Adsの接続オプションが表示されている画面。]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### ステップ2b：Facebook Business ManagerでリードアクセスにZapierを追加する {#step-2b-add-zapier-to-leads-access-in-facebook-business-manager}

Facebook Business Managerで、ナビゲーションメニューの**Integrations** > **Leads Access**に移動します。Facebookページを選択し、**CRMs**をクリックします。CRMタブで**Assign CRMs**を選択し、**Zapier**を追加します。

![Facebook Business ManagerのLeads AccessページでZapierがCRM統合として割り当てられている画面。]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

CRM統合としてZapierを割り当てるステップについては、Facebookの<a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">ドキュメント</a> を参照してください。

### ステップ3：Zapを作成する {#step-3-create-your-zap}

#### ステップ3a：トリガーを作成する {#step-3a-create-the-trigger}

Facebookアカウントを接続したら、Zapの作成に進むことができます。**トリガー**には、ステップ2での選択に基づいて**Facebook Lead Ads**または**Facebook Lead Ads (for Business Admins)**を選択します。

![Facebook Lead Adsが選択されたZapierのトリガーステップ。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

**Event**で**New Leads** > **Continue**を選択します。

![New Leadsが表示されたZapierのトリガーイベント選択画面。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Facebookアカウントを選択し、**Continue**を選択します。

![トリガー用のZapier Facebookアカウント接続ステップ。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

以前に作成したFacebookページとインスタントフォームを選択し、**Continue**を選択します。

![Facebookページとインスタントフォームを選択するZapierのトリガー設定画面。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

次に、このトリガーをテストします。フォーム出力を検証したら、**Continue with selected record**を選択します。

#### ステップ3b：アクションを作成する {#step-3b-create-an-action}

新しいステップを追加し、**Webhooks by Zapier**を選択します。次に、**Event**フィールドで**Custom Request**を選択し、**Continue**をクリックします。

![Webhooks by ZapierとCustom Requestが設定されたZapierのアクションステップ。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

最後に、ペイロードにフィールドを挿入してカスタムリクエストを設定します。次のコードスニペットはペイロードの例です。

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

次に、Zapierでの設定例を示します。

![FacebookリードフィールドをBrazeに送信するためのZapier webhookペイロードマッピングの例。]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

webhookを設定した後、**Continue and test**を選択します。テストが成功した場合は、Zapを公開できます。

### ステップ4：Facebookリード獲得広告のZapをテストする {#step-4-test-your-facebook-lead-ads-zap}

このエンドツーエンドのテストを行うには、Facebook Developer ConsoleでFacebookのLeads Ads Testing Toolを使用します。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">テストとトラブルシューティング</a> を参照してください。

## ユーザーID管理 {#user-identity-management}

この統合により、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number)を通じてメールでFacebookリードを紐づけることができます。

* メールが既存のユーザープロファイルと一致する場合、BrazeはFacebookリードデータでそのプロファイルを更新します。
* 同じメールを持つユーザープロファイルが複数ある場合、Brazeは更新時にexternal IDを持つ最新の更新済みプロファイルを優先します。
* external IDが存在しない場合、Brazeは一致するメールを持つ最新の更新済みプロファイルを優先します。
* 指定されたメールを持つプロファイルが存在しない場合、Brazeは新しいプロファイルを作成し、新しいエイリアスユーザープロファイルが作成されます。新しく作成されたエイリアスユーザープロファイルを識別するには、[`/users/identify`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用します。

{% alert note %}
これらのフィールドが利用可能で、統合に使用したいプライマリ識別子である場合は、Brazeへのリクエストの一部として電話番号またはexternal IDを使用することもできます。これを行うには、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)に示すようにリクエストペイロードを変更してください。
{% endalert %}

## トラブルシューティング {#troubleshooting}

{% details トリガーとアクションのテストは成功しましたが、Zapier Zapを公開できないのはなぜですか？ %}
この統合を使用するには、プレミアムアプリをサポートする<a href="https://zapier.com/app/pricing/" target="_blank">Zapierプラン</a> が必要です。
{% enddetails %}

{% details FacebookリードがBrazeに同期されないのはなぜですか？ %}
1. Facebookページ、広告アカウント、リードアクセスに対する管理者アクセス権があることを確認してください。次に、Zapierでアカウントを再接続します。
2. Facebookで作成したインスタントフォームが、トリガーステップで選択したフォームにマッピングされていることを確認してください。
3. **Facebook Business Manager** > **Integrations** > **Lead Access**に移動して、ZapierをLeads Accessに割り当てていることを確認してください。
{% enddetails %}

{% details 同じメールを持つ重複ユーザープロファイルが表示されるのはなぜですか？ %}
Brazeでは[ユーザープロファイルライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle)に基づいて、ユーザープロファイルを作成および管理する独自の方法があります。

内部プロセスやBraze内での顧客作成のトリガータイミングによっては、統合によるユーザープロファイルの作成とシステムからのユーザー作成の間の競合により、重複するユーザープロファイルが発生することがあります。Brazeでは[ユーザープロファイルをマージ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)できます。
{% enddetails %}

{% details Zapierアカウントを持っていません。Facebookリード獲得広告のwebhookをBrazeにトリガーするにはどうすればよいですか？ %}
Zapierを使用しておらず、使用する予定がない場合は、FacebookからBrazeへの直接統合を構築できます。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">リード獲得広告のドキュメント</a> を参照してください。

Facebookからリードを取得するには、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhook</a> を使用します。Facebookでwebhookの使用を開始するには、<a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">webhookのドキュメント</a> を参照してください。

FacebookでWebhook URLを確立したら、チームと協力して[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)にデータを転送するための最適なパスを決定してください。Zapierアプローチと同様に、`users/track`エンドポイントから[メールによるリクエスト]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number)を実行することをお勧めします。
{% enddetails %}

{% alert tip %}
トラブルシューティングのヒントについては、Zapierの<a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Facebookリードのトラブルシューティングガイド</a> を参照してください。
{% endalert %}