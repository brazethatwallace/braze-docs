---
nav_title: Amazon S3からSnowflakeにデータを転送する
article_title: Amazon S3からSnowflakeにデータを転送する
page_order: 7
page_type: tutorial
description: "このハウツー記事では、ETL（Extract, Transform, Load）プロセスを使用して、クラウドストレージ（Amazon S3など）からデータウェアハウス（Snowflakeなど）にデータを転送する手順を説明します。"
tool: Currents

---

# Amazon S3からSnowflakeにデータを転送する {#transfer-data-from-amazon-s3-to-snowflake}

> 現在データがAmazon S3にある場合は、抽出、読み込み、変換（ELT）プロセスを使用して、Snowflakeや他のリレーショナルデータウェアハウスに転送できます。このページではその方法を説明します。

{% alert note %}
より具体的なユースケースがあり、BrazeにCurrentsインスタンスのサービスを依頼したい場合は、Brazeアカウントマネージャーに連絡し、Braze Data Professional Servicesについてお問い合わせください。
{% endalert %}

## 仕組み {#how-it-works}

抽出、読み込み、変換（ELT）プロセスは、データを[Snowflake](https://www.snowflake.com/)に移動する自動プロセスです。これにより、[Braze Looker Blocks](https://marketplace.looker.com/marketplace/directory)を使用してLookerでそのデータを可視化し、キャンペーン、キャンバス、セグメントにインサイトやフィードバックを活用できます。

Currentsから S3へのエクスポートを設定し、ライブイベントデータを受信したら、次のコンポーネントを設定することによりSnowflakeでライブELTパイプラインを設定できます。

-   [AWS SQSキュー](#aws-sqs-queues)
-   [自動取り込みSnowpipe](#auto-ingest-snowpipes)

## AWS SQSキューの設定 {#aws-sqs-queues}

**自動取り込みSnowpipe**は、S3からSnowpipeへの通知の送信をSQSキューに依存します。このプロセスは、SQSの設定後にSnowflakeによって管理されます。

### ステップ1: 外部S3ステージの設定 {#step-1-configure-the-external-s3-stage}

{% alert note %}
この段階でデータベースのテーブルが作成されます。
{% endalert %}

1. BrazeでCurrentsを設定するときに、S3バケットに転送するCurrentsファイルのフォルダーパスを指定します。ここでは、デフォルトのフォルダーパスである`currents`を使用します。

2. 以下の順番で作成します：
  2.1 AWSで、目的のS3バケットの新しい**公開キーと秘密キーのペア**を作成します。このときに、組織のセキュリティ要件に応じて権限を付与します。
  2.2. Snowflakeで、任意のデータベースとスキーマ（次の例では`currents`と`public`という名前）を作成します。
  2.3. Snowflake S3ステージ（`braze_data`という名前）を作成します。

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3. ステージのAVROファイル形式を定義します。

```sql
CREATE FILE FORMAT
    currents.public.currents_avro
    type = 'avro'
    compression = 'auto';
```

```sql
ALTER STAGE
    currents.public.braze_data
SET
    file_format = currents.public.currents_avro;
```

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{: start="4"}
4. 最後に、`show pipes;`コマンドを使用してSQS情報を表示します。このパイプは自動取り込みパイプとして作成されたため、`NOTIFICATION_CHANNEL`という新しい列にSQSキューの名前が表示されます。

### ステップ2: バケットイベントの作成 {#step-2-create-bucket-events}

1. AWSで、新しいSnowflakeステージに対応するバケットに移動します。次に、**Properties**タブの**Events**に移動します。

![AWSのPropertiesタブ]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2. 必要に応じて、各Currentsデータセットの新しいイベントを作成します（[メッセージング]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、[顧客行動]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)、またはその両方）。

![AWSで新しいイベントを作成する]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3. オブジェクト作成通知の適切なチェックボックスをオンにし、フォームの下部にあるARN（Snowflakeの通知チャネル列から取得）を入力します。

## 自動取り込みSnowpipeの設定 {#auto-ingest-snowpipes}

AWS SQSの設定で正しいテーブルを生成するには、受信データの構造を適切に定義する必要があります。以下の例と、Currentsドキュメントの[メッセージエンゲージメントまたはメッセージングイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、[ユーザーまたは顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)、またはその両方で定義されたスキーマを使用してください。

Braze Currentsは特定のデータタイプの特定のフィールドを通じてデータを継続的に読み込むため、Braze Currentsのスキーマに従ってテーブルを構造化することが重要です。たとえば、`user_id`は文字列として読み込まれ、Currentsデータでは`user_id`と呼ばれます。

{% alert note %}
  Currentsの連携によっては、設定が必要なイベントが異なる場合があります（[メッセージエンゲージメントまたはメッセージングイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)や[ユーザーまたは顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)など）。このプロセスの一部またはすべてについてスクリプトを作成することもできます。
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

1. 以下のCurrentsスキーマの構造を使用して、継続的にデータを読み込むテーブルを`INTO`で作成します。

```sql
CREATE TABLE
  users_behaviors_app_firstsession (
        id               STRING,
        user_id          STRING,
        external_user_id STRING,
        app_id           STRING,
        time             INT,
        session_id       STRING,
        gender           STRING,
        country          STRING,
        timezone         STRING,
        language         STRING,
        device_id        STRING,
        sdk_version      STRING,
        platform         STRING,
        os_version       STRING,
        device_model     STRING
    );
```

{: start="2"}
2. `auto_ingest`パイプを作成し、以下を指定します。
  2.1. 読み込み先のテーブル
  2.2 テーブルの読み込み方法

```sql
CREATE OR REPLACE PIPE
  pipe_users_behaviors_app_firstsession
    auto_ingest=true AS

COPY INTO
  users_behaviors_app_firstsession
          FROM
            (SELECT
              $1:id::STRING,
              $1:user_id::STRING,
              $1:external_user_id::STRING,
              $1:app_id::STRING,
              $1:time::INT,
              $1:session_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:timezone::STRING,
              $1:language::STRING,
              $1:device_id::STRING,
              $1:sdk_version::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
```

{% alert warning %}
イベントタイプごとに`CREATE TABLE`コマンドと`CREATE PIPE`コマンドを繰り返す必要があります。
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

1. 以下のCurrentsスキーマの構造を使用して、継続的にデータを読み込むテーブルを`INTO`で作成します。

```sql
CREATE TABLE
    public_users_messages_pushnotification_open (
        id STRING,
        user_id STRING,
        external_user_id STRING,
        time INT,
        timezone STRING,
        app_id STRING,
        campaign_id STRING,
        campaign_name STRING,
        message_variation_id STRING,
        canvas_id STRING,
        canvas_name STRING,
        canvas_variation_id STRING,
        canvas_step_id STRING,
        canvas_step_message_variation_id STRING,
        platform STRING,
        os_version STRING,
        device_model STRING,
        send_id STRING,
        device_id STRING,
        button_action_type STRING,
        button_string STRING
        );
```

{: start="2"}
2. AUTO継続読み込みパイプを作成し、以下を指定します。
  2.1. 読み込み先のテーブル
  2.2 テーブルの読み込み方法

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{% alert warning %}
イベントタイプごとに`CREATE TABLE`コマンドと`CREATE PIPE`コマンドを繰り返す必要があります。
{% endalert %}

  {% endtab %}
{% endtabs %}

Braze Currentsを使用して実行できる分析の種類については、[Looker Blocks](https://github.com/llooker?q=braze)を参照してください。

{% alert note %}
ご質問がある場合や、Brazeにこのプロセスのガイドを依頼したい場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}