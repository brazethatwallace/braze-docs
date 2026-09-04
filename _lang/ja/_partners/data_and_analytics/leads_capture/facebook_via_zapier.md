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
| Zapierアカウント | このパートナーシップを利用するには、Zapierアカウントが必要です。この統合では<a href="https://zapier.com/app/pricing/" target="_blank">Zapierのプレミアムアプリ</a> を使用するため、お使いのZapierプランがプレミアムアプリにアクセスできることを確認してください。 |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebook Leadsアクセス</a> | Brazeで使用する予定の各広告アカウントに対して、Facebook Leadsアクセスが必要です。 |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business マネージャー</a> | この統合の一環として、ブランドのFacebookアセット（広告アカウント、ページ、アプリなど）を管理する一元管理ツールであるFacebook Business マネージャーを使用します。 |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook広告アカウント</a> | ブランドのビジネスマネージャーに紐づいたアクティブなFacebook広告アカウントが必要です。<br><br>Brazeで使用する予定の各広告アカウントに対して「広告アカウントの管理」権限があること、また広告アカウントの利用規約に同意していることを確認してください。 |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Facebookページ</a> | ブランドのビジネスマネージャーに紐づいたアクティブなFacebookページが必要です。<br><br>Brazeで使用する予定の各Facebookページに対して「ページの管理」権限があることを確認してください。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics#api-definitions)を把握していることを確認してください。APIエンドポイントは、お使いのBrazeインスタンスのダッシュボードURLと一致します。<br><br>たとえば、ダッシュボードURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキーがあることを確認してください。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：インスタントフォームを使用したリード広告キャンペーンを作成する {#step-1-create-a-lead-ads-campaign-with-an-instant-form}

Facebook広告マネージャーから、<a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebookリードキャンペーンとリード広告フォーム</a> を作成します。

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)にリクエストを行ってユーザープロファイルを更新または作成する際に、メールアドレスまたは電話番号を使用できます。そのため、リード広告フォームに**メール**または**電話番号**の**連絡先フィールド**を含めてください。名または姓を収集する場合は、フルネームではなく、フォーム内でそれぞれ別々に収集してください。

### ステップ2：FacebookアカウントをZapierに接続する {#step-2-connect-your-facebook-account-to-zapier}

#### ステップ2a：Zapierで接続方法を選択する {#step-2a-select-your-connection-method-in-zapier}

Zapierで**Apps**に移動し、利用可能なFacebookアプリを検索します。**Facebook Lead Ads**または**Facebook Lead Ads（for Business admins）**のいずれかを選択します。

FacebookアカウントをZapierに接続するこれら2つの方法の詳細については、以下を参照してください。

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads（for Business Admins）</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![Facebook Lead Adsの接続オプションを表示するZapierアプリ検索画面。]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### ステップ2b：Facebook Business マネージャーのリードアクセスにZapierを追加する {#step-2b-add-zapier-to-leads-access-in-facebook-business-manager}

Facebook Business マネージャーで、ナビゲーションメニューから**Integrations** > **Leads Access**に移動します。Facebookページを選択し、**CRMs**をクリックします。CRMタブで**Assign CRMs**を選択し、**Zapier**を追加します。

![ZapierがCRM連携として割り当てられたFacebook Business Managerのリードアクセスページ。]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

ZapierをCRM連携として割り当てる手順については、Facebookの<a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">ドキュメント</a> を参照してください。

### ステップ3：Zapを作成する {#step-3-create-your-zap}

#### ステップ3a：トリガーを作成する {#step-3a-create-the-trigger}

Facebookアカウントを接続したら、Zapの作成に進みます。**Trigger**で、ステップ2での選択に基づき、**Facebook Lead Ads**または**Facebook Lead Ads（for Business Admins）**を選択します。

![Facebook Lead Adsが選択されたZapierトリガーステップ。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

**Event**で、**New Leads** > **Continue**を選択します。

![New Leadsが表示されたZapierトリガーイベント選択画面。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Facebookアカウントを選択し、**Continue**をクリックします。

![トリガーのZapier Facebookアカウント接続ステップ。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Facebookページと先ほど作成したインスタントフォームを選択し、**Continue**をクリックします。

![Facebookページとインスタントフォームを選択するZapierトリガー設定画面。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

次に、このトリガーをテストします。フォーム出力の検証後、**Continue with selected record**を選択します。

#### ステップ3b：アクションを作成する {#step-3b-create-an-action}

新しいステップを追加し、**Webhooks by Zapier**を選択します。次に、**Event**フィールドで**Custom Request**を選択し、**Continue**をクリックします。

![Webhooks by ZapierとCustom Requestが設定されたZapierアクションステップ。]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

最後に、ペイロードにフィールドを挿入してカスタムリクエストを設定します。以下のコードスニペットはペイロードの例です。

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

Zapierでの表示例は以下のとおりです。

![Facebookリードフィールドを Brazeに送信するためのZapier webhookペイロードマッピングの例。]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

webhookを設定したら、**Continue and test**を選択します。テストが成功したら、Zapを公開できます。

### ステップ4：Facebook Lead Ads Zapをテストする {#step-4-test-your-facebook-lead-ads-zap}

エンドツーエンドのテストを行うには、Facebook Developer ConsoleにあるFacebookのLeads Ads Testing Toolを使用します。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testing and Troubleshooting</a> を参照してください。

## ユーザー ID の管理 {#user-identity-management}

この連携では、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number)を通じて、メールによって Facebook リードを紐付けることができます。

* メールが既存のユーザープロファイルと一致する場合、BrazeはそのプロファイルをFacebookリードデータで更新します。
* 同じメールを持つユーザープロファイルが複数存在する場合、Brazeは更新対象としてexternal IDを持つ最も最近更新されたプロファイルを優先します。
* external IDが存在しない場合、Brazeは一致するメールを持つ最も最近更新されたプロファイルを優先します。
* 提供されたメールに該当するプロファイルが存在しない場合、Brazeは新しいプロファイルを作成し、新しいエイリアスユーザープロファイルが作成されます。新しく作成されたエイリアスユーザープロファイルを識別するには、[`/users/identify` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を使用してください。

{% alert note %}
連携の主要な識別子としてそれらのフィールドが利用可能な場合は、Brazeへのリクエストの一部として電話番号やexternal IDを使用することもできます。これを行うには、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)に示されているとおりにリクエストペイロードを変更してください。
{% endalert %}

## トラブルシューティング {#troubleshooting}

{% details トリガーとアクションのテストに成功したのに、Zapier Zapを公開できないのはなぜですか？ %}
このインテグレーションを使用するには、プレミアムアプリをサポートする<a href="https://zapier.com/app/pricing/" target="_blank">Zapierプラン</a> が必要です。
{% enddetails %}

{% details FacebookリードがBrazeに同期されないのはなぜですか？ %}
1. Facebookページ、広告アカウント、およびリードアクセスへの管理者アクセス権があることを確認してください。その後、Zapierでアカウントを再接続してください。
2. Facebookで作成したインスタントフォームが、トリガーステップで選択したフォームにマッピングされていることを確認してください。
3. **Facebook Business マネージャー** > **Integrations** > **Lead Access** に移動して、ZapierにLeads Accessが割り当てられていることを確認してください。
{% enddetails %}

{% details 同じメールアドレスでユーザープロファイルが重複して表示されるのはなぜですか？ %}
Brazeでは、[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)に基づいて、ユーザープロファイルを作成・管理する独自の方法があります。

内部プロセスやBraze内で顧客の作成をトリガーするタイミングによっては、インテグレーションによるユーザープロファイルの作成と、システムからのユーザー作成の競合により、ユーザープロファイルが重複する場合があります。Brazeで[ユーザープロファイルをマージ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)できます。
{% enddetails %}

{% details Zapierアカウントを持っていません。Facebook Lead AdsのwebhookをBrazeにトリガーするにはどうすればよいですか？ %}
Zapierを使用しておらず、今後も使用する予定がない場合は、FacebookからBrazeへのインテグレーションを直接構築できます。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">Lead Adsドキュメント</a> を参照してください。

Facebookからリードを取得するには、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhook</a> を使用してください。Facebookでwebhookを開始するには、<a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">Webhookドキュメント</a> を参照してください。

FacebookでwebhookのURLを設定した後、チームと協力して[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)にデータを転送するための最適なパスを決定してください。Zapierのアプローチと同様に、`users/track`エンドポイントを通じて[メールによるリクエスト]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number)を行うことをお勧めします。
{% enddetails %}

{% alert tip %}
その他のトラブルシューティングのヒントについては、Zapierの<a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Facebookリードトラブルシューティングガイド</a> を参照してください。
{% endalert %}