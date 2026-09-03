---
nav_title: FAQ
article_title: Currents FAQ
page_order: 4
page_type: reference
description: "この記事では、Braze Currentsの設定時によくある質問のいくつかについて説明します。"
tool: Currents
---

# よくある質問 {#frequently-asked-questions}

> このページでは、Currentsに関するよくある質問への回答を提供します。

## 特定の日付範囲でキャンペーンやキャンバスのデータをエクスポートできますか？ {#can-i-export-campaign-or-canvas-data-for-a-specific-date-window}

定義された日付範囲のキャンペーンまたはキャンバスの指標を取得するには、以下のいずれかの方法を使用してください。

- {% multi_lang_include product_feedback_cta.md context="gap" feature="date-aligned campaign or キャンバス exports for dashboard-style reporting outside standard API windows" %}
- `ending_at`および`length`パラメーターを使用して、[キャンペーン分析]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)または[キャンバス分析]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)エンドポイントを呼び出します（または時系列データには[`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)および[`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics)を使用します）。
- 継続的にクエリ可能なメッセージエンゲージメントデータが必要な場合は、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を使用してイベントをAmazon S3、Azure Blob Storage、またはその他のサポートされている送信先にあるデータウェアハウスにストリーミングします。

## ライブのCurrentsインテグレーションを編集するにはどうすればよいですか？ {#how-do-i-edit-a-live-currents-integration}

ライブのCurrentsコネクターを変更するには、インテグレーションを開き、**編集**を選択します。**編集**がなければ、インテグレーションUIは読み取り専用のままとなり、アイコンだけではコネクターの設定を変更できません。

## Brazeはアップロード後にAzure Blob StorageのAvroファイルをどのように処理しますか？ {#how-does-braze-handle-azure-blob-storage-avro-files-after-upload}

Brazeは、アップロード完了後に[Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)内のAvroファイルを変更しません。Azureは、アップロードがまだ進行中の間、Blobの削除をブロックする場合があります。

## 過去のデータを取得するにはどうすればよいですか？ {#how-do-i-get-historical-data}

Currentsはリアルタイムのライブデータストリームであるため、イベントを再生することはできません。ただし、[Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)や[Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)などのデータウェアハウスにCurrentsデータを保存できるため、過去のイベントに対して必要に応じてアクションを実行できます。データは30日間保持されますが、より過去のデータについては、[Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/s3_to_snowflake)でクエリを実行できます。

## CurrentsがJSONではなくAvro形式でデータを出力するのはなぜですか？ {#why-does-currents-output-data-in-the-avro-format-not-json}

スキーマを持たないJSONとは異なり、Avroはスキーマの進化をネイティブにサポートしています。また、Avroは高い圧縮率を備えているため、Avroファイルをより少ない帯域幅で送信でき、ストレージ容量を節約できるというメリットもあります。

## Brazeはファイルのオーバーヘッドをどのように処理しますか？ {#how-does-braze-handle-file-overhead}

Brazeは、Extract, Transform, Load（ETL）プロセスを構築しており、1つのデータベースから大量のデータを引き出し、別のデータベースに配置して保存できます。

## クエリのためにこのデータをどこに保存すべきですか？ {#where-should-i-store-this-data-for-querying}

Brazeは、クエリのためにデータを保存できる複数のデータウェアハウスと提携しています。以下の使用をお勧めします。
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)

## Currentsのデータはどの程度信頼できますか？ {#how-reliable-is-currents-data}

Currentsは「少なくとも1回」の配信を保証しています。つまり、重複イベントがストレージバケットに書き込まれることがあります。ユースケースで厳密に1回だけの配信が必要な場合は、すべてのイベントに含まれる一意の識別子フィールド（`id`）を使用してイベントの重複を排除できます。詳細については、[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics)を参照してください。

## Currentsへのデータ同期はどのくらいの頻度で行われますか？ {#how-often-is-data-synced-to-currents}

データは継続的にストリーミングされます。Brazeは、送信するイベントのバッチが満杯になるたびに、または5分ごとに（いずれか早い方で）バッチを送信します。大量データのコネクターでは、データはほぼリアルタイムで到着します。少量データのコネクターでは、データの到着に5〜30分かかることがあります。詳細については、[Avro書き込み閾値]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics#avro-write-threshold)を参照してください。

{% alert note %}
デバイスがインターネットに接続されていない場合、イベントの作成に遅延が発生することがあります。これはアプリ内メッセージイベントで最も一般的です。アプリ内メッセージはオフライン時にもトリガーできるためです。
{% endalert %}

## Currentsで利用可能なイベントを確認するにはどうすればよいですか？ {#how-do-i-find-which-events-are-available-for-currents}

Currentsがログに記録するイベントの完全なリストについては、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)の用語集を参照してください。これらの用語集は、イベントタイプ（送信、配信、開封など）でフィルターできます。

## Currentsのイベント数がダッシュボードやEngagement Reportの指標と一致しないのはなぜですか？ {#why-do-my-currents-event-counts-not-match-my-dashboard-or-engagement-report-metrics}

Currentsとブレイズのダッシュボードでは、特定の指標の計算方法が異なるため、Currentsのイベントとダッシュボードの指標が完全に一致することは想定されていません。

**ユニーククリック：** メールの場合、ダッシュボードは7日間のユニーククリックを追跡し、`dispatch_id`ごとに測定します。Currentsは各生のクリックイベントを記録します。Currentsベースのユニーククリック数をダッシュボードの指標と一致させるには、`is_unique`が`true`であるイベントをフィルターしてください。

**購読解除：** ダッシュボードの*購読解除*指標は、Brazeの標準的な購読解除リンクのクリックを反映しています。カスタムの購読解除ページでは、APIを通じてユーザーを更新しない限り、この指標は増加しません。Currentsの`users.messages.email.Unsubscribe`イベントは、ユーザーがメール本文やフッターの購読解除リンク、またはlist-unsubscribeヘッダーを通じてクリックした際に発火する、特殊なクリックイベントです。これはすべてのメール購読ステータスの変更を表すものではありません。

**タイムスタンプとタイムゾーン：** CurrentsのタイムスタンプはすべてUTCです。ダッシュボードの指標は、企業のタイムゾーンに従います。Currentsのデータを企業のタイムゾーンに変換せずに暦日で集計すると、ダッシュボードに表示される日付とは異なる日付バケットにカウントが分類される場合があります。

**重複イベント：** Currentsはat-least-once配信を提供しているため、重複イベントが記録されることがあります。ダッシュボードの指標と比較する前に、各イベントの一意の`id`フィールドで重複を排除してください。

## Currentsのメール開封やクリックイベントの`external_user_id`（Brazeスキーマ：`external_id`）がBrazeダッシュボードのユーザープロファイルと異なるのはなぜですか？ {#why-does-the-external_user_id-braze-schema-external_id-in-my-currents-email-open-or-click-event-differ-from-the-user-profile-in-the-braze-dashboard}

- **Brazeダッシュボード：** メールアドレスに関連付けられたユーザーがメールを開封またはクリックすると、そのメールアドレスを共有するすべてのユーザープロファイルが、そのメールを開封またはクリックしたとしてマークされます。詳細については、[メールが送信された際に、複数のプロファイルが同じメールアドレスを持っている場合はどうなりますか？]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address)を参照してください。
- **Currents：** 同じ開封やクリックは1つのプロファイルに保存されます。Brazeは、そのプロファイルがまだそのメールアドレスを共有している場合、送信時に元々ターゲットとなったプロファイルに帰属させます。それ以外の場合、Brazeはそのメールアドレスを共有するプロファイルの中からランダムに選択された1つのプロファイルに帰属させます。

このため、Currentsのメール開封やクリックイベントの`external_user_id`値（Brazeスキーママッピングテーブルでは`external_id`という名前）は、CurrrentsとBrazeダッシュボードを比較した際に、期待するユーザープロファイルと一致しない場合があります。

## すべての送信イベントはCurrentsに記録されますか？ {#are-all-send-events-logged-to-currents}

すべてのイベントはCurrentsに記録されます。Currentsストリームからイベントが意図的に抑制されるシナリオはありません。

## Currentsのデータが破損することはありますか？ {#can-data-be-corrupted-in-currents}

通常の状況では、Currentsのデータが破損することはありません。まれに問題が発生する可能性は常にありますが、データが体系的に破損するような既知の条件はありません。

## Currentsインテグレーションの設定前の日付のカスタムイベントデータが表示されるのはなぜですか？ {#why-do-i-see-custom-event-data-dated-before-my-currents-integration-was-set-up}

BrazeはCurrentsにイベントをバックフィルしません。ただし、カスタムイベントは過去のタイムスタンプで記録される場合があります（例えば、イベント発生時にデバイスがオフラインで、後から同期された場合など）。このような場合、イベントのタイムスタンプはイベントが実際に発生した時点を反映するため、Currentsインテグレーションが設定される前の日付になることがあります。

## Currentsイベントにはどのユーザー識別子が含まれていますか？ {#what-user-identifiers-are-included-in-currents-events}

メッセージエンゲージメントイベント（送信、開封、クリックなど）には、BrazeユーザーID（`user_id`）と、プロファイルに存在する場合は外部識別子（イベントペイロードでは`external_user_id`、Brazeスキーママッピングテーブルでは`external_id`と表記）が含まれます。一部のメールメッセージエンゲージメントイベントには`email_address`も含まれます。カスタム属性は含まれません。

Currentsデータをデータウェアハウスやカスタマーリレーションシップマネジメント CRMにルーティングし、プロファイルデータと結合する必要がある場合は、ダウンストリームシステムで`user_id`または`external_user_id`を使用してその結合を実行してください。

## Currents送信イベントにカスタム属性を含めることはできますか？ {#can-i-include-custom-attributes-in-currents-send-events}

いいえ。Currentsは送信イベントにカスタム属性を含みません。Currentsはカスタムイベントとメッセージエンゲージメントイベントを記録します。利用可能なフィールドの完全なリストについては、[イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary)を参照してください。

## Currentsにはキャンペーンやキャンバスのタグ、またはキーと値のペアが含まれますか？ {#does-currents-include-campaign-or-canvas-tags-or-key-value-pairs}

いいえ。Currentsには、キャンペーンやキャンバスのタグ、またはメッセージレベルのキーと値のペアは含まれません。タグデータを取得するには、[エクスポートREST API]({{site.baseurl}}/api/endpoints/export)を使用してください。別の回避策として、キャンペーン内のWebhookチャネルを使用し、[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)で値をテンプレート化して、タグやキーと値のペアのデータを独自のエンドポイントに送信することもできます。

## BrazeはCurrentsの変更についてどのように顧客に通知しますか？ {#how-does-braze-notify-customers-of-changes-to-currents}

まれに破壊的変更が発生した場合、Brazeはアクティブなインテグレーションの連絡先、および過去30日以内にダッシュボードを使用したアクティブなCurrentsインテグレーションを持つすべての管理者に、事前にメールを送信します。新しいイベントや既存イベントへの新しいフィールドの追加など、破壊的でない変更については、Brazeは通知を送信しません。最新の変更については、[Currents変更履歴]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)を参照してください。

## Currentsデータにはどのくらいのストレージが必要ですか？ {#how-much-storage-do-i-need-for-currents-data}

ストレージの要件は、イベントのボリュームとエクスポートするイベントの種類によって異なります。Brazeは[Avro形式のサンプルイベント](https://github.com/appboy/currents-examples/tree/master/sample-data)を提供しており、ユースケースに合わせたファイルサイズの見積もりに使用できます。

## なぜCurrentsデータでキャンペーン名やキャンバスステップ名が`NULL`になるのですか？ {#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data}

新しいキャンペーンやキャンバスを作成すると、名前がすべてのBrazeシステムに反映されるまでに時間がかかる場合があります。この間にCurrentsを通じて送信されたイベントでは、名前フィールド（`campaign_name`や`canvas_step_name`など）が`NULL`になることがあります。イベントが記録される直前に名前が変更された場合も同様です。これを避けるには、キャンペーンやキャンバスステップを作成または名前変更した後、送信を行う前にしばらく時間を置いてください。

## Currentsでセッション終了イベントが遅延または欠落するのはなぜですか？ {#why-are-session-end-events-delayed-or-missing-in-currents}

セッション終了イベントは、SDKの通常のアップロードスケジュールに従います。Braze SDKはセッションデータをローカルにキャッシュし、ネットワーク品質に基づいて定期的にフラッシュします。例えば、接続が良好な場合は約10秒ごとにフラッシュされます。SDKがイベントをアップロードするまで、Currentsには表示されません。

ユーザーが次のフラッシュの前にアプリを強制終了したりオフラインになったりした場合、セッション終了イベントの到着が遅れるか、まったく届かない可能性があります。iOSでは、SDKがバックグラウンド中にデータを送信できないため、セッション終了イベントはアプリが再度開かれるまでフラッシュされないことがよくあります。

Currentsでよりタイムリーなセッション境界が必要な場合は、アプリがバックグラウンドに移行する時やフォアグラウンドに戻る時など、ライフサイクルのポイントで`requestImmediateDataFlush()`を呼び出してください。詳細については、[データのアップロードとダウンロード]({{site.baseurl}}/developer_guide/getting_started/sdk_overview#data-upload-and-download)および[セッション終了とセッション開始のタイムスタンプが類似している（iOS）]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log#session-end-and-session-start-have-similar-timestamps-ios)を参照してください。

## Currentsがデータを書き込もうとした際にストレージバケットが利用できない場合はどうなりますか？ {#what-happens-if-my-storage-bucket-is-unavailable-when-currents-tries-to-write-data}

データ転送時にストレージバケットが利用できない場合、そのデータは失われます。Brazeは、正常に配信されなかったイベントをバックフィルすることはできません。データの損失を防ぐため、ストレージバケットが常に利用可能で、適切に設定されていることを確認してください。

## Currentsインテグレーションの作成や編集時にエンタイトルメント制限のメッセージが表示されるのはなぜですか？ {#why-do-i-see-entitlement-limit-messages-when-creating-or-editing-a-currents-integration}

Currentsでは、異なるコネクター機能に対して個別のエンタイトルメントプールが使用されます。

- **エンゲージメントイベント**：標準のCurrentsコネクターの作成またはアップグレードに必要です。
- **顧客行動イベント**：**顧客行動とユーザーイベントの追跡**を有効にするために必要です。
- **ユーザープロファイルと属性**：**ユーザープロファイルと属性の追跡**を有効にするために必要です。

いずれかのプールが使い切られると、Brazeはエンタイトルメントの警告を表示し、そのアクションをブロックします。追加のエンタイトルメントのリクエストや設定の調整については、Brazeアカウントマネージャーにお問い合わせください。

## ストレージパスのCurrentsバージョンはどのくらいの頻度で変更されますか？ {#how-often-does-the-currents-version-in-the-storage-path-change}

ストレージパスの`version=<currents_version>`セグメントは、毎月のリリースサイクルに合わせてCurrentsのリリースごとに更新されます（例：`version=6`から`version=7`）。特定のバージョンセグメントをハードコードするのではなく、ルートパスからファイルを再帰的に読み取ることをお勧めします。これにより、バージョン変更後もパイプラインが自動的にデータを取得できます。パスフォーマットの詳細については、[イベント配信セマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics)を参照してください。バージョンごとの変更履歴については、[Currents変更ログ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)を参照してください。

## メッセージエンゲージメントイベントで`campaign_id`や`canvas_id`が欠落しているのはなぜですか？ {#why-are-campaign_id-or-canvas_id-missing-from-a-message-engagement-event}

イベントの種類やコンテキストによっては、メッセージエンゲージメントイベントが特定のキャンペーンやキャンバスステップに紐づいていない場合があります。その場合、`campaign_id`、`canvas_id`、および関連する名前フィールドがイベントペイロードから省略されることがあります。特定のイベントでこれらのフィールドが見つからない場合は、そのイベントの種類やコンテキストで通常キャンペーンやキャンバスの識別子が含まれるかどうかを確認してください。

## Currentsのタイムスタンプが秒精度に制限されているのはなぜですか？ {#why-are-currents-timestamps-limited-to-second-precision}

Currentsイベントの`time`フィールドは32ビット整数として保存されるため、秒精度に制限されています。一部のイベントには、別途64ビットのミリ秒精度タイムスタンプフィールドも含まれています。各イベントタイプで利用可能なフィールドについては、[イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary)を確認してください。

## Currentsの`users.canvas.Conversion`イベントの時間がキャンバスと異なるのはなぜですか？ {#why-does-the-userscanvasconversion-event-from-currents-have-a-different-time-than-the-canvas}

Currentsの`users.canvas.Conversion`イベントの時間は、コンバージョンの合計ウィンドウ（キャンバスの期間とコンバージョン期限の合計）を反映しており、キャンバスへのエントリからの経過時間で計測されます。

## エンゲージメントレポートがS3に送信されるとどうなりますか？ {#what-happens-when-engagement-reports-are-sent-to-s3}

S3認証情報がデータエクスポート用に設定されているがCurrents用には設定されていない場合、Brazeは指定されたS3バケットにエンゲージメントレポートをアップロードします。**Send Report To**フィールドに記載されているユーザーは、S3内のレポートへのリンクが含まれたメールを受信します。

## 匿名ユーザーデータはBraze Currentsを通じてAmplitudeに送信できますか？ {#can-anonymous-user-data-be-sent-to-amplitude-through-braze-currents}

`device_id`で識別される匿名ユーザーデータは、Currentsを通じてAmplitudeに送信できます。これには、Brazeアカウントチームによる機能の有効化が必要です。

## Content Cardsおよびアプリ内メッセージのコントロールグループインプレッションは、Currentsでどのように記録されますか？ {#how-are-control-group-impressions-for-content-cards-and-in-app-messages-logged-in-currents}

ユーザーがContent Cardsまたはアプリ内メッセージキャンペーンのコントロールグループに割り当てられると、Currentsはインプレッションイベントではなく`users.campaigns.EnrollInControl`イベントを送信します。

## APIで存在しないユーザーをターゲットにした場合はどうなりますか？ {#what-happens-when-you-target-a-non-existent-user-through-the-api}

存在しないユーザーをターゲットにした場合、APIは`200`レスポンスを返しますが、送信は「Unknown external ID」という結果でキャンセルされます。その送信に対するCurrentsイベントは生成されません。`send_to_existing_only`パラメーターはデフォルトで`true`に設定されているため、明示的に`false`に設定しない限り、不明なユーザーへの送信はサイレントにスキップされます。