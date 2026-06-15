---
nav_title: Peak
article_title: Peak
description: "이 참조 문서에서는 의사결정 인텔리전스 플랫폼인 Peak과 Braze 간의 파트너십을 설명합니다. 이 파트너십을 통해 고객 행동 및 상호작용을 기반으로 예측된 고객이탈 확률과 속성을 가져와 Braze로 임포트한 후 고객 세분화 및 타겟팅에 활용할 수 있습니다."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://peak.ai/)은 의사결정 인텔리전스 플랫폼으로, 의사결정 인텔리전스가 비즈니스 의사결정을 향상시키고 매출과 수익을 성장시키기 위한 AI의 상업적 적용인 엔드투아웃컴 시스템입니다.

_이 통합은 Peak에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Peak 간의 파트너십을 통해 고객 행동 및 상호작용을 기반으로 예측된 고객이탈 확률과 속성을 가져와 Braze로 임포트한 후 고객 세분화 및 타겟팅에 활용할 수 있습니다.

## 필수 조건 {#prerequisites}

시작점으로, Peak 테넌트가 Peak과 Braze 간의 통합을 호스팅해야 합니다. 이는 일반적으로 Peak 고객의 온보딩 과정에서 생성됩니다. 또한 의사결정 인텔리전스 솔루션이 먼저 필요합니다. 이 솔루션이 이후 Braze에 통합될 AI 기반 출력을 생성하기 때문입니다.

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Peak 테넌트 | 테넌트라고 하는 Peak 플랫폼의 인스턴스가 통합을 호스팅하고 오케스트레이션하는 데 필요합니다. |
| 의사결정 인텔리전스 솔루션 | Peak과 Braze 간의 통합은 AI 기반 출력을 기반으로 하므로 테넌트 내에 Peak 또는 고객이 배포한 솔루션이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br>이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

Peak 솔루션 고객 인텔리전스는 모델을 활용하여 고객 행동 및 상호작용을 기반으로 다양한 미래 지향적 속성을 예측합니다. 이러한 속성은 Peak 내에 저장되며, 고객의 고객이탈 확률을 포함한 예측 세분화를 생성하는 데 사용할 수 있습니다. 이러한 예측 속성의 업데이트는 설정 가능한 주기(일별 또는 주별)를 기반으로 합니다.

### 1단계: 모델 실행 및 고객 추출 {#step-1-run-model-and-extract-customers}

통합은 AI 모델 실행과 예측 고객 속성의 재계산을 기반으로 트리거됩니다. 이러한 AI 출력은 속성이 새로운 상태 또는 값으로 업데이트된 시점을 포함하여 Peak 내에 저장됩니다.

속성이 업데이트된 시점을 기반으로, Peak과 Braze 간의 마지막 동기화 이후 업데이트된 예측 속성을 가진 모든 고객을 수집하기 위한 선택이 수행됩니다.

### 2단계: Braze 업데이트 {#step-2-update-braze}

업데이트된 고객 및 관련 속성을 사용하여 Peak은 [벌크]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates) 헤더를 활용하여 [`/user/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 통해 Braze에 POST합니다.

API에서 성공 상태 코드를 수신하면 Peak은 Peak과 Braze 간의 성공적인 동기화를 기록합니다.

### 3단계: 이 통합 사용하기 {#step-3-using-this-integration}

Peak과 Braze 간의 동기화가 성공하면 업데이트된 사용자에 새로운 속성이 포함됩니다. 이러한 속성을 Campaigns 및 Canvases에서 사용하여 사용자를 타겟팅하고 메시지를 개인화하세요.