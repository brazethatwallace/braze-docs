---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "この参考記事では、Braze Currentsと企業向け顧客データプラットフォームであるトレジャーデータとのパートナーシップの概要を説明します。トレジャーデータを使用すると、ジョブ結果をBrazeに直接書き込むことができます。"
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data for Currents

> [トレジャーデータ](https://www.treasuredata.com/)は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまなロケーションにルーティングする顧客データプラットフォーム（CDP）です。

Brazeとトレジャーデータの統合により、2つのシステム間の情報の流れをシームレスに制御できます。Currentsを使用すると、データをトレジャーデータに接続し、グローススタック全体で実用的なデータにすることもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| トレジャーデータ | このパートナーシップを活用するには、[トレジャーデータのアカウント](https://console.treasuredata.com/users/sign_in)が必要です。 |
| Currents | トレジャーデータにデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)を設定する必要があります。 |
| トレジャーデータURL | トレジャーデータのダッシュボードに移動し、取り込みURLをコピーすることで取得できます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{% alert note %}
トレジャーデータは各イベントをバッチ単位でログに記録します。トレジャーデータにクエリしてイベント数を取得する方法については、「[データのクエリ](https://docs.treasuredata.com/articles/int/braze-currents-import-integration/a/h2__592056238)」を参照してください。<br><br>トレジャーデータの新しいBrazeストリーミングコネクターとの統合をお考えの場合は、[Braze Currents Streaming Import Integration](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration/q/braze/qid/72364/qp/4)の詳細なセットアップ手順を参照してください。Brazeとの統合やセットアップに関するご質問は、Brazeアカウントチームまでお問い合わせください。
{% endalert %}

## 統合 {#integration}

トレジャーデータとの接続には、Postback APIを使用することをお勧めします。この方法はデフォルトのコネクターを必要とせず、プッシュ方式でデータを受け取ることができます。1つのデータバッチで送信されるすべてのイベントは、JSON配列の1つの行の1つのフィールド内にあり、必要なデータを取得するために解析する必要があります。

{% alert important %}
現時点では、イベントコレクターを介したトレジャーデータへの取り込みはリアルタイムでは行われず、最大5分かかることがあります。
{% endalert %}

### ステップ1:Brazeを使用してトレジャーデータのPostback APIを設定する {#step-1-setup-treasure-data-postback-api-with-braze}

Postback APIの作成方法については、[トレジャーデータのWebサイト](https://docs.treasuredata.com/display/public/PD/Postback+API)を参照してください。Brazeは、イベントコレクターによる取り込みを除き、更新されたイベントをリアルタイムでトレジャーデータに直接送信します。完了すると、トレジャーデータからデータソースURLが提供されます。このURLをコピーして、次のステップで使用します。

### ステップ2:Currentを作成する {#step-2-create-current}

Brazeで**Currents** > **+ Create Current** > **Treasure Data Export**に移動します。統合名、連絡先メール、およびトレジャーデータURLを指定します。次に、利用可能なイベントのリストから追跡したいものを選択し、**Launch Current**をクリックします。

トレジャーデータに送信されるすべてのイベントには、ユーザーの`external_user_id`が含まれます。この時点では、Brazeは`external_user_id`が設定されていないユーザーのイベントデータをトレジャーデータに送信しません。

{% alert important %}
トレジャーデータURLを最新の状態に保ってください。コネクターのURLが正しくない場合、Brazeはイベントを送信できません。この状態が**5日間**以上続くと、コネクターのイベントは削除され、データは永久に失われます。
{% endalert %}

#### イベントフィールドの値の例 {#example-event-field-value}
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### インジェストされたビューの例 {#example-of-the-ingested-view}

![トレジャーデータのインジェストされたビューの例][4]{: style="max-width:70%;"}

## 統合の詳細 {#integration-details}

Brazeでは、[Currentsイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)にリストされているすべてのデータ（[メッセージエンゲージメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)イベントおよび[顧客行動]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)イベントのすべてのプロパティを含む）をトレジャーデータにエクスポートできます。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクターのペイロード構造と同じです。これは、[カスタムHTTPコネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}