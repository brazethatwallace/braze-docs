---
nav_title: LiveRamp
article_title: LiveRamp
description: "LiveRampとBrazeをSnowflakeデータ共有またはBraze Currentsを通じて接続し、高度にパーソナライズされた関連性の高いマーケティングCampaignsを作成する方法について説明します。"
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp

> LiveRampとBrazeをSnowflakeデータ共有またはBraze Currentsを通じて接続し、インサイトまでの時間を短縮し、データのサイロ化を解消し、カスタマーエンゲージメントを最適化することで、高度にパーソナライズされた関連性の高いマーケティングCampaignsを作成する方法を説明します。この統合により、実用的な個人ベースのインサイトが提供され、消費者のタッチポイントが集約されることで、より適切なオーディエンスセグメンテーションとタイムリーなCampaignsが可能になり、データドリブン型のマーケティングが強化されます。

## 統合オプション {#integration-options}

LiveRampとBrazeの統合には、以下の2つの方法があります。

- **Snowflakeデータ共有:** Snowflakeのセキュアデータシェアリングを通じて、データを移動させることなくBrazeデータを直接共有します。この方法では、Snowflakeが提供するベンチマークを活用し、業界標準に照らし合わせてマーケティング戦略を洗練させることができます。
- **Braze Currents:** Brazeからリアルタイムのイベントレベルのエンゲージメントデータをクラウドストレージの送信先（Amazon S3、Google Cloud Storage、またはMicrosoft Azure Blob Storage）にストリーミングし、そのデータをデータウェアハウスに読み込んで、クラウド環境でLiveRampのID解決機能を使用します。

{% alert important %}
Snowflakeの[セキュアデータシェアリング](https://docs.snowflake.com/en/user-guide/data-sharing-intro)では、LiveRamp、Snowflake、およびBraze間でデータが転送されません。データは、Snowflakeのサービスおよびメタデータストアでのみ共有されます。つまり、データはコピーされず、追加のストレージ料金は発生しません。共有データへのアクセスは、Snowflakeアカウントのアクセスコントロールを使用して制御および管理されます。
{% endalert %}

## ユースケース {#use-cases}

この統合は、すべてのデータウェアハウス環境で以下のユースケースをサポートします。

- **データの最小化:** LiveRampのソリューションは、セキュアデータシェアリング機能またはクラウドネイティブのID解決を使用して、データウェアハウスからテーブルを直接読み取ります。ダウンストリームパートナーに配信する時点まで、データは移動されません。
- **安全なファーストパーティのアクティベーション:** LiveRampのID解決を使用することで、LiveRampのアクティベーションアプリケーションはデータウェアハウス内のRampIDベースのテーブルのみを使用するため、PIIが外部環境へ流出することがありません。
- **ライブまでの時間を短縮:** お客様の環境でデータを直接RampIDに解決することで、最終宛先への配信が数時間以内に行われます。これに対し、LiveRampの従来のファイルベースの方法では数日間かかっていました。これにより、キャンペーンのパフォーマンスをタイムリーに最適化する能力が大幅に向上します。
- **運用コストの節約:** セキュアデータシェアリングまたはクラウドネイティブのID解決を使用することで、ファイルをLiveRampやその他の最終宛先に直接出力する調整と比較して、時間と費用を節約できます。

## Snowflakeデータ共有との統合 {#integration-with-snowflake-data-sharing}

以下のステップでは、Snowflakeデータ共有を通じてLiveRampとBrazeを統合する方法を説明します。

### 前提条件 {#prerequisites}

| 要件 | 説明 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflakeアカウント | 管理者レベルの権限を持つSnowflakeアカウントが必要です。 |
| LiveRampアカウント | Snowflake内で必要なLiveRampアプリケーションについては、LiveRampアカウントチームまたは[snowflake@liveramp.com](mailto:snowflake@liveramp.com)までお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

### ステップ1: Brazeからのデータ共有を依頼する {#step-1-request-a-data-share-from-braze}

まず、Brazeアカウントマネージャーまたはカスタマーサクセスマネージャーに連絡して、Brazeアカウント用のSnowflake Data Share Connectorを購入します。データ共有を依頼すると、Brazeは共有が購入されたワークスペースから共有をプロビジョニングします。共有がプロビジョニングされると、すべてのデータはSnowflakeインスタンス内から受信データ共有の形式ですぐにアクセス可能になります。共有がインスタンスに表示されたら、共有からデータベースを作成し、テーブルを確認したりクエリしたりできるようにします。

完全なウォークスルーについては、[BrazeとSnowflakeの統合ガイド]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)を参照してください。

### ステップ2: SnowflakeでLiveRampアプリをセットアップする {#step-2-set-up-the-liveramp-app-in-snowflake}

翻訳機能とID解決機能は、Snowflake内でLiveRamp Identity Resolution and Translationネイティブアプリを通じて利用可能です。このアプリにより、アカウントに共有が作成され、ご利用のSnowflake環境から参照データセットをクエリするためのビューが開かれます。

このネイティブアプリを設定するには、LiveRampのドキュメント[SnowflakeでのLiveRampネイティブアプリの設定](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html)に記載されている手順に従います。完了したら、次のステップに進みます。

### ステップ3: データテーブルを作成する {#step-3-create-a-data-table}

{% alert warning %}
PIIベースのテーブルを準備する前に、ジョブで実行される[LiveRampのプライバシーフィルター](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)を理解し、入力テーブルの属性列（識別子以外）に非常にユニークな値が含まれていないことを確認してください。これは、消費者のプライバシーを維持し、再識別を避けるために重要です。
{% endalert %}

次に、LiveRampネイティブアプリに対して呼び出されるデータテーブルを[必要な形式](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)で作成します。以下のカテゴリーを参照し、どの識別子が解決の対象となるかを判断します。

| 識別子の種類 | 説明 |
|-----------------|--------------|
| 完全なPII | 個人を特定できる情報（PII）には、ユーザーの氏名、住所、メール、電話番号が含まれます。**注:** すべての識別子がすべてのレコードに必要なわけではありません。 |
| メールのみ | ユーザーのメールアドレス（`alex-lee@email.com` など）。 |
| デバイス | これには、サードパーティCookie、モバイル広告ID（MAID）、コネクテッドTV ID（CTV ID）、およびRampID（Household RampIDに解決される）が含まれます。 |
| CID | これらは、プラットフォームパートナーまたはLiveRampとのID同期からの識別子です（内部顧客IDなど）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ3: データテーブルを作成する" }

#### Brazeの識別子 {#braze-identifiers}

Brazeのイベントログには、LiveRampネイティブアプリ内で使用できる識別子が含まれています。各イベントタイプで使用可能な識別子の完全なリストについては、[Brazeイベントのスキーマと識別子]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt)をダウンロードしてください。

| 識別子の種類 | 説明 |
|-----------------|--------------|
| `AD_ID` | `ios_idfa`、`google_ad_id`、`roku_ad_id` などの広告IDは、特定のイベントタイプ内でキャプチャされ、LiveRampのデバイス解決サービスと組み合わせて使用できます。デフォルトでは広告IDは収集されませんが、[Brazeのドキュメント]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default)に従ってトラッキングを有効にできます。 |
| `EMAIL_ADDRESS` | LiveRampのメール専用解決サービスと併用できるメールアドレスです。 |
| `TO_PHONE_NUMBER` | LiveRampのPII解決サービスと併用できる電話番号です。 |
| `EXTERNAL_USER_ID` | ユーザーに関連付けられたexternal IDです。LiveRampのDevice Resolutionサービス（CID）と併用できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeの識別子" }

{% alert important %}
LiveRampのアプリケーション内でクライアントまたはブランド固有のカスタム識別子を使用するには、[LiveRampとのID同期](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html)が必要です。
{% endalert %}

### ステップ4: 変数を設定する {#step-4-set-your-variables}

次に、アプリに用意されているExecution Stepsワークシートでジョブの変数を設定します。これには、ターゲットデータベース、関連テーブル（入力データ、指標、ロギング）、出力テーブル名の定義などの詳細が含まれます。完全なウォークスルーについては、[LiveRamp: 変数を指定する](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727)を参照してください。

### ステップ5: PII解決のためのメタデータテーブルを作成する {#step-5-create-the-metadata-table-for-pii-resolution}

変数が設定できたので、PII解決のためのメタデータテーブルを作成します。これは、関係する識別子のカテゴリーに基づいて実行される特定のジョブタイプの詳細を示します。完全なウォークスルーについては、[LiveRamp: メタデータテーブルを作成する](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43)を参照してください。

### ステップ6: ID解決操作を実行する {#step-6-perform-the-identity-resolution-operation}

最後に、ID解決操作を実行します。完全なウォークスルーについては、[LiveRamp: ID解決操作を実行する](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation)を参照してください。

{% tabs local %}
{% tab 入力例 %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab 出力例 %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### 次のステップ {#next-steps}

データがRampIDの専用エンコードに仮名化されたので、RampIDベースのテーブルをLiveRampのManaged Activation Applicationと共有して、主要な広告プラットフォームパートナーに対して効率的なフルフィルメントを実現できます。Activation Applicationには、追加のセグメンテーションとダウンストリーム宛先パートナーの選択・設定のための、ビジネスユーザーにとって使いやすいインターフェイスが含まれています。アプリケーションの詳細については、LiveRampのアカウントチームまたは[snowflake@liveramp.com](mailto:snowflake@liveramp.com)にお問い合わせください。

## Braze Currentsとの統合 {#integration-with-braze-currents}

Braze Currentsは、クラウドストレージの送信先にエクスポートできるリアルタイムのエンゲージメントイベントストリームを提供します。CurrentsをLiveRampと組み合わせて使用することで、Brazeイベントデータをクラウドストレージにストリーミングし、データウェアハウスに読み込んだ後、クラウド環境内でLiveRampのID解決機能を適用できます。

### 仕組み {#how-it-works}

1. **Brazeがリアルタイムのイベントレベルデータを提供:** BrazeはCurrentsを通じて、生のエンゲージメントデータをデータウェアハウスまたはストレージの送信先にストリーミングします。
2. **LiveRampがデータをRampIDに接続:** LiveRampはPIIを削除し、データをブランドのユニバーサル識別子であるRampIDに接続します。
3. **アクティベーションと測定:** Brazeからのファーストパーティデータを他のサードパーティデータと組み合わせて、広告用のより精密な顧客セグメントを作成できます。仮名化されたオーディエンスはLiveRampを通じてダウンストリームのプラットフォームパートナーでアクティベーションされ、LiveRampはパートナーから広告露出データを受け取り、個人ベースのレベルで測定を行います。

### サポートされるクラウドプラットフォーム {#supported-cloud-platforms}

LiveRampのID解決機能は、以下のクラウド環境で利用可能です。

| プラットフォーム | LiveRampソリューション | 説明 |
|----------|------------------|-------------|
| Google BigQuery | [LiveRamp Embedded Identity in BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery) | BigQuery Entity Resolution Frameworkを使用して、BigQuery内でネイティブにID解決とRampID変換を実行します。ID解決を実行する前に、Google Cloud StorageからBigQueryにCurrentsデータを読み込みます。 |
| AWS | [LiveRamp Identity in AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws) | AWS Entity ResolutionまたはAmazon Data Exchange（ADX）スタンドアロンを使用して、識別子をRampIDに解決し、ID変換を実行します。ID解決を実行する前に、Amazon S3からCurrentsデータを読み込みます。 |
| Microsoft Azure | LiveRampにお問い合わせください | Azure Blob StorageはCurrentsの送信先としてサポートされています。Azure固有のID解決ソリューションについては、LiveRampの担当者にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされるクラウドプラットフォーム" }

{% alert note %}
LiveRamp Embedded Identity in BigQueryは現在ベータ版です。プログラムへの参加については、[LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com)までお問い合わせください。
{% endalert %}

### 前提条件

| 要件 | 説明 |
|-------------|-------------|
| Braze Currents | イベントデータをクラウドストレージにストリーミングするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)がセットアップされている必要があります。 |
| クラウドストレージアカウント | Currentsがデータをストリーミングするクラウドストレージアカウント（Amazon S3、Google Cloud Storage、またはMicrosoft Azure Blob Storage）が必要です。 |
| LiveRampアカウント | クラウド環境でLiveRampのID解決をセットアップするには、LiveRampアカウントチームまたは[LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com)にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

### ステップ1: Braze Currentsをセットアップする {#step-1-set-up-braze-currents}

まず、Braze Currentsをセットアップして、エンゲージメントデータをクラウドストレージの送信先にストリーミングします。選択したプラットフォームに基づいて、以下のガイドを参照してください。

- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

LiveRampのID解決に必要な識別子を含むイベントをエクスポートするようにCurrentsを設定します。各イベントタイプで使用可能な識別子の完全なリストについては、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)の用語集を参照してください。

### ステップ2: LiveRampのID解決をセットアップする {#step-2-set-up-liveramp-identity-resolution}

Currentsがクラウドストレージにデータをストリーミングし始めたら、LiveRampの担当者と協力してクラウド環境でID解決をセットアップします。

- **BigQueryの場合:** [LiveRamp Embedded Identity in BigQuery](https://docs.liveramp.com/identity/en/liveramp-embedded-identity-in-bigquery.html#liveramp-embedded-identity-in-bigquery)のセットアップガイドに従って、ID解決とRampID変換を有効にします。ベータプログラムに必要な契約とプロビジョニングのステップを完了するために、LiveRampの担当者と調整してください。
- **AWSの場合:** [LiveRamp Identity in AWS](https://docs.liveramp.com/identity/en/liveramp-identity-in-aws.html#liveramp-identity-in-aws)のセットアップガイドに従って、AWS Entity ResolutionまたはADXスタンドアロンを使用したRampID ID解決を設定します。

### ステップ3: データを読み込んで変換する {#step-3-load-and-transform-your-data}

ETL（Extract、Transform、Load）プロセスを作成して、以下を実行します。

1. クラウドストレージからデータウェアハウスのテーブルにCurrentsデータを読み込みます。
2. LiveRampのID解決サービスが必要とする形式にデータを変換します。
3. LiveRampの解決に必要な識別子（メールアドレス、デバイスID、external user IDなど）を含む入力テーブルを準備します。

### ステップ4: ID解決を実行する {#step-4-perform-identity-resolution}

LiveRampのクラウドネイティブID解決を使用して、Brazeの識別子をRampIDに解決します。このプロセスでは以下を行います。

1. 提供された識別子（PIIまたはデバイス）をLiveRampの仮名化された個人ベースの識別子であるRampIDに解決します。
2. PIIデータを削除した状態で、RampIDを含む出力テーブルをデータウェアハウスに書き戻します。

### ステップ5: オーディエンスをアクティベーションする {#step-5-activate-your-audiences}

データがRampIDに仮名化されたので、以下のことが可能になります。

- Brazeからのファーストパーティデータを他のデータソースと組み合わせて、より精密な顧客セグメントを作成します。
- LiveRampのアクティベーションプラットフォームを通じて、仮名化されたオーディエンスを広告キャンペーンでアクティベーションします。
- パートナーから広告露出データを受け取り、個人ベースのレベルで測定を行います。

アクティベーションの詳細については、LiveRampのアカウントチームまたは[LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com)にお問い合わせください。

## トラブルシューティング {#troubleshooting}

{% alert note %}
より具体的な問題や質問がある場合は、[martech@liveramp.com](mailto:martech@liveramp.com)または[LiveRampIdentitySupport@liveramp.com](mailto:LiveRampIdentitySupport@liveramp.com)までお問い合わせください。
{% endalert %}

### Snowflakeのリージョン {#snowflake-regions}

Snowflakeネイティブアプリは、現在以下の米国ベースのリージョンでのみ利用可能です。

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### プライバシーと列の値 {#privacy-column-values}

LiveRampのID解決プロセスでは、ユニークな値があるかどうか、行ごとにすべての列値の組み合わせを評価します。特定の列値の組み合わせが3回以下しか出現しない場合、それらの列値を含む行はマッチせず、出力テーブルには返されません。同様に、プライバシーを確保するために、LiveRampサービスは列値の組み合わせのユニーク性を評価します。これにより、稀な組み合わせが原因でファイルの行の5%以上が照合不可能になった場合にはジョブが失敗するようになります。

### 過去のデータ {#historical-data}

Snowflakeの過去データは2019年4月まで遡りますが、2019年8月以前のデータには製品変更により若干の差異が生じる可能性があります。

### スピード、パフォーマンス、コスト {#speed-performance-cost}

クエリの速度とコストは、使用するウェアハウスのサイズによって異なります。ウェアハウスのサイズを選択するときには、データアクセスの必要性を考慮してください。

### Brazeベンチマーク {#braze-benchmarks}

ベンチマークでは、Snowflake Data Exchangeで直接利用できる業界標準と自社の指標を比較することができます。

### 破壊的変更と非破壊的変更 {#breaking-vs-non-breaking-changes}

統合に影響を及ぼす可能性のある変更に注意してください。破壊的な変更の前には発表と移行期間が設けられます。