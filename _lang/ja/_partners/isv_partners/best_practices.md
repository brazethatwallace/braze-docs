---
nav_title: ベストプラクティス
hidden: true
---

# ユーザーライフサイクルと識別子のベストプラクティス {#user-lifecycle-and-identifiers-best-practices}

## データ収集 {#data-collection}

Brazeのデータ収集について詳しくはこちらをご覧ください。
- [SDKデータ収集]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Braze識別子 {#braze-identifiers}

- `braze_id`：Brazeが割り当てる識別子で、データベース内で特定のユーザーに関連付けられた後は変更できません。
- `external_id`：顧客が割り当てる識別子で、通常はUUIDです。ユーザーを一意に識別できる時点で`external_id`を割り当てることを推奨します。ユーザーが識別された後は、匿名に戻すことはできません。
- `user_alias`：`external_id`が割り当てられる前にIDでユーザーを参照する手段として、顧客が割り当てることができる一意の代替識別子です。ユーザーエイリアスは、Brazeの[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを通じて、後から他のエイリアスや`external_id`が利用可能になった時点でマージできます。
    - [ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントでは、`merge_behavior`フィールドを使用して、ユーザーエイリアスプロファイルのどのデータを既知のユーザープロファイルに保持するかを指定できます。
    - ユーザーエイリアスを送信可能なプロファイルにするには、プロファイルにメールおよび／または電話番号を標準属性項目として含める必要があることに注意してください。
- `device_id`：自動的に生成されるデバイス固有の識別子です。1つのユーザープロファイルに複数の`device_ids`を関連付けることができます。たとえば、職場のコンピューター、自宅のコンピューター、タブレット、iOSアプリでアカウントにログインしたユーザーには、プロファイルに4つの`device_ids`が関連付けられます。
- メールアドレスと電話番号：
    - Brazeのユーザー追跡エンドポイントで識別子としてサポートされています。
    - リクエスト内でメールアドレスまたは電話番号を識別子として使用する場合、3つの結果が考えられます。
        1. このメール／電話番号を持つユーザーがBraze内に存在しない場合、メールのみ／電話番号のみのユーザープロファイルが作成され、リクエスト内のデータがプロファイルに追加されます。
        2. このメール／電話番号を持つプロファイルがBraze内にすでに存在する場合、リクエスト内で送信されたデータを含むように更新されます。
        3. このメール／電話番号を持つプロファイルが複数存在するユースケースでは、最後に更新されたプロファイルが優先されます。
    - メールのみ／電話番号のみのユーザープロファイルが存在し、その後同じメール／電話番号を持つ識別済みプロファイルが作成された場合（同じメールアドレスかつexternal IDを持つ別のプロファイルなど）、Brazeは2つ目のプロファイルを作成します。以降の更新はexternal IDを持つプロファイルに送られます。
        - 2つのプロファイルはBrazeの[/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)エンドポイントを使用してマージできます。

## 匿名ユーザーの取り扱い {#handling-anonymous-users}

`external_id`にアクセスできない状態でBrazeのユーザープロファイルを作成または更新する必要があるユースケースでは、メールアドレスや電話番号などの別の識別子をBrazeの[識別子によるユーザーエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)エンドポイントに渡すことで、そのユーザーのプロファイルがBraze内に存在するかどうかを判定できます。

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

そのメールアドレスまたは電話番号を持つユーザーがBraze内に存在する場合、そのプロファイルが返されます。存在しない場合は、空の「users」配列が返されます。エクスポートエンドポイントを使用して、そのメールアドレスを持つユーザーが既に存在するかどうかを判定するメリットは、そのユーザーに関連付けられた匿名ユーザープロファイルがあるかどうかを確認できる点です。たとえば、SDKを通じて作成された匿名プロファイル（`braze_id`を持つもの）や、以前作成されたユーザーエイリアスプロファイルなどです。

リクエストがユーザープロファイルを返さない場合、ユーザーエイリアスを作成するか、メールのみのユーザーを作成するかを選択できます。

### ユーザーエイリアス {#user-alias}

ユーザートラックエンドポイントを使用して、選択した識別子をエイリアス名としてユーザーエイリアスを作成します。新しいユーザーエイリアスが定義されている属性、イベント、または購入オブジェクト内で`_update_existing_only`を`false`に設定することで、エイリアスプロファイルを作成し、同時に属性、イベント、購入をそのプロファイルに追加できます。

ユーザーエイリアスを送信可能なプロファイルにするには、次の例に示すように、`email`フィールドにメールアドレスを含める必要があります。

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

`external_id`が利用可能になった場合、[ユーザー識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを通じて、このユーザーエイリアスを識別してマージできます。

### メールのみのユーザーを作成する {#creating-an-email-only-user}

ユーザートラックエンドポイントで、メールアドレスを識別子として使用します。

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
- これは一般にアクセス可能なエンドポイントで、Brazeでユーザーを作成・更新できます。例えば、ユーザープロファイルに属性を記録することが可能です。このエンドポイントには、ワークスペースレベルで1分あたり50,000リクエストのレート制限が適用されます。
- このエンドポイントを使用する際は、パートナードキュメントに記載されているように`partner`キーを含めてください。

[クラウドデータインジェスチョン]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- ユーザートラックエンドポイントと同様に、クラウドデータインジェスチョンを通じてユーザープロファイルにデータを同期できます。このツールを使用すると、同期したいデータウェアハウスのテーブルまたはビューを設定して目的のBrazeワークスペースに接続することで、属性、イベント、購入をプロファイルに記録できます。

[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- Brazeはデータポイントモデルを採用しており、値が変更されたかどうかに関わらず、ユーザープロファイルへの「書き込み」ごとにデータポイントが記録されます。このため、変更された属性のみをBrazeに送信することを推奨しています。

## Brazeへのユーザーオーディエンスの送信 {#sending-audiences-of-users-to-braze}

[コホートインポート同期パートナードキュメント]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- ユーザーのオーディエンスは、BrazeコホートインポートAPIエンドポイントを使用して、コホートとしてBrazeに同期できます。これらのオーディエンスはユーザー属性としてユーザープロファイルに保存されるのではなく、セグメンテーションツール内のパートナーブランドフィルターを通じてこのコホートを構築し、ターゲティングできます。これにより、特定のユーザーセグメントをより効率的に見つけてターゲティングできます。
- コホートインポートエンドポイントは公開されておらず、各パートナーに固有のものです。そのため、コホートエンドポイントへの同期は顧客のワークスペースレート制限にカウントされません。

[ユーザートラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- これは一般公開されているエンドポイントで、ユーザー属性を通じて特定のオーディエンスに属するユーザーを指定することにより、Brazeでユーザーを即座に作成するために使用できます。このエンドポイントとコホートインポートエンドポイントの主な違いは、このエンドポイントを使用して送信されたオーディエンスはユーザープロファイルに保存されるのに対し、コホートインポートエンドポイントはセグメンテーションツール内のフィルターとして表示される点です。このエンドポイントには、ワークスペースレベルで適用される1分あたり50,000リクエストのレート制限があります。
- このエンドポイントを使用する場合は、[パートナードキュメント]({{site.baseurl}}/partners/isv_partners/api_partner)に示されているように`partner`キーを含めるようにしてください。

[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- Brazeにはデータポイントモデルがあり、値が変更されたかどうかに関係なく、ユーザープロファイルへの「書き込み」ごとにデータポイントが記録されます。
- データポイントは、コホートインポートとユーザートラックエンドポイントの両方で発生します。

## パートナーへのエンゲージメント分析ストリーミング {#engagement-analytics-streaming-to-partner}

### Currents

Currentsは、Brazeのほぼリアルタイムのメッセージエンゲージメント分析ストリーミングツールです。顧客のワークスペースから送信されたキャンペーンやキャンバスのすべての送信、配信、開封、クリックなどに関するユーザーレベルのデータをストリーミングします。いくつかの注意点があります。Currentsは顧客に対してコネクター単位で課金されるため、すべての新規Currentsパートナーは早期アクセス（EA）プロセスを経る必要があります。カスタムブランドUIを構築し、コネクターを一般公開する前に、パートナーにはEAの一環として5社の顧客を確保していただくようお願いしています。
- [パートナードキュメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) - Currentsコネクターを購入したすべての顧客がこれらのイベントにアクセスできます。
- [ユーザー行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) - Currentsコネクターを購入したすべての顧客がこれらのイベントを含む「全イベント」コネクターを購入するわけではありません。

### Snowflakeデータシェア {#snowflake-data-share}

Snowflakeデータシェアコネクターを購入した顧客は、メッセージエンゲージメントイベントとユーザー行動イベントの両方に自動的にアクセスできます。Snowflakeデータシェアがパートナー連携として使用される場合、Brazeは顧客に代わってパートナーのSnowflakeインスタンスにシェアをプロビジョニングします。なお、クロスリージョンのデータシェアは顧客にとってより高い価格帯となるため、Snowflakeとの連携を希望するパートナーには、`US-EAST-1` および/または `EU-CENTRAL-1` にアカウントが必要であるというガイダンスに従っていただくようお願いしています。
- [パートナードキュメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## キャンペーンとキャンバスの構築とトリガー {#building-and-triggering-campaigns-and-canvases}

### Brazeでのアセット作成 {#creating-assets-in-braze}
Brazeは、顧客やパートナーが顧客のワークスペース内でメールテンプレートやContent Blocksを作成・更新できる多数のエンドポイントを提供しています。これらのテンプレートやContent Blocksは、顧客のBrazeキャンペーンやキャンバス全体で使用できます。
- メールテンプレート
    - [テンプレート作成エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [テンプレート更新エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
    - [コンテンツブロック作成エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [コンテンツブロック更新エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### APIトリガーのキャンペーンとキャンバス {#api-triggered-campaigns-and-canvases}

顧客はキャンペーンやキャンバスをAPIトリガーとして設定できます。これらのキャンペーンをトリガーするAPIリクエストは、APIトリガープロパティやオーディエンスまたは受信者パラメーターを渡すことで、キャンペーンのさらなるパーソナライズやセグメンテーションに使用できます。
- [API経由でキャンペーンをトリガーする]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - キャンペーンは、個別のメールなどの単一のメッセージです。
- [API経由でキャンバスをトリガーする]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - キャンバスは、マーケターが複数のメッセージとステップを使ってキャンペーンを作成し、一貫性のあるジャーニーを構成できる統合インターフェイスです。キャンバスをトリガーすると、ユーザーはキャンバスフローに入り、キャンバスの基準を満たさなくなるまでメッセージングを受け続けます。
- [APIトリガープロパティ/キャンバスエントリプロパティ]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - 送信時にメッセージにダイナミックに挿入できるデータです。

### APIキャンペーン {#api-campaigns}
APIキャンペーン（このセクションで説明しているAPIトリガーキャンペーンとは異なります）を作成する場合、Brazeダッシュボードは`campaign_id`を生成するためにのみ使用され、顧客はこれを使ってキャンペーンレポートの分析を追跡できます。キャンペーンメッセージ自体はAPIリクエスト内で定義されます。
- [APIキャンペーンを即時送信する]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [APIキャンペーンをスケジュールする]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### 送信ID {#send-ids}
Brazeエンドポイントを使用して送信IDを生成し、送信ごとにキャンペーン分析を分類できます。例えば、ロケーションごとに`campaign_id`（APIキャンペーン）を作成した場合、送信ごとに送信IDを生成して、特定のロケーションに対するさまざまなメッセージングのパフォーマンスを追跡できます。
- [送信ID]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## Connected Content

Connected Contentは、任意のチャネルタイプで使用でき、送信時に指定されたエンドポイントへAPIリクエストを行い、レスポンスで返された内容をメッセージに挿入します。

Connected Contentの汎用性が高いため、Brazeに保存されていない、または保存できないコンテンツを挿入する機能として、多くのお客様にご利用いただいています。よく見られるユースケースには以下のようなものがあります。
- ブログや記事のコンテンツをメッセージにテンプレート化する
- コンテンツのレコメンデーション
- 商品メタデータ
- ローカライゼーションと翻訳

注意すべき点：
- BrazeはAPIコールに対して課金せず、データポイント使用量にもカウントされません。
- Connected Contentのレスポンスには1MBの制限があります。
- Connected Contentの呼び出しはメッセージの送信時に行われますが、アプリ内メッセージの場合はメッセージが表示された時点で呼び出されます。
- Connected Contentの呼び出しはリダイレクトに従いません。Brazeでは、パフォーマンス上の理由からサーバーのレスポンス時間が2秒以内であることが求められます。サーバーのレスポンスに2秒以上かかる場合、コンテンツは挿入されません。
- Brazeのシステムは、1人の受信者に対して同じConnected Content APIコールを複数回行う場合があります。これは、メッセージペイロードをレンダリングするためにConnected Content APIコールが必要になることがあり、メッセージペイロードはバリデーション、リトライロジック、またはその他の内部目的のために受信者ごとに複数回レンダリングされる可能性があるためです。

Connected Contentの詳細については、以下の記事を参照してください。
- [Connected Contentコールを行う]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Connected Contentを中止する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [Connected Contentのリトライ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)