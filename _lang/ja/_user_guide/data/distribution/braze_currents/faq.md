---
nav_title: FAQ
article_title: Currents の FAQ
page_order: 4
page_type: reference
description: "この記事では、Braze Currents の設定時によくある質問のいくつかについて説明します。"
tool: Currents
---

# よくある質問

> このページには Currents に関するよくある質問とその回答を掲載しています。

### 履歴データを取得するには？

Currents はリアルタイムのライブデータストリームです。つまりイベントを再生することはできません。ただし、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) や [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) などのデータウェアハウスに Currents データを保存できるため、過去のイベントを必要に応じて処理できます。データは30日間保持されますが、さらに過去の履歴データについては、[Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake/) をクエリできます。

### Currents が JSON ではなく Avro 形式でデータを出力するのはなぜですか？

Avro は、スキーマレスの JSON とは異なり、スキーマの進化をネイティブでサポートしています。また、Avro は圧縮性が高いため、より少ない帯域幅で Avro ファイルを送信でき、ストレージ容量も節約できるという利点があります。

### Braze はファイルのオーバーヘッドをどのように処理しますか？

Extract, Transform, Load（ETL）プロセスを構築しています。このプロセスにより、あるデータベースから大量のデータを取り出し、別のデータベースに格納できます。

### クエリのためにこのデータをどこに保存すればよいですか？

Braze は、クエリ用にデータを保存できる複数のデータウェアハウスと提携しています。以下を使用することをお勧めします。
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)

### Currents データの信頼性はどの程度ですか？

Currents は「at-least-once（少なくとも1回）」の配信を保証しています。つまり、重複イベントがストレージバケットに書き込まれることがあります。ユースケースで厳密に1回の配信が必要な場合は、すべてのイベントに付与されるユニーク識別子フィールド（`id`）を使用してイベントの重複を排除できます。詳細については、[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/)を参照してください。

### データはどのくらいの頻度で Currents に同期されますか？

データは継続的にストリーミングされます。Braze は、送信するバッチがいっぱいになるたびに、または5分ごとに（いずれか早い方で）イベントのバッチを送信します。大量のコネクターの場合、データはほぼリアルタイムで届きます。少量のコネクターの場合、データの到着には5〜30分かかることがあります。詳細については、[Avro 書き込みしきい値]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/#avro-write-threshold)を参照してください。

{% alert note %}
デバイスがインターネットに接続されていない場合、イベントの作成に遅延が生じることがあります。これはアプリ内メッセージイベントで最もよく見られます。アプリ内メッセージはオフラインでもトリガーされることがあるためです。
{% endalert %}

### Currents で利用可能なイベントを確認するには？

Currents がログに記録するイベントの完全なリストについては、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)の用語集を参照してください。これらの用語集はイベントタイプ（送信、配信、開封など）でフィルターできます。

### Currents のメール開封またはクリックイベントの `external_id` が Braze ダッシュボードのユーザープロファイルと異なるのはなぜですか？

- **Braze ダッシュボードの場合：**あるメールアドレスに関連付けられたユーザーがメールを開封またはクリックすると、そのメールアドレスを共有するすべてのユーザープロファイルが、そのメールを開封またはクリックしたとしてマークされます。詳細については、[メールが送信されたとき、複数のプロファイルが同じメールアドレスを持っている場合はどうなりますか？]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)を参照してください。
- **Currents の場合：**同じ開封またはクリックは1つのプロファイルに保存されます。Braze は、送信時に元々ターゲットとされたプロファイルがまだそのメールアドレスを共有している場合、そのプロファイルに帰属させます。そうでない場合、Braze はそのメールアドレスを共有するプロファイルの中からランダムに選択された1つのプロファイルに帰属させます。

このため、Currents のメール開封またはクリックイベントの `external_id` は、Currents と Braze ダッシュボードを比較したときに期待するユーザープロファイルと一致しない場合があります。

### すべての送信イベントは Currents にログ記録されますか？

すべてのイベントは Currents にログ記録されます。Currents ストリームからイベントが意図的に抑制されるシナリオはありません。

### Currents でデータが破損することはありますか？

通常の状況では、Currents データは破損しません。まれな問題が発生する可能性は常にありますが、データが体系的に破損する既知の条件はありません。

### Currents 統合を設定する前の日付のカスタムイベントデータが表示されるのはなぜですか？

Braze は Currents にイベントをバックフィルしません。ただし、カスタムイベントは過去のタイムスタンプでログ記録されることがあります（たとえば、イベント発生時にデバイスがオフラインで、後から同期された場合など）。このような場合、イベントのタイムスタンプはイベントが最初に発生した時刻を反映するため、Currents 統合が設定される前の日付になることがあります。

### Currents の送信イベントにカスタム属性を含めることはできますか？

いいえ。Currents は送信イベントにカスタム属性を含めません。Currents はカスタムイベントとメッセージエンゲージメントイベントをログ記録します。利用可能なフィールドの完全なリストについては、[イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/)を参照してください。

### Currents には Campaign タグやキーと値のペアが含まれますか？

いいえ。Currents には Campaign タグやメッセージレベルのキーと値のペアは含まれません。回避策として、Campaign 内の Webhook チャネルを使用し、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) でタグやキーと値のペアのデータをテンプレート化して、独自のエンドポイントにこの情報を送信できます。

### Braze は Currents の変更をどのように顧客に通知しますか？

Currents の変更（新しいイベントフィールドやイベントタイプなど）が発生した場合、Braze は過去30日以内にダッシュボードを使用したアクティブな Currents 統合を持つすべての顧客にメールを送信します。最新の変更については、[Currents 変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)も参照できます。

### Currents データにはどのくらいのストレージが必要ですか？

ストレージ要件は、イベントの量とエクスポートするイベントの種類によって異なります。Braze は [Avro 形式のサンプルイベント](https://github.com/braze-inc/currents-examples/tree/master/sample-data)を提供しており、ユースケースに合わせてファイルサイズを見積もることができます。

### Currents データで Campaign 名やキャンバスステップ名が `NULL` になるのはなぜですか？

新しい Campaign や Canvas を作成すると、名前がすべての Braze システムに伝播するまでに時間がかかることがあります。この時間枠内に Currents を通じて送信されたイベントでは、名前フィールド（`campaign_name` や `canvas_step_name` など）が `NULL` になることがあります。これは、イベントがログ記録される直前に名前が変更された場合にも発生します。これを回避するには、Campaign やキャンバスステップを作成または名前変更した後、送信前にしばらく時間を置いてください。

### Currents がデータを書き込もうとしたときにストレージバケットが利用できない場合はどうなりますか？

データ転送時にストレージバケットが利用できない場合、そのデータは失われます。Braze は正常に配信されなかったイベントをバックフィルすることはできません。データ損失を防ぐために、ストレージバケットが常に利用可能で適切に設定されていることを確認してください。

### Currents 統合の編集時に「You do not have any remaining Customer Behavior Events entitlements」と表示されるのはなぜですか？

このメッセージは、既存の Currents 統合を更新する際に、ワークスペースが顧客行動イベントのエンタイトルメント上限に達した場合に表示されることがあります。エンタイトルメントのリクエストや設定の調整については、Braze アカウントマネージャーにお問い合わせください。

### ストレージパスの Currents バージョンはどのくらいの頻度で変更されますか？

ストレージパスの `version=<currents_version>` セグメントは、Currents のリリースごとに月次のペースで更新されます（たとえば、`version=6` から `version=7`）。特定のバージョンセグメントをハードコーディングするのではなく、ルートパスからファイルを再帰的に読み取ることをお勧めします。これにより、バージョン変更後もパイプラインが自動的にデータを取得できます。パス形式の詳細については、[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/)を参照してください。バージョンごとの変更履歴については、[Currents 変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)を参照してください。

### メッセージエンゲージメントイベントで `campaign_id` や `canvas_id` が欠落しているのはなぜですか？

イベントタイプとコンテキストによっては、メッセージエンゲージメントイベントが特定の Campaign やキャンバスステップに紐付けられていない場合があります。その場合、`campaign_id`、`canvas_id`、および関連する名前フィールドはイベントペイロードから省略されることがあります。特定のイベントでこれらのフィールドが表示されない場合は、そのイベントタイプとコンテキストが通常 Campaign や Canvas の識別子を含むかどうかを確認してください。