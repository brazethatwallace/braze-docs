---
nav_title: S3 보안 이벤트 내보내기
article_title: S3로 보안 설정 내보내기
page_order: 1
page_type: reference
description: "이 참조 문서에서는 매일 자정 UTC에 보안 이벤트를 Amazon S3로 자동으로 내보내는 방법을 다룹니다."
---

# Amazon S3로 보안 이벤트 내보내기 {#security-events-export-with-amazon-s3}

> 보안 이벤트를 클라우드 스토리지 제공업체인 Amazon S3로 자동으로 내보낼 수 있으며, 이는 자정 UTC에 실행되는 일일 작업을 통해 이루어집니다. 설정 후에는 대시보드에서 보안 이벤트를 수동으로 내보낼 필요가 없습니다. 이 작업은 지난 24시간 동안의 보안 이벤트를 CSV 형식으로 구성된 S3 저장소에 내보냅니다. CSV 파일은 수동으로 내보낸 보고서와 동일한 열을 사용하며, `Version` 열이 추가됩니다.

{% alert note %}
10,000행 제한은 대시보드에서 수동으로 CSV 보고서를 다운로드할 때만 적용됩니다. S3로의 보안 이벤트 내보내기는 이 행 제한의 적용을 받지 않습니다.
{% endalert %}

Braze는 Amazon S3 내보내기를 설정하기 위한 두 가지 S3 인증 및 승인 방법을 지원합니다:

- AWS 비밀 액세스 키 방법
- AWS 역할 ARN 방법

## AWS 비밀 액세스 키 방법 {#aws-secret-access-key-method}

이 방법은 Braze가 AWS 계정의 사용자로 인증하여 버킷에 데이터를 쓸 수 있도록 하는 비밀 키와 액세스 키 ID를 생성합니다.

### 1단계: IAM(Identity and Access Management) 사용자 생성 {#step-1-create-an-identity-and-access-management-iam-user}

비밀 액세스 키와 액세스 키 ID를 가져오려면 [AWS 계정 설정](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin)의 지침에 따라 IAM 사용자를 생성해야 합니다.

### 2단계: 자격 증명 가져오기 {#step-2-get-credentials}

1. 새 사용자를 만든 후 액세스 키를 생성하고 액세스 키 ID 및 비밀 액세스 키를 다운로드합니다.

!["liyu-chen-test"라는 역할에 대한 요약 페이지입니다.]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2. 이 자격 증명을 어딘가에 기록하거나 자격 증명 파일을 다운로드하세요. 나중에 Braze에 입력해야 합니다.

![액세스 키와 비밀 액세스 키가 포함된 필드입니다.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### 3단계: 정책 생성 {#step-3-create-policy}

1. 사용자에 대한 권한을 추가하려면 **IAM**(Identity and Access Management) > **Policies** > **Create Policy**로 이동합니다.
2. 제한된 권한을 부여하는 **Create Your Own Policy**를 선택하여 Braze가 지정된 버킷에만 접근할 수 있도록 합니다.
3. 원하는 정책 이름을 지정합니다.
4. 다음 코드 스니펫을 **Policy Document** 섹션에 입력합니다. "INSERTBUCKETNAME"을 버킷 이름으로 교체해야 합니다. 이러한 권한이 없으면 통합이 자격 증명 확인에 실패하여 생성되지 않습니다.

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

### 4단계: 정책 연결 {#step-4-attach-policy}

1. 새 정책을 만든 후 **Users**로 이동하여 특정 사용자를 선택합니다.
2. **Permissions** 탭에서 **Add Permissions**를 선택하고 정책을 직접 연결한 다음 해당 정책을 선택합니다.

이제 AWS 자격 증명을 Braze 계정에 연결할 준비가 되었습니다!

### 5단계: Braze를 AWS에 연결 {#step-5-link-braze-to-aws}

1. Braze에서 **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하여 **보안 이벤트 다운로드** 섹션으로 스크롤합니다.
2. **클라우드 스토리지로 내보내기** 아래에서 **Export to AWS S3**를 토글하고 **AWS secret access key**를 선택하여 S3 내보내기를 활성화합니다.
3. 다음 정보를 입력합니다:

- AWS 액세스 키 ID
- AWS 버킷 이름
- AWS 비밀 액세스 키
    - 이 키를 입력할 때 먼저 **Test Credentials**를 선택하여 자격 증명이 올바르게 작동하는지 확인합니다.

![Braze 계정 및 Braze 외부 ID가 입력된 "보안 이벤트 다운로드" 페이지입니다.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4. **변경 사항 저장**을 선택합니다.

AWS S3가 Braze 계정에 통합되었습니다!

## AWS 역할 ARN 방법 {#aws-role-arn-method}

AWS 역할 ARN 방법은 Braze Amazon 계정이 해당 역할의 구성원으로 인증할 수 있도록 하는 역할 Amazon 리소스 이름(ARN)을 생성합니다.

### 1단계: 정책 생성 {#step-1-create-policy}

1. 계정 관리자로 AWS 관리 콘솔에 로그인합니다.
2. AWS 콘솔에서 **IAM**(Identity and Access Management) 섹션 > **Policies**로 이동한 다음 **Create Policy**를 선택합니다.

![정책 목록과 "Create policy" 버튼이 있는 페이지입니다.]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3. **JSON** 탭을 열고 다음 코드 스니펫을 **Policy Document** 섹션에 입력합니다. `INSERTBUCKETNAME`을 버킷 이름으로 교체해야 합니다.

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

{: start="4"}
4. 정책을 검토한 후 **Next**를 선택합니다.

![정책을 검토하고 선택적으로 권한을 추가할 수 있는 페이지입니다.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5. 정책에 이름과 설명을 지정한 다음 **Create Policy**를 선택합니다.

![정책을 검토하고 생성하는 페이지입니다.]({% image_buster /assets/img/security_export/review_and_create.png %})

### 2단계: 역할 생성 {#step-2-create-role}

1. Braze에서 **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하여 **보안 이벤트 다운로드** 섹션으로 스크롤합니다.
2. **AWS Role ARN**을 선택합니다.
3. 역할을 생성하는 데 필요한 식별자인 Braze 계정 ID와 Braze 외부 ID를 기록합니다.

![Braze 계정 및 Braze 외부 ID가 입력된 "보안 이벤트 다운로드" 페이지입니다.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. AWS 콘솔에서 **IAM**(Identity and Access Management) 섹션 > **Roles** > **Create Role**로 이동합니다.
5. 신뢰할 수 있는 엔터티 선택기 유형으로 **Another AWS Account**를 선택합니다.
6. Braze 계정 ID를 입력하고 **Require external ID** 확인란을 선택한 다음 Braze 외부 ID를 입력합니다.
7. 완료되면 **Next**를 선택합니다.

![신뢰할 수 있는 엔터티 유형을 선택하고 AWS 계정 정보를 제공하는 옵션이 있는 페이지입니다.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### 3단계: 정책 연결 {#step-3-attach-policy}

1. 검색 바에서 이전에 만든 정책을 검색한 다음 정책 옆에 체크 표시를 하여 연결합니다.
2. **Next**를 선택합니다.

![유형 및 설명 열이 있는 정책 목록입니다.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3. 역할에 이름과 설명을 지정하고 **Create Role**을 선택합니다.

![이름, 설명, 신뢰 정책, 권한 및 태그와 같은 역할 세부 정보를 제공하는 필드입니다.]({% image_buster /assets/img/security_export/name_review_create.png %})

새로 생성된 역할이 목록에 나타납니다!

### 4단계: Braze AWS에 연결 {#step-4-link-to-braze-aws}

1. AWS 콘솔에서 목록에 있는 새로 생성된 역할을 찾습니다. 이름을 선택하여 해당 역할의 세부 정보를 열고 **ARN**을 기록합니다.

!["security-event-export-olaf"라는 역할의 요약 페이지입니다.]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2. Braze에서 **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하여 **보안 이벤트 다운로드** 섹션으로 스크롤합니다.

!["Export to AWS S3" 토글이 켜진 "보안 이벤트 다운로드" 섹션입니다.]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3. **AWS role ARN**이 선택되어 있는지 확인한 다음 지정된 필드에 역할 ARN과 AWS S3 버킷 이름을 입력합니다.
4. **Test Credentials**를 선택하여 자격 증명이 올바르게 작동하는지 확인합니다.
5. **변경 사항 저장**을 선택합니다.

AWS S3가 Braze 계정에 통합되었습니다!