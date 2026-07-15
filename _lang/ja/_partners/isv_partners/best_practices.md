---
nav_title: ベストプラクティス
hidden: true
---

# ユーザーライフサイクルと識別子のベストプラクティス {#user-lifecycle-and-identifiers-best-practices}

## データ収集 {#data-collection}

Brazeでのデータ収集方法について詳しくは、以下を参照してください。
- [SDKによるデータ収集]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Brazeの識別子 {#braze-identifiers}

- `braze_id`: Brazeが割り当てる識別子で、変更不可能であり、データベース内で作成された時点で特定のユーザーに関連付けられます。
- `external_id`: 顧客が割り当てる識別子で、通常はUUIDです。ユーザーを一意に識別できる場合、`external_id`を割り当てることを推奨します。ユーザーが識別された後は、匿名に戻すことはできません。
- `user_alias`: `external_id`が割り当てられる前に、IDによってユーザーを参照する手段として顧客が割り当てることができる一意の代替識別子です。ユーザーエイリアスは、Brazeの[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを通じて`external_id`が利用可能になった時点で、他のエイリアスまたは`external_id`とマージできます。
    - [ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイント内では、`merge_behavior`フィールドを使用して、ユーザーエイリアスプロファイルのどのデータを既知のユーザープロファイルに保持するかを指定できます。
    - ユーザーエイリアスを送信可能なプロファイルにするには、メールまたは電話番号あるいはその両方を標準属性項目としてプロファイルに含める必要がある点にご注意ください。
- `device_id`: 自動的に生成される、デバイス固有の識別子です。ユーザープロファイルには複数の`device_ids`を関連付けることができます。たとえば、仕事用コンピューター、自宅のコンピューター、タブレット、iOSアプリでアカウントにログインしたユーザーは、プロファイルに4つの`device_ids`が関連付けられます。
- メールアドレスと電話番号:
    - Brazeのユーザー追跡エンドポイントで識別子としてサポートされています。
    - リクエスト内でメールアドレスまたは電話番号を識別子として使用する場合、3つの結果が考えられます。
        1. このメールアドレス/電話番号を持つユーザーがBraze内に存在しない場合、メールのみ/電話番号のみのユーザープロファイルが作成され、リクエスト内のデータがプロファイルに追加されます。
        2. このメールアドレス/電話番号を持つプロファイルがBraze内にすでに存在する場合、リクエストで送信されたデータを含むようにプロファイルが更新されます。
        3. このメールアドレス/電話番号を持つプロファイルが複数あるユースケースでは、最後に更新されたプロファイルが優先されます。
    - メールのみ/電話番号のみのユーザープロファイルが存在し、同じメールアドレス/電話番号を持つ識別済みプロファイルが作成された場合（同じメールアドレスとexternal IDを持つ別のプロファイルなど）、Brazeは2つ目のプロファイルを作成します。それ以降の更新は、external IDを持つプロファイルに送られます。
        - 2つのプロファイルは、Brazeの[/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)エンドポイントを使用してマージできます。

## 匿名ユーザーの取り扱い {#handling-anonymous-users}

`external_id`にアクセスできない状態でBrazeのユーザープロファイルを作成または更新する必要があるユースケースでは、メールアドレスや電話番号などの別の識別子をBrazeの[識別子によるユーザーエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)エンドポイントに渡すことで、そのユーザーのプロファイルがBraze内に存在するかどうかを判断できます。

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Braze内にそのメールアドレスまたは電話番号を持つユーザーが存在する場合、そのユーザーのプロファイルが返されます。存在しない場合は、空の「users」配列が返されます。エクスポートエンドポイントを使用してそのメールアドレスを持つユーザーがすでに存在するかどうかを判断する利点は、匿名ユーザープロファイルがそのユーザーに関連付けられているかどうかを確認できることです。たとえば、SDKで作成された匿名プロファイル（`braze_id`を含むプロファイル）や、以前に作成されたユーザーエイリアスプロファイルなどです。

リクエストがユーザープロファイルを返さない場合は、ユーザーエイリアスを作成するか、メールのみのユーザーを作成するかを選択できます。

### ユーザーエイリアス {#user-alias}

ユーザートラックエンドポイントを使用して、選択した識別子をエイリアス名としてユーザーエイリアスを作成します。新しいユーザーエイリアスが定義されている属性、イベント、または購入オブジェクトに`_update_existing_only`を`false`として含めることで、エイリアスプロファイルを作成し、そのプロファイルに属性、イベント、購入を同時に追加できます。

ユーザーエイリアスを送信可能なプロファイルにするには、以下の例に示すように`email`フィールドにメールアドレスを含める必要があります。

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@example.com",
       "alias_label" : "email"
     },
     "email": "test@example.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

後で`external_id`が利用可能になった時点で、[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを通じてこのユーザーエイリアスを識別し、マージできます。

### メールのみのユーザーの作成 {#creating-an-email-only-user}

ユーザートラックエンドポイントの識別子としてメールアドレスを使用します。

```json
{
    "attributes": [
        {
            "email": "test@example.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
この機能は早期アクセス段階です。
{% endalert %}

## ユーザープロファイルへのデータ同期 {#syncing-data-to-user-profiles}

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- これは一般にアクセス可能なエンドポイントで、ユーザープロファイルへの属性の記録など、Brazeでユーザーを作成および更新できます。このエンドポイントには、ワークスペースレベルで1分あたり50,000件のリクエストというレート制限が適用されています。
- このエンドポイントを使用する場合は、パートナーのドキュメントに記載されているように`partner`キーを含めてください。

[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- ユーザートラックエンドポイントと同様に、クラウドデータ取り込みを通じてデータをユーザープロファイルに同期できます。このツールを使用する場合、目的のBrazeワークスペースに同期するデータウェアハウスのテーブルまたはビューを設定して接続することで、属性、イベント、および購入がプロファイルに記録されます。

[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- Brazeには、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが記録されるデータポイントモデルがあります。このため、変更のあった属性のみをBrazeに送信することを推奨します。

## Brazeへのユーザーオーディエンスの送信 {#sending-audiences-of-users-to-braze}

[コホートインポート同期パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- ユーザーのオーディエンスは、Braze Cohort Import APIエンドポイントを使用して、コホートとしてBrazeに同期できます。これらのオーディエンスをユーザー属性としてユーザープロファイルに保存するのではなく、セグメンテーションツール内のパートナーブランドフィルターを使用してこのコホートを作成し、ターゲットに設定できます。これにより、特定のユーザーセグメントをより効率的に見つけてターゲットにすることができます。
- コホートインポートエンドポイントはパブリックではなく、各パートナーに固有です。このため、コホートエンドポイントへの同期は、顧客のワークスペースのレート制限にカウントされません。

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- これは一般にアクセス可能なエンドポイントで、ユーザー属性を通じて特定のオーディエンスのユーザーを示すことで、Brazeでユーザーをすぐに作成するために使用できます。このエンドポイントとコホートインポートエンドポイントの主な違いは、このエンドポイントを使用して送信されたオーディエンスはユーザープロファイルに保存されるのに対し、コホートインポートエンドポイントではセグメンテーションツールでフィルターとして表示されることです。このエンドポイントには、ワークスペースレベルで1分あたり50,000件のリクエストというレート制限が適用されています。
- このエンドポイントを使用する場合は、[パートナーのドキュメント]({{site.baseurl}}/partners/isv_partners/api_partner)に記載されているように`partner`キーを必ず含めてください。

[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- Brazeには、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが記録されるデータポイントモデルがあります。
- データポイントは、コホートインポートエンドポイントとユーザートラックエンドポイントの両方で発生します。

## パートナーへのエンゲージメント分析ストリーミング {#engagement-analytics-streaming-to-partner}

### Currents

Currentsは、Brazeのほぼリアルタイムのメッセージエンゲージメント分析ストリーミングツールです。顧客のワークスペースから送信されたキャンペーンおよびキャンバスのすべての送信、配信、開封、クリックなどに関するユーザーレベルのデータがストリーミングされます。いくつかの注意点があります。Currentsの価格は顧客のコネクターあたりで設定されるため、すべての新しいCurrentsパートナーはEAプロセスを経る必要があります。カスタムブランドのUIを構築し、コネクターを一般に公開する前に、パートナーにはEAの一部として5社の顧客を確保していただくようお願いしています。
- [パートナーのドキュメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) - Currentsコネクターを購入したすべての顧客がこれらのイベントにアクセスできます。
- [ユーザー行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) - Currentsコネクターを購入したすべての顧客が、これらのイベントを含む「すべてのイベント」コネクターを購入するとは限りません。

### Snowflakeデータシェア {#snowflake-data-share}

Snowflakeデータシェアコネクターを購入した顧客は、メッセージエンゲージメントイベントとユーザー行動イベントの両方に自動的にアクセスできるようになります。Snowflakeデータシェアがパートナー連携として使用される場合、Brazeは顧客に代わってパートナーのSnowflakeインスタンスに共有をプロビジョニングします。クロスリージョンのデータ共有は顧客にとってより高い価格帯となるため、Snowflakeとの連携を希望するパートナーには`US-EAST-1`および/または`EU-CENTRAL-1`にアカウントが必要であるというガイダンスをお伝えしています。
- [パートナーのドキュメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## キャンペーンとキャンバスの構築とトリガー {#building-and-triggering-campaigns-and-canvases}

### Brazeでのアセット作成 {#creating-assets-in-braze}
Brazeは、顧客やパートナーが顧客のワークスペース内でメールテンプレートやContent Blocksを作成・更新できるエンドポイントを多数提供しています。これらのテンプレートとContent Blocksは、顧客のBrazeキャンペーンおよびキャンバス全体で使用できます。
- メールテンプレート
    - [テンプレート作成エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [テンプレート更新エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks)
    - [Content Block作成エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Content Block更新エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### APIトリガーによるキャンペーンとキャンバス {#api-triggered-campaigns-and-canvases}

顧客はキャンペーンやキャンバスをAPIトリガーで起動するように設定できます。これらのキャンペーンをトリガーするAPIリクエストを使用して、APIトリガープロパティとオーディエンスパラメーターまたは受信者パラメーターを渡すことで、キャンペーンをさらにパーソナライズおよびセグメント化できます。
- [APIを使用したキャンペーンのトリガー]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - キャンペーンは、個々のメールのような単発のメッセージです。
- [APIを使用したキャンバスのトリガー]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - キャンバスは、マーケターが複数のメッセージとステップでキャンペーンを作成し、一貫性のあるジャーニーを形成するための統合インターフェイスです。キャンバスをトリガーすると、ユーザーがキャンバスフローに入り、キャンバスの条件に合わなくなるまでメッセージングを受け取り続けます。
- [APIトリガープロパティ/キャンバスエントリプロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - 送信時にメッセージに動的に入力できるデータです。

### APIキャンペーン {#api-campaigns}
APIキャンペーン（このセクションで参照されているAPIトリガーによるキャンペーンとは異なります）を作成する場合、Brazeダッシュボードは`campaign_id`を生成するためにのみ使用されます。これにより顧客はキャンペーンレポートのために分析を追跡できます。キャンペーンメッセージ自体はAPIリクエスト内で定義されます。
- [APIキャンペーンをすぐに送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [APIキャンペーンをスケジュールする]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### 送信ID {#send-ids}
Brazeエンドポイントを使用して送信IDを生成し、キャンペーン分析を送信別に分類できるようにします。たとえば、ロケーションごとに`campaign_id`（APIキャンペーン）が作成されている場合、送信ごとに送信IDを生成して、特定のロケーションに対して異なるメッセージングがどの程度効果的に機能しているかを追跡できます。
- [送信ID]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## コネクテッドコンテンツ {#connected-content}

コネクテッドコンテンツは任意のチャネルタイプ内で使用でき、送信時に指定されたエンドポイントに対してAPIリクエストを実行し、レスポンスで返された内容をメッセージに取り込むことができます。

コネクテッドコンテンツはその汎用性から、多くの顧客がBrazeに存在しないまたは存在できないコンテンツを挿入するために使用する機能となっています。一般的なユースケースとしては、以下のようなものがあります。
- ブログや記事のコンテンツをメッセージにテンプレート化する
- コンテンツレコメンデーション
- 製品メタデータ
- ローカライゼーションと翻訳

以下の点にご注意ください。
- BrazeはAPI呼び出しの料金を請求せず、データポイント使用量にカウントされません。
- コネクテッドコンテンツのレスポンスには1MBの制限があります。
- コネクテッドコンテンツの呼び出しはメッセージの送信時に行われますが、アプリ内メッセージは例外で、メッセージの閲覧時にこの呼び出しが行われます。
- コネクテッドコンテンツの呼び出しはリダイレクトに従いません。Brazeはパフォーマンス上の理由からサーバーの応答時間が2秒未満であることを要求しています。サーバーの応答時間が2秒を超える場合、コンテンツは挿入されません。
- Brazeのシステムは、各受信者に対して同じコネクテッドコンテンツAPI呼び出しを複数回行う場合があります。これは、BrazeがメッセージペイロードをレンダリングするためにコネクテッドコンテンツAPI呼び出しを行う必要がある場合があり、メッセージペイロードは検証、再試行ロジック、またはその他の内部目的のために受信者ごとに複数回レンダリングされることがあるためです。

コネクテッドコンテンツの詳細については、以下の記事を参照してください。
- [コネクテッドコンテンツ呼び出しを実行する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [コネクテッドコンテンツを中止する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [コネクテッドコンテンツの再試行]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)