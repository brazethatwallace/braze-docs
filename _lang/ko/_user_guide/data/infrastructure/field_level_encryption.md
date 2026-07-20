---
nav_title: 식별자 필드 수준 암호화
article_title: 식별자 필드 수준 암호화
page_order: 2
alias: "/field_level_encryption/"
description: "이 참고 문서에서는 Braze에서 공유되는 개인 식별 정보(PII)를 최소화하기 위해 이메일 주소를 암호화하는 방법에 대해 설명합니다."
page_type: reference
---

# 식별자 필드 수준 암호화 {#identifier-field-level-encryption}

> Braze에서 공유되는 개인 식별 정보(PII)를 최소화하기 위해 이메일 주소를 암호화합니다.

{% multi_lang_include data_activation/field_level_encryption_pii_description.md %}

{% alert important %}
식별자 필드 수준 암호화는 애드온 기능으로 사용할 수 있습니다. 식별자 필드 수준 암호화를 시작하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 작동 원리 {#how-it-works}

이메일 주소는 반드시 해시 및 암호화를 거쳐야 Braze에 추가할 수 있습니다. 메시지가 전송되면 복호화된 이메일 주소를 가져오기 위해 AWS KMS로 호출이 이루어집니다. 다음으로, 해시된 이메일 주소가 전달 및 인게이지먼트 이벤트의 메타데이터에 삽입되어 원래 사용자와 연결됩니다. 이것이 바로 Braze가 이메일 분석을 추적하는 방법입니다. Braze는 포함된 모든 일반 텍스트 이메일 주소를 삭제하고 사용자의 일반 텍스트 이메일 주소를 저장하지 않습니다.

## 필수 조건 {#prerequisites}

식별자 필드 수준 암호화를 사용하려면 이메일 주소를 Braze로 보내기 **전에** 이메일 주소를 [암호화하고](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) [해시할](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) 수 있는 AWS KMS에 대한 액세스 권한이 있어야 합니다.

다음 단계에 따라 AWS 비밀 키 인증 방법을 설정하세요.

1. 액세스 키 ID와 비밀 액세스 키를 검색하려면 AWS Key Management Service에 대한 권한 정책을 사용하여 AWS에서 [IAM 사용자 및 관리자 그룹을 생성합니다](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin). IAM 사용자에게는 [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) 및 [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) 권한이 있어야 합니다. 자세한 내용은 [AWS KMS 권한](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html)을 참조하세요.
2. **Show User Security Credentials**를 선택하여 액세스 키 ID와 비밀 액세스 키를 확인합니다. AWS KMS 키를 연결할 때 입력해야 하므로 이 자격 증명을 어딘가에 메모해 두거나 **Download Credentials** 버튼을 선택합니다.
3. 다음 AWS 리전에서 KMS를 설정해야 합니다:
    - **Braze 미국 클러스터:** `us-east-1`
    - **Braze EU 클러스터:** `eu-central-1`
    - **Braze AU 클러스터:** `ap-southeast-2`
    - **Braze ID 클러스터:** `ap-southeast-3`
    - **Braze JP 클러스터:** `ap-northeast-1`
4. AWS Key Management Service에서 두 개의 키를 생성하고 키 사용 권한에 IAM 사용자가 추가되었는지 확인합니다:
    - **[암호화/복호화](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** **Symmetric** 키 유형과 **Encrypt and Decrypt** 키 사용을 선택합니다.
    - **[해시](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** **Symmetric** 키 유형과 **Generate and Verify MAC** 키 사용을 선택합니다. 키 사양은 **HMAC_256**이어야 합니다. 키를 생성한 후에는 Braze에 입력해야 하므로 HMAC 키 ID를 어딘가에 기록해 두세요.

![Symmetric, Generate and Verify MAC, HMAC_256 옵션이 선택된 키 설정 구성 화면]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## 1단계: AWS KMS 키 연결 {#step-1-connect-your-aws-kms-keys}

Braze 대시보드에서 **데이터 설정** > **Field-Level Encryption**으로 이동합니다. AWS KMS 설정에 다음을 입력합니다:

- 액세스 키 ID
- 비밀 액세스 키
- HMAC 키 ID(저장 후에는 업데이트할 수 없음)

## 2단계: 암호화된 필드 선택 {#step-2-select-your-encrypted-fields}

다음으로 **Email address**를 선택하여 필드를 암호화합니다.

필드에 대한 암호화가 켜져 있으면 복호화된 필드로 되돌릴 수 없습니다. 즉, 암호화는 영구적인 설정입니다. 이메일 주소에 대한 암호화를 설정할 때는 워크스페이스에 이메일 주소를 가진 사용자가 없는지 확인하세요. 이렇게 하면 워크스페이스에 대한 기능을 켤 때 Braze에 일반 텍스트 이메일 주소가 저장되지 않습니다.

![필드 수준 암호화 설정 화면]({% image_buster /assets/img/field_level_encryption.png %})

## 3단계: 사용자 가져오기 및 업데이트 {#step-3-import-and-update-users}

식별자 필드 수준 암호화가 켜져 있는 경우, 이메일 주소를 해시하고 암호화한 후 Braze에 추가해야 합니다. 이메일 주소를 해시하기 전에 반드시 소문자로 변환하세요. 자세한 내용은 [사용자 속성 오브젝트](#user-attributes-object)를 참조하세요.

Braze에서 이메일 주소를 업데이트할 때 `email`이 포함되는 모든 곳에서 해시된 이메일 값을 사용해야 합니다. 여기에는 다음이 포함됩니다:

- REST 엔드포인트:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- CSV를 통해 사용자 추가 또는 업데이트하기

{% alert note %}
이메일 주소로 새 사용자를 생성할 때는 사용자의 암호화된 이메일 값과 함께 `email_encrypted`를 추가해야 합니다. 그렇지 않으면 사용자가 생성되지 않습니다. 마찬가지로 이메일이 없는 기존 사용자에게 이메일 주소를 추가하는 경우 `email_encrypted`를 추가해야 합니다. 그렇지 않으면 사용자가 업데이트되지 않습니다.
{% endalert %}

## 고려 사항 {#considerations}

다음 기능은 식별자 필드 수준 암호화에서 지원되지 않습니다:

- SDK를 통한 이메일 주소 식별 및 캡처
- 인앱 메시지 이메일 캡처 양식
- 이메일 인사이트 메일박스 제공업체 차트를 포함한 수신자 도메인에 대한 보고
- 정규표현식으로 이메일 주소 필터링
- 오디언스 동기화
- Shopify 통합

### 사용자 속성 오브젝트 {#user-attributes-object}

`/users/track` 엔드포인트에서 식별자 필드 수준 암호화를 사용하는 경우 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)에 대한 다음 필드 세부 정보에 유의하세요:

- `email` 필드는 이메일의 해시값이어야 합니다.
- `email_encrypted` 필드는 이메일의 암호화된 값이어야 합니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 암호화와 해싱의 차이점은 무엇인가요? {#what-is-the-difference-between-encrypting-and-hashing}

암호화는 데이터를 암호화하고 복호화할 수 있는 양방향 기능입니다. 동일한 일반 텍스트 값을 여러 번 암호화하는 경우 AWS의 암호화 알고리즘(AES-256-GCM)은 서로 다른 암호화 값을 생성합니다. 해싱은 일반 텍스트를 복호화할 수 없는 방식으로 스크램블링하는 단방향 기능입니다. 해싱은 매번 동일한 값을 산출합니다. 이를 통해 동일한 이메일 주소를 공유하는 여러 사용자의 구독 상태 유지를 지원할 수 있습니다.

### 테스트 전송에 어떤 이메일 주소를 사용해야 하나요? {#what-email-address-should-i-use-in-my-test-send}

테스트 전송에서는 일반 텍스트 이메일 주소가 지원됩니다. 특정 사용자에게 이메일이 어떻게 표시되는지 확인하려면 다음과 같이 하세요:

1. **Preview message as a user**를 선택합니다.
2. **Test Send**에서 **Override recipients attributes with current preview user's attributes**를 선택합니다.

{%raw%}
### Braze에서 이 이메일 주소 Liquid `{{${email_address}}}`를 추가하면 어떻게 되나요? {#what-happens-if-i-add-this-email-address-liquid-email_address-in-braze}

Braze는 이메일을 보낼 때 일반 텍스트 이메일 주소를 렌더링합니다. 미리보기에서는 이메일의 암호화된 버전이 표시됩니다. 커스텀 원클릭 URL에서 사용자를 참조하는 경우 해당 사용자의 외부 ID를 사용하는 것이 좋습니다.

`{{${email_address}}}`는 현재 환경설정 센터 및 탈퇴 페이지에서 지원되지 않습니다.
{%endraw%}

### Currents에서 어떤 이메일 주소가 표시되나요? {#what-email-address-should-i-expect-to-see-in-currents}

해시된 이메일 주소는 이메일 전달 및 인게이지먼트 이벤트에 포함됩니다.

### 메시지 아카이브에서 어떤 이메일 주소가 표시되나요? {#what-email-address-should-i-expect-to-see-in-message-archiving}

일반 텍스트 이메일 주소는 메시지 아카이브에 포함됩니다. 이러한 이메일은 고객의 클라우드 스토리지 제공업체로 직접 전송되며 이메일 본문에는 다른 개인 데이터가 포함될 수 있습니다.

### 식별자 필드 수준 암호화로 구독 관리에 mail-to list-unsubscribe를 사용할 수 있나요? {#can-i-use-mail-to-list-unsubscribe-for-subscription-management-with-identifier-field-level-encryption}

아니요. mail-to list-unsubscribe를 사용하면 일반 텍스트로 복호화된 이메일 주소가 Braze로 전송됩니다. 식별자 필드 수준 암호화를 켜면 원클릭을 포함한 URL 기반 HTTP: 방식을 지원합니다. 또한 이메일 본문에 원클릭 수신 거부 링크를 포함할 것을 권장합니다.

### 식별자 필드 수준 암호화는 전화번호와 같은 다른 식별자를 지원하나요? {#does-identifier-field-level-encryption-support-other-identifiers-like-phone}

아니요. 현재 식별자 필드 수준 암호화는 이메일 주소에 대해서만 지원됩니다.