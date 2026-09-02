---
nav_title: Outgrow
article_title: Outgrow
alias: /partners/outgrow/
description: "이 문서에서는 Outgrow와 Braze 간의 네이티브 통합을 구성하여 사용자 데이터 동기화 및 개인화된 캠페인을 강화하는 방법에 대한 종합 가이드를 제공합니다."
page_type: partner
search_tag: Partner
---

# Outgrow

> [Outgrow](https://outgrow.co/)는 퀴즈, 계산기, 설문조사 및 기타 유형의 인터랙티브 콘텐츠를 만들어 사용자 데이터와 인사이트를 수집할 수 있는 인터랙티브 콘텐츠 플랫폼입니다. Braze와 Outgrow 통합을 사용하면 Outgrow에서 Braze로 사용자 데이터를 자동으로 전송하여 고도로 개인화되고 타겟팅된 캠페인을 실행할 수 있습니다.

인터랙티브 콘텐츠에 Braze와 Outgrow 통합을 사용하면 다음과 같은 이점을 얻을 수 있습니다:

- **향상된 개인화**: Outgrow 퀴즈, 설문조사, 계산기에서 수집한 데이터를 Braze의 커스텀 속성에 매핑할 수 있습니다. 이 데이터를 통해 정밀한 세분화와 개인화된 캠페인이 가능합니다.
- **실시간 데이터 동기화**: Outgrow 데이터를 Braze에서 실시간으로 수신하여 사용자 인사이트에 즉시 대응할 수 있습니다. 이를 통해 사용자의 최근 상호작용을 기반으로 적시에 후속 조치를 취하거나 개인화된 메시지를 보낼 수 있습니다.
- **간소화된 데이터 관리**: Outgrow와 Braze 간의 데이터 전송을 자동화하여 수동 데이터 내보내기 및 가져오기를 없애고, 데이터 불일치를 줄이며, 시간을 절약할 수 있습니다.
- **향상된 사용자 경험**: 사용자 인사이트를 활용하여 더 관련성 높은 경험을 만들어 만족도, 유지, LTV or 생애주기 가치를 높일 수 있습니다.
- **유연한 타겟팅 및 세분화**: Outgrow 데이터를 사용하여 Braze에서 세분화를 정교하게 조정하고, 특정 상호작용(예: 퀴즈 점수 또는 설문조사 응답)을 기반으로 사용자를 타겟팅하여 사용자에게 공감을 주는 캠페인을 만들 수 있습니다.

## 필수 조건 {#prerequisites}

Outgrow와 Braze 통합을 설정하기 전에 다음 사항을 확인하세요:

| 요구 사항 | 설명 |
|-------------|-------------|
| **Outgrow 계정** | 인터랙티브 콘텐츠 및 데이터 전송 설정을 구성하고 관리할 수 있는 등록된 Outgrow 계정 |
| **Braze 계정** | REST API 자격 증명에 접근할 수 있는 Braze 계정 |
| **API 키** | 사용자 데이터 전송을 활성화하기 위해 `users.track` 권한이 있는 Braze API 키 |
| **Braze의 커스텀 속성** | Outgrow 응답(예: 퀴즈 점수, 세그먼트 등)을 캡처하기 위해 Braze에 설정된 커스텀 속성 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

다음 단계에 따라 Braze와 Outgrow 통합을 구성하세요:

### 1단계: Braze API 키 생성 {#step-1-generate-braze-api-key}

1. Braze 계정에서 **개발자 콘솔** > **API 설정**으로 이동합니다.
2. **새 API 키 생성**을 선택합니다.
3. API 키의 이름을 지정하고, `users.track` 권한을 활성화한 후 API 키를 저장합니다.

### 2단계: Outgrow에서 Braze 통합 구성 {#step-2-configure-the-braze-integration-in-outgrow}

1. Outgrow 계정에 로그인합니다.
2. 대시보드에서 **Integrations**로 이동합니다.
3. 사용 가능한 통합 목록에서 **Braze**를 선택합니다.
4. **Braze API Key**와 **REST API Endpoint URL**을 입력합니다:
   - **API Key**: Braze에서 생성한 API 키를 입력합니다
   - **REST Endpoint URL**: Braze 인스턴스의 엔드포인트를 입력합니다(예: `https://rest.iad-01.braze.com`)
5. **Save**를 선택하여 통합을 활성화합니다.

### 3단계: Outgrow 데이터를 Braze 속성에 매핑 {#step-3-map-outgrow-data-to-braze-attributes}

Outgrow에서 인터랙티브 콘텐츠의 응답(예: 퀴즈 결과, 커스텀 세그먼트 또는 인게이지먼트 점수)을 Braze 커스텀 속성에 매핑할 수 있습니다.

1. Outgrow의 Braze용 **Integration Settings**에서 Braze 속성에 매핑할 Outgrow 응답을 정의합니다.
2. 선택한 각 응답이 Braze의 커스텀 속성과 일치하는지 확인합니다. 예를 들어:
   - 퀴즈 점수는 `outgrow_quiz_score`에 매핑됩니다.
   - 커스텀 세그먼트는 `outgrow_custom_segment`에 매핑됩니다.
3. 매핑 설정을 저장합니다.

### 4단계: 통합 테스트 {#step-4-test-the-integration}

통합을 구성한 후 Outgrow에서 Braze로 데이터가 올바르게 전송되는지 확인하기 위해 테스트를 실행합니다.

1. Outgrow 경험(예: 퀴즈 또는 계산기)을 게시하고 테스트 사용자로 완료합니다.
2. Braze 계정에서 **고객 프로필** 섹션으로 이동하여 업데이트된 속성(예: `outgrow_quiz_score` 또는 `outgrow_custom_segment`)을 확인합니다.
3. 데이터가 적절한 커스텀 속성 아래에 올바르게 채워졌는지 확인합니다.

## Braze에서 Outgrow 데이터를 세분화 및 타겟팅에 활용하기 {#using-outgrow-data-in-braze-for-segmentation-and-targeting}

### Outgrow 데이터로 Braze에서 Segments 생성하기 {#creating-segments-in-braze-with-outgrow-data}

통합을 통해 Outgrow 응답에서 채워진 커스텀 속성을 기반으로 Braze Segments를 생성할 수 있습니다.

1. Braze에서 **Engagement** > **Segments**로 이동하고 **Create New Segment**를 선택합니다.
2. Segment 이름을 지정하고 Outgrow 데이터를 기반으로 필터를 설정합니다. 예를 들어:
   - `outgrow_quiz_score`로 필터링하여 특정 임계값 이상의 점수를 받은 사용자를 타겟팅합니다.
   - `outgrow_custom_segment`로 필터링하여 특정 Outgrow 정의 세그먼트에 속하는 사용자를 타겟팅합니다.
3. Campaigns 및 Canvases에서 사용할 수 있도록 Segment를 저장합니다.

### Outgrow 정의 세그먼트로 캠페인 시작하기 {#launching-campaigns-with-outgrow-defined-segments}

Outgrow 데이터에서 생성된 커스텀 세그먼트를 사용하여 Braze 캠페인을 개인화하고 인터랙티브 콘텐츠에 대한 응답을 기반으로 사용자를 타겟팅할 수 있습니다. 더 개인화된 사용자 경험을 만들려면 다음 단계를 따르세요:

1. Braze에서 **Engagement** > **Campaigns**로 이동합니다.
2. **Create Campaign**을 선택하고 캠페인 유형(이메일, 푸시, 인앱 메시지 등)을 선택합니다.
3. 오디언스 타겟팅 단계에서 Outgrow 속성으로 생성된 세그먼트(예: 특정 퀴즈 점수 또는 세그먼트를 가진 사용자)를 선택합니다.
4. 캠페인 콘텐츠와 설정을 커스터마이즈한 후 시작합니다.

## 일반적인 문제 해결 {#troubleshooting-common-issues}

| 문제 | 해결 방법 |
|-------|----------|
| **데이터가 Braze로 전송되지 않음** | Outgrow 통합 설정에서 API 키와 엔드포인트 URL이 올바른지 확인하세요. API 키에 `users.track` 권한이 활성화되어 있는지 확인하세요. |
| **잘못된 데이터 매핑** | 매핑된 각 Outgrow 응답이 유효한 Braze 커스텀 속성에 대응하는지, 속성 이름이 정확히 일치하는지 확인하세요. |
| **Segment가 올바르게 필터링되지 않음** | Braze의 커스텀 속성이 올바르게 설정되어 있고 데이터를 수신하고 있는지 확인하세요. Segment 필터 로직을 다시 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="일반적인 문제 해결" }

## 추가 고려 사항 {#additional-considerations}

- **데이터 프라이버시**: 플랫폼 간에 사용자 데이터를 전송할 때 데이터 프라이버시 규정(예: GDPR 및 CCPA)을 준수하세요.
- **사용량 제한**: Outgrow 데이터는 실시간으로 Braze에 전송되지만, 대량의 데이터에 대해서는 Braze API 사용량 제한이 적용될 수 있습니다. 트래픽이 많은 경험에 대해 적절히 계획하세요.
- **커스텀 속성 구성**: 이 통합에 사용되는 Braze 커스텀 속성이 Outgrow에서 전송된 데이터를 캡처하도록 올바르게 구성되어 있는지 확인하세요.

추가 지원이 필요하면 [Outgrow 설명서](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze)를 참조하거나 Outgrow 고객지원에 문의하세요.