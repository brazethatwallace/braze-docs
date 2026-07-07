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

## 요구 사항 또는 필수 조건 {#requirements-or-prerequisites}

이 섹션은 파트너와 통합하고 서비스를 사용하기 시작하는 데 필요한 모든 것에 관한 것입니다. 이 정보를 전달하는 가장 좋은 방법은 통합이 추가 보안 검사나 승인을 받아야 하는지 여부와 같은 비기술적 중요 세부 사항을 설명하는 간단한 안내 문단을 작성하는 것입니다. 그런 다음 차트를 사용하여 통합의 기술적 요구 사항을 설명해야 합니다.

{% alert important %}
다음 요구 사항은 Braze에서 일반적으로 필요한 요구 사항입니다. 다음 차트에 나열된 속성 제목, 출처, 링크 및 문구를 사용하는 것을 권장합니다. 각 요구 사항이 어떤 용도로 사용되는지 알 수 있도록 설명을 조정하세요.
{% endalert %}

| 요구 사항 | 출처 | 액세스 | 설명 |
|---|---|---|---|
| Braze 워크스페이스 REST API 키 | Braze 플랫폼 | **Settings** > **API Key** 페이지 | 이 설명은 워크스페이스 REST API 키를 어떻게 사용해야 하는지 알려줍니다. |
| Braze API 엔드포인트 | Braze 플랫폼 | [나열된 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)를 확인하거나 [고객지원 티켓]({{site.baseurl}}/braze_support/)을 개설하세요. | 설명 보류 중입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## [통합 유형] 통합 {#type-of-integration-integration}

여기에서 통합을 단계별로 세분화합니다. 마케터와 개발자 모두가 통합을 시작하고 실행하는 데 사용할 기술 문서이므로 끝없는 문단을 작성하지 마세요. 이 섹션의 유일한 목표는 Braze 사용자가 작업을 완료하는 데 도움이 되는 설명서를 작성하는 것입니다. 섹션 제목의 '통합 유형'은 이것이 병렬 통합인지, 서버 간 통합인지, 기본 통합인지를 나타내기 위한 것입니다. 이 파트너와 통합할 수 있는 방법이 두 가지 이상인 경우 여러 개의 통합 섹션을 사용할 수 있습니다.

이것이 커런츠 통합인 경우, 이 페이지는 Currents 섹션에 위치해야 하며, 해당 위치로 리디렉션하는 내비게이션 페이지를 구축해야 합니다.

### 1단계: 1단계에 대한 간략한 설명 {#step-1-this-is-a-short-description-of-step-one}

필요에 따라 코드를 포함하여 세분화하면 됩니다. 여러 가지 코드 세트를 제공할 수 있으므로 한 가지 통합 방법만 제공할 필요는 없습니다.

### 2단계: 이 단계에서는 이미지에 대해 설명합니다 {#step-2-this-step-will-describe-images}

설명서에 이미지를 넣을 수 있는 옵션이 있으므로 신중하게 넣는 것을 권장합니다.

### 3단계: 몇 단계가 필요한지 {#step-3-how-many-steps}

특히 메시지 작성기에 Liquid를 삽입하는 경우 통합 사용법을 간략하게 설명합니다.

## 커스터마이징 {#customization}

이 섹션은 **선택 사항**입니다. 여기에서 두 파트너 간의 통합을 커스터마이징하는 구체적인 방법을 설명할 수 있습니다.

## 이 통합 사용하기 {#using-this-integration}

여기에는 통합 사용 방법이 설명되어 있어야 합니다. 통합 후 몇 개의 버튼을 눌러야 하는지, 아니면 아무것도 할 필요가 없는지 독자에게 알려주세요.

### 1단계: 1단계에 대한 간략한 설명

일반적인 단계별 안내입니다.

## 활용 사례 {#use-cases}

이는 설명서에서 중요한 부분이 될 수 있습니다. 선택 사항이지만 통합의 일반적이거나 새로운 활용 사례를 설명하기에 좋은 곳입니다. 이를 통해 관계를 판매하거나 업셀하는 방법으로 활용할 수 있으며, 맥락과 아이디어를 제공하고 가장 중요하게는 통합의 기능을 시각화할 수 있는 방법을 제시합니다.