---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "이 참조 문서에서는 Amazon Web Services에서 제공하는 확장성이 뛰어난 스토리지 시스템인 Amazon S3와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/)는 Amazon Web Services에서 제공하는 확장성이 뛰어난 스토리지 시스템입니다.

{% alert important %}
클라우드 스토리지 제공업체 간에 전환하는 경우, 새로운 통합을 설정하고 검증하는 데 대한 추가 지원을 받으려면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

Braze와 Amazon S3 통합에는 두 가지 통합 전략이 있습니다:

- [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)를 활용하여 다른 플랫폼, 도구 및 위치에 연결할 때까지 데이터를 저장할 수 있습니다.
- 대시보드 데이터 내보내기(CSV 내보내기 및 참여 보고서 등)를 사용합니다.

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Amazon S3 계정 | 이 파트너십을 활용하려면 Amazon S3 계정이 필요합니다. |
| 전용 S3 버킷 | Amazon S3와 통합하기 전에 앱을 위한 S3 버킷을 생성해야 합니다.<br><br>이미 S3 버킷이 있는 경우에도 권한을 제한할 수 있도록 Braze 전용으로 새 버킷을 생성하는 것을 권장합니다. 새 버킷을 생성하는 방법은 아래 지침을 참조하세요. |
| Currents | 데이터를 Amazon S3로 다시 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)가 설정되어 있어야 합니다. 메시지 아카이빙만 설정하는 경우에는 Currents가 필요하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 새 S3 버킷 생성하기 {#creating-a-new-s3-bucket}

앱을 위한 버킷을 생성하려면 다음을 수행합니다:

1. [Amazon S3 콘솔](https://console.aws.amazon.com/s3/)을 열고 지침에 따라 **로그인** 또는 **AWS 계정 생성**을 진행합니다.
2. 로그인 후 **Storage & Content Delivery** 카테고리에서 **S3**를 선택합니다.
3. 다음 화면에서 **Create Bucket**을 선택합니다.
4. 메시지가 표시되면 버킷을 생성하고 AWS 리전을 선택합니다.

Braze에서는 대시보드에서 리전을 선택하거나 구성할 수 없습니다. AWS 리전은 AWS 콘솔에서 버킷을 생성하는 위치에 따라 고정됩니다. 통합 시 사용자가 제공하는 버킷 이름으로 데이터를 전송하며, AWS가 자동으로 해당 버킷의 리전으로 요청을 라우팅합니다. 커넥터가 원하는 리전과 다른 리전에 연결하려고 하는 경우(예: `eu-central-1` 대신 `eu-west-1`), AWS에서 원하는 리전에 S3 버킷을 생성하거나 사용하세요. Braze 쪽에서 변경할 사항은 없습니다.

{% alert note %}
Currents는 [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)이 구성된 버킷을 지원하지 않습니다.
{% endalert %}

## 통합 {#integration}

Braze는 Amazon S3와 두 가지 통합 전략을 제공합니다. 하나는 [Braze 커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents)용이고, 다른 하나는 모든 대시보드 데이터 내보내기(CSV 내보내기 또는 참여 보고서 등)용입니다. 두 통합 모두 두 가지 인증 또는 권한 부여 방법을 지원합니다.

- [AWS 비밀 액세스 키 방법](#aws-secret-key-auth-method)
- [AWS 역할 ARN 방법](#aws-role-arn-auth-method)

## AWS 비밀 키 인증 방법 {#aws-secret-key-auth-method}

이 인증 방법은 비밀 키와 액세스 키 ID를 생성하여 Braze가 AWS 계정의 사용자로 인증하고 버킷에 데이터를 쓸 수 있도록 합니다.

### 1단계: 사용자 생성 {#secret-key-1}

{% alert note %}
메시지 아카이빙만 설정하는 경우 **Dashboard Data Export** 탭의 단계를 따르세요.
{% endalert %}

액세스 키 ID와 비밀 액세스 키를 가져오려면 [AWS에서 IAM 사용자 및 관리자 그룹을 생성](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)하세요.

### 2단계: 자격 증명 가져오기 {#secret-key-2}

새 사용자를 생성한 후 **Show User Security Credentials**를 선택하여 액세스 키 ID와 비밀 액세스 키를 확인합니다. 다음으로 이 자격 증명을 어딘가에 기록하거나 **Download Credentials** 버튼을 선택하세요. 나중에 Braze 대시보드에 입력해야 합니다.

![액세스 키 ID와 비밀 액세스 키가 표시된 AWS IAM 사용자 보안 자격 증명 페이지.]({% image_buster /assets/img_archive/S3_Credentials.png %})

### 3단계: 정책 생성 {#secret-key-3}

**Policies** > **Get Started** > **Create Policy**로 이동하여 사용자에 대한 권한을 추가합니다. 그런 다음 **Create Your Own Policy**를 선택합니다. 이렇게 하면 Braze가 지정된 버킷에만 액세스할 수 있도록 권한이 제한됩니다.

![S3 통합을 위한 정책 옵션이 표시된 AWS IAM 정책 생성 화면.]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Currents와 대시보드 데이터 내보내기에는 서로 다른 정책이 필요합니다. `s3:GetObject`는 Braze 백엔드에서 오류 처리를 수행하기 위해 필요합니다.
{% endalert %}

원하는 정책 이름을 지정하고 다음 코드 스니펫을 **Policy Document** 섹션에 입력합니다. `INSERTBUCKETNAME`을 버킷 이름으로 바꾸세요. 이러한 권한이 없으면 통합이 자격 증명 확인에 실패하여 생성되지 않습니다.

{% alert note %}
메시지 아카이빙만 설정하는 경우 **Dashboard Data Export** 탭의 코드 스니펫을 사용하세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### 4단계: 정책 연결 {#secret-key-4}

새 정책을 생성한 후 **Users**로 이동하여 해당 사용자를 선택합니다. **Permissions** 탭에서 **Attach Policy**를 선택하고 새로 생성한 정책을 선택합니다. 이제 AWS 자격 증명을 Braze 계정에 연결할 준비가 되었습니다.

![Attach Policy 작업이 선택된 AWS IAM 사용자 권한 탭.]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### 5단계: Braze를 AWS에 연결 {#secret-key-5}

{% alert note %}
메시지 아카이빙만 설정하는 경우 **Dashboard Data Export** 탭의 단계를 따르세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Braze에서 **파트너 통합** > **Currents**로 이동합니다.

그런 다음 **Create New Current**을 선택한 후 **Amazon S3 Data Export**를 선택합니다.

Current의 이름을 지정합니다. **Credentials** 섹션에서 **AWS Secret Access Key**가 선택되어 있는지 확인한 후 S3 액세스 ID, AWS 비밀 액세스 키, AWS S3 버킷 이름을 지정된 필드에 입력합니다.

{% multi_lang_include currents/contact_email_notifications.md %}

![AWS 비밀 키 자격 증명 필드가 포함된 Amazon S3용 Braze 새 Current 생성 양식.]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWS 액세스 키 ID와 비밀 액세스 키를 최신 상태로 유지하세요. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중단합니다. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

필요에 따라 다음 커스터마이제이션도 추가할 수 있습니다:

- **폴더 경로:** 기본값은 `currents`입니다. 이 폴더가 존재하지 않으면 Braze가 자동으로 생성합니다.
- **서버 측 저장 시 AES-256 암호화:** 기본값은 OFF이며 `x-amz-server-side-encryption` 헤더를 포함합니다.

계속하려면 **Launch Current**을 선택합니다.

자격 증명이 성공적으로 검증되었는지 여부를 알려주는 알림이 표시됩니다. 이제 AWS S3가 Braze Currents에 설정되었습니다.

{% endtab %}
{% tab Dashboard Data Export %}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하고 **Amazon S3**를 선택합니다.

**AWS Credentials** 페이지에서 **AWS Secret Access Key**가 선택되어 있는지 확인한 후 AWS 액세스 ID, AWS 비밀 액세스 키, AWS S3 버킷 이름을 지정된 필드에 입력합니다. 비밀 키를 입력할 때 먼저 **Test Credentials**를 선택하여 자격 증명이 올바른지 확인한 후, 성공하면 **Save**를 선택합니다.

![테스트 및 저장 작업이 표시된 Braze Amazon S3 기술 파트너 자격 증명 페이지.]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
사용자로 이동하여 AWS 콘솔의 **Security Credentials** 탭에서 **Create Access Key**를 선택하면 언제든지 새 자격 증명을 가져올 수 있습니다.
{% endalert %}

자격 증명이 성공적으로 검증되었는지 여부를 알려주는 알림이 표시됩니다. 이제 AWS S3가 Braze 계정에 통합되었습니다.

{% endtab %}
{% endtabs %}

## AWS 역할 ARN 인증 방법 {#aws-role-arn-auth-method}

이 인증 방법은 역할 Amazon Resource Name(ARN)을 생성하여, Braze Amazon 계정이 버킷에 데이터를 기록하기 위해 생성한 역할의 구성원으로 인증할 수 있도록 합니다.

### 1단계: 정책 생성 {#role-arn-1}

시작하려면 계정 관리자로 AWS 관리 콘솔에 로그인합니다. AWS 콘솔의 IAM 섹션으로 이동하여 탐색 바에서 **Policies**를 선택한 다음 **Create Policy**를 선택합니다.

![Create Policy 버튼이 선택된 AWS IAM Policies 페이지.]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Currents와 대시보드 데이터 내보내기에는 서로 다른 정책이 필요합니다. `s3:GetObject`는 Braze 백엔드에서 오류 처리를 수행하는 데 필요합니다.
{% endalert %}

**JSON** 탭을 열고 다음 코드 스니펫을 **Policy Document** 섹션에 입력합니다. `INSERTBUCKETNAME`을 실제 버킷 이름으로 바꿔야 합니다. 완료되면 **Review Policy**를 선택합니다.

{% alert note %}
메시지 아카이빙만 설정하는 경우 **대시보드 데이터 내보내기** 탭의 코드 스니펫을 사용하세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab 대시보드 데이터 내보내기 %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

다음으로 정책에 이름과 설명을 입력하고 **Create Policy**를 선택합니다.

![정책 이름과 설명 필드가 있는 AWS IAM 정책 검토 단계.]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![새로 생성된 S3 정책이 표시된 AWS IAM 정책 목록.]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### 2단계: 역할 생성 {#role-arn-2}

콘솔의 동일한 IAM 섹션에서 **Roles** > **Create Role**을 선택합니다.

![Create Role 버튼이 선택된 AWS IAM Roles 페이지.]({{site.baseurl}}/assets/img/create_role_1_list.png)

Braze 계정에서 Braze 계정 ID와 외부 ID를 확인합니다:

- **Currents:** Braze에서 **파트너 통합** > **Currents**로 이동합니다. 다음으로 **Create New Current**을 선택한 후 **Amazon S3 Data Export**를 선택합니다. 여기에서 역할을 생성하는 데 필요한 식별자를 찾을 수 있습니다.
- **대시보드 데이터 내보내기:** Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Amazon S3**를 선택합니다. 여기에서 역할을 생성하는 데 필요한 식별자를 찾을 수 있습니다. (메시지 아카이빙만 설정하는 경우 여기에서 역할을 생성합니다.)

AWS 콘솔로 돌아가서 신뢰할 수 있는 엔터티 선택기 유형으로 **Another AWS Account**를 선택합니다. Braze 계정 ID를 입력하고 **Require external ID** 체크박스를 선택한 다음 Braze 외부 ID를 입력합니다. 완료되면 **Next**를 선택합니다.

![S3 '역할 생성' 페이지. 이 페이지에는 역할 이름, 역할 설명, 신뢰할 수 있는 엔터티, 정책, 권한 경계에 대한 필드가 있습니다.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### 3단계: 정책 연결 {#role-arn-3}

다음으로 앞서 생성한 정책을 역할에 연결합니다. 검색 바에서 정책을 검색하고 정책 옆의 체크 표시를 선택하여 연결합니다. 완료되면 **Next**를 선택합니다.

![역할 ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

역할에 이름과 설명을 입력하고 **Create Role**을 선택합니다.

![역할 ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

이제 목록에서 새로 생성된 역할을 확인할 수 있습니다.

### 4단계: Braze AWS에 연결 {#role-arn-4}

AWS 콘솔에서 새로 생성된 역할을 목록에서 찾습니다. 이름을 선택하여 해당 역할의 세부 정보를 엽니다.

![새로 생성된 역할의 AWS IAM 역할 세부 정보 페이지.]({{site.baseurl}}/assets/img/create_role_5_created.png)

역할 요약 페이지 상단의 **Role ARN**을 메모합니다.

![역할 ARN 값이 표시된 AWS IAM 역할 요약.]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Braze 계정으로 돌아가서 제공된 필드에 역할 ARN을 복사합니다.

{% alert note %}
메시지 아카이빙만 설정하는 경우 **대시보드 데이터 내보내기** 탭의 단계를 따르세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Braze에서 **파트너 통합** > **Currents**로 이동합니다. 다음으로 **Create New Current**을 선택한 후 **Amazon S3 Data Export**를 선택합니다.

![AWS 역할 ARN 및 버킷 필드가 있는 Braze Currents Amazon S3 설정 화면.]({{site.baseurl}}/assets/img/currents-role-arn.png)

Current에 이름을 지정합니다. 그런 다음 **자격 증명** 섹션에서 **AWS Role ARN**이 선택되어 있는지 확인한 후, 지정된 필드에 역할 ARN과 AWS S3 버킷 이름을 입력합니다.

{% multi_lang_include currents/contact_email_notifications.md %}

필요에 따라 다음과 같은 커스텀 설정을 추가할 수도 있습니다:

- 폴더 경로(기본값: `currents`)
- 서버 측 저장 시 AES-256 암호화(기본값: OFF) - `x-amz-server-side-encryption` 헤더를 포함합니다

**Launch Current**을 선택하여 계속합니다. 자격 증명이 성공적으로 검증되었는지 알림이 표시됩니다. 이제 AWS S3가 Braze Currents에 설정되었습니다.

{% alert important %}
"S3 credentials are invalid" 오류가 표시되는 경우, AWS에서 역할을 생성한 직후에 너무 빨리 통합을 시도했기 때문일 수 있습니다. 잠시 기다린 후 다시 시도하세요. 메시지에서 `PutObject` 액세스 또는 대시보드 데이터 내보내기의 서버 측 암호화와 관련된 내용이 언급되는 경우 [S3 자격 증명 오류 문제 해결](#troubleshooting)을 참조하세요.
{% endalert %}

{% endtab %}
{% tab 대시보드 데이터 내보내기 %}

Braze에서 **통합** 아래의 **기술 파트너** 페이지로 이동하여 **Amazon S3**를 선택합니다.

![AWS 역할 ARN 자격 증명이 선택된 Braze Amazon S3 기술 파트너 페이지.]({{site.baseurl}}/assets/img/data-export-role-arn.png)

**AWS Credentials** 페이지에서 **AWS Role ARN** 라디오 버튼이 선택되어 있는지 확인한 후, 지정된 필드에 역할 ARN과 AWS S3 버킷 이름을 입력합니다. 먼저 **Test Credentials**를 선택하여 자격 증명이 올바르게 작동하는지 확인한 다음, 성공하면 **Save**를 선택합니다.

{% alert tip %}
사용자로 이동한 후 AWS 콘솔의 **Security Credentials** 탭에서 **Create Access Key**를 선택하면 언제든지 새 자격 증명을 가져올 수 있습니다.
{% endalert %}

자격 증명이 성공적으로 검증되었는지 알림이 표시됩니다. 이제 AWS S3가 Braze 계정에 통합되었습니다.

{% endtab %}
{% endtabs %}

## Currents의 Amazon S3 자격 증명 업데이트 {#updating-currents-credentials}

통합을 중지하거나 이미 버킷으로 내보낸 데이터를 잃지 않고 기존 Braze Currents 커넥터의 Amazon S3 자격 증명을 업데이트할 수 있습니다.

자격 증명을 새로고침하거나 **AWS Secret Access Key**와 **AWS Role ARN** 간에 전환하려면, 이 문서 앞부분에서 선택한 방법에 대한 IAM 및 AWS 측 단계(정책, 사용자 또는 역할, 필요한 식별자)를 완료하세요.

AWS에서 자격 증명 준비를 마쳤으면 Braze에서 **파트너 통합** > **Currents**로 이동하여 목록에서 Amazon S3 커넥터를 찾고 **Edit**을 선택한 다음 **Credentials**를 업데이트하고 **Update Current**을 선택합니다. Braze가 입력한 자격 증명을 검증하며, 커넥터는 계속 실행되고 버킷에 이미 있는 데이터는 그대로 사용할 수 있습니다. 자세한 내용은 [Currents 설정에서 Currents 업데이트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents)를 참조하세요.

## 내보내기 동작 {#export-behavior}

클라우드 데이터 스토리지 솔루션과 내보내기 API, 대시보드 보고서 또는 CSV 보고서를 통합한 사용자는 다음과 같은 동작을 경험합니다:

- 모든 API 내보내기는 응답 본문에 다운로드 URL을 반환하지 않으며, 데이터 스토리지를 통해 조회해야 합니다.
- 모든 대시보드 보고서 및 CSV 보고서는 사용자의 이메일로 전송되어 다운로드할 수 있으며(스토리지 권한 불필요), 데이터 스토리지에 백업됩니다.

### `Unable to connect to S3, please validate that your credentials are correct` 오류 {#unable-to-connect-to-s3-please-validate-that-your-credentials-are-correct-error}

CSV 내보내기를 다운로드할 때 이 오류가 표시되면 **기술 파트너** 페이지에서 [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) 통합을 열고 **Test Credentials**를 선택합니다. 결과에서 어떤 유효성 검사가 실패했는지 확인할 수 있습니다. 예를 들어, 키에 `GetObject` 권한이 누락되어 Braze가 다운로드 링크를 생성하지 못할 수 있습니다.

IAM 정책을 업데이트하여 통합 사용자 또는 역할이 Braze 통합에 구성된 S3 버킷 및 객체 경로에서 `s3:GetObject`를 호출할 수 있도록 합니다. 내보내기 관련 추가 문제는 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)을 참조하세요.

{% alert important %}
**JSON 형식 요구 사항:** JSON 내보내기의 경우, Braze는 JSONL(줄바꿈으로 구분된 JSON) 형식을 사용하며, 각 줄에 별도의 JSON 객체가 포함됩니다. 이 형식은 단일 JSON 배열 또는 객체인 표준 JSON과 다릅니다. 내보낸 파일의 각 줄은 유효한 JSON 객체이지만, 파일 전체는 하나의 유효한 JSON 문서가 아닙니다. 이러한 파일을 처리할 때는 전체 파일을 하나의 JSON 문서로 파싱하지 말고 각 줄을 별도의 JSON 객체로 개별 파싱하세요.

Currents 내보내기는 JSON이 아닌 Apache Avro 형식(`.avro` 파일)을 사용합니다. 이 JSON 형식 요구 사항은 대시보드 데이터 내보내기 및 API 내보내기에 적용됩니다.
{% endalert %}

## 다중 커넥터 {#multiple-connectors}

S3 버킷으로 전송하기 위해 둘 이상의 Currents 커넥터를 생성하려는 경우, 동일한 자격 증명을 사용할 수 있지만 각 커넥터에 대해 서로 다른 폴더 경로를 지정해야 합니다. 동일한 워크스페이스에서 생성하거나 여러 워크스페이스에 분할하여 생성할 수 있습니다. 또한 각 통합에 대해 별도의 정책을 생성하거나 두 통합을 모두 포함하는 하나의 정책을 생성할 수도 있습니다.

동일한 S3 버킷을 Currents와 데이터 내보내기 모두에 사용할 계획이라면, 각 통합에 서로 다른 권한이 필요하므로 두 개의 별도 정책을 생성해야 합니다.

## 문제 해결 {#troubleshooting}

### 오류: 계정에 `PutObject` 액세스 권한이 없음 {#error-account-does-not-have-putobject-access}

대시보드 데이터 내보내기를 위해 Amazon S3 자격 증명을 저장할 때 다음 오류가 표시되면, 잘못된 권한 또는 서버 측 암호화 설정 때문일 수 있습니다.

```
S3 Credentials are invalid because this account does not have 'PutObject access'. Please check the permissions and ensure that this key has access to 'PutObject' in the 'CUSTOMER-BUCKET-HERE' bucket.
```

이 문제를 해결하려면 다음 영역을 확인하세요.

#### 잘못된 버킷 정책 {#incorrect-bucket-policy}

[Amazon S3 통합](#integration)에 설명된 대로 올바른 권한으로 정책을 생성했는지 확인하세요(인증 방법에 맞는 **Dashboard Data Export** 정책을 사용하세요).

#### 서버 측 암호화 {#server-side-encryption}

```
User: arn:aws:sts::XXX:assumed-role/braze-iam-role/braze is not authorized to perform: kms:GenerateDataKey on resource: arn:aws:XXX because no identity-based policy allows the kms:GenerateDataKey action
```

[Braze 지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)이나 AWS 로그에서 이 오류 메시지를 받으면, S3 버킷이 AWS Key Management Service(SSE-KMS) 암호화로 구성되어 있는 것입니다. Braze는 Currents 또는 대시보드 데이터 내보내기에 대해 SSE-KMS를 지원하지 않습니다. 이 문제를 해결하려면 S3 버킷에서 SSE-KMS를 비활성화하세요.

{% alert note %}
Braze는 S3 관리형 키(SSE-S3)를 사용한 서버 측 암호화를 지원하며, 이는 Currents 및 대시보드 데이터 내보내기 모두와 호환됩니다.
{% endalert %}

#### 추가 권한 확인 {#check-additional-permissions}

`s3:GetBucketLocation` 및 `s3:PutObject`를 포함하여 필요한 권한이 있는지 확인하세요.