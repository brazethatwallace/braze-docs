---
nav_title: Lexer
article_title: Lexer
description: "이 참조 문서에서는 고객 데이터를 마케터에게 제공하여 매출을 촉진하는 경험을 만들어내는 고객 데이터 플랫폼인 Lexer와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> 리테일을 위해 구축된 고객 데이터 플랫폼인 [Lexer](https://lexer.io/)는 강력한 데이터 강화와 가장 직관적인 툴 및 전문 자문을 결합하여 향상된 고객 경험을 통해 브랜드의 점진적 매출 성장을 지원합니다.

_이 통합은 Lexer에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Lexer 통합을 사용하면 두 플랫폼 간에 데이터를 동기화할 수 있습니다. Lexer 데이터를 사용하여 유용한 Braze Segments를 생성하거나 기존 Segments를 Lexer로 가져와 인사이트를 확보하세요.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 파트너 계정 | 이 파트너십을 활용하려면 Lexer 계정이 필요합니다. |
| Braze REST API 키 | 모든 `user` 권한(`user.delete` 제외)과 `segment.list` 권한이 있는 Braze REST API 키. Lexer가 더 많은 Braze 오브젝트를 지원함에 따라 권한 세트가 변경될 수 있으므로, 지금 더 많은 권한을 부여하거나 향후 이러한 권한을 업데이트할 계획을 세울 수 있습니다.<br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Amazon AWS S3 버킷 및 자격 증명 | 통합을 시작하기 전에 Lexer 허브에 연결된 AWS S3 버킷에 대한 액세스 자격 증명이 있어야 합니다(직접 생성한 버킷이거나 Lexer가 생성하고 관리하는 버킷일 수 있습니다). 이 요구 사항에 대한 안내는 [Lexer](https://learn.lexer.io/docs/amazon-s3)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Lexer에서 **Manage > Integration**으로 이동하여 **Braze** 타일을 선택하고 **Integrate Braze**를 클릭합니다. 다음 정보를 입력하세요:
- **Braze REST endpoint**
- **Braze REST API key**
- **AWS Credentials**
  - **AWS S3 bucket name**
  - **AWS S3 [bucket region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 bucket path**: 이 경로는 [S3 버킷을 Braze에 연결]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)할 때 지정한 경로와 일치해야 합니다. Braze에 아무것도 지정하지 않은 경우 비워 두세요.
  - **AWS S3 secret access key**: [액세스 키 생성](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/)에 대한 정보는 Amazon을 참조하세요.
- **Braze export segment ID**: Lexer로 내보내려는 모든 사용자를 포함하여 Braze에서 생성한 Segment의 ID입니다. Lexer로 내보내지 않으려는 사용자가 있는 경우 Braze에서 생성한 Segment에서 해당 사용자를 제외할 수 있습니다. 세그먼트 식별자를 찾으려면 Braze에서 원하는 Segment를 클릭하고 **세그먼트 API 식별자**를 찾으세요.

![]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### AWS S3 옵션 선택(Lexer 관리형 또는 자체 관리형) {#choosing-an-aws-s3-option-lexer-managed-or-self-managed}
Lexer 관리형 버킷을 사용하는 것이 Braze를 Lexer 허브에 연결하는 데 권장되는 방법이며, 필요한 설정 작업을 줄일 수 있습니다. Lexer가 Braze를 구성하는 데 필요한 일회성 세부 정보를 제공합니다.

이미 S3 버킷을 Braze에 연결하여 다른 용도로 사용하고 있는 경우, 위의 단계에 따라 Lexer에 이 자체 관리형 버킷에 대한 액세스 권한을 제공해야 합니다.

이 통합은 Lexer에 기존 API 토큰과 시크릿을 제공하여 Lexer가 사용자를 대신하여 이러한 내보내기를 수행할 수 있도록 합니다. 또한 이러한 자격 증명과 S3 구성을 사용하여 Braze 데이터를 Lexer로 가져와 두 플랫폼의 데이터를 자동으로 동기화합니다.

## Braze로 Segments 보내기 {#sending-segments-to-braze}

### 1단계: 활성화 생성 {#step-1-create-activation}

Lexer Activate는 고객이 Segment에 들어오고 나갈 때 속성을 추가하거나 제거하여 Braze 프로필을 자동으로 업데이트합니다.

1. Lexer에서 **Lexer Activations**로 이동하여 **ACTIVATE NEW AUDIENCE**를 클릭합니다.
2. 이 Campaign에 적합한 Braze 활성화를 선택합니다.
3. Segment를 추가합니다.
4. 오디언스 이름을 업데이트합니다. 이 이름이 Braze에서 속성 값이 됩니다.
5. 이것은 Braze에서 업데이트할 커스텀 속성입니다. 업데이트하려면 [Lexer 고객지원](support@lexer.io)에 문의하세요.
6. 적절한 목록 동작을 확인합니다. 대부분의 경우 목록을 유지하는 것이 좋습니다.
7. 이용 약관을 검토하고 **SEND AUDIENCE**를 클릭합니다.

![]({% image_buster /assets/img/lexer/lexer.png %})

### 2단계: 활성화 확인 {#step-2-verify-activation}

Activate에서 활성화가 전송된 것으로 확인되면 Braze에서 레코드가 업데이트되기 시작하는 것을 볼 수 있습니다. Lexer로부터 확인 이메일을 받을 때까지 Braze에서 프로필이 완전히 업데이트되지 않습니다.

### 3단계: Braze Segment 생성 {#step-3-create-your-braze-segment}

Braze에서 Lexer의 오디언스 이름이 이제 `lexer_audience` 커스텀 속성의 값으로 표시됩니다. Braze에는 속성당 100개의 값 제한이 있습니다.

Segment를 생성하려면 **Segment > + Create Segment**로 이동하여 필터로 **Custom Attribute**를 선택합니다. 그런 다음 속성으로 `lexer_audience`를 선택하고 원하는 Lexer 오디언스 이름을 선택합니다. 완료되면 오디언스를 **저장**합니다.

이제 새로 생성한 Segment를 향후 Braze Campaigns 및 Canvases에 추가하여 이러한 최종 사용자를 타겟팅할 수 있습니다.