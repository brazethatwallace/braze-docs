---
nav_title: 파일 스토리지 통합
article_title: 파일 스토리지 통합
description: "이 페이지에서는 Braze 클라우드 데이터 수집과 Amazon S3 또는 Google Cloud Storage에서 Braze로 관련 데이터를 동기화하는 방법에 대해 설명합니다."
page_order: 4
page_type: reference

---

# 파일 스토리지 통합 {#file-storage-integrations}

> 이 페이지에서는 클라우드 데이터 수집을 설정하여 Amazon S3 또는 Google Cloud Storage에서 Braze로 데이터를 동기화하는 방법에 대해 설명합니다.

## 작동 방식 {#how-it-works}

클라우드 데이터 수집(CDI)을 사용하여 클라우드 계정의 하나 이상의 스토리지 버킷을 Braze와 직접 통합할 수 있습니다. 버킷에 새 파일을 추가하면 클라우드 공급자가 알림을 게시하고, Braze 클라우드 데이터 수집이 데이터를 동기화합니다.

알림 메커니즘은 공급자에 따라 다릅니다:

- **Amazon S3:** 새 파일이 S3에 게시되면 Amazon Simple Queue Service(SQS) 대기줄에 메시지가 게시되고, Braze가 해당 메시지를 소비하여 새 파일을 수집합니다.
- **Google Cloud Storage(GCS):** 버킷에서 새 파일이 확정되면 GCS가 Pub/Sub 토픽에 `OBJECT_FINALIZE` 알림을 게시합니다. Braze는 Pub/Sub 구독에서 해당 알림을 소비하여 새 파일을 수집합니다.

클라우드 데이터 수집은 다음을 지원합니다:

- JSON 파일
- CSV 파일
- Parquet 파일
- 속성, 커스텀 이벤트, 구매 이벤트, 사용자 삭제 및 카탈로그 데이터

## 클라우드 데이터 수집 설정 {#setting-up-cloud-data-ingestion}

설정 단계는 파일 스토리지 공급자에 따라 다릅니다. 사용하는 공급자의 탭을 선택한 다음, 이어지는 섹션에서 공통 구성을 완료합니다.

{% tabs %}
{% tab Amazon S3 %}

통합에는 다음 리소스가 필요합니다:

- 데이터 저장을 위한 S3 버킷
- 새 파일 알림을 위한 SQS 대기줄
- Braze 액세스를 위한 IAM 역할

### AWS 정의 {#aws-definitions}

| 용어 | 정의 |
| --- | --- |
| Amazon Resource Name(ARN) | ARN은 AWS 리소스의 고유 식별자입니다. |
| Identity and Access Management(IAM) | IAM은 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스입니다. 이 튜토리얼에서는 IAM 정책을 생성하고 IAM 역할에 할당하여 S3 버킷을 Braze 클라우드 데이터 수집과 통합합니다. |
| Amazon Simple Queue Service(SQS) | SQS는 분산 소프트웨어 시스템 및 컴포넌트를 통합할 수 있는 호스팅된 대기줄입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWS 정의" }

## AWS에서 클라우드 데이터 수집 설정하기 {#setting-up-cloud-data-ingestion-in-aws}

### 1단계: 소스 버킷 생성 {#step-1-create-a-source-bucket}

AWS 계정에서 기본 설정으로 범용 S3 버킷을 생성합니다. S3 버킷은 폴더가 고유한 한 여러 동기화에서 재사용할 수 있습니다.

기본 설정은 다음과 같습니다:

- ACL 비활성화
- 모든 퍼블릭 액세스 차단
- 버킷 버전 관리 비활성화
- SSE-S3 암호화
  - SSE-S3는 유일하게 지원되는 서버 측 암호화 유형입니다. Amazon KMS 암호화는 지원되지 않습니다.

버킷을 생성한 리전을 기록해 두세요. 다음 단계에서 동일한 리전에 SQS 대기줄을 생성합니다.

### 2단계: SQS 대기줄 생성 {#step-2-create-sqs-queue}

생성한 버킷에 객체가 추가되는 시점을 추적하기 위해 SQS 대기줄을 생성합니다. 지금은 기본 구성 설정을 사용합니다.

SQS 대기줄은 전역적으로 고유해야 합니다(예: CDI 동기화에 하나만 사용할 수 있으며 다른 워크스페이스에서 재사용할 수 없습니다).

{% alert important %}
버킷을 생성한 리전과 동일한 리전에 이 SQS를 생성해야 합니다.
{% endalert %}

SQS 대기줄의 ARN과 URL을 기록해 두세요. 이 구성 과정에서 자주 필요합니다.

![대기줄에 액세스할 수 있는 사용자를 정의하는 예시 JSON 객체와 함께 "Advanced"를 선택하는 화면.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### 3단계: 액세스 정책 설정 {#step-3-set-up-access-policy}

액세스 정책을 설정하려면 **Advanced options**를 선택합니다.

대기줄의 액세스 정책에 다음 구문을 추가합니다. `YOUR-BUCKET-NAME-HERE`를 버킷 이름으로, `YOUR-SQS-ARN`을 SQS 대기줄 ARN으로, `YOUR-AWS-ACCOUNT-ID`를 AWS 계정 ID로 바꿔야 합니다:

``` json
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
}
```

### 4단계: S3 버킷에 이벤트 알림 추가 {#step-4-add-an-event-notification-to-the-s3-bucket}

1. 1단계에서 생성한 버킷에서 **Properties** > **Event notifications**로 이동합니다.
2. 구성에 이름을 지정합니다. 선택적으로 Braze에서 파일의 하위 집합만 수집하려면 접두사 또는 접미사를 지정할 수 있습니다.
3. **Destination**에서 **SQS queue**를 선택하고 2단계에서 생성한 SQS의 ARN을 입력합니다.

{% alert note %}
S3 버킷의 루트 폴더에 파일을 업로드한 후 일부 파일을 버킷 내 특정 폴더로 이동하면 예기치 않은 오류가 발생할 수 있습니다. 대신 접두사에 있는 파일에 대해서만 이벤트 알림을 보내도록 변경하고, 해당 접두사 외부의 S3 버킷에 파일을 배치하지 않거나, 접두사 없이 통합을 업데이트하여 모든 파일을 수집할 수 있습니다.
{% endalert %}

### 5단계: IAM 정책 생성 {#step-5-create-an-iam-policy}

Braze가 소스 버킷과 상호 작용할 수 있도록 IAM 정책을 생성합니다. 시작하려면 계정 관리자로 AWS 관리 콘솔에 로그인합니다.

1. AWS 콘솔의 IAM 섹션으로 이동하여 탐색 바에서 **Policies**를 선택한 다음 **Create Policy**를 선택합니다.<br><br>![AWS 콘솔의 "Create policy" 버튼.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. **JSON** 탭을 열고 **Policy Document** 섹션에 다음 코드 스니펫을 입력합니다. `YOUR-BUCKET-NAME-HERE`를 버킷 이름으로, `YOUR-SQS-ARN-HERE`를 SQS 대기줄 이름으로 바꿔야 합니다:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```

{: start="3"}
3. 완료되면 **Review Policy**를 선택합니다.

4. 정책에 이름과 설명을 입력한 다음 **Create Policy**를 선택합니다.

![예시 정책 이름 "new-policy-name".]({% image_buster /assets/img/create_policy_3_name.png %})

![정책의 설명 필드.]({% image_buster /assets/img/create_policy_4_created.png %})

### 6단계: IAM 역할 생성 {#step-6-create-an-iam-role}

AWS에서 설정을 완료하려면 IAM 역할을 생성하고 5단계에서 만든 IAM 정책을 연결합니다.

1. IAM 정책을 생성한 콘솔의 동일한 IAM 섹션에서 **Roles** > **Create Role**로 이동합니다.

![역할 생성 버튼.]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. AWS에서 신뢰할 수 있는 엔터티 선택기 유형으로 **Another AWS Account**를 선택합니다. Braze 계정 ID를 입력합니다. **Require external ID** 체크박스를 선택합니다.
3. Braze에서 **데이터 설정** > **클라우드 데이터 수집** > **소스**로 이동하여 **데이터 소스 추가**를 선택한 다음 파일 소스 섹션에서 **Amazon S3**를 선택합니다.
4. 자동으로 생성된 **Braze 계정 ID**를 복사합니다.

![소스 이름과 S3 연결 세부 정보 섹션이 표시된 "새 소스 추가" 페이지.]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. AWS에서 계정 ID를 붙여넣고 **Next**를 선택합니다.

![S3 "Create Role" 페이지. 이 페이지에는 역할 이름, 역할 설명, 신뢰할 수 있는 엔터티, 정책 및 권한 경계에 대한 필드가 있습니다.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. 4단계에서 생성한 정책을 역할에 연결합니다. 검색 바에서 정책을 검색하고 정책 옆의 체크 표시를 선택하여 연결합니다. 완료되면 **Next**를 선택합니다.

![new-policy-name이 선택된 역할 ARN.]({% image_buster /assets/img/create_role_3_attach.png %})

역할에 이름과 설명을 입력하고 **Create Role**을 선택합니다.

![예시 역할 이름 "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. 생성한 역할의 ARN과 생성된 외부 ID를 기록해 두세요. 클라우드 데이터 수집 통합을 생성할 때 필요합니다.

## Braze에서 클라우드 데이터 수집 설정하기 {#setting-up-cloud-data-ingestion-in-braze}

1. 먼저 Braze 대시보드에서 새 소스를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **소스**로 이동하여 **데이터 소스 추가**를 선택한 다음 **Amazon S3**를 선택합니다.
2. 소스 이름을 선택하고 AWS 설정 과정에서 얻은 정보를 입력하여 새 소스를 생성합니다. 다음을 지정합니다:

  - Role ARN
  - External ID
  - 버킷 이름
  - 리전

![자격 증명(AWS 설정 및 Braze 설정)과 구성 필드가 표시된 S3 연결 세부 정보 섹션.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. **연결 테스트**를 선택하여 Braze가 버킷에 액세스할 수 있는지 확인합니다. 테스트가 성공하면 **소스에 연결**을 선택합니다. 연결에 실패하면 문제를 해결하는 데 도움이 되는 오류 메시지가 표시됩니다.

{: start="4"}
4. 다음으로 새 동기화를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **동기화**로 이동하여 **데이터 동기화 생성**을 선택합니다.

{: start="5"}
5. 동기화 이름을 선택합니다. 그런 다음 활성 상태인 S3 소스를 선택하고 동기화를 위한 소스 테이블을 입력합니다. 데이터 유형을 선택하고 **연결 테스트**를 선택합니다.

![데이터 미리보기와 함께 연결을 테스트하는 옵션.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. AWS 설정 과정에서 얻은 나머지 정보를 입력합니다. 다음을 지정합니다:
- SQS URL(새 통합마다 고유해야 합니다)
- 폴더 경로(선택 사항, 워크스페이스 내 동기화 간에 고유해야 합니다)

7. 데이터 유형을 선택하고 **연결 테스트**를 선택하여 Braze가 수집 가능한 파일 목록을 확인할 수 있는지 확인합니다(파일 내 데이터가 아닌 파일 목록). 성공하면 **다음: 알림**을 선택합니다.
8. 액세스 또는 권한 문제로 동기화가 중단되는 경우 알림을 받을 연락처 이메일을 추가합니다. 선택적으로 사용자 수준 오류 및 동기화 성공에 대한 알림을 활성화합니다.
9. 동기화를 생성합니다.

{% endtab %}
{% tab Google Cloud Storage %}

통합에는 다음 리소스가 필요합니다:

- 데이터 저장을 위한 Cloud Storage 버킷
- 새 파일 알림을 위한 Pub/Sub 토픽 및 구독
- JSON 키를 Braze에 업로드할 서비스 계정

### GCP 정의 {#gcp-definitions}

| 용어 | 정의 |
| --- | --- |
| Google Cloud 프로젝트 | 프로젝트는 모든 Google Cloud 리소스를 구성하며 고유한 프로젝트 ID와 프로젝트 번호로 식별됩니다. |
| Cloud Storage 버킷 | 버킷은 Braze에서 수집할 데이터 파일을 보관하는 컨테이너입니다. |
| Pub/Sub 토픽 | 토픽은 Cloud Storage 버킷에서 새 파일 알림을 수신하는 명명된 리소스입니다. |
| Pub/Sub 구독 | 구독은 토픽에 연결되어 메시지를 전달합니다. Braze는 풀 구독에서 새 파일 알림을 소비합니다. |
| 서비스 계정 | 서비스 계정은 Braze가 버킷과 구독에 액세스하는 데 사용하는 비인간 ID입니다. JSON 키를 Braze에 업로드합니다. |
| IAM 역할 | Identity and Access Management(IAM) 역할은 버킷과 구독에서 서비스 계정에 할당하는 권한 모음입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="GCP 정의" }

## Google Cloud에서 클라우드 데이터 수집 설정하기 {#setting-up-cloud-data-ingestion-in-google-cloud}

### 1단계: Cloud Storage 버킷 생성 {#step-1-create-a-cloud-storage-bucket}

Google Cloud 콘솔에서 **Cloud Storage** > **Buckets** > **Create**로 이동합니다. 프로젝트 ID와 버킷 이름을 기록해 두세요. Braze에서 소스를 구성할 때 필요합니다. IAM으로 권한을 관리할 수 있도록 균일 버킷 수준 액세스를 활성화하는 것을 권장합니다.

또는 gcloud로 버킷을 생성할 수 있습니다:

```shell
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=YOUR-REGION \
  --uniform-bucket-level-access
```

### 2단계: Pub/Sub 토픽 및 구독 생성 {#step-2-create-a-pubsub-topic-and-subscription}

Google Cloud 콘솔에서 **Pub/Sub** > **Topics** > **Create topic**으로 이동합니다. Google이 기본 구독을 생성하도록 하거나 별도로 구독을 생성할 수 있습니다. 그런 다음 해당 토픽에 **풀** 구독을 생성합니다.

또는 gcloud를 사용할 수 있습니다:

```shell
gcloud pubsub topics create YOUR-TOPIC --project=YOUR-PROJECT-ID
gcloud pubsub subscriptions create YOUR-SUBSCRIPTION \
  --topic=YOUR-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
```

**구독 ID**를 기록해 두세요. Braze에서 동기화를 생성할 때 토픽이 아닌 구독이 필요합니다. 구독은 반드시 풀 구독이어야 합니다.

{% alert warning %}
이 구독에 데드 레터 대기줄을 구성하지 마세요. Braze는 클라우드 데이터 수집 구독에 대한 데드 레터 대기줄을 지원하지 않습니다. 자세한 내용은 Google Cloud 설명서의 [데드 레터 토픽](https://cloud.google.com/pubsub/docs/dead-letter-topics)을 참조하세요.
{% endalert %}

### 3단계: 버킷 알림을 토픽으로 전송 {#step-3-send-bucket-notifications-to-the-topic}

{% alert important %}
Cloud Storage에서 Pub/Sub 알림을 생성하는 기능은 Google Cloud 콘솔에서 사용할 수 없습니다. gcloud(여기에 표시), Terraform 또는 JSON API를 사용해야 합니다. 자세한 내용은 Google Cloud 설명서의 [Cloud Storage에 대한 Pub/Sub 알림 구성](https://cloud.google.com/storage/docs/reporting-changes#enabling)을 참조하세요.
{% endalert %}

먼저 Cloud Storage 서비스 에이전트에 토픽 게시 권한을 할당한 다음 `OBJECT_FINALIZE`에 대한 알림을 생성합니다. `OBJECT_FINALIZE` 이벤트는 버킷에 새 객체가 생성되거나 완료될 때마다 트리거됩니다.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Assign it Pub/Sub Publisher on the topic
gcloud pubsub topics add-iam-policy-binding YOUR-TOPIC \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Create the OBJECT_FINALIZE notification (optionally scope to a folder with --object-prefix)
gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
  --topic=YOUR-TOPIC \
  --event-types=OBJECT_FINALIZE \
  --payload-format=json
```

이 명령에서 다음 자리 표시자를 바꿉니다:

- `YOUR-PROJECT-ID`: Google Cloud 프로젝트 ID, 사람이 읽을 수 있는 식별자입니다(예: `my-gcp-project`).
- `YOUR-TOPIC`: [2단계](#step-2-create-a-pubsub-topic-and-subscription)에서 생성한 Pub/Sub 토픽입니다.
- `YOUR-BUCKET-NAME`: Cloud Storage 버킷 이름입니다.
- `YOUR-PROJECT-NUMBER`: 프로젝트 번호, Cloud Storage 서비스 에이전트의 이메일 주소에 사용되는 숫자 식별자입니다. 프로젝트 ID와는 다릅니다. Google Cloud 콘솔의 **Dashboard**에서 확인하거나 다음 명령을 실행합니다:

```shell
gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"
```

### 4단계: 서비스 계정 생성 {#step-4-create-a-service-account}

Google Cloud 콘솔에서 **IAM & Admin** > **Service Accounts** > **Create service account**로 이동합니다.

또는 gcloud를 사용할 수 있습니다:

```shell
gcloud iam service-accounts create braze-cdi-gcs \
  --project=YOUR-PROJECT-ID \
  --display-name="Braze CDI GCS"
```

### 5단계: 권한 할당 {#step-5-assign-permissions}

커넥터는 정확히 다음 권한이 필요합니다: 버킷에 대한 `storage.buckets.get`, `storage.objects.get`, `storage.objects.list`, 구독에 대한 `pubsub.subscriptions.consume`. 커스텀 역할 또는 미리 정의된 역할로 할당할 수 있습니다.

**커스텀 역할:** 해당 권한만으로 커스텀 역할을 생성하고 버킷과 구독에 바인딩합니다:

```shell
gcloud iam roles create brazeCdiGcs --project=YOUR-PROJECT-ID \
  --title="Braze CDI GCS" \
  --permissions=storage.buckets.get,storage.objects.get,storage.objects.list,pubsub.subscriptions.consume \
  --stage=GA

gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"

gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"
```

**미리 정의된 역할:** 버킷에 `roles/storage.objectViewer` 및 `roles/storage.legacyBucketReader`를, 구독에 `roles/pubsub.subscriber`를 할당합니다. `objectViewer` 역할은 `storage.objects.get` 및 `storage.objects.list`를 제공하고, `legacyBucketReader`는 `storage.buckets.get`을 제공합니다:

```shell
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/storage.legacyBucketReader"
gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="roles/pubsub.subscriber"
```

### 6단계: JSON 키 생성 {#step-6-create-a-json-key}

Google Cloud 콘솔에서 서비스 계정을 열고 **Keys** > **Add key** > **Create new key**로 이동한 다음 **JSON**을 선택합니다.

또는 gcloud를 사용할 수 있습니다:

```shell
gcloud iam service-accounts keys create braze-cdi-gcs-key.json \
  --iam-account=braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com
```

## Braze에서 클라우드 데이터 수집 설정하기

1. Braze에서 **데이터 설정** > **클라우드 데이터 수집** > **소스**로 이동하여 **데이터 소스 추가**를 선택한 다음 **Google Cloud Storage**를 선택합니다.

![데이터 소스 목록에서 Google Cloud Storage가 선택된 "새 소스 추가" 화면.]({% image_buster /assets/img/cloud_ingestion/gcs_source_picker.png %})

{: start="2"}
2. 소스 필드를 작성합니다:
    - **Bucket** — 버킷 이름
    - **Project ID** — GCP 프로젝트 ID
    - **Service account JSON key** — 6단계에서 생성한 키 파일을 업로드하고 자격 증명에 이름을 지정합니다

![Bucket, Project ID 및 자격 증명 업로드 필드가 표시된 Google Cloud Storage 소스 양식.]({% image_buster /assets/img/cloud_ingestion/gcs_source_form.png %})

{: start="3"}
3. **연결 테스트**를 선택한 다음 **소스에 연결**을 선택합니다.
4. 동기화를 생성합니다. **데이터 설정** > **클라우드 데이터 수집** > **동기화**로 이동하여 **데이터 동기화 생성**을 선택합니다. 동기화 이름과 **데이터 유형**(**사용자 속성**, **커스텀 이벤트**, **구매 이벤트**, **카탈로그** 또는 **사용자 삭제** 등)을 선택한 다음 **다음**을 선택합니다.
5. **데이터 정의** 단계에서 GCS 소스를 선택한 다음 다음을 지정합니다:
    - **Pub/Sub subscription ID** — 2단계에서 생성한 구독 ID(토픽이 아님)
    - **Folder path**(선택 사항) — 버킷 내 경로 접두사([공유 버킷에서 폴더 동기화](#syncing-a-folder-in-a-shared-bucket) 참조)

![Pub/Sub subscription ID 및 폴더 경로 필드가 표시된 Google Cloud Storage 동기화 양식.]({% image_buster /assets/img/cloud_ingestion/gcs_sync_form.png %})

{: start="6"}
6. **미리보기 및 검증**을 선택하여 Braze가 구독에 도달하고 수집 가능한 파일 목록을 확인할 수 있는지 확인합니다. 테스트가 성공하면 버킷에 있는 기존 파일이 나열되지만, 해당 파일은 자동으로 동기화되지 않습니다.
7. 오류 알림을 받을 연락처 이메일을 추가합니다. Google Cloud Storage 동기화는 이벤트 기반이므로 스케줄이 필요하지 않습니다. Braze는 새 파일이 업로드되면 자동으로 수집합니다. 요약을 검토한 다음 **동기화 생성**을 선택합니다.

### 공유 버킷에서 폴더 동기화 {#syncing-a-folder-in-a-shared-bucket}

하나의 버킷을 여러 동기화에서 재사용할 수 있지만, 각 동기화는 고유한 폴더를 대상으로 해야 **하며** 자체 전용 Pub/Sub 구독을 보유해야 합니다.


{% alert important %}
동일한 소스 버킷을 공유하는 여러 동기화의 경우 폴더 경로와 구독 모두 워크스페이스 내 동기화 간에 고유해야 합니다. [2단계](#step-2-create-a-pubsub-topic-and-subscription)에서와 마찬가지로, 이러한 구독에 데드 레터 대기줄을 구성하지 마세요.
{% endalert %}

공유 버킷에서 동기화할 각 폴더에 대해:

1. 동기화의 **Folder** 필드를 경로 접두사(예: `attributes/`)로 설정합니다. Braze는 해당 접두사로 시작하는 경로의 객체만 나열하고 수집합니다.
2. 해당 폴더에 대해 전용 토픽과 접두사 범위 알림을 생성한 다음 해당 토픽에 구독을 생성합니다:

    ```shell
    # 폴더당 하나의 토픽
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Cloud Storage 서비스 에이전트에 토픽 게시자 역할 할당
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # --object-prefix로 폴더 범위를 제한한 알림
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # 동기화당 하나의 구독
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. [5단계](#step-5-assign-permissions)에서와 같이 Braze 서비스 계정에 해당 구독의 소비 권한을 할당합니다:

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    [5단계](#step-5-assign-permissions)에서 커스텀 역할을 생성한 경우 `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"`를 대신 사용합니다.
4. Braze에서 동기화를 생성할 때 이 폴더의 새 **Pub/Sub subscription ID**와 **Folder path**를 입력하여 해당 폴더의 파일만 수집하도록 합니다.


{% endtab %}
{% endtabs %}

## 필수 파일 형식 {#required-file-formats}

필수 파일 형식은 Amazon S3와 Google Cloud Storage에서 동일합니다. Cloud Data Ingestion은 JSON, CSV, Parquet 파일을 지원합니다. 필수 열은 데이터 유형에 따라 다릅니다.

- 사용자 데이터(속성, 커스텀 이벤트, 구매 이벤트)는 사용자 식별자와 페이로드를 사용합니다.
- 카탈로그 데이터는 카탈로그 식별자를 사용합니다.

카탈로그 데이터에 파일 스토리지를 사용하는 경우, 카탈로그 관련 요구 사항과 동작은 이 페이지와 [카탈로그 데이터 동기화 및 삭제]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)를 함께 참조하세요.

Braze는 파일 스토리지 공급자가 적용하는 것 외에 추가 파일 이름 요구 사항을 적용하지 않습니다. 파일 이름은 고유해야 합니다. 타임스탬프를 추가하면 고유성을 보장하는 데 도움이 됩니다.

지원되는 모든 파일 유형(속성, 커스텀 이벤트, 구매, 카탈로그, 사용자 삭제)의 예시는 [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage)의 샘플 파일을 참조하세요.

### 사용자 식별자 {#user-identifiers}

사용자 데이터 동기화(속성, 커스텀 이벤트, 구매 이벤트)의 경우, 소스 파일의 각 행에는 정확히 하나의 사용자 식별자와 `PAYLOAD` 열이 필요합니다. 소스 파일에는 서로 다른 식별자 유형의 행이 포함될 수 있지만, 각 개별 행에는 하나의 식별자만 사용해야 합니다.

| 식별자 | 설명 |
| --- | --- |
| `EXTERNAL_ID` | 업데이트할 사용자를 식별합니다. Braze에서 사용하는 `external_id` 값과 일치해야 합니다. |
| `ALIAS_NAME` 및 `ALIAS_LABEL` | 이 두 열은 사용자 별칭 객체를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다. |
| `BRAZE_ID` | Braze 사용자 식별자입니다. Braze SDK에 의해 생성되며, Cloud Data Ingestion을 통해 Braze ID로 새 사용자를 생성할 수 없습니다. 새 사용자를 생성하려면 외부 사용자 ID 또는 사용자 별칭을 지정하세요. |
| `EMAIL` | 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 존재하는 경우, 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. 이메일과 전화번호를 모두 포함하면 Braze는 이메일을 기본 식별자로 사용합니다. |
| `PHONE` | 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 존재하는 경우, 가장 최근에 업데이트된 프로필이 우선적으로 업데이트됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 식별자" }

식별자 외에도 각 행에는 Braze의 사용자에게 동기화하려는 필드의 JSON 문자열을 포함하는 `PAYLOAD` 열이 필요합니다.

{% alert note %}
데이터 웨어하우스 소스와 달리, `UPDATED_AT` 열은 파일 스토리지 동기화에 필요하지 않으며 지원되지도 않습니다.
{% endalert %}

### 카탈로그 식별자 {#catalog-identifiers}

카탈로그 동기화의 경우, 소스 파일에 다음 열이 포함되어야 합니다. 카탈로그 파일은 사용자 데이터 파일과 다른 식별자를 사용합니다.

| 열 | 필수 | 설명 |
| --- | --- | --- |
| `ID` | 예 | 카탈로그 항목의 고유 식별자입니다. Braze에서 항목을 생성, 업데이트 또는 삭제하는 데 사용됩니다. |
| `PAYLOAD` | 예 | 동기화할 카탈로그 필드와 값의 JSON 문자열입니다. Braze에서 카탈로그의 스키마와 일치해야 합니다. |
| `DELETED` | 아니오 | `true`인 경우, 일치하는 `ID`를 가진 카탈로그 항목이 Braze의 카탈로그에서 제거됩니다. 생성 또는 업데이트 작업에는 이 열을 생략하거나 `false`로 설정하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="카탈로그 식별자" }

### 예시 {#examples}

{% tabs %}
{% tab JSON 속성 %}
``` json
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```
{% alert important %}
소스 파일의 모든 행에는 유효한 JSON이 포함되어야 하며, 그렇지 않으면 해당 파일이 건너뛰어집니다.
{% endalert %}
{% endtab %}
{% tab JSON 커스텀 이벤트 %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```
{% alert important %}
소스 파일의 모든 행에는 유효한 JSON이 포함되어야 하며, 그렇지 않으면 해당 파일이 건너뛰어집니다.
{% endalert %}
{% endtab %}
{% tab JSON 구매 이벤트 %}
``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```
{% alert important %}
소스 파일의 모든 행에는 유효한 JSON이 포함되어야 하며, 그렇지 않으면 해당 파일이 건너뛰어집니다.
{% endalert %}

{% endtab %}
{% tab CSV 속성 %}
```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV 카탈로그 %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
선택적 `DELETED` 열을 포함할 수 있습니다. `DELETED`가 `true`이면 해당 카탈로그 항목이 Braze의 카탈로그에서 제거됩니다. 필수 열의 전체 목록은 [카탈로그 식별자](#catalog-identifiers)를 참조하세요. 삭제 동작에 대한 자세한 내용은 [카탈로그 항목 삭제](#deleting-catalog-items)를 참조하세요. 대상 카탈로그 생성 및 동기화 동작을 포함한 포괄적인 카탈로그 설정 흐름은 [카탈로그 데이터 동기화 및 삭제]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)를 참조하세요.
{% endtab %}

{% endtabs %}

## 데이터 삭제 {#deleting-data}

파일 스토리지용 클라우드 데이터 수집은 파일 업로드를 통해 사용자 및 카탈로그 항목 삭제를 지원합니다. 각 작업에 대해 별도의 동기화 및 파일 형식을 사용하세요.

- **[사용자 삭제](#deleting-users)** – 데이터 유형을 **Delete Users**로 설정한 동기화를 생성하고, 사용자 식별자만 포함된 파일(페이로드 없음)을 업로드합니다.
- **[카탈로그 항목 삭제](#deleting-catalog-items)** – 기존 카탈로그 동기화를 사용하고, `deleted`(또는 `DELETED`) 열을 추가하여 삭제할 항목을 표시합니다.

### 사용자 삭제 {#deleting-users}

소스 버킷의 파일을 사용하여 Braze에서 고객 프로필을 삭제하려면 다음을 수행하세요.

1. 새 클라우드 데이터 수집 동기화를 생성합니다(다른 동기화와 동일한 설정).
2. Braze에서 동기화를 구성할 때 **Data Type**을 **Delete Users**로 설정합니다.
3. 사용자 식별자 열만 포함된 파일을 소스 버킷에 업로드합니다. `PAYLOAD` 열은 포함하지 마세요. 실수로 인한 삭제를 방지하기 위해 페이로드가 있으면 동기화가 실패합니다.

파일의 각 행은 다음 중 하나를 사용하여 정확히 한 명의 사용자를 식별해야 합니다.

| 식별자 | 설명 |
| --- | --- |
| `EXTERNAL_ID` | Braze에서 사용하는 `external_id`와 일치합니다. |
| `ALIAS_NAME` 및 `ALIAS_LABEL` | 두 열을 함께 사용하여 사용자 별칭으로 사용자를 식별합니다. |
| `BRAZE_ID` | Braze에서 생성한 사용자 ID입니다(기존 사용자만 해당). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 삭제" }

{% alert important %}
사용자 삭제는 영구적이며 되돌릴 수 없습니다. 삭제할 사용자만 포함하세요. 자세한 내용은 [클라우드 데이터 수집으로 사용자 삭제]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users)를 참조하세요.
{% endalert %}

**예시 – JSON(사용자 삭제):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**예시 – CSV(사용자 삭제):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

동기화가 실행되면 Braze는 버킷에서 새 파일을 처리하고 해당하는 고객 프로필을 삭제합니다.

### 카탈로그 항목 삭제 {#deleting-catalog-items}

파일 스토리지를 사용하여 카탈로그에서 항목을 삭제하려면 다음을 수행하세요.

1. [카탈로그 데이터 동기화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)에 사용하는 동일한 동기화(데이터 유형 **Catalogs**)를 사용합니다.
2. CSV 또는 JSON 파일에 선택적 **`deleted`**(또는 **`DELETED`**) 열을 추가합니다.
3. Braze에서 카탈로그에서 삭제할 카탈로그 항목의 `deleted`를 `true`로 설정합니다.

각 행에는 여전히 `ID`와 `PAYLOAD`가 필요합니다. 삭제로 표시된 행의 경우 페이로드는 최소한이어도 됩니다. Braze는 `ID`로 항목을 삭제합니다.

**예시 – JSON(카탈로그 항목 삭제):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**예시 – CSV(카탈로그 항목 삭제):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

동기화가 실행되면 `deleted: true`인 행에 해당하는 카탈로그 항목이 Braze에서 삭제됩니다. 전체 카탈로그 동기화 및 삭제 동작에 대해서는 [카탈로그 데이터 동기화 및 삭제]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)를 참조하세요.

## 알아두어야 할 사항 {#things-to-know}

- 소스 버킷에 추가되는 파일은 512&nbsp;MB를 초과할 수 없습니다. 이 제한은 Amazon S3와 Google Cloud Storage 모두에 적용됩니다. 512&nbsp;MB보다 큰 파일은 오류가 발생하며 Braze에 동기화되지 않습니다.
- 파일당 행 수에 대한 추가 제한은 없지만, 동기화 실행 속도를 개선하려면 더 작은 파일을 사용하는 것이 좋습니다. 예를 들어, 500&nbsp;MB 파일 하나를 수집하는 것보다 100&nbsp;MB 파일 다섯 개를 별도로 수집하는 것이 훨씬 빠릅니다.
- 주어진 시간 내에 업로드할 수 있는 파일 수에 대한 추가 제한은 없습니다.
- 파일 내부 또는 파일 간의 정렬은 지원되지 않습니다. 예상되는 경합 조건을 모니터링하는 경우 업데이트를 주기적으로 일괄 처리하는 것이 좋습니다.

## 문제 해결 {#troubleshooting}

### 파일 업로드 및 처리 {#uploading-files-and-processing}

CDI는 동기화가 생성된 후에 추가된 파일만 처리합니다. 이 과정에서 Braze는 새 파일이 추가되는지 확인하고, 새 파일이 감지되면 새 알림이 트리거됩니다. 이 알림이 새 동기화를 시작하여 새 파일을 처리합니다. Amazon S3의 경우 이 알림은 SQS로 전송되는 메시지이고, Google Cloud Storage의 경우 Pub/Sub으로 전송되는 `OBJECT_FINALIZE` 메시지입니다.

기존 파일을 사용하여 Braze가 버킷에 접근하고 수집할 파일을 감지할 수 있는지 확인할 수 있지만, 이러한 파일은 Braze에 동기화되지 않습니다. CDI가 이를 처리하려면 동기화하려는 기존 파일을 소스 버킷에 다시 업로드해야 합니다.

### 예기치 않은 파일 오류 처리 (Amazon S3) {#handling-unexpected-file-errors-amazon-s3}

오류 또는 실패한 파일이 많이 발생하는 경우, CDI 대상 폴더가 아닌 S3 버킷 내 다른 폴더에 파일을 추가하는 프로세스가 있을 수 있습니다.

소스 버킷에 파일이 업로드되었지만 소스 폴더에 없는 경우, CDI는 SQS 알림을 처리하지만 해당 파일에 대해 아무 작업도 수행하지 않으므로 오류로 나타날 수 있습니다.

문제가 S3 알림 또는 SQS 대상 권한과 관련된 경우(예: 대상 유효성 검증 오류), AWS 설명서를 참조하세요:

- [Amazon S3 콘솔을 사용하여 이벤트 알림 활성화 및 구성](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [대상에 이벤트 알림 메시지를 게시할 수 있는 권한 부여](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Amazon SQS 문제 해결](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### 예기치 않은 파일 오류 처리 (Google Cloud Storage) {#handling-unexpected-file-errors-google-cloud-storage}

Amazon S3와 마찬가지로 CDI는 동기화가 생성된 후에 업로드된 파일만 처리합니다. 새 객체가 추가될 때마다 Pub/Sub 토픽으로 `OBJECT_FINALIZE` 메시지가 트리거됩니다. 버킷에 이미 존재하는 파일을 수집하려면 해당 파일을 다시 업로드하세요.

파일이 수집되지 않는 경우, 다음 사항을 확인하세요:

- 버킷 알림이 존재하는지 확인합니다. `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`으로 버킷의 알림을 조회하세요.
- Cloud Storage 서비스 에이전트가 토픽에 대해 `roles/pubsub.publisher` 역할을 가지고 있는지 확인합니다.
- Braze 서비스 계정이 구독에 대한 소비 권한(`pubsub.subscriptions.consume`, 커스텀 역할 또는 `roles/pubsub.subscriber`를 통해 할당)을 가지고 있는지 확인합니다.
- 구독에 데드레터 대기줄이 구성되어 있지 않은지 확인합니다. Braze는 Cloud Data Ingestion 구독에 대한 데드레터 대기줄을 지원하지 않습니다.

자세한 내용은 Google Cloud 설명서의 [Cloud Storage용 Pub/Sub 알림](https://cloud.google.com/storage/docs/pubsub-notifications)을 참조하세요.