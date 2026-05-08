---
nav_title: Amazon S3에서 Snowflake로 데이터 전송하기
article_title: Amazon S3에서 Snowflake로 데이터 전송하기
page_order: 7
page_type: tutorial
description: "이 사용법 문서에서는 추출, 변환, 로드(ETL) 프로세스를 사용하여 클라우드 스토리지(예: Amazon S3)에서 데이터 웨어하우스(예: Snowflake)로 데이터를 전송하는 방법을 안내합니다."
tool: Currents

---

# Amazon S3에서 Snowflake로 데이터 전송하기

> 데이터가 현재 Amazon S3에 있는 경우, 추출, 로드, 변환(ELT) 프로세스를 사용하여 Snowflake 또는 다른 관계형 데이터 웨어하우스로 데이터를 전송할 수 있습니다. 이 페이지에서는 그 방법을 설명합니다.

{% alert note %}
보다 구체적인 사용 사례가 있고 Braze가 귀하의 커런츠 인스턴스를 서비스하기를 원하는 경우, Braze 계정 매니저에게 연락하여 Braze 데이터 전문가 서비스에 대해 문의하세요.
{% endalert %}

## 작동 방식

ELT(추출, 로드, 변환) 프로세스는 데이터를 [Snowflake](https://www.snowflake.com/)로 이동하는 자동화된 프로세스이며, 이를 통해 [Braze Looker 블록](https://marketplace.looker.com/marketplace/directory)을 사용하여 Looker에서 해당 데이터를 시각화하여 Campaigns, Canvases 및 Segments에 대한 인사이트와 피드백을 도출할 수 있습니다.

Currents to S3 내보내기를 설정하고 라이브 이벤트 데이터를 수신하고 나면 다음 구성요소를 구성하여 Snowflake에서 라이브 ELT 파이프라인을 구성할 수 있습니다:

-   [AWS SQS 대기줄](#aws-sqs-queues)
-   [자동 수집 Snowpipes](#auto-ingest-snowpipes)

## AWS SQS 대기줄 구성 {#aws-sqs-queues}

**자동 수집 Snowpipes**는 S3에서 Snowpipe로 알림을 전송하기 위해 SQS 대기줄을 사용합니다. 이 프로세스는 SQS를 구성한 후 Snowflake에서 관리합니다.

### 1단계: 외부 S3 스테이지 구성

{% alert note %}
데이터베이스의 테이블은 이 단계에서 생성됩니다.
{% endalert %}

1. Braze에서 Currents를 설정할 때, Currents 파일이 S3 버킷에 따라갈 폴더 경로를 지정하세요. 여기서는 기본 폴더 경로인 `currents`를 사용합니다.

2. 나열된 순서대로 다음을 생성합니다:
  2.1 AWS에서 조직의 보안 요구 사항에 따라 권한을 부여하여 원하는 S3 버킷에 대한 새 **공개-비공개 키 쌍**을 생성합니다.
  2.2. Snowflake에서 원하는 데이터베이스와 스키마를 만듭니다(다음 예제에서는 `currents` 및 `public`).
  2.3. Snowflake S3 스테이지를 생성합니다(`braze_data`):

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3. 스테이지에 대한 AVRO 파일 형식을 정의합니다.

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
4. 마지막으로 `show pipes;` 명령을 사용하여 SQS 정보를 확인합니다. 이 파이프가 자동 수집 파이프로 생성되었기 때문에 `NOTIFICATION_CHANNEL`이라는 새 열에 SQS 대기줄 이름이 표시됩니다.

### 2단계: 버킷 이벤트 생성

1. AWS에서 새 Snowflake 스테이지에 해당하는 버킷으로 이동합니다. 그런 다음 **Properties** 탭에서 **Events**로 이동합니다.

![AWS Properties 탭]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2. 필요에 따라 각 Currents 데이터 세트에 대한 새 이벤트를 생성합니다([메시징]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/), [고객 행동]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/), 또는 둘 다).

![AWS에서 새 이벤트 생성하기]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3. 오브젝트 생성 알림에 대한 적절한 체크박스를 선택하고, 양식 하단에 ARN(Snowflake의 알림 채널 열에서 확인)을 입력합니다.

## 자동 수집 Snowpipes 구성 {#auto-ingest-snowpipes}

AWS SQS 구성이 올바른 테이블을 생성하려면, Currents 설명서에서 [메시지 참여 또는 메시징 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/), [사용자 또는 고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/), 또는 둘 다에 대해 결정된 다음 예제와 스키마를 사용하여 수신 데이터의 구조를 올바르게 정의해야 합니다.

Braze Currents가 특정 데이터 유형의 특정 필드를 통해 지속적으로 데이터를 로드하므로, Braze Currents 스키마에 따라 테이블을 구성하는 것이 중요합니다. 예를 들어, `user_id`는 문자열로 로드되며 Currents 데이터에서 `user_id`로 호출됩니다.

{% alert note %}
  커런츠 통합에 따라 설정해야 하는 이벤트가 다를 수 있습니다([메시지 참여 또는 메시징 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) 및 [사용자 또는 고객 행동 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)). 이 프로세스의 일부 또는 전체에 대해 스크립트를 작성할 수도 있습니다.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

1. Currents 스키마에서 다음 구조를 사용하여 지속적으로 로드할 테이블을 `INTO`로 생성합니다:

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
2. `auto_ingest` 파이프를 생성하고 다음을 지정합니다:
  2.1. 로드할 테이블
  2.2 다음 테이블을 로드하는 방법

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
모든 이벤트 유형에 대해 `CREATE TABLE` 및 `CREATE PIPE` 명령을 반복해야 합니다.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

1. Currents 스키마에서 다음 구조를 사용하여 지속적으로 로드할 테이블을 `INTO`로 생성합니다:

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
2. AUTO 연속 로드 파이프를 생성하고 다음을 지정합니다:
  2.1. 로드할 테이블
  2.2 다음 테이블을 로드하는 방법

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
모든 이벤트 유형에 대해 `CREATE TABLE` 및 `CREATE PIPE` 명령을 반복해야 합니다.
{% endalert %}

  {% endtab %}
{% endtabs %}

Braze Currents를 사용하여 수행할 수 있는 분석 유형을 확인하려면 [Looker 블록](https://github.com/llooker?q=braze)을 참조하세요.

{% alert note %}
질문이 있거나 Braze가 이 프로세스를 안내해 주기를 원하시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}