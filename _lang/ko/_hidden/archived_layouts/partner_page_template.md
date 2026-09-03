---
nav_title: 파트너 페이지

page_order: 4

#Required
description: "Google 검색 설명입니다. 160자를 초과하는 문자는 잘리므로 간결하게 작성하세요."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks


noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [파트너 이름] {#partner-name}

> 파트너 페이지 템플릿에 오신 것을 환영합니다! 여기에서 파트너 페이지를 만드는 데 필요한 모든 것을 찾을 수 있습니다. 첫 번째 섹션에서는 첫 번째 문단에서 파트너를 한두 문장으로 설명해야 합니다. 또한 해당 파트너의 메인 사이트로 연결되는 링크를 포함하세요.

두 번째 문단에서는 Braze와 이 파트너 간의 관계를 탐색하고 설명해야 합니다. 이 문단에서는 Braze와 이 파트너가 어떻게 협력하여 Braze 사용자와 고객 간의 유대를 강화하는지 설명합니다. Braze 사용자가 이 파트너 및 해당 서비스를 통합하거나 활용할 때 발생하는 "상승 효과"에 대해 설명합니다.

## 요구 사항 또는 사전 준비 사항 {#requirements-or-prerequisites}

이 섹션에서는 파트너와의 통합 및 서비스 사용을 시작하기 위해 필요한 사항을 다룹니다. 이 정보를 전달하는 가장 좋은 방법은 통합 시 추가적인 보안 검토나 승인 절차가 필요한지 여부와 같은 기술 외적인 중요한 "알아야 할" 세부 정보를 설명하는 간단한 안내 문단을 작성하는 것입니다. 그런 다음 차트를 사용하여 통합의 기술적 요구 사항을 설명해야 합니다.

{% alert important %}
다음 요구 사항은 Braze에서 일반적으로 필요할 수 있는 항목입니다. 아래 차트에 나열된 속성 제목, Origin, 링크 및 문구를 사용하는 것을 권장합니다. 각 요구 사항이 어떤 용도로 사용되는지 파악할 수 있도록 설명을 조정해 주세요.
{% endalert %}

| 요구 사항 | Origin | 접근 방법 | 설명 |
|---|---|---|---|
| Braze 워크스페이스 REST API 키 | Braze 플랫폼 | **설정** > **API 키** 페이지 | 이 설명에는 워크스페이스 REST API 키로 수행해야 할 작업을 안내해야 합니다. |
| Braze API 엔드포인트 | Braze 플랫폼 | [엔드포인트 목록]({{site.baseurl}}/api/basics#endpoints)을 확인하거나 [지원 티켓]({{site.baseurl}}/braze_support)을 제출하세요. | 설명 보류 중. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요구 사항 또는 사전 준비 사항" }

## [통합 유형] 통합 {#type-of-integration-integration}

이 섹션에서는 통합을 단계별로 나누어 설명합니다. 끝없이 긴 문단을 작성하지 마세요. 이 문서는 마케터와 개발자 모두가 통합을 설정하고 실행하는 데 사용하는 기술 문서입니다. 이 섹션의 유일한 목표는 Braze 사용자가 작업을 완료할 수 있도록 돕는 설명적인 설명서를 작성하는 것입니다. 섹션 제목의 '통합 유형'은 병렬 통합, 서버 간 통합, 또는 기본값 통합 중 어떤 방식인지를 나타냅니다. 이를 통해 파트너와의 통합 방법이 여러 가지인 경우 여러 통합 섹션을 구성할 수 있습니다.

Currents 통합인 경우 이 페이지는 Currents 섹션에 위치해야 하며, 해당 Currents 위치로 리디렉션하는 내비게이션 페이지를 별도로 구성해야 합니다.

### 1단계: 첫 번째 단계에 대한 간단한 설명 {#step-1-this-is-a-short-description-of-step-one}

필요에 따라 코드를 포함하여 단계별로 나누어 설명합니다. 여러 가지 코드 세트를 제공할 수 있으므로 반드시 하나의 통합 방법만 제공할 필요는 없습니다.

### 2단계: 이미지 설명 단계 {#step-2-this-step-will-describe-images}

설명서에 이미지를 넣을 수 있으므로, 신중하게 이미지를 추가하는 것을 권장합니다.

### 3단계: 단계 수는 얼마나 될까요? {#step-3-how-many-steps}

통합의 사용 방법을 개괄적으로 설명합니다. 특히 메시지 작성기에 Liquid를 삽입해야 하는 경우를 포함하세요.

## 커스터마이제이션 {#customization}

이 섹션은 **선택 사항**입니다. 여기에서는 두 파트너 간의 통합을 커스터마이즈하는 구체적인 방법을 설명할 수 있습니다.

## 이 통합 사용하기 {#using-this-integration}

이 섹션에서는 통합을 사용하는 방법을 설명해야 합니다. 통합 후 버튼을 몇 번 눌러야 하는지, 아니면 별도의 작업이 필요 없는지 독자에게 알려주세요.

### 1단계: 1단계에 대한 간단한 설명

일반적인 단계별 안내입니다.

## 사용 사례 {#use-cases}

이 섹션은 설명서에서 매우 중요한 부분이 될 수 있습니다. 선택 사항이지만, 통합의 일반적이거나 새로운 사용 사례를 설명하기에 좋은 곳입니다. 이를 통해 파트너십의 가치를 알리거나 확장할 수 있으며, 맥락과 아이디어를 제공하고 무엇보다 통합의 기능을 시각적으로 보여줄 수 있습니다.