---
nav_title: FAQ
article_title: Currents の FAQ
page_order: 4
page_type: reference
description: "この記事では、Braze Currents の設定時によくある質問のいくつかについて説明します。"
tool: Currents
---

# よくある質問 {#frequently-asked-questions}

> このページでは、Currentsに関するよくある質問への回答を提供します。

### 特定の日付範囲のCampaignまたはCanvasデータをエクスポートできますか？ {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

特定の日付範囲のCampaignまたはCanvasの指標を取得するには、以下のいずれかの方法を使用してください。

- 標準APIの時間枠外でダッシュボードスタイルのレポートが必要な場合は、日付に合わせたエクスポートの[製品リクエスト](https://portal.braze.com/)を送信してください。
- `ending_at` と `length` パラメーターを指定して [Campaign分析]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)または[Canvas分析]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)エンドポイントを呼び出すか、時系列データには [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) および [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) を使用してください。
- Amazon S3、Azure Blob Storage、またはその他のサポートされている送信先で、継続的にクエリ可能なメッセージエンゲージメントデータが必要な場合は、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)を使用してイベントをウェアハウスにストリーミングしてください。

### ライブのCurrents統合を編集するにはどうすればよいですか？ {#how-do-i-edit-a-live-currents-integration}

ライブのCurrentsコネクターを変更するには、統合を開き、ページの左下にある**編集**をクリックします。**編集**がない場合、統合UIは読み取り専用のままとなり、アイコンだけではコネクター設定を変更できません。

### BrazeはAzure Blob StorageのAvroファイルをアップロード後にどのように処理しますか？ {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Brazeは、アップロード完了後に [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) のAvroファイルを変更しません。Azureは、アップロードがまだ進行中の場合、Blobの削除をブロックすることがあります。

### 履歴データを取得するにはどうすればよいですか？ {#how-do-i-get-historical-data}

Currentsはリアルタイムのライブデータストリームです。つまり、イベントを再生することはできません。ただし、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) や [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) などのデータウェアハウスにCurrentsデータを保存できるため、過去のイベントを必要に応じて処理できます。データは30日間保持されますが、さらに過去の履歴データについては、[Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake/)をクエリできます。

### CurrentsがJSONではなくAvro形式でデータを出力するのはなぜですか？ {#why-does-currents-output-data-in-the-avro-format-not-json}

Avroは、スキーマレスのJSONとは異なり、スキーマの進化をネイティブでサポートしています。また、Avroは圧縮性が高いため、より少ない帯域幅でAvroファイルを送信でき、ストレージ容量も節約できるという利点があります。

### Brazeはファイルのオーバーヘッドをどのように処理しますか？ {#how-does-braze-handle-file-overhead}

Extract, Transform, Load（ETL）プロセスを構築しています。このプロセスにより、あるデータベースから大量のデータを取り出し、別のデータベースに格納できます。

### クエリのためにこのデータをどこに保存すればよいですか？ {#where-should-i-store-this-data-for-querying}

Brazeは、クエリ用にデータを保存できる複数のデータウェアハウスと提携しています。以下を使用することをお勧めします。
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)

### Currentsデータの信頼性はどの程度ですか？ {#how-reliable-is-currents-data}

Currentsは「at-least-once（少なくとも1回）」の配信を保証しています。つまり、重複イベントがストレージバケットに書き込まれることがあります。ユースケースで厳密に1回の配信が必要な場合は、すべてのイベントに付与されるユニーク識別子フィールド（`id`）を使用してイベントの重複を排除できます。詳細については、[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/)を参照してください。

### データはどのくらいの頻度でCurrentsに同期されますか？ {#how-often-is-data-synced-to-currents}

データは継続的にストリーミングされます。Brazeは、送信するバッチがいっぱいになるたびに、または5分ごとに（いずれか早い方で）イベントのバッチを送信します。大量のコネクターの場合、データはほぼリアルタイムで届きます。少量のコネクターの場合、データの到着には5〜30分かかることがあります。詳細については、[Avro書き込みしきい値]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/#avro-write-threshold)を参照してください。

{% alert note %}
デバイスがインターネットに接続されていない場合、イベントの作成に遅延が生じることがあります。これはアプリ内メッセージイベントで最もよく見られます。アプリ内メッセージはオフラインでもトリガーされることがあるためです。
{% endalert %}

### Currentsで利用可能なイベントを確認するにはどうすればよいですか？ {#how-do-i-find-which-events-are-available-for-currents}

Currentsがログに記録するイベントの完全なリストについては、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)の用語集を参照してください。これらの用語集はイベントタイプ（送信、配信、開封など）でフィルターできます。

### Currentsのメール開封またはクリックイベントの `external_id` がBrazeダッシュボードのユーザープロファイルと異なるのはなぜですか？ {#why-does-the-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Brazeダッシュボードの場合：** あるメールアドレスに関連付けられたユーザーがメールを開封またはクリックすると、そのメールアドレスを共有するすべてのユーザープロファイルが、そのメールを開封またはクリックしたとしてマークされます。詳細については、[メールが送信されたとき、複数のプロファイルが同じメールアドレスを持っている場合はどうなりますか？]({{site.baseurl}}/user_guide/channels/email/faq/#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)を参照してください。
- **Currentsの場合：** 同じ開封またはクリックは1つのプロファイルに保存されます。Brazeは、送信時に元々ターゲットとされたプロファイルがまだそのメールアドレスを共有している場合、そのプロファイルに帰属させます。そうでない場合、Brazeはそのメールアドレスを共有するプロファイルの中からランダムに選択された1つのプロファイルに帰属させます。

このため、Currentsのメール開封またはクリックイベントの `external_id` は、CurrentsとBrazeダッシュボードを比較したときに期待するユーザープロファイルと一致しない場合があります。

### すべての送信イベントはCurrentsにログ記録されますか？ {#are-all-send-events-logged-to-currents}

すべてのイベントはCurrentsにログ記録されます。Currentsストリームからイベントが意図的に抑制されるシナリオはありません。

### Currentsでデータが破損することはありますか？ {#can-data-be-corrupted-in-currents}

通常の状況では、Currentsデータは破損しません。まれな問題が発生する可能性は常にありますが、データが体系的に破損する既知の条件はありません。

### Currents統合を設定する前の日付のカスタムイベントデータが表示されるのはなぜですか？ {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

BrazeはCurrentsにイベントをバックフィルしません。ただし、カスタムイベントは過去のタイムスタンプでログ記録されることがあります（たとえば、イベント発生時にデバイスがオフラインで、後から同期された場合など）。このような場合、イベントのタイムスタンプはイベントが最初に発生した時刻を反映するため、Currents統合が設定される前の日付になることがあります。

### Currentsの送信イベントにカスタム属性を含めることはできますか？ {#can-i-include-custom-attributes-in-currents-send-events}

いいえ。Currentsは送信イベントにカスタム属性を含めません。Currentsはカスタムイベントとメッセージエンゲージメントイベントをログ記録します。利用可能なフィールドの完全なリストについては、[イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/)を参照してください。

### CurrentsにはCampaignタグやキーと値のペアが含まれますか？ {#does-currents-include-campaign-tags-or-key-value-pairs}

いいえ。CurrentsにはCampaignタグやメッセージレベルのキーと値のペアは含まれません。回避策として、Campaign内のWebhookチャネルを使用し、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)でタグやキーと値のペアのデータをテンプレート化して、独自のエンドポイントにこの情報を送信できます。

### BrazeはCurrentsの変更をどのように顧客に通知しますか？ {#how-does-braze-notify-customers-of-changes-to-currents}

Currentsの変更（新しいイベントフィールドやイベントタイプなど）が発生した場合、Brazeは過去30日以内にダッシュボードを使用したアクティブなCurrents統合を持つすべての顧客にメールを送信します。最新の変更については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)も参照できます。

### Currentsデータにはどのくらいのストレージが必要ですか？ {#how-much-storage-do-i-need-for-currents-data}

ストレージ要件は、イベントの量とエクスポートするイベントの種類によって異なります。Brazeは [Avro形式のサンプルイベント](https://github.com/appboy/currents-examples/tree/master/sample-data)を提供しており、ユースケースに合わせてファイルサイズを見積もることができます。

### CurrentsデータでCampaign名やキャンバスステップ名が `NULL` になるのはなぜですか？ {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

新しいCampaignやCanvasを作成すると、名前がすべてのBrazeシステムに伝播するまでに時間がかかることがあります。この時間枠内にCurrentsを通じて送信されたイベントでは、名前フィールド（`campaign_name` や `canvas_step_name` など）が `NULL` になることがあります。これは、イベントがログ記録される直前に名前が変更された場合にも発生します。これを回避するには、CampaignやCanvasステップを作成または名前変更した後、送信前にしばらく時間を置いてください。

### Currentsでセッション終了イベントが遅延または欠落するのはなぜですか？ {#why-are-session-end-events-delayed-or-missing-in-currents}

セッション終了イベントは、SDKの通常のアップロードスケジュールに従います。Braze SDKはセッションデータをローカルにキャッシュし、ネットワーク品質に基づいて定期的にフラッシュします。たとえば、良好な接続では約10秒ごとにフラッシュされます。SDKがイベントをアップロードするまで、Currentsには表示されません。

ユーザーが次のフラッシュの前にアプリを強制終了したりオフラインになったりした場合、セッション終了イベントが遅延するか、まったく届かないことがあります。iOSでは、SDKがバックグラウンドでデータを送信できないため、セッション終了イベントはアプリが再度開かれるまでフラッシュされないことがよくあります。

Currentsでよりタイムリーなセッション境界が必要な場合は、アプリがバックグラウンドに移行するときやフォアグラウンドに戻るときなどのライフサイクルポイントで `requestImmediateDataFlush()` を呼び出してください。詳細については、[データのアップロードとダウンロード]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/#data-upload-and-download)および[セッション終了とセッション開始のタイムスタンプが類似している（iOS）]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/#session-end-and-session-start-have-similar-timestamps-ios)を参照してください。

### Currentsがデータを書き込もうとしたときにストレージバケットが利用できない場合はどうなりますか？ {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

データ転送時にストレージバケットが利用できない場合、そのデータは失われます。Brazeは正常に配信されなかったイベントをバックフィルすることはできません。データ損失を防ぐために、ストレージバケットが常に利用可能で適切に設定されていることを確認してください。

### Currents統合の編集時に「You do not have any remaining Customer Behavior Events entitlements」と表示されるのはなぜですか？ {#why-do-i-see-you-do-not-have-any-remaining-customer-behavior-events-entitlements-when-editing-my-currents-integration}

このメッセージは、既存のCurrents統合を更新する際に、ワークスペースが顧客行動イベントのエンタイトルメント上限に達した場合に表示されることがあります。エンタイトルメントのリクエストや設定の調整については、Brazeアカウントマネージャーにお問い合わせください。

### ストレージパスのCurrentsバージョンはどのくらいの頻度で変更されますか？ {#how-often-does-the-currents-version-in-the-storage-path-change}

ストレージパスの `version=<currents_version>` セグメントは、Currentsのリリースごとに月次のペースで更新されます（たとえば、`version=6` から `version=7`）。特定のバージョンセグメントをハードコーディングするのではなく、ルートパスからファイルを再帰的に読み取ることをお勧めします。これにより、バージョン変更後もパイプラインが自動的にデータを取得できます。パス形式の詳細については、[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics/)を参照してください。バージョンごとの変更履歴については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/)を参照してください。

### メッセージエンゲージメントイベントで `campaign_id` や `canvas_id` が欠落しているのはなぜですか？ {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

イベントタイプとコンテキストによっては、メッセージエンゲージメントイベントが特定のCampaignやキャンバスステップに紐付けられていない場合があります。その場合、`campaign_id`、`canvas_id`、および関連する名前フィールドはイベントペイロードから省略されることがあります。特定のイベントでこれらのフィールドが表示されない場合は、そのイベントタイプとコンテキストが通常CampaignやCanvasの識別子を含むかどうかを確認してください。