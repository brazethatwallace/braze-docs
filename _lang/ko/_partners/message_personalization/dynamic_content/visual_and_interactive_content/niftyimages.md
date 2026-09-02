---
nav_title: NiftyImages
article_title: NiftyImages
description: "NiftyImages를 Braze에 연결하여 개인화된 동적 비주얼을 생성하고, 연락처 속성을 동기화하며, 자산을 재사용 가능한 Content Blocks로 게시하는 방법을 알아보세요."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com)는 Braze 고객이 이메일, 모바일 및 인앱 메시징을 위한 개인화된 실시간 비주얼 콘텐츠를 생성할 수 있도록 도와줍니다. 라이브 고객, 제품 및 비즈니스 데이터를 동적 이미지와 콘텐츠에 연결하여, 브랜드는 카운트다운 타이머, 개인화된 추천, 현지화된 메시징, 재고 업데이트, 프로모션 오퍼 등 참여와 전환을 유도하는 시의적절하고 관련성 높은 경험을 제공할 수 있습니다.

_이 통합은 NiftyImages에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze용 NiftyImages 통합을 사용하면 Braze 연락처 데이터를 활용하여 개인화된 동적 비주얼을 생성할 수 있습니다. 팀은 개인화된 이미지, 카운트다운 타이머, 지도, 캘린더, 로열티 비주얼 등의 자산을 구축한 다음, 이를 재사용 가능한 Braze [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)로 게시하여 Campaigns와 Canvases 전반에서 사용할 수 있습니다. 이를 통해 시간을 절약하고, 오류를 줄이며, 개인화된 콘텐츠 관리를 간소화할 수 있습니다.

## 활용 사례 {#use-cases}

NiftyImages를 사용하여 다음을 수행할 수 있습니다.

- **이미지 개인화:** 각 고객의 이름, 로열티 상태, 리워드 잔액, 위치, 제품 선호도, 멤버십 등급, 계정 세부 정보 또는 기타 Braze 연락처 속성을 포함하는 이미지를 생성합니다.
- **카운트다운 타이머 추가:** 세일, 제품 출시, 이벤트, 한정 오퍼, 예약, 온보딩 마감일 및 개인화된 만료일에 대한 실시간 카운트다운 타이머를 추가합니다.
- **동적 지도 표시:** 고객 위치 데이터 또는 Braze 연락처 속성을 기반으로 가장 가까운 매장, 이벤트 장소, 서비스 지역, 딜러, 클럽, 지점 또는 픽업 위치를 표시합니다.
- **캘린더 표시:** 개인화된 날짜, 이벤트, 예약, 갱신 기간, 캠페인 시점 또는 고객 마일스톤을 캠페인 비주얼 내에 직접 표시합니다.
- **실시간 투표 실행:** 캠페인에 인터랙티브 투표를 추가하고 고객이 투표한 후 실시간으로 업데이트되는 결과를 표시합니다.
- **스크래치 오프 생성:** 개인화된 리워드, 할인, 오퍼, 이미지 또는 메시지를 공개하는 게이미피케이션 스크래치 오프 경험을 생성합니다.
- **로열티 데이터 시각화:** 고객 데이터를 각 수신자에게 개인화된 진행 바, 계정 요약, 로열티 비주얼, 차트 및 그래프로 변환합니다.
- **규칙 기반 콘텐츠 적용:** 시간, 위치, 기기, 고객 데이터, 오디언스 세그먼트 또는 캠페인 로직에 따라 다른 비주얼을 표시합니다.
- **동적 콘텐츠 재사용:** 완성된 NiftyImages 자산을 Braze Content Blocks에 게시하여 팀이 마케팅 이메일, 템플릿, Campaigns 및 공유 브랜드 자산 전반에서 재사용할 수 있습니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음 사항을 확인하세요.

| 요구 사항 | 설명 |
| ------------ | ----------- |
| NiftyImages 계정 | 개인화된 이미지, 타이머, 지도, 캘린더, 스크래치 오프, 차트 및 기타 동적 비주얼을 생성하고 관리하려면 [NiftyImages 계정](https://niftyimages.com/Signup)이 필요합니다. |
| Braze 계정 | Braze Campaigns, Canvases, 이메일 템플릿 및 메시징 채널 내에서 NiftyImages를 사용하려면 Braze 계정이 필요합니다. |
| Braze REST API 키 | `custom_attributes.get` 및 `content_blocks.create` 권한이 있는 Braze REST API 키.<br><br>이 키는 Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Braze 계정을 NiftyImages에 연결하여 연락처 속성을 동기화하고 자산을 Braze Content Blocks에 게시합니다.

### 1단계: NiftyImages에서 통합 열기 {#step-1-open-integrations-in-niftyimages}

1. NiftyImages에서 **Settings** > **Integrations**로 이동합니다.
2. **Braze**를 선택합니다.
3. **Connect Braze**를 선택합니다.

### 2단계: Braze REST API 키 생성 {#step-2-create-your-braze-rest-api-key}

1. Braze에서 **설정** > **API 키**로 이동합니다.
2. NiftyImages 통합을 위한 REST API 키를 생성하거나 선택합니다.
3. **커스텀 속성**에서 `custom_attributes.get`을 선택합니다.
4. **Content Blocks**에서 `content_blocks.create`를 선택합니다.
5. API 키를 저장한 다음, REST API 키와 [REST 엔드포인트]({{site.baseurl}}/api/basics#endpoints)를 복사합니다.

### 3단계: NiftyImages에서 Braze 계정 연결 {#step-3-connect-your-braze-account-in-niftyimages}

1. NiftyImages의 Braze 통합 화면으로 돌아갑니다.
2. Braze REST API 키를 붙여넣습니다.
3. Braze REST 엔드포인트를 입력합니다.
4. 연결을 확인합니다.
5. **Connected Braze accounts** 아래에 Braze 계정이 **Active** 또는 **Connected** 상태로 표시되는지 확인합니다.

필요한 경우 여러 Braze 계정을 연결할 수 있으며, 이는 에이전시, 멀티 브랜드 팀 또는 여러 Braze 인스턴스를 관리하는 조직에 유용합니다.

## NiftyImages에서 자산 커스터마이즈 {#customize-assets-in-niftyimages}

Braze를 연결한 후, 연락처 변수 동기화 및 Content Block 게시를 사용하여 개인화된 비주얼을 관리합니다.

### 연락처 변수 동기화 사용 {#use-contact-variable-sync}

연락처 변수 동기화를 사용하면 머지 태그를 수동으로 입력하거나 다시 생성하지 않고도 기존 Braze 연락처 속성을 NiftyImages 내에서 직접 사용할 수 있습니다.

1. 개인화된 이미지 또는 기타 NiftyImages 자산을 생성하거나 편집합니다.
2. 머지 태그 또는 개인화 선택기를 엽니다.
3. **Pick from connected integrations**를 선택한 다음, 사용하려는 Braze 속성을 선택합니다.
4. 해당 값을 텍스트, 이미지, 타이머, 지도, 차트, 캘린더 또는 동적 콘텐츠 레이어에 추가합니다.
5. 이미지를 저장합니다.

Braze 변수를 사용하는 저장된 이미지는 NiftyImages 이미지 URL에 해당 개인화 값을 자동으로 포함합니다.

### Braze Content Blocks에 게시 {#publish-to-braze-content-blocks}

1. NiftyImages 자산을 완성합니다.
2. **Send to Braze**를 선택합니다.

## Braze에서 NiftyImages 사용 {#use-niftyimages-in-braze}

게시된 Content Blocks를 Braze 이메일 템플릿, Campaigns 및 Canvases에서 사용합니다.

### Braze 이메일에 NiftyImages 자산 추가 {#add-a-niftyimages-asset-to-a-braze-email}

1. Braze에서 이메일 템플릿, Campaign 또는 Canvas 이메일 메시지를 엽니다.
2. 메시지 편집기에서 개인화 메뉴를 열고 개인화 유형으로 **Content Blocks**를 선택합니다.
3. NiftyImages에서 게시한 NiftyImages Content Block을 선택합니다.

### Braze 전반에서 NiftyImages 자산 재사용 {#reuse-niftyimages-assets-across-braze}

1. 게시된 Content Block을 마케팅 이메일, 이메일 템플릿, Campaigns, 공유 브랜드 자산 및 자동화 플로우 전반에서 사용합니다.
2. NiftyImages 자산이 동적 변수를 사용하는 경우, Braze는 메시지와 채널에 따라 연락처 값을 전달합니다.
3. 크리에이티브 변경이 필요한 경우 NiftyImages에서 소스 자산을 업데이트합니다.

### Braze 계정 연결 해제 {#disconnect-a-braze-account}

1. NiftyImages에서 **Settings** > **Integrations**로 돌아갑니다.
2. Braze 연결 페이지를 엽니다.
3. 제거하려는 계정의 제거 또는 연결 해제 아이콘을 선택합니다.
4. 연결 해제를 확인합니다.

## 고려 사항 {#considerations}

- **REST API 권한:** Braze REST API 키에는 연락처 속성 동기화를 위한 `custom_attributes.get`과 Braze Content Blocks에 자산을 게시하기 위한 `content_blocks.create`가 포함되어야 합니다.
- **연락처 속성 가용성:** 연결된 Braze 계정에서 사용 가능한 연락처 속성만 NiftyImages에 동기화할 수 있습니다.
- **대체 값:** 개인화된 비주얼을 구축할 때 대체 값을 사용하여 연락처 속성이 누락된 경우에도 모든 고객이 완성된 이미지를 볼 수 있도록 합니다.
- **재사용 가능한 Content Blocks:** Braze Content Blocks에 게시하면 팀이 수동 HTML 복사 및 붙여넣기를 피하고, 머지 태그 오류를 줄이며, Campaigns와 템플릿 전반에서 자산을 재사용할 수 있습니다.
- **다중 Braze 계정:** NiftyImages는 여러 연결된 Braze 계정을 지원하며, 이는 에이전시, 멀티 브랜드 팀 및 여러 Braze 인스턴스를 관리하는 팀에 유용합니다.
- **테스트:** Campaign 또는 Canvas를 시작하기 전에 샘플 고객 프로필로 최종 Braze 메시지를 테스트하세요.

## 문제 해결 {#troubleshooting}

NiftyImages 통합에 문제가 발생하면 다음 표를 참조하세요.

| 문제 | 해결 방법 |
| ----- | ---------- |
| Braze 계정이 연결되지 않음 | REST API 키가 유효한지, REST 엔드포인트가 올바른지, 키에 필수 권한이 포함되어 있는지 확인합니다. |
| Braze 연락처 속성이 NiftyImages에 표시되지 않음 | API 키에 `custom_attributes.get`이 포함되어 있는지 확인합니다. 그런 다음 NiftyImages 내에서 Braze 연결을 새로고침합니다. |
| 자산이 Braze Content Blocks에 게시되지 않음 | API 키에 `content_blocks.create`가 포함되어 있는지, 연결된 Braze 계정에서 Content Block 생성이 허용되는지 확인합니다. |
| 개인화가 올바르게 표시되지 않음 | 선택한 Braze 연락처 속성에 테스트 사용자에 대한 값이 포함되어 있는지 확인합니다. 필요한 경우 NiftyImages에서 대체 값을 추가합니다. |
| 이미지가 Braze에서 렌더링되지 않음 | NiftyImages 자산이 저장되었고, 활성 상태이며, 올바르게 게시되었는지 확인합니다. Braze 테스트 메시지를 보내 의도한 채널에서 이미지를 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }