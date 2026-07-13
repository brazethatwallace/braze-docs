---
nav_title: Refiner
article_title: Refiner
alias: /partners/refiner/
description: "이 참조 문서에서는 Braze와 Refiner 간의 파트너십을 설명하며, 설문조사 이벤트와 응답 데이터를 Braze로 전송하여 캠페인을 트리거하고, 사용자를 세그먼트하고, 고객 프로필을 업데이트하는 방법을 안내합니다."
page_type: partner
search_tag: Partner

---

# Refiner

> [Refiner](https://refiner.io)는 SaaS 및 모바일 앱을 위한 인앱 설문조사 플랫폼입니다. 제품 팀과 고객의 소리(VoC) 팀이 타겟팅된 인앱 설문조사를 실행하고, 순고객추천지수(NPS), CSAT, CES, 제품 피드백, 제로파티 사용자 데이터를 지속적으로 수집할 수 있도록 지원합니다.

_이 통합은 Refiner에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Refiner와 Braze 통합을 사용하면 Refiner에서 설문조사 이벤트와 응답 데이터를 Braze 계정으로 전송할 수 있습니다. 이 데이터를 활용하여 설문조사 상호작용(예: 설문조사 완료)을 기반으로 Braze 캠페인을 트리거하고, 응답을 기반으로 사용자를 세그먼트하며, 설문조사 답변에서 파생된 특성으로 Braze 고객 프로필을 업데이트할 수 있습니다.

## 사용 사례 {#use-cases}

- 순고객추천지수(NPS) 점수나 CSAT 평점 등 설문조사 응답을 기반으로 사용자를 세그먼트합니다.
- 설문조사 성과를 기반으로 Braze에서 개인화된 캠페인을 트리거합니다.
- Braze Canvas 또는 기타 오케스트레이션 도구를 사용하여 크로스채널 여정을 구축합니다.

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Refiner 계정 | 이 통합을 사용하려면 [Refiner](https://refiner.io) 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스에 해당하는 Braze URL]({{site.baseurl}}/api/basics#endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: Braze 계정 연결 {#step-1-connect-your-braze-account}

Refiner 프로젝트의 **Integrations** 섹션에서 **Connect Braze**를 선택합니다. Braze REST API 키와 Braze 인스턴스 식별자를 입력합니다.

### 2단계: 사용자 식별자 매핑 {#step-2-map-user-identifiers}

Refiner 사용자 식별자를 사용 중인 Braze 식별자(예: Braze `external_id` 또는 이메일 주소)에 매핑합니다. 이렇게 하면 이벤트가 Braze에서 올바른 사용자와 연결됩니다.

### 3단계: 동기화할 데이터 선택 {#step-3-choose-data-to-sync}

- Braze로 동기화할 설문조사 데이터를 선택합니다.
- **Survey Seen**, **Survey Dismissed**, **Survey Completed** 등 Braze로 전송할 Refiner 이벤트를 선택합니다.

![설문조사 선택 및 이벤트 매핑 옵션을 보여주는 Refiner 통합 설정 패널.]({% image_buster /assets/img/refiner.jpg %})

## Refiner 커스터마이즈 {#customize-refiner}

- Braze로 전송되는 데이터에 설문조사 응답만 포함할지, 추가 연락처 데이터 필드도 포함할지 선택합니다.
- 동기화된 데이터 필드에 `refiner_` 접두사를 추가하여 Braze 계정에서 쉽게 식별할 수 있도록 할지 선택합니다.

## Braze에서 설문조사 데이터 활용 {#use-survey-data-in-braze}

Braze와 Refiner를 연결하면 **Saw Survey** 또는 **Completed Survey** 같은 설문조사 이벤트가 Braze 계정의 고객 프로필에 표시됩니다. 이러한 이벤트를 사용하여 Braze에서 메시지를 트리거하고 개인화하거나, 설문조사 응답 데이터를 사용하여 사용자를 세그먼트할 수 있습니다.

{% alert note %}
Braze를 통해 이메일로 Refiner 설문조사를 전송할 수도 있습니다. 자세한 내용은 [Refiner 통합 설명서](https://refiner.io/docs/kb/integrations/braze-integration/)를 참조하세요.
{% endalert %}

## 문제 해결 {#troubleshooting}

통합에 문제가 발생하면 다음 리소스를 참조하세요.

- [Refiner와 Braze 통합 가이드](https://refiner.io/docs/kb/integrations/braze-integration/)
- [Refiner 지원팀 문의](https://refiner.io/docs/kb/getting-started/contact-support/)