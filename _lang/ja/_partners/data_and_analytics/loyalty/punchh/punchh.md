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

BrazeとPunchhの統合により、ギフティングやロイヤルティの目的で2つのプラットフォーム間でデータを同期できます。Brazeで公開されたデータはセグメンテーションに利用でき、Braze webhookを通じてユーザーデータをPunchhに同期することもできます。

## メリットは何ですか？ {#what-are-the-benefits}

- PunchhからのロイヤルティデータをリアルタイムでBrazeに取り込むことができます。
- Brazeの強力なオーディエンスデータを活用・重ね合わせて、意味のあるダイナミックなクロスチャネル体験（アプリ、モバイル、Web、メール、SMS）を提供できます。
  - 顧客はメールを開封しましたか？顧客は店舗の近くでアプリを開きましたか？
- Brazeを通じて送信されるトランザクションメールの外観と操作性を統一できます。
- ABテストや最適化を随時行いながらジャーニーを作成できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Punchh アカウント | このパートナーシップを利用するには、有効な Punchh アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/api/basics#endpoints)。エンドポイントは、お使いのインスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 他に知っておくべきことは？ {#what-else-should-i-know}

### 統合前に {#before-integrating}

- Brazeとの統合を利用する場合、PunchhとBrazeの2つのキャンペーンが必要です。例えば、オファー付きのキャンペーンを送信する場合、ギフティングキャンペーンはPunchh内で設定し、通知はBrazeから送信できます。
- ゲストはすでにPunchhとBrazeの両方に存在している必要があります。Punchhは、まだロイヤルティゲストではない顧客をフィルタリングします。

### 重要な注意事項 {#important-things-to-note}

- Punchhには、Brazeへのデフォルトユーザー属性の送信を無効にする機能が追加されており、顧客がデータポイントの超過料金を発生させないようにできます。これはアダプターの設定時に構成されます。
- 繰り返しキャンペーンでカスタムセグメントを使用する場合、キャンペーンが実行されるたびにIDが変わるため、キャンペーンIDではなくキャンペーン名を使用する必要があります。
- 各Punchhギフティングキャンペーンで利用可能なコミュニケーションチャネルには、リッチメッセージ、プッシュ通知、SMS、メールがあります。
- ユーザーがBrazeからPunchhカスタムセグメントに送信された後は、削除できません。既存のカスタムセグメントには新しいゲストのみを追加できます。既存のPunchhカスタムセグメントからゲストを削除する必要がある場合は、新しいPunchhカスタムセグメントにユーザーを送信するための新しいwebhookキャンペーンをBrazeで作成する必要があります。

## 統合 {#integration}

Punchhは、以下のPunchh APIエンドポイントを使用して、Punchhプラットフォームにexternal IDを追加するためのエンドポイントをBrazeのお客様に提供しています。external IDを追加したら、Punchhでアダプターを作成し、Brazeの認証情報を入力して、同期するイベントを選択します。次に、PunchhのセグメントIDを使用してPunchh webhookを構築し、キャンバスジャーニーで顧客の同期をトリガーできます。

統合が正しく同期するためには、Punchhの`user_id`とBrazeの`external_id`がいずれかのプラットフォームで利用可能である必要があります。
- PunchhからBrazeに送信されるイベントには、識別子としてBrazeの`external_id`が含まれます。Punchhが`external_source_id`を使用するように設定されている場合、その値がBrazeの`external_id`として設定されます。それ以外の場合、統合はデフォルトでPunchhの`user_id`をBrazeの`external_id`として設定します。
- BrazeからPunchhにwebhookを送信するには、Punchhの`user_id`がBrazeのユーザープロファイルで利用可能である必要があります。Punchhの`user_id`がBrazeの`external_id`として使用されていない場合は、カスタム属性「punchh_user_id」として設定する必要があります。

### ステップ1：external ID取り込みエンドポイントを設定する（オプション） {#step-1-set-up-external-id-ingestion-endpoints-optional}

Brazeからのexternal IDは、以下のエンドポイントを使用して、新規および既存のPunchhユーザーに追加できます。

{% alert important %}
`external_source`および`external_source_id`フィールドの値は、Punchh内で一意であり、既存のプロファイルに関連付けられていない必要があります。
{% endalert %}

1. 新規Punchhユーザー<br>
`external_source`および`external_source_id`フィールドを使用して、Punchhのサインアップエンドポイントで新しいユーザーを作成します。Punchhでは、以下のサインアップエンドポイントのいずれかを通じて、外部識別子をユーザープロファイルとともに送信できます。
- [モバイルサインアップAPI](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSOサインアップAPI](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. 既存のPunchhユーザー<br>
既存のPunchhユーザーの`external_source_id`を更新します。Punchhでは、ユーザーAPI更新エンドポイントを通じて外部識別子をプロファイルに追加できます。
- [モバイルユーザー更新](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSOユーザー更新](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [ダッシュボードユーザー更新](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab ユーザーサインアップAPIの例 %}
この例では、サインアップ時にユーザープロファイルとともに外部識別子を送信できます。`external_source`を「customer_id」、`external_source_id`を「111111111111111111」として、文字列データ型で送信します。

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
この例では、ユーザープロファイルとともに外部識別子を更新できます。`external_source`を「customer_id」、`external_source_id`を「111111111111111111」として、文字列データ型で送信します。

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
**プラットフォーム設定：** Punchhで外部識別子を有効にするには、Punchhダッシュボードから**Cockpit** > **Dashboard** > **External User Identifier**に移動します。
{% endalert %}

### ステップ2：PunchhでBrazeアダプターを設定する {#step-2-braze-adapter-setup-in-punchh}

#### 同期可能なイベント {#available-events-to-sync}

1. **ゲスト：** サインアップ、ゲストプロファイルの更新、無効化または削除時にトリガーされます
2. **ロイヤルティチェックイン：** レシートからバーコードをスキャンしてロイヤルティトランザクションまたは獲得が行われた場合にトリガーされます
3. **ギフトチェックイン：** キャンペーンからポイントがギフトされた場合にトリガーされます
4. **リデンプション：** Punchhクーポンを除く報酬のリデンプション時にトリガーされます。クーポンは発行とリデンプションの両方を含むクーポンイベントとして別途送信されます
5. **報酬：** キャンペーン、アクティビティ、ポイントから報酬への変換、または管理者によるギフトからの報酬が付与された場合にトリガーされます
6. **トランザクション通知：** Punchhシステム内でユーザーのトランザクションアクティビティ（例：ポイントの有効期限切れ）が発生した場合にトリガーされます
7. **マーケティング通知：** Punchhで関連するセグメントのユーザーに対して設定されたさまざまなキャンペーン設定に基づいてトリガーされます

{% alert note %}
これらの利用可能なイベントのサンプルペイロードについては、Punchhのドキュメントを参照してください。
{% endalert %}

このアダプターの設定については、Punchhの実装マネージャーにご相談ください。

BrazeとPunchhの統合を設定するには、以下を行います。

1. Punchhダッシュボードで、**Cockpit** > **Dashboard** > **Major Features** > **Enable Webhook Management**に移動し、**Enable Webhook Management**をオンに切り替えます。<br><br>
2. 次に、**Settings** > **Webhooks Manager** > **Configurations** > **Show Adapters Tab**に移動し、**Show Adapters Tab**をオンに切り替えてアダプターを有効にします。<br><br>
3. **Settings**タブの下にある**Webhooks Manager**に移動し、**Adapters**タブを選択して**Create Adapter**をクリックします。<br><br>![「Create Adapter」が選択されたPunchh Webhooksマネージャーのアダプタータブ。]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. アダプター名、説明、管理者メールを入力します。アダプターとして**Braze**を選択し、BrazeのREST APIエンドポイントとBraze APIキーを入力します。<br><br>
5. 次に、有効にする利用可能なイベントを選択します。これらのイベントの一覧は[同期可能なイベント](#available-events-to-sync)で確認できます。<br><br>![Braze同期用の選択可能なイベントが表示されたPunchhアダプター設定。]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. **Submit**をクリックしてwebhookを有効にします。

## BrazeでPunchh webhookを作成する {#create-punchh-webhook-in-braze}

Brazeでは、Punchhカスタムセグメントを利用したwebhookを使って、Punchhセグメントにユーザーを追加できます。

1. Punchhでカスタムセグメントを作成し、以下の例に示すようにPunchhセグメントダッシュボードのURLに含まれる`custom_segment_id`をメモしてください。クラシックまたはベータのセグメントビルダーのどちらでも使用できます。ただし、クラシックは最終的に廃止されるため、ベータが推奨されます。<br><br>Punchhプラットフォームで、**Guest** > **セグメント** > **Custom List** > **New Custom List**に移動します。<br><br>![PunchhカスタムセグメントダッシュボードでURLにカスタムセグメントIDが表示されている画面。]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Brazeでwebhookキャンペーンを作成し、カスタムセグメントにユーザーを追加するためのPunchhエンドポイントをwebhook URLとして設定します。ここで、URLから取得した`custom_segment_id`と`user_id`をキーと値のペアとして指定できます。<br><br>![Punchhエンドポイントとキーバリューペイロードフィールドが設定されたBraze webhookコンポーザー。]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. このwebhookは、単独のキャンペーンとして、またはキャンバス内のステップとして設定できます。また、この特定のPunchhセグメントにユーザーを追加するwebhookを複数のキャンペーンやキャンバスで使用する場合は、[テンプレート]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates)として設定することもできます。<br><br>
webhook内の`user_id`キーは、PunchhユーザーIDにマッピングされます。この識別子は、Punchhカスタムセグメントにユーザーを追加するためにBrazeで作成するすべてのwebhookに追加する必要があります。`punch_user_id`カスタム属性は、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid#pre-formatted-variables)を使用して`user_id`キーの値として動的に入力できます。テンプレートテキストフィールドのツールバーにある青い「プラス」アイコンを使用して、`punchh_user_id`カスタム属性変数を挿入できます。<br><br>![PunchhユーザーID Liquid変数が挿入されたBraze webhookペイロードフィールド。]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![punchh_user_idカスタム属性が表示されたBrazeパーソナライゼーションピッカー。]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. webhookを保存した後、ユーザーの同期に使用できます。たとえば、このBraze webhookキャンペーンが起動されると、136人のゲストがPunchhカスタムセグメントに追加されます。<br><br>![BrazeとPunchhの統合により、保存されたwebhookを使用してユーザーを同期する例。]({% image_buster /assets/img/punchh/punchh6.png %})

Brazeでのwebhookの使用方法について詳しくは、[webhookを作成する]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)を参照してください。

## ユースケースキャンペーン {#use-case-campaigns}

### キャンペーンとキャンバスの設定 {#campaign-and-canvas-configuration}

#### トリガー {#triggering}

報酬イベントやゲストイベントなど、PunchhからBrazeに送信されるPunchhイベントによってトリガーされるBrazeメッセージングのユースケースは、関連するPunchhイベントによってトリガーされる[アクションベースのキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)またはキャンバスとして作成できます。

トリガーを追加すると、Brazeで作成されたイベントのリストが表示されます。キャンペーンまたはキャンバスをトリガーして、イベントを記録したユーザーに送信するイベントを選択します。

![アクションベースのキャンペーン用にPunchhイベントが選択されたBrazeのトリガー設定。]({% image_buster /assets/img/punchh/update5.png %})

プロパティフィルターを追加して、トリガーイベントをさらに絞り込むことができます。たとえば、顧客が「checkins_gift」イベントをトリガーし、承認済みイベントプロパティが`true`の場合にのみメッセージがトリガーされるようにすることができます。これはオプション機能であり、すべてのユースケースに適用されるとは限りません。

#### セグメンテーション {#segmentation}

多くの場合、Punchhイベントによってトリガーされるキャンペーンやキャンバスは「すべてのユーザー」オーディエンスに設定できます。これは、これらのイベントをトリガーするユーザーのセグメンテーションがPunchh内で決定されるためです。ただし、イベントによってトリガーされるBrazeメッセージングを受け取るユーザーのオーディエンスをさらに絞り込みたい場合は、キャンペーンコンポーザーの**ターゲットオーディエンス**セクションまたはキャンバスコンポーザーの**エントリオーディエンス**で、追加のフィルターやセグメントを追加できます。

### ユースケース {#use-cases}

{% tabs local %}
{% tab サインアップ %}
#### サインアップキャンペーン {#sign-up-campaign}

オファーが付いたサインアップキャンペーンにBraze設定を活用する場合、Punchh内でサインアップギフティングキャンペーンを設定し、Brazeでウェルカムメッセージを設定する必要があります。

Punchhでは、サインアップキャンペーンに実行遅延を追加することを推奨しています。これにより、Brazeがまずゲストイベントに基づいてウェルカムメッセージをトリガーできるようになります。ユーザーにギフトが贈られたことを通知するフォローアップメッセージを送信したい場合は、報酬イベントに基づいてトリガーできます。

サインアップキャンペーンの場合、サインアップ済みの全ユーザーをセグメントとして使用できるため、Brazeのカスタムセグメントは必要ありません。

Punchhの必要な設定：
- キャンペーン：サインアップ
- セグメント：サインアップ済み全員
- 報酬：顧客の選択
必要なイベント：
- 報酬イベント
- ゲストイベント
考慮事項：
- 実行遅延、ゲストに5〜10分の遅延を追加することを推奨

![Punchhでユーザーセグメントが設定され、ゲストがロイヤルティプログラムにサインアップする様子。その後、ゲストイベントがトリガーされるとBrazeメッセージングキャンペーンがトリガーされます。次に、10分後にPunchhサインアップギフティングキャンペーンがトリガーされ、報酬イベントとオプションのフォローアップメッセージがトリガーされます。]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Brazeウェルカム %}
#### Brazeウェルカムキャンペーン {#braze-welcome-campaign}

新規ユーザーがサインアップすると、PunchhはBrazeにゲストイベントを送信し、ユーザーを作成してカスタム属性`signup_channel`を送信します。これを使用してBrazeウェルカムキャンペーンをトリガーできます。

Brazeウェルカムキャンペーンを設定するには、次の手順に従います。

1. Brazeでアクションベースのキャンペーンを作成します。
2. トリガーとして、カスタム属性`signup_channel`が**任意の新しい値**に設定された**カスタム属性値の変更**を選択します。
3. キャンペーンの作成を続行し、準備ができたら送信します。

{% endtab %}
{% tab 一斉オファー %}
#### 一斉オファーキャンペーン {#mass-offer-campaign}

ギフティングに一斉オファーキャンペーンを活用する場合、Punchh内で一斉オファーキャンペーンを設定し、Brazeでメッセージングキャンペーンを設定する必要があります。

キャンペーンにBrazeセグメントを使用したい場合、またはPunchhプラットフォームでゲストにギフティングする前にBrazeからコミュニケーションを送信したい場合は、Punchhギフティングキャンペーンに[Punchhカスタムセグメント]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze)が必要です。

このオファーを受け取るユーザーのセグメントをBrazeで作成することは、Punchh内で利用できない属性を使用する場合にのみ推奨されます。それ以外の場合はPunchhのセグメンテーションを使用でき、Brazeメッセージングキャンペーンは、ユーザーが報酬を受け取ったとき（Punchhによってトリガーされる報酬イベント）にトリガーされるアクションベースのキャンペーンとして作成されます。

Punchhの必要な設定：
- キャンペーン：一斉オファー
- セグメント：カスタムリストまたは顧客の選択
- 報酬：顧客の選択

**Punchhでのセグメンテーションとギフティング、Brazeでのメッセージング：**<br>
たとえば、Punchh内で設定可能なセグメントに2ドル割引の報酬を送信し、メッセージングはBrazeを通じて送信します。<br>
![Punchhでユーザーセグメントを設定でき、ユーザーはPunchh一斉オファーキャンペーンを通じてギフトを受け取ります。次に報酬イベントがトリガーされ、Brazeメッセージングキャンペーンがトリガーされます。]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Brazeのセグメンテーションとメッセージング、Punchhでのギフティング：**<br>
たとえば、Punchhで利用できない属性を持つセグメントに、2ドル割引の報酬とメッセージングを送信します。<br>
![Brazeでユーザーセグメントを設定でき、Braze対Brazeセグメントからメッセージを送信できます。次に、Brazeのwebhookでセグメントとユーザー IDを使用してPunchhカスタムセグメントにユーザーが送信されます。その後、カスタムセグメントを使用したPunchh一斉オファーキャンペーンを通じてユーザーがギフトを受け取ります。その後、報酬イベントがトリガーされます。]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Brazeのセグメンテーションと、Punchhでのギフティングまたはメッセージング、あるいはその両方：**<br>
たとえば、Punchhで利用できない属性を持つセグメントに2ドル割引の報酬を送信しますが、メッセージングは不要か、Punchhを通じて送信できます（すべてのゲストがPunchhに存在している必要があります）。<br>
![Brazeでユーザーセグメントを設定でき、BrazeのwebhookでセグメントとユーザーIDを使用してPunchhカスタムセグメントにユーザーが送信されます。その後、カスタムセグメントを使用したPunchh一斉オファーキャンペーンを通じてユーザーがギフトを受け取ります。その後、報酬イベントがトリガーされます。]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab 定期一斉オファー %}
#### 定期一斉オファーキャンペーン {#recurring-mass-offer-campaign}

ギフティングに定期一斉オファーキャンペーンを活用する場合、Punchh内で一斉オファーキャンペーンを設定し、Brazeでメッセージングキャンペーンを設定する必要があります。顧客がBrazeのセグメンテーションを使用したい場合はPunchhカスタムセグメントが必要です（Punchh内で利用できない属性を使用する場合にのみ推奨されます）。それ以外の場合はPunchhのセグメンテーションを使用でき、Brazeメッセージングキャンペーンは報酬イベントに基づいてトリガーされます。

Punchhの必要な設定：
- キャンペーン：定期一斉オファー
- セグメント：カスタムリストまたは顧客の選択
- 報酬：顧客の選択
考慮事項：
- キャンペーンIDとキャンペーン名は、イベントのイベントプロパティとしてBrazeに送信されます。キャンペーンを受け取るオーディエンスをさらにフィルタリングするためにPunchhキャンペーン識別子をBrazeで使用する場合、キャンペーンIDは毎日変わるため、キャンペーン名を使用する必要があります。

{% endtab %}
{% tab 通知付きチェックイン後オファー %}
#### 通知付きチェックイン後オファーキャンペーン {#post-check-in-offer-campaign-with-notification}

チェックイン後オファーキャンペーンを活用する場合、Brazeがギフティングに関する通知を送信し、ゲストがチェックインすると、Punchhのチェックイン後キャンペーンからギフトが贈られます。したがって、Punchh内でチェックイン後オファーキャンペーンを設定し、Brazeでメッセージングキャンペーンを設定する必要があります（キャンペーンについて顧客に通知する場合）。

Punchhの必要な設定：
- キャンペーン：チェックイン後オファー
- セグメント：カスタムリスト
- 報酬：顧客の選択

たとえば、Punchhで利用できない属性を持つセグメントに、今週末の来店でダブルポイントを獲得できることを通知するメールを送信します。Punchhは、対象のチェックイン後にこのセグメントにポイントをギフティングし、Brazeからオプションのメッセージングを送信します。

![Brazeでユーザーセグメントが設定され、Brazeチェックイン後キャンペーンからメッセージが送信されます。次に、BrazeのwebhookでセグメントとユーザーIDを使用して対象ユーザーがPunchhカスタムセグメントに送信されます。最後に、カスタムセグメント内の対象ユーザーがチェックインし、チェックイン後キャンペーンを通じてギフトとオプションのメッセージを受け取ります。]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab 通知なしチェックイン後オファー %}
#### 通知なしチェックイン後オファーキャンペーン {#post-check-in-offer-campaign-without-notification}

事前に顧客に通知しないチェックイン後オファーキャンペーンを活用する場合、キャンペーンはギフティング（オプションのメッセージング）を行い、Braze内で通知をトリガーします。したがって、Punchh内でチェックイン後オファーキャンペーンを設定する必要がありますが、カスタムリストは必要ありません。代わりに、Punchh内で希望するセグメントを選択できます。

Punchhの必要な設定：
- キャンペーン：チェックイン後オファー
- セグメント：顧客の選択
- 報酬：顧客の選択

たとえば、Punchhで利用可能なセグメントに、来店のお礼と次回の来店で2ドル割引の報酬を通知するサプライズ＆デライトBrazeキャンペーンを送信します。

![Punchh内で対象ユーザーセグメントを設定でき、対象ユーザーがチェックインしてPunchhのチェックイン後キャンペーンを通じてギフトを受け取ります。その後、報酬イベントがトリガーされ、Brazeから送信される報酬通知のリコールメッセージがゲストに送信されます。]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab 記念日 %}
#### 記念日キャンペーン {#anniversary-campaign}

記念日キャンペーンを活用する場合、まずPunchhキャンペーンからユーザーに記念日のギフトが贈られます。このギフティング（報酬イベント）がBraze内のメッセージングキャンペーンをトリガーし、ユーザーにギフティングを通知します。したがって、カスタムリストは必要ありません。代わりに、Punchh内でセグメントと記念日の設定を選択できます。

Punchhの必要な設定：
- キャンペーン：記念日キャンペーン
- セグメント：顧客の選択
- 報酬：顧客の選択
考慮事項：
- サインアップ月のギフティング
- 有効期間（誕生日報酬の有効期限はどのくらいですか？）
- 定期キャンペーン、スケジュールが必要

![Punchh内でオプションのセグメントを作成でき、対象ユーザーがPunchh記念日キャンペーンを通じて報酬を受け取ります。その後、報酬イベントがトリガーされ、Brazeから送信される報酬通知のリコールメッセージがゲストに送信されます。]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab リコール %}
#### リコールキャンペーン {#recall-campaign}

非アクティブなユーザーをターゲットにする場合、リコールキャンペーンを使用できます。顧客はPunchh内でセグメントとキャンペーンを作成し、Brazeをメッセージングに使用できます。

Brazeで作成されたセグメンテーションを使用したい場合は、非アクティブに基づく[Punchhカスタムセグメント]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh#step-3-create-punchh-webhook-in-braze)を定期一斉オファーキャンペーンに紐付けることができます。

Punchhの必要な設定：
- キャンペーン：リコールキャンペーン
- セグメント：顧客の選択
- 報酬：顧客の選択
考慮事項：
- キャンペーンはスケジュールに基づいて実行されます

![Punchh内でオプションのセグメントを作成でき、対象ユーザーがPunchhリコールキャンペーンを通じて報酬を受け取ります。その後、報酬イベントがトリガーされ、Brazeから送信される報酬通知のリコールメッセージがゲストに送信されます。]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}