---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "このリファレンス記事では、BrazeとロイヤルティおよびエンゲージメントプラットフォームであるPunchhとのパートナーシップについて説明します。2つのプラットフォーム間でデータを同期できるようになります。Brazeで公開されたデータはセグメンテーションに使用でき、Brazeで設定されたWebhookテンプレートを使用してユーザーデータをPunchhに同期できます。"
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/)は、ブランドが店内でもデジタルでもオムニチャネル顧客ロイヤルティプログラムを配信できる、業界をリードするロイヤルティとエンゲージメントプラットフォームです。

_この統合はPunchhによって管理されています。_

## 統合について {#about-the-integration}

BrazeとPunchhの統合により、2つのプラットフォーム間でギフティングやロイヤルティの目的でデータを同期できます。Brazeで公開されたデータはセグメンテーションに使用でき、Braze webhookを介してユーザーデータを再びPunchhに同期できます。

## メリット {#what-are-the-benefits}

- PunchhからBrazeにロイヤルティデータをリアルタイムで取り込みます。
- Brazeの強力なオーディエンスデータを活用してレイヤー化し、有意義でダイナミックなクロスチャネルエクスペリエンス（アプリ、モバイル、Web、メール、SMS）を提供します。
  - 顧客がメールを開封しましたか？顧客が店舗の近くでアプリを開きましたか？
- Brazeで送信されるトランザクションメールのルックアンドフィールを標準化します。
- ABテストと最適化を可能にするジャーニーを作成します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Punchhアカウント | このパートナーシップを活用するには、アクティブなPunchhアカウントが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/api/basics#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## その他の留意点 {#what-else-should-i-know}

#### 統合前 {#before-integrating}

- Braze統合を使用する場合、PunchhとBrazeそれぞれに1つずつ、2つのキャンペーンが必要です。たとえば、オファーが添付されたキャンペーンを送信する場合、ギフティングキャンペーンはPunchh内で設定され、通知はBrazeから送信できます。
- ゲストはPunchhとBrazeにすでに存在している必要があります。Punchhでは、まだロイヤルティゲストではない顧客はすべて除外されます。

#### 注意すべき重要事項 {#important-things-to-note}

- Punchhでは、Brazeにデフォルトのユーザー属性を送信する動作を無効にできる機能が追加されています。これにより、顧客に対してデータポイントの超過料金が発生しません。これは、アダプターのセットアップ中に設定されます。
- 定期的なキャンペーンでカスタムセグメントを使用する場合は、キャンペーンが実行されるたびにIDが変更されるため、キャンペーンIDの代わりにキャンペーン名を使用する必要があります。
- 各Punchhギフティングキャンペーンで使用できるコミュニケーションチャネルには、リッチメッセージ、プッシュ通知、SMS、メールがあります。
- BrazeからPunchhカスタムセグメントに送信されたユーザーは、削除できません。既存のカスタムセグメントには新規ゲストのみを追加できます。既存のPunchhカスタムセグメントからゲストを削除する必要がある場合は、新しいPunchhカスタムセグメントにユーザーを送信するために、新しいWebhookキャンペーンをBrazeで作成する必要があります。

## 統合 {#integration}

Punchhは、Brazeの顧客が利用できる複数のエンドポイントを提供しています。これは、次のPunchh APIエンドポイントを使用してPunchhプラットフォームにexternal IDを追加するのに役立ちます。external IDを追加したら、Punchhでアダプターを作成し、Braze認証情報を入力して、同期したいイベントを選択します。次に、PunchhセグメントIDを使用して、キャンバスジャーニーで顧客同期をトリガーするPunchh webhookを作成できます。

統合で同期が正しく行われるようにするには、Punchh `user_id`とBraze `external_id`がどちらのプラットフォームでも利用可能でなければなりません。
- PunchhからBrazeに送信されるイベントには、識別子としてBraze `external_id`が含まれます。Punchhが`external_source_id`を使用するように設定されている場合、その値がBraze `external_id`として設定されます。そうでない場合、統合はデフォルトでPunchh `user_id`をBraze `external_id`として設定します。
- BrazeからPunchhへwebhookを送信するには、BrazeユーザープロファイルでPunchh `user_id`が利用できなければなりません。Punchh `user_id`がBraze `external_id`として使用されない場合は、カスタム属性「punchh_user_id」として設定する必要があります。

### ステップ1:external ID取り込みエンドポイントの設定（オプション） {#step-1-set-up-external-id-ingestion-endpoints-optional}

Brazeのexternal IDは、新規および既存のPunchhユーザーの次のエンドポイントを使用して追加できます。

{% alert important %}
`external_source`および`external_source_id`フィールドの値は、Punchhに対して一意であり、既存のプロファイルに関連付けられていてはなりません。
{% endalert %}

1. 新規Punchhユーザー<br>
`external_source`および`external_source_id`フィールドを使用して、PunchhサインアップエンドポイントでPunchhに新しいユーザーを作成します。Punchhでは、外部識別子をユーザープロファイルとともに次のいずれかの登録エンドポイントを介して送信できます。
- [Mobile Signup API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO Signup API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. 既存のPunchhユーザー<br>
既存のPunchhユーザーの`external_source_id`を更新します。Punchhでは、ユーザーAPI更新エンドポイントを介して外部識別子をプロファイルに追加できます。
- [Mobile User Update](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO User Update](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Dashboard User Update](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab ユーザー登録APIの例 %}
この例では、登録時にユーザープロファイルとともに外部識別子を送信できます。これを行うには、`external_source`を「customer_id」として、`external_source_id`を「111111111111111111」として文字列データ型で送信します。

```bash
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab ユーザー更新APIの例 %}
この例では、ユーザープロファイルを使用して外部識別子を更新できます。これを行うには、`external_source`を「customer_id」として、`external_source_id`を「111111111111111111」として文字列データ型で送信します。

```bash
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**プラットフォーム設定:** Punchhで外部識別子を有効にするには、Punchhダッシュボードから**Cockpit** > **Dashboard** > **External User Identifier**に移動します。
{% endalert %}

### ステップ2:PunchhでBrazeアダプターを設定する {#step-2-braze-adapter-setup-in-punchh}

#### 同期できるイベント {#available-events-to-sync}

1. **Guest:** 登録、ゲストプロファイルの更新、非アクティブ化、または削除時にトリガーされます。
2. **Loyalty Check-in:** ロイヤルティトランザクションまたはレシートのバーコードスキャンによる獲得に対してトリガーされます。
3. **Gift Check-in:** キャンペーンで付与されたポイントに対してトリガーされます。
4. **Redemption:** Punchhクーポンを除く報酬償還の場合にトリガーされます。クーポンは発行と償還を含むクーポンイベントとして別途送信されるためです。
5. **Rewards:** キャンペーン、アクティビティ、ポイントからリワードへの変換、または管理者によるギフティングで付与されたリワードからトリガーされます。
6. **Transaction Notifications:** Punchhシステム内でのユーザーのトランザクションアクティビティに対してトリガーされます（ポイントの有効期限など）。
7. **Marketing Notifications:** 関連付けられているユーザーセグメントのPunchhでの各種キャンペーン設定に基づいてトリガーされます。

{% alert note %}
これらの利用可能なイベントのサンプルペイロードの内容については、Punchhのドキュメントを参照してください。
{% endalert %}

Punchh実装マネージャーと協力して、このアダプターを設定します。

BrazeとPunchhの統合を設定するには、次の手順を実行します。

1. Punchhダッシュボードで、**Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management**に移動し、**Enable Webhook Management**をオンに切り替えます。<br><br>
2. 次に、**Settings** > **Webhooks Manager** > **Configurations** > **Show Adapters Tab**に移動してアダプターを有効にし、**Show Adapters Tab**をオンに切り替えます。<br><br>
3. **Settings**タブの**Webhooks Manager**に移動し、**Adapters**タブを選択し、**Create Adapter**をクリックします。<br><br>![Punchh Webhooks ManagerのAdaptersタブでCreate Adapterが選択されている画面。]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. アダプターの名前、説明、および管理メールを入力します。アダプターとして**Braze**を選択し、Braze REST APIエンドポイントとBraze APIキーを入力します。<br><br>
5. 次に、有効にするイベントを選択します。これらのイベントのリストは「[同期できるイベント](#available-events-to-sync)」にあります。<br><br>![Braze同期用の選択可能なイベントが表示されたPunchhアダプター設定画面。]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. **Submit**をクリックしてwebhookを有効にします。

## BrazeでPunchh webhookを作成する {#create-punchh-webhook-in-braze}

Brazeは、Punchhカスタムセグメントを使用してwebhook経由でユーザーをPunchhセグメントに追加できます。

1. Punchhでカスタムセグメントを作成し、以下に示すPunchhセグメントダッシュボードURLに含まれている`custom_segment_id`をメモします。従来のセグメントビルダーまたはベータセグメントビルダーの両方を使用できます。ただし、classicは最終的に非推奨になるため、ベータが推奨されています。<br><br>Punchhプラットフォームで**Guest** > **セグメント** > **Custom List** > **New Custom List**に移動します。<br><br>![URLにカスタムセグメントIDが表示されたPunchhカスタムセグメントダッシュボード。]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Brazeでwebhookキャンペーンを作成するには、ユーザーをカスタムセグメントに追加するためのPunchhエンドポイントをwebhook URLとして使用します。ここでは、URLから取得した`custom_segment_id`と`user_id`をキーと値のペアとして指定できます。<br><br>![Punchhエンドポイントとキーバリューペイロードフィールドが表示されたBraze webhookコンポーザー。]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. このwebhookは、単独のキャンペーンとして、またはキャンバス内のステップとして設定できます。または、この特定のPunchhセグメントにユーザーを追加するwebhookが複数のキャンペーンやキャンバスで使用される場合は、[テンプレート]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)として設定できます。<br><br>
webhook内の`user_id`キーは、PunchhユーザーIDにマッピングされます。ユーザーをPunchhカスタムセグメントに追加するには、Brazeで作成されたすべてのwebhookにこの識別子を追加する必要があります。`punchh_user_id`カスタム属性は、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables)を使用して、`user_id`キーの値として動的に入力できます。`punchh_user_id`カスタム属性変数を挿入するには、テンプレートテキストフィールドのツールバーにある青色の「プラス」アイコンを使用します。<br><br>![PunchhユーザーID Liquid変数が挿入されたBraze webhookペイロードフィールド。]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![punchh_user_idカスタム属性が表示されたBrazeパーソナライゼーションピッカー。]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. webhookが保存されたら、ユーザーの同期に使用できます。たとえば、このBraze webhookキャンペーンを起動すると、136人のゲストがPunchhカスタムセグメントに追加されます。<br><br>![BrazeとPunchhの統合に伴い、保存されたwebhookを使用してユーザーを同期する例。]({% image_buster /assets/img/punchh/punchh6.png %})

BrazeでのWebhookの使用方法の詳細については、[Webhookの作成]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)を参照してください。

## ユースケースキャンペーン {#use-case-campaigns}

### キャンペーンとキャンバスの設定 {#campaign-and-canvas-configuration}

#### トリガー {#triggering}

Brazeに送信されるPunchhイベント（リワードイベントやゲストイベントなど）によりトリガーされるBrazeメッセージングのユースケースは、[アクションベースのキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery)、または該当するPunchhイベントによってトリガーされるキャンバスとして作成できます。

トリガーを追加すると、Brazeで作成されたイベントのリストが表示されます。キャンペーンまたはキャンバスをトリガーし、イベントを記録したユーザーに送信するイベントを選択します。

![アクションベースのキャンペーンでPunchhイベントが選択されたBrazeトリガー設定画面。]({% image_buster /assets/img/punchh/update5.png %})

トリガーイベントをさらに絞り込むには、プロパティフィルターを追加できます。たとえば、顧客が「checkins_gift」イベントをトリガーし、approvedイベントプロパティが`true`の場合にのみメッセージがトリガーされるようにします。これはオプションの機能であり、すべてのユースケースに適用できるわけではありません。

#### セグメンテーション {#segmentation}

多くの場合、PunchhイベントによってトリガーされるBrazeキャンペーンとキャンバスは「すべてのユーザー」オーディエンスに設定できます。これは、これらのイベントをトリガーするユーザーのセグメンテーションがPunchh内で決定されるためです。ただし、イベントによってトリガーされるBrazeメッセージを受信するユーザーのオーディエンスをさらに絞り込む場合は、キャンペーン作成画面の**ターゲットオーディエンス**セクションまたはキャンバス作成画面の**エントリオーディエンス**で、追加のフィルターとセグメントを追加します。

### ユースケース {#use-cases}

{% tabs local %}
{% tab 登録 %}
#### 登録キャンペーン {#sign-up-campaign}

オファーが添付されている登録キャンペーンにBraze設定を使用する場合、Punchh内で登録ギフティングキャンペーンを設定し、Brazeでウェルカムメッセージを設定する必要があります。

Punchhはサインアップキャンペーンに実行遅延を追加することを推奨しています。これにより、Brazeがゲストイベントに基づいてウェルカムメッセージを最初にトリガーできます。ギフトが贈られたことをユーザーに通知するフォローアップメッセージを送信する場合は、リワードイベントに基づいてトリガーできます。

登録キャンペーンの場合、セグメントに「All signed up」を使用できるので、カスタムBrazeセグメントは必要ありません。

必要なPunchh設定:
- キャンペーン:サインアップ
- セグメント:登録済み
- リワード:顧客が選択
必要なイベント:
- リワードイベント
- ゲストイベント
考慮事項:
- 実行遅延として、5〜10分の遅延を追加することをお勧めします

![ユーザーセグメントがPunchhで設定され、ゲストがロイヤルティプログラムに登録されます。この後、ゲストイベント（トリガーされる場合）とBrazeメッセージングキャンペーンがトリガーされます。次に、Punchhサインアップギフティングキャンペーンが10分後にトリガーされ、リワードイベントおよびオプションのフォローアップメッセージをトリガーします。]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Brazeウェルカム %}
#### Brazeウェルカムキャンペーン {#braze-welcome-campaign}

新しいユーザーがサインアップすると、Punchhはユーザーを作成するゲストイベントをBrazeに送信し、カスタム属性`signup_channel`を送信します。これを使用して、Brazeウェルカムキャンペーンをトリガーできます。

Brazeウェルカムキャンペーンを設定するには、次のステップに従います。

1. Brazeで、アクションベースのキャンペーンを作成します。
2. トリガーとして、**Change Custom Attribute Value**を選択し、カスタム属性`signup_channel`を**Any new value**に設定します。
3. キャンペーンの作成を続け、準備ができたら送信します。

{% endtab %}
{% tab マスオファー %}
#### マスオファーキャンペーン {#mass-offer-campaign}

ギフティングにマスオファーキャンペーンを使用する場合、マスオファーキャンペーンはPunchh内で設定し、メッセージングキャンペーンはBrazeで設定する必要があります。

Brazeセグメントをキャンペーンに利用する場合や、Punchhプラットフォームでゲストにギフトを送る前にBrazeからコミュニケーションを送信する場合には、Punchhギフティングキャンペーンに[カスタムPunchhセグメント]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze)が必要になります。

Brazeでこのオファーを受け取るユーザーのセグメントを作成することは、Punchh内で使用できない属性を使用する場合にのみ推奨されます。それ以外の場合は、Punchhセグメンテーションを使用できます。Brazeメッセージングキャンペーンは、ユーザーがリワード（Punchhによってトリガーされるリワードイベント）を受け取ることによって、アクションベースのキャンペーンとして作成されます。

必要なPunchh設定:
- キャンペーン:マスオファー
- セグメント:カスタムリストまたは顧客が選択
- リワード:顧客が選択

**セグメンテーションとギフティングにPunchhを使用し、メッセージングにBrazeを使用する:**<br>
たとえば、2ドル割引リワードが、Punchh内で設定可能なセグメントに送信され、メッセージングはBrazeで送信されます。<br>
![ユーザーセグメントはPunchhで設定可能であり、ユーザーはPunchhマスオファーキャンペーンでギフトを受け取ります。次に、リワードイベントがトリガーされ、次にBrazeメッセージングキャンペーンがトリガーされます。]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Brazeセグメンテーションおよびメッセージングと、ギフティングにPunchhを使用する:**<br>
たとえば、Punchhでは利用できない属性を持つセグメントに送信される2ドル割引リワードとメッセージングです。<br>
![ユーザーセグメントはBrazeで設定でき、メッセージはBrazeセグメントから送信できます。次に、ユーザーはセグメントとユーザーIDを使用してBraze webhookからPunchhカスタムセグメントに送信されます。その後、ユーザーはカスタムセグメントが設定されたPunchhマスオファーキャンペーンでギフトを受け取ります。この後、リワードイベントがトリガーされます。]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**ギフティングとメッセージングのいずれかまたは両方に、BrazeセグメンテーションとPunchhを使用する:**<br>
たとえば、Punchhでは使用できない属性を持つセグメントに2ドル割引リワードが送信されますが、メッセージングが不要であるか、メッセージングをPunchhから送信できます（すべてのゲストがPunchhに存在している必要があることに注意してください）。<br>
![ユーザーセグメントはBrazeで設定でき、ユーザーはセグメントとユーザーIDを使用してBraze webhookからPunchhカスタムセグメントに送信されます。その後、ユーザーはカスタムセグメントが設定されたPunchhマスオファーキャンペーンでギフトを受け取ります。この後、リワードイベントがトリガーされます。]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab 定期的なマスオファー %}
#### 定期的なマスオファーキャンペーン {#recurring-mass-offer-campaign}

定期的なマスオファーキャンペーンをギフティングに使用する場合は、Punchh内でマスオファーキャンペーンを設定し、Brazeでメッセージングキャンペーンを設定する必要があります。顧客がBrazeセグメンテーションを使用する場合は、Punchhカスタムセグメントが必要です（Punchh内で属性を使用できない場合のみ推奨）。それ以外の場合は、Punchhセグメンテーションを使用できます。Brazeメッセージングキャンペーンはリワードイベントに基づいてトリガーされます。

必要なPunchh設定:
- キャンペーン:定期的なマスオファー
- セグメント:カスタムリストまたは顧客が選択
- リワード:顧客が選択
考慮事項:
- キャンペーンIDとキャンペーン名は、イベントのイベントプロパティとしてBrazeに送信されます。Brazeでキャンペーンを受信するオーディエンスをさらにフィルターするためにPunchhキャンペーン識別子を使用する場合は、キャンペーンIDが毎日変更されるため、キャンペーン名を使用する必要があります。

{% endtab %}
{% tab 通知付きチェックイン後オファー %}
#### 通知付きチェックイン後オファーキャンペーン {#post-check-in-offer-campaign-with-notification}

チェックイン後オファーキャンペーンを利用する場合、Brazeはギフティングに関する通知を送信します。ゲストがチェックインすると、Punchhのチェックイン後オファーキャンペーンからギフトが送られます。したがって、チェックイン後オファーキャンペーンはPunchh内で設定し、メッセージングキャンペーンはBraze内で設定する必要があります（顧客にキャンペーンについて通知する場合）。

必要なPunchh設定:
- キャンペーン:チェックイン後のオファー
- セグメント:カスタムリスト
- リワード:顧客が選択

たとえば、この週末に訪問するとポイントが2倍になることをゲストに通知するメールを、Punchhでは使用できない属性を持つセグメントに送信します。対象となるチェックインの完了後に、Punchhがこのセグメントにポイントを付与し、Brazeからオプションのメッセージが送信されます。

![ユーザーセグメントはBrazeで設定され、メッセージはBrazeのチェックイン後キャンペーンから送信されます。次に、対象のユーザーは、セグメントとユーザーIDを使用してBraze webhookからPunchhカスタムセグメントに送信されます。最後に、カスタムセグメントの対象ユーザーがチェックインし、チェックイン後キャンペーンを通じてギフトとオプションメッセージを受け取ります。]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab 通知なしチェックイン後オファー %}
#### 通知なしチェックイン後オファーキャンペーン {#post-check-in-offer-campaign-without-notification}

最初に顧客に通知を送信しないチェックイン後オファーキャンペーンを使用する場合、このキャンペーンはギフトを付与し（オプションのメッセージング）、Braze内で通知をトリガーします。したがって、チェックイン後のオファーキャンペーンはPunchh内で設定する必要がありますが、カスタムリストは必要ありません。代わりに、Punchh内で使用するセグメントを選択できます。

必要なPunchh設定:
- キャンペーン:チェックイン後のオファー
- セグメント:顧客が選択
- リワード:顧客が選択

たとえば、Punchhで使用可能なセグメントに対し、訪問への感謝と次回の訪問で2ドル割引を提供するサプライズBrazeキャンペーンが送信されます。

![対象のユーザーセグメントはPunchh内で設定でき、対象のユーザーがチェックインし、Punchhチェックイン後キャンペーンを通じてギフトを受け取ります。その後、リワードイベントがトリガーされ、Brazeから送信されたリワードをゲストに通知するリコールメッセージが送信されます。]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab 記念日 %}
#### 記念日キャンペーン {#anniversary-campaign}

記念日キャンペーンを利用すると、最初にPunchhキャンペーンから記念日のギフトがユーザーに贈られます。このギフティング（リワードイベント）により、ユーザーにギフトが贈られたことを通知するメッセージングキャンペーンがBraze内でトリガーされます。そのため、カスタムリストは必要ありません。代わりに、Punchh内でセグメントと記念日設定を選択できます。

必要なPunchh設定:
- キャンペーン:記念日キャンペーン
- セグメント:顧客が選択
- リワード:顧客が選択
考慮事項:
- 登録月のギフティング
- 存続期間（誕生日リワードが有効である期間の長さは？）
- 定期的なキャンペーン、スケジュールが必要

![オプションのセグメントはPunchh内で作成でき、対象のユーザーはPunchh記念日キャンペーンからリワードを受け取ります。その後、リワードイベントがトリガーされ、Brazeから送信されたリワードをゲストに通知するリコールメッセージが送信されます。]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab 呼び戻し %}
#### 呼び戻しキャンペーン {#recall-campaign}

休眠状態に基づいてユーザーをターゲット設定するときには、呼び戻しキャンペーンを使用できます。顧客はPunchh内でセグメントとキャンペーンを作成できますが、メッセージングにはBrazeを使用できます。

Brazeで作成されたセグメンテーションを使用する場合は、非アクティブに基づいた[カスタムPunchhセグメント]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze)を定期的なマスオファーキャンペーンにアタッチできます。

必要なPunchh設定:
- キャンペーン:呼び戻しキャンペーン
- セグメント:顧客が選択
- リワード:顧客が選択
考慮事項:
- キャンペーンはスケジュールで実行されます

![オプションのセグメントはPunchh内で作成でき、対象のユーザーはPunchh呼び戻しキャンペーンを介してリワードを受け取ります。この後、リワードイベントがトリガーされ、Brazeから送信されたリワードをゲストに通知するリコールメッセージが送信されます。]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}