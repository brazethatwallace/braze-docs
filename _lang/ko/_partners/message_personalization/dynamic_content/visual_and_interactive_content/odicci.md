---
nav_title: Odicci
article_title: Odicci
description: "개인화된 마케팅 Campaign을 위해 Odicci와 Braze를 통합하는 단계별 가이드"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Odicci와 Braze 통합 {#integrate-odicci-with-braze}

> 로열티 기반 옴니채널 경험을 통해 비즈니스가 고객을 확보, 참여 및 유지할 수 있도록 지원하는 플랫폼인 [Odicci](https://www.odicci.com/)와 Braze를 통합하는 방법을 알아보세요.

{% alert tip %}
추가 리소스 및 FAQ는 [Odicci 도움말 센터](https://help.odicci.com)를 참조하세요.
{% endalert %}

## 활용 사례 {#use-cases}

Odicci 플랫폼을 Braze와 연결하여 원활한 데이터 공유 및 Campaign 관리를 수행할 수 있으며, 여기에는 다음이 포함됩니다:

- Odicci 경험에서 수집된 오디언스 데이터를 Braze로 자동 전송합니다.
- 사용자 상호작용을 기반으로 개인화된 마케팅 Campaign을 트리거합니다.
- Odicci와 Braze 간의 필드를 매핑하여 정확한 데이터 동기화를 보장합니다.

## 예시 {#example}

한 소매업체가 Odicci의 게이미피케이션 경험을 사용하여 마케팅 Campaign을 위한 이메일 주소를 수집합니다.

1. 고객이 Odicci에서 게임을 완료하고 이메일 주소를 제공합니다.
2. Odicci가 이 데이터를 Braze로 자동 동기화합니다.
3. Braze가 개인화된 "감사합니다" 이메일을 트리거하고 할인 코드를 포함합니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Odicci 계정 | 이 파트너십을 활용하려면 **통합** 섹션에 접근할 수 있는 Odicci 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 및 `campaigns.list` 권한이 있는 Braze REST API 키가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## Odicci 통합하기 {#integrating-odicci}

### 1단계: Odicci에서 통합 활성화 {#step-1-enable-the-integration-in-odicci}

1. Odicci 계정에 로그인합니다.
2. **Settings > Integrations** 섹션으로 이동합니다.
3. **Braze** 통합을 찾아 **Connect**를 클릭합니다.

   ![Braze 통합 연결]({% image_buster /assets/img/odicci/braze_connect.png %})

4. 제공된 필드에 Braze REST API 키를 입력합니다.
5. 설정을 저장하여 계정 수준에서 통합을 활성화합니다.

### 2단계: Braze REST API 키 가져오기 {#step-2-obtain-your-braze-rest-api-key}

1. Braze 계정에 로그인합니다.
2. **Developer Console > REST API Keys**로 이동합니다.
3. `users.track` 권한이 있는 새 API 키를 생성하거나 기존 키를 복사합니다.

### 3단계: 경험 수준에서 통합 활성화 {#step-3-activate-the-integration-at-the-experience-level}

1. Odicci Studio에서 **Experience**를 생성하거나 엽니다.
2. **Studio > Settings > Integrations**로 이동합니다.
3. **Braze** 체크박스를 찾아 선택하여 해당 경험에 대한 통합을 활성화합니다.
4. 변경 사항을 저장합니다.

### 4단계: 필드 매핑 {#step-4-map-fields}

1. 통합을 활성화한 후 **Studio > Settings > Integrations** 섹션에 머무릅니다.
2. Odicci 경험의 필드(예: `Email`, `Name`)를 Braze의 해당 필드에 매핑합니다.
3. 구성을 저장합니다.

   ![필드 매핑 구성]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### 5단계: 통합 테스트 {#step-5-test-the-integration}

1. Odicci에서 경험을 실행하여 테스트 데이터를 수집합니다.
2. Braze 대시보드 또는 데이터 로그를 확인하여 데이터가 Braze에 올바르게 동기화되는지 확인합니다.
3. 매핑된 필드가 Braze에 올바르게 채워졌는지 확인합니다.

## 문제 해결 {#troubleshooting}

통합에 문제가 발생하면 다음 해결 방법을 고려하세요. 추가 지원이 필요하면 [Odicci 고객지원](https://help.odicci.com)에 문의하세요.

### API 키가 유효하지 않음 {#api-key-not-valid}

Braze API 키를 다시 확인하고 필요한 권한이 있는지 확인하세요. 그런 다음 Odicci 통합 설정에서 API 키를 다시 입력하세요.

### 데이터가 동기화되지 않음 {#data-not-syncing}

**Field Mapping** 섹션의 필드가 올바르게 구성되어 있는지 확인하세요. 그런 다음 API 키에 사용자 데이터 가져오기 권한이 있는지 확인하세요.

### Campaign이 트리거되지 않음 {#campaign-not-triggering}

Braze Campaign 설정을 확인하여 올바른 오디언스 또는 트리거 조건이 설정되어 있는지 확인하세요.