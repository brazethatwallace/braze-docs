---
nav_title: SessionM
article_title: SessionM
description: "このリファレンス記事では、カスタマーエンゲージメントとロイヤルティのプラットフォームであるBrazeとSessionMのパートナーシップについて説明します。"
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
---

# SessionMロイヤルティプラットフォーム {#sessionm-loyalty-platform}

> [SessionM](https://sessionm.com/)は、Capillary Technologiesの一部であるカスタマーエンゲージメントとロイヤルティのプラットフォームで、キャンペーン管理機能とロイヤルティ管理ソリューションを提供し、マーケターがターゲットを絞ったアウトリーチを推進してエンゲージメントと収益性を向上させるのを支援します。

## 前提条件 {#prerequisites}

| ソース | 必要条件 | 説明 |
| --- | --- | --- |
| Braze | Braze REST APIキー | `trigger_send`権限を持つBraze REST APIキー。これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze | Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics#endpoints)のBraze URLによって異なります。 |
| BrazeとSessionM | 一致する識別子 | 統合を使用するには、SessionMとBrazeの両方が、それぞれのプラットフォームで使用されている識別子の記録を持っていることを確認してください。`user_id`への参照は、SessionMでのプロファイル作成時に生成されたSessionMのユーザー識別子に対応します。 |
| SessionM | SessionMアカウント | このパートナーシップを利用するには、SessionMのアカウントが必要です。 |
| SessionM | SessionM Core RESTエンドポイント | エンドポイントは、インスタンスのSessionM URLに依存します。これはSessionMダッシュボードの**Digital Properties**から作成できます。 |
| SessionM | SessionM Core REST APIキー | インスタンスとBraze統合に関連付けられたSessionM APIキー。このキーは、タグを含むすべてのコアベースのコールに使用できます。これはSessionMダッシュボードの**Digital Properties**から作成できます。 |
| SessionM | SessionM Core REST APIシークレット | インスタンスとBraze統合に関連付けられたSessionM APIシークレット。このキーは、タグを含むすべてのコアベースのコールに使用できます。これはSessionMダッシュボードの**Digital Properties**から作成できます。 |
| SessionM | SessionM Connect RESTエンドポイント | エンドポイントは、インスタンスのSessionM URLに依存します。SessionMテクニカルアカウントマネージャーまたはデリバリーチームに連絡して提供を受けてください。 |
| SessionM | SessionM Connect REST認可文字列 | インスタンスに関連付けられたSessionM Connect Basic Authorization文字列。この認証文字列は、get_user_offersを含むすべての接続ベースのコールに使用できます。SessionMテクニカルアカウントマネージャーまたはデリバリーチームに連絡して提供を受けてください。 |
| SessionM | SessionM Connect RESTリテーラーID | インスタンスに関連付けられている特定の顧客に対する一意のGUID識別子です。SessionMテクニカルアカウントマネージャーまたはデリバリーチームに連絡して提供を受けてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## ユースケース {#use-cases}

以下のユースケースは、SessionMとBrazeの統合を活用するいくつかの方法を示しています。

- ロイヤルティ、顧客管理、メッセージングの各プラットフォームのデータを統合したセグメンテーションを作成します。
- 堅牢なセグメンテーションを使用して、オファーやプロモーションで特定のユーザーセットをターゲットにします。
- メッセージ送信時に、最新のユーザー、オファー、およびロイヤルティの情報を活用します。
- プロモーションやロイヤルティ活動の進捗状況や完了について、顧客に詳細な通知を行います。
- 新しいオファーが付与されたときに顧客に通知し、オファーの詳細を提供します。

## SessionMとBrazeの統合 {#integrating-sessionm-with-braze}

### ステップ1：Brazeでセグメントを作成する {#step-1-create-a-segment-in-braze}

Brazeで、SessionMのプロモーションやオファーでターゲットとするユーザーのセグメントを作成します。

![「カスタム属性」フィルターを選択したセグメントビルダー。]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### ステップ2：BrazeのセグメントをSessionMにインポートする {#step-2-import-braze-segments-into-sessionm}

#### オプション1：SessionMタグエンドポイントにエクスポートする（推奨） {#option-1-export-to-the-sessionm-tag-endpoint-recommended}

まず、BrazeでWebhookキャンペーンを作成し、Webhook URLを{% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}に設定します。Liquidを使って、URL内で`user_id`を定義します。

生テキストの**リクエストボディ**を使用して、SessionMのユーザープロファイルに追加する希望のタグと、必要な存続時間を含むWebhook本文を作成します。例は次のとおりです。

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![Brazeキャンペーントリガー設定用のJSONペイロードを含むSessionM Webhookコンポーザー。]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

**設定**タブで、各リクエストヘッダーフィールドのキーと値のペアを追加します：
    - 対応する値`application/json`を持つキー`Content-Type`を作成します
    - 対応する値`Basic YOUR-ENCODED-STRING-KEY`を持つキー`Authorization`を作成します。エンドポイントのエンコードされた文字列キーについては、SessionMチームに問い合わせてください。

![Webhookの設定。]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

配信をスケジュールし、[以前に作成した](#step-1-create-a-segment-in-braze)セグメントをターゲットとするように**ターゲットオーディエンス**を設定してから、キャンペーンを開始します。

{% alert important %}
このプロセスは、PostmanなどのAPIクライアントを使用して、[SessionMタグエンドポイント](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag)にリクエストを直接送信することでも実行できます。この場合、リクエストには顧客、タグ名、各ユーザーの存続時間（1回の呼び出しにつき1ユーザー）を指定します。
<br><br>
以下のリクエスト例はcURLを使用しています。

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### オプション2：CSVインポート {#option-2-csv-import}

Brazeセグメンターを使用してBrazeのセグメントをエクスポートし、タグ付けする顧客、タグ名、ファイル内の各ユーザーの存続期間を含むCSVファイルをSessionMに提供します。

## Brazeでリアルタイムのオファーウォレットを取得する {#retrieving-real-time-offer-wallet-with-braze}

SessionMとBrazeを統合することで、Connected Contentを使用して、メッセージ送信時にSessionMのユーザーデータをリアルタイムで取り込むことができ、顧客に古い、有効期限が切れた、または既に償還されたロイヤルティオファーを送信するリスクを排除できます。

次の例では、Connected Contentを使用してオファーウォレットデータをメッセージにテンプレート化しています。ただし、Connected ContentはSessionMのConnectエンドポイントのいずれでも使用できます。

### ステップ1：SessionMでオファーを発行する {#step-1-issue-offer-in-sessionm}

SessionMは、設定可能ないくつかの異なる内部レバーから顧客にオファーを発行します。発行後、オファーはSessionMが「オファーウォレット」と呼ぶ状態に移されます。

顧客は、必要なアクションを実行するかターゲティングを満たす必要があり、SessionM内でオファーが発行されます。

次にSessionMは、発行済みの状態で顧客のウォレットにオファーを追加します。

### ステップ2：SessionMオファーウォレットAPIを呼び出す {#step-2-call-sessionm-offer-wallet-api}

SessionMオファーのあるキャンペーンまたはキャンバスステップで、[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を使用して、[SessionM `get_user_offers`エンドポイント](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/)にAPIコールを行います。

Connected Contentリクエストで、ユーザーのSessionM `user_id`と`retailer_id`を指定して、顧客のウォレットにあるアクティブなオファーの完全なリストを取得します。このエンドポイントへの各リクエストには、1人のユーザーを含めることができます。Connected Contentコールの基本認証ヘッダー用のエンコードされた文字列キーについては、SessionMチームに問い合わせてください。

リクエスト本文では、`culture`のデフォルトは`en-US`ですが、Liquidを使用して、多言語SessionMオファー用にユーザーの言語をテンプレート化することができます（たとえば、{% raw %}`"culture":"{{${language}}}"`{% endraw %}を使用します）。

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### ステップ3：Brazeメッセージングにオファーウォレットを入力する {#step-3-populate-offer-wallet-to-braze-messaging}

エンドポイントにリクエストが行われた後、SessionMは各オファーの完全な詳細とともに、発行済み状態のオファーの完全なリストを返します。これは返されたレスポンスの例です：

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Liquidドット記法を使えば、これをメッセージに入力できます。たとえば、結果として得られる`offer_id`でメッセージをパーソナライズするには、{% raw %}`{{wallet.payload.available_points}}`{% endraw %}を使用してリターンペイロードを活用できます。これは`100`を返します。

{% alert note %}
これは個別のAPIです。500ユーザーを超えるバッチを送信する場合は、SessionMアカウントチームに連絡して、統合にバルクデータを組み込む方法について問い合わせてください。
{% endalert %}

## トリガーメッセージの設定 {#setting-up-triggered-messaging}

SessionMとBrazeの統合により、ユーザープロファイルのデータ、オファーの詳細、ポイント残高がメッセージングにダイナミックに入力され、アクションの時点で顧客にリアルタイムで送信されます。

### ステップ1：SessionMデリバリーチームがテンプレートを設定する {#step-1-sessionm-delivery-team-configures-templates}

SessionMデリバリーチームと協力して、トリガーメッセージングで使用するテンプレートを開発します。SessionMは、ユーザープロファイルのデータ、オファーの詳細、ポイント残高をメッセージングに挿入し、Brazeでトリガーすることで、リアルタイムでの顧客メッセージングを実現します。

SessionMのすべてのテンプレートにある標準フィールドには、以下が含まれます：
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
`broadcast flag`を`true`に設定すると、Brazeのキャンペーンまたはキャンバスがターゲットとするセグメント全体にメッセージが送信されます。
{% endalert %}

特定のニーズに応じてフィールドを追加設定することもできます：

- **オファーデータ：** `offer_id`、`offer title`、`user offer id`、`description`、`terms and conditions`、`logo`、`pos discount id`、`expiration date`
- **ポイント付与データ：** `point award amount`、`point account name`
- **イベントトリガーデータ：** トリガー/送信webhookの結果を利用するトリガーイベント内のすべてのデータ
- **キャンペーン固有データ：** `campaign runtime`、`campaign_id`、`campaign name`、`campaign custom data`

追加フィールドは、メッセージをパーソナライズするための`trigger_properties`としてBrazeに送信されます。

### ステップ2：Brazeのキャンペーンまたはキャンバスを作成する {#step-2-create-a-braze-campaign-or-canvas}

SessionMによってトリガーされるAPIトリガーのキャンペーンまたはキャンバスをBrazeで作成します。`offer_id`や`offer title`などの追加フィールドが設定されている場合は、Liquid（例：{% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}）を使用して、パーソナライズされたフィールドをメッセージングに追加します。

![APIトリガーのプロパティ。]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

**配信をスケジュール**タブで、キャンペーンまたはキャンバスIDをメモします。これはSessionMキャンペーンの**詳細設定**に追加されます。

![APIトリガーキャンペーン。]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

キャンペーンまたはキャンバスの詳細を確定し、**開始**を選択します。

### ステップ3：SessionMのプロモーションまたはメッセージングキャンペーンを作成する {#step-3-create-a-sessionm-promotional-or-messaging-campaign}

次に、SessionMでキャンペーンを作成します。

![SessionMキャンペーン作成画面。]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

SessionMキャンペーンの詳細設定を更新して、`braze_campaign_id`または`braze_canvas_id`を含む以下のJSONペイロードを含めます。

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![SessionMの詳細設定。]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

希望のスケジュールまたはビヘイビアに基づいてメッセージトリガーを作成します。次に、**External Message**メニューの**Messaging Variant**として**Braze Messaging Variant**を選択し、テンプレートを使用します。

![SessionMの外部メッセージ。]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

このテンプレートは、関連する静的属性とダイナミック属性を取得し、Brazeエンドポイントにコールアウトします。

![SessionM Brazeテンプレート。]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}